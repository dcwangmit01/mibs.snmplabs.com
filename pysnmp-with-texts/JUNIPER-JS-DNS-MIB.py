#
# PySNMP MIB module JUNIPER-JS-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-JS-DNS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:59:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
jnxJsDnsRoot, = mibBuilder.importSymbols("JUNIPER-JS-SMI", "jnxJsDnsRoot")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, Bits, IpAddress, Counter64, Counter32, Gauge32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Bits", "IpAddress", "Counter64", "Counter32", "Gauge32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "Unsigned32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxJsDns = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 10, 1))
if mibBuilder.loadTexts: jnxJsDns.setLastUpdated('200704141245Z')
if mibBuilder.loadTexts: jnxJsDns.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxJsDns.setContactInfo(' Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net')
if mibBuilder.loadTexts: jnxJsDns.setDescription('This MIB provides collated statistics for the Domain Name System (DNS) proxy collected over all interfaces on which it is configured to serve')
jnxJsDnsProxyDataObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 10, 1, 1))
jnxJsDNSProxyQueriesReceived = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 10, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsDNSProxyQueriesReceived.setStatus('current')
if mibBuilder.loadTexts: jnxJsDNSProxyQueriesReceived.setDescription('Count of total number of DNS queries received by the DNS Proxy.')
jnxJsDnsProxyResponsesSent = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 10, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsDnsProxyResponsesSent.setStatus('current')
if mibBuilder.loadTexts: jnxJsDnsProxyResponsesSent.setDescription('Count of DNS queries answered sent by the DNS Proxy. This includes DNS cache hits and misses that were answered.')
jnxJsDnsProxyQueriesForwarded = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 10, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsDnsProxyQueriesForwarded.setStatus('current')
if mibBuilder.loadTexts: jnxJsDnsProxyQueriesForwarded.setDescription('Count of DNS queries forwarded to other DNS server. This is number of queries that have been proxied due to cache miss.')
jnxJsDnsProxyNegativeResponses = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 10, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsDnsProxyNegativeResponses.setStatus('current')
if mibBuilder.loadTexts: jnxJsDnsProxyNegativeResponses.setDescription('Count of Negative DNS query responses. This is the count of DNS queries that the Proxy could not obtain answers for.')
jnxJsDnsProxyRetryRequests = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 10, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsDnsProxyRetryRequests.setStatus('current')
if mibBuilder.loadTexts: jnxJsDnsProxyRetryRequests.setDescription('Count of DNS retry queries that this proxy received.')
jnxJsDnsProxyPendingRequests = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 10, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsDnsProxyPendingRequests.setStatus('current')
if mibBuilder.loadTexts: jnxJsDnsProxyPendingRequests.setDescription('Count of DNS requests yet to be answered.')
jnxJsDnsProxyServerFailures = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 10, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsDnsProxyServerFailures.setStatus('current')
if mibBuilder.loadTexts: jnxJsDnsProxyServerFailures.setDescription('Count of DNS Proxy Failures.')
mibBuilder.exportSymbols("JUNIPER-JS-DNS-MIB", jnxJsDnsProxyNegativeResponses=jnxJsDnsProxyNegativeResponses, jnxJsDnsProxyServerFailures=jnxJsDnsProxyServerFailures, jnxJsDnsProxyPendingRequests=jnxJsDnsProxyPendingRequests, jnxJsDnsProxyQueriesForwarded=jnxJsDnsProxyQueriesForwarded, jnxJsDnsProxyDataObjects=jnxJsDnsProxyDataObjects, PYSNMP_MODULE_ID=jnxJsDns, jnxJsDns=jnxJsDns, jnxJsDnsProxyResponsesSent=jnxJsDnsProxyResponsesSent, jnxJsDnsProxyRetryRequests=jnxJsDnsProxyRetryRequests, jnxJsDNSProxyQueriesReceived=jnxJsDNSProxyQueriesReceived)