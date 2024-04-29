import wx

# ... (Task and TaskManager classes remain the same)

class TaskFrame(wx.Frame):
    def __init__(self, parent, title):
        super(TaskFrame, self).__init__(parent, title=title, size=(500, 400))
        self.task_manager = TaskManager()
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        panel.SetBackgroundColour((240, 240, 240))  # Light gray background

        box_sizer = wx.BoxSizer(wx.VERTICAL)

        # Task input section with labels and TextCtrls in a GridSizer
        input_grid = wx.GridBagSizer(5, 5)
        input_grid.SetEmptyCellBackgroundColour(wx.NullColour)  # Remove grid lines
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(11)  # Set a slightly larger font size

        # Label and input for Description
        lbl_description = wx.StaticText(panel, label="Description:", style=wx.ALIGN_RIGHT)
        lbl_description.SetFont(font)
        self.txt_description = wx.TextCtrl(panel)
        self.txt_description.SetFont(font)
        input_grid.Add(lbl_description, pos=(0, 0), flag=wx.LEFT | wx.TOP, border=5)
        input_grid.Add(self.txt_description, pos=(0, 1), span=(1, 2), flag=wx.EXPAND | wx.TOP, border=5)

        # Label and input for Category
        lbl_category = wx.StaticText(panel, label="Category:", style=wx.ALIGN_RIGHT)
        lbl_category.SetFont(font)
        self.txt_category = wx.TextCtrl(panel)
        self.txt_category.SetFont(font)
        input_grid.Add(lbl_category, pos=(1, 0), flag=wx.LEFT, border=5)
        input_grid.Add(self.txt_category, pos=(1, 1), span=(1, 2), flag=wx.EXPAND, border=5)

        # Label and input for Priority
        lbl_priority = wx.StaticText(panel, label="Priority:", style=wx.ALIGN_RIGHT)
        lbl_priority.SetFont(font)
        self.txt_priority = wx.TextCtrl(panel)
        self.txt_priority.SetFont(font)
        input_grid.Add(lbl_priority, pos=(2, 0), flag=wx.LEFT | wx.BOTTOM, border=5)
        input_grid.Add(self.txt_priority, pos=(2, 1), span=(1, 2), flag=wx.EXPAND | wx.BOTTOM, border=5)

        box_sizer.Add(input_grid, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)

        # Add button with custom style
        self.btn_add = wx.Button(panel, label="Add Task", style=wx.BUUTTON_ELEVATED)
        self.btn_add.SetBackgroundColour((0, 76, 255))  # Blue button color
        self.btn_add.SetForegroundColour((255, 255, 255))  # White button text
        self.btn_add.SetFont(font)
        self.btn_add.Bind(wx.EVT_BUTTON, self.on_add)
        box_sizer.Add(self.btn_add, proportion=0, flag=wx.ALL | wx.CENTER, border=10)

        # List control for showing tasks
        self.list_ctrl = wx.ListCtrl(panel, style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.list_ctrl.InsertColumn(0, 'Description', wx.LIST_FORMAT