import Services.DataAccessServices.CourseWorksAdapter as cw_adapter

class Student():

    def __init__(self, context, j_data):
        self._context = context
        self.id = j_data["id"]
        self.user_id = j_data["sis_user_id"]
        self.login_id = j_data["login_id"]

        name_fields = j_data["sortable_name"].split(",")
        self.name = {
            "last_name": name_fields[0],
            "first_name": name_fields[1]
        }

    def to_json(self):
        result = {}
        result["id"] = self.id
        result["name"] = self.name
        result["user_id"] = self.user_id
        result["login_id"] = self.login_id

        return result


class Course():

    _field_list = ["id", "name", "uuid", "course_code_full", "course_no", "section", "year", "semester"]

    def __init__(self, context, j_data):
        self._context = context

        self.id = j_data["id"]
        self.name = j_data["name"]
        self.uuid = j_data["uuid"]
        self.course_code_full = j_data["course_code"]

        course_code_fields = self.course_code_full.split("_")
        self.course_no = course_code_fields[0]
        self.section = course_code_fields[1]
        self.year = course_code_fields[2]
        self.semester = course_code_fields[3][0]

    def to_json(self):
        result = {}
        for f in Course._field_list:
            result[f] = getattr(self, f)
        return result

    @classmethod
    def set_context(cls, context):
        cls._context = context

    @classmethod
    def get_courses(cls, role=None):
        res = cw_adapter.Adapter.set_context(cls._context)
        res = cw_adapter.Adapter.get_courses(role=role)

        if res is not None and len(res) > 0:
            result = []
            for j_data in res:
                result.append(Course(cls._context, j_data))
        else:
            result = None

        return result

    @classmethod
    def get_course(cls, course_id):
        res = cw_adapter.Adapter.set_context(cls._context)
        res = cw_adapter.Adapter.get_courses(course_id=course_id)

        if res is not None and len(res) > 0:
            res_in = res[0]
            result = Course(cls._context, res_in)
        else:
            result = None

        return result

    def get_students(self):

        res = cw_adapter.Adapter.set_context(self._context)
        res = cw_adapter.Adapter.get_students(self.id)

        if res[0] == 200:
            result = []
            for j_data in res[1]:
                result.append(Student(self._context, j_data))
        else:
            result = None

        return result


