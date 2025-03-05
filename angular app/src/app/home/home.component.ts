import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  mosaicText: string = "";
  showStepOneInput: boolean = true;
  showStepTwo: boolean = false;
  showStepTwoInput: boolean = true;
  minWidth: number = 2;
  minHeight: number = 2;
  mosaicWidth: number = 0;
  mosaicHeight: number = 0;
  showStepThree: boolean = false;
  showStepFour: boolean = false;

  onSubmit(step: number) {
    switch(step) {
      case 1: {
        this.showStepOneInput = false;
        this.showStepTwo = true;
        break;
      }
      case 2: {
        this.showStepTwoInput = false;
        this.showStepThree = true;
        break;
      }
    }
  }
}
