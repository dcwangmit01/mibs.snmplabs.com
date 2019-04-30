#
# PySNMP MIB module HPN-ICF-IP-ADDRESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-IP-ADDRESS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:27:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter32, Gauge32, MibIdentifier, Bits, ModuleIdentity, Unsigned32, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "Gauge32", "MibIdentifier", "Bits", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "NotificationType", "IpAddress")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
hpnicfIpAddrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67))
hpnicfIpAddrMIB.setRevisions(('2005-11-22 00:00',))
if mibBuilder.loadTexts: hpnicfIpAddrMIB.setLastUpdated('200511220000Z')
if mibBuilder.loadTexts: hpnicfIpAddrMIB.setOrganization('')
hpnicfIpAddressObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1))
hpnicfIpAddressConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1))
hpnicfIpAddrSetTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1), )
if mibBuilder.loadTexts: hpnicfIpAddrSetTable.setStatus('current')
hpnicfIpAddrSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrSetIfIndex"), (0, "HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrSetAddrType"), (0, "HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrSetAddr"))
if mibBuilder.loadTexts: hpnicfIpAddrSetEntry.setStatus('current')
hpnicfIpAddrSetIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpnicfIpAddrSetIfIndex.setStatus('current')
hpnicfIpAddrSetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1, 2), InetAddressType())
if mibBuilder.loadTexts: hpnicfIpAddrSetAddrType.setStatus('current')
hpnicfIpAddrSetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1, 3), InetAddress())
if mibBuilder.loadTexts: hpnicfIpAddrSetAddr.setStatus('current')
hpnicfIpAddrSetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfIpAddrSetMask.setStatus('current')
hpnicfIpAddrSetSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("assignedIp", 1))).clone('assignedIp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfIpAddrSetSourceType.setStatus('current')
hpnicfIpAddrSetCatalog = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("sub", 2))).clone('primary')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfIpAddrSetCatalog.setStatus('current')
hpnicfIpAddrSetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfIpAddrSetRowStatus.setStatus('current')
hpnicfIpAddrReadTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2), )
if mibBuilder.loadTexts: hpnicfIpAddrReadTable.setStatus('current')
hpnicfIpAddrReadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrReadIfIndex"), (0, "HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrReadAddrType"), (0, "HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrReadAddr"))
if mibBuilder.loadTexts: hpnicfIpAddrReadEntry.setStatus('current')
hpnicfIpAddrReadIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpnicfIpAddrReadIfIndex.setStatus('current')
hpnicfIpAddrReadAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2, 1, 2), InetAddressType())
if mibBuilder.loadTexts: hpnicfIpAddrReadAddrType.setStatus('current')
hpnicfIpAddrReadAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2, 1, 3), InetAddress())
if mibBuilder.loadTexts: hpnicfIpAddrReadAddr.setStatus('current')
hpnicfIpAddrReadMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIpAddrReadMask.setStatus('current')
hpnicfIpAddrReadSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("assignedIp", 1), ("cluster", 2), ("dhcp", 3), ("bootp", 4), ("negotiate", 5), ("unnumbered", 6), ("vrrp", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIpAddrReadSourceType.setStatus('current')
hpnicfIpAddrReadCatalog = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("primary", 1), ("sub", 2), ("cluster", 3), ("vrrp", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIpAddrReadCatalog.setStatus('current')
hpnicfIpv4AddrTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 3), )
if mibBuilder.loadTexts: hpnicfIpv4AddrTable.setStatus('current')
hpnicfIpv4AddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfIpv4AddrEntry.setStatus('current')
hpnicfIpv4AddrAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 3, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfIpv4AddrAddr.setStatus('current')
hpnicfIpv4AddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 3, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfIpv4AddrMask.setStatus('current')
hpnicfIpv4AddrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfIpv4AddrRowStatus.setStatus('current')
hpnicfIpAddrNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2))
hpnicfIpAddrNotifyScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 1))
hpnicfIpAddrNotifyIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfIpAddrNotifyIfIndex.setStatus('current')
hpnicfIpAddrOldIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 1, 2), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfIpAddrOldIpAddress.setStatus('current')
hpnicfIpAddrNewIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 1, 3), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfIpAddrNewIpAddress.setStatus('current')
hpnicfIpAddrFirstTrapTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 1, 4), TimeTicks()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfIpAddrFirstTrapTime.setStatus('current')
hpnicfIpAddrNotifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 2))
hpnicfIpAddrNotifyObjectsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 2, 0))
hpnicfIpAddressChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 2, 0, 1)).setObjects(("HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrNotifyIfIndex"), ("HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrOldIpAddress"), ("HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrNewIpAddress"), ("HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrFirstTrapTime"))
if mibBuilder.loadTexts: hpnicfIpAddressChangeNotify.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-IP-ADDRESS-MIB", hpnicfIpAddrSetCatalog=hpnicfIpAddrSetCatalog, hpnicfIpAddrReadEntry=hpnicfIpAddrReadEntry, PYSNMP_MODULE_ID=hpnicfIpAddrMIB, hpnicfIpAddrReadIfIndex=hpnicfIpAddrReadIfIndex, hpnicfIpAddrSetMask=hpnicfIpAddrSetMask, hpnicfIpAddrNotifyObjectsPrefix=hpnicfIpAddrNotifyObjectsPrefix, hpnicfIpAddrReadTable=hpnicfIpAddrReadTable, hpnicfIpAddrNotifyIfIndex=hpnicfIpAddrNotifyIfIndex, hpnicfIpAddrNotify=hpnicfIpAddrNotify, hpnicfIpAddrReadCatalog=hpnicfIpAddrReadCatalog, hpnicfIpAddressObjects=hpnicfIpAddressObjects, hpnicfIpAddrReadSourceType=hpnicfIpAddrReadSourceType, hpnicfIpAddrOldIpAddress=hpnicfIpAddrOldIpAddress, hpnicfIpAddrReadAddrType=hpnicfIpAddrReadAddrType, hpnicfIpAddrSetAddr=hpnicfIpAddrSetAddr, hpnicfIpAddressConfig=hpnicfIpAddressConfig, hpnicfIpAddrReadMask=hpnicfIpAddrReadMask, hpnicfIpAddrSetSourceType=hpnicfIpAddrSetSourceType, hpnicfIpAddrNotifyScalarObjects=hpnicfIpAddrNotifyScalarObjects, hpnicfIpAddrReadAddr=hpnicfIpAddrReadAddr, hpnicfIpAddrSetIfIndex=hpnicfIpAddrSetIfIndex, hpnicfIpv4AddrAddr=hpnicfIpv4AddrAddr, hpnicfIpAddrFirstTrapTime=hpnicfIpAddrFirstTrapTime, hpnicfIpv4AddrEntry=hpnicfIpv4AddrEntry, hpnicfIpv4AddrTable=hpnicfIpv4AddrTable, hpnicfIpAddrSetEntry=hpnicfIpAddrSetEntry, hpnicfIpAddrNotifyObjects=hpnicfIpAddrNotifyObjects, hpnicfIpAddrSetAddrType=hpnicfIpAddrSetAddrType, hpnicfIpAddrNewIpAddress=hpnicfIpAddrNewIpAddress, hpnicfIpv4AddrRowStatus=hpnicfIpv4AddrRowStatus, hpnicfIpAddrSetRowStatus=hpnicfIpAddrSetRowStatus, hpnicfIpv4AddrMask=hpnicfIpv4AddrMask, hpnicfIpAddressChangeNotify=hpnicfIpAddressChangeNotify, hpnicfIpAddrSetTable=hpnicfIpAddrSetTable, hpnicfIpAddrMIB=hpnicfIpAddrMIB)