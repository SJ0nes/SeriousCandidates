import library 

#testing possible inputs for wavespeed = wavelength * frequency
def test_calculate_wave_speed_w_and_f_non0(wavelength, frequency, time): #f and w being nonzero
    result = library.calculate_wave_speed(wavelength=5, frequency= 2) #defining our desired numbers to be tested
    assert(10, "the result is incorrect") # 10 = 2 * 5, if the answer is not 10, return that error message and hault the code
test_calculate_wave_speed_w_and_f_non0() #calling the function after to execute the test

#testing possible inputs for kinetic energy = 1/2 * mass * velocity **2
def test_calculate_kinetic_energy(mass, velocity)
    result = library.calculate_kinetic_energy(mass = 5, velocity= 10)
    assert(250, "the result is incorrect") # 250 = 5 * (10 ** 2)/ 2), if the answer is not 250, return that error message and hault the code)
test_calculate_kinetic_energy() #calling the function after to execute the test

def test_calculate_kinetic_energy(mass, velocity): #testing with mass as 0
    result = library.calculate_kinetic_energy(mass=0, velocity= 2) 
    assert(0, "the result is incorrect")
test_calculate_kinetic_energy() 

#testing possible inputs for photon energy = plancks constant * frequency
def test_calculate_photon_energy(planks constant, frequency, time, wavelenght ):
    result = library.do_calculate_photon_energy_by_frequency(frequency= 2) #defining our desired numbers to be tested
    assert(*******, "the result is incorrect") # 10 = 2 * 5, if the answer is not 10, return that error message and hault the code
test_calculate_photon_energy() #calling the function after to execute the test

#testing possible inputs for photon energy = plancks constant / time
def test_calculate_photon_energy(planks constant, frequency, time, wavelenght ):
    result = library.do_calculate_photon_energy_by_time(time=5) #defining our desired numbers to be tested
    assert(*******, "the result is incorrect") # 10 = 2 * 5, if the answer is not 10, return that error message and hault the code
test_calculate_photon_energy() #calling the function after to execute the test

#testing possible inputs for photon energy = (plancks constant * speed of light) / wavelenght
def test_calculate_photon_energy(planks constant, frequency, time, wavelenght ):
    result = library.do_calculate_photon_energy_by_wavelength(wavelength= 10) #defining our desired numbers to be tested
    assert(*******, "the result is incorrect") # 10 = 2 * 5, if the answer is not 10, return that error message and hault the code
test_calculate_photon_energy() #calling the function after to execute the test



