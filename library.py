#import numpy as np
#import sympy as sym 
#import matplotlib.pyplot as plt



def calculate_wave_speed(wavelength:float, frequency:float) -> float:
    """
    Wavespeed is the distance travelled by a wave per unit time.
    The equation returns the speed of a wave in metres per second.
    It takes wavelength (in metres) and frequency (in hertz) as inputs.
    """ 
    return wavelength * frequency


def calculate_photon_energy(frequency:float=None, time:float=None, wavelength:float=None) -> float:
    planks_constant: float = 6.626e-34
    speed_of_light = 3e8
       
    def do_calculate_photon_energy_by_wavelength(wavelength):
        if wavelength == 0:
            return None
        else:
            return ((planks_constant * speed_of_light) / wavelength)        

    def do_calculate_photon_energy_by_time(time):
        if time == 0:
            return None
        else:
            return (planks_constant / time)

    def do_calculate_photon_energy_by_frequency(frequency):
        return (planks_constant * frequency)        

    if frequency==None and time==None and wavelength==None:        
        return None
    if frequency!=None and time!=None and wavelength!=None:        
        return None
    
    if frequency==None and time==None:        
        return do_calculate_photon_energy_by_wavelength(wavelength)
    elif time==None and wavelength==None:
        return do_calculate_photon_energy_by_frequency(frequency)
    elif frequency==None and wavelength==None:    
        return do_calculate_photon_energy_by_time(time)
    else:
        return None
    



    
    
    """
    Photon energy is the energy carried by a single photo. 
    The equation returns the energy of a photon in Electron Volts.
    It takes either frequency or time as inputs and multiplies with a planks_constant which is a constant value.
    
    Since frequency is equal to the inverse of time, 2 equations can be used to find photon energy.
    Frequency also is equal to the speed of light divided with wavelength.
    When inputting the parameters, only input the parameter you are using.
    """

"""
print('test 1', calculate_photon_energy(frequency=0, time=0, wavelength=0))
print('test 2', calculate_photon_energy(frequency=1, time=2, wavelength=3))
print('test 3', calculate_photon_energy(time=1, wavelength=1))
print('test 4', calculate_photon_energy(frequency=1, wavelength=1))
print('test 5', calculate_photon_energy(frequency=1, time=1))
print('calculate_photon_energy by frequency = ',calculate_photon_energy(frequency=2))
print('calculate_photon_energy by time = ',calculate_photon_energy(time=2))
print('calculate_photon_energy by wavelength = ',calculate_photon_energy(wavelength=2))
print('calculate_photon_energy by frequency = ',calculate_photon_energy(frequency=0))
print('calculate_photon_energy by time = ',calculate_photon_energy(time=0))
print('calculate_photon_energy by wavelength = ',calculate_photon_energy(wavelength=0))
"""
