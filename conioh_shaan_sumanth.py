# -*- coding: utf-8 -*-
"""conioh_shaan_sumanth.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IDHE32URy8viTBiKm7Z4NS2KPeHcTrXK

## Imports
"""

# Commented out IPython magic to ensure Python compatibility.
!pip3 install symbeam
# %matplotlib inline
from symbeam import beam

"""---

# Input

**Set beam type and length**
"""

beam_type = int(input("Choose beam type: \n1.Cantilever \n2.Simply Supported \nChoice:"))
beam_length = int(input("Enter beam length: "))

"""**Set Supports for Beam**


"""

# Set supports for Cantilever
if beam_type == 1:
  left_support = 'fixed'

# Set supports for SimplySupported
elif beam_type == 2:
  left_support = 'pin'
  right_support = 'roller'

else:
  print('Wrong choice!')

"""**Add Loads**"""

point_load_list = []
udl_load_list = []
moment_list = []

print("********************************************************************************************")
load_choice = int(input("\nAdd Loads: \n1.Point Load \n2.UDL \n3.Moment \n0.Finish \nChoice: "))

while load_choice != 0:
  if load_choice == 1:
    point_load_list.append({'mag':int(input("\tEnter magnitude of point load (in N, upward is +ve, downward is -ve): ")), 
                            'pos':int(input("\tEnter distance of point load (from left end): "))})
  elif load_choice == 2:
    udl_load_list.append({'mag':int(input("\tEnter magnitude of UDL (in Nm, upwards is +ve, downwards is -ve): ")), 
                          'start':int(input("\tEnter starting point of UDL (from left end): ")), 
                          'end':int(input("\tEnter ending point of UDL (from left end):"))})
  elif load_choice == 3:
    moment_list.append({'mag':int(input("\tEnter magnitude of moment (in Nm, clockwise is +ve, anitclockwise is -ve): ")), 
                        'pos':int(input("\tEnter distance of moment (from left end): "))})
  else:
    print("Wrong choice\n")

  print("\n********************************************************************************************")

  load_choice = int(input("Add Loads: \n1.Point Load \n2.UDL \n3.Moment \n0.Finish \nChoice: "))

"""---

## Initialize Beam






"""

new = beam(length = beam_length)

"""## Add supports
Options are `pin`, `roller` and `fixed`
"""

# Add left support
new.add_support(x_coord = 0, support_type = left_support)

# Add right support, skip if cantalever
if beam_type != 1:
  new.add_support(x_coord = beam_length, support_type = right_support)

"""## Add loads
Apply external loads to the beam. These can be point forces, point moments or distributed forces.
"""

# Add Point Load
for point_load in point_load_list:
  new.add_point_load(x_coord = point_load['pos'], value = point_load['mag'])

# Add Uniformly Distributed Load
for udl_load in udl_load_list:
  new.add_distributed_load(x_start = udl_load['start'], x_end = udl_load['end'], expression = udl_load['mag'])

# Add Moments
for moments in moment_list:
  new.add_point_moment(x_coord = moments['pos'], value = moments['mag'])

"""## Solve the problem and plot the results"""

new.solve()

new.plot()