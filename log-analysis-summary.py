#!/usr/bin/env python

import psycopg2

# Connect to an existing database

try:
    conn = psycopg2.connect("dbname=news")
except psycopg2.Error as e:
    print("Unable to connect!")
    print(e.pgerror)
    print(e.diag.message_detail)
    sys.exit(1)
else:
    print "Connected!"

# Open a cursor to perform database operations

cur = conn.cursor()

# Creating a View for views by log.path

cur.execute("CREATE VIEW articles_views_count AS \
SELECT path, count(*) AS views \
FROM log \
GROUP BY log.path \
ORDER BY views DESC;")

# Retrieving the 3 most accessed articles of all times

cur.execute("SELECT articles.title, SUM(articles_views_count.views) \
AS views \
FROM articles_views_count \
JOIN articles \
ON articles_views_count.path = '/article/' || articles.slug \
GROUP BY articles.title \
ORDER BY views DESC \
LIMIT 3;")

query_1 = cur.fetchall()

# Retrieving the most popular authors by 
# the total number of views of each author articles

cur.execute("SELECT authors.name, SUM(views) AS views \
FROM articles \
JOIN articles_views_count \
    ON articles_views_count.path = '/article/' || articles.slug \
JOIN authors \
    ON authors.id = articles.author \
GROUP BY authors.name \
ORDER BY views DESC;")

query_2 = cur.fetchall()

# Days errors were throwed more than 1% of the total requests

cur.execute("SELECT err.date AS date, ROUND(100.0 * err.nerr / total.req, 2) \
	AS percentage \
FROM (SELECT date(time) AS date, count(*) AS nerr \
    FROM log \
    WHERE status != '200 OK' \
    GROUP BY date) \
AS err \
JOIN (SELECT date(time) AS date, count(*) AS req \
    FROM log \
    GROUP BY date) \
AS total \
ON err.date = total.date \
WHERE ROUND(100.0 * err.nerr / total.req, 2) >= 1;")

query_3 = cur.fetchall()

questions = ["What are the most popular three articles of all time?",
             "Who are the most popular article authors of all time?",
             "On which days did more than 1% of requests lead to errors?"]

queries = [query_1, query_2, query_3]

# Writting a file containing the questions and the answers

labels = {0: ["Article Name","Views"], 
		  1: ["Author Name","Views"],
		  2: ["Date","Errors Over Total Requests"]}

with open('data.txt', 'w') as f:
    for i, question in enumerate(questions):
        f.write("\nQuestion {index}: {question}\n\n".format(index = i + 1, 
        	question = questions[i]))
        for j, query in enumerate(queries[i]):
            f.write("\t{label_1}: {info_1}\n\t{label_2}: {info_2}\
{conditional_percentage}\n\n".format(label_1 = labels[i][0],
	info_1 = queries[i][j][0],
    label_2 = labels[i][1],
    info_2 = queries[i][j][1],
    conditional_percentage = "%" if i == 2 else ""))
