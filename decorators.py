def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("The functin ran has completed!")
    return wrapper

@announce
def hey():
    print("Hey Young World")

hey()
