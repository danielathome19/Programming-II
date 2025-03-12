from cl213f import ElectricBill


def main():
    try:
        bills = []
        with open("Langdat/prog213f.dat", 'r') as f:
            for line in f:
                kwh = int(line)
                if kwh != -999:
                    e_bill = ElectricBill(kwh)
                    bills.append(e_bill)
        for bill in bills:
            bill.calc()
            print(bill)  # print(str(bill))
    except OSError as e:
        print("Error:", e)
    pass


if __name__ == "__main__":
    main()
