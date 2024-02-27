import os
import nbformat
import re

pattern = r'#\s*SOLUTIONSTART.*?#\s*SOLUTIONEND'

def remove_code_between_keywords(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all ipython notebooks in the input folder
    notebook_files = [file for file in os.listdir(input_folder) if file.endswith(".ipynb")]

    # Iterate through each notebook file
    for notebook_file in notebook_files:
        input_path = os.path.join(input_folder, notebook_file)
        print(f"parsing {input_path}")
        output_path = os.path.join(output_folder, notebook_file)

        # Read the notebook
        with open(input_path, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)

        # Iterate through each cell in the notebook
        for cell in notebook['cells']:
            if (cell['cell_type'] == 'code') or (cell['cell_type'] == 'markdown'):
                # Find and remove code between the specified keywords
                code = cell['source']
                code = re.sub(pattern, '', code, flags=re.DOTALL)

                # Update the cell's source code
                cell['source'] = code

        # Save the modified notebook to the output folder
        with open(output_path, 'w', encoding='utf-8') as f:
            nbformat.write(notebook, f)

        print(f"wrote {output_path}")

if __name__ == "__main__":
    input_folder = "solutions"
    output_folder = "exercises"
    remove_code_between_keywords(input_folder, output_folder)
