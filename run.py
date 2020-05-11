"""
Algo.py - MinMax - Find Min & Max Values
Version : 1.0.0
Author : Seyyed Ali Mojatabvi
Repository : 

"""
import os
import platform 
import sys
from  divid import minmax_divid

from input import array

platform_system = platform.system()

def clear_screen():
    if platform_system == 'Linux':
        os.system('clear')
    elif platform_system == 'Windows':
        os.system('cls')


while True:
    clear_screen()
    print("MinMax Algorithms: ")
    print(" Methods: ")
    print("     1- Divid & Conqure ")
    print("         Coming Soon ... \n ")
    print("     0- Exit ")
    try:
        option = int(input("Enter a number: "))
        if option < 0 or option > 1:
            raise Exception
    except:
        continue

    break

if option == 0:
    sys.exit(0)


a_min = a_max = None 

if option == 1:
    a_min,a_max = minmax_divid(0,(len(array)-1),array)

if a_min == None and a_max == None:
    print("Error !!!!")
else:
    print('Min = ',a_min)
    print('Max = ',a_max)
