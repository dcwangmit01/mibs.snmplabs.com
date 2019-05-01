#
# PySNMP MIB module Gadzoox-1-Control-FIle (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Gadzoox-1-Control-FIle
# Produced by pysmi-0.3.4 at Wed May  1 13:20:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, enterprises, iso, Bits, ModuleIdentity, Counter32, Counter64, MibIdentifier, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "enterprises", "iso", "Bits", "ModuleIdentity", "Counter32", "Counter64", "MibIdentifier", "NotificationType", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
gadzoox = MibIdentifier((1, 3, 6, 1, 4, 1, 1754))
netMgmt = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: netMgmt.setStatus('mandatory')
common = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 1))
system = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1))
zoning = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3))
download = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 1, 3))
security = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 1, 4))
discovery = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 1, 5))
monitor = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 1, 6))
proxy = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7))
policy = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 11))
gbic = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 1, 8))
hub = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 2))
areaSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 3))
channelAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 4))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 5))
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 6))
capChas = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1))
capPim = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 6, 2))
nlPendingZoneTable = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlPendingZoneTable.setStatus('mandatory')
nlPendingZoneMemberTable = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlPendingZoneMemberTable.setStatus('mandatory')
nlActiveZoneTable = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlActiveZoneTable.setStatus('mandatory')
nlActiveZoneMemberTable = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlActiveZoneMemberTable.setStatus('mandatory')
deviceTable = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceTable.setStatus('mandatory')
gbicTable = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gbicTable.setStatus('mandatory')
trapIPaddrTable = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapIPaddrTable.setStatus('mandatory')
capChasTable = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChasTable.setStatus('mandatory')
capChasSlotTable = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChasSlotTable.setStatus('mandatory')
capPimTable = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capPimTable.setStatus('mandatory')
capPortTable = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capPortTable.setStatus('mandatory')
mibBuilder.exportSymbols("Gadzoox-1-Control-FIle", gbicTable=gbicTable, download=download, discovery=discovery, channelAgent=channelAgent, monitor=monitor, trapIPaddrTable=trapIPaddrTable, security=security, nlActiveZoneTable=nlActiveZoneTable, nlPendingZoneTable=nlPendingZoneTable, netMgmt=netMgmt, nlActiveZoneMemberTable=nlActiveZoneMemberTable, areaSwitch=areaSwitch, deviceTable=deviceTable, traps=traps, capPim=capPim, switch=switch, nlPendingZoneMemberTable=nlPendingZoneMemberTable, system=system, gbic=gbic, common=common, capChasTable=capChasTable, zoning=zoning, capChasSlotTable=capChasSlotTable, capPortTable=capPortTable, policy=policy, proxy=proxy, hub=hub, capPimTable=capPimTable, gadzoox=gadzoox, capChas=capChas)