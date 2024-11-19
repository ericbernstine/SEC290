# SEC290.FALL2024.10264.B2 
# Eric Bernstine
# November 13th, 2024
# Week 4 programming assignment step 1.

window_attributes = {}

menu = """
     Window Administration Application

     a: Exit application.
     b: Enter an attribute.
     c: Calculate and display the aspect ratio.
     d: Display the window attributes and values. """
done = False
while not done:
    
    print(menu)
    
    input_value = input("Please make a selection: ")
    input_value = input_value.lower()
    
    if input_value == 'a':
        print('Done!')
        done = True
    elif input_value == 'b':
        print('Entering an attribute selected.')
    elif input_value == 'c':
        print('Calculate aspect ratio selected.')
    elif input_value == 'd':
        print('Display the attributes and values selected.')
    else:
        print('Value not recognized, please enter a, b, c or d.')
    
    