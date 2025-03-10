def main():
    # Write Mode
    with open("cool.txt", 'w') as f:
        f.write('cool\n')
        f.write('beans')

    # Append Mode (add without overwriting)
    with open("cool.txt", 'a') as file:
        file.write('\nwowsers')

    # Read Mode
    with open("cool.txt", 'r') as f:
        # print(f.readlines())
        for line in f:
            print(line, end='')
    pass


if __name__ == "__main__":
    main()
