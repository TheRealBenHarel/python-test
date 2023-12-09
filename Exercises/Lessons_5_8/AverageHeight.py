

heights = [177, 178, 152, 163, 192, 180]
hsum = 0
for students in range(0, len(heights)):
    hsum += heights[students]
average_height = round((hsum/(students + 1)))


print(average_height)
