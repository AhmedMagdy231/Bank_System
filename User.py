class User:
    def __init__(self, name, age, gender, ID, password):
        self._name = name
        self._age = age
        self._gender = gender
        self._ID = ID
        self._password = password

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getAge(self):
        return self._age

    def setAge(self, age):
        self._age = age

    def getGender(self):
        return self._gender

    def setGender(self, gender):
        self._gender = gender

    def getID(self):
        return self._ID

    def setID(self, ID):
        self._ID = ID

    def getPassword(self):
        return self._password

    def setPassword(self, password):
        self._password = password
