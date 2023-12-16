# Storage

В базе хранится содержимое склада магазина   
 
Написать View который вернет для API 127.0.0.1/api/v1/storage/    
JSON с объемом товаров на складе (в куб метрах) и список товаров с флагом is_active    

## Запуск проекта

1. **Шаг 1:** Клонировать репозиторий:

```
    git clone https://github.com/Ydtalel/storage.git
```

2. **Шаг 2:** Установить зависимости:

    ```
    pip install -r requirements.txt
    ```

3. **Шаг 3:** Запустить проект:

    ```
    python manage.py runserver
    ```

4. **Шаг 4:** Перейти по адресу:

    Откройте в браузере `http://127.0.0.1:8000/api/v1/storage/` для доступа к проекту.

## Дополнительная информация

[Ссылка на Docker Hub](https://hub.docker.com/repository/docker/ydtalel/storage/general)

