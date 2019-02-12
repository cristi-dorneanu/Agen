import {Component, OnInit} from '@angular/core';
import {CalculationService} from '../service/calculation.service';
import {Calculation} from '../model/Calculation';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';

@Component({
  selector: 'app-calculation',
  templateUrl: './calculation.component.html',
  styleUrls: ['./calculation.component.scss']
})
export class CalculationComponent implements OnInit {
  public calculation = new Calculation();

  public form: FormGroup;

  public filePath: String;

  constructor(private calculationService: CalculationService, private fb: FormBuilder) {
    this.form = fb.group({
      filename: ['', Validators.required],
      imageFile: null
    });
  }

  addCalculation(): void {
    if (this.form != null && this.form.get('imageFile') != null
      && this.form.get('imageFile').value != null) {
      this.calculation = new Calculation();
      this.calculation.image = this.form.get('imageFile').value.value;
    }
    this.calculationService.postCalculation(this.calculation).subscribe(
      calculation => {
        this.calculation = calculation;
        this.retrieveCalculation(calculation);
      }, error => this.calculation.errorMessage = <any>error
    );
  }

  onFileChange(event) {
    const reader = new FileReader();
    if (event.target.files && event.target.files.length > 0) {
      const file = event.target.files[0];
      reader.readAsDataURL(file);
      reader.onload = (ev: any) => {
        this.form.get('imageFile').setValue({
          filename: file.name,
          filetype: file.type,
          value: reader.result.split(',')[1]
        });

        this.form.get('filename').setValue(file.name);

        this.filePath = ev.target.result;
      };
    }
  }

  retrieveCalculation(calculation: Calculation) {
    this.calculationService.getCalculation(calculation.id).subscribe(
      response => this.onResponse(response), error => this.calculation.errorMessage = <any>error
    );
  }

  onResponse(calculation: Calculation) {
    if (calculation.status === null || calculation.status === 'NOT_STARTED' || calculation.status === 'IN_PROGRESS') {
      setTimeout(() => {
        this.retrieveCalculation(calculation);
      }, 2000);
    } else if (calculation.status === 'ERROR') {
      this.calculation.errorMessage = 'An error occured; The image may have not been loaded or the image does not contain a face';
    } else {
      this.calculation = calculation;
      console.log(this.calculation);
    }
  }

  ngOnInit() {
  }

}
