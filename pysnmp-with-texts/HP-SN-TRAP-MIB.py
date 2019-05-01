#
# PySNMP MIB module HP-SN-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-SN-MIBS
# Produced by pysmi-0.3.4 at Wed May  1 13:36:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
snAgentBrdIndex, snChasPwrSupplyStatus, snChasPwrSupplyIndex, snChasFanIndex, snChasFanDescription, snChasPwrSupplyDescription, snAgGblTrapMessage = mibBuilder.importSymbols("HP-SN-AGENT-MIB", "snAgentBrdIndex", "snChasPwrSupplyStatus", "snChasPwrSupplyIndex", "snChasFanIndex", "snChasFanDescription", "snChasPwrSupplyDescription", "snAgGblTrapMessage")
hp, = mibBuilder.importSymbols("HP-SN-ROOT-MIB", "hp")
snL4TrapRealServerName, snL4TrapRealServerPort, snL4TrapRealServerIP, snL4MaxSessionLimit, snL4TcpSynLimit, snL4TrapRealServerCurConnections = mibBuilder.importSymbols("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName", "snL4TrapRealServerPort", "snL4TrapRealServerIP", "snL4MaxSessionLimit", "snL4TcpSynLimit", "snL4TrapRealServerCurConnections")
snSwViolatorMacAddress, snSwViolatorPortNumber = mibBuilder.importSymbols("HP-SN-SWITCH-GROUP-MIB", "snSwViolatorMacAddress", "snSwViolatorPortNumber")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, TimeTicks, Integer32, NotificationType, Unsigned32, iso, Counter64, Gauge32, ObjectIdentity, Counter32, IpAddress, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "TimeTicks", "Integer32", "NotificationType", "Unsigned32", "iso", "Counter64", "Gauge32", "ObjectIdentity", "Counter32", "IpAddress", "NotificationType", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snTrapChasPwrSupply = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,1)).setObjects(("HP-SN-AGENT-MIB", "snChasPwrSupplyStatus"))
if mibBuilder.loadTexts: snTrapChasPwrSupply.setDescription('The SNMP trap that is generated when a power supply fails to operate normally. The value is a packed bit string; the 2 power supplies status are encoded into 4 bits (a nibble). The following shows the meaning of each bit: (bit 0 is the least significant bit). bit position meaning ------------ ------- 4-31 reserved 3 Power Supply 2 DC (0=bad, 1=good). 2 Power Supply 1 DC (0=bad, 1=good). 1 Power Supply 2 present status (0=present, 1=not-present). 0 Power Supply 1 present status (0=present, 1=not-present).')
snTrapLockedAddressViolation = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,2)).setObjects(("HP-SN-SWITCH-GROUP-MIB", "snSwViolatorPortNumber"), ("HP-SN-SWITCH-GROUP-MIB", "snSwViolatorMacAddress"))
if mibBuilder.loadTexts: snTrapLockedAddressViolation.setDescription('The SNMP trap that is generated when more source MAC addresses are received from a port than the maximum number of addresses configured to that port.')
snTrapL4MaxSessionLimitReached = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,19)).setObjects(("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4MaxSessionLimit"))
if mibBuilder.loadTexts: snTrapL4MaxSessionLimitReached.setDescription('The SNMP trap that is generated when the maximum number of connections reached.')
snTrapL4TcpSynLimitReached = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,20)).setObjects(("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TcpSynLimit"))
if mibBuilder.loadTexts: snTrapL4TcpSynLimitReached.setDescription('The SNMP trap that is generated when the number of TCP SYN limits reached.')
snTrapL4RealServerUp = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,21)).setObjects(("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"), ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"))
if mibBuilder.loadTexts: snTrapL4RealServerUp.setDescription('The SNMP trap that is generated when the load balancing real server is up.')
snTrapL4RealServerDown = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,22)).setObjects(("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"), ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"))
if mibBuilder.loadTexts: snTrapL4RealServerDown.setDescription('The SNMP trap that is generated when the load balancing real server is down.')
snTrapL4RealServerPortUp = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,23)).setObjects(("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"), ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"), ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerPort"))
if mibBuilder.loadTexts: snTrapL4RealServerPortUp.setDescription('The SNMP trap that is generated when the load balancing real server TCP port is up.')
snTrapL4RealServerPortDown = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,24)).setObjects(("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"), ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"), ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerPort"))
if mibBuilder.loadTexts: snTrapL4RealServerPortDown.setDescription('The SNMP trap that is generated when the load balancing real server TCP port is down.')
snTrapL4RealServerMaxConnectionLimitReached = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,25)).setObjects(("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"), ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"), ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerCurConnections"))
if mibBuilder.loadTexts: snTrapL4RealServerMaxConnectionLimitReached.setDescription('The SNMP trap that is generated when the real server reaches maximum number of connections.')
snTrapL4BecomeStandby = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,26))
if mibBuilder.loadTexts: snTrapL4BecomeStandby.setDescription('The SNMP trap that is generated when the server load balancing switch changes state from active to standby.')
snTrapL4BecomeActive = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,27))
if mibBuilder.loadTexts: snTrapL4BecomeActive.setDescription('The SNMP trap that is generated when the server load balancing switch changes state from standby to active.')
snTrapModuleInserted = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,28)).setObjects(("HP-SN-AGENT-MIB", "snAgentBrdIndex"))
if mibBuilder.loadTexts: snTrapModuleInserted.setDescription('The SNMP trap that is generated when a module was inserted to the chassis during system running.')
snTrapModuleRemoved = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,29)).setObjects(("HP-SN-AGENT-MIB", "snAgentBrdIndex"))
if mibBuilder.loadTexts: snTrapModuleRemoved.setDescription('The SNMP trap that is generated when a module was removed from the chassis during system running.')
snTrapChasPwrSupplyFailed = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,30)).setObjects(("HP-SN-AGENT-MIB", "snChasPwrSupplyIndex"), ("HP-SN-AGENT-MIB", "snChasPwrSupplyDescription"))
if mibBuilder.loadTexts: snTrapChasPwrSupplyFailed.setDescription('The SNMP trap that is generated when a power supply operational status changed from normal to failure.')
snTrapChasFanFailed = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,31)).setObjects(("HP-SN-AGENT-MIB", "snChasFanIndex"), ("HP-SN-AGENT-MIB", "snChasFanDescription"))
if mibBuilder.loadTexts: snTrapChasFanFailed.setDescription('The SNMP trap that is generated when a fan fails to operate normally.')
snTrapLockedAddressViolation2 = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,32)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapLockedAddressViolation2.setDescription('The SNMP trap that is generated when more source MAC addresses are received from a port than the maximum number of addresses configured to that port.')
snTrapFsrpIfStateChange = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,33)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapFsrpIfStateChange.setDescription('The SNMP trap that is generated when a FSRP routing device changed state from active to standby or vice-versa.')
snTrapVrrpIfStateChange = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,34)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapVrrpIfStateChange.setDescription('The SNMP trap that is generated when a VRRP routing device switched between states master, backup, intialized or uknown.')
snTrapMgmtModuleRedunStateChange = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,35)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapMgmtModuleRedunStateChange.setDescription('The SNMP trap that is generated when the management module changes redundancy state.')
snTrapTemperatureWarning = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,36)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapTemperatureWarning.setDescription('The SNMP trap that is generated when the actual temperature reading is above the warning temperature threshold.')
snTrapAccessListDeny = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,37)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapAccessListDeny.setDescription('The SNMP trap that is generated when a packet was denied by an access list.')
snTrapMacFilterDeny = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,38)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapMacFilterDeny.setDescription('The SNMP trap that is generated when a packet was denied by a MAC address filter.')
snTrapL4GslbRemoteUp = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,39)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapL4GslbRemoteUp.setDescription('The SNMP trap that is generated when the connection to the remote SI is established.')
snTrapL4GslbRemoteDown = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,40)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapL4GslbRemoteDown.setDescription('The SNMP trap that is generated when the connection to the remote SI is down.')
snTrapL4GslbRemoteControllerUp = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,41)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapL4GslbRemoteControllerUp.setDescription('The SNMP trap that is generated when the connection to the GSLB SI is established.')
snTrapL4GslbRemoteControllerDown = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,42)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapL4GslbRemoteControllerDown.setDescription('The SNMP trap that is generated when the connection to the GSLB SI is down.')
snTrapL4GslbHealthCheckIpUp = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,43)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapL4GslbHealthCheckIpUp.setDescription('The SNMP trap that is generated when GSLB health check for an address transitions from down to active state.')
snTrapL4GslbHealthCheckIpDown = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,44)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapL4GslbHealthCheckIpDown.setDescription('The SNMP trap that is generated when GSLB health check for an address transitions from active to down state.')
snTrapL4GslbHealthCheckIpPortUp = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,45)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapL4GslbHealthCheckIpPortUp.setDescription('The SNMP trap that is generated when a given port for a health check address is up.')
snTrapL4GslbHealthCheckIpPortDown = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,46)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapL4GslbHealthCheckIpPortDown.setDescription('The SNMP trap that is generated when a given port for a health check address is down.')
snTrapL4FirewallBecomeStandby = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,47))
if mibBuilder.loadTexts: snTrapL4FirewallBecomeStandby.setDescription('The SNMP trap that is generated when the server load balancing switch Firewall changes state from active to standby.')
snTrapL4FirewallBecomeActive = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,48))
if mibBuilder.loadTexts: snTrapL4FirewallBecomeActive.setDescription('The SNMP trap that is generated when the server load balancing switch Firewall changes state from standby to active.')
snTrapL4FirewallPathUp = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,49))
if mibBuilder.loadTexts: snTrapL4FirewallPathUp.setDescription('The SNMP trap that is generated when the server load balancing switch Firewall path is up.')
snTrapL4FirewallPathDown = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,50))
if mibBuilder.loadTexts: snTrapL4FirewallPathDown.setDescription('The SNMP trap that is generated when the server load balancing switch Firewall path is down.')
snTrapIcmpLocalExceedBurst = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,51)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapIcmpLocalExceedBurst.setDescription('The SNMP trap that is generated when incoming ICMP exceeds burst-MAX.')
snTrapIcmpTransitExceedBurst = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,52)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapIcmpTransitExceedBurst.setDescription('The SNMP trap that is generated when transit ICMP exceeds burst-MAX.')
snTrapTcpLocalExceedBurst = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,53)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapTcpLocalExceedBurst.setDescription('The SNMP trap that is generated when incoming TCP SYN exceeds burst-MAX.')
snTrapTcpTransitExceedBurst = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,54)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapTcpTransitExceedBurst.setDescription('The SNMP trap that is generated when transit TCP exceeds burst-MAX.')
snTrapL4ContentVerification = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,55))
if mibBuilder.loadTexts: snTrapL4ContentVerification.setDescription('The SNMP trap that is generated when the HTTP match-list pattern is found.')
snTrapDuplicateIp = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,56))
if mibBuilder.loadTexts: snTrapDuplicateIp.setDescription('Duplicate IP address detected.')
snTrapMplsProblem = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,57))
if mibBuilder.loadTexts: snTrapMplsProblem.setDescription('MPLS Problem Detected.')
snTrapMplsException = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,58))
if mibBuilder.loadTexts: snTrapMplsException.setDescription('MPLS Exception Detected.')
snTrapMplsAudit = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,59))
if mibBuilder.loadTexts: snTrapMplsAudit.setDescription('MPLS Audit Trap.')
snTrapMplsDeveloper = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,60))
if mibBuilder.loadTexts: snTrapMplsDeveloper.setDescription('MPLS Developer Trap.')
snTrapNoBmFreeQueue = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,61)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapNoBmFreeQueue.setDescription('The SNMP trap that is generated when no free queue is available in buffer manager.')
snTrapSmcDmaDrop = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,62)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapSmcDmaDrop.setDescription('The SNMP trap that is generated when SMC DMA packet is dropped.')
snTrapSmcBpDrop = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,63)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapSmcBpDrop.setDescription('The SNMP trap that is generated when SMC BackPlane packet is dropped.')
snTrapBmWriteSeqDrop = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,64)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapBmWriteSeqDrop.setDescription('The SNMP trap that is generated when BM write sequence packet is dropped.')
snTrapBgpPeerUp = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,65)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapBgpPeerUp.setDescription('The SNMP trap that is generated when the bgp peer is up.')
snTrapBgpPeerDown = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,66)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapBgpPeerDown.setDescription('The SNMP trap that is generated when the bgp peer is down.')
snTrapL4RealServerResponseTimeLowerLimit = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,67)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapL4RealServerResponseTimeLowerLimit.setDescription('The SNMP trap that is generated when the real server average response time exceeds lower threshold.')
snTrapL4RealServerResponseTimeUpperLimit = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,68)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapL4RealServerResponseTimeUpperLimit.setDescription('The SNMP trap that is generated when the real server average response time exceeds upper threshold.')
snTrapL4TcpAttackRateExceedMax = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,69)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapL4TcpAttackRateExceedMax.setDescription('The SNMP trap that is generated when the TCP attack rate exceeds configured maximum.')
snTrapL4TcpAttackRateExceedThreshold = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,70)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapL4TcpAttackRateExceedThreshold.setDescription('The SNMP trap that is generated when the TCP attack rate exceeds 80% of configured maximum.')
snTrapL4ConnectionRateExceedMax = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,71)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapL4ConnectionRateExceedMax.setDescription('The SNMP trap that is generated when the L4 connection rate exceeds configured maximum.')
snTrapL4ConnectionRateExceedThreshold = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,72)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapL4ConnectionRateExceedThreshold.setDescription('The SNMP trap that is generated when the L4 connection rate exceeds 80% of configured maximum')
snTrapRunningConfigChanged = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,73)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapRunningConfigChanged.setDescription('The SNMP trap that is generated when the running configuration was changed.')
snTrapStartupConfigChanged = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,74)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapStartupConfigChanged.setDescription('The SNMP trap that is generated when the startup configuration was changed.')
snTrapUserLogin = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,75)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapUserLogin.setDescription('The SNMP trap that is generated when user login.')
snTrapUserLogout = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,76)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapUserLogout.setDescription('The SNMP trap that is generated when user logout.')
snTrapPortSecurityViolation = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,77)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapPortSecurityViolation.setDescription('The SNMP trap that is generated when insecure MAC addresses are received from a port with MAC security feature enabled.')
snTrapPortSecurityShutdown = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,78)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapPortSecurityShutdown.setDescription('The SNMP trap that is generated when insecure MAC addresses are received from a port caused the port to shutdown.')
snTrapMrpStateChange = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,79)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapMrpStateChange.setDescription('The SNMP trap that is generated when a MRP switching and routing device changed state to disabled, blocking, preforwarding, forwarding, uknown.')
snTrapMrpCamError = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,80)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapMrpCamError.setDescription('The SNMP trap that is generated when a MRP Cam Error occurs.')
snTrapChasPwrSupplyOK = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,81)).setObjects(("HP-SN-AGENT-MIB", "snChasPwrSupplyIndex"), ("HP-SN-AGENT-MIB", "snChasPwrSupplyDescription"))
if mibBuilder.loadTexts: snTrapChasPwrSupplyOK.setDescription('The SNMP trap that is generated when a power supply operational status changed from failure to normal.')
snTrapVrrpeIfStateChange = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,82)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapVrrpeIfStateChange.setDescription('The SNMP trap that is generated when a VRRPE routing device switched between states master, backup, intialized or uknown.')
snTrapVsrpIfStateChange = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,83)).setObjects(("HP-SN-AGENT-MIB", "snAgGblTrapMessage"))
if mibBuilder.loadTexts: snTrapVsrpIfStateChange.setDescription('The SNMP trap that is generated when a VSRP switching and routing device switched between states master, backup, intialized or uknown.')
mibBuilder.exportSymbols("HP-SN-TRAP-MIB", snTrapModuleRemoved=snTrapModuleRemoved, snTrapMplsException=snTrapMplsException, snTrapBgpPeerDown=snTrapBgpPeerDown, snTrapTcpLocalExceedBurst=snTrapTcpLocalExceedBurst, snTrapRunningConfigChanged=snTrapRunningConfigChanged, snTrapL4ConnectionRateExceedThreshold=snTrapL4ConnectionRateExceedThreshold, snTrapIcmpTransitExceedBurst=snTrapIcmpTransitExceedBurst, snTrapAccessListDeny=snTrapAccessListDeny, snTrapMrpStateChange=snTrapMrpStateChange, snTrapSmcDmaDrop=snTrapSmcDmaDrop, snTrapMplsProblem=snTrapMplsProblem, snTrapL4RealServerResponseTimeUpperLimit=snTrapL4RealServerResponseTimeUpperLimit, snTrapL4GslbRemoteControllerDown=snTrapL4GslbRemoteControllerDown, snTrapDuplicateIp=snTrapDuplicateIp, snTrapLockedAddressViolation2=snTrapLockedAddressViolation2, snTrapL4BecomeActive=snTrapL4BecomeActive, snTrapPortSecurityViolation=snTrapPortSecurityViolation, snTrapFsrpIfStateChange=snTrapFsrpIfStateChange, snTrapL4MaxSessionLimitReached=snTrapL4MaxSessionLimitReached, snTrapNoBmFreeQueue=snTrapNoBmFreeQueue, snTrapMacFilterDeny=snTrapMacFilterDeny, snTrapL4ConnectionRateExceedMax=snTrapL4ConnectionRateExceedMax, snTrapL4RealServerDown=snTrapL4RealServerDown, snTrapL4RealServerUp=snTrapL4RealServerUp, snTrapMgmtModuleRedunStateChange=snTrapMgmtModuleRedunStateChange, snTrapL4GslbHealthCheckIpDown=snTrapL4GslbHealthCheckIpDown, snTrapUserLogout=snTrapUserLogout, snTrapMrpCamError=snTrapMrpCamError, snTrapVsrpIfStateChange=snTrapVsrpIfStateChange, snTrapL4FirewallPathDown=snTrapL4FirewallPathDown, snTrapBmWriteSeqDrop=snTrapBmWriteSeqDrop, snTrapL4TcpAttackRateExceedMax=snTrapL4TcpAttackRateExceedMax, snTrapL4TcpAttackRateExceedThreshold=snTrapL4TcpAttackRateExceedThreshold, snTrapL4TcpSynLimitReached=snTrapL4TcpSynLimitReached, snTrapBgpPeerUp=snTrapBgpPeerUp, snTrapPortSecurityShutdown=snTrapPortSecurityShutdown, snTrapL4RealServerPortUp=snTrapL4RealServerPortUp, snTrapL4RealServerMaxConnectionLimitReached=snTrapL4RealServerMaxConnectionLimitReached, snTrapChasPwrSupply=snTrapChasPwrSupply, snTrapChasPwrSupplyFailed=snTrapChasPwrSupplyFailed, snTrapVrrpIfStateChange=snTrapVrrpIfStateChange, snTrapL4GslbRemoteUp=snTrapL4GslbRemoteUp, snTrapL4FirewallPathUp=snTrapL4FirewallPathUp, snTrapTcpTransitExceedBurst=snTrapTcpTransitExceedBurst, snTrapL4BecomeStandby=snTrapL4BecomeStandby, snTrapL4GslbHealthCheckIpUp=snTrapL4GslbHealthCheckIpUp, snTrapUserLogin=snTrapUserLogin, snTrapChasPwrSupplyOK=snTrapChasPwrSupplyOK, snTrapVrrpeIfStateChange=snTrapVrrpeIfStateChange, snTrapL4FirewallBecomeActive=snTrapL4FirewallBecomeActive, snTrapSmcBpDrop=snTrapSmcBpDrop, snTrapL4RealServerResponseTimeLowerLimit=snTrapL4RealServerResponseTimeLowerLimit, snTrapMplsDeveloper=snTrapMplsDeveloper, snTrapL4GslbRemoteDown=snTrapL4GslbRemoteDown, snTrapL4GslbHealthCheckIpPortUp=snTrapL4GslbHealthCheckIpPortUp, snTrapL4GslbRemoteControllerUp=snTrapL4GslbRemoteControllerUp, snTrapLockedAddressViolation=snTrapLockedAddressViolation, snTrapIcmpLocalExceedBurst=snTrapIcmpLocalExceedBurst, snTrapChasFanFailed=snTrapChasFanFailed, snTrapL4ContentVerification=snTrapL4ContentVerification, snTrapMplsAudit=snTrapMplsAudit, snTrapStartupConfigChanged=snTrapStartupConfigChanged, snTrapTemperatureWarning=snTrapTemperatureWarning, snTrapL4GslbHealthCheckIpPortDown=snTrapL4GslbHealthCheckIpPortDown, snTrapModuleInserted=snTrapModuleInserted, snTrapL4RealServerPortDown=snTrapL4RealServerPortDown, snTrapL4FirewallBecomeStandby=snTrapL4FirewallBecomeStandby)