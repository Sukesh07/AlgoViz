import time

################### Sorting Algorithms ###################
# Bubble Sort
def bubble_sort(array, plot, bar_color):
    size = len(array)

    for i in range(size - 1):
        swapped = False  # This implementation makes the time complexity O(n)
        for j in range(size - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                colors = ["#34eb98" if k == j else "#1e51e8" if k == j +
                          1 else bar_color for k in range(size)]
                plot(array, colors)
                time.sleep(1)
                swapped = True
        if not swapped:
            break

# Selection Sort
def selection_sort(array, plot, bar_color):
    size = len(array)

    for i in range(size):
        min_idx = i
        for j in range(i + 1, size):
            if array[min_idx] > array[j]:
                min_idx = j
            
            colors = ["#34eb98" if k == min_idx else "#1e51e8" if k == j 
                     else bar_color for k in range(size)]
            plot(array, colors)
            time.sleep(1)

        array[i], array[min_idx] = array[min_idx], array[i]
        colors = ["#551bd1" if k == min_idx else "#551bd1" if k == i 
                     else bar_color for k in range(size)]
        plot(array, colors)
        time.sleep(1.5)

# Insertion Sort
def insertion_sort(array, plot, bar_color):
    size = len(array)

    for i in range(1, size):
        curr = array[i]
        j = i - 1

        while j >= 0 and array[j] > curr:
            array[j+1] = array[j]
            j -= 1

            colors = ["#34eb98" if k == j else "#1e51e8" if k == j+1
                     else "orange" if k == i else bar_color for k in range(size)]
            plot(array, colors)
            time.sleep(1)
            
        array[j+1] = curr

# Quick Sort
def partition(array, head, tail, plot, bar_color):
    size = len(array)
    border = head
    pivot = array[tail]

    plot(array, quick_get_colors(size, head,
                                 tail, border, border, bar_color=bar_color))
    time.sleep(1)

    for j in range(head, tail):
        if array[j] < pivot:
            plot(array, quick_get_colors(size, head, tail,
                                         border, j, bar_color=bar_color, is_swap=True))
            time.sleep(1)

            array[border], array[j] = array[j], array[border]
            border += 1

        plot(array, quick_get_colors(size, head,
                                     tail, border, j, bar_color=bar_color))
        time.sleep(1)

    plot(array, quick_get_colors(size, head, tail,
                                 border, tail, bar_color=bar_color, is_swap=True))
    time.sleep(1)

    array[border], array[tail] = array[tail], array[border]
    return border

def quick_sort(array, head, tail, plot, bar_color):
    if head < tail:
        partition_idx = partition(array, head, tail, plot, bar_color=bar_color)

        quick_sort(array, head, partition_idx - 1, plot,
                   bar_color)  # Left Side of Pivot
        quick_sort(array, partition_idx + 1, tail, plot,
                   bar_color)  # Right Side of Pivot

def quick_get_colors(size, head, tail, border, curr_idx, bar_color, is_swap=False):
    colors = []
    for i in range(size):
        if i >= head and i <= tail:
            colors.append(bar_color)
        else:
            colors.append(bar_color)

        if i == tail:
            colors[i] = '#93dbca'
        elif i == border:
            colors[i] = '#286eb5'
        elif i == curr_idx:
            colors[i] = '#d5e68a'

        if is_swap:
            if i == border or i == curr_idx:
                colors[i] = '#fcba03'
    return colors

# Merge Sort
def merge_sort(array, plot, bar_color):
    merge_sort_algo(array, 0, len(array) - 1, plot, bar_color)

def merge_sort_algo(array, left, right, plot, bar_color):
    if left < right:
        middle = (left + right) // 2
        merge_sort_algo(array, left, middle, plot, bar_color)
        merge_sort_algo(array, middle + 1, right, plot, bar_color)
        merge(array, left, middle, right, plot, bar_color)

def merge(array, left, middle, right, plot, bar_color):
    plot(array, merge_get_colors(len(array), left, middle, right, bar_color))
    time.sleep(0.3)

    left_part = array[left:middle + 1]
    right_part = array[middle + 1: right + 1]

    left_idx = right_idx = 0

    for index in range(left, right + 1):
        if left_idx < len(left_part) and right_idx < len(right_part):
            if left_part[left_idx] <= right_part[right_idx]:
                array[index] = left_part[left_idx]
                left_idx += 1
            else:
                array[index] = right_part[right_idx]
                right_idx += 1

        elif left_idx < len(left_part):
            array[index] = left_part[left_idx]
            left_idx += 1
        else:
            array[index] = right_part[right_idx]
            right_idx += 1

    plot(array, ["green" if x >= left and x <= right 
                else bar_color for x in range(len(array))])
    time.sleep(1)

def merge_get_colors(size, left, middle, right, bar_color):
    colors = []

    for i in range(size):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colors.append("#d5e68a")
            else:
                colors.append("#286eb5")
        else:
            colors.append(bar_color)
    return colors

####################### Searching Algorithms ########################
# Linear Search
def linear_search(array, plot, bar_color, to_search):
    to_search_idx = array.index(to_search)
    plot(array, ["#ed1915" if i == to_search_idx else bar_color for i in range(len(array))])
    time.sleep(2.5)

    for ele in array:
        colors = ["#03c6fc" if i == ele else bar_color for i in array]
        plot(array, colors)
        time.sleep(1)

        if ele == to_search:
            colors = ["green" if i == ele else bar_color for i in array]
            plot(array, colors)
            time.sleep(1)
            return to_search_idx

# Jump Search
def jump_search(array, plot, bar_color, to_search):
    size = len(array)
    i, j = 0, int(size**0.5)

    colors = [bar_color] * size
    plot(array, colors) # Plot sorted array
    time.sleep(1.5)

    colors = ["red" if ele == to_search else bar_color for ele in array] 
    plot(array, colors) # Plot Target
    time.sleep(1)

    colors = ["#34eb98" if k == i else "#1e51e8" if k == j 
             else "red" if array[k] == to_search else bar_color 
             for k in range(size)]
    plot(array, colors) # Plot the pointers and begin searching
    time.sleep(1)

    while j < size and array[j] <= to_search:
        i = j
        j += int(size**0.5)
        if i >= size:
            break

        colors = ["#34eb98" if k == i else "#1e51e8" if k == j 
             else bar_color for k in range(size)]
        plot(array, colors)
        time.sleep(1)
    
    for ele in array[i:j+1]:
        colors = ["#34eb98" if k == i else "#1e51e8" if k == j 
                 else "#03c6fc" if array[k] == ele else bar_color 
                 for k in range(size)]
        plot(array, colors)
        time.sleep(1)

        if ele == to_search:
            colors = ["green" if i == ele else bar_color for i in array]
            plot(array, colors)
            time.sleep(0.7)
            return array.index(ele)

# Binary Search
def binary_search(array, plot, bar_color, to_search):
    colors = [bar_color] * len(array)
    plot(array, colors) # Plot sorted array
    time.sleep(1.5)

    colors = ["red" if ele == to_search else bar_color for ele in array] 
    plot(array, colors) # Plot Target
    time.sleep(1)

    size = len(array)
    start, end = 0, size - 1

    colors = ["#34eb98" if k == start else "#1e51e8" if k == end 
             else bar_color for k in range(size)]
    plot(array, colors)
    time.sleep(1)

    while start <= end:
        mid = (start + end) // 2

        colors = ["#34eb98" if k == start else "#1e51e8" if k == end 
                else bar_color for k in range(size)] # Plot start and end
        plot(array, colors)
        time.sleep(1)

        colors = ["#911bd1" if k == mid else bar_color for k in range(size)] # Plot mid (and target if found)
        plot(array, colors)
        time.sleep(1)

        if array[mid] == to_search:
            colors = [bar_color] * size
            colors[mid] = "green"
            plot(array, colors)
            time.sleep(1)
            return mid

        elif array[mid] < to_search:
            start = mid + 1
        else:
            end = mid - 1
    

            
        
        
        