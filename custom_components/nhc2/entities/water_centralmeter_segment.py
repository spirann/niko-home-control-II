from homeassistant.components.sensor import SensorEntity, SensorDeviceClass
from homeassistant.helpers.entity import EntityCategory

from .nhc_entity import NHCBaseEntity
from ..nhccoco.devices.water_centralmeter import CocoWaterCentralmeter


class Nhc2WaterCentralmeterSegmentEntity(NHCBaseEntity, SensorEntity):
    _attr_has_entity_name = True

    def __init__(self, device_instance: CocoWaterCentralmeter, hub, gateway):
        """Initialize a sensor."""
        super().__init__(device_instance, hub, gateway)

        self._attr_unique_id = device_instance.uuid + '_segment'

        self._attr_device_class = SensorDeviceClass.ENUM
        self._attr_options = self._device.possible_segments
        self._attr_native_value = self._device.segment
        self._attr_entity_category = EntityCategory.DIAGNOSTIC

    @property
    def name(self) -> str:
        return 'Segment'

    @property
    def state(self) -> str:
        return self._device.segment
