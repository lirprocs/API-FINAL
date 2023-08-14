import fastapi
from fastapi import BackgroundTasks, Depends

from app.schemas.dish import Dish, DishCreate
from app.services.dish_service import DishService

router = fastapi.APIRouter()


@router.get('/dishes', response_model=list[Dish])
async def get_dishes(menu_id: int, submenu_id: int,
                     response: DishService = Depends(),
                     background_tasks: BackgroundTasks = BackgroundTasks()):
    return await response.read_dishes(submenu_id=submenu_id, menu_id=menu_id)


@router.post('/dishes', status_code=201)
async def create_new_dish(menu_id: int, submenu_id: int, new_menu: DishCreate,
                          response: DishService = Depends(),
                          background_tasks: BackgroundTasks = BackgroundTasks()):
    return await response.create_dish(new_menu=new_menu, submenu_id=submenu_id, menu_id=menu_id)


@router.get('/dishes/{dish_id}')
async def get_dish(menu_id: int, submenu_id: int, dish_id: int,
                   response: DishService = Depends(),
                   background_tasks: BackgroundTasks = BackgroundTasks()):
    return await response.read_dish(dish_id=dish_id, submenu_id=submenu_id, menu_id=menu_id)


@router.patch('/dishes/{dish_id}')
async def change_dish(menu_id: int, submenu_id: int, dish_id: int, menu: DishCreate,
                      response: DishService = Depends(),
                      background_tasks: BackgroundTasks = BackgroundTasks()):
    return await response.update_dish(dish_id=dish_id, menu=menu, submenu_id=submenu_id, menu_id=menu_id)


@router.delete('/dishes/{dish_id}')
async def delete_dish(menu_id: int, submenu_id: int, dish_id: int,
                      response: DishService = Depends(),
                      background_tasks: BackgroundTasks = BackgroundTasks()):
    return await response.delete_dish(dish_id=dish_id, submenu_id=submenu_id, menu_id=menu_id)
