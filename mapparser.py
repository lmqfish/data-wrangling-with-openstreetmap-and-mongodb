#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
Fill out the count_tags function. It should return a dictionary with the
tag name as the key and number of times this tag can be encountered in
the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""
import xml.etree.cElementTree as ET
import pprint

def count_tags(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    tagCounts = {root.tag: 1}
    for node in root:
        for tag in node:
            if tag.tag not in tagCounts:
                tagCounts[tag.tag] = 0
            tagCounts[tag.tag] += 1

        if node.tag not in tagCounts:
           tagCounts[node.tag] = 0
        tagCounts[node.tag] += 1

    return tagCounts



def test():

    tags = count_tags('san-francisco_california.osm')
    pprint.pprint(tags)
    # assert tags == {'bounds': 1,
    #                 'member': 7745,
    #                 'nd': 1203161,
    #                 'node': 1510907,
    #                 'osm': 1,
    #                 'relation': 792,
    #                 'tag': 5925339,
    #                 'way': 117911}



if __name__ == "__main__":
    test()
