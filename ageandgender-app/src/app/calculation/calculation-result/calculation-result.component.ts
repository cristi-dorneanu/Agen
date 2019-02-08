import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {Calculation} from '../../model/Calculation';
import {CalculationService} from '../../service/calculation.service';
import {Observable} from 'rxjs/index';

@Component({
  selector: 'app-calculation-result',
  templateUrl: './calculation-result.component.html',
  styleUrls: ['calculation-result.component.scss']
})
export class CalculationResultComponent implements OnInit {
  public calculation = new Calculation();

  private eventsCalculation: any;

  @Input() events: Observable<Calculation>;

  public errorMessage: string;

  constructor(private _calculationService: CalculationService) { }

  retrieveCalculation(calculation: Calculation) {
    this._calculationService.getCalculation(calculation.id).subscribe(
      response => this.onResponse(response), error => this.errorMessage = <any>error
    );
  }

  onResponse(calculation: Calculation) {
    if (calculation.status === null || calculation.status === 'NOT_STARTED' || calculation.status === 'IN_PROGRESS') {
      setTimeout(() => {
        this.retrieveCalculation(calculation);
      }, 2000);
    } else if (calculation.status === 'ERROR') {
      this.errorMessage = 'An error occured; The image may have not been loaded';
    } else {
      this.calculation = calculation;
      console.log(this.calculation);
    }
  }

  ngOnInit() {
    this.eventsCalculation = this.events.subscribe(calculation => this.retrieveCalculation(calculation));
  }

}
