-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

\c tournament
-- Order is very important here, because of dependencies.
-- Get the order wrong and you will get an error.
DROP VIEW IF EXISTS player_standings;
DROP VIEW IF EXISTS matches_by_player;
DROP VIEW IF EXISTS wins_by_player;

DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS players;


CREATE TABLE players (
  id SERIAL PRIMARY KEY,
  name TEXT
);


CREATE TABLE matches (
  id SERIAL,
  winner INTEGER REFERENCES players(id),
  loser INTEGER REFERENCES players(id)
);


CREATE VIEW matches_by_player AS
  SELECT p.id, p.name, count(m.id) as matches
  FROM players as p
  LEFT JOIN matches as m ON p.id = m.winner or p.id = m.loser
  GROUP BY p.id;


CREATE VIEW wins_by_player AS
  SELECT p.id, p.name, count(m.winner) as wins
  FROM players as p
  LEFT JOIN matches as m ON m.winner = p.id 
  GROUP BY p.id;
 
CREATE VIEW player_standings AS
  SELECT w.id, w.name, w.wins, m.matches 
  FROM wins_by_player as w
  JOIN matches_by_player as m on w.id = m.id
  ORDER BY wins;

