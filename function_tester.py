#import src.linear_aligned_ele
#import src.diag_aligned_ele

import dataval_constructor
"""
for i in linear_aligned_ele.linear_aligned_ele(0.5, 4):
    print(i)
    

for i in diag_aligned_ele.diag_aligned_ele(0.5, 4):
    print(i)"""
    
X ,y = dataval_constructor.dataval_constructor(number_of_value=6, pixel_diff = 0.3, greator_val = None, data_percent_split=0.5, shuffle = True)
print(X)
print(y)