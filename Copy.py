# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 20:55:43 2018

@author: Administrator
"""
import copy
origin = [1, 2, [3, 4]]
#origin 里边有三个元素：1， 2，[3, 4]
cop1 = copy.copy(origin)
cop2 = copy.deepcopy(origin)
cop1 == cop2

cop1 is cop2


