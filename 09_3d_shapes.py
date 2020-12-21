#09_3d_shapes:

def three_d_shapes():
    shape = str(input("Which 3d shape do you want to learn about?\
                      cube, Pyramid, Cylinder, Sphere, Cone,\
                      rectangular prism, triangular prism or\
                      a Hemisphere? "
                     )
               ).lower()
    shapes = ['cube', 
              'pyramid', 
              'cylinder', 
              'sphere', 
              'cone', 
              'rectangular prism', 
              'triangular prism', 
              'hemisphere'
             ]
    
    if shape in shapes:
        shape_dict = {'cube':[8,12,6], 'pyramid':[5,8,5], 'cylinder':[0,2,2], 'sphere':[0,0,0], 'cone':[1,1,1], 'rectangular prism':[8,12,6], 'triangular prism':[6,9,5], 'hemisphere':[1,0,1]}
        vertices = shape_dict[shape][0]
        edges = shape_dict[shape][1]
        faces = shape_dict[shape][2]
        
        print("{} has {} vertices, {} edges and {} faces.".format(shape.capitalize(),vertices,edges,faces))
three_d_shapes()