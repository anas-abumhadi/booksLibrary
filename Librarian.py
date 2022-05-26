import Users


class Librarian(Users.Users):
    def __init__(self, id, full_name, age, id_no, emplyment_type):
        super().__init__(id, full_name, age, id_no)
        self.emplyment_type = emplyment_type
