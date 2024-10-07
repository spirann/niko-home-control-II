from homeassistant.components.sensor import SensorEntity, SensorDeviceClass, SensorStateClass
from homeassistant.helpers.entity import EntityCategory

from .nhc_entity import NHCBaseEntity
from ..nhccoco.devices.water_centralmeter import CocoWaterCentralmeter


class Nhc2WaterCentralmeterWaterPulsePerVolumeEntity(NHCBaseEntity, SensorEntity):
    _attr_has_entity_name = True

    def __init__(self, device_instance: CocoWaterCentralmeter, hub, gateway):
        """Initialize a sensor."""
        super().__init__(device_instance, hub, gateway)

        self._attr_unique_id = device_instance.uuid + '_pulse_per_unit'

        self._attr_native_value = self._device.pulse_per_unit
        self._attr_entity_category = EntityCategory.DIAGNOSTIC

    @property
    def name(self) -> str:
        return 'Pulse Per Unit'

    @property
    def native_value(self) -> int:
        return self._device.pulse_per_unit
