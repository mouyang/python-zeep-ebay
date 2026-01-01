from copy import deepcopy
from enum import Enum

from zeep import Client, Settings, Transport
from zeep.ebay.transport import EbaySoapTransport

# TODO Add sandbox support; currently not implemented because it downloads and parses a WSDL that doesn't include the 
# sandbox URL in it. 
class TradingApiClient(Client):
    def __init__(self, siteid : str, version : str = "latest", 
        wsse=None,
        transport : Transport = Transport(),
        service_name=None,
        port_name=None,
        plugins=None,
        settings=None
    ):
        self.siteid = siteid
        self.version = version
        self.wsdl = f"""https://developer.ebay.com/webservices/{self.version}/ebaysvc.wsdl"""
        
        self.settings = Settings()
        if settings:
            self.settings.strict = settings.strict
            self.settings.raw_response = settings.raw_response
            self.settings.force_https = settings.force_https
            self.settings.extra_http_headers = settings.extra_http_headers
            self.settings.xml_huge_tree = settings.xml_huge_tree
            self.settings.forbid_dtd = settings.forbid_dtd
            self.settings.forbid_entities = settings.forbid_entities
            self.settings.forbid_external = settings.forbid_external
            self.settings.xsd_ignore_sequence_order = settings.xsd_ignore_sequence_order
        # strict=False will be used regardless of what is provided as a constructor argument.  This is required for 
        # this API it sometimes returns elements that are not part of the schema. 
        # (example: GetItem v1375 returns 
        # /GetItemResponseType/Item/Seller/SellerInfo/LiveAuctionedAuthorized when it is not the associated schema.)
        self.settings.strict = False

        super().__init__(self.wsdl  
            , transport=EbaySoapTransport(
                version=self.version, siteid=self.siteid, 
                cache=transport.cache, timeout=transport.load_timeout, operation_timeout=transport.operation_timeout, session=transport.session)
            , settings=self.settings
            , wsse=wsse
            , service_name=service_name
            , port_name=port_name
            , plugins=plugins
        )