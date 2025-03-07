export class Calculate {
    calculateWidthOfCharacter(character: string) {
        switch (character) {
            case "a":
            case "b":
            case "c":
            case "d":
            case "e":
            case "f":
            case "g":
            case "h":
            case "i":
            case "k":
            case "l":
            case "o":
            case "p":
            case "r":
            case "s":
            case "t":
            case "u":
            case "v":
            case "y":
            case "1":
            case "2":
            case "3":
            case "4":
            case "5":
            case "6":
            case "7":
            case "8":
            case "9":
            case "0":
            case "?": {
                return 3;
            }
            case "j":
            case "n": {
                return 4;
            }
            case "m":
            case "w":
            case "x":
            case "#":
            case "q": {
                return 5;
            }
            case "!":
            case "'": {
                return 1;
            }
            default: {
                return 0;
            }
        }
    }

    calculateWidthOfWord(word: string) {
        let widthOfWord = 0;
        let letters: string[] = word.split("")
        letters.forEach((letter) => {
            widthOfWord += this.calculateWidthOfCharacter(letter);
        });
        widthOfWord += letters.length - 1;
        return widthOfWord
    }

    makeLine(mosaicText: string, widthOfMosaic: number): [string, string, number] {
        let words: string[] = mosaicText.split(" ");
        let piecesLeftInLine: number = widthOfMosaic;
        let singleLine: string[] = [];
        let loopCount: number = 0
        while (piecesLeftInLine > 0 && words.length > 0) {
            loopCount += 1;
            if (loopCount > 3) {
                break;
            }
            let wordLength: number = this.calculateWidthOfWord(words[0]);
            if (singleLine.length > 1) {
                if (wordLength <= piecesLeftInLine - 2) {
                    singleLine.push(words[0]);
                    piecesLeftInLine -= wordLength - 2;
                    words.splice(0, 1);
                } else {
                    break;
                }
            } else {
                if (wordLength <= piecesLeftInLine) {
                    singleLine.push(words[0]);
                    piecesLeftInLine -= wordLength;
                    words.splice(0, 1);
                } else {
                    break;
                }
            }
        }
        //join arrays
        let lineFinal = singleLine.join(" ");
        let remainingText = words.join(" ");
        if (lineFinal.includes("?")) {
            return [lineFinal, remainingText, 6];
        } else if (lineFinal.includes("'")) {
            return [lineFinal, remainingText, 6];
        } else {
            return [lineFinal, remainingText, 5];
        }
    }

    makeAllLines(mosaicText: string, widthOfLine: number) {
        let lines: [string, number][] = [];
        let remainingText: string = mosaicText;
        while (remainingText.length > 0) {
            let result: [string, string, number] = this.makeLine(remainingText, widthOfLine);
            let newLine: [string, number] = [result[0], result[2]];
            lines.push(newLine);
            remainingText = result[1];
        }
        return lines;
    }

    calculateMinimumSize(mosaicText: string): [[string, number][], number, number] {
        let minWidth: number = 0;
        let words = mosaicText.split(" ");
        words.forEach((word) => {
            let wordLength = this.calculateWidthOfWord(word);
            if (wordLength > minWidth) {
                minWidth = wordLength;
            }
        });
        let minHeight: number = 0;
        let lines: [string, number][] = this.makeAllLines(mosaicText, minWidth);
        lines.forEach((line) => {
            minHeight += line[1];
        });
        minHeight += lines.length;
        let minCubesWide: number = Math.ceil(minWidth / 3);
        let minCubesTall: number = Math.ceil(minHeight / 3);

        return [lines, minCubesWide, minCubesTall];
    }

    centertext(lineText: string, lineWidth: number) {
        let widthOfText: number = 0;
        let words: string[] = lineText.split(" ");
        let numberOfSpaces: number = words.length - 1;
        words.forEach((word) => {
            widthOfText += this.calculateWidthOfWord(word);
        });
        widthOfText += (numberOfSpaces * 2);
        let piecesBeforeText = Math.floor((lineWidth - widthOfText) / 2);
        if (piecesBeforeText < 0) {
            return 0;
        } else {
            return piecesBeforeText;
        }
    }

    caculateLineSpacings(lines: [string, number][], mosaicWidth: number) {
        let lineSpacings: [string, number, number][] = [];
        lines.forEach((line) => {
            let piecesBeforeText = this.centertext(line[0], mosaicWidth);
            lineSpacings.push([line[0], piecesBeforeText, line[1]]);
        });
        return lineSpacings;
    }
}