# Fyle Task Backend Part
Part of Fyle Assignment.
Link to [Frontend Part](https://github.com/ashank2603/fyle-task-frontend).
The deployed API can be accessed [here](https://fyle-github.onrender.com/).

## How to run

 - Clone this repository. Open the repository in a terminal.
 - Create a virtual environment using the following command:

> virtualenv venv
- Activate the virtual environment using the following command:
> venv\scripts\activate

 - Install the required libraries using the following command:

> pip install requirements.txt

- Create a GITHUB access token to access the GitHub API.
- Create a .env file in the directory and paste the following in it and save it:

    GITHUB_API_KEY  =  "<YOUR_GITHUB_ACCESS_TOKEN>"

 - Run the following command in the terminal:
> 
> python app.py

 - The flask server will run on [PORT:5000](http://127.0.0.1:5000/)

## How to use the API

Simple run the following url in the browser:

> http://127.0.0.1:5000/api/<GITHUB_USERNAME>

For Example:
> http://127.0.0.1:5000/api/ashank2603

The above will return data with status code 200.
If the username does not exist it will return status code 404.

## How to run tests
Run the following command in the terminal:

> python -m pytest -v

