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
After run build_db.py
![obraz](https://github.com/kaczmprz/invoices/assets/111633053/78ff8592-c64f-42f2-92b7-90ff083870af)

2. Customers view (Materials and Companies view are similar)
List view:
![obraz](https://github.com/kaczmprz/invoices/assets/111633053/095061e1-72a9-44ac-a996-67bf206dbdcf)
Detail view:
![obraz](https://github.com/kaczmprz/invoices/assets/111633053/090d5677-1a0a-4279-a9c8-547c602dbbdf)
Edit view:
![obraz](https://github.com/kaczmprz/invoices/assets/111633053/968a4a2b-85e9-4923-910f-d854ccb9c09c)
Delete view:
![obraz](https://github.com/kaczmprz/invoices/assets/111633053/36939fd1-72ad-4b91-aa4c-c995944c5b65)

3. Invoices view
Create new invoice:
![obraz](https://github.com/kaczmprz/invoices/assets/111633053/97e7cd3a-0c71-41bc-b8a9-5656f611ef76)
Detail view:
![obraz](https://github.com/kaczmprz/invoices/assets/111633053/7873a1a1-a840-4bdb-b473-a268614b8d2d)
Get pdf view:
![obraz](https://github.com/kaczmprz/invoices/assets/111633053/f435be89-066c-4881-bf0c-c34f74ad418c)

4. REST API
Simple output to list data
Invoices:
![obraz](https://github.com/kaczmprz/invoices/assets/111633053/58934f45-f3ea-4f73-aeec-744de3edd1b2)

Customers:
![obraz](https://github.com/kaczmprz/invoices/assets/111633053/546d7899-ef02-4c90-a818-0798e790ab0e)


