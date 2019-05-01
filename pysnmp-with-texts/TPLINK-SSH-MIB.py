#
# PySNMP MIB module TPLINK-SSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-SSH-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:25:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, ModuleIdentity, iso, Gauge32, Unsigned32, IpAddress, Bits, Counter32, NotificationType, ObjectIdentity, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "ModuleIdentity", "iso", "Gauge32", "Unsigned32", "IpAddress", "Bits", "Counter32", "NotificationType", "ObjectIdentity", "TimeTicks", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkSshMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 5))
tplinkSshMIB.setRevisions(('2012-12-13 09:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkSshMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkSshMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkSshMIB.setOrganization('TPLINK')
if mibBuilder.loadTexts: tplinkSshMIB.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkSshMIB.setDescription('Private MIB for SSH configuration.')
tplinkSshMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 5, 1))
tplinkSshNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 5, 2))
tpSshEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpSshEnable.setStatus('current')
if mibBuilder.loadTexts: tpSshEnable.setDescription('0. disable 1. enable')
tpSshProtocolV1Enable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpSshProtocolV1Enable.setStatus('current')
if mibBuilder.loadTexts: tpSshProtocolV1Enable.setDescription('0. disable 1. enable')
tpSshProtocolV2Enable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpSshProtocolV2Enable.setStatus('current')
if mibBuilder.loadTexts: tpSshProtocolV2Enable.setDescription('0. disable 1. enable')
tpSshQuietPeriod = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 120))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpSshQuietPeriod.setStatus('current')
if mibBuilder.loadTexts: tpSshQuietPeriod.setDescription('quiet period(1-120 second)')
tpSshMaxConnections = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpSshMaxConnections.setStatus('current')
if mibBuilder.loadTexts: tpSshMaxConnections.setDescription('max connection(1-5)')
tpSshEncryptAlgAES128Enable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpSshEncryptAlgAES128Enable.setStatus('current')
if mibBuilder.loadTexts: tpSshEncryptAlgAES128Enable.setDescription('0. disable 1. enable')
tpSshEncryptAlgAES192Enable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpSshEncryptAlgAES192Enable.setStatus('current')
if mibBuilder.loadTexts: tpSshEncryptAlgAES192Enable.setDescription('0. disable 1. enable')
tpSshEncryptAlgAES256Enable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpSshEncryptAlgAES256Enable.setStatus('current')
if mibBuilder.loadTexts: tpSshEncryptAlgAES256Enable.setDescription('0. disable 1. enable')
tpSshEncryptAlgBlowfishEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpSshEncryptAlgBlowfishEnable.setStatus('current')
if mibBuilder.loadTexts: tpSshEncryptAlgBlowfishEnable.setDescription('0. disable 1. enable')
tpSshEncryptAlgCast128Enable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpSshEncryptAlgCast128Enable.setStatus('current')
if mibBuilder.loadTexts: tpSshEncryptAlgCast128Enable.setDescription('0. disable 1. enable')
tpSshEncryptAlg3DESEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpSshEncryptAlg3DESEnable.setStatus('current')
if mibBuilder.loadTexts: tpSshEncryptAlg3DESEnable.setDescription('0. disable 1. enable')
tpSshInteAlgSHA1Enable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpSshInteAlgSHA1Enable.setStatus('current')
if mibBuilder.loadTexts: tpSshInteAlgSHA1Enable.setDescription('0. disable 1. enable')
tpSshInteAlgMD5Enable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpSshInteAlgMD5Enable.setStatus('current')
if mibBuilder.loadTexts: tpSshInteAlgMD5Enable.setDescription('0. disable 1. enable')
mibBuilder.exportSymbols("TPLINK-SSH-MIB", tpSshEncryptAlgCast128Enable=tpSshEncryptAlgCast128Enable, tplinkSshMIBObjects=tplinkSshMIBObjects, tpSshEncryptAlgBlowfishEnable=tpSshEncryptAlgBlowfishEnable, tpSshEncryptAlgAES128Enable=tpSshEncryptAlgAES128Enable, tpSshProtocolV2Enable=tpSshProtocolV2Enable, tpSshMaxConnections=tpSshMaxConnections, tpSshInteAlgMD5Enable=tpSshInteAlgMD5Enable, tpSshProtocolV1Enable=tpSshProtocolV1Enable, tpSshEncryptAlg3DESEnable=tpSshEncryptAlg3DESEnable, PYSNMP_MODULE_ID=tplinkSshMIB, tplinkSshNotifications=tplinkSshNotifications, tpSshInteAlgSHA1Enable=tpSshInteAlgSHA1Enable, tplinkSshMIB=tplinkSshMIB, tpSshEncryptAlgAES192Enable=tpSshEncryptAlgAES192Enable, tpSshEncryptAlgAES256Enable=tpSshEncryptAlgAES256Enable, tpSshEnable=tpSshEnable, tpSshQuietPeriod=tpSshQuietPeriod)