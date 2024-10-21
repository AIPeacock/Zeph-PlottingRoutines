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
x_position = int(nx/2)                 # Z SLICE FIXED AT CENTRE unless stated otherwise -
x_position = 22     # to change, remove # from this line and state the line
slice_index = int((x_position/dx)-1)   # Have to remove 1 due to Python indexing
# Load the chosen data file as one long list
datafile = open('bx__05.dat','r')   # Define which file to analyse
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
# Plotting Bx for an (y,z) slice at a constant x
# Have to use rot90 to plot it the right way round
plt.imshow(np.rot90((tb[slice_index,:,:])),aspect = 'auto') 
# Change plot labels and add a colorbar
plt.xlabel(r'y ($\mu$m)')
plt.ylabel(r'z ($\mu$m)')
plt.title(r'$B_{x}$ for x = 22 $\mu$m at 5 ps')
plt.colorbar(extend="both")
#plt.clim(1.5, 2.9)
plt.show()