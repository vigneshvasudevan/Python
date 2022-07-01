# first python program, this is a the way to do single line comment in python
from datetime import date #importing an module


'''
This is the way to do multi-line comment in python.
Python is fun to learn, let's enjoy learning python.

'''

print("Hello there") 
print("Today is ", date.today())
print("This is the day we wrote our first python program")



'''
How to run your first python program?

1. Install VS(Visual studio) code or any editor or IDE of your preference. 
    For vs code : https://code.visualstudio.com/download

    What's an IDE ? 
        IDE = Integrated Development Environment, It has 3 components
        1. Editor e.g) Notepad, Notepad++, Microsoft word where we write code
        2. Compiler/interpreter -> To run the program
        3. Debugger -> To debug the program
        

2. Install python from https://www.python.org

3. Add python to system environment variables

    For windows: 
        1. Copy the path where you have installed python, it’s usually
            C:\Users\YourUsername\AppData\Local\Programs\Python\Python310
            C:\Users\YourUsername\AppData\Local\Programs\Python\Python310\Scripts
        
    
        2. Open System Properties (Right click Computer in the start menu, or 
        use the keyboard shortcut Win+Pause)
        
        3. Click Advanced system settings in the sidebar.
        4. Click Environment Variables...
        5. Select PATH in the System variables section
        6. Click Edit
        7. Add Python's path to the end of the list (the paths are separated by semicolons).

    On completing this, open the command prompt on the Windows and run below command
        python --version
    
    sample output for the above command is: Python 3.8.9

4. Launch VS code and click on extensions. Search for python and install it

5. Optional step, search for Jupyter in VScode extensions and install it

6. Now that you're all set, click on the play button on the VScode to run your first 
    python code. 
    
    Note: If you face any problem at step6, try restarting the VScode once
'''