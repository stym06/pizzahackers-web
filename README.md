# PizzaHackers

Website for PizzaHackers - the __doer__ community of [NIT Jamshedpur](http://nitjsr.ac.in).

## Colophon

PizzaHackers runs on the following technologies.

### Backend

- [Python](http://python.org)

- [Django](https://www.djangoproject.com)

### Frontend

- [HTML5](http://html5rocks.org)

- [LESS](http://lesscss.org)

- [Twitter Bootstrap](http://getbootstrap.com)

- [AngularJS](http://angularjs.org)

## Development Ennviroment

### Backend

1. Clone the repository to your workspace.
```
git clone https://github.com/PizzaHackers/pizzahackers-web.git
```

2. Install `virtualenvwrapper` as described [here](http://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation).

3. Create a new virtualenv.
```
mkvirtualenv pizzahackers-web
```

4. Install the required dependencies in your virtualenv.
```
cd pizzahackers-web
pip install -r requirements.txt
```

3. Run the local Django server.
```
python manage.py runserver
```
You app should now be live at `http://localhost:8000`

4. Start hacking!

### Frontend

The project uses LESS for styling. The LESS files are then compiled into CSS using `lessc`.

1. Install `nodejs` on your machine. Google it.

2. Install `lessc`.
```
$ npm -g install lessc
```

3. Install `pywatch`.
```
$ pip install pywatch
```

4. Move into the project directory, `pizzahackers-web`. Now, run a worker that'll watch all LESS files for changes, and compile them to CSS automatically.
```
$ pywatch -v "lessc static/less/app.less static/css/app.css" static/less/*.less static/less/bootstrap/*.less
```

5. Start hacking!
