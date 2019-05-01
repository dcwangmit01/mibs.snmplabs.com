#
# PySNMP MIB module ADTRAN-ATLAS-BRI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADTRAN-ATLAS-BRI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:14:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ModuleIdentity, enterprises, NotificationType, TimeTicks, Bits, ObjectIdentity, iso, Counter32, Integer32, IpAddress, Counter64, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "enterprises", "NotificationType", "TimeTicks", "Bits", "ObjectIdentity", "iso", "Counter32", "Integer32", "IpAddress", "Counter64", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adtran = MibIdentifier((1, 3, 6, 1, 4, 1, 664))
adMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2))
adATLASmg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154))
adGenATLASmg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154, 1))
adATLASBRImg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8))
adATLASBRIIfNumber = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASBRIIfNumber.setStatus('mandatory')
if mibBuilder.loadTexts: adATLASBRIIfNumber.setDescription('The number of BRI ports (regardless of their current state) present on this system.')
adATLASBRIIfTable = MibTable((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 2), )
if mibBuilder.loadTexts: adATLASBRIIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: adATLASBRIIfTable.setDescription('The ATLAS BRI Interface Status Table.')
adATLASBRIIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 2, 1), ).setIndexNames((0, "ADTRAN-ATLAS-BRI-MIB", "adATLASBRIIfIndex"))
if mibBuilder.loadTexts: adATLASBRIIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: adATLASBRIIfEntry.setDescription('An entry in the ATLAS BRI Interface Status Table')
adATLASBRIIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASBRIIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: adATLASBRIIfIndex.setDescription('This variable indicates the interface number of a particular BRI port within the ATLAS product. This number will be the same as the ifIndex located in the MIB-II interface table.')
adATLASBRIIfSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASBRIIfSlotNum.setStatus('mandatory')
if mibBuilder.loadTexts: adATLASBRIIfSlotNum.setDescription('This variable indicates the slot number of a particular ATLAS module with a BRI interface.')
adATLASBRIIfPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASBRIIfPortNum.setStatus('mandatory')
if mibBuilder.loadTexts: adATLASBRIIfPortNum.setDescription('This variable indicates the port number of a particular BRI interface on an ATLAS module.')
adATLASBRIIfAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("layer1up", 1), ("layer1down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASBRIIfAlarmStatus.setStatus('mandatory')
if mibBuilder.loadTexts: adATLASBRIIfAlarmStatus.setDescription('This variable shows whether Layer 1 is up or down. It has a value of 1 for up and 2 for down.')
adATLASBRIIfChanStatTable = MibTable((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 3), )
if mibBuilder.loadTexts: adATLASBRIIfChanStatTable.setStatus('mandatory')
if mibBuilder.loadTexts: adATLASBRIIfChanStatTable.setDescription('The ATLAS BRI Interface Channel Status Table.')
adATLASBRIIfChanStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 3, 1), ).setIndexNames((0, "ADTRAN-ATLAS-BRI-MIB", "adATLASBRIIfChanStatIndex"))
if mibBuilder.loadTexts: adATLASBRIIfChanStatEntry.setStatus('mandatory')
if mibBuilder.loadTexts: adATLASBRIIfChanStatEntry.setDescription('An entry in the ATLAS BRI Interface Channel Status Table.')
adATLASBRIIfChanStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASBRIIfChanStatIndex.setStatus('mandatory')
if mibBuilder.loadTexts: adATLASBRIIfChanStatIndex.setDescription('This variable indicates the Interface number of a particular BRI port within the ATLAS product. This number will be the same as the ifIndex located in the MIB-II interface table.')
adATLASBRIIfChanStatB1 = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unallocated", 1), ("active", 2), ("inactive", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASBRIIfChanStatB1.setStatus('mandatory')
if mibBuilder.loadTexts: adATLASBRIIfChanStatB1.setDescription('This Variable shows the status of the first B channel. It has a value of 1 for unallocated, 2 for active, and 3 for inactive.')
adATLASBRIIfChanStatB2 = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unallocated", 1), ("active", 2), ("inactive", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASBRIIfChanStatB2.setStatus('mandatory')
if mibBuilder.loadTexts: adATLASBRIIfChanStatB2.setDescription('This Variable shows the status of the second B channel. It has a value of 1 for unallocated, 2 for active, and 3 for inactive.')
adATLASBRIIfChanStatD = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unallocated", 1), ("allocated", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASBRIIfChanStatD.setStatus('mandatory')
if mibBuilder.loadTexts: adATLASBRIIfChanStatD.setDescription('This Variable shows the status of the D channel. It has a value of 1 for unallocated and 2 for allocated.')
adATLASBRITstTable = MibTable((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 4), )
if mibBuilder.loadTexts: adATLASBRITstTable.setStatus('mandatory')
if mibBuilder.loadTexts: adATLASBRITstTable.setDescription('The ATLAS BRI Interface Test Table.')
adATLASBRITstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 4, 1), ).setIndexNames((0, "ADTRAN-ATLAS-BRI-MIB", "adATLASBRITstIndex"))
if mibBuilder.loadTexts: adATLASBRITstEntry.setStatus('mandatory')
if mibBuilder.loadTexts: adATLASBRITstEntry.setDescription('An entry in the ATLAS BRI Interface Test Table.')
adATLASBRITstIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASBRITstIndex.setStatus('mandatory')
if mibBuilder.loadTexts: adATLASBRITstIndex.setDescription('This variable indicates the Interface number of a particular BRI port within the ATLAS product. This number will be the same as the ifIndex located in the MIB-II interface table.')
adATLASBRITstLLB = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("lpBkB1", 2), ("lpBkB2", 3), ("lpBkB1B2", 4), ("lpBkAll", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adATLASBRITstLLB.setStatus('mandatory')
if mibBuilder.loadTexts: adATLASBRITstLLB.setDescription('This variable allows different channels to be looped back. 1: None 2: B1 3: B2 4: B1&B2 5: All Channels')
mibBuilder.exportSymbols("ADTRAN-ATLAS-BRI-MIB", adtran=adtran, adATLASBRIIfNumber=adATLASBRIIfNumber, adATLASBRITstEntry=adATLASBRITstEntry, adATLASBRITstLLB=adATLASBRITstLLB, adATLASBRIIfAlarmStatus=adATLASBRIIfAlarmStatus, adMgmt=adMgmt, adATLASBRIIfPortNum=adATLASBRIIfPortNum, adGenATLASmg=adGenATLASmg, adATLASBRIIfChanStatB1=adATLASBRIIfChanStatB1, adATLASBRITstTable=adATLASBRITstTable, adATLASBRIIfChanStatD=adATLASBRIIfChanStatD, adATLASBRIIfChanStatTable=adATLASBRIIfChanStatTable, adATLASBRIIfIndex=adATLASBRIIfIndex, adATLASBRIIfChanStatIndex=adATLASBRIIfChanStatIndex, adATLASBRIIfEntry=adATLASBRIIfEntry, adATLASBRIIfTable=adATLASBRIIfTable, adATLASBRITstIndex=adATLASBRITstIndex, adATLASBRIIfChanStatB2=adATLASBRIIfChanStatB2, adATLASmg=adATLASmg, adATLASBRImg=adATLASBRImg, adATLASBRIIfChanStatEntry=adATLASBRIIfChanStatEntry, adATLASBRIIfSlotNum=adATLASBRIIfSlotNum)