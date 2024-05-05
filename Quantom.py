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
   
def calculate_photon_energy(frequency:float=None, time:float=None, wavelength:float=None) -> float:
    if frequency==None and time==None:  
        return do_calculate_photon_energy_by_wavelength(wavelength)
    elif time==None and wavelength==None:
        return do_calculate_photon_energy_by_frequency(frequency)
    elif frequency==None and wavelength==None:    
        return do_calculate_photon_energy_by_time(time)
    else:
        return None

def calculate_photoelectric_effect(workfunction:float = None, kinetic_energy:float = None) -> float:
    if workfunction == None:
        return kinetic_energy
    elif kinetic_energy == None:
        return workfunction
    else:
        photon_energy = workfunction + kinetic_energy
        return photon_energy

def calculate_kinetic_energy(velocity:float = None) -> float:
    if velocity == None:
        return None
    else:
        return (mass * (velocity ** 2 )/ 2)

def calculate_de_broglie(momentum:float = None, velocity:float = None, ) -> float: # 2 different formulas for calculating wavelength
    if momentum == None and velocity != None: # case where using velocity
        return do_calculate_de_broglie_by_velocity(velocity)
    elif momentum != None and velocity == None: # case where using momentum
        return do_calculate_de_broglie_by_momentum(momentum)
    else: # ensuring no errors can occur
        return None
