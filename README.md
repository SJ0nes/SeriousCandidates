# QuanTom

Functionality for solving quantum mechanic equations.


## Tutorial

In this tutorial we will see how to use 'QuanTom' to solve simple quantum equations. These equations can be used to calculate wave speed, photon energy, De Broglie wavelength and kinetic energy. For some background information <insert wiki link >

The process in which 'QuanTom' is used is very simple. For example, if someone wanted to calculate the wave speed of a moving particle in quantum mechanics, and they knew the frequency and wavelength of said particle, they would merely have to import our library:

```python
import QuanTom 

wave_speed = QuanTom1.calculate_wave_speed(wavelength=X, frequency=Y)
wave_speed
```
Simply putting in the values for X and Y will return the calculated wave speed. This process can be used for all other equations by rewriting the input with what it is you want to calculate and which variables are necessary.


## How To Guides

### How to calculate Kinetic Energy

As mentioned before in the tutorial, the QuanTom function does all the work for you all we need to do is simply plug in values. We've seen the basics of how it works for wave speed but now let's see a proper example of how to effectively use QuanTom.

The equation for Kinetic Energy: 

$KE$ = $\frac{1}{2}mv^2$

With $m$ = Mass (kg), and $v$ = Velocity (m/s)

As we are working with quantum mechanics, this equation is usually applied to the kinetic energy of an electron which has a fixed mass:

$9.11$ x $10^{-31}kg$

If you en electron was travelling at a velocity of $3000 m/s$ , using the QuanTom function it would be easy to work out the electron's Kinetic Energy ($KE$):


```python
import QuanTom

kinetic_energy = QuanTom.calculate_kinetic_energy(velocity=3000)
kinetic_energy
```
This gives:

```python 
4.0995e-24
```
### How to calculate the energy of a photon 

Just like the Kinetic Energy of an electron, using the QuanTom fucnction for Photon energy noly requires substituting in values, although unlike Kinetic Energy there isn't only one equation involved.


The three equations QuanTom uses for Photon energy are:

$PE = \frac{hc}{\lambda}$  

Where $h$ = Plancks Constant, c = Speed of Light (m/s) and $\lambda$ = Wavelength (m)

$PE = hf$

Where $h$ = Plancks Constant and $f$ = frequency (Hz)

$PE = \frac{h}{t}$

Where $h$ = Plancks Constant and $t$ = time (s)

All 3 equations can be solved by QuanTom in the same way as before. For an example, we will use the equation involving Plancks Constant, Speed of light and Wavelength.
The speed of light and Plancks Constant are both fixed values that have already been inputted into the QuanTom fucntion.

If a photon were to have a wavelength of $5$ metres:

```python
import QuanTom

photon_energy = QuanTom.calculate_photon_energy(wavelength=5)
photon_energy
```

This gives:

```python
3.9756e-26
```

## Explanation

### Brief overview of quantum mechanics

Quantum mechanics describes the behaviour of particles at the smallest scales, referring to atoms and subatomic particles. It introduces the idea that electrons and photons can possibly exist in multiple states simultaneously. Quantum mechanics is the foundation for all areas of quantum Physics which branches out into so many fields. Our function 'QuanTom' focuses on the 'Wave-particle duality' and solving equations within this sector of quantum mechanics.

### Photons 

In 1905, Einstein showed that atoms absorb and emit light in individual packets of energy. Einstein's explanation opened up the paradox that sometimes light's behaviour can only be explained by thinking of it as consisting of particles. Louis de Broglie showed light could behave both as a particle and a wave and so Quantas of light became known as photons.

This formed the equation for a single photon:

$E = hf$

Where $E$ = Photon Energy, $h$ = Plancks Constant and $f$ = frequency

### Kinetic Energy and De Broglie's Wavelength

From the wave of new ideas surrounding light, the wave-particle duality theory was born. Louis de Broglie suggested that all matter could display wave-like properties. He proposed that if electrons and other particles travel through space as a wave, they have an associated wavelength. The predicted wavelength is found by equating the work done to accelerate the electrons with the kinetic energy transferred to the electrons. Substituting:

$KE$ = $\frac{1}{2}mv^2$

we get:

$\lambda = \frac{h}{mv}$

Where $\lambda$ = De Broglie's Wavelength, $m$ = mass, $h$ = Plancks Constant  and $v$ = velocity

This equation can be simplied as:

$\lambda = \frac{h}{p}$

Where $p$ = momentum 

### Photoelectric Effect 

Einstein's explanation for the Photoelectric Effect was that in order for electrons to be realeased from a metal, the incident radiation must exceed the the threshold frequency for that metal. The minimum energy required is called the work function. Einstein then suggested each single photon could only eject one electron from the metal surface, if the photon energy was larger than the work function. Using the pricniple of conservation of energy, Einstein created the equation:

$hf = \phi + KE_{max}$

Where $hf$ = photon energy, $\phi$ = work function and $KE_{max}$ = the maximum kinetic energy

## References

### List of functionality

The following fucntions are written in QuanTom:

      . calculate_wave_speed
      . calculate_de_broglie
      . calculate_photon_energy
      . calculate_photoelectric_effect
      . calculate_kinetic energy

### Bibliography

The wikipedia page on quantum mechanics gives a good overview of the subject: <insert link>

The following text is a recommended reference on quantum mechanics:

>Piccirillo, L. (2023). Introduction to the Maths and Physics of Quantum Mechanics. CRC Press.

The following textbook is a recommeneded referene on quantum physics:

>O’neill, M. (2015). OCR AS/A level physics A. Student book 1. Pearson.
‌
