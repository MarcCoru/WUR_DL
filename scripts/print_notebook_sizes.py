import os

def format_size(file_size):
    # Define units and their respective scales
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    scale = 1024

    # Determine the appropriate unit
    unit_index = 0
    while file_size >= scale and unit_index < len(units) - 1:
        file_size /= scale
        unit_index += 1

    return f"{file_size:.2f} {units[unit_index]}"

def print_file_sizes(folder):
    # Get a list of all ipython notebooks in the specified folder
    files = [file for file in os.listdir(folder) if (file.endswith(".ipynb") or file.endswith(".pdf"))]

    for file in files:
        path = os.path.join(folder, file)

        # Get the size of the notebook file
        file_size = os.path.getsize(path)

        print(f"{file}: {format_size(file_size)}")

if __name__ == "__main__":
    print("Exercise Notebooks:")
    print_file_sizes("exercises")

    print("\nSolution Notebooks:")
    print_file_sizes("solutions")

    print("\nCompiled Solution PDF:")
    print_file_sizes("compiled_solutions")