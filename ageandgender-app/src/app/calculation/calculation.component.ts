import {Component, OnInit, ViewChild} from '@angular/core';
import {CalculationService} from '../service/calculation.service';
import {Calculation} from '../model/Calculation';
import {Subject} from 'rxjs/index';
import {CalculationInputComponent} from './calculation-input/calculation-input.component';

@Component({
  selector: 'app-calculation',
  templateUrl: './calculation.component.html',
  styleUrls: ['./calculation.component.scss']
})
export class CalculationComponent implements OnInit {
  public calculation = new Calculation();

  public errorMessage: string;

  private eventsCalculation: Subject<Calculation> = new Subject<Calculation>();

  @ViewChild(CalculationInputComponent)
  private inputComponent: CalculationInputComponent;

  constructor(private calculationService: CalculationService) {
  }

  addCalculation(): void {
    if (this.inputComponent.form != null && this.inputComponent.form.get('imageFile') != null
      && this.inputComponent.form.get('imageFile').value != null) {
      this.calculation.image = this.inputComponent.form.get('imageFile').value.value;
    }
    this.calculationService.postCalculation(this.calculation).subscribe(
      calculation => {
        this.calculation = calculation;
        this.emitEventToChild(calculation);
      }, error => this.errorMessage = <any>error
    );
  }

  emitEventToChild(calculation) {
    this.eventsCalculation.next(calculation);
  }

  ngOnInit() {
  }

}
