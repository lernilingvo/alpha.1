#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""parameters.py: testing the lerni program."""

__author__ = "Henri Le Foll"
__copyright__ = "Copyright 2024"
__credits__ = ["Henri Le Foll"]
__license__ = "GPL"
__version__ = "3.0"
__maintainer__ = "Henri Le Foll"
__email__ = "lerni@gmail.com"
__status__ = "Prototype"

import os,sys
import gettext,json
from .read import Read
from .param import Param
from .model import Model

class Parameters(Param):

	def __init__(self ,dic_):

		super().__init__(dic_)
		self.initI18n()
		model = "data/config/model.lerni.json"
		self._model = Model(self._debug,model)

#-

	def initI18n(self):

		appname = 'crudAdd'
		localedir = '../locales'
		en_i18n = gettext.translation(appname, localedir, fallback=True, languages=['fr'])
		en_i18n.install()

#-

	def controlModelOK(self):

		print(" À faire !")
		return True

#-

	def getApps(self):
		#dic = self._model.get(self._param)#default)
		print(file = self._debugFile)
		print(self._param["learn"],file = self._debugFile)
		print(file = self._debugFile)
		self._model.help()
		print(file = self._debugFile)
		
		#exit()
		print("learn",file = self._debugFile)
		print(self._param["learn"],file = self._debugFile)
		dic = self._model.get(self._param["learn"])
		return dic["model"]

	def get(self,param_):
		return self._param[param_]


	def getM(self,param_):
		return self._model[param_]

	def getStructure(self,key_):
		dic = self._model.get(self._default)
		types = self._model.get("fileType")
		ret = types[key_]

		return types[key_]

	

	def getDetails(self):
		dic = self._model.get(self._default)
		types = self._model.get("keyDetail")

		return types

