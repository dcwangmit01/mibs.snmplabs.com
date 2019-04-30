#
# PySNMP MIB module INTEL-VAS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTEL-VAS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:43:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
mib2ext, = mibBuilder.importSymbols("INTEL-GEN-MIB", "mib2ext")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, Unsigned32, ModuleIdentity, MibIdentifier, Counter64, Bits, Integer32, iso, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "Unsigned32", "ModuleIdentity", "MibIdentifier", "Counter64", "Bits", "Integer32", "iso", "Counter32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vas = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 53))
vasConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 53, 1))
vasConfigTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1), )
if mibBuilder.loadTexts: vasConfigTable.setStatus('mandatory')
vasConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1), ).setIndexNames((0, "INTEL-VAS-MIB", "vasConfigIndex"))
if mibBuilder.loadTexts: vasConfigEntry.setStatus('mandatory')
vasConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vasConfigIndex.setStatus('mandatory')
vasConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vasConfigStatus.setStatus('mandatory')
vasConfigLicenseKey = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vasConfigLicenseKey.setStatus('mandatory')
vasConfigNameOfLicense = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vasConfigNameOfLicense.setStatus('mandatory')
vasConfigEraseLicense = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vasConfigEraseLicense.setStatus('mandatory')
vasConfigDemoLicenseKey = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vasConfigDemoLicenseKey.setStatus('mandatory')
vasConfigNameOfUser = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vasConfigNameOfUser.setStatus('mandatory')
vasConfigDateOfIssue = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 19))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vasConfigDateOfIssue.setStatus('mandatory')
mibBuilder.exportSymbols("INTEL-VAS-MIB", vasConfig=vasConfig, vasConfigDemoLicenseKey=vasConfigDemoLicenseKey, vasConfigDateOfIssue=vasConfigDateOfIssue, vasConfigTable=vasConfigTable, vas=vas, vasConfigEntry=vasConfigEntry, vasConfigStatus=vasConfigStatus, vasConfigEraseLicense=vasConfigEraseLicense, vasConfigIndex=vasConfigIndex, vasConfigNameOfLicense=vasConfigNameOfLicense, vasConfigNameOfUser=vasConfigNameOfUser, vasConfigLicenseKey=vasConfigLicenseKey)