import os
import numpy as np
import argparse





def convert_pidx_to_npy(directory):
    """
    Convert all .pidx files in the given directory to .npy format.
    
    Parameters:
    - directory (str): Path to the directory containing .pidx files.
    """
    # Check if the provided path is a valid directory
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file has a .pidx extension
        if filename.endswith('.pidx'):
            pidx_path = os.path.join(directory, filename)
            npy_path = os.path.join(directory, filename + '.npy')

            try:
                # Load the .pidx file (assuming it's stored in a way compatible with NumPy arrays)
                # Example: If your .pidx file is binary and can be loaded with numpy.fromfile
                # Replace with the appropriate file loading mechanism if needed.
                # data = np.fromfile(pidx_path, dtype=np.float32)  # Change dtype if necessary
                data = np.loadtxt(pidx_path, dtype=np.int32)

                # Save the loaded data to a .npy file
                np.save(npy_path, data)
                print(f"Converted {pidx_path} to {npy_path}")
            except Exception as e:
                print(f"Failed to convert {pidx_path}: {str(e)}")

if __name__ == "__main__":
    # Setup argument parser to accept the directory path from the console
    parser = argparse.ArgumentParser(description="Convert .pidx files to .npy format")
    parser.add_argument("directory", type=str, help="Path to the directory containing .pidx files")

    # Parse the arguments
    args = parser.parse_args()
    
    # Call the conversion function with the provided directory
    convert_pidx_to_npy(args.directory)