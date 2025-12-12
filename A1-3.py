## Sorting Algotithms ##
#1. Quick Sort
def quicksort(arr):
    if len(arr) <=1:
        return arr
    else:
        # pivot=arr[0]  # choose the first element as pivot
        # pivot = random.choice(arr) # ramdom pivot
        pivot= sorted([arr[0], arr[len(arr)//2], arr[-1]])[1] #median of three (middle number of first/last/middle index number)
        left= [x for x in arr if x<pivot] #elements smaller than pivot
        middle= [x for x in arr if x==pivot] #elements equal to pivot
        right= [x for x in arr if x>pivot] #elements larger than pivot

        return quicksort(left) + middle + quicksort(right) #recursive sort and combine

# 2. Merge Sort
def mergesort(arr):
    if len(arr) <=1:
        return arr
    mid=len(arr)//2 
    left_half=mergesort(arr[:mid]) #divide - recursive by calling same function within a function on each side, divide until individual elements
    right_half=mergesort(arr[mid:])
    return merge(left_half, right_half) #conquer

def merge(left, right):
    merged=[]
    i=j=0
    while i<len(left) and j<len(right):  #merge while comparing elements
        if left[i]<=right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:]) #append remaining elements if one side has more elements compared to another, the remaining elements in left/right list will already be sorted
    merged.extend(right[j:])
    return merged

# 3. Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # define the element to insert
        j = i - 1
        while j >= 0 and arr[j] > key: # shift elements that are greater than key to the right
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # insert key at correct position
    return arr
     
# 4. Selection Sort
def selection_sort(arr):
    for i in range (len(arr)):
        min_index=i #set current elements as minimum first
        for j in range(i+1, len(arr)): #find the smallest in remianining unsorted array
            if arr[j] < arr[min_index]:
                min_index=j #update new minimum
        arr[i], arr[min_index] = arr[min_index], arr[i]  #swap the min with original min in unsorted array, swap only after all j is review and find the min
    return arr

# Sorting algorithms
sort_algorithms = [
    (quicksort, "Quick Sort"),
    (mergesort, "Merge Sort"),
    (insertion_sort, "Insertion Sort"),
    (selection_sort, "Selection Sort")  ]

# measure the execution time
import time

def measure_execution_time(function, *argument):  ## *argument = positional argument(list) to pass the function 
    start_time=time.time()
    result=function(*argument)
    end_time=time.time()
    exec_time=end_time-start_time
    return result, exec_time

# dict to store execeution result for each list type {list name: {sort type: [execution time for each list size]}}
execution_results={}

## list size ##
list_size= (1000, 5000, 10000, 20000, 30000, 40000, 50000, 100000)

## list type##
import random

for size in list_size:
    random.seed(1)  # Set a seed for reproducibility for consistency for sort function comparison 

        # 1. random lists
    randomlist = [random.randint(1, size) for _ in range(size)]
        
        # 2. reverse sorted list
    randomlist_inverted = [random.randint(1, size) for _ in range(size)]
    randomlist_inverted.sort(reverse=True)

        # 3. list with extreme value distributions (eg mostly small values with a few large outliers)
    small_value=[random.randint(1, size) for _ in range(int(size*0.9))]
    outliers=[random.randint(size*2, size*5) for _ in range(int(size*0.1))]
    extremelist=small_value+outliers
    random.shuffle(extremelist)

        # 4. list with many duplicate values
    normal=[random.randint(1, size) for _ in range(int(size*0.7))]
    choices = [i*10 for i in range(size//10)]
    duplicate=[random.choice(choices) for _ in range(int(size*0.3))]
    duplicatelist=normal+duplicate
    random.shuffle(duplicatelist)

    # List Tyepes (4)
    list_types = [
        (randomlist, "Random List"),
        (randomlist_inverted, "Reverse Sorted List"),
        (extremelist, "Extreme List"),
        (duplicatelist, "Duplicate List")  ]

    ## call function for all 16 combinations and update execution_result (dict)##
    for input_list, list_name in list_types:
        if list_name not in execution_results:
            execution_results[list_name]={sort_name:[] for _, sort_name in sort_algorithms}
        for sort_function, sort_name in sort_algorithms:
            sorted_result, execution_time=measure_execution_time(sort_function, input_list[:])
            execution_results[list_name][sort_name].append(execution_time)


for list_name, sort_name in execution_results.items():
    print(list_name)
    for sort_name, execution_time in execution_results[list_name].items():
        print(f"  {sort_name}: {execution_time}")
    print()


#plot the result in line graph (matplotlib)
import matplotlib.pyplot as plt
# import numpy as np

list_names = ["Random List", "Reverse Sorted List", "Extreme List", "Duplicate List"]

for list_name in list_names:
    # Execution times for each algorithm (Y-axis)
    quick_sort_times     = execution_results[list_name]["Quick Sort"]
    merge_sort_times     = execution_results[list_name]["Merge Sort"]
    insertion_sort_times = execution_results[list_name]["Insertion Sort"]
    selection_sort_times = execution_results[list_name]["Selection Sort"]

    # table size, plotting with marker
    plt.figure(figsize=(10, 6))
    plt.plot(list_size, quick_sort_times,     marker='o', label='Quick Sort')
    plt.plot(list_size, merge_sort_times,     marker='o', label='Merge Sort')
    plt.plot(list_size, insertion_sort_times, marker='o', label='Insertion Sort')
    plt.plot(list_size, selection_sort_times, marker='o', label='Selection Sort')
    plt.yscale('log') # Logarithmic scale for Y-axis

    # Labels, title, and grid
    plt.xlabel("List Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title(f"Sorting Performance: {list_name}")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)

    # Show the plot
    plt.tight_layout()
    plt.show(block=False)

input("All graphs are open — press Enter to close them when you're done.")






























# ## Sorting Algotithms ##
# #1. Quick Sort
# def quicksort(arr):
#     if len(arr) <=1:
#         return arr
#     else:
#         # pivot=arr[0]  # choose the first element as pivot
#         # pivot = random.choice(arr) # ramdom pivot
#         pivot= sorted([arr[0], arr[len(arr)//2], arr[-1]])[1] #median of three (middle number of first/last/middle index number)
#         left= [x for x in arr if x<pivot] #elements smaller than pivot
#         middle= [x for x in arr if x==pivot] #elements equal to pivot
#         right= [x for x in arr if x>pivot] #elements larger than pivot

#         return quicksort(left) + middle + quicksort(right) #recursive sort and combine

# # 2. Merge Sort
# def mergesort(arr):
#     if len(arr) <=1:
#         return arr
#     mid=len(arr)//2 
#     left_half=mergesort(arr[:mid]) #divide - recursive by calling same function within a function on each side, divide until individual elements
#     right_half=mergesort(arr[mid:])
#     return merge(left_half, right_half) #conquer

# def merge(left, right):
#     merged=[]
#     i=j=0
#     while i<len(left) and j<len(right):  #merge while comparing elements
#         if left[i]<=right[j]:
#             merged.append(left[i])
#             i += 1
#         else:
#             merged.append(right[j])
#             j += 1
#     merged.extend(left[i:]) #append remaining elements if one side has more elements compared to another, the remaining elements in left/right list will already be sorted
#     merged.extend(right[j:])
#     return merged

# # 3. Insertion Sort
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]  # define the element to insert
#         j = i - 1
#         while j >= 0 and arr[j] > key: # shift elements that are greater than key to the right
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key  # insert key at correct position
#     return arr
     
# # 4. Selection Sort
# def selection_sort(arr):
#     for i in range (len(arr)):
#         min_index=i #set current elements as minimum first
#         for j in range(i+1, len(arr)): #find the smallest in remianining unsorted array
#             if arr[j] < arr[min_index]:
#                 min_index=j #update new minimum
#         arr[i], arr[min_index] = arr[min_index], arr[i]  #swap the min with original min in unsorted array, swap only after all j is review and find the min
#     return arr

# # Sorting algorithms
# sort_algorithms = [
#     (quicksort, "Quick Sort"),
#     (mergesort, "Merge Sort"),
#     (insertion_sort, "Insertion Sort"),
#     (selection_sort, "Selection Sort")  ]

# # measure the execution time
# import time

# def measure_execution_time(function, *argument):  ## *argument = positional argument(list) to pass the function 
#     start_time=time.time()
#     result=function(*argument)
#     end_time=time.time()
#     exec_time=end_time-start_time
#     return result, exec_time

# # dict to store execeution result for each list type {list name: {sort type: [execution time for each list size]}}
# execution_results={}

# ## list size ##
# list_size= (1000, 5000, 10000)
# # list_size= (1000, 5000, 10000, 20000, 30000, 40000, 50000, 100000)

# ## list type##
# import random

# for size in list_size:
#     random.seed(1)  # Set a seed for reproducibility for consistency for sort function comparison 

#         # 1. random lists
#     randomlist = [random.randint(1, size) for _ in range(size)]
        
#         # 2. reverse sorted list
#     randomlist_inverted = [random.randint(1, size) for _ in range(size)]
#     randomlist_inverted.sort(reverse=True)

#         # 3. list with extreme value distributions (eg mostly small values with a few large outliers)
#     small_value=[random.randint(1, size) for _ in range(int(size*0.9))]
#     outliers=[random.randint(size*2, size*5) for _ in range(int(size*0.1))]
#     extremelist=small_value+outliers
#     random.shuffle(extremelist)

#         # 4. list with many duplicate values
#     normal=[random.randint(1, size) for _ in range(int(size*0.7))]
#     choices = [i*10 for i in range(size//10)]
#     duplicate=[random.choice(choices) for _ in range(int(size*0.3))]
#     duplicatelist=normal+duplicate
#     random.shuffle(duplicatelist)

#     # List Tyepes (4)
#     list_types = [
#         (randomlist, "Random List"),
#         (randomlist_inverted, "Reverse Sorted List"),
#         (extremelist, "Extreme List"),
#         (duplicatelist, "Duplicate List")  ]


#     # ## call function for all 16 combinations##
#     # print(f"===List Size: {size}===")
#     # for input_list, list_name in list_types:
#     #     for sort_function, sort_name in sort_algorithms:
#     #         sorted_result, execution_time=measure_execution_time(sort_function, input_list[:])
#     #         print(f"{sort_name}, {list_name}", sorted_result[:30], "...") #show only first 10 output as sample in console as result
#     #         print(f"   Execution Time: {execution_time:.6f} seconds")

#     # ## call function for all 16 combinations##
#     # print(f"===List Size: {size}===")
#     # for input_list, list_name in list_types:
#     #     if list_name not in execution_results:
#     #         execution_results[list_name]={sort_name:[] for _, sort_name in sort_algorithms}
#     #     for sort_function, sort_name in sort_algorithms:
#     #         sorted_result, execution_time=measure_execution_time(sort_function, input_list[:])
#     #         execution_results[list_name][sort_name].append(execution_time)
#     #         print(f"{sort_name}, {list_name} - Time: {execution_time:.6f} seconds") 

#     ## call function for all 16 combinations##
#     for input_list, list_name in list_types:
#         if list_name not in execution_results:
#             execution_results[list_name]={sort_name:[] for _, sort_name in sort_algorithms}
#         for sort_function, sort_name in sort_algorithms:
#             sorted_result, execution_time=measure_execution_time(sort_function, input_list[:])
#             execution_results[list_name][sort_name].append(execution_time)


# for list_name, sort_name in execution_results.items():
#     print(list_name)
#     for sort_name, execution_time in execution_results[list_name].items():
#         print(f"  {sort_name}: {execution_time}")
#     print()


# #plot the result in line graph (matplotlib)
# import matplotlib.pyplot as plt
# import numpy as np

# list_names = ["Random List", "Reverse Sorted List", "Extreme List", "Duplicate List"]

# for list_name in list_names:
#     # Execution times for each algorithm (Y-axis)
#     quick_sort_times     = execution_results[list_name]["Quick Sort"]
#     merge_sort_times     = execution_results[list_name]["Merge Sort"]
#     insertion_sort_times = execution_results[list_name]["Insertion Sort"]
#     selection_sort_times = execution_results[list_name]["Selection Sort"]

#     # Plotting
#     plt.figure(figsize=(10, 6))

#     plt.plot(list_size, quick_sort_times,     marker='o', label='Quick Sort')
#     plt.plot(list_size, merge_sort_times,     marker='o', label='Merge Sort')
#     plt.plot(list_size, insertion_sort_times, marker='o', label='Insertion Sort')
#     plt.plot(list_size, selection_sort_times, marker='o', label='Selection Sort')

#     # Logarithmic scale for Y-axis
#     plt.yscale('log')

#     # Labels and title
#     plt.xlabel("List Size")
#     plt.ylabel("Execution Time (seconds)")
#     plt.title(f"Sorting Performance: {list_name}")
#     plt.legend()

#     # Grid for better readability
#     plt.grid(True, which="both", linestyle="--", linewidth=0.5)

#     # Show the plot
#     plt.tight_layout()
#     plt.show(block=False)

# input("All graphs are open — press Enter to close them when you're done.")



# ## 16 combinations
# sort_type, list_type, list_name = quicksort, randomlist, "quicksort"
# sort_type, list_type, list_name = mergesort, randomlist, "mergesort"
# sort_type, list_type, list_name = insertion_sort, randomlist, "insertion_sort"
# sort_type, list_type, list_name = selection_sort, randomlist, "selection_sort"

# sort_type, list_type, list_name = quicksort, randomlist_inverted, "quicksort"
# sort_type, list_type, list_name = mergesort, randomlist_inverted, "mergesort"
# sort_type, list_type, list_name = insertion_sort, randomlist_inverted, "insertion_sort"
# sort_type, list_type, list_name = selection_sort, randomlist_inverted, "selection_sort"

# sort_type, list_type, list_name = quicksort, extremelist, "quicksort"
# sort_type, list_type, list_name = mergesort, extremelist, "mergesort"
# sort_type, list_type, list_name = insertion_sort, extremelist, "insertion_sort"
# sort_type, list_type, list_name = selection_sort, extremelist, "selection_sort"

# sort_type, list_type, list_name = quicksort, duplicatelist, "quicksort"
# sort_type, list_type, list_name = mergesort, duplicatelist, "mergesort"
# sort_type, list_type, list_name = insertion_sort, duplicatelist, "insertion_sort"
# sort_type, list_type, list_name = selection_sort, duplicatelist, "selection_sort"





# ## Sorting Algotithms ##
# #1. Quick Sort
# def quicksort(arr):
#     if len(arr) <=1:
#         return arr
#     else:
#         # pivot=arr[0]  # choose the first element as pivot
#         # pivot = random.choice(arr) # ramdom pivot
#         pivot= sorted([arr[0], arr[len(arr)//2], arr[-1]])[1] #median of three (middle number of first/last/middle index number)
#         left= [x for x in arr if x<pivot] #elements smaller than pivot
#         middle= [x for x in arr if x==pivot] #elements equal to pivot
#         right= [x for x in arr if x>pivot] #elements larger than pivot

#         return quicksort(left) + [pivot] + quicksort(right) #recursive sort and combine

# # 2. Merge Sort
# def mergesort(arr):
#     if len(arr) <=1:
#         return arr
#     mid=len(arr)//2 
#     #divide - recursive by calling same function within a function, divide until individual elements
#     left_half=mergesort(arr[:mid])
#     right_half=mergesort(arr[mid:])
#     #conquer
#     return merge(left_half, right_half) 

# def merge(left, right):
#     merged=[]
#     i=j=0
#     #merge while comparing elements
#     while i<len(left) and j<len(right):
#         if left[i]<=right[j]:
#             merged.append(left[i])
#             i += 1
#         else:
#             merged.append(right[j])
#             j += 1
#     #append remaining elements if one side has more elements compared to another, the remaining elements in left/right list will already be sorted
#     merged.extend(left[i:])
#     merged.extend(right[j:])
#     return merged

# # 3. Insertion Sort
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]  # define the element to insert
#         j = i - 1
#         # shift elements that are greater than key to the right
#         while j >= 0 and arr[j] > key: 
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key  # insert key at correct position
#     return arr
     
# # 4. Selection Sort
# def selection_sort(arr):
#     for i in range (len(arr)):
#         min_index=i #set current elements as minimum first
#         #find the smallest in remianining unsorted array
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index=j #update new minimum
#         #swap the min with original min in unsorted array, swap only after all j is review and find the min
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr


# # measure the execution time
# import time

# def measure_execution_time(function, *argument):
#     """
#     measure the execution time of function 
#     *argument = positional argument(list) to pass the function 
#     return result of funciton & execution time in seconds(float)
#     """
#     start_time=time.time()
#     result=function(*argument)
#     end_time=time.time()
#     execution_time=end_time-start_time
#     return result, execution_time

# ## run the test samples ##
# import random

# # Set a seed for reproducibility for consistency for sort function comparison 
# random.seed(4)

# ## list size ##
# list_size= (1000, 5000, 10000, 20000, 30000, 40000, 50000, 100000)

# for size in list_size:
#     # 1. random lists
#     randomlist = [random.randint(1, size) for _ in range(size)]
    
#     # 2. reverse sorted list
#     randomlist_inverted = [random.randint(1, size) for _ in range(size)]
#     randomlist_inverted.sort(reverse=True)

#     # 3. list with extreme value distributions (eg mostly small values with a few large outliers)
#     small_value=[random.randint(1, size) for _ in range(int(size*0.9))]
#     outliers=[random.randint((size*2), (size*5)) for _ in range(int(size*0.1))]
#     extremelist=small_value+outliers
#     random.shuffle(extremelist)

#     # 4. list with many duplicate values
#     choices = [size * i for i in range(0, size, 5)]
#     duplicatelist = [random.choice(choices) for _ in range(size)]

#     ## call function ##
#     sort_type, list_type, list_name = mergesort, extremelist, "quicksort" # update those element to run function for different combination of test samples
#     sort, exec_time=measure_execution_time(sort_type, list_type)
#     print("List size", size)
#     print(f"{sort_type.__name__} Result - {list_name}", sort[:10], "...") #only show sample in console as result
#     print(f"Execution Time: {exec_time:.6f} seconds")

# #run the function by updateing line 108 "sort_type, list_type, list_name"



# ## list for small-size testing ##
# listsample=[10, 3, 2, 4, 2, 4, 5, 8, 7]