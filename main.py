def greet(name, age=None): # ageパラメータを追加
    message = f"Hello, {name}! Welcome to your first Git project. This is an updated message."
    if age: # ageがあればメッセージに追加
        message += f" You are {age} years old."
    return message

if __name__ == "__main__":
    user_name = input("Please enter your name: ")
    user_age = input("Please enter your age (optional): ") # 年齢入力の追加

    if user_age.isdigit(): # 数字かどうかチェック
        print(greet(user_name, int(user_age)))
    else:
        print(greet(user_name)) # 年齢が入力されなかった場合