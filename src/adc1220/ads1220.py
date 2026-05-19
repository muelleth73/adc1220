import json
import time
from collections.abc import Callable
from typing import Any

from senspi.constants import NUMBER_PARAMETERS
from senspi.readconfig import get_logger

from jonasjelonek.ads1220 import ADS1220

"""
Read ADS1220 analog-digital converter 2026-01-11 15:30

Based on code https://codeberg.org/jonasjelonek/ads1220-python
Released under the MIT License




"""

SCHEMA = {
    "@type": "float",
    "@defaults": NUMBER_PARAMETERS,
}

log = get_logger(__name__)


def initialize(parameters: dict[str, Any] | None = None) -> Callable[[], float]:
    if parameters is None:
        parameters = {}
    gain = parameters.get("gain", 1)
    sensor = ADS1220()
    sensor.set_gain(gain)
    log.info(f"Initialized pushpull, gain={gain}, cfg is {parameters}")

    def read():
        """
        Return just the raw value from the ADC,
        ignoring the gain and voltage.
        """
        (
            _,
            _,
            readout,
        ) = sensor.read_adc_voltage()
        # print("voltage: {:7.3f}".format(voltage * 1000))
        #    print("gain:    " + str(gain))
        # print("raw:     " + str(readout))
        return readout

    return read


if __name__ == "__main__":
    r = initialize()
    while True:
        v = r()
        time.sleep(0.3)
        print(json.dumps(v, indent=2))
