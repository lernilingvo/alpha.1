#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""read.py: testing the lerni program."""

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

class Read():

	def __init__(self , name_,debug_,file_=None):

		self._filename = name_
		self._debugFile = file_
		self._debug = debug_
		self.setJson()
#-

	def setJson(self):

		if self._debug:
			print("init READ : " + self._filename,file =self._debugFile)

		self.controlFileExists()

		with open(self._filename) as f:
			data = f.read()

		self._json = json.loads(data)
		self._json["debug"] = self._debug
		self._json["debugFile"] = self._debugFile
 
#-

	def controlFileExists(self):

		if not os.path.isfile(self._filename):
			error = "FILE NOT FOUND : " + self._filename
			self.print(error)
			exit()
			#return False


	def print(self,string_,nb=12):
		if nb in [1,12]:
			print(file = self._debugFile)
		print(string_,file = self._debugFile)
		if nb in [2,12]:
			print(file = self._debugFile)


	def isJsonKey(self,key_,dic_=None):

		if dic_ == None:
			dic_ = self._paramComplete

		if not key_ in dic_.keys():
			self._error = "KEY: " + key_ + " NOT FOUND"
			return False

		return True

	def get(self,key_):

		if key_ in self._json.keys():
			return self._json[key_]
		else:
			print("get - KEY: " + key_ + " NOT FOUND")
			print(self._filename)
			exit()

	def all(self):
		print(self._json)
		return self._json

	def param(self):
		print(self._param)
		return self._param

	def help(self):

		for aKey in self._json.keys():
			print(aKey + " : " + str(self._json[aKey]))
