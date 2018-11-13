# loganalysis

loganlysis is module in python  that analyzes the data log of a news website ,it recognizes the most popular articles and authors and The worst days for site visitors.

## Install and Run
to running program cd into folder that contain loganalysis.py then type:
~~~
$ python loganalysis.py
~~~
Before you run this program, you must install `news` database , so download [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) file .
cd into folder that contain file then use the command:
`psql -d news -f newsdata.sql`
This will create a database called news and fill it with data.

Then connect to the database and  create two views:
~~~
   create view daily_log as 
   select date_trunc('day', time) as date,count(*) from log 
   group by date;
~~~
~~~
   create view daily_err as 
    select date_trunc('day', time) as date,count(*) from log 
    where status ~ '.*4[0-5][0-9].*' 
    group by date;
~~~
    


## Code Design
This module has three functions:
- popular_articles():  take database cursor as input and print the most popular three articles.
- popular_authors():  take database cursor as input and print the most popular authors articles.
- errors_days(): take database cursor as input and print days have more than 1% requests errors.
## Reference

   - Udacity classroom.
   - [How to Writing READMEs](https://classroom.udacity.com/courses/ud777) lesson, Udacity website.
   - newsdata.sql file that create database, from Udacity website.
   - [PostgreSQL 9.5.15 Documentation Chapter 9. Functions and Operators](https://www.postgresql.org/docs/9.5/functions-string.html)
 