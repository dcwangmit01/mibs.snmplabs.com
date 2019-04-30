#
# PySNMP MIB module LANART-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LANART-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:54:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
rptrPortOperStatus, = mibBuilder.importSymbols("SNMP-REPEATER-MIB", "rptrPortOperStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, IpAddress, ModuleIdentity, Counter32, Bits, ObjectIdentity, enterprises, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, iso, NotificationType, Counter64, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "ModuleIdentity", "Counter32", "Bits", "ObjectIdentity", "enterprises", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "iso", "NotificationType", "Counter64", "Gauge32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lanart = MibIdentifier((1, 3, 6, 1, 4, 1, 712))
laMib1 = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1))
laProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1))
laHubMib = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 2))
laSys = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 2, 1))
laTpPort = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 2, 2))
laTpHub = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1))
laTpHub1 = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 1))
etm120x = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 1, 12))
etm160x = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 1, 16))
etm240x = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 1, 24))
laTpHub2 = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 2))
ete120x = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 2, 12))
ete160x = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 2, 16))
ete240x = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 2, 24))
laTpHub3 = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 3))
bbAui = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 3, 0))
bbAuiTp = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 3, 1))
bbAuiBnc = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 3, 2))
bbAuiTpBnc = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 3, 3))
bbAui10BASE_FL = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 3, 4)).setLabel("bbAui10BASE-FL")
laSysConfig = MibScalar((1, 3, 6, 1, 4, 1, 712, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("save", 1), ("load", 2), ("factory", 3), ("ok", 4), ("failed", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laSysConfig.setStatus('mandatory')
laJoystick = MibScalar((1, 3, 6, 1, 4, 1, 712, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laJoystick.setStatus('mandatory')
laLinkAlert = MibScalar((1, 3, 6, 1, 4, 1, 712, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("not-applicable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laLinkAlert.setStatus('mandatory')
laTpPortTable = MibTable((1, 3, 6, 1, 4, 1, 712, 1, 2, 2, 1), )
if mibBuilder.loadTexts: laTpPortTable.setStatus('mandatory')
laTpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 712, 1, 2, 2, 1, 1), ).setIndexNames((0, "LANART-MIB", "laTpPortGroupIndex"), (0, "LANART-MIB", "laTpPortIndex"))
if mibBuilder.loadTexts: laTpPortEntry.setStatus('mandatory')
laTpPortGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 712, 1, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: laTpPortGroupIndex.setStatus('mandatory')
laTpPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 712, 1, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: laTpPortIndex.setStatus('mandatory')
laTpLinkTest = MibTableColumn((1, 3, 6, 1, 4, 1, 712, 1, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("failed", 3), ("not-applicable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laTpLinkTest.setStatus('mandatory')
laTpAutoPolarity = MibTableColumn((1, 3, 6, 1, 4, 1, 712, 1, 2, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("corrected", 3), ("not-applicable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laTpAutoPolarity.setStatus('mandatory')
laPortStatus = NotificationType((1, 3, 6, 1, 4, 1, 712) + (0,1)).setObjects(("SNMP-REPEATER-MIB", "rptrPortOperStatus"))
mibBuilder.exportSymbols("LANART-MIB", laHubMib=laHubMib, etm120x=etm120x, laTpPortIndex=laTpPortIndex, bbAuiTpBnc=bbAuiTpBnc, ete120x=ete120x, etm160x=etm160x, laLinkAlert=laLinkAlert, laTpHub2=laTpHub2, ete160x=ete160x, laProducts=laProducts, laTpHub=laTpHub, laTpLinkTest=laTpLinkTest, laSys=laSys, bbAuiTp=bbAuiTp, laSysConfig=laSysConfig, laTpPortGroupIndex=laTpPortGroupIndex, laTpHub3=laTpHub3, lanart=lanart, laMib1=laMib1, bbAuiBnc=bbAuiBnc, laTpPortTable=laTpPortTable, ete240x=ete240x, laTpHub1=laTpHub1, laTpPortEntry=laTpPortEntry, laPortStatus=laPortStatus, bbAui=bbAui, bbAui10BASE_FL=bbAui10BASE_FL, laJoystick=laJoystick, laTpAutoPolarity=laTpAutoPolarity, laTpPort=laTpPort, etm240x=etm240x)