"""
Copyright @Donald F. Ferguson, 2021

This file is part of the application template for W4111, Section 002, Spring 21 HW assignments 3 and 4.

app.py is the 'main program.'

"""
import json

# DFF TODO -- Not critical for W4111, but should switch from print statements to logging framework.
from datetime import datetime
from flask_cors import CORS

#
# These packages provide functions for deliverying a web application using Flask.
# Students can look online for education resources.
#
from flask import Flask, Response, request

# rest_utils provides simplification and isolation for interacting with Flask APIs and object,
# specifically the request object.
import utils.rest_utils as rest_utils

#
# DFF TODO -- Importing the service classes in the main app.py is easy but not a best practice
# The class implements one of the resources this application exposes.
#

from Services.BussinessLogicServices.CourseService import CourseService
from Services.DataAccessServices.CourseWorksAdapter import Adapter

Adapter.set_context(
    {
        "base_url": "https://courseworks2.columbia.edu/api/v1",
        "access_token": "Bearer 1396~rfxFAeGSHHcYDWc9awIw1IQ5OJrgLyW9c832KzZXPPaUS9XRbCHtaoQXMOcZPZiQ"
    }
)


# DFF TODO - We should not hardcode this here, and we should do in a context/environment service.
# OK for W4111 - This is not a course on microservices and robust programming.
#

#
# Create the Flask application object.
app = Flask(__name__)
CORS(app)

_course_service = CourseService()


##################################################################################################################

# DFF TODO A real service would have more robust health check methods.
# This path simply echoes to check that the app is working.
# The path is /health and the only method is GETs
@app.route("/health", methods=["GET"])
def health_check():
    rsp_data = {"status": "healthy", "time": str(datetime.now())}
    rsp_str = json.dumps(rsp_data)
    rsp = Response(rsp_str, status=200, content_type="app/json")
    return rsp


# TODO Remove later. Solely for explanatory purposes.
# The method take any REST request, and produces a response indicating what
# the parameters, headers, etc. are. This is simply for education purposes.
#
@app.route("/api/demo/<parameter1>", methods=["GET", "POST", "PUT", "DELETE"])
@app.route("/api/demo/", methods=["GET", "POST", "PUT", "DELETE"])
def demo(parameter1=None):
    """
    Returns a JSON object containing a description of the received request.

    :param parameter1: The first path parameter.
    :return: JSON document containing information about the request.
    """

    # DFF TODO -- We should wrap with an exception pattern.
    #

    # Mostly for isolation. The rest of the method is isolated from the specifics of Flask.
    inputs = rest_utils.RESTContext(request, {"parameter1": parameter1})

    # DFF TODO -- We should replace with logging.
    r_json = inputs.to_json()
    msg = {
        "/demo received the following inputs": inputs.to_json()
    }
    print("/api/demo/<parameter> received/returned:\n", msg)

    rsp = Response(json.dumps(msg), status=200, content_type="application/json")
    return rsp


##################################################################################################################
# Actual routes begin here.
#

@app.route("/api/courseworks/", methods=["GET"])
def get_courses():
    # Mostly for isolation. The rest of the method is isolated from the specifics of Flask.
    #inputs = rest_utils.RESTContext(request, None)
    #result = CourseService.get_courses()
    #rsp = Response(json.dumps(result), status=200, content_type='application/json')
    #return rsp
    rsp = Response("NOT IMPLEMENTED", status=501, content_type="text/plain")
    return rsp


@app.route("/api/courses/<id>", methods=["GET"])
def get_courses_by_id(id):

    try:
        rsp = _course_service.get_course(id)
        if rsp is None or len(rsp) == 0:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")
        else:
            rsp = Response(json.dumps(rsp, default=str), status=200, content_type="application/json")
    except Exception as e:
        print("Exception = ", e)
        rsp = Response("SERVER ERROR", status=500, content_type="text/plain")

    return rsp


@app.route("/api/courses", methods=["GET"])
def get_course_by_query():

    try:
        x = _course_service.apply_map()
        rsp = _course_service.get_courses(request.args)
        if rsp is None or len(rsp) == 0:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")
        else:
            rsp = Response(json.dumps(rsp, default=str), status=200, content_type="application/json")
    except Exception as e:
        print("Exception = ", e)
        rsp = Response("SERVER ERROR", status=500, content_type="text/plain")

    return rsp




if __name__ == '__main__':
    #host, port = ctx.get_host_and_port()

    # DFF TODO We will handle host and SSL certs different in deployments.
    app.run(host="0.0.0.0", port=5001)
