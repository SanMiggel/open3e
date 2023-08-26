"""
  Copyright 2023 abnoname
  
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
"""

import Open3Ecodecs
from Open3Ecodecs import *

dataIdentifiersVdens = {
    256	: RawCodec(36, "BusIdentification"),
    268	: O3EInt16(9, "FlowTemperatureSensor", signed=True),
    271	: O3EInt16(9, "DomesticHotWaterSensor", signed=True),
    273 : O3EInt16(9, "SolarRoofTemperatureSensor", signed=True),
    274	: O3EInt16(9, "OutsideTemperatureSensor", signed=True),
    275 : O3EInt16(9, "SolarBottomTemperatureSensor", signed=True),
    284	: O3EInt16(9, "MixerOneCircuitFlowTemperatureSensor", signed=True),
    286	: O3EInt16(9, "MixerTwoCircuitFlowTemperatureSensor", signed=True),
    288	: O3EInt16(9, "MixerThreeCircuitFlowTemperatureSensor", signed=True),
    290	: O3EInt16(9, "MixerFourCircuitFlowTemperatureSensor", signed=True),
    318	: O3EInt16(9, "WaterPressureSensor"),
    331	: O3EInt16(9, "FlueGasTemperatureSensor", signed=True),
    360 : O3EInt16(9, "DomesticHotWaterOutletSensor", signed=True),
    364 : O3EInt8(6, "Flame", offset = 1),
    365 : RawCodec(42, "FlameStatistical"),
    377	: RawCodec(16, "ViessmannIdentificationNumber"),
    381	: O3EInt8(4, "CentralHeatingPump", offset = 1),
    396	: O3EInt16(2, "DomesticHotWaterTemperatureSetpoint", signed=True),
    402 : O3EInt16(5, "MixerTwoCircuitPump", signed=True),
    417 : O3EInt8(5, "SolarCircuitPump"),
    424	: O3EInt16(9, "MixerOneCircuitRoomTemperatureSetpoint", signed=True),
    426	: O3EInt16(9, "MixerTwoCircuitRoomTemperatureSetpoint", signed=True),
    428	: O3EInt16(9, "MixerThreeCircuitRoomTemperatureSetpoint", signed=True),
    430	: O3EInt16(9, "MixerFourCircuitRoomTemperatureSetpoint", signed=True),
    476 : O3EInt8(2,  "MixerTwoCircuitThreeWayValvePositionPercent", signed=True),
    497	: O3EInt16(5, "DomesticHotWaterCirculationPumpMode", signed=True),
    503	: RawCodec(2, "ScaldProtection"),
    504	: RawCodec(10, "DomesticHotWaterSetpointMetaData"),
    526 : O3EInt16(2, "ModulationCurrentValue"),
    527 : O3EInt16(2, "FlowTemperatureTargetSetpoint", signed=True),
    531 : O3EInt16(2, "DomesticHotWaterOperationState", signed=True),
    874	: RawCodec(2, "LegionellaProtectionTargetTemperatureSetpoint"),
    880	: O3EHeatingCurve(4, "MixerOneCircuitCentralHeatingCurve"),
    881	: O3EHeatingCurve(4, "MixerTwoCircuitCentralHeatingCurve"),
    882	: O3EHeatingCurve(4, "MixerThreeCircuitCentralHeatingCurve"),
    883	: O3EHeatingCurve(4, "MixerFourCircuitCentralHeatingCurve"),
    896	: O3EInt8(2, "OutsideTemperatureOffset"),
    897	: O3EInt8(1, "ScreedDryingProfileActivation"),
    901	: O3EInt8(1, "ServiceManagerIsRequired"),
    902	: O3EInt8(1, "MalfunctionIdentification"),
    919	: RawCodec(2, "OutsideTemperatureDampingFactor"),
    933	: O3EInt16(9, "MixerOneCircuitProperty"),
    934	: O3EInt16(9, "MixerTwoCircuitProperty"),
    935	: O3EInt16(9, "MixerThreeCircuitProperty"),
    936	: O3EInt16(9, "MixerFourCircuitProperty"),
    950 : O3EInt8(4, "SolarCircuitWaterFlowRate", signed=True),
    988 : O3EInt16(2, "MixerTwoCircuitFlowTemperatureTargetSetpoint", signed=True),
    1043	: O3EInt16(5, "AllengraSensor"),
    1085	: O3EInt16(4, "DomesticHotWaterHysteresis"),
    1087	: O3EInt8(2, "MaximumDomesticHotWaterLoadingTime"),
    1100	: RawCodec(3, "CentralHeatingPumpMinimumMaximumLimit"),
    1101	: RawCodec(3, "DomesticHotWaterPumpMinimumMaximumLimit"),
    1125 : O3EInt16(2, "SolarMaximumLoadingTemperature", signed=True),
    1128 : O3EInt16(2, "SolarStagnationHours", signed=True),
    1192	: RawCodec(10, "MixerOneCircuitFlowTemperatureMinimumMaximumLimit"),
    1193	: RawCodec(10, "MixerTwoCircuitFlowTemperatureMinimumMaximumLimit"),
    1194	: RawCodec(10, "MixerThreeCircuitFlowTemperatureMinimumMaximumLimit"),
    1195	: RawCodec(10, "MixerFourCircuitFlowTemperatureMinimumMaximumLimit"),
    1240	: O3EInt8(1, "CentralHeatingPumpMode"),
    1339	: O3EInt8(1, "MalfunctionHeatingUnitBlocked"),
    1394 : O3EInt16(2, "SolarChargingDomesticHotWaterSetpoint", signed=True),
    1395	: RawCodec(3, "MixerOneCircuitSummerSavingTemperatureThreshold"),
    1396	: RawCodec(3, "MixerTwoCircuitSummerSavingTemperatureThreshold"),
    1397	: RawCodec(3, "MixerThreeCircuitSummerSavingTemperatureThreshold"),
    1398	: RawCodec(3, "MixerFourCircuitSummerSavingTemperatureThreshold"),
    1415	: O3EInt8(2, "MixerOneCircuitOperationState", offset = 1),
    1416	: O3EInt8(2, "MixerTwoCircuitOperationState", offset = 1),
    1417	: O3EInt8(2, "MixerThreeCircuitOperationState", offset = 1),
    1418	: O3EInt8(2, "MixerFourCircuitOperationState", offset = 1),
    2257 : O3EInt16(2, "DomesticHotWaterTemperatureSetpointOffset", signed=True),
    2320	: O3EInt8(1, "DomesticHotWaterStatus"),
    2426	: RawCodec(6, "MixerOneCircuitRoomEcoFunctionSettings"),
    2427	: RawCodec(6, "MixerTwoCircuitRoomEcoFunctionSettings"),
    2428	: RawCodec(6, "MixerThreeCircuitRoomEcoFunctionSettings"),
    2429	: RawCodec(6, "MixerFourCircuitRoomEcoFunctionSettings"),
    2457	: O3EInt16(9, "CalculatedOutsideTemperature", signed=True),
}