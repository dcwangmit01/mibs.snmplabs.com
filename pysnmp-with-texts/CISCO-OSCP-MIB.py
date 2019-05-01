#
# PySNMP MIB module CISCO-OSCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-OSCP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:08:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, Integer32, Bits, iso, Counter64, TimeTicks, IpAddress, MibIdentifier, Gauge32, NotificationType, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "Integer32", "Bits", "iso", "Counter64", "TimeTicks", "IpAddress", "MibIdentifier", "Gauge32", "NotificationType", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
ciscoOscpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 202))
ciscoOscpMIB.setRevisions(('2001-05-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoOscpMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoOscpMIB.setLastUpdated('200105180000Z')
if mibBuilder.loadTexts: ciscoOscpMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoOscpMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-dwdm@cisco.com')
if mibBuilder.loadTexts: ciscoOscpMIB.setDescription('The MIB module for managing the Cisco Optical Supervisory Channel Protocol (OSCP). The OSCP is used to determine and maintain wavelength connectivity with remote nodes. OSCP includes support for bundles of wavelengths to a common remote node, including dynamic selection of the message channel on one wavelength to carry control and management traffic for the entire wavelength bundle.')
ciscoOscpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 202, 1))
class CoscpSwitchId(TextualConvention, OctetString):
    description = 'A switch identifier - this is used to identify the originator and recipient of the OSCP hello packets. A valid switch identifier has a value different than all zeros. A switch identifier value of all zeros indicates that the switch identifier of a remote switch is not yet known.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class CoscpPortId(TextualConvention, Unsigned32):
    description = 'An OSCP port ID - this is used to identify a point of attachment of an optical wavelength to a given switch. The distinguished value 0 indicates that no port is specified. The terms link and wavelength are used interchangeably. Thus the Optical Supervisory Channel (OSC) is created on a given wavelength (link).'
    status = 'current'

class CoscpBundleId(TextualConvention, Unsigned32):
    description = 'An OSCP bundling identifier - this is used to determine which wavelengths to a given remote switch are to be aggregated and treated as a single logical link with a single control channel. This control channel is called the Optical Supervisory Channel (OSC). The scope of a bundle identifier value is limited to wavelengths between the same pair of switches. The same bundle identifier value may be used for wavelengths between other pairs of nodes without confusion.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class CoscpVersion(TextualConvention, Integer32):
    description = 'Indicates a version of OSCP.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unknown", 1), ("version1", 2))

ciscoOscpBaseGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1))
coscpHighestVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 1), CoscpVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpHighestVersion.setStatus('current')
if mibBuilder.loadTexts: coscpHighestVersion.setDescription('The highest version of OSCP that the software in this switch is capable of executing. If the version of a received hello packet is greater than coscpHighestVersion, the received hello packet will be discarded.')
coscpLowestVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 2), CoscpVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLowestVersion.setStatus('current')
if mibBuilder.loadTexts: coscpLowestVersion.setDescription('The lowest version of OSCP that the software in this switch is capable of executing. If the version of a received hello packet is smaller than coscpLowestVersion, the received hello packet will be discarded. The switch supports all OSCP versions between the lowest and the highest versions inclusive.')
coscpSwitchId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 3), CoscpSwitchId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpSwitchId.setStatus('current')
if mibBuilder.loadTexts: coscpSwitchId.setDescription('The value this switch is using to represent itself as a network node. This should be a globally unique identifier. Typically this value is a MAC address preconfigured in the switch hardware.')
coscpPriorityChangeMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("immediate", 1), ("delayed", 2))).clone('immediate')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpPriorityChangeMode.setStatus('current')
if mibBuilder.loadTexts: coscpPriorityChangeMode.setDescription("This value defines how OSCP will react to a change in the configured value of coscpLinkSelPriority. If the value is set to 'immediate', the reevaluation of the selected OSC in the bundle occurs immediately. If the value is set to 'delayed', then the OSC reevaluation can happen only when the current OSC goes out of the 'twoWay' state.")
coscpHelloHoldDown = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 10000)).clone(100)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpHelloHoldDown.setStatus('current')
if mibBuilder.loadTexts: coscpHelloHoldDown.setDescription("In OSCP, some hello packets are generated periodically while others are triggered by events. Specifically, event-triggered hellos are sent upon every state change (except 'oneWay' to 'twoWay') and when a change occurs in the bundle identifier. To avoid potential system misbehavior in which hello packets would be triggered in an uncontrolled fashion, a hello hold down timer is introduced that prevents successive event-triggered hellos from being sent in too short a time interval. This object contains the minimum time between (triggered) hellos. This value must be smaller than 75% of the value of coscpHelloInterval.")
coscpHelloInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(150, 30000)).clone(3000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpHelloInterval.setStatus('current')
if mibBuilder.loadTexts: coscpHelloInterval.setDescription('The average time interval between successive hellos sent by this switch on each link running OSCP, in the absence of triggered hellos.')
coscpHelloInactivityFactor = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 50)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpHelloInactivityFactor.setStatus('current')
if mibBuilder.loadTexts: coscpHelloInactivityFactor.setDescription("The value for the Hello Inactivity factor that this switch will use to determine when a link has gone down. A link will be returned to the 'attempt' state if the switch has not received an OSCP hello packet for an interval of time equal to coscpHelloInactivityFactor multiplied by the remote switch's advertised Hello Interval from the most recent received hello packet.")
coscpNotifiesEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpNotifiesEnabled.setStatus('current')
if mibBuilder.loadTexts: coscpNotifiesEnabled.setDescription("Notifications that OSCP has gone down on a link are enabled if this value is set to 'true'.")
coscpLinkTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2), )
if mibBuilder.loadTexts: coscpLinkTable.setStatus('current')
if mibBuilder.loadTexts: coscpLinkTable.setDescription('This table contains the objects necessary to describe the operation of OSCP over wavelengths that terminate at this switch. There is one entry for each wavelength that has a message channel for control and management purposes. The table is also used to configure the parameters used to control aggregation of multiple wavelengths that terminate at the same remote switch. Most of the information in this table is discovered by OSCP dynamically.')
coscpLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1), ).setIndexNames((0, "CISCO-OSCP-MIB", "coscpLinkPortId"))
if mibBuilder.loadTexts: coscpLinkEntry.setStatus('current')
if mibBuilder.loadTexts: coscpLinkEntry.setDescription('An entry in the table, containing information about a link attached to a switch running OSCP.')
coscpLinkPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 1), CoscpPortId())
if mibBuilder.loadTexts: coscpLinkPortId.setStatus('current')
if mibBuilder.loadTexts: coscpLinkPortId.setDescription('The Port Identifier of the link as selected by the local switch. This value has meaning only within the context of the switch to which the port is attached. This value is invariant across system restarts.')
coscpLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("dedicatedWavelength", 2), ("inBand", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkType.setStatus('current')
if mibBuilder.loadTexts: coscpLinkType.setDescription("This object indicates the type of link being described. A link type of 'dedicatedWavelength' represents a wavelength that is dedicated to carrying control and network management traffic, rather than user data. A dedicated wavelength should be terminated on the switch that physically connects to the fiber carrying that wavelength, i.e., the remote switch should be a physical neighbor. A link type of 'inBand' represents a message channel used to carry control and management traffic on a wavelength that otherwise carries user data. An 'inBand' link does not need to be terminated on the switch that physically connects to the fiber carrying that wavelength, i.e., the remote switch need not be a physical neighbor.")
coscpLinkVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 3), CoscpVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkVersion.setStatus('current')
if mibBuilder.loadTexts: coscpLinkVersion.setDescription("This object indicates the version of OSCP used to exchange information over this link. If communication with the remote switch has not yet been established, then the Version is set to 'unknown'.")
coscpLinkHelloState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("down", 1), ("attempt", 2), ("oneWay", 3), ("twoWay", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkHelloState.setStatus('current')
if mibBuilder.loadTexts: coscpLinkHelloState.setDescription("This object indicates the state of the Hello protocol exchange over this link. The 'down' state is the initial state of the OSCP Hello finite state machine. This state is also reached when lower-level protocols declare that the wavelength is not usable. No hello packets are sent or received in this state. The 'attempt' state indicates that either no hellos or hellos with mismatch information have recently been received from the remote switch. In this state, attempts are made to contact the remote switch by periodically sending hellos with period coscpHelloInterval. The 'oneWay' state indicates that Hellos have recently been received from the remote switch, but the remote switch identifier and the remote port identifier in the remote switch's hello packets were set to zero. This means that the remote switch does not know the identity of this switch. The 'twoWay' state indicates that hellos have recently been received from the remote switch including the correct remote switch identifier and remote port identifier fields. This means that bi-directional communication with the remote switch over the message channel on this wavelength has been achieved. The link is now capable of becoming the active OSC for a wavelength bundle. A link that is not in the 'twoWay' state is not capable of becoming the active OSC for a wavelength bundle.")
coscpLinkRemoteSwitchId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 5), CoscpSwitchId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkRemoteSwitchId.setStatus('current')
if mibBuilder.loadTexts: coscpLinkRemoteSwitchId.setDescription('This object indicates the switch identifier of the remote switch on the other end of the link.')
coscpLinkRemotePortId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 6), CoscpPortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkRemotePortId.setStatus('current')
if mibBuilder.loadTexts: coscpLinkRemotePortId.setDescription('This object indicates the port identifier of the port at the remote end of the link as assigned by the remote switch.')
coscpLinkDerivedBundleId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 7), CoscpBundleId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkDerivedBundleId.setStatus('current')
if mibBuilder.loadTexts: coscpLinkDerivedBundleId.setDescription('This object identifies the wavelength bundle to the remote switch that this link belongs to. All links with the same value of coscpLinkRemoteSwitchId and the same value of this object are aggregated and treated as a single logical link with a single control channel. The aggregated logical link that contains this link is shown in coscpBundleTable as the coscpBundleEntry with coscpBundleRemoteSwitchId value equal to the value of coscpLinkRemoteSwitchId and with coscpBundleId value equal to the value of this object. The value of this object is derived from the bundle identifier advertised by this switch in the OSCP (specified in coscpLinkConfigBundleId) and the bundle identifier advertised by the remote switch. The two switches on either end of the link run the same algorithm on the same information to determine common values of the derived bundle identifier. The derivation process is intended for minimal configuration as well as acceptable behavior in the face of misconfiguration. By default all links have the coscpLinkConfigBundleId value zero. Since all links have the same default value, the default behavior is to aggregate all links between two switches into a single logical link with derived bundle identifier value zero. In order to assign a non-default bundle identifier to a link between two switches, only one side needs to be configured with the non-default value. The coscpLinkConfigBundleId value zero indicates that the switch will use as the derived bundle identifier value whatever value the remote switch has. The algorithm for computing the value of the derived bundle identifier is: 1. If the two switches exchange identical values of the configured bundle identifier, that value becomes the derived bundle identifier. 2. If the configured bundle identifier value of one of the switches is zero and that of the other switch is non-zero, the non-zero value becomes the derived bundle identifier value. 3. If the configured bundle identifier values of the two switches are different and both non-zero, the link has been misconfigured and the derived bundle identifier value becomes zero.')
coscpLinkConfigBundleId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 8), CoscpBundleId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpLinkConfigBundleId.setStatus('current')
if mibBuilder.loadTexts: coscpLinkConfigBundleId.setDescription('This object specifies the identifier of the wavelength bundle to the remote switch configured for this link. The configured bundle identifier is carried in the OSCP hello packet. At both this switch and the remote switch, the configured bundle identifier is used to derive coscpLinkDerivedBundleId according to the algorithm presented in the description of the coscpLinkDerivedBundleId. By default all links have the value zero. Since all links have the same default value, the default behavior is to aggregate all links between two switches into a single logical link with derived bundle identifier value zero. In order to assign a non-default bundle identifier to a link between two switches, only one side needs to be configured with the non-default value. The distinguished value zero indicates that the switch will use as the derived bundle identifier value whatever value the remote switch has.')
coscpLinkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 9), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkIfIndex.setStatus('current')
if mibBuilder.loadTexts: coscpLinkIfIndex.setDescription('The interface index identifying this link.')
coscpLinkSelPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coscpLinkSelPriority.setStatus('current')
if mibBuilder.loadTexts: coscpLinkSelPriority.setDescription("This object indicates the priority with which this link gets selected as the active Optical Supervisory Channel (OSC) when multiple links are present in the same wavelength bundle. If selected, this link will be used to transmit all control and network management traffic to the remote switch, for the entire wavelength bundle. The link with the highest value of the selection priority is chosen by this switch to be the active OSC. Only links in the wavelength bundle that have coscpLinkHelloState value 'twoWay' are considered. If there is more than one link with the same highest value of the selection priority, the choice between these links is arbitrary. If it is desired to have one OSC link candidate be picked over another, its priority should be configured to a higher value than other candidate links. The OSCP will react to a reconfiguration of the selection priority according to the rules defined for the configured variable coscpPriorityChangeMode.")
coscpLinkInHellos = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkInHellos.setStatus('current')
if mibBuilder.loadTexts: coscpLinkInHellos.setDescription('This object contains a count of the number of Hello packets received over this link.')
coscpLinkInDiscardedHellos = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkInDiscardedHellos.setStatus('current')
if mibBuilder.loadTexts: coscpLinkInDiscardedHellos.setDescription('This object contains a count of the number of Hello packets received over this link that were discarded since the version of the received Hello packet was outside the range of coscpLowestVersion to coscpHighestVersion.')
coscpLinkOutHellos = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkOutHellos.setStatus('current')
if mibBuilder.loadTexts: coscpLinkOutHellos.setDescription('This object contains a count of the number of Hello packets transmitted over this link.')
coscpLinkTransDown = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpLinkTransDown.setStatus('current')
if mibBuilder.loadTexts: coscpLinkTransDown.setDescription("This object contains a count of the number of times this link transitioned from the 'twoWay' state to a hello state other than 'twoWay'.")
coscpBundleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3), )
if mibBuilder.loadTexts: coscpBundleTable.setStatus('current')
if mibBuilder.loadTexts: coscpBundleTable.setDescription('This table contains objects describing the wavelength bundles on this switch.')
coscpBundleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1), ).setIndexNames((0, "CISCO-OSCP-MIB", "coscpBundleRemoteSwitchId"), (0, "CISCO-OSCP-MIB", "coscpBundleId"))
if mibBuilder.loadTexts: coscpBundleEntry.setStatus('current')
if mibBuilder.loadTexts: coscpBundleEntry.setDescription("Each entry contains information about one wavelength bundle to one remote switch. The wavelength bundle is modeled as a single logical link (identified by coscpBundleIfIndex) with a single control and management channel. This logical link is known as the Optical Supervisory Channel (OSC). At any one time, only one wavelength in the bundle is selected to transmit the OSC control and network management traffic. This link is identified by coscpBundleActivePortId. The wavelength bundle must be created by a manager using the coscpBundleRowStatus object. Once the row has been activated, an interface index is assigned by the agent and shown in coscpBundleIfIndex. This value can then be used by the manager to configure control and management protocols, e.g. to configure the OSC's IP address. Aside from coscpBundleRowStatus, the other objects in the row are read-only, since they reflect the dynamic state of the wavelength bundle as determined by OSCP. The wavelength bundle does not become operational until at least one component link reaches the hello state 'twoWay', i.e., until at least one entry in coscpLinkTable with coscpLinkRemoteSwitchId value equal to the value of coscpBundleRemoteSwitchId and coscpLinkDerivedBundleId value equal to the value of coscpBundleId has coscpLinkHelloState value 'twoWay'. The operational status of the wavelength bundle is indicated by the value of ifOperStatus in the ifEntry with ifIndex value equal to the value of coscpBundleIfIndex.")
coscpBundleRemoteSwitchId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 1), CoscpSwitchId())
if mibBuilder.loadTexts: coscpBundleRemoteSwitchId.setStatus('current')
if mibBuilder.loadTexts: coscpBundleRemoteSwitchId.setDescription('The switch identifier of the remote switch.')
coscpBundleId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 2), CoscpBundleId())
if mibBuilder.loadTexts: coscpBundleId.setStatus('current')
if mibBuilder.loadTexts: coscpBundleId.setDescription('The bundle identifier value used to distinguish this wavelength bundle from other wavelength bundles to the same remote switch. All entries in coscpLinkTable with the value of coscpLinkRemoteSwitchId equal to the value of coscpBundleRemoteSwitchId and with the value of coscpLinkDerivedBundleId equal to the value of this object identify links that are present in this wavelength bundle.')
coscpBundleActivePortId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 3), CoscpPortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpBundleActivePortId.setStatus('current')
if mibBuilder.loadTexts: coscpBundleActivePortId.setDescription('The port identifier of the link currently selected as the active OSC. This link is used to transmit all OSC control and network management traffic to the remote switch, for the entire wavelength bundle.')
coscpBundleIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpBundleIfIndex.setStatus('current')
if mibBuilder.loadTexts: coscpBundleIfIndex.setDescription('The interface index assigned by the agent to represent the OSC for the wavelength bundle.')
coscpBundlePortCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coscpBundlePortCount.setStatus('current')
if mibBuilder.loadTexts: coscpBundlePortCount.setDescription("A count of the total number of component links in the wavelength bundle that have coscpLinkHelloState value 'twoWay'.")
coscpBundleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 202, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: coscpBundleRowStatus.setStatus('current')
if mibBuilder.loadTexts: coscpBundleRowStatus.setDescription("This object is used to create a new row or to modify or delete an existing row in this table. Each row in the table must be created using this object. Once the row has been activated, an interface index is assigned by the agent and shown in coscpBundleIfIndex. This value can then be used by the manager to configure control and management protocols, e.g. to configure the OSC's IP address. After the row has been activated, this object cannot be set to any value other than 'destroy'. The row status never changes to 'notInService' after reaching the value 'active'.")
ciscoOscpMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 202, 2))
ciscoOscpNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 202, 2, 0))
coscpNotifyTransDown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 202, 2, 0, 1)).setObjects(("CISCO-OSCP-MIB", "coscpLinkTransDown"))
if mibBuilder.loadTexts: coscpNotifyTransDown.setStatus('current')
if mibBuilder.loadTexts: coscpNotifyTransDown.setDescription("A coscpNotifyTransDown notification is sent when the value of an instance of coscpTransDown increments. This indicates that a link exited the 'twoWay' state and cannot be used to carry control and management traffic for an optical supervisory channel.")
ciscoOscpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 202, 3))
ciscoOscpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 1))
ciscoOscpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 2))
ciscoOscpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 1, 1)).setObjects(("CISCO-OSCP-MIB", "ciscoOscpBasicGroup"), ("CISCO-OSCP-MIB", "ciscoOscpNotificationsGroup"), ("CISCO-OSCP-MIB", "ciscoOscpBundleGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOscpMIBCompliance = ciscoOscpMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoOscpMIBCompliance.setDescription('The compliance statement for entities which implement the Cisco OSCP MIB.')
ciscoOscpBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 2, 1)).setObjects(("CISCO-OSCP-MIB", "coscpHighestVersion"), ("CISCO-OSCP-MIB", "coscpLowestVersion"), ("CISCO-OSCP-MIB", "coscpSwitchId"), ("CISCO-OSCP-MIB", "coscpHelloHoldDown"), ("CISCO-OSCP-MIB", "coscpHelloInterval"), ("CISCO-OSCP-MIB", "coscpHelloInactivityFactor"), ("CISCO-OSCP-MIB", "coscpNotifiesEnabled"), ("CISCO-OSCP-MIB", "coscpLinkType"), ("CISCO-OSCP-MIB", "coscpLinkVersion"), ("CISCO-OSCP-MIB", "coscpLinkHelloState"), ("CISCO-OSCP-MIB", "coscpLinkRemoteSwitchId"), ("CISCO-OSCP-MIB", "coscpLinkRemotePortId"), ("CISCO-OSCP-MIB", "coscpLinkIfIndex"), ("CISCO-OSCP-MIB", "coscpLinkInHellos"), ("CISCO-OSCP-MIB", "coscpLinkInDiscardedHellos"), ("CISCO-OSCP-MIB", "coscpLinkOutHellos"), ("CISCO-OSCP-MIB", "coscpLinkTransDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOscpBasicGroup = ciscoOscpBasicGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoOscpBasicGroup.setDescription('A collection of cisco specific MIB objects used for management of OSCP.')
ciscoOscpBundleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 2, 2)).setObjects(("CISCO-OSCP-MIB", "coscpPriorityChangeMode"), ("CISCO-OSCP-MIB", "coscpLinkDerivedBundleId"), ("CISCO-OSCP-MIB", "coscpLinkConfigBundleId"), ("CISCO-OSCP-MIB", "coscpLinkSelPriority"), ("CISCO-OSCP-MIB", "coscpBundleActivePortId"), ("CISCO-OSCP-MIB", "coscpBundleIfIndex"), ("CISCO-OSCP-MIB", "coscpBundlePortCount"), ("CISCO-OSCP-MIB", "coscpBundleRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOscpBundleGroup = ciscoOscpBundleGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoOscpBundleGroup.setDescription('A collection of cisco specific MIB objects used for management of wavelength bundles to a common remote node that are controlled by OSCP.')
ciscoOscpNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 202, 3, 2, 3)).setObjects(("CISCO-OSCP-MIB", "coscpNotifyTransDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOscpNotificationsGroup = ciscoOscpNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoOscpNotificationsGroup.setDescription('A collection of cisco specific notifications used for management of OSCP.')
mibBuilder.exportSymbols("CISCO-OSCP-MIB", PYSNMP_MODULE_ID=ciscoOscpMIB, coscpNotifyTransDown=coscpNotifyTransDown, coscpHelloInactivityFactor=coscpHelloInactivityFactor, coscpLinkInHellos=coscpLinkInHellos, coscpBundleTable=coscpBundleTable, ciscoOscpBundleGroup=ciscoOscpBundleGroup, CoscpPortId=CoscpPortId, CoscpBundleId=CoscpBundleId, coscpLinkTransDown=coscpLinkTransDown, ciscoOscpMIB=ciscoOscpMIB, coscpLinkType=coscpLinkType, ciscoOscpNotificationsGroup=ciscoOscpNotificationsGroup, coscpLinkPortId=coscpLinkPortId, coscpLinkConfigBundleId=coscpLinkConfigBundleId, coscpLinkTable=coscpLinkTable, coscpLinkDerivedBundleId=coscpLinkDerivedBundleId, ciscoOscpMIBCompliances=ciscoOscpMIBCompliances, coscpHelloInterval=coscpHelloInterval, ciscoOscpMIBGroups=ciscoOscpMIBGroups, ciscoOscpBasicGroup=ciscoOscpBasicGroup, coscpLowestVersion=coscpLowestVersion, coscpBundleIfIndex=coscpBundleIfIndex, coscpHelloHoldDown=coscpHelloHoldDown, ciscoOscpMIBConformance=ciscoOscpMIBConformance, coscpBundlePortCount=coscpBundlePortCount, ciscoOscpBaseGroup=ciscoOscpBaseGroup, coscpHighestVersion=coscpHighestVersion, coscpSwitchId=coscpSwitchId, CoscpVersion=CoscpVersion, coscpLinkEntry=coscpLinkEntry, ciscoOscpNotificationsPrefix=ciscoOscpNotificationsPrefix, ciscoOscpMIBCompliance=ciscoOscpMIBCompliance, coscpLinkRemoteSwitchId=coscpLinkRemoteSwitchId, coscpLinkHelloState=coscpLinkHelloState, ciscoOscpMIBObjects=ciscoOscpMIBObjects, ciscoOscpMIBNotifications=ciscoOscpMIBNotifications, coscpBundleEntry=coscpBundleEntry, coscpLinkInDiscardedHellos=coscpLinkInDiscardedHellos, coscpNotifiesEnabled=coscpNotifiesEnabled, coscpPriorityChangeMode=coscpPriorityChangeMode, coscpLinkRemotePortId=coscpLinkRemotePortId, coscpBundleRowStatus=coscpBundleRowStatus, coscpBundleRemoteSwitchId=coscpBundleRemoteSwitchId, coscpLinkIfIndex=coscpLinkIfIndex, CoscpSwitchId=CoscpSwitchId, coscpLinkOutHellos=coscpLinkOutHellos, coscpLinkSelPriority=coscpLinkSelPriority, coscpBundleId=coscpBundleId, coscpBundleActivePortId=coscpBundleActivePortId, coscpLinkVersion=coscpLinkVersion)