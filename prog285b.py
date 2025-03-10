from cl285b import Salesperson


def main():
    try:
        print("Number\tCode\tSales\tCommission")
        with open("Langdat/prog285b.dat", 'r') as f:
            for line in f:
                data = line.split(" ")
                id = int(data[0])
                code = int(data[1])
                sales = float(data[2])

                # Option 2: List Comprehension
                # id, code, sales = [float(x) for x in line.split(" ")]
                # Option 3: Conditional List Comprehension
                # id, code, sales = [float(x) if '.' in x else int(x) for x in line.split(" ")]

                person = Salesperson(id, code, sales)
                person.calc_commission()
                print(str(person))  # print(person)
    except Exception as e:
        print("Error:", e)
    pass


if __name__ == "__main__":
    main()
