import math
u= int(input("Give initial velocity:"))
a= int(input("Give final velocity: "))
s=int( input("Give distance travelled: "))
v_sq = u*u + 2*a*s
v=math.sqrt(v_sq)
print ( "Final velocity (v):" , v)
