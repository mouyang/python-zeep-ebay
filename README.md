# Introduction

This repository has components that allow Zeep to work with the eBay Trading API.

# Dependencies

The only dependency is a custom Zeep build (https://github.com/mouyang/python-zeep/tree/release/4.3.2%2Bebaytradingapi).  It is required the API requires query string parameters to be added to its POST request (https://developer.ebay.com/devzone/xml/docs/Concepts/MakingACall.html#SOAPURLParameters) and the upstream project cannot do this.  In particular, 

1. Support for query strings in POST requests. **PR** https://github.com/mvantellingen/python-zeep/pull/1479
2. Access to operation name in the Transport layer.  The required *callname* parameter is dependent on the operation being performed.  **PR** https://github.com/mvantellingen/python-zeep/pull/1480

The custom build will no longer be required once the PRs have been incorporated in the upstream project.  However, releases are quite infrequent (about 1 per year) and the upstream maintainer claims upstream to be "stable" (https://github.com/mvantellingen/python-zeep?tab=readme-ov-file#status).

# Installation

Until this has been published to PyPI, you'll need to pull this repository and the custom Zeep build, and install it locally.

# Code Sample

```
from zeep import Client
from zeep.ebay_transport import EbaySoapTransport

version, site_id ="<VERSION>", "<SITE_ID>"
transport = EbaySoapTransport(version=version, siteid=site_id)
client = Client(_trading_api_url, transport=transport)
```
