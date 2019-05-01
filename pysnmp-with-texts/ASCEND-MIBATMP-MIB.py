#
# PySNMP MIB module ASCEND-MIBATMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBATMP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:26:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter32, MibIdentifier, Bits, ModuleIdentity, Integer32, TimeTicks, Gauge32, Unsigned32, ObjectIdentity, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "MibIdentifier", "Bits", "ModuleIdentity", "Integer32", "TimeTicks", "Gauge32", "Unsigned32", "ObjectIdentity", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibatmpProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 42))
mibatmpProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 42, 1), )
if mibBuilder.loadTexts: mibatmpProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibatmpProfileTable.setDescription('A list of mibatmpProfile profile entries.')
mibatmpProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1), ).setIndexNames((0, "ASCEND-MIBATMP-MIB", "atmpProfile-Index-o"))
if mibBuilder.loadTexts: mibatmpProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibatmpProfileEntry.setDescription('A mibatmpProfile entry containing objects that maps to the parameters of mibatmpProfile profile.')
atmpProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 1), Integer32()).setLabel("atmpProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpProfile_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: atmpProfile_Index_o.setDescription('')
atmpProfile_AgentMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("tunnelDisabled", 1), ("homeAgent", 2), ("foreignAgent", 3), ("homeAndForeignAgent", 4)))).setLabel("atmpProfile-AgentMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmpProfile_AgentMode.setStatus('mandatory')
if mibBuilder.loadTexts: atmpProfile_AgentMode.setDescription('The valid modes for this ATMP agent.')
atmpProfile_AgentType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("routerHomeAgent", 1), ("gatewayHomeAgent", 2)))).setLabel("atmpProfile-AgentType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmpProfile_AgentType.setStatus('mandatory')
if mibBuilder.loadTexts: atmpProfile_AgentType.setDescription('The type of Home Agent.')
atmpProfile_UdpPort = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 4), Integer32()).setLabel("atmpProfile-UdpPort").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmpProfile_UdpPort.setStatus('mandatory')
if mibBuilder.loadTexts: atmpProfile_UdpPort.setDescription('UDP port number to use locally.')
atmpProfile_HomeAgentPassword = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 5), DisplayString()).setLabel("atmpProfile-HomeAgentPassword").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmpProfile_HomeAgentPassword.setStatus('mandatory')
if mibBuilder.loadTexts: atmpProfile_HomeAgentPassword.setDescription('The password required to access this home agent.')
atmpProfile_AtmpSapReply = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("atmpProfile-AtmpSapReply").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmpProfile_AtmpSapReply.setStatus('mandatory')
if mibBuilder.loadTexts: atmpProfile_AtmpSapReply.setDescription('Whether an ATMP Home Agent should reply to IPX SAP Nearest Server queries from the Mobile Client.')
atmpProfile_RetryTimeout = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 7), Integer32()).setLabel("atmpProfile-RetryTimeout").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmpProfile_RetryTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: atmpProfile_RetryTimeout.setDescription('The number of seconds between retries to establish a tunnel.')
atmpProfile_RetryLimit = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 8), Integer32()).setLabel("atmpProfile-RetryLimit").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmpProfile_RetryLimit.setStatus('mandatory')
if mibBuilder.loadTexts: atmpProfile_RetryLimit.setDescription('The maximum number of failed attempts to establish a tunnel before switching to the alternate home agent.')
atmpProfile_IdleTimer = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 9), Integer32()).setLabel("atmpProfile-IdleTimer").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmpProfile_IdleTimer.setStatus('mandatory')
if mibBuilder.loadTexts: atmpProfile_IdleTimer.setDescription('The number of minutes of no activity before an ATMP Home Agent will drop a tunnel. The value 0 disables the idle timer.')
atmpProfile_MtuLimit = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 10), Integer32()).setLabel("atmpProfile-MtuLimit").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmpProfile_MtuLimit.setStatus('mandatory')
if mibBuilder.loadTexts: atmpProfile_MtuLimit.setDescription('The maximum IP packet size that can be transmitted to a remote agent without performing pre-fragmentation. The value 0 disables this feature. If enabled, the smallest size the system will use is 68, even if a smaller size is specified. This is to comply with the minimum IP packet size requirement per RFC 791.')
atmpProfile_ForceFragmentation = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("atmpProfile-ForceFragmentation").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmpProfile_ForceFragmentation.setStatus('mandatory')
if mibBuilder.loadTexts: atmpProfile_ForceFragmentation.setDescription('When set to NO, an ICMP message will be sent if a frame needs fragmentation and the DF bit is set. This is the standard behavior. When set to YES, it forces pre-fragmentation of large IP frames before they are sent to the remote agent, even if the frame has the DF bit set. This behavior is not standard and prevents MTU discovery mechanisms.')
atmpProfile_AtmpSnmpTrap = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("atmpProfile-AtmpSnmpTrap").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmpProfile_AtmpSnmpTrap.setStatus('mandatory')
if mibBuilder.loadTexts: atmpProfile_AtmpSnmpTrap.setDescription('When set to No, do not send ATMP SNMP traps. If Yes, send traps. The default is No.')
atmpProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("atmpProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmpProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: atmpProfile_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBATMP-MIB", mibatmpProfile=mibatmpProfile, atmpProfile_RetryLimit=atmpProfile_RetryLimit, atmpProfile_MtuLimit=atmpProfile_MtuLimit, atmpProfile_ForceFragmentation=atmpProfile_ForceFragmentation, atmpProfile_Action_o=atmpProfile_Action_o, atmpProfile_IdleTimer=atmpProfile_IdleTimer, atmpProfile_RetryTimeout=atmpProfile_RetryTimeout, atmpProfile_Index_o=atmpProfile_Index_o, atmpProfile_AgentMode=atmpProfile_AgentMode, atmpProfile_AtmpSnmpTrap=atmpProfile_AtmpSnmpTrap, mibatmpProfileTable=mibatmpProfileTable, atmpProfile_AtmpSapReply=atmpProfile_AtmpSapReply, DisplayString=DisplayString, mibatmpProfileEntry=mibatmpProfileEntry, atmpProfile_HomeAgentPassword=atmpProfile_HomeAgentPassword, atmpProfile_UdpPort=atmpProfile_UdpPort, atmpProfile_AgentType=atmpProfile_AgentType)