import pymysql as pm

def connectdb():
    try:
        con = pm.connect(host='localhost', database='books', \
                         user='root', password='root')
        cursor = con.cursor()
        query = 'create table if not exists book(id int(5) primary key auto_increment, title varchar(10), author varchar(10), year int(4), isbn int(20))'
        cursor.execute(query)
        con.commit()

    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print('Problem occured: ', e)

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

def insert(title, author, year, isbn):
    try:
        con = pm.connect(host='localhost', database='books', \
                         user='root', password='root')
        cursor = con.cursor()
        query = 'insert into book values (NULL, %s, %s, %s, %s)'
        data = (title, author, year, isbn)
        cursor.execute(query, data)
        con.commit()

    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print('Problem occured: ', e)

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

def view():
    try:
        con = pm.connect(host='localhost', database='books', \
                         user='root', password='root')
        cursor = con.cursor()
        query = 'select * from book'
        cursor.execute(query)
        data = cursor.fetchall()
        return data

    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print('Problem occured: ', e)

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

def search(title='', author='', year='', isbn=''):
    try:
        con = pm.connect(host='localhost', database='books', \
                         user='root', password='root')
        cursor = con.cursor()
        query = 'select * from book where title=%s OR author=%s OR year=%s OR isbn=%s'
        d = (title, author, year, isbn)
        cursor.execute(query, d)
        data = cursor.fetchall()
        return data

    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print('Problem occured: ', e)

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

def delete(id):
    try:
        con = pm.connect(host='localhost', database='books', \
                         user='root', password='root')
        cursor = con.cursor()
        query = 'delete from book where id=%s'
        cursor.execute(query, id)
        con.commit()

    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print('Problem occured: ', e)

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

def update(id, title, author, year, isbn):
    try:
        con = pm.connect(host='localhost', database='books', \
                         user='root', password='root')
        cursor = con.cursor()
        query = 'update book set title=%s, author=%s, year=%s, isbn=%s where id=%s'
        data = (title, author, year, isbn, id)
        cursor.execute(query, data)
        con.commit()

    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print('Problem occured: ', e)

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()
