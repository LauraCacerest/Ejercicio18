import numpy as np 
import matplotlib.pyplot as plt

datos=np.loadtxt('numeros.txt')

x=datos[:,0]
y=datos[:,1]
x=np.linspace(0,3,50)
ed=np.exp(-x)

plt.figure()
plt.plot(x,ed)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
plt.savefig('primerorden.png')

