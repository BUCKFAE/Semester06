/**
 * Determines the colour of a pixel (x, y) to create
 * a checkerboard pattern and saves it into the data array.
 * The data array holds the linearised pixel data of the target canvas
 * row major. Each pixel is of RGBA format.
 * @param data The linearised pixel array
 * @param x The x coordinate of the pixel
 * @param y The y coordinate of the pixel
 * @param width The width of the canvas
 * @param height The height of the canvas
 */
export function checkerboard(data: Uint8ClampedArray, x: number, y: number, width: number, height: number) {
    
    // Start of the current pixel in the data array
    var data_start = (y * height * 4) + x * 4
    
    // Size of one black / white square
    var field_size = width / 8

    // Mapping the x and y coordinates to [0, 8]
    var rel_x = Math.floor(x / field_size)
    var rel_y = Math.floor(y / field_size)

    // Coloring every other field black
    if (rel_y % 2 == rel_x % 2) {
        // Coloring the pixel black
        data[data_start] = 0
        data[data_start + 1] = 0
        data[data_start + 2] = 0
        data[data_start + 3] = 255
    } else {
        // Coloring the pixel white
        data[data_start] = 255
        data[data_start + 1] = 255
        data[data_start + 2] = 255
        data[data_start + 3] = 255
    }

}

