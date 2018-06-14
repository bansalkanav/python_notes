import pymysql as pm

def connectdb():
    try:
        con = pm.connect(host='localhost', database='books', \
                         user='root', password='root')
        cursor = con.cursor()
        query = 'create table if not exist book(id int(5) primary key, \
            title varchar(10), author varchar(10), year int(4), isbn int(20))'
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
        query = 'insert into book values (NULL, ?, ?, ?, ?)',(title, author, year, isbn)
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
        query = 'select * from book where title=? OR author=? OR year=? OR isbn=?',(title, author, year, isbn)
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

def delete(id):
    try:
        con = pm.connect(host='localhost', database='books', \
                         user='root', password='root')
        cursor = con.cursor()
        query = 'delete from book where id=?',(id,)
        cursor.execute(query)
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
        query = 'update book set title=?, author=?, year=?, isbn=? where id=?',(title, author, year, isbn)
        cursor.execute(query)
    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print('Problem occured: ', e)

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()