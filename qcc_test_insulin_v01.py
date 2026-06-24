from Bio.PDB import PDBList
from Bio.PDB import PDBParser

# PDB ダウンロード
#pdbl = PDBList()
#pdbl.retrieve_pdb_file('4INS', pdir='.', file_format='pdb')

import subprocess

cmd = [
    'xtb',
    'insulin.xyz',
    '--gfn2',
    '--opt',
    '--alpb', 'water'
]

subprocess.run(cmd)





