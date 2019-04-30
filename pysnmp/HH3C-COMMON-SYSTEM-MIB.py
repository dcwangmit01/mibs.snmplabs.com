#
# PySNMP MIB module HH3C-COMMON-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-COMMON-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:12:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
hh3cSystem, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cSystem")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Integer32, Counter64, ModuleIdentity, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, NotificationType, Gauge32, TimeTicks, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Counter64", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "NotificationType", "Gauge32", "TimeTicks", "Unsigned32", "Counter32")
TextualConvention, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "DateAndTime")
hh3cWriteConfig = MibScalar((1, 3, 6, 1, 4, 1, 25506, 6, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("save", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cWriteConfig.setStatus('current')
hh3cStartFtpServer = MibScalar((1, 3, 6, 1, 4, 1, 25506, 6, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cStartFtpServer.setStatus('current')
hh3cReboot = MibScalar((1, 3, 6, 1, 4, 1, 25506, 6, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reboot", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cReboot.setStatus('current')
hh3cSystemNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 6, 8))
hh3cWriteSuccessTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 6, 8, 1))
if mibBuilder.loadTexts: hh3cWriteSuccessTrap.setStatus('current')
hh3cWriteFailureTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 6, 8, 2))
if mibBuilder.loadTexts: hh3cWriteFailureTrap.setStatus('current')
hh3cRebootSendTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 6, 8, 3))
if mibBuilder.loadTexts: hh3cRebootSendTrap.setStatus('current')
hh3cSysColdStartTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 6, 8, 4))
if mibBuilder.loadTexts: hh3cSysColdStartTrap.setStatus('current')
hh3cSysWarmStartTrap = NotificationType((1, 3, 6, 1, 4, 1, 25506, 6, 8, 5))
if mibBuilder.loadTexts: hh3cSysWarmStartTrap.setStatus('current')
hh3cSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 25506, 6, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSoftwareVersion.setStatus('current')
hh3cSysBootType = MibScalar((1, 3, 6, 1, 4, 1, 25506, 6, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("coldStart", 1), ("warmStart", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSysBootType.setStatus('current')
hh3cSystemInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 6, 11))
hh3cSysStatisticPeriod = MibScalar((1, 3, 6, 1, 4, 1, 25506, 6, 11, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSysStatisticPeriod.setStatus('current')
hh3cSysSamplePeriod = MibScalar((1, 3, 6, 1, 4, 1, 25506, 6, 11, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 300))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSysSamplePeriod.setStatus('current')
hh3cSysTrapResendPeriod = MibScalar((1, 3, 6, 1, 4, 1, 25506, 6, 11, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSysTrapResendPeriod.setStatus('current')
hh3cSysTrapCollectionPeriod = MibScalar((1, 3, 6, 1, 4, 1, 25506, 6, 11, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSysTrapCollectionPeriod.setStatus('current')
hh3cSysSnmpPort = MibScalar((1, 3, 6, 1, 4, 1, 25506, 6, 11, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSysSnmpPort.setStatus('current')
hh3cSysSnmpTrapPort = MibScalar((1, 3, 6, 1, 4, 1, 25506, 6, 11, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSysSnmpTrapPort.setStatus('current')
hh3cSysNetID = MibScalar((1, 3, 6, 1, 4, 1, 25506, 6, 11, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSysNetID.setStatus('current')
hh3cSysLastSampleTime = MibScalar((1, 3, 6, 1, 4, 1, 25506, 6, 11, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSysLastSampleTime.setStatus('current')
mibBuilder.exportSymbols("HH3C-COMMON-SYSTEM-MIB", hh3cWriteConfig=hh3cWriteConfig, hh3cSysSnmpTrapPort=hh3cSysSnmpTrapPort, hh3cSysSnmpPort=hh3cSysSnmpPort, hh3cSysStatisticPeriod=hh3cSysStatisticPeriod, hh3cSystemInfo=hh3cSystemInfo, hh3cSoftwareVersion=hh3cSoftwareVersion, hh3cSysColdStartTrap=hh3cSysColdStartTrap, hh3cWriteSuccessTrap=hh3cWriteSuccessTrap, hh3cSysTrapCollectionPeriod=hh3cSysTrapCollectionPeriod, hh3cReboot=hh3cReboot, hh3cWriteFailureTrap=hh3cWriteFailureTrap, hh3cStartFtpServer=hh3cStartFtpServer, hh3cSysSamplePeriod=hh3cSysSamplePeriod, hh3cRebootSendTrap=hh3cRebootSendTrap, hh3cSystemNotification=hh3cSystemNotification, hh3cSysNetID=hh3cSysNetID, hh3cSysBootType=hh3cSysBootType, hh3cSysLastSampleTime=hh3cSysLastSampleTime, hh3cSysWarmStartTrap=hh3cSysWarmStartTrap, hh3cSysTrapResendPeriod=hh3cSysTrapResendPeriod)