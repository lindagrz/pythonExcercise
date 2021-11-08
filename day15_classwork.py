# TO DO: the following 5 functions for CRUD(create, read,update,delete) operations that work with sqlite database called chinook.db
#
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
    cur.execute('INSERT INTO artists (Name) VALUES (?)', (artist_name,))
    conn.commit()


def read_artists(conn):  # can add some extra parameters to limit
    cur = conn.cursor()
    cur.execute('SELECT * FROM artists limit 10')
    artists = cur.fetchall()
    return artists  # can return a list of tuples, or you can create a list of artist objects if you want


def update_artist(conn, id, new_name):
    cur = conn.cursor()
    cur.execute('UPDATE artists SET name = (?) WHERE artistid = (?)', (new_name, id, ))
    conn.commit()


def delete_artist(conn, id=None, name=""):
    cur = conn.cursor()

    if name == "" and not id is None:
        cur.execute('DELETE FROM artists WHERE artistid = (?)', (id, ))
    elif not name == "" and id is None:
        cur.execute('DELETE FROM artists WHERE name = (?)', (name, ))
    elif not name == "" and not id is None:
        cur.execute('DELETE FROM artists WHERE artistid = (?) and name = (?)', (id, name,))
    conn.commit()


def main():
    con = create_connection('chinook.db')
    create_artist(con, 'Rammstein')
    print(read_artists(con))
    update_artist(con, 3, 'Something else')
    print(read_artists(con))
    delete_artist(con, name='Something else')
    print(read_artists(con))

    con.close()


if __name__ == "__main__":
    main()
