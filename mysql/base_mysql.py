import pymysql

class Mysql(object):

    def __init__(self):
        self.conn = pymysql.connect(host='localhost',user='root',
                                    password='root',database='school',charset='utf8')
    #实现查询方法
    def get_all(self,sql):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(e)

        finally:
            if self.conn:
                self.conn.close()

     # 添加学生的方法
    def add_stu(self, *args):
         # 实现思路
        # 1.确定用户数据，最终组装成sql语句
        lst = list(args)
        while len(lst) <= 6:
           # lst.append('')
         sql = "insert into students(name,age,sex,class,card,city) values('{}',{},'{}','{}','{}','{}')".format(*lst)
        #2.调用update()方法，实现插入学生操作
        result = self.m.update(sql)
        #3.给出用户提示
        if not result:
            print("添加学生记录成功")
        else:
            print("添加失败")

    #实现修改方法
    def update(self):
        pass

#if __name__ == '__main__':
# sql = "select * from students where age = 30"
    # m = Mysql()
    # print(m.get_all(sql))

    #us.add_stu('测试总监',38,'男','7班','1000020003000800','北京')