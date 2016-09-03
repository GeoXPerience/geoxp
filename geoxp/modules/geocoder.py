"""Module for geocoding."""
import geocoder


class Location(object):
    """Location is an model for representing a physical location."""

    def __init__(self, address, number, zip_code):
        """Initialize an Location with an address, number and zip code."""
        self.address = address
        self.number = number
        self.zip_code = zip_code

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return '%s, %s - %s' % (self.address, self.number, self.zip_code)


class Geocoder(object):
    """A class for geocoding objects."""

    def __init__(self, location=None, location_list=None):
        """Initialize geocoder.

        Receice a single location or a list of locations.
        """
        if location is not None:
            self.location_list = [location]
        else:
            self.location_list = location_list

    def geocode(self):
        pass
