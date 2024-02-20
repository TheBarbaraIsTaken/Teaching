import json

TEST_FILE_PATH = "test_result.json"

class Exercise:
    def __init__(self):
        self.test_path = TEST_FILE_PATH

        with open(self.test_path, "r") as f:
            self.data = json.load(f)

        self.test_num = len(self.data)

        
    