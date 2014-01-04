# PizzaHackers

Website for PizzaHackers - the __doer__ community of [NIT Jamshedpur](http://nitjsr.ac.in).

## Colophon

PizzaHackers runs on the following technologies.

### Backend

- [Python](http://python.org)

- [Google App Engine](http://developer.google.com/appengine)

- [Flask](http://flask.pocoo.org)

### Frontend

- [HTML5](http://html5rocks.org)

- [LESS](http://lesscss.org)

- [Twitter Bootstrap](http://getbootstrap.com)

- [AngularJS](http://angularjs.org)

## Development Ennviroment

### Backend

1. Download [Google App Engine](http://developer.google.com/appengine/downloads) for your operating system.

	- If you are running Linux, download the SDK and unzip it to `/usr/local`. Your SDK's path will then look like, `/usr/local/google_appengine`, and it will be available on `$PATH`.

	- Add aliases for common GAE executables to your `~/.bashrc` file.

	```
	$ echo "alias devappserver='/usr/local/google_appengine/dev_appserver.py'" >> ~/.bashrc
	$ echo "alias appcfg='/usr/local/google_appengine/appcfg.py'" >> ~/.bashrc
	$ source ~/.bashrc
	```
	
	- If you are running Mac / Windows, you can use Google App Engine Launcher.

2. Move to the project directory, `pizzahackers-web`. Create a `virtualenv`, and then execute:
```
$ pip install -r requirements.txt -t server/lib
```
This will install the dependencies in your `virtualenv`.

3. Run the local GAE server.
```
$ devappserver .
```

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