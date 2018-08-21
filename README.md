#  Log Analysis Project



This project is the third project of [Udacity Full-Stack Web Developer Nanodegree](https://udacity.com/course/full-stack-web-developer-nanodegree--nd004). In this project the student is challenged to stretch the SQL skills accquired, interacting with a live database both from the command line and from code.

The dabase contains over a million rows and the student's job is to refine complex queries and use them to draw business conclusions from the data generation reports.



## The task

The student's task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the `psycopg2` module to connect to the database. 



## The Data

The data used to build this project can be found [here.](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)   



## So what are we reporting, anyway?

Here are the questions the reporting tool should answer.

**1. What are the most popular three articles of all time?** Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

**2. Who are the most popular article authors of all time?** That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

**3. On which days did more than 1% of requests lead to errors?** The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.



## The code and exploration behing the answers


```python
import psycopg2
```


```python
# Connect to an existing database

conn = psycopg2.connect("dbname=news")

# Open a cursor to perform database operations

cur = conn.cursor()
```


```python
# Get database tables

cur.execute("SELECT table_name \
FROM information_schema.tables \
WHERE table_schema = 'public'")

tables = cur.fetchall()
tables
```




    [('log',), ('authors',), ('articles',)]




```python
# Getting to know the columns/categories for each Table

for table in tables:
    
    cur.execute("SELECT column_name \
    FROM information_schema.columns \
    WHERE table_name = '{!s}';".format(table[0]))
    
    print('\n' + table[0] + ': \n')
    print(cur.fetchall())
```


    log: 
    
    [('path',), ('ip',), ('method',), ('status',), ('time',), ('id',)]
    
    authors: 
    
    [('name',), ('bio',), ('id',)]
    
    articles: 
    
    [('author',), ('title',), ('slug',), ('lead',), ('body',), ('time',), ('id',)]



```python
# Getting to know log.path

cur.execute("SELECT path, count(*) \
AS views \
FROM log \
GROUP BY path \
ORDER BY views DESC")

cur.fetchall()
```




    [('/', 479121L),
     ('/article/candidate-is-jerk', 338647L),
     ('/article/bears-love-berries', 253801L),
     ('/article/bad-things-gone', 170098L),
     ('/article/goats-eat-googles', 84906L),
     ('/article/trouble-for-troubled', 84810L),
     ('/article/balloon-goons-doomed', 84557L),
     ('/article/so-many-bears', 84504L),
     ('/article/media-obsessed-with-bears', 84383L),
     ('/spam-spam-spam-humbug', 301L),
     ('/%20%20%20', 290L),
     ('/+++ATH0', 288L),
     ('/article/candidate-is-jerkx', 161L),
     ('/article/candidate-is-jerkq', 155L),
     ('/article/candidate-is-jerkh', 152L),
     ('/article/candidate-is-jerkr', 148L),
     ('/article/candidate-is-jerkg', 147L),
     ('/article/candidate-is-jerke', 146L),
     ('/article/candidate-is-jerkb', 144L),
     ('/article/candidate-is-jerkl', 144L),
     ('/article/candidate-is-jerkv', 143L),
     ('/article/candidate-is-jerki', 142L),
     ('/article/candidate-is-jerkn', 138L),
     ('/article/candidate-is-jerkt', 138L),
     ('/article/candidate-is-jerky', 137L),
     ('/article/candidate-is-jerkf', 137L),
     ('/article/candidate-is-jerkp', 135L),
     ('/article/candidate-is-jerka', 135L),
     ('/article/candidate-is-jerkw', 134L),
     ('/article/candidate-is-jerkc', 134L),
     ('/article/candidate-is-jerkz', 133L),
     ('/article/candidate-is-jerkm', 132L),
     ('/article/candidate-is-jerks', 131L),
     ('/article/candidate-is-jerkd', 124L),
     ('/article/candidate-is-jerku', 124L),
     ('/article/bears-love-berriesp', 123L),
     ('/article/candidate-is-jerkj', 121L),
     ('/article/candidate-is-jerkk', 120L),
     ('/article/bears-love-berriesb', 118L),
     ('/article/bears-love-berriesv', 117L),
     ('/article/bears-love-berriesw', 115L),
     ('/article/bears-love-berriesy', 111L),
     ('/article/bears-love-berriess', 110L),
     ('/article/bears-love-berriesm', 109L),
     ('/article/bears-love-berriesu', 106L),
     ('/article/bears-love-berriesj', 106L),
     ('/article/bears-love-berriest', 104L),
     ('/article/bears-love-berriesg', 104L),
     ('/article/bears-love-berriesq', 102L),
     ('/article/bears-love-berriesr', 102L),
     ('/article/bears-love-berriesi', 101L),
     ('/article/bears-love-berriesk', 101L),
     ('/article/bears-love-berriesn', 101L),
     ('/article/bears-love-berriesx', 100L),
     ('/article/bears-love-berriesc', 100L),
     ('/article/bears-love-berriesa', 97L),
     ('/article/bears-love-berriesd', 95L),
     ('/article/bears-love-berriese', 92L),
     ('/article/bears-love-berriesl', 92L),
     ('/article/bad-things-gonek', 88L),
     ('/article/bears-love-berriesf', 88L),
     ('/article/bears-love-berriesz', 88L),
     ('/article/bad-things-gonev', 84L),
     ('/article/bears-love-berriesh', 82L),
     ('/article/bad-things-goney', 73L),
     ('/article/bad-things-goneq', 73L),
     ('/article/bad-things-gonee', 72L),
     ('/article/bad-things-goneh', 72L),
     ('/article/bad-things-gonez', 72L),
     ('/article/bad-things-goneu', 70L),
     ('/article/bad-things-goneb', 69L),
     ('/article/bad-things-gonef', 68L),
     ('/article/bad-things-gonec', 67L),
     ('/article/bad-things-gonen', 67L),
     ('/article/bad-things-gones', 66L),
     ('/article/bad-things-gonea', 66L),
     ('/article/bad-things-gonem', 66L),
     ('/article/bad-things-gonew', 66L),
     ('/article/bad-things-gonep', 65L),
     ('/article/bad-things-gonej', 64L),
     ('/article/bad-things-goneg', 60L),
     ('/article/bad-things-gonel', 60L),
     ('/article/bad-things-gonei', 60L),
     ('/article/bad-things-gonex', 59L),
     ('/article/bad-things-goner', 55L),
     ('/article/bad-things-goned', 52L),
     ('/article/balloon-goons-doomedt', 50L),
     ('/article/goats-eat-googlesc', 50L),
     ('/article/trouble-for-troubledk', 50L),
     ('/article/bad-things-gonet', 50L),
     ('/article/media-obsessed-with-bearsb', 49L),
     ('/article/media-obsessed-with-bearse', 45L),
     ('/article/trouble-for-troubledm', 45L),
     ('/article/media-obsessed-with-bearsg', 44L),
     ('/article/trouble-for-troubledy', 44L),
     ('/article/balloon-goons-doomeda', 44L),
     ('/article/media-obsessed-with-bearsh', 43L),
     ('/article/goats-eat-googlesd', 43L),
     ('/article/so-many-bearsf', 43L),
     ('/article/media-obsessed-with-bearsc', 43L),
     ('/article/trouble-for-troubledg', 43L),
     ('/article/goats-eat-googlesl', 42L),
     ('/article/so-many-bearsx', 42L),
     ('/article/so-many-bearsv', 42L),
     ('/article/goats-eat-googlesx', 42L),
     ('/article/balloon-goons-doomedu', 41L),
     ('/article/so-many-bearsc', 41L),
     ('/article/trouble-for-troublede', 41L),
     ('/article/so-many-bearsm', 41L),
     ('/article/balloon-goons-doomedi', 41L),
     ('/article/media-obsessed-with-bearsa', 40L),
     ('/article/goats-eat-googlesb', 40L),
     ('/article/so-many-bearsh', 40L),
     ('/article/media-obsessed-with-bearsy', 40L),
     ('/article/goats-eat-googlesp', 39L),
     ('/article/so-many-bearsz', 39L),
     ('/article/trouble-for-troubledp', 39L),
     ('/article/goats-eat-googlesk', 38L),
     ('/article/balloon-goons-doomedb', 38L),
     ('/article/media-obsessed-with-bearsr', 38L),
     ('/article/trouble-for-troubledn', 38L),
     ('/article/balloon-goons-doomedj', 38L),
     ('/article/balloon-goons-doomedk', 38L),
     ('/article/trouble-for-troubleda', 38L),
     ('/article/goats-eat-googlesr', 38L),
     ('/article/trouble-for-troubledx', 37L),
     ('/article/balloon-goons-doomeds', 37L),
     ('/article/so-many-bearsb', 37L),
     ('/article/so-many-bearsl', 37L),
     ('/article/goats-eat-googless', 37L),
     ('/article/so-many-bearst', 37L),
     ('/article/so-many-bearsp', 37L),
     ('/article/so-many-bearsn', 37L),
     ('/article/media-obsessed-with-bearsm', 36L),
     ('/article/trouble-for-troubledh', 36L),
     ('/article/so-many-bearsj', 36L),
     ('/article/trouble-for-troubledb', 36L),
     ('/article/goats-eat-googlesw', 36L),
     ('/article/media-obsessed-with-bearsn', 36L),
     ('/article/goats-eat-googlesa', 36L),
     ('/article/so-many-bearsk', 35L),
     ('/article/balloon-goons-doomedp', 35L),
     ('/article/goats-eat-googlesz', 35L),
     ('/article/goats-eat-googlesm', 35L),
     ('/article/media-obsessed-with-bearsj', 35L),
     ('/article/media-obsessed-with-bearsk', 34L),
     ('/article/goats-eat-googlesv', 34L),
     ('/article/media-obsessed-with-bearsz', 34L),
     ('/article/media-obsessed-with-bearsf', 34L),
     ('/article/trouble-for-troubledw', 34L),
     ('/article/trouble-for-troubledj', 34L),
     ('/article/trouble-for-troubledt', 34L),
     ('/article/media-obsessed-with-bearsq', 34L),
     ('/article/goats-eat-googlesq', 34L),
     ('/article/trouble-for-troubledf', 34L),
     ('/article/goats-eat-googlesf', 34L),
     ('/article/media-obsessed-with-bearsi', 34L),
     ('/article/so-many-bearsa', 34L),
     ('/article/balloon-goons-doomedq', 34L),
     ('/article/so-many-bearsi', 34L),
     ('/article/so-many-bearss', 33L),
     ('/article/media-obsessed-with-bearsv', 33L),
     ('/article/so-many-bearsd', 33L),
     ('/article/so-many-bearsg', 33L),
     ('/article/so-many-bearsu', 33L),
     ('/article/balloon-goons-doomedd', 33L),
     ('/article/media-obsessed-with-bearsx', 33L),
     ('/article/goats-eat-googlesg', 33L),
     ('/article/trouble-for-troubledi', 33L),
     ('/article/balloon-goons-doomedn', 32L),
     ('/article/so-many-bearsw', 32L),
     ('/article/balloon-goons-doomedc', 31L),
     ('/article/goats-eat-googlesi', 31L),
     ('/article/so-many-bearsr', 31L),
     ('/article/media-obsessed-with-bearsp', 31L),
     ('/article/media-obsessed-with-bearss', 31L),
     ('/article/balloon-goons-doomedz', 31L),
     ('/article/media-obsessed-with-bearst', 31L),
     ('/article/balloon-goons-doomedy', 30L),
     ('/article/trouble-for-troubledv', 30L),
     ('/article/media-obsessed-with-bearsu', 30L),
     ('/article/trouble-for-troubledc', 30L),
     ('/article/balloon-goons-doomedv', 30L),
     ('/article/balloon-goons-doomedl', 30L),
     ('/article/goats-eat-googlese', 30L),
     ('/article/trouble-for-troubledl', 30L),
     ('/article/so-many-bearsy', 30L),
     ('/article/balloon-goons-doomedh', 30L),
     ('/article/media-obsessed-with-bearsl', 30L),
     ('/article/balloon-goons-doomedr', 30L),
     ('/article/media-obsessed-with-bearsd', 29L),
     ('/article/balloon-goons-doomedm', 29L),
     ('/article/trouble-for-troubledu', 29L),
     ('/article/trouble-for-troubleds', 29L),
     ('/article/balloon-goons-doomedw', 28L),
     ('/article/goats-eat-googlesj', 28L),
     ('/article/goats-eat-googlesh', 28L),
     ('/article/trouble-for-troubledz', 28L),
     ('/article/goats-eat-googlesu', 27L),
     ('/article/goats-eat-googlesy', 27L),
     ('/article/so-many-bearsq', 27L),
     ('/article/goats-eat-googlest', 27L),
     ('/article/trouble-for-troubledr', 26L),
     ('/article/balloon-goons-doomede', 26L),
     ('/article/trouble-for-troubledd', 26L),
     ('/article/balloon-goons-doomedg', 26L),
     ('/article/balloon-goons-doomedf', 25L),
     ('/article/goats-eat-googlesn', 25L),
     ('/article/trouble-for-troubledq', 25L),
     ('/article/so-many-bearse', 24L),
     ('/article/balloon-goons-doomedx', 23L),
     ('/article/media-obsessed-with-bearsw', 23L)]




```python
# Getting to know articles.slug

cur.execute("SELECT slug \
FROM articles;")

cur.fetchall()
```




    [('bad-things-gone',),
     ('balloon-goons-doomed',),
     ('bears-love-berries',),
     ('candidate-is-jerk',),
     ('goats-eat-googles',),
     ('media-obsessed-with-bears',),
     ('trouble-for-troubled',),
     ('so-many-bears',)]




```python
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
query_1
```




    [('Candidate is jerk, alleges rival', 342102L),
     ('Bears love berries, alleges bear', 256365L),
     ('Bad things gone, say good people', 171762L)]




```python
# Getting to know articles.author

cur.execute("SELECT author FROM articles;")
cur.fetchall()
```




    [(3,), (4,), (1,), (2,), (1,), (1,), (2,), (1,)]



From the above query we can see that `articles.author` refer to authors IDs, not to the actual name of the *authors*


```python
# Getting to know authors.id

cur.execute("SELECT id FROM authors;")
cur.fetchall()
```




    [(1,), (2,), (3,), (4,)]




```python
# Retrieving the most popular authors by the total number of views of each author articles

cur.execute("SELECT authors.name, count(log) AS views \
FROM authors \
JOIN articles ON authors.id = articles.author \
JOIN log ON log.path LIKE CONCAT('%',articles.slug,'%') \
GROUP BY authors.name \
ORDER BY views DESC;")

query_2 = cur.fetchall()
query_2
```




    [('Ursula La Multa', 512805L),
     ('Rudolf von Treppenwitz', 427781L),
     ('Anonymous Contributor', 171762L),
     ('Markoff Chaney', 85387L)]




```python
# Seeing which status codes we have in the log table

cur.execute("SELECT status, count(status) FROM log GROUP BY status;")

cur.fetchall()
```




    [('404 NOT FOUND', 12908L), ('200 OK', 1664827L)]



Since we only have two types of status codes, there's no need of grouping any further for counting, it either is a successful request or it throwed an *404 not found* error.


```python
# Number of errors by day

cur.execute("SELECT date(time), count(*) as nerr \
FROM log \
WHERE status LIKE '%404%' \
GROUP BY date(time) \
ORDER BY nerr DESC;")

cur.fetchall()
```




    [(datetime.date(2016, 7, 17), 1265L),
     (datetime.date(2016, 7, 19), 433L),
     (datetime.date(2016, 7, 24), 431L),
     (datetime.date(2016, 7, 5), 423L),
     (datetime.date(2016, 7, 6), 420L),
     (datetime.date(2016, 7, 21), 418L),
     (datetime.date(2016, 7, 8), 418L),
     (datetime.date(2016, 7, 9), 410L),
     (datetime.date(2016, 7, 15), 408L),
     (datetime.date(2016, 7, 22), 406L),
     (datetime.date(2016, 7, 11), 403L),
     (datetime.date(2016, 7, 3), 401L),
     (datetime.date(2016, 7, 30), 397L),
     (datetime.date(2016, 7, 26), 396L),
     (datetime.date(2016, 7, 28), 393L),
     (datetime.date(2016, 7, 25), 391L),
     (datetime.date(2016, 7, 2), 389L),
     (datetime.date(2016, 7, 20), 383L),
     (datetime.date(2016, 7, 14), 383L),
     (datetime.date(2016, 7, 13), 383L),
     (datetime.date(2016, 7, 29), 382L),
     (datetime.date(2016, 7, 4), 380L),
     (datetime.date(2016, 7, 18), 374L),
     (datetime.date(2016, 7, 16), 374L),
     (datetime.date(2016, 7, 12), 373L),
     (datetime.date(2016, 7, 23), 373L),
     (datetime.date(2016, 7, 10), 371L),
     (datetime.date(2016, 7, 27), 367L),
     (datetime.date(2016, 7, 7), 360L),
     (datetime.date(2016, 7, 31), 329L),
     (datetime.date(2016, 7, 1), 274L)]




```python
# Total number of access by day

cur.execute("SELECT date(time), count(*) as req \
FROM log \
GROUP BY date(time) \
ORDER BY req DESC;")

cur.fetchall()
```




    [(datetime.date(2016, 7, 17), 55907L),
     (datetime.date(2016, 7, 18), 55589L),
     (datetime.date(2016, 7, 19), 55341L),
     (datetime.date(2016, 7, 21), 55241L),
     (datetime.date(2016, 7, 9), 55236L),
     (datetime.date(2016, 7, 22), 55206L),
     (datetime.date(2016, 7, 2), 55200L),
     (datetime.date(2016, 7, 14), 55196L),
     (datetime.date(2016, 7, 13), 55180L),
     (datetime.date(2016, 7, 24), 55100L),
     (datetime.date(2016, 7, 8), 55084L),
     (datetime.date(2016, 7, 30), 55073L),
     (datetime.date(2016, 7, 15), 54962L),
     (datetime.date(2016, 7, 29), 54951L),
     (datetime.date(2016, 7, 4), 54903L),
     (datetime.date(2016, 7, 23), 54894L),
     (datetime.date(2016, 7, 3), 54866L),
     (datetime.date(2016, 7, 12), 54839L),
     (datetime.date(2016, 7, 28), 54797L),
     (datetime.date(2016, 7, 6), 54774L),
     (datetime.date(2016, 7, 7), 54740L),
     (datetime.date(2016, 7, 25), 54613L),
     (datetime.date(2016, 7, 5), 54585L),
     (datetime.date(2016, 7, 20), 54557L),
     (datetime.date(2016, 7, 16), 54498L),
     (datetime.date(2016, 7, 11), 54497L),
     (datetime.date(2016, 7, 27), 54489L),
     (datetime.date(2016, 7, 10), 54489L),
     (datetime.date(2016, 7, 26), 54378L),
     (datetime.date(2016, 7, 31), 45845L),
     (datetime.date(2016, 7, 1), 38705L)]




```python
# Percentage of errors by day

cur.execute("SELECT err.date as date, ROUND(100.0 * err.nerr / total.req, 2) AS percentage \
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
ORDER BY percentage DESC;")

cur.fetchall()
```




    [(datetime.date(2016, 7, 17), Decimal('2.26')),
     (datetime.date(2016, 7, 19), Decimal('0.78')),
     (datetime.date(2016, 7, 24), Decimal('0.78')),
     (datetime.date(2016, 7, 6), Decimal('0.77')),
     (datetime.date(2016, 7, 5), Decimal('0.77')),
     (datetime.date(2016, 7, 8), Decimal('0.76')),
     (datetime.date(2016, 7, 21), Decimal('0.76')),
     (datetime.date(2016, 7, 11), Decimal('0.74')),
     (datetime.date(2016, 7, 22), Decimal('0.74')),
     (datetime.date(2016, 7, 9), Decimal('0.74')),
     (datetime.date(2016, 7, 15), Decimal('0.74')),
     (datetime.date(2016, 7, 3), Decimal('0.73')),
     (datetime.date(2016, 7, 26), Decimal('0.73')),
     (datetime.date(2016, 7, 31), Decimal('0.72')),
     (datetime.date(2016, 7, 25), Decimal('0.72')),
     (datetime.date(2016, 7, 28), Decimal('0.72')),
     (datetime.date(2016, 7, 30), Decimal('0.72')),
     (datetime.date(2016, 7, 1), Decimal('0.71')),
     (datetime.date(2016, 7, 20), Decimal('0.70')),
     (datetime.date(2016, 7, 29), Decimal('0.70')),
     (datetime.date(2016, 7, 2), Decimal('0.70')),
     (datetime.date(2016, 7, 13), Decimal('0.69')),
     (datetime.date(2016, 7, 14), Decimal('0.69')),
     (datetime.date(2016, 7, 4), Decimal('0.69')),
     (datetime.date(2016, 7, 16), Decimal('0.69')),
     (datetime.date(2016, 7, 12), Decimal('0.68')),
     (datetime.date(2016, 7, 23), Decimal('0.68')),
     (datetime.date(2016, 7, 10), Decimal('0.68')),
     (datetime.date(2016, 7, 27), Decimal('0.67')),
     (datetime.date(2016, 7, 18), Decimal('0.67')),
     (datetime.date(2016, 7, 7), Decimal('0.66'))]




```python
# Days errors were throwed more than 1% of the total requests

cur.execute("SELECT err.date as date, ROUND(100.0 * err.nerr / total.req, 2) AS percentage \
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
query_3
```




    [(datetime.date(2016, 7, 17), Decimal('2.26'))]




```python
questions = ["What are the most popular three articles of all time?",
            "Who are the most popular article authors of all time?",
            "Who are the most popular article authors of all time?"]

queries = [query_1, query_2, query_3]
```


```python
# Writting a file containing the questions and the answers

with open('data.txt', 'w') as f:
    for i, question in enumerate(questions):
        f.write(question + '\n\n' + '\n'.join(map(str,queries[i])) + '\n\n')
```



## How can I run this project myself ?



- #### Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox.](https://www.virtualbox.org/wiki/Downloads)

- #### Windows user?

   It's probably a more adequate choice to try out the [Windows PowerShell](https://docs.microsoft.com/pt-br/powershell/scripting/setup/installing-windows-powershell?view=powershell-6) instead of the usual Windows Command Prompt. Alternatively you can use [Git Bash](https://git-scm.com/downloads) as recommended by Udacity or any other Shell Prompt for Windows of your choice.

- #### Clone the repository to your local machine:

  ```
  git clone https://github.com/EduGord/Log-Analysis-Project
  ```
   or alternatively do it from the Udacity's original source at [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm)

- #### Start the virtual machine

   From your terminal, inside the project directory, run `vagrant up` to download and install the Linux operating in use for this project. As soon as that's finished, you are all set to run `vagrant ssh` (default password is: `vagrant`) to log in into the VM!

- #### Find the right directory ###

   Usually you'll have to run the following commands in your shell command line to get to the right directory where the files are at:

   ```
   cd ..
   cd ..
   cd vagrant
   ```

   Run a `ls` command to see if you're in the right directory.

- #### Setup the Database

  To load the database use the following command:

  ```
  psql -d news -f newsdata.sql;
  ```

- #### Interact with it through Python + Jupyter Notebook

   If you want to interact with the database as shown in this README file, you should also do a couple more things:

   - Install jupyter notebook in your VM machine, through the shell command line:

     ```
     sudo pip install jupyter
     ```

   - Run your jupyter notebook locally, through the shell command line:

     ```
     jupyter notebook --ip 0.0.0.0 --port 8080
     ```

   - Open your browser and go to http://localhost:8080

   - Insert the *token* displayed in your shell command line after running the *jupyter notebook*

     
