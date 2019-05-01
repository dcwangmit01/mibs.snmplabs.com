#
# PySNMP MIB module UCD-SNMP-MIB-OLD (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/UCD-SNMP-MIB-OLD
# Produced by pysmi-0.3.4 at Wed May  1 15:28:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, NotificationType, ObjectIdentity, IpAddress, Integer32, MibIdentifier, TimeTicks, Counter64, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "NotificationType", "ObjectIdentity", "IpAddress", "Integer32", "MibIdentifier", "TimeTicks", "Counter64", "Counter32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ucdavis, = mibBuilder.importSymbols("UCD-SNMP-MIB", "ucdavis")
processes = MibTable((1, 3, 6, 1, 4, 1, 2021, 1), ).setIndexNames((0, "UCD-SNMP-MIB-OLD", "processIndex"))
if mibBuilder.loadTexts: processes.setStatus('mandatory')
if mibBuilder.loadTexts: processes.setDescription('A set of information on running programs/daemons.')
processIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: processIndex.setStatus('mandatory')
if mibBuilder.loadTexts: processIndex.setDescription('Reference Index for each observed process.')
processNames = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: processNames.setStatus('mandatory')
if mibBuilder.loadTexts: processNames.setDescription("The table of process names we're Counting.")
processMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: processMin.setStatus('mandatory')
if mibBuilder.loadTexts: processMin.setDescription('The minimum number of processes that should be running. An error flag is generated if the number of running processes is < the minimum.')
processMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: processMax.setStatus('mandatory')
if mibBuilder.loadTexts: processMax.setDescription('The maximum number of processes that should be running. An error flag is generated if the number of running processes is > the maximum.')
processCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: processCount.setStatus('mandatory')
if mibBuilder.loadTexts: processCount.setDescription('The number of current processes running with the name in question.')
processErrorFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 1, 100), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: processErrorFlag.setStatus('mandatory')
if mibBuilder.loadTexts: processErrorFlag.setDescription('A Error flag to indicate trouble with a process. It goes to 1 if there is an error, 0 if no error.')
processErrMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 1, 101), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: processErrMessage.setStatus('mandatory')
if mibBuilder.loadTexts: processErrMessage.setDescription('An error message describing the problem (if one exists).')
processErrFix = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 1, 102), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: processErrFix.setStatus('mandatory')
if mibBuilder.loadTexts: processErrFix.setDescription('Setting this to one will try to fix the problem if possible.')
extensible = MibTable((1, 3, 6, 1, 4, 1, 2021, 3), ).setIndexNames((0, "UCD-SNMP-MIB-OLD", "extensibleIndex"))
if mibBuilder.loadTexts: extensible.setStatus('mandatory')
if mibBuilder.loadTexts: extensible.setDescription('Extensible commands returning output and result codes.')
extensibleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extensibleIndex.setStatus('mandatory')
if mibBuilder.loadTexts: extensibleIndex.setDescription('Reference Index for extensible calls.')
extensibleNames = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 3, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extensibleNames.setStatus('mandatory')
if mibBuilder.loadTexts: extensibleNames.setDescription('Short, one name descriptions of the extensible commands.')
extensibleCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 3, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extensibleCommand.setStatus('mandatory')
if mibBuilder.loadTexts: extensibleCommand.setDescription('The command line to be executed.')
extensibleResult = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 3, 100), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extensibleResult.setStatus('mandatory')
if mibBuilder.loadTexts: extensibleResult.setDescription('The result code from the executed command.')
extensibleOutput = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 3, 101), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extensibleOutput.setStatus('mandatory')
if mibBuilder.loadTexts: extensibleOutput.setDescription('The output of the extensible command (top line only).')
extensibleErrFix = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 3, 102), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extensibleErrFix.setStatus('mandatory')
if mibBuilder.loadTexts: extensibleErrFix.setDescription('Set to 1 to fix the problem, if possible.')
disk = MibTable((1, 3, 6, 1, 4, 1, 2021, 6), ).setIndexNames((0, "UCD-SNMP-MIB-OLD", "diskIndex"))
if mibBuilder.loadTexts: disk.setStatus('mandatory')
if mibBuilder.loadTexts: disk.setDescription('Disk watching information.')
diskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIndex.setStatus('mandatory')
if mibBuilder.loadTexts: diskIndex.setDescription('Reference number for the Disk Mib.')
diskPath = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 6, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPath.setStatus('mandatory')
if mibBuilder.loadTexts: diskPath.setDescription('Path where disk is mounted.')
diskDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 6, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskDevice.setStatus('mandatory')
if mibBuilder.loadTexts: diskDevice.setDescription('Device path')
diskMinimum = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 6, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskMinimum.setStatus('mandatory')
if mibBuilder.loadTexts: diskMinimum.setDescription('Minimum space required on the disk.')
diskMinPercent = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 6, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskMinPercent.setStatus('mandatory')
if mibBuilder.loadTexts: diskMinPercent.setDescription('Minimum percentage of space required on the disk.')
diskTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 6, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskTotal.setStatus('mandatory')
if mibBuilder.loadTexts: diskTotal.setDescription('Total Disk Size (kbytes)')
diskAvail = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 6, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskAvail.setStatus('mandatory')
if mibBuilder.loadTexts: diskAvail.setDescription('Available disk Space')
diskUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 6, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskUsed.setStatus('mandatory')
if mibBuilder.loadTexts: diskUsed.setDescription('Used Space on Disk')
diskPercent = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 6, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPercent.setStatus('mandatory')
if mibBuilder.loadTexts: diskPercent.setDescription('Percentage of space used on disk')
diskErrorFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 6, 100), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskErrorFlag.setStatus('mandatory')
if mibBuilder.loadTexts: diskErrorFlag.setDescription('Error flag signaling disk is over minimum required space')
diskErrorMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 6, 101), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskErrorMsg.setStatus('mandatory')
if mibBuilder.loadTexts: diskErrorMsg.setDescription('A text description of what caused the error flag to be set.')
loadaves = MibTable((1, 3, 6, 1, 4, 1, 2021, 7), ).setIndexNames((0, "UCD-SNMP-MIB-OLD", "loadaveIndex"))
if mibBuilder.loadTexts: loadaves.setStatus('mandatory')
if mibBuilder.loadTexts: loadaves.setDescription('Load average information.')
loadaveIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 7, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loadaveIndex.setStatus('mandatory')
if mibBuilder.loadTexts: loadaveIndex.setDescription('Reference Index for each observed loadave.')
loadaveNames = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 7, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: loadaveNames.setStatus('mandatory')
if mibBuilder.loadTexts: loadaveNames.setDescription("The list of loadave names we're Counting.")
loadaveLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 7, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loadaveLoad.setStatus('mandatory')
if mibBuilder.loadTexts: loadaveLoad.setDescription('The 1,5 and 10 minute load averages.')
loadaveConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 7, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loadaveConfig.setStatus('mandatory')
if mibBuilder.loadTexts: loadaveConfig.setDescription('The watch point for loadaverages to signal an error.')
loadaveErrorFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 7, 100), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loadaveErrorFlag.setStatus('mandatory')
if mibBuilder.loadTexts: loadaveErrorFlag.setDescription('A Error flag to indicate trouble with a loadave. It goes to 1 if there is an error, 0 if no error.')
loadaveErrMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 7, 101), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: loadaveErrMessage.setStatus('mandatory')
if mibBuilder.loadTexts: loadaveErrMessage.setDescription('An error message describing the problem (if one exists).')
mibBuilder.exportSymbols("UCD-SNMP-MIB-OLD", diskMinimum=diskMinimum, diskPercent=diskPercent, diskErrorFlag=diskErrorFlag, processIndex=processIndex, diskPath=diskPath, diskMinPercent=diskMinPercent, extensibleErrFix=extensibleErrFix, loadaveConfig=loadaveConfig, diskErrorMsg=diskErrorMsg, loadaveIndex=loadaveIndex, disk=disk, loadaveLoad=loadaveLoad, loadaveNames=loadaveNames, extensible=extensible, processErrorFlag=processErrorFlag, processNames=processNames, processMax=processMax, extensibleOutput=extensibleOutput, extensibleResult=extensibleResult, processes=processes, processCount=processCount, diskAvail=diskAvail, loadaveErrorFlag=loadaveErrorFlag, diskDevice=diskDevice, extensibleNames=extensibleNames, diskTotal=diskTotal, loadaves=loadaves, extensibleCommand=extensibleCommand, diskUsed=diskUsed, loadaveErrMessage=loadaveErrMessage, processErrFix=processErrFix, processMin=processMin, processErrMessage=processErrMessage, extensibleIndex=extensibleIndex, diskIndex=diskIndex)