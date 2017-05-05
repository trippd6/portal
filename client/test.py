from dme2 import DME2
import json
dns = DME2("1a3b6c5f-fa77-40ae-ba40-d01cdd8e93e3", "be6e37ed-3f84-49c8-8a69-3e274312f816")

#domains = dns.get_domains()
#for d in domains:
#    print(d)
#    
#dns.add_domains('test12341234.com')

records = dns.get_records_from_domain('3333946')

recorddict = {}
for record in records:
    recorddict[record['name']] = record
    
print('root: ' + recorddict['']['value'])
print('dfw1: ' + recorddict['dfw1']['value'])
print('las1: ' + recorddict['las1']['value'])

    
    
#print(json.dumps(records, sort_keys=True, indent=4))