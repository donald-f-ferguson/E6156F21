import { Injectable } from '@angular/core';
import {stringify} from 'querystring';

@Injectable({
  providedIn: 'root'
})
export class LoginStateService {

  loginStatus: boolean;

  constructor() {
    // console.log('Setting the login status to false!');
    this.loginStatus = false;
  }
  getLoginStatus(): boolean {
    const lState = sessionStorage.getItem('loginStatus');
    // console.log('Login status = ' + JSON.stringify(lState, null, 2));
    if (lState === 'true') {
      // console.log('Returning the login status = true');
      return true;
    }
    else {
      // console.log('Returning the login status = false');
      return false;
    }
  }
  setLoginStatus(s: boolean): void{
    // console.log('Setting the login status to ' + s);
    this.loginStatus = s;
    sessionStorage.setItem('loginStatus', stringify(s));
  }
}
