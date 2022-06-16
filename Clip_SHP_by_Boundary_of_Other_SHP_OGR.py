# this script was written by Daniel Clement - 2022
"""This script clips a shapefile to the boundaries of an input shapefile using OGR2OGR"""

# do imports
from os import system, path

# set parameters
############################################################################################
# the shapefile you want to clip
shp_to_clip = r"C:\Data\Example.shp"

# the shapefile consisting of the AOI boundary you want to clip the shapefile to
clipping_shp = r"C:\Data\Example_AOI_Polygon.shp"

# the folder you want the clipped shapefile to be output to
output_folder = r"C:\Outputs"
############################################################################################

# create output shapefile name and path
input_name = path.basename(shp_to_clip)
output_shp = path.join(output_folder, input_name.replace(".shp", "_Clipped.shp"))

# create command
command = "ogr2ogr -clipsrc {} {} {}".format(clipping_shp, output_shp, shp_to_clip)

print("\nClipping feature...")

# run command
system(command)

print("\nFeature clipped successfully!")
