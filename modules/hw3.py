def main():
    SAT = "Sat"

    SUN = "Sun"

    day = input("Which day is better for brunch?\n")

    while day != SAT or day != SUN:

        day = input("Sorry, what? Please enter a valid day.\n")

    print("Thank you!")
if __name__ == "__main__":
    main()
