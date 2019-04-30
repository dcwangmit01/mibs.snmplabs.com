#
# PySNMP MIB module Wellfleet-IFWALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-IFWALL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:33:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, ModuleIdentity, Bits, Gauge32, ObjectIdentity, MibIdentifier, iso, IpAddress, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "ModuleIdentity", "Bits", "Gauge32", "ObjectIdentity", "MibIdentifier", "iso", "IpAddress", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfFwallGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfFwallGroup")
wfIFwallIfTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 1), )
if mibBuilder.loadTexts: wfIFwallIfTable.setStatus('obsolete')
wfIFwallIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 1, 1), ).setIndexNames((0, "Wellfleet-IFWALL-MIB", "wfIFwallIfSlot"), (0, "Wellfleet-IFWALL-MIB", "wfIFwallIfPort"))
if mibBuilder.loadTexts: wfIFwallIfEntry.setStatus('obsolete')
wfIFwallIfDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIFwallIfDelete.setStatus('obsolete')
wfIFwallIfDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIFwallIfDisable.setStatus('obsolete')
wfIFwallIfCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIFwallIfCct.setStatus('obsolete')
wfIFwallIfSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIFwallIfSlot.setStatus('obsolete')
wfIFwallIfPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 44))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIFwallIfPort.setStatus('obsolete')
wfIFwallIfLineNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIFwallIfLineNumber.setStatus('obsolete')
wfIFwallIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIFwallIfName.setStatus('obsolete')
wfFwallIntfTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 3), )
if mibBuilder.loadTexts: wfFwallIntfTable.setStatus('mandatory')
wfFwallIntfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 3, 1), ).setIndexNames((0, "Wellfleet-IFWALL-MIB", "wfFwallIntfCct"))
if mibBuilder.loadTexts: wfFwallIntfEntry.setStatus('mandatory')
wfFwallIntfDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("create", 1), ("delete", 2))).clone('create')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFwallIntfDelete.setStatus('mandatory')
wfFwallIntfDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFwallIntfDisable.setStatus('mandatory')
wfFwallIntfCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFwallIntfCct.setStatus('mandatory')
wfFwallIntfName = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFwallIntfName.setStatus('mandatory')
wfFwallIntfPolicyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFwallIntfPolicyIndex.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-IFWALL-MIB", wfFwallIntfName=wfFwallIntfName, wfIFwallIfPort=wfIFwallIfPort, wfFwallIntfDelete=wfFwallIntfDelete, wfFwallIntfCct=wfFwallIntfCct, wfFwallIntfDisable=wfFwallIntfDisable, wfIFwallIfDisable=wfIFwallIfDisable, wfIFwallIfTable=wfIFwallIfTable, wfIFwallIfName=wfIFwallIfName, wfFwallIntfEntry=wfFwallIntfEntry, wfIFwallIfSlot=wfIFwallIfSlot, wfIFwallIfLineNumber=wfIFwallIfLineNumber, wfIFwallIfCct=wfIFwallIfCct, wfFwallIntfTable=wfFwallIntfTable, wfIFwallIfDelete=wfIFwallIfDelete, wfIFwallIfEntry=wfIFwallIfEntry, wfFwallIntfPolicyIndex=wfFwallIntfPolicyIndex)