accounts = {"ashley": {"password": "cats", "posts": ["yay", "wow"]}}
currentPost = []

def viewPost(currentUser):
    if len(currentPost) == 0:
        print("No posts")
        homepage(currentUser)
    else:
        for i in range(len(currentPost)):
            print(f"{i + 1}. {currentPost[i]}")
    ask = input("Would you like to return to home page?")
    if ask == "yes":
        homepage(currentUser)
    else:
        changePassword(currentUser)


def editPost(currentUser):
    if len(currentPost) == 0:
        print("No posts")
    else:
        for i in range(len(currentPost)):
            print(f"{i + 1}. {currentPost[i]}")
        ask = int(input("Which post would you like to edit? "))
        if 0 <= ask - 1 < len(currentPost):
            edit = input("What would you like to edit it to? ")
            currentPost[ask - 1] = edit
        else:
            print("Invalid Input!")

    ask = input("Would you like to return back to the homepage? ")
    if ask == "yes":
        homepage(currentUser)
    else:
        editPost(currentUser)


def changePassword(currentUser):
    change = input("What would you like to change your password into? ")
    accounts[currentUser] = {"password": change, "posts": []}
    ask = input("Would you like to return to home page?")
    if ask == "yes":
        homepage(currentUser)
    else:
        changePassword(currentUser)


def deletePost(currentUser):
    if len(currentPost) == 0:
        print("No posts")
    else:
        for i in range(len(currentPost)):
            print(f"{i + 1}. {currentPost[i]}")
        ask = int(input("Which post would you like to delete? "))
        if 0 <= ask - 1 < len(currentPost):
            del currentPost[ask - 1]
        else:
            print("Invalid Input!")

    ask = input("Would you like to return back to the homepage? ")
    if ask == "yes":
        homepage(currentUser)
    else:
        deletePost(currentUser)


def addPost(currentUser):
    add = input("What would you like to add? ")
    currentPost.append(add)
    ask = input("Would you like to return back to the homepage? ")
    if ask == "yes":
        homepage(currentUser)
    else:
        addPost(currentUser)


def homepage(currentUser):
    print(f"Hello {currentUser}")
    print(
        """
        CHOOSE AN OPTION
        ----------------
        1. View Post
        2. Edit Post
        3. Delete Post
        4. Add Post
        5. Change Password
        6. Return to Home Screen
        """)
    global currentPost
    currentPost = accounts[currentUser]["posts"]
    choice = input("Choose an option: ")
    if choice == "5":
        changePassword(currentUser)
    elif choice == "1":
        viewPost(currentUser)
    elif choice == "3":
        deletePost(currentUser)
    elif choice == "2":
        editPost(currentUser)
    elif choice == "6":
        homepage(currentUser)
    elif choice == "4":
        addPost(currentUser)
    else:
        print("Invalid Input")


def main():
    username = input("Username: ")
    password = input("Password: ")
    choice = input("Press 1 for login / 2 for signup")
    if choice == "1":
        if (password == accounts[username]["password"]):
            homepage(username)
        elif choice == "2":
            if username not in accounts:
                accounts[username] = {"password": password, "posts": []}
                homepage(username)
            else:
                print("this user exists already!")
                homepage(username)

        else:
            attempts = 3
            while (attempts > 0):
                password = input("Password: ")
                if (password == accounts[username]["password"]):
                    homepage(username)
                else:
                    attempts -= 1
                    print(f"Incorrect password! Try again you have {attempts}")
                if attempts == 0:
                    print("Try again later!")
                    main()


main()
