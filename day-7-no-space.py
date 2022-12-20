

def answer_part_one():
    with open("day-7-input.txt") as f:
        lines = f.read()
        commands = lines.split('\n')

        ## patterns of commands to look for

        # if something starts with a $, it's a command - anything after it before the
        # next $ is a listing of files/ directories
        directories = {"/root":0}
        current_path = "/root"

        for content in commands:

            if content.startswith('$'):
                #commands are cd /, cd dir, cd .., ls

                command = content
                if command[2:4] == "ls":
                    pass

                # Manage changing the path
                elif command[2:4] == "cd":

                    # go back to home base
                    if command[5:6] == '/':
                        current_path = '/root'

                    # go a level up
                    elif command[5:7] == '..':
                        current_path = current_path[:current_path.rfind('/')]

                    else:
                        # get directory
                        directory = command[5:]
                        # add to path
                        current_path += f'/{directory}'

                        # add to directory size dict
                        directories.update({current_path:0})

            elif content.startswith('dir'):
                pass
            else:
                size = int(content.split(' ')[0])
                directory = current_path
                for subpath in range(current_path.count('/')):
                    directories[directory] += size
                    print(f"Added {size} to {directories[directory]}")
                    directory = directory[:directory.rfind('/')]
                    print(f"Directory is now {directory}")

        total_size = 0
        for directory, size in directories.items():

            if size <= 100000:
                total_size += size

        print(f"total size for under 100k directories is {total_size}")

        # answer was 1517599
        # time to solve was 30:00


def answer_part_two():

    with open("day-7-input.txt") as f:
        lines = f.read()
        commands = lines.split('\n')

        ## patterns of commands to look for

        # if something starts with a $, it's a command - anything after it before the
        # next $ is a listing of files/ directories
        directories = {"/root": 0}
        current_path = "/root"

        for content in commands:

            if content.startswith('$'):
                # commands are cd /, cd dir, cd .., ls

                command = content
                if command[2:4] == "ls":
                    pass

                # Manage changing the path
                elif command[2:4] == "cd":

                    # go back to home base
                    if command[5:6] == '/':
                        current_path = '/root'

                    # go a level up
                    elif command[5:7] == '..':
                        current_path = current_path[:current_path.rfind('/')]

                    else:
                        # get directory
                        directory = command[5:]
                        # add to path
                        current_path += f'/{directory}'

                        # add to directory size dict
                        directories.update({current_path: 0})

            elif content.startswith('dir'):
                pass
            else:
                size = int(content.split(' ')[0])
                directory = current_path
                for subpath in range(current_path.count('/')):
                    directories[directory] += size
                    directory = directory[:directory.rfind('/')]

        space_needed = 30000000
        spare_space = 70000000 - directories['/root']
        difference_needed = space_needed - spare_space

        print(difference_needed)

        ideal_dir_delete_space = -100000000000  # start big, we want a small difference
        ideal_dir_size = 0

        for directory, size in directories.items():

            size_difference = difference_needed - size

            if size_difference > 0: # this means the repo doesn't meet the conditions
                pass
            else:
                if size_difference > ideal_dir_delete_space:
                    ideal_dir_delete_space = size_difference
                    ideal_dir_size = size
                    print(f"difference between {directory} with size {size} and difference needed is {size_difference}. Making this the ideal.")

        print(f"Most ideal dir size is {ideal_dir_size} - we need to get rid of {difference_needed}.")

        # answer was 2481982
        # time to solve was 10:47


