import numpy as np
import matplotlib.pyplot as plt 

### Import data from the file
m_frac = np.loadtxt("model1.txt",comments="#")[:,0]
r_frac = np.loadtxt("model1.txt",comments="#")[:,1]
temp = np.loadtxt("model1.txt",comments="#")[:,2]  # In Kelvins
rho = np.loadtxt("model1.txt",comments="#")[:,3] # in g/cm^3
press = np.loadtxt("model1.txt",comments="#")[:,4] # in dyn/cm^2
lum_frac = np.loadtxt("model1.txt",comments="#")[:,5]
x_h1 = np.loadtxt("model1.txt",comments="#")[:,6] #Hydrogen mass fraction
x_he4 = np.loadtxt("model1.txt",comments="#")[:,7] # Helium 4 mass fraction
x_he3 = np.loadtxt("model1.txt",comments="#")[:,8] # Helium 3 mass fraction
x_c12 = np.loadtxt("model1.txt",comments="#")[:,9] # Carbon 12 mass fraction 
x_n14 = np.loadtxt("model1.txt",comments="#")[:,10] # Nitrogen 14 mass fraction
x_016 = np.loadtxt("model1.txt",comments="#")[:,11] # Oxygen 16 mass fraction 

# Constants 
sun_radius = 6.96*10**8 #Metres
sun_mass = 1.989*10**30 # Kg
h_mass = 1.67*10**-27 # kg (for the atom)
k = 1.3807*10**-23 # JK^-1
G = 6.67408*10**-11 #m^3kg^-1s^-2

def mu_mass(x,y,z):
    mass_inv = (2*x + (3/4)*y +1/2*z)
    mass = 1/mass_inv
    return mass

mu_sun = mu_mass(0.74,0.24,0.02)
print("The solar mean mass is {:.4} Proton masses".format(mu_sun))
rho_sun = 1.505*10**5 #kg/m^3
press_sun = 2.338*10**16 # N/m^2
t_sun = 1.548*10**7 #Kelvin

press_frac = (0.1*press)/press_sun
t_frac = temp/t_sun

#Question 9 
rho_c = (3*sun_mass)/(np.pi*(sun_radius**3))
print(rho_c)
press_c = (5*G*sun_mass**2)/(4*np.pi*sun_radius**4)
print(press_c)
t_c = (h_mass*mu_sun*press_c)/(k*rho_c)
print(t_c)

radius = r_frac*sun_radius
density = rho_c*(1-r_frac)

mass = 4/3*np.pi*rho_c*((radius)**3)-(rho_c*np.pi/sun_radius)*((radius)**4)
mass_func = mass/sun_mass

pressure = press_c - (9*G*sun_mass**2/(np.pi*sun_radius**6))*((2/3*(radius**2))
                 -(7/(9*sun_radius)*radius**3)+(1/(4*sun_radius**2)*radius**4))
pressure_func = pressure/press_c

temperature = h_mass*mu_sun*pressure/(k*density)
temperature_func = temperature/t_c
print(temperature_func)
print(radius[np.where(temperature_func == np.max(temperature_func))])
print(np.max(temperature_func))



## Plotting mr as a function of r
plt.scatter(r_frac,mass_func,s=3,c="r",label="Simple Model")
plt.plot(r_frac,m_frac,"b-",label="Standard Solar Model")
plt.xlabel("Radius of the sun in terms of 1 Solar Radii",fontsize=16)
plt.xlim(0,1)
plt.ylabel("Mass of the sun at given radius in terms of the sun's total mass",fontsize=16)
plt.ylim(0,1.02)
plt.title("Mass of the sun as a function of its radius, both normalized",fontsize=20)
plt.legend(loc="best",fontsize="xx-large")
plt.show()

## Plotting Pressure as a function of r 
plt.scatter(r_frac,pressure_func,s=3,c="r",label="Simple Model")
plt.plot(r_frac,press_frac,"b-",label="Standard Solar Model")
plt.xlabel("Radius of the sun in terms of 1 Solar Radii",fontsize=16)
plt.xlim(0,1)
plt.ylabel("Pressure of the sun at given radius in terms of the sun's central Pressure",fontsize=16)
plt.ylim(0,1.02)
plt.title("Pressure of the sun as a function of its radius, both normalized",fontsize=20)
plt.legend(loc="best",fontsize="xx-large")
plt.show()


## Plotting Temperature as a function of r
plt.scatter(r_frac,temperature_func,s=3,c="r",label="Simple Model")
plt.plot(r_frac,t_frac,"b-",label="Standard Solar Model")
plt.xlabel("Radius of the sun in terms of 1 Solar Radii",fontsize=16)
plt.xlim(0,1)
plt.ylabel("Temperature of the sun at given radius in terms of the sun's central Temperature",fontsize=16)
plt.ylim(0,1.08)
plt.title("Temperature of the sun as a function of its radius, both normalized",fontsize=20)
plt.legend(loc="best",fontsize="xx-large")
plt.show()