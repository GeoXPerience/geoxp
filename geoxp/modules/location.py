from collections import namedtuple
import geocoder


class Location(object):
    '''Location is a model for representing a physical location'''

    def __init__(self, address):
        '''Initialize an Location with an address, number, zip code
        and geolocation'''
        self.street = address[0]
        self.number = address[1]
        self.zip = address[2]
        self.geoloc = self.geocode(address)

    def geocode(self, address):
        loc = '%s, %s - %s' % (address[0], address[1], address[2])
        g = geocoder.google(loc)
        Geocode = namedtuple('Geocode', 'lat, long')
        return Geocode(lat=g.latlng[0], long=g.latlng[1])

    def write(self, csv_file):
        address = '%s;%s;%s;%s;%s\n' % (self.street, self.number, self.zip,
                                        self.geoloc.lat, self.geoloc.long)
        csv_file.write(address)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return '%s, %s - %s (%s, %s)' % (self.street, self.number, self.zip,
                                         self.geoloc.lat, self.geoloc.long)
