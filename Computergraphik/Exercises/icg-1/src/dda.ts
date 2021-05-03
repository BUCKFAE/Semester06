/**
 * Draws a line from pointA to pointB on the canvas
 * with the DDA algorithm.
 * @param  {Array.<number>} data   - The linearised pixel array
 * @param  {Array.<number>} pointA - The start point of the line
 * @param  {Array.<number>} pointB - The end point of the line
 * @param  {number} width          - The width of the canvas
 * @param  {number} height         - The height of the canvas
 */
export function dda(
    data: Uint8ClampedArray,
    pointA: [number, number],
    pointB: [number, number],
    width: number, height: number
) {

    // Point 1
    var p1x = Math.round(pointA[0])
    var p1y = Math.round(pointA[1])

    // Point 2
    var p2x = Math.round(pointB[0])
    var p2y = Math.round(pointB[1])

    // Slope of the line
    var m = (p2y - p1y) / (p2x - p1x)

    // Coloring start and end
    colorPixelBlack(data, p1x, p1y, width, height)
    colorPixelBlack(data, p2x, p2y, width, height)

    // Getting t
    var t = (m * (0 - p1x)) + p1y

    // Iterating over x to draw the line
    for(var x = Math.min(p1x, p2x); x < Math.max(p1x, p2x); x++) {
        var newY = Math.round(m * x + t)
        colorPixelBlack(data, x, newY, width, height)
    }

    // Iterating over y to draw the line
    for(var y = Math.min(p1y, p2y); y < Math.max(p1y, p2y); y++) {
        var newX = Math.round((y - t) / m)
        colorPixelBlack(data, newX, y, width, height)
    }

}

// Colors the pixel at the given x / y coordinate black
function colorPixelBlack(data: Uint8ClampedArray, x: number, y: number, width: number, height: number) {
    var data_start = (y * height * 4) + x * 4 
    data[data_start] = 0
    data[data_start + 1] = 0
    data[data_start + 2] = 0
    data[data_start + 3] = 255
}
