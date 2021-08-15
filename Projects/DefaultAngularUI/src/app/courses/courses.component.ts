import { Component, OnInit } from '@angular/core';
import {NavbarComponent} from '../navbar/navbar.component';
import { Course } from '../courses';
import { CoursesService} from '../courses.service';

@Component({
  selector: 'app-courses',
  templateUrl: './courses.component.html',
  styleUrls: ['./courses.component.css']
})
export class CoursesComponent implements OnInit {

  public navBar: NavbarComponent;
  private coursesService: CoursesService;
  course: Course;
  courseId: string;

  constructor(navb: NavbarComponent,
              courseService: CoursesService) {
    console.log('NavBar = ' + navb);
    this.navBar = navb;
    this.coursesService = courseService;
    this.course = undefined;
    this.courseId = undefined;
  }

  ngOnInit(): void {
    // this.getCourseByID('11912');
  }


  setCourse(course: Course): void {
    console.log('Setting course to ' + JSON.stringify(course, null, 2));
    this.course = course;
    this.courseId = course.id.toString();
  }
  // @ts-ignore
  getCourseByID(courseID): void {
    // @ts-ignore
    this.coursesService.getCourseByID('11912')
        .subscribe(course => this.setCourse(course));
  }

}
