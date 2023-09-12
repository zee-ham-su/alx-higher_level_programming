#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      this.width = 0;
      this.height = 0;
    }
  }

  print () {
    if (this.width === 0 || this.height === 0) {
      console.log('wrong dimensions. Cannot print.');
    } else {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += 'X';
        }
        console.log(row);
      }
    }
  }

  rotate () {
    if (this.width !== 0 && this.height !== 0) {
      [this.width, this.height] = [this.height, this.width];
    }
  }

  double () {
    if (this.width !== 0 && this.height !== 0) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;
