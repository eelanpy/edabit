#10_exam_3d_shapes_version1:

def exam_3d():

    shape_dict = {'cube':[8,12,6], 'pyramid':[5,8,5], 'cylinder':[0,2,2], 'sphere':[0,0,0], 'cone':[1,1,1], 'rectangular prism':[8,12,6], 'triangular prism':[6,9,5], 'hemisphere':[1,0,1], 'circle':[0,0,0]}
    points = 0
    round = 1
    while round <= 10:
        
        print("Welcome to round {}".format(round))
        lst_questions = ['A solid object has six faces which are all squares. What is the name of this object? ',
                         'The shape of a can of soup is an everyday example of a...',
                         'Baked beans usually come in what shaped cans? ',
                         'Most dice are the shape of which 3-D shape? ',
                         'A cupboard usually has the shape of which 3-D shape? ',
                         '3-D shapes are regular when all the faces are equal. Which 3-D shape is regular? ',
                         'What shape can be the cross section of a cylinder?',
                         'How many edges does a cylinder have?'
                         'How many edges does a cube have?',
                         'How many vertices does a cylinder have?']
        
        question1 = input(lst_questions[0])
        if question1 in shape_dict.keys() and question1 == 'cube':
            print("You got it correct!")
            round += 1
            points += 1
            
        question2 = input(lst_questions[1])  
        if question2 in shape_dict.keys() and question2 == 'cylinder':
            print("You got it correct!")
            round += 1
            points += 1
                    
        question3 = input(lst_questions[2])
        if question3 in shape_dict.keys() and question3 == 'cylinder':
            print("You got it correct!")
            round += 1
            points += 1
         
        question4 = input(lst_questions[3])
        if question4 in shape_dict.keys() and question4 == 'cube':
            print("You got it correct!")
            round += 1
            points += 1
        question5 = input(lst_questions[4])
        if question5 in shape_dict.keys() and question5 == 'rectangular prism':
            print("You got it correct!")
            round += 1
            points += 1
            
        question6 = input(lst_questions[5])
        if question6 in shape_dict.keys() and question6 == 'cube':
            print("You got it correct!")
            round += 1
            points += 1
            
        question7 = input(lst_questions[6])
        if question7 in shape_dict.keys() and question7 == 'circle':
            print("You got it correct!")
            round += 1
            points += 1
        
        question8 = input(lst_questions[7])
        if question8 in shape_dict.keys() and question7 == '2':
            print("You got it correct!")
            round += 1
            points += 1
        
        question9 = input(lst_questions[8])
        if question9 in shape_dict.keys() and question9 == '12':
            print("You got it correct!")
            round += 1
            points += 1
        
        question10 = input(lst_questions[9])
        if question10 in shape_dict.keys() and question10 == '0':
            print("You got it correct!")
            round += 1
            points += 1
            
        print("You got {} points!!".format(points))    
        break
    
exam_3d()