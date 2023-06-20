# TextColorizer

Ever wanted to visualize your data in a more intuitive and fun way? Meet TextColorizer, a unique Python library that enables you to visualize numerical data as color-coded text. With TextColorizer, your data isn't just numbers in a table, but a vibrant display of color-mapped text.

## Getting Started

Open your terminal and type:
pip install TextColorizer

Usage
import numpy as np
from TextColorizer import TextColorizer

# Start by initializing the input tokens and data
tokens = ["The", " ", "quick", " ", "brown", " ", "fox", " ", "jumps", " ", "over", " ", "the", " ", "lazy", " ", "dog"]
data_dict = {
    'var_1': list(np.random.rand(len(tokens))),
    'var_2': list(np.random.rand(len(tokens)))
}

# Create an instance of TextColorizer and generate the colorized HTML
colorizer = TextColorizer(tokens, data_dict)
colorful_html = colorizer.colorize()

# Print the colorized HTML string
print(colorful_html)

# Want to use this HTML elsewhere? You can save the output to an HTML file
with open('colorize.html', 'w') as f:
    f.write(colorful_html)

## Breakdown of Classes and Methods
TextColorizer
At the heart of it all is our main class, TextColorizer, designed to take your text and data and turn it into a color-coded visualization.

__init__(self, tokens, data_dict)
The constructor of TextColorizer takes in your tokens (like words or punctuation) and a dictionary containing the corresponding data.

normalize(self, values)
This function normalizes your data values to fit between 0 and 1.

colorize(self)
The star of the show, this function generates colorized text as an HTML table based on your input data.

Directory Structure
To keep everything neat and tidy, we've organized the TextColorizer library as follows:

markdown
Copy code
TextColorizer/
│
├── TextColorizer/
│   ├── __init__.py
│   └── text_colorizer.py
│
├── examples/
│   ├── example1.py
│   └── example2.py
│
├── tests/
│   ├── test_text_colorizer.py
│   └── __init__.py
│
├── README.md
└── setup.py



