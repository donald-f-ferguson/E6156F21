"""

This should be an installed package, and not something inside all projects.
I did not want to set up all the Python package stuff.

"""

import os
import json

def get_context_property(property_name):

    prop_str = os.environ.get(property_name, None)
    result = prop_str

    # If the string is not None, let's see if we can convert into a dict/JSON
    try:
        json_props = json.loads(prop_str)
    except json.JSONDecodeError as je:
        # Was not JSON but that is OK.


