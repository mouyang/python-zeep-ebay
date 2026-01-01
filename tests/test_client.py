import pytest

from zeep import Settings, Transport
from zeep.ebay.client import TradingApiClient

def test_strictTrue_retained():
    transport = Transport(timeout=10, operation_timeout=20)
    settings = Settings(strict = True)
    client_obj = TradingApiClient("2", "1375", settings=settings)
    assert settings.strict
