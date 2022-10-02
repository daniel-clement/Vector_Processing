import geopandas as gpd
from glob import glob
from tqdm import tqdm

################################################################################################
# the shapefile you want to project
# states_shp = r"C:\Users\DC-User\Desktop\Data\cb_2018_us_state_500k\cb_2018_us_state_500k.shp"
in_folder = r"C:\Users\DC-User\Desktop\Data\cb_2018_us_state_500k"

# the EPSG code of the new projection you want to use
new_epsg = 3857
################################################################################################

shp_list = glob(in_folder + "/*.shp")

for shp in tqdm(shp_list):

    # read in the shapefile
    states_gdf = gpd.read_file(shp)

    # create new geodataframe with new projection
    states_prj_gdf = states_gdf.to_crs(epsg=new_epsg)

    # creating the output shapefile path
    prj_shp = shp.replace(".shp", "_prj.shp")

    # saving the projected dataframe to a new shapefile
    states_prj_gdf.to_file(prj_shp)
