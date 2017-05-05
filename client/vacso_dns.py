from .dme2 import DME2
import logging
import pprint

#import json

dns = DME2("1a3b6c5f-fa77-40ae-ba40-d01cdd8e93e3", "be6e37ed-3f84-49c8-8a69-3e274312f816")
logger = logging.getLogger(__name__)

def get_domain_id(domain):
    domainroot = dns.get_domain('name?domainname=' + domain)
    return(domainroot['id'])

def get_current_dc(domain):
    domainid = get_domain_id(domain)
    domainrecords = dns.get_records_from_domain(domainid)
    logger.error(pprint.pformat(domainrecords))
    
    recorddict = {}
    for record in domainrecords:
        if record['type'] != 'A':
            continue
        recorddict[record['name']] = record
        
    rootip = recorddict['']['value']
    rootid = recorddict['']['id']
    rootrecord = recorddict['']
    dfwip = recorddict['dfw1']['value']
    lasip = recorddict['las1']['value']
    
    
    logger.error(rootip + ' ' +  dfwip + ' ' + lasip)
    
    current_dc = 'Unknown'
    current_ip = rootip
    other_ip = ''
    
    if rootip == dfwip:
        current_dc = 'dfw1'
        other_ip = lasip
    elif rootip == lasip:
        current_dc = 'las1'
        other_ip = dfwip
    
    return(current_dc, current_ip, other_ip, domainid, rootid, rootrecord)

def swap_dc(domain):
    #update_record_by_id(self, domainId, recordId, data):
    current_dc, current_ip, other_ip, domainid, rootid, rootrecord = get_current_dc(domain)
    rootrecord['value'] = other_ip
    dns.update_record_by_id(domainid, rootid, rootrecord)
    