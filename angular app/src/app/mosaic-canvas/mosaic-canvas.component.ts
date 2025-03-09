import { AfterViewInit, Component, Input, ViewChild, ElementRef } from '@angular/core';

@Component({
  selector: 'app-mosaic-canvas',
  standalone: true,
  imports: [],
  templateUrl: './mosaic-canvas.component.html',
  styleUrl: './mosaic-canvas.component.css'
})
export class MosaicCanvasComponent implements AfterViewInit {
  @ViewChild('pixelCanvas', { static: false }) pixelCanvas!: ElementRef<HTMLCanvasElement>;
  @Input() pixels: [number, number][] = [];
  @Input() imageWidth: number = 0;
  @Input() imageHeight: number = 0;
  @Input() textColor: string = "";
  @Input() backgroundColor: string = "";
  @Input() text: string = "";
  private ctx!: CanvasRenderingContext2D;
  private gridSize = 50; // Size of each grid cell (pixel)

  ngAfterViewInit(): void {
    this.ctx = this.pixelCanvas.nativeElement.getContext('2d')!;
    this.ctx.fillStyle = this.backgroundColor;
    this.ctx.fillRect(0, 0, this.imageWidth, this.imageHeight);
    this.pixels.forEach((pixel) => {
      this.drawPixel(pixel[0], pixel[1], this.textColor);
    });
    this.drawGrid();
  }

  drawGrid(): void {
    const canvas = this.pixelCanvas.nativeElement;
    const width = this.imageWidth;
    const height = this.imageHeight;

    this.ctx.strokeStyle = 'black';

    // Draw vertical lines
    for (let x = 0; x <= width; x += this.gridSize) {
      this.ctx.beginPath();
      this.ctx.moveTo(x, 0);
      this.ctx.lineTo(x, height);

      // Check if it's every third line
      if ((x / this.gridSize) % 3 === 0) {
        this.ctx.lineWidth = 2; // Twice as thick
      } else {
        this.ctx.lineWidth = 1; // Normal thickness
      }

      this.ctx.stroke();
    }

    // Draw horizontal lines
    for (let y = 0; y <= height; y += this.gridSize) {
      this.ctx.beginPath();
      this.ctx.moveTo(0, y);
      this.ctx.lineTo(width, y);

      // Check if it's every third line
      if ((y / this.gridSize) % 3 === 0) {
        this.ctx.lineWidth = 2; // Twice as thick
      } else {
        this.ctx.lineWidth = 1; // Normal thickness
      }

      this.ctx.stroke();
    }
  }

  drawPixel(x: number, y: number, color: string): void {
    this.ctx.fillStyle = color;
    this.ctx.fillRect(x * this.gridSize, y * this.gridSize, this.gridSize, this.gridSize);
  }

  downloadImage(): void {
    const canvas = this.pixelCanvas.nativeElement;
    const dataURL = canvas.toDataURL('image/png');
    const link = document.createElement('a');
    link.href = dataURL;
    link.download = `${this.text.replace(" ", "-")}-mosaic.png`
    link.click();
  }
}
