coords = []

with open("insulin.xyz") as f:
    lines = f.readlines()[2:]  # XYZ header除去

for i, line in enumerate(lines, start=1):
    parts = line.split()

    atom = parts[0]
    x, y, z = map(float, parts[1:4])

    coords.append((atom, x, y, z))

for idx in [261, 262]:
    atom, x, y, z = coords[idx - 1]
    print(idx, atom, x, y, z)


    