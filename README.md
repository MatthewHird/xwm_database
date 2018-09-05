# xwm_database

A PostgreSQL server and database must be set up before this script can be run. Additionally, a text file must be created called "server_parameters" in the main directory. This file should contain a single line in the form of:

    host=server_id dbname=database_name user=postgres_username password=postgres_password

The app also requires the psycopg2 library. This can be installed on linux using:

for python2:
    
    sudo pip install psycopg2

for python3:

    sudo pip3 install psycopg2
