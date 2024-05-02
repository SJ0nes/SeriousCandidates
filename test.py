import library

#testing possible inputs for wavespeed = wavelength * frequency
def test_calculate_wave_speed_w_and_f_non0(wavelength, frequency, time): #f and w being nonzero
    result = library.calculate_wave_speed(wavelength=5, frequency= 2) #defining our desired numbers to be tested
    assert(10, "the result is incorrect") # 10 = 2 * 5, if the answer is not 10, return that error message and hault the code
test_calculate_wave_speed_w_and_f_non0() #calling the function after to execute the test

def test_calculate_wave_speed_w_and_fis0(wavelength, frequency, time): #testing with frequency as 0
    result = library.calculate_wave_speed(wavelength=5, frequency= 0) 
    assert(0, "the result is incorrect")
test_calculate_wave_speed_w_and_fis0()

def test_calculate_wave_speed_wis0_and_f(wavelength, frequency, time): #testing with wavelength as 0
    result = library.calculate_wave_speed(wavelength=0, frequency= 2) 
    assert(0, "the result is incorrect")
test_calculate_wave_speed_wis0_and_f() 

#testing possible inputs for wavespeed = wavelength * frequency
def test_calculate_wave_speed_w_and_t_non0(wavelength, frequency, time): #f and t being nonzero
    result = library.calculate_wave_speed(wavelength=6, time= 2) 
    assert(3, "the result is incorrect") 
test_calculate_wave_speed_w_and_t_non0() 

def test_calculate_wave_speed_w_and_tis0(wavelength, frequency, time): #testing with time as 0
    result = library.calculate_wave_speed(wavelength=5, time= 0) 
    assert(None, "the result is incorrect")
test_calculate_wave_speed_w_and_tis0()

def test_calculate_wave_speed_wis0_and_t(wavelength, frequency, time): #testing with wavelength as 0
    result = library.calculate_wave_speed(wavelength=0, time= 2) 
    assert(0, "the result is incorrect")
test_calculate_wave_speed_wis0_and_t() 

