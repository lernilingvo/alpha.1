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

import argparse,sys
from reader.parameters import Parameters
from controller.reload import Reload
from controller.book import Book

class Parser():

	def __init__(self):

		parser = argparse.ArgumentParser(description="reload the init files")
		#parser.add_argument("--reset",action="store_true",help="delete everything")
		subparsers = parser.add_subparsers(dest = "command")
		drop = subparsers.add_parser("drop" , help = "delete everything")
		reset = subparsers.add_parser("reset" , help = "delete everything and reload")
		delete = subparsers.add_parser("delete" , help = "delete a book")
		delete.add_argument("-a","--author" , type = str , required = True , help = "name of the author")
		delete.add_argument("-t","--title" , type = str , required = True , help = "title of the book")
		self._args = parser.parse_args()
		

def main():

	print()
	print(" svl doit être activé")
	print()

	conf =  Parameters({"debug":False,"debugFile":None})
	reload = Reload(conf)

	parser = Parser()

	if parser._args.command in ["drop","reset"]:
		print("reset complet")
		reload.deleteTables(True)

	if parser._args.command == "delete":
		param = conf.param()
		param["author"] = parser._args.author
		param["title"] = parser._args.title
		aBook = Book(param,param)
		aBook.setKey()
		aBook.delete()
		reload.loadFiles()
		exit()

	if parser._args.command not in ["drop"]:
		reload.loadFiles()

	print()
	print(" Fin")
	print()

main()
