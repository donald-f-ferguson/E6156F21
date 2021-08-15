import json
import Services.BussinessLogicServices.CourseService as c_svc
import csv

context = {
    "base_url":  "https://courseworks2.columbia.edu/api/v1",
    "access_token": "Bearer 1396~rfxFAeGSHHcYDWc9awIw1IQ5OJrgLyW9c832KzZXPPaUS9XRbCHtaoQXMOcZPZiQ"
}

cw_context = context

def t1():
    c_svc.CourseService.set_context(context)
    res = c_svc.CourseService.get_courses()

    if res is not None:
        print("Courses = ")
        for c in res:
            print(json.dumps(c, indent=2))
    else:
        print("Nothing")

def t2():
    c_svc.CourseService.set_context(context)
    res = c_svc.CourseService.get_course(59653)

    if res is not None:
        print("Courses = ")
        print(json.dumps(res.to_json(), indent=2))
    else:
        print("Nothing")

def t3():
    c_svc.CourseService.set_context(context)
    c = c_svc.CourseService.get_course(59653)
    res = c.get_students()

    if res is not None:
        print("Students = ")
        for s in res:
            print(json.dumps(s.to_json(), indent=2))
    else:
        print("Nothing")

def t4():
    c_svc.CourseService.set_context(context)
    ccs  = c_svc.CourseService.get_courses(role='teacher')
    d_svc.set_context(context)

    if ccs is not None:
        print("Saving courses = ")
        for c in ccs:
            d_svc.create_course(c)
    else:
        print("Nothing")

def t5():

    d_svc.set_context(context)
    ids = d_svc.get_course_ids()
    print("IDs = ", ids)

def t6():
    c_svc.CourseService.set_context(context)
    d_svc.set_context(context)

    ids = d_svc.get_course_ids()

    for v in ids:
        i = v['id']
        c = c_svc.CourseService.get_course(i)
        res = c.get_students()

        if res is not None:
            print("Students = ")
            for s in res:
                print(json.dumps(s.to_json(), indent=2))
        else:
            print("Nothing")


def t7():
    c_svc.CourseService.set_context(context)
    d_svc.set_context(context)

    ids = d_svc.get_course_ids()

    for v in ids:
        i = v['id']
        c = c_svc.CourseService.get_course(i)
        res = c.get_students()

        if res is not None:
            for s in res:
                ln = s.name['last_name']
                if ln != 'Student':
                    d_svc.add_student_course(i, s)
        else:
            print("Nothing")


def t8():
    c_svc.CourseService.set_context(context)
    d_svc.set_context(context)

    c = c_svc.CourseService.get_course(87722)
    res = c.get_students()

    if res is not None:
        for s in res:
            ln = s.name['last_name']
            if ln != 'Student':
                print(s.to_json())
    else:
        print("Nothing")


def t9():
    c_svc.CourseService.set_context(context)
    #d_svc.set_context(context)

    c = c_svc.CourseService.get_courses()

    print(json.dumps(c, indent=2, default=str))

    f = "../data/course_info.csv"
    with open(f, "w") as out_file:
        f_names = c[0].keys()
        c_writer = csv.DictWriter(out_file, fieldnames=f_names)
        c_writer.writeheader()

        for x in c:
            c_writer.writerow(x)

#t1()
#t2()
#t3()
#t4()
#t5()
#t6()
#t7()
#t8()
t9()