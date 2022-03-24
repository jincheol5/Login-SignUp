import pymysql

#db = basic
#table = user
#column = id,name,userid,userpw

#db 연결 
def connect_db():
    connect = pymysql.connect(host='localhost', user='root', password='4293', db='basic', charset='utf8')
    return connect


#sign up
def signup_db(name,userid,userpw):

    connect=connect_db()
    cur=connect.cursor()

    sql="insert into user(name,userid,userpw) values('"+name+"','"+userid+"','"+userpw+"');"
    cur.execute(sql)
    
    connect.commit() #완전히 저장
    connect.close() #연결 종료 
    

