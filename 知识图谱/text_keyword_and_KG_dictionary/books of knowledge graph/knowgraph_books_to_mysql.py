from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

engine = create_engine("mysql+pymysql://updater:Yuanjing123!@101.132.171.20:3306/aivision?charset=utf8", encoding="utf8", poolclass=QueuePool, pool_size=100, pool_timeout=100)



data = list()
for i in data:
    conn = engine.connect()
    transction = conn.begin()
    arg = (book_uri_list, knowledge_map_title)

    data = conn.execute("update tbl_knowledge_map set book_uri_list=%s where knowledge_map_title=%s", arg)
    transction.commit()


conn.close()