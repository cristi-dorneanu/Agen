import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';

@Component({
  selector: 'app-calculation-input',
  templateUrl: './calculation-input.component.html',
  styleUrls: []
})
export class CalculationInputComponent implements OnInit {
  form: FormGroup;

  filePath: String;

  constructor(private fb: FormBuilder) {
    this.form = fb.group({
      filename: ['', Validators.required],
      imageFile: null
    });
  }

  ngOnInit() {
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

}
