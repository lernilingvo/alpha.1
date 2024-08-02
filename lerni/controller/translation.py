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

	def __init__(self , param_,book_,conf_):

		super().__init__(param_,book_)

		self._file = "translation.py"
		self._function = "__init__"

		self._structure = conf_.getStructure(book_["type"])
		self._details = conf_.getDetails()

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

				vDescription = self._structure

				self._boucle = " # # ."
				self.printIf()
				self.printIf("translation.py ## read avant boucle : " +str (vDescription))
				self._continuer = True
				self._continuerInc = 0


				while self._continuer:

					vApp = vDescription["app"]
					vTable =  vDescription["table"]
					self._array = []
					self._pozicio = "0"
					self._increment = 0
					self.printIf("translation.py ## read avant boucle - vDesc: " +str (vDescription["data"]))

					for  aData in vDescription["data"]:

						if aData["position"] == "array":
							self._roots =  self._line[0].split(",")
							self.printIf("translation.py -- roots : " +str (self._roots))
						self._boucle = " # # # # ."
						self.printIf()
						self.printIf("translation.py - read - aData : " + str(aData))
						self.printIf("translation.py - read - avant readData_ : "+str(self._array))
						self.readData(aData,vApp,vTable)
						self._function = "read"
						self.printIf("translation.py ### read - après readData_ fin boucle : position " + str(aData["position"]))

					if aData["position"] == "array":
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
						case "radical_list_ordered":
							aColumnName = "radikuLibre_id"
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

		self._function = "readData"
		self.printIf("---- "+str(desc_))

		xDic = {}
		vField = desc_["field"]
		vPosition = desc_["position"]
		self.printIf("----+" + str(self._details))
		vDetails = self._details[vField]


		if vPosition in [0,1,2,3,4,5,6,7,8,9]:

			self.printIf()
			self.printIf("translation.py - readData_ : " + str(self._line))
			self.printIf(vPosition)
			self.printIf()
			vLu = self._line[vPosition]

		if vPosition == "increment":
			vLu = str(self._continuerInc)

		if vPosition == "concatenation":
			vLu = ""
			for vRoot in  self._roots:
				vLu += vRoot

		if vPosition == "array":
			vLu = self._roots[self._continuerInc]
			self.printIf("ICI positions" + vLu)
			#self._continuer = self._continuerInc == len(self._roots)

			

		if vDetails == "end" :
			xDic["select"] = desc_["field"]
			xDic["value"] = vLu.replace("'","’")
			self._array.append(xDic)

			self.printIf("####### : "  + str(desc_))
			

		if isinstance(vDetails, dict):
			d = vDetails
			self.printIf("d = "+str(d))
			xInfo = {"app":d["app"],"table":d["table"],"request":[
					{"select":d["field"],"value":vLu.replace("'","’")}]
					}
			self.printIf("translation.py - readData_ - xInfo : " + str(xInfo))
			xKey,isAdded = self.add(xInfo)
			xDic["select"] = desc_["field"]
			xDic["value"] = xKey

			self._array.append(xDic)

