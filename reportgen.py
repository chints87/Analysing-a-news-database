#!/usr/bin/env python3

import psycopg2
import sys


def main():
    """Text generated to report most read articles; top read authors
    and the day for which the request error was more than 1% """

    # Makes connection to the news database
    conn = psycopg2.connect(database="news", user="vagrant",
                            password="vagrant", host="localhost")
    cursor = conn.cursor()

    mostarticles(conn, cursor)
    mostreadauthor(conn, cursor)
    mosterror(conn, cursor)

    # The connection to the news database is closed.
    conn.close()


def mostarticles(conn, cursor):
    """List three most read articles from the news database"""

    # Queries are executed from the tables and views in the news database
    cursor.execute(
        """SELECT * from mostview;""")

    # Result is a python list
    results = cursor.fetchall()

    # Text is generated as output from the print statement of total views of
    # of top three most read articles
    print ("\nWhat are the most popular three articles of all time?\n")

    for articleid, title, views in results:
        print ('\"{}\" - {}'.format(title, views))


def mostreadauthor(conn, cursor):
    """List authors from highest to lowest readership from the news database"""

    # Queries are executed from the tables and views in the news database
    cursor.execute(
        """SELECT authors.name, SUM(mostread.views) as readership
           FROM authors, mostread
           WHERE authors.id = mostread.author
           GROUP BY mostread.author, authors.name
           ORDER BY readership DESC;""")

    # Result is a python list
    results = cursor.fetchall()

    # Text is generated as output from the print statement of most read author
    # from the results list.
    print ("\nWhat are the most read article authors of all time?\n")

    for author, views in results:
        print("{} - {} views".format(author, views))


def mosterror(conn, cursor):
    """List day with request errors more than 1% from the news database"""

    cursor.execute(
           """SELECT requestbad.date,
           ROUND(requestbad.type * 100.0 / totalhits.hits, 3) as percent
           FROM requestbad, totalhits
           WHERE requestbad.date = totalhits.date
           AND ROUND(requestbad.type * 100.0 / totalhits.hits, 3) > 1.0;""")

    # Result is a python list
    results = cursor.fetchall()

    # Text is generated as output from the print statement for the day with
    # the highest bad request as percentage of total requests.

    for date, percentage in results:
        print("\nOn which days did more than 1 percent requests lead ",
              "\nto errors?\n")
        print('{0:%d, %B %Y} : {1:.2f}% errors'.format(date, percentage))


if __name__ == "__main__":
    main()
