# def greet():
#     print("1,2,3,3")
#     greet()
# greet()
# printing using recursion




cout = 0

def count():
    global cout  # Fix: use the global variable

    if cout == 4:
        return

    print(cout)
    cout += 1
    count()

count()