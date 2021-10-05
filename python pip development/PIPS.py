import os
class PIPS:#PIPS类：主要存储具体的pip指令实际操作的类
    def __init__(self):
        pass#暂无类变量，设为pass就行

    def install(self,packages):#下载安装的cmd操作函数
        cmd='pip install '+packages
        operation = os.popen(cmd)#不同打开cmd窗口，就可以运行命令
        return operation.read()#返回成功后的信息内容

    def uninstall(self,packages):#卸载的cmd操作函数
        cmd='pip uninstall '+packages#由于要在cmd中做二次选择（y或n），所以要打开cmd窗口
        os.system(cmd)

    def piplist(self):#库列表的cmd操作函数
        cmd='pip list'
        operation = os.popen(cmd)
        return operation.read()

    def checkpip(self,packages):#库查询的cmd操作函数
        cmd='pip show '+packages
        operation = os.popen(cmd)
        return operation.read()

    def uppip(self,packages):#更新库的cmd操作函数
        cmd='python -m pip install --upgrade '+packages
        operation = os.popen(cmd)
        return operation.read()

    def opencmd(self):#cmd打开窗口操作函数
        os.system('cmd/c start')








