#
# PySNMP MIB module PACKETLOGIC-RAID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PACKETLOGIC-RAID-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:36:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
hw, = mibBuilder.importSymbols("PACKETLOGIC-HW-MIB", "hw")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Integer32, TimeTicks, NotificationType, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, ObjectIdentity, Unsigned32, ModuleIdentity, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "TimeTicks", "NotificationType", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "MibIdentifier", "Gauge32")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
raid = ModuleIdentity((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1))
raid.setRevisions(('2012-09-26 12:48',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: raid.setRevisionsDescriptions((' Latest version at the revision date for version GET VERSION HERE',))
if mibBuilder.loadTexts: raid.setLastUpdated('201209261248Z')
if mibBuilder.loadTexts: raid.setOrganization('Procera Networks, Inc.')
if mibBuilder.loadTexts: raid.setContactInfo('support@proceranetworks.com')
if mibBuilder.loadTexts: raid.setDescription('MIB for PacketLogic2 RAID devices')
raidCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 1))
ld = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3), )
if mibBuilder.loadTexts: ld.setStatus('current')
if mibBuilder.loadTexts: ld.setDescription('Conceptual Table')
ldEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3, 1), ).setIndexNames((0, "PACKETLOGIC-RAID-MIB", "ldEntryIndex"))
if mibBuilder.loadTexts: ldEntry.setStatus('current')
if mibBuilder.loadTexts: ldEntry.setDescription('Conceptual Table')
ldEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ldEntryIndex.setStatus('current')
if mibBuilder.loadTexts: ldEntryIndex.setDescription('Unique Row Index for Conceptual Table')
disk = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4), )
if mibBuilder.loadTexts: disk.setStatus('current')
if mibBuilder.loadTexts: disk.setDescription('Conceptual Table')
diskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1), ).setIndexNames((0, "PACKETLOGIC-RAID-MIB", "diskEntryIndex"))
if mibBuilder.loadTexts: diskEntry.setStatus('current')
if mibBuilder.loadTexts: diskEntry.setDescription('Conceptual Table')
diskEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: diskEntryIndex.setStatus('current')
if mibBuilder.loadTexts: diskEntryIndex.setDescription('Unique Row Index for Conceptual Table')
adpNumber = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpNumber.setStatus('current')
if mibBuilder.loadTexts: adpNumber.setDescription('Number of available adapters in system')
ldNumber = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ldNumber.setStatus('current')
if mibBuilder.loadTexts: ldNumber.setDescription('Number of available logical devices in system')
diskNumber = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskNumber.setStatus('current')
if mibBuilder.loadTexts: diskNumber.setDescription('Number of available disks in system')
ldId = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ldId.setStatus('current')
if mibBuilder.loadTexts: ldId.setDescription('LD Index')
ldState = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ldState.setStatus('current')
if mibBuilder.loadTexts: ldState.setDescription('LD State')
diskId = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskId.setStatus('current')
if mibBuilder.loadTexts: diskId.setDescription('Disk Index')
diskState = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskState.setStatus('current')
if mibBuilder.loadTexts: diskState.setDescription('Disk State')
mibBuilder.exportSymbols("PACKETLOGIC-RAID-MIB", diskEntry=diskEntry, adpNumber=adpNumber, diskId=diskId, ld=ld, ldEntryIndex=ldEntryIndex, ldId=ldId, raidCfg=raidCfg, ldNumber=ldNumber, diskNumber=diskNumber, ldState=ldState, PYSNMP_MODULE_ID=raid, diskEntryIndex=diskEntryIndex, diskState=diskState, disk=disk, ldEntry=ldEntry, raid=raid)