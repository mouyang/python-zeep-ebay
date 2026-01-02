import pytest

from zeep import Settings
from zeep.ebay.client import TradingApiClient

def test_strictTrue_retained():
    settings = Settings(strict = True)
    client_obj = TradingApiClient("2", "1375", settings=settings)
    assert settings.strict
