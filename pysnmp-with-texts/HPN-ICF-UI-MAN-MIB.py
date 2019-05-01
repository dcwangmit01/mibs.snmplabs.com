#
# PySNMP MIB module HPN-ICF-UI-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-UI-MAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:41:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, Integer32, IpAddress, MibIdentifier, Counter32, Gauge32, Unsigned32, Counter64, iso, ModuleIdentity, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "Integer32", "IpAddress", "MibIdentifier", "Counter32", "Gauge32", "Unsigned32", "Counter64", "iso", "ModuleIdentity", "NotificationType", "TimeTicks")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
hpnicfUIMgt = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2))
if mibBuilder.loadTexts: hpnicfUIMgt.setLastUpdated('200404081405Z')
if mibBuilder.loadTexts: hpnicfUIMgt.setOrganization('')
if mibBuilder.loadTexts: hpnicfUIMgt.setContactInfo('')
if mibBuilder.loadTexts: hpnicfUIMgt.setDescription('User interfaces management MIB')
hpnicfUIMgtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1))
hpnicfUIBasicInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 1))
hpnicfUIScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 1, 1))
hpnicfUITrapBindObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 1, 2))
hpnicfTerminalUserName = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 1, 2, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfTerminalUserName.setStatus('current')
if mibBuilder.loadTexts: hpnicfTerminalUserName.setDescription(' It represents the name of the logging user when login with authentication, otherwise login mode, such as Console, AUX, TTY, VTY etc. ')
hpnicfTerminalSource = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 1, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfTerminalSource.setStatus('current')
if mibBuilder.loadTexts: hpnicfTerminalSource.setDescription(' Login mode, such as Console, AUX, TTY, VTY etc. ')
hpnicfTerminalUserAuthFailureReason = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("exceedRetries", 1), ("authTimeout", 2), ("otherReason", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfTerminalUserAuthFailureReason.setStatus('current')
if mibBuilder.loadTexts: hpnicfTerminalUserAuthFailureReason.setDescription('The reason why a user failed to log in.')
hpnicfUINotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 1, 3))
hpnicfUINotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 1, 3, 0))
hpnicfLogIn = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 1, 3, 0, 1)).setObjects(("HPN-ICF-UI-MAN-MIB", "hpnicfTerminalUserName"), ("HPN-ICF-UI-MAN-MIB", "hpnicfTerminalSource"))
if mibBuilder.loadTexts: hpnicfLogIn.setStatus('current')
if mibBuilder.loadTexts: hpnicfLogIn.setDescription(' This notification is generated when a user logs in. ')
hpnicfLogOut = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 1, 3, 0, 2)).setObjects(("HPN-ICF-UI-MAN-MIB", "hpnicfTerminalUserName"), ("HPN-ICF-UI-MAN-MIB", "hpnicfTerminalSource"))
if mibBuilder.loadTexts: hpnicfLogOut.setStatus('current')
if mibBuilder.loadTexts: hpnicfLogOut.setDescription(' This notification is generated when a user logs out. ')
hpnicfLogInAuthenFailure = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 1, 3, 0, 3)).setObjects(("HPN-ICF-UI-MAN-MIB", "hpnicfTerminalUserName"), ("HPN-ICF-UI-MAN-MIB", "hpnicfTerminalSource"), ("HPN-ICF-UI-MAN-MIB", "hpnicfTerminalUserAuthFailureReason"))
if mibBuilder.loadTexts: hpnicfLogInAuthenFailure.setStatus('current')
if mibBuilder.loadTexts: hpnicfLogInAuthenFailure.setDescription(' This notification is generated when a user fails to log in because of authentication. ')
hpnicfVtyMan = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 2))
hpnicfVtyAccTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 2, 1), )
if mibBuilder.loadTexts: hpnicfVtyAccTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfVtyAccTable.setDescription('Description.')
hpnicfVtyAccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 2, 1, 1), ).setIndexNames((0, "HPN-ICF-UI-MAN-MIB", "hpnicfVtyAccUserIndex"), (0, "HPN-ICF-UI-MAN-MIB", "hpnicfVtyAccConnway"))
if mibBuilder.loadTexts: hpnicfVtyAccEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfVtyAccEntry.setDescription('Description.')
hpnicfVtyAccUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: hpnicfVtyAccUserIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfVtyAccUserIndex.setDescription(' The relative index of the user interface of vty. ')
hpnicfVtyAccConnway = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 11, 12))).clone(namedValues=NamedValues(("inbound", 1), ("outbound", 2), ("linkinbound", 3), ("acl6inbound", 11), ("acl6outbound", 12))))
if mibBuilder.loadTexts: hpnicfVtyAccConnway.setStatus('current')
if mibBuilder.loadTexts: hpnicfVtyAccConnway.setDescription(' inbound(1):Filter login connections from current UI with ipv4 layer acl. outbound(2):Filter logout connections from current UI with ipv4 layer acl. linkinbound(3):Filter login connections from current UI with link layer acl. acl6inbound(11):Filter login connections from current UI with ipv6 layer acl. acl6outbound(12):Filter logout connections from current UI with ipv6 layer acl. ')
hpnicfVtyAccAclNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 2, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVtyAccAclNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfVtyAccAclNum.setDescription(' The filter rule number of ACL. ')
hpnicfVtyAccEntryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 2, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVtyAccEntryRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfVtyAccEntryRowStatus.setDescription(' The status of this conceptual row. Now only support CreateAndGo and Destroy and Active. ')
hpnicfConStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 3))
hpnicfConStatusTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 3, 1), )
if mibBuilder.loadTexts: hpnicfConStatusTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfConStatusTable.setDescription(' The current status of CONSOLE user interface. A group of attributes are used to describe the current status. ')
hpnicfConStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 3, 1, 1), ).setIndexNames((0, "HPN-ICF-UI-MAN-MIB", "hpnicfConUserIndex"))
if mibBuilder.loadTexts: hpnicfConStatusEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfConStatusEntry.setDescription(' An entry of hpnicfConStatusTable. ')
hpnicfConUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 3, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hpnicfConUserIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfConUserIndex.setDescription(" The index of the user interface of CONSOLE. It's equal to current UserID. ")
hpnicfConReAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfConReAuth.setStatus('current')
if mibBuilder.loadTexts: hpnicfConReAuth.setDescription(' The re-authentication attribute of current user interface. After disconnection of current user interface, connection is rebuilt, at the moment disable(1): re-authentication is not need. enable(2): re-authentication is need. ')
hpnicfUIMgtMIBConformance18 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 2))
hpnicfUIMgtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 2, 1))
hpnicfUIMgtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 2, 1, 1)).setObjects(("HPN-ICF-UI-MAN-MIB", "hpnicfUIMgtBasicGroup"), ("HPN-ICF-UI-MAN-MIB", "hpnicfConStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfUIMgtMIBCompliance = hpnicfUIMgtMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: hpnicfUIMgtMIBCompliance.setDescription('The compliance statement')
hpnicfUIMgtManMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 2, 2))
hpnicfUIMgtBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 2, 2, 1)).setObjects(("HPN-ICF-UI-MAN-MIB", "hpnicfVtyAccAclNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfUIMgtBasicGroup = hpnicfUIMgtBasicGroup.setStatus('current')
if mibBuilder.loadTexts: hpnicfUIMgtBasicGroup.setDescription('A collection of objects for a basic implement.')
hpnicfConStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2, 2, 2, 2)).setObjects(("HPN-ICF-UI-MAN-MIB", "hpnicfConReAuth"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfConStatusGroup = hpnicfConStatusGroup.setStatus('current')
if mibBuilder.loadTexts: hpnicfConStatusGroup.setDescription('A collection of current user interface status.')
mibBuilder.exportSymbols("HPN-ICF-UI-MAN-MIB", hpnicfUIMgtMIBCompliance=hpnicfUIMgtMIBCompliance, hpnicfTerminalSource=hpnicfTerminalSource, hpnicfVtyAccEntryRowStatus=hpnicfVtyAccEntryRowStatus, PYSNMP_MODULE_ID=hpnicfUIMgt, hpnicfTerminalUserAuthFailureReason=hpnicfTerminalUserAuthFailureReason, hpnicfUIMgtBasicGroup=hpnicfUIMgtBasicGroup, hpnicfUIScalarObjects=hpnicfUIScalarObjects, hpnicfVtyAccConnway=hpnicfVtyAccConnway, hpnicfConUserIndex=hpnicfConUserIndex, hpnicfUINotifications=hpnicfUINotifications, hpnicfVtyAccEntry=hpnicfVtyAccEntry, hpnicfUIMgtManMIBGroups=hpnicfUIMgtManMIBGroups, hpnicfTerminalUserName=hpnicfTerminalUserName, hpnicfUIMgtObjects=hpnicfUIMgtObjects, hpnicfUITrapBindObjects=hpnicfUITrapBindObjects, hpnicfLogOut=hpnicfLogOut, hpnicfVtyMan=hpnicfVtyMan, hpnicfConReAuth=hpnicfConReAuth, hpnicfLogIn=hpnicfLogIn, hpnicfVtyAccAclNum=hpnicfVtyAccAclNum, hpnicfUINotificationsPrefix=hpnicfUINotificationsPrefix, hpnicfUIMgt=hpnicfUIMgt, hpnicfConStatus=hpnicfConStatus, hpnicfConStatusEntry=hpnicfConStatusEntry, hpnicfUIMgtMIBCompliances=hpnicfUIMgtMIBCompliances, hpnicfLogInAuthenFailure=hpnicfLogInAuthenFailure, hpnicfConStatusTable=hpnicfConStatusTable, hpnicfVtyAccTable=hpnicfVtyAccTable, hpnicfUIBasicInfo=hpnicfUIBasicInfo, hpnicfUIMgtMIBConformance18=hpnicfUIMgtMIBConformance18, hpnicfVtyAccUserIndex=hpnicfVtyAccUserIndex, hpnicfConStatusGroup=hpnicfConStatusGroup)