#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""log.py: testing the lerni program."""

__author__ = "Henri Le Foll"
__copyright__ = "Copyright 2024"
__credits__ = ["Henri Le Foll"]
__license__ = "GPL"
__version__ = "3.0"
__maintainer__ = "Henri Le Foll"
__email__ = "lerni@gmail.com"
__status__ = "Prototype"

#self.addAro #créer des objets Book, translationBook...
import csv,os,sys
import gettext,json
from datetime import datetime
from .sql import Sql

class Log(Sql):

	def __init__(self,param_):

		super().__init__(param_)

		self._file = "log.py"
		self._function = "__init__"


#-


	def save(self,array_):
	
		vApp = "logs"
		vTable = "log" 
		vInfo = {"app":vApp,"table":vTable,"request":array_}

		self.printIf("----")
		self.printIf("log : "+str(vInfo))
		self.printIf("----")

		vKey,isAdded = self.add(vInfo)

#-
