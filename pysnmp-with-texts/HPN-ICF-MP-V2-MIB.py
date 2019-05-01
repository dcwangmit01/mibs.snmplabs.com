#
# PySNMP MIB module HPN-ICF-MP-V2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-MP-V2-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:40:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, ModuleIdentity, IpAddress, NotificationType, Counter64, ObjectIdentity, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "ModuleIdentity", "IpAddress", "NotificationType", "Counter64", "ObjectIdentity", "TimeTicks", "Unsigned32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfMultilinkPPPV2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140))
hpnicfMultilinkPPPV2.setRevisions(('2013-07-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfMultilinkPPPV2.setRevisionsDescriptions(('HPN-ICF-MP-V2-MIB module for managing MP(Multilink PPP).',))
if mibBuilder.loadTexts: hpnicfMultilinkPPPV2.setLastUpdated('201307150000Z')
if mibBuilder.loadTexts: hpnicfMultilinkPPPV2.setOrganization('')
if mibBuilder.loadTexts: hpnicfMultilinkPPPV2.setContactInfo('')
if mibBuilder.loadTexts: hpnicfMultilinkPPPV2.setDescription('The HPN-ICF-MP-V2-MIB provides read access to MP(Multilink PPP) link status information. The information available through this MIB includes: the father channel, the bundled son channel, the slot on which son channels are bundled, the number of son channels, the bundle name, the statistics for lost fragments, reordered packets, unassigned packets, interleaved packets, and the received/sent sequence number, etc.')
hpnicfMpObjectsV2 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1))
hpnicfMpMultilinkV2Table = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1), )
if mibBuilder.loadTexts: hpnicfMpMultilinkV2Table.setStatus('current')
if mibBuilder.loadTexts: hpnicfMpMultilinkV2Table.setDescription('This table describes the information of MP link. The index of this table is the interface index of MP group or VA (Virtual Access) interface.')
hpnicfMpMultilinkV2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfMpMultilinkV2Entry.setStatus('current')
if mibBuilder.loadTexts: hpnicfMpMultilinkV2Entry.setDescription('Each entry in this table describes the information of MP link. The available information includes: the father channel, the slot on which son channels are bundled, the number of bundled son channels, the statistics for lost fragments, reordered packets, unassigned packets, interleaved packets, and received/sent sequence number.')
hpnicfMpMultilinkDescrV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMpMultilinkDescrV2.setStatus('current')
if mibBuilder.loadTexts: hpnicfMpMultilinkDescrV2.setDescription('The interface name of the father interface on which son channels are bundled. It is the name of a Virtual Access or an MP group.')
hpnicfMpBundleNameV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMpBundleNameV2.setStatus('current')
if mibBuilder.loadTexts: hpnicfMpBundleNameV2.setDescription('The bundle name of the multilink. When authentication is configured, the bundle name is the authenticated user name; when authentication is not configured, the bundle name is multilink. ')
hpnicfMpBundledSlotV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMpBundledSlotV2.setStatus('current')
if mibBuilder.loadTexts: hpnicfMpBundledSlotV2.setDescription('The slot on which son channels are bundled. ')
hpnicfMpBundledMemberCntV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMpBundledMemberCntV2.setStatus('current')
if mibBuilder.loadTexts: hpnicfMpBundledMemberCntV2.setDescription('The number of the bundled son channel of the MP link. ')
hpnicfMpLostFragmentsV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMpLostFragmentsV2.setStatus('current')
if mibBuilder.loadTexts: hpnicfMpLostFragmentsV2.setDescription('The number of fragments of the MP link discarded because bad fragments were received, or assembling the packet failed, etc.')
hpnicfMpReorderedPktsV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMpReorderedPktsV2.setStatus('current')
if mibBuilder.loadTexts: hpnicfMpReorderedPktsV2.setDescription('The number of reordered incoming packets of the MP link. ')
hpnicfMpUnassignedPktsV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMpUnassignedPktsV2.setStatus('current')
if mibBuilder.loadTexts: hpnicfMpUnassignedPktsV2.setDescription('The number of received packets of the MP link waiting for reordering. ')
hpnicfMpInterleavedPktsV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMpInterleavedPktsV2.setStatus('current')
if mibBuilder.loadTexts: hpnicfMpInterleavedPktsV2.setDescription('The number of received packets of the MP link interleaved by the packets queued in RTPQ (Real-time Transport Protocol Queue) or LLQ (Low Latency Queue). ')
hpnicfMpRcvdSequenceV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMpRcvdSequenceV2.setStatus('current')
if mibBuilder.loadTexts: hpnicfMpRcvdSequenceV2.setDescription('The current sequence number for the MP link to receive. ')
hpnicfMpSentSequenceV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMpSentSequenceV2.setStatus('current')
if mibBuilder.loadTexts: hpnicfMpSentSequenceV2.setDescription('The current sequence number for the MP link to send. ')
hpnicfMpMemberlinkV2Table = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 2), )
if mibBuilder.loadTexts: hpnicfMpMemberlinkV2Table.setStatus('current')
if mibBuilder.loadTexts: hpnicfMpMemberlinkV2Table.setDescription('This table describes the information of son channels of the MP link. The index of this table is the interface index of MP group or VA (Virtual Access) interface. ')
hpnicfMpMemberlinkV2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-MP-V2-MIB", "hpnicfMpMemberlinkSeqNumberV2"))
if mibBuilder.loadTexts: hpnicfMpMemberlinkV2Entry.setStatus('current')
if mibBuilder.loadTexts: hpnicfMpMemberlinkV2Entry.setDescription('Each entry in this table describes the information of the bundled son channels of MP link. The available information includes: the interface index of the son channel, the interface name of the son channel. ')
hpnicfMpMemberlinkSeqNumberV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMpMemberlinkSeqNumberV2.setStatus('current')
if mibBuilder.loadTexts: hpnicfMpMemberlinkSeqNumberV2.setDescription('The bundled sequence number of the son channels of the MP link. This object is one of the index of the table. ')
hpnicfMpMemberlinkIfIndexV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMpMemberlinkIfIndexV2.setStatus('current')
if mibBuilder.loadTexts: hpnicfMpMemberlinkIfIndexV2.setDescription('The interface index of the son channels of the MP link. ')
hpnicfMpMemberlinkDescrV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMpMemberlinkDescrV2.setStatus('current')
if mibBuilder.loadTexts: hpnicfMpMemberlinkDescrV2.setDescription('The interface name of the son channels of the MP link. ')
hpnicfMpMemberlinkMpStatusV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMpMemberlinkMpStatusV2.setStatus('current')
if mibBuilder.loadTexts: hpnicfMpMemberlinkMpStatusV2.setDescription('The MP status of the son channels of the MP link. ')
mibBuilder.exportSymbols("HPN-ICF-MP-V2-MIB", hpnicfMpUnassignedPktsV2=hpnicfMpUnassignedPktsV2, PYSNMP_MODULE_ID=hpnicfMultilinkPPPV2, hpnicfMpMemberlinkDescrV2=hpnicfMpMemberlinkDescrV2, hpnicfMpInterleavedPktsV2=hpnicfMpInterleavedPktsV2, hpnicfMpMultilinkV2Entry=hpnicfMpMultilinkV2Entry, hpnicfMpReorderedPktsV2=hpnicfMpReorderedPktsV2, hpnicfMpSentSequenceV2=hpnicfMpSentSequenceV2, hpnicfMpObjectsV2=hpnicfMpObjectsV2, hpnicfMpLostFragmentsV2=hpnicfMpLostFragmentsV2, hpnicfMultilinkPPPV2=hpnicfMultilinkPPPV2, hpnicfMpMemberlinkMpStatusV2=hpnicfMpMemberlinkMpStatusV2, hpnicfMpBundleNameV2=hpnicfMpBundleNameV2, hpnicfMpMemberlinkV2Entry=hpnicfMpMemberlinkV2Entry, hpnicfMpMemberlinkSeqNumberV2=hpnicfMpMemberlinkSeqNumberV2, hpnicfMpRcvdSequenceV2=hpnicfMpRcvdSequenceV2, hpnicfMpMemberlinkIfIndexV2=hpnicfMpMemberlinkIfIndexV2, hpnicfMpBundledSlotV2=hpnicfMpBundledSlotV2, hpnicfMpBundledMemberCntV2=hpnicfMpBundledMemberCntV2, hpnicfMpMultilinkV2Table=hpnicfMpMultilinkV2Table, hpnicfMpMultilinkDescrV2=hpnicfMpMultilinkDescrV2, hpnicfMpMemberlinkV2Table=hpnicfMpMemberlinkV2Table)