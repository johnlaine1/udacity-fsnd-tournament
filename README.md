# Tournament Results

#### Created by: John Laine

## Description
In this project I have created a PostgreSQL database schema to store swiss style tournament game matches between players.
I then created a Python module to rank the players and pair them up in matches in the tournament.

This project was created and submitted to Udacity as part of the Full Stack Developer Nanodegree program.

## Running the Application
1. You must first have a PostgreSQL database installed and running locally. You can find more info [here](https://wiki.postgresql.org/wiki/Detailed_installation_guides)
2. You will also need python and psycopg2 installed.
2. Clone this repo `git clone https://github.com/johnlaine1/udacity-fsnd-tournament.git`
3. cd into the directory `cd udacity-fsnd-tournament'
4. Start the psql terminal by typing `psql`
5. Load the database schema `\i tournament.sql`
6. Open another terminal window and navigate to the udacity-fsnd-tournament directory.
7. Run the tests with `python tournament_test.py`. This will check that the tournament.py module is written correctly.