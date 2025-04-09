import os

def convert_pdb_to_crd(pdb_path, seg_id="HETA"):
    """
    Convert a PDB file to CRD format.
    
    Args:
        pdb_path (str): Path to input PDB file
        seg_id (str): Segment ID to use in CRD file (default: "HETA")
    
    Returns:
        str: CRD formatted content
    """
    try:
        with open(pdb_path, 'r') as f:
            pdb_lines = f.readlines()

    except IOError as e:
        raise ValueError(f"Could not read PDB file: {str(e)}")

    atoms = [line for line in pdb_lines if line.startswith(("ATOM", "HETATM"))]
    
    if not atoms:
        raise ValueError("No ATOM/HETATM records found in PDB file")

    crd_lines = []
    atoms = [line for line in pdb_lines if line.startswith(("ATOM", "HETATM"))]
    crd_lines.append(f"{len(atoms):5d} EXT")

    for i, line in enumerate(atoms, 1):
        try:
            atom_num = int(line[6:11].strip())
            atom_name = line[12:16].strip().ljust(4)
            res_name = line[17:20].strip().ljust(4)
            res_num = int(line[22:26].strip())
            x = float(line[30:38].strip())
            y = float(line[38:46].strip())
            z = float(line[46:54].strip())
            
            crd_line = (
                f"{i:10d}{i:10d}  {res_name:4s}      {atom_name:4s}  "
                f"{x:12.6f}      {y:12.6f}      {z:12.6f}  {seg_id}      {res_num:6d}"
                )
            crd_lines.append(crd_line)
        except (ValueError, IndexError) as e:
            raise ValueError(f"Error parsing line {i}: {line.strip()}") from e

    return "\n".join(crd_lines)

def save_crd(pdb_path, output_path=None, seg_id="HETA"):
    """
    Convert PDB to CRD and save to file.
    
    Args:
        pdb_path (str): Path to input PDB file
        output_path (str, optional): Output CRD path. If None, uses same name as PDB with .crd extension
        seg_id (str): Segment ID to use in CRD file
    """
    crd_content = convert_pdb_to_crd(pdb_path, seg_id)
    
    if output_path is None:
        output_path = os.path.splitext(pdb_path)[0] + ".crd"
    
    with open(output_path, 'w') as f:
        f.write(crd_content)
    
    return output_path