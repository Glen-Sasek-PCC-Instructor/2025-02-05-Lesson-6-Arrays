def main():
    element = []
    atomic_number = []
    melting_point_c = []

    max_melt_index = 0

    it = " "
    while it != "":
        it = input("ELEMENT: ")
        if it == "":
            continue
        element.append(it)
        atomic_number.append(int(input("ATOMIC NUMBER: ")))
        melting_point_c.append(float(input("MELTING POINT C: ")))
        if(melting_point_c[len(melting_point_c)-1]) > melting_point_c[max_melt_index]:
            max_melt_index = len(melting_point_c)-1


    print(element)
    print(atomic_number)
    print(melting_point_c)


    print("GREATEST MELTING POINT")
    print(element[max_melt_index])
    print(atomic_number[max_melt_index])
    print(melting_point_c[max_melt_index])

main()
