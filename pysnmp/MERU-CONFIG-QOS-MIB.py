#
# PySNMP MIB module MERU-CONFIG-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MERU-CONFIG-QOS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:01:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
mwConfiguration, = mibBuilder.importSymbols("MERU-SMI", "mwConfiguration")
MwlDscpType, MwlQosCodecProtocol, MwlQosCodec, MwlQosRulesMatchClassBits, MwlDropPolicy, MwlOnOffSwitch, MwlQosRulesMatchClass, MwlQosAction, MwlQosProtocol, MwlAdmissionControl = mibBuilder.importSymbols("MERU-TC", "MwlDscpType", "MwlQosCodecProtocol", "MwlQosCodec", "MwlQosRulesMatchClassBits", "MwlDropPolicy", "MwlOnOffSwitch", "MwlQosRulesMatchClass", "MwlQosAction", "MwlQosProtocol", "MwlAdmissionControl")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, ModuleIdentity, iso, Counter32, TimeTicks, Gauge32, Bits, MibIdentifier, NotificationType, Integer32, Counter64, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "iso", "Counter32", "TimeTicks", "Gauge32", "Bits", "MibIdentifier", "NotificationType", "Integer32", "Counter64", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress")
TimeStamp, RowStatus, DisplayString, DateAndTime, TimeInterval, TruthValue, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "RowStatus", "DisplayString", "DateAndTime", "TimeInterval", "TruthValue", "TextualConvention", "MacAddress")
mwConfigQoS = ModuleIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8))
if mibBuilder.loadTexts: mwConfigQoS.setLastUpdated('200506050000Z')
if mibBuilder.loadTexts: mwConfigQoS.setOrganization('Meru Networks')
mwQosVars = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1))
mwQosVarsQosOnOff = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 1), MwlOnOffSwitch()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosOnOff.setStatus('current')
mwQosVarsQosAdmissionControl = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 2), MwlAdmissionControl()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosAdmissionControl.setStatus('current')
mwQosVarsQosDropPolicy = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 3), MwlDropPolicy()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosDropPolicy.setStatus('current')
mwQosVarsQosDefaultTimeToLive = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosDefaultTimeToLive.setStatus('current')
mwQosVarsQosUdpTimeToLive = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosUdpTimeToLive.setStatus('current')
mwQosVarsQosTcpTimeToLive = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosTcpTimeToLive.setStatus('current')
mwQosVarsPercentBWScaling = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 7), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsPercentBWScaling.setStatus('current')
mwQosVarsQosMaxCallsPerAp = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 8), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosMaxCallsPerAp.setStatus('current')
mwQosVarsQosMaxCallsPerInterfRegion = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosMaxCallsPerInterfRegion.setStatus('current')
mwQosVarsQosLoadBalanceMaxStationsPerAp = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 10), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosLoadBalanceMaxStationsPerAp.setStatus('current')
mwQosVarsQosLoadBalanceMaxStationsPerBssid = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 11), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosLoadBalanceMaxStationsPerBssid.setStatus('current')
mwQosVarsQosLoadBalanceOverflow = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 12), MwlOnOffSwitch()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosLoadBalanceOverflow.setStatus('current')
mwQosVarsQosMaxCallsPerBssid = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 13), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosMaxCallsPerBssid.setStatus('current')
mwQosVarsQosCacDeauth = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 14), MwlOnOffSwitch()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosCacDeauth.setStatus('current')
mwQosVarsQosStationAssignAge = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 15), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosStationAssignAge.setStatus('current')
mwQosVarsQosSipIdleTimeout = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 16), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosSipIdleTimeout.setStatus('current')
mwQosRuleTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2), )
if mibBuilder.loadTexts: mwQosRuleTable.setStatus('current')
mwQosRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1), ).setIndexNames((0, "MERU-CONFIG-QOS-MIB", "mwQosRuleTableIndex"))
if mibBuilder.loadTexts: mwQosRuleEntry.setStatus('current')
mwQosRuleTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: mwQosRuleTableIndex.setStatus('current')
mwQosRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleId.setStatus('current')
mwQosRuleDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 3), MwlDscpType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleDscp.setStatus('current')
mwQosRuleDstIp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleDstIp.setStatus('current')
mwQosRuleSrcIp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleSrcIp.setStatus('current')
mwQosRuleAction = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 6), MwlQosAction()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleAction.setStatus('current')
mwQosRuleDstMask = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleDstMask.setStatus('current')
mwQosRuleDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleDstPort.setStatus('current')
mwQosRuleSrcMask = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 9), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleSrcMask.setStatus('current')
mwQosRuleSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleSrcPort.setStatus('current')
mwQosRuleProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 11), MwlQosProtocol()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleProtocol.setStatus('current')
mwQosRulePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRulePriority.setStatus('current')
mwQosRuleIdUfcFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 13), MwlQosRulesMatchClass()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleIdUfcFlag.setStatus('current')
mwQosRuleDstIpFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 14), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleDstIpFlag.setStatus('current')
mwQosRuleSrcIpFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 15), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleSrcIpFlag.setStatus('current')
mwQosRuleL4Protocol = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleL4Protocol.setStatus('current')
mwQosRuleDstPortFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 18), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleDstPortFlag.setStatus('current')
mwQosRuleSrcPortFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 19), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleSrcPortFlag.setStatus('current')
mwQosRuleDstIpUfcFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 20), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleDstIpUfcFlag.setStatus('current')
mwQosRuleSrcIpUfcFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 21), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleSrcIpUfcFlag.setStatus('current')
mwQosRuleAvgPacketRate = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 22), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleAvgPacketRate.setStatus('current')
mwQosRuleDstPortUfcFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 23), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleDstPortUfcFlag.setStatus('current')
mwQosRuleSrcPortUfcFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 24), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleSrcPortUfcFlag.setStatus('current')
mwQosRuleL4ProtocolFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 25), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleL4ProtocolFlag.setStatus('current')
mwQosRuleTrafficControl = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 26), MwlOnOffSwitch()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleTrafficControl.setStatus('current')
mwQosRuleLogging = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 27), MwlOnOffSwitch()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleLogging.setStatus('current')
mwQosRulePacketMinLength = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 28), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRulePacketMinLength.setStatus('current')
mwQosRulePacketMaxLength = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 29), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRulePacketMaxLength.setStatus('current')
mwQosRuleTokenBucketRate = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 30), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleTokenBucketRate.setStatus('current')
mwQosRuleFirewallFilterId = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 31), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleFirewallFilterId.setStatus('current')
mwQosRuleL4ProtocolUfcFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 32), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleL4ProtocolUfcFlag.setStatus('current')
mwQosRulePacketMinLengthFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 33), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRulePacketMinLengthFlag.setStatus('current')
mwQosRuleFirewallFilterIdFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 34), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleFirewallFilterIdFlag.setStatus('current')
mwQosRulePacketMinLengthUfcFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 35), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRulePacketMinLengthUfcFlag.setStatus('current')
mwQosRuleFirewallFilterIdUfcFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 36), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleFirewallFilterIdUfcFlag.setStatus('current')
mwQosRuleLoggingFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 37), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 60))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleLoggingFrequency.setStatus('current')
mwQosRuleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 40), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleRowStatus.setStatus('current')
mwQosCodecTranslRuleTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3), )
if mibBuilder.loadTexts: mwQosCodecTranslRuleTable.setStatus('current')
mwQosCodecTranslRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1), ).setIndexNames((0, "MERU-CONFIG-QOS-MIB", "mwQosCodecTranslRuleTableIndex"))
if mibBuilder.loadTexts: mwQosCodecTranslRuleEntry.setStatus('current')
mwQosCodecTranslRuleTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: mwQosCodecTranslRuleTableIndex.setStatus('current')
mwQosCodecTranslRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleId.setStatus('current')
mwQosCodecTranslRuleQosCtrProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 3), MwlQosCodecProtocol()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrProtocol.setStatus('current')
mwQosCodecTranslRuleQosCtrCodecEnum = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 4), MwlQosCodec()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrCodecEnum.setStatus('current')
mwQosCodecTranslRuleQosCtrRspecRate = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrRspecRate.setStatus('current')
mwQosCodecTranslRuleQosCtrRspecSlack = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 6), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrRspecSlack.setStatus('current')
mwQosCodecTranslRuleQosCtrSampleRate = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 7), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrSampleRate.setStatus('current')
mwQosCodecTranslRuleQosCtrTspecPeakRate = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 8), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrTspecPeakRate.setStatus('current')
mwQosCodecTranslRuleQosCtrTspecMinPolicedUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 9), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrTspecMinPolicedUnit.setStatus('current')
mwQosCodecTranslRuleQosCtrTspecTokenBucketRate = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 10), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrTspecTokenBucketRate.setStatus('current')
mwQosCodecTranslRuleQosCtrTspecTokenBucketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 11), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrTspecTokenBucketSize.setStatus('current')
mwQosCodecTranslRuleQosCtrTspecMaxDatagramSize = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 12), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrTspecMaxDatagramSize.setStatus('current')
mwQosCodecTranslRuleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleRowStatus.setStatus('current')
mibBuilder.exportSymbols("MERU-CONFIG-QOS-MIB", mwQosVarsQosSipIdleTimeout=mwQosVarsQosSipIdleTimeout, mwQosRuleFirewallFilterIdFlag=mwQosRuleFirewallFilterIdFlag, mwQosCodecTranslRuleQosCtrTspecMinPolicedUnit=mwQosCodecTranslRuleQosCtrTspecMinPolicedUnit, mwQosRuleL4ProtocolUfcFlag=mwQosRuleL4ProtocolUfcFlag, mwQosVarsQosMaxCallsPerBssid=mwQosVarsQosMaxCallsPerBssid, mwQosRuleL4Protocol=mwQosRuleL4Protocol, mwQosRuleAvgPacketRate=mwQosRuleAvgPacketRate, mwQosCodecTranslRuleQosCtrProtocol=mwQosCodecTranslRuleQosCtrProtocol, mwQosCodecTranslRuleQosCtrTspecPeakRate=mwQosCodecTranslRuleQosCtrTspecPeakRate, mwQosVarsQosLoadBalanceMaxStationsPerAp=mwQosVarsQosLoadBalanceMaxStationsPerAp, mwQosRuleSrcPortFlag=mwQosRuleSrcPortFlag, mwQosVarsQosMaxCallsPerAp=mwQosVarsQosMaxCallsPerAp, mwQosVarsQosDefaultTimeToLive=mwQosVarsQosDefaultTimeToLive, mwQosVarsQosTcpTimeToLive=mwQosVarsQosTcpTimeToLive, mwQosRuleTokenBucketRate=mwQosRuleTokenBucketRate, mwQosVarsPercentBWScaling=mwQosVarsPercentBWScaling, mwQosVarsQosCacDeauth=mwQosVarsQosCacDeauth, mwQosRuleDstMask=mwQosRuleDstMask, mwQosCodecTranslRuleEntry=mwQosCodecTranslRuleEntry, mwQosRuleSrcIpFlag=mwQosRuleSrcIpFlag, mwQosCodecTranslRuleQosCtrRspecSlack=mwQosCodecTranslRuleQosCtrRspecSlack, mwQosRuleFirewallFilterId=mwQosRuleFirewallFilterId, mwQosRulePacketMaxLength=mwQosRulePacketMaxLength, mwQosRuleLogging=mwQosRuleLogging, mwQosRuleSrcIpUfcFlag=mwQosRuleSrcIpUfcFlag, mwQosVarsQosAdmissionControl=mwQosVarsQosAdmissionControl, mwQosRuleLoggingFrequency=mwQosRuleLoggingFrequency, mwQosRuleTableIndex=mwQosRuleTableIndex, mwQosRuleDscp=mwQosRuleDscp, mwQosRuleIdUfcFlag=mwQosRuleIdUfcFlag, mwQosRuleDstIpFlag=mwQosRuleDstIpFlag, mwQosCodecTranslRuleQosCtrTspecTokenBucketSize=mwQosCodecTranslRuleQosCtrTspecTokenBucketSize, mwQosRulePacketMinLengthUfcFlag=mwQosRulePacketMinLengthUfcFlag, mwQosVarsQosUdpTimeToLive=mwQosVarsQosUdpTimeToLive, mwQosRuleFirewallFilterIdUfcFlag=mwQosRuleFirewallFilterIdUfcFlag, mwQosRuleAction=mwQosRuleAction, mwQosRuleSrcPortUfcFlag=mwQosRuleSrcPortUfcFlag, mwQosRuleSrcMask=mwQosRuleSrcMask, mwQosRulePriority=mwQosRulePriority, mwQosRuleDstPortUfcFlag=mwQosRuleDstPortUfcFlag, mwQosCodecTranslRuleQosCtrTspecMaxDatagramSize=mwQosCodecTranslRuleQosCtrTspecMaxDatagramSize, mwQosRuleDstIpUfcFlag=mwQosRuleDstIpUfcFlag, mwQosRuleL4ProtocolFlag=mwQosRuleL4ProtocolFlag, mwQosRuleRowStatus=mwQosRuleRowStatus, mwQosRulePacketMinLengthFlag=mwQosRulePacketMinLengthFlag, mwQosRuleDstPort=mwQosRuleDstPort, mwQosRuleDstPortFlag=mwQosRuleDstPortFlag, mwQosCodecTranslRuleTable=mwQosCodecTranslRuleTable, mwQosCodecTranslRuleQosCtrSampleRate=mwQosCodecTranslRuleQosCtrSampleRate, mwQosVarsQosOnOff=mwQosVarsQosOnOff, mwQosCodecTranslRuleQosCtrCodecEnum=mwQosCodecTranslRuleQosCtrCodecEnum, mwQosRuleTable=mwQosRuleTable, mwQosCodecTranslRuleQosCtrRspecRate=mwQosCodecTranslRuleQosCtrRspecRate, mwQosVarsQosDropPolicy=mwQosVarsQosDropPolicy, mwQosCodecTranslRuleRowStatus=mwQosCodecTranslRuleRowStatus, mwConfigQoS=mwConfigQoS, mwQosRuleId=mwQosRuleId, mwQosCodecTranslRuleTableIndex=mwQosCodecTranslRuleTableIndex, mwQosVarsQosLoadBalanceMaxStationsPerBssid=mwQosVarsQosLoadBalanceMaxStationsPerBssid, mwQosVarsQosStationAssignAge=mwQosVarsQosStationAssignAge, mwQosVarsQosMaxCallsPerInterfRegion=mwQosVarsQosMaxCallsPerInterfRegion, mwQosRuleDstIp=mwQosRuleDstIp, mwQosRuleTrafficControl=mwQosRuleTrafficControl, mwQosVarsQosLoadBalanceOverflow=mwQosVarsQosLoadBalanceOverflow, mwQosVars=mwQosVars, mwQosRuleEntry=mwQosRuleEntry, mwQosRuleSrcIp=mwQosRuleSrcIp, mwQosRuleProtocol=mwQosRuleProtocol, mwQosCodecTranslRuleQosCtrTspecTokenBucketRate=mwQosCodecTranslRuleQosCtrTspecTokenBucketRate, mwQosRulePacketMinLength=mwQosRulePacketMinLength, PYSNMP_MODULE_ID=mwConfigQoS, mwQosRuleSrcPort=mwQosRuleSrcPort, mwQosCodecTranslRuleId=mwQosCodecTranslRuleId)