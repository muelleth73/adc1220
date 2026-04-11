from adc1220.ads1220 import initialize


def test_placeholder():
    r = initialize()
    v = r()
    assert v is not None
