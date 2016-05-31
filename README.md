 - Set up env with
 ```
    pip install -r requirements.txt
 ```

 - Add next environment variables
 ```
 DB_NAME
 DB_USER
 DB_PASS
 DB_HOST
 DB_PORT
 ```

 - Create database

 - Run migrations

 ```
 ./manage.py migrate
 ```

 - Create superuser
 ```
 ./manage.py createsuperuser
 ```

 - Load fixtures
 ```
 ./manage.py loaddata product/fixtures/product.json
 ```

 - Start from /products/ page
