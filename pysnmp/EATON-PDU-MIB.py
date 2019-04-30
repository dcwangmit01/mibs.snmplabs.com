#
# PySNMP MIB module EATON-PDU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EATON-PDU-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:44:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
pduAgent, = mibBuilder.importSymbols("EATON-OIDS", "pduAgent")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, TimeTicks, Counter64, iso, Unsigned32, ObjectIdentity, ModuleIdentity, Bits, Integer32, MibIdentifier, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Counter64", "iso", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "Bits", "Integer32", "MibIdentifier", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eatonPduMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 534, 6, 6, 4))
eatonPduMIB.setRevisions(('2007-01-08 00:00',))
if mibBuilder.loadTexts: eatonPduMIB.setLastUpdated('200701080000Z')
if mibBuilder.loadTexts: eatonPduMIB.setOrganization('Eaton Corporation')
class PositiveInteger(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class NonNegativeInteger(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

eatonPduMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1))
mainPdu = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1))
pduPanel = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2))
pduBreaker = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3))
pduNameplate = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 1))
pduRatingVA = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 1, 1), PositiveInteger()).setUnits('volt-amps').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduRatingVA.setStatus('current')
pduNominalOutputVoltage = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 1, 2), PositiveInteger()).setUnits('Volts RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduNominalOutputVoltage.setStatus('current')
pduNumPhases = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 1, 3), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pduNumPhases.setStatus('current')
pduNumPanels = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 1, 4), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pduNumPanels.setStatus('current')
pduInput = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2))
pduFrequency = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 1), NonNegativeInteger()).setUnits('0.1 Hertz').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduFrequency.setStatus('current')
pduInputVA = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 2), NonNegativeInteger()).setUnits('VA').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduInputVA.setStatus('current')
pduInputPower = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 3), NonNegativeInteger()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduInputPower.setStatus('current')
pduInputPowerFactor = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 100))).setUnits('pf * 100').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduInputPowerFactor.setStatus('current')
pduGroundCurrent = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 5), NonNegativeInteger()).setUnits('0.1 Amps RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduGroundCurrent.setStatus('current')
pduInputVoltageUnits = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pduInputVoltageUnits.setStatus('current')
pduInputNumPhases = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 7), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pduInputNumPhases.setStatus('current')
pduInputTable = MibTable((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 8), )
if mibBuilder.loadTexts: pduInputTable.setStatus('current')
pduInputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 8, 1), ).setIndexNames((0, "EATON-PDU-MIB", "pduInputPhaseIndex"))
if mibBuilder.loadTexts: pduInputEntry.setStatus('current')
pduInputPhaseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 8, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: pduInputPhaseIndex.setStatus('current')
pduInputPhaseVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 8, 1, 2), NonNegativeInteger()).setUnits('Volts RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduInputPhaseVoltage.setStatus('current')
pduInputPhaseCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 8, 1, 3), NonNegativeInteger()).setUnits('0.1 Amps RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduInputPhaseCurrent.setStatus('current')
pduInputPhasePercentLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 8, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduInputPhasePercentLoad.setStatus('current')
pduOutput = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3))
pduOutputKilowattHours = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 1), NonNegativeInteger()).setUnits('KWH').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduOutputKilowattHours.setStatus('current')
pduOutputVA = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 2), NonNegativeInteger()).setUnits('VA').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduOutputVA.setStatus('current')
pduOutputPower = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 3), NonNegativeInteger()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduOutputPower.setStatus('current')
pduOutputPowerFactor = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 100))).setUnits('pf * 100').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduOutputPowerFactor.setStatus('current')
pduNeutralCurrent = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 5), NonNegativeInteger()).setUnits('0.1 Amps RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduNeutralCurrent.setStatus('current')
pduRatedOutputCurrent = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 6), PositiveInteger()).setUnits('0.1 Amps RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduRatedOutputCurrent.setStatus('current')
pduOutputVoltageUnits = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pduOutputVoltageUnits.setStatus('current')
pduOutputNumPhases = MibScalar((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 8), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pduOutputNumPhases.setStatus('current')
pduOutputTable = MibTable((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 9), )
if mibBuilder.loadTexts: pduOutputTable.setStatus('current')
pduOutputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 9, 1), ).setIndexNames((0, "EATON-PDU-MIB", "pduOutputPhaseIndex"))
if mibBuilder.loadTexts: pduOutputEntry.setStatus('current')
pduOutputPhaseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 9, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: pduOutputPhaseIndex.setStatus('current')
pduOutputPhaseVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 9, 1, 2), NonNegativeInteger()).setUnits('Volts RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduOutputPhaseVoltage.setStatus('current')
pduOutputPhaseCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 9, 1, 3), NonNegativeInteger()).setUnits('0.1 Amps RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduOutputPhaseCurrent.setStatus('current')
pduOutputPhasePercentLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 9, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: pduOutputPhasePercentLoad.setStatus('current')
panelRatingsTable = MibTable((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1), )
if mibBuilder.loadTexts: panelRatingsTable.setStatus('current')
panelRatingsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1, 1), ).setIndexNames((0, "EATON-PDU-MIB", "panelNumber"))
if mibBuilder.loadTexts: panelRatingsEntry.setStatus('current')
panelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: panelNumber.setStatus('current')
panelRatedVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1, 1, 2), PositiveInteger()).setUnits('Volts RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelRatedVoltage.setStatus('current')
panelRatedBreakerCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1, 1, 3), PositiveInteger()).setUnits('0.1 Amps RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelRatedBreakerCurrent.setStatus('current')
panelNumPhases = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1, 1, 4), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panelNumPhases.setStatus('current')
panelNumBreakers = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1, 1, 5), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panelNumBreakers.setStatus('current')
panelVoltageUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: panelVoltageUnits.setStatus('current')
panelMetersTable = MibTable((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2), )
if mibBuilder.loadTexts: panelMetersTable.setStatus('current')
panelMetersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1), ).setIndexNames((0, "EATON-PDU-MIB", "panelNumber"))
if mibBuilder.loadTexts: panelMetersEntry.setStatus('current')
panelTotalKilowattHours = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1, 1), NonNegativeInteger()).setUnits('KWH').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelTotalKilowattHours.setStatus('current')
panelMonthlyKilowattHours = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1, 2), NonNegativeInteger()).setUnits('KWH').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelMonthlyKilowattHours.setStatus('current')
panelYtdKilowattHours = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1, 3), NonNegativeInteger()).setUnits('KWH').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelYtdKilowattHours.setStatus('current')
panelVA = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1, 4), NonNegativeInteger()).setUnits('VA').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelVA.setStatus('current')
panelPower = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1, 5), NonNegativeInteger()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelPower.setStatus('current')
panelPowerFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 100))).setUnits('pf * 100').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelPowerFactor.setStatus('current')
panelNeutralCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1, 7), NonNegativeInteger()).setUnits('0.1 Amps RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelNeutralCurrent.setStatus('current')
panelPhaseMetersTable = MibTable((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 3), )
if mibBuilder.loadTexts: panelPhaseMetersTable.setStatus('current')
panelPhaseMetersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 3, 1), ).setIndexNames((0, "EATON-PDU-MIB", "panelNumber"), (0, "EATON-PDU-MIB", "panelPhaseIndex"))
if mibBuilder.loadTexts: panelPhaseMetersEntry.setStatus('current')
panelPhaseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 3, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: panelPhaseIndex.setStatus('current')
panelPhaseVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 3, 1, 2), NonNegativeInteger()).setUnits('Volts RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelPhaseVoltage.setStatus('current')
panelPhaseCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 3, 1, 3), NonNegativeInteger()).setUnits('0.1 Amps RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelPhaseCurrent.setStatus('current')
panelPhasePercentLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: panelPhasePercentLoad.setStatus('current')
breakerRatingsTable = MibTable((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 1), )
if mibBuilder.loadTexts: breakerRatingsTable.setStatus('current')
breakerRatingsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 1, 1), ).setIndexNames((0, "EATON-PDU-MIB", "panelNumber"), (0, "EATON-PDU-MIB", "breakerNumber"))
if mibBuilder.loadTexts: breakerRatingsEntry.setStatus('current')
breakerNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 1, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: breakerNumber.setStatus('current')
breakerName = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: breakerName.setStatus('current')
breakerRatedCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 1, 1, 3), PositiveInteger()).setUnits('0.1 Amps RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: breakerRatedCurrent.setStatus('current')
breakerNumPhases = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 1, 1, 4), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: breakerNumPhases.setStatus('current')
breakerMetersTable = MibTable((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 2), )
if mibBuilder.loadTexts: breakerMetersTable.setStatus('current')
breakerMetersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 2, 1), ).setIndexNames((0, "EATON-PDU-MIB", "panelNumber"), (0, "EATON-PDU-MIB", "breakerNumber"))
if mibBuilder.loadTexts: breakerMetersEntry.setStatus('current')
breakerTotalKilowattHours = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 2, 1, 1), NonNegativeInteger()).setUnits('KWH').setMaxAccess("readonly")
if mibBuilder.loadTexts: breakerTotalKilowattHours.setStatus('current')
breakerMonthlyKilowattHours = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 2, 1, 2), NonNegativeInteger()).setUnits('KWH').setMaxAccess("readonly")
if mibBuilder.loadTexts: breakerMonthlyKilowattHours.setStatus('current')
breakerYtdKilowattHours = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 2, 1, 3), NonNegativeInteger()).setUnits('KWH').setMaxAccess("readonly")
if mibBuilder.loadTexts: breakerYtdKilowattHours.setStatus('current')
breakerPhaseMetersTable = MibTable((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3), )
if mibBuilder.loadTexts: breakerPhaseMetersTable.setStatus('current')
breakerPhaseMetersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3, 1), ).setIndexNames((0, "EATON-PDU-MIB", "panelNumber"), (0, "EATON-PDU-MIB", "breakerNumber"), (0, "EATON-PDU-MIB", "breakerPhaseIndex"))
if mibBuilder.loadTexts: breakerPhaseMetersEntry.setStatus('current')
breakerPhaseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: breakerPhaseIndex.setStatus('current')
breakerPhaseVA = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3, 1, 2), NonNegativeInteger()).setUnits('VA').setMaxAccess("readonly")
if mibBuilder.loadTexts: breakerPhaseVA.setStatus('current')
breakerPhasePower = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3, 1, 3), NonNegativeInteger()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: breakerPhasePower.setStatus('current')
breakerPhasePowerFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 100))).setUnits('pf * 100').setMaxAccess("readonly")
if mibBuilder.loadTexts: breakerPhasePowerFactor.setStatus('current')
breakerPhaseCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3, 1, 5), NonNegativeInteger()).setUnits('0.1 Amps RMS').setMaxAccess("readonly")
if mibBuilder.loadTexts: breakerPhaseCurrent.setStatus('current')
breakerPhasePercentLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: breakerPhasePercentLoad.setStatus('current')
eatonPduConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2))
pduNameplateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 1)).setObjects(("EATON-PDU-MIB", "pduNumPhases"), ("EATON-PDU-MIB", "pduNominalOutputVoltage"), ("EATON-PDU-MIB", "pduRatingVA"), ("EATON-PDU-MIB", "pduNumPanels"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pduNameplateGroup = pduNameplateGroup.setStatus('current')
pduInputGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 2)).setObjects(("EATON-PDU-MIB", "pduFrequency"), ("EATON-PDU-MIB", "pduInputVA"), ("EATON-PDU-MIB", "pduInputPower"), ("EATON-PDU-MIB", "pduInputPowerFactor"), ("EATON-PDU-MIB", "pduGroundCurrent"), ("EATON-PDU-MIB", "pduInputVoltageUnits"), ("EATON-PDU-MIB", "pduInputNumPhases"), ("EATON-PDU-MIB", "pduInputPhaseVoltage"), ("EATON-PDU-MIB", "pduInputPhaseCurrent"), ("EATON-PDU-MIB", "pduInputPhasePercentLoad"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pduInputGroup = pduInputGroup.setStatus('current')
pduOutputGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 3)).setObjects(("EATON-PDU-MIB", "pduOutputKilowattHours"), ("EATON-PDU-MIB", "pduOutputVA"), ("EATON-PDU-MIB", "pduOutputPower"), ("EATON-PDU-MIB", "pduOutputPowerFactor"), ("EATON-PDU-MIB", "pduNeutralCurrent"), ("EATON-PDU-MIB", "pduRatedOutputCurrent"), ("EATON-PDU-MIB", "pduOutputVoltageUnits"), ("EATON-PDU-MIB", "pduOutputNumPhases"), ("EATON-PDU-MIB", "pduOutputPhaseVoltage"), ("EATON-PDU-MIB", "pduOutputPhaseCurrent"), ("EATON-PDU-MIB", "pduOutputPhasePercentLoad"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pduOutputGroup = pduOutputGroup.setStatus('current')
panelRatingsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 4)).setObjects(("EATON-PDU-MIB", "panelRatedVoltage"), ("EATON-PDU-MIB", "panelRatedBreakerCurrent"), ("EATON-PDU-MIB", "panelNumPhases"), ("EATON-PDU-MIB", "panelNumBreakers"), ("EATON-PDU-MIB", "panelVoltageUnits"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    panelRatingsGroup = panelRatingsGroup.setStatus('current')
panelMetersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 5)).setObjects(("EATON-PDU-MIB", "panelTotalKilowattHours"), ("EATON-PDU-MIB", "panelMonthlyKilowattHours"), ("EATON-PDU-MIB", "panelYtdKilowattHours"), ("EATON-PDU-MIB", "panelVA"), ("EATON-PDU-MIB", "panelPower"), ("EATON-PDU-MIB", "panelPowerFactor"), ("EATON-PDU-MIB", "panelNeutralCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    panelMetersGroup = panelMetersGroup.setStatus('current')
panelPhaseMetersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 6)).setObjects(("EATON-PDU-MIB", "panelPhaseVoltage"), ("EATON-PDU-MIB", "panelPhaseCurrent"), ("EATON-PDU-MIB", "panelPhasePercentLoad"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    panelPhaseMetersGroup = panelPhaseMetersGroup.setStatus('current')
breakerRatingsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 7)).setObjects(("EATON-PDU-MIB", "breakerName"), ("EATON-PDU-MIB", "breakerRatedCurrent"), ("EATON-PDU-MIB", "breakerNumPhases"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    breakerRatingsGroup = breakerRatingsGroup.setStatus('current')
breakerMetersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 8)).setObjects(("EATON-PDU-MIB", "breakerTotalKilowattHours"), ("EATON-PDU-MIB", "breakerMonthlyKilowattHours"), ("EATON-PDU-MIB", "breakerYtdKilowattHours"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    breakerMetersGroup = breakerMetersGroup.setStatus('current')
breakerPhaseMetersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 9)).setObjects(("EATON-PDU-MIB", "breakerPhaseVA"), ("EATON-PDU-MIB", "breakerPhasePower"), ("EATON-PDU-MIB", "breakerPhasePowerFactor"), ("EATON-PDU-MIB", "breakerPhaseCurrent"), ("EATON-PDU-MIB", "breakerPhasePercentLoad"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    breakerPhaseMetersGroup = breakerPhaseMetersGroup.setStatus('current')
pdu3phaseCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 10)).setObjects(("EATON-PDU-MIB", "pduNameplateGroup"), ("EATON-PDU-MIB", "pduInputGroup"), ("EATON-PDU-MIB", "pduOutputGroup"), ("EATON-PDU-MIB", "panelRatingsGroup"), ("EATON-PDU-MIB", "panelMetersGroup"), ("EATON-PDU-MIB", "panelPhaseMetersGroup"), ("EATON-PDU-MIB", "breakerRatingsGroup"), ("EATON-PDU-MIB", "breakerMetersGroup"), ("EATON-PDU-MIB", "breakerPhaseMetersGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdu3phaseCompliance = pdu3phaseCompliance.setStatus('current')
mibBuilder.exportSymbols("EATON-PDU-MIB", eatonPduConformance=eatonPduConformance, panelNeutralCurrent=panelNeutralCurrent, pduNameplateGroup=pduNameplateGroup, eatonPduMIB=eatonPduMIB, panelRatedBreakerCurrent=panelRatedBreakerCurrent, pduInputPhaseVoltage=pduInputPhaseVoltage, panelNumPhases=panelNumPhases, breakerPhaseMetersTable=breakerPhaseMetersTable, panelRatedVoltage=panelRatedVoltage, breakerPhaseIndex=breakerPhaseIndex, PYSNMP_MODULE_ID=eatonPduMIB, pduOutput=pduOutput, pduOutputPhaseVoltage=pduOutputPhaseVoltage, panelMetersGroup=panelMetersGroup, pduInputVoltageUnits=pduInputVoltageUnits, breakerTotalKilowattHours=breakerTotalKilowattHours, pduOutputTable=pduOutputTable, breakerPhaseCurrent=breakerPhaseCurrent, panelMonthlyKilowattHours=panelMonthlyKilowattHours, breakerPhasePowerFactor=breakerPhasePowerFactor, pduPanel=pduPanel, pduBreaker=pduBreaker, panelPhaseVoltage=panelPhaseVoltage, breakerNumber=breakerNumber, panelTotalKilowattHours=panelTotalKilowattHours, panelRatingsGroup=panelRatingsGroup, pduInputTable=pduInputTable, panelPowerFactor=panelPowerFactor, pduInputPower=pduInputPower, pduNumPhases=pduNumPhases, pduGroundCurrent=pduGroundCurrent, panelPhaseIndex=panelPhaseIndex, panelPower=panelPower, pduOutputPhasePercentLoad=pduOutputPhasePercentLoad, mainPdu=mainPdu, panelVA=panelVA, panelPhasePercentLoad=panelPhasePercentLoad, breakerPhaseVA=breakerPhaseVA, panelNumber=panelNumber, breakerMetersTable=breakerMetersTable, panelNumBreakers=panelNumBreakers, panelRatingsTable=panelRatingsTable, panelPhaseMetersGroup=panelPhaseMetersGroup, pduNumPanels=pduNumPanels, breakerRatingsGroup=breakerRatingsGroup, pduInputPhaseCurrent=pduInputPhaseCurrent, pduOutputVA=pduOutputVA, pduInputGroup=pduInputGroup, breakerPhasePercentLoad=breakerPhasePercentLoad, panelVoltageUnits=panelVoltageUnits, NonNegativeInteger=NonNegativeInteger, panelMetersEntry=panelMetersEntry, pduOutputGroup=pduOutputGroup, pduOutputKilowattHours=pduOutputKilowattHours, breakerPhasePower=breakerPhasePower, pduNeutralCurrent=pduNeutralCurrent, pduOutputPhaseCurrent=pduOutputPhaseCurrent, panelPhaseMetersEntry=panelPhaseMetersEntry, pduRatingVA=pduRatingVA, breakerRatedCurrent=breakerRatedCurrent, panelYtdKilowattHours=panelYtdKilowattHours, pduOutputPower=pduOutputPower, pduInputNumPhases=pduInputNumPhases, breakerPhaseMetersGroup=breakerPhaseMetersGroup, pdu3phaseCompliance=pdu3phaseCompliance, pduInputPowerFactor=pduInputPowerFactor, pduOutputNumPhases=pduOutputNumPhases, breakerName=breakerName, pduFrequency=pduFrequency, pduInputPhasePercentLoad=pduInputPhasePercentLoad, pduInputVA=pduInputVA, pduInput=pduInput, pduOutputVoltageUnits=pduOutputVoltageUnits, pduInputPhaseIndex=pduInputPhaseIndex, breakerMetersEntry=breakerMetersEntry, pduNameplate=pduNameplate, eatonPduMIBObjects=eatonPduMIBObjects, breakerMetersGroup=breakerMetersGroup, pduOutputPhaseIndex=pduOutputPhaseIndex, pduOutputEntry=pduOutputEntry, pduOutputPowerFactor=pduOutputPowerFactor, panelMetersTable=panelMetersTable, panelPhaseCurrent=panelPhaseCurrent, breakerNumPhases=breakerNumPhases, panelPhaseMetersTable=panelPhaseMetersTable, pduRatedOutputCurrent=pduRatedOutputCurrent, breakerMonthlyKilowattHours=breakerMonthlyKilowattHours, breakerYtdKilowattHours=breakerYtdKilowattHours, breakerRatingsTable=breakerRatingsTable, PositiveInteger=PositiveInteger, breakerPhaseMetersEntry=breakerPhaseMetersEntry, pduInputEntry=pduInputEntry, panelRatingsEntry=panelRatingsEntry, pduNominalOutputVoltage=pduNominalOutputVoltage, breakerRatingsEntry=breakerRatingsEntry)