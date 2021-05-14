/**
 * Draws a line from pointA to pointB on the canvas
 * with the Bresenham algorithm.
 * @param  {Uint8ClampedArray} data   - The linearised pixel array
 * @param  {[number, number]} pointA - The start point of the line
 * @param  {[number, number]} pointB - The end point of the line
 * @param  {number} width          - The width of the canvas
 * @param  {number} height         - The height of the canvas
 */
export function bresenham(data: Uint8ClampedArray, pointA: [number, number], pointB: [number, number], width: number, height: number) {

    // Point 1
    var p1x = Math.round(pointA[0])
    var p1y = Math.round(pointA[1])

    // Point 2
    var p2x = Math.round(pointB[0])
    var p2y = Math.round(pointB[1])

    // Making p1x always smaller than p2y
    if (p1x > p2x) {
        p1x = pointB[0]
        p1y = pointB[1]

        p2x = pointA[0]
        p2y = pointA[0]
    }

    var deltaX = p2x - p1x
    var deltaY = p2y - p1y


    // Slope of the line
    var m = (p2y - p1y) / (p2x - p1x)

    var t = (m * (0 - p1x)) + p1y


    var iterStart = p1x
    var iterEnd = p2x

    if (Math.abs(m) < 1) {
        // We will iterate from x1 to x2

        var constantPart = 2 * deltaY - deltaX + 2 * t * deltaX

        var last_y = p1y

        for (var x = p1x; x < p2x; x++) {
            var e = 2 * x * deltaY - 2 * last_y * deltaX + constantPart
            if (m > 0) {
                if (e <= 0) {
                    colorPixelBlack(data, x, last_y, width, height)
                } else {
                    colorPixelBlack(data, x, ++last_y, width, height)
                }
            } else {
                if (e > 0) {
                    colorPixelBlack(data, x, last_y, width, height)
                } else {
                    colorPixelBlack(data, x, --last_y, width, height)
                }
            }
        }
    } else {
        // We will iterate from y2 to y2

        var temp1 = p1x
        var temp2 = p1y

        p1x = p2y
        p1y = - p2x

        p2x = temp2
        p2y = - temp1

        var deltaX = p2x - p1x
        var deltaY = p2y - p1y

        // Slope of the line
        var m = (p2y - p1y) / (p2x - p1x)

        var t = (m * (0 - p1x)) + p1y


        var constantPart = 2 * deltaY - deltaX + 2 * t * deltaX

        var last_y = p1y

        for (var x = Math.min(p1x, p2x); x < Math.max(p1x, p2x); x++) {
            var e = 2 * x * deltaY - 2 * last_y * deltaX + constantPart
            if (m > 0) {
                if (e <= 0) {
                    colorPixelBlack(data, - last_y, x, width, height)
                } else {
                    colorPixelBlack(data, - (++last_y), x, width, height)
                }
            } else {
                if (e > 0) {
                    colorPixelBlack(data, - last_y, x, width, height)
                } else {
                    colorPixelBlack(data, - (--last_y), x, width, height)
                }
            }
        }
    }

    // Coloring start and end
    colorPixelBlack(data, p1x, p1y, width, height)
    colorPixelBlack(data, p2x, p2y, width, height)

    // // Getting t
    // var t = (m * (0 - p1x)) + p1y

    // // DeltaX and DeltaY
    // var deltaX = p2x - p1x
    // var deltaY = p2y - p1y

    // if (deltaX > 0) {

    //     if (0 < m && m < 1) {
    //         // Calculating teh constant Part
    //         var constantPart = 2 * deltaY - deltaX + 2 * t * deltaX

    //         // Stores the last y we used
    //         var last_y = p1y

    //         for(var x = p1x; x < p2x; x++) {

    //             var e =2 * x * deltaY - 2 * last_y * deltaX + constantPart

    //             if (e <= 0) {
    //                 colorPixelBlack(data, x, last_y, width, height)
    //             } else {
    //                 colorPixelBlack(data, x, ++last_y, width, height)
    //             }
    //         }
    //     }
    // }


}

// Colors the pixel at the given x / y coordinate black
function colorPixelBlack(data: Uint8ClampedArray, x: number, y: number, width: number, height: number) {
    var data_start = (y * height * 4) + x * 4
    data[data_start] = 0
    data[data_start + 1] = 0
    data[data_start + 2] = 0
    data[data_start + 3] = 255
}

