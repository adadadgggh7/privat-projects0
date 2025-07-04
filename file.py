import sqlite3
from sqlite3 import Error
import os
import sys

# # Creating a connection to our database
# os.makedirs(os.path.join(os.getcwd(), 'database_new'))
database = os.path.join(os.getcwd(), "database_new/film_1.db")
print(database)
try:
    conn = sqlite3.connect(database)
except Error as e:
    print(e)
    sys.exit()
# # # # #
# # # # # # Creating a cursor to execute commands (queries)
curs = conn.cursor()
# # Create a table with name projects which has rows: id , name , begin_date, end_date
user_table_create = """ CREATE TABLE IF NOT EXISTS Users (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        username text NOT NULL UNIQUE,
                                        email text UNIQUE,
                                        password text,
                                        created_at datetime
                                    ); """
# #
# # # # # # # # # executing the query
curs.execute(user_table_create)
# # # we should commit the changes
conn.commit()


# # Filling the projects table with values
# # query:
insert_query = """INSERT INTO Users (username, email, password, created_at)
                    VALUES
                    ('Jack', 'jack@yopmail.com', 'test123321', '2021-09-01'),
                    ('Jane', 'jane@yopmail.com', 'test123321', '2021-10-01')
                    ;

                """

curs.execute(insert_query)
conn.commit()

# # # Updating the date of created row
update_query = """UPDATE Users
                    SET created_at = "2020-01-01"
                    WHERE id = 2 and email = "jack@yopmail.com"
                """

curs.execute(update_query)
conn.commit()

# # better way not to use conn.commit every time

update_query = """UPDATE Users
                    SET created_at = '2019-12-02'
                    WHERE id = 3
                """
with conn:
    curs.execute(update_query)

username = input("username: ")
password = input("password: ")
# # #
# # #
# # # # # Grabbing data from database
curs.execute("""SELECT email
                FROM {}
                WHERE username='{}' and password='{}'""".format("Users", username, password))

result = curs.fetchone()
if result:
    print("Logged in successfully", result)
else:
    raise Exception("Authentication failed!!!")

curs.execute("""SELECT email, id, created_at
                FROM Users
                ORDER BY ID desc
                """)

# # Fetch the values
result = curs.fetchall()
result_1 = curs.fetchone()
result_2 = curs.fetchmany(10)
print(result)
print(result_1)
print(result_2)
print(type(result))
print(result[0])
for i in result[0]:
    print(F"type of {i} is {type(i)}")

from pprint import pprint


select = """select *
            from Users
            where username like "%a"
            """

result = curs.execute(select)
pprint(result.fetchall())
database = os.path.join(os.getcwd(), "database_new/film_data.db")
print(database)
try:
    conn = sqlite3.connect(database)
except Error as e:
    print(e)
    sys.exit()
# #
# # # Creating a cursor to execute commands (queries)
curs = conn.cursor()
#
#
# # lets create a new film for film table
class Film:
    def __init__(self, film_id, title, description, release_year: str, rate, length: int, special_features):
        self.film_id = film_id
        self.title = title
        self.description = description
        self.release_year = release_year
        self.rate = rate
        self.length = length
        self.special_features = special_features

        self.conn = None
        self.curs = None

    def connect(self):
        database = os.path.join(os.getcwd(), 'database_new', "film_data.db")
        print(database)
        try:
            conn = sqlite3.connect(database)
        except Error as e:
            print(e)
            sys.exit()
        self.conn = conn
        self.curs = conn.cursor()

    def get_atr_as_tuple(self):
        return (
                self.film_id, self.title, self.description, self.release_year,
                self.rate, self.length, self.special_features
        )

    def get_atr_as_dict(self):
        return {
            'film_id': self.film_id,
            'title': self.title,
            'description': self.description,
            'release_year': self.release_year,
            'rate': self.rate,
            'length': self.length,
            'special_features': self.special_features
        }

    def __create_film_table(self):
        if not self.conn:
            self.connect()

        film_table_create = """ CREATE TABLE IF NOT EXISTS US_films (
                                                id integer PRIMARY KEY AUTOINCREMENT,
                                                film_id integer,
                                                title text,
                                                description text,
                                                release_year text,
                                                rate integer,
                                                length integer,
                                                special_features text
                                            ); """

        with self.conn:
            self.curs.execute(film_table_create)

    def insert_function_film(self):
        self._create_film_table()

        insert_query = """INSERT INTO US_films(film_id, title, description, release_year, rate, length, special_features)
                            VALUES(?,?,?,?,?,?,?);
                            """
        if not self.conn:
            self.connect()

        self.curs.execute(insert_query, self.get_atr_as_tuple())
        self.conn.commit()

    def remove_from_table_by_id(self):
        if not self.conn:
            self.connect()

        remove_query = """delete from US_films
                            where film_id = {}""".format(self.film_id)

        self.curs.execute(remove_query)
        self.conn.commit()

    def __repr__(self):
        return self.title


desc = """In_a post-apocalyptic wasteland, Max, a drifter and survivor, unwillingly joins Imperator Furiosa,
        a rebel warrior, in a quest to overthrow a tyrant who controls the lands water supply."""

film_1 = Film(501, 'Mad_Max', desc, '2015', 120, 5, 'Action')
film_2 = Film(601, 'Avangers', 'marvel movie', '2015', 5, 120, 'Action')
film_3 = Film(701, 'Avangers 2', 'marvel movie', '2015', 5, 120, 'Action')
film_4 = Film(701, 'Avangers 3', 'marvel movie', '2015', 5, 120, 'Action')
film_1.insert_function_film()
film_2.insert_function_film()
film_4.insert_function_film()
film_4.remove_from_table_by_id()


#
#
# # #
# # #
# # #
# #
# #
#
database = os.path.join(os.getcwd(), "database/film_data.db")
# print(database)
try:
    conn = sqlite3.connect(database)
except Error as e:
    print(e)
    sys.exit()
# #
# # # # Creating a cursor to execute commands (queries)
curs = conn.cursor()

def insert_function_film_2(value: dict):
    insert_query = """INSERT INTO US_films(film_id, title, description, release_year, rate, length, special_features)
        VALUES(:film_id,:title,:description,:release_year,:rate,:length,:special_features);
        """
    curs.execute(insert_query, value)
    conn.commit()


film_3 = Film(701, 'Avangers 2', 'marvel movie', '2015', 5, 120, 'Action')
film_3._create_film_table()

insert_function_film_2(film_3.get_atr_as_dict())
# # #
# # # class Users:
# # #     def __init__(self, db_name):
# # #         self.db_name = db_name
# # #         self.conn = None
# # #
# # #     def connect_(self):
# # #         try:
# # #             self.conn = sqlite3.connect(database)
# # #             self.curs = conn.cursor()
# # #         except Error as e:
# # #             print(e)
# # #             sys.exit()
# # #
# # #     def add_user(self):
# # #         if not self.conn:
# # #             try:
# # #                 self.connect_()
# # #             except:
# # #                 pass
# # #
# # #         query = """insert into Users"""
# # #         self.curs.execute(query)
