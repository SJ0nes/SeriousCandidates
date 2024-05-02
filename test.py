import library

def test_calculate_wave_speed_w_and_f_non0(wavelength, frequency, time): #testing wavespeed = wavelength * frequency with f and w being nonzero
    result = library.calculate_wave_speed(wavelength=5, frequency= 2) #defining our desired numbers to be tested
    assert(10, "the result is incorrect") # 10 = 2 * 5, if the answer is not 10, return that error message and hault the code

def test_calculate_wave_speed_w_and_fis0(wavelength, frequency, time): #testing with frequency as 0
    result = library.calculate_wave_speed(wavelength=5, frequency= 0) 
    assert(0, "the result is incorrect")

def test_calculate_wave_speed_wis0_and_f(wavelength, frequency, time): #testing with wavelength as 0
    result = library.calculate_wave_speed(wavelength=0, frequency= 2) 
    assert(0, "the result is incorrect")