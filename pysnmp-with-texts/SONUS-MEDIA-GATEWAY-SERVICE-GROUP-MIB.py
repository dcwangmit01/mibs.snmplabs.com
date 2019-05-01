#
# PySNMP MIB module SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:09:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, TimeTicks, Counter32, Counter64, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, Unsigned32, Gauge32, MibIdentifier, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Counter32", "Counter64", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "Unsigned32", "Gauge32", "MibIdentifier", "iso", "IpAddress")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
sonusSignallingMIBs, = mibBuilder.importSymbols("SONUS-SMI", "sonusSignallingMIBs")
SonusBoolean, SonusNameReference, SonusName = mibBuilder.importSymbols("SONUS-TC", "SonusBoolean", "SonusNameReference", "SonusName")
sonusMediaGatewayServiceGroupMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3))
if mibBuilder.loadTexts: sonusMediaGatewayServiceGroupMIB.setLastUpdated('200102030000Z')
if mibBuilder.loadTexts: sonusMediaGatewayServiceGroupMIB.setOrganization('Sonus Networks, Inc.')
if mibBuilder.loadTexts: sonusMediaGatewayServiceGroupMIB.setContactInfo(' Customer Support Sonus Networks, Inc, 5 Carlisle Road Westford, MA 01886 USA Tel: 978-692-8999 Fax: 978-392-9118 E-mail: cs.snmp@sonusnet.com')
if mibBuilder.loadTexts: sonusMediaGatewayServiceGroupMIB.setDescription('The MIB Module for Media Gateway Service Group management.')
sonusMediaGatewayServiceGroupMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1))
sonusMgsgServiceGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1))
sonusMgsgServiceGrpNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusMgsgServiceGrpNextIndex.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgServiceGrpNextIndex.setDescription('The next valid index to use when creating a new sonusMgsgServiceGrpEntry')
sonusMgsgServiceGrpTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 2), )
if mibBuilder.loadTexts: sonusMgsgServiceGrpTable.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgServiceGrpTable.setDescription('This table contains information about each Media Gateway Service Group configured to be a member of the node. A management entity may create rows for Service Group that are anticipated to be supported in the future.')
sonusMgsgServiceGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 2, 1), ).setIndexNames((0, "SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB", "sonusMgsgServiceGrpListIndex"))
if mibBuilder.loadTexts: sonusMgsgServiceGrpEntry.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgServiceGrpEntry.setDescription('This table describes the Media Gateway Service Groups that are configured as members of the Marlin Node.')
sonusMgsgServiceGrpListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusMgsgServiceGrpListIndex.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgServiceGrpListIndex.setDescription('The index of the Media Gateway Service Group entry.')
sonusMgsgServiceGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 2, 1, 2), SonusName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusMgsgServiceGrpName.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgServiceGrpName.setDescription('The name of the Media Gateway Service Group.')
sonusMgsgServiceGrpAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusMgsgServiceGrpAdminState.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgServiceGrpAdminState.setDescription('The admin state of the Media Gateway Service Group.')
sonusMgsgServiceGrpControllerName = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 2, 1, 4), SonusNameReference()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusMgsgServiceGrpControllerName.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgServiceGrpControllerName.setDescription('The Name of the Media Gateway Controller which controls this service group')
sonusMgsgServiceGrpType = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipdc", 1), ("mgcp", 2))).clone('mgcp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusMgsgServiceGrpType.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgServiceGrpType.setDescription('The type(protocol) of media gateway control protocol Note: ipdc value is obsolete and can not be used')
sonusMgsgServiceGrpMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("blocked", 1), ("unblocked", 2))).clone('blocked')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusMgsgServiceGrpMode.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgServiceGrpMode.setDescription('Whether the Service Group is in Blocked or Unblocked Mode')
sonusMgsgServiceGrpAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dryup", 1), ("force", 2))).clone('dryup')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusMgsgServiceGrpAction.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgServiceGrpAction.setDescription('Indicates whether the service group is to be put in blocked immediately or after a dry-up period')
sonusMgsgServiceGrpTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1440)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusMgsgServiceGrpTimeout.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgServiceGrpTimeout.setDescription('The TimeOut Period for DryUp In Minutes')
sonusMgsgServiceGrpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 2, 1, 9), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusMgsgServiceGrpRowStatus.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgServiceGrpRowStatus.setDescription('')
sonusMgsgServiceGrpStatTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 2), )
if mibBuilder.loadTexts: sonusMgsgServiceGrpStatTable.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgServiceGrpStatTable.setDescription('This table contains status information about each MGSG service group in the Marlin Switch node. ')
sonusMgsgServiceGrpStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 2, 1), ).setIndexNames((0, "SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB", "sonusMgsgServiceGrpStatListIndex"))
if mibBuilder.loadTexts: sonusMgsgServiceGrpStatEntry.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgServiceGrpStatEntry.setDescription('This table describes the status of MGSG Service Groups')
sonusMgsgServiceGrpStatListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusMgsgServiceGrpStatListIndex.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgServiceGrpStatListIndex.setDescription('The index of the MGSG Service Group.')
sonusMgsgServiceGrpStatName = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 2, 1, 2), SonusNameReference()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusMgsgServiceGrpStatName.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgServiceGrpStatName.setDescription('The name of the MGSG Service Group.')
sonusMgsgServiceGrpStatStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("available", 1), ("unavailable", 2), ("blocked", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusMgsgServiceGrpStatStatus.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgServiceGrpStatStatus.setDescription('The state of the MGSG Service Group.')
sonusMgsgCktTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3), )
if mibBuilder.loadTexts: sonusMgsgCktTable.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktTable.setDescription('The Mgsg Ckt table describes the ckts in a MGSG service Group.')
sonusMgsgCktEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1), ).setIndexNames((0, "SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB", "sonusMgsgCktShelfIndex"), (0, "SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB", "sonusMgsgCktSlotIndex"), (0, "SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB", "sonusMgsgCktDs1Index"), (0, "SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB", "sonusMgsgCktDs0Index"))
if mibBuilder.loadTexts: sonusMgsgCktEntry.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktEntry.setDescription('This is the admin table for MGSG Circuits')
sonusMgsgCktShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusMgsgCktShelfIndex.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktShelfIndex.setDescription('The Shelf Index for this Ckt Table')
sonusMgsgCktSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusMgsgCktSlotIndex.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktSlotIndex.setDescription('The Slot Index for this Ckt Table')
sonusMgsgCktDs1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 28))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusMgsgCktDs1Index.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktDs1Index.setDescription('The Ds1 Index for this Ckt Table')
sonusMgsgCktDs0Index = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusMgsgCktDs0Index.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktDs0Index.setDescription('Identifies the channel the ckt represents.')
sonusMgsgCktSrvGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 5), SonusNameReference()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusMgsgCktSrvGrpName.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktSrvGrpName.setDescription('The name of the MGSG Service Group this ckt is under.')
sonusMgsgCktMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("blocked", 1), ("unblocked", 2))).clone('blocked')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusMgsgCktMode.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktMode.setDescription('Whether the Circuit is in Blocked or Unblocked Mode')
sonusMgsgCktAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dryup", 1), ("force", 2))).clone('dryup')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusMgsgCktAction.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktAction.setDescription('Indicates whether the circuit is to be put in blocked immediately or after a dry-up period')
sonusMgsgCktTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1440)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusMgsgCktTimeout.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktTimeout.setDescription('The TimeOut Period for DryUp In Minutes')
sonusMgsgCktAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusMgsgCktAdminState.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktAdminState.setDescription('The admin state of the MGSG Ckt.')
sonusMgsgCktProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 10), SonusNameReference()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusMgsgCktProfileName.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktProfileName.setDescription('The ckt profile name assigned to the MGSG ckt.')
sonusMgsgCktType = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("data", 1), ("dchan-user", 2), ("dchan-ntwk", 3))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusMgsgCktType.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktType.setDescription('The type of the MGSG Ckt. (data or a D-channel)')
sonusMgsgCktDchanSwitchType = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("ni2", 1), ("sw4ess", 2), ("sw5esscust", 3), ("dms", 4), ("kdd", 5), ("ntt", 6), ("itu", 7), ("net5", 8), ("sw1tr6", 9), ("ts014", 10), ("vn", 11))).clone('itu')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusMgsgCktDchanSwitchType.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktDchanSwitchType.setDescription('For Ckts of type D-chan this describes the switch type that D-chan is connected to.')
sonusMgsgCktRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 13), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusMgsgCktRowStatus.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktRowStatus.setDescription('')
sonusMgsgCktStatTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 4), )
if mibBuilder.loadTexts: sonusMgsgCktStatTable.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktStatTable.setDescription('This table contains status information about each MGSG ckt in the Marlin Switch node. .')
sonusMgsgCktStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 4, 1), ).setIndexNames((0, "SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB", "sonusMgsgCktStatShelfIndex"), (0, "SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB", "sonusMgsgCktStatSlotIndex"), (0, "SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB", "sonusMgsgCktStatDs1Index"), (0, "SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB", "sonusMgsgCktStatDs0Index"))
if mibBuilder.loadTexts: sonusMgsgCktStatEntry.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktStatEntry.setDescription('This table describes the status of the configured MGSG ckts.')
sonusMgsgCktStatShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusMgsgCktStatShelfIndex.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktStatShelfIndex.setDescription('The Shelf Index for this Ckt Table')
sonusMgsgCktStatSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusMgsgCktStatSlotIndex.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktStatSlotIndex.setDescription('The Slot Index for this Ckt Table')
sonusMgsgCktStatDs1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusMgsgCktStatDs1Index.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktStatDs1Index.setDescription('The Ds1 Index for this Ckt Table')
sonusMgsgCktStatDs0Index = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusMgsgCktStatDs0Index.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktStatDs0Index.setDescription('Identifies the channel the ckt represents.')
sonusMgsgCktStatSrvGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 4, 1, 5), SonusNameReference()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusMgsgCktStatSrvGrpName.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktStatSrvGrpName.setDescription('The name of the MGSG Service Group this ckt is under.')
sonusMgsgCktStatMgcState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("notPresent", 1), ("outOfService", 2), ("maintenance", 3), ("blocked", 4), ("loopback", 5), ("idle", 6), ("inUse", 7), ("connected", 8), ("disabled", 9), ("dualToneLoop", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusMgsgCktStatMgcState.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktStatMgcState.setDescription('The state of MGSG ckt, as reported to the Media Gateway Controller ')
sonusMgsgCktStatLocalHwState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("available", 1), ("unavailable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusMgsgCktStatLocalHwState.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktStatLocalHwState.setDescription('The local state of the MGSG ckt from a hardware perspective')
sonusMgsgCktStatDryupInProgress = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 4, 1, 8), SonusBoolean()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusMgsgCktStatDryupInProgress.setStatus('current')
if mibBuilder.loadTexts: sonusMgsgCktStatDryupInProgress.setDescription('This object indicates whether a dry-up is in progress or not on the circuit')
sonusMediaGatewayServiceGroupMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 2))
sonusMediaGatewayServiceGroupMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 2, 0))
sonusMediaGatewayServiceGroupMIBNotificationsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 2, 1))
mibBuilder.exportSymbols("SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB", sonusMediaGatewayServiceGroupMIBObjects=sonusMediaGatewayServiceGroupMIBObjects, sonusMgsgServiceGrpTimeout=sonusMgsgServiceGrpTimeout, sonusMgsgCktShelfIndex=sonusMgsgCktShelfIndex, PYSNMP_MODULE_ID=sonusMediaGatewayServiceGroupMIB, sonusMgsgServiceGrpAction=sonusMgsgServiceGrpAction, sonusMgsgServiceGrpStatListIndex=sonusMgsgServiceGrpStatListIndex, sonusMgsgCktSrvGrpName=sonusMgsgCktSrvGrpName, sonusMgsgServiceGrpListIndex=sonusMgsgServiceGrpListIndex, sonusMgsgServiceGrpType=sonusMgsgServiceGrpType, sonusMgsgCktStatShelfIndex=sonusMgsgCktStatShelfIndex, sonusMgsgCktEntry=sonusMgsgCktEntry, sonusMgsgServiceGrpStatStatus=sonusMgsgServiceGrpStatStatus, sonusMgsgCktStatDs1Index=sonusMgsgCktStatDs1Index, sonusMgsgCktStatDs0Index=sonusMgsgCktStatDs0Index, sonusMediaGatewayServiceGroupMIBNotificationsObjects=sonusMediaGatewayServiceGroupMIBNotificationsObjects, sonusMediaGatewayServiceGroupMIBNotifications=sonusMediaGatewayServiceGroupMIBNotifications, sonusMgsgCktStatMgcState=sonusMgsgCktStatMgcState, sonusMgsgCktStatSlotIndex=sonusMgsgCktStatSlotIndex, sonusMgsgCktRowStatus=sonusMgsgCktRowStatus, sonusMgsgServiceGrpTable=sonusMgsgServiceGrpTable, sonusMgsgServiceGrpStatTable=sonusMgsgServiceGrpStatTable, sonusMgsgServiceGrpName=sonusMgsgServiceGrpName, sonusMgsgCktType=sonusMgsgCktType, sonusMgsgServiceGrpControllerName=sonusMgsgServiceGrpControllerName, sonusMediaGatewayServiceGroupMIBNotificationsPrefix=sonusMediaGatewayServiceGroupMIBNotificationsPrefix, sonusMgsgServiceGrpNextIndex=sonusMgsgServiceGrpNextIndex, sonusMgsgCktDs1Index=sonusMgsgCktDs1Index, sonusMgsgCktStatEntry=sonusMgsgCktStatEntry, sonusMgsgServiceGrpStatName=sonusMgsgServiceGrpStatName, sonusMgsgCktStatLocalHwState=sonusMgsgCktStatLocalHwState, sonusMgsgServiceGrpRowStatus=sonusMgsgServiceGrpRowStatus, sonusMgsgServiceGrpEntry=sonusMgsgServiceGrpEntry, sonusMgsgCktSlotIndex=sonusMgsgCktSlotIndex, sonusMgsgServiceGrpAdminState=sonusMgsgServiceGrpAdminState, sonusMgsgCktStatDryupInProgress=sonusMgsgCktStatDryupInProgress, sonusMgsgCktMode=sonusMgsgCktMode, sonusMgsgCktAction=sonusMgsgCktAction, sonusMgsgCktAdminState=sonusMgsgCktAdminState, sonusMgsgCktStatTable=sonusMgsgCktStatTable, sonusMgsgCktProfileName=sonusMgsgCktProfileName, sonusMgsgCktStatSrvGrpName=sonusMgsgCktStatSrvGrpName, sonusMediaGatewayServiceGroupMIB=sonusMediaGatewayServiceGroupMIB, sonusMgsgCktTimeout=sonusMgsgCktTimeout, sonusMgsgCktDchanSwitchType=sonusMgsgCktDchanSwitchType, sonusMgsgServiceGrp=sonusMgsgServiceGrp, sonusMgsgServiceGrpMode=sonusMgsgServiceGrpMode, sonusMgsgCktTable=sonusMgsgCktTable, sonusMgsgServiceGrpStatEntry=sonusMgsgServiceGrpStatEntry, sonusMgsgCktDs0Index=sonusMgsgCktDs0Index)