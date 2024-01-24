#We have to have the Module ready to go for matplotlib, similar to having an app for that
#there are best practices to download a copy and use a virtual environment to not disturb the root python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))

plt.show()

print("Hello World!")

# Step 1: Create Virtual environment(VE) " py -3 -m venv myvenv"
# myvenv is the name of the VE, we can change this name to anything we want
# Step 2: Activate the VE, in terminal type 'myvenv/scripts/activate'
# Step 3: Install the needed 3rd Party module "pip3 install 'libraryname'"

#Git-Hub / Source Control is tracking all of tha changes that we make to this document.