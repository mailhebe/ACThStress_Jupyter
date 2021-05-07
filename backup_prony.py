# backup Prony series

def invmat(x,y,tau1,tau2,tau3,tau4):
    n0=np.ones(len(x))
    n1=1-np.exp(-x/10**tau1)
    n2=1-np.exp(-x/10**tau2)
    n3=1-np.exp(-x/10**tau3)
    n4=1-np.exp(-x/10**tau4)
    n5=x
    
    mtau=np.matrix([n0,n1,n2,n3,n4,n5]).T
    
    temp=mtau.T
    temp1=temp*mtau
    temp2=temp1.I
    temp3=temp2*temp
    temp4=temp3*np.array([y]).T
    
    return temp4
