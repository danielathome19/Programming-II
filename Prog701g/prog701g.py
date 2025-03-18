from cl701g import *


def main():
    try:
        people: list[Person] = []
        with open("../Langdat/prog701g.dat", 'r') as f:
            num = int(f.readline())
            while num != 99:
                fn = f.readline()
                ln = f.readline()
                if num == 1:
                    gpa = float(f.readline())
                    p = Student(fn, ln, gpa)
                    people.append(p)
                elif num == 2:
                    num_stu = int(f.readline())
                    p = Teacher(fn, ln, num_stu)
                    people.append(p)
                elif num == 3:
                    fav_word = f.readline().strip()
                    p = Admin(fn, ln, fav_word)
                    people.append(p)
                num = int(f.readline())
            tot = 0.0
            cnt = 0
            tot_stus = 0
            large = ""
            small = "ljksdhfgkjdshgkjdjkhgkjsdkjdvbkjsbviuewbuidsbjkbzlliubwubi"
            for person in people:
                if isinstance(person, Student):
                    tot += person.gpa
                    cnt += 1
                elif isinstance(person, Teacher):
                    tot_stus += person.num_stu
                elif isinstance(person, Admin):
                    fw = person.fav_word
                    if len(fw) > len(large):
                        large = fw
                    if len(fw) < len(small):
                        small = fw
            print("Average student GPA:", round(tot/cnt, 2))
            print("Total number of students taught:", tot_stus)
            print("Smallest favorite admin word:", small)
            print("Largest favorite admin word:", large)
    except OSError as e:
        print("Error:", e)
    pass


if __name__ == "__main__":
    main()
