#
# PySNMP MIB module RFC1406-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RFC1406-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:59:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, transmission, iso, TimeTicks, ModuleIdentity, Gauge32, MibIdentifier, Integer32, Counter32, ObjectIdentity, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "transmission", "iso", "TimeTicks", "ModuleIdentity", "Gauge32", "MibIdentifier", "Integer32", "Counter32", "ObjectIdentity", "Unsigned32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ds1 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 18))
dsx1ConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 18, 6), )
if mibBuilder.loadTexts: dsx1ConfigTable.setStatus('mandatory')
dsx1ConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 18, 6, 1), ).setIndexNames((0, "RFC1406-MIB", "dsx1LineIndex"))
if mibBuilder.loadTexts: dsx1ConfigEntry.setStatus('mandatory')
dsx1LineIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1LineIndex.setStatus('mandatory')
dsx1IfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1IfIndex.setStatus('mandatory')
dsx1TimeElapsed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 899))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TimeElapsed.setStatus('mandatory')
dsx1ValidIntervals = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1ValidIntervals.setStatus('mandatory')
dsx1LineType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("dsx1ESF", 2), ("dsx1D4", 3), ("dsx1E1", 4), ("dsx1E1-CRC", 5), ("dsx1E1-MF", 6), ("dsx1E1-CRC-MF", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1LineType.setStatus('mandatory')
dsx1LineCoding = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("dsx1JBZS", 1), ("dsx1B8ZS", 2), ("dsx1HDB3", 3), ("dsx1ZBTSI", 4), ("dsx1AMI", 5), ("other", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1LineCoding.setStatus('mandatory')
dsx1SendCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("dsx1SendNoCode", 1), ("dsx1SendLineCode", 2), ("dsx1SendPayloadCode", 3), ("dsx1SendResetCode", 4), ("dsx1SendQRS", 5), ("dsx1Send511Pattern", 6), ("dsx1Send3in24Pattern", 7), ("dsx1SendOtherTestPattern", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1SendCode.setStatus('mandatory')
dsx1CircuitIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1CircuitIdentifier.setStatus('mandatory')
dsx1LoopbackConfig = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dsx1NoLoop", 1), ("dsx1PayloadLoop", 2), ("dsx1LineLoop", 3), ("dsx1OtherLoop", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1LoopbackConfig.setStatus('mandatory')
dsx1LineStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8191))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1LineStatus.setStatus('mandatory')
dsx1SignalMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("robbedBit", 2), ("bitOriented", 3), ("messageOriented", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1SignalMode.setStatus('mandatory')
dsx1TransmitClockSource = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loopTiming", 1), ("localTiming", 2), ("throughTiming", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1TransmitClockSource.setStatus('mandatory')
dsx1Fdl = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8))).clone(namedValues=NamedValues(("other", 1), ("dsx1Ansi-T1-403", 2), ("dsx1Att-54016", 4), ("dsx1Fdl-none", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1Fdl.setStatus('mandatory')
dsx1CurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 18, 7), )
if mibBuilder.loadTexts: dsx1CurrentTable.setStatus('mandatory')
dsx1CurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 18, 7, 1), ).setIndexNames((0, "RFC1406-MIB", "dsx1CurrentIndex"))
if mibBuilder.loadTexts: dsx1CurrentEntry.setStatus('mandatory')
dsx1CurrentIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1CurrentIndex.setStatus('mandatory')
dsx1CurrentESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1CurrentESs.setStatus('mandatory')
dsx1CurrentSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1CurrentSESs.setStatus('mandatory')
dsx1CurrentSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1CurrentSEFSs.setStatus('mandatory')
dsx1CurrentUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1CurrentUASs.setStatus('mandatory')
dsx1CurrentCSSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1CurrentCSSs.setStatus('mandatory')
dsx1CurrentPCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1CurrentPCVs.setStatus('mandatory')
dsx1CurrentLESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1CurrentLESs.setStatus('mandatory')
dsx1CurrentBESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1CurrentBESs.setStatus('mandatory')
dsx1CurrentDMs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1CurrentDMs.setStatus('mandatory')
dsx1CurrentLCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1CurrentLCVs.setStatus('mandatory')
dsx1IntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 18, 8), )
if mibBuilder.loadTexts: dsx1IntervalTable.setStatus('mandatory')
dsx1IntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 18, 8, 1), ).setIndexNames((0, "RFC1406-MIB", "dsx1IntervalIndex"), (0, "RFC1406-MIB", "dsx1IntervalNumber"))
if mibBuilder.loadTexts: dsx1IntervalEntry.setStatus('mandatory')
dsx1IntervalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1IntervalIndex.setStatus('mandatory')
dsx1IntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1IntervalNumber.setStatus('mandatory')
dsx1IntervalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1IntervalESs.setStatus('mandatory')
dsx1IntervalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1IntervalSESs.setStatus('mandatory')
dsx1IntervalSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1IntervalSEFSs.setStatus('mandatory')
dsx1IntervalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1IntervalUASs.setStatus('mandatory')
dsx1IntervalCSSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1IntervalCSSs.setStatus('mandatory')
dsx1IntervalPCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1IntervalPCVs.setStatus('mandatory')
dsx1IntervalLESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1IntervalLESs.setStatus('mandatory')
dsx1IntervalBESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1IntervalBESs.setStatus('mandatory')
dsx1IntervalDMs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1IntervalDMs.setStatus('mandatory')
dsx1IntervalLCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1IntervalLCVs.setStatus('mandatory')
dsx1TotalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 18, 9), )
if mibBuilder.loadTexts: dsx1TotalTable.setStatus('mandatory')
dsx1TotalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 18, 9, 1), ).setIndexNames((0, "RFC1406-MIB", "dsx1TotalIndex"))
if mibBuilder.loadTexts: dsx1TotalEntry.setStatus('mandatory')
dsx1TotalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TotalIndex.setStatus('mandatory')
dsx1TotalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TotalESs.setStatus('mandatory')
dsx1TotalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TotalSESs.setStatus('mandatory')
dsx1TotalSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TotalSEFSs.setStatus('mandatory')
dsx1TotalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TotalUASs.setStatus('mandatory')
dsx1TotalCSSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TotalCSSs.setStatus('mandatory')
dsx1TotalPCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TotalPCVs.setStatus('mandatory')
dsx1TotalLESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TotalLESs.setStatus('mandatory')
dsx1TotalBESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TotalBESs.setStatus('mandatory')
dsx1TotalDMs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TotalDMs.setStatus('mandatory')
dsx1TotalLCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TotalLCVs.setStatus('mandatory')
dsx1FarEndCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 18, 10), )
if mibBuilder.loadTexts: dsx1FarEndCurrentTable.setStatus('mandatory')
dsx1FarEndCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 18, 10, 1), ).setIndexNames((0, "RFC1406-MIB", "dsx1FarEndCurrentIndex"))
if mibBuilder.loadTexts: dsx1FarEndCurrentEntry.setStatus('mandatory')
dsx1FarEndCurrentIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndCurrentIndex.setStatus('mandatory')
dsx1FarEndTimeElapsed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 899))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndTimeElapsed.setStatus('mandatory')
dsx1FarEndValidIntervals = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndValidIntervals.setStatus('mandatory')
dsx1FarEndCurrentESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndCurrentESs.setStatus('mandatory')
dsx1FarEndCurrentSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndCurrentSESs.setStatus('mandatory')
dsx1FarEndCurrentSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndCurrentSEFSs.setStatus('mandatory')
dsx1FarEndCurrentUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndCurrentUASs.setStatus('mandatory')
dsx1FarEndCurrentCSSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndCurrentCSSs.setStatus('mandatory')
dsx1FarEndCurrentLESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndCurrentLESs.setStatus('mandatory')
dsx1FarEndCurrentPCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndCurrentPCVs.setStatus('mandatory')
dsx1FarEndCurrentBESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndCurrentBESs.setStatus('mandatory')
dsx1FarEndCurrentDMs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndCurrentDMs.setStatus('mandatory')
dsx1FarEndIntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 18, 11), )
if mibBuilder.loadTexts: dsx1FarEndIntervalTable.setStatus('mandatory')
dsx1FarEndIntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 18, 11, 1), ).setIndexNames((0, "RFC1406-MIB", "dsx1FarEndIntervalIndex"), (0, "RFC1406-MIB", "dsx1FarEndIntervalNumber"))
if mibBuilder.loadTexts: dsx1FarEndIntervalEntry.setStatus('mandatory')
dsx1FarEndIntervalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndIntervalIndex.setStatus('mandatory')
dsx1FarEndIntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndIntervalNumber.setStatus('mandatory')
dsx1FarEndIntervalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndIntervalESs.setStatus('mandatory')
dsx1FarEndIntervalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndIntervalSESs.setStatus('mandatory')
dsx1FarEndIntervalSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndIntervalSEFSs.setStatus('mandatory')
dsx1FarEndIntervalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndIntervalUASs.setStatus('mandatory')
dsx1FarEndIntervalCSSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndIntervalCSSs.setStatus('mandatory')
dsx1FarEndIntervalLESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndIntervalLESs.setStatus('mandatory')
dsx1FarEndIntervalPCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndIntervalPCVs.setStatus('mandatory')
dsx1FarEndIntervalBESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndIntervalBESs.setStatus('mandatory')
dsx1FarEndIntervalDMs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndIntervalDMs.setStatus('mandatory')
dsx1FarEndTotalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 18, 12), )
if mibBuilder.loadTexts: dsx1FarEndTotalTable.setStatus('mandatory')
dsx1FarEndTotalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 18, 12, 1), ).setIndexNames((0, "RFC1406-MIB", "dsx1FarEndTotalIndex"))
if mibBuilder.loadTexts: dsx1FarEndTotalEntry.setStatus('mandatory')
dsx1FarEndTotalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndTotalIndex.setStatus('mandatory')
dsx1FarEndTotalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndTotalESs.setStatus('mandatory')
dsx1FarEndTotalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndTotalSESs.setStatus('mandatory')
dsx1FarEndTotalSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndTotalSEFSs.setStatus('mandatory')
dsx1FarEndTotalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndTotalUASs.setStatus('mandatory')
dsx1FarEndTotalCSSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndTotalCSSs.setStatus('mandatory')
dsx1FarEndTotalLESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndTotalLESs.setStatus('mandatory')
dsx1FarEndTotalPCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndTotalPCVs.setStatus('mandatory')
dsx1FarEndTotalBESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndTotalBESs.setStatus('mandatory')
dsx1FarEndTotalDMs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FarEndTotalDMs.setStatus('mandatory')
dsx1FracTable = MibTable((1, 3, 6, 1, 2, 1, 10, 18, 13), )
if mibBuilder.loadTexts: dsx1FracTable.setStatus('mandatory')
dsx1FracEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 18, 13, 1), ).setIndexNames((0, "RFC1406-MIB", "dsx1FracIndex"), (0, "RFC1406-MIB", "dsx1FracNumber"))
if mibBuilder.loadTexts: dsx1FracEntry.setStatus('mandatory')
dsx1FracIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 13, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FracIndex.setStatus('mandatory')
dsx1FracNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 13, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1FracNumber.setStatus('mandatory')
dsx1FracIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 13, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1FracIfIndex.setStatus('mandatory')
mibBuilder.exportSymbols("RFC1406-MIB", dsx1FarEndIntervalTable=dsx1FarEndIntervalTable, dsx1IntervalLESs=dsx1IntervalLESs, dsx1CurrentCSSs=dsx1CurrentCSSs, dsx1SendCode=dsx1SendCode, dsx1FarEndTotalESs=dsx1FarEndTotalESs, dsx1FarEndTotalBESs=dsx1FarEndTotalBESs, dsx1TotalUASs=dsx1TotalUASs, dsx1TotalTable=dsx1TotalTable, dsx1TransmitClockSource=dsx1TransmitClockSource, dsx1IntervalTable=dsx1IntervalTable, dsx1FarEndCurrentUASs=dsx1FarEndCurrentUASs, dsx1TotalEntry=dsx1TotalEntry, dsx1FarEndIntervalCSSs=dsx1FarEndIntervalCSSs, dsx1FarEndIntervalUASs=dsx1FarEndIntervalUASs, dsx1LineStatus=dsx1LineStatus, dsx1CurrentEntry=dsx1CurrentEntry, dsx1IntervalPCVs=dsx1IntervalPCVs, dsx1FarEndCurrentESs=dsx1FarEndCurrentESs, dsx1IntervalEntry=dsx1IntervalEntry, dsx1FarEndCurrentSEFSs=dsx1FarEndCurrentSEFSs, dsx1LoopbackConfig=dsx1LoopbackConfig, dsx1CurrentDMs=dsx1CurrentDMs, dsx1FarEndCurrentEntry=dsx1FarEndCurrentEntry, dsx1FarEndIntervalIndex=dsx1FarEndIntervalIndex, dsx1TotalPCVs=dsx1TotalPCVs, dsx1FarEndIntervalDMs=dsx1FarEndIntervalDMs, dsx1IfIndex=dsx1IfIndex, dsx1FarEndCurrentDMs=dsx1FarEndCurrentDMs, dsx1FarEndCurrentPCVs=dsx1FarEndCurrentPCVs, dsx1ValidIntervals=dsx1ValidIntervals, dsx1FarEndIntervalLESs=dsx1FarEndIntervalLESs, dsx1FarEndTotalSESs=dsx1FarEndTotalSESs, dsx1FarEndTimeElapsed=dsx1FarEndTimeElapsed, dsx1CurrentLCVs=dsx1CurrentLCVs, dsx1SignalMode=dsx1SignalMode, dsx1CurrentSEFSs=dsx1CurrentSEFSs, dsx1CurrentLESs=dsx1CurrentLESs, dsx1TotalBESs=dsx1TotalBESs, dsx1TotalLCVs=dsx1TotalLCVs, dsx1FarEndIntervalESs=dsx1FarEndIntervalESs, dsx1FarEndCurrentCSSs=dsx1FarEndCurrentCSSs, dsx1FarEndValidIntervals=dsx1FarEndValidIntervals, dsx1FarEndIntervalSEFSs=dsx1FarEndIntervalSEFSs, dsx1FarEndTotalEntry=dsx1FarEndTotalEntry, dsx1TotalLESs=dsx1TotalLESs, dsx1FarEndCurrentIndex=dsx1FarEndCurrentIndex, dsx1FarEndTotalLESs=dsx1FarEndTotalLESs, dsx1ConfigEntry=dsx1ConfigEntry, dsx1FarEndTotalSEFSs=dsx1FarEndTotalSEFSs, dsx1FarEndCurrentTable=dsx1FarEndCurrentTable, dsx1CurrentUASs=dsx1CurrentUASs, dsx1CircuitIdentifier=dsx1CircuitIdentifier, dsx1IntervalLCVs=dsx1IntervalLCVs, dsx1CurrentSESs=dsx1CurrentSESs, dsx1IntervalUASs=dsx1IntervalUASs, ds1=ds1, dsx1FarEndTotalUASs=dsx1FarEndTotalUASs, dsx1ConfigTable=dsx1ConfigTable, dsx1TotalCSSs=dsx1TotalCSSs, dsx1CurrentESs=dsx1CurrentESs, dsx1FracIfIndex=dsx1FracIfIndex, dsx1IntervalBESs=dsx1IntervalBESs, dsx1CurrentBESs=dsx1CurrentBESs, dsx1FracTable=dsx1FracTable, dsx1FarEndIntervalPCVs=dsx1FarEndIntervalPCVs, dsx1FarEndTotalDMs=dsx1FarEndTotalDMs, dsx1TotalDMs=dsx1TotalDMs, dsx1FarEndIntervalNumber=dsx1FarEndIntervalNumber, dsx1FracIndex=dsx1FracIndex, dsx1FarEndTotalPCVs=dsx1FarEndTotalPCVs, dsx1CurrentTable=dsx1CurrentTable, dsx1IntervalESs=dsx1IntervalESs, dsx1IntervalNumber=dsx1IntervalNumber, dsx1Fdl=dsx1Fdl, dsx1CurrentPCVs=dsx1CurrentPCVs, dsx1IntervalSEFSs=dsx1IntervalSEFSs, dsx1FarEndCurrentLESs=dsx1FarEndCurrentLESs, dsx1IntervalCSSs=dsx1IntervalCSSs, dsx1FarEndCurrentSESs=dsx1FarEndCurrentSESs, dsx1LineCoding=dsx1LineCoding, dsx1IntervalIndex=dsx1IntervalIndex, dsx1TotalESs=dsx1TotalESs, dsx1FarEndCurrentBESs=dsx1FarEndCurrentBESs, dsx1FarEndIntervalBESs=dsx1FarEndIntervalBESs, dsx1FracEntry=dsx1FracEntry, dsx1FarEndIntervalSESs=dsx1FarEndIntervalSESs, dsx1IntervalDMs=dsx1IntervalDMs, dsx1FarEndTotalCSSs=dsx1FarEndTotalCSSs, dsx1FarEndTotalTable=dsx1FarEndTotalTable, dsx1FarEndTotalIndex=dsx1FarEndTotalIndex, dsx1TimeElapsed=dsx1TimeElapsed, dsx1TotalIndex=dsx1TotalIndex, dsx1TotalSESs=dsx1TotalSESs, dsx1CurrentIndex=dsx1CurrentIndex, dsx1LineType=dsx1LineType, dsx1LineIndex=dsx1LineIndex, dsx1FarEndIntervalEntry=dsx1FarEndIntervalEntry, dsx1TotalSEFSs=dsx1TotalSEFSs, dsx1FracNumber=dsx1FracNumber, dsx1IntervalSESs=dsx1IntervalSESs)