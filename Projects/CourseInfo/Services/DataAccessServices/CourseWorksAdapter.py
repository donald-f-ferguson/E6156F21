import requests



class Adapter():

    _default_ctx = context = {
        "base_url":  "https://courseworks2.columbia.edu/api/v1",
        "access_token": "Bearer 1396~yOhKmofKhElEGTZNZhYj8qp1fHw8GL5Cepd1NpIx8yHj0IEDpeNuzES7ezOyU7Hz"
    }
    _context = None

    @classmethod
    def set_context(cls, ctx):
        cls._context = ctx
        pass

    @classmethod
    def get_context(cls):
        if cls._context is None:
            cls._context = Adapter._default_ctx
        return cls._context

    @classmethod
    def get_next_url(cls, links=None):
        next_url = None
        if links is not None:
            all_links = links.split(',')
            for l in all_links:
                this_l = l.split(';')
                if this_l[1].find("next") != -1:
                    next_url = this_l[0]
                    next_url = next_url[1:-1]
                    break
        return next_url

    @classmethod
    def get_with_pagination(cls, url):
        tk = cls.get_context()["access_token"]
        headers = {"Authorization": tk}
        all_data = []

        print("Headers = ", headers)

        next_url = url
        while next_url is not None:
            result = requests.get(url=next_url, headers=headers)
            if result.status_code == 200:
                dd = result.json()
                if type(dd) == list:
                    all_data.extend(dd)
                else:
                    all_data.append(dd)
                links = result.headers.get("Link")
                next_url = cls.get_next_url(links)
            else:
                dd = None
                done = True
                next_url = None

        return all_data

    @classmethod
    def get_courses(cls, course_id=None, role=None):
        url = cls.get_context()["base_url"] + "/courses"
        if course_id is not None:
            url += "/" + str(course_id)

        if role is not None:
            url += "?enrollment_type=" + role

        result = cls.get_with_pagination(url)

        ret = result
        return ret

    @classmethod
    def get_students(cls, class_id, student_id=None):
        url = cls.get_context()["base_url"] + "/courses/" + str(class_id) + "/students"
        if student_id is not None:
            url += "/" + str(student_id)

        tk = cls._context["access_token"]
        headers = {"Authorization": tk}
        result = requests.get(url=url, headers=headers)

        if result.status_code == 200:
            dd = result.json()
        else:
            dd = None

        ret = (result.status_code, dd)
        return ret


