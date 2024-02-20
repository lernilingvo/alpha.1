#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""test_crud.py: testing the lerni program."""

__author__ = "Henri Le Foll"
__copyright__ = "Copyright 2024"
__credits__ = ["Henri Le Foll"]
__license__ = "GPL"
__version__ = "3.0"
__maintainer__ = "Henri Le Foll"
__email__ = "lerni@gmail.com"
__status__ = "Prototype"

import io,os,pytest,unittest,sys
from unittest.mock import patch,MagicMock

from lerni.json.jsoncontrol import JsonControl


class TestJsonControl(unittest.TestCase):

	def setup_class(self):
		self._add = JsonControl(["prog","tests/json/default.json"])


	def testArgvDefault(self):
		add = JsonControl(["prog","tests/json/default.json"])
		filename = add.getFilename()
		self.assertEqual(filename,"tests/json/default.json")


	def testArgvVide(self):
		sys.argv = []
		add = JsonControl()
		filename = add.getFilename()
		self.assertEqual(filename,os.environ["HOME"]+"/lerni.param.json")

	def testGetJsonDefault(self):
		json = self._add.getJson("tests/json/default.json")	
		print(json)


	def testGetJsonVide(self):
		json = self._add.getJson("tests/json/vide.json")	
		print(json)


	def testIsKeyVide(self):
		self._add = JsonControl(["prog","tests/json/vide.json"])
		self.assertEqual(self._add.isKey("default"),False)


	def testIsKeyDefault(self):
		self._add = JsonControl(["prog","tests/json/default.json"])
		self.assertEqual(self._add.isKey("default"),True)
		

	@unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
	def test_print(self, mock_stdout):
		self._add.print("Hello")
		self.assertEqual(mock_stdout.getvalue(),
			'\nHello\n\n')

"""
	@unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
	def test_add(self, mock_stdout):
		
		self._add = JsonControl()
		self.assertEqual(mock_stdout.getvalue(),
		'\nfilename is missing\n\n')
		#'\nWelcome\n')

	#def testGetJson(self,monkeypatch):
		#mock_file = MagicMock()
		#mock_file.readLine = MagicMock(return_value="test line")
		#mock_open = MagicMock(return_value)
		
		
		#with pytest.raises(SystemExit) as sample:
		#	assert sample.type == SystemExit  
		#self._add = JsonControl()
		#self.assertEqual(
		#	mock_stdout.getvalue(),
		#	'\n paramètre manquant : langue (fr/en)\n\n'  # It's important to remember about '\n'
		#)
"""		
