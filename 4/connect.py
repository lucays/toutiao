'''
本代码由于你可能没有对应数据，实质上无法正常运行。
'''
import pymysql


def test_mysql(title: str, speaker: str):
    conn = pymysql.connect(host='localhost',  # 远端数据库的话改成对应地址
                                user='root',  # 用户
                                password='huanghai',  # 演示用密码，替换成自己数据库的密码
                                db='spider',  # 数据库名称
                                charset='utf8mb4',  # 设置编码
                                cursorclass=pymysql.cursors.SSCursor)
    try:
        sql = "insert into zhihu (title, speaker) values (%s, %s)"
        with conn.cursor(pymysql.cursors.SSCursor) as cur:
            cur.execute(sql, (title, speaker))
        # conn.commit()
        sql = "select title, speaker from zhihu where id>100"
        with conn.cursor() as cur:
            cur.execute(sql)
            while True:
                l, r = cur.fetchone()
                '''
                sql_id = "select id from zhihu where title=%s"
                cur.execute(sql_id)
                for i in cur:
                    print(i[0])
                '''
                if not r:
                    break
        sql = "select title from zhihu where id<100"
        with conn.cursor() as cur:
            cur.execute(sql)
            for i in cur:
                '''
                sql_id = "select id from zhihu where title=%s"
                cur.execute(sql_id)
                for i in cur:
                    print(i[0])
                '''
                print(i[0])
            # titles = [i[0] for i in cur]
        with conn.cursor() as cur:
            # datas是一个list，里面又包含几十万个list
            bigN = 50000 # 一次插5万条，设置的太高mysql也不让插那么多
            for i in range(len(datas)//bigN):
                l, r = i * bigN, (i + 1) * bigN
                sql = "insert ... values %s"
                sql = sql % ','.join(datas[l:r])
                cur.execute(sql)
                if r + bigN > len(datas):
                    sql = "insert ... values %s"
                    sql = sql % ','.join(datas[r:]) # 边界条件，保证尾部元素都能插入
                    cur.execute(sql)
    except:
        conn.rollback()  # 抛出异常时回滚事务
    finally:
        conn.close()


def main():
    title, speaker = 'test', 'test'
    test_mysql(title, speaker)


if __name__ == '__main__':
    main()
