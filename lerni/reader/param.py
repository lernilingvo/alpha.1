#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""param.py: testing the lerni program."""

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

class Param(Read):

	def __init__(self ,dic_):

		self._paramName =  "data/config/param.lerni.json"
		super().__init__(self._paramName,dic_["debug"],dic_["debugFile"])
		self.initParam(dic_)

		if self._param["debug"]:
			print(file = self._debugFile)
			print(self._param,file = self._debugFile)

#-

	def initParam(self,dic_):
		self._error = "None"

		#print("----Model")
		
		self.setJsonParam()

		for aKey in dic_:
			self._param[aKey] = dic_[aKey]

		if self._param["debug"]:
			print(self._param,file = self._debugFile)
		#exit()
	
		
#-

	def setJsonParam(self):

		#print("----Control")
		self._param = {}
		vUser =  self._json["defaultUser"]
		tUsers = self._json["users"]	

		for aUser in tUsers:
		
			if vUser == aUser["name"] :

				self._param = self._json[aUser["defaultLanguage"]]

		if len(self._param) == 0:
			print()
			print(" ATTENTION : pb de paramètres")
			print()
			exit()				

		self._param["user"] = vUser

		vLanguages = self._param["languages"]
		
		self._param["learn"] = vLanguages["learn"]
		self._param["home"] = vLanguages["home"]
		self._default = vLanguages["learn"]

		print()
		print()
		print(self._param)
		print()
		print()

		return

