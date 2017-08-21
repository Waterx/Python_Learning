

import datetime as dt
import my_finance as finance
import matplotlib.pyplot as plt
import pandas as pd
import _thread as thread
import wx
ID_EVENT_REFRESH = 9999

class StockFrame(wx.Frame):
    # 括号里的wx.Frame为本类继承自之
    # option_list为复选框架构
    option_list = {'open': True, 'close': True, 'high': False, 'low': False, 'volume': False}

    def __init__(self):
        # 1.使用父类的构造函数
        wx.Frame.__init__(self, None, title="Dji_info", size=(430, 600))

        # 2.创建状态栏
        self.CreateStatusBar()

        # 3.创建菜单栏
        # 3.1创建菜单栏对象
        menuBar = wx.MenuBar()
        # 3.2创建菜单对象
        filemenu = wx.Menu()
        # 3.3向菜单栏添加菜单对象
        menuBar.Append(filemenu, "&Fileeee")
        # 3.4向菜单对象添加条目对象
        menuRefresh = filemenu.Append(
            ID_EVENT_REFRESH, "&Refresh", "Refresh the price")
        menuQuit = filemenu.Append(
            wx.ID_EXIT, "Q&uit", "Terminate the program")
        # 3.5放置菜单栏，从这句开始菜单就会显示出来，但没有功能
        self.SetMenuBar(menuBar)
        # 3.6绑定条目的操作，实现功能
        #
        #

        # 4.创建容器
        panel = wx.Panel(self)

        # 5.创建代码输入区域
        codeSizer = wx.BoxSizer(wx.HORIZONTAL)
        # 5.1创建一段静态文字框
        labelText = wx.StaticText(panel, label="Stock Code:  ")
        # 5.2创建一个文本输入框
        codeText = wx.TextCtrl(panel, value='BA', style=wx.TE_PROCESS_ENTER)
        # 5.3创建一个sizer来调整他们的位置
        # 下面0是什么意思？？
        codeSizer.Add(labelText, 0, wx.ALIGN_BOTTOM)
        codeSizer.Add(codeText)
        # 5.4binding

        # 6.创建复选框
        # 6.1创建一个szier
        optionSizer = wx.BoxSizer(wx.HORIZONTAL)
        # 6.2遍历option_list
        for key, value in self.option_list.items():
            checkBox = wx.CheckBox(panel, label=key.title())
            checkBox.SetValue(value)
            optionSizer.Add(checkBox)
            #6.3 binding

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(codeSizer, 0, wx.ALL, 5)
        sizer.Add(optionSizer, 0, wx.ALL, 5)

        panel.SetSizerAndFit(sizer)
        self.Center()

if __name__ == '__main__':
    app = wx.App(False)
    top = StockFrame()
    top.Show(True)
    app.MainLoop()