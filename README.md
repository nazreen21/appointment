Appointment CRUD API built with Django REST Framework and PostgreSQL.

Features:
- Create, retrieve, update, and delete appointments
- Versioned API (/api/v1/)
- PostgreSQL database
- Django admin support

Setup Instructions:

1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt

3. Configure PostgreSQL in .env

   DB_NAME=,
   
   DB_USER=,
   
   DB_PASSWORD=,
   
   DB_HOST=,
   
   DB_PORT=,
   
5. Run migrations:
   python manage.py makemigrations ,
   
   python manage.py migrate

7. Start the server:
   python manage.py runserver

Postman collection is included in the /postman folder for easy testing.
