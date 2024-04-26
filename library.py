#import numpy as np
#import sympy as sym 
#import matplotlib.pyplot as plt

wavelength:float = None
time:float = None
frequency:float = None
speed_of_light = 3e8
planks_constant: float = 6.626e-34
mass:float = 9.11e-31 # mass of electron is constant

def do_calculate_wave_speed_by_frequency(frequency):
        return wavelength * frequency

def do_calculate_wave_speed_by_time(time):
        if time == 0:
            return None 
        else:
            return wavelength / time

def do_calculate_de_broglie_by_momentum(momentum): # wavelength = planks constant / momentum
        if momentum == 0:
            return None # preventing division by 0
        else:
            return (planks_constant / momentum)
        
def do_calculate_de_broglie_by_velocity(velocity): # wavelength = planks constant / (mass * velocity)
        if velocity == 0: # preventing division by 0
            return None
        else:
            return (planks_constant / (mass * velocity))

def do_calculate_photon_energy_by_time(time): # E = h/t since f = 1/t
        if time == 0: #preventing division by 0
            return None
        else:
            return (planks_constant / time)
        
def do_calculate_photon_energy_by_frequency(frequency): # E = h * f
        return (planks_constant * frequency) #multiplication by 0 is okay   

def do_calculate_photon_energy_by_wavelength(wavelength): # E = h * c / wavelength since f = c / wavelength
        if wavelength == 0: # preventing division by 0
            return None #none is the null value
        else:
            return ((planks_constant * speed_of_light) / wavelength)     
        


def calculate_wave_speed(wavelength:float = None, frequency:float = None, time:float = None) -> float: # wavespeed = wavelength * frequency    
    if wavelength != None and frequency == None:
        return do_calculate_wave_speed_by_time
    elif wavelength != None and time == None:
        return do_calculate_wave_speed_by_frequency
    else:
        return None
    """
    Wavespeed is the distance travelled by a wave per unit time.
    The equation returns the speed of a wave in metres per second.
    It takes wavelength (in metres) and frequency (in hertz) as inputs.
    """ 
def calculate_photon_energy(frequency:float=None, time:float=None, wavelength:float=None) -> float: # telling the code that the result will be a float
# ensuring only 1 is inputted
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

def calculate_photoelectric_effect(workfunction:float, kinetic_energy:float) -> float: # E = hf = workfunction + kinetic energy
    return (workfunction + kinetic_energy)

def calculate_kinetic_energy(velocity:float) -> float: # eV = 1/2 * m * v ** 2
    mass:float = 9.11e-31 # mass of electron is constant
    return (mass * (velocity ** 2 )/ 2)

def calculate_de_broglie(momentum:float = None, velocity:float = None, ) -> float: # 2 different formulas for calculating wavelength
    if momentum == None and velocity != None: # case where using velocity
        return do_calculate_de_broglie_by_velocity(velocity)
    elif momentum != None and velocity == None: # case where using momentum
        return do_calculate_de_broglie_by_momentum(momentum)
    else: # ensuring no errors can occur
        return None
    
# Tests for calculate photon energy
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