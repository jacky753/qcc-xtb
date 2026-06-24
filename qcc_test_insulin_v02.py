import subprocess

cmd = [
    "xtb",
    "insulin_fixed.xyz",
    "--gfn2",
    "--opt",
    "--alpb",
    "water"
]

subprocess.run(cmd, check=True)

