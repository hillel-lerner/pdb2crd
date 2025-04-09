# pdb2crd
## PDB to CRD Converter

A Python package for converting PDB coordinate files to CHARMM/NAMD CRD format.

**Note**: This tool only converts coordinate information, not trajectories.

## Installation

```bash
pip install pdb2crd
```

## Usage

### Command Line Interface

```bash
pdb2crd input.pdb [-o output.crd] [-s SEGID]
```

- `input.pdb`: Input PDB file
- `-o output.crd`: Optional output file (default: same name as input with .crd extension)
- `-s SEGID`: Segment ID to use in CRD file (default: "HETA")

### Python API

```python
from pdb2crd import convert_pdb_to_crd, save_crd

# Convert and get CRD content as string
crd_content = convert_pdb_to_crd("input.pdb")

# Convert and save to file
output_path = save_crd("input.pdb", output_path="output.crd", seg_id="MYSEGID")
```

## Limitations

1. **Coordinate Data Only**: This converter only processes coordinate information from PDB files. It does not handle:
   - Trajectory data
   - Velocity information
   - Force field parameters

2. **Heteroatom Focus**: Designed primarily for small molecules/heteroatoms. For proteins, you may need to adjust the segment ID.

3. **Fixed Format**: Input PDB must follow standard column formatting.

## Development

To install for development:

```bash
git clone https://github.com/yourusername/pdb2crd.git
cd pdb2crd
pip install -e .
```

Run tests:
```bash
python -m pytest
```
