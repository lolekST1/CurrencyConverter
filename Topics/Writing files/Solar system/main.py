# create the planets.txt
with open("planets.txt", "w", encoding='utf-8') as f:
    planety = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    for planeta in planety:
        f.writelines(planeta + "\n")
