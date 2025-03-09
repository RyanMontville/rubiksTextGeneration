export class Letters {
    drawA(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 3], [currentX, currentY + 4], [currentX + 1, currentY],
        [currentX + 1, currentY + 2], [currentX + 2, currentY], [currentX + 2, currentY + 1],
        [currentX + 2, currentY + 2], [currentX + 2, currentY + 3], [currentX + 2, currentY + 4]];
    }
    drawB(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 3], [currentX, currentY + 4], [currentX + 1, currentY],
        [currentX + 1, currentY + 2], [currentX + 1, currentY + 4], [currentX + 2, currentY + 1],
        [currentX + 2, currentY + 3]];
    }
    drawC(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 3], [currentX, currentY + 4], [currentX + 1, currentY],
        [currentX + 1, currentY + 4], [currentX + 2, currentY], [currentX + 2, currentY + 4]];
    }
    drawD(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 3], [currentX, currentY + 4], [currentX + 1, currentY],
        [currentX + 1, currentY + 4], [currentX + 2, currentY + 1], [currentX + 2, currentY + 2],
        [currentX + 2, currentY + 3]];
    }
    drawE(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 3], [currentX, currentY + 4], [currentX + 1, currentY],
        [currentX + 1, currentY + 2], [currentX + 1, currentY + 4], [currentX + 2, currentY],
        [currentX + 2, currentY + 4]];
    }
    drawF(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 3], [currentX, currentY + 4], [currentX + 1, currentY],
        [currentX + 1, currentY + 2]];
    }
    drawG(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 3], [currentX, currentY + 4], [currentX + 1, currentY],
        [currentX + 1, currentY + 4], [currentX + 2, currentY], [currentX + 2, currentY + 3],
        [currentX + 2, currentY + 4]];
    }
    drawH(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 3], [currentX, currentY + 4], [currentX + 1, currentY + 2],
        [currentX + 2, currentY], [currentX + 2, currentY + 1], [currentX + 2, currentY + 2],
        [currentX + 2, currentY + 3], [currentX + 2, currentY + 4]];
    }
    drawI(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 4], [currentX + 1, currentY],
        [currentX + 1, currentY + 1], [currentX + 1, currentY + 2], [currentX + 1, currentY + 3],
        [currentX + 1, currentY + 4], [currentX + 2, currentY], [currentX + 2, currentY + 4]];
    }
    drawJ(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 3], [currentX, currentY + 4],
        [currentX + 1, currentY], [currentX + 1, currentY + 4], [currentX + 2, currentY],
        [currentX + 2, currentY + 1], [currentX + 2, currentY + 2], [currentX + 2, currentY + 3],
        [currentX + 2, currentY + 4], [currentX + 3, currentY]];
    }
    drawK(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 3], [currentX, currentY + 4], [currentX + 1, currentY + 2],
        [currentX + 2, currentY], [currentX + 2, currentY + 1], [currentX + 2, currentY + 3],
        [currentX + 2, currentY + 4]];
    }
    drawL(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 3], [currentX, currentY + 4], [currentX + 1, currentY + 4],
        [currentX + 2, currentY + 4]];
    }
    drawM(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 3], [currentX, currentY + 4], [currentX + 1, currentY + 1],
        [currentX + 2, currentY + 2], [currentX + 3, currentY + 1], [currentX + 4, currentY],
        [currentX + 4, currentY + 1], [currentX + 4, currentY + 2], [currentX + 4, currentY + 3],
        [currentX + 4, currentY + 4]];
    }
    drawN(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 3], [currentX, currentY + 4], [currentX + 1, currentY + 1],
        [currentX + 2, currentY + 2], [currentX + 3, currentY], [currentX + 3, currentY + 1],
        [currentX + 3, currentY + 2], [currentX + 3, currentY + 3], [currentX + 3, currentY + 4]];
    }
    drawO(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 3], [currentX, currentY + 4], [currentX + 1, currentY],
        [currentX + 1, currentY + 4], [currentX + 2, currentY], [currentX + 2, currentY + 1],
        [currentX + 2, currentY + 2], [currentX + 2, currentY + 3], [currentX + 2, currentY + 4]];
    }
    drawP(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 3], [currentX, currentY + 4], [currentX + 1, currentY],
        [currentX + 1, currentY + 2], [currentX + 2, currentY], [currentX + 2, currentY + 1],
        [currentX + 2, currentY + 2]];
    }
    drawQ(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 3], [currentX, currentY + 4], [currentX + 1, currentY],
        [currentX + 1, currentY + 4], [currentX + 2, currentY], [currentX + 2, currentY + 1],
        [currentX + 2, currentY + 2], [currentX + 2, currentY + 3], [currentX + 2, currentY + 4],
        [currentX + 3, currentY + 4]];
    }
    drawR(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 3], [currentX, currentY + 4], [currentX + 1, currentY],
        [currentX + 1, currentY + 2], [currentX + 2, currentY], [currentX + 2, currentY + 1],
        [currentX + 2, currentY + 3], [currentX + 2, currentY + 4]];
    }
    drawS(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 4], [currentX + 1, currentY], [currentX + 1, currentY + 2],
        [currentX + 1, currentY + 4], [currentX + 2, currentY], [currentX + 2, currentY + 2],
        [currentX + 2, currentY + 3], [currentX + 2, currentY + 4]];
    }
    drawT(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX + 1, currentY], [currentX + 1, currentY + 1],
        [currentX + 1, currentY + 2], [currentX + 1, currentY + 3], [currentX + 1, currentY + 4],
        [currentX + 2, currentY]];
    }
    drawU(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 3], [currentX, currentY + 4], [currentX + 1, currentY + 4],
        [currentX + 2, currentY], [currentX + 2, currentY + 1], [currentX + 2, currentY + 2],
        [currentX + 2, currentY + 3], [currentX + 2, currentY + 4]];
    }
    drawV(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 3], [currentX + 1, currentY + 4], [currentX + 2, currentY],
        [currentX + 2, currentY + 1], [currentX + 2, currentY + 2], [currentX + 2, currentY + 3]];
    }
    drawW(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 3], [currentX, currentY + 4], [currentX + 1, currentY + 4],
        [currentX + 2, currentY + 3], [currentX + 3, currentY + 4], [currentX + 4, currentY],
        [currentX + 4, currentY + 1], [currentX + 4, currentY + 2], [currentX + 4, currentY + 3],
        [currentX + 4, currentY + 4]];
    }
    drawX(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 4], [currentX + 1, currentY + 1],
        [currentX + 1, currentY + 3], [currentX + 2, currentY + 2], [currentX + 3, currentY + 1],
        [currentX + 3, currentY + 3], [currentX + 4, currentY], [currentX + 4, currentY + 4]];
    }
    drawY(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX + 1, currentY + 2], [currentX + 1, currentY + 3], [currentX + 1, currentY + 4],
        [currentX + 2, currentY], [currentX + 2, currentY + 1], [currentX + 2, currentY + 2]];
    }
    drawZ(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 4],
        [currentX + 1, currentY], [currentX + 1, currentY + 2], [currentX + 1, currentY + 4],
        [currentX + 2, currentY], [currentX + 2, currentY + 3], [currentX + 2, currentY + 4]];
    }
    drawZero(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 3], [currentX, currentY + 4], [currentX + 1, currentY],
        [currentX + 1, currentY + 4], [currentX + 2, currentY], [currentX + 2, currentY + 1],
        [currentX + 2, currentY + 2], [currentX + 2, currentY + 3], [currentX + 2, currentY + 4]];
    }
    drawOne(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY + 1], [currentX, currentY + 4], [currentX + 1, currentY],
        [currentX + 1, currentY + 1], [currentX + 1, currentY + 2], [currentX + 1, currentY + 3],
        [currentX + 1, currentY + 4], [currentX + 2, currentY + 4]];
    }
    drawTwo(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 2], [currentX, currentY + 3],
        [currentX, currentY + 4], [currentX + 1, currentY], [currentX + 1, currentY + 2],
        [currentX + 1, currentY + 4], [currentX + 2, currentY], [currentX + 2, currentY + 1],
        [currentX + 2, currentY + 2], [currentX + 2, currentY + 4]];
    }
    drawThree(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 2], [currentX, currentY + 4],
        [currentX + 1, currentY], [currentX + 1, currentY + 2], [currentX + 1, currentY + 4],
        [currentX + 2, currentY], [currentX + 2, currentY + 1], [currentX + 2, currentY + 2],
        [currentX + 2, currentY + 3], [currentX + 2, currentY + 4]];
    }
    drawFour(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX + 1, currentY + 2], [currentX + 2, currentY], [currentX + 2, currentY + 1],
        [currentX + 2, currentY + 2], [currentX + 2, currentY + 3], [currentX + 2, currentY + 4]];
    }
    drawFive(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 4], [currentX + 1, currentY], [currentX + 1, currentY + 2],
        [currentX + 1, currentY + 4], [currentX + 2, currentY], [currentX + 2, currentY + 2],
        [currentX + 2, currentY + 3], [currentX + 2, currentY + 4]];
    }
    drawSix(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1],
        [currentX, currentY + 2], [currentX, currentY + 3], [currentX, currentY + 4],
        [currentX + 1, currentY], [currentX + 1, currentY + 2], [currentX + 1, currentY + 4],
        [currentX + 2, currentY], [currentX + 2, currentY + 2], [currentX + 2, currentY + 3],
        [currentX + 2, currentY + 4]];
    }
    drawSeven(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX + 1, currentY], [currentX + 2, currentY],
        [currentX + 2, currentY + 1], [currentX + 2, currentY + 2], [currentX + 2, currentY + 3],
        [currentX + 2, currentY + 4]];
    }
    drawEight(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 3], [currentX, currentY + 4], [currentX + 1, currentY],
        [currentX + 1, currentY + 2], [currentX + 1, currentY + 4], [currentX + 2, currentY],
        [currentX + 2, currentY + 1], [currentX + 2, currentY + 2], [currentX + 2, currentY + 3],
        [currentX + 2, currentY + 4]];
    }
    drawNine(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX + 1, currentY], [currentX + 1, currentY + 2], [currentX + 2, currentY],
        [currentX + 2, currentY + 1], [currentX + 2, currentY + 2], [currentX + 2, currentY + 3],
        [currentX + 2, currentY + 4]];
    }
    drawPound(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY + 1], [currentX, currentY + 3], [currentX + 1, currentY],
        [currentX + 1, currentY + 1], [currentX + 1, currentY + 2], [currentX + 1, currentY + 3],
        [currentX + 1, currentY + 4], [currentX + 2, currentY + 1], [currentX + 2, currentY + 3],
        [currentX + 3, currentY], [currentX + 3, currentY + 1], [currentX + 3, currentY + 2],
        [currentX + 3, currentY + 3], [currentX + 3, currentY + 4], [currentX + 4, currentY + 1],
        [currentX + 4, currentY + 3]];
    }
    drawExclamation(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX, currentY + 1], [currentX, currentY + 2],
        [currentX, currentY + 4]];
    }
    drawQuestion(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY], [currentX + 1, currentY - 1],
        [currentX + 1, currentY + 2], [currentX + 1, currentY + 4],
        [currentX + 2, currentY], [currentX + 2, currentY + 1]];
    }
    drawApostrophe(currentX: number, currentY: number): [number, number][] {
        return [[currentX, currentY - 1], [currentX, currentY]];
    }

    drawCharacter(characterToDraw: string, currentX: number, currentY: number) {
        switch(characterToDraw) {
        case "a":
            {return this.drawA(currentX, currentY)}
        case "b":
            {return this.drawB(currentX, currentY)}
        case "c":
            {return this.drawC(currentX, currentY)}
        case "d":
            {return this.drawD(currentX, currentY)}
        case "e":
            {return this.drawE(currentX, currentY)}
        case "f":
            {return this.drawF(currentX, currentY)}
        case "g":
            {return this.drawG(currentX, currentY)}
        case "h":
            {return this.drawH(currentX, currentY)}
        case "i":
            {return this.drawI(currentX, currentY)}
        case "j":
            {return this.drawJ(currentX, currentY)}
        case "k":
            {return this.drawK(currentX, currentY)}
        case "l":
            {return this.drawL(currentX, currentY)}
        case "m":
            {return this.drawM(currentX, currentY)}
        case "n":
            {return this.drawN(currentX, currentY)}
        case "o":
            {return this.drawO(currentX, currentY)}
        case "p":
            {return this.drawP(currentX, currentY)}
        case "q":
            {return this.drawQ(currentX, currentY)}
        case "r":
            {return this.drawR(currentX, currentY)}
        case "s":
            {return this.drawS(currentX, currentY)}
        case "t":
            {return this.drawT(currentX, currentY)}
        case "u":
            {return this.drawU(currentX, currentY)}
        case "v":
            {return this.drawV(currentX, currentY)}
        case "w":
            {return this.drawW(currentX, currentY)}
        case "x":
            {return this.drawX(currentX, currentY)}
        case "y":
            {return this.drawY(currentX, currentY)}
        case "z":
            {return this.drawZ(currentX, currentY)}
        case "0":
            {return this.drawZero(currentX, currentY)}
        case "1":
            {return this.drawOne(currentX, currentY)}
        case "2":
            {return this.drawTwo(currentX, currentY)}
        case "3":
            {return this.drawThree(currentX, currentY)}
        case "4":
            {return this.drawFour(currentX, currentY)}
        case "5":
            {return this.drawFive(currentX, currentY)}
        case "6":
            {return this.drawSix(currentX, currentY)}
        case "7":
            {return this.drawSeven(currentX, currentY)}
        case "8":
            {return this.drawEight(currentX, currentY)}
        case "9":
            {return this.drawNine(currentX, currentY)}
        case "?":
            {return this.drawQuestion(currentX, currentY)}
        case "'":
            {return this.drawApostrophe(currentX, currentY)}
        case "!":
            {return this.drawExclamation(currentX, currentY)}
        case "#":
            {return this.drawPound(currentX, currentY)}
        default:
            {return []}
        }
    }
}