def main():
    try:
        with open("Langdat/prog213f.dat", 'r') as f:
            for line in f:
                ldata = line.split(" ")

    except Exception as e:
        print("Error:", e)
    pass


if __name__ == "__main__":
    main()
