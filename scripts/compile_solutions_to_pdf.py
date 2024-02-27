import os
import nbformat
from nbconvert import PDFExporter
from nbconvert.preprocessors import ExecutePreprocessor

def compile_solutions_to_pdf(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all ipython notebooks in the input folder
    notebook_files = [file for file in os.listdir(input_folder) if file.endswith(".ipynb")]

    # Define the PDF exporter
    exporter = PDFExporter()

    # Define the execution preprocessor
    executor = ExecutePreprocessor(timeout=600, kernel_name='python3')

    for notebook_file in notebook_files:
        input_path = os.path.join(input_folder, notebook_file)
        output_path = os.path.join(output_folder, notebook_file.replace(".ipynb", ".pdf"))

        # Read the notebook
        with open(input_path, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)

        # Execute the notebook
        try:
            executor.preprocess(notebook, {'metadata': {'path': input_folder}})
        except Exception as e:
            print(f"Error executing notebook {notebook_file}: {str(e)}")

        # Export to PDF
        pdf_data, resources = exporter.from_notebook_node(notebook)

        # Save the PDF
        with open(output_path, 'wb') as pdf_file:
            pdf_file.write(pdf_data)

if __name__ == "__main__":
    solutions_folder = "solutions"
    pdf_output_folder = "compiled_solutions"

    compile_solutions_to_pdf(solutions_folder, pdf_output_folder)
