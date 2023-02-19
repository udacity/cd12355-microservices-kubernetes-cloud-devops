# Check In System
## Overview
This is a simple API used to check in and validate members of a co-working space. An API endpoint exists for a user to request a one-time token that is valid for 10 minutes. Another API endpoint exists to check the validity of the token.

This is built with in Python with Flask using PostgreSQL.

## Running Locally

### Database Setup
A PostgreSQL database needs to be set up. Run the SQL scripts in `db/` to create the tables and seed them with data.

A username and password must also be set up to read and write to the tables.

You can use the tool `psql` to interface with the PostgreSQL database. This command line utility usually comes installed with PostgreSQL installations.
```bash
psql < 1_create_tables.sql
psql < 2_seed_users.sql
psql < 3_seed_tokens.sql
```

If the `psql` commands prompt for a username and password, you can run `psql` with the following flags:
```bash
PGPASSWORD <DB_PASSWORD> psql -U <DB_USERNAME> <DB_NAME> ...
```
Example:
```bash
PGPASSWORD <DB_PASSWORD> psql -U <DB_USERNAME> <DB_NAME> < 1_create_tables.sql
```

### Running the API
```python
pip install requirements.txt
python app.py
```

## Running in Docker
The Docker image already has a PostgreSQL database embedded in it.

1. Build an Image
```bash
docker build --build-arg DB_USERNAME=<DB_USERNAME> --build-arg DB_PASSWORD=<DB_PASSWORD> -t coworking-checkin .
```
Sometimes if you don't find your changes propagating, you might need to add the flag `--no-cache`.

2. Run a Container
```bash
docker run -e DB_USERNAME=<DB_USERNAME> -e DB_PASSWORD=<DB_PASSWORD> -p 5151:5151 <CONTAINER_NAME>
```

## Usage
1. Request for a Token
```bash
curl -iX POST "<BASE_URL>/api/users/<USER_ID>/tokens"
```

2. Validate a Token
```bash
curl -iX POST "<BASE_URL>/api/tokens?value=<TOKEN>&user=<USER_ID>"
```

3. Health Check
```bash
curl -i "<BASE_URL>/health_check"
```
