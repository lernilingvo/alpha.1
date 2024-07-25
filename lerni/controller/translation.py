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

		self._file = "translation.py"
		self._function = "__init__"

		self._structure = structure_

		# récupérer l’id

	def read(self):

		self._function = "read"
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

			self._boucle = " # ."
			vNum +=1
			self.printIf("translation.py # read avant boucle  - line : " + str(self._line))

			for vDescription in self._structure:

				self._boucle = " # # ."
				self.printIf()
				self.printIf("translation.py ## read avant boucle : " +str (vDescription["data"][0]))
				self._continuer = True
				self._continuerInc = 0

				if "positions" in vDescription["data"][0].keys():
					self._roots =  self._line[0].split(",")


				while self._continuer:

					vApp = vDescription["app"]
					vTable =  vDescription["table"]
					self._array = []
					self._pozicio = "0"
					self._increment = 0
					self.printIf("translation.py ## read avant boucle : " +str (vDescription["data"]))

					for  aData in vDescription["data"]:
						self._boucle = " # # # # ."
						self.printIf()
						self.printIf("translation.py - read - aData : " + str(aData))
						self.printIf("translation.py - read - avant readData_ : "+str(self._array))
						self._function = "readData"
						self.readData(aData,vApp,vTable)
						self._function = "read"
						self.printIf("translation.py ### read - après readData_ fin boucle : "+str(self._array))

					if "positions" in vDescription["data"][0].keys():
						self._continuerInc += 1
						self._continuer = self._continuerInc <= len(self._roots) - 1
					else:
						self._continuer = False

					self._boucle = " # # # ."
					self._increment += 1

					match self._book["type"]:
						case "word_list":
							aColumnName = "vortuLibre_id"
							self._array.append({"select":aColumnName,"value":str(self._book["bookId"])})
						case "word_translation_ordered"|"word_translation_minimal":
							aColumnName = "vortarLibrejo_id"
							self._array.append({"select":aColumnName,"value":str(self._book["bookId"])})
						case "radical_decomposition":
							pass
						case _:
							print()
							print("translation.py case - " + self._book["type"] + " : not known yet")
							print()
							exit()
						#case "radical_decomposition":
						#	aColumnName = "vortuLibre_id"
						#	exit()
					

	
					vInfo = {"app":vApp,"table":vTable,"request":self._array}
					self.printIf("----")
					self.printIf(vInfo)
					self.printIf("----")
					vKey,isAdded = self.add(vInfo)
					self.printIf("---- fin boucle ")


	def readData(self,desc_,app_,table_):

		xDic = {}

		if "table" in desc_.keys():
			table_ = desc_["table"]

		if "app" in desc_.keys():
			app_ = desc_["app"]

		if "field" in desc_.keys():
			vField = desc_["field"]

		if "position" in desc_.keys():
			vPosition = desc_["position"]

			self.printIf()
			self.printIf("translation.py - readData_ : " + str(self._line))
			self.printIf(vPosition)
			self.printIf()
			vLu = self._line[vPosition]

		if "increment" in desc_.keys():
			vLu = str(self._continuerInc)

		if "concatenation" in desc_.keys():
			vLu = ""
			for vRoot in  self._roots:
				vLu += vRoot

		if "positions" in desc_.keys():
			vLu = self._roots[self._continuerInc]
			self.printIf("ICI positions" + vLu)
			#self._continuer = self._continuerInc == len(self._roots)

		if "subData" in desc_.keys():
			for sub in desc_["subData"]:
				self.readData(sub,app_,table_)
						
		if "complete" in desc_.keys():

			xInfo = {"app":app_,"table":table_,"request":[
					{"select":vField,"value":vLu.replace("'","’")}]
					}

			xKey,isAdded = self.add(xInfo)
			self.printIf(" translation.py - readData_ - xKey : " + str(xKey))

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
			self.printIf("translation.py - readData_ - xInfo : " + str(xInfo))
			xKey,isAdded = self.add(xInfo)
			xDic["select"] = desc_["field"]
			xDic["value"] = xKey

			self._array.append(xDic)

