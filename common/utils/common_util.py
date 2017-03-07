import psycopg2
import os

from django.core.cache import cache

def get_source_path(nn_id, wf_ver, name) :
    """
    conbine parms and return source path (before data transformation)
    :param nn_id:
    :param wf_ver:
    :param name:
    :return:
    """
    return cache.get("source_root") + "/" + nn_id + "/" + wf_ver + "/" + name

def get_store_path(nn_id, name) :
    """
    conbine parms and return store path (after data transformation, use on net train)
    :param name:
    :return:
    """
    from master import models
    try:
        obj = models.NN_DEF_LIST_INFO.objects.get(nn_id=str(nn_id))
        if(obj != None) :
            return cache.get("store_root") + "/" + obj.biz_cate + "/" + obj.biz_sub_cate + "/" + name
        else :
            return ""
    except Exception as e:
        raise Exception(e)

def get_filepaths(directory):
    """
    utils return file paths under directory
    :param directory:
    :return:
    """

    import os
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths


gLogFloag = "Y"
gUserId = "-1"
gUrl = "{0}:{1}".format(os.environ['HOSTNAME'] , "8000")
gConpg = "dbname='tensormsa' user='tfmsauser' host='localhost' password='1234'"

def println(printStr):
    if gLogFloag == "Y":
        conn = psycopg2.connect(gConpg)
        cur = conn.cursor()
        if printStr == "S" or printStr == "s":
            sql = "delete from common_log_info where created_by = '"+gUserId+"'"
            cur.execute(sql)
            conn.commit()
        elif printStr == "E" or printStr == "e":
            sql = "select * from common_log_info where created_by = '"+gUserId+"' order by log_id"
            cur.execute(sql)
            rows = cur.fetchall()

            print("Trace.............................................................................")
            for i in range(0, len(rows)):
                for j in range(0, len(rows[i])):
                    if rows[i][j] is not None and cur.description[j][0] not in (
                    "id", "log_id", "creation_date", "last_update_date", "created_by", "last_updated_by"):
                        print(rows[i][j])
            print("..................................................................................")
        else:
            print(printStr)
            cur.execute("select COALESCE(max(log_id)::int,0)+10 seq from common_log_info where created_by = '"+gUserId+"'")
            rows = cur.fetchall()

            sql = "INSERT INTO common_log_info( "
            valueStr = ""

            # 일반적인 String 형태일 경우 출력을 해준다.
            try:
                valS = printStr.split("+")

                cnt = 1
                for i in valS:
                    if cnt != 1 and cnt < 31:
                        sql += ","
                        valueStr += ","
                    if cnt < 31:
                        sql += str("attr") + str(cnt)
                        valueStr += "'" + str(i) + "'"
                    cnt += 1

                sql += ",creation_date,last_update_date, created_by, last_updated_by,log_id) "
                sql += "VALUES (" + valueStr + ",now(),now(),'"+gUserId+"','"+gUserId+"','" + str(rows[0][0]) + "')"

                cur.execute(sql)
                conn.commit()
            except Exception as e:
                # 객체 형태일 경우 출력을 해준다.
                sql += "attr1,creation_date,last_update_date, created_by, last_updated_by,log_id) "
                sql += "VALUES ('" + str(printStr).replace("'","")+"',now(),now(),'" + gUserId + "','" + gUserId + "','" + str(rows[0][0]) + "')"
                cur.execute(sql)
                conn.commit()
        # 연결을 종료한다
        cur.close()
        conn.close()