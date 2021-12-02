with open("input.txt", "r") as reader:
    def parser(text):
        operation, distance = text.strip().split()
        return operation, int(distance)
    
    def move(cordinate, operation, distance):
        if operation == "forward":
            cordinate[1] += distance
        if operation == "down":
            cordinate[0] += distance
        if operation == "up":
            cordinate[0] -= distance
    
    def new_move(cordinate, operation, distance):
        if operation == "forward":
            cordinate[1] += distance
            cordinate[0] += cordinate[2] * distance
        if operation == "down":
            cordinate[2] += distance
        if operation == "up":
            cordinate[2] -= distance

    cordinate = [0, 0]
    new_cordinate= [0, 0, 0]
    for line in reader:
        ops, dis = parser(line)
        move(cordinate, ops, dis)
        new_move(new_cordinate, ops, dis)
    print(cordinate, cordinate[0] * cordinate[1])
    print(new_cordinate, new_cordinate[0] * new_cordinate[1])