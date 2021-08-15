from abc import ABC, abstractmethod, abstractclassmethod


class BaseService(ABC):

    _public_field_list = None

    def __init__(self):
        pass

    @classmethod
    def _matches_template(cls, resource, template):

        result = True

        if template is not None and template != {}:
            for k,v in template.items():
                test_v = resource.get(k, None)
                if test_v is None or test_v != v:
                    result = False
                    break

        return result

    @classmethod
    def get_public_field_list(cls):
        cls._public_field_list

    @classmethod
    def apply_map(cls, row):
        return row

    @classmethod
    def project_row(cls, row, fields):

        project_fields = fields
        public_fields = cls._public_field_list

        if public_fields is None:
            final_field_list = None
        elif project_fields is None:
            final_field_list = public_fields
        else:
            final_field_list = set(project_fields).intersection(set(public_fields))

        result_row = cls.apply_map(row)
        result_row = {f:row.get(f, None) for f in final_field_list}


        return result_row




    @classmethod
    def apply_filter(cls, result_list, template=None, fields=None):

        if template is not None and template != {}:
            result = []
            for r in result_list:
                if cls._matches_template(r, template):
                    result.append(r)
        else:
            result = result_list

        final_result = []

        for r in result:
            new_r = cls.project_row(r, fields=fields)
            final_result.append(new_r)

        return final_result
