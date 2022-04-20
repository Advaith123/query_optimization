'''
things to do

add ui
add sql to store last 5 queries

'''


import sqlparse

#query = input()
#query = sqlparse.split(query)
#SELECT *, (SELECT count(DISTINCT c.id)   FROM  comments AS c   WHERE  c.PostId = p.id LIMIT 1)   FROM  posts AS p  WHERE p.AnswerCount > 3 AND p.title LIKE '%optimized'  AND p.CreationDate >= '2017-01-01 00:00:00'  ORDER BY p.CreationDate LIMIT 100
#print(query)
#SELECT p.id, count(distinct c.id) FROM posts AS p LEFT JOIN comments AS c ON c.PostId = p.id GROUP BY;

def star(query):
    if 'SELECT *' in query or 'select *' in query:
        return 'use column names instead of *'

def like(query):
    subs = query.split("'")
    #print(subs)
    for i in subs:
        if i[-1] == "%":
            return 'avoid using leading wildcard'

def dates(query):
    subs = query.split("'")
    #print(subs)
    count = 0
    for i in subs:
        try:
            if i[4]=='-' and i[7]=='-' :
            #print('date yey',i)
                count = 1
        except:
            pass
    if count>0:
        return 'Avoid Using Date Functions In Conditions' 

def group(query):
    parsed = sqlparse.parse(query)
    #print(parsed[0].tokens)
    g=0; j=0; jf=0
    for i in parsed[0].tokens:
        k = str(i)
        #print(k)
        if 'GROUP BY' in k:
            #print(k)
            g=1
        if 'JOIN' in k and g>0:
            #its ok
            j=1
        if 'JOIN' in k and g==0:
            #not ok
            jf=1
            #print("perform group by before join to improve speed")
    if jf>0 and g>0:
        return "perform group by before join to improve speed"
    pass

def dist(query):
    parsed = sqlparse.parse(query)
    for i in parsed[0].tokens:
        #print(i)
        if 'DISTINCT' or 'distinct' in i:
            return "Avoid distinct if possible to increase speed"

#dist(query)
#group(query)
#dates(query)
#like(query)
#star(query)