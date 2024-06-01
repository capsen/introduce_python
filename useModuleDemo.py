import classdemo
import module.lottory as pb_alias
#from module.lottory import picknumbers

# import only method
from module.lottory import generatePowerball

e3=classdemo.Employee("Capsen", "Python class", 100)
print("======module demo========")
print(e3.name)

print(pb_alias.picknumbers(40, 8))
#print(picknumbers(40,8))
generatePowerball()