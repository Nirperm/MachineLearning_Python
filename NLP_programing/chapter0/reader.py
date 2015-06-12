class Reader:

    def __init__(self, file_name):
        self.file_name = file_name
        self.filedata_list = []

    def read_file(self):
        with open(self.file_name, encoding='utf-8') as f:
            print(f)
            for line in f:
                self.filedata_list.append(line)
