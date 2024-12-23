import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import reddit_stories

def generate_video():
    output_file = output_entry.get()
    if not output_file:
        messagebox.showerror("Error", "Please enter an output file name.")
        return
    try:
        reddit_stories.main(output_file)
        messagebox.showinfo("Success", f"Video generated successfully: {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("Story Video Generator")

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

output_label = ttk.Label(main_frame, text="Output File Name:")
output_label.grid(row=0, column=0, sticky=tk.W, pady=5)

output_entry = ttk.Entry(main_frame, width=30)
output_entry.grid(row=0, column=1, sticky=tk.E, pady=5)

generate_button = ttk.Button(main_frame, text="Generate Video", command=generate_video)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()