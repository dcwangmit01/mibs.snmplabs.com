#
# PySNMP MIB module HPN-ICF-DOT11-WLANEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-DOT11-WLANEXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:25:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
HpnicfDot11ObjectIDType, HpnicfDot11QosAcType, hpnicfDot11, HpnicfDot11RadioScopeType = mibBuilder.importSymbols("HPN-ICF-DOT11-REF-MIB", "HpnicfDot11ObjectIDType", "HpnicfDot11QosAcType", "hpnicfDot11", "HpnicfDot11RadioScopeType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Unsigned32, iso, IpAddress, Gauge32, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, Integer32, ObjectIdentity, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "iso", "IpAddress", "Gauge32", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "Integer32", "ObjectIdentity", "ModuleIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfDot11WLANEXT = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7))
hpnicfDot11WLANEXT.setRevisions(('2007-06-08 20:00',))
if mibBuilder.loadTexts: hpnicfDot11WLANEXT.setLastUpdated('200706082000Z')
if mibBuilder.loadTexts: hpnicfDot11WLANEXT.setOrganization('')
hpnicfDot11RFGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 1))
hpnicfDot11QosGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2))
hpnicfDot11RFSignalStatisTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 1, 1), )
if mibBuilder.loadTexts: hpnicfDot11RFSignalStatisTable.setStatus('current')
hpnicfDot11RFSignalStatisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-DOT11-WLANEXT-MIB", "hpnicfDot11RFAPID"), (0, "HPN-ICF-DOT11-WLANEXT-MIB", "hpnicfDot11RFRadioID"))
if mibBuilder.loadTexts: hpnicfDot11RFSignalStatisEntry.setStatus('current')
hpnicfDot11RFAPID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 1, 1, 1, 1), HpnicfDot11ObjectIDType())
if mibBuilder.loadTexts: hpnicfDot11RFAPID.setStatus('current')
hpnicfDot11RFRadioID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 1, 1, 1, 2), HpnicfDot11RadioScopeType())
if mibBuilder.loadTexts: hpnicfDot11RFRadioID.setStatus('current')
hpnicfDot11RFSignalStatisInterv = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 1, 1, 1, 3), Integer32()).setUnits('second').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11RFSignalStatisInterv.setStatus('current')
hpnicfDot11RFAverageSignalStrength = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 1, 1, 1, 4), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11RFAverageSignalStrength.setStatus('current')
hpnicfDot11RFMaxSignalStrength = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 1, 1, 1, 5), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11RFMaxSignalStrength.setStatus('current')
hpnicfDot11RFMinSignalStrength = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 1, 1, 1, 6), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11RFMinSignalStrength.setStatus('current')
hpnicfDot11QosStatisTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2, 1), )
if mibBuilder.loadTexts: hpnicfDot11QosStatisTable.setStatus('current')
hpnicfDot11QosStatisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2, 1, 1), ).setIndexNames((0, "HPN-ICF-DOT11-WLANEXT-MIB", "hpnicfDot11QosAPID"), (0, "HPN-ICF-DOT11-WLANEXT-MIB", "hpnicfDot11QosRadioID"))
if mibBuilder.loadTexts: hpnicfDot11QosStatisEntry.setStatus('current')
hpnicfDot11QosAPID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2, 1, 1, 1), HpnicfDot11ObjectIDType())
if mibBuilder.loadTexts: hpnicfDot11QosAPID.setStatus('current')
hpnicfDot11QosRadioID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2, 1, 1, 2), HpnicfDot11RadioScopeType())
if mibBuilder.loadTexts: hpnicfDot11QosRadioID.setStatus('current')
hpnicfDot11QosAverageQueLen = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11QosAverageQueLen.setStatus('current')
hpnicfDot11QosDropFrameRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11QosDropFrameRatio.setStatus('current')
hpnicfDot11QosAverageDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2, 1, 1, 5), Integer32()).setUnits('Kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11QosAverageDataRate.setStatus('current')
hpnicfDot11QosAcStatisTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2, 2), )
if mibBuilder.loadTexts: hpnicfDot11QosAcStatisTable.setStatus('current')
hpnicfDot11QosAcStatisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2, 2, 1), ).setIndexNames((0, "HPN-ICF-DOT11-WLANEXT-MIB", "hpnicfDot11QosAPID"), (0, "HPN-ICF-DOT11-WLANEXT-MIB", "hpnicfDot11QosRadioID"), (0, "HPN-ICF-DOT11-WLANEXT-MIB", "hpnicfDot11QosAcType"))
if mibBuilder.loadTexts: hpnicfDot11QosAcStatisEntry.setStatus('current')
hpnicfDot11QosAcType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2, 2, 1, 1), HpnicfDot11QosAcType())
if mibBuilder.loadTexts: hpnicfDot11QosAcType.setStatus('current')
hpnicfDot11AcDropFrameCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 7, 2, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11AcDropFrameCnt.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-DOT11-WLANEXT-MIB", hpnicfDot11QosRadioID=hpnicfDot11QosRadioID, hpnicfDot11QosAverageDataRate=hpnicfDot11QosAverageDataRate, hpnicfDot11QosAcStatisTable=hpnicfDot11QosAcStatisTable, hpnicfDot11QosAcStatisEntry=hpnicfDot11QosAcStatisEntry, hpnicfDot11QosAverageQueLen=hpnicfDot11QosAverageQueLen, hpnicfDot11AcDropFrameCnt=hpnicfDot11AcDropFrameCnt, hpnicfDot11RFSignalStatisTable=hpnicfDot11RFSignalStatisTable, hpnicfDot11RFRadioID=hpnicfDot11RFRadioID, hpnicfDot11RFMaxSignalStrength=hpnicfDot11RFMaxSignalStrength, hpnicfDot11QosStatisEntry=hpnicfDot11QosStatisEntry, hpnicfDot11RFGroup=hpnicfDot11RFGroup, PYSNMP_MODULE_ID=hpnicfDot11WLANEXT, hpnicfDot11RFSignalStatisInterv=hpnicfDot11RFSignalStatisInterv, hpnicfDot11RFAPID=hpnicfDot11RFAPID, hpnicfDot11QosAPID=hpnicfDot11QosAPID, hpnicfDot11RFAverageSignalStrength=hpnicfDot11RFAverageSignalStrength, hpnicfDot11RFSignalStatisEntry=hpnicfDot11RFSignalStatisEntry, hpnicfDot11QosStatisTable=hpnicfDot11QosStatisTable, hpnicfDot11QosAcType=hpnicfDot11QosAcType, hpnicfDot11RFMinSignalStrength=hpnicfDot11RFMinSignalStrength, hpnicfDot11QosDropFrameRatio=hpnicfDot11QosDropFrameRatio, hpnicfDot11QosGroup=hpnicfDot11QosGroup, hpnicfDot11WLANEXT=hpnicfDot11WLANEXT)