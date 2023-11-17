from typing import Any, Container, Dict, Generic, Iterable, Iterator, List, Optional, Set, Tuple, TypeVar, Union
import cStringIO
import maya.cmds as cmds
import maya
import PySide2.QtXml as qt
import PySide2.QtCore as QtCore
import maya.api.OpenMaya as nom
import maya.mel as mel
import inspect
import maya.OpenMaya as om
import PySide2.QtSvg as QtSvg
import PySide2.QtWidgets as QtWidgets
import maya.OpenMayaUI as omui
import json
import math
import PySide2.QtXml as QtXml
import shiboken2 as shiboken
import csv
import os
import codecs
import PySide2.QtGui as QtGui


from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin as dockableMixin
from PySide2.QtCore import Slot


if False:
    from typing import Dict, List, Tuple, Union, Optional

class csv_writer:
    __init__ : instancemethod
    def writerow(self, row): ...
    def writerows(self, rows): ...


class csv_reader:
    __init__ : instancemethod
    def __iter__(self): ...
    def next(self): ...


class UTF8Wrapper:
    def __init__(self, f, encoding): ...
    def __iter__(self): ...
    def next(self): ...


class MCallbackIdWrapper(object):
    """
    Wrapper class to handle cleaning up of MCallbackIds from registered MMessage
    """
    
    
    
    def __del__(self): ...
    def __init__(self, callbackId): ...
    def __repr__(self) -> str: ...
    __dict__ : dictproxy
    
    __weakref__ : getset_descriptor




def getReadFileName(message, fileFilter="''"): ...
def importJSONFile(): ...
def getStringResource(indentifier, key): ...
def getFluxString(key): ...
def unwrapInstance(*args, **kwargs): ...
def endProgressBar(): ...
def getColourFromLabel(label): ...
def stepProgressBar(amount='1'): ...
def getQtWidgetAtPos(x, y): ...
def getWriteFileName(message, fileFilter="''"): ...
def getFuncFullName(func): ...
def wrapInstance(*args, **kwargs): ...
def colorLabel(identifier): ...
def createColorIcon(colorName='None', qcolor='None', x='100', y='100'): ...
def printCallStack(): ...
def getWidgetNameAtPos(x, y): ...
def applyRotations(rotations, origin): ...
def getDagPathFromName(nodeName): ...
def mayaWindow(): ...
def str_res(name): ...
def getMObjectFromName(nodeName): ...
def getMayaWidget(name): ...
def registerStringResources(identifier, resources): ...
def getPluginStringResource(key): ...
def mayaViewport(): ...
def startProgressBar(message="'Loading...'", length='100'): ...
def allColorLabels(): ...
def loadStringResources(module): ...
def getAttributePlug(name, attr): ...
def exportJSONFile(jsonData): ...
def getLocale(): ...


_color_labels : list
fluxResourcesFolder : str
moduleIdentifier : str
