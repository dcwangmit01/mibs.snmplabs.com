#
# PySNMP MIB module ARISTA-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-QOS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:25:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
PhysicalIndexOrZero, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndexOrZero")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Integer32, MibIdentifier, Bits, Counter32, Counter64, NotificationType, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Integer32", "MibIdentifier", "Bits", "Counter32", "Counter64", "NotificationType", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aristaQosMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 13))
aristaQosMib.setRevisions(('2016-07-22 00:00', '2016-03-21 00:00', '2014-08-15 00:00', '2014-05-22 00:00', '2013-06-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aristaQosMib.setRevisionsDescriptions(('Added aristaEcnCounterTable', 'Added vlan to aristaClassMapMatchType', 'Updated postal address.', 'Updated the upper limit for aristaPolicyMapClassIndex.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: aristaQosMib.setLastUpdated('201607220000Z')
if mibBuilder.loadTexts: aristaQosMib.setOrganization('Arista Networks, Inc.')
if mibBuilder.loadTexts: aristaQosMib.setContactInfo('Arista Networks, Inc. Postal: 5453 Great America Parkway Santa Clara, CA 95054 Tel: +1 408 547-5500 E-mail: snmp@arista.com')
if mibBuilder.loadTexts: aristaQosMib.setDescription('********************************** Overview ********************************** This MIB provides read access to Quality of Service (QoS) configuration and statistics information for Arista platforms. Configuration information available through this MIB includes all class-map, policy-map, and service-policy parameters. The definitions of these object types are given below. Statistics available through this MIB include dropped, sent and matched packet counters per traffic class after any configured QoS policies are applied and per chip ECN counters if supported. ********************************** Definitions ********************************** Class map - A data structure that uses access-control lists to define a data stream. Policy map - A data structure that associates class maps identifying specific data streams with actions that control its transmission. Action - A traffic-management action that is applied to traffic classified as belonging to a particular class. Actions may include modifying CoS or DSCP fields, assigning to traffic-class queues, shaping, or filtering.')
class AristaQosMapType(TextualConvention, Integer32):
    description = 'The type of a class or policy map. controlPlane - The map is applicable only on the control plane of the device. dataPlane - The map is applicable only on the data plane of the device.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("controlPlane", 1), ("dataPlane", 2))

class AristaQosShortId(TextualConvention, OctetString):
    description = "Identifier with bounded length, derived from a name that may be longer. It includes the first 30 characters of the name. If the name is longer than 30 characters, the identifier contains a hash of the remaining characters in the name, expressed as decimal digits. For example: - name 'one-two-three': identifier 'one-two-three' - name 'one-two-three-four-five-six-seven': identifier 'one-two-three-four-five-six-se3877954092'"
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 40)

aristaQosMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1))
aristaQosMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 13, 2))
aristaClassMapTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 1), )
if mibBuilder.loadTexts: aristaClassMapTable.setStatus('current')
if mibBuilder.loadTexts: aristaClassMapTable.setDescription('Lists the class maps configured on the system.')
aristaClassMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 1, 1), ).setIndexNames((0, "ARISTA-QOS-MIB", "aristaClassMapId"), (0, "ARISTA-QOS-MIB", "aristaClassMapType"))
if mibBuilder.loadTexts: aristaClassMapEntry.setStatus('current')
if mibBuilder.loadTexts: aristaClassMapEntry.setDescription('A conceptual row in aristaClassMapTable.')
aristaClassMapId = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 1, 1, 1), AristaQosShortId())
if mibBuilder.loadTexts: aristaClassMapId.setStatus('current')
if mibBuilder.loadTexts: aristaClassMapId.setDescription("Bounded-length identifier for a given class map, derived from the class map's name.")
aristaClassMapType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 1, 1, 2), AristaQosMapType())
if mibBuilder.loadTexts: aristaClassMapType.setStatus('current')
if mibBuilder.loadTexts: aristaClassMapType.setDescription('Type of a given class map.')
aristaClassMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaClassMapName.setStatus('current')
if mibBuilder.loadTexts: aristaClassMapName.setDescription('Name of a given class map.')
aristaClassMapMatchCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("matchConditionAny", 1), ("matchConditionAll", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaClassMapMatchCondition.setStatus('current')
if mibBuilder.loadTexts: aristaClassMapMatchCondition.setDescription('Indicates how many match criteria traffic must match in order to belong to a class with multiple match critera.')
aristaClassMapMatchTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 2), )
if mibBuilder.loadTexts: aristaClassMapMatchTable.setStatus('current')
if mibBuilder.loadTexts: aristaClassMapMatchTable.setDescription('Describes the match criteria used to classify traffic as belonging to a class map.')
aristaClassMapMatchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 2, 1), ).setIndexNames((0, "ARISTA-QOS-MIB", "aristaClassMapId"), (0, "ARISTA-QOS-MIB", "aristaClassMapType"), (0, "ARISTA-QOS-MIB", "aristaClassMapMatchIndex"))
if mibBuilder.loadTexts: aristaClassMapMatchEntry.setStatus('current')
if mibBuilder.loadTexts: aristaClassMapMatchEntry.setDescription('A conceptual row in the aristaClassMapMatchTable.')
aristaClassMapMatchIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: aristaClassMapMatchIndex.setStatus('current')
if mibBuilder.loadTexts: aristaClassMapMatchIndex.setDescription('This index identifies the position of a match criterion among all the criteria for a class map.')
aristaClassMapMatchType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ipv4AccessGroup", 1), ("ipv6AccessGroup", 2), ("vlan", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaClassMapMatchType.setStatus('current')
if mibBuilder.loadTexts: aristaClassMapMatchType.setDescription('Indicates the type of a match criterion for a class map. ipv4AccessGroup(1) means that it is an IPv4 access-control list. ipv6AccessGroup(2) means that it is an IPv6 access-control list. vlan(3) means that it is a VLAN-based match criterion.')
aristaClassMapMatchName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaClassMapMatchName.setStatus('current')
if mibBuilder.loadTexts: aristaClassMapMatchName.setDescription('Indicates the name of the access-control list if aristaClassMapMatchType is ipv4AccessGroup(1) or ipv6AccessGroup(2). Otherwise, it indicates the masked VLAN value or the comma-separated list of VLAN range values contained in the match criterion.')
aristaPolicyMapTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 3), )
if mibBuilder.loadTexts: aristaPolicyMapTable.setStatus('current')
if mibBuilder.loadTexts: aristaPolicyMapTable.setDescription('Lists the policy maps configured on the system.')
aristaPolicyMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 3, 1), ).setIndexNames((0, "ARISTA-QOS-MIB", "aristaPolicyMapId"), (0, "ARISTA-QOS-MIB", "aristaPolicyMapType"))
if mibBuilder.loadTexts: aristaPolicyMapEntry.setStatus('current')
if mibBuilder.loadTexts: aristaPolicyMapEntry.setDescription('A conceptual row in aristaPolicyMapTable.')
aristaPolicyMapId = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 3, 1, 1), AristaQosShortId())
if mibBuilder.loadTexts: aristaPolicyMapId.setStatus('current')
if mibBuilder.loadTexts: aristaPolicyMapId.setDescription("Bounded-length identifier for a given policy map, derived from the policy map's name.")
aristaPolicyMapType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 3, 1, 2), AristaQosMapType())
if mibBuilder.loadTexts: aristaPolicyMapType.setStatus('current')
if mibBuilder.loadTexts: aristaPolicyMapType.setDescription('Type of a given policy map.')
aristaPolicyMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaPolicyMapName.setStatus('current')
if mibBuilder.loadTexts: aristaPolicyMapName.setDescription('Name of a given policy map.')
aristaPolicyMapClassTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 4), )
if mibBuilder.loadTexts: aristaPolicyMapClassTable.setStatus('current')
if mibBuilder.loadTexts: aristaPolicyMapClassTable.setDescription('Lists the classes associated with a given policy map.')
aristaPolicyMapClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 4, 1), ).setIndexNames((0, "ARISTA-QOS-MIB", "aristaPolicyMapId"), (0, "ARISTA-QOS-MIB", "aristaPolicyMapType"), (0, "ARISTA-QOS-MIB", "aristaPolicyMapClassIndex"))
if mibBuilder.loadTexts: aristaPolicyMapClassEntry.setStatus('current')
if mibBuilder.loadTexts: aristaPolicyMapClassEntry.setDescription('A conceptual row in aristaPolicyMapClassTable.')
aristaPolicyMapClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: aristaPolicyMapClassIndex.setStatus('current')
if mibBuilder.loadTexts: aristaPolicyMapClassIndex.setDescription('Determines the sequence in which traffic is matched to classes within a policy map. The class with the smallest aristaPolicyMapClassIndex is given the first preference. Class Index values may not be consecutive.')
aristaPolicyMapClassId = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 4, 1, 2), AristaQosShortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaPolicyMapClassId.setStatus('current')
if mibBuilder.loadTexts: aristaPolicyMapClassId.setDescription('Identifier of the class map for a given class in a policy map.')
aristaPolicyMapActionTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 5), )
if mibBuilder.loadTexts: aristaPolicyMapActionTable.setStatus('current')
if mibBuilder.loadTexts: aristaPolicyMapActionTable.setDescription('Lists the actions that are applied to traffic classified as belonging to a particular class in a policy map.')
aristaPolicyMapActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 5, 1), ).setIndexNames((0, "ARISTA-QOS-MIB", "aristaPolicyMapId"), (0, "ARISTA-QOS-MIB", "aristaPolicyMapType"), (0, "ARISTA-QOS-MIB", "aristaClassMapId"), (0, "ARISTA-QOS-MIB", "aristaPolicyMapActionType"))
if mibBuilder.loadTexts: aristaPolicyMapActionEntry.setStatus('current')
if mibBuilder.loadTexts: aristaPolicyMapActionEntry.setDescription('A conceptual row in the aristaPolicyMapActionTable.')
aristaPolicyMapActionType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("actionSetShape", 1), ("actionSetBandwidth", 2), ("actionSetCos", 3), ("actionSetDscp", 4), ("actionSetTc", 5))))
if mibBuilder.loadTexts: aristaPolicyMapActionType.setStatus('current')
if mibBuilder.loadTexts: aristaPolicyMapActionType.setDescription("Type of a traffic-management action. For example: If the action is 'set cos 5', then the action type is 'actionSetCos'.")
aristaPolicyMapActionRateUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("rateUnitNone", 0), ("rateUnitPps", 1), ("rateUnitKbps", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaPolicyMapActionRateUnit.setStatus('current')
if mibBuilder.loadTexts: aristaPolicyMapActionRateUnit.setDescription('Indicates the rate unit of shaping/bandwidth actions. rateUnitNone - This action is not a shaping or bandwidth action. rateUnitPps - Packets per second rateUnitKbps - Kilobits per second')
aristaPolicyMapActionValue = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaPolicyMapActionValue.setStatus('current')
if mibBuilder.loadTexts: aristaPolicyMapActionValue.setDescription("Value applied in a traffic-management action. For example: If the action is 'set cos 5', then aristaPolicyMapActionValue is 5.")
aristaServicePolicyTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 6), )
if mibBuilder.loadTexts: aristaServicePolicyTable.setStatus('current')
if mibBuilder.loadTexts: aristaServicePolicyTable.setDescription('Lists the policy maps currently applied to interfaces.')
aristaServicePolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 6, 1), ).setIndexNames((0, "ARISTA-QOS-MIB", "aristaServicePolicyIfIndex"), (0, "ARISTA-QOS-MIB", "aristaServicePolicyDirection"))
if mibBuilder.loadTexts: aristaServicePolicyEntry.setStatus('current')
if mibBuilder.loadTexts: aristaServicePolicyEntry.setDescription('A conceptual row in the aristaServicePolicyTable.')
aristaServicePolicyIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 6, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: aristaServicePolicyIfIndex.setReference('RFC 2863, ifIndex')
if mibBuilder.loadTexts: aristaServicePolicyIfIndex.setStatus('current')
if mibBuilder.loadTexts: aristaServicePolicyIfIndex.setDescription('The index of interface to which a policy map is applied.')
aristaServicePolicyDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("input", 1), ("output", 2))))
if mibBuilder.loadTexts: aristaServicePolicyDirection.setStatus('current')
if mibBuilder.loadTexts: aristaServicePolicyDirection.setDescription('The direction of traffic for which the service policy applies. input - The service policy applies to inbound traffic. output - The service policy applies to outbound traffic.')
aristaServicePolicyMapId = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 6, 1, 3), AristaQosShortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaServicePolicyMapId.setStatus('current')
if mibBuilder.loadTexts: aristaServicePolicyMapId.setDescription('Identifier of the policy map applied to the interface.')
aristaServicePolicyMapType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 6, 1, 4), AristaQosMapType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaServicePolicyMapType.setStatus('current')
if mibBuilder.loadTexts: aristaServicePolicyMapType.setDescription('Type of the policy map applied to the interface.')
aristaQosStatsTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 7), )
if mibBuilder.loadTexts: aristaQosStatsTable.setStatus('current')
if mibBuilder.loadTexts: aristaQosStatsTable.setDescription('An entry in this table contains dropped, sent and matched packet counters for a given class of a policy map applied in a given direction. Counts are aggregated for all interfaces.')
aristaQosStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 7, 1), ).setIndexNames((0, "ARISTA-QOS-MIB", "aristaPolicyMapId"), (0, "ARISTA-QOS-MIB", "aristaPolicyMapType"), (0, "ARISTA-QOS-MIB", "aristaClassMapId"), (0, "ARISTA-QOS-MIB", "aristaServicePolicyDirection"))
if mibBuilder.loadTexts: aristaQosStatsEntry.setStatus('current')
if mibBuilder.loadTexts: aristaQosStatsEntry.setDescription('A conceptual row in the aristaQosStatsTable.')
aristaQosPktsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 7, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaQosPktsDropped.setStatus('current')
if mibBuilder.loadTexts: aristaQosPktsDropped.setDescription('The number of packets dropped by a service policy. This number is zero for classes of type dataPlane.')
aristaQosPktsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 7, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaQosPktsSent.setStatus('current')
if mibBuilder.loadTexts: aristaQosPktsSent.setDescription('The number of packets classified by a service policy and allowed through.')
aristaQosPktsMatched = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 7, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaQosPktsMatched.setStatus('current')
if mibBuilder.loadTexts: aristaQosPktsMatched.setDescription('The number of packets classified by a service policy. Equal to the sum of aristaQosPktsDropped and aristaQosPktsSent.')
aristaEcnCounterTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 8), )
if mibBuilder.loadTexts: aristaEcnCounterTable.setStatus('current')
if mibBuilder.loadTexts: aristaEcnCounterTable.setDescription('Lists the ECN Counter Value per unit as supported. Since different Arista devices have different capabilities for ECN counters, the table would contain the counter information per entity. This includes both packets that were received with congestion marked (ECN bits set) as well as packets that this Arista device marked with ECN bits before transmission. In cases where the platform is unable to count the already marked packets, the counter will only reflect the ones being marked by this specific device on the transmit side.')
aristaEcnCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 8, 1), ).setIndexNames((0, "ARISTA-QOS-MIB", "aristaEcnCounterDescriptor"))
if mibBuilder.loadTexts: aristaEcnCounterEntry.setStatus('current')
if mibBuilder.loadTexts: aristaEcnCounterEntry.setDescription('A conceptual row in the aristaEcnCounterTable.')
aristaEcnCounterDescriptor = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 8, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: aristaEcnCounterDescriptor.setStatus('current')
if mibBuilder.loadTexts: aristaEcnCounterDescriptor.setDescription('Describes the entity that the counter corresponds to. For instance, devices supporting ECN counters per forwarding element (or per chip) will have descriptor containing information like <ChipName>')
aristaEcnCounterValue = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 8, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaEcnCounterValue.setStatus('current')
if mibBuilder.loadTexts: aristaEcnCounterValue.setDescription('The number of packets above average threshhold')
aristaEcnCounterEntity = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 8, 1, 3), PhysicalIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaEcnCounterEntity.setStatus('current')
if mibBuilder.loadTexts: aristaEcnCounterEntity.setDescription('The physical index corresponding to the entity which is a non zero value used to identify a physical entity. This value will be zero if the entity does not have a physical index')
aristaQosMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 1))
aristaQosMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 2))
aristaQosMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 1, 1)).setObjects(("ARISTA-QOS-MIB", "aristaClassMapGroup"), ("ARISTA-QOS-MIB", "aristaPolicyMapGroup"), ("ARISTA-QOS-MIB", "aristaPolicyMapActionGroup"), ("ARISTA-QOS-MIB", "aristaServicePolicyGroup"), ("ARISTA-QOS-MIB", "aristaEcnCounterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaQosMibCompliance = aristaQosMibCompliance.setStatus('current')
if mibBuilder.loadTexts: aristaQosMibCompliance.setDescription('The compliance statement for Arista switches that support ARISTA-QOS-MIB.')
aristaClassMapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 2, 1)).setObjects(("ARISTA-QOS-MIB", "aristaClassMapName"), ("ARISTA-QOS-MIB", "aristaClassMapMatchCondition"), ("ARISTA-QOS-MIB", "aristaClassMapMatchType"), ("ARISTA-QOS-MIB", "aristaClassMapMatchName"), ("ARISTA-QOS-MIB", "aristaPolicyMapClassId"), ("ARISTA-QOS-MIB", "aristaQosPktsDropped"), ("ARISTA-QOS-MIB", "aristaQosPktsMatched"), ("ARISTA-QOS-MIB", "aristaQosPktsSent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaClassMapGroup = aristaClassMapGroup.setStatus('current')
if mibBuilder.loadTexts: aristaClassMapGroup.setDescription('The collection of objects that represent QoS configuration and statistics information for class maps.')
aristaPolicyMapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 2, 2)).setObjects(("ARISTA-QOS-MIB", "aristaPolicyMapName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaPolicyMapGroup = aristaPolicyMapGroup.setStatus('current')
if mibBuilder.loadTexts: aristaPolicyMapGroup.setDescription('The collection of objects that represent QoS configuration information for policy maps.')
aristaPolicyMapActionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 2, 3)).setObjects(("ARISTA-QOS-MIB", "aristaPolicyMapActionRateUnit"), ("ARISTA-QOS-MIB", "aristaPolicyMapActionValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaPolicyMapActionGroup = aristaPolicyMapActionGroup.setStatus('current')
if mibBuilder.loadTexts: aristaPolicyMapActionGroup.setDescription('The collection of objects that represent configuration information for QoS actions.')
aristaServicePolicyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 2, 4)).setObjects(("ARISTA-QOS-MIB", "aristaServicePolicyMapId"), ("ARISTA-QOS-MIB", "aristaServicePolicyMapType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaServicePolicyGroup = aristaServicePolicyGroup.setStatus('current')
if mibBuilder.loadTexts: aristaServicePolicyGroup.setDescription('The collection of objects that represent QoS configuration information for service policies.')
aristaEcnCounterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 2, 5)).setObjects(("ARISTA-QOS-MIB", "aristaEcnCounterValue"), ("ARISTA-QOS-MIB", "aristaEcnCounterEntity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaEcnCounterGroup = aristaEcnCounterGroup.setStatus('current')
if mibBuilder.loadTexts: aristaEcnCounterGroup.setDescription('The objects that represent ECN counter information')
mibBuilder.exportSymbols("ARISTA-QOS-MIB", aristaQosMib=aristaQosMib, AristaQosShortId=AristaQosShortId, AristaQosMapType=AristaQosMapType, aristaQosMibCompliance=aristaQosMibCompliance, aristaPolicyMapActionEntry=aristaPolicyMapActionEntry, aristaClassMapEntry=aristaClassMapEntry, aristaQosPktsDropped=aristaQosPktsDropped, aristaClassMapMatchType=aristaClassMapMatchType, aristaPolicyMapEntry=aristaPolicyMapEntry, aristaQosMibGroups=aristaQosMibGroups, aristaClassMapMatchEntry=aristaClassMapMatchEntry, aristaQosMibConformance=aristaQosMibConformance, aristaClassMapName=aristaClassMapName, aristaPolicyMapName=aristaPolicyMapName, aristaPolicyMapActionRateUnit=aristaPolicyMapActionRateUnit, aristaServicePolicyGroup=aristaServicePolicyGroup, aristaQosPktsMatched=aristaQosPktsMatched, aristaClassMapGroup=aristaClassMapGroup, aristaPolicyMapClassEntry=aristaPolicyMapClassEntry, aristaClassMapTable=aristaClassMapTable, aristaClassMapId=aristaClassMapId, aristaQosPktsSent=aristaQosPktsSent, aristaEcnCounterEntry=aristaEcnCounterEntry, aristaPolicyMapId=aristaPolicyMapId, aristaPolicyMapActionType=aristaPolicyMapActionType, aristaPolicyMapClassIndex=aristaPolicyMapClassIndex, aristaServicePolicyMapType=aristaServicePolicyMapType, aristaServicePolicyTable=aristaServicePolicyTable, aristaEcnCounterEntity=aristaEcnCounterEntity, aristaPolicyMapActionTable=aristaPolicyMapActionTable, aristaClassMapMatchTable=aristaClassMapMatchTable, aristaEcnCounterGroup=aristaEcnCounterGroup, aristaPolicyMapActionGroup=aristaPolicyMapActionGroup, aristaClassMapMatchName=aristaClassMapMatchName, aristaClassMapMatchCondition=aristaClassMapMatchCondition, aristaClassMapMatchIndex=aristaClassMapMatchIndex, aristaEcnCounterTable=aristaEcnCounterTable, aristaServicePolicyIfIndex=aristaServicePolicyIfIndex, aristaQosMibCompliances=aristaQosMibCompliances, aristaPolicyMapClassTable=aristaPolicyMapClassTable, PYSNMP_MODULE_ID=aristaQosMib, aristaPolicyMapActionValue=aristaPolicyMapActionValue, aristaServicePolicyMapId=aristaServicePolicyMapId, aristaQosStatsEntry=aristaQosStatsEntry, aristaQosStatsTable=aristaQosStatsTable, aristaPolicyMapType=aristaPolicyMapType, aristaServicePolicyEntry=aristaServicePolicyEntry, aristaPolicyMapTable=aristaPolicyMapTable, aristaEcnCounterValue=aristaEcnCounterValue, aristaEcnCounterDescriptor=aristaEcnCounterDescriptor, aristaClassMapType=aristaClassMapType, aristaQosMibObjects=aristaQosMibObjects, aristaServicePolicyDirection=aristaServicePolicyDirection, aristaPolicyMapClassId=aristaPolicyMapClassId, aristaPolicyMapGroup=aristaPolicyMapGroup)