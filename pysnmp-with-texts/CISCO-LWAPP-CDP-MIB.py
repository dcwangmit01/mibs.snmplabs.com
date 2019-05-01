#
# PySNMP MIB module CISCO-LWAPP-CDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-CDP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:04:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
cLApSysMacAddress, = mibBuilder.importSymbols("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress")
CLCdpAdvtVersionType, = mibBuilder.importSymbols("CISCO-LWAPP-TC-MIB", "CLCdpAdvtVersionType")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, Bits, Counter64, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, Unsigned32, MibIdentifier, IpAddress, TimeTicks, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Counter64", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "Unsigned32", "MibIdentifier", "IpAddress", "TimeTicks", "Integer32", "Counter32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoLwappCdpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 623))
ciscoLwappCdpMIB.setRevisions(('2009-11-23 00:00', '2007-03-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappCdpMIB.setRevisionsDescriptions(('Added the variables clcCdpApCacheDuplex and clcCdpApCacheInterfaceSpeed to clcCdpApCacheTable.', 'This is the initial version of this module.',))
if mibBuilder.loadTexts: ciscoLwappCdpMIB.setLastUpdated('200911230000Z')
if mibBuilder.loadTexts: ciscoLwappCdpMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoLwappCdpMIB.setContactInfo('Cisco Systems, Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS Email: cs-wnbu-snmcp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappCdpMIB.setDescription("This MIB is intended to be implemented on all those devices operating as Central Controllers (CC) that terminate the Light Weight Access Point Protocol tunnel from Light-weight LWAPP Access Points. This MIB provides configuration and status information about CDP neighbors of LWAPP APs. The MIB provides configuration of CDP feature on the LWAPP Access Points. The MIB can also be used to retrive the status of the CDP cache information on the various LWAPP LWAPP Access Points. The CDP MIB is also supported by Controller and provides configuration and status information about CDP neighbours of the controller. The relationship between CC and the LWAPP APs can be depicted as follows: +......+ +......+ +......+ +......+ + + + + + + + + + CC + + CC + + CC + + CC + + + + + + + + + +......+ +......+ +......+ +......+ .. . . . .. . . . . . . . . . . . . . . . . . . . . . . . +......+ +......+ +......+ +......+ +......+ + + + + + + + + + + + AP + + AP + + AP + + AP + + AP + + + + + + + + + + + +......+ +......+ +......+ +......+ +......+ . . . . . . . . . . . . . . . . . . . . . . . . +......+ +......+ +......+ +......+ +......+ + + + + + + + + + + + MN + + MN + + MN + + MN + + MN + + + + + + + + + + + +......+ +......+ +......+ +......+ +......+ The LWAPP tunnel exists between the controller and the APs. The MNs communicate with the APs through the protocol defined by the 802.11 standard. LWAPP APs, upon bootup, discover and join one of the controllers and the controller pushes the configuration, that includes the WLAN parameters, to the LWAPP APs. The APs then encapsulate all the 802.11 frames from wireless clients inside LWAPP frames and forward the LWAPP frames to the controller. GLOSSARY Access Point ( AP ) An entity that contains an 802.11 medium access control ( MAC ) and physical layer ( PHY ) interface and provides access to the distribution services via the wireless medium for associated clients. LWAPP APs encapsulate all the 802.11 frames in LWAPP frames and sends it to the controller to which it is logically connected. Basic Service Set Identifier (BSSID) The identifier for the service set comprising of all the 802.11 stations under the control of one coordinating Access Point. This identifier happens to be the MAC address of the dot11 radio interface of the Access Point. The wireless clients that associate with the Access Point get the wired uplink through this particular dot11 interface. Central Controller ( CC ) The central entity that terminates the LWAPP protocol tunnel from the LWAPP APs. Throughout this MIB, this entity also referred to as 'controller'. Light Weight Access Point Protocol ( LWAPP ) This is a generic protocol that defines the communication between the Access Points and the Central Controller. Cisco Discovery Protocol ( CDP ) Protocol for discovery of neighboring devices. REFERENCE [1] Part 11 Wireless LAN Medium Access Control ( MAC ) and Physical Layer ( PHY ) Specifications. [2] Draft-obara-capwap-lwapp-00.txt, IETF Light Weight Access Point Protocol.")
ciscoLwappCdpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 623, 0))
ciscoLwappCdpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 623, 1))
ciscoLwappCdpMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 623, 2))
clcCdpTraffic = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 1))
clcCdpGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 2))
clcCdpApCacheStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3))
clcCdpApCacheConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 4))
clcCdpInPackets = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 1, 1), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clcCdpInPackets.setStatus('current')
if mibBuilder.loadTexts: clcCdpInPackets.setDescription('Count of total CDP packets received by the Controller.')
clcCdpOutPackets = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 1, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clcCdpOutPackets.setStatus('current')
if mibBuilder.loadTexts: clcCdpOutPackets.setDescription('Count of total CDP packets sent by the Controller.')
clcCdpChecksumErrorPackets = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 1, 3), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clcCdpChecksumErrorPackets.setStatus('current')
if mibBuilder.loadTexts: clcCdpChecksumErrorPackets.setDescription('Total number of CDP packets that experienced checksum error.')
clcCdpNoMemoryPackets = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 1, 4), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clcCdpNoMemoryPackets.setStatus('current')
if mibBuilder.loadTexts: clcCdpNoMemoryPackets.setDescription('Total number of CDP packets that were dropped because of no memory availability.')
clcCdpInvalidPackets = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 1, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clcCdpInvalidPackets.setStatus('current')
if mibBuilder.loadTexts: clcCdpInvalidPackets.setDescription('Total number of CDP packets that were invalid.')
clcCdpAdvtVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 2, 1), CLCdpAdvtVersionType().clone('cdpv1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clcCdpAdvtVersion.setStatus('current')
if mibBuilder.loadTexts: clcCdpAdvtVersion.setDescription('Cisco Discovery Protocol advertisement version.')
clcCdpMessageInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 2, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 900)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clcCdpMessageInterval.setStatus('current')
if mibBuilder.loadTexts: clcCdpMessageInterval.setDescription('The interval (in seconds) at which CDP messages are to be generated.')
clcCdpGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 2, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clcCdpGlobalEnable.setStatus('current')
if mibBuilder.loadTexts: clcCdpGlobalEnable.setDescription("This is a template variable to enable / disable CDP on all APs. When 'true' is set, then internally CDP is enabled on all APs associated with the Controller. When 'false' is set, then internally CDP is disabled on all APs associated with the Controller. However, setting this attribute has no effect when CDP is disabled globally, that is when the cdpGlobalRun from the CISCO-CDP-MIB is set to 'false'on the Controller.")
clcCdpApTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 4, 1), )
if mibBuilder.loadTexts: clcCdpApTable.setStatus('current')
if mibBuilder.loadTexts: clcCdpApTable.setDescription('The (conceptual) table containing the status of Cisco Discovery Protocol on LWAPP Access Points. An entry is added to the table when an Aceess Point joins a controller. An entry is deleted when the Access Point disassociates from the controller. This table is used to configure CDP feature per Access Point.')
clcCdpApEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 4, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"))
if mibBuilder.loadTexts: clcCdpApEntry.setStatus('current')
if mibBuilder.loadTexts: clcCdpApEntry.setDescription("An entry (conceptual row) in the clcCdpApTable, containing the status of CDP on an AP. Consider a setup where two APs, 'AP1' and 'AP2' have been connected to a CISCO-3750 switch. Both the APs register with WLAN CONTROLLER 440x which is on LAN/Internet/Intranet. +.........................+ + + + WLAN CONTROLLER 4400 + + 10.14.2.11 + +.........................+ .. .. INTERNET .. LAN .. +...............+ + + + SWITCH-3750 + + 10.16.1.1 + +...............+ .. . . . . . . . . . . +......+ +......+ + + + + + AP1 + + AP2 + + + + + +......+ +......+ 00:12:CF:DA:29:11 23:43:CE:9A:66:76 10.16.1.43 10.16.1.45 Given the above example, the clcCdpApEntry on WLAN CONTROLLER 4400 looks like : ------------------------------------------------------------------ | MIB - ATTRIBUTES | ROW#1 | ROW#2 | ------------------------------------------------------------------ | cLApSysMacAddress | 00:12:CF:DA:29:11 | 23:43:CE:9A:66:76 | ------------------------------------------------------------------ | clcCdpApStatus | true | false | ------------------------------------------------------------------")
clcCdpApCdpEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 4, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clcCdpApCdpEnable.setStatus('current')
if mibBuilder.loadTexts: clcCdpApCdpEnable.setDescription("An indication of whether the Cisco Discovery Protocol is currently running on this AP. When set to 'true', that means CDP is enabled on the AP denoted by MAC address cLApSysMacAddress. When set to 'false', that means CDP is disabled on the AP denoted by MAC address cLApSysMacAddress. This variable has no effect when CDP is globally disabled. That is when the cdpGlobalRun from the CISCO-CDP-MIB is set to 'false'.")
clcCdpApCacheTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1), )
if mibBuilder.loadTexts: clcCdpApCacheTable.setStatus('current')
if mibBuilder.loadTexts: clcCdpApCacheTable.setDescription('This table contains the cached neighbor information obtained via receiving CDP messages on APs. Entries are added to this table when a CDP advertisement is received from a neighboring device. Entries get deleted when CDP is disabled on the interface or globally.')
clcCdpApCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"), (0, "CISCO-LWAPP-CDP-MIB", "clcCdpApCacheDeviceIndex"))
if mibBuilder.loadTexts: clcCdpApCacheEntry.setStatus('current')
if mibBuilder.loadTexts: clcCdpApCacheEntry.setDescription("An entry in the clcCdpApCacheTable, containing the information received via CDP on one interface from one device. Entries appear when a CDP advertisement is received from a neighbor device. Entries disappear when CDP is disabled on the interface or globally. Consider a setup where two APs, 'AP1' and 'AP2' have been connected to a CISCO-3750 switch. Both the APs register with WLAN CONTROLLER 4400 which is on LAN/Internet/Intranet. +.........................+ + + + WLAN CONTROLLER 4400 + + 10.14.2.11 + +.........................+ .. .. INTERNET .. LAN .. +...............+ + + + SWITCH-3750 + + 10.16.1.1 + +...............+ FE 0/13 .. FE 0/15 . . . . . . . . . . +......+ +......+ + + + + + AP1 + + AP2 + + + + + +......+ +......+ 00:12:CF:DA:29:11 23:43:CE:9A:66:76 10.16.1.43 10.16.1.45 Given the above example, the clcCdpApEntry on WLAN CONTROLLER 4400 looks like : ---------------------------------------------------------------------- | MIB - ATTRIBUTES | ROW#1 | ROW#2 | ---------------------------------------------------------------------- | cLApSysMacAddress | 00:12:CF:DA:29:11 | 23:43:CE:9A:66:76| ---------------------------------------------------------------------- | clcCdpApCacheDeviceIndex | 16 | 16 | ---------------------------------------------------------------------- | clcCdpApCacheApName | AP1 | AP2 | ---------------------------------------------------------------------- | clcCdpApCacheApAddressType | ip(1) | ip(1) | ---------------------------------------------------------------------- | clcCdpApCacheApAddress | 10.16.1.43 | 10.16.1.45 | ---------------------------------------------------------------------- | clcCdpApCacheLocalInterface | Port - 1 | Port -2 | ---------------------------------------------------------------------- | clcCdpApCacheNeighName | SWITCH-3750 | SWITCH-3750 | ---------------------------------------------------------------------- | clcCdpApCacheNeighAddressType| ip(1) | ip(1) | ---------------------------------------------------------------------- | clcCdpApCacheNeighAddress | 10.16.1.1 | 10.16.1.1 | ---------------------------------------------------------------------- | clcCdpApCacheNeighInterface | FE 0/13 | FE 0/45 | ---------------------------------------------------------------------- | clcCdpApCacheNeighVersion | IOS Ver2.2. ... | IOS Ver 2.2. ... | ---------------------------------------------------------------------- | clcCdpApCacheAdvtVersion | cdpv1(1) | cdpv2(2) | ---------------------------------------------------------------------- | clcCdpApCachePlatform | WS-C3750-24P | WS-C3750-24P | ---------------------------------------------------------------------- | clcCdpApCacheCapabilities | RSI | RSI | ---------------------------------------------------------------------- | clcCdpApCacheHoldtimeLeft | 179 | 165 | ---------------------------------------------------------------------- | clcCdpApCacheDuplex | fullduplex(3) | fullduplex(3) | ---------------------------------------------------------------------- | clcCdpApCacheInterfaceSpeed | hundredMbps(2) | hundredMbps(2) | ----------------------------------------------------------------------")
clcCdpApCacheDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: clcCdpApCacheDeviceIndex.setStatus('current')
if mibBuilder.loadTexts: clcCdpApCacheDeviceIndex.setDescription('A unique value for each device from which CDP messages are being received.')
clcCdpApCacheApName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clcCdpApCacheApName.setStatus('current')
if mibBuilder.loadTexts: clcCdpApCacheApName.setDescription('Name assigned to this AP. If an AP is not configured its factory default name will be ap:<last three byte of MAC Address>. eg. ap:af:12:be')
clcCdpApCacheApAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clcCdpApCacheApAddressType.setStatus('current')
if mibBuilder.loadTexts: clcCdpApCacheApAddressType.setDescription('An indication of the type of address contained in the corresponding instance of clcCdpApCacheAddress for the AP.')
clcCdpApCacheApAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clcCdpApCacheApAddress.setStatus('current')
if mibBuilder.loadTexts: clcCdpApCacheApAddress.setDescription("This is the address of the AP. For example, if the the corresponding instance of clcCdpApCacheApAddressType had the value 'ip(1)', then this object would be an IP-address.")
clcCdpApCacheLocalInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 5), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clcCdpApCacheLocalInterface.setStatus('current')
if mibBuilder.loadTexts: clcCdpApCacheLocalInterface.setDescription('This is the local port on which LWAPP encapsulated CDP packets was received.')
clcCdpApCacheNeighName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clcCdpApCacheNeighName.setStatus('current')
if mibBuilder.loadTexts: clcCdpApCacheNeighName.setDescription('The Device-ID string as reported in the most recent CDP message. The zero-length string indicates no Device-ID field (TLV) was reported in the most recent CDP message.')
clcCdpApCacheNeighAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 7), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clcCdpApCacheNeighAddressType.setStatus('current')
if mibBuilder.loadTexts: clcCdpApCacheNeighAddressType.setDescription('An indication of the type of address contained in the corresponding instance of clcCdpApCacheAddress of Neighbor.')
clcCdpApCacheNeighAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 8), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clcCdpApCacheNeighAddress.setStatus('current')
if mibBuilder.loadTexts: clcCdpApCacheNeighAddress.setDescription("The (first) network-layer address of the device's SNMP-agent as reported in the most recent CDP message. For example, if the the corresponding instance of clcCdpApCacheApAddressType had the value 'ip(1)', then this object would be an IP-address.")
clcCdpApCacheNeighInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clcCdpApCacheNeighInterface.setStatus('current')
if mibBuilder.loadTexts: clcCdpApCacheNeighInterface.setDescription("The Port-ID string as reported in the most recent CDP message. This will typically be the value of the ifName object (e.g., 'Ethernet0'). The zero-length string indicates no Port-ID field (TLV) was reported in the most recent CDP message.")
clcCdpApCacheNeighVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clcCdpApCacheNeighVersion.setStatus('current')
if mibBuilder.loadTexts: clcCdpApCacheNeighVersion.setDescription('The Version string refers to the software running on neighboring device.')
clcCdpApCacheAdvtVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 11), CLCdpAdvtVersionType().clone('cdpv1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clcCdpApCacheAdvtVersion.setStatus('current')
if mibBuilder.loadTexts: clcCdpApCacheAdvtVersion.setDescription('Cisco Discovery Protocol advertisement version.')
clcCdpApCachePlatform = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clcCdpApCachePlatform.setStatus('current')
if mibBuilder.loadTexts: clcCdpApCachePlatform.setDescription("The Device's Hardware Platform as reported in the most recent CDP message. The zero-length string indicates that no Platform field (TLV) was reported in the most recent CDP message.")
clcCdpApCacheCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clcCdpApCacheCapabilities.setStatus('current')
if mibBuilder.loadTexts: clcCdpApCacheCapabilities.setDescription("The Device's Functional Capabilities as reported in the most recent CDP message. For latest set of specific values, see the latest version of the CDP specification. The zero-length string indicates no Capabilities field (TLV) was reported in the most recent CDP message.")
clcCdpApCacheHoldtimeLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 255)).clone(180)).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: clcCdpApCacheHoldtimeLeft.setStatus('current')
if mibBuilder.loadTexts: clcCdpApCacheHoldtimeLeft.setDescription('The time left, in seconds, before the CDP neighbor entry gets aged-out.')
clcCdpApCacheDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("fullduplex", 2), ("halfduplex", 3), ("auto", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clcCdpApCacheDuplex.setStatus('current')
if mibBuilder.loadTexts: clcCdpApCacheDuplex.setDescription("This object denotes the duplex mode of the Ethernet interface between the AP and it's neighboring CDP device, as reported in the most recent CDP message. The value unknown(1) indicates no duplex mode field (TLV) was reported in the most recent CDP message or the neighboring device is not connected to the AP though ethernet interface.")
clcCdpApCacheInterfaceSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("tenMbps", 2), ("hundredMbps", 3), ("thousandMbps", 4), ("auto", 5)))).setUnits('Mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: clcCdpApCacheInterfaceSpeed.setStatus('current')
if mibBuilder.loadTexts: clcCdpApCacheInterfaceSpeed.setDescription("This variable denotes the speed of the Ethernet interface between the AP and it's neighboring CDP device. The unit is Mbps. This variable would be populated at AP join and periodically thereafter. The value none(1), would be shown if the interface is not an ethernet interface.")
ciscoLwappCdpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 623, 2, 1))
ciscoLwappCdpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 623, 2, 2))
ciscoLwappCdpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 623, 2, 1, 1)).setObjects(("CISCO-LWAPP-CDP-MIB", "clcCdpRev01ConfigGroup"), ("CISCO-LWAPP-CDP-MIB", "clcCdpRev01StatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappCdpMIBCompliance = ciscoLwappCdpMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoLwappCdpMIBCompliance.setDescription('The compliance statement for the SNMP entities that implement the ciscoLwappCdpMIB module.')
ciscoLwappCdpMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 623, 2, 1, 2)).setObjects(("CISCO-LWAPP-CDP-MIB", "clcCdpRev01ConfigGroup"), ("CISCO-LWAPP-CDP-MIB", "clcCdpRev01StatusGroup"), ("CISCO-LWAPP-CDP-MIB", "clcCdpRev02StatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappCdpMIBComplianceRev1 = ciscoLwappCdpMIBComplianceRev1.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappCdpMIBComplianceRev1.setDescription('The compliance statement for the SNMP entities that implement the ciscoLwappCdpMIB module.')
clcCdpRev01ConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 623, 2, 2, 1)).setObjects(("CISCO-LWAPP-CDP-MIB", "clcCdpApCdpEnable"), ("CISCO-LWAPP-CDP-MIB", "clcCdpAdvtVersion"), ("CISCO-LWAPP-CDP-MIB", "clcCdpMessageInterval"), ("CISCO-LWAPP-CDP-MIB", "clcCdpGlobalEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCdpRev01ConfigGroup = clcCdpRev01ConfigGroup.setStatus('current')
if mibBuilder.loadTexts: clcCdpRev01ConfigGroup.setDescription('This is a collection of objects which can configured to control functional parameters of Cisco Discovery Protocol feature in WLAN controllers and LWAPP APs.')
clcCdpRev01StatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 623, 2, 2, 2)).setObjects(("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheApName"), ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheApAddressType"), ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheApAddress"), ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheLocalInterface"), ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheNeighName"), ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheNeighAddressType"), ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheNeighAddress"), ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheNeighInterface"), ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheNeighVersion"), ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheAdvtVersion"), ("CISCO-LWAPP-CDP-MIB", "clcCdpApCachePlatform"), ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheCapabilities"), ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheHoldtimeLeft"), ("CISCO-LWAPP-CDP-MIB", "clcCdpInPackets"), ("CISCO-LWAPP-CDP-MIB", "clcCdpOutPackets"), ("CISCO-LWAPP-CDP-MIB", "clcCdpChecksumErrorPackets"), ("CISCO-LWAPP-CDP-MIB", "clcCdpNoMemoryPackets"), ("CISCO-LWAPP-CDP-MIB", "clcCdpInvalidPackets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCdpRev01StatusGroup = clcCdpRev01StatusGroup.setStatus('current')
if mibBuilder.loadTexts: clcCdpRev01StatusGroup.setDescription('This collection of objects represents the information about the general status attributes of Cisco Discovery Protocol in WLAN controllers and LWAPP APs.')
clcCdpRev02StatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 623, 2, 2, 3)).setObjects(("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheDuplex"), ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheInterfaceSpeed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCdpRev02StatusGroup = clcCdpRev02StatusGroup.setStatus('current')
if mibBuilder.loadTexts: clcCdpRev02StatusGroup.setDescription('These are the additional objects which represent the information about the general status attributes of Cisco Discovery Protocol in WLAN controllers and LWAPP APs.')
mibBuilder.exportSymbols("CISCO-LWAPP-CDP-MIB", clcCdpApCacheInterfaceSpeed=clcCdpApCacheInterfaceSpeed, clcCdpOutPackets=clcCdpOutPackets, clcCdpApEntry=clcCdpApEntry, ciscoLwappCdpMIBComplianceRev1=ciscoLwappCdpMIBComplianceRev1, clcCdpChecksumErrorPackets=clcCdpChecksumErrorPackets, clcCdpNoMemoryPackets=clcCdpNoMemoryPackets, clcCdpApCacheNeighName=clcCdpApCacheNeighName, clcCdpApCacheAdvtVersion=clcCdpApCacheAdvtVersion, clcCdpApCacheNeighVersion=clcCdpApCacheNeighVersion, ciscoLwappCdpMIBGroups=ciscoLwappCdpMIBGroups, ciscoLwappCdpMIBCompliances=ciscoLwappCdpMIBCompliances, clcCdpApCacheNeighAddress=clcCdpApCacheNeighAddress, clcCdpApCdpEnable=clcCdpApCdpEnable, clcCdpMessageInterval=clcCdpMessageInterval, clcCdpApCacheHoldtimeLeft=clcCdpApCacheHoldtimeLeft, ciscoLwappCdpMIBConform=ciscoLwappCdpMIBConform, clcCdpTraffic=clcCdpTraffic, clcCdpApCacheApName=clcCdpApCacheApName, clcCdpApCacheConfig=clcCdpApCacheConfig, ciscoLwappCdpMIBNotifs=ciscoLwappCdpMIBNotifs, clcCdpApCacheDuplex=clcCdpApCacheDuplex, clcCdpRev01StatusGroup=clcCdpRev01StatusGroup, clcCdpApCacheDeviceIndex=clcCdpApCacheDeviceIndex, clcCdpAdvtVersion=clcCdpAdvtVersion, clcCdpApCacheLocalInterface=clcCdpApCacheLocalInterface, clcCdpApCacheStatus=clcCdpApCacheStatus, clcCdpGlobalEnable=clcCdpGlobalEnable, clcCdpRev01ConfigGroup=clcCdpRev01ConfigGroup, ciscoLwappCdpMIBCompliance=ciscoLwappCdpMIBCompliance, PYSNMP_MODULE_ID=ciscoLwappCdpMIB, clcCdpApCacheNeighAddressType=clcCdpApCacheNeighAddressType, ciscoLwappCdpMIBObjects=ciscoLwappCdpMIBObjects, clcCdpInvalidPackets=clcCdpInvalidPackets, clcCdpGlobalConfig=clcCdpGlobalConfig, clcCdpApCacheApAddress=clcCdpApCacheApAddress, clcCdpApCacheEntry=clcCdpApCacheEntry, clcCdpApTable=clcCdpApTable, clcCdpApCacheNeighInterface=clcCdpApCacheNeighInterface, clcCdpApCacheApAddressType=clcCdpApCacheApAddressType, clcCdpApCacheCapabilities=clcCdpApCacheCapabilities, ciscoLwappCdpMIB=ciscoLwappCdpMIB, clcCdpApCacheTable=clcCdpApCacheTable, clcCdpInPackets=clcCdpInPackets, clcCdpApCachePlatform=clcCdpApCachePlatform, clcCdpRev02StatusGroup=clcCdpRev02StatusGroup)