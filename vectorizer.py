import drawsvg as draw
from PIL import Image


def vectorizer(file, output="output.svg", pixelScale=5, lineThickness=0, pixelSpacing=0):
    """
    Converts an image file into a vectorized representation and saves it as an SVG file.

    Parameters:
        file (str): The path to the input image file.
        output (str): The path to save the output SVG file (default: "output.svg").
        pixelScale (int): The size (in pixels) of each vectorized pixel (default: 5).
        lineThickness (int): The thickness (in pixels) of the vectorized lines (default: 0).
        pixelSpacing (int): The spacing (in pixels) between vectorized pixels (default: 0).

    Returns:
        None

    Raises:
        FileNotFoundError: If the input image file cannot be found.
        IOError: If there is an error while reading the input image file.
        draw.DrawingError: If there is an error while creating or saving the SVG.

    Example:
        vectorizer("image.png", output="output.svg", pixelScale=10, lineThickness=1, pixelSpacing=2)
    """

    # Open the input image file
    with Image.open(file, mode="r") as pic:
        width, height = pic.size
        delta = pixelScale + lineThickness

        # Create a new drawing with the appropriate dimensions
        d = draw.Drawing(height * (delta + pixelSpacing), width * (delta + pixelSpacing))
        cornerx = 0
        cornery = 0

        # Iterate over each pixel in the image
        for y in range(height):
            for x in range(width):
                # Check if the pixel is transparent (alpha channel > 0)
                if pic.getpixel((x, y))[3]:
                    # Add a rectangle representing the pixel to the drawing
                    d.append(draw.Rectangle(cornerx, cornery, delta, delta,
                                            fill='#{:02x}{:02x}{:02x}'.format(*pic.getpixel((x, y))),
                                            stroke="black",
                                            stroke_width=lineThickness))
                cornerx += delta + pixelSpacing
            cornerx = 0
            cornery += delta + pixelSpacing

        # Save the drawing as an SVG file
        d.save_svg(output)


if __name__ == "__main__":
    vectorizer("Icon.png")
