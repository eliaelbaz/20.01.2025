from datetime import datetime
from user_exceptions import *

class User:
    def __init__(self, name: str, email: str, password: str, birthday: str):
        self._created_at = datetime.now()
        self.name = name
        self.email = email
        self.password = password
        self.birthday = birthday

    @property
    def created_at(self):
        return self._created_at

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 3:
            raise UserNameTooShortError()
        if not value.isalpha():
            raise UserNameNonCharError()
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value:
            raise IllegalEmailFormatError()
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if len(value) < 8 or not any(c.isupper() for c in value) or not any(c.isdigit() for c in value) or not any(c in "!@#$%^&*()-" for c in value):
            raise IllegalPasswordFormatError()
        self._password = value

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        try:
            birth_date = datetime.strptime(value, "%Y-%m-%d")
            age = (datetime.now() - birth_date).days // 365
            if age < 20:
                raise UserTooYoungError()
            self._birthday = birth_date
        except ValueError:
            raise IllegalBirthdayError()

    @property
    def age(self):
        return (datetime.now() - self._birthday).days // 365

    def __str__(self):
        return f"User: {self.name}, Email: {self.email}, Age: {self.age}, Created At: {self.created_at}"