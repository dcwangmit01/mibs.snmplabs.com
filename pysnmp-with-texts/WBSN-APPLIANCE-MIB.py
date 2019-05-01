#
# PySNMP MIB module WBSN-APPLIANCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WBSN-APPLIANCE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:36:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, Unsigned32, IpAddress, MibIdentifier, ModuleIdentity, NotificationType, Bits, TimeTicks, Counter32, ObjectIdentity, Integer32, Gauge32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Unsigned32", "IpAddress", "MibIdentifier", "ModuleIdentity", "NotificationType", "Bits", "TimeTicks", "Counter32", "ObjectIdentity", "Integer32", "Gauge32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
memSwapErrorMsg, memTotalSwap, ssCpuUser, ssCpuSystem, dskErrorMsg, memCached, memTotalFree, memErrorName, fileName, ssErrorName, fileErrorMsg, memTotalReal, memAvailReal, memBuffer, ssCpuIdle, dskPath, memShared, memAvailSwap = mibBuilder.importSymbols("UCD-SNMP-MIB", "memSwapErrorMsg", "memTotalSwap", "ssCpuUser", "ssCpuSystem", "dskErrorMsg", "memCached", "memTotalFree", "memErrorName", "fileName", "ssErrorName", "fileErrorMsg", "memTotalReal", "memAvailReal", "memBuffer", "ssCpuIdle", "dskPath", "memShared", "memAvailSwap")
websense = ModuleIdentity((1, 3, 6, 1, 4, 1, 23365))
if mibBuilder.loadTexts: websense.setLastUpdated('201202200000Z')
if mibBuilder.loadTexts: websense.setOrganization('Websense, Inc.')
if mibBuilder.loadTexts: websense.setContactInfo('http://www.websense.com')
if mibBuilder.loadTexts: websense.setDescription('Websense Appliance SNMP')
appliance = MibIdentifier((1, 3, 6, 1, 4, 1, 23365, 10000))
moduleName = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleName.setStatus('current')
if mibBuilder.loadTexts: moduleName.setDescription('The name of current module: Appliance Controller, Websense Content Gateway, Websense Web Security, Network Agent, Websense Email Security Gateway')
memUsageFlag = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memUsageFlag.setStatus('current')
if mibBuilder.loadTexts: memUsageFlag.setDescription('The flag to indicate memory usage exceed')
vmTable = MibTable((1, 3, 6, 1, 4, 1, 23365, 10000, 3), )
if mibBuilder.loadTexts: vmTable.setStatus('current')
if mibBuilder.loadTexts: vmTable.setDescription('A list of virtual machines.')
vmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23365, 10000, 3, 1), ).setIndexNames((0, "WBSN-APPLIANCE-MIB", "vmName"))
if mibBuilder.loadTexts: vmEntry.setStatus('current')
if mibBuilder.loadTexts: vmEntry.setDescription('A concept row of virtual machine table.')
vmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("online", 0), ("offline", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmStatus.setStatus('current')
if mibBuilder.loadTexts: vmStatus.setDescription('The status of virtual machine.')
vmName = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmName.setStatus('current')
if mibBuilder.loadTexts: vmName.setDescription('The name of virtual machine.')
hostname = MibIdentifier((1, 3, 6, 1, 4, 1, 23365, 10000, 4))
hostnameChangeFlag = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostnameChangeFlag.setStatus('current')
if mibBuilder.loadTexts: hostnameChangeFlag.setDescription('The flag to indicate hostname change.')
prevHostname = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 4, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prevHostname.setStatus('current')
if mibBuilder.loadTexts: prevHostname.setDescription('The hostname before changed.')
currHostname = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 4, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currHostname.setStatus('current')
if mibBuilder.loadTexts: currHostname.setDescription('The current hostname.')
ifaTable = MibTable((1, 3, 6, 1, 4, 1, 23365, 10000, 5), )
if mibBuilder.loadTexts: ifaTable.setStatus('current')
if mibBuilder.loadTexts: ifaTable.setDescription('A list of monitoring interface IP addresses.')
ifaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1), ).setIndexNames((0, "WBSN-APPLIANCE-MIB", "ifaName"))
if mibBuilder.loadTexts: ifaEntry.setStatus('current')
if mibBuilder.loadTexts: ifaEntry.setDescription('A concept row of monitoring interface IP address table.')
ifaChangeFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaChangeFlag.setStatus('current')
if mibBuilder.loadTexts: ifaChangeFlag.setDescription('The flag to indicate whether the IP address of monitoring interface has been changed.')
ifaName = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaName.setStatus('current')
if mibBuilder.loadTexts: ifaName.setDescription('The name of monitoring interface.')
ifaPrevAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaPrevAddress.setStatus('current')
if mibBuilder.loadTexts: ifaPrevAddress.setDescription('The previous IP address of monitoring interface.')
ifaCurrAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaCurrAddress.setStatus('current')
if mibBuilder.loadTexts: ifaCurrAddress.setDescription('The current IP address of monitoring interface.')
ifaSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaSpeed.setStatus('current')
if mibBuilder.loadTexts: ifaSpeed.setDescription('The speed of monitoring interface.')
ifaInboundExceedFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaInboundExceedFlag.setStatus('current')
if mibBuilder.loadTexts: ifaInboundExceedFlag.setDescription('The flag to indicate whether the inbound network traffic of monitoring interface exceeds its threhold.')
ifaOutboundExceedFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaOutboundExceedFlag.setStatus('current')
if mibBuilder.loadTexts: ifaOutboundExceedFlag.setDescription('The flag to indicate whether the outbound network traffic of monitoring interface exceeds its threhold.')
ifaPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaPhysAddress.setStatus('current')
if mibBuilder.loadTexts: ifaPhysAddress.setDescription('The physical address of monitoring interface.')
ifaChangeFlagv6 = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaChangeFlagv6.setStatus('current')
if mibBuilder.loadTexts: ifaChangeFlagv6.setDescription('The flag to indicate whether the IPv6 address of monitoring interface has been changed.')
ifaPrevAddressv6 = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaPrevAddressv6.setStatus('current')
if mibBuilder.loadTexts: ifaPrevAddressv6.setDescription('The previous IPv6 address of monitoring interface.')
ifaCurrAddressv6 = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 5, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifaCurrAddressv6.setStatus('current')
if mibBuilder.loadTexts: ifaCurrAddressv6.setDescription('The current IPv6 address of monitoring interface.')
raidStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 23365, 10000, 6))
raidErrorFlag = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidErrorFlag.setStatus('current')
if mibBuilder.loadTexts: raidErrorFlag.setDescription('The flag is set when disk error is detected.')
dskPhysicalNr = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 6, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskPhysicalNr.setStatus('current')
if mibBuilder.loadTexts: dskPhysicalNr.setDescription('The number of physical disks in the RAID controller.')
dskCriticalNr = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 6, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskCriticalNr.setStatus('current')
if mibBuilder.loadTexts: dskCriticalNr.setDescription('The number of physical disks in critical state.')
dskFailedNr = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 6, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskFailedNr.setStatus('current')
if mibBuilder.loadTexts: dskFailedNr.setDescription('The number of physical disks in failed state.')
dskPhysErrMsg = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 6, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskPhysErrMsg.setStatus('current')
if mibBuilder.loadTexts: dskPhysErrMsg.setDescription('The error message to describe the abnormal state of physical disks.')
dskVirtualNr = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 6, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskVirtualNr.setStatus('current')
if mibBuilder.loadTexts: dskVirtualNr.setDescription('The number of virtual drives in the RAID controller.')
dskDegradedNr = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 6, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskDegradedNr.setStatus('current')
if mibBuilder.loadTexts: dskDegradedNr.setDescription('The number of degraded virtual drives.')
dskOfflineNr = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 6, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskOfflineNr.setStatus('current')
if mibBuilder.loadTexts: dskOfflineNr.setDescription('The number of offline virtual drives.')
svcTable = MibTable((1, 3, 6, 1, 4, 1, 23365, 10000, 7), )
if mibBuilder.loadTexts: svcTable.setStatus('current')
if mibBuilder.loadTexts: svcTable.setDescription('A list of service entries.')
svcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23365, 10000, 7, 1), ).setIndexNames((0, "WBSN-APPLIANCE-MIB", "svcName"))
if mibBuilder.loadTexts: svcEntry.setStatus('current')
if mibBuilder.loadTexts: svcEntry.setDescription('A concept row of service table.')
svcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 0), ("down", 1), ("yellow", 2), ("resetting", 3), ("disabled", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcStatus.setStatus('current')
if mibBuilder.loadTexts: svcStatus.setDescription('The status of service.')
svcName = MibTableColumn((1, 3, 6, 1, 4, 1, 23365, 10000, 7, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcName.setStatus('current')
if mibBuilder.loadTexts: svcName.setDescription('The name of service.')
loadAvg = MibIdentifier((1, 3, 6, 1, 4, 1, 23365, 10000, 8))
loadErrorFlag = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loadErrorFlag.setStatus('current')
if mibBuilder.loadTexts: loadErrorFlag.setDescription('The flag is set when load average limit is met.')
loadName = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 8, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loadName.setStatus('current')
if mibBuilder.loadTexts: loadName.setDescription('The load name.')
loadErrorMessage = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 8, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loadErrorMessage.setStatus('current')
if mibBuilder.loadTexts: loadErrorMessage.setDescription('The message to describe current load error.')
wsAlert = MibIdentifier((1, 3, 6, 1, 4, 1, 23365, 10000, 9))
wsAlertMessage = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 9, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsAlertMessage.setStatus('current')
if mibBuilder.loadTexts: wsAlertMessage.setDescription('The detailed message to describe current alert.')
evtInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23365, 10000, 10))
evtTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 10, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: evtTimestamp.setStatus('current')
if mibBuilder.loadTexts: evtTimestamp.setDescription('Timestamp when current event occurred')
evtDir = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 10, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("assertion", 0), ("deassertion", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: evtDir.setStatus('current')
if mibBuilder.loadTexts: evtDir.setDescription('The direction of the event')
evtSensor = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 10, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: evtSensor.setStatus('current')
if mibBuilder.loadTexts: evtSensor.setDescription('The name of sensor: Power Supply, Temperature, Fan, Voltage, System ACPI Power State, Event Logging Disabled, Physical Security (Chassis Intrusion), Battery')
evtDesc = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 10, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: evtDesc.setStatus('current')
if mibBuilder.loadTexts: evtDesc.setDescription('The name of current event')
triggerReading = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 10, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerReading.setStatus('current')
if mibBuilder.loadTexts: triggerReading.setDescription('The trigger reading of sensor')
triggerThreshold = MibScalar((1, 3, 6, 1, 4, 1, 23365, 10000, 10, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerThreshold.setStatus('current')
if mibBuilder.loadTexts: triggerThreshold.setDescription('The threshold to trigger this event')
errorClear = MibIdentifier((1, 3, 6, 1, 4, 1, 23365, 10000, 10000))
testEvent = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,10))
if mibBuilder.loadTexts: testEvent.setDescription(' Websense Alert: this event is for testing use')
cpuMaxUsageExceed = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1000)).setObjects(("UCD-SNMP-MIB", "ssErrorName"), ("UCD-SNMP-MIB", "ssCpuUser"), ("UCD-SNMP-MIB", "ssCpuSystem"), ("UCD-SNMP-MIB", "ssCpuIdle"))
if mibBuilder.loadTexts: cpuMaxUsageExceed.setDescription(' Websense Alert: high CPU usage')
cpuMaxUsageExceedClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,1000)).setObjects(("UCD-SNMP-MIB", "ssErrorName"), ("UCD-SNMP-MIB", "ssCpuUser"), ("UCD-SNMP-MIB", "ssCpuSystem"), ("UCD-SNMP-MIB", "ssCpuIdle"))
if mibBuilder.loadTexts: cpuMaxUsageExceedClear.setDescription(" Websense Alert: 'high CPU usage' is cleared")
memMaxUsageExceed = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1001)).setObjects(("UCD-SNMP-MIB", "memTotalReal"), ("UCD-SNMP-MIB", "memAvailReal"), ("UCD-SNMP-MIB", "memTotalFree"), ("UCD-SNMP-MIB", "memShared"), ("UCD-SNMP-MIB", "memBuffer"), ("UCD-SNMP-MIB", "memCached"), ("UCD-SNMP-MIB", "memTotalSwap"), ("UCD-SNMP-MIB", "memAvailSwap"))
if mibBuilder.loadTexts: memMaxUsageExceed.setDescription(' Websense Alert: high memory usage')
memMaxUsageExceedClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,1001)).setObjects(("UCD-SNMP-MIB", "memTotalReal"), ("UCD-SNMP-MIB", "memAvailReal"), ("UCD-SNMP-MIB", "memTotalFree"), ("UCD-SNMP-MIB", "memShared"), ("UCD-SNMP-MIB", "memBuffer"), ("UCD-SNMP-MIB", "memCached"), ("UCD-SNMP-MIB", "memTotalSwap"), ("UCD-SNMP-MIB", "memAvailSwap"))
if mibBuilder.loadTexts: memMaxUsageExceedClear.setDescription(" Websense Alert: 'high memory usage' is cleared")
networkMaxBandwidthExceed = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1002)).setObjects(("WBSN-APPLIANCE-MIB", "ifaName"), ("WBSN-APPLIANCE-MIB", "ifaCurrAddress"), ("WBSN-APPLIANCE-MIB", "ifaSpeed"), ("WBSN-APPLIANCE-MIB", "ifaPhysAddress"))
if mibBuilder.loadTexts: networkMaxBandwidthExceed.setDescription(' Websense Alert: heavy network traffic on interface')
networkMaxBandwidthExceedClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,1002)).setObjects(("WBSN-APPLIANCE-MIB", "ifaName"), ("WBSN-APPLIANCE-MIB", "ifaCurrAddress"), ("WBSN-APPLIANCE-MIB", "ifaSpeed"), ("WBSN-APPLIANCE-MIB", "ifaPhysAddress"))
if mibBuilder.loadTexts: networkMaxBandwidthExceedClear.setDescription(" Websense Alert: 'heavy network traffic on interface' is cleared")
diskFreeMinSizeExceed = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1003)).setObjects(("UCD-SNMP-MIB", "dskPath"), ("UCD-SNMP-MIB", "dskErrorMsg"))
if mibBuilder.loadTexts: diskFreeMinSizeExceed.setDescription(' Websense Alert: low free disk space')
diskFreeMinSizeExceedClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,1003)).setObjects(("UCD-SNMP-MIB", "dskPath"), ("UCD-SNMP-MIB", "dskErrorMsg"))
if mibBuilder.loadTexts: diskFreeMinSizeExceedClear.setDescription(" Websense Alert: 'low free disk space' is cleared")
swapMinFreeExceed = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1004)).setObjects(("UCD-SNMP-MIB", "memErrorName"), ("UCD-SNMP-MIB", "memSwapErrorMsg"))
if mibBuilder.loadTexts: swapMinFreeExceed.setDescription(' Websense Alert: low free swap space')
swapMinFreeExceedClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,1004)).setObjects(("UCD-SNMP-MIB", "memErrorName"), ("UCD-SNMP-MIB", "memSwapErrorMsg"))
if mibBuilder.loadTexts: swapMinFreeExceedClear.setDescription(" Websense Alert: 'low free swap space' is cleared")
systemLoad = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1005)).setObjects(("WBSN-APPLIANCE-MIB", "loadName"), ("WBSN-APPLIANCE-MIB", "loadErrorMessage"))
if mibBuilder.loadTexts: systemLoad.setDescription(' Websense Alert: heavy system load')
systemLoadClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,1005)).setObjects(("WBSN-APPLIANCE-MIB", "loadName"), ("WBSN-APPLIANCE-MIB", "loadErrorMessage"))
if mibBuilder.loadTexts: systemLoadClear.setDescription(" Websense Alert: 'heavy system load' is cleared")
logFileMaxSizeExceed = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1006)).setObjects(("UCD-SNMP-MIB", "fileName"), ("UCD-SNMP-MIB", "fileErrorMsg"))
if mibBuilder.loadTexts: logFileMaxSizeExceed.setDescription(' Websense Alert: too large log file size')
logFileMaxSizeExceedClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,1006)).setObjects(("UCD-SNMP-MIB", "fileName"), ("UCD-SNMP-MIB", "fileErrorMsg"))
if mibBuilder.loadTexts: logFileMaxSizeExceedClear.setDescription(" Websense Alert: 'too large log file size' is cleared")
logCacheMinFreeExceed = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1007)).setObjects(("WBSN-APPLIANCE-MIB", "wsAlertMessage"))
if mibBuilder.loadTexts: logCacheMinFreeExceed.setDescription(' Websense Alert: low free log cache space')
logCacheMinFreeExceedClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,1007)).setObjects(("WBSN-APPLIANCE-MIB", "wsAlertMessage"))
if mibBuilder.loadTexts: logCacheMinFreeExceedClear.setDescription(" Websense Alert: 'low free log cache space' is cleared")
moduleDown = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1050)).setObjects(("WBSN-APPLIANCE-MIB", "vmName"))
if mibBuilder.loadTexts: moduleDown.setDescription(' Websense Alert: appliance module down')
moduleDownClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,1050)).setObjects(("WBSN-APPLIANCE-MIB", "vmName"))
if mibBuilder.loadTexts: moduleDownClear.setDescription(" Websense Alert: 'appliance module down' is cleared")
serviceDown = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1051)).setObjects(("WBSN-APPLIANCE-MIB", "svcStatus"), ("WBSN-APPLIANCE-MIB", "svcName"))
if mibBuilder.loadTexts: serviceDown.setDescription(' Websense Alert: appliance service down')
serviceDownClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,1051)).setObjects(("WBSN-APPLIANCE-MIB", "svcStatus"), ("WBSN-APPLIANCE-MIB", "svcName"))
if mibBuilder.loadTexts: serviceDownClear.setDescription(" Websense Alert: 'appliance service down' is cleared")
backupFailure = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1052)).setObjects(("WBSN-APPLIANCE-MIB", "wsAlertMessage"))
if mibBuilder.loadTexts: backupFailure.setDescription(' Websense Alert: appliance backup failure')
logServerConnectionLost = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1053)).setObjects(("WBSN-APPLIANCE-MIB", "wsAlertMessage"))
if mibBuilder.loadTexts: logServerConnectionLost.setDescription(' Websense Alert: log server connection lost')
logServerConnectionLostClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,1053)).setObjects(("WBSN-APPLIANCE-MIB", "wsAlertMessage"))
if mibBuilder.loadTexts: logServerConnectionLostClear.setDescription(" Websense Alert: 'log server connection lost' is cleared")
hostnameChange = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1061)).setObjects(("WBSN-APPLIANCE-MIB", "prevHostname"), ("WBSN-APPLIANCE-MIB", "currHostname"))
if mibBuilder.loadTexts: hostnameChange.setDescription(' Websense Alert: appliance hostname changed')
ipAddressChange = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,1062)).setObjects(("WBSN-APPLIANCE-MIB", "ifaName"), ("WBSN-APPLIANCE-MIB", "ifaPrevAddress"), ("WBSN-APPLIANCE-MIB", "ifaCurrAddress"), ("WBSN-APPLIANCE-MIB", "ifaPrevAddressv6"), ("WBSN-APPLIANCE-MIB", "ifaCurrAddressv6"))
if mibBuilder.loadTexts: ipAddressChange.setDescription(' Websense Alert: appliance IP address changed')
powerSupply = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,2001)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
if mibBuilder.loadTexts: powerSupply.setDescription(' Websense Alert: appliance power supply warning')
powerSupplyClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,2001)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
if mibBuilder.loadTexts: powerSupplyClear.setDescription(" Websense Alert: 'appliance power supply warning' is cleared")
redundancy = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,2002)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
if mibBuilder.loadTexts: redundancy.setDescription(' Websense Alert: appliance redundancy warning')
redundancyClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,2002)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
if mibBuilder.loadTexts: redundancyClear.setDescription(" Websense Alert: 'appliance redundancy warning' is cleared")
temps = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,2003)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"), ("WBSN-APPLIANCE-MIB", "triggerReading"), ("WBSN-APPLIANCE-MIB", "triggerThreshold"))
if mibBuilder.loadTexts: temps.setDescription(' Websense Alert: appliance temperatures warning')
tempsClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,2003)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"), ("WBSN-APPLIANCE-MIB", "triggerReading"), ("WBSN-APPLIANCE-MIB", "triggerThreshold"))
if mibBuilder.loadTexts: tempsClear.setDescription(" Websense Alert: 'appliance temperatures warning' is cleared")
fans = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,2004)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"), ("WBSN-APPLIANCE-MIB", "triggerReading"), ("WBSN-APPLIANCE-MIB", "triggerThreshold"))
if mibBuilder.loadTexts: fans.setDescription(' Websense Alert: appliance fans warning')
fansClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,2004)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"), ("WBSN-APPLIANCE-MIB", "triggerReading"), ("WBSN-APPLIANCE-MIB", "triggerThreshold"))
if mibBuilder.loadTexts: fansClear.setDescription(" Websense Alert: 'appliance fans warning' is cleared")
volt = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,2005)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"), ("WBSN-APPLIANCE-MIB", "triggerReading"), ("WBSN-APPLIANCE-MIB", "triggerThreshold"))
if mibBuilder.loadTexts: volt.setDescription(' Websense Alert: appliance voltages warning')
voltClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,2005)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"), ("WBSN-APPLIANCE-MIB", "triggerReading"), ("WBSN-APPLIANCE-MIB", "triggerThreshold"))
if mibBuilder.loadTexts: voltClear.setDescription(" Websense Alert: 'appliance voltages warning' is cleared")
logs = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,2006)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
if mibBuilder.loadTexts: logs.setDescription(' Websense Alert: appliance logs warning')
logsClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,2006)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
if mibBuilder.loadTexts: logsClear.setDescription(" Websense Alert: 'appliance logs warning' is cleared")
mem = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,2007)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
if mibBuilder.loadTexts: mem.setDescription(' Websense Alert: appliance memory warning')
memClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,2007)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
if mibBuilder.loadTexts: memClear.setDescription(" Websense Alert: 'appliance memory warning' is cleared")
intrusion = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,2008)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
if mibBuilder.loadTexts: intrusion.setDescription(' Websense Alert: appliance chassis intrusion detected')
intrusionClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,2008)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
if mibBuilder.loadTexts: intrusionClear.setDescription(" Websense Alert: 'appliance chassis intrusion detected' is cleared")
battery = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,2009)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
if mibBuilder.loadTexts: battery.setDescription(' Websense Alert: appliance battery warning')
batteryClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,2009)).setObjects(("WBSN-APPLIANCE-MIB", "evtTimestamp"), ("WBSN-APPLIANCE-MIB", "evtDir"), ("WBSN-APPLIANCE-MIB", "evtSensor"), ("WBSN-APPLIANCE-MIB", "evtDesc"))
if mibBuilder.loadTexts: batteryClear.setDescription(" Websense Alert: 'appliance battery warning' is cleared")
raid = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000) + (0,2010)).setObjects(("WBSN-APPLIANCE-MIB", "dskPhysicalNr"), ("WBSN-APPLIANCE-MIB", "dskCriticalNr"), ("WBSN-APPLIANCE-MIB", "dskFailedNr"), ("WBSN-APPLIANCE-MIB", "dskPhysErrMsg"), ("WBSN-APPLIANCE-MIB", "dskVirtualNr"), ("WBSN-APPLIANCE-MIB", "dskDegradedNr"), ("WBSN-APPLIANCE-MIB", "dskOfflineNr"))
if mibBuilder.loadTexts: raid.setDescription(' Websense Alert: appliance RAID controller warning')
raidClear = NotificationType((1, 3, 6, 1, 4, 1, 23365, 10000, 10000) + (0,2010)).setObjects(("WBSN-APPLIANCE-MIB", "dskPhysicalNr"), ("WBSN-APPLIANCE-MIB", "dskCriticalNr"), ("WBSN-APPLIANCE-MIB", "dskFailedNr"), ("WBSN-APPLIANCE-MIB", "dskPhysErrMsg"), ("WBSN-APPLIANCE-MIB", "dskVirtualNr"), ("WBSN-APPLIANCE-MIB", "dskDegradedNr"), ("WBSN-APPLIANCE-MIB", "dskOfflineNr"))
if mibBuilder.loadTexts: raidClear.setDescription(" Websense Alert: 'appliance RAID controller warning' is cleared")
mibBuilder.exportSymbols("WBSN-APPLIANCE-MIB", ifaCurrAddress=ifaCurrAddress, tempsClear=tempsClear, backupFailure=backupFailure, logServerConnectionLost=logServerConnectionLost, dskOfflineNr=dskOfflineNr, PYSNMP_MODULE_ID=websense, ifaChangeFlagv6=ifaChangeFlagv6, loadName=loadName, triggerThreshold=triggerThreshold, cpuMaxUsageExceedClear=cpuMaxUsageExceedClear, hostname=hostname, prevHostname=prevHostname, raidStatus=raidStatus, logFileMaxSizeExceed=logFileMaxSizeExceed, voltClear=voltClear, logsClear=logsClear, dskDegradedNr=dskDegradedNr, memMaxUsageExceed=memMaxUsageExceed, svcEntry=svcEntry, redundancyClear=redundancyClear, cpuMaxUsageExceed=cpuMaxUsageExceed, memUsageFlag=memUsageFlag, dskFailedNr=dskFailedNr, loadErrorMessage=loadErrorMessage, logCacheMinFreeExceedClear=logCacheMinFreeExceedClear, appliance=appliance, logFileMaxSizeExceedClear=logFileMaxSizeExceedClear, systemLoadClear=systemLoadClear, memClear=memClear, ifaPrevAddress=ifaPrevAddress, currHostname=currHostname, evtSensor=evtSensor, battery=battery, errorClear=errorClear, raid=raid, diskFreeMinSizeExceed=diskFreeMinSizeExceed, evtDesc=evtDesc, vmEntry=vmEntry, volt=volt, redundancy=redundancy, ifaName=ifaName, fansClear=fansClear, websense=websense, swapMinFreeExceed=swapMinFreeExceed, hostnameChange=hostnameChange, ipAddressChange=ipAddressChange, powerSupply=powerSupply, memMaxUsageExceedClear=memMaxUsageExceedClear, ifaCurrAddressv6=ifaCurrAddressv6, batteryClear=batteryClear, ifaOutboundExceedFlag=ifaOutboundExceedFlag, logCacheMinFreeExceed=logCacheMinFreeExceed, ifaTable=ifaTable, fans=fans, loadErrorFlag=loadErrorFlag, loadAvg=loadAvg, ifaInboundExceedFlag=ifaInboundExceedFlag, svcTable=svcTable, dskPhysErrMsg=dskPhysErrMsg, dskVirtualNr=dskVirtualNr, moduleName=moduleName, ifaPhysAddress=ifaPhysAddress, raidErrorFlag=raidErrorFlag, intrusion=intrusion, vmStatus=vmStatus, evtInfo=evtInfo, serviceDownClear=serviceDownClear, dskPhysicalNr=dskPhysicalNr, ifaSpeed=ifaSpeed, logs=logs, vmName=vmName, networkMaxBandwidthExceedClear=networkMaxBandwidthExceedClear, vmTable=vmTable, svcName=svcName, hostnameChangeFlag=hostnameChangeFlag, temps=temps, raidClear=raidClear, evtDir=evtDir, mem=mem, moduleDownClear=moduleDownClear, testEvent=testEvent, diskFreeMinSizeExceedClear=diskFreeMinSizeExceedClear, wsAlertMessage=wsAlertMessage, intrusionClear=intrusionClear, ifaChangeFlag=ifaChangeFlag, logServerConnectionLostClear=logServerConnectionLostClear, systemLoad=systemLoad, ifaEntry=ifaEntry, svcStatus=svcStatus, ifaPrevAddressv6=ifaPrevAddressv6, wsAlert=wsAlert, evtTimestamp=evtTimestamp, swapMinFreeExceedClear=swapMinFreeExceedClear, networkMaxBandwidthExceed=networkMaxBandwidthExceed, powerSupplyClear=powerSupplyClear, serviceDown=serviceDown, triggerReading=triggerReading, dskCriticalNr=dskCriticalNr, moduleDown=moduleDown)