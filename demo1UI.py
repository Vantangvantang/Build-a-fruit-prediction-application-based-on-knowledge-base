import tkinter as tk
from tkinter import ttk
import random

# List of fruits
fruits = ["Banana", "Watermelon", "Honeydew", "Cantaloupe", "Apple", "Apricot", "Cherry", "Orange", "Peach", "Plume"]

# Function to select a random fruit
def select_random_fruit():
    return random.choice(fruits)

# Randomly select a fruit
selected_fruit = select_random_fruit()
print("Selected fruit:", selected_fruit)

def predict_fruit(shape, diameter, surface, color, seed_class, fruit_class):
    if (shape == "long" or shape == "round") and (color == "green" or color == "yellow"):
        return "Banana"
    elif (shape == "round" or shape == "oblong") and diameter > 4:
        return "Vines"
    elif shape == "round" and diameter < 4:
        return "Tree"
    elif fruit_class == "vine" and color == "green":
        return "Watermelon"
    elif fruit_class == "vine" and surface == "smooth" and color == "yellow":
        return "Honeydew"
    elif fruit_class == "vine" and surface == "rough" and color == "tan":
        return "Cantaloupe"
    elif (color == "green" or color == "yellow" or color == "red") and fruit_class == "tree" and seed_class == "multiple":
        return "Apple"
    elif color == "orange" and fruit_class == "tree" and seed_class == "stonefruit":
        return "Apricot"
    elif color == "red" and fruit_class == "tree" and seed_class == "stonefruit":
        return "Cherry"
    elif color == "orange" and fruit_class == "tree" and seed_class == "multiple":
        return "Orange"
    elif color == "orange" and fruit_class == "tree" and seed_class == "stonefruit":
        return "Peach"
    elif color == "purple" and fruit_class == "tree" and seed_class == "stonefruit":
        return "Plume"
    else:
        return "Unknown"

def yesorno(selected_fruit, fruitname):
    if selected_fruit == fruitname:
        return "Success"
    else:
        return "Failed"

def predict():
    shape = shape_combobox.get()
    diameter = float(diameter_entry.get() or 0.0)
    surface = surface_combobox.get()
    color = color_combobox.get()
    seed_class = seed_class_combobox.get()
    fruit_class = fruit_class_combobox.get()

    fruitname = predict_fruit(shape, diameter, surface, color, seed_class, fruit_class)
    result = yesorno(selected_fruit, fruitname)
    
    result_label.config(text=f"Predicted: {fruitname}\nResult: {result}")

def reset():
    global selected_fruit
    selected_fruit = select_random_fruit()
    print("New selected fruit:", selected_fruit)
    
    shape_combobox.set("None")
    diameter_entry.delete(0, tk.END)
    surface_combobox.set("None")
    color_combobox.set("None")
    seed_class_combobox.set("None")
    fruit_class_combobox.set("None")
    
    result_label.config(text="")
    selected_fruit_label.config(text=f"Selected Fruit: {selected_fruit}")

# Set up the main application window
root = tk.Tk()
root.title("Fruit Predictor")
root.geometry("400x500")
root.configure(bg="#f0f0f0")

# Create a style
style = ttk.Style()
style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
style.configure("TButton", background="#4CAF50", foreground="black", font=("Arial", 10, "bold"))
style.configure("TCombobox", font=("Arial", 10))

# Frame for input fields
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=20)

# Input fields
ttk.Label(input_frame, text="Shape:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
shape_combobox = ttk.Combobox(input_frame, values=["None", "long", "round", "oblong"])
shape_combobox.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(input_frame, text="Diameter (inch):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
diameter_entry = tk.Entry(input_frame)
diameter_entry.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(input_frame, text="Surface:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
surface_combobox = ttk.Combobox(input_frame, values=["None", "smooth", "rough"])
surface_combobox.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(input_frame, text="Color:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
color_combobox = ttk.Combobox(input_frame, values=["None", "green", "yellow", "tan", "orange", "red", "purple"])
color_combobox.grid(row=3, column=1, padx=10, pady=5)

ttk.Label(input_frame, text="Seed Class:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
seed_class_combobox = ttk.Combobox(input_frame, values=["None", "multiple", "stonefruit"])
seed_class_combobox.grid(row=4, column=1, padx=10, pady=5)

ttk.Label(input_frame, text="Fruit Class:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
fruit_class_combobox = ttk.Combobox(input_frame, values=["None", "vine", "tree"])
fruit_class_combobox.grid(row=5, column=1, padx=10, pady=5)

# Frame for buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

# Button to predict fruit
predict_button = ttk.Button(button_frame, text="Predict Fruit", command=predict)
predict_button.grid(row=0, column=0, padx=10, pady=10)

# Button to reset
reset_button = ttk.Button(button_frame, text="Reset", command=reset)
reset_button.grid(row=0, column=1, padx=10, pady=10)

# Label to display results
result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

# Display the selected fruit
selected_fruit_label = ttk.Label(root, text=f"Selected Fruit: {selected_fruit}", font=("Arial", 12, "bold"))
selected_fruit_label.pack(pady=10)

# Label for note
note_label = ttk.Label(root, text="If not selected, choose None | For Diameter, enter 0 if unknown", font=("Arial", 8))
note_label.pack(pady=10)

# Start the main loop
root.mainloop()
