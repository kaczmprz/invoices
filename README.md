# Description

This project is a simple app to manage create and manage settlements with various vendors.
On the frontend you can create customers, companies, materialas and invoices.
On the backend you can you simple rest api to list above objects. 


## Prerequisities

1. Python 3.8.0
2. Create virtualenv and clone this repository
    ```
    python -m venv myenv
    cd myenv
    git clone https://github.com/kaczmprz/invoices.git
    ```
3. Activate virtualenv
    ```
    source bin/activate
    ```
4. Install libraries from requirements.txt
    ```
    pip install -r requirements.txt
    ```
5. Prepare database
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
6. Create superuser 
    ```
    python manage.py createsuperuser
    ```
7. Generate random data and load to database
    ```
    python build_db.py
    ```
8. If you would like to clean database run
    ```
    python manage.py flush
    ```
9. Runserver
    ```
    python manage.py runserver
    ```
   
## Screenshots
1. Home view
![obraz](https://github.com/kaczmprz/invoices/assets/111633053/d92abfc8-9f65-4ab5-bf95-c9213c1931f4)

2. Customers view (Materials and Companies view are similar)

3. Invoices view

4. REST API

