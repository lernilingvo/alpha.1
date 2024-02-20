#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""vocabulary.py: testing the lerni program."""

__author__ = "Henri Le Foll"
__copyright__ = "Copyright 2024"
__credits__ = ["Henri Le Foll"]
__license__ = "GPL"
__version__ = "3.0"
__maintainer__ = "Henri Le Foll"
__email__ = "lerni@gmail.com"
__status__ = "Prototype"

import os,sys,sqlite3,json,random
from datetime import datetime
from reader.param import Param
from controller.book import Book
from controller.sql import Sql
from controller.log import Log

class Vocabulary(Sql):

	def __init__(self,param_):

		super().__init__(param_)

		self._log = Log(param_)
		self._lesson = Book(self._param,self._param)

		self.printIf("Type : " + str(self._lesson._book["type"]))

		self._forget ="none"

		for aString in ["all","day","week"]:
			if self._param[aString]:
				self._forget = aString

		self._direction = "both"

		for aString in ["translation","reverse"]:
			if self._param[aString]:
				self._direction = aString

		self.printIf(self._forget + " "+self._direction)

		self._choices = ["not asked","errors"]

		self._isAll = False

		if self._param["all"] or self._param["card"] :
			self._isAll = True
		
		if self._param["all"]:
			self._choices = ["complete"]

		self._themes = [False,True]

		match self._direction:

			case "translation":
				self._themes = [False]

			case "reverse":
				self._themes = [True]

		#exit()

		self.setVocabulary()


	def save(self,selection_):
		self._log.save(selection_)
		

#-

	def setVocabulary(self):

		#self._param["theme"] = True
		self.clear()
		self.printIf("setVocabulary begin")
		aSelect = "vortuVorto_id"

		if self._lesson._book["type"] == "radical_decomposition":
			aSelect = "*"

		self._allWords = self._lesson.read(aSelect)
		self.printIf(self._allWords)
		isBreak = False
		self._listEx =[]

		for aTheme in self._themes:
	
			self.printIf("------------------------------------------------")
			self.printIf("setVocabulary for ")
			self.printIf("Break : "+str(isBreak))

			if isBreak:
				break

			for aChoice in self._choices:
				self.printIf("----------")
				self.printIf("Theme : "+str(aTheme))
				self.printIf("choice : "+str(aChoice))

				aResult = self.getPartialList(aChoice,aTheme)
				resRandom = aResult

				if not self._param["all"]:
					resRandom = random.sample(aResult,len(aResult))

				self.printIf(resRandom)
				#exit()

				if len(resRandom)>0:

					aDic = {"liste":resRandom,"theme":aTheme,"choice":aChoice}
					self._listEx.append(aDic)
					isBreak = True
					break

		self.printIf()
		self.printIf("### setVocabulary end ")
		self.printIf(self._listEx)
		#self.clear()
		if len(self._listEx) == 0:
			self.printIf()
			self.printIf(" Well done")
			self.printIf()
		#exit()

#-


#- 

	def getPartialList(self,param_,theme_):

		ret = []

		self.printIf("getPartialList - allWords : "+str(self._allWords))
		#self.printIf(self._allWords)
				
		for aTabElement in self._allWords:

			aData = self.getWord(aTabElement,param_,theme_,False)
			self.printIf("getPartialList - getWord : " + str(aData))
		

			if len(aData)>0:
				aPair = self.toPair(aData,theme_)
				self.printIf()
				self.printIf("getPartialList - aData : " + str(aData))
				self.printIf(aPair[0])

				dataFound = self.getWord(aPair[0],param_,theme_,True)

				self.printIf("getPartialList - after dataFound : " + str(aPair))

				if dataFound is None or self._isAll:
					ret.append(aPair)

				self.printIf(" ######")
				self.printIf("getPartialListe - ret : "+str(ret))
				

		self.printIf("getPartialListe - Fin : "+str(ret))
		self.printIf()
		#	exit()
		#exit()
		return ret

	def getList(self):
		
		return self._listEx

#- 

	def getWord(self,word_,param_,theme_,isControl):

		pQuestion = "vortarVorto_id"
		pResponse = "vortarTraduko_id"

		if theme_:
			pQuestion = "vortarTraduko_id"
			pResponse = "vortarVorto_id"

		endRequest = " AND " +  pQuestion
		subRequest = "SELECT demando from logs_log"

		if not isControl:
			endRequest += " NOT "

		aWord = self.extract(self._lesson._book["type"],word_)

		"""RESTE À RESTREINDRE sur L’utilisateur et la date (semaine)"""
		match param_:

			case "complete":
				endRequest = ""
				subRequest = ""
				isControl = False

			case "not asked":
				endRequest += " IN (" + subRequest +") "

			case "errors":
				subRequest += " WHERE error = 0"
				endRequest += " IN (" + subRequest +") "

		if isControl:
			endSubRequest = " demando = '" + word_ + "'"
			if "WHERE" in subRequest:
				 subRequest += " AND " + endSubRequest
			else:
				 subRequest += " WHERE " + endSubRequest
			return self.runSQL(subRequest,None)
			
		
		aSelect = pQuestion + "," + pResponse + ",vortarPrecizeco,vortarKomento"
		
		aTable = "t" + self._param["learn"] + self._param["home"] +"_vortaro"
		aDic = {"table":aTable,"select":aSelect,"where":"vortarVorto_id"+'  = "' + aWord + '"' + endRequest }

		return self.select(aDic,False)

#-

	def toPair(self,data_,theme_):

		self.printIf()
		#self.printIf(data_)
		aQuestion = ""
		aResponse = ""
		i = 0
		isComplex = False

		for anElement in data_:

			self.printIf(anElement)

			i +=1
			if i == 1:
				aQuestion = anElement[0]
				aFirst = aQuestion
			elif aFirst != anElement[0]:
				aQuestion += ","+anElement[0]

			if anElement[1] not in aResponse.strip(","):
				if i > 1:
					aResponse += ","
				aResponse += anElement[1]

			if self.isNotNone(anElement[2]) or self.isNotNone(anElement[3]):
				aQuestion += "("
				isComplex = True
				aQuestion = self.concat(aQuestion,anElement[2])
				aQuestion = self.concat(aQuestion,anElement[3])
				aQuestion += ")"

		self.printIf("aQuestion : " + str(aQuestion))
		self.printIf("aResponse : " + str(aResponse))
		return [aQuestion,aResponse]

		#if isComplex:
		#	exit()

#-

	def isNotNone(self,str_):
		
		if str_ is None:
			return False

		if len(str_) == 0:
			return False
		
		return True
#-

	def concat(self,ret_,str_):
		if str_ != None:
			ret_ += str(str_)
		return ret_

#-

	def extract(self,type_,tab_):

		if type_ == "word_list":
			self.printIf(tab_)
			return tab_
		elif 1 == 0:#plus tard (concatener les radicaux)
			aWord = ""
			for anElement in aTabElement:
				aWord += anElement[0]
		

	def getParam(self,str_):
		return str(self._param[str_])
