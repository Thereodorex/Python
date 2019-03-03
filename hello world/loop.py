running = 1
while running:
    inp = input("> ")
 #   inp = str(inp)
 #   print(f"{inp}")
    if (inp.lower() == "start"):
        print("Car started...Ready to go")
    elif (inp.lower() == "stop"):
        print("Car stopped.")
    elif (inp.lower() == "quit"):
        running = 0
    else:
        print("I don't understand that...")