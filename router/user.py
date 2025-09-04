from fastapi import APIRouter,Depends,HTTPException,Request,Form,Response
from schemas import UserBase,UserDisplay
from database.database import get_db
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,RedirectResponse
from sqlalchemy.orm import Session
from database.database_user import *
from auth.oauth2 import oauth2_scheme, get_current_user
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm
from auth import auth
router = APIRouter(
    prefix='/user',
    tags=['user']
)
templates= Jinja2Templates(directory='template')


@router.get('/home', response_class=HTMLResponse)
async def user_home(request: Request):
    username = request.query_params.get("username")
    return templates.TemplateResponse("landing.html", {"request": request, "username": username})

@router.post('/login', response_class=HTMLResponse)
async def login(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    username = form.get('username')
    password = form.get('password')
    user = db.query(UserData).filter(UserData.username == username).first()
    if not user or not Hash.verify(user.password, password):
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})
    access_token = auth.oauth2.create_access_token(data={"sub": user.username})
    response = RedirectResponse(url=f"/user/home?username={user.username}", status_code=302)
    response.set_cookie(key="access_token", value=access_token, httponly=True)
    return response

#create user
@router.get("/",response_class=HTMLResponse,status_code=201)
async def login_page(request:Request):
    return templates.TemplateResponse("login.html", {"request": request})
                                      
@router.post('/register', response_class=HTMLResponse)
async def create_user_data(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    name = form.get('name')
    email = form.get('email')
    password = form.get('password')
    confirm_password = form.get('confirm_password')
    if password != confirm_password:
        return templates.TemplateResponse("login.html", {"request": request, "register_error": "Passwords do not match"})
    try:
        user = UserBase(username=name, email=email, password=password)
        created_user = create_user(db, user)
    except Exception as e:
        return templates.TemplateResponse("login.html", {"request": request, "register_error": f"Not able to register the user: {str(e)}"})
    return templates.TemplateResponse("login.html", {"request": request, "register_success": "Registration successful! Please login."})

@router.get('/',response_model=list[UserDisplay])
async def get_user_route(db:Session=Depends(get_db)): 
    return get_user(db)

@router.get('/{id}',response_model=UserDisplay,status_code=201)
async def get_user_based_on_id(id :int ,db:Session=Depends(get_db),token:UserDisplay= Depends(oauth2_scheme)):
    return get_user_id(id,db)

@router.get("/logout")
async def logout(request: Request, response: Response):
    response.delete_cookie("session_token") 
    return RedirectResponse(url="/user/login")

@router.post('/update/{id}')
async def update_user_data(id:int,request:UserBase,db:Session=Depends(get_db)):
    return update_user(id,request,db)

@router.delete('/delete/{id}',status_code=200)
async def delete_user_data(id:int,db:Session=Depends(get_db)):
    if delete_user(id,db):
        return {"User id {id} data deleted successfully"}
    return HTTPException(status_code=404,detail="Delete couldn't be performed")