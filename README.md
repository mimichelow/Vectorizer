# Vectorizer

## Description

The module contains a function for converting an image file into a vectorized pixel representation and saving it as an SVG file.

## Installation

To use this module, you need to have the dependencies included in "requierements.txt"

You can install the dependencies by running the following command:

pip install pillow drawSvg

# Usage

Import the `vectorizer` function from the module and use it as follows:

```python
from vectorizer import vectorizer

# Call the vectorizer function
vectorizer(file, output="output.svg", pixelScale=5, lineThickness=0, pixelSpacing=0)

