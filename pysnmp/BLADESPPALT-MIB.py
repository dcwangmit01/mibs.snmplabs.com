#
# PySNMP MIB module BLADESPPALT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BLADESPPALT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:22:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, TimeTicks, Bits, Counter32, Integer32, Gauge32, NotificationType, ObjectIdentity, MibIdentifier, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "TimeTicks", "Bits", "Counter32", "Integer32", "Gauge32", "NotificationType", "ObjectIdentity", "MibIdentifier", "Unsigned32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
supportProcessor = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 158))
mmRemoteSupTrapMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 158, 3))
remoteSupTrapMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1))
spTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1))
spTrapDateTime = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapDateTime.setStatus('mandatory')
spTrapAppId = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapAppId.setStatus('mandatory')
spTrapSpTxtId = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapSpTxtId.setStatus('mandatory')
spTrapSysUuid = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapSysUuid.setStatus('mandatory')
spTrapSysSern = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapSysSern.setStatus('mandatory')
spTrapAppType = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapAppType.setStatus('mandatory')
spTrapPriority = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapPriority.setStatus('mandatory')
spTrapMsgText = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapMsgText.setStatus('mandatory')
spTrapHostContact = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapHostContact.setStatus('mandatory')
spTrapHostLocation = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapHostLocation.setStatus('mandatory')
spTrapBladeName = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapBladeName.setStatus('mandatory')
spTrapBladeSern = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapBladeSern.setStatus('mandatory')
spTrapBladeUuid = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapBladeUuid.setStatus('mandatory')
mmTrapTempC = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,0)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapVoltC = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,1)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapTampC = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,2)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapMffC = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,3)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapPsC = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,4)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mTrapHdC = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,5)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapVrmC = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,6)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapSffC = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,11)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapMsC = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,31)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapIhcC = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,36)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapRdpsN = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,10)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapTempN = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,12)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapVoltN = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,13)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapRmN = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,32)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapSecDvS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,15)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapPostToS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,20)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapOsToS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,21)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapAppS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,22)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapPoffS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,23)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapPonS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,24)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapBootS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,25)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapLdrToS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,26)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapPFAS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,27)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapKVMSwitchS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,33)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapSysInvS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,34)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapSysLogS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,35)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapNwChangeS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,37)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapBlThrS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,39)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mmTrapPwrMgntS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,40)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
mibBuilder.exportSymbols("BLADESPPALT-MIB", mmTrapSysInvS=mmTrapSysInvS, mmTrapKVMSwitchS=mmTrapKVMSwitchS, spTrapBladeSern=spTrapBladeSern, ibm=ibm, spTrapSysSern=spTrapSysSern, mmTrapOsToS=mmTrapOsToS, spTrapAppId=spTrapAppId, mmTrapTampC=mmTrapTampC, mmTrapNwChangeS=mmTrapNwChangeS, mmTrapTempN=mmTrapTempN, spTrapAppType=spTrapAppType, spTrapSysUuid=spTrapSysUuid, spTrapBladeName=spTrapBladeName, mmTrapVoltC=mmTrapVoltC, mmTrapPsC=mmTrapPsC, mmTrapPonS=mmTrapPonS, mmTrapLdrToS=mmTrapLdrToS, mmTrapPwrMgntS=mmTrapPwrMgntS, spTrapHostLocation=spTrapHostLocation, mmTrapVoltN=mmTrapVoltN, remoteSupTrapMibObjects=remoteSupTrapMibObjects, mmTrapBlThrS=mmTrapBlThrS, mmTrapPostToS=mmTrapPostToS, mmTrapVrmC=mmTrapVrmC, mmTrapTempC=mmTrapTempC, mmTrapSffC=mmTrapSffC, mmRemoteSupTrapMIB=mmRemoteSupTrapMIB, spTrapInfo=spTrapInfo, mmTrapMffC=mmTrapMffC, mmTrapAppS=mmTrapAppS, mmTrapSysLogS=mmTrapSysLogS, spTrapPriority=spTrapPriority, spTrapMsgText=spTrapMsgText, mTrapHdC=mTrapHdC, spTrapSpTxtId=spTrapSpTxtId, ibmProd=ibmProd, spTrapHostContact=spTrapHostContact, mmTrapSecDvS=mmTrapSecDvS, mmTrapMsC=mmTrapMsC, mmTrapPoffS=mmTrapPoffS, mmTrapIhcC=mmTrapIhcC, mmTrapPFAS=mmTrapPFAS, spTrapBladeUuid=spTrapBladeUuid, mmTrapRmN=mmTrapRmN, mmTrapRdpsN=mmTrapRdpsN, mmTrapBootS=mmTrapBootS, spTrapDateTime=spTrapDateTime, supportProcessor=supportProcessor)