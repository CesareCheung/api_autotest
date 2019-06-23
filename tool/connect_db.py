import pymysql.cursors
import json


class OperationMysql:
    """操作数据库"""

    def __init__(self):
        self.conn=pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            db='test',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor

        )

        self.cur=self.conn.cursor()

    def search_all(self,sql):
        """
        查询数据
        :param sql:
        :return:
        """
        self.cur.execute(sql)
        result=self.cur.fetchone()
        result=json.dumps(result)
        return result
if __name__ == '__main__':
    op_mysql=OperationMysql()
    res=op_mysql.search_all('select * from student where s_no=1;')
    print(res)