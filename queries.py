from database import get_connection
from fastapi import HTTPException
import asyncpg


async def create_user(username:str, email:str, password:str):
    async with get_connection() as conn:
        try:
            user_id = await conn.fetchval(
                "INSERT INTO users(username, email, password) VALUES($1, $2, $3) RETURNING id"
            , username, email, password)
            return user_id
        except asyncpg.UniqueViolationError:
            raise HTTPException(
                status_code=400, detail="Bad request"
            )
        
    

async def get_user():
    async with get_connection() as conn:
        rows = await conn.fetch("SELECT * FROM users")
        return [dict(row) for row in rows]



async def get_user_by_id(id:int):
    async with get_connection() as conn:
        res = await conn.fetchrow("SELECT * FROM users WHERE id = $1", id)
        if res:
            return dict(res)
        return ("Does not exist")


async def update_user(id:int, username:str, email:str, password:str):
    async with get_connection() as conn:
        try:
            res = await conn.fetchrow(
                "UPDATE users SET username = $1, email = $2, password = $3 WHERE id = $4 RETURNING id, username, email, password"
            , username, email, password, id)
            if not res:
                raise HTTPException(status_code=404, detail="User not found")
            return dict(res)
        except asyncpg.UniqueViolationError:
            raise HTTPException(
                status_code=400, detail="Bad request in update user"
            )


async def delete_user(id:int):
    async with get_connection() as conn:
        res = await conn.execute("DELETE FROM users WHERE id = $1", id)
        if not res:
                raise HTTPException(status_code=404, detail="User not found")
        return {"message":"User Successfully deleted."}



async def create_car(title:str, description:str, model:str, price:int, user_id:int):
    async with get_connection() as conn:
        try:
            car_id = await conn.fetchval(
                "INSERT INTO car(title, description, model, price, user_id) VALUES($1, $2, $3, $4, $5) RETURNING id"
            , title,description,model, price, user_id)
            return car_id
        except asyncpg.UniqueViolationError:
            raise HTTPException(
                status_code=400, detail="Bad create request"
            )


async def get_car():
    async with get_connection() as conn:
        rows = await conn.fetch("SELECT * FROM car")
        return [dict(row) for row in rows]



async def get_car_by_id(id:int):
    async with get_connection() as conn:
        res = await conn.fetchrow("SELECT * FROM car WHERE id = $1", id)
        if res:
            return dict(res)
        return ("Does not exist")


async def update_car(id:int, title:str, description:str, model:str, price:int, user_id:int):
    async with get_connection() as conn:
        try:
            res = await conn.fetchrow(
                "UPDATE car SET title = $1, description = $2, model = $3, price = $4, user_id = $5 WHERE id = $6 RETURNING *"
            , title, description, model, price, user_id, id)
            if not res:
                raise HTTPException(status_code=404, detail="Car not found")
            return dict(res)
        except asyncpg.UniqueViolationError:
            raise HTTPException(
                status_code=400, detail="Bad request"
            )


async def delete_car(id:int):
    async with get_connection() as conn:
        res = await conn.execute("DELETE FROM car WHERE id = $1", id)
        if not res:
                raise HTTPException(status_code=404, detail="Car not found")
        return {"message":" Car Successfully deleted."}

