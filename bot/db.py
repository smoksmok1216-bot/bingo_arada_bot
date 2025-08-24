import asyncpg
from bot.config import DATABASE_URL

async def connect_db():
    return await asyncpg.create_pool(DATABASE_URL)

async def create_users_table(conn):
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            telegram_id BIGINT UNIQUE,
            balance INTEGER DEFAULT 10
        );
    """)

async def register_user(conn, telegram_id):
    user = await conn.fetchrow("SELECT * FROM users WHERE telegram_id = $1", telegram_id)
    if not user:
        await conn.execute("INSERT INTO users (telegram_id, balance) VALUES ($1, $2)", telegram_id, 10)

async def get_balance(conn, telegram_id):
    user = await conn.fetchrow("SELECT balance FROM users WHERE telegram_id = $1", telegram_id)
    return user['balance'] if user else 0
