from ..const import PROPERTY_WATER_VOLUME, PARAMETER_FLOW, PARAMETER_SEGMENT, PROPERTY_WATER_PULSE_PER_UNIT
from ..helpers import to_float_or_none, to_int_or_none
from .device import CoCoDevice

class CocoWaterCentralmeter(CoCoDevice):

    #{'Uuid': 'd60f1f18-05d2-489c-9042-b2e7bb93a5b1', 'Identifier': 'ed36ad43-a5a5-48a9-bf2a-86fba30ef675', 'Model': 'water', 'Online': 'True', 'Name': 'Boiler', 'Technology': 'nikohomecontrol', 'Type': 'centralmeter', 'Traits': [{'Channel': '0'}, {'MacAddress': '00200FA9'}], 'Parameters': [{'LocationId': '0ee306fe-3046-4263-a487-89fec29dfc62'}, {'Segment': 'Subsegment'}, {'PulsesPerUnit': '1000'}, {'LocationIcon': 'cold-storage-room'}, {'Flow': 'Consumer'}, {'ShortName': 'Boiler'}, {'LocationName': 'Annexe'}], 'Properties': [{'WaterVolume': ''}], 'PropertyDefinitions': [{'WaterVolume': {'HasStatus': 'false', 'CanControl': 'false', 'Description': 'Range(0.0000,3.2512,0.0001)'}}]}

    @property
    def pulse_per_unit(self) -> int:
        return to_int_or_none(self.extract_property_value(PROPERTY_WATER_PULSE_PER_UNIT))

    @property
    def water_volume(self) -> float:
        return to_float_or_none(self.extract_property_value(PROPERTY_WATER_VOLUME))

    @property
    def flow(self) -> str:
        return self.extract_parameter_value(PARAMETER_FLOW)

    @property
    def possible_flows(self) -> list:
        self.extract_property_definition_description_choices(PARAMETER_FLOW)

    @property
    def segment(self) -> str:
        return self.extract_parameter_value(PARAMETER_SEGMENT)

    @property
    def possible_segments(self) -> list:
        self.extract_property_definition_description_choices(PARAMETER_SEGMENT)

    @property
    def is_online(self) -> bool:
        # For some reason NHC return `False` for these devices. Sor overruling this.
        return True