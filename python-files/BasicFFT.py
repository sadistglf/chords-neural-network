from pylab import*
import matplotlib.pyplot as plt

Fs = 1000.0
dt = 1/Fs

t = arange(0,1,dt)
print len(t)

e = np.random.randn(len(t))
# plt.plot(e)
# plt.show()
# 

f = 10.0 # frecuencia en Hz 
x = np.cos(2*np.pi*f*t)
# plt.plot(x)
# plt.show()
# 
xr = x+e
# plt.plot(xr)
# plt.show()

N = len(x)
xdft = np.fft.fft(xr)

print type(xdft)
print xdft.shape
print type(xdft[0])  #Vemos que estos son numeros complejos!

xdft = xdft[0:(N/2)]
print len(xdft)

psdx = (1/(Fs*N))*np.square(np.abs(xdft))
psdx[1:-1] = 2*psdx[1:-1]
freq = arange(0,Fs/2,Fs/N)
print len(freq)
plt.plot(freq,psdx)
#plt.plot(freq,np.log10(psdx))
plt.show()



