#
# PySNMP MIB module CISCOSB-STORMCTRL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-STORMCTRL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:23:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, ObjectIdentity, MibIdentifier, Counter32, ModuleIdentity, Integer32, Unsigned32, NotificationType, Counter64, TimeTicks, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "ObjectIdentity", "MibIdentifier", "Counter32", "ModuleIdentity", "Integer32", "Unsigned32", "NotificationType", "Counter64", "TimeTicks", "iso", "Gauge32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
class RlStormCtrlRateUnit(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("packetsPerSecond", 1), ("bytesPerSecond", 2), ("framesPerBuffer", 3), ("precentages", 4), ("kiloBytesPerSecond", 5), ("kiloBitsPerSecond", 6))

rlStormCtrl = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77))
rlStormCtrl.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlStormCtrl.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlStormCtrl.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlStormCtrl.setOrganization('Cisco Small Business')
if mibBuilder.loadTexts: rlStormCtrl.setContactInfo('Postal: 170 West Tasman Drive San Jose , CA 95134-1706 USA Website: Cisco Small Business Home http://www.cisco.com/smb>;, Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlStormCtrl.setDescription('This private MIB module defines storm control private MIBs.')
rlStormCtrlSupport = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStormCtrlSupport.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlSupport.setDescription('Identify if the strom control protection is supported')
rlStormCtrlMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStormCtrlMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlMibVersion.setDescription("MIB's version, the current version is 3.")
rlStormCtrlRateUnitTypeSupport = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStormCtrlRateUnitTypeSupport.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlRateUnitTypeSupport.setDescription('the supported rate unit type for the storm rate control')
rlStormCtrlTypeSupport = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStormCtrlTypeSupport.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlTypeSupport.setDescription('the supported frame type for the storm control protection')
rlStormCtrlRateSupportPerType = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStormCtrlRateSupportPerType.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlRateSupportPerType.setDescription('identify if rate control is supported for each frame type')
rlStormCtrlEnbaleDependencyBetweenTypes = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStormCtrlEnbaleDependencyBetweenTypes.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlEnbaleDependencyBetweenTypes.setDescription('indicate enable limitation of dependency between frame types, such as enabling of multicast should be with the enabling of broadcast type (bcm 5632)')
rlStormCtrlRateDependencyBetweenTypes = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStormCtrlRateDependencyBetweenTypes.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlRateDependencyBetweenTypes.setDescription('indicate limitation of dependency between frame types for rate assignment, for example: assigning of rate limit for unicast frame must assigning the same rate for multicast and bradcast frame (bcm 5615), in case the device support enbale per each frame type but with the same rate limitation.')
rlStormCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 8), )
if mibBuilder.loadTexts: rlStormCtrlTable.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlTable.setDescription('The table contains the storm control protection per port')
rlStormCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 8, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: rlStormCtrlEntry.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlEntry.setDescription('storm control protection, defined per port,frame type and rate')
rlStormCtrlRateType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 8, 1, 1), RlStormCtrlRateUnit()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStormCtrlRateType.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlRateType.setDescription('indicate the rate unit type')
rlStormCtrlUnknownUnicastEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 8, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStormCtrlUnknownUnicastEnable.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlUnknownUnicastEnable.setDescription('enable or disable the storm control for unknown unicast frames')
rlStormCtrlUnknownUnicastRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 8, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStormCtrlUnknownUnicastRate.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlUnknownUnicastRate.setDescription('set the storm control rate limit for the unknown unicast frames, 0 indicate blocking of frames from this type.')
rlStormCtrlUnknownMulticastEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 8, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStormCtrlUnknownMulticastEnable.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlUnknownMulticastEnable.setDescription('enable or disable the storm control for unknown multicast frames')
rlStormCtrlUnknownMulticastRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 8, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStormCtrlUnknownMulticastRate.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlUnknownMulticastRate.setDescription('set the storm control rate limit for the unknown multicast frames, 0 indicate blocking of frames from this type.')
rlStormCtrlBroadcastEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 8, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStormCtrlBroadcastEnable.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlBroadcastEnable.setDescription('enable or disable the storm control for Broadcast frames')
rlStormCtrlBroadcastRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 8, 1, 7), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStormCtrlBroadcastRate.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlBroadcastRate.setDescription('set the storm control rate limit for the Broadcast frames, 0 indicate blocking of frames from this type.')
rlStormCtrlMulticastEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 8, 1, 8), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStormCtrlMulticastEnable.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlMulticastEnable.setDescription('enable or disable the storm control for multicast frames')
rlStormCtrlMulticastRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 8, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStormCtrlMulticastRate.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlMulticastRate.setDescription('set the storm control rate limit for the multicast frames, 0 indicate blocking of frames from this type.')
rlStormCtrlSetDefaultRateType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 8, 1, 10), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStormCtrlSetDefaultRateType.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlSetDefaultRateType.setDescription('indicate if return the rate unit type to its default.')
rlStormCtrlSetDefaultUnknownUnicastEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 8, 1, 11), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStormCtrlSetDefaultUnknownUnicastEnable.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlSetDefaultUnknownUnicastEnable.setDescription('indicate if return the storm control enable for unknown unicast frames to its default.')
rlStormCtrlSetDefaultUnknownUnicastRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 8, 1, 12), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStormCtrlSetDefaultUnknownUnicastRate.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlSetDefaultUnknownUnicastRate.setDescription('indicate if return the storm control rate limit for the unknown unicast frames to its default.')
rlStormCtrlSetDefaultUnknownMulticastEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 8, 1, 13), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStormCtrlSetDefaultUnknownMulticastEnable.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlSetDefaultUnknownMulticastEnable.setDescription('indicate if return the storm control enable for unknown multicast frames to its default.')
rlStormCtrlSetDefaultUnknownMulticastRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 8, 1, 14), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStormCtrlSetDefaultUnknownMulticastRate.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlSetDefaultUnknownMulticastRate.setDescription('indicate if return the storm control rate limit for the unknown multicast frames to its default.')
rlStormCtrlSetDefaultBroadcastEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 8, 1, 15), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStormCtrlSetDefaultBroadcastEnable.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlSetDefaultBroadcastEnable.setDescription('indicate if return the storm control enable for Broadcast frames to its default.')
rlStormCtrlSetDefaultBroadcastRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 8, 1, 16), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStormCtrlSetDefaultBroadcastRate.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlSetDefaultBroadcastRate.setDescription('indicate if return the storm control rate limit for the Broadcast frames to its default.')
rlStormCtrlSetDefaultMulticastEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 8, 1, 17), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStormCtrlSetDefaultMulticastEnable.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlSetDefaultMulticastEnable.setDescription('indicate if return the storm control for multicast frames to its default.')
rlStormCtrlSetDefaultMulticastRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 8, 1, 18), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStormCtrlSetDefaultMulticastRate.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlSetDefaultMulticastRate.setDescription('indicate if return the storm control rate limit for the multicast frames to its default.')
rlStormCtrlBroadcastOperRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 8, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStormCtrlBroadcastOperRate.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlBroadcastOperRate.setDescription('Operative storm control rate limit for the Broadcast frames. The value will be 0 if rlStormCtrlRateType is not from type precentages.')
rlStormCtrlGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 9), )
if mibBuilder.loadTexts: rlStormCtrlGroupTable.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlGroupTable.setDescription('The table contains per port for each supported frame type to which group it belongs.')
rlStormCtrlGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 9, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: rlStormCtrlGroupEntry.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlGroupEntry.setDescription('group id for each supported frame type defined per port.')
rlStormCtrlGroupUnknownUnicastId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStormCtrlGroupUnknownUnicastId.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlGroupUnknownUnicastId.setDescription('Indicates the id of the group for unknown unicast frame type that the port belongs to, 0 indicates that unknown unicast frame type is not supported.')
rlStormCtrlGroupUnknownMulticastId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 9, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStormCtrlGroupUnknownMulticastId.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlGroupUnknownMulticastId.setDescription('Indicates the id of the group for unknown multicast frame type that the port belongs to, 0 indicates that unknown multicast frame type is not supported.')
rlStormCtrlGroupBroadcastId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 9, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStormCtrlGroupBroadcastId.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlGroupBroadcastId.setDescription('Indicates the id of the group for broadcast frame type that the port belongs to, 0 indicates that broadcast frame type is not supported.')
rlStormCtrlGroupMulticastId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77, 9, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStormCtrlGroupMulticastId.setStatus('current')
if mibBuilder.loadTexts: rlStormCtrlGroupMulticastId.setDescription('Indicates the id of the group for multicast frame type that the port belongs to, 0 indicates that multicast frame type is not supported.')
mibBuilder.exportSymbols("CISCOSB-STORMCTRL-MIB", rlStormCtrlUnknownMulticastRate=rlStormCtrlUnknownMulticastRate, rlStormCtrlMibVersion=rlStormCtrlMibVersion, rlStormCtrlSetDefaultRateType=rlStormCtrlSetDefaultRateType, rlStormCtrlSetDefaultUnknownUnicastEnable=rlStormCtrlSetDefaultUnknownUnicastEnable, rlStormCtrlBroadcastEnable=rlStormCtrlBroadcastEnable, rlStormCtrlEnbaleDependencyBetweenTypes=rlStormCtrlEnbaleDependencyBetweenTypes, rlStormCtrlGroupTable=rlStormCtrlGroupTable, rlStormCtrlUnknownUnicastEnable=rlStormCtrlUnknownUnicastEnable, rlStormCtrlMulticastEnable=rlStormCtrlMulticastEnable, rlStormCtrlRateUnitTypeSupport=rlStormCtrlRateUnitTypeSupport, rlStormCtrlBroadcastOperRate=rlStormCtrlBroadcastOperRate, rlStormCtrlRateDependencyBetweenTypes=rlStormCtrlRateDependencyBetweenTypes, PYSNMP_MODULE_ID=rlStormCtrl, rlStormCtrlRateSupportPerType=rlStormCtrlRateSupportPerType, rlStormCtrlSetDefaultUnknownMulticastRate=rlStormCtrlSetDefaultUnknownMulticastRate, rlStormCtrlGroupMulticastId=rlStormCtrlGroupMulticastId, rlStormCtrlBroadcastRate=rlStormCtrlBroadcastRate, rlStormCtrlSupport=rlStormCtrlSupport, rlStormCtrlGroupEntry=rlStormCtrlGroupEntry, rlStormCtrlSetDefaultBroadcastRate=rlStormCtrlSetDefaultBroadcastRate, rlStormCtrlUnknownUnicastRate=rlStormCtrlUnknownUnicastRate, rlStormCtrlGroupUnknownMulticastId=rlStormCtrlGroupUnknownMulticastId, rlStormCtrlTypeSupport=rlStormCtrlTypeSupport, RlStormCtrlRateUnit=RlStormCtrlRateUnit, rlStormCtrlSetDefaultUnknownUnicastRate=rlStormCtrlSetDefaultUnknownUnicastRate, rlStormCtrlMulticastRate=rlStormCtrlMulticastRate, rlStormCtrlSetDefaultUnknownMulticastEnable=rlStormCtrlSetDefaultUnknownMulticastEnable, rlStormCtrlEntry=rlStormCtrlEntry, rlStormCtrlGroupUnknownUnicastId=rlStormCtrlGroupUnknownUnicastId, rlStormCtrlGroupBroadcastId=rlStormCtrlGroupBroadcastId, rlStormCtrlTable=rlStormCtrlTable, rlStormCtrlSetDefaultBroadcastEnable=rlStormCtrlSetDefaultBroadcastEnable, rlStormCtrlRateType=rlStormCtrlRateType, rlStormCtrlSetDefaultMulticastEnable=rlStormCtrlSetDefaultMulticastEnable, rlStormCtrl=rlStormCtrl, rlStormCtrlUnknownMulticastEnable=rlStormCtrlUnknownMulticastEnable, rlStormCtrlSetDefaultMulticastRate=rlStormCtrlSetDefaultMulticastRate)