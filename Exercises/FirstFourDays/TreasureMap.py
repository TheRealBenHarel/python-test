line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]

map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot!")
print("Choose the column(letter) and the line (number) to hide the treasure(letter first):\n")
position = input()
print(position[0])
letter = position[0].lower()
abc = ["a", "b", "c"]
abc_index = abc.index(letter)
number_index = (int(position[1])-1)
map[number_index][abc_index] = "X"




print(f"{line1}\n{line2}\n{line3}")