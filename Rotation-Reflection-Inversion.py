import numpy as np
import matplotlib.pyplot as plt

#DEfine the 2d point
point = np.array([6,1])
rotation_angle= 60

print(point)
print(rotation_angle)

#writing a function rotate 2d
def rotate_2d(point , angle_degree) :
  angle_radians = np.radians(angle_degree)
  rotation_matrix = np.array([[np.cos(angle_radians),-np.sin(angle_radians)],[np.sin(angle_radians),np.cos(angle_radians)] ])
  return np.dot(rotation_matrix, point) #np.matmu() can also be used

#rotation operation on point
rotated_point = rotate_2d(point , rotation_angle)
print(rotated_point)



#inversion

def invert_2d(point):
    inversion_matrix = np.array([[-1,0],[0,-1]])
    return np.dot(inversion_matrix,point)
#perform inversion
inverted_point = invert_2d(point)
print("inverted through origin", inverted_point)



# reflection operation
def reflect_2d(point, axis='x') :
    if axis == 'x':
      reflection_matrix = np.array([[1,0],[0,-1]])
    elif axis == 'y':
      reflection_matrix = np.array([[-1,0],[0,1]])
    else:
      raise ValueError("axis must be x or y")
    return np.dot(reflection_matrix, point)

print("inverted through origin", reflected_point)



#improper rotation operation

def improper_rotation_2d(point, angle_degree):
    rotated_point = rotate_2d(point, angle_degree)
    return invert_2d(rotated_point)

#perform improper rotation
improper_rotate_point = improper_rotation_2d(point, 90)
print("improperlyn rotated point (90 degrees + inversion)")
  #visualisation


plt.figure(figsize=(6,6)) #


plt.scatter(0,0,color='white', edgecolor='black', s=50,marker='o', label= 'Origin')

#plot straight lines
plt.plot([-10,10],[0,0],color='black',linestyle='--', linewidth=1) #xaxis
plt.plot([0,0],[-10,10],color='black',linestyle='--', linewidth=1) #yaxis

#original point in blue
plt.scatter(point[0], point[1], color='blue', s=100, label='original point')

#rotated point in red
plt.scatter(rotated_point[0],rotated_point[1], color='red', s=100, label='roated point')
plt.scatter(inverted_point[0],inverted_point[1], color='green', s=100, label='inverted point')
reflected_point = reflect_2d(point,'x')
plt.scatter(reflected_point[0],reflected_point[1], color='orange', s=100, label='reflected point')
reflected_point = reflect_2d(point,'y')
plt.scatter(reflected_point[0],reflected_point[1], color='orange', s=100, label='reflected point')
plt.scatter(improper_rotate_point[0],improper_rotate_point[1], color='magenta', s=100, label='improper rotated point point')
plt.xlabel('X')
plt.ylabel('Y')

plt.title('2D Rotational Symmetry about the origin' , pad=20)

plt.grid(True)

# set equal scaling and limits
plt.gca().set_aspect('equal', adjustable='box')
plt.xlim(-10,10)
plt.ylim(-10,10)

#place the legent outside the plot area
plt.legend(loc='upper left', bbox_to_anchor=(1,1))

plt.show()
