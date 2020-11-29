#!/usr/bin/python

from juniper.junos import Device

if _name_ == '_main_' :
    dev = Device(host='',user ='', passwd='')
    dev.open()
    routelxml= dev.rpc.get_route_information(table='inet.0')
    listofroutes=routelxml.findall('.//rt')
    for route in listofroutes:
        print("Route : {} Protocols :{}".format(route.findtext('rt-destination'),(route.findtext('rt-entry/protocol-name'))))
    dev.close()