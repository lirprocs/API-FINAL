from httpx import AsyncClient


# проверяем, чтобы изначальный список меню был пустой
async def test_read_menus(ac: AsyncClient, start_tables):
    response = await ac.get('/api/v1/menus')
    assert response.status_code == 200
    assert response.json() == []

# проверяем добавление меню


async def test_create_menu(ac: AsyncClient):
    response = await ac.post(
        '/api/v1/menus',
        json={'title': 'Created menu', 'description': 'Created menu description'},
    )
    assert response.status_code == 201
    assert response.json() == {
        'title': 'Created menu',
        'id': '1',
        'description': 'Created menu description',
        'manual_id': None
    }

# проверяем изменение меню


async def test_update_menu(ac: AsyncClient):
    response = await ac.patch(
        '/api/v1/menus/1',
        json={'title': 'Updated menu', 'description': 'Updated menu description'},

    )
    assert response.status_code == 200
    assert response.json() == {
        'title': 'Updated menu',
        'id': 1,
        'description': 'Updated menu description',
        'dishes_count': 0,
        'submenus_count': 0,
        'manual_id': None
    }

# проверяем чтение конкретного меню


async def test_read_menu(ac: AsyncClient):
    response = await ac.get('/api/v1/menus/1')
    assert response.status_code == 200
    assert response.json() == {
        'title': 'Updated menu',
        'id': '1',
        'description': 'Updated menu description',
        'submenus_count': 0,
        'dishes_count': 0,
        'manual_id': None
    }

# проверяем добавление подменю


async def test_create_submenu(ac: AsyncClient):
    response = await ac.post(
        '/api/v1/menus/1/submenus',
        json={'title': 'Created submenu', 'description': 'Created submenu description'},
    )
    assert response.status_code == 201
    assert response.json() == {
        'title': 'Created submenu',
        'id': '1',
        'description': 'Created submenu description',
        'parent_id': '1',
        'manual_id': None
    }

# проверяем изменение подменю


async def test_update_submenu(ac: AsyncClient):
    response = await ac.patch(
        '/api/v1/menus/1/submenus/1',
        json={'title': 'Updated submenu', 'description': 'Updated submenu description'},
    )
    assert response.status_code == 200
    assert response.json() == {
        'title': 'Updated submenu',
        'id': 1,
        'description': 'Updated submenu description',
        'parent_id': 1,
        'dishes_count': 0,
        'manual_id': None
    }

# проверяем чтение конкретного подменю


async def test_read_submenu(ac: AsyncClient):
    response = await ac.get('/api/v1/menus/1/submenus/1')
    assert response.status_code == 200
    assert response.json() == {
        'title': 'Updated submenu',
        'id': 1,
        'description': 'Updated submenu description',
        'parent_id': 1,
        'dishes_count': 0,
        'manual_id': None
    }

# проверяем чтение всех подменю


async def test_read_submenus(ac: AsyncClient):
    response = await ac.get('/api/v1/menus/1/submenus')
    assert response.status_code == 200
    assert response.json() == [{
        'title': 'Updated submenu',
        'description': 'Updated submenu description',
        'id': 1,
        'parent_id': 1,
        #'manual_id': None
    }]

# проверяем количество подменю и блюд в конкретном меню


async def test_read_menu_submenus(ac: AsyncClient):
    response = await ac.get('/api/v1/menus/1')
    assert response.status_code == 200
    assert response.json() == {
        'title': 'Updated menu',
        'id': '1',
        'description': 'Updated menu description',
        'submenus_count': 1,
        'dishes_count': 0,
        'manual_id': None
    }

# проверяем добавление блюда


async def test_create_dish(ac: AsyncClient):
    response = await ac.post(
        '/api/v1/menus/1/submenus/1/dishes',
        json={'title': 'Created dish', 'description': 'Created dish description', 'price': 0.55},
    )
    assert response.status_code == 201
    assert response.json() == {
        'title': 'Created dish',
        'id': '1',
        'description': 'Created dish description',
        'price': '0.55',
        'main_menu_id': 1,
        'parent_id': '1',
        'manual_id': None
    }

# проверяем изменение блюда


async def test_update_dish(ac: AsyncClient):
    response = await ac.patch(
        '/api/v1/menus/1/submenus/1/dishes/1',
        json={'title': 'Updated dish', 'description': 'Updated dish description', 'price': 0.55},
    )
    assert response.status_code == 200
    assert response.json() == {
        'title': 'Updated dish',
        'id': 1,
        'description': 'Updated dish description',
        'price': '0.55',
        'main_menu_id': 1,
        'parent_id': 1,
        'manual_id': None
    }

# проверяем чтение конкретного блюда


async def test_read_dish(ac: AsyncClient):
    response = await ac.get('/api/v1/menus/1/submenus/1/dishes/1')
    assert response.status_code == 200
    assert response.json() == {
        'title': 'Updated dish',
        'id': '1',
        'description': 'Updated dish description',
        'price': '0.55',
        'main_menu_id': 1,
        'parent_id': 1,
        'manual_id': None
    }

# проверяем чтение всех блюд


async def test_read_dishes(ac: AsyncClient):
    response = await ac.get('/api/v1/menus/1/submenus/1/dishes')
    assert response.status_code == 200
    assert response.json() == [{
        'title': 'Updated dish',
        'description': 'Updated dish description',
        'price': 0.55,
        'id': 1,
        'parent_id': 1,
        'main_menu_id': 1,
        #'manual_id': None
    }]

# проверяем количество подменю и блюд в конкретном меню


async def test_read_menu_dishes(ac: AsyncClient):
    response = await ac.get('/api/v1/menus/1')
    assert response.status_code == 200
    assert response.json() == {
        'title': 'Updated menu',
        'id': '1',
        'description': 'Updated menu description',
        'submenus_count': 1,
        'dishes_count': 1,
        'manual_id': None
    }


async def test_read_full_menus(ac: AsyncClient):
    response = await ac.get('/api/v1/full_menus')
    assert response.status_code == 200
    data = response.json()
    menus = data.get('menus', [])
    assert len(menus) > 0  # Проверяем, что список меню не пустой

    for menu in menus:
        assert 'id' in menu
        assert 'title' in menu
        assert 'description' in menu
        submenus = menu.get('submenus', [])

        for submenu in submenus:
            assert 'id' in submenu
            assert 'title' in submenu
            assert 'description' in submenu
            dishes = submenu.get('dishes', [])

            for dish in dishes:
                assert 'id' in dish
                assert 'title' in dish
                assert 'description' in dish
                assert 'price' in dish


# проверяем удаление блюда


async def test_delete_dish(ac: AsyncClient):
    response = await ac.delete('/api/v1/menus/1/submenus/1/dishes/1')
    assert response.status_code == 200

# проверяем удаление подменю


async def test_delete_submenu(ac: AsyncClient):
    response = await ac.delete('/api/v1/menus/1/submenus/1')
    assert response.status_code == 200


# проверяем удаление меню
async def test_delete_menu(ac: AsyncClient):
    response = await ac.delete('/api/v1/menus/1')
    assert response.status_code == 200
