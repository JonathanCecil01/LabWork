# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 11:39:19 2022

@author: 20PT12
"""
import matplotlib
import matplotlib.pyplot as plt
rect = matplotlib.patches.Rectangle((.25, .25), .25, .5, angle=0)
plt.gca().add_patch(rect)
plt.draw()
rect = matplotlib.patches.Rectangle((.25, .25), .25, .5, angle=20, color = 'red')
plt.gca().add_patch(rect)
plt.draw()