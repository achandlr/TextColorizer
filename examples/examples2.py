import numpy as np
from TextColorizer import TextColorizer

tokens = ["Hello", ",", "world", "!"]
data_dict = {
    'random_var_1': list(np.random.rand(len(tokens))),
    'random_var_2': list(np.random.rand(len(tokens)))
}

colorizer = TextColorizer(tokens, data_dict)
s = colorizer.colorize()

print(s)
