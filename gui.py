import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import reddit_stories

def generate_video():
    output_file = output_entry.get()
    if not output_file:
        messagebox.showerror("Error", "Please enter an output file name.")
        return
    
    story_choice = story_var.get()
    
    if story_choice == 1:
        try:
            reddit_stories.main(output_file)
            messagebox.showinfo("Success", f"Video generated successfully: {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    elif story_choice == 2:
        custom_prompt = custom_prompt_entry.get()
        if not custom_prompt:
            messagebox.showerror("Error", "Please enter a custom story prompt.")
            return
        try:
            # Modify reddit_stories.py to accept a custom prompt
            reddit_stories.main(output_file, custom_prompt)
            messagebox.showinfo("Success", f"Video generated successfully: {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    elif story_choice == 3:
        user_story = user_story_text.get("1.0", tk.END).strip()
        if not user_story:
            messagebox.showerror("Error", "Please enter your story.")
            return
        try:
            reddit_stories.main(output_file, user_story=user_story)
            messagebox.showinfo("Success", f"Video generated successfully: {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showerror("Error", "Please select a story option.")

root = tk.Tk()
root.title("Story Video Generator")

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

output_label = ttk.Label(main_frame, text="Output File Name:")
output_label.grid(row=0, column=0, sticky=tk.W, pady=5)

output_entry = ttk.Entry(main_frame, width=30)
output_entry.grid(row=0, column=1, sticky=tk.E, pady=5)

story_var = tk.IntVar(value=1)

pregen_radio = ttk.Radiobutton(main_frame, text="Use Pre-generated Story", variable=story_var, value=1)
pregen_radio.grid(row=1, column=0, sticky=tk.W, pady=5)

custom_radio = ttk.Radiobutton(main_frame, text="Create Custom Story", variable=story_var, value=2)
custom_radio.grid(row=2, column=0, sticky=tk.W, pady=5)

custom_prompt_label = ttk.Label(main_frame, text="Custom Story Prompt:")
custom_prompt_label.grid(row=3, column=0, sticky=tk.W, pady=5)

custom_prompt_entry = ttk.Entry(main_frame, width=30)
custom_prompt_entry.grid(row=3, column=1, sticky=tk.E, pady=5)

user_radio = ttk.Radiobutton(main_frame, text="Input Your Own Story", variable=story_var, value=3)
user_radio.grid(row=4, column=0, sticky=tk.W, pady=5)

user_story_label = ttk.Label(main_frame, text="Your Story:")
user_story_label.grid(row=5, column=0, sticky=tk.W, pady=5)

user_story_text = tk.Text(main_frame, width=30, height=5)
user_story_text.grid(row=5, column=1, sticky=tk.E, pady=5)


generate_button = ttk.Button(main_frame, text="Generate Video", command=generate_video)
generate_button.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()

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