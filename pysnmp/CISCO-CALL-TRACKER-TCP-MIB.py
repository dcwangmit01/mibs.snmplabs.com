#
# PySNMP MIB module CISCO-CALL-TRACKER-TCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CALL-TRACKER-TCP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:34:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
cctActiveCallId, cctHistoryIndex = mibBuilder.importSymbols("CISCO-CALL-TRACKER-MIB", "cctActiveCallId", "cctHistoryIndex")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoPort, = mibBuilder.importSymbols("CISCO-TC", "CiscoPort")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, NotificationType, Counter32, TimeTicks, MibIdentifier, Counter64, Unsigned32, Bits, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Counter32", "TimeTicks", "MibIdentifier", "Counter64", "Unsigned32", "Bits", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoCallTrackerTCPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 164))
ciscoCallTrackerTCPMIB.setRevisions(('2005-12-06 00:00', '2000-06-07 00:00',))
if mibBuilder.loadTexts: ciscoCallTrackerTCPMIB.setLastUpdated('200512060000Z')
if mibBuilder.loadTexts: ciscoCallTrackerTCPMIB.setOrganization('Cisco Systems, Inc.')
ccttMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 164, 1))
ccttActive = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 1))
ccttHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 2))
ccttActiveTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 1, 1), )
if mibBuilder.loadTexts: ccttActiveTable.setStatus('current')
ccttActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-CALL-TRACKER-MIB", "cctActiveCallId"))
if mibBuilder.loadTexts: ccttActiveEntry.setStatus('current')
ccttActiveLocalIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccttActiveLocalIpAddress.setStatus('current')
ccttActiveLocalTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 1, 1, 1, 2), CiscoPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccttActiveLocalTcpPort.setStatus('current')
ccttActiveRemoteIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 1, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccttActiveRemoteIpAddress.setStatus('current')
ccttActiveRemoteTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 1, 1, 1, 4), CiscoPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccttActiveRemoteTcpPort.setStatus('current')
ccttActiveDestinationFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccttActiveDestinationFailures.setStatus('current')
ccttHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 2, 1), )
if mibBuilder.loadTexts: ccttHistoryTable.setStatus('current')
ccttHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-CALL-TRACKER-MIB", "cctHistoryIndex"))
if mibBuilder.loadTexts: ccttHistoryEntry.setStatus('current')
ccttHistoryLocalIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 2, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccttHistoryLocalIpAddress.setStatus('current')
ccttHistoryLocalTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 2, 1, 1, 2), CiscoPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccttHistoryLocalTcpPort.setStatus('current')
ccttHistoryRemoteIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccttHistoryRemoteIpAddress.setStatus('current')
ccttHistoryRemoteTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 2, 1, 1, 4), CiscoPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccttHistoryRemoteTcpPort.setStatus('current')
ccttHistoryDestinationFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccttHistoryDestinationFailures.setStatus('current')
ccttMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 164, 2))
ccttMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 164, 2, 0))
ccttMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 164, 3))
ccttMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 164, 3, 1))
ccttMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 164, 3, 2))
ccttMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 164, 3, 1, 1)).setObjects(("CISCO-CALL-TRACKER-TCP-MIB", "ccttActiveGroup"), ("CISCO-CALL-TRACKER-TCP-MIB", "ccttHistoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccttMIBCompliance = ccttMIBCompliance.setStatus('current')
ccttActiveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 164, 3, 2, 2)).setObjects(("CISCO-CALL-TRACKER-TCP-MIB", "ccttActiveLocalIpAddress"), ("CISCO-CALL-TRACKER-TCP-MIB", "ccttActiveLocalTcpPort"), ("CISCO-CALL-TRACKER-TCP-MIB", "ccttActiveRemoteIpAddress"), ("CISCO-CALL-TRACKER-TCP-MIB", "ccttActiveRemoteTcpPort"), ("CISCO-CALL-TRACKER-TCP-MIB", "ccttActiveDestinationFailures"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccttActiveGroup = ccttActiveGroup.setStatus('current')
ccttHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 164, 3, 2, 3)).setObjects(("CISCO-CALL-TRACKER-TCP-MIB", "ccttHistoryLocalIpAddress"), ("CISCO-CALL-TRACKER-TCP-MIB", "ccttHistoryLocalTcpPort"), ("CISCO-CALL-TRACKER-TCP-MIB", "ccttHistoryRemoteIpAddress"), ("CISCO-CALL-TRACKER-TCP-MIB", "ccttHistoryRemoteTcpPort"), ("CISCO-CALL-TRACKER-TCP-MIB", "ccttHistoryDestinationFailures"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccttHistoryGroup = ccttHistoryGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-CALL-TRACKER-TCP-MIB", PYSNMP_MODULE_ID=ciscoCallTrackerTCPMIB, ccttActiveDestinationFailures=ccttActiveDestinationFailures, ccttMIBObjects=ccttMIBObjects, ciscoCallTrackerTCPMIB=ciscoCallTrackerTCPMIB, ccttActiveLocalIpAddress=ccttActiveLocalIpAddress, ccttMIBCompliance=ccttMIBCompliance, ccttActive=ccttActive, ccttActiveRemoteTcpPort=ccttActiveRemoteTcpPort, ccttHistoryTable=ccttHistoryTable, ccttHistory=ccttHistory, ccttMIBCompliances=ccttMIBCompliances, ccttActiveEntry=ccttActiveEntry, ccttMIBNotificationPrefix=ccttMIBNotificationPrefix, ccttHistoryDestinationFailures=ccttHistoryDestinationFailures, ccttHistoryRemoteIpAddress=ccttHistoryRemoteIpAddress, ccttActiveLocalTcpPort=ccttActiveLocalTcpPort, ccttActiveGroup=ccttActiveGroup, ccttActiveTable=ccttActiveTable, ccttHistoryEntry=ccttHistoryEntry, ccttMIBConformance=ccttMIBConformance, ccttHistoryRemoteTcpPort=ccttHistoryRemoteTcpPort, ccttHistoryLocalTcpPort=ccttHistoryLocalTcpPort, ccttHistoryGroup=ccttHistoryGroup, ccttMIBNotifications=ccttMIBNotifications, ccttMIBGroups=ccttMIBGroups, ccttHistoryLocalIpAddress=ccttHistoryLocalIpAddress, ccttActiveRemoteIpAddress=ccttActiveRemoteIpAddress)