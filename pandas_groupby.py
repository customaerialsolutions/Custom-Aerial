import folium
import webbrowser
import pandas as pd
from folium import plugins
import json
import requests
from pandas.io.json import json_normalize

df_incidents = pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Police_Department_Incidents_-_Previous_Year__2016_.csv')

df_incidents.drop(['IncidntNum','Category','Descript', 'DayOfWeek', 'Date', 'Time','Resolution', 'Address', 'X', 'Y', 'Location','PdId'], axis=1, inplace=True)
df_incidents.rename(columns={'PdDistrict':'Neighborhood'}, inplace=True)
d = df_incidents['Neighborhood'].value_counts().reset_index()
d.columns=['Neighborhood','Total']
print(d)


san_fran = r'https://cocl.us/sanfran_geojson'
latitude = 37.77
longitude = -122.42
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12,)

sanfran_map.choropleth(
    geo_data=san_fran,
    data=d,
    columns=['Neighborhood','Total'],
    key_on = 'feature.properties.DISTRICT',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Crime rate in San Fransisco'
)
             

sanfran_map.save('map.html')
webbrowser.open('map.html')


