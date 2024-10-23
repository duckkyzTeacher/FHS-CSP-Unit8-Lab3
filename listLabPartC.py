scores = [85, 90, 78, 92, 88]

scores.insert(1,95)
print("Scores after adding a new score:", scores)

scores[2] = 80
print("Scores after updating the second score:", scores)

del scores[5]
print("Scores after deleting the 5th score:", scores)
