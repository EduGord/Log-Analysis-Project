import psycopg2

# Connect to an existing database

conn = psycopg2.connect("dbname=news")

# Open a cursor to perform database operations

cur = conn.cursor()

# Retrieving the 3 most accessed articles of all times

cur.execute("SELECT articles.title, count(log) \
AS views \
FROM log \
JOIN articles \
ON log.path LIKE CONCAT('%',articles.slug,'%') \
GROUP BY articles.title \
ORDER BY views DESC \
LIMIT 3;")

query_1 = cur.fetchall()

# Retrieving the most popular authors
# by the total number of views of each author articles

cur.execute("SELECT authors.name, count(log) AS views \
FROM authors \
JOIN articles ON authors.id = articles.author \
JOIN log ON log.path LIKE CONCAT('%',articles.slug,'%') \
GROUP BY authors.name \
ORDER BY views DESC;")

query_2 = cur.fetchall()

# Days errors were throwed more than 1% of the total requests

cur.execute("SELECT err.date as date, ROUND(100.0 * err.nerr / total.req, 2) \
AS percentage \
FROM (SELECT date(time) as date, count(*) as nerr \
    FROM log \
    WHERE status LIKE '%404%' \
    GROUP BY date) \
AS err \
JOIN (SELECT date(time) as date, count(*) as req \
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

with open('data.txt', 'w') as f:
    for i, question in enumerate(questions):
        f.write(question + '\n\n' + '\n'.join(map(str, queries[i])) + '\n\n')
