from matplotlib import pyplot as plt
import numpy as np
from matplotlib import dates as mdates
import datetime as dt
from matplotlib import style

print(plt.style.available)
style.use('fivethirtyeight')

fig=plt.figure()
ax1 = plt.subplot2grid ((1,1),(0,0))
events = {}

e = {'v':'22','f':'22','b':'0','j':'0'}
f = {'v':'0','e':'0','b':'0','j':'0'}
b = {'v':'0','f':'0','e':'0','j':'0'}
v = {'e':'4','f':'0','b':'5,5','j':'5,5'}
j = {'e':'0','f':'0','b':'0','v':'0'}
people = {e,f,b,v,j}
with plt.xkcd():
    ax1.plot(event,people, '-', label='event')
