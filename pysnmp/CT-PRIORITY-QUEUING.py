#
# PySNMP MIB module CT-PRIORITY-QUEUING (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CT-PRIORITY-QUEUING
# Produced by pysmi-0.3.4 at Mon Apr 29 18:13:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, Counter64, ObjectIdentity, NotificationType, Integer32, Unsigned32, ModuleIdentity, iso, Bits, MibIdentifier, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter64", "ObjectIdentity", "NotificationType", "Integer32", "Unsigned32", "ModuleIdentity", "iso", "Bits", "MibIdentifier", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cabletron = MibIdentifier((1, 3, 6, 1, 4, 1, 52))
mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4))
ctronExp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2))
ctVLANMib = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 12))
ctVLANMgr = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1))
ctPriority = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4))
ctBasePriority = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2))
ctUserDefPriority = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 1))
ctRegenPriority = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 2))
ctTrafPriority = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 3))
ctUserDefTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 1, 1), )
if mibBuilder.loadTexts: ctUserDefTable.setStatus('obsolete')
ctUserDefEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 1, 1, 1), ).setIndexNames((0, "CT-PRIORITY-QUEUING", "ctUserDefPriorityIndex"))
if mibBuilder.loadTexts: ctUserDefEntry.setStatus('obsolete')
ctUserDefPriorityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctUserDefPriorityIndex.setStatus('obsolete')
ctUserDefPriorityValue = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctUserDefPriorityValue.setStatus('obsolete')
ctUserDefNumTrafficClass = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctUserDefNumTrafficClass.setStatus('obsolete')
ctRegenerationTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 2, 1), )
if mibBuilder.loadTexts: ctRegenerationTable.setStatus('obsolete')
ctRegenerationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 2, 1, 1), ).setIndexNames((0, "CT-PRIORITY-QUEUING", "ctRegenerationIndex"), (0, "CT-PRIORITY-QUEUING", "ctRegenerationId"))
if mibBuilder.loadTexts: ctRegenerationEntry.setStatus('obsolete')
ctRegenerationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctRegenerationIndex.setStatus('obsolete')
ctRegenerationId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctRegenerationId.setStatus('obsolete')
ctRegenerationValue = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctRegenerationValue.setStatus('obsolete')
ctTrafClassTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 3, 1), )
if mibBuilder.loadTexts: ctTrafClassTable.setStatus('obsolete')
ctTrafClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 3, 1, 1), ).setIndexNames((0, "CT-PRIORITY-QUEUING", "ctTrafClassIndex"), (0, "CT-PRIORITY-QUEUING", "ctTrafClassId"))
if mibBuilder.loadTexts: ctTrafClassEntry.setStatus('obsolete')
ctTrafClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTrafClassIndex.setStatus('obsolete')
ctTrafClassId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTrafClassId.setStatus('obsolete')
ctTrafClassValue = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2, 3, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTrafClassValue.setStatus('obsolete')
mibBuilder.exportSymbols("CT-PRIORITY-QUEUING", ctTrafClassIndex=ctTrafClassIndex, ctTrafClassTable=ctTrafClassTable, ctUserDefNumTrafficClass=ctUserDefNumTrafficClass, ctTrafClassId=ctTrafClassId, ctPriority=ctPriority, cabletron=cabletron, ctUserDefPriority=ctUserDefPriority, ctUserDefPriorityValue=ctUserDefPriorityValue, ctTrafClassValue=ctTrafClassValue, ctBasePriority=ctBasePriority, ctRegenerationId=ctRegenerationId, ctRegenerationIndex=ctRegenerationIndex, ctUserDefPriorityIndex=ctUserDefPriorityIndex, ctVLANMgr=ctVLANMgr, mibs=mibs, ctronExp=ctronExp, ctRegenerationValue=ctRegenerationValue, ctTrafClassEntry=ctTrafClassEntry, ctUserDefEntry=ctUserDefEntry, ctRegenerationTable=ctRegenerationTable, ctTrafPriority=ctTrafPriority, ctRegenerationEntry=ctRegenerationEntry, ctVLANMib=ctVLANMib, ctRegenPriority=ctRegenPriority, ctUserDefTable=ctUserDefTable)