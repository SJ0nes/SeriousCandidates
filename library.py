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




#    def do_calculate_photon_energy(frequency:float=0, time:float=0, wavelength:float=0) -> float:
#        error = 0
#        planks_constant: float = 6.626e-34
#        speed_of_light = 3e8
#        #validation
#        #check inputs
#        if frequency!=0 and time!=0 and wavelength!=0:
#            error = 1
#            result = 0
#            return error,result
#        if frequency!=0 and time!=0:
#            error = 2
#            result = 0
#            return error,result
#        if time!=0 and wavelength!=0:
#            error = 3
#            result = 0
#            return error,result
#        if frequency!=0 and wavelength!=0:
#            error = 4
#            result = 0
#            return error,result
#
#        if time == 0 and wavelength == 0:
#            result = (planks_constant * frequency)
#        elif frequency == 0 and wavelength == 0:
#            result = (planks_constant / time)
#        elif time == 0 and frequency == 0:
#            result = ((planks_constant * speed_of_light) / wavelength)
#        return error, result



def calculate_photon_energy(frequency:float=0, time:float=0, wavelength:float=0) -> float:
       
    def do_calculate_photon_energy_by_wavelength(wavelength):
        planks_constant: float = 6.626e-34
        speed_of_light = 3e8
        return ((planks_constant * speed_of_light) / wavelength)        

    def do_calculate_photon_energy_by_time(time):
        planks_constant: float = 6.626e-34
        return (planks_constant / time)

    def do_calculate_photon_energy_by_frequency(frequency):
        planks_constant: float = 6.626e-34
        return (planks_constant * frequency)        

    # run validation - check inputs
    #if frequency!=0 and time!=0 and wavelength!=0:        
    #    return None
    #if frequency!=0 and time!=0:        
    #    return None
    #if time!=0 and wavelength!=0:
    #    return None
    #if frequency!=0 and wavelength!=0:    
    #    return None
    #
    #only 1 unit defined
    #if frequency>0: return do_calculate_photon_energy_by_frequency(frequency)
    #elif time>0: return do_calculate_photon_energy_by_time(time)
    #elif wavelength>0: return do_calculate_photon_energy_by_wavelength(wavelength)


    if frequency==0 and time==0 and wavelength==0:        
        return None
    if frequency!=0 and time!=0 and wavelength!=0:        
        return None
    
    if frequency==0 and time==0:        
        return do_calculate_photon_energy_by_wavelength(wavelength)
    elif time==0 and wavelength==0:
        return do_calculate_photon_energy_by_frequency(frequency)
    elif frequency==0 and wavelength==0:    
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


    

print("frequency", calculate_photon_energy(frequency=2))
print("wavelength", calculate_photon_energy(wavelength=2))
print("time", calculate_photon_energy(time=2))
print("time", calculate_photon_energy(time=0))
print("no values", calculate_photon_energy())
print("2 values", calculate_photon_energy(time=2, wavelength=2))
print("2 values", calculate_photon_energy(frequency=2, wavelength=2))
