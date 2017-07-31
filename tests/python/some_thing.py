# 可一通过sys.path来知道怎么寻找module的
import sys
for place in sys.path:
    print("search path:", place)
