#!/usr/bin/env python3

import numpy as np
import pandas as pd
from scipy.io.arff import loadarff

raw_data = loadarff('PhishingWebsites.arff')
print(raw_data)

df_data = pd.DataFrame(raw_data[0])
print(df_data.head())

df_data.to_csv('PhishingWebSites.csv', index=False, encoding='utf-8')
