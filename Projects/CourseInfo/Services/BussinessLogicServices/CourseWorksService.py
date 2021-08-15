import Services.DataAccessServices.CourseWorksAdapter as cw_adapter
from Services.BussinessLogicServices.BaseService import BaseService


class CourseService(BaseService):

    _public_field_list = ["id", "name", "uuid", "course_code", "course_title", "course_no", "section", "year", "semester"]
    _context = None

    def __init__(self):
        super().__init__()

    @classmethod
    def get_public_field_list(cls):
        return cls._public_field_list

    @classmethod
    def set_context(cls, context):
        cls._context = context
        cw_adapter.Adapter.set_context(context)

    @classmethod
    def get_courses(cls, role=None, template=None, fields=None):
        #res = cw_adapter.Adapter.set_context(cls._context)
        res = cw_adapter.Adapter.get_courses(role=role)

        if res is not None and len(res) > 0:
            res = cls.apply_filter(res, template, fields=None)
            result = res
        else:
            result = None

        return result

    @classmethod
    def get_course(cls, course_id):
        res = cw_adapter.Adapter.set_context(cls._context)
        res = cw_adapter.Adapter.get_courses(course_id=course_id)

        if res is not None and len(res) > 0:
            res_in = res[0]
            result = res_in
        else:
            result = None

        return result

    @classmethod
    def apply_map(cls, row):
        course_code = row.get('name', None)
        if course_code is not None:
            code_split = course_code.split("-")
            course_title = code_split[1].strip()
            row['course_title'] = course_title

            course_fields = code_split[0].strip()
            course_fields = course_fields.split("_")
            row["course_no"] = course_fields[0]
            row["section"] = course_fields[1]
            row["year"] = course_fields[2]
            row["semester"] = course_fields[3]

        return row






