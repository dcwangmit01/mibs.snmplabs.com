#
# PySNMP MIB module TPLINK-8021X-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-8021X-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:24:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Counter32, ModuleIdentity, Counter64, Unsigned32, MibIdentifier, ObjectIdentity, Gauge32, IpAddress, Integer32, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Counter32", "ModuleIdentity", "Counter64", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Gauge32", "IpAddress", "Integer32", "iso", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplink8021xMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 31))
tplink8021xMIB.setRevisions(('2012-12-17 10:50',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplink8021xMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplink8021xMIB.setLastUpdated('201212171050Z')
if mibBuilder.loadTexts: tplink8021xMIB.setOrganization('TPLINK')
if mibBuilder.loadTexts: tplink8021xMIB.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplink8021xMIB.setDescription('Private MIB for 802.1x configuration.')
tplink8021xMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1))
tplink8021xNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 31, 2))
tp8021xGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1))
tp8021xGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xGlobalEnable.setStatus('current')
if mibBuilder.loadTexts: tp8021xGlobalEnable.setDescription('0. disable 1. enable Enable/Disable the 802.1X function.')
tp8021xAuthMode = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("pap", 0), ("eap", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xAuthMode.setStatus('current')
if mibBuilder.loadTexts: tp8021xAuthMode.setDescription('Select the Authentication Method 0. pap: IEEE 802.1X authentication system uses extensible authentication protocol (EAP) to exchange information between the switch and the client. The transmission of EAP packets is terminated at the switch and the EAP packets are converted to the other protocol (such as RADIUS) packets for transmission. 1. eap: IEEE 802.1X authentication system uses extensible authentication protocol (EAP) to exchange information between the switch and the client. The EAP protocol packets with authentication data can be encapsulated in the advanced protocol (such as RADIUS) packets to be transmitted to the authentication server.')
tp8021xHandshake = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xHandshake.setStatus('current')
if mibBuilder.loadTexts: tp8021xHandshake.setDescription('0. disable 1. enable Enable/Disable the handshake feature.')
tp8021xGuestVlanEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xGuestVlanEnable.setStatus('current')
if mibBuilder.loadTexts: tp8021xGuestVlanEnable.setDescription('0. disable 1. enable Enable/Disable the Guest VLAN feature.')
tp8021xGuestVlanID = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xGuestVlanID.setStatus('current')
if mibBuilder.loadTexts: tp8021xGuestVlanID.setDescription('Enter your desired VLAN ID to enable the Guest VLAN feature. The supplicants in the Guest VLAN can access the specified network source.')
tp8021xQuietEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xQuietEnable.setStatus('current')
if mibBuilder.loadTexts: tp8021xQuietEnable.setDescription('0. disable 1. enable Enable/Disable the Quiet timer.')
tp8021xQuietPeriod = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xQuietPeriod.setStatus('current')
if mibBuilder.loadTexts: tp8021xQuietPeriod.setDescription('Specify a value for Quiet Period. Once the supplicant failed to the 802.1X Authentication, then the switch will not respond to the authentication request from the same supplicant during the Quiet Period. (1-999 second)')
tp8021xRetryTimes = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xRetryTimes.setStatus('current')
if mibBuilder.loadTexts: tp8021xRetryTimes.setDescription('Specify the maximum transfer times of the repeated authentication request.(1-9)')
tp8021xSupplicantTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xSupplicantTimeOut.setStatus('current')
if mibBuilder.loadTexts: tp8021xSupplicantTimeOut.setDescription('Specify the maximum time for the switch to wait for the response from supplicant before resending a request to the supplicant. (1-9 second)')
tp8021xServerTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xServerTimeOut.setStatus('current')
if mibBuilder.loadTexts: tp8021xServerTimeOut.setDescription('Specify the maximum time for the switch to wait for the response from authentication server before resending a request to the authentication server. (1-9 second)')
tp8021xAuthPrimaryIP = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xAuthPrimaryIP.setStatus('current')
if mibBuilder.loadTexts: tp8021xAuthPrimaryIP.setDescription('Enter the IP address of the authentication server.')
tp8021xAuthSecondaryIP = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 12), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xAuthSecondaryIP.setStatus('current')
if mibBuilder.loadTexts: tp8021xAuthSecondaryIP.setDescription('Enter the IP address of the alternate authentication server.')
tp8021xServerAuthPort = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xServerAuthPort.setStatus('current')
if mibBuilder.loadTexts: tp8021xServerAuthPort.setDescription('Set the UDP port of authentication server(s). The default port is 1812(1-65535)')
tp8021xServerAuthKey = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xServerAuthKey.setStatus('current')
if mibBuilder.loadTexts: tp8021xServerAuthKey.setDescription('Set the shared password for the switch and the authentication servers to exchange messages.(0-31 characters).')
tp8021xAcctEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xAcctEnable.setStatus('current')
if mibBuilder.loadTexts: tp8021xAcctEnable.setDescription('0. disable 1. enable Enable/Disable the accounting feature. ')
tp8021xAcctPrimaryIP = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 16), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xAcctPrimaryIP.setStatus('current')
if mibBuilder.loadTexts: tp8021xAcctPrimaryIP.setDescription('Enter the IP address of the accounting server.')
tp8021xAcctSecondaryIP = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 17), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xAcctSecondaryIP.setStatus('current')
if mibBuilder.loadTexts: tp8021xAcctSecondaryIP.setDescription('Enter the IP address of the alternate accounting server.')
tp8021xAcctPort = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xAcctPort.setStatus('current')
if mibBuilder.loadTexts: tp8021xAcctPort.setDescription('Set the UDP port of accounting server(s). The default port is 1813(1-65535)')
tp8021xAcctKey = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xAcctKey.setStatus('current')
if mibBuilder.loadTexts: tp8021xAcctKey.setDescription('Set the shared password for the switch and the accounting servers to exchange messages. (0-31 characters).')
tp8021xPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 2))
tp8021xPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 2, 1), )
if mibBuilder.loadTexts: tp8021xPortConfigTable.setStatus('current')
if mibBuilder.loadTexts: tp8021xPortConfigTable.setDescription('A list of 8021x port config entries.')
tp8021xPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tp8021xPortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: tp8021xPortConfigEntry.setDescription('An entry contains of the information of 8021x port config. Here you can configure the ports for the 802.1X authentication.')
tp8021xPortConfigPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tp8021xPortConfigPortIndex.setStatus('current')
if mibBuilder.loadTexts: tp8021xPortConfigPortIndex.setDescription('This object indicates the port number.')
tp8021xPortConfigEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xPortConfigEnable.setStatus('current')
if mibBuilder.loadTexts: tp8021xPortConfigEnable.setDescription('0. disable 1. enable Select Enable/Disable the 802.1X authentication feature for the port.')
tp8021xPortConfigGuestVlanEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xPortConfigGuestVlanEnable.setStatus('current')
if mibBuilder.loadTexts: tp8021xPortConfigGuestVlanEnable.setDescription('0. disable 1. enable Select Enable/Disable the Guest VLAN feature for the port.')
tp8021xPortConfigControlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("forceAuth", 0), ("forceUnAuth", 1), ("autoAuth", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xPortConfigControlMode.setStatus('current')
if mibBuilder.loadTexts: tp8021xPortConfigControlMode.setDescription('Specify the Control Mode for the port. 0. force auth: In this mode, the port can work normally without passing the 802.1X Authentication. 1. force unauth: In this mode, the port is forbidden working for its fixed unauthorized status. 2. auto auth: In this mode, the port will normally work only after passing the 802.1X Authentication.')
tp8021xPortConfigControlType = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("macBased", 0), ("portBased", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp8021xPortConfigControlType.setStatus('current')
if mibBuilder.loadTexts: tp8021xPortConfigControlType.setDescription('Specify the Control Type for the port. 0. base of mac: Any client connected to the port should pass the 802.1X Authentication for access. 1. base of port: All the clients connected to the port can access the network on the condition that any one of the clients has passed the 802.1X Authentication. ')
tp8021xPortConfigAuthState = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("unAuthorized", 0), ("authorized", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tp8021xPortConfigAuthState.setStatus('current')
if mibBuilder.loadTexts: tp8021xPortConfigAuthState.setDescription('The authentication status of the port. 0. unAuthorized 1. Authorized')
tp8021xPortConfigPortLag = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 2, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tp8021xPortConfigPortLag.setStatus('current')
if mibBuilder.loadTexts: tp8021xPortConfigPortLag.setDescription('the lag the port belong to')
mibBuilder.exportSymbols("TPLINK-8021X-MIB", tp8021xSupplicantTimeOut=tp8021xSupplicantTimeOut, tp8021xAuthSecondaryIP=tp8021xAuthSecondaryIP, tp8021xPortConfigControlMode=tp8021xPortConfigControlMode, tp8021xGlobalConfig=tp8021xGlobalConfig, tplink8021xMIB=tplink8021xMIB, tp8021xAuthMode=tp8021xAuthMode, tp8021xHandshake=tp8021xHandshake, tp8021xQuietPeriod=tp8021xQuietPeriod, tplink8021xMIBObjects=tplink8021xMIBObjects, tp8021xPortConfigEntry=tp8021xPortConfigEntry, tp8021xPortConfigPortLag=tp8021xPortConfigPortLag, tp8021xGlobalEnable=tp8021xGlobalEnable, tp8021xPortConfigAuthState=tp8021xPortConfigAuthState, tp8021xAcctEnable=tp8021xAcctEnable, tp8021xGuestVlanEnable=tp8021xGuestVlanEnable, tp8021xRetryTimes=tp8021xRetryTimes, tp8021xAuthPrimaryIP=tp8021xAuthPrimaryIP, tp8021xAcctPort=tp8021xAcctPort, tp8021xAcctSecondaryIP=tp8021xAcctSecondaryIP, tp8021xAcctKey=tp8021xAcctKey, tp8021xServerAuthKey=tp8021xServerAuthKey, tplink8021xNotifications=tplink8021xNotifications, tp8021xPortConfigPortIndex=tp8021xPortConfigPortIndex, PYSNMP_MODULE_ID=tplink8021xMIB, tp8021xAcctPrimaryIP=tp8021xAcctPrimaryIP, tp8021xPortConfigGuestVlanEnable=tp8021xPortConfigGuestVlanEnable, tp8021xPortConfig=tp8021xPortConfig, tp8021xQuietEnable=tp8021xQuietEnable, tp8021xPortConfigEnable=tp8021xPortConfigEnable, tp8021xServerAuthPort=tp8021xServerAuthPort, tp8021xPortConfigControlType=tp8021xPortConfigControlType, tp8021xPortConfigTable=tp8021xPortConfigTable, tp8021xGuestVlanID=tp8021xGuestVlanID, tp8021xServerTimeOut=tp8021xServerTimeOut)