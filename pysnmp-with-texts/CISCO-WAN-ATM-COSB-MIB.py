#
# PySNMP MIB module CISCO-WAN-ATM-COSB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-ATM-COSB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:20:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, IpAddress, ModuleIdentity, Gauge32, Integer32, Bits, MibIdentifier, Unsigned32, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "IpAddress", "ModuleIdentity", "Gauge32", "Integer32", "Bits", "MibIdentifier", "Unsigned32", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanAtmCosbMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 16))
ciscoWanAtmCosbMIB.setRevisions(('2003-03-21 00:00', '2002-06-10 00:00', '2000-04-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanAtmCosbMIB.setRevisionsDescriptions(('Descriptions have been clarified for few objects or tables.', '1. Added following objects to cwacIntervalTable, as upper 32-bits for counters which are 64-bit wide: cwacHighIntCellArrivals, cwacHighIntCellDiscards, cwacHighIntCellDeparts. 2. Added following 64-bit objects to cwacIntervalTable for 64-bit counter support: cwacHCIntCellArrivals, cwacHCIntCellDiscards, cwacHCIntCellDeparts', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoWanAtmCosbMIB.setLastUpdated('200303210000Z')
if mibBuilder.loadTexts: ciscoWanAtmCosbMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanAtmCosbMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanAtmCosbMIB.setDescription('The MIB to manage CoS(Class of Service) queue/buffer related parameters. One or more virtual interfaces may exist on a physical interface or a channelized interface. Every virtual interface has certain number (e.g. 16) of CoS queues. These queues are also known as Class Of Service Buffers. Every COS queue maps to an ATM trafiic type such as CBR, VBR-rt, ABR etc. These COS queues are used to provide QOS (quality of service), depending on the corresponding ATM trafiic type. This MIB provides management functionality such as Threshold Crossing Alarms(TCA) for cell discards and interval statistics for these COS queues.')
ciscoWanAtmCosbMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 16, 1))
cwacConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 1))
cwacStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2))
cwacStatsAlarmConfgTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 1), )
if mibBuilder.loadTexts: cwacStatsAlarmConfgTable.setStatus('current')
if mibBuilder.loadTexts: cwacStatsAlarmConfgTable.setDescription('This table contains alarm configuration parameters related to CoS queue. Entries in this table are automatically created when a new virtual interface is added.')
cwacStatsAlarmConfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-WAN-ATM-COSB-MIB", "cwacCosbIndex"))
if mibBuilder.loadTexts: cwacStatsAlarmConfgEntry.setStatus('current')
if mibBuilder.loadTexts: cwacStatsAlarmConfgEntry.setDescription('An entry in CoS queue alarm configuration table. This table is indexed by ifIndex, that belongs to the ifTable entry with ifType value atmVirtual(149), and cwacCosbIndex.')
cwacCosbIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: cwacCosbIndex.setStatus('current')
if mibBuilder.loadTexts: cwacCosbIndex.setDescription('This is the CoS queue number to which this entry belongs.')
cwacCosbCurrentCellsDiscThres = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwacCosbCurrentCellsDiscThres.setStatus('current')
if mibBuilder.loadTexts: cwacCosbCurrentCellsDiscThres.setDescription('This object indicates the threshold for cell discards for the current 15-min interval, above which alarm is generated.')
cwacStatsAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwacStatsAlarmStatus.setStatus('current')
if mibBuilder.loadTexts: cwacStatsAlarmStatus.setDescription('This is a bitmap that shows the status of TCA(Threshold Crossing Alarm) of current queue. This bitmap is sent as part of the trap that is generated as part of TCA being raised. Bit assignmed is as follows: ---------------------------- 1 Cell discard 15 minute threshold was exceeded. ')
cwacValidIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwacValidIntervals.setStatus('current')
if mibBuilder.loadTexts: cwacValidIntervals.setDescription('The number of previous intervals for which valid data has been stored.')
cwacIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2), )
if mibBuilder.loadTexts: cwacIntervalTable.setStatus('current')
if mibBuilder.loadTexts: cwacIntervalTable.setDescription('This table reflects interval statistics associated with each of the CoS queues. Entries in this table are automatically created when a new virtual interface is added.')
cwacIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-WAN-ATM-COSB-MIB", "cwacCosbIndex"), (0, "CISCO-WAN-ATM-COSB-MIB", "cwacIntervalNumber"))
if mibBuilder.loadTexts: cwacIntervalEntry.setStatus('current')
if mibBuilder.loadTexts: cwacIntervalEntry.setDescription('An entry for per virtual interface CoS queue interval statistics. In addition to the current 15-minute interval bucket, the previous 24 hours worth of 15-minute interval buckets are collected for each vitual interface. This table is indexed by ifIndex, that belongs to the ifTable entry with ifType value atmVirtual(149), cwacCosbIndex and cwacIntervalNumber.')
cwacIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96)))
if mibBuilder.loadTexts: cwacIntervalNumber.setStatus('current')
if mibBuilder.loadTexts: cwacIntervalNumber.setDescription('A number used to uniquely identify per virtual interface CoS queue interval statistics. 0 is used to identify the current 15-minute interval. 1-96 identify the previous 24 hours of 15-minute interval buckets.')
cwacIntCellArrivals = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwacIntCellArrivals.setStatus('current')
if mibBuilder.loadTexts: cwacIntCellArrivals.setDescription('The number of cells arrived at the queue during a particular 15 minute interval.')
cwacIntCellDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwacIntCellDiscards.setStatus('current')
if mibBuilder.loadTexts: cwacIntCellDiscards.setDescription('The number of cells discarded due to congestion during a particular 15 minute interval.')
cwacIntCellDeparts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwacIntCellDeparts.setStatus('current')
if mibBuilder.loadTexts: cwacIntCellDeparts.setDescription('The number of cells that left the QBIN during a particular 15 minute interval.')
cwacHighIntCellArrivals = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwacHighIntCellArrivals.setStatus('current')
if mibBuilder.loadTexts: cwacHighIntCellArrivals.setDescription('The upper 32-bits of the number of cells arrived at the queue during a particular 15-minute interval.')
cwacHighIntCellDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwacHighIntCellDiscards.setStatus('current')
if mibBuilder.loadTexts: cwacHighIntCellDiscards.setDescription('The upper 32-bits of the number of cells discarded due to congestion during a particular 15-minute interval.')
cwacHighIntCellDeparts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwacHighIntCellDeparts.setStatus('current')
if mibBuilder.loadTexts: cwacHighIntCellDeparts.setDescription('The upper 32-bits of the number of cells that left the QBIN during a particular 15-minute interval.')
cwacHCIntCellArrivals = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwacHCIntCellArrivals.setStatus('current')
if mibBuilder.loadTexts: cwacHCIntCellArrivals.setDescription('The 64 bit value of the number of cells arriving at the queue during a particular 15-minute interval.')
cwacHCIntCellDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwacHCIntCellDiscards.setStatus('current')
if mibBuilder.loadTexts: cwacHCIntCellDiscards.setDescription('The 64 bit value of the number of cells discarded due to congestion during a particular 15-minute interval.')
cwacHCIntCellDeparts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwacHCIntCellDeparts.setStatus('current')
if mibBuilder.loadTexts: cwacHCIntCellDeparts.setDescription('The 64 bit value of the number of cells that left the QBIN during a particular 15-minute interval.')
ciscoWanAtmCosbMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 16, 2))
ciscoWanAtmCosbMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 16, 2, 1))
ciscoWanAtmCosbMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 16, 2, 2))
ciscoWanAtmCosbMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 16, 2, 1, 1)).setObjects(("CISCO-WAN-ATM-COSB-MIB", "ciscoWanAtmCosbAlarmMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmCosbMIBCompliance = ciscoWanAtmCosbMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoWanAtmCosbMIBCompliance.setDescription('The Compliance statement for CoS queue configuration group.')
ciscoWanAtmCosbMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 16, 2, 1, 2)).setObjects(("CISCO-WAN-ATM-COSB-MIB", "ciscoWanAtmCosbAlarmMIBGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmCosbMIBCompliance1 = ciscoWanAtmCosbMIBCompliance1.setStatus('current')
if mibBuilder.loadTexts: ciscoWanAtmCosbMIBCompliance1.setDescription('The Compliance statement for CoS queue configuration group.')
ciscoWanAtmCosbAlarmMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 16, 2, 2, 1)).setObjects(("CISCO-WAN-ATM-COSB-MIB", "cwacCosbCurrentCellsDiscThres"), ("CISCO-WAN-ATM-COSB-MIB", "cwacStatsAlarmStatus"), ("CISCO-WAN-ATM-COSB-MIB", "cwacValidIntervals"), ("CISCO-WAN-ATM-COSB-MIB", "cwacIntCellArrivals"), ("CISCO-WAN-ATM-COSB-MIB", "cwacIntCellDiscards"), ("CISCO-WAN-ATM-COSB-MIB", "cwacIntCellDeparts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmCosbAlarmMIBGroup = ciscoWanAtmCosbAlarmMIBGroup.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoWanAtmCosbAlarmMIBGroup.setDescription('The statistical per virtual interface CoS queue alarm group.')
ciscoWanAtmCosbAlarmMIBGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 16, 2, 2, 2)).setObjects(("CISCO-WAN-ATM-COSB-MIB", "cwacCosbCurrentCellsDiscThres"), ("CISCO-WAN-ATM-COSB-MIB", "cwacStatsAlarmStatus"), ("CISCO-WAN-ATM-COSB-MIB", "cwacValidIntervals"), ("CISCO-WAN-ATM-COSB-MIB", "cwacIntCellArrivals"), ("CISCO-WAN-ATM-COSB-MIB", "cwacIntCellDiscards"), ("CISCO-WAN-ATM-COSB-MIB", "cwacIntCellDeparts"), ("CISCO-WAN-ATM-COSB-MIB", "cwacHighIntCellArrivals"), ("CISCO-WAN-ATM-COSB-MIB", "cwacHighIntCellDiscards"), ("CISCO-WAN-ATM-COSB-MIB", "cwacHighIntCellDeparts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmCosbAlarmMIBGroup1 = ciscoWanAtmCosbAlarmMIBGroup1.setStatus('current')
if mibBuilder.loadTexts: ciscoWanAtmCosbAlarmMIBGroup1.setDescription('The statistical per virtual interface CoS queue alarm group.')
ciscoHCWanAtmCosbAlarmMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 16, 2, 2, 3)).setObjects(("CISCO-WAN-ATM-COSB-MIB", "cwacHCIntCellArrivals"), ("CISCO-WAN-ATM-COSB-MIB", "cwacHCIntCellDiscards"), ("CISCO-WAN-ATM-COSB-MIB", "cwacHCIntCellDeparts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHCWanAtmCosbAlarmMIBGroup = ciscoHCWanAtmCosbAlarmMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoHCWanAtmCosbAlarmMIBGroup.setDescription('The statistical per virtual interface CoS queue alarm group.')
mibBuilder.exportSymbols("CISCO-WAN-ATM-COSB-MIB", cwacHighIntCellDiscards=cwacHighIntCellDiscards, cwacIntervalNumber=cwacIntervalNumber, ciscoWanAtmCosbAlarmMIBGroup1=ciscoWanAtmCosbAlarmMIBGroup1, PYSNMP_MODULE_ID=ciscoWanAtmCosbMIB, cwacCosbCurrentCellsDiscThres=cwacCosbCurrentCellsDiscThres, cwacHCIntCellArrivals=cwacHCIntCellArrivals, cwacHCIntCellDeparts=cwacHCIntCellDeparts, cwacIntervalTable=cwacIntervalTable, ciscoWanAtmCosbMIBGroups=ciscoWanAtmCosbMIBGroups, cwacIntCellDiscards=cwacIntCellDiscards, cwacStatistics=cwacStatistics, ciscoWanAtmCosbMIBCompliance1=ciscoWanAtmCosbMIBCompliance1, ciscoWanAtmCosbAlarmMIBGroup=ciscoWanAtmCosbAlarmMIBGroup, cwacHighIntCellDeparts=cwacHighIntCellDeparts, cwacStatsAlarmStatus=cwacStatsAlarmStatus, cwacHCIntCellDiscards=cwacHCIntCellDiscards, ciscoHCWanAtmCosbAlarmMIBGroup=ciscoHCWanAtmCosbAlarmMIBGroup, cwacHighIntCellArrivals=cwacHighIntCellArrivals, cwacStatsAlarmConfgEntry=cwacStatsAlarmConfgEntry, ciscoWanAtmCosbMIBObjects=ciscoWanAtmCosbMIBObjects, cwacConfig=cwacConfig, cwacIntervalEntry=cwacIntervalEntry, cwacIntCellDeparts=cwacIntCellDeparts, ciscoWanAtmCosbMIBConformance=ciscoWanAtmCosbMIBConformance, cwacCosbIndex=cwacCosbIndex, ciscoWanAtmCosbMIBCompliances=ciscoWanAtmCosbMIBCompliances, ciscoWanAtmCosbMIB=ciscoWanAtmCosbMIB, ciscoWanAtmCosbMIBCompliance=ciscoWanAtmCosbMIBCompliance, cwacValidIntervals=cwacValidIntervals, cwacIntCellArrivals=cwacIntCellArrivals, cwacStatsAlarmConfgTable=cwacStatsAlarmConfgTable)