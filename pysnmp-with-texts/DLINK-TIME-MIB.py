#
# PySNMP MIB module DLINK-TIME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-TIME-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:49:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, IpAddress, Unsigned32, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, NotificationType, ObjectIdentity, Gauge32, MibIdentifier, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "Unsigned32", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "NotificationType", "ObjectIdentity", "Gauge32", "MibIdentifier", "Counter32", "TimeTicks")
TruthValue, DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DateAndTime", "DisplayString", "TextualConvention")
swDlinkTimeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 10))
if mibBuilder.loadTexts: swDlinkTimeMIB.setLastUpdated('0202140000Z')
if mibBuilder.loadTexts: swDlinkTimeMIB.setOrganization('DLink Corporation')
if mibBuilder.loadTexts: swDlinkTimeMIB.setContactInfo('')
if mibBuilder.loadTexts: swDlinkTimeMIB.setDescription('DLink equipments absolute time.')
swSystemTime = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 10, 10))
swSNTP = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 10, 11))
swSummerTime = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 10, 12))
swTimeNotifPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 10, 13))
swTimeCapacity = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 10, 1), Bits().clone(namedValues=NamedValues(("systemTime", 0), ("sntp", 1), ("summerTime", 2), ("realTimeClock", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swTimeCapacity.setStatus('current')
if mibBuilder.loadTexts: swTimeCapacity.setDescription('A string of 8 bits, corresponding to indicates the time capacity supported in the system. If sntp bit(1) is 1 , indicate the SNTP is supported else if sntp bit is 0, the SNTP is not supported and the subtree swSNTP will not supported also. If summerTime bit(2) is 1 ,indicate the SummerTime is supported else if sntp bit is 0, the SummerTime is not supported and the subtree swSummerTime will not supported also. If realTimeClock(3) bit is 1 , indicate the real time clock is supported else if the bit is 0, the real time clock is not supported . Default systemTime bit(0) is 1; indicate the system time is supported. ')
swCurrentClock = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 10, 2), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swCurrentClock.setStatus('current')
if mibBuilder.loadTexts: swCurrentClock.setDescription('The current local date and time for the system. Setting this object is equivalent to setting an automated clock and calendar. The value of the object will track the date and time from the value set. Note that due to hardware limitations some systems may not be able to preserve such meaning across reboots of the system, as indicated by swDlinkClockLostOnReboot. A constant value of all zeros and length 8 indicates the system is not aware of the present date and time. This object may be read-only on some systems.')
swClockLostOnReboot = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 10, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swClockLostOnReboot.setStatus('current')
if mibBuilder.loadTexts: swClockLostOnReboot.setDescription("Indication of whether the system can preserve knowledge of current date and time across a system reboot. A value of 'true' indicates the clock must be reset from some external source each time the system reboots. A value of 'false' indicates the system has the ability to keep time across reboots.")
swSystemCurrentTime = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 10, 10, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSystemCurrentTime.setStatus('current')
if mibBuilder.loadTexts: swSystemCurrentTime.setDescription('the mandatory network time was got from the SNTP server')
swSystemUpTime = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 10, 10, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSystemUpTime.setStatus('current')
if mibBuilder.loadTexts: swSystemUpTime.setDescription('The time (in second) since the network management portion of the system was last re-initialized. It is the same as sysUptime.')
swSystemBootTime = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 10, 10, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSystemBootTime.setStatus('current')
if mibBuilder.loadTexts: swSystemBootTime.setDescription('The boot time of the switch is equal to subtract systemUpTime from swSNTPCurrentTime')
swSystemTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 10, 10, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-779, 839))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSystemTimeZone.setStatus('current')
if mibBuilder.loadTexts: swSystemTimeZone.setDescription('Local time offset in minutes from GMT.')
swSNTPState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 10, 11, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSNTPState.setStatus('current')
if mibBuilder.loadTexts: swSNTPState.setDescription('This object enable/disable the SNTP function.')
swSNTPTimeSource = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 10, 11, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("system", 0), ("server1", 1), ("server2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSNTPTimeSource.setStatus('current')
if mibBuilder.loadTexts: swSNTPTimeSource.setDescription('the SNTP server status for time source changing')
swSNTPServer1IPAddr = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 10, 11, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSNTPServer1IPAddr.setStatus('current')
if mibBuilder.loadTexts: swSNTPServer1IPAddr.setDescription('Configure the SNTP server #1 IP address')
swSNTPServer2IPAddr = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 10, 11, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSNTPServer2IPAddr.setStatus('current')
if mibBuilder.loadTexts: swSNTPServer2IPAddr.setDescription('Configure the SNTP server #2 IP address')
swSNTPPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 10, 11, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 99999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSNTPPollInterval.setStatus('current')
if mibBuilder.loadTexts: swSNTPPollInterval.setDescription('Update time in seconds from SNTP server.')
swSummerTimeStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 10, 12, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disable", 0), ("repeating", 1), ("annual", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSummerTimeStatus.setStatus('current')
if mibBuilder.loadTexts: swSummerTimeStatus.setDescription('An indication of whether the summertime feature is disabled or enabled in reprating or annual mode on this device. When this object is set to repeating,then the summertime frature is enabled and swSummerTimeOffset,swSummerTimeRepeatingStart ,swSummerTimeRepeatingEnd objects are work effectively . When this object is set to annual, then the summertime frature is enabled and swSummerTimeOffset, swAnnualSummerTimeStart, swAnnualSummerTimeEnd objects are work effectively. ')
swSummerTimeOffset = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 10, 12, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440)).clone(60)).setUnits('Minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSummerTimeOffset.setStatus('current')
if mibBuilder.loadTexts: swSummerTimeOffset.setDescription('The value of this object indicates number of minutes to add or to subtract during summertime. This object is not instantiated when swSummerTimeStatus object is set to disable.')
swRepeatSummerTimeStart = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 10, 12, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swRepeatSummerTimeStart.setStatus('current')
if mibBuilder.loadTexts: swRepeatSummerTimeStart.setDescription('Indicates summertime starts at this time every year. octets contents range 1 week 1..4,00 last = 00 2-3 day 1..7 where sunday = 1 saturday = 7 4 month 1..12 where january = 1 december = 12 5 hour 0..23 6 min 0..59 For example, the first Monday in Feb at 13:30pm should be given as 01 00 02 02 0e 1e For the last Tuesday in dec at 1:20am should be given as 00 00 03 0c 01 14 This object is not instantiated when swSummerTimeStatus object is not set to repeating.')
swRepeatSummerTimeEnd = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 10, 12, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swRepeatSummerTimeEnd.setStatus('current')
if mibBuilder.loadTexts: swRepeatSummerTimeEnd.setDescription('Indicates summertime ends at this time every year. octets contents range 1 week 1..5,ff where ff = last 2-3 day 1..7 where sunday = 1 saturday = 7 4 month 1..12 where january = 1 december = 12 5 hour 0..23 6 min 0..59 For example, the third friday in February at 3:30am should be given as 03 00 06 02 03 1e For the first Tuesday in May at 1:20am should be given as 01 00 03 05 01 14 This object is not instantiated when swSummerTimeStatus object is not set to repeating.')
swAnnualSummerTimeStart = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 10, 12, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swAnnualSummerTimeStart.setStatus('current')
if mibBuilder.loadTexts: swAnnualSummerTimeStart.setDescription('Indicates summertime starts at this time every year. octets contents range 1 monthDay 1..31, 2 month 1..12 where january = 1 december = 12 3 hour 0..23 4 min 0..59 For example, the first Feb at 13:30pm should be given as 01 02 0e 1e For the tenth dec at 1:20am should be given as ff 00 03 0c 01 14 This object is not instantiated when swSummerTimeStatus object is not set to annual.')
swAnnualSummerTimeEnd = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 10, 12, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swAnnualSummerTimeEnd.setStatus('current')
if mibBuilder.loadTexts: swAnnualSummerTimeEnd.setDescription('Indicates summertime ends at this time every year. octets contents range 1 monthDay 1..31, 2 month 1..12 where january = 1 december = 12 3 hour 0..23 4 min 0..59 For example, the third February at 3:30am should be given as 03 02 03 1e For the first May at 1:20am should be given as 01 05 01 14 This object is not instantiated when swSummerTimeStatus object is not set to annual.')
mibBuilder.exportSymbols("DLINK-TIME-MIB", swSystemTime=swSystemTime, swSNTP=swSNTP, swSystemCurrentTime=swSystemCurrentTime, swSummerTime=swSummerTime, swSNTPState=swSNTPState, swSNTPPollInterval=swSNTPPollInterval, swAnnualSummerTimeStart=swAnnualSummerTimeStart, swCurrentClock=swCurrentClock, swTimeNotifPrefix=swTimeNotifPrefix, swRepeatSummerTimeStart=swRepeatSummerTimeStart, swSNTPServer2IPAddr=swSNTPServer2IPAddr, swRepeatSummerTimeEnd=swRepeatSummerTimeEnd, swAnnualSummerTimeEnd=swAnnualSummerTimeEnd, swSummerTimeOffset=swSummerTimeOffset, swTimeCapacity=swTimeCapacity, swClockLostOnReboot=swClockLostOnReboot, swSNTPServer1IPAddr=swSNTPServer1IPAddr, PYSNMP_MODULE_ID=swDlinkTimeMIB, swDlinkTimeMIB=swDlinkTimeMIB, swSystemUpTime=swSystemUpTime, swSNTPTimeSource=swSNTPTimeSource, swSystemBootTime=swSystemBootTime, swSystemTimeZone=swSystemTimeZone, swSummerTimeStatus=swSummerTimeStatus)