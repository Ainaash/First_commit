def greet_users(names):

    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['Ainash', 'Saliha', 'Sofia']
greet_users(usernames)
