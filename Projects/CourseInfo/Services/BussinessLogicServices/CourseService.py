import pymysql

from Services.BussinessLogicServices.BaseService import BaseService
from Services.DataAccessServices.RDBAdaptor import RDBAdaptor


# DFF TODO -- This is also sloppy
c_info = {
    "user": "dbuser",
    "password": "dbuserdbuser",
    "autocommit": True,
    "cursorclass": pymysql.cursors.DictCursor
}
_rdb_adaptor = RDBAdaptor(c_info)


# DFF TODO -- Should be a singleton.
class CourseService(BaseService):

    _public_field_list = ["id", "name", "uuid", "course_code", "course_title", "course_no", "section", "year", "semester"]
    _context = None

    _table_name = "courses"
    _db_name = "new_e6156"

    def __init__(self):
        super().__init__()
        self._db_adaptor = _rdb_adaptor

    @classmethod
    def get_public_field_list(cls):
        return cls._public_field_list

    def get_course(self, course_id):
        pk = {"id": course_id}

        res = self._db_adaptor.get_by_primary_key(
            CourseService._db_name, CourseService._table_name, key_dict= pk)

        if res is not None and len(res) > 0:
            res_in = res[0]
            result = res_in
        else:
            result = None

        return result

    def get_courses(self, template):

        res = self._db_adaptor.get_by_template(
            CourseService._db_name, CourseService._table_name, template)

        return res







