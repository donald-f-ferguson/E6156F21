import { Injectable } from '@angular/core';
import { Course } from './courses';
import { Observable, of } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CoursesService {

  private courseUrl = 'http://0.0.0.0:5001/api/courses/';  // URL to web api

  constructor(
    private http: HttpClient) { }

  getCourseByID(courseId): Observable<Course> {
    const result = this.http.get<Course>(this.courseUrl + courseId);
    console.log('CourseService.getCourses');
    return result;
  }

}
