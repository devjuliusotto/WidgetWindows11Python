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
        super(TaskFrame, self).__init__(parent, title=title, size=(500, 400))
        self.task_manager = TaskManager()
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Color settings
        background_color = "#004D40"  # Teal
        text_color = "#E0F2F1"       # Light teal
        button_color = "#00796B"     # Dark teal

        panel.SetBackgroundColour(background_color)

        # Adding components
        instruction = wx.StaticText(panel,
                                    label="Enter task as: Description, Category, Priority\nExample: Task, Work, 5")
        instruction.SetForegroundColour(text_color)  # Set text color

        self.text_ctrl = wx.TextCtrl(panel)
        self.add_button = wx.Button(panel, label='Add Task')
        self.add_button.SetBackgroundColour(button_color)
        self.add_button.SetForegroundColour(text_color)
        self.add_button.Bind(wx.EVT_BUTTON, self.on_add)

        self.list_button = wx.Button(panel, label='List Tasks')
        self.list_button.SetBackgroundColour(button_color)
        self.list_button.SetForegroundColour(text_color)
        self.list_button.Bind(wx.EVT_BUTTON, self.on_list)

        self.list_ctrl = wx.ListCtrl(panel, style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.list_ctrl.InsertColumn(0, 'Description', wx.LIST_FORMAT_LEFT, 120)
        self.list_ctrl.InsertColumn(1, 'Category', wx.LIST_FORMAT_LEFT, 120)
        self.list_ctrl.InsertColumn(2, 'Priority', wx.LIST_FORMAT_LEFT, 80)
        self.list_ctrl.SetBackgroundColour("#B2DFDB")  # Lighter teal

        # Layout
        vbox.Add(instruction, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(self.text_ctrl, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(self.add_button, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(self.list_button, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(self.list_ctrl, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)

        panel.SetSizer(vbox)

    def on_add(self, event):
        user_input = self.text_ctrl.GetValue()
        parts = user_input.split(',')
        if len(parts) == 3:
            description, category, priority = [part.strip() for part in parts]
            if description and category and priority.isdigit():
                self.task_manager.add_task(description, category, priority)
                wx.MessageBox('Task added successfully.', 'Success', wx.OK | wx.ICON_INFORMATION)
                self.text_ctrl.Clear()
                self.update_list()
            else:
                wx.MessageBox('Please ensure all fields are filled correctly and priority is numeric.', 'Error',
                              wx.OK | wx.ICON_ERROR)
        else:
            wx.MessageBox('Please enter the task in the format: Description, Category, Priority.', 'Error',
                          wx.OK | wx.ICON_ERROR)

    def on_list(self, event):
        self.update_list()

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
