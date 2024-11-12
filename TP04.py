import matplotlib.pyplot as plt
import numpy as np 

def f1(x) :
    return (x+1)**2 + 7*np.sin(x)
"""
def minimumDichotomie(f,x_min,x_max,precision):
    x_centre = (x_max+x_min)/2
    epsilon= np.abs (x_max-x_min)
    nb_it=0
    Erreur = True
    bornes_inf = []
    bornes_sup = []
    while epsilon>precision:
        x_centre = (x_max+x_min)/2
        bornes_inf.append(x_min)
        bornes_sup.append(x_max)
        f_centre = f(x_centre)
        f_min = f(x_min)
        f_max = f(x_max)
        if f_centre * f_max  > 0 :
            x_max = x_centre
        else: 
            x_min=x_centre
        
        epsilon= np.abs (x_max-x_min)
        nb_it +=1
    Erreur = False    
    return  bornes_inf,bornes_sup,nb_it,Erreur

"""
#%%
#MÃ©thode de dichotomie
#%%
"""

def minimumDichotomie(f,x_min,x_max,precision):
    listex_inf =[]
    listey_inf =[]
    listex_sup =[]
    listey_sup =[]
    Erreur = False
    while x_max-x_min>precision:
        listex_inf.append(x_min)
        listey_inf.append(f(x_min))
        listex_sup.append(x_max)
        listey_sup.append(f(x_max))
        
       
        x1 = x_min
        x5= x_max
        x3= (x1+x5)/2
        x2= (x1+x3)/2
        x4= (x3+x5)/2
        
        
        if f(x1) > f(x2) > f(x3) > f(x4) > f(x5):
            x_min =x4
            x_max =x5       
        elif f(x1) < f(x2) < f(x3) < f(x4) < f(x5):
            x_min =x1
            x_max =x2  
        elif f(x1) > f(x2) > f(x3) < f(x4) < f(x5):
            x_min =x2
            x_max =x4 
        elif f(x1) > f(x2) > f(x3) > f(x4) < f(x5):
            x_min =x3
            x_max =x5 
        elif f(x1) > f(x2) < f(x3) < f(x4) < f(x5):
            x_min =x1
            x_max =x3
        
        else:
            Erreur = True
            break
        
        x_centre = (x_max+x_min)/2
        epsilon= np.abs (x_max-x_min)
        nb_it=0
        nb_it +=1
        
    bornes_inf = [listex_inf,listey_inf]
    bornes_max = [listex_sup,listey_sup]
       
        
        
    
    print(bornes_inf)
    print("######################################")
    print(bornes_max)
        
    return  bornes_inf,bornes_max,nb_it,Erreur



#%% Recherche du minimum de f1 sur l'intervalle [-4,4]
#%%
x_min = -4
x_max = +4

f = f1
precision = 1e-1
# METHODE minimumDichotomie A CREER
bornes_min, bornes_max, n_iter, ier = minimumDichotomie(f,x_min,x_max,precision)
#
x_min, y_min = bornes_min[0][-1], bornes_min[1][-1]
x_max, y_max = bornes_max[0][-1], bornes_max[1][-1]

# Visualisation des rÃ©sultats
plt.plot(bornes_min[0],bornes_min[1],'rs', label = 'x_min')
plt.plot(bornes_max[0],bornes_max[1],'bs', label = 'x_max')
plt.legend()
plt.xlabel('Valeurs de $x$')
plt.ylabel('Valeurs de $f_1(x)$')
plt.title('Recherche du minimum de $f_1$ par dichotomie')
plt.grid()

message = 'Precision = {}'.format(precision)
message += '\nCV en {} iterations'.format(n_iter)
message += '\nBorne infÃ©rieure :'
message += '\n  x_min = {:6.4f}'.format(x_min)
message += '\n  y_min = {:6.4f}'.format(y_min)
message += '\nBorne supÃ©rieure :'
message += '\n  x_max = {:6.4f}'.format(x_max)
message += '\n  y_max = {:6.4f}'.format(y_max)
plt.text(1,-5,message)
print(n_iter)
"""
#%%
#MÃ©thode de Newton 

#%%
f = f1
x0=-4
def NewtonMin(f,df1,df2,x0,precision,iter_max):
    epsilon = 10
    nb_iter = 0
    Erreur = False
    while epsilon> precision and nb_iter<iter_max:
        Vderiv1 = df1(x0)
        Vderiv2 = df2(x0)
        try:
            solution = x0 - (Vderiv1/Vderiv2)
        except ZeroDivisionError:
            Erreur = True
            break
        epsilon = np.abs(solution-x0)
        x0=solution
        nb_iter+=1
        
    
    
    return solution,nb_iter,Erreur


def df1(x):
    return 2*(x+1) + (7*np.cos(x))
def df2(x):
    return 2-(7*np.sin(x))

precision = 1e-1
iter_max = 10
solution,nbiter,erreur = NewtonMin(f, df1, df2, x0, precision, iter_max)
print(solution)
print(nbiter)


















# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:25:15 2020

UE MU4MEN01 - Introduction Ã  l'optimisation

Programme cadre pour le TP nÂ°2

@author: Florence Ossart, Sorbonne UniversitÃ©
"""

#%% Programme de test de la recherche de minimum par dichotomie

#%% Fonction test nÂ°1
def f1(x) :
    return (x+1)**2 + 7*np.sin(x)





