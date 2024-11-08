def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("The function ran has completed!")

    return wrapper

@announce
def hey():
    print("Hey Young World")
