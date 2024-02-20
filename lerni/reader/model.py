#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""model.py: testing the lerni program."""

__author__ = "Henri Le Foll"
__copyright__ = "Copyright 2024"
__credits__ = ["Henri Le Foll"]
__license__ = "GPL"
__version__ = "3.0"
__maintainer__ = "Henri Le Foll"
__email__ = "lerni@gmail.com"
__status__ = "Prototype"

import os,sys
import gettext,json
from .read import Read

class Model(Read):

	def __init__(self ,file_,name_=""):

		super().__init__(name_,file_)
		self.controlJsonModel()


#-

	def controlJsonModel(self):

		for element in self._json:
			if False:
				print("MODEL "+str(element),file = self._debug)

		return True
