FROM python:3.11.3

WORKDIR /opt/spiderweb/app
COPY . .
RUN apt-get update && apt-get install -y sassc
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r ./requirements.txt
RUN make setup compile cleansass

ENV pg_username = root
ENV pg_password = root
ENV pg_host = localhost
ENV pg_database = spiderweb
ENV session_key = changeme
ENV session_lifetime = 2880

CMD [ "./boot.sh" ]
