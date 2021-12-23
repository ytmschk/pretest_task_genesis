#!/usr/bin/env python
# coding: utf-8

import pandas as pd

df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]}) 

grouped_df = df.groupby("grps")

maximum = grouped_df.max()
