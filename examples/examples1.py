import numpy as np
from TextColorizer import TextColorizer

tokens = ["The", " ", "quick", " ", "brown", " ", "fox", " ", "jumps", " ", "over", " ", "the", " ", "lazy", " ", "dog"]
data_dict = {
    'var1': list(np.random.rand(len(tokens))),
    'var2': list(np.random.rand(len(tokens)))
}

colorizer = TextColorizer(tokens, data_dict)
s = colorizer.colorize()

print(s)
