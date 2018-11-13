import psycopg2

Month = ['January', 'February', 'March',
         'April', 'May', 'June',
         'July', 'August', 'September',
         'October', 'November', 'December']
DBNAME = "news"


def popular_articles(cursor):
    '''It receives database cursor and and print
    the most popular three article'''

    qry = '''select  title, count(*) as views
        from articles,log
        where articles.slug=regexp_replace(log.path,'/article/','')
        and status='200 OK'
        group by title
        order by views desc
        limit 3;'''
    cursor.execute(qry)
    rows = cursor.fetchall()
    print ('\n\n%s\n\n  most popular three articles:\n\n%s\n\n'
           % ('*'*40, '*'*40))
    for row in rows:
        print (''' * "%s" - %s Views\n''' % (row[0], row[1]))


def popular_authors(cursor):
    '''It receives database cursor and
    prints the most popular articles authors'''

    qry = '''select  authors.id, name, count(*) as views
           from log join (articles join authors
           on articles.author=authors.id)
           on articles.slug=regexp_replace(log.path,'/article/','')
           and status='200 OK'
           group by authors.id
           order by views desc ;'''
    cursor.execute(qry)
    rows = cursor.fetchall()
    print ('\n\n%s\n\n  most popular articles authors:\n\n%s\n\n'
           % ('*'*40, '*'*40))
    for row in rows:
        print (''' * "%s" - %s Views\n''' % (row[1], row[2]))


def errors_days(cursor):
    '''It receives database cursor and
    prints the days with request errors more than 1% '''

    qry = '''select date_part('day', daily_log.date),
                  date_part('month', daily_log.date),
                  date_part('year', daily_log.date),
                  (daily_err.count*100.0/daily_log.count) as errprsnt
                  from daily_err
                  join daily_log
                  on daily_err.date=daily_log.date
                  where (daily_err.count*100.0/daily_log.count)>1.0;'''
    cursor.execute(qry)
    rows = cursor.fetchall()
    print ('\n\n%s\n\n Worst days for client :\n\n%s\n\n' % ('*'*40, '*'*40))
    res = "* {} {}, {} - {}% errors"
    for row in rows:
        print (res.format(Month[int(row[1]-1)], int(row[0]),
               int(row[2]), round(row[3], 2)) + '\n\n')


db = psycopg2.connect(database="news")
c = db.cursor()

popular_articles(c)
popular_authors(c)
errors_days(c)
db.close()
