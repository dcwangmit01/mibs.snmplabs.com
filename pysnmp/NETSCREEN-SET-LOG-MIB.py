#
# PySNMP MIB module NETSCREEN-SET-LOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETSCREEN-SET-LOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:10:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
netscreenSettingMibModule, netscreenSetting = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenSettingMibModule", "netscreenSetting")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, IpAddress, ModuleIdentity, Counter64, Counter32, iso, TimeTicks, MibIdentifier, Bits, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "IpAddress", "ModuleIdentity", "Counter64", "Counter32", "iso", "TimeTicks", "MibIdentifier", "Bits", "Integer32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netscreenSetLogMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 7, 0, 8))
netscreenSetLogMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2003-11-10 00:00', '2001-09-28 00:00', '2001-05-27 00:00',))
if mibBuilder.loadTexts: netscreenSetLogMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenSetLogMibModule.setOrganization('Juniper Networks, Inc.')
nsSetLog = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 7, 8))
nsSetLogEnable = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetLogEnable.setStatus('current')
nsSetLogVPNEnable = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 8, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetLogVPNEnable.setStatus('current')
nsSetLogTraffic = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 8, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetLogTraffic.setStatus('current')
nsSetLogHostName = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 8, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetLogHostName.setStatus('current')
nsSetLogPort = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 8, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetLogPort.setStatus('current')
nsSetLogSecFacility = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 8, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(16, 17, 18, 19, 20, 21, 22, 23, 4))).clone(namedValues=NamedValues(("local0", 16), ("local1", 17), ("local2", 18), ("local3", 19), ("local4", 20), ("local5", 21), ("local6", 22), ("local7", 23), ("auth-sec", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetLogSecFacility.setStatus('current')
nsSetLogFacility = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 8, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(16, 17, 18, 19, 20, 21, 22, 23, 4))).clone(namedValues=NamedValues(("local0", 16), ("local1", 17), ("local2", 18), ("local3", 19), ("local4", 20), ("lcoal5", 21), ("local6", 22), ("loca7", 23), ("auth-sec", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetLogFacility.setStatus('current')
nsSetLogLevel = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 8, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("emergency", 0), ("aleart", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetLogLevel.setStatus('current')
nsSetLogWebTrendsEnable = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 8, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetLogWebTrendsEnable.setStatus('current')
nsSetLogWebTrendsVPNEnable = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 8, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetLogWebTrendsVPNEnable.setStatus('current')
nsSetLogWebTrendsHostName = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 8, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetLogWebTrendsHostName.setStatus('current')
nsSetLogWebTrendsPort = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 8, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetLogWebTrendsPort.setStatus('current')
mibBuilder.exportSymbols("NETSCREEN-SET-LOG-MIB", nsSetLogWebTrendsHostName=nsSetLogWebTrendsHostName, nsSetLogHostName=nsSetLogHostName, nsSetLog=nsSetLog, nsSetLogPort=nsSetLogPort, netscreenSetLogMibModule=netscreenSetLogMibModule, PYSNMP_MODULE_ID=netscreenSetLogMibModule, nsSetLogFacility=nsSetLogFacility, nsSetLogWebTrendsPort=nsSetLogWebTrendsPort, nsSetLogVPNEnable=nsSetLogVPNEnable, nsSetLogEnable=nsSetLogEnable, nsSetLogTraffic=nsSetLogTraffic, nsSetLogWebTrendsVPNEnable=nsSetLogWebTrendsVPNEnable, nsSetLogWebTrendsEnable=nsSetLogWebTrendsEnable, nsSetLogSecFacility=nsSetLogSecFacility, nsSetLogLevel=nsSetLogLevel)