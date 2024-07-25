#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""reload.py: testing the lerni program."""

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
from controller.read import Read
from controller.book import Book

class Parser():

	def __init__(self):

		self._liste = ["--help","debug","delete","drop","reset"]
		parser = argparse.ArgumentParser(description="read the init files")
		#parser.add_argument("--reset",action="store_true",help="delete everything")
		subparsers = parser.add_subparsers(dest = "command")
		debug = subparsers.add_parser("debug" , help = "debug in file")
		drop = subparsers.add_parser("drop" , help = "delete everything")
		reset = subparsers.add_parser("reset" , help = "delete everything and read")
		delete = subparsers.add_parser("delete" , help = "delete a book")
		delete.add_argument("-a","--author" , type = str , required = True , help = "name of the author")
		delete.add_argument("-t","--title" , type = str , required = True , help = "title of the book")
		self._args = parser.parse_args()

		if not self._args.command in self._liste:
			print(" il faut passer un argument parmi : "+str(self._liste))
			print()
			exit()
		

def main():

	print()
	print(" svl doit être activé")
	print()

	conf =  Parameters({"debug":False,"debugFile":None})
	read = Read(conf)
	param = conf.param()
	param["debug"] = False

	parser = Parser()

	if parser._args.command in ["drop","reset"]:
		print("reset complet")
		read.deleteTables(True)

	if parser._args.command == "debug":
		os.system("mv debug_* sos")
		vNow = datetime.datetime.now()
		vTmp = str(vNow.year) + "." + str(vNow.month).zfill(2) + "." + str(vNow.day).zfill(2)
		vTmp += "_" + str(vNow.hour).zfill(2) + "." + str(vNow.minute).zfill(2) + "." + str(vNow.second).zfill(2)
		debugFilename = os.getcwd() + "/debug_" + vTmp + ".log"

		f = open(debugFilename, 'w+')

		print()
		print(debugFilename)
		print()
		print(param,file=f)
		param["debugFile"]=f
		param["debug"] = True

	if parser._args.command == "delete":
		param["author"] = parser._args.author
		param["title"] = parser._args.title
		aBook = Book(param,param)
		aBook.setKey()
		aBook.delete()
		read.loadFiles()
		exit()

	if parser._args.command not in ["drop"]:
		read.loadFiles()

	print()
	print(" Fin")
	print()

main()
