# %load copy of tb_slicer_Z.py
import matplotlib.pyplot as plt
import numpy as np
# Zeph input dimensions
nx = 44
ny = 44
nz = 1000
dy = 1.0**-6
dx = 1.0**-6
dz = 1.0**-6
# Choose z_position to take a slice from 
z_position = int(nz/2)                 # Z SLICE FIXED AT CENTRE unless stated otherwise -
z_position = 500     # to change, remove # from this line and state the line
slice_index = int((z_position/dz)-1)   # Have to remove 1 due to Python indexing
# Load the chosen data file as one long list
datafile = open('tb__05.dat','r')   # Define which file to analyse
numlines = (nx*ny*nz)             # Find number of lines in the data file
datafile.seek(0)
y = np.zeros(numlines)              # Create empty array to store data
i = 0
for line in datafile:    
     row=line.strip()
     column=row.split()            
     y[i]=float(column[0])
     i=i+1
datafile.close()
# Extract data into more convenient 3D array
tb = np.empty((nx, ny, nz))         # Create empty 3D array to store data
for iz in range(0,nz):
    for iy in range(0,ny):
        for ix in range(0,nx):
            n = ix + nx*(iy-1) + nx*ny*(iz-1)
            tb[ix, iy, iz] = y[n]
# Plotting Tb for an (x,y) slice at a constant z
# Have to use rot90 to plot it the right way round
plt.imshow(np.rot90(np.log10(tb[:,:,slice_index]))) 
# Change plot labels and add a colorbar
plt.xlabel(r'x ($\mu$m)')
plt.ylabel(r'y ($\mu$m)')
plt.title(r'log($T_{b}$) for z = 500 $\mu$m at 5 ps')
plt.colorbar(extend="both")
plt.clim(1.5, 2.9)
plt.show()
