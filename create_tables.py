import asyncio
from database import get_connection

async def main():
    async with get_connection() as conn:
            await conn.execute(
    """
    CREATE TABLE IF NOT EXIST users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(250) NOT NULL UNIQUE,
        password VARCHAR(200) NOT NULL,
    );
    CREATE TABLE IF NOT EXIST car(
        id SERIAL PRIMARY KEY,
        title VARCHAR(150) NOT NULL,
        description VARCHAR(250) ,
        price INT,
        created_at DATE DEFAULT CURRENT DATE,
        user_id INT REFERENCES user(id) ON DELETE CASCADE
    );
    """
            )
            print('OK 200')

asyncio.run(main())