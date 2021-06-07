import numpy as np
import matplotlib.pyplot as plt

# Constants:
a = 1  # If you change this, unlike the 21b Eq, results will be changed (only for figure 5); because it appears as a coefficient too (see Eq 21a).
b = 1  # It is a coefficient too, so if you pass different values, it will change results (again only for figure 5).
P = (3*np.pi)/2  # Pass different values to P and see what will happen to the results.
n = 10000  # Number of points that will be created for K space, if you increase this value, you will have better visual results (for figure 6).

# Equations
Q = ((2*P)/(a*b))**0.5

# Codes for figure 5 (for Eq 21a):
# Define a linear space for K:
K = np.linspace((-4*np.pi)/a, (4*np.pi)/a, n)

# Putting all K values in a list:
K_list = []
for K in K:
    K_list.append(K)

# Iterate in K_list and calculate energy for every K (for Figure 5 with Eq 21a):
e5 = []
for K in K_list:
    e5.append(((Q**2 - K**2)/(2*Q*K))*np.sinh(Q*b)*np.sin(K*a) + np.cosh(Q*b)*np.cos(K*a))
    
# Generate Ka space to put as x-axis:
Ka_list = []
for K in K_list:
    Ka_list.append(K*a)

# Some settings for Figure 5 plot:
# Setup an empty figure:
fig = plt.figure(figsize=(16,9))
ax = fig.add_subplot(1, 1, 1)

# Move left y-axis and bottim x-axis to centre, passing through (0,0):
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

# Eliminate upper and right axes:
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Show ticks in the left and lower axes only:
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Passing xlabel and ylabel:
plt.xlabel('Ka', loc='right', labelpad=-10, rotation=0, fontsize=20, color='green')
plt.ylabel('e: [(Q^2 - K^2)/2QK]sinh(Qb)sin(Ka) + cosh(Qb)cos(Ka)\n', loc='top',labelpad=-450, rotation=0, fontsize=20, color='green')

# Drawing horizantal lines y=1 and y=-1 :
plt.axhline(y=1, lw=0.75, color='r')
plt.axhline(y=-1, lw=0.75, color='r')

# Plot the final figure:
plt.plot(Ka_list, e5)

# Codes for figure 6 (Eq 21a):
# Iterate in K_list and calculate energy for every K >= 0 which satisfies this condition: -1 <= [(Q^2 - K^2)/2QK]sinh(Qb)sin(Ka) + cosh(Qb)cos(Ka) <= 1 :
# energy is in units ((h*pi)^2)/2ma^2 ,the same as in book.
e6 = []
for K in K_list:
    if (-1 <= ((Q**2 - K**2)/(2*Q*K))*np.sinh(Q*b)*np.sin(K*a) + np.cosh(Q*b)*np.cos(K*a) <= 1) and K >= 0 :
        e6.append((K**2)/(np.pi**2))
        
# Define a linear space for k:      
k = np.linspace(0, (4*np.pi)/(a+b), len(e6))

# Putting all k values in a list:
k_list = []
for k in k:
    k_list.append(k)

# Drawing a dashed line as seen in book (but I can't really find out why it doesn't result exactly like the book?!!)
y = []
for k in k_list:
    y.append((k**2)/(np.pi**2))

# Generate k(a+b) space to put as x-axis for Figure 6:
ka_kb_list = []
for k in k_list:
    ka_kb_list.append(k*a + k*b)

# Some settings for figure 6 plot (for Eq 21a):
# Setup an empty figure:
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(1, 1, 1)

# Passing xlabel and ylabel:
plt.xlabel('k(a+b)', loc='center', rotation=0, fontsize=20, color='green')
plt.ylabel('e', loc='center', rotation=0, fontsize=20, color='green')

# Plot the final figure:
plt.scatter(ka_kb_list, e6, marker='.')
#plt.plot(ka_kb_list, y, linestyle='--')
