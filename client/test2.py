import libcloud.dns.providers
import dnsmadeeasy

API_KEY = '1a3b6c5f-fa77-40ae-ba40-d01cdd8e93e3'
API_SECRET = 'be6e37ed-3f84-49c8-8a69-3e274312f816'

Driver = libcloud.dns.providers.get_driver('dnsmadeeasy')
connection = Driver(API_KEY, API_SECRET)

for zone in driver.list_zones():
    print(zone);
    