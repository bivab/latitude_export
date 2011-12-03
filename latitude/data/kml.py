from __future__ import division
from datetime import datetime
from latitude.config import config
from latitude.data import Data

import StringIO
import pytz
import xml.etree.ElementTree as ET

local_tz = config.get('KML', 'timezone')
local_tz = pytz.timezone(local_tz)

class KML(Data):
    extension = 'kml'

    def prepare(self):
        return self.build_document()

    def build_document(self):
        # build a tree structure
        kml = ET.Element("kml")
        kml.set('xmlns', "http://www.opengis.net/kml/2.2")
        kml.set('xmlns:atom', "http://www.w3.org/2005/Atom")
        kml.set('xmlns:kml', "http://www.opengis.net/kml/2.2")
        kml.set('xmlns:gx', "http://www.google.com/kml/ext/2.2")
        doc = ET.SubElement(kml, "Document")
        e = ET.SubElement(doc, "name")
        e.text = "Location history for %d"
        e = ET.SubElement(doc, "open")
        e.text= '1'
        ET.SubElement(doc, "description")
        self.build_stylemap(doc)
        self.build_styles(doc)
        self.build_placemark(doc)
        return ET.ElementTree(kml)


    def build_stylemap(self, root):
        e = ET.SubElement(root, "StyleMap")
        e.set("id", "multiTrack")
        p = ET.SubElement(e, "Pair")
        k = ET.SubElement(p, "key")
        k.text = "normal"
        s = ET.SubElement(p, "styleUrl")
        s.text = "#multiTrack_n"
        p = ET.SubElement(e, "Pair")
        k = ET.SubElement(p, "key")
        k.text = "highlight"
        s = ET.SubElement(p, "styleUrl")
        s.text = "#multiTrack_h"

    def build_styles(self, root):
        style = ET.SubElement(root, "Style")
        style.set("id", "multiTrack_n")
        ic = ET.SubElement(style, "IconStyle")
        i = ET.SubElement(ic, "Icon")
        href = ET.SubElement(i, "href")
        href.text = "http://earth.google.com/images/kml-icons/track-directional/track-0.png"
        ls = ET.SubElement(style, "LineStyle")
        color = ET.SubElement(ls, "color")
        color.text = "99ffac59"
        width = ET.SubElement(ls, "width")
        width.text = '6'

        style = ET.SubElement(root, "Style")
        style.set("id", "multiTrack_h")
        ic = ET.SubElement(style, "IconStyle")
        s = ET.SubElement(ic, "scale")
        s.text = "1.2"
        i = ET.SubElement(ic, "Icon")
        href = ET.SubElement(i, "href")
        href.text = "http://earth.google.com/images/kml-icons/track-directional/track-0.png"
        ls = ET.SubElement(style, "LineStyle")
        color = ET.SubElement(ls, "color")
        color.text = "99ffac59"
        width = ET.SubElement(ls, "width")
        width.text = '8'

    def build_placemark(self, root):
        mark = ET.SubElement(root, "Placemark")
        name = ET.SubElement(mark, "name")
        name.text = "Latitude User"
        descr = ET.SubElement(mark, "description")
        descr.text = "Location history for Latitude User from 11/28/2011 to 11/29/2011"
        url = ET.SubElement(mark, "styleUrl")
        url.text = "#multiTrack"
        self.build_track(mark)

    def build_track(self, placemark):
        track = ET.SubElement(placemark, "gx:Track" )
        am = ET.SubElement(track, "altitudeMode")
        am.text = "clampToGround"
        #XXX propper error handling
        # collect and sort entries
        entries = []
        for entry in self.data['items']:
            when = self.timestamp_to_utctime(entry['timestampMs'])
            where = "%s %s 0" % (entry['longitude'], entry['latitude'])
            entries.append((when, where))
        entries.sort()
        for time, location in entries:
            when = ET.SubElement(track, "when")
            when.text = time
            coord = ET.SubElement(track, "gx:coord")
            coord.text = location

    def timestamp_to_utctime(self, ts):
        event = datetime.fromtimestamp(long(ts)/1000)
        event = event - local_tz.utcoffset(event)
        return event.strftime("%Y-%m-%dT%H:%M:%S")
        #return event.strftime("%Y-%m-%dT%H:%M:%S%z")

    def __str__(self):
        root = self.prepare()
        output = StringIO.StringIO()
        root.write(output)
        contents = output.getvalue()
        output.close()
        return contents

format = KML
