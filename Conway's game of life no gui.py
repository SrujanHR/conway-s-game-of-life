'''so the griid(g) will be squar
r = rows 
c = columns
so 
we need r lists with c number of elements all being assigned 0 and 1 randomly
'''
import random
import time
d= int(input('Enter the size of the square grid eg 10: '))-1
def random_grid_generation(d):
    global r,c
    r = d
    c = r
    grid = []
    for i in range(r):
        temp = []
        for j in range(c):
            temp.append(random.randint(0,1))
        temp.append(temp[0])
        grid.append(temp)

    return grid
    
def display(grid):
    for h in range(r):
        print(str(grid[h]).replace('0',' ').replace(',','').replace('1','#'))
    print(str(grid[0]).replace('0',' ').replace(',','').replace('1','#'))


'''now we need to check the number of neighbours that are alive
so take the index y,x then check the states of 

(y-1,x-1) (y-1,x) (y-1,x+1)
 (y,x-1)   (y,x)   (y,x+1) 
(y+1,x-1) (y+1,x) (y+1,x+1)

but we have edges to deal with so we can try to use a try else loop

'''

def find_neighbours(grid):
    k = []
    l = []
    for y in range(r):

        if y ==r-1:
                        grid.append(grid[0])
        for x in range(c+1):
                try:
                    k.append(
                        [grid[y-1][x-1] ,grid[y-1][x] ,grid[y-1][x+1] ,
                        grid[y][x-1]  , grid[y][x]  , grid[y][x+1],
                        grid[y+1][x-1] ,grid[y+1][x] ,grid[y+1][x+1]])

                except IndexError:
                      pass
        #print(k)
        l.append(k)
        k = []
    grid.pop(-1)
    return l
def rule(neighbours):
    ng = []
    num = 0
    for f in neighbours:
            tl =[]

            for k in f:
                num +=1
                #print(k.count(1))
                if k.count(1)-k[4] >3 :
                     tl.append(0)
                elif k.count(1)-k[4] <= 1:
                    tl.append(0)
                elif k.count(1)-k[4] == 2 and k[4] == 0:
                    tl.append(0)
                elif k.count(1) -k[4]== 2 and k[4] == 1 :
                    tl.append(1)
                elif k.count(1)-k[4] ==3 :
                    tl.append(1)
                else:
                    tl.append (0)
            tl.append(tl[0])
            ng.append(tl)
    ng.append(ng[0])
    return ng

grid = random_grid_generation(d)
sjfg= grid
display(grid)
print()
for i in range(200):
    
    neighbours =find_neighbours(grid)
    new_grid = rule(neighbours)
    display(new_grid)
    grid = new_grid
    print()
    time.sleep(0.15)
display(sjfg)