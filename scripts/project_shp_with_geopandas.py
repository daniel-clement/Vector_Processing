# this script was written by Daniel Clement - 2022
"""
This script uses qgis to convert a GeoJSON to a CSV file.
Only works for point data.
"""

# do imports
import geopandas as gpd
from glob import glob
from tqdm import tqdm

# set input parameters
##############################################################################
# the folder with the shapefiles you want to project
input_folder_path = r"C:\Users\user-1\path\to\folder"

# the EPSG code of the new projection you want to use
new_epsg = 3857

# the format of the input files
input_format = "geojson"  # "geojson" or "shp"
##############################################################################


def project_file(in_file: str, epsg_code: int, in_format: str) -> str:
    """
    reprojects the input file to the desired new projection
    Args:
        in_file: the path to the input file as a string
        epsg_code: the epsg code to reproject to
        in_format: the format of the input files

    Returns:
        the path to the reprojected file as a string
    """
    # read in the shapefile
    states_gdf = gpd.read_file(in_file)

    # create new geodataframe with new projection
    states_prj_gdf = states_gdf.to_crs(epsg=epsg_code)

    # creating the output file path
    out_file = in_file.replace(
        f".{in_format}", f"_{epsg_code}.{in_format}"
    )

    # saving the projected dataframe to a new shapefile
    states_prj_gdf.to_file(out_file)

    return out_file


def main():
    # create list of all GeoJSON files in the input folder
    in_files = glob(input_folder_path + f"/*.{input_format}")

    # make an empty list to hold output csv paths
    out_file_path_list = []

    # Ensure there are input files in inDir, else throw an error and stop the
    # script
    if len(in_files) > 0:
        pass
    else:
        print("ERROR - No input files found...")
        exit()

    # loop through each geojson in inFiles and convert to a csv
    for file in tqdm(in_files, desc="Reprojecting Files"):
        out_file = project_file(
            in_file=file, epsg_code=new_epsg, in_format=input_format
        )

        out_file_path_list.append(out_file)

    # get number of files processed
    num_in_files = len(in_files)
    num_out_files = len(out_file_path_list)

    print("\n################################################################")
    # check to see if number of in files equal out files
    if num_out_files == num_in_files:
        print("All Files Successfully Reprojected!")
    else:
        print("Error! - Not all Files successfully Reprojected. :(")
    print("##################################################################")


if __name__ == "__main__":
    main()
