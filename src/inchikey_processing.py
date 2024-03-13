from rdkit import Chem
from rdkit.Chem import inchi
import warnings

def standardise_inchikey(smiles_list):
    inchikey_list = []
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
    for smi in smiles_list:
        smi = str(smi)
        mol = Chem.MolFromSmiles(smi)
        if mol is not None:
            inchikey = inchi.MolToInchiKey(mol)
            inchikey_list.append(inchikey)
        else:
            inchikey_list.append(None)
    return inchikey_list