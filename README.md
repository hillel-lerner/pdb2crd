# PDB to CRD Converter

Convert PDB coordinate files to CHARMM/NAMD CRD format directly from GitHub.

![PDB to CRD Conversion](https://img.shields.io/badge/format-PDB→CRD-blue) 
![Python 3.6+](https://img.shields.io/badge/python-3.6+-green)

## Features
- Convert PDB/HETATM records to CRD format
- Preserve atom/residue naming conventions
- Cross-platform (Windows/Linux/macOS)
- CLI and Python API support

## Installation

### From GitHub (Recommended)
```bash
pip install git+https://github.com/hillel-lerner/pdb2crd.git
```

### Manual Installation
1. Download the repository:
   ```bash
   git clone https://github.com/hillel-lerner/pdb2crd.git
   cd pdb2crd
   ```
2. Install:
   ```bash
   pip install .
   ```

## Usage

### Command Line
```bash
pdb2crd input.pdb [-o output.crd] [-s SEGID]
```
Example:
```bash
pdb2crd molecule.pdb -o molecule.crd -s PFP
```

### Python API
```python
from pdb2crd import convert_pdb_to_crd, save_crd

# Convert to CRD string
crd_content = convert_pdb_to_crd("input.pdb")

# Save to file
save_crd("input.pdb", "output.crd", seg_id="MYID")
```

## Limitations
- Only converts coordinate data (no trajectories)
- Requires standard PDB formatting
- Designed for small molecules

## Development
```bash
git clone https://github.com/yourusername/pdb2crd.git
cd pdb2crd
pip install -e .[dev]  # Install with development dependencies
pytest -v  # Run tests
```

## License
MIT License - See [LICENSE](LICENSE) file


**For Windows Users**: Add this troubleshooting section if needed:
   ```markdown
   ## Windows Troubleshooting
   If encountering SSL errors:
   ```cmd
   git config --global http.sslBackend schannel
   ```
   ```
