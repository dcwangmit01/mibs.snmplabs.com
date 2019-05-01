#
# PySNMP MIB module BPDU-PROTECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BPDU-PROTECTION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:40:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Counter32, IpAddress, MibIdentifier, Gauge32, Bits, iso, ObjectIdentity, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Counter32", "IpAddress", "MibIdentifier", "Gauge32", "Bits", "iso", "ObjectIdentity", "Counter64", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
swBpduProtectionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 76))
if mibBuilder.loadTexts: swBpduProtectionMIB.setLastUpdated('0903120000Z')
if mibBuilder.loadTexts: swBpduProtectionMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: swBpduProtectionMIB.setContactInfo('http://support.dlink.com')
if mibBuilder.loadTexts: swBpduProtectionMIB.setDescription('The structure of BPDU Protection management for the proprietary enterprise.')
swBpduProtectionCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 76, 1))
swBpduProtectionInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 76, 2))
swBpduProtectionMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 76, 3))
swBpduProtectionNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 76, 4))
swBpduProtectionAdminState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 76, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swBpduProtectionAdminState.setStatus('current')
if mibBuilder.loadTexts: swBpduProtectionAdminState.setDescription('This object indicates the BPDU Protection status for the system.')
swBpduProtectionRecoveryTime = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 76, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(60, 1000000), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swBpduProtectionRecoveryTime.setStatus('current')
if mibBuilder.loadTexts: swBpduProtectionRecoveryTime.setDescription('This object indicates the recovery time. The range is from 60 to 1000000 sec. The value of 0 disables the recover function.')
swBpduProtectionTrapMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 76, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("attackDetected", 2), ("attackCleared", 3), ("both", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swBpduProtectionTrapMode.setStatus('current')
if mibBuilder.loadTexts: swBpduProtectionTrapMode.setDescription('This object indicates the BPDU Protection trap mode for the system.')
swBpduProtectionLogMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 76, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("attackDetected", 2), ("attackCleared", 3), ("both", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swBpduProtectionLogMode.setStatus('current')
if mibBuilder.loadTexts: swBpduProtectionLogMode.setDescription('This object indicates the BPDU Protection log mode for the system.')
swBpduProtectionPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 76, 3, 1), )
if mibBuilder.loadTexts: swBpduProtectionPortTable.setStatus('current')
if mibBuilder.loadTexts: swBpduProtectionPortTable.setDescription('The table specifies the BPDU Protection function specified by port.')
swBpduProtectionPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 76, 3, 1, 1), ).setIndexNames((0, "BPDU-PROTECTION-MIB", "swBpduProtectionPortIndex"))
if mibBuilder.loadTexts: swBpduProtectionPortEntry.setStatus('current')
if mibBuilder.loadTexts: swBpduProtectionPortEntry.setDescription('The table specifies the BPDU Protection function specified by port.')
swBpduProtectionPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 76, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swBpduProtectionPortIndex.setStatus('current')
if mibBuilder.loadTexts: swBpduProtectionPortIndex.setDescription("This object indicates the module's port number. The range is from 1 to the maximum port number specified in the module.")
swBpduProtectionPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 76, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swBpduProtectionPortState.setStatus('current')
if mibBuilder.loadTexts: swBpduProtectionPortState.setDescription('This object indicates the BPDU Protection function state on the port.')
swBpduProtectionPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 76, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("drop", 1), ("block", 2), ("shutdown", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swBpduProtectionPortMode.setStatus('current')
if mibBuilder.loadTexts: swBpduProtectionPortMode.setDescription('This object indicates the BPDU Protection function mode on the port.')
swBpduProtectionPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 76, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("underAttack", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swBpduProtectionPortStatus.setStatus('current')
if mibBuilder.loadTexts: swBpduProtectionPortStatus.setDescription('This object indicates the port status.')
swBpduProtectionNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 76, 4, 0))
swBpduProtectionUnderAttackingTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 76, 4, 0, 1)).setObjects(("BPDU-PROTECTION-MIB", "swBpduProtectionPortIndex"), ("BPDU-PROTECTION-MIB", "swBpduProtectionPortMode"))
if mibBuilder.loadTexts: swBpduProtectionUnderAttackingTrap.setStatus('current')
if mibBuilder.loadTexts: swBpduProtectionUnderAttackingTrap.setDescription('When the BPDU Protection trap is enabled, if the specific port changes from a normal state to an under attack state, a trap will be sent out.')
swBpduProtectionRecoveryTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 76, 4, 0, 2)).setObjects(("BPDU-PROTECTION-MIB", "swBpduProtectionPortIndex"), ("BPDU-PROTECTION-MIB", "swBpduProtectionRecoveryMethod"))
if mibBuilder.loadTexts: swBpduProtectionRecoveryTrap.setStatus('current')
if mibBuilder.loadTexts: swBpduProtectionRecoveryTrap.setDescription('When the BPDU Protection trap is enabled, if the specific port changes from an under attack state to a normal state, a trap will be sent out.')
swBpduProtectionNotificationBidings = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 76, 4, 2))
swBpduProtectionRecoveryMethod = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 76, 4, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("automatically", 1), ("manually", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: swBpduProtectionRecoveryMethod.setStatus('current')
if mibBuilder.loadTexts: swBpduProtectionRecoveryMethod.setDescription('This object indicates the method of recovery from BPDU under attack.')
mibBuilder.exportSymbols("BPDU-PROTECTION-MIB", swBpduProtectionLogMode=swBpduProtectionLogMode, swBpduProtectionNotify=swBpduProtectionNotify, swBpduProtectionInfo=swBpduProtectionInfo, swBpduProtectionAdminState=swBpduProtectionAdminState, swBpduProtectionMgmt=swBpduProtectionMgmt, swBpduProtectionUnderAttackingTrap=swBpduProtectionUnderAttackingTrap, swBpduProtectionPortState=swBpduProtectionPortState, swBpduProtectionNotifyPrefix=swBpduProtectionNotifyPrefix, swBpduProtectionPortTable=swBpduProtectionPortTable, swBpduProtectionTrapMode=swBpduProtectionTrapMode, swBpduProtectionRecoveryMethod=swBpduProtectionRecoveryMethod, swBpduProtectionRecoveryTrap=swBpduProtectionRecoveryTrap, swBpduProtectionPortIndex=swBpduProtectionPortIndex, swBpduProtectionPortMode=swBpduProtectionPortMode, swBpduProtectionCtrl=swBpduProtectionCtrl, swBpduProtectionPortEntry=swBpduProtectionPortEntry, PYSNMP_MODULE_ID=swBpduProtectionMIB, swBpduProtectionMIB=swBpduProtectionMIB, swBpduProtectionRecoveryTime=swBpduProtectionRecoveryTime, swBpduProtectionPortStatus=swBpduProtectionPortStatus, swBpduProtectionNotificationBidings=swBpduProtectionNotificationBidings)