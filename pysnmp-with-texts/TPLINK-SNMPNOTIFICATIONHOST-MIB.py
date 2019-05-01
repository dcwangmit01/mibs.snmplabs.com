#
# PySNMP MIB module TPLINK-SNMPNOTIFICATIONHOST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-SNMPNOTIFICATIONHOST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:25:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, NotificationType, iso, Integer32, Counter32, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, MibIdentifier, Bits, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "iso", "Integer32", "Counter32", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Bits", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkSnmpMIBObjects, = mibBuilder.importSymbols("TPLINK-SNMP-MIB", "tplinkSnmpMIBObjects")
TPRowStatus, = mibBuilder.importSymbols("TPLINK-TC-MIB", "TPRowStatus")
tpSnmpNotificationHost = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1))
tpSnmpNotificationHostTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1), )
if mibBuilder.loadTexts: tpSnmpNotificationHostTable.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostTable.setDescription('A list of SNMP notification host control entries.')
tpSnmpNotificationHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1), ).setIndexNames((0, "TPLINK-SNMPNOTIFICATIONHOST-MIB", "tpSnmpNotificationHostIpAddr"), (0, "TPLINK-SNMPNOTIFICATIONHOST-MIB", "tpSnmpNotificationHostUserName"))
if mibBuilder.loadTexts: tpSnmpNotificationHostEntry.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostEntry.setDescription(' With the Notification function enabled, the switch can initiatively report to the management station about the important events that occur on the Views, which allows the management station to monitor and process the events in time.')
tpSnmpNotificationHostIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpSnmpNotificationHostIpAddr.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostIpAddr.setDescription('IP Address of the management Host.')
tpSnmpNotificationHostUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpSnmpNotificationHostUserName.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostUserName.setDescription('The User name of the management station.')
tpSnmpNotificationHostUDPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 3), Integer32().clone(162)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpSnmpNotificationHostUDPPort.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostUDPPort.setDescription(' The number of the UDP port used to send notifications. The UDP port functions with the IP address for the notification sending. The default is 162. ')
tpSnmpNotificationHostSecMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("v1", 1), ("v2c", 2), ("v3", 3))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpSnmpNotificationHostSecMode.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostSecMode.setDescription('The Security Model of the management station. v1(1),SNMPv1 is defined for the notify. v2c(2),SNMPv2c is defined for the notify. v3(3),SNMPv3 is defined for the notify.')
tpSnmpNotificationHostSecLev = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAuthNoPriv", 1), ("authNoPriv", 2), ("authPriv", 3))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpSnmpNotificationHostSecLev.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostSecLev.setDescription('The Security Level for the SNMP v3 User. noAuthNoPriv(1),No authentication and no privacy security level are used. authNoPriv(2),Only the authentication security level is used. authPriv(3),Both the authentication and the privacy security levels are used.')
tpSnmpNotificationHostNtfyType = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("trap", 1), ("inform", 2))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpSnmpNotificationHostNtfyType.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostNtfyType.setDescription('The type for the notifications. trap(1),Indicates traps are sent. inform(2),Indicates informs are sent. The Inform type has a higher security than the Trap type.')
tpSnmpNotificationHostRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpSnmpNotificationHostRetry.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostRetry.setDescription(" Specify the amount of times the switch resends an inform request. The switch will resend the inform request if it doesn't get the response from the management station during the Timeout interval, and it will terminate resending the inform request if the resending times reach the specified Retry times. Its value range is 1-255.")
tpSnmpNotificationHostTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 8), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpSnmpNotificationHostTimeout.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostTimeout.setDescription(' Specify the maximum time for the switch to wait for the response from the management station before resending a request. Its value range is 1-3600.')
tpSnmpNotificationHostRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 9), TPRowStatus().clone(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpSnmpNotificationHostRowStatus.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostRowStatus.setDescription("The status column has three defined values: - `active(1)', which indicates that the conceptual row is available for using by the managed device; - `createAndGo(4)', which is supplied by a management station wishing to create a new instance of a conceptual row and to have its status automatically set to active, making it available for using by the managed device; - `destroy(6)', which is supplied by a management station wishing to delete all of the instances associated with an existing conceptual row.")
tpSnmpNotificationHostV6Table = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2), )
if mibBuilder.loadTexts: tpSnmpNotificationHostV6Table.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostV6Table.setDescription('A list of SNMP notification host control entries, supports IPV6.')
tpSnmpNotificationHostV6Entry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1), ).setIndexNames((0, "TPLINK-SNMPNOTIFICATIONHOST-MIB", "tpSnmpNotificationHostV6Index"))
if mibBuilder.loadTexts: tpSnmpNotificationHostV6Entry.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostV6Entry.setDescription(' With the Notification function enabled, the switch can initiatively report to the management station about the important events that occur on the Views, which allows the management station to monitor and process the events in time.')
tpSnmpNotificationHostV6Index = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 12)))
if mibBuilder.loadTexts: tpSnmpNotificationHostV6Index.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostV6Index.setDescription('The index to the conceptual row of the table. Negative numbers are not allowed. There are objects defined that point to conceptual rows of this table with this index value. Zero is used to denote that no corresponding row exists. Index values are assigned by the agent, and should not be reused but should continue to increase in value.')
tpSnmpNotificationHostV6IpMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpSnmpNotificationHostV6IpMode.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostV6IpMode.setDescription('The type of IP address.Type is IPv4 or IPv6')
tpSnmpNotificationHostV6IpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpSnmpNotificationHostV6IpAddr.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostV6IpAddr.setDescription('IP Address of the management Host. Just input like a string.')
tpSnmpNotificationHostV6UserName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpSnmpNotificationHostV6UserName.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostV6UserName.setDescription('The User name of the management station.')
tpSnmpNotificationHostV6UDPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1, 5), Integer32().clone(162)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpSnmpNotificationHostV6UDPPort.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostV6UDPPort.setDescription(' The number of the UDP port used to send notifications. The UDP port functions with the IP address for the notification sending. The default is 162. ')
tpSnmpNotificationHostV6SecMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("v1", 1), ("v2c", 2), ("v3", 3))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpSnmpNotificationHostV6SecMode.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostV6SecMode.setDescription('The Security Model of the management station. v1(1),SNMPv1 is defined for the notify. v2c(2),SNMPv2c is defined for the notify. v3(3),SNMPv3 is defined for the notify.')
tpSnmpNotificationHostV6SecLev = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAuthNoPriv", 1), ("authNoPriv", 2), ("authPriv", 3))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpSnmpNotificationHostV6SecLev.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostV6SecLev.setDescription('The Security Level for the SNMP v3 User. noAuthNoPriv(1),No authentication and no privacy security level are used. authNoPriv(2),Only the authentication security level is used. authPriv(3),Both the authentication and the privacy security levels are used.')
tpSnmpNotificationHostV6NtfyType = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("trap", 1), ("inform", 2))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpSnmpNotificationHostV6NtfyType.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostV6NtfyType.setDescription('The type for the notifications. trap(1),Indicates traps are sent. inform(2),Indicates informs are sent. The Inform type has a higher security than the Trap type.')
tpSnmpNotificationHostV6Retry = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpSnmpNotificationHostV6Retry.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostV6Retry.setDescription(" Specify the amount of times the switch resends an inform request. The switch will resend the inform request if it doesn't get the response from the management station during the Timeout interval, and it will terminate resending the inform request if the resending times reach the specified Retry times. Its value range is 1-255.")
tpSnmpNotificationHostV6Timeout = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1, 10), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpSnmpNotificationHostV6Timeout.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostV6Timeout.setDescription(' Specify the maximum time for the switch to wait for the response from the management station before resending a request. Its value range is 1-3600.')
tpSnmpNotificationHostV6RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1, 11), TPRowStatus().clone(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpSnmpNotificationHostV6RowStatus.setStatus('current')
if mibBuilder.loadTexts: tpSnmpNotificationHostV6RowStatus.setDescription("The status column has three defined values: - `active(1)', which indicates that the conceptual row is available for using by the managed device; - `createAndGo(4)', which is supplied by a management station wishing to create a new instance of a conceptual row and to have its status automatically set to active, making it available for using by the managed device; - `destroy(6)', which is supplied by a management station wishing to delete all of the instances associated with an existing conceptual row.")
mibBuilder.exportSymbols("TPLINK-SNMPNOTIFICATIONHOST-MIB", tpSnmpNotificationHostV6RowStatus=tpSnmpNotificationHostV6RowStatus, tpSnmpNotificationHostSecLev=tpSnmpNotificationHostSecLev, tpSnmpNotificationHostV6Table=tpSnmpNotificationHostV6Table, tpSnmpNotificationHostV6SecLev=tpSnmpNotificationHostV6SecLev, tpSnmpNotificationHostRowStatus=tpSnmpNotificationHostRowStatus, tpSnmpNotificationHostEntry=tpSnmpNotificationHostEntry, tpSnmpNotificationHostV6Timeout=tpSnmpNotificationHostV6Timeout, tpSnmpNotificationHostUserName=tpSnmpNotificationHostUserName, tpSnmpNotificationHostV6Index=tpSnmpNotificationHostV6Index, tpSnmpNotificationHostRetry=tpSnmpNotificationHostRetry, tpSnmpNotificationHostNtfyType=tpSnmpNotificationHostNtfyType, tpSnmpNotificationHostV6SecMode=tpSnmpNotificationHostV6SecMode, tpSnmpNotificationHostV6UserName=tpSnmpNotificationHostV6UserName, tpSnmpNotificationHostV6IpAddr=tpSnmpNotificationHostV6IpAddr, tpSnmpNotificationHostTable=tpSnmpNotificationHostTable, tpSnmpNotificationHostTimeout=tpSnmpNotificationHostTimeout, tpSnmpNotificationHostV6NtfyType=tpSnmpNotificationHostV6NtfyType, tpSnmpNotificationHostV6Entry=tpSnmpNotificationHostV6Entry, tpSnmpNotificationHostSecMode=tpSnmpNotificationHostSecMode, tpSnmpNotificationHostV6Retry=tpSnmpNotificationHostV6Retry, tpSnmpNotificationHostV6UDPPort=tpSnmpNotificationHostV6UDPPort, tpSnmpNotificationHostV6IpMode=tpSnmpNotificationHostV6IpMode, tpSnmpNotificationHost=tpSnmpNotificationHost, tpSnmpNotificationHostUDPPort=tpSnmpNotificationHostUDPPort, tpSnmpNotificationHostIpAddr=tpSnmpNotificationHostIpAddr)