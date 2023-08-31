#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 11:37:40 2023

@author: samuelfrachon
"""

#Library imports

import numpy as np
import matplotlib.pyplot as plt
#Variables

n = 3
t_max = 10

A = np.zeros((n,n)) #matrice_of_techniques
se = np.zeros(n) #sales_expectation
v = np.zeros((n,n)) #raw_material_inventories
m = np.zeros((n,n)) #raw_material_orders
z = np.zeros(n) #product_inventories
x = np.zeros(n) #production
s = np.zeros((t_max,n)) #sales
l = np.zeros(n) #buffer_coefficient_raw_material
k = np.zeros(n) #buffer_coefficient_product


#Matrice of techniques
A = np.array([[0,0.6,0.2],[0.25,0,0.55],[0.3,0.45,0]])

d = np.array([95,120,100]) # la demande finale

def spectral_radius(M): #frobenius root
    eigen_values,eigen_vectors = np.linalg.eig(M)
    return max(np.absolute(eigen_values))




# Séquence :
# 1. Actualisation de z
z = z + x - s[0] #si toutes les ventes ont pu être satisfaite, possibilité de rupture
# 2. Actualisation des expectations et commandes
m = se * (np.identity(n)+np.diag(l)) * A - v
# 3. Arrivée du matériel et lancement de la production
x = se * (np.identity(n)+np.diag(k)) - z #prévision de la production
v = v + m - A*x # s'il y a assez d'inventaire, possibilité de rupture
# 4. La production a lieu


