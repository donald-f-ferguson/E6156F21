import {Component, Injectable, OnInit} from '@angular/core';
import {NavbarstateService} from '../navbarstate.service';
// import {NavbarComponent} from '../navbar/navbar.component';
import {LoginStateService} from '../login-state.service';

@Component({
  selector: 'app-people',
  templateUrl: './people.component.html',
  styleUrls: ['./people.component.css']
})

@Injectable(
  {providedIn: 'root'}
)

export class PeopleComponent implements OnInit {

  aPerson = 'A Person';
  currentPage: string;
  loginStatus = undefined;

  // navBar: NavbarComponent;

  constructor(// navb: NavbarComponent,
              loginStatus: LoginStateService) {
    // this.navBar = navb;
    this.loginStatus = loginStatus;
  }

  ngOnInit(): void {
    this.currentPage = 'People';
  }

  getClass(id: string): string {
    let result = null;

    // console.log('id = ' + id);
    if (id === this.currentPage) {
      result = 'nav-item active';
    }
    else {
      result = 'nav-item';
    }

    // console.log('currentPage = ' + this.currentPage + ', id = ' + id + ', result = ' + result);
    return result;
  }

  isLoggedin(): boolean {
    return this.loginStatus.getLoginStatus();
  }

}
