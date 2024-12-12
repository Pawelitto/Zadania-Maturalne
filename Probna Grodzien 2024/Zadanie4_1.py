results = []

with open("Dane-2412/prostokaty_przyklad.txt", "r") as file:
    for line in file:
        resolutions = line.rstrip().split(" ")
        res = int(resolutions[0]) * int(resolutions[1])
        results.append(res)

print(min(results))
print(max(results))
