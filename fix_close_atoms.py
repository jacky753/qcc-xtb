import numpy as np

with open("insulin.xyz") as f:
    lines = f.readlines()

natoms = int(lines[0])

atoms = []
coords = []

for line in lines[2:]:
    parts = line.split()

    atoms.append(parts[0])
    coords.append(np.array(list(map(float, parts[1:4]))))

coords = np.array(coords)

threshold = 0.01  # Å

for i in range(natoms):
    for j in range(i + 1, natoms):

        dist = np.linalg.norm(coords[i] - coords[j])

        if dist < threshold:
            print(f"Too close: {i+1} {j+1} dist={dist}")

            coords[j] += np.random.normal(scale=0.1, size=3)

with open("insulin_fixed.xyz", "w") as f:

    f.write(f"{natoms}\n")
    f.write("fixed structure\n")

    for atom, c in zip(atoms, coords):
        f.write(
            f"{atom} "
            f"{c[0]:.6f} "
            f"{c[1]:.6f} "
            f"{c[2]:.6f}\n"
        )

print("Wrote insulin_fixed.xyz")


