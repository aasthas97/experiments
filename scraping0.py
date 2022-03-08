"""Script to enter the name of a locality and find how far it is from Friedrichshain."""

import webbrowser

DESTINATION = 'eemagine Medical Imaging Solutions GmbH, Gubener Str. 47, 10243 Berlin, Germany'

def how_far_is_the_house(house_location):
    maps_url = 'https://www.google.com/maps/dir/%s/%s' % (house_location, DESTINATION)
    webbrowser.open(maps_url)

print('LOCALITY:')
loc = input('')
how_far_is_the_house(loc)