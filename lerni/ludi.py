#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ludi.py: testing the lerni program."""

__author__ = "Henri Le Foll"
__copyright__ = "Copyright 2024"
__credits__ = ["Henri Le Foll"]
__license__ = "GPL"
__version__ = "3.0"
__maintainer__ = "Henri Le Foll"
__email__ = "lerni@gmail.com"
__status__ = "Prototype"

import argparse,datetime,os,sys
from reader.parameters import Parameters
from game.game import Game

class Parser():

	def __init__(self,version_):

		self._independantArguments = {"card":"just ask, don’t memorize"
				,"debug":"display debug information"
				,"version":"version of the software"
			}

		self._orderedArguments = {
				"random":"only random"
				,"order":"only ordedered"
		}

		forgetArguments = {
			"all":"ask all the questions"
			,"day":"remember only the questions of the day"
			,"week":"remember only the questions of the week"
		}

		self._directionArguments = {
				"reverse":"only reverse translation"
				,"translation":"only translation"
			}

		self._parser = argparse.ArgumentParser(description="ask a question")

		self.addMutuallyExclusive(self._directionArguments)
		self.addMutuallyExclusive(forgetArguments)
		

		for aName in self._independantArguments:
			anArg = "--" + aName
			self._parser.add_argument(anArg,action="store_true",help=self._independantArguments[aName])

		#self._args = self._parser.parse_args(self._directionArguments)
		self._args = self._parser.parse_args()

		if self._args.version:
			print()
			print(version_)
			print()
			exit()

	def addMutuallyExclusive(self,arguments_):	

		aGroup = self._parser.add_mutually_exclusive_group()

		for aName in arguments_:
			anArg = "--" + aName
			aGroup.add_argument(anArg,action="store_true",help=arguments_[aName])

def main():


	version = "alfa.0.1"

	print()
	print(" svl doit être activé")
	print()

	parser = Parser(version)

	aDic = {}
	aDic["all"] = parser._args.all
	aDic["day"] = parser._args.day
	aDic["week"] = parser._args.week
	aDic["card"] = parser._args.card
	aDic["debug"] = parser._args.debug
	aDic["reverse"] = parser._args.reverse
	aDic["translation"] = parser._args.translation
	aDic["version"] = parser._args.version
	#aDic["random"] = parser._args.random
	aDic["dfn"]="debug.txt"
	aDic["debugFile"] = None

	

	if  parser._args.debug:

		vNow = datetime.datetime.now()
		vTmp = str(vNow.year) + "." + str(vNow.month).zfill(2) + "." + str(vNow.day).zfill(2)
		vTmp += "_" + str(vNow.hour).zfill(2) + "." + str(vNow.minute).zfill(2) + "." + str(vNow.second).zfill(2)
		debugFilename = os.getcwd() + "/debug_" + vTmp + ".log"

		f = open(debugFilename, 'w+')

		print()
		print(debugFilename)
		print()
		print(aDic,file=f)
		aDic["debugFile"]=f


	conf =  Parameters(aDic)
	param = conf.get("lessons")
	param.update(aDic)
	param["db"] = conf.get("db")
	print(param["db"] )
	param["languages"] = conf.get("languages")

	if  parser._args.debug:
		print(file=f)
		print(param,file=f)
		print("param : " + str(param),file=f)
		print(file=f)

	game = Game(param)

main()
