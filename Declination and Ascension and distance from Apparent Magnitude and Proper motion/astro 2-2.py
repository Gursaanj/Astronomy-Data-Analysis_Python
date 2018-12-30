import numpy as np
import matplotlib.pyplot as plt


v_mag =(np.loadtxt("data2.txt", comments ='#',))[:, 0]
i_mag =(np.loadtxt("data2.txt", comments = "#",))[:, 1]
P_x = (np.loadtxt("data2.txt", comments = "#",))[:, 2]
P_y = (np.loadtxt("data2.txt", comments = "#",))[:, 3]

## Part a
v_i = v_mag - i_mag

plt.scatter(v_i, v_mag, c="r", s=0.4)
plt.title("Colour Magnitude Diagram (CMD) of 47-Tucanae of V-I and V filters", fontsize=20)
plt.xlabel("V filter subtracted by the I filter (V-I)", fontsize=16)
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])
plt.ylabel("V filter")
plt.xlim(0,5)
plt.show()

### Part b
### PMx adn PMy plot
plt.scatter(P_x, P_y, c="b",s=0.7)
plt.title("Proper motion observed in the x and y direction", fontsize=20)
plt.xlabel("Horizontal Proper motion of stars (mas/year)", fontsize=16)
plt.ylabel("Vertical Proper motion of stars (mas/year)", fontsize=16)
plt.show()

#p_f = (np.sqrt(((np.mean(P_x))**2)+((np.mean(P_y))**2)))
p_f = (np.sqrt((P_x**2)+(P_y**2)))

P_xu = P_x[np.where(p_f <= 0.4)]
P_yu = P_y[np.where(p_f <= 0.4)]


#P_xu = P_x[np.where(np.logical_and((np.abs(P_x) <= 0.3), (np.abs(P_y) <= 0.3)))]
#P_yu = P_y[np.where(np.logical_and((np.abs(P_x) <= 0.3), (np.abs(P_y) <= 0.3)))]

print(len(P_xu))
print(len(P_yu))

print(len(P_x)-len(P_xu))
print(np.mean(P_xu))
print(np.mean(P_yu))
print(np.sqrt(((np.mean(P_xu))**2)+((np.mean(P_yu))**2)))


plt.scatter(P_xu, P_yu,c='r', s=0.5)
plt.title("Proper motion of stars within 47-Tucanae with reduced background", fontsize=20)
plt.xlabel("Horizontal Proper motion of stars(mas/yr)", fontsize=16)
plt.ylabel("Vertical Proper motion of stars(mas/yr)", fontsize=16)
plt.show()

### Part c
vnew = v_mag[np.where(p_f <= 0.4)]
inew = i_mag[np.where(p_f <= 0.4)]

v_i_new = vnew - inew

plt.scatter(v_i_new, vnew, c='b', s=0.5)
plt.title("Colour Magnitude Diagram(CMD) of 47-Tucanae with reduced background stars, With V and V-I filters", fontsize=20)
plt.xlabel("V filter subtracted by the I filter (V-I)", fontsize=16)
plt.ylabel("V filter", fontsize=16)
plt.xlim(0,5)
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])
plt.show()

##### Part D

P_xn = P_x[np.where(p_f > 0.4)]
P_yn = P_y[np.where(p_f > 0.4)]
V_newn = v_mag[np.where(p_f > 0.4)]
I_newn = i_mag[np.where(p_f > 0.4)]

vi = V_newn - I_newn
plt.scatter(v_i_new, vnew, c='b', s=0.5)  
plt.scatter(vi, V_newn, c='r', s=0.5)
plt.xlim(0,5)
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])
plt.xlabel("V filter Subtracted by the I filter (V-I)")
plt.title("Colour magnitude Diagrams of both 47-Tucanae (Blue) and the Small Magellanic Cloud(red)")
plt.ylabel("V filter")
plt.show()
