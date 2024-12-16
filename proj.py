from tkinter import *
from tkinter import ttk, messagebox

# Conversion function
def convert_units():
    input_value = entry.get()
    try:
        input_value = float(input_value)
        from_unit = from_combobox.get().lower()
        to_unit = to_combobox.get().lower()
        selected_category = category_combobox.get().lower()

        # Debugging: Print the values to check
        print(f"Selected Category: {selected_category}")
        print(f"From Unit: {from_unit}, To Unit: {to_unit}")
        
        # Conversion factors
        conversions = {
            'mass': {'kg': 1, 'g': 1000, 'lb': 2.20462, 'oz': 35.274},
            'length': {'m': 1, 'cm': 100, 'mm': 1000, 'in': 39.3701, 'ft': 3.28084, 'yd': 1.09361, 'km': 0.001, 'mile': 0.000621371},
            'time': {'s': 1, 'min': 1/60, 'hr': 1/3600, 'day': 1/86400},
            'temperature': {'c': 1, 'f': lambda c: c * 9/5 + 32, 'k': lambda c: c + 273.15},
            'volume': {'l': 1, 'ml': 1000, 'm3': 0.001, 'gal': 0.264172, 'qt': 1.05669},
            'area': {'m2': 1, 'cm2': 10000, 'mm2': 1000000, 'in2': 1550, 'ft2': 10.7639, 'acre': 0.000247105, 'km2': 0.000001, 'mile2': 3.861e-7},
            'speed': {'m/s': 1, 'km/h': 3.6, 'mph': 2.23694, 'knot': 1.94384}
        }

        if selected_category not in conversions:
            result_label.config(text="Invalid category.")
            return

        units = conversions[selected_category]
        if selected_category == 'temperature':
            if from_unit == 'c':
                result = units[to_unit](input_value) if callable(units[to_unit]) else input_value
            elif from_unit == 'f':
                celsius = (input_value - 32) * 5/9
                result = units[to_unit](celsius) if callable(units[to_unit]) else celsius
            elif from_unit == 'k':
                celsius = input_value - 273.15
                result = units[to_unit](celsius) if callable(units[to_unit]) else celsius
        else:
            result = input_value * units[to_unit] / units[from_unit]

        result_label.config(text=f"Result: {result:.2f} {to_unit}")

    except ValueError:
        result_label.config(text="Invalid input, please enter a number.")
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")

# Update units based on category
def update_units(event):
    category = category_combobox.get().lower()
    if category == "mass":
        from_combobox.config(values=["kg", "g", "lb", "oz"])
        to_combobox.config(values=["kg", "g", "lb", "oz"])
    elif category == "length":
        from_combobox.config(values=["m", "cm", "mm", "in", "ft", "yd", "km", "mile"])
        to_combobox.config(values=["m", "cm", "mm", "in", "ft", "yd", "km", "mile"])
    elif category == "time":
        from_combobox.config(values=["s", "min", "hr", "day"])
        to_combobox.config(values=["s", "min", "hr", "day"])
    elif category == "temperature":
        from_combobox.config(values=["c", "f", "k"])
        to_combobox.config(values=["c", "f", "k"])
    elif category == "volume":
        from_combobox.config(values=["l", "ml", "m3", "gal", "qt"])
        to_combobox.config(values=["l", "ml", "m3", "gal", "qt"])
    elif category == "area":
        from_combobox.config(values=["m2", "cm2", "mm2", "in2", "ft2", "acre", "km2", "mile2"])
        to_combobox.config(values=["m2", "cm2", "mm2", "in2", "ft2", "acre", "km2", "mile2"])
    elif category == "speed":
        from_combobox.config(values=["m/s", "km/h", "mph", "knot"])
        to_combobox.config(values=["m/s", "km/h", "mph", "knot"])
    else:
        messagebox.showerror("Selection Error", "Please select a valid category from the dropdown!")

# Clear all inputs
def clear_all():
    category_combobox.set("Select Category")
    from_combobox.set("")
    to_combobox.set("")
    entry.delete(0, END)
    result_label.config(text="Result: ")

# Main window
root = Tk()
root.title("Unit Converter")
root.minsize(300, 300)
root.maxsize(350, 300)

# Widgets
Label(root, text="Category:", font="Arial 14").grid(row=0, column=0, pady=5, sticky=W)
category_combobox = ttk.Combobox(root, values=["Mass", "Length", "Time", "Temperature", "Volume", "Area", "Speed"], font="Arial 14", state="readonly")
category_combobox.grid(row=0, column=1, pady=5)
category_combobox.set("Select Category")
category_combobox.bind("<<ComboboxSelected>>", update_units)

Label(root, text="From Unit:", font="Arial 14").grid(row=1, column=0, pady=5, sticky=W)
from_combobox = ttk.Combobox(root, font="Arial 14", state="readonly")
from_combobox.grid(row=1, column=1, pady=5)

Label(root, text="To Unit:", font="Arial 14").grid(row=2, column=0, pady=5, sticky=W)
to_combobox = ttk.Combobox(root, font="Arial 14", state="readonly")
to_combobox.grid(row=2, column=1, pady=5)

Label(root, text="Value:", font="Arial 14").grid(row=3, column=0, pady=5, sticky=W)
entry = Entry(root, font="Arial 14")
entry.grid(row=3, column=1, pady=5)

convert_button = Button(root, text="Convert", font="Arial 14", command=convert_units)
convert_button.grid(row=4, column=0, columnspan=2, pady=10)

result_label = Label(root, text="Result: ", font="Arial 14")
result_label.grid(row=5, column=0, columnspan=2, pady=5)

clear_button = Button(root, text="Clear", font="Arial 14", command=clear_all)
clear_button.grid(row=6, column=0, pady = 5)


root.mainloop()