#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""sql.py: testing the lerni program."""

__author__ = "Henri Le Foll"
__copyright__ = "Copyright 2024"
__credits__ = ["Henri Le Foll"]
__license__ = "GPL"
__version__ = "3.0"
__maintainer__ = "Henri Le Foll"
__email__ = "lerni@gmail.com"
__status__ = "Prototype"

import os,sys,sqlite3,json
from reader.param import Param

class Sql:

	def __init__(self,param_):
		""" param_ must be a dictionnary with two keys : db and languages"""

		self._param = param_
		self._debug = param_["debugFile"]

		self.printIf()
		self.printIf(self._param)
		self.printIf()

		vLanguages = param_["languages"]
		self._param["learn"] = vLanguages["learn"]
		self._param["home"] = vLanguages["home"]
		if "LOG" in os.environ:
			self._log = os.environ["LOG"]
		else:
			self._log = "False"
		self._language = vLanguages["learn"]
		self._db = param_["db"]
		self.initDB()

	def initDB(self):

		self._nb = 0
		self._appLearn = "l" + self._language
		self._appTranslate = "t" + self._language + self._param["home"]
		self._appHome = "l" + self._param["home"]
		self._con = sqlite3.connect(self._db)

		try:
			self._cur = self._con.cursor()
			print(" Connexion à la base OK !")
		except Exception as ex:
			print(" PB de connexion à la base ")

	def printIf(self,signoj_=""):
		if self._param["debug"]:
			print(file=self._debug)
			print(" "+str(signoj_),file=self._debug)
			print(file=self._debug)


	def getKey(self,table_,where_=""):

		vId = "id"
		
		
		self.printIf(table_)

		aTable = table_.split("_")[1]

		self.printIf(aTable)

		#if table_ in  ["komuno_autoro","komuno_titro","komuno_pozicio","leo_vorto","lfr_vorto","leo_radikejo"]:
		if aTable in  ["autoro","titro","pozicio","vorto","radikejo"]:
			vId = "nomo"

		if where_ != "":
			where_ = " WHERE " + where_

		aRequest = "SELECT " +  vId + " FROM " + table_ + " " + where_ + " ORDER BY " +  vId + " DESC limit 1"

		return self.runSQL(aRequest)

		if fe == None:
			return 0
			print(" PB : " + aRequest)

		return fe[0]

#-

	def  runSQL(self,request_,ret_=0):

		self.printIf("runSQL: " + request_)

		res = self._cur.execute(request_)
		fe = res.fetchone()
		felen = 0 

		if fe != None :
			return fe[0]

			self.printIf("runSQL - ret : " + str(felen) + " " + str(fe))

		return ret_

#-

	def add(self,info_):

		isAdded = False

		anApp = info_["app"]

		match info_["app"]:
			case "home":
				anApp = self._appHome
			case "learn":
				anApp = self._appLearn
			case "translation":
				anApp = self._appTranslate

		aTable = anApp + "_" + info_["table"]
		aSelect = self.partialSQLRequest("select",info_["request"],'"')
		columns = self.partialSQLRequest("columns",info_["request"],'"')
		values = self.partialSQLRequest("value",info_["request"],'"')

		aRequest = "SELECT  * FROM " + aTable + " WHERE " + aSelect
		self.printIf(aRequest)
		self.printIf("values : "+str(values))

		if self.runSQL(aRequest) == 0:

			aRequest = "INSERT INTO " + aTable + " (" + columns + ") VALUES (" + values + ")"

			self.printIf()
			self.printIf(" - add : " + aRequest)
			self.printIf()
			self.printIf (" requ : "+str(aRequest))

			self.runSQL(aRequest)
			self._con.commit()
			isAdded = True
		else:
			self.printIf()
			self.printIf("add - résultat : "+aRequest+" pas d’insert de "+values) 
			self.printIf()
		return self.getKey(aTable,aSelect),isAdded

#-

	def delete(self,table_):
		aRequest = "DELETE FROM "+table_
		self.runSQL(aRequest)
		self._con.commit()
		aRequest = "UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='" + table_ + "';"
		self.runSQL(aRequest)
		self._con.commit()
		self.printIf(table_+" deleted")

#-

	def partialSQLRequest(self,type_,array_,separator_):

		nb = 0
		ret = ""	
		quote = separator_
		separator = {"value":",","select":" AND ","columns":","}
		#print(array_)

		if type_ in ["value","columns"]:
			ret = quote

		for element in array_:

			element["columns"] = element[type_]
			self.printIf(element)

			if "type" in element.keys():
				if element["type"] == "integer" and type_ == "value":
					quote = ""
					self.printIf("quote : "+str(ret))

			nb += 1

			if nb > 1:
				ret +=	separator[type_]

				if type_ in  ["value","columns"]:
					ret += quote

			if element[type_] == "id" and type_== "value":

				aTable = element["table"]
				aRequest = "SELECT id FROM " + aTable + " ORDER BY id DESC limit 1"

				self.printIf()
				self.printIf("### aRequest")
				self.printIf(aRequest)

				self._id = str(self.getKey(aTable)+1)
				values = self._id 
				self.printIf(values)
				ret += str(values)

			else:

				ret += str(element[type_])

			if type_ == "select":

				ret += ' == '+ quote + element["value"] 

			#ret += "' "
			ret += quote

		return ret

#-

	def select(self,info_,concat_=True):	
	
		tab = []

		aRequest = " SELECT " + info_["select"]
		aRequest += " FROM " + info_["table"]

		if len(info_["where"]) > 1:
			aRequest += " WHERE " + info_["where"]

		self.printIf("select : "+str(aRequest))
	
		aResult = self._cur.execute(aRequest)

		if concat_:

			for aRow in self._cur.execute(aRequest):
				for anElement in aRow:
					tab.append(anElement)

		else:

			for aRow in self._cur.execute(aRequest):
				tab.append(aRow)
		
		return tab

		#nb = 0
		#elem = " "
		#if nb == pos:
		#	tab = elem.split(",")

#-

	def clear(self):

		print(sys.platform.startswith('win'))

		if sys.platform.startswith('win'):
			os.system("cls")	
		else:
			os.system("clear")	

