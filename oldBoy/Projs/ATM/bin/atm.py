# author: elan

import sys, os

# 必须将路径加入到path中 这样才可以导入
WORK_DIR = '\\'.join((os.path.abspath(__file__).split('\\')[0:-2]))
sys.path.append(WORK_DIR);

# 跨文件导入库
from cores import ShoppingChart
# import cores  # 在cores文件夹中__init__加入import ShoppingChart,但是后面代码需要改为cores.ShoppingChart

# 初始化商品
ShoppingChart.goods('zara',    'clothes', 200)
ShoppingChart.goods('tommy',    'clothes', 150)
ShoppingChart.goods('jackjones',  'clothes', 150)
ShoppingChart.goods('小熊饼干',  'snacks', 4)
ShoppingChart.goods('多多棒',   'snacks', 10)
ShoppingChart.goods('小浣熊',   'snacks', 2)

print(ShoppingChart.goods.good_list)

xiaomei = ShoppingChart.chart() ;
xiaomei.buy_clothes('zara', 300);

