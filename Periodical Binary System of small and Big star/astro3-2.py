import numpy as np
import matplotlib.pyplot as plt

d_sys = 1.82 #kpc
jd = (np.loadtxt("vel.txt", comments='#'))[:,0]
v_p = (np.loadtxt("vel.txt", comments='#'))[:,1] #km/s
v_s = (np.loadtxt("vel.txt", comments='#'))[:,2] #km/s
phase = (np.loadtxt("vel.txt", comments='#'))[:,3] # -0.5 ~ 0.5

vp_max = np.max(v_p)
vs_max = np.min(v_s)
mid_line = (vp_max+vs_max)/2
print("The velocity of the primary star is {:.4} km/s \n".format(vp_max-mid_line))
print("The velocity of the secondary star is {:.4} km/s \n".format(mid_line-vs_max))
print("the velocity of the system(?????) is {:.4} km/s".format(vp_max-vs_max))

plt.scatter(phase, v_p, c='r', label="Primary Star")
plt.scatter(phase, v_s, c='b', label="Secondary Star")
plt.xlabel("Arbitrary Phase")
plt.ylabel("Velocity of the Stars (Km/s)")
plt.legend(loc="best")
plt.show()

