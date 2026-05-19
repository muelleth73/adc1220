import pytest

adc = pytest.importorskip("adc1220")
ads = pytest.importorskip("ads1220")


def test_hardware():
    r = ads.initialize()
    v = r()
    assert v is not None
