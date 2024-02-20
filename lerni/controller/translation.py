#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""translation.py: testing the lerni program."""

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
from .book import Book

class Translation(Book):

	def __init__(self , param_,book_,structure_):

		super().__init__(param_,book_)

		self._structure = structure_

		# récupérer l’id

	def read(self):

		self.printIf("#-")
		self.printIf("readTranslation : " + self._book["type"])
		data = self.getData()
		apps = ["l" + self._book["language"] , "l" + self._book["translation"]]
		self.printIf()
		self.printIf()
		#rows = self._conf.getType(self._book["type"])
		#rows = self._sructure
		self.printIf(apps)
		self.printIf("##")
		self.printIf(self._structure)
		vNum = 0

		for self._line in data:

			vNum +=1

			for vDescription in self._structure:

				vApp = vDescription["app"]
				vTable =  vDescription["table"]
				self._array = []
				self._pozicio = "0"
				self._increment = 0
				self.printIf()
				self.printIf()
				self.printIf()
				self.printIf(self._book["type"])
				self.printIf()
				self.printIf(vDescription["data"])
				

				for  aData in vDescription["data"]:

					self.printIf()
					self.printIf("aData : " + str(aData))
					self.printIf("avant array : "+str(self._array))
					self.readData(aData,vApp,vTable)
					self.printIf("après array : "+str(self._array))

				aColumnName = "vortarLibrejo_id"

				match self._book["type"]:
					case "word_list":
						aColumnName = "vortuLibre_id"
					case "radical_decomposition":
						aColumnName = "vortuLibre_id"
						exit()

	
				self._array.append({"select":aColumnName,"value":str(self._book["bookId"])})
				vInfo = {"app":vApp,"table":vTable,"request":self._array}
				self.printIf("----")
				self.printIf(vInfo)
				self.printIf("----")
				vKey,isAdded = self.add(vInfo)


	def readData(self,desc_,app_,table_):

		xDic = {}
		self._increment += 1

		if "table" in desc_.keys():
			table_ = desc_["table"]

		if "app" in desc_.keys():
			app_ = desc_["app"]

		if "field" in desc_.keys():
			vField = desc_["field"]

		if "position" in desc_.keys():
			vPosition = desc_["position"]

			self.printIf()
			self.printIf(self._line)
			self.printIf(vPosition)
			self.printIf()
			vLu = self._line[vPosition]

		if "increment" in desc_.keys():
			vLu = str(self._increment)
			self.printIf("ICI  vLu = "+str(vLu))

		if "positions" in desc_.keys():
			vLu = ""
			for vPosition in  desc_["positions"]:
				vLu += self._line[vPosition]

		if "subData" in desc_.keys():
			for sub in desc_["subData"]:
				self.readData(sub,app_,table_)
						
		if "complete" in desc_.keys():

			xInfo = {"app":app_,"table":table_,"request":[
					{"select":vField,"value":vLu.replace("'","’")}]
					}

			xKey,isAdded = self.add(xInfo)
			self.printIf(" xKey : " + str(xKey))

		if "end" in desc_.keys():
			xDic["select"] = desc_["field"]
			xDic["value"] = vLu.replace("'","’")
			self._array.append(xDic)

			self.printIf("####### : "  + str(desc_))
			
			

		if "key" in desc_.keys():
			d = desc_["key"]
			self.printIf("d = "+str(d))
			xInfo = {"app":d["app"],"table":d["table"],"request":[
					{"select":d["field"],"value":vLu.replace("'","’")}]
					}
			self.printIf("xInfo : " + str(xInfo))
			xKey,isAdded = self.add(xInfo)
			xDic["select"] = desc_["field"]
			xDic["value"] = xKey

			self._array.append(xDic)

