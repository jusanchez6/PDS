import scipy.signal as signal
#from scipy import signal
from pylab import *
import numpy as np

#funcion que que permite crear y graficar la respuesta en frecuencia de un filtro     
def mfreqz(b,a=1):
    w,h = signal.freqz(b,a)
    h_dB = 20 * log10 (abs(h))
    h_pot = abs(h)
    
    plt.figure(figsize=(18,8))
    subplot(311)
    plot(w/max(w),h_dB)
    ylabel('Magnitude (db)')
    xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
    title(r'Frequency response')


    subplot(312)
    plot(w/max(w),h_pot)
    ylabel('Magnitude (W)')
    xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
    title(r'Frequency response')

    subplot(313)
    
    h_Phase =  np.angle(h)  #unwrap(arctan2(imag(h),real(h)))
   
    plot(w/max(w),h_Phase)
    ylabel('Phase (radians)')
    #xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
    title(r'Phase response')
    subplots_adjust(hspace=0.5)
    show()


def impz(b,a=1):
    l = len(b)
    impulse = repeat(0.,l); impulse[0] =1.
    x = arange(0,l)
    response = signal.lfilter(b,a,impulse)
    
    plt.figure(figsize=(12,5))
    subplot(211)
    stem(x, response)
    ylabel('Amplitude')
    xlabel(r'n (samples)')
    title(r'Impulse response')
    subplot(212)
    step = cumsum(response)
    stem(x, step)
    ylabel('Amplitude')
    xlabel(r'n (samples)')
    title(r'Step response')
    subplots_adjust(hspace=0.5)
    show()

def zeropoles(b, a=1):
    w,h = signal.freqz(b,a)
    sys1=signal.lti(b, a)
    #subplot(121)
    #plot(h.real, h.imag)
    #plot(h.real, -h.imag)
    #subplot(122)
    ang=np.arange(0.0,2*np.pi,0.01)
    xp=np.cos(ang)
    yp=np.sin(ang)
    plot(xp,yp,'--')
    plot(sys1.zeros.real, sys1.zeros.imag, 'o')
    plot(sys1.poles.real, sys1.poles.imag, 'x')
    #xlim(np.min(sys1.zeros.imag)-1, np.max(sys1.zeros.imag)+1)
    #ylim(np.min(sys1.zeros.imag)-1, np.max(sys1.zeros.imag)+1)
    show()
