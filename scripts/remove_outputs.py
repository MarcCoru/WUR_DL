import os
import nbformat

def remove_outputs(notebook_folder):
    # Get a list of all ipython notebooks in the specified folder
    notebook_files = [file for file in os.listdir(notebook_folder) if file.endswith(".ipynb")]

    for notebook_file in notebook_files:
        notebook_path = os.path.join(notebook_folder, notebook_file)

        # Read the notebook
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)

        # Remove outputs from all cells
        for cell in notebook['cells']:
            if 'outputs' in cell:
                cell['outputs'] = []

        # Save the modified notebook back
        with open(notebook_path, 'w', encoding='utf-8') as f:
            nbformat.write(notebook, f)

if __name__ == "__main__":
    remove_outputs("exercises")
    remove_outputs("solutions")
