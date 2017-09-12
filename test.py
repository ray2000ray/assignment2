from pylab import *

t = arange(0.0, 20.0, 1)
s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
s2 = [4, 5, 6, 7, 8, 9, 10, None, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

plot(t, s)
plot(t, s2)

xlabel('Item (s)')
ylabel('Value')
title('Python Line Chart: Plotting numbers')
grid(True)
show()