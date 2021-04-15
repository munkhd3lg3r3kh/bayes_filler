import os

#0 == open
#1 == closed

#believe bel(x)
bel = [0.5, 0.5]

#bel pa bel'(x)
belp = [0,0]

p_z_x = [[0.6, 0.2],[0.4, 0.8]]

#0 == open      |   push
#1 == closed    |   nothing
p_x_u_x = [[[1,0.8],[1,0]],[[0,0.2],[0,1]]]

def screen_clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def belpa(u):  
    for il in range(2):
        sum = 0  
        z = 0
        for i in p_x_u_x[il][u]:
            sum = sum + i*bel[z]
            z+=1
        belp[il] = sum
    

if __name__ == "__main__":
    #Cleaning...
    screen_clear()
    #Simulation counter
    k = 0
    while True: 
        print("Simulation ",(k+1))
        u = int(input("Command ( push : 1, do_nothing : 2 ): "))-1
        z = int(input("Sensor data (open : 1, closed : 2) : "))-1
        #normalization
        n = 0
        belpa(u)    
        for i in range(2):
            bel[i] = p_z_x[z][i] * belp[i] 
            n += bel[i]
        n = 1/n
        for i in range(2):
            bel[i] = n*bel[i]
        k+=1
        print("bel(x=open) : %.5f"%bel[0])
        print("bel(x=closed) : %.5f"%bel[1],"\n")



        