import numpy as np
import matplotlib
matplotlib.use('TKAgg')

from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import figure

step = 50
scale = 10000

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, scale), ylim=(-20, 20))
line, = ax.plot([], [], lw=2)

plotlays, plotcols = [3], ["blue","black","green"]
lines = []
for index in range(3):
    lobj = ax.plot([],[],lw=2,color=plotcols[index])[0]
    lines.append(lobj)

# initialization function: plot the background of each frame
def init():
    for line in lines:
        line.set_data([], [])
    return lines

# animation function.  This is called sequentially
def animate(i):
    x1, y1 = [],[]
    x2, y2 = [],[]
    x3, y3 = [],[]

    # All Planets
    x = np.linspace(0, scale, 1000)
    y = (
        .00808 * (np.sin((2 * np.pi / 87.97)  * (x - (step * i)))) + # Mercury
        .08711 * (np.sin((2 * np.pi / 224.71) * (x - (step * i)))) + # Venus
        .09091 * (np.sin((2 * np.pi / 365.26) * (x - (step * i)))) + # Earth
        .00791 * (np.sin((2 * np.pi / 686.99) * (x - (step * i)))) + # Mars
        12.673 * (np.sin((2 * np.pi / 4332.9) * (x - (step * i)))) + # Jupiter
        2.8017 * (np.sin((2 * np.pi / 10756)  * (x - (step * i)))) + # Saturn
        .30107 * (np.sin((2 * np.pi / 30688)  * (x - (step * i)))) + # Uranus
        .28539 * (np.sin((2 * np.pi / 60192)  * (x - (step * i)))) + # Neptune
        .00003 * (np.sin((2 * np.pi / 90592)  * (x - (step * i))))   # Pluto
        )
    x1.append(x)
    y1.append(y)
    
    # No Jupiter
    x = np.linspace(0, scale, 1000)
    y = (
        .00808 * (np.sin((2 * np.pi / 87.97)  * (x - (step * i)))) + # Mercury
        .08711 * (np.sin((2 * np.pi / 224.71) * (x - (step * i)))) + # Venus
        .09091 * (np.sin((2 * np.pi / 365.26) * (x - (step * i)))) + # Earth
        .00791 * (np.sin((2 * np.pi / 686.99) * (x - (step * i)))) + # Mars
        2.8017 * (np.sin((2 * np.pi / 10756)  * (x - (step * i)))) + # Saturn
        .30107 * (np.sin((2 * np.pi / 30688)  * (x - (step * i)))) + # Uranus
        .28539 * (np.sin((2 * np.pi / 60192)  * (x - (step * i)))) + # Neptune
        .00003 * (np.sin((2 * np.pi / 90592)  * (x - (step * i))))   # Pluto
        )
    x2.append(x)
    y2.append(y)

    # No Jupiter or Saturn
    x = np.linspace(0, scale, 1000)
    y = (
        .00808 * (np.sin((2 * np.pi / 87.97)  * (x - (step * i)))) + # Mercury
        .08711 * (np.sin((2 * np.pi / 224.71) * (x - (step * i)))) + # Venus
        .09091 * (np.sin((2 * np.pi / 365.26) * (x - (step * i)))) + # Earth
        .00791 * (np.sin((2 * np.pi / 686.99) * (x - (step * i)))) + # Mars
        .30107 * (np.sin((2 * np.pi / 30688)  * (x - (step * i)))) + # Uranus
        .28539 * (np.sin((2 * np.pi / 60192)  * (x - (step * i)))) + # Neptune
        .00003 * (np.sin((2 * np.pi / 90592)  * (x - (step * i))))   # Pluto
        )
    x3.append(x)
    y3.append(y)
    
    xList = [x1, x2, x3]
    yList = [y1, y2, y3]

    for lnum, line in enumerate(lines):
        line.set_data(xList[lnum], yList[lnum])

    #line.set_data(x, y)
    return lines

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
           frames=250, interval=40, blit=True)

mng = plt.get_current_fig_manager()

maxSize = mng.window.maxsize()
maxSize = (maxSize[0] * .9, maxSize[1] * .9)

mng.resize(*maxSize)

anim.save("sunWobbleWithModifications.mp4", dpi=256)

#plt.show()
