

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
        menuBar.Append(filemenu, "&File")
        # 3.4向菜单对象添加条目对象
        menuRefresh = filemenu.Append(
            ID_EVENT_REFRESH, "&Refresh", "Refresh the price")
        menuQuit = filemenu.Append(
            wx.ID_EXIT, "Q&uit", "Terminate the program")
        # 3.5放置菜单栏，从这句开始菜单就会显示出来，但没有功能
        self.SetMenuBar(menuBar)
        # 3.6绑定条目的操作，实现功能
        self.Bind(wx.EVT_MENU, self.OnRefresh, menuRefresh)
        self.Bind(wx.EVT_MENU, self.OnQuit, menuQuit)


        # 4.创建容器
        panel = wx.Panel(self)

        # 5.创建代码输入区域
        codeSizer = wx.BoxSizer(wx.HORIZONTAL)
        # 5.1创建一段静态文字框
        labelText = wx.StaticText(panel, label="Stock Code:  ")
        # 5.2创建一个文本输入框
        codeText = wx.TextCtrl(panel, value='BA', style=wx.TE_PROCESS_ENTER)
        # 5.3创建一个sizer来调整他们的位置
        # 下面0是什么意思？？ proportion 后面的大写来自sizer flag list
        codeSizer.Add(labelText, 0, wx.ALIGN_BOTTOM)
        codeSizer.Add(codeText)
        # 5.4binding
        self.Bind(wx.EVT_TEXT_ENTER, self.OnTextSubmitted, codeText)


        # 6.创建复选框
        # 6.1创建一个szier
        optionSizer = wx.BoxSizer(wx.HORIZONTAL)
        # 6.2遍历option_list
        for key, value in self.option_list.items():
            checkBox = wx.CheckBox(panel, label=key.title())
            checkBox.SetValue(value)
            optionSizer.Add(checkBox)
            # 6.3 binding
            self.Bind(wx.EVT_CHECKBOX, self.OnChecked)

        # 7.创建列表对象
        self.list = wx.ListCtrl(panel, wx.NewId(), style=wx.LC_REPORT)
        # 7.1创建表头，以下这个函数是一个自定义函数
        self.createHeader()

        # 7.2创建等待状态文字
        pos = self.list.InsertItem(0, "--")
        self.list.SetItem(pos, 1, "loading···")
        self.list.SetItem(pos, 2, "--")
        # 7.2.1 binding
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnDoubleClick, self.list)


        # 8.创建按钮区域Quit和Refresh
        # 下面的-1是什么意思？ id
        buttonQuit = wx.Button(panel, -1, "Quit")
        buttonRefresh = wx.Button(panel, -1, "Refresh")
        # 8.1 sizer
        ctrlSizer = wx.BoxSizer(wx.HORIZONTAL)
        ctrlSizer.Add(buttonQuit)
        ctrlSizer.Add(buttonRefresh)
        # 8.2 binding
        self.Bind(wx.EVT_BUTTON, self.OnQuit, buttonQuit)
        self.Bind(wx.EVT_BUTTON, self.OnRefresh, buttonRefresh)

        # 9.整体布局
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(codeSizer, 0, wx.ALL, 5)
        sizer.Add(optionSizer, 0, wx.ALL, 5)
        sizer.Add(self.list, -1, wx.ALL | wx.EXPAND, 5)
        sizer.Add(ctrlSizer, 0, wx.ALIGN_BOTTOM)

        panel.SetSizerAndFit(sizer)
        self.Center()

        # 10.一开始就刷新一下
        self.OnRefresh(None)

    def createHeader(self):
        self.list.InsertColumn(0, "Symbol")
        self.list.InsertColumn(1, "Name")
        self.list.InsertColumn(2, "Last Trade")
    def setData(self, data):
        self.list.ClearAll()
        self.createHeader()
        pos = 0
        for row in data:
            pos = self.list.InsertItem(pos + 1, row['code'])
            self.list.SetItem(pos, 1, row['name'])
            self.list.SetColumnWidth(1, -1)
            self.list.SetItem(pos, 2, str(row['price']))
            if pos % 2 == 0:
                # Set new look and feel for odd lines
                self.list.SetItemBackgroundColour(pos, (134, 225, 249))

    def PlotData(self, code):
        quotes = finance.retrieve_quotes_historical(code)
        fields = ['date', 'open', 'close', 'high', 'low', 'volume']
        dates = []
        for i in range(0, len(quotes)):
            x = dt.datetime.utcfromtimestamp(int(quotes[i]['date']))
            y = dt.datetime.strftime(x, '%Y-%m-%d')
            dates.append(y)
        quotesdf = pd.DataFrame(quotes, index=dates, columns=fields)

        # remove unchecked fields
        fields_to_drop = ['date']
        for key, value in self.option_list.items():
            if not value:
                fields_to_drop.append(key)

        quotesdf = quotesdf.drop(fields_to_drop, axis=1)
        quotesdf.plot()
        plt.show()

    def OnDoubleClick(self, event):
        self.PlotData(event.GetText())

    def OnTextSubmitted(self, event):
        self.PlotData(event.GetString())

    def OnChecked(self, event):
        checkBox = event.GetEventObject()
        text = checkBox.GetLabel().lower()
        self.option_list[text] = checkBox.GetValue()

    def OnQuit(self, event):
        self.Close()
        self.Destroy()

    def OnRefresh(self, event):
        thread.start_new_thread(self.retrieve_quotes, ())

    def retrieve_quotes(self):
        data = finance.retrieve_dji_list()
        if data:
            self.setData(data)
        else:
            wx.MessageBox('Download failed.', 'Message', wx.OK | wx.ICON_INFORMATION)

if __name__ == '__main__':
    app = wx.App(False)
    top = StockFrame()
    top.Show(True)
    app.MainLoop()
