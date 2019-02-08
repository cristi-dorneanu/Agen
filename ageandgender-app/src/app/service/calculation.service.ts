import {HttpClient} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {from, Observable, range, timer, zip} from 'rxjs/index';
import {Calculation} from '../model/Calculation';
import {catchError, concatMap, filter, map, mergeMap, retryWhen, take} from 'rxjs/internal/operators';

@Injectable()
export class CalculationService {
  private _calculationUrl = 'http://localhost:8080/calculate/';


  constructor(private _http: HttpClient) {
  }

  getCalculation(id): Observable<Calculation> {
    return this._http.get<Calculation>(this._calculationUrl + id);
  }

  postCalculation(calculation: Calculation): Observable<Calculation> {
    return this._http.post<Calculation>(this._calculationUrl, calculation);
  }


}
