import { Injectable, OnInit, NgModule } from '@angular/core';

@Injectable({
  providedIn: 'root'
})

@NgModule({
  declarations: [ NavbarstateService ],
  exports:      [ GreetingComponent ]
})

export class NavbarstateService {

  private currentPage = 'Undefined';

  constructor() {
    console.log('navbarstate constructor being callled.');
    this.currentPage = 'Home';
  }

  setCurrentPage(pageName: string): void {
    this.currentPage = pageName;
  }
  getCurrentPage(): string {
    return this.currentPage;
  }

}
