from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from queries import *


app = FastAPI(title="CRUD for users and cars", description="API for CRUD", version="1.0.0")

class UserCreate(BaseModel):
    username:str
    email:str
    password:str


class UserResponse(BaseModel):
    id:int
    username:str
    email:str
    password:str
    

@app.get("/user/{user_id}", response_model=dict, summary="Your id")
async def get_user_endpoint(user_id:int):
    user = await get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Not Found")
    return user



app.post("/create_user/", response_model=UserResponse, summary="Create new user")
async def create_user_endpoint(user:UserCreate):
    user_id = await create_user(user.username, user.email, user.password    )
    return UserResponse(id = user_id, username= user.username, email = user.email, password=user.password)


@app.get("/list_user/", response_model=list[dict], summary="All Users")
async def list_users_endpoint():
    user = await get_user()
    return user


@app.put("/user/{user_id}", response_model=UserResponse, summary="update user")
async def update_user_endpoint(user_id:int, user:UserCreate):
    updated = await update_user(user_id, user.username, user.email, user.password)
    if not updated:
        return HTTPException(status_code=404, detail="user not found")
    return {"message":"user updated"}

@app.delete("/user/{user_id}", summary="delete user")
async def deleted_user_endpoint(user_id:int):
    deleted = await delete_user(user_id)
    if not deleted:
        return HTTPException(status_code=404, detail="USER NOT FOND")
    return {"message":"user deleted"}




class CarCreate(BaseModel):
    title:str
    description:str
    model:str
    price:str
    user_id:int


class CarResponse(BaseModel):
    id:int
    title:str
    description:str
    model:str
    price:str
    user_id:int



@app.get("/get_car_id/{car_id}", response_model=dict, summary="Your id for car")
async def get_car_endpoint(car_id:int):
    car = await get_car_by_id(car_id)
    if not car:
        raise HTTPException(status_code=404, detail="Not Found")
    return car


app.post("/create_car/", response_model=UserResponse, summary="Create new car")
async def create_car_endpoint(car:CarCreate):
    car_id = await create_car(car.title,  car.description, car.model, car.price, car.user_id)
    return CarResponse(id=car_id, title=car.title, description=car.description, price=car.price, user_id=car.user_id)


@app.get("/list_car/", response_model=list[dict], summary="All Users")
async def list_car_endpoint():
    books = await get_car()
    return books



@app.put("/car_update/{car_id}", response_model=CarResponse, summary="update car")
async def update_car_endpoint(car_id:int, car:CarCreate):
    updated = await update_car(car_id, car.title, car.description, car.model, car.price, car.user_id)
    if not updated:
        return HTTPException(status_code=404, detail="car not found")
    return {"message":"car updated"}

@app.delete("/deleted_car/{book_id}", summary="delete car")
async def deleted_car_endpoint(car_id:int):
    deleted = await delete_car(car_id)
    if not deleted:
        return HTTPException(status_code=404, detail="CAR NOT FOND")
    return {"message":"Car deleted"}