#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2012-07 xGeek
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

class Addr(int):
   """Used to represent adresses"""

   def __init__(self, arg):
      self.int = arg

   def __str__(self):
      return hex(self.int)

   def __add__(self,n):
      datatype = type(n)
      if datatype == Addr:
         return Addr(self.int + n.int)
      elif datatype == int:
         return Addr(self.int + n)
      else:
         raise TypeError("Only 'int' or 'Addr' can be added")

