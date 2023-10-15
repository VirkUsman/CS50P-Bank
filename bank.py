greeting = input("Greetings :  ")

# print (greeting)

greeting = greeting.strip()
greeting = greeting.lower()

# print (greeting)


if "hello" in greeting:
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")