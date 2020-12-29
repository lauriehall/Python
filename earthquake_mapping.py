# Laurie Hall
# Assignment PA_13 - PART TWO
# Purpose: using json file, plot earthquakes on map with 
# magnitude >=5.0 an only in southern hemisphere
# Answers to questions on bottom of file
#######################################################

import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = input ('Enter the path and file name of the file containing the earthquake data: ')

# store the entire set of data in a file. The json load function converts to format-giant dictionary
with open (filename) as f:
    all_mo_data = json.load(f)

all_mo_dicts = all_mo_data['features']

#add an addl list for hover_text
mags, lons, lats, hover_texts = [], [], [], []

# only pull magnitudes >5.0 and southern hemisphere
for mo_dict in all_mo_dicts:
    mag = float (mo_dict['properties']['mag'])
    lat = float (mo_dict['geometry']['coordinates'][1])
    lon = float (mo_dict['geometry']['coordinates'][0])
    if mag >= 5.0 and lat <= 0.0:
            lon = mo_dict ['geometry']['coordinates'][0]
            lat = mo_dict ['geometry']['coordinates'][1]

            title = mo_dict ['properties']['title']
            mags.append(mag)
            lons.append(lon)
            lats.append(lat)
            hover_texts.append(title)

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [3 * mag for mag in mags],
        'color': mags,
        'colorscale': 'Jet',                # different colerscale than video
        'reversescale': False,              # false so blue/cool shows low mag and red/hot showed high mag
        'colorbar': {'title': 'Magnitude'},
    },
}]

# give chart a title
my_layout = Layout(title = 'Earthquakes in the southern hemisphere with magnitude >= 5.0 on Richter scale: ')

# create dictionary called fig that contains the data and layout
fig = {'data': data, 'layout': my_layout}

# pass fig to the plot() function along with a descriptive filename for the output
offline.plot(fig, filename = 'global_earthquakes.html')

####### Questions for assignment #######

# True or False, there was an earthquake with a magnitude of 5.0 or greater in Australia?
    # False

# In what country was the largest earthquake located in?  What was the magnitude?
    # Indonesia in Saumlaki with a magnitude of 6.8

# What was the magnitude of the largest earthquake in South America? What were it's longitude and latitude?
    # 5.7 in Lampa, Puru with coordinates of -70.4705, --15.2907 degrees


# C:/Users/lauri/OneDrive/Desktop/Laurie Files/MCC/CIS156_Python/Assignment 13/all_month.json