import Users


class Client(Users.Users):
    def __init__(self, id, full_name, age, id_no, phone_number):
        super().__init__(id, full_name, age, id_no)
        self.phone_number = phone_number
