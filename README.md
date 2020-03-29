Boggle Game - Python Django Backend

<div style="width:260px;max-width:100%;"><div style="height:0;padding-bottom:81.15%;position:relative;"><iframe width="260" height="211" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameBorder="0" src="https://imgflip.com/embed/3uhswr"></iframe></div><p><a href="https://imgflip.com/gif/3uhswr">via Imgflip</a></p></div>

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
