from homeassistant.components.sensor import SensorEntity, SensorDeviceClass, SensorStateClass
from homeassistant.const import UnitOfVolume

from .nhc_entity import NHCBaseEntity
from ..nhccoco.devices.water_centralmeter import CocoWaterCentralmeter


class Nhc2WaterCentralmeterWaterVolumeEntity(NHCBaseEntity, SensorEntity):
    _attr_has_entity_name = True

    def __init__(self, device_instance: CocoWaterCentralmeter, hub, gateway):
        """Initialize a sensor."""
        super().__init__(device_instance, hub, gateway)

        self._attr_unique_id = device_instance.uuid + '_water_volume'

        self._attr_device_class = SensorDeviceClass.WATER
        self._attr_native_value = self._device.water_volume
        self._attr_native_unit_of_measurement = UnitOfVolume.CUBIC_METERS
        self._attr_state_class = SensorStateClass.TOTAL_INCREASING
        self._attr_suggested_display_precision = 3
        self._attr_native_precision = 3

    @property
    def name(self) -> str:
        return 'Water Volume'

    @property
    def native_value(self) -> float:
        return self._device.water_volume
