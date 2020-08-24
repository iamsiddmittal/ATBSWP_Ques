try:
    file_name = input("Enter name/path of the file: ")

    text_file = open(file_name, "r")
    count_tf = len(text_file.read())

    buffered_binary_file = open(file_name, "rb")
    count_bbf = len(buffered_binary_file.read())

    print("\nNum of bytes/characters in the file(excluding newlines and end-of-file): ")
    print(count_tf, "\n")

    print("Num of bytes/characters(exact): ")
    print(count_bbf, "\n")

    count_nl = count_bbf - count_tf
    print(f"Newlines in the file: { count_nl } \n")

except:
    print("Error!")
