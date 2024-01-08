import csv
import random
inventions=[]
f=open("talalmanyok.txt","r",encoding="utf-8")
for sor in f:
    kislista=sor[:-1].split(",")
    inventions.append(kislista)
f.close()


def display_inventions(choice):
    if choice == 1:
        for invention in inventions:
            print(', '.join(invention))
    elif choice == 2:
        file_name = input("Enter the file name: ")
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(inventions)
    elif choice == 3:
        start_year = int(input("Enter the start year: "))
        end_year = int(input("Enter the end year: "))
        filtered_inventions = [invention for invention in inventions if start_year <= int(invention[0]) <= end_year]
        for invention in filtered_inventions:
            print(', '.join(invention))
    elif choice == 4:
        year = random.choice([invention[0] for invention in inventions])
        invention = random.choice([invention for invention in inventions if invention[0] == year])
        print("In which year was the following invention discovered: ", ', '.join(invention[1:]))
        user_input = input("Enter the year: ")
        if user_input == year:
            print("Correct!")
        else:
            print("Incorrect. The correct year is:", year)
def main():
    print("Welcome to the Inventions Program!")
    print("1. Display all inventions")
    print("2. Write all inventions to a file")
    print("3. Display inventions within a specific time period")
    print("4. Take a quiz")
    choice = int(input("Enter the number of your choice: "))
    display_inventions(choice)

if __name__ == "__main__":
    main()
