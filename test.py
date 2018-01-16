# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:53:22 2018

@author: lenovo
"""

import tushare as ts
import pandas as pd



'''
basic = ts.get_stock_basics()

basic.to_excel("basic.xls")
basic
'''

basic = pd.read_excel("basic.xls")
basic = pd.DataFrame(basic)
basic = basic.sort_values("code")

