#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-VirtualRouterMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-VirtualRouterMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:19:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
DisplayString, RowPointer, RowStatus, Counter32, Gauge32, InterfaceIndex, StorageType, Integer32, Unsigned32 = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "DisplayString", "RowPointer", "RowStatus", "Counter32", "Gauge32", "InterfaceIndex", "StorageType", "Integer32", "Unsigned32")
AsciiString, HexString, AsciiStringIndex, NonReplicated, Link, IntegerSequence = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", "AsciiString", "HexString", "AsciiStringIndex", "NonReplicated", "Link", "IntegerSequence")
mscPassportMIBs, mscComponents = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs", "mscComponents")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, iso, IpAddress, Counter32, Gauge32, ModuleIdentity, Counter64, TimeTicks, Unsigned32, MibIdentifier, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "IpAddress", "Counter32", "Gauge32", "ModuleIdentity", "Counter64", "TimeTicks", "Unsigned32", "MibIdentifier", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
virtualRouterMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 26))
mscVr = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100))
mscVrRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 1), )
if mibBuilder.loadTexts: mscVrRowStatusTable.setStatus('mandatory')
mscVrRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"))
if mibBuilder.loadTexts: mscVrRowStatusEntry.setStatus('mandatory')
mscVrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVrRowStatus.setStatus('mandatory')
mscVrComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrComponentName.setStatus('mandatory')
mscVrStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrStorageType.setStatus('mandatory')
mscVrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 1, 1, 10), AsciiStringIndex().subtype(subtypeSpec=ValueSizeConstraint(1, 8)))
if mibBuilder.loadTexts: mscVrIndex.setStatus('mandatory')
mscVrAdminContorlTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 100), )
if mibBuilder.loadTexts: mscVrAdminContorlTable.setStatus('mandatory')
mscVrAdminContorlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 100, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"))
if mibBuilder.loadTexts: mscVrAdminContorlEntry.setStatus('mandatory')
mscVrSnmpAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 100, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVrSnmpAdminStatus.setStatus('mandatory')
mscVrManagementAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 100, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVrManagementAccess.setStatus('mandatory')
mscVrVirtualPrivateIntranetIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 100, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVrVirtualPrivateIntranetIdentifier.setStatus('mandatory')
mscVrVpnMode = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 100, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("customer", 0), ("carrier", 1))).clone('customer')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVrVpnMode.setStatus('mandatory')
mscVrCidDataTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 101), )
if mibBuilder.loadTexts: mscVrCidDataTable.setStatus('mandatory')
mscVrCidDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 101, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"))
if mibBuilder.loadTexts: mscVrCidDataEntry.setStatus('mandatory')
mscVrCustomerIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 101, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8191), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVrCustomerIdentifier.setStatus('mandatory')
mscVrOperStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 103), )
if mibBuilder.loadTexts: mscVrOperStatusTable.setStatus('mandatory')
mscVrOperStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 103, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"))
if mibBuilder.loadTexts: mscVrOperStatusEntry.setStatus('mandatory')
mscVrSnmpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 103, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrSnmpOperStatus.setStatus('mandatory')
mscVrStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 104), )
if mibBuilder.loadTexts: mscVrStateTable.setStatus('mandatory')
mscVrStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 104, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"))
if mibBuilder.loadTexts: mscVrStateEntry.setStatus('mandatory')
mscVrAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 104, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrAdminState.setStatus('mandatory')
mscVrOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 104, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrOperationalState.setStatus('mandatory')
mscVrUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 104, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrUsageState.setStatus('mandatory')
mscVrIfNumberOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 105), )
if mibBuilder.loadTexts: mscVrIfNumberOperTable.setStatus('mandatory')
mscVrIfNumberOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 105, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"))
if mibBuilder.loadTexts: mscVrIfNumberOperEntry.setStatus('mandatory')
mscVrIfNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 105, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfNumber.setStatus('mandatory')
mscVrMm = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2))
mscVrMmRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 1), )
if mibBuilder.loadTexts: mscVrMmRowStatusTable.setStatus('mandatory')
mscVrMmRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrMmIndex"))
if mibBuilder.loadTexts: mscVrMmRowStatusEntry.setStatus('mandatory')
mscVrMmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrMmRowStatus.setStatus('mandatory')
mscVrMmComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrMmComponentName.setStatus('mandatory')
mscVrMmStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrMmStorageType.setStatus('mandatory')
mscVrMmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscVrMmIndex.setStatus('mandatory')
mscVrMmProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 10), )
if mibBuilder.loadTexts: mscVrMmProvTable.setStatus('mandatory')
mscVrMmProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrMmIndex"))
if mibBuilder.loadTexts: mscVrMmProvEntry.setStatus('mandatory')
mscVrMmVrMaxHeapSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVrMmVrMaxHeapSpace.setStatus('mandatory')
mscVrMmIpMaxHeapSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVrMmIpMaxHeapSpace.setStatus('mandatory')
mscVrMmIpxMaxHeapSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 10, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVrMmIpxMaxHeapSpace.setStatus('mandatory')
mscVrMmBridgingMaxHeapSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 10, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVrMmBridgingMaxHeapSpace.setStatus('mandatory')
mscVrMmNetSentryMaxHeapSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 10, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVrMmNetSentryMaxHeapSpace.setStatus('mandatory')
mscVrMmSresMaxHeapSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 10, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVrMmSresMaxHeapSpace.setStatus('mandatory')
mscVrMmSnaMaxHeapSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 10, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVrMmSnaMaxHeapSpace.setStatus('mandatory')
mscVrMmOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 11), )
if mibBuilder.loadTexts: mscVrMmOperTable.setStatus('mandatory')
mscVrMmOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrMmIndex"))
if mibBuilder.loadTexts: mscVrMmOperEntry.setStatus('mandatory')
mscVrMmVrHeapSpaceBytesAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 11, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrMmVrHeapSpaceBytesAllocated.setStatus('mandatory')
mscVrMmVrHeapSpaceAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 11, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrMmVrHeapSpaceAllocated.setStatus('mandatory')
mscVrMmIpHeapSpaceAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 11, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrMmIpHeapSpaceAllocated.setStatus('mandatory')
mscVrMmIpxHeapSpaceAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 11, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrMmIpxHeapSpaceAllocated.setStatus('mandatory')
mscVrMmBridgingHeapSpaceAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 11, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrMmBridgingHeapSpaceAllocated.setStatus('mandatory')
mscVrMmNetSentryHeapSpaceAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 11, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrMmNetSentryHeapSpaceAllocated.setStatus('mandatory')
mscVrMmSresHeapSpaceAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 11, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrMmSresHeapSpaceAllocated.setStatus('mandatory')
mscVrMmSnaHeapSpaceAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 11, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrMmSnaHeapSpaceAllocated.setStatus('mandatory')
mscVrPp = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3))
mscVrPpRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 1), )
if mibBuilder.loadTexts: mscVrPpRowStatusTable.setStatus('mandatory')
mscVrPpRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"))
if mibBuilder.loadTexts: mscVrPpRowStatusEntry.setStatus('mandatory')
mscVrPpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVrPpRowStatus.setStatus('mandatory')
mscVrPpComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrPpComponentName.setStatus('mandatory')
mscVrPpStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrPpStorageType.setStatus('mandatory')
mscVrPpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 1, 1, 10), AsciiStringIndex().subtype(subtypeSpec=ValueSizeConstraint(1, 20)))
if mibBuilder.loadTexts: mscVrPpIndex.setStatus('mandatory')
mscVrPpAdminControlTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 100), )
if mibBuilder.loadTexts: mscVrPpAdminControlTable.setStatus('mandatory')
mscVrPpAdminControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 100, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"))
if mibBuilder.loadTexts: mscVrPpAdminControlEntry.setStatus('mandatory')
mscVrPpSnmpAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 100, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVrPpSnmpAdminStatus.setStatus('mandatory')
mscVrPpProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 101), )
if mibBuilder.loadTexts: mscVrPpProvTable.setStatus('mandatory')
mscVrPpProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 101, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"))
if mibBuilder.loadTexts: mscVrPpProvEntry.setStatus('mandatory')
mscVrPpLinkToMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 101, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVrPpLinkToMedia.setStatus('mandatory')
mscVrPpOperStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 102), )
if mibBuilder.loadTexts: mscVrPpOperStatusTable.setStatus('mandatory')
mscVrPpOperStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 102, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"))
if mibBuilder.loadTexts: mscVrPpOperStatusEntry.setStatus('mandatory')
mscVrPpSnmpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 102, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrPpSnmpOperStatus.setStatus('mandatory')
mscVrPpStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 103), )
if mibBuilder.loadTexts: mscVrPpStateTable.setStatus('mandatory')
mscVrPpStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 103, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"))
if mibBuilder.loadTexts: mscVrPpStateEntry.setStatus('mandatory')
mscVrPpAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 103, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrPpAdminState.setStatus('mandatory')
mscVrPpOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 103, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrPpOperationalState.setStatus('mandatory')
mscVrPpUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 103, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrPpUsageState.setStatus('mandatory')
mscVrPpOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 104), )
if mibBuilder.loadTexts: mscVrPpOperTable.setStatus('mandatory')
mscVrPpOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 104, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"))
if mibBuilder.loadTexts: mscVrPpOperEntry.setStatus('mandatory')
mscVrPpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 104, 1, 1), InterfaceIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrPpIfIndex.setStatus('mandatory')
mscVrPpNbmaAddressTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 105), )
if mibBuilder.loadTexts: mscVrPpNbmaAddressTable.setStatus('mandatory')
mscVrPpNbmaAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 105, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"))
if mibBuilder.loadTexts: mscVrPpNbmaAddressEntry.setStatus('mandatory')
mscVrPpAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 105, 1, 1), HexString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrPpAtmAddress.setStatus('mandatory')
mscVrIfTableEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10))
mscVrIfTableEntryRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 1), )
if mibBuilder.loadTexts: mscVrIfTableEntryRowStatusTable.setStatus('mandatory')
mscVrIfTableEntryRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIfTableEntryIndex"))
if mibBuilder.loadTexts: mscVrIfTableEntryRowStatusEntry.setStatus('mandatory')
mscVrIfTableEntryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryRowStatus.setStatus('mandatory')
mscVrIfTableEntryComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryComponentName.setStatus('mandatory')
mscVrIfTableEntryStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryStorageType.setStatus('mandatory')
mscVrIfTableEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: mscVrIfTableEntryIndex.setStatus('mandatory')
mscVrIfTableEntryIftTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10), )
if mibBuilder.loadTexts: mscVrIfTableEntryIftTable.setStatus('mandatory')
mscVrIfTableEntryIftEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIfTableEntryIndex"))
if mibBuilder.loadTexts: mscVrIfTableEntryIftEntry.setStatus('mandatory')
mscVrIfTableEntryIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryIfAdminStatus.setStatus('mandatory')
mscVrIfTableEntryIfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryIfOperStatus.setStatus('mandatory')
mscVrIfTableEntryIfLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryIfLastChange.setStatus('mandatory')
mscVrIfTableEntryIfInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryIfInOctets.setStatus('mandatory')
mscVrIfTableEntryIfOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryIfOutOctets.setStatus('mandatory')
mscVrIfTableEntryIfInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryIfInDiscards.setStatus('mandatory')
mscVrIfTableEntryIfOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryIfOutDiscards.setStatus('mandatory')
mscVrIfTableEntryIfInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryIfInErrors.setStatus('mandatory')
mscVrIfTableEntryIfOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryIfOutErrors.setStatus('mandatory')
mscVrIfTableEntryIfInUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryIfInUcastPkts.setStatus('mandatory')
mscVrIfTableEntryIfOutUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryIfOutUcastPkts.setStatus('mandatory')
mscVrIfTableEntryIfInNuCastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryIfInNuCastPkts.setStatus('mandatory')
mscVrIfTableEntryIfOutNuCastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryIfOutNuCastPkts.setStatus('mandatory')
mscVrIfTableEntryIfInUnknownProtos = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryIfInUnknownProtos.setStatus('mandatory')
mscVrIfTableEntryIfOutQlength = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 16), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryIfOutQlength.setStatus('mandatory')
mscVrIfTableEntryIfDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 17), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryIfDescription.setStatus('mandatory')
mscVrIfTableEntryIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 30, 31, 32, 44, 45, 46, 59, 60, 64, 1039, 1040, 1041, 1042, 1043))).clone(namedValues=NamedValues(("other", 1), ("ddnX25", 4), ("rfc877x25", 5), ("ethernetCsmacd", 6), ("ethernet8023", 7), ("tokenBus8024", 8), ("tokenring8025", 9), ("man802", 10), ("starLan", 11), ("hyperChannel", 14), ("fddi", 15), ("lapb", 16), ("sdlc", 17), ("ds1", 18), ("e1", 19), ("basicIsdn", 20), ("primaryIsdn", 21), ("propPointToPointSerial", 22), ("ppp", 23), ("ds3", 30), ("smds", 31), ("frameRelay", 32), ("frameRelayService", 44), ("v35", 45), ("hssi", 46), ("aflane8023", 59), ("aflane8025", 60), ("v11", 64), ("atmMpeVcEncap", 1039), ("atmMpeLlcEncap", 1040), ("ilsForwarder", 1041), ("ipTunnel", 1042), ("virtualMedia", 1043)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryIfType.setStatus('mandatory')
mscVrIfTableEntryIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 19), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryIfMtu.setStatus('mandatory')
mscVrIfTableEntryIfSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 20), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryIfSpeed.setStatus('mandatory')
mscVrIfTableEntryIfPhysicalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 21), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryIfPhysicalAddress.setStatus('mandatory')
mscVrIfTableEntryIfSpecific = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 22), IntegerSequence()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryIfSpecific.setStatus('mandatory')
mscVrIfTableEntryAdditionalInfoTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 11), )
if mibBuilder.loadTexts: mscVrIfTableEntryAdditionalInfoTable.setStatus('mandatory')
mscVrIfTableEntryAdditionalInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIfTableEntryIndex"))
if mibBuilder.loadTexts: mscVrIfTableEntryAdditionalInfoEntry.setStatus('mandatory')
mscVrIfTableEntryStdComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 11, 1, 1), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrIfTableEntryStdComponentName.setStatus('mandatory')
mscVrQosP = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15))
mscVrQosPRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15, 1), )
if mibBuilder.loadTexts: mscVrQosPRowStatusTable.setStatus('mandatory')
mscVrQosPRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrQosPIndex"))
if mibBuilder.loadTexts: mscVrQosPRowStatusEntry.setStatus('mandatory')
mscVrQosPRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVrQosPRowStatus.setStatus('mandatory')
mscVrQosPComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrQosPComponentName.setStatus('mandatory')
mscVrQosPStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVrQosPStorageType.setStatus('mandatory')
mscVrQosPIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3)))
if mibBuilder.loadTexts: mscVrQosPIndex.setStatus('mandatory')
mscVrQosPProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15, 10), )
if mibBuilder.loadTexts: mscVrQosPProvTable.setStatus('mandatory')
mscVrQosPProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrQosPIndex"))
if mibBuilder.loadTexts: mscVrQosPProvEntry.setStatus('mandatory')
mscVrQosPVnsDiscardPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVrQosPVnsDiscardPriority.setStatus('mandatory')
mscVrQosPVnsEmissionPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVrQosPVnsEmissionPriority.setStatus('mandatory')
mscVrQosPWanEmissionPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15, 10, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVrQosPWanEmissionPriority.setStatus('mandatory')
virtualRouterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 26, 1))
virtualRouterGroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 26, 1, 1))
virtualRouterGroupCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 26, 1, 1, 3))
virtualRouterGroupCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 26, 1, 1, 3, 2))
virtualRouterCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 26, 3))
virtualRouterCapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 26, 3, 1))
virtualRouterCapabilitiesCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 26, 3, 1, 3))
virtualRouterCapabilitiesCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 26, 3, 1, 3, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-VirtualRouterMIB", mscVrCustomerIdentifier=mscVrCustomerIdentifier, mscVrIfNumberOperEntry=mscVrIfNumberOperEntry, mscVrAdminState=mscVrAdminState, mscVrRowStatusEntry=mscVrRowStatusEntry, mscVrPpRowStatusTable=mscVrPpRowStatusTable, mscVrComponentName=mscVrComponentName, mscVrPpRowStatus=mscVrPpRowStatus, mscVrIfNumber=mscVrIfNumber, mscVrPpStateEntry=mscVrPpStateEntry, virtualRouterCapabilitiesCA02=virtualRouterCapabilitiesCA02, mscVrMmBridgingMaxHeapSpace=mscVrMmBridgingMaxHeapSpace, mscVrQosPVnsEmissionPriority=mscVrQosPVnsEmissionPriority, mscVrMmProvTable=mscVrMmProvTable, mscVrIfTableEntryIfOutQlength=mscVrIfTableEntryIfOutQlength, mscVrPpLinkToMedia=mscVrPpLinkToMedia, mscVrPpAdminState=mscVrPpAdminState, mscVrRowStatusTable=mscVrRowStatusTable, virtualRouterGroupCA02A=virtualRouterGroupCA02A, mscVrMmStorageType=mscVrMmStorageType, mscVrOperStatusEntry=mscVrOperStatusEntry, mscVrMmNetSentryMaxHeapSpace=mscVrMmNetSentryMaxHeapSpace, mscVrMmComponentName=mscVrMmComponentName, mscVrIfTableEntryIftEntry=mscVrIfTableEntryIftEntry, mscVrIfTableEntryIfDescription=mscVrIfTableEntryIfDescription, mscVrRowStatus=mscVrRowStatus, mscVrIfTableEntryIfOutErrors=mscVrIfTableEntryIfOutErrors, mscVrPpOperationalState=mscVrPpOperationalState, mscVrIfTableEntryIndex=mscVrIfTableEntryIndex, mscVrPpProvEntry=mscVrPpProvEntry, mscVrIfTableEntryStorageType=mscVrIfTableEntryStorageType, mscVrIfTableEntryAdditionalInfoTable=mscVrIfTableEntryAdditionalInfoTable, mscVrMmSnaMaxHeapSpace=mscVrMmSnaMaxHeapSpace, mscVrStateEntry=mscVrStateEntry, virtualRouterGroup=virtualRouterGroup, mscVrOperStatusTable=mscVrOperStatusTable, mscVrPpOperTable=mscVrPpOperTable, mscVrIfTableEntryIfPhysicalAddress=mscVrIfTableEntryIfPhysicalAddress, mscVrPpNbmaAddressTable=mscVrPpNbmaAddressTable, mscVrMmIpMaxHeapSpace=mscVrMmIpMaxHeapSpace, mscVrCidDataEntry=mscVrCidDataEntry, mscVrPpStateTable=mscVrPpStateTable, virtualRouterMIB=virtualRouterMIB, mscVrQosPVnsDiscardPriority=mscVrQosPVnsDiscardPriority, mscVrIfTableEntryIfOutNuCastPkts=mscVrIfTableEntryIfOutNuCastPkts, mscVrIfTableEntryStdComponentName=mscVrIfTableEntryStdComponentName, mscVrIfTableEntryIfOutDiscards=mscVrIfTableEntryIfOutDiscards, virtualRouterCapabilitiesCA=virtualRouterCapabilitiesCA, mscVrPpOperStatusTable=mscVrPpOperStatusTable, mscVrQosPProvEntry=mscVrQosPProvEntry, mscVrQosPWanEmissionPriority=mscVrQosPWanEmissionPriority, mscVrMmVrHeapSpaceBytesAllocated=mscVrMmVrHeapSpaceBytesAllocated, mscVrQosPIndex=mscVrQosPIndex, mscVr=mscVr, mscVrCidDataTable=mscVrCidDataTable, mscVrAdminContorlTable=mscVrAdminContorlTable, mscVrIfTableEntryIfInNuCastPkts=mscVrIfTableEntryIfInNuCastPkts, mscVrManagementAccess=mscVrManagementAccess, mscVrIfTableEntryRowStatusEntry=mscVrIfTableEntryRowStatusEntry, mscVrIfTableEntryIfMtu=mscVrIfTableEntryIfMtu, mscVrPpAdminControlTable=mscVrPpAdminControlTable, mscVrMmProvEntry=mscVrMmProvEntry, mscVrIfTableEntryIfSpeed=mscVrIfTableEntryIfSpeed, mscVrMmOperTable=mscVrMmOperTable, mscVrIndex=mscVrIndex, mscVrMmSresHeapSpaceAllocated=mscVrMmSresHeapSpaceAllocated, mscVrMmOperEntry=mscVrMmOperEntry, mscVrPpRowStatusEntry=mscVrPpRowStatusEntry, mscVrIfNumberOperTable=mscVrIfNumberOperTable, mscVrIfTableEntryIfOutOctets=mscVrIfTableEntryIfOutOctets, mscVrPpIfIndex=mscVrPpIfIndex, mscVrPpOperEntry=mscVrPpOperEntry, mscVrMmVrMaxHeapSpace=mscVrMmVrMaxHeapSpace, mscVrStateTable=mscVrStateTable, mscVrMmNetSentryHeapSpaceAllocated=mscVrMmNetSentryHeapSpaceAllocated, mscVrIfTableEntryIfAdminStatus=mscVrIfTableEntryIfAdminStatus, mscVrMmIpxHeapSpaceAllocated=mscVrMmIpxHeapSpaceAllocated, mscVrIfTableEntryIfInDiscards=mscVrIfTableEntryIfInDiscards, mscVrPpOperStatusEntry=mscVrPpOperStatusEntry, mscVrQosPProvTable=mscVrQosPProvTable, virtualRouterGroupCA=virtualRouterGroupCA, virtualRouterCapabilitiesCA02A=virtualRouterCapabilitiesCA02A, mscVrMmVrHeapSpaceAllocated=mscVrMmVrHeapSpaceAllocated, mscVrPpNbmaAddressEntry=mscVrPpNbmaAddressEntry, mscVrVpnMode=mscVrVpnMode, mscVrPpSnmpAdminStatus=mscVrPpSnmpAdminStatus, mscVrAdminContorlEntry=mscVrAdminContorlEntry, mscVrQosPStorageType=mscVrQosPStorageType, mscVrStorageType=mscVrStorageType, mscVrMmIpxMaxHeapSpace=mscVrMmIpxMaxHeapSpace, mscVrMmBridgingHeapSpaceAllocated=mscVrMmBridgingHeapSpaceAllocated, mscVrIfTableEntryIfInUcastPkts=mscVrIfTableEntryIfInUcastPkts, mscVrPpIndex=mscVrPpIndex, mscVrIfTableEntryIfInUnknownProtos=mscVrIfTableEntryIfInUnknownProtos, mscVrPpComponentName=mscVrPpComponentName, virtualRouterCapabilities=virtualRouterCapabilities, mscVrIfTableEntryAdditionalInfoEntry=mscVrIfTableEntryAdditionalInfoEntry, mscVrMmRowStatus=mscVrMmRowStatus, mscVrIfTableEntryIfOperStatus=mscVrIfTableEntryIfOperStatus, mscVrMmSresMaxHeapSpace=mscVrMmSresMaxHeapSpace, mscVrQosPRowStatusTable=mscVrQosPRowStatusTable, mscVrMm=mscVrMm, mscVrMmIpHeapSpaceAllocated=mscVrMmIpHeapSpaceAllocated, mscVrMmRowStatusTable=mscVrMmRowStatusTable, mscVrQosPRowStatus=mscVrQosPRowStatus, mscVrPpUsageState=mscVrPpUsageState, mscVrIfTableEntryIfSpecific=mscVrIfTableEntryIfSpecific, mscVrQosP=mscVrQosP, mscVrQosPRowStatusEntry=mscVrQosPRowStatusEntry, mscVrSnmpOperStatus=mscVrSnmpOperStatus, mscVrIfTableEntryRowStatus=mscVrIfTableEntryRowStatus, mscVrIfTableEntryIfOutUcastPkts=mscVrIfTableEntryIfOutUcastPkts, mscVrMmSnaHeapSpaceAllocated=mscVrMmSnaHeapSpaceAllocated, mscVrPpAdminControlEntry=mscVrPpAdminControlEntry, mscVrPpAtmAddress=mscVrPpAtmAddress, mscVrSnmpAdminStatus=mscVrSnmpAdminStatus, mscVrIfTableEntryComponentName=mscVrIfTableEntryComponentName, virtualRouterGroupCA02=virtualRouterGroupCA02, mscVrIfTableEntryIfType=mscVrIfTableEntryIfType, mscVrPpProvTable=mscVrPpProvTable, mscVrIfTableEntryIfInErrors=mscVrIfTableEntryIfInErrors, mscVrPpSnmpOperStatus=mscVrPpSnmpOperStatus, mscVrPp=mscVrPp, mscVrIfTableEntryIftTable=mscVrIfTableEntryIftTable, mscVrQosPComponentName=mscVrQosPComponentName, mscVrIfTableEntryRowStatusTable=mscVrIfTableEntryRowStatusTable, mscVrIfTableEntry=mscVrIfTableEntry, mscVrIfTableEntryIfLastChange=mscVrIfTableEntryIfLastChange, mscVrVirtualPrivateIntranetIdentifier=mscVrVirtualPrivateIntranetIdentifier, mscVrIfTableEntryIfInOctets=mscVrIfTableEntryIfInOctets, mscVrMmIndex=mscVrMmIndex, mscVrOperationalState=mscVrOperationalState, mscVrUsageState=mscVrUsageState, mscVrPpStorageType=mscVrPpStorageType, mscVrMmRowStatusEntry=mscVrMmRowStatusEntry)