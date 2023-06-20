'''
The TextColorizer module.

This module provides a way to visualize numerical data as color-coded text. The data is mapped to a 
color gradient and applied to the input text. The output is an HTML table with the color-coded text.

'''

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

class TextColorizer:
    def __init__(self, tokens, data_dict):
        """
        Initialize the TextColorizer with the tokens (words, punctuation, etc.) and a dictionary containing 
        the data to colorize.

        :param tokens: list of tokens (words, punctuation, etc.).
        :param data_dict: dictionary containing the data to colorize.
        """
        self.tokens = tokens
        self.data_dict = data_dict

    def normalize(self, values):
        """
        Normalize a list of values to range between 0 and 1.

        :param values: list of numerical values.
        :return: list of normalized values.
        """
        min_value = min(values)
        max_value = max(values)
        normalized_values = [(v - min_value) / (max_value - min_value) for v in values]
        return normalized_values

    def colorize(self):
        """
        Colorize the tokens and formats them into an HTML table based on the data in the dictionary.

        :return: string containing the HTML table.
        """
        cmap = matplotlib.cm.get_cmap("Reds")
        template = '<span class="barcode"; style="color: black; background-color: {}">{}</span>'
        
        # Create an HTML table with a row for each key in the dictionary
        output = "<table>"
        for key, values in self.data_dict.items():
            norm_values = self.normalize(values)
            colored_values = ''.join(template.format(
                matplotlib.colors.rgb2hex(cmap(norm_values[i])[:3]), self.tokens[i]
            ) for i in range(len(self.tokens)))
            
            output += f'<tr><td>{key}:</td><td>{colored_values}</td></tr>'
        
        output += "</table>"
        return output
