import ibm_db

conn_string = "DATABASE=bludb;HOSTNAME=0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31198;PROTOCOL=TCPIP;UID={{ UID }};PWD={{ PASSWORD }};SECURITY=SSL"

def connect():    
    try:
        conn=ibm_db.connect(conn_string,"","")
        return conn
    except:
        return False
    
def ret_data(conn,sql):
    ret=list()
    stmt = ibm_db.exec_immediate(conn, sql)
    tup = ibm_db.fetch_tuple(stmt)
    while tup != False:
        ret.append(tup)
        tup = ibm_db.fetch_tuple(stmt)
    return ret