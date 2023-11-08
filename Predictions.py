import numpy as np
import matplotlib.pyplot as plt

x = np.array([1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990])
y = np.array([106.46, 123.08, 132.12, 152.27, 180.67, 205.05, 227.23, 249.46])

def fx (x1, coef):
    fx = 0
    n = len(coef) - 1
    for p in coef:
        fx = fx + p*x1**n
        n = n-1
    return fx

anno = 2000
for i in range(0, 10):
    coef = np.polyfit(x, y, i)
    p = np.polyval(coef, anno)

    print(f'To grade {i} the prediction is: {p}')
    x1 = np.linspace(1920, anno + 1, 1000)
    y1 = fx(x1, coef)  #Function
    plt.figure(figsize = [20, 10])
    plt.title('Liters vs years To grade: ' + str(i))

    plt.scatter(x, y, s= 120, c= 'blueviolet')
    plt.plot(x1, y1, '--', linewidth = 3, color= 'red')
    plt.scatter(anno, p, s= 200, c= 'red')
    plt.yticks(range(100, 320, 20))
    plt.grid('on')
    ax = plt.gca()
    ax.set_xlabel('Years')
    ax.set_ylabel('Number of liters')
    ax.set_axisbelow(True)
    plt.show()

#So.... what grade should we pick?

year = 2000
grade = np.arange(0, 20 + 1, 1) #from 0 to 100 but 1 by 1
aprox = np.array([])
y_pred_vec = np.array([])

for i in grade:
    coef = np.polyfit(x, y, i)
    p = np.polyval(coef, year)
    aprox = np.append(aprox, p)

    #To do the MSE(Mean Squared Error)
    y_pred_vec = np.array([])
    for j in x:
        y_pred = np.polyval(coef, j)
        y_pred_vec = np.append(y_pred_vec, y_pred)
    #print(f'los y: {y}')
    #print(f'the y_prox: {y_pred_vec}')
    MSE = (sum( (y - y_pred_vec)**2))/len(y)
    print(f'at grade {i} the MSE is {MSE}')
plt.figure(figsize= [20, 10])
plt.title('Polynomial grade vs prediction')
plt.plot(grade, aprox, '--', linewidth= 3, color= 'red')
plt.grid('on')
plt.show()

