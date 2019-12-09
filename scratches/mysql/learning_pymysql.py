#导入包
import  pymysql
#链接数据库
#cursorclass = pymysql.cursors.DictCursor可以转化为元组对象
conn = pymysql.connect(host = 'localhost',port = 3306 , user = 'root',passwd = 'psy@123',db='test_create',cursorclass = pymysql.cursors.DictCursor)


try:
    #实例化游标对象
    cursor = conn.cursor()

    #输入sql语句
    sql = 'SELECT *FROM `students`;'
    result = cursor.execute(sql)


    #只能输出到数据的行数
    print(result)
    #fetchone（）取剩下的下一行
    #取出后，游标会发生移动
    print(cursor.fetchone())

    #fetchmany(n)取剩下的n行
    print(cursor.fetchmany(2))
    #mode='relative'相对位置移动
    cursor.scroll(-1,mode='relative')

    #fetchall()取剩下所有行
    data_r = cursor.fetchall()
    for data in data_r:
        print(data)
    #mode='absolute'绝对位置移动
    cursor.scroll(1,mode='absolute')



except Exception:print("查询失败")


#提交语句
conn.commit()

#关闭对象
cursor.close()
conn.close()
