import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Calculate } from '../functions/calculate';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  COLORS: [number, number, number][] = [[255, 0, 0], [255, 165, 0], [255, 255, 0], [50, 205, 50], [0, 0, 255], [255, 255, 255]]

  mosaicText: string = "";
  showStepOneInput: boolean = true;
  showStepTwo: boolean = false;
  showStepTwoInput: boolean = true;
  minWidth: number = 2;
  minHeight: number = 2;
  mosaicWidth: number = 0;
  mosaicHeight: number = 0;
  showStepThree: boolean = false;
  showStepThreeSelection: boolean = true;
  showStepFour: boolean = false;
  showStepFourSelection: boolean = true;
  mosaicBackgroundColor: number = 0;
  mosaicTextColor: number = 0;
  errorMesage: string = "";
  mosaicLines: [string, number][] = []; //[Line Text, Height of Line]
  mosaicLineWithSpacing: [string, number, number][] = []; //[Line Text, Number of pieces before text to center it, height of Line]
  loading: boolean = false;

  calulator: Calculate = new Calculate();

  onSubmit(step: number) {
    this.errorMesage = "";
    this.loading = true;
    switch (step) {
      case 1: {
        this.mosaicText = this.mosaicText.toLowerCase();
        let calcLines: [[string, number][], number, number] = this.calulator.calculateMinimumSize(this.mosaicText);
        this.mosaicLines = calcLines[0];
        this.minWidth = calcLines[1];
        this.minHeight = calcLines[2];
        this.showStepOneInput = false;
        this.showStepTwo = true;
        this.mosaicWidth = this.minWidth;
        this.mosaicHeight = this.minHeight;
        break;
      }
      case 2: {
        let goodDimensions: boolean = true;
        if (this.mosaicWidth < this.minWidth) {
          this.errorMesage = "Error, width cannot be less than minimum width.";
          goodDimensions = false;
        }
        if (this.mosaicHeight < this.minHeight) {
          this.errorMesage = "Error, height cannot be less than minimum height."
          goodDimensions = false;
        }
        if (goodDimensions) {
          this.showStepTwoInput = false;
          this.showStepThree = true;
          this.mosaicLineWithSpacing = this.calulator.caculateLineSpacings(this.mosaicLines, (this.mosaicWidth * 3));
        }
        break;
      }
    }
    this.loading = false;
  }

  setColor(background: boolean, color: number) {
    this.errorMesage = "";
    if (background) {
      this.mosaicBackgroundColor = color;
      this.showStepFour = true;
      this.showStepThreeSelection = false;

    } else {
      if (color === this.mosaicBackgroundColor) {
        this.errorMesage = "Error, text color cannot be the same as background color"
      } else {
        this.mosaicTextColor = color;
        this.showStepFourSelection = false;
      }
    }
  }

  convertRGBToName(color: number) {
    switch (color) {
      case 0: {
        return "red";
      }
      case 1: {
        return "orange";
      }
      case 2: {
        return "yellow"
      }
      case 3: {
        return "green";
      }
      case 4: {
        return "blue";
      }
      case 5: {
        return "white"
      }
      default: {
        return "Error";
      }
    }
  }

  getTextSampleImage() {
    switch (this.mosaicBackgroundColor) {
      case 0: {
        return "https://raw.githubusercontent.com/RyanMontville/rubiksTextGeneration/refs/heads/main/images/red-combos.png";
      }
      case 1: {
        return "https://raw.githubusercontent.com/RyanMontville/rubiksTextGeneration/refs/heads/main/images/orange-combos.png"
      }
      case 2: {
        return "https://raw.githubusercontent.com/RyanMontville/rubiksTextGeneration/refs/heads/main/images/yellow-combos.png"
      }
      case 3: {
        return "https://raw.githubusercontent.com/RyanMontville/rubiksTextGeneration/refs/heads/main/images/green-combos.png"
      }
      case 4: {
        return "https://raw.githubusercontent.com/RyanMontville/rubiksTextGeneration/refs/heads/main/images/blue-combos.png"
      }
      default: {
        return "https://raw.githubusercontent.com/RyanMontville/rubiksTextGeneration/refs/heads/main/images/white-combos.png"
      }
    }
  }
}
