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

from c4dprototyping.proxy import DelayedBinding as _DelayedBinding

__author__  = 'Niklas Rosenstein <rosensteinniklas@gmail.com>'
__version__ = (0, 0, 1)

res = _DelayedBinding()

def init(resource):
    r""" Called from ``nr-prototyping.pyp`` to initialize the module
    with the loaded resource symbols. GUI operations may only be
    invoked after this function was called.

    It also creates the global instances of the :class:`ScriptEditor`
    and :class:`ScriptExecutor`. """

    global res
    if type(res) != _DelayedBinding:
        raise RuntimeError('already initialized')

    # Bind the proxy for all that imported the resource
    # before initializing.
    res._bind(resource)

    # Make the original object available to those that want
    # to import it after initializing.
    res = resource

