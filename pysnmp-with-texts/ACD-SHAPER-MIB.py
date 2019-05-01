#
# PySNMP MIB module ACD-SHAPER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ACD-SHAPER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:13:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
acdMibs, = mibBuilder.importSymbols("ACCEDIAN-SMI", "acdMibs")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, NotificationType, ObjectIdentity, Unsigned32, Integer32, IpAddress, Bits, MibIdentifier, Counter64, ModuleIdentity, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "NotificationType", "ObjectIdentity", "Unsigned32", "Integer32", "IpAddress", "Bits", "MibIdentifier", "Counter64", "ModuleIdentity", "iso", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
acdShaper = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420, 2, 10))
acdShaper.setRevisions(('2009-11-01 01:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: acdShaper.setRevisionsDescriptions(('Initial version of MIB module ACD-SHAPER-MIB.',))
if mibBuilder.loadTexts: acdShaper.setLastUpdated('200911010100Z')
if mibBuilder.loadTexts: acdShaper.setOrganization('Accedian Networks, Inc.')
if mibBuilder.loadTexts: acdShaper.setContactInfo('Accedian Technical Assistance Center Accedian Networks, Inc. 4878 Levy, suite 202 Saint-Laurent, Quebec Canada H4R 2P1 E-mail: support@accedian.com')
if mibBuilder.loadTexts: acdShaper.setDescription('.')
acdShaper1 = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1))
acdShaper1MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1))
acdShaper1Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 2))
acdShaper1Config = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 1))
acdShaper1Stats = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2))
acdShaper1CodePointStatsTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1), )
if mibBuilder.loadTexts: acdShaper1CodePointStatsTable.setStatus('current')
if mibBuilder.loadTexts: acdShaper1CodePointStatsTable.setDescription('This table contains statistics for all Code Point in the system. Each Code Point are define by tuple PCP, color, incoming port and outgoing port.')
acdShaper1CodePointStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1), ).setIndexNames((0, "ACD-SHAPER-MIB", "acdShaper1CodePointStatsDstID"), (0, "ACD-SHAPER-MIB", "acdShaper1CodePointStatsSrcID"), (0, "ACD-SHAPER-MIB", "acdShaper1CodePointStatsColorID"), (0, "ACD-SHAPER-MIB", "acdShaper1CodePointStatsPcpID"))
if mibBuilder.loadTexts: acdShaper1CodePointStatsEntry.setStatus('current')
if mibBuilder.loadTexts: acdShaper1CodePointStatsEntry.setDescription('.')
acdShaper1CodePointStatsDstID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: acdShaper1CodePointStatsDstID.setStatus('current')
if mibBuilder.loadTexts: acdShaper1CodePointStatsDstID.setDescription('Destination port ID.')
acdShaper1CodePointStatsSrcID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: acdShaper1CodePointStatsSrcID.setStatus('current')
if mibBuilder.loadTexts: acdShaper1CodePointStatsSrcID.setDescription('Source port ID.')
acdShaper1CodePointStatsColorID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("green", 1), ("yellow", 2))))
if mibBuilder.loadTexts: acdShaper1CodePointStatsColorID.setStatus('current')
if mibBuilder.loadTexts: acdShaper1CodePointStatsColorID.setDescription('Color value.')
acdShaper1CodePointStatsPcpID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: acdShaper1CodePointStatsPcpID.setStatus('current')
if mibBuilder.loadTexts: acdShaper1CodePointStatsPcpID.setDescription('PCP value.')
acdShaper1CodePointStatsFwdOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 5), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsFwdOctets.setStatus('current')
if mibBuilder.loadTexts: acdShaper1CodePointStatsFwdOctets.setDescription('Total number of octets forwarded without delay.')
acdShaper1CodePointStatsFwdPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 6), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsFwdPkts.setStatus('current')
if mibBuilder.loadTexts: acdShaper1CodePointStatsFwdPkts.setDescription('Total number of packets forwarded without delay.')
acdShaper1CodePointStatsFwdRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 7), Gauge32()).setUnits('Mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsFwdRate.setStatus('current')
if mibBuilder.loadTexts: acdShaper1CodePointStatsFwdRate.setDescription('Bit rate in Mbps forwarded without delay.')
acdShaper1CodePointStatsDelayedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 8), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsDelayedOctets.setStatus('current')
if mibBuilder.loadTexts: acdShaper1CodePointStatsDelayedOctets.setDescription('Total number of octets enqueued.')
acdShaper1CodePointStatsDelayedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 9), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsDelayedPkts.setStatus('current')
if mibBuilder.loadTexts: acdShaper1CodePointStatsDelayedPkts.setDescription('Total number of packets enqueued.')
acdShaper1CodePointStatsDelayedRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 10), Gauge32()).setUnits('Mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsDelayedRate.setStatus('current')
if mibBuilder.loadTexts: acdShaper1CodePointStatsDelayedRate.setDescription('Bit rate in Mbps enqueued.')
acdShaper1CodePointStatsOverflowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 11), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsOverflowOctets.setStatus('current')
if mibBuilder.loadTexts: acdShaper1CodePointStatsOverflowOctets.setDescription('Total number of octets dropped due to the queue overflow.')
acdShaper1CodePointStatsOverflowPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 12), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsOverflowPkts.setStatus('current')
if mibBuilder.loadTexts: acdShaper1CodePointStatsOverflowPkts.setDescription('Total number of packets dropped due to the queue overflow.')
acdShaper1CodePointStatsOverflowRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 13), Gauge32()).setUnits('Mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsOverflowRate.setStatus('current')
if mibBuilder.loadTexts: acdShaper1CodePointStatsOverflowRate.setDescription('Bit rate in Mbps dropped due to the queue overflow.')
acdShaper1CodePointStatsQMgmtDropOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 14), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsQMgmtDropOctets.setStatus('current')
if mibBuilder.loadTexts: acdShaper1CodePointStatsQMgmtDropOctets.setDescription('Total number of octets dropped by the queue management algorithm.')
acdShaper1CodePointStatsQMgmtDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 15), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsQMgmtDropPkts.setStatus('current')
if mibBuilder.loadTexts: acdShaper1CodePointStatsQMgmtDropPkts.setDescription('Total number of packets dropped by the queue management algorithm.')
acdShaper1CodePointStatsQMgmtDropRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 16), Gauge32()).setUnits('Mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsQMgmtDropRate.setStatus('current')
if mibBuilder.loadTexts: acdShaper1CodePointStatsQMgmtDropRate.setDescription('Bit rate in Mbps dropped by the queue management algorithm.')
acdShaper1Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 2, 1))
acdShaper1Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 2, 2))
acdShaper1CodePointStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 2, 2, 1)).setObjects(("ACD-SHAPER-MIB", "acdShaper1CodePointStatsFwdOctets"), ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsFwdPkts"), ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsFwdRate"), ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsDelayedOctets"), ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsDelayedPkts"), ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsDelayedRate"), ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsOverflowOctets"), ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsOverflowPkts"), ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsOverflowRate"), ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsQMgmtDropOctets"), ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsQMgmtDropPkts"), ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsQMgmtDropRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdShaper1CodePointStatsGroup = acdShaper1CodePointStatsGroup.setStatus('current')
if mibBuilder.loadTexts: acdShaper1CodePointStatsGroup.setDescription('.')
acdShaper1Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 2, 1, 1)).setObjects(("ACD-SHAPER-MIB", "acdShaper1CodePointStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdShaper1Compliance = acdShaper1Compliance.setStatus('current')
if mibBuilder.loadTexts: acdShaper1Compliance.setDescription('The compliance statement for support of the ACD-SHAPER-MIB module.')
mibBuilder.exportSymbols("ACD-SHAPER-MIB", acdShaper1CodePointStatsQMgmtDropRate=acdShaper1CodePointStatsQMgmtDropRate, acdShaper1Stats=acdShaper1Stats, acdShaper1CodePointStatsDelayedOctets=acdShaper1CodePointStatsDelayedOctets, acdShaper1Groups=acdShaper1Groups, acdShaper1MIBObjects=acdShaper1MIBObjects, acdShaper1Compliance=acdShaper1Compliance, acdShaper1CodePointStatsFwdPkts=acdShaper1CodePointStatsFwdPkts, acdShaper1CodePointStatsQMgmtDropOctets=acdShaper1CodePointStatsQMgmtDropOctets, acdShaper1Config=acdShaper1Config, acdShaper1CodePointStatsFwdOctets=acdShaper1CodePointStatsFwdOctets, acdShaper1=acdShaper1, acdShaper1CodePointStatsOverflowOctets=acdShaper1CodePointStatsOverflowOctets, acdShaper1Compliances=acdShaper1Compliances, acdShaper1CodePointStatsGroup=acdShaper1CodePointStatsGroup, acdShaper=acdShaper, acdShaper1CodePointStatsColorID=acdShaper1CodePointStatsColorID, acdShaper1CodePointStatsEntry=acdShaper1CodePointStatsEntry, acdShaper1CodePointStatsDstID=acdShaper1CodePointStatsDstID, acdShaper1CodePointStatsQMgmtDropPkts=acdShaper1CodePointStatsQMgmtDropPkts, acdShaper1Conformance=acdShaper1Conformance, acdShaper1CodePointStatsOverflowPkts=acdShaper1CodePointStatsOverflowPkts, acdShaper1CodePointStatsDelayedRate=acdShaper1CodePointStatsDelayedRate, acdShaper1CodePointStatsDelayedPkts=acdShaper1CodePointStatsDelayedPkts, PYSNMP_MODULE_ID=acdShaper, acdShaper1CodePointStatsPcpID=acdShaper1CodePointStatsPcpID, acdShaper1CodePointStatsTable=acdShaper1CodePointStatsTable, acdShaper1CodePointStatsOverflowRate=acdShaper1CodePointStatsOverflowRate, acdShaper1CodePointStatsFwdRate=acdShaper1CodePointStatsFwdRate, acdShaper1CodePointStatsSrcID=acdShaper1CodePointStatsSrcID)