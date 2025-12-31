from zeep.transports import Transport

# Subclass that injects the required query string parameters to an API call
# https://developer.ebay.com/api-docs/user-guides/static/make-a-call/using-soap.html#parameters
class EbaySoapTransport(Transport):
    def __init__(self, version, siteid):
        super().__init__()
        self.version = version
        self.siteid = siteid

    def post_xml(self, address, operation, envelope, headers, params={}):
        params = {
            "version": self.version, 
            "callname": operation, 
            "siteid": self.siteid, 
            "Routing": "new"
        }
        return super().post_xml(address, operation, envelope, headers, params)

