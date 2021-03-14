import csv


class UserRegister:
    def __init__(self, firstname, lastname, hid, couchname):
        self.firstname = firstname
        self.lastname = lastname
        self.hid = hid
        self.couchname = couchname

    def writeHeaders(self):
        headers = ['firstname', 'lastname', 'id', 'couchname']
        with open('herbalife.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheaders()

    def add_herba_user(self):
        with open('herbalife.csv', 'a', newline='') as file:
            columns = ['firstname', 'lastname', 'id', 'couchname']
            writer = csv.DictWriter(file, fieldnames=columns)
            user = {"firstname": self.firstname, "lastname": self.lastname, "id": self.hid, 'couchname': self.couchname}
            writer.writerow(user)
            file.close()

    def get_users_rows(self):
        lines = ''
        with open('herbalife.csv', 'r',newline='') as file:
            reader = csv.DictReader(file)
            columns = ['firstname', 'lastname', 'id', 'sponsor']
            for call in columns:
                lines += call + ','
            lines += '\n'
            for row in reader:
                lines += row['firstname'] + ',' + row['lastname'] + ',' + row['id'] + ',' + row['coachname'] + '\n'
            file.close()
        return lines

    def remove(self, user_id):
        lines = list()
        with open('herbalife.csv', 'r',newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if str(user_id) != str(row['id']):
                    dick = {'firstname': row['firstname'], 'lastname': row['lastname'], 'id': row['id'], 'couchname': row['couchname']}
                    lines.append(dick)

        with open(self.filename, 'w', newline='') as file:
            columns = ['firstname', 'lastname', 'id', 'couchname']
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            for row in lines:
                user = {'firstname': row['firstname'], 'lastname': row['lastname'], 'id': row['id'], 'couchname': row['couchname']}
                writer.writerow(user)

    def get_all_ids(self):
        with open(self.filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            userlist = []
            for row in reader:
                userlist.append(row["id"])

            return userlist
