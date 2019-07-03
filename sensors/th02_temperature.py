from .sensor import Sensor
import logging

logger = logging.getLogger('root')


class Th02TemperatureSensor(Sensor):
    def __init__(self, name, topic, poll_freq_ms, flush_size, flush_after_s):
        super().__init__(name, topic, poll_freq_ms, flush_size, flush_after_s)

    def get_data(self):
        logger.debug('TH02 temp data')
        return 40
