# author: elan

import shutil
'''
  本次练习围绕shutil
    
'''

#
f_src = open("data.md",encoding="utf-8") ;
f_trg = open("data_c.md","w",encoding="utf-8") ;
shutil.copyfileobj(f_src, f_trg)

# copymode 仅拷贝权限、内容、组、用户均不变
