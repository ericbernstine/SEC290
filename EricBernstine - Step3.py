# SEC290.FALL2024.10264.B2 
# Eric Bernstine
# November 13th, 2024
# Week 4 programming assignment step 3.

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
        attr_name = input('Please enter an attribute name: ')
        attr_value = input('\nPlease enter an attribute value: ')
        attr_name = attr_name.lower()
        attr_value = attr_value.lower()
        window_attributes[attr_name] = attr_value
        print(f'\n{attr_name}: {window_attributes[attr_name]} has been added to the dictionary.')
        
    elif input_value == 'c':
        if 'width' in window_attributes and 'height' in window_attributes:
            
            try:
                height = int(window_attributes['height'])  
                width = int(window_attributes['width'])
                aspect_ratio = width / height
                print(f'\nAspect Ratio: {aspect_ratio}')
            except ValueError:
                print("\nError: 'width' and 'height' attributes must be valid integers.")
            except ZeroDivisionError:
                print("\nError: Height cannot be zero. Please re-enter a positive integer.")
                
        else:
            if 'width' not in window_attributes and 'height' not in window_attributes:
                print("\nError: Both 'width' and 'height' attributes must be entered.")
            elif 'width' not in window_attributes:
                print("\nError: The 'width' attribute must be entered.")
            elif 'height' not in window_attributes:
                print("\nError: The 'height' attribute must be entered.")
                
    elif input_value == 'd':
        print('\nDisplaying the window attributes.\n')
        for key in window_attributes:
            print(f'{key}: {window_attributes[key]}')
        
    else:
        print('Value not recognized, please enter a, b, c or d.')
    
    