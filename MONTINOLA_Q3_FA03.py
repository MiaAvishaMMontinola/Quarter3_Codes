scores = [
   [89,97,83],
   [76,84,89],
   [97,94,92],
   [65,73,78],
   [83,89,94]
]

subjects = ["Math", "Science", "English"]

print("Student", *subjects, sep="\t")
for i in range(len(scores)):
    rows = scores[i]
    total = sum(rows)
    avg = total/len(rows)
    print(f"Student {i+1}", *rows, f"Total: {total}", f"Avg: {avg:.2f}", sep="\t")

Making a 2D array made it easier because we can see the data in clumns and rows making the data easier to read and comprehend.
