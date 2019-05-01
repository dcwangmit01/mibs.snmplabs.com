#
# PySNMP MIB module F10-BMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/F10-BMP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:11:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
f10Mgmt, = mibBuilder.importSymbols("FORCE10-SMI", "f10Mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, IpAddress, Gauge32, MibIdentifier, Integer32, Bits, ModuleIdentity, ObjectIdentity, Counter32, TimeTicks, Unsigned32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "Gauge32", "MibIdentifier", "Integer32", "Bits", "ModuleIdentity", "ObjectIdentity", "Counter32", "TimeTicks", "Unsigned32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
f10BmpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 6027, 3, 23))
f10BmpMib.setRevisions(('2014-07-21 12:00', '2011-12-07 12:48',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: f10BmpMib.setRevisionsDescriptions(('Adding relay related objects - bmpRelay and bmpRelayRemoteID.', 'Initial version of this mib.',))
if mibBuilder.loadTexts: f10BmpMib.setLastUpdated('201112071248Z')
if mibBuilder.loadTexts: f10BmpMib.setOrganization('Dell Inc.')
if mibBuilder.loadTexts: f10BmpMib.setContactInfo('http://www.force10networks.com/support')
if mibBuilder.loadTexts: f10BmpMib.setDescription('Dell Networking OS Baremetal Provisioning MIB.')
f10Bmp = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 23, 1))
bmpReloadType = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 23, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normalReload", 1), ("bmpReload", 2))).clone('bmpReload')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bmpReloadType.setStatus('current')
if mibBuilder.loadTexts: bmpReloadType.setDescription('Configure reload type to enable/disable BMP. normalReload - Regular reload type; BMP process is not initiated. bmpReload - Bmp reload type; BMP process is initiated and image/config files are upgraded based on the DHCP/BOOTP offer. Default is bmpReload.')
bmpAutoSave = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 23, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bmpActionEnable", 1), ("bmpActionDisable", 2))).clone('bmpActionDisable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bmpAutoSave.setStatus('current')
if mibBuilder.loadTexts: bmpAutoSave.setDescription('Configure auto-save option for downloaded config file. bmpActionEnable - Enable auto-save option. bmpActionDisable - Disable auto-save option. Default is bmpActionDisable.')
bmpConfigDownload = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 23, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bmpActionEnable", 1), ("bmpActionDisable", 2))).clone('bmpActionDisable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bmpConfigDownload.setStatus('current')
if mibBuilder.loadTexts: bmpConfigDownload.setDescription('Enable/disable config file download. bmpActionEnable - Enable config-download option. bmpActionDisable - Disable config-download option. Default is bmpActionEnable.')
bmpDhcpTimeout = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 23, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 50))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bmpDhcpTimeout.setStatus('current')
if mibBuilder.loadTexts: bmpDhcpTimeout.setDescription('Configure the DHCP timeout value. Default is infinity which can be set using value 0')
bmpRetryCount = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 23, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 6))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bmpRetryCount.setStatus('current')
if mibBuilder.loadTexts: bmpRetryCount.setDescription('Configure the number of attempts to download a config file. Default value is 3.')
bmpUserDefinedString = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 23, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bmpUserDefinedString.setStatus('current')
if mibBuilder.loadTexts: bmpUserDefinedString.setDescription('A textual string containing information about the option 60.')
bmpRelay = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 23, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bmpActionEnable", 1), ("bmpActionDisable", 2))).clone('bmpActionDisable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bmpRelay.setStatus('current')
if mibBuilder.loadTexts: bmpRelay.setDescription('Configure relay option in bmp to support option82 information. bmpActionEnable - Enable option82 - relay information. bmpActionDisable - Disable option82 - relay information. Default is bmpActionDisable.')
bmpRelayRemoteId = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 23, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bmpRelayRemoteId.setStatus('current')
if mibBuilder.loadTexts: bmpRelayRemoteId.setDescription('A textual string to be appened for the remote-id value.')
mibBuilder.exportSymbols("F10-BMP-MIB", bmpConfigDownload=bmpConfigDownload, bmpAutoSave=bmpAutoSave, bmpUserDefinedString=bmpUserDefinedString, bmpRelayRemoteId=bmpRelayRemoteId, f10Bmp=f10Bmp, bmpDhcpTimeout=bmpDhcpTimeout, bmpRetryCount=bmpRetryCount, bmpReloadType=bmpReloadType, PYSNMP_MODULE_ID=f10BmpMib, bmpRelay=bmpRelay, f10BmpMib=f10BmpMib)