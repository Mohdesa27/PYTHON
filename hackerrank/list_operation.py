if __name__ == '__main__':
    # Initialize the list
    lst = []
    
    # Read the number of commands
    N = int(input())
    
    # Iterate through each command
    for _ in range(N):
        # Read the command and split into parts
        command = input().split()
        cmd = command[0]
        
        # Execute the corresponding command
        if cmd == 'insert':
            lst.insert(int(command[1]), int(command[2]))
        elif cmd == 'print':
            print(lst)
        elif cmd == 'remove':
            lst.remove(int(command[1]))
        elif cmd == 'append':
            lst.append(int(command[1]))
        elif cmd == 'sort':
            lst.sort()
        elif cmd == 'pop':
            lst.pop()
        elif cmd == 'reverse':
            lst.reverse()
