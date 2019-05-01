#
# PySNMP MIB module AT-LOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-LOG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:30:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter32, Bits, Counter64, ModuleIdentity, Gauge32, Integer32, MibIdentifier, ObjectIdentity, NotificationType, IpAddress, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "Bits", "Counter64", "ModuleIdentity", "Gauge32", "Integer32", "MibIdentifier", "ObjectIdentity", "NotificationType", "IpAddress", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
log = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601))
log.setRevisions(('2012-06-08 00:00', '2012-06-07 00:00', '2011-05-30 00:00', '2011-04-18 00:00', '2010-09-07 00:00', '2010-06-14 05:11', '2008-10-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: log.setRevisionsDescriptions(('Change OCTET STRING to DisplayString for all MIBs.', 'Change the MAX-ACCESS for the logIndex to not-accessible.', 'Updated enumeration type to use INTEGER.', 'Reformatted MIB file.', 'Generic syntax tidy up', 'MIB revision history dates in descriptions updated.', 'Initial revision.',))
if mibBuilder.loadTexts: log.setLastUpdated('201206080000Z')
if mibBuilder.loadTexts: log.setOrganization('Allied Telesis Labs New Zealand')
if mibBuilder.loadTexts: log.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: log.setDescription('The AT Log MIB, for listing log entries from the buffered and permament logs.')
logTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1), )
if mibBuilder.loadTexts: logTable.setStatus('current')
if mibBuilder.loadTexts: logTable.setDescription('A list of log entries from the source specified in the logSource object. The list is ordered from oldest entry to newest entry.')
logEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1), ).setIndexNames((0, "AT-LOG-MIB", "logIndex"))
if mibBuilder.loadTexts: logEntry.setStatus('current')
if mibBuilder.loadTexts: logEntry.setDescription('A log entry from the source specified in the logSource object.')
logIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: logIndex.setStatus('current')
if mibBuilder.loadTexts: logIndex.setDescription('An index value. This index is not directly tied to any specific log entry. Over time, the log will grow larger and eventually older entries will be removed.')
logDate = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logDate.setStatus('current')
if mibBuilder.loadTexts: logDate.setDescription('The date that the log was generated, in the form YYYY MMM DD, eg: 2008 Oct 9.')
logTime = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logTime.setStatus('current')
if mibBuilder.loadTexts: logTime.setDescription('The time that the log was generated, in the form HH:MM:SS, eg: 07:15:04.')
logFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logFacility.setStatus('current')
if mibBuilder.loadTexts: logFacility.setDescription('The syslog facility that generated the log entry. See the Software Reference Manual for more information.')
logSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSeverity.setStatus('current')
if mibBuilder.loadTexts: logSeverity.setDescription('The severity level of the log entry: emerg Emergency, system is unusable alert Action must be taken immediately crit Critical conditions err Error conditions warning Warning conditions notice Normal, but significant, conditions info Informational messages debug Debug-level messages')
logProgram = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logProgram.setStatus('current')
if mibBuilder.loadTexts: logProgram.setDescription('The program that generated the log entry. See the Software Reference Manual for more information.')
logMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logMessage.setStatus('current')
if mibBuilder.loadTexts: logMessage.setDescription('The log message.')
logOptions = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 2))
logSource = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bufferedLog", 1), ("permanentLog", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: logSource.setStatus('current')
if mibBuilder.loadTexts: logSource.setDescription('The source to retrieve the log entries from. Valid values are: 1 - Buffered log 2 - Permanent log This source is used when retrieving the logTable objects, and also specifies the log to be cleared when the clearLog object is set.')
logAll = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: logAll.setStatus('current')
if mibBuilder.loadTexts: logAll.setDescription('Determines the quantity of logs to be retrieved. Valid values are: 0 - Display only recent log messages 1 - Show all available log entries. Note: Choosing to retrieve all log entries may result in a delay of several seconds before they may be viewed via SNMP.')
clearLog = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clearLog.setStatus('current')
if mibBuilder.loadTexts: clearLog.setDescription('Set with a value of 1 to clear the log that is specified by the logSource object.')
mibBuilder.exportSymbols("AT-LOG-MIB", logSource=logSource, logAll=logAll, logDate=logDate, log=log, logTable=logTable, PYSNMP_MODULE_ID=log, logEntry=logEntry, logSeverity=logSeverity, logMessage=logMessage, logOptions=logOptions, logFacility=logFacility, clearLog=clearLog, logTime=logTime, logProgram=logProgram, logIndex=logIndex)