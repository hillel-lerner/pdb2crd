import argparse
from .converter import save_crd

def main():
    parser = argparse.ArgumentParser(
        description="Convert PDB coordinate files to CRD format",
        epilog="Note: This only converts coordinate information, not trajectories."
    )
    parser.add_argument("pdb_file", help="Input PDB file")
    parser.add_argument("-o", "--output", help="Output CRD file (default: same as PDB with .crd extension)")
    parser.add_argument("-s", "--segid", default="HETA", help="Segment ID to use in CRD file")
    
    args = parser.parse_args()
    
    try:
        output_path = save_crd(args.pdb_file, args.output, args.segid)
        print(f"Successfully converted {args.pdb_file} to {output_path}")
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()