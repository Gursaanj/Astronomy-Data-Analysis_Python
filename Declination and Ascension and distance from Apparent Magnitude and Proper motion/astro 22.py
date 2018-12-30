import numpy as np
import matplotlib.pyplot as plt

# Defining the columds of data 
v_mag =(np.loadtxt("data2.txt", comments ='#',))[:, 0]
i_mag =(np.loadtxt("data2.txt", comments = "#",))[:, 1]
P_x = (np.loadtxt("data2.txt", comments = "#",))[:, 2]
P_y = (np.loadtxt("data2.txt", comments = "#",))[:, 3]

## Part a
v_i = v_mag - i_mag

#Plotting the CMD diagram with inverted Y-axis (as seen online)
plt.scatter(v_i, v_mag, c="r", s=0.4)
plt.title("Colour Magnitude Diagram (CMD) of 47-Tucanae of V-I and V filters", fontsize=20)
plt.xlabel("$m_V$ - $m_I$ (V-I)", fontsize=16)
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])
plt.ylabel("$m_V$ (apparent Magnitude)", fontsize=18)
plt.xlim(0,5)
plt.show()

### Part b
### PMx adn PMy plot
plt.scatter(P_x, P_y, c="b",s=0.7)
plt.title("Proper motion observed in the x and y direction", fontsize=20)
plt.xlabel("Horizontal Proper motion of stars (mas/year)", fontsize=16)
plt.ylabel("Vertical Proper motion of stars (mas/year)", fontsize=16)
plt.show()


### Seperating the points for the SML and 47 Tuc
#p_xu = P_x[np.logical_and(-0.88 <= P_x, P_x <= -0.3) and np.logical_and(-0.3 <= P_y, P_y <= 0.3)]
p_xm = P_x[np.where((-0.88 <= P_x) & (P_x <= -0.3) & (-0.56 <= P_y) & (P_y <= 0.1))]
p_ym = P_y[np.where((-0.88 <= P_x) & (P_x <= -0.3) & (-0.56 <= P_y) & (P_y <= 0.1))]
v_m = v_mag[np.where((-0.88 <= P_x) & (P_x <= -0.3) & (-0.56 <= P_y) & (P_y <= 0.1))]
i_m = i_mag[np.where((-0.88 <= P_x) & (P_x <= -0.3) & (-0.56 <= P_y) & (P_y <= 0.1))]
v_im = v_m - i_m

p_xt = P_x[np.where((-0.3 <= P_x) & (P_x <= 0.32) & (-0.37 <= P_y) & (P_y <= 0.3))]
p_yt = P_y[np.where((-0.3 <= P_x) & (P_x <= 0.32) & (-0.37 <= P_y) & (P_y <= 0.3))]
v_t = v_mag[np.where((-0.3 <= P_x) & (P_x <= 0.32) & (-0.37 <= P_y) & (P_y <= 0.3))]
i_t = i_mag[np.where((-0.3 <= P_x) & (P_x <= 0.32) & (-0.37 <= P_y) & (P_y <= 0.3))]
v_it = v_t - i_t

## Part C
#Showing filtered 47 Tuc without SML 
plt.scatter(v_it, v_t, c='b',s=0.5)
plt.title("Filtered stars of 47-Tucanae without the presence of the Small Magellanic cloud and other background stars", fontsize=20)
plt.xlabel("$m_V$ - $m_I$ (V-I)", fontsize=16)
plt.ylabel("$m_V$ (apparent Magnitude)", fontsize=16)
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])
plt.xlim(0,5)
plt.show()

## Part D
##Plotting both 47 TUC and SML
plt.scatter(v_im, v_m, c='r', s=0.5, label="Small Magellanic Cloud")
plt.scatter(v_it, v_t, c='b', s=0.5, label="47 Tucanae")
plt.title("Filtered stars of both 47-Tucanae (blue) and the Small Magellanic Cloud (red) with reduction of other background stars", fontsize=20)
plt.xlabel("$m_V$ - $m_I$ (V-I)",fontsize=16)
plt.ylabel("$m_V$ (apparent Magnitude)",fontsize=16)
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])
plt.xlim(0,5)
plt.legend(loc="best",fontsize="large",markerscale=12)
plt.show()

#Locating comparable Supergiant in SML (finding its m_V)
smy = v_m[np.where((0.464 <= v_im) & (v_im <= 0.525) & (21.70 <= v_m) & (v_m <= 22.33))] 
sm_y = np.min(smy)
print(sm_y)

#Locating comparable Supergiant in 47 Tuc (finding its m_V)
sty = v_m[np.where((0.52 <= v_im) & (v_im <= 0.56) & (17.017 <= v_m) & (v_im <= 17.20))]
st_y = np.min(sty)
print(st_y)

# Distance to 47 Tuc
d = 4000

# Finding the M_V of the supergiant in 47 Tuc
def dist_mod(x,y):
    M = x -(5*(np.log10(y))) + 5
    return M

print("From the point of interest, the absolute magnitude seems to be {:.3}\n".format(dist_mod(st_y, d)))

# Using the M_V of the other supergiant and its m_V, finding SML distance
def dist(x,y):
    d = 10**((1/5)*(x-y+5))
    return d

print("The distance to the Small Magellanic Cloud is {:.3} kpc".format((dist(sm_y, dist_mod(st_y, d)))/1000))


