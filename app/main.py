from fastapi import FastAPI

from app.database.db_setup import Base, engine
from app.routers import dishes, menus, submenus

app = FastAPI(
    title='ASYNC Menu App'
)

app.include_router(menus.router, prefix='/api/v1', tags=['Menus'])
app.include_router(submenus.router, prefix='/api/v1/menus/{menu_id}', tags=['Submenus'])
app.include_router(dishes.router, prefix='/api/v1/menus/{menu_id}/submenus/{submenu_id}', tags=['Dishes'])


@app.on_event('startup')
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
