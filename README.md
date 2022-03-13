## Installation and Use
    - Install Python, Pipenv, Postgres on your machine
    - Clone the repository
    - Change the directory to the cloned repository
    - Create a virtual environment using `pipenv --three`
    - Activate the virtual environment `pip shell` command
    - Install all dependencies with command `pipenv install`
    - Add environmental variables to your machine
        ```
        export FLASK_ENV=development
        export DATABASE_URL=postgresql://blogadmin:blogpass@localhost:5432/blogapi
        ```

    - Create database blogapi
        If using linux:
        ```
        sudo -u postgres psql
        create database blogapi;
        create user blogadmin with encrypted password 'blogpass';
        grant all privileges on database blogapi to blogadmin;
        ```
    - Run commands 
        `flask db init`
        `flask db migrate`
        `flask db upgrade`
    - Start app with `python run.py`


    TO use the app,  use a tool for example `POSTMAN` or anything similar than sends different crud operations.

    Example using POSTMAN
        - To create a category go to http://127.0.0.1:5000/categories/
        - Now fill the 'Body' of Postman with JSON and json appropriate info.
    
    Functions

    Category
        - http://127.0.0.1:5000/categories/ - POST REQUEST - to create a category, add a appropriate new name in json format in the body
        example:
        {
            name": "Testing"
        }
        - http://127.0.0.1:5000/categories/all - GET REQUEST - to get all categories
        - http://127.0.0.1:5000/categories/find/<category_id> - GET REQUEST - get category and its blogposts of id
        - http://127.0.0.1:5000/categories/update/<category_id> - PUT REQUEST - add a appropriate new name in json format in the body
        example: 
        {
            "name": "NewCategory"
        }

    Blog Posts
        - http://127.0.0.1:5000/blogposts/create/<category_id> - POST REQUEST - add appropriate json
        example:
        {
            "title": "Java testing",
            "contents": "Who is jason?"
        }
        - http://127.0.0.1:5000/blogposts/addcategory/<blog_id>/<category_id> - PUT REQUEST
        - http://127.0.0.1:5000/blogposts/remcategory/<blog_id>/<category_id> - PUT REQUEST
        -http://127.0.0.1:5000/blogposts/update/<blog_id> - PUT REQUEST - add json
        example:
        {
            "title": "Java testing",
            "contents": "What is JSON?"
        }
        - http://127.0.0.1:5000/blogposts/delete/<blog_id> - DELETE REQUEST
        - http://127.0.0.1:5000/blogposts/find/<blog_id> - GET REQUEST