# defining all the necessary variables
wavelength:float = None
time:float = None
frequency:float = None
speed_of_light = 3e8
planks_constant: float = 6.626e-34
mass:float = 9.11e-31

def do_calculate_wave_speed_by_frequency(frequency): 
    return wavelength * frequency

def do_calculate_wave_speed_by_time(time):
    if time == 0: #since dividing by time, ensuring there isn't any errors
        return None 
    else:
        return wavelength / time

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
    if time == 0: #preventing division by 0
        return None
    else:
        return (planks_constant / time)
        
def do_calculate_photon_energy_by_frequency(frequency): 
        return (planks_constant * frequency) 

def do_calculate_photon_energy_by_wavelength(wavelength): 
    if wavelength == 0: # preventing division by 0
        return None #none is the null value
    else:
        return ((planks_constant * speed_of_light) / wavelength)     
        

#the functions used in practice while using the library
def calculate_wave_speed(wavelength:float = None, frequency:float = None, time:float = None) -> float: # wavespeed = wavelength * frequency    
    if wavelength != None and frequency == None:
        return do_calculate_wave_speed_by_time(time)
    if wavelength != None and time == None:
        return do_calculate_wave_speed_by_frequency(frequency)
    else:
        return None
  
def calculate_photon_energy(frequency:float=None, time:float=None, wavelength:float=None) -> float: 
    if frequency==None and time==None and wavelength==None: #ensuring only 1 parameter is entered.
        return None
    if frequency!=None and time!=None and wavelength!=None:        
        return None
    
    if frequency==None and time==None: # using wavelenth
        return do_calculate_photon_energy_by_wavelength(wavelength)
    if time==None and wavelength==None: # using frequency
        return do_calculate_photon_energy_by_frequency(frequency)
    if frequency==None and wavelength==None: # using time
        return do_calculate_photon_energy_by_time(time)
    else:
        return None

def calculate_photoelectric_effect(workfunction:float, kinetic_energy:float) -> float:
    return (workfunction + kinetic_energy)

def calculate_kinetic_energy(velocity:float) -> float:
    return (mass * (velocity ** 2 )/ 2)

def calculate_de_broglie(momentum:float = None, velocity:float = None, ) -> float: # 2 different formulas for calculating wavelength
    if momentum == None and velocity != None: # case where using velocity
        return do_calculate_de_broglie_by_velocity(velocity)
    if momentum != None and velocity == None: # case where using momentum
        return do_calculate_de_broglie_by_momentum(momentum)
    else: # ensuring no errors can occur if too many parameters are entered
        return None
    
