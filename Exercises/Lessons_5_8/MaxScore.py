scores = [65, 85, 72, 22, 33, 94, 95, 13, 61, 80]
heighest_score = 0
for score in range(0, len(scores)):
    if heighest_score < scores[score]:
        heighest_score = scores[score]
print(f"The Heighest score is: {heighest_score}")