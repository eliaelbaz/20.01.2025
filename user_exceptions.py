class UserNameTooShortError(Exception):
    """Error for usernames shorter than 3 characters."""
    def __init__(self):
        super().__init__("Error: Username must be at least 3 characters long.")

class UserNameNonCharError(Exception):
    """Error for usernames containing non-alphabetic characters."""
    def __init__(self):
        super().__init__("Error: Username must contain only letters.")

class IllegalEmailFormatError(Exception):
    """Error for invalid email format (missing '@' or '.')."""
    def __init__(self):
        super().__init__("Error: Email must contain '@' and '.'.")

class IllegalPasswordFormatError(Exception):
    """Error for passwords that do not meet security criteria."""
    def __init__(self):
        super().__init__("Error: Password must be at least 8 characters long, contain at least one uppercase letter, one digit, and one special character.")

class UserTooYoungError(Exception):
    """Error for users younger than 20 years old."""
    def __init__(self):
        super().__init__("Error: User must be at least 20 years old.")

class IllegalBirthdayError(Exception):
    """Error for invalid birth date format or future dates."""
    def __init__(self):
        super().__init__("Error: Invalid birth date format. Use YYYY-MM-DD.")