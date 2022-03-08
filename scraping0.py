"""Script to enter the location of a house and figure out how far it is from my place of work in Berlin."""

import webbrowser

# https://www.google.com/maps/dir/Mitte,+Berlin,+Germany/eemagine+Medical+Imaging+Solutions+GmbH,+Gubener+Stra%C3%9Fe,+Berlin,+Germany/

DESTINATION = 'eemagine Medical Imaging Solutions GmbH, Gubener Str. 47, 10243 Berlin, Germany'

def how_far_is_the_house(house_location):
    maps_url = 'https://www.google.com/maps/dir/%s/%s' % (house_location, DESTINATION)
    webbrowser.open(maps_url)

loc = 'La Femme Patisserie'
how_far_is_the_house(loc)