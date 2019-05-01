#
# PySNMP MIB module HUAWEI-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-TUNNEL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:49:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ipv6IfIndex, = mibBuilder.importSymbols("IPV6-MIB", "ipv6IfIndex")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, Bits, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, ObjectIdentity, Counter64, Unsigned32, Counter32, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Bits", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "ObjectIdentity", "Counter64", "Unsigned32", "Counter32", "Integer32", "MibIdentifier")
TruthValue, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString", "RowStatus")
hwTunnelMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201))
if mibBuilder.loadTexts: hwTunnelMib.setLastUpdated('200906201610Z')
if mibBuilder.loadTexts: hwTunnelMib.setOrganization('IPv6-Team of Huawei Technologies')
if mibBuilder.loadTexts: hwTunnelMib.setContactInfo('R&D BeiJing, Huawei Technologies co.,Ltd. Showchuang Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China Zip:100085 ')
if mibBuilder.loadTexts: hwTunnelMib.setDescription('The MIB module for entities implementing the Tunnel protocol configuration.')
hwTunnelMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1))
hwTunnelCfgTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 1), )
if mibBuilder.loadTexts: hwTunnelCfgTable.setStatus('current')
if mibBuilder.loadTexts: hwTunnelCfgTable.setDescription('MIB table for the tunnel configuration information.')
hwTunnelCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 1, 1), ).setIndexNames((0, "IPV6-MIB", "ipv6IfIndex"))
if mibBuilder.loadTexts: hwTunnelCfgEntry.setStatus('current')
if mibBuilder.loadTexts: hwTunnelCfgEntry.setDescription('Describes tunnel interface configuration information.')
hwTunnelProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("gre", 1), ("mplsTe", 2), ("ipv6Ipv4", 3), ("ipv6Ipv4Auto", 4), ("ipv6Ipv46to4", 5), ("ipv6Ipv4Isatap", 6), ("ipv4Ipv6", 7), ("none", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwTunnelProtocol.setStatus('current')
if mibBuilder.loadTexts: hwTunnelProtocol.setDescription('This object specifies the Tunnel protocol type.')
hwTunnelSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("interfaceName", 1), ("sourceAddress", 2), ("unknown", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwTunnelSourceType.setStatus('current')
if mibBuilder.loadTexts: hwTunnelSourceType.setDescription('This object specifies the Tunnel source type.')
hwTunnelSrcIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwTunnelSrcIfName.setStatus('current')
if mibBuilder.loadTexts: hwTunnelSrcIfName.setDescription('This object specifies the tunnel source interface name.')
hwTunnelAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 1, 1, 4), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwTunnelAddrType.setStatus('current')
if mibBuilder.loadTexts: hwTunnelAddrType.setDescription('This object specifies the address type for Tunnel source and destination address.')
hwTunnelSourceAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 1, 1, 5), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwTunnelSourceAddr.setStatus('current')
if mibBuilder.loadTexts: hwTunnelSourceAddr.setDescription('This object specifies source address of the tunnel interface.')
hwTunnelDestinationAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 1, 1, 6), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwTunnelDestinationAddr.setStatus('current')
if mibBuilder.loadTexts: hwTunnelDestinationAddr.setDescription('This object specifies destination address of the tunnel interface.')
hwTunnelCfgUndoFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("undoTunnelProtocol", 1), ("undoTunnelSource", 2), ("undoTunnelDestination", 3), ("invalid", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwTunnelCfgUndoFlag.setStatus('current')
if mibBuilder.loadTexts: hwTunnelCfgUndoFlag.setDescription('This object specifies undo operation for specified hwTunnelCfgTable parameter.')
hwIpv6Tunnel4Over6CfgTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 2), )
if mibBuilder.loadTexts: hwIpv6Tunnel4Over6CfgTable.setStatus('current')
if mibBuilder.loadTexts: hwIpv6Tunnel4Over6CfgTable.setDescription('MIB table for 4Over6 tunnel configuration information.')
hwIpv6Tunnel4Over6CfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 2, 1), ).setIndexNames((0, "IPV6-MIB", "ipv6IfIndex"))
if mibBuilder.loadTexts: hwIpv6Tunnel4Over6CfgEntry.setStatus('current')
if mibBuilder.loadTexts: hwIpv6Tunnel4Over6CfgEntry.setDescription('Describes IPv6 tunnel 4Over6 parameters.')
hwIpv6TunnelEncapLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwIpv6TunnelEncapLimit.setStatus('current')
if mibBuilder.loadTexts: hwIpv6TunnelEncapLimit.setDescription('This object specifies Tunnel ipv4-ipv6 encapsulation limit.')
hwIpv6TunnelEncapLimitDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIpv6TunnelEncapLimitDisable.setStatus('current')
if mibBuilder.loadTexts: hwIpv6TunnelEncapLimitDisable.setDescription('This object specifies Tunnel encapsulation is disabled or not. Default value is false.')
hwIpv6TunnelFlowLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1048575))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwIpv6TunnelFlowLabel.setStatus('current')
if mibBuilder.loadTexts: hwIpv6TunnelFlowLabel.setDescription('This object specifies Tunnel ipv4-ipv6 flow label.')
hwIpv6TunnelHopLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwIpv6TunnelHopLimit.setStatus('current')
if mibBuilder.loadTexts: hwIpv6TunnelHopLimit.setDescription('This object specifies Tunnel ipv4-ipv6 hop limit.')
hwIpv6TunnelTrafficClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwIpv6TunnelTrafficClass.setStatus('current')
if mibBuilder.loadTexts: hwIpv6TunnelTrafficClass.setDescription('This object specifies Tunnel ipv4-ipv6 traffic-class.')
hwIpv6TunnelTrafficOriginal = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 2, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwIpv6TunnelTrafficOriginal.setStatus('current')
if mibBuilder.loadTexts: hwIpv6TunnelTrafficOriginal.setDescription('Specifies Tunnel ipv4-ipv6 traffic-class original is enabled or not.')
hwIPv6Tunnel4Over6CfgUndoFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("undoTunnelEncapLimit", 1), ("undoTunnelFlowLabel", 2), ("undoTunnelHopLimit", 3), ("undoTunnelTrafficClass", 4), ("invalid", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwIPv6Tunnel4Over6CfgUndoFlag.setStatus('current')
if mibBuilder.loadTexts: hwIPv6Tunnel4Over6CfgUndoFlag.setDescription('This object specifies undo operation for specified hwIpv6Tunnel4Over6CfgTable parameter.')
hwTunnelMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 2))
hwTunnelCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 2, 1))
hwTunnelCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 2, 1, 1)).setObjects(("HUAWEI-TUNNEL-MIB", "hwTunnelGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTunnelCompliance = hwTunnelCompliance.setStatus('current')
if mibBuilder.loadTexts: hwTunnelCompliance.setDescription('The compliance statement for systems supporting the HUAWEI-TUNNEL-MIB.')
hwTunnelGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 2, 2))
hwTunnelGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 201, 2, 2, 1)).setObjects(("HUAWEI-TUNNEL-MIB", "hwTunnelProtocol"), ("HUAWEI-TUNNEL-MIB", "hwTunnelSourceType"), ("HUAWEI-TUNNEL-MIB", "hwTunnelSrcIfName"), ("HUAWEI-TUNNEL-MIB", "hwTunnelAddrType"), ("HUAWEI-TUNNEL-MIB", "hwTunnelSourceAddr"), ("HUAWEI-TUNNEL-MIB", "hwTunnelDestinationAddr"), ("HUAWEI-TUNNEL-MIB", "hwTunnelCfgUndoFlag"), ("HUAWEI-TUNNEL-MIB", "hwIpv6TunnelEncapLimit"), ("HUAWEI-TUNNEL-MIB", "hwIpv6TunnelEncapLimitDisable"), ("HUAWEI-TUNNEL-MIB", "hwIpv6TunnelFlowLabel"), ("HUAWEI-TUNNEL-MIB", "hwIpv6TunnelHopLimit"), ("HUAWEI-TUNNEL-MIB", "hwIpv6TunnelTrafficClass"), ("HUAWEI-TUNNEL-MIB", "hwIpv6TunnelTrafficOriginal"), ("HUAWEI-TUNNEL-MIB", "hwIPv6Tunnel4Over6CfgUndoFlag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTunnelGroup = hwTunnelGroup.setStatus('current')
if mibBuilder.loadTexts: hwTunnelGroup.setDescription('The Tunnel table member.')
mibBuilder.exportSymbols("HUAWEI-TUNNEL-MIB", hwTunnelCompliance=hwTunnelCompliance, hwTunnelMibObjects=hwTunnelMibObjects, hwTunnelCompliances=hwTunnelCompliances, hwTunnelCfgEntry=hwTunnelCfgEntry, hwTunnelSourceType=hwTunnelSourceType, PYSNMP_MODULE_ID=hwTunnelMib, hwTunnelMib=hwTunnelMib, hwIpv6TunnelFlowLabel=hwIpv6TunnelFlowLabel, hwTunnelGroups=hwTunnelGroups, hwIpv6TunnelTrafficOriginal=hwIpv6TunnelTrafficOriginal, hwTunnelAddrType=hwTunnelAddrType, hwTunnelMibConformance=hwTunnelMibConformance, hwTunnelSourceAddr=hwTunnelSourceAddr, hwTunnelDestinationAddr=hwTunnelDestinationAddr, hwIpv6TunnelHopLimit=hwIpv6TunnelHopLimit, hwIPv6Tunnel4Over6CfgUndoFlag=hwIPv6Tunnel4Over6CfgUndoFlag, hwIpv6TunnelEncapLimitDisable=hwIpv6TunnelEncapLimitDisable, hwTunnelProtocol=hwTunnelProtocol, hwIpv6TunnelEncapLimit=hwIpv6TunnelEncapLimit, hwTunnelCfgTable=hwTunnelCfgTable, hwTunnelGroup=hwTunnelGroup, hwIpv6Tunnel4Over6CfgEntry=hwIpv6Tunnel4Over6CfgEntry, hwTunnelSrcIfName=hwTunnelSrcIfName, hwTunnelCfgUndoFlag=hwTunnelCfgUndoFlag, hwIpv6Tunnel4Over6CfgTable=hwIpv6Tunnel4Over6CfgTable, hwIpv6TunnelTrafficClass=hwIpv6TunnelTrafficClass)