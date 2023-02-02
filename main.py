def create_file(file_name):
    file = open(file_name, 'w+')
    for i in range(0, 19):
        file.write(str(i) + "\n")
    file.seek(0, 0)
    return file


def open_file(file_name):
    try:
        file = open(file_name, 'r+')
    except:
        file = create_file(file_name)

    return file


def main():
    file = open_file('numbers.txt')
    sumNumbers = 0

    while True:
        line = file.readline().strip()
        if not line:
            break
        sumNumbers += int(line)

    file.close()
    with open('answer.txt.', 'w') as file:
        file.write(str(sumNumbers))


main()
