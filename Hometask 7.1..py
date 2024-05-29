def user_info(name: str, age: int, hobby: str) -> None:
    print(f"Welcome, {name}! Your age: {age} and hobby is {hobby}")


name = input("Enter your name: ")
age = int(input("Enter your age: "))
user_hobby = input("Enter your hobby: ")
user_info(name, age, user_hobby)



