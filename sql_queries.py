# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL PRIMARY KEY,
    start_time TIMESTAMP,
    user_id INTEGER,
    level VARCHAR,
    song_id VARCHAR,
    artist_id VARCHAR,
    session_id INTEGER,
    location VARCHAR,
    user_agent VARCHAR
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS
    users(user_id INTEGER PRIMARY KEY, first_name varchar,
    last_name varchar, gender char, level varchar)""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs
    (song_id varchar PRIMARY KEY, title varchar, artist_id varchar NOT NULL,
    year integer, duration decimal) """)

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists
    (artist_id varchar PRIMARY KEY,
    name VARCHAR, location VARCHAR, latitude FLOAT,
    longitude FLOAT)""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time
    (start_time TIMESTAMP PRIMARY KEY,
    hour INTEGER NOT NULL, day INTEGER NOT NULL, week INTEGER NOT NULL, month INTEGER NOT NULL,
    year INTEGER NOT NULL,weekday INTEGER NOT NULL)""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (songplay_id, start_time, user_id, level,
    song_id, artist_id, session_id, location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT(songplay_id) DO NOTHING;
    """)

user_table_insert = ("""
INSERT INTO users(user_id,
    first_name,last_name,gender,level)
    VALUES (%s,%s,%s,%s,%s) ON CONFLICT (user_id) DO NOTHING""")

song_table_insert = ("""
INSERT INTO songs(song_id,title,
    artist_id,year,duration)
    VALUES (%s,%s,%s,%s,%s)
    ON CONFLICT (song_id) DO NOTHING""")

artist_table_insert = ("""
INSERT INTO artists(artist_id,name,
    location,latitude,longitude)
    VALUES (%s,%s,%s,%s,%s)
    ON CONFLICT (artist_id) DO NOTHING""")

time_table_insert = ("""
INSERT INTO time(start_time, hour, day,
    week, month, year,weekday)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT (start_time) DO NOTHING""")

# FIND SONGS

song_select = ("""
    SELECT s.song_id, a.artist_id
            FROM songs AS s
            LEFT JOIN artists AS a
                ON a.artist_id = s.artist_id
            WHERE   s.title = (%s) AND \
                    a.name = (%s)  AND \
                    s.duration = (%s);
""")
# QUERY LISTS

create_table_queries = [
                        songplay_table_create, user_table_create,
                        song_table_create, artist_table_create,
                        time_table_create]
drop_table_queries = [
                        songplay_table_drop, user_table_drop, song_table_drop,
                        artist_table_drop, time_table_drop]
