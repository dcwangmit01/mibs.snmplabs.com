#
# PySNMP MIB module CISCO-WRED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WRED-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:05:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, TimeTicks, NotificationType, iso, ModuleIdentity, Gauge32, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "TimeTicks", "NotificationType", "iso", "ModuleIdentity", "Gauge32", "Unsigned32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWredMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 83))
ciscoWredMIB.setRevisions(('1997-07-18 00:00',))
if mibBuilder.loadTexts: ciscoWredMIB.setLastUpdated('9707180000Z')
if mibBuilder.loadTexts: ciscoWredMIB.setOrganization('Cisco Systems, Inc.')
ciscoWredMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 83, 1))
cwredConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 1))
cwredStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 2))
cwredConfigGlobTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 1, 1), )
if mibBuilder.loadTexts: cwredConfigGlobTable.setStatus('current')
cwredConfigGlobEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cwredConfigGlobEntry.setStatus('current')
cwredConfigGlobQueueWeight = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwredConfigGlobQueueWeight.setStatus('current')
cwredConfigPrecedTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 1, 2), )
if mibBuilder.loadTexts: cwredConfigPrecedTable.setStatus('current')
cwredConfigPrecedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-WRED-MIB", "cwredConfigPrecedPrecedence"))
if mibBuilder.loadTexts: cwredConfigPrecedEntry.setStatus('current')
cwredConfigPrecedPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: cwredConfigPrecedPrecedence.setStatus('current')
cwredConfigPrecedMinDepthThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 1, 2, 1, 2), Integer32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwredConfigPrecedMinDepthThreshold.setStatus('current')
cwredConfigPrecedMaxDepthThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 1, 2, 1, 3), Integer32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwredConfigPrecedMaxDepthThreshold.setStatus('current')
cwredConfigPrecedPktsDropFraction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwredConfigPrecedPktsDropFraction.setStatus('current')
cwredQueueTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 2, 1), )
if mibBuilder.loadTexts: cwredQueueTable.setStatus('current')
cwredQueueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 2, 1, 1), )
cwredConfigGlobEntry.registerAugmentions(("CISCO-WRED-MIB", "cwredQueueEntry"))
cwredQueueEntry.setIndexNames(*cwredConfigGlobEntry.getIndexNames())
if mibBuilder.loadTexts: cwredQueueEntry.setStatus('current')
cwredQueueAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 2, 1, 1, 1), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwredQueueAverage.setStatus('current')
cwredQueueDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 2, 1, 1, 2), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwredQueueDepth.setStatus('current')
cwredStatTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 2, 2), )
if mibBuilder.loadTexts: cwredStatTable.setStatus('current')
cwredStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 2, 2, 1), )
cwredConfigPrecedEntry.registerAugmentions(("CISCO-WRED-MIB", "cwredStatEntry"))
cwredStatEntry.setIndexNames(*cwredConfigPrecedEntry.getIndexNames())
if mibBuilder.loadTexts: cwredStatEntry.setStatus('current')
cwredStatSwitchedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 2, 2, 1, 1), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwredStatSwitchedPkts.setStatus('current')
cwredStatRandomFilteredPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 2, 2, 1, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwredStatRandomFilteredPkts.setStatus('current')
cwredStatMaxFilteredPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 2, 2, 1, 3), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwredStatMaxFilteredPkts.setStatus('current')
ciscoWredMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 83, 3))
ciscoWredMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 83, 3, 1))
ciscoWredMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 83, 3, 2))
ciscoWredMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 83, 3, 1, 1)).setObjects(("CISCO-WRED-MIB", "ciscoWredMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWredMIBCompliance = ciscoWredMIBCompliance.setStatus('current')
ciscoWredMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 83, 3, 2, 1)).setObjects(("CISCO-WRED-MIB", "cwredConfigGlobQueueWeight"), ("CISCO-WRED-MIB", "cwredConfigPrecedMinDepthThreshold"), ("CISCO-WRED-MIB", "cwredConfigPrecedMaxDepthThreshold"), ("CISCO-WRED-MIB", "cwredConfigPrecedPktsDropFraction"), ("CISCO-WRED-MIB", "cwredQueueAverage"), ("CISCO-WRED-MIB", "cwredQueueDepth"), ("CISCO-WRED-MIB", "cwredStatSwitchedPkts"), ("CISCO-WRED-MIB", "cwredStatRandomFilteredPkts"), ("CISCO-WRED-MIB", "cwredStatMaxFilteredPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWredMIBGroup = ciscoWredMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WRED-MIB", ciscoWredMIBCompliance=ciscoWredMIBCompliance, cwredConfigGlobQueueWeight=cwredConfigGlobQueueWeight, cwredStats=cwredStats, PYSNMP_MODULE_ID=ciscoWredMIB, cwredConfigGlobTable=cwredConfigGlobTable, cwredConfigGlobEntry=cwredConfigGlobEntry, cwredConfig=cwredConfig, cwredQueueDepth=cwredQueueDepth, ciscoWredMIBGroups=ciscoWredMIBGroups, ciscoWredMIBCompliances=ciscoWredMIBCompliances, cwredConfigPrecedMaxDepthThreshold=cwredConfigPrecedMaxDepthThreshold, cwredConfigPrecedPktsDropFraction=cwredConfigPrecedPktsDropFraction, ciscoWredMIBConformance=ciscoWredMIBConformance, ciscoWredMIBGroup=ciscoWredMIBGroup, cwredConfigPrecedEntry=cwredConfigPrecedEntry, cwredStatSwitchedPkts=cwredStatSwitchedPkts, cwredStatEntry=cwredStatEntry, cwredConfigPrecedTable=cwredConfigPrecedTable, cwredQueueEntry=cwredQueueEntry, cwredConfigPrecedPrecedence=cwredConfigPrecedPrecedence, cwredQueueAverage=cwredQueueAverage, cwredStatTable=cwredStatTable, cwredQueueTable=cwredQueueTable, ciscoWredMIBObjects=ciscoWredMIBObjects, cwredStatRandomFilteredPkts=cwredStatRandomFilteredPkts, cwredStatMaxFilteredPkts=cwredStatMaxFilteredPkts, cwredConfigPrecedMinDepthThreshold=cwredConfigPrecedMinDepthThreshold, ciscoWredMIB=ciscoWredMIB)