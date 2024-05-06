wavelength:float = None
time:float = None
frequency:float = None
speed_of_light = 3e8
planks_constant: float = 6.626e-34
mass:float = 9.11e-31 

def do_calculate_wave_speed_by_frequency(wavelength, frequency):
    return wavelength * frequency

def do_calculate_wave_speed_by_time(wavelength, time):
    if time > 0: #time cannot be negative
        return wavelength / time
    else:
        return None

def do_calculate_de_broglie_by_momentum(momentum): 
    if momentum == 0:
        return None # preventing division by 0
    else:
        return (planks_constant / momentum)
        
def do_calculate_de_broglie_by_velocity(velocity):
    if velocity == 0: # preventing division by 0
        return None
    else:
        return (planks_constant / (mass * velocity))

def do_calculate_photon_energy_by_time(time):
    if time>0: #preventing division by 0 and restricting time to be positive
        return (planks_constant / time)
    else:
        return None
        
def do_calculate_photon_energy_by_frequency(frequency): 
    return (planks_constant * frequency) 

def do_calculate_photon_energy_by_wavelength(wavelength): 
    if wavelength == 0: # preventing division by 0
        return None 
    else:
        return ((planks_constant * speed_of_light) / wavelength)     
        


def calculate_wave_speed(wavelength:float = None, frequency:float = None, time:float = None) -> float: 
    if wavelength != None and frequency == None:
        return do_calculate_wave_speed_by_time(wavelength, time)
    elif wavelength != None and time == None:
        return do_calculate_wave_speed_by_frequency(wavelength, frequency)
    else:
        return None
    
"""
The function returns the wave speed for an electromagnetic wave in metres per second.

It takes the inputs as wavelength in meters and divides it by time in seconds, or multiplies it by frequency in hertz.

Time inputted is the period of the wave. 

This can be rearranged since frequency (hertz) is equal to the inverse of time period (seconds). This allows the equations to be interchangeable.  

"""
   
def calculate_photon_energy(frequency:float=None, time:float=None, wavelength:float=None) -> float:
    if frequency==None and time==None:  
        return do_calculate_photon_energy_by_wavelength(wavelength)
    elif time==None and wavelength==None:
        return do_calculate_photon_energy_by_frequency(frequency)
    elif frequency==None and wavelength==None:    
        return do_calculate_photon_energy_by_time(time)
    else:
        return None

"""
Returns the energy of the photon in electronvolts.

It takes the inputs Plank's constant in joule-seconds and multiplies it with frequency in hertz.

This can be rearranged in 2 other ways since frequency (hertz) is equal to the inverse of time (seconds), and frequncy is equal to speed of light (meters per second) divided by wavelength (meters).
This allows the equations to be interchangeable. 

The speed of light and plank's constant are fixed constant values so cannot be inputted. 

"""

def calculate_photoelectric_effect(workfunction:float = None, kinetic_energy:float = None) -> float:
    if workfunction == None:
        return kinetic_energy
    elif kinetic_energy == None:
        return workfunction
    else:
        photon_energy = workfunction + kinetic_energy
        return photon_energy

"""
The function returns the energy of the photon in joules.

It takes the inputs as the work function in joules (which is specific to each element/metal) and multiplies it with the kinetic energy in joules of the incoming photon.

The kinetic energy has to be at it's maximum value.

"""

def calculate_kinetic_energy(velocity:float = None) -> float:
    if velocity == None:
        return None
    else:
        return (mass * (velocity ** 2 )/ 2)
    
"""
The function returns kinetic energy in joules.

It takes the inputs as the mass in kilograms and multiplies it with the velocity sqaured in meters per second, and divides this by 2.

"""

def calculate_de_broglie(momentum:float = None, velocity:float = None, ) -> float: # 2 different formulas for calculating wavelength
    if momentum == None and velocity != None: # case where using velocity
        return do_calculate_de_broglie_by_velocity(velocity)
    elif momentum != None and velocity == None: # case where using momentum
        return do_calculate_de_broglie_by_momentum(momentum)
    else: # ensuring no errors can occur
        return None

"""
The de Broglie function returns the wavelength of a particle in meters.

It takes inputs as the mass in kilograms and multiplies it with the velocity in meters per second, and this is divided by plank's constant.

Since momentum is equal to the product of mass (kilograms) and velocity (meters per second), wavelength can also be expressed as plank's constant divided by momentum in kilogram meters per second.

The mass of a electron is a fixed constant value so cannot be inputted. 

"""       
