FROM postgres:15.2-bullseye

ARG DB_PASSWORD=$DB_PASSWORD
ARG DB_USERNAME=$DB_USERNAME

ENV POSTGRES_PASSWORD $DB_PASSWORD
ENV POSTGRES_USER $DB_USERNAME
ENV POSTGRES_DB postgres

# Container will run scripts in the directory
# See: https://hub.docker.com/_/postgres - "Initialization Scripts"
COPY ./*.sql /docker-entrypoint-initdb.d/
