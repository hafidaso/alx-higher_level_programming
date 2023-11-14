#!/usr/bin/node

class Rectangle {
    constructor(w, h) {
        if (w > 0 && h > 0) {
            this.width = w;
            this.height = h;
        }
        // If w or h is 0 or negative, no attributes are set, resulting in an empty object.
    }
}

module.exports = Rectangle;
