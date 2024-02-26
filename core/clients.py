class ID:
    __internal_ID = 1
    def __init__(self):
        self.__internal_ID = ID.__internal_ID
        ID.__internal_ID +=1
    def get_total_clients():
        return ID.__internal_ID - 1

class Clients(ID):
    def __init__(self, user, pw, name, surname, age, email, recovery, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.__pw = pw
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.recovery = recovery

