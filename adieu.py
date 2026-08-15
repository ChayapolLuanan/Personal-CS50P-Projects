def main():

    names = []

    while True:
        try:
            user_input = input("Name: ")
            names.append(user_input)
        except EOFError:
            break

    print("\n","Adieu, adieu, to ", end="")
    
    if len(names) == 1:
        print(names[0])
    elif len(names) == 2:
        print(names[0],"and",names[1],)

    else:
        iteration = 0

        for name in names:
            if iteration == (len(names) - 1):
                print("and", name)
            else:
                print(name,",", sep = "", end=" ")
                iteration = iteration + 1



main()
