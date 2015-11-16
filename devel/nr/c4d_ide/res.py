# Automatically generated using craftr-c4d

import os
import sys
import c4d

_frame = sys._getframe(1)
while _frame and not '__res__' in _frame.f_globals:
    _frame = _frame.f_back

project_path = os.path.dirname(_frame.f_globals['__file__'])
resource = _frame.f_globals['__res__']


def string(name, *subst):
    result = resource.LoadString(globals()[name])
    for item in subst:
        result = result.replace('#', item, 1)
    return result


def tup(name, *subst):
    return (globals()[name], string(name, *subst))


def file(*parts):
    return os.path.join(project_path, *parts)


def bitmap(*parts):
    bitmap = c4d.bitmaps.BaseBitmap()
    result, ismovie = bitmap.InitWith(file(*parts))
    if result != c4d.IMAGERESULT_OK:
        return None
    return bitmap


GROUP_MAIN             = 10000
STATIC_STATUS          = 10001
BUTTON_UNDO            = 10002
BUTTON_REDO            = 10003
BUTTON_SEND            = 10004
BUTTON_SEND_TOOLTIP    = 10005
TEXT_SCRIPT            = 10006
GROUP_TRACEBACK        = 10007
TREE_TRACEBACK         = 10008
BUTTON_CLOSE_TRACEBACK = 10009
MENU_FILE              = 10010
MENU_FILE_OPEN         = 10011
MENU_FILE_SAVETO       = 10012
MENU_VIEW              = 10013
MENU_VIEW_TRACEBACK    = 10014
MENU_HELP              = 10015
MENU_HELP_ABOUT        = 10016
ABOUT_LINE1            = 10017
ABOUT_LINE2            = 10018
ABOUT_LINE3            = 10019
IDC_SCRIPT_EDITOR      = 10020
IDC_SCRIPT_EDITOR_HELP = 10021
IDC_CODE_OK            = 10022
IDC_NO_TRACEBACK       = 10023
IDS_EDITOR             = 10024
IDS_EDITOR_HELP        = 10025
IDS_EDITOR_TABS        = 10026
IDS_EDITOR_CODE        = 10027
IDC_EDITOR_ASKCLOSE    = 10028

