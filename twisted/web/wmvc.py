# Twisted, the Framework of Your Internet
# Copyright (C) 2001 Matthew W. Lefkowitz
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of version 2.1 of the GNU Lesser General Public
# License as published by the Free Software Foundation.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

"""
webmvc.py

The webmvc module collects together most of the modules and functions you will need to use Twisted's model view controller architecture for the web.
"""

from twisted.web import domtemplate
from twisted.python import mvc
from twisted.python import components
from twisted.web import domwidgets
from twisted.web import domhandlers
from twisted.web import resource


WModel = mvc.Model
WView = domtemplate.DOMTemplate
WController = domtemplate.DOMController


def registerViewForModel(view, model):
    components.registerAdapter(view, model, mvc.IView)

def registerControllerForModel(controller, model):
    components.registerAdapter(controller, model, mvc.IController)
    components.registerAdapter(controller, model, resource.IResource)

