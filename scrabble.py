from multiprocessing.sharedctypes import Value


letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 69, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {
    key: Value 
    for key, value 
    in zip(letters, points)
    }
print(letter_to_points)

letter_to_points[" "] = 0

print(letter_to_points)