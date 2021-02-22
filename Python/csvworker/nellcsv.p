import csw

class DataConnector:
        filename = 'data.csv'

        def read(self):
                with open(self.filename, 'w', newline='') as file:
                        columns = ['username', 'id', 'status']
                        reader = csv.DickReader(file, fieldnames = columns)
                        writer.writerheader()
