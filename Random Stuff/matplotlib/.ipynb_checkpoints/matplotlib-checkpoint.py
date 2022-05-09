import matplotlib.pyplot as plt
import numpy as np

# Create a list of evenly-spaced numbers over the range
x = np.linspace(0, 20, 100)  
# Create the sine of each x points
plt.plot(x, np.sin(x))       
# Display the plot
plt.show()