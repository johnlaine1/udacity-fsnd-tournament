#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    
    cmd = "DELETE FROM matches;"
    db = connect()
    c = db.cursor()
    c.execute(cmd)
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""

    cmd = "DELETE FROM players;"
    db = connect()
    c = db.cursor()
    c.execute(cmd)
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""

    cmd = "SELECT count(*) as num FROM players;"
    db = connect()
    c = db.cursor()
    c.execute(cmd)
    player_count = c.fetchone()
    db.close()
    
    return player_count[0]

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    Args:
      name: the player's full name (need not be unique).
    """
    
    cmd = "INSERT INTO players (name) VALUES (%s);"
    db = connect()
    c = db.cursor()
    c.execute(cmd, (name,))
    db.commit()
    db.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    
    cmd = "SELECT * FROM player_standings;"
    db = connect()
    c = db.cursor()
    c.execute(cmd)
    player_standings = c.fetchall()
    db.close()
    
    return player_standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
 
    cmd = "INSERT INTO matches(winner, loser) VALUES(%s, %s)"
    db = connect()
    c = db.cursor()
    c.execute(cmd, (winner, loser))
    db.commit()
    db.close()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    cmd = "SELECT id, name FROM player_standings;"
    db = connect()
    c = db.cursor()
    c.execute(cmd)
    rows = c.fetchall()
    db.close()

    standings = []
    total_rows = len(rows)
    count = 0
    while count < total_rows:
      standings.append(
        (
          rows[count][0], 
          rows[count][1], 
          rows[count+1][0], 
          rows[count+1][1]
        )
      )
      count += 2
    
    return standings
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    