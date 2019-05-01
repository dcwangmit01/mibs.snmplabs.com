#
# PySNMP MIB module NOKIA-IPSO-LBCLUSTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIA-IPSO-LBCLUSTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:23:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ipsoProducts, = mibBuilder.importSymbols("NOKIA-IPSO-REGISTRATION-MIB", "ipsoProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, TimeTicks, Bits, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, Gauge32, ModuleIdentity, Unsigned32, iso, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "Bits", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "Gauge32", "ModuleIdentity", "Unsigned32", "iso", "Counter64", "IpAddress")
MacAddress, TextualConvention, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString", "TimeStamp")
ipsoLBClusterMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 94, 1, 21, 5))
ipsoLBClusterMIB.setRevisions(('1901-05-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ipsoLBClusterMIB.setRevisionsDescriptions(('Initial Version of the MIB -- Kripa Karlekar',))
if mibBuilder.loadTexts: ipsoLBClusterMIB.setLastUpdated('0105140000Z')
if mibBuilder.loadTexts: ipsoLBClusterMIB.setOrganization('Nokia IPRG')
if mibBuilder.loadTexts: ipsoLBClusterMIB.setContactInfo(' Nokia IPRG Customer Service')
if mibBuilder.loadTexts: ipsoLBClusterMIB.setDescription('The MIB Module for the management of Load Balancing IPSO systems. A load balancing IPSO cluster comprises a number of nodes with a single master node and multiple member nodes. A master or member can be a part of single cluster or multiple clusters. The master is responsible for calculating the worksets and assigning it to all the members and to itself. The information provided by this MIB implementation will vary depending on if this node is a master or member.')
ipsoLBClusterInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1))
ipsoLBClusterNodeSpecificInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2))
ipsoLBClusterNotificationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3))
ipsoLBNumClusters = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsoLBNumClusters.setStatus('current')
if mibBuilder.loadTexts: ipsoLBNumClusters.setDescription('Number of clusters in which this node is either a master or a member')
ipsoLBClusterInfoTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2), ).setIndexNames((0, "NOKIA-IPSO-LBCLUSTER-MIB", "ClusterIndex"))
if mibBuilder.loadTexts: ipsoLBClusterInfoTable.setStatus('current')
if mibBuilder.loadTexts: ipsoLBClusterInfoTable.setDescription('This table contains a row for each cluster to which this system belongs.')
ipsoLBClusterInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1), )
if mibBuilder.loadTexts: ipsoLBClusterInfoEntry.setStatus('current')
if mibBuilder.loadTexts: ipsoLBClusterInfoEntry.setDescription('An entry containing cluster management information for each cluster this system belongs.')
clusterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterIndex.setStatus('current')
if mibBuilder.loadTexts: clusterIndex.setDescription('The Cluster Index')
clusterID = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterID.setStatus('current')
if mibBuilder.loadTexts: clusterID.setDescription('The Identity for the cluster')
clusterNumMembers = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterNumMembers.setStatus('current')
if mibBuilder.loadTexts: clusterNumMembers.setDescription('Number of members for this cluster')
clusterNumInterfaces = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterNumInterfaces.setStatus('current')
if mibBuilder.loadTexts: clusterNumInterfaces.setDescription('Number of interfaces participating in this cluster')
clusterUpTimeAtJoin = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterUpTimeAtJoin.setStatus('current')
if mibBuilder.loadTexts: clusterUpTimeAtJoin.setDescription('Time since the cluster started when this member joined the cluster')
systemUpTimeAtJoin = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpTimeAtJoin.setStatus('current')
if mibBuilder.loadTexts: systemUpTimeAtJoin.setDescription('The system up time when this member joined the cluster')
clusterTotalBuckets = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterTotalBuckets.setStatus('current')
if mibBuilder.loadTexts: clusterTotalBuckets.setDescription('Overall number of buckets that will be distributed among cluster members for this cluster')
clusterBucketsAssigned = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterBucketsAssigned.setStatus('current')
if mibBuilder.loadTexts: clusterBucketsAssigned.setDescription('Total number of buckets assigned to each individual cluster members on this cluster')
ipsoLBClusterAddressTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 3), ).setIndexNames((0, "NOKIA-IPSO-LBCLUSTER-MIB", "ClusterIndex"), (0, "NOKIA-IPSO-LBCLUSTER-MIB", "ClusterAddress"))
if mibBuilder.loadTexts: ipsoLBClusterAddressTable.setStatus('current')
if mibBuilder.loadTexts: ipsoLBClusterAddressTable.setDescription('This table contains a row for each cluster to which this system belongs. This table provides cluster interface address for this cluster.')
ipsoLBClusterAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 3, 1), )
if mibBuilder.loadTexts: ipsoLBClusterAddressEntry.setStatus('current')
if mibBuilder.loadTexts: ipsoLBClusterAddressEntry.setDescription('An entry containing cluster interface address information of each cluster this node is participating.')
clusterIndex2 = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterIndex2.setStatus('current')
if mibBuilder.loadTexts: clusterIndex2.setDescription('The cluster index')
clusterAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterAddress.setStatus('current')
if mibBuilder.loadTexts: clusterAddress.setDescription('The cluster interface address')
clusterMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 3, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterMACAddress.setStatus('current')
if mibBuilder.loadTexts: clusterMACAddress.setDescription('The cluster MAC Address')
ipsoLBClusterMemberTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 4), ).setIndexNames((0, "NOKIA-IPSO-LBCLUSTER-MIB", "ClusterIndex"), (0, "NOKIA-IPSO-LBCLUSTER-MIB", "MemberID"))
if mibBuilder.loadTexts: ipsoLBClusterMemberTable.setStatus('current')
if mibBuilder.loadTexts: ipsoLBClusterMemberTable.setDescription('This table has information about all the members in each cluster this node participates. The information in this table varies depending on if this mode is a member or master in each cluster. If this node is a master in a cluster it furnishes more information')
ipsoLBClusterMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 4, 1), )
if mibBuilder.loadTexts: ipsoLBClusterMemberEntry.setStatus('current')
if mibBuilder.loadTexts: ipsoLBClusterMemberEntry.setDescription('An entry containing member information.')
clusterIndex3 = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterIndex3.setStatus('current')
if mibBuilder.loadTexts: clusterIndex3.setDescription('The index of the cluster')
memberID = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memberID.setStatus('current')
if mibBuilder.loadTexts: memberID.setDescription('The member id in the cluster')
memberPercentageBucketsAssigned = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memberPercentageBucketsAssigned.setStatus('current')
if mibBuilder.loadTexts: memberPercentageBucketsAssigned.setDescription('A percentage of how many buckets this member is processing for each cluster')
memberRating = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 4, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memberRating.setStatus('current')
if mibBuilder.loadTexts: memberRating.setDescription('The Rating of this member for this cluster, only available on Master.')
memberPrimaryAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 4, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memberPrimaryAddress.setStatus('current')
if mibBuilder.loadTexts: memberPrimaryAddress.setDescription("Members's primary interface address")
ipsoLBClusterNodeSpecificTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1), ).setIndexNames((0, "NOKIA-IPSO-LBCLUSTER-MIB", "ClusterIndex"))
if mibBuilder.loadTexts: ipsoLBClusterNodeSpecificTable.setStatus('current')
if mibBuilder.loadTexts: ipsoLBClusterNodeSpecificTable.setDescription('This table contains a row for each cluster to which this system belongs. This table provides specific cluster related information about this node')
ipsoLBClusterNodeSpecificEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1, 1), )
if mibBuilder.loadTexts: ipsoLBClusterNodeSpecificEntry.setStatus('current')
if mibBuilder.loadTexts: ipsoLBClusterNodeSpecificEntry.setDescription('An entry containing management information for this node in each cluster.')
clusterIndex4 = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterIndex4.setStatus('current')
if mibBuilder.loadTexts: clusterIndex4.setDescription('The cluster index for which this node is a member')
memberID2 = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memberID2.setStatus('current')
if mibBuilder.loadTexts: memberID2.setDescription("This member's id in the cluster")
percentageBucketsAssigned = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: percentageBucketsAssigned.setStatus('current')
if mibBuilder.loadTexts: percentageBucketsAssigned.setDescription('Percentage of buckets assigned to this member in this cluster')
memberMode = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("uninitialized", 1), ("initialized", 2), ("joining", 3), ("becomingmaster", 4), ("master", 5), ("member", 6), ("unknown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: memberMode.setStatus('current')
if mibBuilder.loadTexts: memberMode.setDescription("The member's mode in this cluster")
memberRating2 = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memberRating2.setStatus('current')
if mibBuilder.loadTexts: memberRating2.setDescription("Member's rating in this cluster")
memberPrimaryAddress2 = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memberPrimaryAddress2.setStatus('current')
if mibBuilder.loadTexts: memberPrimaryAddress2.setDescription("Members's primary interface address")
ipsoLBClusterNodeSpecificInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2), ).setIndexNames((0, "NOKIA-IPSO-LBCLUSTER-MIB", "ClusterIndex"), (0, "NOKIA-IPSO-LBCLUSTER-MIB", "ifIndex"))
if mibBuilder.loadTexts: ipsoLBClusterNodeSpecificInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: ipsoLBClusterNodeSpecificInterfaceTable.setDescription('This table contains information about each interface that participates in the cluster. The interfaces in this node can be a part of multiple cluster in which case there will be a row for each interface in each cluster.')
ipsoLBClusterNodeSpecificInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1), )
if mibBuilder.loadTexts: ipsoLBClusterNodeSpecificInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: ipsoLBClusterNodeSpecificInterfaceEntry.setDescription('An entry containing management information for each interface in this member for each cluster.')
clusterIndex5 = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterIndex5.setStatus('current')
if mibBuilder.loadTexts: clusterIndex5.setDescription('The cluster index for which this node is a member')
memberID3 = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memberID3.setStatus('current')
if mibBuilder.loadTexts: memberID3.setDescription("This member's ID")
ifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifIndex.setStatus('current')
if mibBuilder.loadTexts: ifIndex.setDescription('The interface index in the interface table')
clusterIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterIPAddress.setStatus('current')
if mibBuilder.loadTexts: clusterIPAddress.setDescription("Cluster's IP address for this interface")
clusterNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterNetMask.setStatus('current')
if mibBuilder.loadTexts: clusterNetMask.setDescription('Cluster Netmask ')
clusterBroadcastAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterBroadcastAddress.setStatus('current')
if mibBuilder.loadTexts: clusterBroadcastAddress.setDescription('The Broadcast address')
realIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: realIPAddress.setStatus('current')
if mibBuilder.loadTexts: realIPAddress.setDescription('The real IP Address of the interface, if there are multiple IP address then this will the first IP address configured')
masterIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: masterIPAddress.setStatus('current')
if mibBuilder.loadTexts: masterIPAddress.setDescription("Master's IP address assosiated with this interface")
ipsoLBMemberJoinRejectReason = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 0), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fewinterface", 1), ("illegallicence", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ipsoLBMemberJoinRejectReason.setStatus('current')
if mibBuilder.loadTexts: ipsoLBMemberJoinRejectReason.setDescription('Reason why a node was rejected from joining a cluster.')
ipsoLBClusterNewMasterReason = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("oldMasterHelloTimeout", 1), ("iamBetterMaster", 2), ("initalizedAsMaster", 3), ("unknown", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ipsoLBClusterNewMasterReason.setStatus('current')
if mibBuilder.loadTexts: ipsoLBClusterNewMasterReason.setDescription('Potential reason why this node became a master.')
ipsoLBClusterMemberJoin = NotificationType((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 2)).setObjects(("NOKIA-IPSO-LBCLUSTER-MIB", "clusterID"), ("NOKIA-IPSO-LBCLUSTER-MIB", "memberID"), ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberIPAddress"))
if mibBuilder.loadTexts: ipsoLBClusterMemberJoin.setStatus('current')
if mibBuilder.loadTexts: ipsoLBClusterMemberJoin.setDescription('This trap is sent when a member node joins the cluster by the master')
ipsoLBClusterMemberLeft = NotificationType((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 3)).setObjects(("NOKIA-IPSO-LBCLUSTER-MIB", "clusterID"), ("NOKIA-IPSO-LBCLUSTER-MIB", "memberID"), ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberIPAddress"))
if mibBuilder.loadTexts: ipsoLBClusterMemberLeft.setStatus('current')
if mibBuilder.loadTexts: ipsoLBClusterMemberLeft.setDescription('This trap is sent when a member node leaves the cluster by the master.')
ipsoLBClusterNewMaster = NotificationType((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 4)).setObjects(("NOKIA-IPSO-LBCLUSTER-MIB", "clusterID"), ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoLBClusterNewMasterReason"))
if mibBuilder.loadTexts: ipsoLBClusterNewMaster.setStatus('current')
if mibBuilder.loadTexts: ipsoLBClusterNewMaster.setDescription('This trap is sent when a cluster is formed and a new master is elected.')
ipsoLBJoinReject = NotificationType((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 5)).setObjects(("NOKIA-IPSO-LBCLUSTER-MIB", "clusterID"), ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberIPAddress"), ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberRejectErcode"), ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberRejectWrongIntf"), ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberRejectprimaryintf"), ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberRejectCip"), ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberRejectHash"))
if mibBuilder.loadTexts: ipsoLBJoinReject.setStatus('current')
if mibBuilder.loadTexts: ipsoLBJoinReject.setDescription("This trap is sent when a member's request to join the cluster is rejected")
ipsoMemberRejectErcode = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(55, 22, 65, 61, 6))).clone(namedValues=NamedValues(("internalerroronmaster", 55), ("numberofmembersclustercansupportexceeded", 22), ("nodeunreachableononeoftheselectedinterfaces", 65), ("protocolversionmismatch", 61), ("configurationmismatch", 6)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ipsoMemberRejectErcode.setStatus('current')
if mibBuilder.loadTexts: ipsoMemberRejectErcode.setDescription('Potential reason why this node is rejected.')
ipsoMemberRejectWrongIntf = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 7), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ipsoMemberRejectWrongIntf.setStatus('current')
if mibBuilder.loadTexts: ipsoMemberRejectWrongIntf.setDescription('Wrong number of Interfaces Selected.')
ipsoMemberRejectprimaryintf = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 8), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ipsoMemberRejectprimaryintf.setStatus('current')
if mibBuilder.loadTexts: ipsoMemberRejectprimaryintf.setDescription("Primary addresses didn't match.")
ipsoMemberRejectCip = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 9), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ipsoMemberRejectCip.setStatus('current')
if mibBuilder.loadTexts: ipsoMemberRejectCip.setDescription("Cluster IP address didn't match on one or more interfaces.")
ipsoMemberRejectHash = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 10), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ipsoMemberRejectHash.setStatus('current')
if mibBuilder.loadTexts: ipsoMemberRejectHash.setDescription('Hash Configuration did not match on one or more interfaces.')
ipsoMemberIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 11), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ipsoMemberIPAddress.setStatus('current')
if mibBuilder.loadTexts: ipsoMemberIPAddress.setDescription('IP address of a member.')
mibBuilder.exportSymbols("NOKIA-IPSO-LBCLUSTER-MIB", clusterNumMembers=clusterNumMembers, systemUpTimeAtJoin=systemUpTimeAtJoin, clusterUpTimeAtJoin=clusterUpTimeAtJoin, ipsoLBClusterNodeSpecificInterfaceEntry=ipsoLBClusterNodeSpecificInterfaceEntry, masterIPAddress=masterIPAddress, clusterIndex4=clusterIndex4, memberID=memberID, ipsoMemberRejectErcode=ipsoMemberRejectErcode, clusterID=clusterID, PYSNMP_MODULE_ID=ipsoLBClusterMIB, ipsoLBMemberJoinRejectReason=ipsoLBMemberJoinRejectReason, ipsoLBJoinReject=ipsoLBJoinReject, ipsoLBClusterAddressEntry=ipsoLBClusterAddressEntry, realIPAddress=realIPAddress, ipsoLBClusterMemberLeft=ipsoLBClusterMemberLeft, ipsoMemberRejectHash=ipsoMemberRejectHash, ipsoLBClusterInfo=ipsoLBClusterInfo, memberID2=memberID2, clusterIndex2=clusterIndex2, clusterAddress=clusterAddress, percentageBucketsAssigned=percentageBucketsAssigned, clusterTotalBuckets=clusterTotalBuckets, clusterMACAddress=clusterMACAddress, clusterNumInterfaces=clusterNumInterfaces, clusterIndex3=clusterIndex3, ipsoMemberRejectWrongIntf=ipsoMemberRejectWrongIntf, memberID3=memberID3, ipsoLBClusterMemberEntry=ipsoLBClusterMemberEntry, ipsoLBClusterNewMasterReason=ipsoLBClusterNewMasterReason, memberPrimaryAddress2=memberPrimaryAddress2, ipsoLBClusterNodeSpecificInterfaceTable=ipsoLBClusterNodeSpecificInterfaceTable, clusterBucketsAssigned=clusterBucketsAssigned, clusterNetMask=clusterNetMask, clusterIPAddress=clusterIPAddress, ipsoLBClusterInfoEntry=ipsoLBClusterInfoEntry, ipsoMemberRejectprimaryintf=ipsoMemberRejectprimaryintf, ipsoLBClusterNewMaster=ipsoLBClusterNewMaster, ipsoLBClusterInfoTable=ipsoLBClusterInfoTable, ipsoLBClusterNodeSpecificTable=ipsoLBClusterNodeSpecificTable, ipsoMemberIPAddress=ipsoMemberIPAddress, memberMode=memberMode, ipsoLBClusterMemberJoin=ipsoLBClusterMemberJoin, ipsoLBClusterAddressTable=ipsoLBClusterAddressTable, ipsoLBClusterNotificationGroup=ipsoLBClusterNotificationGroup, ipsoLBClusterMIB=ipsoLBClusterMIB, memberPercentageBucketsAssigned=memberPercentageBucketsAssigned, clusterIndex5=clusterIndex5, clusterIndex=clusterIndex, ipsoLBClusterNodeSpecificInfo=ipsoLBClusterNodeSpecificInfo, memberRating=memberRating, memberRating2=memberRating2, ipsoMemberRejectCip=ipsoMemberRejectCip, ipsoLBClusterMemberTable=ipsoLBClusterMemberTable, clusterBroadcastAddress=clusterBroadcastAddress, ipsoLBNumClusters=ipsoLBNumClusters, memberPrimaryAddress=memberPrimaryAddress, ipsoLBClusterNodeSpecificEntry=ipsoLBClusterNodeSpecificEntry, ifIndex=ifIndex)