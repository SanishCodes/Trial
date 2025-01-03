x = input("Enter a number: ")
y = input("Enter Second Numnber: ")

try:
    z = (x) / int(y)
except Exception as e:
    print(type(e).__name__)


