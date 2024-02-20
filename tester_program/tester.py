import subprocess
import sys
from exercise import Exercise

class Tester:
    def __init__(self):
        self.exercise = Exercise()        

        self.python_command = "python3"
        if sys.platform.startswith('win'):
            self.python_command = "python"
    

    def run_tests(self, program_path):
        try:
            program_results = []

            for i in range(self.exercise.test_num):
                input_data = self.exercise.input_data[i]

                # Launch the Python program and capture output
                result = subprocess.run([self.python_command, program_path], input=input_data, capture_output=True, text=True, check=True)

                # Store the print results of the program in a list
                outputs = result.stdout.splitlines()
                program_results.append(outputs)

            results = self.evaluate_tests(program_results)
            
            return results
        except subprocess.CalledProcessError as e:
            print("Error:", e)
            return []

    def evaluate_tests(self, program_results):
        pass
