#
# PySNMP MIB module ALCATEL-IND1-DOT1Q-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-DOT1Q-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:17:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1Dot1Q, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1Dot1Q")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
enterprises, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, NotificationType, iso, Counter32, ModuleIdentity, Gauge32, IpAddress, Counter64, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "NotificationType", "iso", "Counter32", "ModuleIdentity", "Gauge32", "IpAddress", "Counter64", "Integer32", "ObjectIdentity")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
alcatelIND1Dot1QMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1))
alcatelIND1Dot1QMIB.setRevisions(('2007-04-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alcatelIND1Dot1QMIB.setRevisionsDescriptions(('Addressing discrepancies with Alcatel Standard.',))
if mibBuilder.loadTexts: alcatelIND1Dot1QMIB.setLastUpdated('200704030000Z')
if mibBuilder.loadTexts: alcatelIND1Dot1QMIB.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: alcatelIND1Dot1QMIB.setContactInfo('Please consult with Customer Service to ensure the most appropriate version of this document is used with the products in question: Alcatel-Lucent, Enterprise Solutions Division (Formerly Alcatel Internetworking, Incorporated) 26801 West Agoura Road Agoura Hills, CA 91301-5122 United States Of America Telephone: North America +1 800 995 2696 Latin America +1 877 919 9526 Europe +31 23 556 0100 Asia +65 394 7933 All Other +1 818 878 4507 Electronic Mail: support@ind.alcatel.com World Wide Web: http://alcatel-lucent.com/wps/portal/enterprise File Transfer Protocol: ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1Dot1QMIB.setDescription('This module describes an authoritative enterprise-specific Simple Network Management Protocol (SNMP) Management Information Base (MIB): For the Birds Of Prey Product Line 802.1q for vlan assignment to slot/port and aggregates The right to make changes in specification and other information contained in this document without prior notice is reserved. No liability shall be assumed for any incidental, indirect, special, or consequential damages whatsoever arising from or related to this document or the information contained herein. Vendors, end-users, and other interested parties are granted non-exclusive license to use this specification in connection with management of the products for which it is intended to be used. Copyright (C) 1995-2007 Alcatel-Lucent ALL RIGHTS RESERVED WORLDWIDE')
alcatelIND1Dot1QMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1))
if mibBuilder.loadTexts: alcatelIND1Dot1QMIBObjects.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1Dot1QMIBObjects.setDescription('Branch For 802.1Q Subsystem Managed Objects.')
alcatelIND1Dot1QMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 2))
if mibBuilder.loadTexts: alcatelIND1Dot1QMIBConformance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1Dot1QMIBConformance.setDescription('Branch For 802.1Q Subsystem Conformance Information.')
alcatelIND1Dot1QMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1Dot1QMIBGroups.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1Dot1QMIBGroups.setDescription('Branch For 802.1Q Subsystem Units Of Conformance.')
alcatelIND1Dot1QMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1Dot1QMIBCompliances.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1Dot1QMIBCompliances.setDescription('Branch For 802.1Q Subsystem Compliance Statements.')
v8021Q = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1))
qPortVlanTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 1), )
if mibBuilder.loadTexts: qPortVlanTable.setStatus('current')
if mibBuilder.loadTexts: qPortVlanTable.setDescription('This table lists the 802.1q vlans on a port.')
qPortVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-DOT1Q-MIB", "qPortVlanSlot"), (0, "ALCATEL-IND1-DOT1Q-MIB", "qPortVlanPort"), (0, "ALCATEL-IND1-DOT1Q-MIB", "qPortVlanTagValue"))
if mibBuilder.loadTexts: qPortVlanEntry.setStatus('current')
if mibBuilder.loadTexts: qPortVlanEntry.setDescription('An entry in 802.1q port vlan table.')
qPortVlanSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qPortVlanSlot.setStatus('current')
if mibBuilder.loadTexts: qPortVlanSlot.setDescription('The slot id of the required port.')
qPortVlanPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qPortVlanPort.setStatus('current')
if mibBuilder.loadTexts: qPortVlanPort.setDescription('The physical port number.')
qPortVlanTagValue = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qPortVlanTagValue.setStatus('current')
if mibBuilder.loadTexts: qPortVlanTagValue.setDescription('Tag for a particular port')
qPortVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qPortVlanStatus.setStatus('current')
if mibBuilder.loadTexts: qPortVlanStatus.setDescription('Row Status for creating/deleting rules')
qPortVlanDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qPortVlanDescription.setStatus('current')
if mibBuilder.loadTexts: qPortVlanDescription.setDescription('Textual description of vlan added to a port.')
qPortVlanForceTagInternal = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 1, 0))).clone(namedValues=NamedValues(("na", 2), ("on", 1), ("off", 0))).clone('na')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qPortVlanForceTagInternal.setStatus('current')
if mibBuilder.loadTexts: qPortVlanForceTagInternal.setDescription('0-ON, 1-OFF and 2-NA')
qAggregateVlanTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 2), )
if mibBuilder.loadTexts: qAggregateVlanTable.setStatus('current')
if mibBuilder.loadTexts: qAggregateVlanTable.setDescription('This table lists the 802.1q vlans on a aggregate.')
qAggregateVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 2, 1), ).setIndexNames((0, "ALCATEL-IND1-DOT1Q-MIB", "qAggregateVlanAggregateId"), (0, "ALCATEL-IND1-DOT1Q-MIB", "qAggregateVlanTagValue"))
if mibBuilder.loadTexts: qAggregateVlanEntry.setStatus('current')
if mibBuilder.loadTexts: qAggregateVlanEntry.setDescription('An entry in 802.1q aggregate vlan table.')
qAggregateVlanAggregateId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qAggregateVlanAggregateId.setStatus('current')
if mibBuilder.loadTexts: qAggregateVlanAggregateId.setDescription('The aggreagte id of the aggregate.')
qAggregateVlanTagValue = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qAggregateVlanTagValue.setStatus('current')
if mibBuilder.loadTexts: qAggregateVlanTagValue.setDescription('Tag Value on the particular aggregate.')
qAggregateVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 2, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qAggregateVlanStatus.setStatus('current')
if mibBuilder.loadTexts: qAggregateVlanStatus.setDescription('Row status for creating/deleting rules.')
qAggregateVlanDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qAggregateVlanDescription.setStatus('current')
if mibBuilder.loadTexts: qAggregateVlanDescription.setDescription('Textual description of vlan added to a aggregate.')
qAtmIfIndexVpiVciTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 3), )
if mibBuilder.loadTexts: qAtmIfIndexVpiVciTable.setStatus('current')
if mibBuilder.loadTexts: qAtmIfIndexVpiVciTable.setDescription('This table lists the 802.1q vlans on an ATM port.')
qAtmIfIndexVpiVciEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 3, 1), ).setIndexNames((0, "ALCATEL-IND1-DOT1Q-MIB", "qAtmIfIndex"), (0, "ALCATEL-IND1-DOT1Q-MIB", "qAtmVpiValue"), (0, "ALCATEL-IND1-DOT1Q-MIB", "qAtmVciValue"), (0, "ALCATEL-IND1-DOT1Q-MIB", "qAtmIfIndexVpiVciVlanTagValue"))
if mibBuilder.loadTexts: qAtmIfIndexVpiVciEntry.setStatus('current')
if mibBuilder.loadTexts: qAtmIfIndexVpiVciEntry.setDescription('An entry in 802.1q IfIndex/VPI/VCI vlan table.')
qAtmIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4259841, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qAtmIfIndex.setStatus('current')
if mibBuilder.loadTexts: qAtmIfIndex.setDescription('The ATM Interface Index.')
qAtmVpiValue = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qAtmVpiValue.setStatus('current')
if mibBuilder.loadTexts: qAtmVpiValue.setDescription('.The Vpi value of the ATM VC..')
qAtmVciValue = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qAtmVciValue.setStatus('current')
if mibBuilder.loadTexts: qAtmVciValue.setDescription('.The Vci value of the ATM VC..')
qAtmIfIndexVpiVciVlanTagValue = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qAtmIfIndexVpiVciVlanTagValue.setStatus('current')
if mibBuilder.loadTexts: qAtmIfIndexVpiVciVlanTagValue.setDescription('Tag for a particular ATM Interface Index')
qAtmIfIndexVpiVciVlanAction = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 3, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qAtmIfIndexVpiVciVlanAction.setStatus('current')
if mibBuilder.loadTexts: qAtmIfIndexVpiVciVlanAction.setDescription('Row Status for creating/deleting services.')
qAtmIfIndexVpiVciVlanDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 3, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qAtmIfIndexVpiVciVlanDescription.setStatus('current')
if mibBuilder.loadTexts: qAtmIfIndexVpiVciVlanDescription.setDescription('Textual description of vlan added to an Interface Index.')
qAtmIfIndexVpiVciAcceptableFrameTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("admitAll", 1), ("admitOnlyVlanTagged", 2))).clone('admitAll')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qAtmIfIndexVpiVciAcceptableFrameTypes.setStatus('current')
if mibBuilder.loadTexts: qAtmIfIndexVpiVciAcceptableFrameTypes.setDescription('When this is admitOnlyVlanTagged(2) the device will discard untagged frames or Priority-Tagged frames received on this port. When admitAll(1), untagged frames or Priority-Tagged frames received on this port will be accepted and assigned to the PVID for this port. This control does not affect VLAN independent BPDU frames, such as GVRP and STP. It does affect VLAN dependent BPDU frames, such as GMRP.')
qAtmIfIndexVpiVciForceTagInternal = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 1, 0))).clone(namedValues=NamedValues(("na", 2), ("on", 1), ("off", 0))).clone('na')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qAtmIfIndexVpiVciForceTagInternal.setStatus('current')
if mibBuilder.loadTexts: qAtmIfIndexVpiVciForceTagInternal.setDescription('0-ON, 1-OFF and 2-NA')
alcatelIND1Dot1QMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-DOT1Q-MIB", "dot1qPortGroup"), ("ALCATEL-IND1-DOT1Q-MIB", "dot1qAggregateGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1Dot1QMIBCompliance = alcatelIND1Dot1QMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1Dot1QMIBCompliance.setDescription('Compliance statement for 802.1q.')
dot1qPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-DOT1Q-MIB", "qPortVlanSlot"), ("ALCATEL-IND1-DOT1Q-MIB", "qPortVlanPort"), ("ALCATEL-IND1-DOT1Q-MIB", "qPortVlanTagValue"), ("ALCATEL-IND1-DOT1Q-MIB", "qPortVlanStatus"), ("ALCATEL-IND1-DOT1Q-MIB", "qPortVlanDescription"), ("ALCATEL-IND1-DOT1Q-MIB", "qPortVlanForceTagInternal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1qPortGroup = dot1qPortGroup.setStatus('current')
if mibBuilder.loadTexts: dot1qPortGroup.setDescription('Collection of objects for management of 802.1q on the ports.')
dot1qAggregateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-DOT1Q-MIB", "qAggregateVlanAggregateId"), ("ALCATEL-IND1-DOT1Q-MIB", "qAggregateVlanTagValue"), ("ALCATEL-IND1-DOT1Q-MIB", "qAggregateVlanStatus"), ("ALCATEL-IND1-DOT1Q-MIB", "qAggregateVlanDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1qAggregateGroup = dot1qAggregateGroup.setStatus('current')
if mibBuilder.loadTexts: dot1qAggregateGroup.setDescription('Collection of objects for management of 802.1q on the aggregate.')
mibBuilder.exportSymbols("ALCATEL-IND1-DOT1Q-MIB", qAggregateVlanTagValue=qAggregateVlanTagValue, qAtmIfIndexVpiVciEntry=qAtmIfIndexVpiVciEntry, qAggregateVlanStatus=qAggregateVlanStatus, qPortVlanTagValue=qPortVlanTagValue, qAtmIfIndexVpiVciForceTagInternal=qAtmIfIndexVpiVciForceTagInternal, alcatelIND1Dot1QMIB=alcatelIND1Dot1QMIB, v8021Q=v8021Q, qPortVlanTable=qPortVlanTable, dot1qPortGroup=dot1qPortGroup, PYSNMP_MODULE_ID=alcatelIND1Dot1QMIB, qAtmVciValue=qAtmVciValue, alcatelIND1Dot1QMIBObjects=alcatelIND1Dot1QMIBObjects, qAtmIfIndex=qAtmIfIndex, alcatelIND1Dot1QMIBGroups=alcatelIND1Dot1QMIBGroups, qAtmVpiValue=qAtmVpiValue, qAtmIfIndexVpiVciTable=qAtmIfIndexVpiVciTable, alcatelIND1Dot1QMIBCompliances=alcatelIND1Dot1QMIBCompliances, qPortVlanDescription=qPortVlanDescription, qPortVlanForceTagInternal=qPortVlanForceTagInternal, qAggregateVlanDescription=qAggregateVlanDescription, alcatelIND1Dot1QMIBConformance=alcatelIND1Dot1QMIBConformance, alcatelIND1Dot1QMIBCompliance=alcatelIND1Dot1QMIBCompliance, qAtmIfIndexVpiVciAcceptableFrameTypes=qAtmIfIndexVpiVciAcceptableFrameTypes, qAggregateVlanTable=qAggregateVlanTable, qAggregateVlanEntry=qAggregateVlanEntry, qAtmIfIndexVpiVciVlanTagValue=qAtmIfIndexVpiVciVlanTagValue, qAtmIfIndexVpiVciVlanDescription=qAtmIfIndexVpiVciVlanDescription, dot1qAggregateGroup=dot1qAggregateGroup, qAggregateVlanAggregateId=qAggregateVlanAggregateId, qAtmIfIndexVpiVciVlanAction=qAtmIfIndexVpiVciVlanAction, qPortVlanPort=qPortVlanPort, qPortVlanSlot=qPortVlanSlot, qPortVlanStatus=qPortVlanStatus, qPortVlanEntry=qPortVlanEntry)