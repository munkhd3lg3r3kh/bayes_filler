
#X : state of the door ( x1 == open, x2 == closed )
#z : measurement of sensor ( z1 == open, z2 == closed )
#u : command (1 == push , 2 == nothing )
#p : probability
#p_a : p(a) etc
#n : normalization

#0 == open
#1 == closed
bel = [0.5, 0.5]
p_z_x = [[0.6, 0.2],[0.4, 0.8]]

#0 == open, push
#1 == closed, nothing
p_x_u_x = [[[1,0.8],[1,0]],[[0,0.2],[0,1]]]

#this var is simulation counter
k = 0

def beli(j,u):
    sum = 0
    z = 0
    for i in p_x_u_x[j][u]:
        sum = sum + i*bel[z]
    return sum

if __name__ == "__main__":
    while True:
        a= int(input("open : 1, closed : 2: "))-1
        b=int(input("push : 1, nothing : 2: "))-1
        c=int(input("open : 1, closed : 2: "))-1
        print(p_x_u_x[a][b][c])