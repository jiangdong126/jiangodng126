# 借助于importlib包可以实现导入数字开头的模块名称
import importlib

# 相当于导入了一个叫01的模块并把导入模块赋值给liaoning
liaoning = importlib.import_module('01')

stu = liaoning.Student()
stu.say()