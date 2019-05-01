#
# PySNMP MIB module JUNIPER-WX-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-WX-GLOBAL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:01:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
jnxWxGrpStatus, = mibBuilder.importSymbols("JUNIPER-WX-GLOBAL-MIB", "jnxWxGrpStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, Gauge32, ModuleIdentity, ObjectIdentity, MibIdentifier, Counter32, Counter64, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "Gauge32", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "Counter32", "Counter64", "IpAddress", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxWxGrpStatusSys = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 1))
if mibBuilder.loadTexts: jnxWxGrpStatusSys.setStatus('current')
if mibBuilder.loadTexts: jnxWxGrpStatusSys.setDescription('This group contains WX system status information. ')
jnxWxGrpStatusSysModel = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("wxc250", 1), ("wxc500", 2), ("wxc590", 3), ("wxc1800", 4), ("wxc2600", 5), ("wxc3400", 6), ("wxc7800", 7), ("other", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatusSysModel.setStatus('current')
if mibBuilder.loadTexts: jnxWxGrpStatusSysModel.setDescription('The device model number. ')
jnxWxGrpStatusSysSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatusSysSwVersion.setStatus('current')
if mibBuilder.loadTexts: jnxWxGrpStatusSysSwVersion.setDescription('The software version for this device. ')
jnxWxGrpStatusSysHwVersion = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatusSysHwVersion.setStatus('current')
if mibBuilder.loadTexts: jnxWxGrpStatusSysHwVersion.setDescription('The hardware version for this device. ')
jnxWxGrpStatusApp = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 2))
if mibBuilder.loadTexts: jnxWxGrpStatusApp.setStatus('current')
if mibBuilder.loadTexts: jnxWxGrpStatusApp.setDescription('This group contains application status information. ')
jnxWxGrpStatusAppMonCount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatusAppMonCount.setStatus('current')
if mibBuilder.loadTexts: jnxWxGrpStatusAppMonCount.setDescription('Number of applications currently being monitored. ')
jnxWxGrpStatusAppTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 2, 2), )
if mibBuilder.loadTexts: jnxWxGrpStatusAppTable.setStatus('current')
if mibBuilder.loadTexts: jnxWxGrpStatusAppTable.setDescription('This table displays the application level status. It contains information for only the applications currently being monitored. ')
jnxWxGrpStatusAppEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 2, 2, 1), ).setIndexNames((0, "JUNIPER-WX-STATUS-MIB", "jnxWxGrpStatusAppId"))
if mibBuilder.loadTexts: jnxWxGrpStatusAppEntry.setStatus('current')
if mibBuilder.loadTexts: jnxWxGrpStatusAppEntry.setDescription('A row in jnxWxGrpStatusAppTable. ')
jnxWxGrpStatusAppId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: jnxWxGrpStatusAppId.setStatus('current')
if mibBuilder.loadTexts: jnxWxGrpStatusAppId.setDescription('The unique application ID. ')
jnxWxGrpStatusAppName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatusAppName.setStatus('current')
if mibBuilder.loadTexts: jnxWxGrpStatusAppName.setDescription('The application name. ')
jnxWxGrpStatusAppType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("default", 1), ("ftp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatusAppType.setStatus('current')
if mibBuilder.loadTexts: jnxWxGrpStatusAppType.setDescription('The application type. ')
jnxWxGrpStatusRemoteWx = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 3))
if mibBuilder.loadTexts: jnxWxGrpStatusRemoteWx.setStatus('current')
if mibBuilder.loadTexts: jnxWxGrpStatusRemoteWx.setDescription('This group contains remote WX status information. ')
jnxWxGrpStatusRemoteWxMonCount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatusRemoteWxMonCount.setStatus('current')
if mibBuilder.loadTexts: jnxWxGrpStatusRemoteWxMonCount.setDescription('Number of remote WXs currently being monitored. ')
jnxWxGrpStatusRemoteWxTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 3, 2), )
if mibBuilder.loadTexts: jnxWxGrpStatusRemoteWxTable.setStatus('current')
if mibBuilder.loadTexts: jnxWxGrpStatusRemoteWxTable.setDescription('This table displays the application level status. It contains information for only the applications currently being monitored. ')
jnxWxGrpStatusRemoteWxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 3, 2, 1), ).setIndexNames((0, "JUNIPER-WX-STATUS-MIB", "jnxWxGrpStatusRemoteWxId"))
if mibBuilder.loadTexts: jnxWxGrpStatusRemoteWxEntry.setStatus('current')
if mibBuilder.loadTexts: jnxWxGrpStatusRemoteWxEntry.setDescription('A row in jnxWxGrpStatusRemoteWxTable. ')
jnxWxGrpStatusRemoteWxId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 3, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: jnxWxGrpStatusRemoteWxId.setStatus('current')
if mibBuilder.loadTexts: jnxWxGrpStatusRemoteWxId.setDescription('The unique Remote WX ID. ')
jnxWxGrpStatusRemoteWxName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 3, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatusRemoteWxName.setStatus('current')
if mibBuilder.loadTexts: jnxWxGrpStatusRemoteWxName.setDescription('The remote WX name. ')
jnxWxGrpStatusRemoteWxType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("wx-device", 1), ("wx-client", 2), ("non-wx-device", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatusRemoteWxType.setStatus('current')
if mibBuilder.loadTexts: jnxWxGrpStatusRemoteWxType.setDescription('The remote WX type. ')
mibBuilder.exportSymbols("JUNIPER-WX-STATUS-MIB", jnxWxGrpStatusSysSwVersion=jnxWxGrpStatusSysSwVersion, jnxWxGrpStatusRemoteWxEntry=jnxWxGrpStatusRemoteWxEntry, jnxWxGrpStatusAppType=jnxWxGrpStatusAppType, jnxWxGrpStatusAppTable=jnxWxGrpStatusAppTable, jnxWxGrpStatusAppId=jnxWxGrpStatusAppId, jnxWxGrpStatusAppName=jnxWxGrpStatusAppName, jnxWxGrpStatusApp=jnxWxGrpStatusApp, jnxWxGrpStatusSysHwVersion=jnxWxGrpStatusSysHwVersion, jnxWxGrpStatusRemoteWx=jnxWxGrpStatusRemoteWx, jnxWxGrpStatusRemoteWxTable=jnxWxGrpStatusRemoteWxTable, jnxWxGrpStatusRemoteWxType=jnxWxGrpStatusRemoteWxType, jnxWxGrpStatusRemoteWxId=jnxWxGrpStatusRemoteWxId, jnxWxGrpStatusAppMonCount=jnxWxGrpStatusAppMonCount, jnxWxGrpStatusRemoteWxMonCount=jnxWxGrpStatusRemoteWxMonCount, jnxWxGrpStatusAppEntry=jnxWxGrpStatusAppEntry, jnxWxGrpStatusSysModel=jnxWxGrpStatusSysModel, jnxWxGrpStatusRemoteWxName=jnxWxGrpStatusRemoteWxName, jnxWxGrpStatusSys=jnxWxGrpStatusSys)