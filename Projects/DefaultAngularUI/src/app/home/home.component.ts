import {Component, Injectable, OnInit} from '@angular/core';

import { NavbarComponent } from '../navbar/navbar.component';
import { LoginStateService } from '../login-state.service';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {GoogleLoginProvider, SocialAuthService, SocialUser} from 'angularx-social-login';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

@Injectable(
  {providedIn: 'root'}
)

export class HomeComponent implements OnInit {

  currentPage: string;
  navBar: NavbarComponent;
  loginStatus: LoginStateService;

  loginForm: FormGroup;
  socialUser: SocialUser;


  constructor(
    navb: NavbarComponent,
    loginStatus: LoginStateService,
    private formBuilder: FormBuilder,
    private socialAuthService: SocialAuthService
  ) {
    this.navBar = navb;
    this.loginStatus = loginStatus;
    // this.navModule = navm;

    // console.log('navm = ' + navm);
  }

  ngOnInit(): void {
    this.loginForm = this.formBuilder.group({
      email: ['', Validators.required],
      password: ['', Validators.required]
    });

    this.socialAuthService.authState.subscribe((user) => {
      this.socialUser = user;
      console.log('Setting social user = ' + JSON.stringify(user));
      this.loginStatus.setLoginStatus(true);
      console.log(this.socialUser);
    });
  }

  isLoggedin(): boolean {
    return this.loginStatus.getLoginStatus();
  }

  loginWithGoogle(): void {
    this.socialAuthService.signIn(GoogleLoginProvider.PROVIDER_ID);
  }

  logOut(): void {
    this.socialAuthService.signOut();
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

}
