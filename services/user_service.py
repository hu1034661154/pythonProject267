

#添加学生的方法
def add_stu(self,*args):
        #实现思路
        #1.确定用户数据，最终组装成sql语句
        lst = list(args)
        while len(lst) <= 6:
            lst.append('')
        sql = "insert into students(name,)"