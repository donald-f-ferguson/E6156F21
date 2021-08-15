import { TestBed } from '@angular/core/testing';

import { NavbarstateService } from './navbarstate.service';

describe('NavbarstateService', () => {
  let service: NavbarstateService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(NavbarstateService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
