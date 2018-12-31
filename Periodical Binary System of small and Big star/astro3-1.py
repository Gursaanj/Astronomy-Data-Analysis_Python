import numpy as np
import matplotlib.pyplot as plt 

d_sys = 1.82 #kpc

jd = (np.loadtxt("vedit.txt", comments='#'))[:,0]
v_mag = (np.loadtxt("vedit.txt", comments='#'))[:,1]
error = (np.loadtxt("vedit.txt", comments='#'))[:,2]
phase = (np.loadtxt("vedit.txt", comments='#'))[:,3]

jd_use = jd[np.where((jd>2763) & (jd<2768))]
v_use = v_mag[np.where((jd>2763) & (jd<2768))]
phase_use = phase[np.where((jd>2763) & (jd<2768))]


#phase_start = np.min(phase_use[np.where(phase_use >= 0)])
#day_start = jd_use[np.where(phase_use == phase_start)]
#print(day_start)
#phase_half = np.max(phase_use[np.where(phase_use <= 0.5)])
#half_period = jd_use[np.where(phase_use == phase_half)]
#halft= half_period-day_start
#print("The period of the binary system is {:.5} Julian Days".format(np.float(2*halft)))


eclp_1 = np.float(jd_use[np.where(v_use == np.max(v_use))])
v_use_2 = v_use[np.where(jd_use > 2767)]
jd_use_2 = jd_use[np.where(jd_use > 2767)]
eclp_2 = np.float(jd_use_2[np.where(v_use_2 == np.max(v_use_2))])
period_days = 2*(eclp_2-eclp_1)
period = period_days *86400
print("The full period of the Binary system is {:.5} Julian Days or {:.8} seconds".format(period_days,period))



plt.scatter(jd_use,v_use,c='r')
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])
plt.title("Visual magnitude of Spectroscopic Binary system as a function of Julian Days")
plt.xlabel("Time in terms of Julian days")
plt.ylabel("V_mag of system")
plt.show()

plt.scatter(phase_use, v_use, c='b')
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])
plt.title("Visual magnitude of spectroscopic Binary system as a function of its phase")
plt.xlabel("Phase (fraction of period)")
plt.ylabel("V_mag of system")
plt.show()


##############################################################


jd_vel = (np.loadtxt("vel.txt", comments='#'))[:,0]
v_p = (np.loadtxt("vel.txt", comments='#'))[:,1] #km/s
v_s = (np.loadtxt("vel.txt", comments='#'))[:,2] #km/s
phases = (np.loadtxt("vel.txt", comments='#'))[:,3] # -0.5 ~ 0.5

vp_max = np.max(v_p)
vs_max = np.min(v_s)
mid_line = (vp_max+vs_max)/2
print("The velocity of the primary star is {:.4} km/s \n".format(vp_max-mid_line))
print("The velocity of the secondary star is {:.4} km/s \n".format(mid_line-vs_max))
print("the velocity of the system(?????) is {:.4} km/s".format(vp_max-vs_max))

plt.scatter(phases, v_p, c='r', label="Primary Star")
plt.scatter(phases, v_s, c='b', label="Secondary Star")
plt.xlabel("Arbitrary Phase", fontsize=16)
plt.ylabel("Velocity of the Stars (Km/s)", fontsize=16)
plt.legend(loc="best")
plt.show()

print("The ratio of the velovity of the primary star and the second star are the same as the ratio of their masses and in turn their semi major axis are the same \n")
print("m1/m2 = a1/a2 = {}".format((vp_max-mid_line)/(mid_line -vs_max)))

#Assuming there are circular orbits 
a_p, a_s = (period*vp_max/(2*np.pi)), (period*vs_max/(2*np.pi))
a_tot = a_p + a_s
m_tot = (4*((np.pi)**2)*(a_tot**3))/((period**2)*(6.67*10**-11))
m_p, m_s = m_tot/(1+((mid_line-vs_max)/(vp_max-mid_line))), m_tot/(((vp_max-mid_line)/(mid_line-vs_max))+1)



