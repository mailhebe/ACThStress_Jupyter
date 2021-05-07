for i in range(len(time)):
    for k in range(len(zm)):
        ttemp=0
        for j in range(len(p)):
            temp0=p[j]/time[i] #here is the 0 div by time[0]
            
            #temp1=temp0/kac
            #r1=cmath.sqrt(temp1)
            #temp1=temp0/kag
            #r2=cmath.sqrt(temp1)
            #temp2=aac*r1
            #temp3=aag*r2
            #temp4=temp2/temp3
            #llrp=1+temp4.real
            #llrm=1-temp4.real
            #ldiv=llrp/llrm
            
            r1=cmath.sqrt(temp0/kac) #equiv r1
            r2=cmath.sqrt(temp0/kag) #equiv r2
            mixprop=(aac/aag)*(r1/r2) #equiv temp4
            ldiv=(1+mixprop.real)/(1-mixprop.real) #equiv ldiv
            
            fs=((tmax+tmin)/2)/temp0+(6*math.pi*(tmax-tmin))/(144*temp0**2+math.pi**2)
                        
            #temp2=tamb/temp0
            #temp3=fs-temp2
            #temp4=2*zmax*r1
            #temp5=cmath.exp(temp4)
            #temp6=ldiv*temp5
            #temp7=1-temp6
            #a=temp3/temp7
            
            a=(fs-tamb/temp0)/(1-ldiv*cmath.exp(2*zmax*r1))
                        
            #temp1=zm[k]*r1
            #temp2=cmath.exp(temp1)
            #temp3=(2*zmax-zm[k])*r1
            #temp4=cmath.exp(temp3)
            #temp5=ldiv*temp4
            #temp6=temp2-temp5
            
            b=cmath.exp(zm[k]*r1)-ldiv*cmath.exp((2*zmax-zm[k])*r1)
                        
            #U=a*temp6
            
            U=a*b
            FFs=temp0*U
            
            out=m[j]*FFs
            ttemp=ttemp+out.real
            
        ftemp[i,k]=ttemp+tamb