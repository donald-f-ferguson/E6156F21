import pymysql
from Services.DataAccessServices.RDBAdaptor import RDBAdaptor as RDBAdaptor
import json

dd = {
    "id": 69174,
    "name": "COMSE6156_001_2018_3 - TOPICS IN SOFTWARE ENGINEERING: Cloud and Microservice Applications",
    "uuid": "DO57H1uh7HiQ3fyx9F9Ag9Bxjnsxe42QWO2BmzFO",
    "course_code": "COMSE6156_001_2018_3 - TOPICS IN SOFTWARE ENGINEERING",
    "course_title": "TOPICS IN SOFTWARE ENGINEERING: Cloud and Microservice Applications",
    "course_no": "COMSE6156",
    "section": "001",
    "year": "2018",
    "semester": "3"
}

c_info = {
    "user": "dbuser",
    "password": "dbuserdbuser",
    #"db": "e6156_new",
    "autocommit": True,
    "cursorclass": pymysql.cursors.DictCursor
}


def t1():

    rdba = RDBAdaptor(c_info)
    print("t1: cool")


def t2():

    rdba = RDBAdaptor(c_info)
    res = rdba.insert("new_e6156", "courses", dd)
    print("T2: res = ", res)


def t3():

    rdba = RDBAdaptor(c_info)
    res = rdba.get_by_primary_key("new_e6156", "courses", {"id": "11912"})
    print("T3: res = ", json.dumps(res, indent=2))


#t1()
#t2()
t3()