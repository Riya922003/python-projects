command = ""
is_started, is_stopped = False, False

while True:
    command = input(">").lower()
    
    if command == "start":
        if not is_started:
            print("Car started")
            is_started = True
        else:
            print("Car is already started")        

    elif command == "stop":
        if not is_started:
            print("Car is not started yet")
        elif not is_stopped:
            print("Car stopped")
            is_stopped = True
            is_started = False
        else:
            print("Car is already stopped")
    
    elif command == "help":
        print("""start - to start the car
stop - to stop the car
quit - to quit""")
    
    elif command == "quit":
        print("Quit")
        break
    
    else:
        print("I don't understand that")
