import maya.cmds as cmds


class CalculateUI:
    # create class variable, the same across all CalculateUI objects
    ui_name = 'Calculate'
    window_name = '%sWindow' % ui_name

    def __init__(self):
        pass

    def delete(self):
        # check to see if exists and delete if true
        if cmds.window(CalculateUI.window_name, exists=True):
            cmds.deleteUI(CalculateUI.window_name)

    def create(self):
        self.delete()
        print (CalculateUI.window_name)
        CalculateUI.window_name = cmds.window('test7',
                                       title='%s Tool' % (CalculateUI.window_name))
        print (CalculateUI.window_name)
        #
        # # define layout
        # self.cmds.columnLayout()
        #
        # # add controls as needed
        # cmds.button()
        # cmds.button()
        # cmds.button()
        #
        # cmds.showWindow(self.window_name)


test = CalculateUI()
test.create()