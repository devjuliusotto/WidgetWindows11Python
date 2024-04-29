import wx

class Task:
    def __init__(self, description, category, priority):
        self.description = description
        self.category = category
        self.priority = int(priority)

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, category, priority):
        task = Task(description, category, priority)
        self.tasks.append(task)
        return "Task added successfully."

    def list_tasks(self):
        return self.tasks

class TaskFrame(wx.Frame):
    def __init__(self, parent, title):
        super(TaskFrame, self).__init__(parent, title=title, size=(500, 500))
        self.task_manager = TaskManager()
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        grid = wx.GridBagSizer(5, 5)

        # Color settings
        background_color = "#004D40"  # Teal
        text_color = "#E0F2F1"       # Light teal
        button_color = "#00796B"     # Dark teal

        panel.SetBackgroundColour(background_color)

        # Setup fonts
        font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        # Adding components
        lbl_description = wx.StaticText(panel, label="Description")
        lbl_description.SetForegroundColour(text_color)
        lbl_description.SetFont(font)
        self.txt_description = wx.TextCtrl(panel)
        self.txt_description.SetBackgroundColour("#B2DFDB")

        lbl_category = wx.StaticText(panel, label="Category")
        lbl_category.SetForegroundColour(text_color)
        lbl_category.SetFont(font)
        self.txt_category = wx.TextCtrl(panel)
        self.txt_category.SetBackgroundColour("#B2DFDB")

        lbl_priority = wx.StaticText(panel, label="Priority")
        lbl_priority.SetForegroundColour(text_color)
        lbl_priority.SetFont(font)
        self.txt_priority = wx.TextCtrl(panel)
        self.txt_priority.SetBackgroundColour("#B2DFDB")

        self.btn_add = wx.Button(panel, label="Add Task")
        self.btn_add.SetBackgroundColour(button_color)
        self.btn_add.SetForegroundColour(text_color)
        self.btn_add.Bind(wx.EVT_BUTTON, self.on_add)

        # Adding to grid
        grid.Add(lbl_description, pos=(0, 0), flag=wx.LEFT | wx.TOP, border=5)
        grid.Add(self.txt_description, pos=(0, 1), span=(1, 2), flag=wx.EXPAND | wx.TOP, border=5)
        grid.Add(lbl_category, pos=(1, 0), flag=wx.LEFT, border=5)
        grid.Add(self.txt_category, pos=(1, 1), span=(1, 2), flag=wx.EXPAND, border=5)
        grid.Add(lbl_priority, pos=(2, 0), flag=wx.LEFT | wx.BOTTOM, border=5)
        grid.Add(self.txt_priority, pos=(2, 1), span=(1, 2), flag=wx.EXPAND | wx.BOTTOM, border=5)
        grid.Add(self.btn_add, pos=(3, 0), span=(1, 3), flag=wx.EXPAND | wx.BOTTOM, border=5)

        # List control for showing tasks
        self.list_ctrl = wx.ListCtrl(panel, style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.list_ctrl.InsertColumn(0, 'Description', wx.LIST_FORMAT_LEFT, 180)
        self.list_ctrl.InsertColumn(1, 'Category', wx.LIST_FORMAT_LEFT, 180)
        self.list_ctrl.InsertColumn(2, 'Priority', wx.LIST_FORMAT_LEFT, 100)
        self.list_ctrl.SetBackgroundColour("#B2DFDB")
        grid.Add(self.list_ctrl, pos=(4, 0), span=(1, 3), flag=wx.EXPAND)

        # Sizer configuration
        grid.AddGrowableCol(1)
        grid.AddGrowableRow(4)
        panel.SetSizer(grid)

    def on_add(self, event):
        description = self.txt_description.GetValue()
        category = self.txt_category.GetValue()
        priority = self.txt_priority.GetValue()
        if description and category and priority.isdigit():
            self.task_manager.add_task(description, category, priority)
            wx.MessageBox('Task added successfully.', 'Success', wx.OK | wx.ICON_INFORMATION)
            self.txt_description.Clear()
            self.txt_category.Clear()
            self.txt_priority.Clear()
            self.update_list()
        else:
            wx.MessageBox('Please ensure all fields are filled correctly and priority is numeric.', 'Error', wx.OK | wx.ICON_ERROR)

    def update_list(self):
        self.list_ctrl.DeleteAllItems()
        for task in self.task_manager.list_tasks():
            index = self.list_ctrl.InsertItem(self.list_ctrl.GetItemCount(), task.description)
            self.list_ctrl.SetItem(index, 1, task.category)
            self.list_ctrl.SetItem(index, 2, str(task.priority))

if __name__ == '__main__':
    app = wx.App(False)
    frame = TaskFrame(None, 'Enhanced Task Manager')
    frame.Show()
    app.MainLoop()
