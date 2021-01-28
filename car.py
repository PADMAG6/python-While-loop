command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "help":
       print("""start- to start d car 
              stop- to stop d car 
               quit- to exit""")
    elif command == "start":
        if started:
            print("car already started")
        else:
            started = True
            print("car started ready to go")
    elif command == "stop":
        if not started:
            print("car already stopped")
        else:
            started = False
            print("car started")
    elif command == "quit":
        break
    else:
       print("I dn't understand")
