#
# PySNMP MIB module CHARACTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CHARACTER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:31:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, iso, mib_2, Unsigned32, Bits, TimeTicks, ModuleIdentity, Counter32, Counter64, ObjectIdentity, MibIdentifier, transmission, Gauge32, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "mib-2", "Unsigned32", "Bits", "TimeTicks", "ModuleIdentity", "Counter32", "Counter64", "ObjectIdentity", "MibIdentifier", "transmission", "Gauge32", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
InstancePointer, AutonomousType, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "InstancePointer", "AutonomousType", "TextualConvention", "DisplayString")
char = ModuleIdentity((1, 3, 6, 1, 2, 1, 19))
if mibBuilder.loadTexts: char.setLastUpdated('9405261700Z')
if mibBuilder.loadTexts: char.setOrganization('IETF Character MIB Working Group')
class PortIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

charNumber = MibScalar((1, 3, 6, 1, 2, 1, 19, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charNumber.setStatus('current')
charPortTable = MibTable((1, 3, 6, 1, 2, 1, 19, 2), )
if mibBuilder.loadTexts: charPortTable.setStatus('current')
charPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 19, 2, 1), ).setIndexNames((0, "CHARACTER-MIB", "charPortIndex"))
if mibBuilder.loadTexts: charPortEntry.setStatus('current')
charPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 1), PortIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortIndex.setStatus('current')
charPortName = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPortName.setStatus('current')
charPortType = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("physical", 1), ("virtual", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortType.setStatus('current')
charPortHardware = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 4), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortHardware.setStatus('current')
charPortReset = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("execute", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPortReset.setStatus('current')
charPortAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("off", 3), ("maintenance", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPortAdminStatus.setStatus('current')
charPortOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("maintenance", 3), ("absent", 4), ("active", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortOperStatus.setStatus('current')
charPortLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortLastChange.setStatus('current')
charPortInFlowType = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("xonXoff", 2), ("hardware", 3), ("ctsRts", 4), ("dsrDtr", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPortInFlowType.setStatus('deprecated')
charPortOutFlowType = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("xonXoff", 2), ("hardware", 3), ("ctsRts", 4), ("dsrDtr", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPortOutFlowType.setStatus('deprecated')
charPortInFlowState = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("unknown", 2), ("stop", 3), ("go", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortInFlowState.setStatus('current')
charPortOutFlowState = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("unknown", 2), ("stop", 3), ("go", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortOutFlowState.setStatus('current')
charPortInCharacters = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortInCharacters.setStatus('current')
charPortOutCharacters = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortOutCharacters.setStatus('current')
charPortAdminOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dynamic", 1), ("network", 2), ("local", 3), ("none", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPortAdminOrigin.setStatus('current')
charPortSessionMaximum = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPortSessionMaximum.setStatus('current')
charPortSessionNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 17), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortSessionNumber.setStatus('current')
charPortSessionIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortSessionIndex.setStatus('current')
charPortInFlowTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPortInFlowTypes.setStatus('current')
charPortOutFlowTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 20), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPortOutFlowTypes.setStatus('current')
charPortLowerIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 21), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortLowerIfIndex.setStatus('current')
charSessTable = MibTable((1, 3, 6, 1, 2, 1, 19, 3), )
if mibBuilder.loadTexts: charSessTable.setStatus('current')
charSessEntry = MibTableRow((1, 3, 6, 1, 2, 1, 19, 3, 1), ).setIndexNames((0, "CHARACTER-MIB", "charSessPortIndex"), (0, "CHARACTER-MIB", "charSessIndex"))
if mibBuilder.loadTexts: charSessEntry.setStatus('current')
charSessPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 1), PortIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charSessPortIndex.setStatus('current')
charSessIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charSessIndex.setStatus('current')
charSessKill = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("execute", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charSessKill.setStatus('current')
charSessState = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("connecting", 1), ("connected", 2), ("disconnecting", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charSessState.setStatus('current')
charSessProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 5), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charSessProtocol.setStatus('current')
wellKnownProtocols = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 4))
protocolOther = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 4, 1))
protocolTelnet = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 4, 2))
protocolRlogin = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 4, 3))
protocolLat = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 4, 4))
protocolX29 = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 4, 5))
protocolVtp = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 4, 6))
charSessOperOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("network", 2), ("local", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charSessOperOrigin.setStatus('current')
charSessInCharacters = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charSessInCharacters.setStatus('current')
charSessOutCharacters = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charSessOutCharacters.setStatus('current')
charSessConnectionId = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 9), InstancePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charSessConnectionId.setStatus('current')
charSessStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charSessStartTime.setStatus('current')
charConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 5))
charGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 5, 1))
charCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 5, 2))
charCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 19, 5, 2, 1)).setObjects(("CHARACTER-MIB", "charGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    charCompliance = charCompliance.setStatus('current')
charGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 19, 5, 1, 1)).setObjects(("CHARACTER-MIB", "charNumber"), ("CHARACTER-MIB", "charPortIndex"), ("CHARACTER-MIB", "charPortName"), ("CHARACTER-MIB", "charPortType"), ("CHARACTER-MIB", "charPortHardware"), ("CHARACTER-MIB", "charPortReset"), ("CHARACTER-MIB", "charPortAdminStatus"), ("CHARACTER-MIB", "charPortOperStatus"), ("CHARACTER-MIB", "charPortLastChange"), ("CHARACTER-MIB", "charPortInFlowState"), ("CHARACTER-MIB", "charPortOutFlowState"), ("CHARACTER-MIB", "charPortAdminOrigin"), ("CHARACTER-MIB", "charPortSessionMaximum"), ("CHARACTER-MIB", "charPortInFlowTypes"), ("CHARACTER-MIB", "charPortOutFlowTypes"), ("CHARACTER-MIB", "charPortInCharacters"), ("CHARACTER-MIB", "charPortOutCharacters"), ("CHARACTER-MIB", "charPortSessionNumber"), ("CHARACTER-MIB", "charPortSessionIndex"), ("CHARACTER-MIB", "charPortLowerIfIndex"), ("CHARACTER-MIB", "charSessPortIndex"), ("CHARACTER-MIB", "charSessIndex"), ("CHARACTER-MIB", "charSessKill"), ("CHARACTER-MIB", "charSessState"), ("CHARACTER-MIB", "charSessProtocol"), ("CHARACTER-MIB", "charSessOperOrigin"), ("CHARACTER-MIB", "charSessInCharacters"), ("CHARACTER-MIB", "charSessOutCharacters"), ("CHARACTER-MIB", "charSessConnectionId"), ("CHARACTER-MIB", "charSessStartTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    charGroup = charGroup.setStatus('current')
mibBuilder.exportSymbols("CHARACTER-MIB", charSessTable=charSessTable, charPortSessionMaximum=charPortSessionMaximum, charPortLowerIfIndex=charPortLowerIfIndex, char=char, charSessOutCharacters=charSessOutCharacters, charGroup=charGroup, charPortInFlowType=charPortInFlowType, charPortIndex=charPortIndex, charGroups=charGroups, charSessConnectionId=charSessConnectionId, charPortOutFlowState=charPortOutFlowState, charPortInFlowState=charPortInFlowState, charSessStartTime=charSessStartTime, charPortOutCharacters=charPortOutCharacters, charSessEntry=charSessEntry, protocolTelnet=protocolTelnet, charPortEntry=charPortEntry, charPortInCharacters=charPortInCharacters, wellKnownProtocols=wellKnownProtocols, charSessPortIndex=charSessPortIndex, charSessState=charSessState, charCompliance=charCompliance, protocolOther=protocolOther, charPortOperStatus=charPortOperStatus, charPortAdminOrigin=charPortAdminOrigin, charPortName=charPortName, charConformance=charConformance, protocolVtp=protocolVtp, charCompliances=charCompliances, charSessInCharacters=charSessInCharacters, charPortTable=charPortTable, charPortLastChange=charPortLastChange, charPortHardware=charPortHardware, charPortAdminStatus=charPortAdminStatus, PYSNMP_MODULE_ID=char, protocolX29=protocolX29, protocolRlogin=protocolRlogin, charPortOutFlowType=charPortOutFlowType, charSessProtocol=charSessProtocol, charNumber=charNumber, charPortType=charPortType, charSessIndex=charSessIndex, PortIndex=PortIndex, charPortReset=charPortReset, charSessOperOrigin=charSessOperOrigin, charPortSessionIndex=charPortSessionIndex, charSessKill=charSessKill, protocolLat=protocolLat, charPortOutFlowTypes=charPortOutFlowTypes, charPortInFlowTypes=charPortInFlowTypes, charPortSessionNumber=charPortSessionNumber)