import argparse
import os
import sys
from .converter import save_crd

def main():
    parser = argparse.ArgumentParser(
        description="Convert PDB coordinate files to CHARMM CRD format",
        epilog="Note: This converts ATOM/HETATM records only, preserving original coordinates."
    )
    
    # Required arguments
    parser.add_argument(
        "pdb_file", 
        help="Input PDB file path"
    )
    
    # Optional arguments
    parser.add_argument(
        "-o", "--output", 
        help="Output CRD file path (default: <input>.crd)"
    )
    parser.add_argument(
        "-s", "--segid", 
        default="HETA",
        help="Segment ID to use in CRD file (default: HETA)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show detailed conversion information"
    )
    
    args = parser.parse_args()
    
    try:
        # Validate input file exists
        if not os.path.exists(args.pdb_file):
            raise FileNotFoundError(f"Input file not found: {args.pdb_file}")
            
        # Perform conversion
        output_path = save_crd(
            pdb_path=args.pdb_file,
            output_path=args.output,
            seg_id=args.segid
        )
        
        # Success message
        if args.verbose:
            print(f"Conversion successful:")
            print(f"• Input:  {os.path.abspath(args.pdb_file)}")
            print(f"• Output: {os.path.abspath(output_path)}")
            print(f"• Atoms converted: {len(open(output_path).readlines()) - 2}")  # Subtract header lines
        else:
            print(f"Successfully created: {output_path}")
            
    except Exception as e:
        print(f"\nError: {str(e)}", file=sys.stderr)
        if args.verbose:
            print(f"\nDebug info:", file=sys.stderr)
            print(f"- Input file: {args.pdb_file}", file=sys.stderr)
            print(f"- Output path: {args.output}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()