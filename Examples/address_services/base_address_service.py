from abc import ABC, abstractmethod

candidate_fields = [
    'city_name', 'default_city_name', 'delivery_point', 'delivery_point_check_digit', 'extra_secondary_designator',
    'extra_secondary_number', 'plus4_code', 'pmb_designator', 'pmb_number', 'primary_number', 'secondary_designator',
    'secondary_number', 'state_abbreviation', 'street_name', 'street_postdirection', 'street_predirection',
    'street_suffix', 'urbanization', 'zipcode'
]


class AddressDataTransferObject():

    def __init__(self):
        self.city_name = None
        self.city_name = None
        self.unique_id = None
        self.street_no_1 = None
        self.state = None
        self.street_name = None
        self.street_prefix = None
        self.street_cat = None
        self.street_suffix = None
        self.zipcode = None
        self.extras = None


class BaseAddressService(ABC):

    def __init__(self):
        pass

    @abstractmethod
    @classmethod
    def look_up(cls, address_dto):
        pass
