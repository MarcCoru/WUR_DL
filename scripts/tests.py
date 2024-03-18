import unittest
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

class TestNotebooks(unittest.TestCase):
    def test_notebooks_execution(self):
        solution_folder = "solutions"

        # Get a list of all ipython notebooks in the solutions folder
        notebook_files = [file for file in os.listdir(solution_folder) if file.endswith(".ipynb")]

        # only regularization notebooks (Segmentation Notebook is too heavy)
        notebook_files = [file for file in notebook_files if file.startswith("Regularization")]


        for notebook_file in notebook_files:
            notebook_path = os.path.join(solution_folder, notebook_file)

            with self.subTest(notebook=notebook_file):
                # Read the notebook
                with open(notebook_path, 'r', encoding='utf-8') as f:
                    notebook = nbformat.read(f, as_version=4)

                # Create an execution preprocessor
                executor = ExecutePreprocessor(timeout=600, kernel_name='python3')

                try:
                    # Execute the notebook
                    executor.preprocess(notebook, {'metadata': {'path': solution_folder}})
                except Exception as e:
                    # If an exception occurs, fail the test
                    self.fail(f"Error executing notebook {notebook_file}: {str(e)}")

if __name__ == '__main__':
    unittest.main()
