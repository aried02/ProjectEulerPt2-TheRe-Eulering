# A utility function to calculate area 
# of triangle formed by (x1, y1), 
# (x2, y2) and (x3, y3)
# borrowed from internet
# original author: Danish Raza

def area(x1, y1, x2, y2, x3, y3):
 
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) 
                + x3 * (y1 - y2)) / 2.0)
 
 
# A function to check whether point P(x, y)
# lies inside the triangle formed by 
# A(x1, y1), B(x2, y2) and C(x3, y3) 
def isInside((x1, y1, x2, y2, x3, y3), x, y):
 
    # Calculate area of triangle ABC
    A = area (x1, y1, x2, y2, x3, y3)
 
    # Calculate area of triangle PBC 
    A1 = area (x, y, x2, y2, x3, y3)
     
    # Calculate area of triangle PAC 
    A2 = area (x1, y1, x, y, x3, y3)
     
    # Calculate area of triangle PAB 
    A3 = area (x1, y1, x2, y2, x, y)
     
    # Check if sum of A1, A2 and A3 
    # is same as A
    if(A == A1 + A2 + A3):
        return True
    else:
        return False
 
counter = 0
with open('triangles.txt') as f:
    for line in f:
        tri = line.split(',')
        tri[-1] = tri[-1][:-1]
        tri = [int(x) for x in tri]
        if isInside(tri, 0, 0):
            counter = counter+1

print(counter)