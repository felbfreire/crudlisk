crudlisk id a using Flask, Flask-SQLAlchemy and Flask-Migrate. It has a minimal frontend for 
sending requests and interact with SQLite database. for now, you can register, login/logout.

Author: Felipe Freire - felbfreire
repo: https://github.com/felbfreire/crudlisk.git


-- Installing dependencies --

-> create a virtual enviroment:
```bash
$ python -m venv venv

$ source venv/bin/activate
```

-> upgrade pip and install dependencies

```bash
pip install --upgrade pip

pip install -r requirements.txt
```

-- Using Crudlisk --

-> set enviroment variable and run

```bash
$ export FLASK_APP=crudlisk/app

$ flask run
```

-> routes

	home -> localhost:5000
	register -> localhost:5000/register
	login -> localhost:5000/login
	login -> localhost:5000/logoff
	unsign -> localhost:5000/unsign
