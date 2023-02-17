# django_api_ToDoList
Django projects using Django rest framework. created a ToDoList CRUD operations using API


Python Version:
  This Django application requires Python 3.6 or later versions to be installed on your system.

Steps to Run the Django Application:
  
  1> Clone the repository or download the project files to your local machine.
  2> Open a terminal window and navigate to the project directory.
  3> Create a new virtual environment and activate it:


bash
      python3 -m venv env
      source env/bin/activate   # For Linux or macOS
      env\Scripts\activate     # For Windows
    
    
Install the required packages from the requirements.txt file:

bash
    pip install -r requirements.txt
      
      
Apply the database migrations:

bash
    python manage.py migrate


Create a superuser for accessing the Django admin panel:
bash
    python manage.py createsuperuser



Start the development server:
bash
    python manage.py runserver
    Open a web browser and go to http://127.0.0.1:8000 to access the Django application.



To access the admin panel, go to http://127.0.0.1:8000/admin and login with the superuser credentials.

That's it! You can now use the Django application and make changes to the code as per your requirements.



how to access CRUD operations in this project

    CREAT a ToDoList  : http://127.0.0.1:8000/api/create/
    
    READ a ToDoList   : http://127.0.0.1:8000/api/
    
    UPDATE a ToDoList : http://127.0.0.1:8000/api/3/
          note :- 3 no is nothing but id number of your TODO
          
    DELETE a ToDoList : http://127.0.0.1:8000/api/delete/3/



