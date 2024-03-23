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



### Plotting x and y points

The plot() function is used to draw points (markers) in a diagram.

By default, the plot() function draws a line from point to point.

The function takes parameters for specifying points in the diagram.

Parameter 1 is an array containing the points on the x-axis.

Parameter 2 is an array containing the points on the y-axis.

If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.


Draw a line in a diagram from position (1, 3) to position (8, 10):
```
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()
```

![image](https://github.com/yaswanthteja/Python-Interview-Questions/assets/93423367/32d3d99a-0498-4fd7-aa12-df98042400be)
