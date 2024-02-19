TEST_FILE_PATH = "test_result.txt"

class Exercise:
    def __init__(self):
        self.test_path = TEST_FILE_PATH

        with open(self.self.test_path, "r") as f:
            self.test_num = int(f.readline())
            self.tests = [line for line in f.readlines()]
    
    