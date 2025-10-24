import pandas as pd
import numpy as np

# Ma'lumotlar lug'atini DataFrame'ga aylantiramiz
df = pd.DataFrame({
    'yil': [2021, 2022, 2023, 2024, 2025, 2025],
    'aholi': [33, 9, 34, 24.4, 232424.3, 9],
    'temp': [12, 3, 123, 1232, 1313, 12321]
})

hdpd = pd.HDFStore('data.h5')

hdpd.put('uz_data', df)

# print(hdpd)
# a=pd.read_hdf(hdpd)
# print(a)
# hdpd.close()
a=hdpd.keys()
print(a)