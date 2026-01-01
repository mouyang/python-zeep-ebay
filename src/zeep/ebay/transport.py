from zeep.transports import Transport

# Subclass that injects the required query string parameters to an API call
# https://developer.ebay.com/api-docs/user-guides/static/make-a-call/using-soap.html#parameters
class EbaySoapTransport(Transport):
    def __init__(self, version, siteid,
        cache=None, timeout=300, operation_timeout=None, session=None):
        super().__init__(cache=cache, timeout=timeout, operation_timeout=operation_timeout, session=session)
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

