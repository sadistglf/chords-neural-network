from pylab import*
from scipy.io import wavfile
import matplotlib.pyplot as plt

gus = 2
print gus

sampFreq, snd = wavfile.read('../Archivos/Cmin.wav') 
print snd.dtype
# Cmaj.wav corresponde a int16

# snd = snd / (2.**15)

ndata = snd.shape[0]
nchan = snd.shape[1]
print "Sampling Frequency (Hz): " + str(sampFreq)
print "Audio Data Channels: " + str(nchan) 
print "Audio Data Samples: " + str(ndata)
print "Duration: (Samples/Sampling_Freq) (s): " + str(ndata/sampFreq)
print snd[100000:100200,:]

print "Se seleccionara solo el primer canal"

s1 = snd[:,1]/2.**15

plt.plot(snd[:,0]/2.**15)
snd = snd[:,0]/2.**15

# SI SE QUIERE ESCUCHAR, REVISAR pyaudio, pyalsaaudio
# 

timeArray = arange(0, ndata, 1)
timeArray = timeArray / (sampFreq*1.0)
# timeArray = timeArray  #scale to milliseconds

#print timeArray
#plt.plot(timeArray,s1)
#plt.axis([0, 7, -1, 1])
#plt.draw()


n = len(s1) 
p = fft(s1) # take the fourier transform 
nUniquePts = int(ceil((n+1)/2.0))
p = p[0:nUniquePts]
p = abs(p)

p = p / float(n) # scale by the number of points so that
                 # the magnitude does not depend on the length 
                 # of the signal or on its sampling frequency  
p = p**2  # square it to get the power 



# multiply by two (see technical document for details)
# odd nfft excludes Nyquist point
if n % 2 > 0: # we've got odd number of points fft
    p[1:len(p)] = p[1:len(p)] * 2
else:
    p[1:len(p) -1] = p[1:len(p) - 1] * 2 # we've got even number of points fft

freqArray = arange(0, nUniquePts, 1.0) * (sampFreq / n);
# plt.plot(freqArray/1000, 10*log10(p), color='k')
plt.plot(freqArray/1000, (p), color='k')

# xlabel('Frequency (kHz)')
# ylabel('Power (dB)')
plt.show()