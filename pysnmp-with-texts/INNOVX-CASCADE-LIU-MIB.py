#
# PySNMP MIB module INNOVX-CASCADE-LIU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INNOVX-CASCADE-LIU-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:53:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
casGroup, = mibBuilder.importSymbols("INNOVX-CORE-MIB", "casGroup")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, IpAddress, Counter32, Unsigned32, TimeTicks, MibIdentifier, iso, Counter64, NotificationType, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "IpAddress", "Counter32", "Unsigned32", "TimeTicks", "MibIdentifier", "iso", "Counter64", "NotificationType", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adminGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 1))
configGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2))
alarmCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3))
diagnostics = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 4))
statusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 5))
cascadeMIBversion = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cascadeMIBversion.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeMIBversion.setDescription("Identifies the version of the MIB as `X.YZT' where: X: Major Revision (1-9) Y: Minor Revision (0-9) Z: Typographical Revision (0-9) T: Test Revision (A-Z) Upon formal release, the test revision will not be present.")
cascadeInService = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inService", 1), ("outOfService", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeInService.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeInService.setDescription('Defines the cascade interface port state. WEBFLAG In Service Out Of Service WEBEND')
cascadeSetFrameType = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("esf", 1), ("d4", 2), ("auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeSetFrameType.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeSetFrameType.setDescription("Defines the line interface framing type as follows: `esf' sets extended superframe format, `d4' sets D4 framing format, `auto' instructs the unit to determine framing WEBFLAG ESF D4 Automatic WEBEND")
cascadeOperFrameType = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("esf", 1), ("d4", 2), ("auto", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cascadeOperFrameType.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeOperFrameType.setDescription("Identifies the line interface framing type acquired by the unit as defined by the `cascadeNetSetFrameType' object as follows: `esf' indicates extended superframe format, `d4' indicates D4 framing format, `auto' indicates the unit is still `acquiring', frame type is indeterminate at this time. WEBFLAG ESF D4 Automatic WEBEND")
cascadeLineCoding = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("b8zs", 1), ("ami", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeLineCoding.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeLineCoding.setDescription("Defines the Zero Code Suppression mechanism for the interface. `b8zs' defines the use of a specified pattern of normal bits and bipolar violations used to replace a sequence of eight zero bits. `ami' (alternate mark inversion) defines a mode wherein no zero code suppression is provided. Therefore ami line encoding does not protect against inadequate ones density. The DSU will enforce an 8x(N+1) minimum ones density requirement when ap553CasLineCoding == `ami' and cascadeDS0Format == `nx64k' and cascadeDS0AllocationScheme == `consecutive'. WEBFLAG B8ZS AMI WEBEND")
cascadeIntfType = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("ds1-auto-lbo", 1), ("ds1-zero-dB", 2), ("ds1-neg7pt5-dB", 3), ("ds1-neg15pt0-dB", 4), ("ds1-neg22pt5-dB", 5), ("dsx1-preeq130-ft", 6), ("dsx1-preeq260-ft", 7), ("dsx1-preeq390-ft", 8), ("dsx1-preeq530-ft", 9), ("dsx1-preeq655-ft", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeIntfType.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeIntfType.setDescription("Defines the operating mode of the interface, and the attenuation or gain. The following values specify operation as a standard DS1 interface, with the specified attenuation: `ds1-auto-lbo' allows the unit to determine the transmit buildout value. `ds1-zero-dB' sets the transmit buildout to 0.0 dB. `ds1-neg7pt5-dB' sets the transmit buildout to -7.5dB. `ds1-neg15pt0-dB' sets the transmit buildout to -15.0dB. `ds1-neg22pt5-dB' sets the transmit buildout to -22.5dB. The following values specify operation as a standard cross-connect DSX-1 interface, with the specified transmitter gain: `dsx1-preeq130-ft' -- transmitter gain for 0 < 130 feet `dsx1-preeq260-ft' -- transmitter gain for 130 < 260 feet `dsx1-preeq390-ft' -- transmitter gain for 260 < 390 feet `dsx1-preeq530-ft' -- transmitter gain for 390 < 530 feet `dsx1-preeq655-ft' -- transmitter gain for 530 < 655 feet WEBFLAG DS1 Auto Line Buildout DS1 0.0dB Line Buildout DS1 -7.5dB Line Buildout DS1 -15.0dB Line Buildout DS1 -22.5dB Line Buildout DSX1 0 - 133 ft Pre-equalization DSX1 133 - 266 ft Pre-equalization DSX1 266 - 399 ft Pre-equalization DSX1 399 - 533 ft Pre-equalization DSX1 533 - 655 ft Pre-equalization WEBEND")
cascadeDS1IntfRcvLevel = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("noSignal", 1), ("pos2toNeg7pt5-dB", 2), ("neg7pt5toNeg15-dB", 3), ("neg15toNeg22pt5-dB", 4), ("lessThanNeg22pt5-dB", 5), ("invalidDSX1intf", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cascadeDS1IntfRcvLevel.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeDS1IntfRcvLevel.setDescription("Identifies the Cascade Interface Receive level for a DS1 type interface. `noSignal' indicates that no T1 signal is detected on the interface, (the `NS' LED on the unit's front panel will be on. `pos2toNeg7pt5-dB'=> + 2.0dB to - 7.5dB DS1 interface receive level `neg7pt5toNeg15-dB'=> - 7.5dB to -15.0dB DS1 interface receive level `neg15toNeg22pt5-dB'=> -15.0dB to -22.5dB DS1 interface receive level `lessThanNeg22pt5-dB'=> less than -22.5dB DS1 interface receive level `invalidDSX1intf=> invalid object, interface type is DSX1 WEBFLAG + 2.0dB to - 7.5dB - 7.5dB to -15.0dB -15.0dB to -22.5dB less than -22.5dB not applicable WEBEND")
cascadeDropAndInsertTable = MibTable((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 7), )
if mibBuilder.loadTexts: cascadeDropAndInsertTable.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeDropAndInsertTable.setDescription('This table defines the channel type for each of the timeslots passthru from LIU to Cascade. This contiguous timeslot bundle is defined via the objects ap553StartingDS0 and ap553NumDS0s from AP553Liu.mib.')
channelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 7, 1), ).setIndexNames((0, "INNOVX-CASCADE-LIU-MIB", "channelIndex"))
if mibBuilder.loadTexts: channelEntry.setStatus('mandatory')
if mibBuilder.loadTexts: channelEntry.setDescription(' Identifies an entry (row) in cascadeDropAndInsertMapTable table.')
channelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelIndex.setStatus('mandatory')
if mibBuilder.loadTexts: channelIndex.setDescription(' Identifies a channel (row)for the time slots - 1-24 for T1 and 1-32 for E1. For E1, 1 = TS0 and 32 = TS31.')
cascadeDropAndInsert = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("clearChannel", 2), ("signallingChannel", 3), ("casChannel", 4), ("tsNotAvailable", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeDropAndInsert.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeDropAndInsert.setDescription(' Rules: 1) For a T1 interface timeslots 25 - 32 are not available and will contain 5 for each of these timeslots. 2) For an E1 interface timeslot 0 is not available and will contain 5 for this timeslot. 3) For an E1 interface timeslot 16 is not available if CAS is enabled. and will contain 4 for this timeslot. CHANNEL TYPE none(1) - This timeslot is dropped at DTE port. clearChannel(2) - all eight bits are passed through to cascade port. signallingChannel(3) - used for voice channels with robbed-bit signalling (for T1 networks). casChannel(4) - used for timeslot 16 when CAS is on when LIU is E1 interface. tsNotAvailable(5) - Used for timeslots 25 - 32 when LIU is T1 interface. Used for timeslot 0 when LIU is E1 interface. WEBFLAG DTE Channel Clear Channel Voice Channel CAS Channel TS Not Avail WEBEND')
cascadeBpvTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("inhibit", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("info", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeBpvTrapSeverity.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeBpvTrapSeverity.setDescription('Controls the reporting and defines the severity of the Cascade Bipolar Violations Alarm when this event occurs and meets the window and threshold requirements for reporting as specified by the associated window and threshold object values below. WEBFLAG Inhibit Critical Major Minor Warning Info WEBEND')
cascadeBpvWindow = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("oneMinute", 1), ("fifteenMinutes", 2), ("oneHour", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeBpvWindow.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeBpvWindow.setDescription("Specifies the sampling window in which to report the Cascade Bipolar Violationslarm condition as active. All other values specify the size of the sampling window in which the event may be reported one time as active, as controlled by the associated mask object value, when the associated obj's threshold condition is met. WEBFLAG One Minute Fifteen Minutes One Hour WEBEND")
cascadeBpvThresh = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("thr1", 1), ("thr10", 2), ("thr100", 3), ("thr1000", 4), ("thr10000", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeBpvThresh.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeBpvThresh.setDescription("Specifies the threshold of events to be exceeded for reporting the Cascade Bipolar Violations alarm condition. When the associated window object value is `report_all' the value of this object is ignored. WEBFLAG 1 10 100 1,000 10,000 WEBEND")
cascadeCrcTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("inhibit", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("info", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeCrcTrapSeverity.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeCrcTrapSeverity.setDescription('Controls the reporting and defines the severity of the Cascade Cyclical Redundancy Check Alarm when this event occurs and meets the window and threshold requirements for reporting as specified by the associated window and threshold object values below. WEBFLAG Inhibit Critical Major Minor Warning Info WEBEND')
cascadeCrcWindow = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("oneMinute", 1), ("fifteenMinutes", 2), ("oneHour", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeCrcWindow.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeCrcWindow.setDescription("Specifies the sampling window in which to report the Cascade Cyclical Redundancy Check alarm condition as active. All other values specify the size of the sampling window in which the event may be reported one time as active, as controlled by the associated mask object value, when the associated obj's threshold condition is met. WEBFLAG One Minute Fifteen Minutes One Hour WEBEND")
cascadeCrcThresh = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("thr1", 1), ("thr10", 2), ("thr100", 3), ("thr1000", 4), ("thr10000", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeCrcThresh.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeCrcThresh.setDescription("Specifies the threshold of events to be exceeded for reporting the Cascade Cyclical Redundancy Check alarm condition. When the associated window object value is `report_all' the value of this object is ignored. WEBFLAG 1 10 100 1,000 10,000 WEBEND")
cascadeLadTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("inhibit", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("info", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeLadTrapSeverity.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeLadTrapSeverity.setDescription('Controls the reporting and defines the severity of the Cascade Low Average Density Alarm when this event occurs and meets the window and threshold requirements for reporting as specified by the associated window and threshold object values below. WEBFLAG Inhibit Critical Major Minor Warning Info WEBEND')
cascadeLadWindow = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("oneMinute", 1), ("fifteenMinutes", 2), ("oneHour", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeLadWindow.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeLadWindow.setDescription("Specifies the sampling window in which to report the Cascade Low Average Density alarm condition as active. All other values specify the size of the sampling window in which the event may be reported one time as active, as controlled by the associated mask object value, when the associated obj's threshold condition is met. WEBFLAG One Minute Fifteen Minutes One Hour WEBEND")
cascadeLadThresh = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("thr1", 1), ("thr10", 2), ("thr100", 3), ("thr1000", 4), ("thr10000", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeLadThresh.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeLadThresh.setDescription("Specifies the threshold of events to be exceeded for reporting the Cascade Low Average Density alarm condition. When the associated window object value is `reportAll' the value of this object is ignored. WEBFLAG 1 10 100 1,000 10,000 WEBEND")
cascadeAisTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("inhibit", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("info", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeAisTrapSeverity.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeAisTrapSeverity.setDescription('Controls the reporting and defines the severity of the Cascade Alarm Indication Signal Alarm when this event occurs. WEBFLAG Inhibit Critical Major Minor Warning Info WEBEND')
cascadeLosTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("inhibit", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("info", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeLosTrapSeverity.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeLosTrapSeverity.setDescription('Controls the reporting and defines the severity of the Cascade Loss of Signal Alarm when this event occurs. WEBFLAG Inhibit Critical Major Minor Warning Info WEBEND')
cascadeOofTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("inhibit", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("info", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeOofTrapSeverity.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeOofTrapSeverity.setDescription('Controls the reporting and defines the severity of the Cascade Out of Frame Alarm when this event occurs. WEBFLAG Inhibit Critical Major Minor Warning Info WEBEND')
cascadeRcdYelTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("inhibit", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("info", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeRcdYelTrapSeverity.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeRcdYelTrapSeverity.setDescription('Controls the reporting and defines the severity of the Cascade Received Yellow Alarm when this event occurs. WEBFLAG Inhibit Critical Major Minor Warning Info WEBEND')
cascadeUssTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("inhibit", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("info", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeUssTrapSeverity.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeUssTrapSeverity.setDescription('Controls the reporting and defines the severity of the Cascade Unavailable Signal State Alarm when this event occurs. WEBFLAG Inhibit Critical Major Minor Warning Info WEBEND')
cascadeDiagTest = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cascadeLineLoopback", 1), ("cascadePayLoadLoopback", 2), ("cascadeStopTest", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeDiagTest.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeDiagTest.setDescription('Specifies the test to be executed, or stops the current test.')
cascadeDiagTestDuration = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("testTime1Min", 1), ("testTime5Mins", 2), ("testTime10Mins", 3), ("testTime20Mins", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeDiagTestDuration.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeDiagTestDuration.setDescription('Defines the length of all LIU diagnostic tests.')
cascadeDiagTestStatus = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("statcascadeLineLoopback", 1), ("statcascadePayLoadLoopback", 2), ("statNoTestinProgress", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cascadeDiagTestStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cascadeDiagTestStatus.setDescription('Displays the test in progress, if any.')
cascadePortStatus = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 5, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cascadePortStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cascadePortStatus.setDescription('A bitwise snapshot of interface port status conditions and EIA signals, where 0 = condition not present, and 1 = condition present, as follows: Octet 1 - CASCADE Interface Port Status bit 7 - n/u bit 6 - n/u bit 5 - n/u bit 4 - n/u bit 3 - Alarm Indication Signal bit 2 - Out Of Frame Alarm bit 1 - Loss Of Signal Alarm bit 0 - Remote Alarm')
mibBuilder.exportSymbols("INNOVX-CASCADE-LIU-MIB", cascadeDiagTestStatus=cascadeDiagTestStatus, alarmCfgGroup=alarmCfgGroup, cascadeOofTrapSeverity=cascadeOofTrapSeverity, cascadeDiagTestDuration=cascadeDiagTestDuration, diagnostics=diagnostics, cascadePortStatus=cascadePortStatus, cascadeLadTrapSeverity=cascadeLadTrapSeverity, cascadeIntfType=cascadeIntfType, cascadeLadThresh=cascadeLadThresh, cascadeAisTrapSeverity=cascadeAisTrapSeverity, cascadeDropAndInsert=cascadeDropAndInsert, cascadeSetFrameType=cascadeSetFrameType, adminGroup=adminGroup, cascadeBpvTrapSeverity=cascadeBpvTrapSeverity, channelIndex=channelIndex, cascadeLadWindow=cascadeLadWindow, cascadeLosTrapSeverity=cascadeLosTrapSeverity, cascadeDiagTest=cascadeDiagTest, cascadeLineCoding=cascadeLineCoding, cascadeCrcTrapSeverity=cascadeCrcTrapSeverity, cascadeCrcThresh=cascadeCrcThresh, cascadeCrcWindow=cascadeCrcWindow, cascadeInService=cascadeInService, cascadeOperFrameType=cascadeOperFrameType, configGroup=configGroup, channelEntry=channelEntry, cascadeBpvWindow=cascadeBpvWindow, cascadeBpvThresh=cascadeBpvThresh, cascadeDS1IntfRcvLevel=cascadeDS1IntfRcvLevel, cascadeRcdYelTrapSeverity=cascadeRcdYelTrapSeverity, cascadeUssTrapSeverity=cascadeUssTrapSeverity, statusGroup=statusGroup, cascadeDropAndInsertTable=cascadeDropAndInsertTable, cascadeMIBversion=cascadeMIBversion)