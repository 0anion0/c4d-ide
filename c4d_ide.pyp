# Copyright (c) 2014  Niklas Rosenstein
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os
import sys
import c4d
import json

PROJECT_PATH  = os.path.dirname(__file__)
RESOURCE_PATH = os.path.join(PROJECT_PATH, 'res')
DEVEL_PATH  = os.path.join(PROJECT_PATH, 'devel')

if DEVEL_PATH not in sys.path:
    sys.path.append(DEVEL_PATH)

# Remove all occurences of the nr.c4d_ide package in the module
# cache to fully reload it.
for key in sys.modules.keys():
    if key == 'nr.c4d_ide' or key.startswith('nr.c4d_ide.'):
        del sys.modules[key]

import nr.c4d_ide
from nr.c4d_ide import res


class OpenEditorWindow(c4d.plugins.CommandData):

  PLUGIN_ID = 1031950
  PLUGIN_NAME = res.string('IDS_EDITOR')
  PLUGIN_HELP = res.string('IDS_EDITOR_HELP')
  PLUGIN_INFO = 0
  PLUGIN_ICON = res.bitmap('img', 'editor.png')

  @classmethod
  def Register(cls):
    return c4d.plugins.RegisterCommandPlugin(
      cls.PLUGIN_ID, cls.PLUGIN_NAME, cls.PLUGIN_INFO,
      cls.PLUGIN_ICON, cls.PLUGIN_HELP, cls())

  # c4d.plugins.CommandData

  def Execute(self, doc):
    return nr.c4d_ide.main_window.Open(c4d.DLG_TYPE_ASYNC, self.PLUGIN_ID, 0)

  def RestoreLayout(self, secret):
    return nr.c4d_ide.main_window.Restore(self.PLUGIN_ID, secret)


def PluginStart():
  OpenEditorWindow.Register()


if __name__ == "__main__":
  PluginStart()
