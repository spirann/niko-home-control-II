from homeassistant.components.binary_sensor import BinarySensorEntity

from ..nhccoco.devices.overallcomfort_action import CocoOverallcomfortAction


class Nhc2OverallcomfortActionAllStartedEntity(BinarySensorEntity):
    _attr_has_entity_name = True

    def __init__(self, device_instance: CocoOverallcomfortAction, hub, gateway):
        """Initialize a binary sensor."""
        self._device = device_instance
        self._hub = hub
        self._gateway = gateway

        self._device.after_change_callbacks.append(self.on_change)

        self._attr_available = self._device.is_online
        self._attr_unique_id = device_instance.uuid + '_all_started'
        self._attr_should_poll = False
        self._attr_device_info = self._device.device_info(self._hub)

        self._attr_state = self._device.is_all_started
        self._attr_state_class = None

    @property
    def name(self) -> str:
        return 'All Started'

    @property
    def is_on(self) -> bool:
        return self._device.is_all_started

    def on_change(self):
        self.schedule_update_ha_state()
