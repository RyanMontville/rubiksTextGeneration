import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Calculate } from '../functions/calculate';
import { Letters } from '../functions/letters';
import { MosaicCanvasComponent } from "../mosaic-canvas/mosaic-canvas.component";

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [FormsModule, CommonModule, MosaicCanvasComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  COLORS: [number, number, number][] = [[255, 0, 0], [255, 165, 0], [255, 255, 0], [50, 205, 50], [0, 0, 255], [255, 255, 255]]

  mosaicText: string = "";
  showStep: number = 1;
  verticalAlignment: string = "top";
  minWidth: number = 0;
  minHeight: number = 0;
  mosaicWidth: number = 0;
  mosaicHeight: number = 0;
  mosaicBackgroundColor: number = 0;
  mosaicTextColor: number = 0;
  errorMesage: string = "";
  mosaicLines: [string, number][] = []; //[Line Text, Height of Line]
  mosaicLineWithSpacing: [string, number, number][] = []; //[Line Text, Number of pieces before text to center it, height of Line]
  loading: boolean = false;
  showImage: boolean = false;

  calulator: Calculate = new Calculate();
  letters: Letters = new Letters();

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
        this.showStep = 2;
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
          this.showStep = 4;
          this.mosaicLineWithSpacing = this.calulator.caculateLineSpacings(this.mosaicLines, (this.mosaicWidth * 3));
        }
        break;
      }
      case 3: {
        this.mosaicText = "";
        this.showStep = 1;
        this.minWidth = 0;
        this.minHeight = 0;
        this.mosaicWidth = 0;
        this.mosaicHeight = 0;
        this.mosaicBackgroundColor = 0;
        this.mosaicTextColor = 0;
        this.errorMesage = "";
        this.mosaicLines = [];
        this.mosaicLineWithSpacing = [];
        this.loading = false;
        this.showImage =false;
      }
    }
    this.loading = false;
  }

  setVerticalAlign(alignment: string) {
    this.verticalAlignment = alignment;
    this.showStep = 3;
  }

  setColor(background: boolean, color: number) {
    this.errorMesage = "";
    if (background) {
      this.mosaicBackgroundColor = color;
      this.showStep = 5;

    } else {
      if (color === this.mosaicBackgroundColor) {
        this.errorMesage = "Error, text color cannot be the same as background color"
      } else {
        this.mosaicTextColor = color;
        this.showStep = 6;
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

  generateImage() {
    let pixelsToPlace: [number, number][] = [];
    let currentY: number = this.calulator.verticallyAlignText(this.mosaicLines, this.verticalAlignment, this.mosaicHeight);
    if (this.mosaicLineWithSpacing[0][2] === 6) {
      currentY = 2;
    }
    this.mosaicLineWithSpacing.forEach((line) => {
      //[Line Text, Number of pieces before text to center it, height of Line]
      let currentX: number = line[1];
      let characters: string[] = line[0].split("");
      characters.forEach((character) => {
        pixelsToPlace.push(...this.letters.drawCharacter(character, currentX, currentY));
        currentX += this.calulator.calculateWidthOfCharacter(character);
        if(currentX < this.mosaicWidth * 3) {
          currentX += 1;
        }
      });
      currentY += line[2] + 1;
    });
    this.showStep = 0;
    this.showImage = true;
    return pixelsToPlace;
  }

  mosaicCanvasReset() {
    this.onSubmit(3);
  }
}
