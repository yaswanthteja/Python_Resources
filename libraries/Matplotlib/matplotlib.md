## Matplotlib


Matplotlib is a low-level graph plotting library in Python that serves as a visualization utility.

Matplotlib was created by John D. Hunter.

Matplotlib is open source and we can use it freely.

Matplotlib is mostly written in Python, a few segments are written in C, Objective-C and Javascript for Platform compatibility.


Most of the Matplotlib utilities lie under the pyplot submodule, and are usually imported under the plt alias:

import matplotlib.pyplot as plt
Now the Pyplot package can be referred to as plt.

ExampleGet your own Python Server
Draw a line in a diagram from position (0,0) to position (6,250):
```
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()
```
Result:

![image](https://github.com/yaswanthteja/Python-Interview-Questions/assets/93423367/29352d89-3384-468b-91a1-3cefd80c6706)
