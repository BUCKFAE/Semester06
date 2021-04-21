/**
 * Determines the colour of a pixel (x, y) to create
 * a circle and saves it into the data array.
 * The data array holds the linearised pixel data of the target canvas
 * row major. Each pixel is of RGBA format.
 * @param data The linearised pixel array
 * @param x The x coordinate of the pixel
 * @param y The y coordinate of the pixel
 * @param width The width of the canvas
 * @param height The height of the canvas
 * @param radius The radius of the circle
 */
export function circle(data: Uint8ClampedArray, x: number, y: number, width: number, height: number, radius: number) {

    // Start of the current pixel in the data array
    var data_start = (y * height * 4) + x * 4

    // Calculating the center of the circle
    var circle_center_x = width / 2
    var circle_center_y = height / 2

    // Calculating the distance of the current point to the center
    var distance_to_center = Math.pow(x - circle_center_x, 2) + Math.pow(y - circle_center_y, 2)

    // If the distance is smaller than the radiusthe point lies in the circle
    if (distance_to_center < Math.pow(width / 3, 2)) {
        // Coloring the pixel black
        data[data_start] = 0
        data[data_start + 1] = 0
        data[data_start + 2] = 0
        data[data_start + 3] = 255
    } else {
        // Colorint the pixel white
        data[data_start] = 255
        data[data_start + 1] = 255
        data[data_start + 2] = 255
        data[data_start + 3] = 255
    }
}