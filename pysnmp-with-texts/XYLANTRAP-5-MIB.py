#
# PySNMP MIB module XYLANTRAP-5-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLANTRAP-5-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:45:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
chasModuleSubUnit, chasControlSlot, chasPowerSupply2State, chasModuleSlot, chasControlState, chasModuleType, chasModuleOperStatus, chasPowerSupply1State = mibBuilder.importSymbols("CHASSIS-MIB", "chasModuleSubUnit", "chasControlSlot", "chasPowerSupply2State", "chasModuleSlot", "chasControlState", "chasModuleType", "chasModuleOperStatus", "chasPowerSupply1State")
fddimibSMTIndex, fddimibSMTCFState = mibBuilder.importSymbols("FDDI-SMT73-MIB", "fddimibSMTIndex", "fddimibSMTCFState")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Unsigned32, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, Integer32, Bits, ModuleIdentity, iso, NotificationType, MibIdentifier, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "Integer32", "Bits", "ModuleIdentity", "iso", "NotificationType", "MibIdentifier", "NotificationType", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atmxVccAdmStatus, atmxVccSlotIndex, atmxServicePortIndex, atmxVccVpi, atmxServiceAdmStatus, atmxPortEnableILMI, atmxServiceNumber, atmxVccVci, atmxServiceSlotIndex, atmxVccPortIndex, atmxPortPortIndex, atmxPortSlotIndex = mibBuilder.importSymbols("XYLAN-ATM-MIB", "atmxVccAdmStatus", "atmxVccSlotIndex", "atmxServicePortIndex", "atmxVccVpi", "atmxServiceAdmStatus", "atmxPortEnableILMI", "atmxServiceNumber", "atmxVccVci", "atmxServiceSlotIndex", "atmxVccPortIndex", "atmxPortPortIndex", "atmxPortSlotIndex")
pizzaSwitch, microSwitch, xylanSwitchDevice, omniswitch5, omniswitch9, xylan = mibBuilder.importSymbols("XYLAN-BASE-MIB", "pizzaSwitch", "microSwitch", "xylanSwitchDevice", "omniswitch5", "omniswitch9", "xylan")
frxVcControlSlotIndex, frxVcControlPortIndex, frxVcControlDlci = mibBuilder.importSymbols("XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex", "frxVcControlPortIndex", "frxVcControlDlci")
healthThreshModTrapData, healthThreshModTrapCount, healthThreshDevTrapData = mibBuilder.importSymbols("XYLAN-HEALTH-MIB", "healthThreshModTrapData", "healthThreshModTrapCount", "healthThreshDevTrapData")
xylanIpAssocDupSlot, xylanIpAssocAddr, xylanIpAssocDupIntf, xylanIpAssocSlot, xylanIpAssocDupMac, xylanIpAssocMac, xylanIpAssocIntf = mibBuilder.importSymbols("XYLAN-IP-MIB", "xylanIpAssocDupSlot", "xylanIpAssocAddr", "xylanIpAssocDupIntf", "xylanIpAssocSlot", "xylanIpAssocDupMac", "xylanIpAssocMac", "xylanIpAssocIntf")
systemEventTrapNumber, = mibBuilder.importSymbols("XYLAN-MGMTSTN-MIB", "systemEventTrapNumber")
vportIF, vportFuncTypeInstance, vportFuncType, vportAdmStatus, vportSlot = mibBuilder.importSymbols("XYLAN-PORT-MIB", "vportIF", "vportFuncTypeInstance", "vportFuncType", "vportAdmStatus", "vportSlot")
vLanAdmStatus, vDupMacSlot, vDupMacTime, vDupMacMac, atVLANId, atVLANAdminStatus, atVLANGroupId, vLanNumber, vDupMacIntf, vBrdgTpFdbAddress = mibBuilder.importSymbols("XYLAN-VLAN-MIB", "vLanAdmStatus", "vDupMacSlot", "vDupMacTime", "vDupMacMac", "atVLANId", "atVLANAdminStatus", "atVLANGroupId", "vLanNumber", "vDupMacIntf", "vBrdgTpFdbAddress")
tempAlarm5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,1))
if mibBuilder.loadTexts: tempAlarm5.setDescription('A tempAlarm indicates a temperature sensor has changed its state from underThreshold(4) to overThreshold(3).')
moduleChange5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,2)).setObjects(("CHASSIS-MIB", "chasModuleSlot"), ("CHASSIS-MIB", "chasModuleSubUnit"), ("CHASSIS-MIB", "chasModuleType"))
if mibBuilder.loadTexts: moduleChange5.setDescription('A moduleChange trap occurs when a module is inserted or removed from the chassis.')
powerEvent5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,3)).setObjects(("CHASSIS-MIB", "chasPowerSupply1State"), ("CHASSIS-MIB", "chasPowerSupply2State"))
if mibBuilder.loadTexts: powerEvent5.setDescription('A powerEvent trap occurs when a power supply is inserted or removed from the chassis, or a problem condition is recognized on a power supply.')
controllerEvent5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,4)).setObjects(("CHASSIS-MIB", "chasControlSlot"), ("CHASSIS-MIB", "chasControlState"))
if mibBuilder.loadTexts: controllerEvent5.setDescription('A controlEvent trap occurs when a chassis controller (MPM) loses or gains the state of master(3). If this is due to chassis controller being inserted or removed from the slot, a moduleChange trap will also be sent.')
loginViolation5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,5))
if mibBuilder.loadTexts: loginViolation5.setDescription('A loginViolation trap occurs when a login attempt fails due to an incorrect login-id or password.')
macVlanViolation5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,6)).setObjects(("XYLAN-VLAN-MIB", "vBrdgTpFdbAddress"))
if mibBuilder.loadTexts: macVlanViolation5.setDescription('A macVlanViolation trap occurs when a frame is received from a port with a VLAN ID different from the VLAN where the frame previously has received.')
macDuplicatePort5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,7)).setObjects(("XYLAN-VLAN-MIB", "vBrdgTpFdbAddress"))
if mibBuilder.loadTexts: macDuplicatePort5.setDescription('A macDuplicatePort trap occurs when a frame is received from a source port different from the port where the frame previously has received although they both ports belong to the same VLAN.')
portLinkUpEvent5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,8)).setObjects(("XYLAN-PORT-MIB", "vportSlot"), ("XYLAN-PORT-MIB", "vportIF"), ("XYLAN-PORT-MIB", "vportFuncType"), ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
if mibBuilder.loadTexts: portLinkUpEvent5.setDescription('A portLinkTrap occurs whenever a phy, log, or virt port is enabled.')
portLinkDownEvent5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,9)).setObjects(("XYLAN-PORT-MIB", "vportSlot"), ("XYLAN-PORT-MIB", "vportIF"), ("XYLAN-PORT-MIB", "vportFuncType"), ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
if mibBuilder.loadTexts: portLinkDownEvent5.setDescription('A portLinkTrap occurs whenever a phy, log, or virt port is disabled.')
portPartitioned5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,10)).setObjects(("XYLAN-PORT-MIB", "vportSlot"), ("XYLAN-PORT-MIB", "vportIF"), ("XYLAN-PORT-MIB", "vportFuncType"), ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
if mibBuilder.loadTexts: portPartitioned5.setDescription('A portPartioned trap occurs when the physical port has transitioned thru enable/disable states faster than 10 times in the past second...indicative of a flakey cable.')
portRecordMismatch5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,11)).setObjects(("XYLAN-PORT-MIB", "vportSlot"), ("XYLAN-PORT-MIB", "vportIF"), ("XYLAN-PORT-MIB", "vportFuncType"), ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
if mibBuilder.loadTexts: portRecordMismatch5.setDescription('A portRecordMismatch trap occurs when the specified port data is found to be diferent than the privious configuration. Typically this will be generated when a NIC of one type is swapped out for a DIFFERENT type. IE ethernet for fddi, atm for token-ring, etc...')
groupChange5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,14)).setObjects(("XYLAN-VLAN-MIB", "vLanNumber"), ("XYLAN-VLAN-MIB", "vLanAdmStatus"))
if mibBuilder.loadTexts: groupChange5.setDescription('A groupChange trap occurs whenever a group is created or deleted from the system via the UI or SNMP. The group and status code are sent as part of the variable binding. The status codes are: 1 - disable 2 - enable 3 - delete 4 - create 5 - modify (see xylan-vport MIB)')
vlanChange5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,15)).setObjects(("XYLAN-VLAN-MIB", "atVLANGroupId"), ("XYLAN-VLAN-MIB", "atVLANId"), ("XYLAN-VLAN-MIB", "atVLANAdminStatus"))
if mibBuilder.loadTexts: vlanChange5.setDescription('A vlanChange trap occurs whenever a VLAN is created or deleted from the system via the UI or SNMP. The group, vlan and status code are sent as part of the variable binding. See groupChange for the status codes.')
portMove5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,16)).setObjects(("XYLAN-PORT-MIB", "vportSlot"), ("XYLAN-PORT-MIB", "vportIF"), ("XYLAN-PORT-MIB", "vportFuncType"), ("XYLAN-PORT-MIB", "vportFuncTypeInstance"), ("XYLAN-PORT-MIB", "vportAdmStatus"))
if mibBuilder.loadTexts: portMove5.setDescription('A portMove trap occurs when the specified port is moved from a group/vlan or has had its configuration changed.')
moduleResetReload5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,17)).setObjects(("CHASSIS-MIB", "chasModuleSlot"), ("CHASSIS-MIB", "chasModuleSubUnit"), ("CHASSIS-MIB", "chasModuleType"), ("CHASSIS-MIB", "chasModuleOperStatus"))
if mibBuilder.loadTexts: moduleResetReload5.setDescription('A moduleResetReload trap occurs when the specified module has been reset or reloaded by the chassis mgr.')
systemEvent5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,18)).setObjects(("XYLAN-MGMTSTN-MIB", "systemEventTrapNumber"))
if mibBuilder.loadTexts: systemEvent5.setDescription('A systemEvent trap occurs when a potentially fatal system error occurrs. Such as: out of FLASH/ memory space. The event type is in the var bind. A Descriptive string MAY be present. The following trap numbers are defined (see xylan-trapc.mib): 10 Unspecified log event 11 Log file full 12 Log file erased 20 Unspecified memory event 21 Memory shortage 30 Unsepcified CPU event 31 Long term CPU overload 32 Short term CPU overload 40 Unspecified ffs event 41 Attempt to write to full ffs 42 System/user directed purge 43 Removed imgs/cfgs 44 Exec file removed 45 Config file removed 46 Exec file updated 47 Config file updated 50 Unspecified chassis event 51 Module failed to init 52 Module failed to load 53 Module startup failed 54 Module failed 55 Driver failed ')
vlanRouteTableFull5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,19))
if mibBuilder.loadTexts: vlanRouteTableFull5.setDescription('A vlanRouteTableFull trap occurs when either the IP or IPX route table is full. (discovered on insertion attempt)')
sapTableFull5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,20))
if mibBuilder.loadTexts: sapTableFull5.setDescription('A sapTableFull trap occurs when the IPX SAP table is found to be full on insertion.')
atmSSCOPstate5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,21)).setObjects(("XYLAN-ATM-MIB", "atmxPortSlotIndex"), ("XYLAN-ATM-MIB", "atmxPortPortIndex"))
if mibBuilder.loadTexts: atmSSCOPstate5.setDescription('A atmSSCOPstate trap occurs when the signalling state for the specified physical port changes.')
ilmiState5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,22)).setObjects(("XYLAN-ATM-MIB", "atmxPortSlotIndex"), ("XYLAN-ATM-MIB", "atmxPortPortIndex"), ("XYLAN-ATM-MIB", "atmxPortEnableILMI"))
if mibBuilder.loadTexts: ilmiState5.setDescription('A ilmiState trap occurs when the ILMI state for the specified physical port changes.')
atmConnection5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,23)).setObjects(("XYLAN-ATM-MIB", "atmxVccSlotIndex"), ("XYLAN-ATM-MIB", "atmxVccPortIndex"), ("XYLAN-ATM-MIB", "atmxVccVpi"), ("XYLAN-ATM-MIB", "atmxVccVci"), ("XYLAN-ATM-MIB", "atmxVccAdmStatus"))
if mibBuilder.loadTexts: atmConnection5.setDescription('A atmConnection trap occurs when the specified ATM Vcc is created or deleted.')
atmService5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,24)).setObjects(("XYLAN-ATM-MIB", "atmxServiceSlotIndex"), ("XYLAN-ATM-MIB", "atmxServicePortIndex"), ("XYLAN-ATM-MIB", "atmxServiceNumber"), ("XYLAN-ATM-MIB", "atmxServiceAdmStatus"))
if mibBuilder.loadTexts: atmService5.setDescription('A atmService trap occurs when the specified ATM service is created or deleted>')
dlciNew5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,27)).setObjects(("XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex"), ("XYLAN-FRAME-RELAY-MIB", "frxVcControlPortIndex"), ("XYLAN-FRAME-RELAY-MIB", "frxVcControlDlci"))
if mibBuilder.loadTexts: dlciNew5.setDescription('Frame-Relay Dlci Just Created')
dlciDel5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,28)).setObjects(("XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex"), ("XYLAN-FRAME-RELAY-MIB", "frxVcControlPortIndex"), ("XYLAN-FRAME-RELAY-MIB", "frxVcControlDlci"))
if mibBuilder.loadTexts: dlciDel5.setDescription('Frame-Relay Dlci Just Deleted')
dlciUp5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,29)).setObjects(("XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex"), ("XYLAN-FRAME-RELAY-MIB", "frxVcControlPortIndex"), ("XYLAN-FRAME-RELAY-MIB", "frxVcControlDlci"))
if mibBuilder.loadTexts: dlciUp5.setDescription('Frame-Relay Dlci Just Changed to Active')
dlciDn5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,30)).setObjects(("XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex"), ("XYLAN-FRAME-RELAY-MIB", "frxVcControlPortIndex"), ("XYLAN-FRAME-RELAY-MIB", "frxVcControlDlci"))
if mibBuilder.loadTexts: dlciDn5.setDescription('Frame-Relay Dlci Just Changed to InActive')
portManualForwardingMode5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,31)).setObjects(("XYLAN-PORT-MIB", "vportSlot"), ("XYLAN-PORT-MIB", "vportIF"), ("XYLAN-PORT-MIB", "vportFuncType"), ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
if mibBuilder.loadTexts: portManualForwardingMode5.setDescription('A portManualForwardingMode trap occurs when the specified port is placed into manual mode forwarding as its default setting whenever the port is assigned to a Group that is participating in the IBM spanning tree algorithm.')
fddiCFStateChange5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,32)).setObjects(("FDDI-SMT73-MIB", "fddimibSMTIndex"), ("FDDI-SMT73-MIB", "fddimibSMTCFState"))
if mibBuilder.loadTexts: fddiCFStateChange5.setDescription('A fddiCFStateChange trap occurs when the specified fddi physical port changes from wrap configuration state.')
duplicateIPaddress5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,35)).setObjects(("XYLAN-IP-MIB", "xylanIpAssocAddr"), ("XYLAN-IP-MIB", "xylanIpAssocMac"), ("XYLAN-IP-MIB", "xylanIpAssocSlot"), ("XYLAN-IP-MIB", "xylanIpAssocIntf"), ("XYLAN-IP-MIB", "xylanIpAssocDupMac"), ("XYLAN-IP-MIB", "xylanIpAssocDupSlot"), ("XYLAN-IP-MIB", "xylanIpAssocDupIntf"))
if mibBuilder.loadTexts: duplicateIPaddress5.setDescription('A duplicateIPaddress trap occurs whenever the switch detects a duplicate IP address.')
duplicateMACaddress5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,36)).setObjects(("XYLAN-VLAN-MIB", "vDupMacMac"), ("XYLAN-VLAN-MIB", "vDupMacSlot"), ("XYLAN-VLAN-MIB", "vDupMacIntf"), ("XYLAN-VLAN-MIB", "vDupMacTime"))
if mibBuilder.loadTexts: duplicateMACaddress5.setDescription('A duplicateMACaddress trap occurs whenever the switch detects a duplicate MAC address of one of its own router ports.')
healthThresholdRising5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,37))
if mibBuilder.loadTexts: healthThresholdRising5.setDescription('A healthThresholdRising trap occurs when at least one of the user-specified thresholds is exceeded for the first time.')
healthThresholdFalling5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,38))
if mibBuilder.loadTexts: healthThresholdFalling5.setDescription('A healthThresholdFalling trap occurs when at least one of the user-specified thresholds was exceeded during the previous cycle and none of them are exceeded this cycle.')
healthThresholdDevice5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,39)).setObjects(("XYLAN-HEALTH-MIB", "healthThreshDevTrapData"))
if mibBuilder.loadTexts: healthThresholdDevice5.setDescription('A healthThresholdDevice trap occurs when at least one device-level threshold crossing is detected.')
healthThresholdModule5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,40)).setObjects(("XYLAN-HEALTH-MIB", "healthThreshModTrapCount"), ("XYLAN-HEALTH-MIB", "healthThreshModTrapData"))
if mibBuilder.loadTexts: healthThresholdModule5.setDescription('A healthThresholdModule trap occurs when at least one module-level threshold crossing is detected.')
pnniRouteConflictPort5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,50))
if mibBuilder.loadTexts: pnniRouteConflictPort5.setDescription('This trap occurs when PNNI detects that a static route on the pnnixIfPortId port has been created and this port has been configured as a PNNI port. This is something that may cause misrouting in a PNNI network if the port turns out to be an Inside port.')
pnniRouteConflictSamePG5 = NotificationType((1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1) + (0,51))
if mibBuilder.loadTexts: pnniRouteConflictSamePG5.setDescription('This trap occurs when PNNI detects that a static route on the pnnixIfPortId port has been created and this route matches (a prefix of) the Peer Group ID. This is something that may cause misrouting in a PNNI network.')
mibBuilder.exportSymbols("XYLANTRAP-5-MIB", ilmiState5=ilmiState5, dlciUp5=dlciUp5, portRecordMismatch5=portRecordMismatch5, atmConnection5=atmConnection5, healthThresholdDevice5=healthThresholdDevice5, portLinkUpEvent5=portLinkUpEvent5, portLinkDownEvent5=portLinkDownEvent5, portManualForwardingMode5=portManualForwardingMode5, powerEvent5=powerEvent5, groupChange5=groupChange5, systemEvent5=systemEvent5, atmSSCOPstate5=atmSSCOPstate5, healthThresholdFalling5=healthThresholdFalling5, atmService5=atmService5, pnniRouteConflictSamePG5=pnniRouteConflictSamePG5, pnniRouteConflictPort5=pnniRouteConflictPort5, sapTableFull5=sapTableFull5, healthThresholdRising5=healthThresholdRising5, loginViolation5=loginViolation5, vlanChange5=vlanChange5, moduleChange5=moduleChange5, macDuplicatePort5=macDuplicatePort5, vlanRouteTableFull5=vlanRouteTableFull5, controllerEvent5=controllerEvent5, macVlanViolation5=macVlanViolation5, portPartitioned5=portPartitioned5, fddiCFStateChange5=fddiCFStateChange5, portMove5=portMove5, duplicateIPaddress5=duplicateIPaddress5, dlciDn5=dlciDn5, tempAlarm5=tempAlarm5, healthThresholdModule5=healthThresholdModule5, duplicateMACaddress5=duplicateMACaddress5, moduleResetReload5=moduleResetReload5, dlciDel5=dlciDel5, dlciNew5=dlciNew5)