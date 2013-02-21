my-python-webapp
================

Just for learning purposes...

Dependencies:
-------------
(tested under Ubuntu 12.10)

web.py Framework

```bash
sudo easy_install web.py
```

psycopg2 PostgreSQL driver for python:

```bash
sudo apt-get install python-psycopg2
```

Install PostgreSQL and PostGIS

```bash
sudo apt-get install postgresql postgresql-9.1-postgis
```
Set up the database with PostGIS functions:

```bash
psql -U postgres -c "create database test_webapp;"
psql -U postgres -d osm -f /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql
psql -U postgres -d osm -f /usr/share/postgresql/9.1/contrib/postgis-1.5/spatial_ref_sys.sql
```

Create Table:

TODO !
