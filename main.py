"""
This script performs a sorting experiment on a list of intergers, `comrades` for fun.
It uses various sorting functions to sort the comrades and writes the results
to the file, Examine_result.txt .
"""
import Sorting_Algo as st
import Time_Analysis as an
import sys, os

def main():
    """It performs a sorting experiment on a list of intergers, `comrades` for fun.
    """
    # Basic setup
    numComrades: int = 20    # Modify this value to change the number of comrades to be sorted
    sorting_functions: dict = {
        st.stalin_sort: {},
        st.tim_sort: {},
        st.recursive_stalin_sort: {},
        st.bubble_sort: {},
        st.insertion_sort: {},
        st.merge_sort: {},
        st.quick_sort: {"low": 0, "high": numComrades-1}
    }
    Comrades: list[int] = an.Examine_Comrades(numComrades)
    comrades_arr: list[list] = [Comrades.copy() for _ in range(len(sorting_functions))]

    # Output the time taken to sort the comrades using each sorting function
    for i, (func, args) in enumerate(sorting_functions.items()):
        try:
            func(comrades_arr[i], **args)
        except Exception as e:
            print(f"An error occurred while trying to sort the comrades: {e}")
    
    # Write the results to the file
    script_dir: str = os.path.abspath(os.path.split(sys.argv[0])[0])  # Get the directory of the current script
    output_dir: str = os.path.join(script_dir, 'output')  # Create the path for the output directory
    try:
        os.makedirs(output_dir, exist_ok=True)
        print("Directory '%s' created successfully" % output_dir)
    except OSError as e:
        print("Directory '%s' can not be created")
        print(f"Error: {e}")
    result_file_path: str = os.path.join(output_dir, "Examine_result.txt")  # Create the path for the result file
    try:
        with open(result_file_path, "w") as f:
            for i, (func, _) in enumerate(sorting_functions.items()):
                f.write(f"Sorting algorithm: {func.__name__}\n")
                f.write(f"Sorted comrades: {comrades_arr[i]}\n")
                f.write("\n")
    except IOError as e:
        print("An error occurred while trying to write to the file.")
        print(f"Error: {e}")

# Driver code
if __name__ == "__main__":
    main()