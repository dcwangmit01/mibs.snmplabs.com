#
# PySNMP MIB module ALCATEL-IND1-MAC-ADDRESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-MAC-ADDRESS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:18:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1MacAddress, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1MacAddress")
vlanNumber, = mibBuilder.importSymbols("ALCATEL-IND1-VLAN-MGR-MIB", "vlanNumber")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
dot1qVlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qVlanIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, ObjectIdentity, iso, IpAddress, Gauge32, NotificationType, Counter32, ModuleIdentity, Integer32, MibIdentifier, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "ObjectIdentity", "iso", "IpAddress", "Gauge32", "NotificationType", "Counter32", "ModuleIdentity", "Integer32", "MibIdentifier", "TimeTicks", "Bits")
MacAddress, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "RowStatus", "DisplayString")
alcatelIND1MacAddressMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1))
alcatelIND1MacAddressMIB.setRevisions(('2010-05-13 00:00', '2007-04-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alcatelIND1MacAddressMIB.setRevisionsDescriptions(('Fixed the Notifications to use MIB Module OID.0 as Notifications root.', 'The MIB module for Source Learning Mac Address entity.',))
if mibBuilder.loadTexts: alcatelIND1MacAddressMIB.setLastUpdated('201005130000Z')
if mibBuilder.loadTexts: alcatelIND1MacAddressMIB.setOrganization('Alcatel-Lucent, Enterprise Solutions Division')
if mibBuilder.loadTexts: alcatelIND1MacAddressMIB.setContactInfo('Please consult with Customer Service to ensure the most appropriate version of this document is used with the products in question: Alcatel-Lucent, Enterprise Solutions Division (Formerly Alcatel Internetworking, Incorporated) 26801 West Agoura Road Agoura Hills, CA 91301-5122 United States Of America Telephone: North America +1 800 995 2696 Latin America +1 877 919 9526 Europe +31 23 556 0100 Asia +65 394 7933 All Other +1 818 878 4507 Electronic Mail: support@ind.alcatel.com World Wide Web: http://alcatel-lucent.com/wps/portal/enterprise File Transfer Protocol: ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1MacAddressMIB.setDescription('This module describes an authoritative enterprise-specific Simple Network Management Protocol (SNMP) Management Information Base (MIB): For the Birds Of Prey Product Line, this is the MIB module for address learning mac addresses entity. The right to make changes in specification and other information contained in this document without prior notice is reserved. No liability shall be assumed for any incidental, indirect, special, or consequential damages whatsoever arising from or related to this document or the information contained herein. Vendors, end-users, and other interested parties are granted non-exclusive license to use this specification in connection with management of the products for which it is intended to be used. Copyright (C) 1995-2007 Alcatel-Lucent ALL RIGHTS RESERVED WORLDWIDE')
alcatelIND1MacAddressMIBNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 0))
if mibBuilder.loadTexts: alcatelIND1MacAddressMIBNotifications.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1MacAddressMIBNotifications.setDescription('Branch For MacAddress MIB Subsystem Notifications.')
alcatelIND1MacAddressMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1))
if mibBuilder.loadTexts: alcatelIND1MacAddressMIBObjects.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1MacAddressMIBObjects.setDescription('Branch For Source Learning Module MIB Subsystem Managed Objects.')
alcatelIND1MacAddressMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 2))
if mibBuilder.loadTexts: alcatelIND1MacAddressMIBConformance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1MacAddressMIBConformance.setDescription('Branch for Source Learning Module MIB Subsystem Conformance Information.')
alcatelIND1MacAddressMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1MacAddressMIBGroups.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1MacAddressMIBGroups.setDescription('Branch for Source Learning Module MIB Subsystem Units of Conformance.')
alcatelIND1MacAddressMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1MacAddressMIBCompliances.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1MacAddressMIBCompliances.setDescription('Branch for Source Learning Module MIB Subsystem Compliance Statements.')
class MacAddressProtocolType(TextualConvention, Integer32):
    description = 'Protocol value should be displayed in hex format'
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

slMacAddressAgingTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 2), )
if mibBuilder.loadTexts: slMacAddressAgingTable.setStatus('current')
if mibBuilder.loadTexts: slMacAddressAgingTable.setDescription('Definition of the timeout for those learned mac addresses and configured as deleted_on_timeout addresses.')
slMacAddressAgingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 2, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: slMacAddressAgingEntry.setStatus('current')
if mibBuilder.loadTexts: slMacAddressAgingEntry.setDescription('Information about the aging time for some specific vlan. For creation of the aging time, If the vlan Id is specified, then the aging time value will be applied to those mac addresses in that vlan. Otherwise, the aging time will be applied to all of the mac addresses throughout the vlans.')
slMacAgingValue = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 1000000)).clone(300)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slMacAgingValue.setStatus('current')
if mibBuilder.loadTexts: slMacAgingValue.setDescription('This object indicates the value of mac address aging time.')
slMacAgingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slMacAgingRowStatus.setStatus('current')
if mibBuilder.loadTexts: slMacAgingRowStatus.setDescription('Row Status for creating/deleting the aging time.')
slDistributedMacMode = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slDistributedMacMode.setStatus('current')
if mibBuilder.loadTexts: slDistributedMacMode.setDescription('Enable/Disable Distributed MAC Mode. When changed, the user must save the current configuration and reboot the switch for change to take effect.')
slMacLearningControlTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 7), )
if mibBuilder.loadTexts: slMacLearningControlTable.setStatus('current')
if mibBuilder.loadTexts: slMacLearningControlTable.setDescription('This table provides the control information about the mac learning on ports')
slMacLearningControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 7, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: slMacLearningControlEntry.setStatus('current')
if mibBuilder.loadTexts: slMacLearningControlEntry.setDescription('This table provides the control information about the mac learning on ports')
slMacLearningControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slMacLearningControlStatus.setStatus('current')
if mibBuilder.loadTexts: slMacLearningControlStatus.setDescription('Status of mac learning on port.')
slMacLearningVlanControlTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 10), )
if mibBuilder.loadTexts: slMacLearningVlanControlTable.setStatus('current')
if mibBuilder.loadTexts: slMacLearningVlanControlTable.setDescription('This table provides the control information about the mac learning on ports')
slMacLearningVlanControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 10, 1), ).setIndexNames((0, "ALCATEL-IND1-VLAN-MGR-MIB", "vlanNumber"))
if mibBuilder.loadTexts: slMacLearningVlanControlEntry.setStatus('current')
if mibBuilder.loadTexts: slMacLearningVlanControlEntry.setDescription('This table provides the control information about the mac learning on ports')
slMacLearningVlanControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slMacLearningVlanControlStatus.setStatus('current')
if mibBuilder.loadTexts: slMacLearningVlanControlStatus.setDescription('Status of mac learning on port.')
alaSlMacAddressGlobalTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8), )
if mibBuilder.loadTexts: alaSlMacAddressGlobalTable.setStatus('current')
if mibBuilder.loadTexts: alaSlMacAddressGlobalTable.setDescription('This table contains MAC addresses from both Vlan, VPLS, SPBM or EVB domain. This table contains source addresses which can be configured as permanent (not aged out), delete on reset, delete on timeout in the MAC address table, and those dynamic learned addresses which can be viewed and deleted.')
alaSlMacAddressGlobalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1), ).setIndexNames((0, "ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacDomain"), (0, "ALCATEL-IND1-MAC-ADDRESS-MIB", "slLocaleType"), (0, "ALCATEL-IND1-MAC-ADDRESS-MIB", "slOriginId"), (0, "ALCATEL-IND1-MAC-ADDRESS-MIB", "slServiceId"), (0, "ALCATEL-IND1-MAC-ADDRESS-MIB", "slSubId"), (0, "ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAddressGbl"))
if mibBuilder.loadTexts: alaSlMacAddressGlobalEntry.setStatus('current')
if mibBuilder.loadTexts: alaSlMacAddressGlobalEntry.setDescription('Defninition of the Mac Addresses entries for which the switch has information. For creation of a Mac Address in VLAN domain, the following fields in slMacAddressGlobalEntry are required: slMacDomain slOriginId - IfIndex slServiceId - Vlan ID slMacAddressGbl slMacAddressGblManagement slMacAddressGblDisposition slMacAddressGblRowStatus: must be set last Dynamic mac addresses can not be created manually. For creation of Mac Address in VPLS domain, following fields in alaSlMacAddressGlobalEntry are required: slMacDomain slLocaleType - SAP/sBind slServiceId - VPLS Service ID slOriginId - SAP - PortId; sBind - SDPID slSubId - SAP - VlanId; sBind - VcID slMacAddressGbl slMacAddressGblRowStatus: must be set last Dynamic mac addresses can not be created manually. For creation of Mac Address in SPBM domain, following fields in alaSlMacAddressGlobalEntry are required: slMacDomain slLocaleType - SAP/sBind slServiceId - SPBM Service ID slSvcISID - SPBM I-SID Service Identifier slOriginId - SAP - PortId; sBind - SDPID slSubId - SAP - VlanId; sBind - VcID slMacAddressGbl slMacAddressGblRowStatus: must be set last Dynamic mac addresses can not be created manually. For creation of Mac Address in EVB domain, following fields in alaSlMacAddressGlobalEntry are required: slMacDomain slLocaleType - SAP slServiceId - SPBM Service ID slSvcISID - SPBM I-SID Service Identifier slOriginId - SAP - PortId; slSubId - SAP - VlanId; slMacAddressGbl slMacAddressGblRowStatus: must be set last Dynamic mac addresses can not be created manually. For deletion of a Mac Address in VLAN domain, the following fields in alaSlMacAddressGlobalEntry are required: slMacDomain slOriginId - IfIndex slServiceId - Vlan ID slMacAddressGbl slMacAddressGblManagement slMacAddressGblRowStatus: must be set last For deletion of a Mac Address in VPLS based, following fileds in alaSlMacAddressGlobalEntry are required: slMacDomain slLocaleType - SAP/sBind slServiceId - VPLS Service ID slOriginId - SAP - PortId; sBind - SDPID slSubId - SAP - VlanId; sBind - VcID slMacAddressGbl slMacAddressGblRowStatus: must be set last For deletion of a Mac Address in SPBM based, following fileds in alaSlMacAddressGlobalEntry are required: slMacDomain slLocaleType - SAP/sBind slServiceId - VPLS Service ID slSvcISID - SPBM I-SID Service Identifier slOriginId - SAP - PortId; sBind - SDPID slSubId - SAP - VlanId; sBind - VcID slMacAddressGbl slMacAddressGblRowStatus: must be set last For deletion of a Mac Address in EVB based, following fileds in alaSlMacAddressGlobalEntry are required: slMacDomain slLocaleType - SAP slServiceId - VPLS Service ID slSvcISID - SPBM I-SID Service Identifier slOriginId - SAP - PortId; slSubId - SAP - VlanId; slMacAddressGbl slMacAddressGblRowStatus: must be set last ')
slMacDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("all", 0), ("vlan", 1), ("vpls", 2), ("spbm", 3), ("evb", 4))).clone('all'))
if mibBuilder.loadTexts: slMacDomain.setStatus('current')
if mibBuilder.loadTexts: slMacDomain.setDescription('* This object indicates whether this MAC is learned on Vlan, VPLS, SPBM, EVB domain. * To flush a MAC or MACs, this field may or may not be specified. If this field is not specified, then the default -all(0)- value will be expected; * To program a static MAC address, this field must be specified with values other than -all(0)-')
slLocaleType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("default", 0), ("sap", 1), ("sBind", 2))).clone('default'))
if mibBuilder.loadTexts: slLocaleType.setStatus('current')
if mibBuilder.loadTexts: slLocaleType.setDescription('* This field is used in VPLS, SPBM or EVB domain. This field will be -default(0)- for VLAN domain. * To flush a MAC or MACs, this field may or may not be specified. If this field is not specified, then the -default(0)- value will be expected; * To program a MAC address on Vlan domain, this field will be -default(0)-; To program a MAC address on non VLAN domain, this field must be specfied with values other than -default(0)-')
slOriginId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), )))
if mibBuilder.loadTexts: slOriginId.setStatus('current')
if mibBuilder.loadTexts: slOriginId.setDescription('* This field should be ifIndex for MAC address from Vlan domain, and also ifindex for SAP from VPLS, SPBM & EVB, domain; * This field should be the SDP_ID for MAC address from sBind of VPLS and SPBM domain; * To flush a MAC or MACs, this field may or may not be specified. If this field is not specified, then value `0` will be expected; * To program a static MAC address, this field must be specified with values within the range (1..2147483647) spcified')
slServiceId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32767), )))
if mibBuilder.loadTexts: slServiceId.setStatus('current')
if mibBuilder.loadTexts: slServiceId.setDescription(' * This field should be the VLAN ID for MAC learnt from VLAN domain; * This field should be the Service ID for MAC learnt from VPLS, SPB, and EVB domain; * To flush a MAC or MACs, this field may or may not be specified. If this field is not specified, then value `0` will be expected; * To program a static MAC address, this field must be specified with values within the range (1..32767) spcified')
slSubId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: slSubId.setStatus('current')
if mibBuilder.loadTexts: slSubId.setDescription(' * This field is used in VPLS, SPBM, and EVB domain only. This field should be the EncapId for SAP, and VCID for SBIND. * If this MAC is from SAP, then this field should be the VLANID (1 ..4096); * If this MAC is from SDP, then this field should be the SvcId (1 .. 32767); * Since we may need to support QinQ (OVlan and IVlan), this field will be partitioned into 2 16 bits values, upper 16 bits will be Ovlan and lower 16 bits will be IVlan. If neither OVlan or IVlan is specified, then 0xFFFF will be expected. * To flush a MAC or MACs, this field may or may not be specified. If this field is not specified, then value `0` will be expected; * To program a static MAC address, this field must be specified with values within range specified')
slMacAddressGbl = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 6), MacAddress())
if mibBuilder.loadTexts: slMacAddressGbl.setStatus('current')
if mibBuilder.loadTexts: slMacAddressGbl.setDescription(' * The MAC address for this entry. * To flush a MAC or MACs, this field may or may not be specified. If this field is not specified, then value `FF:FF:FF:FF:FF:FF` will be expected, then all MAC addresses will be flushed. * To program a static MAC address, this field must be specified * with valid MAC address')
slMacAddressGblManagement = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("permanent", 1), ("deleteOnReset", 2), ("deleteOnTimeout", 3), ("learned", 4), ("staticMulticast", 5))).clone('permanent')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slMacAddressGblManagement.setStatus('current')
if mibBuilder.loadTexts: slMacAddressGblManagement.setDescription('This object indicates the management of this entry. permanent(1) - this entry is currently in use and will remain so after the user removing this entry. deleteOnReset(2) - this entry is currently in use and will remain so until the next reset of the bridge. deleteOnTimeout(3) - this entry is currently in use and will remain so until it is aged out. learned(4) - this entry is currently in use and will remain so until it is aged out. staticMulticast(5) - this entry is only applicable to multicast destination addresses')
slMacAddressGblDisposition = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("bridging", 1), ("filtering", 2), ("quarantined", 3), ("hostIntegrity", 4), ("userNetworkProf", 5))).clone('bridging')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slMacAddressGblDisposition.setStatus('current')
if mibBuilder.loadTexts: slMacAddressGblDisposition.setDescription('This object indicates the disposition of the entry. bridging(1) - this entry is currently in use for bridging. filtering(2) - this entry is currently in use for filtering. quarantined(3) - this entry is currently in use for quarantined mac. hostIntegritycheck(4) - the entry is currently under host integrity checking. userNetworkProf(5) - the entry is currently under user network profile Qos. ')
slMacAddressGblRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slMacAddressGblRowStatus.setStatus('current')
if mibBuilder.loadTexts: slMacAddressGblRowStatus.setDescription('Row Status for creating/deleting the mac address.')
slMacAddressGblProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 10), MacAddressProtocolType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slMacAddressGblProtocol.setStatus('current')
if mibBuilder.loadTexts: slMacAddressGblProtocol.setDescription('This object indicates the protocol associated with a mac address.')
slMacAddressGblGroupField = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 11), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slMacAddressGblGroupField.setStatus('current')
if mibBuilder.loadTexts: slMacAddressGblGroupField.setDescription(' ')
slSvcISID = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(256, 16777214), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slSvcISID.setStatus('current')
if mibBuilder.loadTexts: slSvcISID.setDescription(' * This field is used in SPBM domain only. This field should be the ISID ID of MAC learnt in SPBM domain; * To flush a MAC or MACs, this field may or may not be specified. If this field is not specified, then value `-1` will be expected; * To program a static MAC address, this field may or may not sepcified as well. If not specified, then value `0` will be expected; If this field is specified, then the values must be within the range (256..16777214)')
alcatelIND1MacAddressMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAddressGroup"), ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAgingGroup"), ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacGeneralGroup"), ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacLearningGroup"), ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacVlanLearningGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1MacAddressMIBCompliance = alcatelIND1MacAddressMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1MacAddressMIBCompliance.setDescription('Compliance statement for source learning.')
slMacAddressGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAddressGblManagement"), ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAddressGblDisposition"), ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAddressGblRowStatus"), ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAddressGblProtocol"), ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAddressGblGroupField"), ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slSvcISID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    slMacAddressGroup = slMacAddressGroup.setStatus('current')
if mibBuilder.loadTexts: slMacAddressGroup.setDescription('Collection of objects for management of source learning Mac addresses.')
slMacAgingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAgingValue"), ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAgingRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    slMacAgingGroup = slMacAgingGroup.setStatus('current')
if mibBuilder.loadTexts: slMacAgingGroup.setDescription('Collection of objects for management of source learning Mac addresses aging-time.')
slMacGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 2, 1, 3)).setObjects(("ALCATEL-IND1-MAC-ADDRESS-MIB", "slDistributedMacMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    slMacGeneralGroup = slMacGeneralGroup.setStatus('current')
if mibBuilder.loadTexts: slMacGeneralGroup.setDescription('Collection of general sl objects.')
slMacLearningGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 2, 1, 4)).setObjects(("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacLearningControlStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    slMacLearningGroup = slMacLearningGroup.setStatus('current')
if mibBuilder.loadTexts: slMacLearningGroup.setDescription('Collection of objects for management of enabling or disabling source learning on the ports.')
slMacVlanLearningGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 2, 1, 5)).setObjects(("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacLearningVlanControlStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    slMacVlanLearningGroup = slMacVlanLearningGroup.setStatus('current')
if mibBuilder.loadTexts: slMacVlanLearningGroup.setDescription('Collection of objects for management of enabling or disabling source learning on the vlans.')
mibBuilder.exportSymbols("ALCATEL-IND1-MAC-ADDRESS-MIB", slMacLearningControlTable=slMacLearningControlTable, slMacAddressGblDisposition=slMacAddressGblDisposition, alaSlMacAddressGlobalEntry=alaSlMacAddressGlobalEntry, slMacVlanLearningGroup=slMacVlanLearningGroup, slMacLearningVlanControlTable=slMacLearningVlanControlTable, slMacAddressGblManagement=slMacAddressGblManagement, alaSlMacAddressGlobalTable=alaSlMacAddressGlobalTable, slMacAgingRowStatus=slMacAgingRowStatus, slLocaleType=slLocaleType, slMacAddressGbl=slMacAddressGbl, slSvcISID=slSvcISID, alcatelIND1MacAddressMIBObjects=alcatelIND1MacAddressMIBObjects, slMacAddressGblRowStatus=slMacAddressGblRowStatus, slMacGeneralGroup=slMacGeneralGroup, alcatelIND1MacAddressMIBNotifications=alcatelIND1MacAddressMIBNotifications, alcatelIND1MacAddressMIBCompliances=alcatelIND1MacAddressMIBCompliances, slMacAddressAgingEntry=slMacAddressAgingEntry, alcatelIND1MacAddressMIB=alcatelIND1MacAddressMIB, slSubId=slSubId, slOriginId=slOriginId, alcatelIND1MacAddressMIBCompliance=alcatelIND1MacAddressMIBCompliance, slMacLearningVlanControlStatus=slMacLearningVlanControlStatus, slMacAgingValue=slMacAgingValue, PYSNMP_MODULE_ID=alcatelIND1MacAddressMIB, slMacLearningVlanControlEntry=slMacLearningVlanControlEntry, slMacAddressGblGroupField=slMacAddressGblGroupField, slMacDomain=slMacDomain, slMacLearningGroup=slMacLearningGroup, slMacLearningControlEntry=slMacLearningControlEntry, slMacAddressGblProtocol=slMacAddressGblProtocol, MacAddressProtocolType=MacAddressProtocolType, slMacLearningControlStatus=slMacLearningControlStatus, alcatelIND1MacAddressMIBConformance=alcatelIND1MacAddressMIBConformance, slServiceId=slServiceId, slMacAddressGroup=slMacAddressGroup, slDistributedMacMode=slDistributedMacMode, alcatelIND1MacAddressMIBGroups=alcatelIND1MacAddressMIBGroups, slMacAgingGroup=slMacAgingGroup, slMacAddressAgingTable=slMacAddressAgingTable)