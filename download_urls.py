import sys
import collections
from KalturaClient import *
from KalturaClient.Plugins.Core import *

#
# This program receives a list of entries, and provides the download URL for them
#
# Usage:
#       python3 download_urls <pId> <userId> <adminSecret> <entriesFileName> <outputFileName>
# 

myConfig = {
    'pId': None,
    'adminSecret': None, 
    'userId': None,
    'entriesFileName': None,
    'outputFileName':'remove_flavors.log' }

myFiles= {
    'in': None,
    'out': None }

myKaltura= {
    'serviceUrl': 'https://www.kaltura.com/',
    'client': None ,
    'filterAsset': None,
    'pagerAsset': None}

exceptions = { 
    'usage': 'Use following commandline arguments: <pId> <userId> <adminSecret> <entriesFileName> <outputFileName>',
    'io': 'Error when opening in/out files. Check permissions etc.' }

def processConfig():
    try:
        myConfig['pId']= int(sys.argv[1])
        myConfig['userId']= sys.argv[2]
        myConfig['adminSecret']= sys.argv[3]
        myConfig['entriesFileName']= sys.argv[4]
        myConfig['outputFileName']= sys.argv[5]
    except:
        raise ValueError(exceptions['usage'])

def openFiles():
    try:
        myFiles['in']= open(myConfig['entriesFileName'],'r')
        myFiles['out']= open(myConfig['outputFileName'],'w')
        myFiles['out'].write('\t'.join(['ENTRY_ID', 'DOWNLOAD_URL'])+'\n')
    except:
        raise ValueError[exceptions['io']]

def closeFiles():
    for file in myFiles:
        myFiles[file].close()

def kalturaInit():
    config = KalturaConfiguration()
    config.serviceUrl = myKaltura['serviceUrl']
    myKaltura['client'] = KalturaClient(config)
    ks =  myKaltura['client'].session.start(
        myConfig['adminSecret'],
        myConfig['userId'],
        KalturaSessionType.ADMIN,
        myConfig['pId'])
    myKaltura['client'].setKs(ks)
    myKaltura['filterAsset']= KalturaAssetFilter()
    myKaltura['filterAsset'].sizeGreaterThanOrEqual = 1
    myKaltura['pagerAsset']= KalturaFilterPager()

    
def kalturaProcessEntryId(entryId):
    myKaltura['filterAsset'].entryIdEqual = entryId
    result = myKaltura['client'].flavorAsset.list(myKaltura['filterAsset'], myKaltura['pagerAsset'])
    flavors={}
    for flavor in result.getObjects():
        if flavor.flavorParamsId > 0:
            flavors[flavor.size]= flavor.id
    flavorId= flavors[sorted(flavors.keys())[-1]]    
    downloadUrl = myKaltura['client'].flavorAsset.getUrl(flavorId, 0, False, KalturaFlavorAssetUrlOptions())
    myFiles['out'].write('\t'.join([entryId, downloadUrl])+'\n')

def main():
    
    processConfig()
    openFiles()
    kalturaInit()

    try:
        while True:
            entryId= myFiles['in'].readline().strip()
            if not entryId:
                break
            kalturaProcessEntryId(entryId)
    except:
        raise ValueError(exceptions['usage'])

    closeFiles()
    
main()
