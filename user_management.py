from datetime import datetime

class User:
    def __init__(self, name: str, email: str, password: str, birthday: datetime):
        self._created_at = datetime.now()
        self.name = name
        self.email = email
        self.password = password
        self.birthday = birthday

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 4 or not value.isalpha():
            self._name = None
        else:
            self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value:
            self._email = None
        else:
            self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if (
            len(value) < 8
            or not any(char.isupper() for char in value)
            or not any(char.islower() for char in value)
            or not any(char in "~!@#$%^&*()_+" for char in value)
        ):
            self._password = None
        else:
            self._password = value

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        if not isinstance(value, datetime) or value >= datetime.now() or (datetime.now().year - value.year) < 20:
            self._birthday = None
        else:
            self._birthday = value

    @property
    def age(self):
        if self.birthday:
            today = datetime.now()
            age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
            return age
        return None

    @property
    def created_at(self):
        return self._created_at

    def __str__(self):
        if None in [self.name, self.email, self.password, self.birthday]:
            return "User creation failed due to invalid data."
        return f"User(name={self.name}, email={self.email}, age={self.age})"

users = []
users.append(
    User(
        name="eliya",
        email="eliyaelbaz050@gmail.com",
        password="Eliyaelbaz050!",
        birthday=datetime(1999, 11, 11)
    )
)

users.append(
    User(
        name="Aviya",
        email="Aviyaelbaz2@gmail.com",
        password="Aviyaelbaz2!",
        birthday=datetime(1994, 12, 6)
    )
)

users.append(
    User(
        name="iris",
        email="iriselbaz@gmail.com",
        password="Iriselbaz3!",
        birthday=datetime(1985, 8, 20)
    )
)

for i, user in enumerate(users, start=1):
    print(f"User {i}: {user}")
