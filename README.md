# SafeChain Python Challenge

Here is my solution for the Python/Django challenge for my SafeChain Software Engineer application. This README explains setting up the solution and returning JSON data from the API endpoint.

<br>

### Prerequisites
You will need the following things installed on your computer

* Git
* Python 3.6.x
* Django 2.1.2
* django-tastypie 0.14.0

<br>

### Setup
Navigate to where you want to clone the repo to on your local machine and run the following command:
```
git clone https://github.com/jomofoshoyo/safechain_challenge.git
cd safechain_challenge
```

Setup your virtual environment to run the application; make sure you have python 3.6.x installed.
```
virtualenv --python=python3 venv
source venv/bin/activate
```

Install dependencies in your virtual environment. You can do this manually or simply run the dependencies shell script to install them for you.
```
./dependencies.sh
```
or
```
pip install Django
pip install django-tastypie
```

Now that you environment is setup and dependencies are installed you can start the django web server and get results at http://localhost:8000/. The included sqlite database is pre-populated with some sample data.

```
python manage.py runserver
```

<br>

### Results

The API endpoint for creating, deleting, and altering users is found at http://localhost:8000/api/users/

###### GET
Hitting this endpoint in your browser or in Postman with a GET request will return a JSON response of all the users and their associated information. Appending a number to the end of the url will return all information for that user id.

###### POST
To create a new user make a POST request from the API endpoint and pass through the desired fields for each user added.
```
{
    "email": " ",
    "first_name": " ",
    "is_staff": true/false,
    "is_superuser": true/false,
    "last_name": " ",
    "username": " "
    "groups": []
}
```

###### PUT
To update and existing user, make a PUT request for a specific user id and change to desired fields to their new values (fields to change same as above for new user creation). E.g. make a PUT request to the endpoint:  `http://localhost:8000/api/users/4/`

###### DELETE
To delete a user, simply make a DELETE request to the endpoint for the user id that you'd like to delete.
