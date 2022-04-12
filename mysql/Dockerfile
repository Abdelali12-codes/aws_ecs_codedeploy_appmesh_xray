FROM mysql:latest

RUN rm -f /etc/mysql/conf.d/mysql.cnf

COPY ./mysql.cnf /etc/mysql/conf.d/

COPY ./db.sql /docker-entrypoint-initdb.d
