#
# PySNMP MIB module NETSCREEN-BGP4-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETSCREEN-BGP4-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:20:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
netscreenVR, = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenVR")
netscreenTrapDesc, netscreenTrapType = mibBuilder.importSymbols("NETSCREEN-TRAP-MIB", "netscreenTrapDesc", "netscreenTrapType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter64, TimeTicks, Gauge32, ObjectIdentity, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, ModuleIdentity, iso, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "TimeTicks", "Gauge32", "ObjectIdentity", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "ModuleIdentity", "iso", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nsBgp = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 18, 3))
if mibBuilder.loadTexts: nsBgp.setLastUpdated('200506032022Z')
if mibBuilder.loadTexts: nsBgp.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: nsBgp.setContactInfo('Customer Support 1194 North Mathilda Avenue Sunnyvale, California 94089-1206 USA Tel: 1-800-638-8296 E-mail: customerservice@juniper.net HTTP://www.juniper.net')
if mibBuilder.loadTexts: nsBgp.setDescription('The MIB module for NS-BGP-4.')
nsBgpInfoTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 18, 3, 1), )
if mibBuilder.loadTexts: nsBgpInfoTable.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpInfoTable.setDescription("BGP info table. This table contains, one entry per VR, information about the BGP's Version, LocalAs and Identifier.")
nsBgpInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 18, 3, 1, 1), ).setIndexNames((0, "NETSCREEN-BGP4-MIB", "nsBgpInfoVRID"))
if mibBuilder.loadTexts: nsBgpInfoEntry.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpInfoEntry.setDescription("Entry containing information about the BGP's Version, LocalAs and Identifier")
nsBgpInfoVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpInfoVersion.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpInfoVersion.setDescription('Vector of supported BGP protocol version numbers. Each peer negotiates the version from this vector. Versions are identified via the string of bits contained within this object. The first octet contains bits 0 to 7, the second octet contains bits 8 to 15, and so on, with the most significant bit referring to the lowest bit number in the octet (e.g., the MSB of the first octet refers to bit 0). If a bit, i, is present and set, then the version (i+1) of the BGP is supported.')
nsBgpInfoLocalAs = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpInfoLocalAs.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpInfoLocalAs.setDescription('The local autonomous system number.')
nsBgpInfoIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpInfoIdentifier.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpInfoIdentifier.setDescription('The BGP Identifier of local system.')
nsBgpInfoVRID = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpInfoVRID.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpInfoVRID.setDescription('Virtual Router ID')
nsBgpPeerTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3), )
if mibBuilder.loadTexts: nsBgpPeerTable.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerTable.setDescription('BGP peer table. This table contains, one entry per BGP peer, information about the connections with BGP peers.')
nsBgpPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1), ).setIndexNames((0, "NETSCREEN-BGP4-MIB", "nsBgpPeerRemoteAddr"), (0, "NETSCREEN-BGP4-MIB", "nsBgpPeerVRID"))
if mibBuilder.loadTexts: nsBgpPeerEntry.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerEntry.setDescription('Entry containing information about the connection with a BGP peer.')
nsBgpPeerIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerIdentifier.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerIdentifier.setDescription("The BGP Identifier of this entry's BGP peer.")
nsBgpPeerState = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("idle", 1), ("connect", 2), ("active", 3), ("opensent", 4), ("openconfirm", 5), ("established", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerState.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerState.setDescription('The BGP peer connection state.')
nsBgpPeerAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stop", 1), ("start", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerAdminStatus.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerAdminStatus.setDescription("The desired state of the BGP connection. A transition from 'stop' to 'start' will cause the BGP Start Event to be generated. A transition from 'start' to 'stop' will cause the BGP Stop Event to be generated. This parameter can be used to restart BGP peer connections. Care should be used in providing write access to this object without adequate authentication.")
nsBgpPeerNegotiatedVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerNegotiatedVersion.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerNegotiatedVersion.setDescription('The negotiated version of BGP running between the two peers.')
nsBgpPeerLocalAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerLocalAddr.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerLocalAddr.setDescription("The local IP address of this entry's BGP connection.")
nsBgpPeerLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerLocalPort.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerLocalPort.setDescription('The local port for the TCP connection between the BGP peers.')
nsBgpPeerRemoteAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerRemoteAddr.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerRemoteAddr.setDescription("The remote IP address of this entry's BGP peer.")
nsBgpPeerRemotePort = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerRemotePort.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerRemotePort.setDescription('The remote port for the TCP connection between the BGP peers. Note that the objects nsBgpPeerLocalAddr, nsBgpPeerLocalPort, nsBgpPeerRemoteAddr and nsBgpPeerRemotePort provide the appropriate reference to the standard MIB TCP connection table.')
nsBgpPeerRemoteAs = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerRemoteAs.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerRemoteAs.setDescription('The remote autonomous system number.')
nsBgpPeerInUpdates = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerInUpdates.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerInUpdates.setDescription('The number of BGP UPDATE messages received on this connection. This object should be initialized to zero (0) when the connection is established.')
nsBgpPeerOutUpdates = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerOutUpdates.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerOutUpdates.setDescription('The number of BGP UPDATE messages transmitted on this connection. This object should be initialized to zero (0) when the connection is established.')
nsBgpPeerInTotalMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerInTotalMessages.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerInTotalMessages.setDescription('The total number of messages received from the remote peer on this connection. This object should be initialized to zero when the connection is established.')
nsBgpPeerOutTotalMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerOutTotalMessages.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerOutTotalMessages.setDescription('The total number of messages transmitted to the remote peer on this connection. This object should be initialized to zero when the connection is established.')
nsBgpPeerLastError = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerLastError.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerLastError.setDescription('The last error code and subcode seen by this peer on this connection. If no error has occurred, this field is zero. Otherwise, the first byte of this two byte OCTET STRING contains the error code, and the second byte contains the subcode.')
nsBgpPeerFsmEstablishedTransitions = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerFsmEstablishedTransitions.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerFsmEstablishedTransitions.setDescription('The total number of times the BGP FSM transitioned into the established state.')
nsBgpPeerFsmEstablishedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerFsmEstablishedTime.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerFsmEstablishedTime.setDescription('This timer indicates how long (in seconds) this peer has been in the Established state or how long since this peer was last in the Established state. It is set to zero when a new peer is configured or the router is booted.')
nsBgpPeerConnectRetryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerConnectRetryInterval.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerConnectRetryInterval.setDescription('Time interval in seconds for the ConnectRetry timer. The suggested value for this timer is 120 seconds.')
nsBgpPeerHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3, 65535), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerHoldTime.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerHoldTime.setDescription('Time interval in seconds for the Hold Timer established with the peer. The value of this object is calculated by this BGP speaker by using the smaller of the value in nsBgpPeerHoldTimeConfigured and the Hold Time received in the OPEN message. This value must be at lease three seconds if it is not zero (0) in which case the Hold Timer has not been established with the peer, or, the value of nsBgpPeerHoldTimeConfigured is zero (0).')
nsBgpPeerKeepAlive = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 21845), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerKeepAlive.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerKeepAlive.setDescription('Time interval in seconds for the KeepAlive timer established with the peer. The value of this object is calculated by this BGP speaker such that, when compared with nsBgpPeerHoldTime, it has the same proportion as what nsBgpPeerKeepAliveConfigured has when compared with nsBgpPeerHoldTimeConfigured. If the value of this object is zero (0), it indicates that the KeepAlive timer has not been established with the peer, or, the value of nsBgpPeerKeepAliveConfigured is zero (0).')
nsBgpPeerHoldTimeConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3, 65535), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerHoldTimeConfigured.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerHoldTimeConfigured.setDescription('Time interval in seconds for the Hold Time configured for this BGP speaker with this peer. This value is placed in an OPEN message sent to this peer by this BGP speaker, and is compared with the Hold Time field in an OPEN message received from the peer when determining the Hold Time (nsBgpPeerHoldTime) with the peer. This value must not be less than three seconds if it is not zero (0) in which case the Hold Time is NOT to be established with the peer. The suggested value for this timer is 90 seconds.')
nsBgpPeerKeepAliveConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 21845), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerKeepAliveConfigured.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerKeepAliveConfigured.setDescription("Time interval in seconds for the KeepAlive timer configured for this BGP speaker with this peer. The value of this object will only determine the KEEPALIVE messages' frequency relative to the value specified in nsBgpPeerHoldTimeConfigured; the actual time interval for the KEEPALIVE messages is indicated by nsBgpPeerKeepAlive. A reasonable maximum value for this timer would be configured to be one third of that of nsBgpPeerHoldTimeConfigured. If the value of this object is zero (0), no periodical KEEPALIVE messages are sent to the peer after the BGP connection has been established. The suggested value for this timer is 30 seconds.")
nsBgpPeerMinASOriginationInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerMinASOriginationInterval.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerMinASOriginationInterval.setDescription('Time interval in seconds for the MinASOriginationInterval timer. The suggested value for this timer is 15 seconds.')
nsBgpPeerMinRouteAdvertisementInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerMinRouteAdvertisementInterval.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerMinRouteAdvertisementInterval.setDescription('Time interval in seconds for the MinRouteAdvertisementInterval timer. The suggested value for this timer is 30 seconds.')
nsBgpPeerInUpdateElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 24), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerInUpdateElapsedTime.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerInUpdateElapsedTime.setDescription('Elapsed time in seconds since the last BGP UPDATE message was received from the peer. Each time nsBgpPeerInUpdates is incremented, the value of this object is set to zero (0).')
nsBgpPeerVRID = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgpPeerVRID.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpPeerVRID.setDescription('Virtual Router ID')
nsBgp4PathAttrTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 18, 3, 6), )
if mibBuilder.loadTexts: nsBgp4PathAttrTable.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgp4PathAttrTable.setDescription('The BGP-4 Received Path Attribute Table contains information about paths to destination networks received from all BGP4 peers.')
nsBgp4PathAttrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1), ).setIndexNames((0, "NETSCREEN-BGP4-MIB", "nsBgp4PathAttrIpAddrPrefix"), (0, "NETSCREEN-BGP4-MIB", "nsBgp4PathAttrIpAddrPrefixLen"), (0, "NETSCREEN-BGP4-MIB", "nsBgp4PathAttrPeer"), (0, "NETSCREEN-BGP4-MIB", "nsBgp4PathAttrVRID"))
if mibBuilder.loadTexts: nsBgp4PathAttrEntry.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgp4PathAttrEntry.setDescription('Information about a path to a network.')
nsBgp4PathAttrPeer = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgp4PathAttrPeer.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgp4PathAttrPeer.setDescription('The IP address of the peer where the path information was learned.')
nsBgp4PathAttrIpAddrPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgp4PathAttrIpAddrPrefixLen.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgp4PathAttrIpAddrPrefixLen.setDescription('Length in bits of the IP address prefix in the Network Layer Reachability Information field.')
nsBgp4PathAttrIpAddrPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgp4PathAttrIpAddrPrefix.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgp4PathAttrIpAddrPrefix.setDescription('An IP address prefix in the Network Layer Reachability Information field. This object is an IP address containing the prefix with length specified by nsBgp4PathAttrIpAddrPrefixLen. Any bits beyond the length specified by nsBgp4PathAttrIpAddrPrefixLen are zeroed.')
nsBgp4PathAttrOrigin = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("igp", 1), ("egp", 2), ("incomplete", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgp4PathAttrOrigin.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgp4PathAttrOrigin.setDescription('The ultimate origin of the path information.')
nsBgp4PathAttrASPathSegment = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgp4PathAttrASPathSegment.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgp4PathAttrASPathSegment.setDescription('The sequence of AS path segments. Each AS path segment is represented by a triple <type, length, value>. The type is a 1-octet field which has two possible values: 1 AS_SET: unordered set of ASs a route in the UPDATE message has traversed 2 AS_SEQUENCE: ordered set of ASs a route in the UPDATE message has traversed. The length is a 1-octet field containing the number of ASs in the value field. The value field contains one or more AS numbers, each AS is represented in the octet string as a pair of octets according to the following algorithm: first-byte-of-pair = ASNumber / 256; second-byte-of-pair = ASNumber & 255;')
nsBgp4PathAttrNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgp4PathAttrNextHop.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgp4PathAttrNextHop.setDescription('The address of the border router that should be used for the destination network.')
nsBgp4PathAttrMultiExitDisc = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgp4PathAttrMultiExitDisc.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgp4PathAttrMultiExitDisc.setDescription('This metric is used to discriminate between multiple exit points to an adjacent autonomous system. A value of -1 indicates the absence of this attribute.')
nsBgp4PathAttrLocalPref = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgp4PathAttrLocalPref.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgp4PathAttrLocalPref.setDescription("The originating BGP4 speaker's degree of preference for an advertised route. A value of -1 indicates the absence of this attribute.")
nsBgp4PathAttrAtomicAggregate = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lessSpecificRrouteNotSelected", 1), ("lessSpecificRouteSelected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgp4PathAttrAtomicAggregate.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgp4PathAttrAtomicAggregate.setDescription('Whether or not the local system has selected a less specific route without selecting a more specific route.')
nsBgp4PathAttrAggregatorAS = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgp4PathAttrAggregatorAS.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgp4PathAttrAggregatorAS.setDescription('The AS number of the last BGP4 speaker that performed route aggregation. A value of zero (0) indicates the absence of this attribute.')
nsBgp4PathAttrAggregatorAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 11), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgp4PathAttrAggregatorAddr.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgp4PathAttrAggregatorAddr.setDescription('The IP address of the last BGP4 speaker that performed route aggregation. A value of 0.0.0.0 indicates the absence of this attribute.')
nsBgp4PathAttrCalcLocalPref = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgp4PathAttrCalcLocalPref.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgp4PathAttrCalcLocalPref.setDescription('The degree of preference calculated by the receiving BGP4 speaker for an advertised route. A value of -1 indicates the absence of this attribute.')
nsBgp4PathAttrBest = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgp4PathAttrBest.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgp4PathAttrBest.setDescription('An indication of whether or not this route was chosen as the best BGP4 route.')
nsBgp4PathAttrUnknown = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgp4PathAttrUnknown.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgp4PathAttrUnknown.setDescription('One or more path attributes not understood by this BGP4 speaker. Size zero (0) indicates the absence of such attribute(s). Octets beyond the maximum size, if any, are not recorded by this object.')
nsBgp4PathAttrVRID = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsBgp4PathAttrVRID.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgp4PathAttrVRID.setDescription('Virtual Router ID')
nsBgpTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 18, 3, 7))
nsBgpEstablished = NotificationType((1, 3, 6, 1, 4, 1, 3224, 18, 3, 7, 1)).setObjects(("NETSCREEN-TRAP-MIB", "netscreenTrapType"), ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"), ("NETSCREEN-BGP4-MIB", "nsBgpPeerIdentifier"), ("NETSCREEN-BGP4-MIB", "nsBgpPeerVRID"), ("NETSCREEN-BGP4-MIB", "nsBgpPeerLastError"), ("NETSCREEN-BGP4-MIB", "nsBgpPeerState"))
if mibBuilder.loadTexts: nsBgpEstablished.setStatus('deprecated')
if mibBuilder.loadTexts: nsBgpEstablished.setDescription('The BGP Established event is generated when the BGP FSM enters the ESTABLISHED state.')
mibBuilder.exportSymbols("NETSCREEN-BGP4-MIB", nsBgp4PathAttrMultiExitDisc=nsBgp4PathAttrMultiExitDisc, nsBgpPeerInUpdateElapsedTime=nsBgpPeerInUpdateElapsedTime, nsBgpInfoIdentifier=nsBgpInfoIdentifier, nsBgp4PathAttrNextHop=nsBgp4PathAttrNextHop, nsBgpEstablished=nsBgpEstablished, nsBgp4PathAttrASPathSegment=nsBgp4PathAttrASPathSegment, nsBgp4PathAttrLocalPref=nsBgp4PathAttrLocalPref, nsBgpPeerHoldTime=nsBgpPeerHoldTime, nsBgpPeerFsmEstablishedTime=nsBgpPeerFsmEstablishedTime, nsBgp4PathAttrIpAddrPrefix=nsBgp4PathAttrIpAddrPrefix, nsBgpPeerMinRouteAdvertisementInterval=nsBgpPeerMinRouteAdvertisementInterval, nsBgp4PathAttrUnknown=nsBgp4PathAttrUnknown, nsBgpInfoVersion=nsBgpInfoVersion, nsBgpPeerOutUpdates=nsBgpPeerOutUpdates, PYSNMP_MODULE_ID=nsBgp, nsBgpInfoLocalAs=nsBgpInfoLocalAs, nsBgp4PathAttrCalcLocalPref=nsBgp4PathAttrCalcLocalPref, nsBgp4PathAttrTable=nsBgp4PathAttrTable, nsBgp4PathAttrVRID=nsBgp4PathAttrVRID, nsBgp=nsBgp, nsBgpPeerAdminStatus=nsBgpPeerAdminStatus, nsBgpPeerTable=nsBgpPeerTable, nsBgpPeerLastError=nsBgpPeerLastError, nsBgpPeerRemoteAs=nsBgpPeerRemoteAs, nsBgp4PathAttrAtomicAggregate=nsBgp4PathAttrAtomicAggregate, nsBgpPeerLocalPort=nsBgpPeerLocalPort, nsBgpPeerNegotiatedVersion=nsBgpPeerNegotiatedVersion, nsBgpPeerRemoteAddr=nsBgpPeerRemoteAddr, nsBgpPeerMinASOriginationInterval=nsBgpPeerMinASOriginationInterval, nsBgp4PathAttrIpAddrPrefixLen=nsBgp4PathAttrIpAddrPrefixLen, nsBgpTraps=nsBgpTraps, nsBgpPeerInTotalMessages=nsBgpPeerInTotalMessages, nsBgpPeerRemotePort=nsBgpPeerRemotePort, nsBgpPeerVRID=nsBgpPeerVRID, nsBgpPeerEntry=nsBgpPeerEntry, nsBgp4PathAttrPeer=nsBgp4PathAttrPeer, nsBgpPeerKeepAliveConfigured=nsBgpPeerKeepAliveConfigured, nsBgpPeerFsmEstablishedTransitions=nsBgpPeerFsmEstablishedTransitions, nsBgp4PathAttrBest=nsBgp4PathAttrBest, nsBgpInfoTable=nsBgpInfoTable, nsBgp4PathAttrEntry=nsBgp4PathAttrEntry, nsBgpInfoVRID=nsBgpInfoVRID, nsBgp4PathAttrAggregatorAddr=nsBgp4PathAttrAggregatorAddr, nsBgpPeerState=nsBgpPeerState, nsBgpPeerKeepAlive=nsBgpPeerKeepAlive, nsBgp4PathAttrOrigin=nsBgp4PathAttrOrigin, nsBgpPeerIdentifier=nsBgpPeerIdentifier, nsBgpPeerInUpdates=nsBgpPeerInUpdates, nsBgpPeerLocalAddr=nsBgpPeerLocalAddr, nsBgpPeerOutTotalMessages=nsBgpPeerOutTotalMessages, nsBgpPeerHoldTimeConfigured=nsBgpPeerHoldTimeConfigured, nsBgpInfoEntry=nsBgpInfoEntry, nsBgpPeerConnectRetryInterval=nsBgpPeerConnectRetryInterval, nsBgp4PathAttrAggregatorAS=nsBgp4PathAttrAggregatorAS)