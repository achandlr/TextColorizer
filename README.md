# TextColorizer

TextColorizer is a Python library used to visualize numerical data as color-coded text. It maps the data to a color gradient and applies this to the input text. The output is an HTML table with the color-coded text.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install TextColorizer.

```bash
pip install TextColorizer

## Usage
# Import required libraries
import numpy as np
from TextColorizer import TextColorizer

# Initialize the input tokens and data
tokens = ["The", " ", "quick", " ", "brown", " ", "fox", " ", "jumps", " ", "over", " ", "the", " ", "lazy", " ", "dog"]
data_dict = {
    'variance': list(np.random.rand(len(tokens))),
    'diff_from_empty_str': list(np.random.rand(len(tokens)))
}

# Initialize the TextColorizer and generate colorized HTML
colorizer = TextColorizer(tokens, data_dict)
s = colorizer.colorize()

# Print the HTML string
print(s)

# Save the output to an HTML file
with open('colorize.html', 'w') as f:
    f.write(s)

## Class and Methods
TextColorizer
The main class to colorize text based on the input data.

__init__(self, tokens, data_dict)
Constructor to initialize the TextColorizer.

normalize(self, values)
Normalize a list of values to the range [0, 1].

colorize(self)
Generate colorized text as an HTML table based on the input data.
