default :: compile

.ONESHELL:
help ::
	echo .
	echo .
	echo --- SpiderWeb ---
	echo help - shows this list
	echo install - runs setup, compile and cleansass
	echo run - compiles css and runs the web server using gunicorn
	echo setup - installs js libs and bootstrap
	echo docker - builds the docker image and runs it
	echo compile - runs all compile targets
	echo migrate - migrates the database
	echo bootstrap - downloads bootstrap source
	echo jslibs - donwloads all used javascript libraries
	echo clean - removes all downloaded js and css libraries
	echo cleansass - removes bootstrap source code
	echo cleanlibs - removes downloaded js libraries
	echo cleancss - removes all compiled css files
	echo buildimg - builds the docker image
	echo runimg - runs the docker image
	echo guni - runs the gunicorn server
	echo css - compiles sass files into css

install :: setup compile cleansass

run :: compile guni

setup :: bootstrap jslibs

docker :: buildimg runimg

compile :: css

clean :: cleansass cleancss cleanlibs

cleansass ::
	rm -frd ./static/sass/bootstrap/

cleanlibs ::
	rm ./static/js/popper.min.js
	rm ./static/js/bootstrap.min.js

cleancss ::
	rm -frd ./static/css/*.css

.ONESHELL:
migrate ::
	cd ..
	flask db init
	flask db migrate
	flask db upgrade

bootstrap ::
	wget https://github.com/twbs/bootstrap/archive/refs/tags/v5.3.0.zip
	unzip ./v5.3.0.zip
	rm ./v5.3.0.zip
	mv ./bootstrap-5.3.0/scss/ ./static/sass/bootstrap/
	rm -frd ./bootstrap-5.3.0/

jslibs ::
	wget https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js
	wget https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js
	mv ./bootstrap.min.js ./static/js/
	mv ./popper.min.js ./static/js/

buildimg ::
	docker build . -t classweb:latest

runimg ::
	docker run -it --rm -p 8080:8000 -e pg_host=db classweb:latest

guni ::
	cd ..
	gunicorn app:app -b 0.0.0.0

css ::
	sassc static/sass/main.scss static/css/main.css
