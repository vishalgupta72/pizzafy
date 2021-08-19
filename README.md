# Pizzafy

1. Firstly system should have python3 installed.
2. Then run the command 
    "pip install -r requirement.txt"

    to install all requirements to run this project

3. Run command
    "python manage.py runserver"

    then django will serve the API to the link
        i. API home
            http://127.0.0.1:8000/
        ii. Pizza details
            http://127.0.0.1:8000/pizzas/

Normal user or unauthenticated person can only view the data

To add and update data user should be superuser/admin

    Admin/root credential
        username: root
        password: root

    Login link
        http://127.0.0.1:8000/admin/