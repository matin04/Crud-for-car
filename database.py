import asyncpg
from contextlib import asynccontextmanager
import os

DB_CONFIG = {
    "host" : "localhost",
    "port" : 5432,
    "database" : "Crud_car_for_fastapi",
    "user":"postgres",
    "password" : "55055904855"
}

@asynccontextmanager
async def get_connection():
    conn = await asyncpg.connect(**DB_CONFIG)
    try:
        yield conn
    finally:
        await conn.close()