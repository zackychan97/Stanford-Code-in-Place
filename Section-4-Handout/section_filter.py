# LINK TO HANDOUT: https://codeinplace2020.github.io/faqs/section4.pdf

from simpleimage import SimpleImage

def main():
    """
    This program loads an image and applies the narok filter
    to it by setting "bright" pixels to grayscale values.
    """
    grey_scale()

def get_pixel_average(pixel):
    avg = (pixel.red + pixel.green + pixel.blue) // 3
    return avg

def grey_scale():
    image = SimpleImage('images/flower.png')
    for pixel in image:
        average = get_pixel_average(pixel)
        if average > 153:
            pixel.red = average
            pixel.blue = average
            pixel.green = average
    image.show()

if __name__ == '__main__':
    main()