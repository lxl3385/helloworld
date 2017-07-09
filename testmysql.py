#-*- coding:utf-8 -*-

def test_sql():
   ### 开发者直接在requirements.txt中指定依赖MySQL-python
    import MySQLdb
    dbname = "<mytest>" # 数据库名称
    api_key = "<f02f03fe58b541e381376d3da6134fde>" # 用户AK
    secret_key = "<2d5595f54c124380a9c4667d1333b694>" # 用户SK
    raise "hello"
   ### 连接MySQL服务
    mydb = MySQLdb.connect(
        host   = "sqld.duapp.com",
        port   = 4050,
        user   = api_key,
        passwd = secret_key,
        db = dbname)

   ### 执行sql命令，创建table test
    cursor = mydb.cursor()
    
    cmd = '''CREATE TABLE IF NOT EXISTS test (
         id int(4) auto_increment,
         name char(20) not null,
         age int(2),
         sex char(8) default 'man',
         primary key (id))'''

    cursor.execute(cmd)

    mydb.close()
    return 'create table test success!'

def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    try:
        return test_sql()
    except:
        return 'handle exceptions'

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)