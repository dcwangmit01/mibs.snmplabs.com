#
# PySNMP MIB module JUNIPER-LSYSSP-NATSRCNOPATAD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-LSYSSP-NATSRCNOPATAD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:00:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
jnxLsysSpNATsrcnopatad, = mibBuilder.importSymbols("JUNIPER-LSYS-SECURITYPROFILE-MIB", "jnxLsysSpNATsrcnopatad")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, TimeTicks, Integer32, Counter32, Bits, MibIdentifier, NotificationType, Unsigned32, ObjectIdentity, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Integer32", "Counter32", "Bits", "MibIdentifier", "NotificationType", "Unsigned32", "ObjectIdentity", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxLsysSpNATsrcnopatadMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1))
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadMIB.setLastUpdated('201005191644Z')
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadMIB.setContactInfo('Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net HTTP://www.juniper.net')
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadMIB.setDescription('This module defines the NAT-src-no-pat-address-specific MIB for Juniper Enterprise Logical-System (LSYS) security profiles. Juniper documentation is recommended as the reference. The LSYS security profile provides various static and dynamic resource management by observing resource quota limits. Security NAT-src-no-pat-address resource is the focus in this MIB. ')
jnxLsysSpNATsrcnopatadObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1))
jnxLsysSpNATsrcnopatadSummary = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2))
jnxLsysSpNATsrcnopatadTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1), )
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadTable.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadTable.setDescription('LSYSPROFILE NAT-src-no-pat-address objects for NAT-src-no-pat- address resource consumption per LSYS.')
jnxLsysSpNATsrcnopatadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1), ).setIndexNames((1, "JUNIPER-LSYSSP-NATSRCNOPATAD-MIB", "jnxLsysSpNATsrcnopatadLsysName"))
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadEntry.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadEntry.setDescription('An entry in NAT-src-no-pat-address resource table.')
jnxLsysSpNATsrcnopatadLsysName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadLsysName.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadLsysName.setDescription('The name of the logical system for which NAT-src-no-pat-address resource information is retrieved. ')
jnxLsysSpNATsrcnopatadProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadProfileName.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadProfileName.setDescription('The security profile name string for the LSYS.')
jnxLsysSpNATsrcnopatadUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadUsage.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadUsage.setDescription('The current resource usage count for the LSYS.')
jnxLsysSpNATsrcnopatadReserved = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadReserved.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadReserved.setDescription('The reserved resource count for the LSYS.')
jnxLsysSpNATsrcnopatadMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadMaximum.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadMaximum.setDescription('The maximum allowed resource usage count for the LSYS.')
jnxLsysSpNATsrcnopatadUsedAmount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadUsedAmount.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadUsedAmount.setDescription('The NAT-src-no-pat-address resource consumption over all LSYS.')
jnxLsysSpNATsrcnopatadMaxQuota = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadMaxQuota.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadMaxQuota.setDescription('The NAT-src-no-pat-address resource maximum quota for the whole device for all LSYS.')
jnxLsysSpNATsrcnopatadAvailableAmount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadAvailableAmount.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadAvailableAmount.setDescription('The NAT-src-no-pat-address resource available in the whole device.')
jnxLsysSpNATsrcnopatadHeaviestUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadHeaviestUsage.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadHeaviestUsage.setDescription('The most amount of NAT-src-no-pat-address resource consumed of a LSYS.')
jnxLsysSpNATsrcnopatadHeaviestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadHeaviestUser.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadHeaviestUser.setDescription('The LSYS name that consume the most NAT-src-no-pat-address resource.')
jnxLsysSpNATsrcnopatadLightestUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadLightestUsage.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadLightestUsage.setDescription('The least amount of NAT-src-no-pat-address resource consumed of a LSYS.')
jnxLsysSpNATsrcnopatadLightestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadLightestUser.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadLightestUser.setDescription('The LSYS name that consume the least NAT-src-no-pat-address resource.')
mibBuilder.exportSymbols("JUNIPER-LSYSSP-NATSRCNOPATAD-MIB", jnxLsysSpNATsrcnopatadReserved=jnxLsysSpNATsrcnopatadReserved, jnxLsysSpNATsrcnopatadSummary=jnxLsysSpNATsrcnopatadSummary, jnxLsysSpNATsrcnopatadLsysName=jnxLsysSpNATsrcnopatadLsysName, jnxLsysSpNATsrcnopatadLightestUsage=jnxLsysSpNATsrcnopatadLightestUsage, jnxLsysSpNATsrcnopatadMaximum=jnxLsysSpNATsrcnopatadMaximum, jnxLsysSpNATsrcnopatadAvailableAmount=jnxLsysSpNATsrcnopatadAvailableAmount, PYSNMP_MODULE_ID=jnxLsysSpNATsrcnopatadMIB, jnxLsysSpNATsrcnopatadHeaviestUsage=jnxLsysSpNATsrcnopatadHeaviestUsage, jnxLsysSpNATsrcnopatadLightestUser=jnxLsysSpNATsrcnopatadLightestUser, jnxLsysSpNATsrcnopatadObjects=jnxLsysSpNATsrcnopatadObjects, jnxLsysSpNATsrcnopatadMIB=jnxLsysSpNATsrcnopatadMIB, jnxLsysSpNATsrcnopatadEntry=jnxLsysSpNATsrcnopatadEntry, jnxLsysSpNATsrcnopatadUsage=jnxLsysSpNATsrcnopatadUsage, jnxLsysSpNATsrcnopatadMaxQuota=jnxLsysSpNATsrcnopatadMaxQuota, jnxLsysSpNATsrcnopatadTable=jnxLsysSpNATsrcnopatadTable, jnxLsysSpNATsrcnopatadHeaviestUser=jnxLsysSpNATsrcnopatadHeaviestUser, jnxLsysSpNATsrcnopatadProfileName=jnxLsysSpNATsrcnopatadProfileName, jnxLsysSpNATsrcnopatadUsedAmount=jnxLsysSpNATsrcnopatadUsedAmount)