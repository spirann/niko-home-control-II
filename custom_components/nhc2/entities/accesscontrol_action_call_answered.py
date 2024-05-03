from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.helpers.entity import EntityCategory

from ..nhccoco.devices.accesscontrol_action import CocoAccesscontrolAction


class Nhc2AccesscontrolActionCallAnsweredEntity(BinarySensorEntity):
    _attr_has_entity_name = True

    def __init__(self, device_instance: CocoAccesscontrolAction, hub, gateway):
        """Initialize a binary sensor."""
        self._device = device_instance
        self._hub = hub
        self._gateway = gateway

        self._device.after_change_callbacks.append(self.on_change)

        self._attr_available = self._device.is_online
        self._attr_unique_id = device_instance.uuid + '_call_answered'
        self._attr_should_poll = False
        self._attr_device_info = self._device.device_info(self._hub)

        self._attr_state = self._device.is_call_answered
        self._attr_state_class = None
        self._attr_entity_category = EntityCategory.DIAGNOSTIC

    @property
    def name(self) -> str:
        return 'Call Answered'

    @property
    def is_on(self) -> bool:
        return self._device.is_call_answered

    def on_change(self):
        self.schedule_update_ha_state()
