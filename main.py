import tkinter as tk

def converter_cm_m():

  try:
    cm = float(cm_entry.get())
    metros = cm / 100
    result_label.config(text=f"{cm} centímetros é igual a {metros:.2f} metros")
  except ValueError:
    result_label.config(text="Porfavor entre um número válido.")

# Create the main window
window = tk.Tk()
window.title("Converter centímetros para metros")

# Create input label and entry field
cm_label = tk.Label(window, text="entrar centímetros:")
cm_label.pack()
cm_entry = tk.Entry(window)
cm_entry.pack()

# Create conversion button
converter_button = tk.Button(window, text="Converter", command=converter_cm_m)
converter_button.pack()

# Create result label
result_label = tk.Label(window, text="")
result_label.pack()

# Run the main loop
window.mainloop()
