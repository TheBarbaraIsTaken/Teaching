import json
import subprocess
import sys

PROGRAM_PATH = "program.py"
OUTPUT_PATH = "test_result.json"
INPUT_DATA = [
    "1\n2",
    "2\n3",
]

if __name__ == "__main__":
    python_command = "python3"
    
    if sys.platform.startswith('win'):
        python_command = "python"

    try:
        program_results = []

        for input_data in INPUT_DATA:

            # Launch the Python program and capture output
            result = subprocess.run([python_command, PROGRAM_PATH], input=input_data, capture_output=True, text=True, check=True)

            # Store the print results of the program in a list
            outputs = result.stdout

            program_results.append(outputs)

        # TODO: write inputs and program_results to json file
        # TODO: do something to have more exercises: print a special character?
        print(program_results)
    except subprocess.CalledProcessError as e:
        print("Error:", e)
    