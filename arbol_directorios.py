# ----------------------------------------------
# LISTAR LOS ARCHIVOS DE UN DIRECTORIO
# ----------------------------------------------
# leoparada.com@gmail.com

# Scaneo de directorios
import os
# Dibujo en codigo ACII de la estructura de arbol 
from rptree.rptree import DirectoryTree

path = './'

#LOS ARCHIVOS Y ARCHIVOS DEL NIVEL 
print ('')
print ('')
print ('-------------------------------------------------------------------')
print ('LOS FICHEROS Y ARCHIVOS DEL NIVEL ---------------------------------')
print ('-------------------------------------------------------------------')
with os.scandir(path) as ficheros:
    for fichero in ficheros:
        print(fichero.name)

print ('-------------------------------------------------------------------')
print ('')
print ('')

#TODOS LOS ARCHIVOS
print ('-------------------------------------------------------------------')
print ('TODOS LOS FICHEROS Y ARCHIVOS DEL ARBOL DE FICHEROS ---------------')
print ('-------------------------------------------------------------------')

for base, dirs, files in os.walk(path):
    print (base)
    print (dirs)
    print (files)
    print ('-------------------------------------------------------------------')
    print ('')


print ('')
print ('')
print ('-------------------------------------------------------------------')
print ('EL ARBOL DE DIRECTORIOS -------------------------------------------')
print ('-------------------------------------------------------------------')
tree = DirectoryTree(path)
tree.generate()
