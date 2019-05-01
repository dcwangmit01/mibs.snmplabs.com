#
# PySNMP MIB module CADANT-CMTS-DNSCLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CADANT-CMTS-DNSCLIENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:44:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
cadLayer3, = mibBuilder.importSymbols("CADANT-PRODUCTS-MIB", "cadLayer3")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, Counter64, TimeTicks, ObjectIdentity, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, NotificationType, ModuleIdentity, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "Counter64", "TimeTicks", "ObjectIdentity", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "NotificationType", "ModuleIdentity", "Counter32", "IpAddress")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
cadDnsClientMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8))
cadDnsClientMib.setRevisions(('2003-07-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cadDnsClientMib.setRevisionsDescriptions(('Added support for default domain name MIB.',))
if mibBuilder.loadTexts: cadDnsClientMib.setLastUpdated('200307140000Z')
if mibBuilder.loadTexts: cadDnsClientMib.setOrganization('Cadant Inc')
if mibBuilder.loadTexts: cadDnsClientMib.setContactInfo('Email: support@cadant.com')
if mibBuilder.loadTexts: cadDnsClientMib.setDescription('This MIB module defines objects to help support the Domain Name Server Client (DNS) in the Cadant CMTS.')
cadDnsClientObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 1))
cadDnsClientEnable = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDnsClientEnable.setStatus('current')
if mibBuilder.loadTexts: cadDnsClientEnable.setDescription('If set to true(1), then DNS client operations should be enabled. Otherwise, DNS client operations are disabled.')
cadDnsClientDefaultDomain = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDnsClientDefaultDomain.setStatus('current')
if mibBuilder.loadTexts: cadDnsClientDefaultDomain.setDescription(' Specifies the default domain name to use for non-FQDN hostname queries.')
cadDnsClientServerTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 2), )
if mibBuilder.loadTexts: cadDnsClientServerTable.setStatus('current')
if mibBuilder.loadTexts: cadDnsClientServerTable.setDescription('')
cadDnsClientServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 2, 1), ).setIndexNames((0, "CADANT-CMTS-DNSCLIENT-MIB", "cadDnsClientServerIpAddr"))
if mibBuilder.loadTexts: cadDnsClientServerEntry.setStatus('current')
if mibBuilder.loadTexts: cadDnsClientServerEntry.setDescription(' Each entry contains a DNS server address. The table has a maximum size of 6 entries.')
cadDnsClientServerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: cadDnsClientServerIpAddr.setStatus('current')
if mibBuilder.loadTexts: cadDnsClientServerIpAddr.setDescription(' The DNS server IP address')
cadDnsClientServerPrefId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadDnsClientServerPrefId.setStatus('current')
if mibBuilder.loadTexts: cadDnsClientServerPrefId.setDescription(' The preference ID of the DNS server. Lower values denote greater preference. The first row created in the table will be assigned a value of 1. Subsequent rows will be assigned a value 1 greater than the largest cadDnsClientServerPrefId currently in use. When a row is deleted from this table, any other rows that have values of cadDnsClientServerPrefId larger than it will all have their values decreased by 1. This ensures the values of cadDnsClientServerPrefId in use always start at 1 and are of monotonically increasing values, thus providing an unambiguous representation of the preference order of each DNS server.')
cadDnsClientServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadDnsClientServerRowStatus.setStatus('current')
if mibBuilder.loadTexts: cadDnsClientServerRowStatus.setDescription(' MIB row control object')
cadDnsClientDomainNameTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 3), )
if mibBuilder.loadTexts: cadDnsClientDomainNameTable.setStatus('current')
if mibBuilder.loadTexts: cadDnsClientDomainNameTable.setDescription('')
cadDnsClientDomainNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 3, 1), ).setIndexNames((0, "CADANT-CMTS-DNSCLIENT-MIB", "cadDnsClientDomainName"))
if mibBuilder.loadTexts: cadDnsClientDomainNameEntry.setStatus('current')
if mibBuilder.loadTexts: cadDnsClientDomainNameEntry.setDescription(' Each entry contains a DNS domain name.')
cadDnsClientDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 3, 1, 1), DisplayString())
if mibBuilder.loadTexts: cadDnsClientDomainName.setStatus('current')
if mibBuilder.loadTexts: cadDnsClientDomainName.setDescription(' The DNS domain name')
cadDnsClientDomainNameRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadDnsClientDomainNameRowStatus.setStatus('current')
if mibBuilder.loadTexts: cadDnsClientDomainNameRowStatus.setDescription(' MIB row control object')
mibBuilder.exportSymbols("CADANT-CMTS-DNSCLIENT-MIB", cadDnsClientDomainNameRowStatus=cadDnsClientDomainNameRowStatus, cadDnsClientDefaultDomain=cadDnsClientDefaultDomain, cadDnsClientServerRowStatus=cadDnsClientServerRowStatus, cadDnsClientServerEntry=cadDnsClientServerEntry, cadDnsClientDomainNameEntry=cadDnsClientDomainNameEntry, cadDnsClientDomainNameTable=cadDnsClientDomainNameTable, cadDnsClientEnable=cadDnsClientEnable, cadDnsClientObjects=cadDnsClientObjects, cadDnsClientDomainName=cadDnsClientDomainName, cadDnsClientServerPrefId=cadDnsClientServerPrefId, PYSNMP_MODULE_ID=cadDnsClientMib, cadDnsClientMib=cadDnsClientMib, cadDnsClientServerTable=cadDnsClientServerTable, cadDnsClientServerIpAddr=cadDnsClientServerIpAddr)