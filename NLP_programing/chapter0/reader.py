class Reader:

    def __init__(self, file_name):
        self.file_name = file_name
        self.data_list = []

    def read_file(self):
        with open(self.file_name, 'rb') as f:
            for line in f:
                self.data_list.append(line)
