import argparse
import toml

def get_params():
    """Gets command line arguments"""
    
    # ArgumentParser with a single argument to get the TOML file
    parser = argparse.ArgumentParser()
    parser.add_argument("parameterfile", help="Path to parameter file.")
    args = parser.parse_args()
    
    # Import parameters
    parameters = toml.load(args.parameterfile)

    return parameters


def main():
    parameters = get_params()
    sample_numbers = parameters["sample_numbers"]
    diameter = parameters["geometric_parameters"]["diameter"]
    length = parameters["geometric_parameters"]["length"]
    density = parameters["material_properties"]["density"]
    
    print(f"Sample numbers = {sample_numbers}"
          f"Diameter = {diameter} m"
          f"Length = {length} m"
          f"Density = {density} kg/m3")
    
    
if __name__ == "__main__":
    main() 
    