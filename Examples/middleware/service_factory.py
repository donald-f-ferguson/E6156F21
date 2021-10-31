"""

Students: Ignore this file ... ...


"""


from address_services.smarty_address_service import SmartyAddressService


class ServiceFactory():

    @staticmethod
    def get_address_service():
        return SmartyAddressService()