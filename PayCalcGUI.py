# Laurie Hall 
# PA_10 
# CIS156 Python
# Purpose: This will wirte a GUI program that calculates 
# employee pay including overtime at time and a half for 
# hours >40. Prompt user for hours # worked and pay rate. 
# Two lables-Caluclate and Quit


import tkinter

class PayCalcGUI:
    def __init__ (self): 

#create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title('Pay Calculator')
        self.main_window.geometry ('400x250')

#create four frames to group widgets
        self.frame1 = tkinter.Frame()
        self.frame2 = tkinter.Frame()
        self.frame3 = tkinter.Frame()
        self.frame4 = tkinter.Frame()

# Create the widgets for the top frame
        self.hours_label = tkinter.Label(self.frame1, \
                                text = 'Enter the number of hours worked for the week: ')
        self.hours_entry = tkinter.Entry(self.frame1, width=13)
        
        self.rate_label = tkinter.Label(self.frame2, \
                            text='Enter the rate of pay:')
        self.rate_entry = tkinter.Entry(self.frame2, width=13)

# Pack the top frame's widget 
        self.hours_label.pack(side='left')
        self.hours_entry.pack(side='left')
        self.rate_label.pack(side='left')
        self.rate_entry.pack(side='left')

# Create the widget for the midddle frame
        self.calculate_label = tkinter.Label(self.frame3, text = 'Calculate Pay: ')
    
# StringVar object to associate with output label. Use the object's set method
  # to store a string of blank characters.
        self.value = tkinter.StringVar()

#Create a label and associate it with StringVar object
        self.pay_label = tkinter.Label(self.frame3, textvariable = self.value)

# Pack the middle frame widgets
        self.calculate_label.pack(side='left')
        self.pay_label.pack(side='left')

# Create the buttom widgets for the bottom frame.
        self.calc_button = tkinter.Button(self.frame4, text = 'Calculate Pay', command = self.calculate)

        self.quit_button = tkinter.Button(self.frame4, text = 'Quit', command = self.main_window.destroy)  
    
# Pack the buttons 
        self.calc_button.pack(side='left', padx=15)
        self.quit_button.pack(side='left')

# Pack the frames
        self.frame1.pack(pady=5)
        self.frame2.pack(pady=5)
        self.frame3.pack(pady=5)
        self.frame4.pack(pady=5)

        tkinter.mainloop()

# Calculate method is a callback function for the Calculate button.
    def calculate(self):

# Get the values entered by the user into the hours and rate widgets
        hours = float(self.hours_entry.get())
        rate = float(self.rate_entry.get()) 

# Calculate pay with OT at time and a half
        pay = hours * rate 

        if hours > 40.0:
            pay = pay + ((hours - 40.0) * (rate * .5))

# Calculate pay and store it in the StringVal object
        self.value.set(pay)

# Create an instance of the KiloConverterGUI class
my_gui = PayCalcGUI ()

# thank you