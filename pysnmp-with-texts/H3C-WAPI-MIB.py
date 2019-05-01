#
# PySNMP MIB module H3C-WAPI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-WAPI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:24:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ifDescr, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifDescr", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, Bits, Counter32, TimeTicks, ObjectIdentity, ModuleIdentity, Integer32, Unsigned32, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "Bits", "Counter32", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "Integer32", "Unsigned32", "NotificationType", "iso")
MacAddress, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TruthValue", "TextualConvention", "DisplayString")
h3cwapiMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77))
if mibBuilder.loadTexts: h3cwapiMIB.setLastUpdated('201012011757Z')
if mibBuilder.loadTexts: h3cwapiMIB.setOrganization('H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cwapiMIB.setContactInfo('Platform Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: h3cwapiMIB.setDescription('H3C-WAPI-MIB is an extension of MIB in WAPI protocol. This MIB contains objects to manage configuration and monitor running state for WAPI feature.')
h3cwapiMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 1))
h3cwapiMIBStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 2))
h3cwapiMIBTableObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3))
h3cwapiTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4))
h3cwapiModeEnabled = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cwapiModeEnabled.setStatus('current')
if mibBuilder.loadTexts: h3cwapiModeEnabled.setDescription('When this object is set to TRUE, it shall indicate that WAPI is enabled. Otherwise, it shall indicate that WAPI is disabled.')
h3cwapiASIPAddressType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cwapiASIPAddressType.setStatus('current')
if mibBuilder.loadTexts: h3cwapiASIPAddressType.setDescription('This object is used to set global IP addresses type (IPv4 or IPv6) of AS.')
h3cwapiASIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 1, 3), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cwapiASIPAddress.setStatus('current')
if mibBuilder.loadTexts: h3cwapiASIPAddress.setDescription('This object is used to set the global IP address of AS.')
h3cwapiCertificateInstalled = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cwapiCertificateInstalled.setStatus('current')
if mibBuilder.loadTexts: h3cwapiCertificateInstalled.setDescription("This object indicates whether the entity has installed certificate. When the value is TURE, it shall indicate that the entity has installed certificate. Otherwise, it shall indicate that the entity hasn't installed certificate.")
h3cwapiStatsWAISignatureErrors = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cwapiStatsWAISignatureErrors.setStatus('current')
if mibBuilder.loadTexts: h3cwapiStatsWAISignatureErrors.setDescription('This counter increases when the received packet of WAI signature is wrong.')
h3cwapiStatsWAIHMACErrors = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cwapiStatsWAIHMACErrors.setStatus('current')
if mibBuilder.loadTexts: h3cwapiStatsWAIHMACErrors.setDescription('This counter increases when the received packet of WAI message authentication key checking error occurs.')
h3cwapiStatsWAIAuthRsltFailures = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cwapiStatsWAIAuthRsltFailures.setStatus('current')
if mibBuilder.loadTexts: h3cwapiStatsWAIAuthRsltFailures.setDescription('This counter increases when the WAI authentication result is unsuccessful.')
h3cwapiStatsWAIDiscardCounters = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cwapiStatsWAIDiscardCounters.setStatus('current')
if mibBuilder.loadTexts: h3cwapiStatsWAIDiscardCounters.setDescription('This counter increases when the received packet of WAI are discarded.')
h3cwapiStatsWAITimeoutCounters = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cwapiStatsWAITimeoutCounters.setStatus('current')
if mibBuilder.loadTexts: h3cwapiStatsWAITimeoutCounters.setDescription('This counter increases when the packet of WAI overtime are detected.')
h3cwapiStatsWAIFormatErrors = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cwapiStatsWAIFormatErrors.setStatus('current')
if mibBuilder.loadTexts: h3cwapiStatsWAIFormatErrors.setDescription('This counter increases when the WAI packet of WAI format error is detected.')
h3cwapiStatsWAICtfHskFailures = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cwapiStatsWAICtfHskFailures.setStatus('current')
if mibBuilder.loadTexts: h3cwapiStatsWAICtfHskFailures.setDescription('This counter increases when the WAI certificate authenticates unsuccessfully.')
h3cwapiStatsWAIUniHskFailures = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cwapiStatsWAIUniHskFailures.setStatus('current')
if mibBuilder.loadTexts: h3cwapiStatsWAIUniHskFailures.setDescription('This counter increases when the WAI unicast cipher key negotiates unsuccessfully.')
h3cwapiStatsWAIMulHskFailures = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 2, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cwapiStatsWAIMulHskFailures.setStatus('current')
if mibBuilder.loadTexts: h3cwapiStatsWAIMulHskFailures.setDescription('This counter increases when the WAI multicast cipher key announces unsuccessfully.')
h3cwapiConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 1), )
if mibBuilder.loadTexts: h3cwapiConfigTable.setStatus('current')
if mibBuilder.loadTexts: h3cwapiConfigTable.setDescription('The table containing WAPI configuration objects.')
h3cwapiConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cwapiConfigEntry.setStatus('current')
if mibBuilder.loadTexts: h3cwapiConfigEntry.setDescription('An entry in the h3cwapiConfigTable.')
h3cwapiConfigASIPAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 1, 1, 1), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cwapiConfigASIPAddressType.setStatus('current')
if mibBuilder.loadTexts: h3cwapiConfigASIPAddressType.setDescription('This object is used to set IP addresses type of AS.')
h3cwapiConfigASIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 1, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cwapiConfigASIPAddress.setStatus('current')
if mibBuilder.loadTexts: h3cwapiConfigASIPAddress.setDescription('This object is used to set the IP address of AS.')
h3cwapiConfigAuthMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("certificate", 1), ("psk", 2), ("certificatePsk", 3))).clone('certificate')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cwapiConfigAuthMethod.setStatus('current')
if mibBuilder.loadTexts: h3cwapiConfigAuthMethod.setDescription('This object selects a mechanism for WAPI authentication method. The default is certificate.')
h3cwapiConfigAuthMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standard", 1), ("radiusExtension", 2))).clone('standard')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cwapiConfigAuthMode.setStatus('current')
if mibBuilder.loadTexts: h3cwapiConfigAuthMode.setDescription('This object selects a mechanism for WAPI authentication mode. When the value is standard, it shall indicate that the entity acts accord with the official definition. Otherwise, it shall indicate that the entity finishs authentication by means of RADIUS. The default is standard.')
h3cwapiConfigISPDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cwapiConfigISPDomain.setStatus('current')
if mibBuilder.loadTexts: h3cwapiConfigISPDomain.setDescription('The ISP domain name.')
h3cwapiConfigCertificateDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cwapiConfigCertificateDomain.setStatus('current')
if mibBuilder.loadTexts: h3cwapiConfigCertificateDomain.setDescription('The PKI domain name.')
h3cwapiConfigASName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cwapiConfigASName.setStatus('current')
if mibBuilder.loadTexts: h3cwapiConfigASName.setDescription('The name of AS.')
h3cwapiConfigBKRekeyEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 1, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cwapiConfigBKRekeyEnabled.setStatus('current')
if mibBuilder.loadTexts: h3cwapiConfigBKRekeyEnabled.setDescription('This object indicates whether the BK rekey function is supported. When the value is TURE, it shall indicate that the BK rekey function is supported. Otherwise, it shall indicate that the BK rekey function is not supported.')
h3cwapiConfigExtTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2), )
if mibBuilder.loadTexts: h3cwapiConfigExtTable.setStatus('current')
if mibBuilder.loadTexts: h3cwapiConfigExtTable.setDescription('The table containing WAPI configuration objects for SSID.')
h3cwapiConfigExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2, 1), ).setIndexNames((0, "H3C-WAPI-MIB", "h3cwapiConfigServicePolicyID"))
if mibBuilder.loadTexts: h3cwapiConfigExtEntry.setStatus('current')
if mibBuilder.loadTexts: h3cwapiConfigExtEntry.setDescription('An extend entry in the h3cwapiConfigExtTable.')
h3cwapiConfigServicePolicyID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cwapiConfigServicePolicyID.setStatus('current')
if mibBuilder.loadTexts: h3cwapiConfigServicePolicyID.setDescription('Represents the ID of each service policy.')
h3cwapiConfigUnicastCipherEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cwapiConfigUnicastCipherEnabled.setStatus('current')
if mibBuilder.loadTexts: h3cwapiConfigUnicastCipherEnabled.setDescription('This object enables or disables the unicast cipher.')
h3cwapiConfigUnicastCipherSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cwapiConfigUnicastCipherSize.setStatus('current')
if mibBuilder.loadTexts: h3cwapiConfigUnicastCipherSize.setDescription('This object indicates the length in bits of the unicast cipher key. This should be 256 for SMS4, first 128 bits for encrypting, last 128 bits for integrity checking.')
h3cwapiConfigAuthenticationSuiteEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cwapiConfigAuthenticationSuiteEnabled.setStatus('current')
if mibBuilder.loadTexts: h3cwapiConfigAuthenticationSuiteEnabled.setDescription('This variable indicates the corresponding AKM suite is enabled or disabled.')
h3cwapiConfigAuthenticationSuite = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cwapiConfigAuthenticationSuite.setStatus('current')
if mibBuilder.loadTexts: h3cwapiConfigAuthenticationSuite.setDescription('The selector of an AKM suite. It consists of an OUI (the first 3 octets) and a cipher suite identifier (the last octet).')
h3cwapiCfgExtASIPAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2, 1, 6), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cwapiCfgExtASIPAddressType.setStatus('current')
if mibBuilder.loadTexts: h3cwapiCfgExtASIPAddressType.setDescription('This object is used to set IP addresses type of AS.')
h3cwapiCfgExtASIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2, 1, 7), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cwapiCfgExtASIPAddress.setStatus('current')
if mibBuilder.loadTexts: h3cwapiCfgExtASIPAddress.setDescription('This object is used to set the IP address of AS.')
h3cwapiCfgExtASName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cwapiCfgExtASName.setStatus('current')
if mibBuilder.loadTexts: h3cwapiCfgExtASName.setDescription('This object is used to set the name of AS.')
h3cwapiCfgExtCertDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cwapiCfgExtCertDomain.setStatus('current')
if mibBuilder.loadTexts: h3cwapiCfgExtCertDomain.setDescription('This object is used to set the PKI domain name.')
h3cwapiCfgExtCertInstalled = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cwapiCfgExtCertInstalled.setStatus('current')
if mibBuilder.loadTexts: h3cwapiCfgExtCertInstalled.setDescription("This object indicates whether the entity has installed certificate. When the value is TURE, it shall indicate that the SSID has installed certificate. Otherwise, it shall indicate that the SSID hasn't installed certificate.")
h3cwapiTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4, 0))
h3cwapiUserwithInvalidCertificate = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("H3C-WAPI-MIB", "h3cwapiTrapInfoMacAddr"), ("H3C-WAPI-MIB", "h3cwapiTrapInfoAPId"), ("H3C-WAPI-MIB", "h3cwapiTrapInfoRadioId"), ("H3C-WAPI-MIB", "h3cwapiTrapInfoBSSId"))
if mibBuilder.loadTexts: h3cwapiUserwithInvalidCertificate.setStatus('current')
if mibBuilder.loadTexts: h3cwapiUserwithInvalidCertificate.setDescription('This trap is sent when a user intrudes upon network with invalid certificate.')
h3cwapiStationReplayAttack = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("H3C-WAPI-MIB", "h3cwapiTrapInfoMacAddr"), ("H3C-WAPI-MIB", "h3cwapiTrapInfoAPId"), ("H3C-WAPI-MIB", "h3cwapiTrapInfoRadioId"), ("H3C-WAPI-MIB", "h3cwapiTrapInfoBSSId"))
if mibBuilder.loadTexts: h3cwapiStationReplayAttack.setStatus('current')
if mibBuilder.loadTexts: h3cwapiStationReplayAttack.setDescription('This trap is sent when an attacker records and replays network transactions.')
h3cwapiTamperAttack = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("H3C-WAPI-MIB", "h3cwapiTrapInfoMacAddr"), ("H3C-WAPI-MIB", "h3cwapiTrapInfoAPId"), ("H3C-WAPI-MIB", "h3cwapiTrapInfoRadioId"), ("H3C-WAPI-MIB", "h3cwapiTrapInfoBSSId"))
if mibBuilder.loadTexts: h3cwapiTamperAttack.setStatus('current')
if mibBuilder.loadTexts: h3cwapiTamperAttack.setDescription('This trap is sent when an attacker monitors network traffic and maliciously changes data in transit(for example, an attacker may modify the contents of a WAI message).')
h3cwapiLowSafeLevelAttack = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("H3C-WAPI-MIB", "h3cwapiTrapInfoMacAddr"), ("H3C-WAPI-MIB", "h3cwapiTrapInfoAPId"), ("H3C-WAPI-MIB", "h3cwapiTrapInfoRadioId"), ("H3C-WAPI-MIB", "h3cwapiTrapInfoBSSId"))
if mibBuilder.loadTexts: h3cwapiLowSafeLevelAttack.setStatus('current')
if mibBuilder.loadTexts: h3cwapiLowSafeLevelAttack.setDescription('This trap is sent when a station associates AP(Access Point), creates packet of Unicast Key Negotiation Response with wrong WIE(WAPI Information Element) of ASUE(Authentication Supplicant Entity).')
h3cwapiAddressRedirectionAttack = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4, 0, 5)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("H3C-WAPI-MIB", "h3cwapiTrapInfoMacAddr"), ("H3C-WAPI-MIB", "h3cwapiTrapInfoAPId"), ("H3C-WAPI-MIB", "h3cwapiTrapInfoRadioId"), ("H3C-WAPI-MIB", "h3cwapiTrapInfoBSSId"))
if mibBuilder.loadTexts: h3cwapiAddressRedirectionAttack.setStatus('current')
if mibBuilder.loadTexts: h3cwapiAddressRedirectionAttack.setDescription('This trap is sent when an attacker maliciously changes destination MAC address of WPI(WLAN Privacy Infrastructure) frame.')
h3cwapiTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4, 1))
h3cwapiTrapInfoMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4, 1, 1), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cwapiTrapInfoMacAddr.setStatus('current')
if mibBuilder.loadTexts: h3cwapiTrapInfoMacAddr.setDescription('The MAC address of the WAPI user.')
h3cwapiTrapInfoAPId = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4, 1, 2), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cwapiTrapInfoAPId.setStatus('current')
if mibBuilder.loadTexts: h3cwapiTrapInfoAPId.setDescription('To uniquely identify each AP.')
h3cwapiTrapInfoRadioId = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4, 1, 3), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cwapiTrapInfoRadioId.setStatus('current')
if mibBuilder.loadTexts: h3cwapiTrapInfoRadioId.setDescription('Represents each radio.')
h3cwapiTrapInfoBSSId = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4, 1, 4), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cwapiTrapInfoBSSId.setStatus('current')
if mibBuilder.loadTexts: h3cwapiTrapInfoBSSId.setDescription('As MAC Address format, it is to identify BSS.')
mibBuilder.exportSymbols("H3C-WAPI-MIB", h3cwapiTrapInfoAPId=h3cwapiTrapInfoAPId, h3cwapiStatsWAISignatureErrors=h3cwapiStatsWAISignatureErrors, h3cwapiTrapPrefix=h3cwapiTrapPrefix, h3cwapiUserwithInvalidCertificate=h3cwapiUserwithInvalidCertificate, h3cwapiASIPAddress=h3cwapiASIPAddress, h3cwapiConfigAuthenticationSuite=h3cwapiConfigAuthenticationSuite, h3cwapiMIBTableObjects=h3cwapiMIBTableObjects, h3cwapiConfigAuthenticationSuiteEnabled=h3cwapiConfigAuthenticationSuiteEnabled, h3cwapiTrap=h3cwapiTrap, h3cwapiConfigUnicastCipherSize=h3cwapiConfigUnicastCipherSize, h3cwapiConfigASName=h3cwapiConfigASName, h3cwapiTamperAttack=h3cwapiTamperAttack, h3cwapiStatsWAIMulHskFailures=h3cwapiStatsWAIMulHskFailures, h3cwapiMIB=h3cwapiMIB, h3cwapiTrapInfoRadioId=h3cwapiTrapInfoRadioId, h3cwapiASIPAddressType=h3cwapiASIPAddressType, h3cwapiStatsWAIAuthRsltFailures=h3cwapiStatsWAIAuthRsltFailures, h3cwapiCfgExtASIPAddress=h3cwapiCfgExtASIPAddress, h3cwapiConfigExtTable=h3cwapiConfigExtTable, h3cwapiStatsWAICtfHskFailures=h3cwapiStatsWAICtfHskFailures, h3cwapiStationReplayAttack=h3cwapiStationReplayAttack, h3cwapiMIBObjects=h3cwapiMIBObjects, h3cwapiConfigExtEntry=h3cwapiConfigExtEntry, h3cwapiStatsWAITimeoutCounters=h3cwapiStatsWAITimeoutCounters, h3cwapiModeEnabled=h3cwapiModeEnabled, PYSNMP_MODULE_ID=h3cwapiMIB, h3cwapiConfigAuthMethod=h3cwapiConfigAuthMethod, h3cwapiConfigISPDomain=h3cwapiConfigISPDomain, h3cwapiTrapInfoBSSId=h3cwapiTrapInfoBSSId, h3cwapiStatsWAIUniHskFailures=h3cwapiStatsWAIUniHskFailures, h3cwapiMIBStatsObjects=h3cwapiMIBStatsObjects, h3cwapiConfigServicePolicyID=h3cwapiConfigServicePolicyID, h3cwapiConfigCertificateDomain=h3cwapiConfigCertificateDomain, h3cwapiCfgExtASName=h3cwapiCfgExtASName, h3cwapiStatsWAIHMACErrors=h3cwapiStatsWAIHMACErrors, h3cwapiStatsWAIFormatErrors=h3cwapiStatsWAIFormatErrors, h3cwapiConfigTable=h3cwapiConfigTable, h3cwapiCertificateInstalled=h3cwapiCertificateInstalled, h3cwapiCfgExtCertDomain=h3cwapiCfgExtCertDomain, h3cwapiConfigASIPAddress=h3cwapiConfigASIPAddress, h3cwapiConfigASIPAddressType=h3cwapiConfigASIPAddressType, h3cwapiTrapInfoMacAddr=h3cwapiTrapInfoMacAddr, h3cwapiStatsWAIDiscardCounters=h3cwapiStatsWAIDiscardCounters, h3cwapiConfigBKRekeyEnabled=h3cwapiConfigBKRekeyEnabled, h3cwapiAddressRedirectionAttack=h3cwapiAddressRedirectionAttack, h3cwapiConfigUnicastCipherEnabled=h3cwapiConfigUnicastCipherEnabled, h3cwapiConfigAuthMode=h3cwapiConfigAuthMode, h3cwapiTrapInfo=h3cwapiTrapInfo, h3cwapiCfgExtCertInstalled=h3cwapiCfgExtCertInstalled, h3cwapiCfgExtASIPAddressType=h3cwapiCfgExtASIPAddressType, h3cwapiConfigEntry=h3cwapiConfigEntry, h3cwapiLowSafeLevelAttack=h3cwapiLowSafeLevelAttack)