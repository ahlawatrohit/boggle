Boggle Game - Python Django Backend

Setup

1. Create virtual environment for python where the project dependencies will be installed
### `python -m venv venv`
Activate the newly created virtual environment
### `source venv/bin/activate`

2. Install the project dependencies from requirements.txt

### `pip install -r requirements.txt`

3. Next we need to install the NLTK words which will be our english dictionary for the game.

Goto python shell and execute the following commands:
### `python`
### `import nltk`
### `nltk.download('words')`

4. Run the server with the following command

### `python manage.py runserver`

This will run the app in the development mode.<br />
Open [http://localhost:8000](http://localhost:8000) to view it in the browser.

Please run the boggle-ui from this repository https://github.com/ahlawatrohit/boggle-ui

TestCases:
There are test cases with the project and that can be executed with the following command:
### `python manage.py test`
