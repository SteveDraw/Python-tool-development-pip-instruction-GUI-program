from tkinter import *
from PIPS import PIPS
class PIPGUI(PIPS):
    #GUI控件类定义
    def __init__(self):
        super().__init__()#继承自PIPS类
        #主窗体
        root=Tk()
        root.title('pip下载程序')
        root.geometry('1020x550+200+80')#程序窗口大小及位置
        root.iconbitmap('pips.ico')#窗口图标

        # install按钮
        install_button = Button(root, text='下载并安装', width=18, height=2, command=self.installs)
        install_button.place(x=20, y=100)

        # uninstall按钮
        uninstall__button = Button(root, text='卸载', width=18, height=2, command=self.uninstalls)
        uninstall__button.place(x=200, y=100)

        # 库列表按钮
        list_button = Button(root, text='第三库列表', width=18, height=2, command=self.piplists)
        list_button.place(x=20, y=160)

        # 查询库信息按钮
        checkp_button = Button(root, text='库查询', width=18, height=2, command=self.checkpips)
        checkp_button.place(x=200, y=160)

        # pip指令更新按钮
        up_button = Button(root, text='更新库包', width=18, height=2, command=self.uppips)
        up_button.place(x=20, y=220)

        # cmd打开按钮
        self.cmd_textout_button = Button(root, text='打开cmd窗口', width=18, height=2, command=self.opencmds)
        self.cmd_textout_button.place(x=200, y=220)

        # 输入框清空按钮
        self.in_textout_button = Button(root, text='清空输入框', width=18, height=2, command=self.in_textouts)
        self.in_textout_button.place(x=200, y=280)

        #cmd运行内容清除按钮
        self.cmd_textout_button=Button(root, text='清空cmd运行结果', width=18, height=2, command=self.cmd_textout)
        self.cmd_textout_button.place(x=20,y=280)

        # 运行内容显示
        self.cmd_text = Text(root, width=85, height=40)
        self.cmd_text.place(x=400, y=10)

        # 输入显示窗口
        self.in_text = Text(root, width=50, height=2)
        self.in_text.place(x=20, y=10)

        # 程序状态标签
        self.tip_label = Label(root, text='程序操作提示', width=35, height=2, bg='green', font=('宋体', 14))
        self.tip_label.place(x=20, y=430)

        # 操作提示栏
        self.tipout_label = Label(root, width=50, height=3, bg='green',font=('宋体',10))
        self.tipout_label.place(x=20, y=485)
        root.mainloop()

    # 函数部分:
    def text_get(self):  # 获取输入框内容函数
        return self.in_text.get('1.0', 'end')

    def cmd_in(self,result):  # cmd运行结果输入函数
        self.cmd_text.insert(1.0, result)

    def cmd_textout(self):  # cmd内容清除函数
        self.cmd_text.delete('1.0', 'end')
        self.tipout_label['text'] = '你清空了cmd运行内容框！'

    def installs(self):  # 下载安装按钮函数
        self.cmd_textout()
        self.tipout_label['text'] = '你使用了下载安装的功能！注意使用前不要开代理节点！'
        result = self.install(self.text_get())
        self.cmd_in(result)

    def uninstalls(self):  # 卸载按钮函数
        self.cmd_textout()
        self.tipout_label['text'] = '不要输入带有等号的命令！请到弹出的cmd窗口确定是否卸载！'
        self.uninstall(self.text_get())

    def piplists(self):  # 库列表按钮函数
        self.cmd_textout()
        self.tipout_label['text'] = '你查询了库列表，查询结果可下滑查看更多的内容'
        result = self.piplist()
        self.cmd_in(result)

    def checkpips(self):  # 库查询按钮函数
        self.cmd_textout()
        self.tipout_label['text'] = '注意输入时不要带有等号！'
        result = self.checkpip(self.text_get())
        self.cmd_in(result)

    def uppips(self):  # 库更新按钮函数
        self.cmd_textout()
        self.tipout_label['text'] = '你使用了库更新的功能！'
        result = self.uppip(self.text_get())
        self.cmd_in(result)

    def in_textouts(self):#输入框清除函数
        self.in_text.delete('1.0', 'end')
        self.tipout_label['text'] = '你清空了输入框窗口！'
        
    def opencmds(self):#cmd打开窗口操作函数
        self.opencmd()
        self.tipout_label['text']='你打开了cmd窗口！'

if __name__ == '__main__':
    PIPGUI()

