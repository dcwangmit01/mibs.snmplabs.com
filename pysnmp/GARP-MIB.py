#
# PySNMP MIB module GARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GARP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:04:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, ModuleIdentity, ObjectIdentity, Unsigned32, IpAddress, enterprises, Counter32, MibIdentifier, Integer32, Counter64, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "IpAddress", "enterprises", "Counter32", "MibIdentifier", "Integer32", "Counter64", "NotificationType", "Gauge32")
PhysAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "TextualConvention", "DisplayString")
cabletron = MibIdentifier((1, 3, 6, 1, 4, 1, 52))
mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4))
ctronExp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2))
ctVLANMib = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 12))
ctVLANMgr = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1))
ctGarp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3))
ctGarpTables = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2))
garpApplicationTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 1), )
if mibBuilder.loadTexts: garpApplicationTable.setStatus('mandatory')
garpApplicationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 1, 1), ).setIndexNames((0, "GARP-MIB", "garpApplicationAppType"))
if mibBuilder.loadTexts: garpApplicationEntry.setStatus('mandatory')
garpApplicationAppType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: garpApplicationAppType.setStatus('mandatory')
garpApplicationName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 1, 1, 2), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: garpApplicationName.setStatus('mandatory')
garpApplicationFailedRegistrations = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: garpApplicationFailedRegistrations.setStatus('mandatory')
garpApplicationOperationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: garpApplicationOperationStatus.setStatus('mandatory')
garpPortOperationTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 2), )
if mibBuilder.loadTexts: garpPortOperationTable.setStatus('mandatory')
garpPortOperationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 2, 1), ).setIndexNames((0, "GARP-MIB", "garpPortOperationAppType"), (0, "GARP-MIB", "garpPortOperationPort"))
if mibBuilder.loadTexts: garpPortOperationEntry.setStatus('mandatory')
garpPortOperationAppType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: garpPortOperationAppType.setStatus('mandatory')
garpPortOperationPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: garpPortOperationPort.setStatus('mandatory')
garpPortOperationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: garpPortOperationStatus.setStatus('mandatory')
garpTimerTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 3), )
if mibBuilder.loadTexts: garpTimerTable.setStatus('mandatory')
garpTimerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 3, 1), ).setIndexNames((0, "GARP-MIB", "garpTimerAttributeAppType"), (0, "GARP-MIB", "garpTimerAttributePort"))
if mibBuilder.loadTexts: garpTimerEntry.setStatus('mandatory')
garpTimerAttributeAppType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: garpTimerAttributeAppType.setStatus('mandatory')
garpTimerAttributePort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: garpTimerAttributePort.setStatus('mandatory')
garpTimerAttributeJoin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: garpTimerAttributeJoin.setStatus('mandatory')
garpTimerAttributeLeave = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 3, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: garpTimerAttributeLeave.setStatus('mandatory')
garpTimerAttributeLeaveAll = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: garpTimerAttributeLeaveAll.setStatus('mandatory')
garpAttributeTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 4), )
if mibBuilder.loadTexts: garpAttributeTable.setStatus('mandatory')
garpAttributeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 4, 1), ).setIndexNames((0, "GARP-MIB", "garpAttributeAppType"), (0, "GARP-MIB", "garpAttributePort"), (0, "GARP-MIB", "garpAttributeValue"), (0, "GARP-MIB", "garpAttributeGIPContextID"))
if mibBuilder.loadTexts: garpAttributeEntry.setStatus('mandatory')
garpAttributeAppType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: garpAttributeAppType.setStatus('mandatory')
garpAttributePort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: garpAttributePort.setStatus('mandatory')
garpAttributeValue = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 4, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: garpAttributeValue.setStatus('mandatory')
garpAttributeGIPContextID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: garpAttributeGIPContextID.setStatus('mandatory')
garpAttributeType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: garpAttributeType.setStatus('mandatory')
garpAttributeProtoAdminCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normal-Participan", 0), ("non-Participan", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: garpAttributeProtoAdminCtrl.setStatus('mandatory')
garpAttributeRegisControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("garpRegistrarNormal", 0), ("garpRegistrarFixed", 1), ("garpRegistrarForbidden", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: garpAttributeRegisControl.setStatus('mandatory')
garpAttributeStateValue = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))).clone(namedValues=NamedValues(("va-mt", 0), ("va-lv", 1), ("vp-mt", 2), ("vp-lv", 3), ("vo-mt", 4), ("vo-lv", 5), ("va-in", 6), ("vp-in", 7), ("vo-in", 8), ("aa-mt", 9), ("aa-lv", 10), ("aa-in", 11), ("ap-in", 12), ("ao-in", 13), ("qa-mt", 14), ("qa-lv", 15), ("qa-in", 16), ("qp-in", 17), ("qo-in", 18), ("la-mt", 19), ("la-lv", 20), ("lo-mt", 21), ("lo-lv", 22), ("la-in", 23)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: garpAttributeStateValue.setStatus('mandatory')
garpAttributeOrigOfLastPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2, 4, 1, 9), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: garpAttributeOrigOfLastPDU.setStatus('optional')
mibBuilder.exportSymbols("GARP-MIB", garpApplicationAppType=garpApplicationAppType, garpAttributeTable=garpAttributeTable, garpTimerTable=garpTimerTable, ctVLANMgr=ctVLANMgr, cabletron=cabletron, garpTimerEntry=garpTimerEntry, garpPortOperationTable=garpPortOperationTable, garpAttributeGIPContextID=garpAttributeGIPContextID, garpAttributeRegisControl=garpAttributeRegisControl, garpAttributeValue=garpAttributeValue, mibs=mibs, garpApplicationTable=garpApplicationTable, garpTimerAttributeJoin=garpTimerAttributeJoin, garpAttributeEntry=garpAttributeEntry, garpAttributeAppType=garpAttributeAppType, garpPortOperationAppType=garpPortOperationAppType, ctronExp=ctronExp, garpPortOperationEntry=garpPortOperationEntry, garpAttributeProtoAdminCtrl=garpAttributeProtoAdminCtrl, garpApplicationFailedRegistrations=garpApplicationFailedRegistrations, ctGarpTables=ctGarpTables, garpTimerAttributeLeaveAll=garpTimerAttributeLeaveAll, garpPortOperationStatus=garpPortOperationStatus, garpAttributePort=garpAttributePort, garpApplicationName=garpApplicationName, garpAttributeType=garpAttributeType, garpApplicationEntry=garpApplicationEntry, garpTimerAttributeLeave=garpTimerAttributeLeave, garpPortOperationPort=garpPortOperationPort, ctVLANMib=ctVLANMib, garpAttributeOrigOfLastPDU=garpAttributeOrigOfLastPDU, garpTimerAttributeAppType=garpTimerAttributeAppType, garpAttributeStateValue=garpAttributeStateValue, ctGarp=ctGarp, garpTimerAttributePort=garpTimerAttributePort, garpApplicationOperationStatus=garpApplicationOperationStatus)