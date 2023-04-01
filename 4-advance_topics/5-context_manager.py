"""
    Important Notes::
    =>Context Manager is used to manage resources
    =>Context Manager is executed using "with" keyword and following sequence is followed while its execution
    1. __init__()
    2. __enter__()
    3. statement body (code inside the with block)
    4. __exit__()
"""


# Context Manager
class FileManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):  # parameters in this method are used to manage exceptions
        self.file.close()


# Main Function
if __name__ == '__main__':
    # writing to file using Context Manager(FileManager)
    with FileManager('names.txt', 'w') as file:
        file.write('Arslan Haider Sherazi')

    # check whether file is closed by context manager after writing or not
    is_closed = file.closed
    print(is_closed)

