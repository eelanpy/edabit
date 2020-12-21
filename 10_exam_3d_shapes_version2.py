#10_exam_3d_shapes_version2:

def exam_3d2():
    import random as rand
    points = 0
    rounds = 1
    while rounds <= 10:
        questions = ['A solid object has six faces which are all squares. What is the name of this object? ',
                         'The shape of a can of soup is an everyday example of a...',
                         'Baked beans usually come in what shaped cans? ',
                         'Most dice are the shape of which 3-D shape? ',
                         'A cupboard usually has the shape of which 3-D shape? ',
                         '3-D shapes are regular when all the faces are equal. Which 3-D shape is regular? ',
                         'What shape can be the cross section of a cylinder? ',
                         'How many edges does a cylinder have? ',
                         'How many edges does a cube have? ',
                         'How many vertices does a cylinder have? ']
        
        answers = ['cube',
                         'cylinder',
                         'cylinder',
                         'cube',
                         'rectangular prism',
                         'cube',
                         'circle',
                         '2',
                         '12',
                         '0']
        
        question_num = rand.randint(0,len(questions)-1)
        response = input("\nWelcome to round {}.\n {}".format(rounds,questions[question_num]+ ' '))
        answer = answers[question_num]
        rounds += 1
        
        if response == answer:
            points += 1
            print("You got it correct! ")
        else:
            print("Wrong  answer! \n")
       
            
    print("You got {} points!!".format(points))    

    
exam_3d2()