def announce(f):
    def wrapper():

        print("  ")
        print("About to run the function...")

        f()
        print("The functin ran has completed!")
        print("  ")
    return wrapper

@announce
def hey():
    print("Hey Young World!!! ")

hey()
 