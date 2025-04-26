try:
    file1 = open('script.txt', 'r')
    reading_file = file1.read()
    print(reading_file)
    file1.close()
except FileNotFoundError:
    print("Error: The file 'script.txt' was not found.")

