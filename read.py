import pandas as pd
import numpy as np
data1=pd.read_html('https://en.wikipedia.org/wiki/Tanjiro_Kamado')
print(data1[0])