import maya.cmds as cmds

class CalculateUI():
    def __init__(self):
        self.window_name = 'Calculate'

    def delete(self):
        # check to see if exists and delete if true
        if cmds.window('%sWindow' % (self.window_name), exists=True):
            cmds.deleteUI('%sWindow' % (self.window_name))

    def create(self):
        # create window
        self.delete()
        
        self.window_name = cmds.window('%sWindow' % (self.window_name),
                                       title='%s Tool' % (self.window_name))
    
        #define layout
        cmds.columnLayout()
    
        # add controls as needed
        cmds.button()
        cmds.button()
        cmds.button()

        cmds.showWindow(self.window_name)