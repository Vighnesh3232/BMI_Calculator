# Import necessary libraries
import tkinter as tk
from tkinter import messagebox

# Create the main application window
app = tk.Tk()
app.title('BMI Calculator')
app.geometry('350x450')
app.configure(bg='#F7F7F7')  # Set background color

# Define fonts
font_title = ('Arial', 30, 'bold')
font_label = ('Arial', 18)
font_entry = ('Arial', 16)
font_button = ('Arial', 14, 'bold')

# Create and place elements in the window
title_label = tk.Label(app, text='BMI Calculator', font=font_title, bg='#F7F7F7')
title_label.pack(pady=20)

weight_label = tk.Label(app, text='Weight:', font=font_label, bg='#F7F7F7')
weight_label.pack()
weight_entry = tk.Entry(app, font=font_entry)
weight_entry.pack(pady=5)

weight_unit = tk.StringVar(app)
weight_unit.set('kg')  # Default unit is kg
weight_option = tk.OptionMenu(app, weight_unit, 'kg', 'lbs')
weight_option.pack(pady=5)

height_label = tk.Label(app, text='Height:', font=font_label, bg='#F7F7F7')
height_label.pack()
height_entry = tk.Entry(app, font=font_entry)
height_entry.pack(pady=5)

height_unit = tk.StringVar(app)
height_unit.set('cm')  # Default unit is cm
height_option = tk.OptionMenu(app, height_unit, 'cm', 'ft')
height_option.pack(pady=5)

# Calculate BMI function
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        if weight_unit.get() == 'lbs':
            weight *= 0.453592  # Convert lbs to kg

        height = float(height_entry.get())
        if height_unit.get() == 'ft':
            height *= 30.48  # Convert ft to cm

        height /= 100  # Convert cm to meters
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            bmi_category = "Underweight"
        elif 18.5 <= bmi < 25:
            bmi_category = "Normal Weight"
        elif 25 <= bmi < 30:
            bmi_category = "Overweight"
        else:
            bmi_category = "Obese"

        result_label.configure(text=f'Your BMI: {bmi:.1f} - {bmi_category}', fg='#06911F')
    except ValueError:
        messagebox.showerror('Error', 'Enter valid numbers for weight and height.')
    except ZeroDivisionError:
        messagebox.showerror('Error', 'Height cannot be zero.')

calculate_button = tk.Button(app, text='Calculate BMI', font=font_button, bg='#06911F', fg='white', command=calculate_bmi)
calculate_button.pack(pady=20)

result_label = tk.Label(app, text='', font=font_label, bg='#F7F7F7')
result_label.pack()

# Run the application
app.mainloop()
