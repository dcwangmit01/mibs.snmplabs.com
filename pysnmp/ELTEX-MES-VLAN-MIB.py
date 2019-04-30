#
# PySNMP MIB module ELTEX-MES-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-VLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:47:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
VlanIndex, PortList, dot1qVlanIndex = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex", "PortList", "dot1qVlanIndex")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
vlanMulticastTvEntry, = mibBuilder.importSymbols("RADLAN-vlan-MIB", "vlanMulticastTvEntry")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ModuleIdentity, Gauge32, Counter64, TimeTicks, ObjectIdentity, Integer32, Unsigned32, iso, Bits, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "Gauge32", "Counter64", "TimeTicks", "ObjectIdentity", "Integer32", "Unsigned32", "iso", "Bits", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
DisplayString, MacAddress, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TruthValue", "TextualConvention")
eltMesVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 5))
eltMesVlan.setRevisions(('2013-11-18 00:00', '2013-11-18 00:00',))
if mibBuilder.loadTexts: eltMesVlan.setLastUpdated('201311180000Z')
if mibBuilder.loadTexts: eltMesVlan.setOrganization('Eltex Ltd.')
class EltVlanMode(TextualConvention, Integer32):
    reference = 'TR-101'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("basic", 1), ("tr101", 2))

eltVlanMulticastTvTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 1), )
if mibBuilder.loadTexts: eltVlanMulticastTvTable.setStatus('current')
eltVlanMulticastTvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 1, 1), )
vlanMulticastTvEntry.registerAugmentions(("ELTEX-MES-VLAN-MIB", "eltVlanMulticastTvEntry"))
eltVlanMulticastTvEntry.setIndexNames(*vlanMulticastTvEntry.getIndexNames())
if mibBuilder.loadTexts: eltVlanMulticastTvEntry.setStatus('current')
eltVlanMulticastTvVIDIsTagged = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltVlanMulticastTvVIDIsTagged.setStatus('current')
eltVlanMode = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 2), EltVlanMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltVlanMode.setStatus('current')
eltdot1qPortVlanCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 3), )
if mibBuilder.loadTexts: eltdot1qPortVlanCurrentTable.setStatus('current')
eltdot1qPortVlanCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: eltdot1qPortVlanCurrentEntry.setStatus('current')
eltdot1qPortVlanCurrentEgressList1to1024 = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltdot1qPortVlanCurrentEgressList1to1024.setStatus('current')
eltdot1qPortVlanCurrentEgressList1025to2048 = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltdot1qPortVlanCurrentEgressList1025to2048.setStatus('current')
eltdot1qPortVlanCurrentEgressList2049to3072 = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltdot1qPortVlanCurrentEgressList2049to3072.setStatus('current')
eltdot1qPortVlanCurrentEgressList3073to4094 = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltdot1qPortVlanCurrentEgressList3073to4094.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-VLAN-MIB", EltVlanMode=EltVlanMode, eltdot1qPortVlanCurrentEntry=eltdot1qPortVlanCurrentEntry, eltMesVlan=eltMesVlan, eltVlanMulticastTvEntry=eltVlanMulticastTvEntry, eltdot1qPortVlanCurrentEgressList3073to4094=eltdot1qPortVlanCurrentEgressList3073to4094, eltVlanMulticastTvVIDIsTagged=eltVlanMulticastTvVIDIsTagged, eltdot1qPortVlanCurrentEgressList2049to3072=eltdot1qPortVlanCurrentEgressList2049to3072, eltdot1qPortVlanCurrentEgressList1to1024=eltdot1qPortVlanCurrentEgressList1to1024, eltVlanMulticastTvTable=eltVlanMulticastTvTable, eltVlanMode=eltVlanMode, PYSNMP_MODULE_ID=eltMesVlan, eltdot1qPortVlanCurrentEgressList1025to2048=eltdot1qPortVlanCurrentEgressList1025to2048, eltdot1qPortVlanCurrentTable=eltdot1qPortVlanCurrentTable)