# Product_registration_django

## Prerequisites
```
Python 3.8 and pip module Django==4.2.11 
```

## Start the service
```
$ git clone https://github.com/RamIdavalapaati/Product_registration_django
$ cd product_registration
$ python manage.py runserver
```

## Example API to store or register product information
```
http://127.0.0.1:8000/basic/register_product?date_of_manufacture=2024-1-1&serial_number=1&product_name=ABC&manufacturer_info=ABC-info&product_desc=Not much
```

## API to list all the registered products
```
http://127.0.0.1:8000/basic/list_products
```
