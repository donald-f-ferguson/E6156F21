import os
import json
from smartystreets_adaptor import SmartyStreetsAdaptor

from smartystreets_python_sdk import StaticCredentials, exceptions, ClientBuilder
from smartystreets_python_sdk.us_street import Lookup as StreetLookup


def t1():

    lookup = StreetLookup()
    # lookup.input_id = "24601"  # Optional ID from your system

    lookup.street = "520 W. 120th Street"
    # lookup.street2 = "closet under the stairs"
    #lookup.secondary = "APT 2"
    #lookup.urbanization = ""  # Only applies to Puerto Rico addresses
    lookup.city = "New York"
    lookup.state = "NY"
    lookup.zipcode = "10027"
    lookup.candidates = 3
    # lookup.match = "invalid"  # "invalid" is the most permissive match,
    # this will always return at least one result even if the address is invalid.
    # Refer to the documentation for additional Match Strategy options.

    sm_adaptor = SmartyStreetsAdaptor()
    sm_adaptor.do_lookup(lookup)
    j_result = sm_adaptor.to_json()

    print("T1 result = \n", json.dumps(j_result, indent=2, default=str))

def t2():

    lookup = StreetLookup()
    # lookup.input_id = "24601"  # Optional ID from your system

    lookup.street = "21 Hoyt"
    # lookup.street2 = "closet under the stairs"
    #lookup.secondary = "APT 2"
    #lookup.urbanization = ""  # Only applies to Puerto Rico addresses
    lookup.city = "S Salem"
    lookup.state = "NY"
    # lookup.zipcode = "02341"
    lookup.candidates = 3
    # lookup.match = "invalid"  # "invalid" is the most permissive match,
    # this will always return at least one result even if the address is invalid.
    # Refer to the documentation for additional Match Strategy options.

    sm_adaptor = SmartyStreetsAdaptor()
    sm_adaptor.do_lookup(lookup)
    j_result = sm_adaptor.to_json()

    print("T1 result = \n", json.dumps(j_result, indent=2, default=str))


def t3():
    sm = SmartyStreetsAdaptor()

    q = {
        "city": "Washington",
        "state": "DC",
        "street1": "1600 Penssylvania Ave"
    }
    res = sm.do_search(q)
    print("t3 result = ", res)

    if res >= 1:
        print(json.dumps(sm.to_json(), indent=2, default=str))


t1()
#t2()
#t3()

