from homeassistant.components.sensor import SensorEntity, SensorDeviceClass

from ..nhccoco.devices.robinsip_videodoorstation import CocoRobinsipVideodoorstation


class Nhc2RobinsipVideodoorstationCallStatus01Entity(SensorEntity):
    _attr_has_entity_name = True

    def __init__(self, device_instance: CocoRobinsipVideodoorstation, hub, gateway):
        """Initialize a enum sensor."""
        self._device = device_instance
        self._hub = hub
        self._gateway = gateway

        self._device.after_change_callbacks.append(self.on_change)

        self._attr_available = self._device.is_online
        self._attr_unique_id = device_instance.uuid + '_call_status_01'
        self._attr_should_poll = False
        self._attr_device_info = self._device.device_info(self._hub)

        self._attr_device_class = SensorDeviceClass.ENUM
        self._attr_options = self._device.possible_call_statuses_01
        self._attr_native_value = self._device.call_status_01
        self._attr_state_class = None

    @property
    def name(self) -> str:
        return 'Call Status 01'

    @property
    def state(self) -> str:
        return self._device.call_status_01

    def on_change(self):
        self.schedule_update_ha_state()
