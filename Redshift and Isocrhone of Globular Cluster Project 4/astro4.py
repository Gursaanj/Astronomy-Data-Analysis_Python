import numpy as np
import matplotlib.pyplot as plt

## Import the data from Clusters UBV txt file 
v_cubv = np.loadtxt("clusterubv.txt",comments="#")[:,2]
b_vcubv = np.loadtxt("clusterubv.txt",comments="#")[:,3]
u_bcubv = np.loadtxt("clusterubv.txt",comments="#")[:,4]

plt.scatter(b_vcubv,v_cubv,c="r",s=5)
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])
plt.title("Colour-colour diagram with the V and B-V filter for the cluster", fontsize=20)
plt.xlabel("B-V",fontsize=16)
plt.ylabel("Apparent Magnitude in the Visual Spectrum", fontsize=16)
plt.show()

count = 32
star_count = len(b_vcubv[np.where((b_vcubv > 0) & (b_vcubv <0.8))])
#print("The binary frequency is {:.4} or {:.4} %".format(count/star_count, 100*(count/star_count)))

####### Import from intrinsic ubvis
b_vred = np.loadtxt("ubvic.txt",comments="#")[:,0]
u_bred = np.loadtxt("ubvic.txt",comments="#")[:,1]

plt.plot(b_vred,u_bred,"r-",linewidth=3, label="Intrinsic_Colour Data")
plt.scatter(b_vcubv,u_bcubv,c="b",s=5, label="Cluster Data")
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])
plt.title("Colour-Colour digaram for Cluster and its intrinsic Colour", fontsize=20)
plt.xlabel("B-V passband filter magnitude", fontsize=16)
plt.ylabel("U-B passband filter magnitude", fontsize=16)
plt.legend(loc="best", fontsize="x-large")
plt.show()

red_shift_bv = 0.05
b_new = b_vcubv-red_shift_bv
red_shift_ub = red_shift_bv/0.72
u_new = u_bcubv - red_shift_ub
print("The cluster is redshifted by {} in the (B-V) filter".format(red_shift_bv))
print("The cluster is redshifted by {:.3} in the (U-B) filter".format(red_shift_ub))
print("The Extinction of the cluster in the visual filter is {:.3}".format(3*red_shift_bv))

plt.plot(b_vred,u_bred,"r-",linewidth=3, label="Intrinsic_Colour Data")
plt.scatter(b_new,u_new,c="b",s=5, label="Cluster Data shifted")
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])
plt.title("Colour-Colour digaram for Cluster shifted and its intrinsic Colour", fontsize=20)
plt.xlabel("B-V passband filter magnitude", fontsize=16)
plt.ylabel("U-B passband filter magnitude", fontsize=16)
plt.legend(loc="best", fontsize="x-large")
plt.show()

##################### Replotting it dereddened and extinction corrected
v_shift = v_cubv - (3*red_shift_bv)

plt.scatter(b_new,v_shift,c="r",s=5)
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])
plt.title("Colour-colour diagram with the V and B-V filter for the cluster", fontsize=20)
plt.xlabel("B-V",fontsize=16)
plt.ylabel("Apparent Magnitude in the Visual Spectrum", fontsize=16)
plt.show()

############################ import UBV_intrinsic_ms 

v_ms = np.loadtxt("ubvims.txt",comments="#")[:,0]
b_vms = np.loadtxt("ubvims.txt",comments="#")[:,1]

plt.scatter(b_new,v_shift,c="r",s=5, label="Cluster accounted for reddening and Extinction")
plt.plot(b_vms,v_ms,"b-",linewidth=3, label="Intrinsic fiducial Main sequence")
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])
plt.title("Colour-colour diagram with the V and B-V filter for the cluster and Fiducial main sequence", fontsize=20)
plt.xlabel("B-V",fontsize=16)
plt.ylabel("Apparent Magnitude in the Visual Spectrum", fontsize=16)
plt.legend(loc="best", fontsize="x-large")
plt.show()

shift = 5.65
y = np.full((len(b_vms),),shift)
v_fit = v_ms + y
print("m-M (to fit the fiducial function) is {}".format(shift))

plt.scatter(b_new,v_shift,c="r",s=5, label="Cluster accounted for reddening and extinction")
plt.plot(b_vms,v_fit,"b-",linewidth=3, label="Intrinisc fiducial Main sequence shifted")
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])
plt.title("Colour-colour diagram with the V and B-V filter for the cluster shifted and Fiducial main sequence", fontsize=20)
plt.xlabel("B-V",fontsize=16)
plt.ylabel("Apparent Magnitude in the Visual Spectrum", fontsize=16)
plt.legend(loc="best", fontsize="x-large")
plt.show()

distance = 10*(10**((shift-(3*red_shift_bv))/5))
print("The Distance to the Cluster is {:.3} pc".format(distance))

####################### Plotting the Ischrones

iso_3e7_v = np.loadtxt("iso316e7.txt",comments="#")[:,1] + (shift+(3*red_shift_bv))
iso_3e7_bv = np.loadtxt("iso316e7.txt",comments="#")[:,0] - np.loadtxt("iso316e7.txt",comments="#")[:,1]

iso_1e8_v = np.loadtxt("iso100e8.txt",comments="#")[:,1] +  (shift+(3*red_shift_bv))
iso_1e8_bv = np.loadtxt("iso100e8.txt",comments="#")[:,0] - np.loadtxt("iso100e8.txt",comments="#")[:,1]

iso_3e8_v = np.loadtxt("iso316e8.txt", comments="#")[:,1] + (shift+(3*red_shift_bv))
iso_3e8_bv = np.loadtxt("iso316e8.txt", comments="#")[:,0] - np.loadtxt("iso316e8.txt", comments="#")[:,1]

v_new = v_shift - shift

plt.scatter(b_new,v_cubv,c="r",s=5, label="Cluster accounted for reddening")
plt.plot(iso_3e7_bv,iso_3e7_v,"g-",label="Isochrone that is 3.16e7 years old")
plt.plot(iso_1e8_bv,iso_1e8_v,"b-",label="Isochrone that is 1.00e8 years old")
plt.plot(iso_3e8_bv,iso_3e8_v,"c-",label="Isochrone that is 3.16e8 years old")
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])
plt.title("The colour-color digram of the cluster shited for reddening compared with the isochrones", fontsize=20)
plt.xlabel("B-V passband filter magnitude",fontsize=16)
plt.ylabel("Apparent Magnitude in the Visual Spectrum", fontsize=16)
plt.legend(loc="best", fontsize="x-large")
plt.show()


