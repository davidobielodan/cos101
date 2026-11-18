# Display summary information for a list of scores.
scores = [70, 85, 60, 90]
print("Scores:", scores)
print("Number of scores:", len(scores))
print("Total:", sum(scores))
print("Highest score:", max(scores))
print("Lowest score:", min(scores))
average = sum(scores) / len(scores)
print(f"Average score: {average:.2f}")