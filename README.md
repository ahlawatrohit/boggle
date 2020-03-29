Boggle Game - Python Django Backend

Setup

Install python 3.6 or greater to run this project.

1. Create virtual environment for python where the project dependencies will be installed
### `python -m venv venv`
Activate the newly created virtual environment
### `source venv/bin/activate`

2. Install the project dependencies from requirements.txt present in boggle project folder.

### `pip install -r requirements.txt`

3. Next we need to install the NLTK library words which will be our core english dictionary for the game.
This is a very important step. Please do not skip this step.

Goto python shell and execute the following commands:
### `python`
### `import nltk`
### `nltk.download('words')`

4. Run the server with the following command from boggle project folder.

### `python manage.py runserver`

This will run the app in the development mode.<br />
Open [http://localhost:8000](http://localhost:8000) to view it in the browser.

Please run the boggle-ui from this repository https://github.com/ahlawatrohit/boggle-ui

TestCases:
To run the project tests, execute the following command from boggle project folder:
### `python manage.py test`
