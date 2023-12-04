import maya.cmds as cmds


class CalculateUI:
    ui_name = 'Calculate'
    window_name = '%sWindow' % ui_name

    def __init__(self):
        pass

    def delete(self):
        # check to see if window exists and delete if true
        if cmds.window(CalculateUI.window_name, exists=True):
            cmds.deleteUI(CalculateUI.window_name)

    def create(self):
        # create window
        self.delete()
        self.window_name = cmds.window(CalculateUI.window_name,
                                       title='%s Tool' % (CalculateUI.ui_name),
                                       widthHeight=(504, 139),
                                       sizeable=False)

        # define layout
        self.m_col = cmds.columnLayout(p=CalculateUI.window_name, adj=True)

        # create int slider called 'Number of Values with min 2, max 10, default 2.
        # when slider is changed, call self.update_num_fields()
        self.num_values = cmds.intSliderGrp(p=self.m_col,
                                            l='Number of Values',
                                            field=True,
                                            minValue=2,
                                            maxValue=10,
                                            value=2,
                                            cw=[(1, 150), (2, 50)],
                                            cl3=['center', 'center', 'center'],
                                            dc=lambda *args: self.update_num_fields())

        # add separator
        cmds.separator(p=self.m_col, style='in', h=10)

        # create dropdown menu called 'Operation' with 4 options: 'add', 'subtract', 'multiply', 'divide'
        self.operation = cmds.optionMenu(p=self.m_col, label='Operation')
        cmds.menuItem(p=self.operation, label='add')
        cmds.menuItem(p=self.operation, label='subtract')
        cmds.menuItem(p=self.operation, label='multiply')
        cmds.menuItem(p=self.operation, label='divide')

        # add separator
        cmds.separator(p=self.m_col, style='in', h=10)

        # create button called 'Calculate' with label 'Calculate' and command btn_cmd_calculate
        cmds.button(p=self.m_col, l='Calculate', c=lambda *args: self.btn_cmd_calculate())

        # add separator
        cmds.separator(p=self.m_col, style='in', h=10)

        # build float fields based on num_values
        self.update_num_fields()

        self.show()

    def show(self):
        cmds.showWindow(CalculateUI.window_name)

    # define update_num_fields() to create float fields based on num_values
    def update_num_fields(self):
        # get current value of num_values
        num_values = cmds.intSliderGrp(self.num_values, q=True, value=True)

        # delete any existing float fields
        if cmds.rowColumnLayout('float_fields', exists=True):
            cmds.deleteUI('float_fields')

        # create new rowcolumnlayout called 'float_fields' with 4 columns that expands to fill the window. Width of each column is 100
        f_row = cmds.rowColumnLayout('float_fields', p=self.m_col, nc=5,
                                     cat=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0), (4, 'both', 0),
                                          (5, 'both', 0)],
                                     cw=[(1, 100), (2, 100), (3, 100), (4, 100), (5, 100)])

        # create float fields based on num_values and assign to instance variables
        self.num_field_list = []
        for i in range(num_values):
            self.num_field_list.append(cmds.floatField(p=f_row, value=0, pre=2))

    # define btn_cmd_calculate() to calculate the values in the float fields using import calculate module
    def btn_cmd_calculate(self):
        import calculate

        # get current value of operation
        oper_type = cmds.optionMenu(self.operation, q=True, value=True)

        # create empty list
        num_list = []

        # iterate through num_list and append the value of each float field to num_list
        for num in self.num_field_list:
            num_list.append(cmds.floatField(num, q=True, value=True))

        # call calculate function from calculate module and pass num_list and oper_type
        total, operator = calculate.calculate(num_list[:], oper_type)

        # print total in a popup window with the operator and the values used
        num_list_str = ((" %s " % operator).join(map(str, num_list)))
        cmds.confirmDialog(title='Total', messageAlign='center', message='%s is %s' % (num_list_str, total))


myTest = CalculateUI()
myTest.create()