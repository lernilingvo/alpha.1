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

#self.addAro #créer des objets Book, translationBook...
import argparse,csv,os,sys
import gettext,json
from .sql import Sql
from .book import Book
from .translation import Translation


class Read(Sql):

	def __init__(self , conf_):

		super().__init__(conf_.param())

		self._file = "read.py"
		self._function = "__init__"

		self._conf = conf_

		print()

#-

	def deleteTables(self,all_ = False):

		deletedApps = [{"name":"leo","tables":["vortujo"]}
						,{"name":"lja","tables":["vortujo"]}
						,{"name":"komuno","tables":["librejo","vortaro","autoro","titro","pozicio"]}]

		if all_:
			deletedApps = self._conf.getApps()

		print()
		print(deletedApps)
		print()
		
		for anApp in deletedApps:
			print(anApp)
			for table in anApp["tables"]:
				self.delete(anApp["name"] + "_" + table)		
		print()
#-

	def loadFiles(self):

		for book in self._param.get("csvs"):

			print("#### loadFiles")
			print(book)
			aBook = self.getBook(book)
			if aBook.save():
				aBook.read()
			else:
				print("déjà dans la base")

	def getBook(self,book_):

		print(book_["type"])
		print()
		print()
		print("APPS")

		match book_["type"]:

			case "word_translation_ordered"|"radical_translation"|"word_translation_minimal":
				return Translation(self._param,book_,self._conf.getStructure(book_["type"]))

			case "word_list"|"radical_decomposition":
				return Translation(self._param,book_,self._conf.getStructure(book_["type"]))
 
		print("Book type not known : " + book_["type"])
		exit()
