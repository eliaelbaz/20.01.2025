from user import User

def test_user_creation():
    try:
        print("\nCreating valid user...")
        user1 = User(name="Alice", email="alice@example.com", password="Secure@123", birthday="1995-06-15")
        print("User created successfully:", user1)
    except Exception as e:
        print("Error:", e)

    try:
        print("\nCreating user with short name...")
        print("Expecting error due to short name...")
        user2 = User(name="Al", email="bob@example.com", password="Secure@123", birthday="1990-05-20")
        print("User created successfully:", user2)
    except Exception as e:
        print("Error:", e)

    try:
        print("\nCreating underage user...")
        print("Expecting error due to age restriction...")
        user3 = User(name="Charlie", email="charlie@example.com", password="Strong@Pass1", birthday="2010-08-22")
        print("User created successfully:", user3)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    test_user_creation()