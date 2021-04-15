
x = []
z = [[]]



def sume(i):
    return float( z[i][0]*x[i] + z[i][1]*(1-x[i]))

if __name__ == "__main__":
    
    x.append("")
    i = 1
    x.append(0.5)
    while True: 
        z.append([float(input("Enter Z|open  : ")) , float(input("Enter Z|close  : "))])
        #z[i].append(float(input("Enter Z|open  : ")))
        #z[i].append(float(input("Enter Z|close : ")))

        #x[i+1] = (z[i]*x[i])/(sume(i))
        #a = (z[i][0]*x[i])/sume(i)
        x.append((z[i][0]*x[i])/sume(i))
        print("p(open|z) : %.3f" % x[i+1])
        i+=1
    
    
      
        