from pylab import*
from scipy.io import wavfile
import matplotlib.pyplot as plt


# OJO CON LOS TYPES
Fs = 1000
dt = 1/Fs
print "Fs es tipo: " + str(type(Fs))
print "dt es tipo: " + str(type(dt))

dt = 1.0/Fs
print "dt es tipo: " + str(type(dt))

Fs = 1000.0
dt = 1/Fs
print "Fs es tipo: " + str(type(Fs))
print "dt es tipo: " + str(type(dt))

## Para no perder precision, es buena idea utilizar .0 para forzar a que el tipo sea floar
#

Fs = 1000.0
dt = 1/Fs

## vectores (estas funciones al parecer son del paquete numpy)
t = arange(0,1,dt)  # matlab: x = 0:dt:1    # Incluye el 0, excluye el 1. 
print "El tipo de t es: " + str(type(t))    #numpy.ndarray
print "El largo de t es: " + str(len(t))	# 1000
print "El ultimo elemento: " + str(t[-1]) 	# 0.999

## Index $ slicing de vectores

# Se parte del 0
print "El primer elemento de t es: " + str(t[0])

# El ultimo es elemento len(vector)-1
print "El ultimo elemento de t es: " + str(t[len(t)-1])

# Se pueden acceder similar a Matlab
print "Varios elementos de t: " + str(t[0:10])

# Incluso con steps, pero diferente sintaxis (elemento inicial (incluyente):elemento final (excluyente):step)
print "Varios elementos usando steps: " + str(t[0:10:2])

## Operaciones de ndarrays
A = arange(0,100.0,1)
B = arange(100,200.0,1)
# Suma
print "Suma de ndarray: " + str(type(A+B))   #ndarray!
print "A[0] + B[0] = (A+B)[0]?: " + str(A[33]) + ' + ' + str(B[33]) + ' = ' + str((A+B)[33])
# Multiplicacion por escalar
print "Multiplicacion por escalar: 3*A[end] = " + str((3*A)[-1]) 

# Funciones
C = np.sin(2*0.1*A)
print "C = sin(2*0.01*A). Type(C): " + str(type(C))
plt.plot(C)
# plt.show()  #Solo para verificar!

# Vectores de zeros o unos
C = np.zeros(5)
print "C = np.zeros(5): " + str(C) + " tipo: " + str(type(C))
B = np.ones(5)
print "B = np.ones(5): " + str(B) + " tipo: " + str(type(B))

B = np.ones(5)
print "Verificacion de tipos por division: B = np.ones(5)/5: " + str(B/5) + " tipo: " + str(type(B/5))

# MATRICES
A = arange(0,5.0,1)
H = [A,A]
print "H = [A,A]: " + str(H) + " tipo: " + str(type(H))   #Se pierde el tipo! Asi solo se es un tipo basico de python

H = np.array([A,A])
print "H = np.array([A,A]): " + str(H) + " tipo: " + str(type(H))

# Slicing de matrices
J = H[:,:]
print "J = H[:,:] " + str(J) + " tipo: " + str(type(J))

J = H[1,:]
print "J = H[1,:] " + str(J) + " tipo: " + str(type(J))   #Fila de indice 1, todas las columnas

J = H[:,2]
print "J = H[:,2] " + str(J) + " tipo: " + str(type(J))   #Todas las filas, columna de indice 2
# Aca se ve que la representacion de un vector no tiene direccion. Es decir puede ser fila o columna. 
# Realmente no importa ya que es unidimensional. Es por esto que se puede hacer multiplicacion de vectores
# aunque no tenga consistencia con la algebra matricial.  

#multiplicacion de matrices
I = np.array([A,A,A])
print "I = np.array([A,A,A]): " + str(I) + " tipo: " + str(type(I))
Y = np.transpose(I)
print "Y = np.transpose(I): " + str(Y) + " tipo: " + str(type(Y))
try:
	K = H*I
except:
	print "Error: la multiplicacion de matrices tiene que respetar el algebra lineal, a menos que tengan el mismo shape"

L = np.ones([2,2])
print L
P = L+L
M = L*P
print "Error: La multiplicacion de matrices al parecer siempre es element-wise"
print M
N = np.dot(L,P)
print N
print "Para multiplicar matrices, es mejor usar np.dot()"
T = np.dot(I,Y)
R = np.dot(Y,I)
print T
print R
print "Confirmamos que la multiplicacion de matrices no es conmutativa!"


# Multiplicacion punto a punto
A = arange(0,5.0,1)
C = np.multiply(A,(B+B))
print "C = A.*(2*B): " + str(C) + " tipo: " + str(type(C))

# Division punto a punto
C = np.divide(A,(B+B))
print "C = A./(2*B): " + str(C) + " tipo: " + str(type(C))

# Potencia element-wise

# Esto funciona aunque no tenga consistencia dimensional. 
C = A*A
G = H*H 
print "C = A*A: " + str(C) + " tipo: " + str(type(C))
print "G = H*H: " + str(G) + " tipo: " + str(type(G))

# Esto es realmente un shorthand de lo anterior (?)
C = A**2
G = H**2
print "C = A**2: " + str(C) + " tipo: " + str(type(C))
print "G = H**2: " + str(G) + " tipo: " + str(type(G))

# Una forma explicita de decir que se esta elevando cada elemento al cuadrado:
C = np.square(A)
G = np.square(H)
print "G = np.square(H): " + str(G) + " tipo: " + str(type(G))


# Numeros aleatorios
R = np.random.rand(2,2)	#distribucion uniforme [0,1)
print R
R = np.random.randn(3,3)  #distribucion normal norm(mu=0, sigma=1)
print R

# print "" + str()