# Fitness
This is a full-stack Django project, which includes both a back-end server and a front-end client. The back-end server provides RESTful APIs to the front-end client, and the front-end client is built with React.

## Installation
To install and run this project, follow these steps:

Clone the repository to your local machine.
Install Python 3.8 or higher and Node.js on your machine if they are not already installed.
Create a virtual environment and activate it:
bash
Copy code
```
python3 -m venv venv
source venv/bin/activate
```
Install the Python dependencies:
Copy code
```
pip install -r requirements.txt
```
Install the Node.js dependencies:
Copy code
```
npm install
```
Set up the database:
Copy code
```
python manage.py migrate
```
Run the development server:
Copy code
```
python manage.py runserver
```
and in a separate terminal window, run:
sql
Copy code
```
npm start
```
Open your web browser and navigate to http://localhost:3000 to see the application.
## Configuration
The project uses environment variables for configuration. You can set these variables in a file named .env in the project root directory. An example .env file is provided in the project.

The following environment variables are used:

**SECRET_KEY**: Django secret key. This should be a long, random string and should be kept secret.
**DEBUG**: Whether or not to run the application in debug mode. Set to True in development, False in production.
**DATABASE_URL**: URL for the database. By default, the project is configured to use a SQLite database, but you can change this to use a different database if you prefer.
CORS_ORIGIN_WHITELIST: Comma-separated list of origins that are allowed to access the API. This is used to configure Cross-Origin Resource Sharing (CORS).
**ALLOWED_HOSTS**: Comma-separated list of hostnames that the application is allowed to run on. This is used for security purposes.
## Usage
The application is a simple to-do list application. You can create an account, log in, and create, edit, and delete tasks.

## Development
To run the tests, run:

bash
Copy code
```
python manage.py test
```
To build the React client for production, run:

arduino
Copy code
```
npm run build
```
## Deployment
To deploy the application to production, you can follow these steps:

Set the **SECRET_KEY**, DEBUG, **DATABASE_URL**, **CORS_ORIGIN_WHITELIST**, and **ALLOWED_HOSTS** environment variables appropriately.
Run **python manage.py** collectstatic to collect the static files.
Run **npm run build** to build the React client.
Use your preferred method to deploy the Django application and the React client. A common method is to use a platform like Heroku or AWS Elastic Beanstalk.
