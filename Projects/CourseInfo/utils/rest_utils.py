import copy
from flask import request
import json
import logging
from datetime import datetime

logger = logging.getLogger()




class RESTContext:

    _default_limit = 10

    @classmethod
    def _de_array_args(cls, args):
        result = {}

        if args is not None:
            for k, v in args.items():
                if type(v) == list:
                    result[k] = ",".join(v)
                else:
                    result[k] = v

        return result

    def __init__(self, request_context, path_parameters=None):

        log_message = ""

        self.limit = RESTContext._default_limit

        self.path = request_context.path
        args = dict(request_context.args)

        args = self._de_array_args(args)
        self.path = request.path

        self.data = None
        self.headers = dict(request.headers)
        self.method = request.method
        self.host_url = request.host_url

        self.path_parameters = path_parameters

        try:
            self.data = request_context.get_json()
        except Exception as e:
            pass

        args, limit = self._get_and_remove_arg(args, "limit")
        self.limit = limit

        args, offset = self._get_and_remove_arg(args, "offset")
        self.offset = offset

        args, order_by = self._get_and_remove_arg(args, "order_by")
        self.order_by = order_by

        args, fields = self._get_and_remove_arg(args, "fields")
        self.fields = fields

        self.args = args

        try:
            if request.data is not None:
                data = request.json
            else:
                data = None
        except Exception as e:
            # This would fail the request in a more real solution.
            data = "You sent something but I could not get JSON out of it."

            log_message = str(datetime.now()) + ": Method " + self.method

        log_message += " received: \n" + json.dumps(str(self), indent=2)
        logger.debug(log_message)

    def to_json(self):

        result = {
            'path': self.path,
            "path_parameters": self.path_parameters,
            'args': self.args,
            'headers': self.headers,
            'limit': self.limit,
            'offset': self.offset,
            'method': self.method,
            'host_url': self.host_url,
            'order_by': self.order_by,
            'fields': self.fields,
            'data': self.data}

        return result

    def __str__(self):
        result = self.to_json()
        result = json.dumps(result, indent=2)
        return result


    @classmethod
    def _get_and_remove_arg(cls, args, arg_name):
        val = copy.copy(args.get(arg_name, None))
        if val is not None:
            del args[arg_name]

        return args, val





# 1. Extract the input information from the requests object.
# 2. Log the information
# 3. Return extracted information.
#



def log_response(method, status, data, txt):
    msg = {
        "method": method,
        "status": status,
        "txt": txt,
        "data": data
    }

    logger.debug(str(datetime.now()) + ": \n" + json.dumps(msg, indent=2, default=str))


def log_request(method_name, request_context):

    info = {
        "method_name": method_name,
        "request": request_context
    }
    msg = json.dumps(info, indent=2, default=str)

    logger.debug(str(datetime.now()) + ": \n" + msg)


def split_key_string(s):

    result = s.split("_")
    return result
