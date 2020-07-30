"""Created on Sun May 10 15:53:11 2020 @author: dadhikar"""
import sys
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# import matplotlib.animation as animation


# create  backbone of the plot
fig = plt.figure(figsize=(5, 5), dpi=150, facecolor=None, edgecolor=None)
ax = fig.add_subplot(1,1,1, facecolor='cyan')
def animate_frame(i):
    data = open('stock_data.txt', 'r+').read()
    lines= data.split('\n')
    t = []
    stock_price = []
    for line in lines:
        time, price = line.split(',')
        t.append(float(time))
        stock_price.append(float(price))
    ax.clear()
    ax.plot(t, stock_price, ls='-.', lw=0.5, color='r', marker='o', ms=6)
    ax.set_xlabel('time [days]')
    ax.set_ylabel('stock price [$]')
    ax.set_title('stock trend')
        
    # myfile.close()    

#ani = animation.FuncAnimation(fig, animate_frame, interval=1000)
animation = FuncAnimation(fig, animate_frame, interval=500)

plt.show()
   
        