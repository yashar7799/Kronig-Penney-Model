import numpy as np
import matplotlib.pyplot as plt

# Constants:
a = 1  # If you change this, results won't change; because it appears only in Ka & ka spaces (see Eq 21b).
P = (3*np.pi)/2  # Pass different values to P and see what will happen to the results.
n = 5000  # Number of points that will be created for K space, if you increase this value, you will have better visual results (for figure 6).

# Codes for figure 5:
# Define a linear space for K:
K = np.linspace((-4*np.pi)/a, (4*np.pi)/a, n)

# Putting all K values in a list:
K_list = []
for K in K:
    K_list.append(K)

# Iterate in K_list and calculate energy for every K (for Figure 5):
e5 = []
for K in K_list:
    e5.append((P/(K*a))*np.sin(K*a) + np.cos(K*a))
    
# Generate Ka space to put as x-axis for Figure 5:
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
plt.ylabel('e: (P/Ka)sin(Ka) + cos(Ka)\n', loc='top',labelpad=-275, rotation=0, fontsize=20, color='green')

# Drawing horizantal lines y=1 and y=-1 :
plt.axhline(y=1, lw=0.75, color='r')
plt.axhline(y=-1, lw=0.75, color='r')

# Plot the final figure:
plt.plot(Ka_list, e5)

# Codes for figure 6:
# Iterate in K_list and calculate energy (for Figure 6) for every K >= 0 which satisfies this condition: -1 <= (P/Ka)sin(Ka) + cos(Ka) <= 1 :
# energy is in units ((h*pi)^2)/2ma^2 ,the same as in book.
e6 = []
for K in K_list:
    if (-1 <= (P/(K*a))*np.sin(K*a) + np.cos(K*a) <= 1) and K >= 0 :
        e6.append((K**2)/(np.pi**2))
        
# Define a linear space for k:      
k = np.linspace(0, (4*np.pi)/a, len(e6))

# Putting all k values in a list:
k_list = []
for k in k:
    k_list.append(k)

# Drawing a dashed line as seen in book (but I can't really find out why it doesn't result exactly like the book?!!)
y = []
for k in k_list:
    y.append((k**2)/(np.pi**2))

# Generate ka space to put as x-axis for Figure 6:
ka_list = []
for k in k_list:
    ka_list.append(k*a)

# Some settings for figure 6 plot:
# Setup an empty figure:
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(1, 1, 1)

# Passing xlabel and ylabel:
plt.xlabel('ka', loc='center', rotation=0, fontsize=20, color='green')
plt.ylabel('e', loc='center', rotation=0, fontsize=20, color='green')

# Plot the final figure:
plt.scatter(ka_list, e6, marker='.')
#plt.plot(ka_list, y, linestyle='--')
