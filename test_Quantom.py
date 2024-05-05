import Quantom

def test_calculate_wave_speed():
    assert Quantom.calculate_wave_speed(wavelength=5, frequency= 2) == 10, "the function should return 10 when the value of wavelength is 5 and frequency is 2" #testing when wavelength and frequency are non-zero real numbers.
    assert Quantom.calculate_wave_speed(wavelength=5, frequency= 0) == 0, "the function should return 0 when the value of wavelength is 5 and frequency is 0" #testing when wavelength is non-zero and frequency is 0
    assert Quantom.calculate_wave_speed(wavelength=0, frequency= 2) == 0, "the function should return 0 when the value of wavelength is 0 and frequency is 2" #testing when wavelength is zero and frequency is non-zero
    assert Quantom.calculate_wave_speed(wavelength=6, time= 2) == 3, "the function should return 3 when the value of wavelength is 6 and time is 2"#testing other entered parameters.
    assert Quantom.calculate_wave_speed(wavelength=6, time= 0) == None, "the function should return None when the value of wavelength is 6 and time is 0"#testing if function can work around an undefined answer.
    assert Quantom.calculate_wave_speed(wavelength=0, time= 2) == 0, "the function should return 0 when the value of wavelength is 0 and time is 2"#testing when multiplying with 0 .
    assert Quantom.calculate_wave_speed(wavelength=1,frequenc=2, time=3) == None, "the function should return None when 2 parameters are not inputted"#testing when too many parameters are entered
    assert Quantom.calculate_wave_speed(time=3) == None, "the function should return None when 2 parameters are not inputted"#testing when not enough parameters are entered"
    assert Quantom.calulate_wave_speed(wavelength = 2, time = -1) == None, "the function should return None when time is negative"#testing when time negative

def test_calculate_photon_energy():
    assert Quantom.calculate_photon_energy(frequency=2) == 1.3252e-33, "the function should return 1.3252e-33"#testing with only frequency inputted
    assert Quantom.calculate_photon_energy(wavelength=2) == 9.939e-26, "the function should return 9.939e-26"#testing with only wavelength inputted
    assert Quantom.calculate_photon_energy(wavelength=0) == None, "the function should return None"#testing for undefined answer since dividing by wavelength
    assert Quantom.calculate_photon_energy(time=2) == 3.313e-43, "the function should return 3.313e-34"#testing with only time inputted
    assert Quantom.calculate_photon_energy(time=0) == None, "the function should return None"#testing for undefined answer since dividing by time
    assert Quantom.calculate_photon_energy(wavelength=2,time=2) == None, "the function should return None"#testing with too many inputs
    assert Quantom.calculate_photon_energy(wavelength=0,time=2, frequency=4) == None, "the function should return None"#testing with too many inputs

def test_calculate_photoelectric_effect():
    assert Quantom.calculate_photoelectric_effect(workfunction=1, kinetic_energy=2) == 3, "function should  return 3"#testing with 2 inputs
    assert Quantom.calculate_photoelectric_effect(kinetic_energy=2) == 2, "function should  return 2"#testing with 1 inputs
    assert Quantom.calculate_photoelectric_effect(workfunction=1) == 1, "function should  return 1"#testing with 1 inputs

def test_calculate_kinetic_energy():
    assert Quantom.calculate_kinetic_energy(velocity=5) == 1.13875e-29, "function should return 1.13875e-29"#testing with non-zero velocity
    assert Quantom.calculate_kinetic_energy(velocity=0) == 0, "function should return 0"#testing with zero velocity

def test_calculate_de_broglie():
    assert Quantom.calculate_de_broglie(velocity=3) == 0.00024244420051225757, "function should return 0.00024244420051225757" #testing with 1 input
    assert Quantom.calculate_de_broglie(momentum=3) == 2.2086666666666665e-34, "function should return 2.2086666666666665e-34" #testing with 1 input
    assert Quantom.calculate_de_broglie(momentum=3, velocity=2) == None, "function should return None" #testing with 2 input

test_calculate_de_broglie
test_calculate_kinetic_energy
test_calculate_photoelectric_effect
test_calculate_photon_energy
test_calculate_wave_speed
