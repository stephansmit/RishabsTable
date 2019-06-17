import CoolProp.CoolProp as CP
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#table input 
Tmin=-20
Tmax=60
Pmax=700
Pmin=20
Np = 10
Nt = 10

#discretization
P_vec = np.geomspace(Pmin, Pmax, Np)
T_vec = np.linspace(Tmin, Tmax, Nt)
T = np.array([[t for t in T_vec ] for p in P_vec])
P = np.array([[p for t in T_vec ] for p in P_vec])

#calculation of values
df = pd.DataFrame(data= [T.flatten(), P.flatten()]).transpose()
df.columns=['T','P']
df['R']= df.apply(lambda x: CP.PropsSI('D','T',x['T']+273.15, 'P',x['P']*1e5, 'hydrogen'),axis=1)

#writing of the table
df.to_csv('table.csv',sep=',')

#make the contour map
hdf = df.groupby(['T','P']).mean()
hdfreset = hdf.reset_index()
hdfreset.columns = ['T', 'P', 'R']
hdfpivot=hdfreset.pivot('T', 'P')
X=hdfpivot.columns.levels[1].values
Y=hdfpivot.index.values
Z=hdfpivot.values
Xi,Yi = np.meshgrid(X, Y)
CS = plt.contourf(Yi, Xi, Z, alpha=0.7, cmap=plt.cm.jet);
cbar = plt.colorbar(CS)
plt.title('Density as a function of P and T')
plt.xlabel('Temperature [Celcius]')
plt.ylabel('Pressure [Bar]')
cbar.ax.set_ylabel('Density [kg/m^3]')
plt.savefig("table.png")

