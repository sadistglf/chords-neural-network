from pylab import*
from scipy.io import wavfile
import matplotlib.pyplot as plt

sampFreq, snd = wavfile.read('../Archivos/Cmin.wav') 
print snd.dtype
# Cmaj.wav corresponde a int16

ndata = snd.shape[0]
nchan = snd.shape[1]
print "Sampling Frequency (Hz): " + str(sampFreq)
print "Audio Data Channels: " + str(nchan) 
print "Audio Data Samples: " + str(ndata)
print "Duration: (Samples/Sampling_Freq) (s): " + str(ndata/sampFreq)

s1 = snd[:,1]/2.**15

# plt.plot(snd[:,0]/2.**15)
snd = snd[:,0]/2.**15

# SI SE QUIERE ESCUCHAR, REVISAR pyaudio, pyalsaaudio
timeArray = arange(0, ndata, 1)
timeArray = timeArray / (sampFreq*1.0)

# timeArray = timeArray  #scale to milliseconds

#print timeArray
plt.plot(timeArray,s1)
plt.show()