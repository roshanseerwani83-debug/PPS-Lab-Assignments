# Phone Number Database Management

n = int(input())
contacts = {}

for _ in range(n):
    command = input().split()
    
    if command[0] == "ADD":
        name = command[1]
        phone = command[2]
        contacts[name] = phone  # Add or update
    
    elif command[0] == "REMOVE":
        name = command[1]
        contacts.pop(name, None)  # Remove if exists, ignore otherwise
    
    elif command[0] == "DISPLAY":
        if not contacts:
            print("No contacts")
        else:
            for name in sorted(contacts):
                print(f"{name}: {contacts[name]}")
