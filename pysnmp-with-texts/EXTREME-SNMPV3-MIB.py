#
# PySNMP MIB module EXTREME-SNMPV3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:07:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
snmpTargetAddrEntry, = mibBuilder.importSymbols("SNMP-TARGET-MIB", "snmpTargetAddrEntry")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, IpAddress, Integer32, Gauge32, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, ModuleIdentity, ObjectIdentity, TimeTicks, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Integer32", "Gauge32", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Bits", "Unsigned32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
extremeSnmpv3 = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 23))
if mibBuilder.loadTexts: extremeSnmpv3.setLastUpdated('0007240000Z')
if mibBuilder.loadTexts: extremeSnmpv3.setOrganization('Extreme Networks, Inc.')
if mibBuilder.loadTexts: extremeSnmpv3.setContactInfo('www.extremenetworks.com')
if mibBuilder.loadTexts: extremeSnmpv3.setDescription('Extreme-specific SNMPv3 objects')
extremeTarget = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 23, 1))
extremeTargetAddrExtTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 23, 1, 1), )
if mibBuilder.loadTexts: extremeTargetAddrExtTable.setStatus('current')
if mibBuilder.loadTexts: extremeTargetAddrExtTable.setDescription('This table is an extension to the snmpTargetAddrTable found in the SNMP-TARGET-MIB. It contains Extreme Networks specific objects needed for each management target.')
extremeTargetAddrExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 23, 1, 1, 1), )
snmpTargetAddrEntry.registerAugmentions(("EXTREME-SNMPV3-MIB", "extremeTargetAddrExtEntry"))
extremeTargetAddrExtEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())
if mibBuilder.loadTexts: extremeTargetAddrExtEntry.setStatus('current')
if mibBuilder.loadTexts: extremeTargetAddrExtEntry.setDescription('An entry in the extremeTargetAddrExtTable.')
extremeTargetAddrExtIgnoreMPModel = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 23, 1, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeTargetAddrExtIgnoreMPModel.setStatus('current')
if mibBuilder.loadTexts: extremeTargetAddrExtIgnoreMPModel.setDescription("When this object is set to TRUE, the version of the trap/notification sent to the corresponding management target (trap receiver) will be the same as in releases of Extremeware prior to 7.1.0. Thus, the value of the snmpTargetParamsMPModel object in the snmpTargetParamsTable will be ignored while determining the version of the trap/notification to be sent. When a trap-receiver is created via the RMON trapDestTable or from the CLI command 'configure snmp add trapreceiver ....', the value of this object will be set to TRUE for the corresponding entry in this table.")
extremeTargetAddrExtStandardMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 23, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeTargetAddrExtStandardMode.setStatus('current')
if mibBuilder.loadTexts: extremeTargetAddrExtStandardMode.setDescription("When this object is set to TRUE, the management target will be treated as a 'standard mode' one, in that any Extreme Networks specific extra varbinds present in a standards-based trap/notification will not be sent to this management target. Only the varbinds defined in the standard will be sent.")
extremeTargetAddrExtTrapDestIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 23, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeTargetAddrExtTrapDestIndex.setStatus('current')
if mibBuilder.loadTexts: extremeTargetAddrExtTrapDestIndex.setDescription('This object contains the value of the trapDestIndex in the corresponding entry of the RMON trapDestTable.')
extremeTargetAddrExtUseEventComm = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 23, 1, 1, 1, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeTargetAddrExtUseEventComm.setStatus('current')
if mibBuilder.loadTexts: extremeTargetAddrExtUseEventComm.setDescription("This object is used only when sending RMON alarms as SNMPv3 traps. When it is set to TRUE and an RMON risingAlarm or fallingAlarm is being sent for an event, then the eventCommunity in the RMON event table is compared to the snmpTargetAddrName in the snmpTargetAddrTable. The alarm is sent to the target only when the two are the same. This behavior is exhibited only when the snmpTargetParamsMPModel corresponding to the target indicates an SNMPv3 trap. For SNMPv1/v2c traps, the community in the RMON trapDestTable is used for the comparision, which is the 'regular' method, as per the standards. When this object is set to FALSE, then the RMON alarm (if being sent as an SNMPv3 trap) is sent without using the event community for any comparision.")
mibBuilder.exportSymbols("EXTREME-SNMPV3-MIB", extremeTargetAddrExtTable=extremeTargetAddrExtTable, extremeTargetAddrExtEntry=extremeTargetAddrExtEntry, extremeTargetAddrExtUseEventComm=extremeTargetAddrExtUseEventComm, extremeTargetAddrExtIgnoreMPModel=extremeTargetAddrExtIgnoreMPModel, extremeTargetAddrExtStandardMode=extremeTargetAddrExtStandardMode, extremeTargetAddrExtTrapDestIndex=extremeTargetAddrExtTrapDestIndex, extremeSnmpv3=extremeSnmpv3, extremeTarget=extremeTarget, PYSNMP_MODULE_ID=extremeSnmpv3)