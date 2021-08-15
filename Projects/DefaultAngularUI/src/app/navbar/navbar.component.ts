import {Component, Injectable, OnInit} from '@angular/core';
import { NavbarstateService } from '../navbarstate.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})

@Injectable(
  {providedIn: 'root'}
)


export class NavbarComponent implements OnInit {

  currentPage: string;

  constructor(private nbService: NavbarstateService) {
    this.nbService = nbService;

    // this.currentPage = 'Home';
    console.log('NavBar Constructor being called.');
  }


  ngOnInit(): void {
    // this.currentPage = 'Home';
    // console.log('NavbarComponent: OnInit called.');
  }



  handleClick(id: string): void {
    // alert('handleClick ID = ' + id);
    alert('Setting page ID to ... ' + id);
    this.currentPage = id;
    this.nbService.setCurrentPage(id);
  }

  getClass(id: string): string {
    let result = null;

    // console.log('Get class for ... ' + id);
    // console.log('Current id = ' + this.currentPage);
    // console.log('Navbarstate services days ' + this.nbService.getCurrentPage());

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
