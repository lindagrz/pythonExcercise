# Database is here: https://prosemind.com/mod/resource/view.php?id=88
#
# ER diagram is here: https://prosemind.com/mod/page/view.php?id=89

import sqlite3


def create_connection(dbpath):
    # can add verbose parameter that prints sqlite version used
    print("sqlite3 version:", sqlite3.version)
    conn = sqlite3.connect(dbpath)
    return conn


def create_artist(conn, artist_name):
    # do not have to return anything but can use try: inside this function
    cur = conn.cursor()
    cur.execute('INSERT INTO artist (Name) VALUES (?)', artist_name)
    conn.commit()


def read_artists(conn):  # can add some extra parameters to limit
    conn.execute('SELECT * FROM artist')
    artists = conn.fetchall()
    return artists  # can return a list of tuples, or you can create a list of artist objects if you want

# def update_artist(id, new_name):
#
# def delete_artist(id=None, name=""):

   # provide deletion by id AND/OR name


def main():
    con = create_connection("chinook.db")
    # create_artist(con, 'Linda')
    print(read_artists(con))

    con.commit()
    con.close()


if __name__ == "__main__":
    main()
