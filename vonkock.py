## VON KOCK FLAKE

# Import libraries

import matplotlib.pyplot as plt
import math as mt

# Function to get X,Y coordonate from de two lists

def vonkoch(order,X=[0,1],Y=[0,0]):
    if order==0:
        return (X,Y)

    for l in range(order):
        i=0
        for betwX in range(len(X)-1):
            "Math part ... "
            u = [ (X[i+1]-X[i])/3 , (Y[i+1]-Y[i])/3 ]
            v = [ 2*(X[i+1]-X[i])/3 , 2*(Y[i+1]-Y[i])/3 ]
            w = [ (X[i+1]-X[i])/2 , (Y[i+1]-Y[i])/2 ]
            n = [ -(Y[i+1]-Y[i]) , (X[i+1]-X[i]) ]
            norm_n = mt.sqrt( n[0]**2 + n[1]**2 )
            N =  [ -(Y[i+1]-Y[i])/norm_n , (X[i+1]-X[i])/norm_n ]
            L = mt.sqrt( abs(X[i+1]-X[i])**2 + abs(Y[i+1]-Y[i])**2 )
            I = [ X[i]+w[0] , Y[i]+w[1] ]
            c = L/6 * mt.tan(mt.pi/3)

            "insert at 1/3"
            X.insert(i+1, X[i]+u[0])
            Y.insert(i+1, Y[i]+u[1])

            "insert at 2/3"
            X.insert(i+2, X[i]+v[0])
            Y.insert(i+2, Y[i]+v[1])

            "insert the top"
            X.insert(i+2, I[0]+N[0]*c)
            Y.insert(i+2, I[1]+N[1]*c)

            i+= 4

    return (X,Y)

# Function for draw the courb of Von Koch in order n

def trace(order):
    Xf = vonkoch(order,[0,1],[0,0])[0]
    Yf = vonkoch(order,[0,1],[0,0])[1]
    plt.plot(Xf ,Yf, color="black")
    plt.axis('equal')
    plt.show()
    plt.close()

# Function for draw the Von Koch flake in order n

def flake(order):
    X1 = vonkoch(order,[0,1],[0,0])[0]
    Y1 = vonkoch(order,[0,1],[0,0])[1]
    X2 = vonkoch(order,[1,1/2],[0,-mt.sqrt(3)/2])[0]
    Y2 = vonkoch(order,[1,1/2],[0,-mt.sqrt(3)/2])[1]
    X3 = vonkoch(order,[1/2,0],[-mt.sqrt(3)/2,0])[0]
    Y3 = vonkoch(order,[1/2,0],[-mt.sqrt(3)/2,0])[1]

    Xf = X1+X2+X3 ; Yf = Y1+Y2+Y3

    plt.plot(Xf ,Yf, color="black")
    plt.axis('equal')
    plt.show()
    plt.close()


# Do a pretty flake :
flake(7)










