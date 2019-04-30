#
# PySNMP MIB module CISCO-VOICE-APPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-APPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, iso, Counter64, Counter32, ModuleIdentity, Gauge32, TimeTicks, ObjectIdentity, NotificationType, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Counter64", "Counter32", "ModuleIdentity", "Gauge32", "TimeTicks", "ObjectIdentity", "NotificationType", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoVoiceAppsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 190))
ciscoVoiceAppsMIB.setRevisions(('2005-12-22 00:00', '2001-02-26 00:00',))
if mibBuilder.loadTexts: ciscoVoiceAppsMIB.setLastUpdated('200512220000Z')
if mibBuilder.loadTexts: ciscoVoiceAppsMIB.setOrganization('Cisco Systems, Inc.')
ciscoVoiceAppsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 190, 1))
cvaGeneralInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1))
cvaModuleFailureInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2))
cvaWorkflowInstallTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 1), )
if mibBuilder.loadTexts: cvaWorkflowInstallTable.setStatus('current')
cvaWorkflowInstallEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VOICE-APPS-MIB", "cvaWorkflowInstallIndex"))
if mibBuilder.loadTexts: cvaWorkflowInstallEntry.setStatus('current')
cvaWorkflowInstallIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cvaWorkflowInstallIndex.setStatus('current')
cvaWorkflowInstallName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvaWorkflowInstallName.setStatus('current')
cvaWorkflowInstallLocator = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvaWorkflowInstallLocator.setStatus('current')
cvaWorkflowInstallScriptName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvaWorkflowInstallScriptName.setStatus('current')
cvaWorkflowInstallEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvaWorkflowInstallEnable.setStatus('current')
cvaNotificationEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvaNotificationEnable.setStatus('current')
cvaAlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("informational", 7)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cvaAlarmSeverity.setStatus('current')
cvaModuleName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cvaModuleName.setStatus('current')
cvaProcessId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cvaProcessId.setStatus('current')
cvaModuleFailureName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cvaModuleFailureName.setStatus('current')
cvaModuleFailureCause = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("gracefulShutDown", 2), ("heartBeatFailure", 3), ("initFailure", 4), ("outOfResource", 5), ("partialFailure", 6)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cvaModuleFailureCause.setStatus('current')
cvaModuleFailureMessage = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cvaModuleFailureMessage.setStatus('current')
cvaModuleRunTimeFailureCause = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("other", 1), ("readAccessFailure", 2), ("writeAccessFailure", 3), ("createFailure", 4), ("deleteFailure", 5), ("updateFailure", 6), ("initFailure", 7), ("loadFailure", 8), ("outOfResource", 9), ("callProcessFailure", 10), ("registrationFailure", 11), ("deRegistrationFailure", 12), ("connectionFailure", 13), ("disconnectionFailure", 14), ("unknownTarget", 15), ("unReacheableTarget", 16)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cvaModuleRunTimeFailureCause.setStatus('current')
ciscoVoiceAppsMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 190, 2))
ciscoVoiceAppsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 190, 2, 0))
cvaModuleStart = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 190, 2, 0, 1)).setObjects(("CISCO-VOICE-APPS-MIB", "cvaAlarmSeverity"), ("CISCO-VOICE-APPS-MIB", "cvaModuleName"))
if mibBuilder.loadTexts: cvaModuleStart.setStatus('current')
cvaModuleStop = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 190, 2, 0, 2)).setObjects(("CISCO-VOICE-APPS-MIB", "cvaAlarmSeverity"), ("CISCO-VOICE-APPS-MIB", "cvaModuleName"), ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureCause"), ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureName"), ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureMessage"))
if mibBuilder.loadTexts: cvaModuleStop.setStatus('current')
cvaModuleRunTimeFailure = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 190, 2, 0, 3)).setObjects(("CISCO-VOICE-APPS-MIB", "cvaAlarmSeverity"), ("CISCO-VOICE-APPS-MIB", "cvaModuleName"), ("CISCO-VOICE-APPS-MIB", "cvaModuleRunTimeFailureCause"), ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureName"), ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureMessage"))
if mibBuilder.loadTexts: cvaModuleRunTimeFailure.setStatus('current')
cvaProcessStart = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 190, 2, 0, 4)).setObjects(("CISCO-VOICE-APPS-MIB", "cvaAlarmSeverity"), ("CISCO-VOICE-APPS-MIB", "cvaModuleName"), ("CISCO-VOICE-APPS-MIB", "cvaProcessId"))
if mibBuilder.loadTexts: cvaProcessStart.setStatus('current')
cvaProcessStop = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 190, 2, 0, 5)).setObjects(("CISCO-VOICE-APPS-MIB", "cvaAlarmSeverity"), ("CISCO-VOICE-APPS-MIB", "cvaModuleName"), ("CISCO-VOICE-APPS-MIB", "cvaProcessId"))
if mibBuilder.loadTexts: cvaProcessStop.setStatus('current')
ciscoVoiceAppsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 190, 3))
ciscoVoiceAppsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 190, 3, 1))
ciscoVoiceAppsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 190, 3, 2))
ciscoVoiceAppsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 190, 3, 1, 1)).setObjects(("CISCO-VOICE-APPS-MIB", "cvaModuleInfoGroup"), ("CISCO-VOICE-APPS-MIB", "cvaNotificationInfoGroup"), ("CISCO-VOICE-APPS-MIB", "cvaNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceAppsMIBCompliance = ciscoVoiceAppsMIBCompliance.setStatus('current')
cvaModuleInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 190, 3, 2, 1)).setObjects(("CISCO-VOICE-APPS-MIB", "cvaWorkflowInstallName"), ("CISCO-VOICE-APPS-MIB", "cvaWorkflowInstallLocator"), ("CISCO-VOICE-APPS-MIB", "cvaWorkflowInstallScriptName"), ("CISCO-VOICE-APPS-MIB", "cvaWorkflowInstallEnable"), ("CISCO-VOICE-APPS-MIB", "cvaNotificationEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvaModuleInfoGroup = cvaModuleInfoGroup.setStatus('current')
cvaNotificationInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 190, 3, 2, 2)).setObjects(("CISCO-VOICE-APPS-MIB", "cvaAlarmSeverity"), ("CISCO-VOICE-APPS-MIB", "cvaModuleName"), ("CISCO-VOICE-APPS-MIB", "cvaProcessId"), ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureName"), ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureCause"), ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureMessage"), ("CISCO-VOICE-APPS-MIB", "cvaModuleRunTimeFailureCause"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvaNotificationInfoGroup = cvaNotificationInfoGroup.setStatus('current')
cvaNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 190, 3, 2, 3)).setObjects(("CISCO-VOICE-APPS-MIB", "cvaModuleStart"), ("CISCO-VOICE-APPS-MIB", "cvaModuleStop"), ("CISCO-VOICE-APPS-MIB", "cvaModuleRunTimeFailure"), ("CISCO-VOICE-APPS-MIB", "cvaProcessStart"), ("CISCO-VOICE-APPS-MIB", "cvaProcessStop"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvaNotificationGroup = cvaNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-APPS-MIB", cvaModuleFailureName=cvaModuleFailureName, ciscoVoiceAppsMIBNotifications=ciscoVoiceAppsMIBNotifications, cvaModuleFailureCause=cvaModuleFailureCause, cvaModuleRunTimeFailureCause=cvaModuleRunTimeFailureCause, cvaProcessStart=cvaProcessStart, cvaAlarmSeverity=cvaAlarmSeverity, ciscoVoiceAppsMIBObjects=ciscoVoiceAppsMIBObjects, ciscoVoiceAppsMIB=ciscoVoiceAppsMIB, cvaNotificationGroup=cvaNotificationGroup, cvaWorkflowInstallIndex=cvaWorkflowInstallIndex, cvaWorkflowInstallLocator=cvaWorkflowInstallLocator, ciscoVoiceAppsMIBCompliances=ciscoVoiceAppsMIBCompliances, ciscoVoiceAppsMIBGroups=ciscoVoiceAppsMIBGroups, cvaNotificationEnable=cvaNotificationEnable, ciscoVoiceAppsMIBCompliance=ciscoVoiceAppsMIBCompliance, cvaModuleFailureInfo=cvaModuleFailureInfo, cvaNotificationInfoGroup=cvaNotificationInfoGroup, cvaWorkflowInstallScriptName=cvaWorkflowInstallScriptName, PYSNMP_MODULE_ID=ciscoVoiceAppsMIB, cvaModuleStart=cvaModuleStart, cvaProcessStop=cvaProcessStop, cvaWorkflowInstallEnable=cvaWorkflowInstallEnable, cvaProcessId=cvaProcessId, ciscoVoiceAppsMIBNotificationPrefix=ciscoVoiceAppsMIBNotificationPrefix, cvaModuleInfoGroup=cvaModuleInfoGroup, cvaModuleFailureMessage=cvaModuleFailureMessage, cvaModuleStop=cvaModuleStop, cvaGeneralInfo=cvaGeneralInfo, cvaModuleName=cvaModuleName, cvaModuleRunTimeFailure=cvaModuleRunTimeFailure, ciscoVoiceAppsMIBConformance=ciscoVoiceAppsMIBConformance, cvaWorkflowInstallTable=cvaWorkflowInstallTable, cvaWorkflowInstallName=cvaWorkflowInstallName, cvaWorkflowInstallEntry=cvaWorkflowInstallEntry)