import csv


class UserRegister:
    def __init__(self, name, couchname):
        self.name = name
        self.couchname = couchname

    def writeHeaders(self):
        headers = ['name', 'couchname']
        with open('Costumerdb.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheaders()

    def add_herba_user(self):
        with open('Costumerdb.csv', 'a', newline='') as file:
            columns = ['name', 'couchname']
            writer = csv.DictWriter(file, fieldnames=columns)
            user = {"name": self.name, 'couchname': self.couchname}
            writer.writerow(user)
            file.close()

    def get_users_rows(self):
        lines = ''
        with open('Costumerdb.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            columns = ['name', 'couchname']
            for call in columns:
                lines += call + ','
            lines += '\n'
            for row in reader:
                lines += row['name'] + ',' + row['coachname'] + '\n'
            file.close()
        return lines

    def remove(self, user_id):
        lines = list()
        with open('Costumerdb.csv', 'r',newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if str(user_id) != str(row['id']):
                    dick = {'name': row['name'], 'couchname': row['couchname']}
                    lines.append(dick)

        with open('Costumerdb.csv', 'w', newline='') as file:
            columns = ['name', 'couchname']
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            for row in lines:
                user = {'name': row['name'], 'couchname': row['couchname']}
                writer.writerow(user)

    def get_all_ids(self):
        with open('Costumerdb.csv', "r", newline="") as file:
            reader = csv.DictReader(file)
            userlist = []
            for row in reader:
                userlist.append(row["id"])

            return userlist
