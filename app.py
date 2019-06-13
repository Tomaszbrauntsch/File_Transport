import wx
class myWindow(wx.Frame):
	def __init__(self, parent, title): 
		super(myWindow, self).__init__(parent, title=title, size=(400,300))
		panel = wx.Panel(self)
		box = wx.BoxSizer(wx.VERTICAL)
		center_text = wx.StaticText(panel,style = wx.ALIGN_CENTER)
		
		txt = "Hello World!"
		
		font = wx.Font(8,wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
		center_text.SetFont(font)
		center_text.SetLabel(txt)
		
		center_text.SetForegroundColour((255,0,0))
		self.Center()
		self.Show()
	
app = wx.App()
myWindow(None, 'Demo')
app.MainLoop()