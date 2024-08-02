#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""book.py: testing the lerni program."""

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
from .sql import Sql

class Book(Sql):

	def __init__(self , param_,book_):

		""" param_ must be a dictionnary with two keys : db and languages"""
		""" book_ must be a dictionnary with two keys : author and title """

		super().__init__(param_)
		self.initF("controller/book.py","__init__")

		self._book = book_
		self.restoreF()


	def save(self):

		self.initF("controller/book.py","save")
		if self._book["type"] == "radical_decomposition":
			return 0,False

		vInfo = {"app":"komuno","table":"autoro","request":[
			{"select":"nomo","value":self._book["author"],"type":"string"}
			]}
		self.add(vInfo)

		vInfo = {"app":"komuno","table":"titro","request":[
			{"select":"nomo","value":self._book["title"],"type":"string"}
			]}
		self.add(vInfo)
		
		
		vInfo = {"app":"komuno","table":"librejo","request":[
			#{"select":"id","value":"id","table":"komuno_librejo"}
			{"select":"libreAutoro_id","value":self._book["author"],"type":"string"}
			,{"select":"libreTitro_id","value":self._book["title"],"type":"string"}
			]}

		
		vKey,isAdded =  self.add(vInfo)

		self._book["bookId"] = vKey
		self.restoreF()

		return vKey,isAdded

#-

	def getData(self):

		self.initF("controller/book.py","getData")
		self.printIf("readBook : " + self._book["csv"])
		self.printIf()

		if not os.path.isfile(self._book["csv"]):
			print(" PB FILE : " + self._book["csv"] )
			sys.exit()

		with open(self._book["csv"],"r", newline='',encoding="utf-8") as file:
			raw = file.read().splitlines()
			data = csv.reader(raw, delimiter=';') #, quotechar='|')

		self.restoreF()

		return data
		

	def setKey(self):

		self.initF("controller/book.py","setKey")
		aRequete = ' libreAutoro_id = "' + self._book["author"] + '" AND libreTitro_id = "' + self._book["title"] +'"'
		self._book["bookId"] = self.getKey("komuno_librejo",aRequete)		

		self.printIf("------")
		self.printIf(self._book["bookId"])
		self.printIf("------")
		self.restoreF()

#-

	def read(self,select_):

		self.initF("controller/book.py","read")
		if "csv" in self._param.keys():
			data = self.getData()
			num = 0
			ret_all = "("
			for aLine in data:
				if num != 0:
					ret_all +=","
				ret_all += '"' + aLine[0]+'"'
				num += 1
			ret_all += ")"
			aTable = "l" + self._param["learn"] + "_radikopo"
			print(ret_all)
			print ("csv : " + self._param["csv"])
			aSelect = "radikopoVorto_id" 
			aWhere = "radikopoRadiko_id in " + ret_all
		else:
			self.setKey()
			aTable = "l" + self._param["learn"] + "_vortujo"
			aSelect = select_
			aWhere = "vortuLibre_id = " +  str(self._book["bookId"])
		self.printIf(aTable)
		reqBook = {"table":aTable,"select":aSelect,"where":aWhere}
		self.printIf("avant : "+str(reqBook))
		ret  =  self.select(reqBook)
		self.printIf(ret)
		self.restoreF()
		return  ret

	def delete(self):
		aRequest = "delete from " + self._appt +"_vortaro WHERE vortarLibrejo_id = " + str(self._book["bookId"])		
		self.runSQL(aRequest)
		aRequest = "delete from komuno_librejo WHERE id = " + str(self._book["bookId"])		
		self.runSQL(aRequest)
		self._con.commit()
