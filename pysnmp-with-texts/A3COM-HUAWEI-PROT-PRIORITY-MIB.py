#
# PySNMP MIB module A3COM-HUAWEI-PROT-PRIORITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-PROT-PRIORITY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:06:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, Unsigned32, Integer32, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter32, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "Integer32", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter32", "Gauge32", "Bits")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
h3cProtocolPriority = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37))
h3cProtocolPriority.setRevisions(('2005-01-17 16:33',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cProtocolPriority.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: h3cProtocolPriority.setLastUpdated('200501171633Z')
if mibBuilder.loadTexts: h3cProtocolPriority.setOrganization('Huawei 3Com Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cProtocolPriority.setContactInfo('Platform Team Huawei 3Com Technologies Co., Ltd. Hai-Dian District Beijing P.R. China http://www.huawei-3com.com Zip:100085 ')
if mibBuilder.loadTexts: h3cProtocolPriority.setDescription('This MIB is used to manage and configure the priority of specified protocol. This MIB is applicable to routers, switches and other products. ')
h3cProtocolPriorityObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1))
h3cPPri = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1, 1))
h3cProtocolPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1, 1, 1), )
if mibBuilder.loadTexts: h3cProtocolPriorityTable.setStatus('current')
if mibBuilder.loadTexts: h3cProtocolPriorityTable.setDescription('A table is used to configure the priority of the protocol.')
h3cProtocolPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-PROT-PRIORITY-MIB", "h3cPPriProtocolType"))
if mibBuilder.loadTexts: h3cProtocolPriorityEntry.setStatus('current')
if mibBuilder.loadTexts: h3cProtocolPriorityEntry.setDescription('An entry containing information about the priority of the protocol.')
h3cPPriProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ospf", 1), ("telnet", 2), ("snmp", 3), ("icmp", 4), ("bgp", 5), ("ldp", 6))))
if mibBuilder.loadTexts: h3cPPriProtocolType.setStatus('current')
if mibBuilder.loadTexts: h3cPPriProtocolType.setDescription('Protocol type.')
h3cPPriPriorityType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipPrecedence", 1), ("dscp", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cPPriPriorityType.setStatus('current')
if mibBuilder.loadTexts: h3cPPriPriorityType.setDescription('Priority type.')
h3cPPriPriorityVlaue = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cPPriPriorityVlaue.setStatus('current')
if mibBuilder.loadTexts: h3cPPriPriorityVlaue.setDescription('Priority value. If setting h3cPPriPriorityType to ip-precedence(1), the range of h3cPPriPriorityVlaue is from 0 to 7. If setting h3cPPriPriorityType to dscp(2), the range of h3cPPriPriorityVlaue is from 0 to 63.')
h3cPPriRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cPPriRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cPPriRowStatus.setDescription('RowStatus, Now support createAndGo,active and destroy. To create a new row, h3cPPriPriorityType and h3cPPriPriorityValue must be specified. To modify a row,h3cPPriPriorityType and h3cPPriPriorityValue must change at the same time and the h3cPPriRowStatus is active .')
mibBuilder.exportSymbols("A3COM-HUAWEI-PROT-PRIORITY-MIB", h3cProtocolPriorityObjects=h3cProtocolPriorityObjects, h3cPPriPriorityVlaue=h3cPPriPriorityVlaue, h3cPPriRowStatus=h3cPPriRowStatus, h3cProtocolPriorityTable=h3cProtocolPriorityTable, h3cPPriPriorityType=h3cPPriPriorityType, h3cProtocolPriorityEntry=h3cProtocolPriorityEntry, h3cPPriProtocolType=h3cPPriProtocolType, h3cPPri=h3cPPri, PYSNMP_MODULE_ID=h3cProtocolPriority, h3cProtocolPriority=h3cProtocolPriority)