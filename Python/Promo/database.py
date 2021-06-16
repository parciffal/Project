import csv
import config


class DataConnector:
    filename = config.FILENAME
    headers = ['message_id','sended_id', 'name', 'promo', 'expire', 'terms', 'limit', 'time', 'code']

    def write_headers(self):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writeheader()

    def add_user(self, name, promo, expire, terms, limit, time, code, message_id):
        with open(self.filename, 'a', newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            user = {'message_id': message_id,
                    'sended_id': ' ',
                    'name': name,
                    'promo': promo,
                    'expire': expire,
                    'terms': terms,
                    'limit': limit,
                    'time': time,
                    'code': code}
            writer.writerow(user)

    def get_all_ids(self):
        with open(self.filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            userlist = []
            for row in reader:
                userlist.append({
                                    'message_id': row['message_id'],
                                    'name': row['name'],
                                    'promo': row['promo'],
                                    'expire': row['expire'],
                                    'terms': row['terms'],
                                    'limit': int(row['limit']),
                                    'time': row['time'],
                                    'code': row['code']
                                })
            file.close()
            return userlist

    def remove(self, message_id):
        lines = []
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if str(message_id) == str(row['id']):
                    continue
                else:
                    demo = {
                                'message_id': row['message_id'],
                                'sended_id': row['sended_if'],
                                'name': row['name'],
                                'promo': row['promo'],
                                'expire': row['expire'],
                                'terms': row['terms'],
                                'limit': row['limit'],
                                'time': row['time'],
                                'code': row['code']
                            }
                    lines.append(demo)

        with open(self.filename, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writeheader()
            for row in lines:
                demo = {
                    'message_id': row['message_id'],
                    'sended_id': row['sended_if'],
                    'name': row['name'],
                    'promo': row['promo'],
                    'expire': row['expire'],
                    'terms': row['terms'],
                    'limit': row['limit'],
                    'time': row['time'],
                    'code': row['code']
                }
                writer.writerow(demo)

    def change_groups(self, user_id, groups):
        lines = []
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if str(user_id) == str(row['id']):
                    dick = {"name": row['name'],
                            "id": row['id'],
                            'groups': groups,
                            'message': row['message'],
                            'time': row['time'],
                            'send': row['send']}
                    lines.append(dick)
                else:
                    dick = {"name": row['name'],
                            "id": row['id'],
                            'groups': row['groups'],
                            'message': row['message'],
                            'time': row['time'],
                            'send': row['send']}
                    lines.append(dick)

        with open(self.filename, 'w') as file:
            columns = ['id', 'name', 'groups', 'message', 'time', 'send']
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            for row in lines:
                user = {"name": row['name'],
                        "id": row['id'],
                        'groups': row['groups'],
                        'message': row['message'],
                        'time': row['time'],
                        'send': row['send']}
                writer.writerow(user)

    def change_message(self, user_id, message):
        lines = []
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if str(user_id) == str(row['id']):
                    dick = {"name": row['name'],
                            "id": row['id'],
                            'groups': row['groups'],
                            'message': message,
                            'time': row['time'],
                            'send': row['send']}
                    lines.append(dick)
                else:
                    dick = {"name": row['name'],
                            "id": row['id'],
                            'groups': row['groups'],
                            'message': row['message'],
                            'time': row['time'],
                            'send': row['send']}
                    lines.append(dick)

        with open(self.filename, 'w') as file:
            columns = ['id', 'name', 'groups', 'message', 'time', 'send']
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            for row in lines:
                user = {"name": row['name'],
                        "id": row['id'],
                        'groups': row['groups'],
                        'message': row['message'],
                        'time': row['time'],
                        'send': row['send']}
                writer.writerow(user)

    def change_time(self, user_id, time):
        lines = []
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if str(user_id) == str(row['id']):
                    dick = {"name": row['name'],
                            "id": row['id'],
                            'groups': row['groups'],
                            'message': row['message'],
                            'time': time,
                            'send': row['send']}
                    lines.append(dick)
                else:
                    dick = {"name": row['name'],
                            "id": row['id'],
                            'groups': row['groups'],
                            'message': row['message'],
                            'time': row['time'],
                            'send': row['send']}
                    lines.append(dick)

        with open(self.filename, 'w') as file:
            columns = ['id', 'name', 'groups', 'message', 'time', 'send']
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            for row in lines:
                user = {"name": row['name'],
                        "id": row['id'],
                        'groups': row['groups'],
                        'message': row['message'],
                        'time': row['time'],
                        'send': row['send']}
                writer.writerow(user)

    def change_s_to_True(self, user_id):
        lines = []
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if str(user_id) == str(row['id']):
                    dick = {"name": row['name'],
                            "id": row['id'],
                            'groups': row['groups'],
                            'message': row['message'],
                            'time': row['time'],
                            'send': True}
                    lines.append(dick)
                else:
                    dick = {"name": row['name'],
                            "id": row['id'],
                            'groups': row['groups'],
                            'message': row['message'],
                            'time': row['time'],
                            'send': row['send']}
                    lines.append(dick)
        with open(self.filename, 'w') as file:
            columns = ['id', 'name', 'groups', 'message', 'time', 'send']
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            for row in lines:
                user = {"name": row['name'],
                        "id": row['id'],
                        'groups': row['groups'],
                        'message': row['message'],
                        'time': row['time'],
                        'send': row['send']}
                writer.writerow(user)


    def change_s_to_False(self, user_id):
        lines = []
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if str(user_id) == str(row['id']):
                    dick = {"name": row['name'],
                            "id": row['id'],
                            'groups': row['groups'],
                            'message': row['message'],
                            'time': row['time'],
                            'send': False}
                    lines.append(dick)
                else:
                    dick = {"name": row['name'],
                            "id": row['id'],
                            'groups': row['groups'],
                            'message': row['message'],
                            'time': row['time'],
                            'send': row['send']}
                    lines.append(dick)
        with open(self.filename, 'w') as file:
            columns = ['id', 'name', 'groups', 'message', 'time', 'send']
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            for row in lines:
                user = {"name": row['name'],
                        "id": row['id'],
                        'groups': row['groups'],
                        'message': row['message'],
                        'time': row['time'],
                        'send': row['send']}
                writer.writerow(user)