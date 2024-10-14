# Kartify_E-commerce-Website
This project uses Django for backend and React for frontend
To start the project, follow the steps:

Activate the environment by navigating to /Scripts and
run >activate
Back in the parent directory, install the required libraries using requirements.txt (first-time only)
>pip install -r requirements.txt
Navigate to /kartify/kartify and open settings.py and into the database section make changes according to your database
Navigate to /kartify and run make models migration into your database using manage.py
>python manage.py makemigrations 
Now run the django server >python manage.py runserver
With the Django server running, in another terminal, start react server

Navigate to /kartify_react folder to install the required modules (first-time only)
>npm install 
Now start the react server
>npm start
