from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from colour import Color
import random
import time
import algorithms

root = Tk()
root.geometry('900x550')
root.title("AlgoViz")
root.config(bg="black")
root.resizable(False, False)

icon = PhotoImage(file="sort.png")
root.iconphoto(False, icon)

# Utility Functions
def check_color(color):
    try:
        Color(color.replace(" ", ""))
        # if everything goes fine then return True
        return True
    except ValueError:  # The color code was not found
        return False

# Variables
selected_algo = StringVar()
color_var = StringVar()
arr_size = IntVar(value=15)
array = []

# Commands
def generate_array():
    ''' Add Random elements to the array '''
    global array
    try:
        size = arr_size.get()
    except:
        messagebox.showerror("AlgoViz", "Size Not A Valid Number")
    else:
        if size < 15 or size > 25:
            messagebox.showerror("AlgoViz", "Kindly Input Array Size In Range (15 <= Size <= 25)")
        else:
            array = []
            for _ in range(size):
                random_num = random.randint(10, 85)
                if random_num not in array:
                    array.append(random_num)

            if check_color(color_var.get()):
                bar_color = [color_var.get() for _ in range(size)]
                plot_bars(array, bar_color)
            else:
                messagebox.showerror("AlgoViz", "Invalid Color Code/ Name")

def plot_bars(array, colors):
    ''' Plot the Bars '''
    canvas.delete("all")
    CANVAS_WIDTH, CANVAS_HEIGHT = 900, 335
    bar_width = CANVAS_WIDTH / (len(array) + 2)
    offset = 25
    spacing = 15
    # Normalizing the data to get constant bar heights irrespective of the values
    normalized_array = [i / max(array) for i in array]

    for i, value in enumerate(normalized_array):
        # Top Left X-Coordinate of Bar
        tl_x = (i * bar_width) + offset + spacing
        tl_y = CANVAS_HEIGHT - (value * 300)  # Top Left Y-Coordinate of Bar
        br_x = (i + 1) * bar_width + offset  # Bottom Right X-Coordinate of Bar
        br_y = CANVAS_HEIGHT  # Bottom Right Y-Coordinate of Bar

        canvas.create_rectangle(tl_x, tl_y, br_x, br_y, fill=colors[i])
        canvas.create_text(tl_x + 4, tl_y, anchor=SW,
                           text=str(array[i]), font="comicsansms 13", fill="white")
    root.update()

def show_animation():
    ''' Show the sorting animation
    based one the chosen algorithm '''
    global array
    if array:
        if selected_algo.get() == "Bubble Sort":
            start = time.time()
            algorithms.bubble_sort(array, plot_bars, color_var.get())
            time_elapsed = round(time.time() - start, 2)
            plot_bars(array, ["#53c28b" for _ in range(len(array))])
            messagebox.showinfo("AlgoViz",
                                f"Time Elapsed: {time_elapsed} secs.\n"
                                + "Time Complexity: O(n^2)\n"
                                + "Space Complexity: O(1)")

        elif selected_algo.get() == "Selection Sort":
            start = time.time()
            algorithms.selection_sort(array, plot_bars, color_var.get())
            time_elapsed = round(time.time() - start, 2)
            plot_bars(array, ["#53c28b" for _ in range(len(array))])
            messagebox.showinfo("AlgoViz",
                                f"Time Elapsed: {time_elapsed} secs.\n"
                                + "Time Complexity: O(n^2)\n"
                                + "Space Complexity: O(1)")

        elif selected_algo.get() == "Insertion Sort":
            start = time.time()
            algorithms.insertion_sort(array, plot_bars, color_var.get())
            time_elapsed = round(time.time() - start, 2)
            plot_bars(array, ["#53c28b" for _ in range(len(array))])
            messagebox.showinfo("AlgoViz",
                                f"Time Elapsed: {time_elapsed} secs.\n"
                                + "Time Complexity: O(n^2)\n"
                                + "Space Complexity: O(1)")

        elif selected_algo.get() == "Quick Sort":
            start = time.time()
            algorithms.quick_sort(array, 0, len(array) - 1, plot_bars, color_var.get())
            time_elapsed = round(time.time() - start, 2)
            plot_bars(array, ["#53c28b" for _ in range(len(array))])
            messagebox.showinfo("AlgoViz",
                                f"Time Elapsed: {time_elapsed} secs.\n"
                                + "Time Complexity: O(n^2)\n"
                                + "Space Complexity: O(n*logn)")


        elif selected_algo.get() == "Merge Sort":
            start = time.time()
            algorithms.merge_sort(array, plot_bars, color_var.get())
            time_elapsed = round(time.time() - start, 2)
            plot_bars(array, ["#53c28b" for _ in range(len(array))])
            messagebox.showinfo("AlgoViz",
                                f"Time Elapsed: {time_elapsed} secs.\n"
                                + "Time Complexity: O(n*logn)\n"
                                + "Space Complexity: O(n)")

        elif selected_algo.get() == "Linear Search":
            start = time.time()
            target = random.choice(array)
            idx = algorithms.linear_search(array, plot_bars, color_var.get(), target)
            time_elapsed = round(time.time() - start, 2)
            messagebox.showinfo("AlgoViz",
                                f"Time Elapsed: {time_elapsed} secs.\n"
                                + f"Target {target} found at index {idx}\n"
                                + "Time Complexity: O(n)\n"
                                + "Space Complexity: O(1)"
                                )

        elif selected_algo.get() == "Jump Search":
            messagebox.showinfo("AlgoViz", 
                                "Jump Search works on sorted arrays only. "
                                + "The array will be sorted first in order to visualize the algorithm")
            array.sort()
            start = time.time()
            target = random.choice(array[arr_size.get()//2:])
            idx = algorithms.jump_search(array, plot_bars, color_var.get(), target)
            time_elapsed = round(time.time() - start, 2)
            messagebox.showinfo("AlgoViz",
                                f"Time Elapsed: {time_elapsed} secs.\n"
                                + f"Target {target} found at index {idx}\n"
                                + "Time Complexity: O(√n)\n"
                                + "Space Complexity: O(1)"
                                )

        elif selected_algo.get() == "Binary Search":
            messagebox.showinfo("AlgoViz", 
                                "Binary Search works on sorted arrays only. "
                                + "The array will be sorted first in order to visualize the algorithm")
            array.sort()
            start = time.time()
            target = random.choice(array[arr_size.get()//2:])
            idx = algorithms.binary_search(array, plot_bars, color_var.get(), target)
            time_elapsed = round(time.time() - start, 2)
            messagebox.showinfo("AlgoViz",
                                f"Time Elapsed: {time_elapsed} secs.\n"
                                + f"Target {target} found at index {idx}\n"
                                + "Time Complexity: O(log(n))\n"
                                + "Space Complexity: O(1)"
                                )

        else:
            messagebox.showerror("AlgoViz", "No such algorithm available!")
    else:
        messagebox.showerror("AlgoViz", "Your Array is Empty :(")


# Main Interface
canvas = Canvas(root, width=880, height=350, background="#1a211c")
canvas.config(bd=6, relief=SUNKEN)
canvas.grid(row=0, column=0, sticky=W)

frame = Frame(root, background="black", width=880, height=350)
frame.config(bd=6, relief=SUNKEN)
frame.grid(row=1, column=0, sticky=W, pady=15, padx=22)

# Styling the ComboBox
combostyle = ttk.Style()

combostyle.theme_create('combostyle', parent='alt',
                        settings={'TCombobox':
                                  {'configure':
                                   {'selectbackground': '#6082d1',
                                    'fieldbackground': '#2a2b2b',
                                    'background': '#6082d1',
                                    }}}
                        )
combostyle.theme_use('combostyle')

######################### Frame Widgets
# Algorithm Select
sub_frame1 = Frame(frame, width=150, height=100, background="black")

algo_label = Label(sub_frame1, text="Choose Algorithm", font="comicsansms 20 bold",
                   foreground="#6082d1", background="#2a2b2b", bd=3, relief=SUNKEN,
                   padx=3, pady=3)
algo_label.grid(row=0, column=0, sticky=W, padx=5, pady=5)
dropdown = ttk.Combobox(sub_frame1, textvariable=selected_algo,
                        values=["Bubble Sort", "Selection Sort", "Insertion Sort",
                                "Quick Sort", "Merge Sort", "Linear Search", 
                                "Jump Search", "Binary Search"],
                        foreground="#e2e3d8", width=12, font="comicsansms 20",
                        justify=CENTER)
dropdown.set("Bubble Sort")
dropdown.grid(row=0, column=1, padx=5, pady=5, sticky=W)

sub_frame1.grid(row=0, column=0, sticky=W)

# Bar Color
sub_frame2 = Frame(frame, width=150, height=100, background="black")

bar_color = Label(sub_frame2, text="Bar Color", font="comicsansms 20 bold",
                  foreground="#6082d1", background="#2a2b2b", bd=3, relief=SUNKEN,
                  padx=3, pady=3)
bar_color.grid(row=0, column=0, sticky=W, padx=5, pady=5)
color_dropdown = ttk.Combobox(sub_frame2, textvariable=color_var,
                              values=["Yellow", "Sky Blue", "Pink"],
                              foreground="#e2e3d8", width=8, justify=CENTER,
                              font="comicsansms 20", )
color_dropdown.set("White")
color_dropdown.grid(row=0, column=1, padx=7, pady=7, sticky=W)

size_label = Label(sub_frame2, text="Array Size", font="comicsansms 20 bold",
                   foreground="#6082d1", background="#2a2b2b", bd=3, relief=SUNKEN,
                   padx=3, pady=3)
size_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)
size = Entry(sub_frame2, textvariable=arr_size, width=5, font="comicsansms 18",
             background="#2a2b2b", foreground="#e2e3d8", justify=CENTER)
size.config(highlightbackground="#2a2b2b")
size.grid(row=1, column=1, padx=5, pady=5)

sub_frame2.grid(row=0, column=1, padx=15, sticky=E)

# Buttons
sub_frame3 = Frame(frame, width=60, height=50, background="black")

generate_data = Button(sub_frame3, text="Generate Data", command=generate_array,
                       font="comicsansms 17 bold", cursor="hand", padx=5, pady=5,
                       fg="red")
generate_data.config(highlightbackground="#de7f78",
                     highlightthickness=4, relief=SUNKEN)
generate_data.grid(row=0, column=0, padx=10, pady=6)

visualize_btn = Button(sub_frame3, text="VISUALIZE", command=show_animation,
                     font="comicsansms 19 bold", cursor="hand", padx=5,
                     pady=5, fg="seagreen")
visualize_btn.config(highlightbackground="#95de8c", highlightthickness=4)
visualize_btn.grid(row=1, column=0, padx=10, pady=7)

sub_frame3.grid(row=0, column=2, padx=15, sticky=E)

root.mainloop()
