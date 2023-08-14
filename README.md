## Запуск проекта
### Инструкция
1. Клонируйте репозиторий
2. Перейдите в директорию проекта и выполните:
```bash
docker-compose -f docker-compose-test.yaml up
```
3. После вывода результатов тестов остановите выполнение (CTR + C для PyCharm)
4. В дерриктории проекта выполните:
```bash
docker-compose down --rmi all --volumes --remove-orphans
```
**Примечание:** Оба варианта используют одни и те же порты, поэтому при запуске одного из них, другой должен быть остановлен.

5. В дерриктории проекта выполните:
```bash
docker-compose up
```
Файл Menu.xlsx находится в папке /app/admin , при внесении изменений в файл все изменения отображаются в БД. Периодичность обновления 15 секунд.
Результат изменений можно увидеть перейдя по адресу http://localhost:8000/docs и выполнив конечную точку /api/v1/full_menus

### Дополнение
* Реализовал тестовый сценарий «Проверка кол-ва блюд и подменю в меню» из Postman с помощью pytest -
сценарий использовался в тестах: tests/test_one.py
* Добавил эндпоинт (GET) для вывода всех меню со всеми связанными подменю и со всеми связанными блюдами. - repositories/menus (get_full_menus)
* Добавил тест эндпоинта (GET) для вывода всех меню со всеми связанными подменю и со всеми связанными блюдами tests/test_one.py
* Папка /app/admin является наружней и в ней можно вносить изменения в файл Menu.xlsx, при внесении изменений в файл все изменения отображаются в БД
* 
