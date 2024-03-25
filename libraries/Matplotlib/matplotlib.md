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




### Markers
You can use the keyword argument marker to emphasize each point with a specified marker:

Example: Get your own Python Server
Mark each point with a circle:

```
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()
```

Result:
![image](https://github.com/yaswanthteja/Python-Interview-Questions/assets/93423367/2fe0c514-267d-4072-bab5-97d5f75d2680)


### Linestyle
You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line:

ExampleGet your own Python Server
Use a dotted line:
```
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()
```
Result:

![image](https://github.com/yaswanthteja/Python-Interview-Questions/assets/93423367/f4a72991-13d3-45c1-9a0c-9237815f8fb5)

Use a dashed line:

```
plt.plot(ypoints, linestyle = 'dashed')
```

![image](https://github.com/yaswanthteja/Python-Interview-Questions/assets/93423367/fa1e995d-feb7-45a1-a36b-fcb87680e14e)


### Shorter Syntax
The line style can be written in a shorter syntax:

linestyle can be written as ls.

dotted can be written as :.

dashed can be written as --.

Example
Shorter syntax:
```
plt.plot(ypoints, ls = ':')
```
Result:
![image](https://github.com/yaswanthteja/Python-Interview-Questions/assets/93423367/c0b924c1-8362-452c-9526-7cf2a2570026)


Line Styles
You can choose any of these styles:

Style	Or
- 'solid' (default)	'-'	
- 'dotted'	':'	
- 'dashed'	'--'	
- 'dashdot'	'-.'	
- 'None'	'' or ' '	
### Line Color
You can use the keyword argument color or the shorter c to set the color of the line:

Example
Set the line color to red:
```
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'r')
plt.show()
```
Result:

![image](https://github.com/yaswanthteja/Python-Interview-Questions/assets/93423367/de9e1cb7-267f-431c-823d-02272925aa7e)

Example
Plot with a beautiful green line:

...
plt.plot(ypoints, c = '#4CAF50')
...
Result:

![image](https://github.com/yaswanthteja/Python-Interview-Questions/assets/93423367/517d4fbf-0962-4f96-b2f3-f565f5a48292)

Example
Plot with the color named "hotpink":

...
plt.plot(ypoints, c = 'hotpink')
...
Result:

![image](https://github.com/yaswanthteja/Python-Interview-Questions/assets/93423367/2b57f46d-8bc1-48f3-9961-f4198f530c42)


### Line Width
You can use the keyword argument linewidth or the shorter lw to change the width of the line.

The value is a floating number, in points:

Example
Plot with a 20.5pt wide line:
```
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20.5')
plt.show()
```

![image](https://github.com/yaswanthteja/Python-Interview-Questions/assets/93423367/28a4a4b8-94d1-4ef5-b056-b26fc95c0081)


### Multiple Lines
You can plot as many lines as you like by simply adding more plt.plot() functions:

Example
Draw two lines by specifying a plt.plot() function for each line:
```
import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()

```
Result:
![image](https://github.com/yaswanthteja/Python-Interview-Questions/assets/93423367/dbf8521e-2386-44f3-9038-60dd91c71cd2)

You can also plot many lines by adding the points for the x- and y-axis for each line in the same plt.plot() function.

(In the examples above we only specified the points on the y-axis, meaning that the points on the x-axis got the the default values (0, 1, 2, 3).)

The x- and y- values come in pairs:

Example
Draw two lines by specifiyng the x- and y-point values for both lines:

```
import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()
```


![image](https://github.com/yaswanthteja/Python-Interview-Questions/assets/93423367/35507157-1e9a-4a50-ab53-0fd55aaff3cf)


