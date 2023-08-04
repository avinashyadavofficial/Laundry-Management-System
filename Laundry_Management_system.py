import tkinter as tk
class LaundryCounter:
 def __init__(self, master):
 self.master = master
 self.master.title("Laundry Counter")
 # Increase font size
 self.font = ('Courier', 15)
 # Create a label for the title
 self.title_label = tk.Label(self.master, text="Laundry Counter", font=self.font)
 self.title_label.grid(row=0, column=0, columnspan=3, pady=20)
 # Create a dictionary to store the counts for each type of clothes
 self.counts = {"Shirts": 0, "T-Shirts": 0, "Lower": 0, "Pants": 0, "Bedsheets":0, "Pillow covers":0,"Other":0}
 # Create labels and buttons for each type of clothes
 for i, (clothes, count) in enumerate(self.counts.items()):
 # Create a label for the clothes type
 tk.Label(self.master, text=clothes, font=self.font).grid(row=i + 1, column=0, pady=10,padx=10)
 # Create a label for the current count
 tk.Label(self.master, text="Count: {}".format(count), font=self.font).grid(row=i + 1, column=1, pady=10)
 # Create a button to increment the count
 tk.Button(self.master, text="Add", command=lambda clothes=clothes: self.increment_count(clothes), 
font=self.font).grid( row=i + 1, column=2, padx=2, pady=10)
 # Create a button to reset the counts
 self.reset_button = tk.Button(self.master, text="Reset counts", command=self.reset_counts, font=self.font)
 self.reset_button.grid(row=len(self.counts) + 1, column=1, pady=20)
 # Create a button to quit the program
 self.label = tk.Label(self.master, text="Total: 0", font=self.font)
 self.label.grid(row=len(self.counts) + 2, column=0, columnspan=3, pady=20)
 self.submit_button = tk.Button(self.master, text="Submit", command=self.total, font=self.font)
 self.submit_button.grid(row=len(self.counts) + 1, column=2, padx=10, pady=20)
 # Increase window size
 def increment_count(self, clothes):
 self.counts[clothes] += 1
 # Update the count label for the corresponding clothes type
 for i, (key, value) in enumerate(self.counts.items()):
 if key == clothes:
 self.master.grid_slaves(row=i + 1, column=1)[0].config(text="Count: {}".format(value))
 def reset_counts(self):
 # Reset the counts for all types of clothes
 for clothes in self.counts:
 self.counts[clothes] = 0
 # Update the count labels for all types of clothes
 for i, (key, value) in enumerate(self.counts.items()):
 self.master.grid_slaves(row=i + 1, column=1)[0].config(text="Count: {}".format(value))
 self.label.configure(text=f"Total: {0}")
 def total(self):
 sum = 0
 for i, (key, value) in enumerate(self.counts.items()):
 sum += value
 self.label.configure(text=f"Total: {sum}")
root = tk.Tk()
app = LaundryCounter(root)
root.mainloop()