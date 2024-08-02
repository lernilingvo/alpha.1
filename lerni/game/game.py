#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""game.py: testing the lerni program."""

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
from .vocabulary import Vocabulary

class Game(Sql):

	def __init__(self,param_):

		self._file = "game.py"
		self._boucle = "."
		self._function = "__init__"
		self._param = param_

		if "debug" in self._param.keys():
			self._debug = self._param["debug"]

		self._vocabulary = Vocabulary(param_)

		self.printIf("--- liste :" + str(self._vocabulary.getList()))
		for anElement in self._vocabulary.getList():
			self.lesson(anElement["liste"],anElement["theme"])

#-
		
	def lesson(self,tEx_,isTheme_):

		vNbOk = 0
		vNbEr = 0
		tErrors = []

		self.clear()

		for elem in tEx_:

			#vColorSuccess = '\x1b[0m'
			vColorSuccess = '\033[93m' #yellow
			vColorSuccess = '\033[92m' #green
			vColorError = '\033[91m'
			vColorNormal = '\033[97m'
			vColorNormal = '\x1b[0m'
			vEol ="\n"

			vTypeTranslation = " from " + self._vocabulary.getParam("learn") +"  To " + self._vocabulary.getParam("home")
			vOrder = " (ordered) "
			vStrQuit = "  , $ to quit "
			vQuestion = elem[0].strip()
			vSolution = elem[1].strip()

			if isTheme_:
				vOrder = " (Thème) "
				vTypeTranslation = " from " + self._vocabulary.getParam("home") +"  To " + self._vocabulary.getParam("learn")
				#vTemp = vQuestion
				#vQuestion = vSolution
				#vSolution = vTemp

			print()
			vSolutionTestee = self.replace(vSolution)
			mTraduction = input(vColorNormal + " Translate : "+ vQuestion + " - ")

			if mTraduction == "$":
				print()
				exit()

			self.clear()
			vStar =""
			vOk = 0

			if vNbEr == 0:
				vStar = " ** "
			
			if mTraduction in vSolutionTestee.split(","):
				vNbOk += 1
				vColor = vColorSuccess
				vResultat = vStar+" Congratulations !  "+vStar+"(" +  str(vNbOk) + ") : " + vSolution
			else:
				vOk = 1
				vNbEr += 1
				tErrors.append([vQuestion,vSolution])
				#tEx_.append([vQuestion,vSolution])
				vColor = vColorError
				vResultat = " ------- To bad ----  (" + str(vNbEr) +") : " + vEol + vEol
				vResultat = "Your answer was : " + mTraduction + vEol + vEol
				vResultat += " the translation of '" + vQuestion + "' was : " + vSolution +" (" + str(vNbEr)+")"

			print(vColor)
			print("------------------------------------")
			print()
			print(vResultat)
			print()
			print("------------------------------------")
			print()
			aSelect = []
		
			aTime = datetime.now()		
			aSelect.append({"select":"time","value":str(aTime),"type":"string"})
			aSelect.append({"select":"uzanto_id","value":"h","type":"string"})
			aSelect.append({"select":"libro_id","value":"1","type":"string"})
			aSelect.append({"select":"demando","value":vQuestion,"type":"string"})
			aSelect.append({"select":"respondo","value":mTraduction,"type":"string"})
			aSelect.append({"select":"solution","value":vSolutionTestee,"type":"string"})
			aSelect.append({"select":"error","value":str(vOk),"type":"integer"})

			if not self._vocabulary._param["card"]:
				self._vocabulary.save(aSelect)

		print()
		print("========================")
		print()
		print(" Résultat : ")
		print()

		if vNbEr == 0:
			print("Félicitation : aucune erreur")
		else:
			print(" Résultat Correctes : " + str(vNbOk))
			print()
			print(" Erreurs : " + str(vNbEr) + "(" + str(tErrors) + ")")
		print()

#-

	def replace(self,str_):

		str_ = str_.replace("ŭ","u")
		str_ = str_.replace("ĉ","c")
		str_ = str_.replace("ĝ","g")
		str_ = str_.replace("ĵ","j")
		str_ = str_.replace("ŝ","s")
		str_ = str_.replace("’","'")

		return str_
