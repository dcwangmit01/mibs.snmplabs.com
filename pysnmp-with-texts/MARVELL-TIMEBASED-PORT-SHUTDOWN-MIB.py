#
# PySNMP MIB module MARVELL-TIMEBASED-PORT-SHUTDOWN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MARVELL-TIMEBASED-PORT-SHUTDOWN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:10:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ObjectIdentity, iso, NotificationType, ModuleIdentity, Counter64, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, TimeTicks, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "iso", "NotificationType", "ModuleIdentity", "Counter64", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "TimeTicks", "Unsigned32", "MibIdentifier")
RowStatus, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString")
rlTimeBasedPort = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 208))
rlTimeBasedPort.setRevisions(('2011-08-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlTimeBasedPort.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: rlTimeBasedPort.setLastUpdated('201108060000Z')
if mibBuilder.loadTexts: rlTimeBasedPort.setOrganization('Marvell Semiconductor, Inc.')
if mibBuilder.loadTexts: rlTimeBasedPort.setContactInfo('www.marvell.com')
if mibBuilder.loadTexts: rlTimeBasedPort.setDescription('The private MIB module definition for Time Based Port Operation MIB.')
rlTimeBasedPortVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 208, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTimeBasedPortVersion.setStatus('current')
if mibBuilder.loadTexts: rlTimeBasedPortVersion.setDescription('This scalar keep current supported version for Time Based Port feature.Initial version value is 1')
rlTimeBasedPortTable = MibTable((1, 3, 6, 1, 4, 1, 89, 208, 2), )
if mibBuilder.loadTexts: rlTimeBasedPortTable.setStatus('current')
if mibBuilder.loadTexts: rlTimeBasedPortTable.setDescription('The table is used to manage time based port operation schedules.')
rlTimeBasedPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 208, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MARVELL-TIMEBASED-PORT-SHUTDOWN-MIB", "rlTimeBasedPortTimeRangeName"))
if mibBuilder.loadTexts: rlTimeBasedPortEntry.setStatus('current')
if mibBuilder.loadTexts: rlTimeBasedPortEntry.setDescription('An entry (conceptual row) in the rlTimeBasedPortEntry.')
rlTimeBasedPortTimeRangeName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 208, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: rlTimeBasedPortTimeRangeName.setStatus('current')
if mibBuilder.loadTexts: rlTimeBasedPortTimeRangeName.setDescription('Name of time range.')
rlTimeBasedPortAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 208, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTimeBasedPortAction.setStatus('current')
if mibBuilder.loadTexts: rlTimeBasedPortAction.setDescription('This field constitutes what action must be applyed to port during the time range.')
rlTimeBasedPortActive = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 208, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTimeBasedPortActive.setStatus('current')
if mibBuilder.loadTexts: rlTimeBasedPortActive.setDescription('This field indicates if the time-range is active or not .')
rlTimeBasedPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 208, 2, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTimeBasedPortRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlTimeBasedPortRowStatus.setDescription('The status of a table entry. It is used to delete an entry from this table.')
mibBuilder.exportSymbols("MARVELL-TIMEBASED-PORT-SHUTDOWN-MIB", rlTimeBasedPortRowStatus=rlTimeBasedPortRowStatus, rlTimeBasedPortVersion=rlTimeBasedPortVersion, rlTimeBasedPortTable=rlTimeBasedPortTable, rlTimeBasedPort=rlTimeBasedPort, rlTimeBasedPortEntry=rlTimeBasedPortEntry, rlTimeBasedPortActive=rlTimeBasedPortActive, rlTimeBasedPortTimeRangeName=rlTimeBasedPortTimeRangeName, PYSNMP_MODULE_ID=rlTimeBasedPort, rlTimeBasedPortAction=rlTimeBasedPortAction)