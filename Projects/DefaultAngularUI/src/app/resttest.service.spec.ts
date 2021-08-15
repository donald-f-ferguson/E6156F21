import { TestBed } from '@angular/core/testing';

import { ResttestService } from './resttest.service';

describe('ResttestService', () => {
  let service: ResttestService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ResttestService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
