#
# PySNMP MIB module IBMESCONCUB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IBMESCONCUB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:51:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, iso, Counter64, NotificationType, Unsigned32, TimeTicks, IpAddress, ModuleIdentity, Counter32, Integer32, MibIdentifier, enterprises, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "Counter64", "NotificationType", "Unsigned32", "TimeTicks", "IpAddress", "ModuleIdentity", "Counter32", "Integer32", "MibIdentifier", "enterprises", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention")
ibmIROCescon = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14))
esconPortData = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 1))
esconLinkData = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 2))
esconStationData = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3))
esconConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 4))
esconPortTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 1, 1), )
if mibBuilder.loadTexts: esconPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: esconPortTable.setDescription('Table of objects that describe an ESCON channel port.')
esconPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: esconPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: esconPortEntry.setDescription('Table of objects that describe an ESCON channel port. This table is indexed by ifIndex from MIB-II.')
esconPortInFiberStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("inLoff", 1), ("inOls", 2), ("inIdle", 3), ("inUnknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconPortInFiberStatus.setStatus('mandatory')
if mibBuilder.loadTexts: esconPortInFiberStatus.setDescription('Status of the fiber into this device from the host: inLoff = the light is off on the fiber into this device from the host inOls = the fiber into this device from the host is in an intermediate state between light-off and light-on inIdle = the fiber into this device from the host is in the light-on state, and is ready to transfer data from the host to this device inUnknown = the agent cannot determine the status of the fiber into this device from the host')
esconPortOutFiberStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("outDisableReq", 1), ("outDisableForced", 2), ("outLoffForced", 3), ("outOls", 4), ("outOlsForced", 5), ("outEnable", 6), ("outError", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconPortOutFiberStatus.setStatus('mandatory')
if mibBuilder.loadTexts: esconPortOutFiberStatus.setDescription('Status of the fiber out of this device to the host: outDisableReq = out disable obtained; the fiber out of this device into the host is not in the light-on state outDisableForced = out ESCON emits OLS; the fiber out of this device into the host is not in the light-on state outLoffForced = out ESCON forced light-off; the fiber out of this device into the host is not in the light-on state outOls = the fiber out of this device into the host is in an intermediate state between light-off and light-on outOlsforced = out ESCON forced OLS; the fiber out of this device into the host is not in the light-on state outEnable = the fiber out of this device into the host is in the light-on state, and is ready to transfer data from this device to the host outError = the status of the fiber out of this device to the host is none of those listed above. This is a state that should not occur')
esconLinkTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 2, 1), )
if mibBuilder.loadTexts: esconLinkTable.setStatus('mandatory')
if mibBuilder.loadTexts: esconLinkTable.setDescription('Table of objects that describe an ESCON channel link.')
esconLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "IBMESCONCUB-MIB", "esconLinkHostLinkAddress"), (0, "IBMESCONCUB-MIB", "esconLinkControlUnitAddress"), (0, "IBMESCONCUB-MIB", "esconLinkPartitionNumber"))
if mibBuilder.loadTexts: esconLinkEntry.setStatus('mandatory')
if mibBuilder.loadTexts: esconLinkEntry.setDescription('Table of objects that describe an ESCON channel link. This table is indexed by ifIndex from MIB-II, by host link address, (host) control unit address, and by (host) partition number.')
esconLinkHostLinkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1))
if mibBuilder.loadTexts: esconLinkHostLinkAddress.setStatus('mandatory')
if mibBuilder.loadTexts: esconLinkHostLinkAddress.setDescription('This address identifies the ESCON Director port to which the optical fiber between the ESCON Director and the host is attached.')
esconLinkControlUnitAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1))
if mibBuilder.loadTexts: esconLinkControlUnitAddress.setStatus('mandatory')
if mibBuilder.loadTexts: esconLinkControlUnitAddress.setDescription('A number identifying a logical control unit within an actual host.')
esconLinkPartitionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1))
if mibBuilder.loadTexts: esconLinkPartitionNumber.setStatus('mandatory')
if mibBuilder.loadTexts: esconLinkPartitionNumber.setDescription('A number identifying a logical host within an actual host.')
esconLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("hlpNotEstab", 1), ("hlpEstab", 2), ("hlpError", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconLinkStatus.setStatus('mandatory')
if mibBuilder.loadTexts: esconLinkStatus.setDescription('Gives the status of the link: hlpNotEstab = Host Logical Path not established hlpEstab = Host Logical Path established hlpError = Host Logical Path error')
esconStationTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1), )
if mibBuilder.loadTexts: esconStationTable.setStatus('mandatory')
if mibBuilder.loadTexts: esconStationTable.setDescription('Table of objects that describe an ESCON channel station.')
esconStationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "IBMESCONCUB-MIB", "esconStationHostLinkAddress"), (0, "IBMESCONCUB-MIB", "esconStationControlUnitAddress"), (0, "IBMESCONCUB-MIB", "esconStationPartitionNumber"), (0, "IBMESCONCUB-MIB", "esconStationDeviceAddress"))
if mibBuilder.loadTexts: esconStationEntry.setStatus('mandatory')
if mibBuilder.loadTexts: esconStationEntry.setDescription('Table of objects that describe an ESCON channel station. This table is indexed by ifIndex from MIB-II, by host link address, by (host) control unit address, by (host) partition number, and by ESCON device address.')
esconStationHostLinkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1))
if mibBuilder.loadTexts: esconStationHostLinkAddress.setStatus('mandatory')
if mibBuilder.loadTexts: esconStationHostLinkAddress.setDescription('This address identifies the ESCON Director port to which the optical fiber between the ESCON Director and the host is attached.')
esconStationControlUnitAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1))
if mibBuilder.loadTexts: esconStationControlUnitAddress.setStatus('mandatory')
if mibBuilder.loadTexts: esconStationControlUnitAddress.setDescription('A number identifying a logical control unit within an actual host.')
esconStationPartitionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1))
if mibBuilder.loadTexts: esconStationPartitionNumber.setStatus('mandatory')
if mibBuilder.loadTexts: esconStationPartitionNumber.setDescription('A number identifying a logical host within an actual host.')
esconStationDeviceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1))
if mibBuilder.loadTexts: esconStationDeviceAddress.setStatus('mandatory')
if mibBuilder.loadTexts: esconStationDeviceAddress.setDescription('A unique hexadecimal number allocated to each station on the same host link.')
esconStationState = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("idle", 1), ("cpDefined", 2), ("cpReset", 3), ("cpActive", 4), ("cpDelete", 5), ("cpAbend", 6), ("cldpWait", 7), ("cldpDefinedl", 8), ("cldpError", 9), ("cldpLoad", 10), ("cldpDump", 11), ("deletePending", 12), ("deleted", 13), ("cpXidExpected", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconStationState.setStatus('mandatory')
if mibBuilder.loadTexts: esconStationState.setDescription('The current state of the station.')
esconStationAttentionDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 420))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: esconStationAttentionDelay.setStatus('mandatory')
if mibBuilder.loadTexts: esconStationAttentionDelay.setDescription('Specifies the amount of time in seconds that elapses from the receipt of a packet at an ESCON station (when no other packets are queued) before that station sends buffered data to the Host. An update to this object takes effect the next time the station establishes communications with the host.')
esconStationAttentionTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 840))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: esconStationAttentionTimeOut.setStatus('mandatory')
if mibBuilder.loadTexts: esconStationAttentionTimeOut.setDescription('Specifies the amount of time in seconds that the station is to wait for a response to an attention signal it sent to the host before initiating channel disconnect. An update to this object takes effect the next time the station establishes communications with the host.')
esconStationMaxBfru = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconStationMaxBfru.setStatus('mandatory')
if mibBuilder.loadTexts: esconStationMaxBfru.setDescription('Number of buffers in the host buffer pool for receiving data from this station.')
esconStationUnitSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(64, 4000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconStationUnitSize.setStatus('mandatory')
if mibBuilder.loadTexts: esconStationUnitSize.setDescription('Maximum size of a buffer, in bytes, that the host can receive from this station.')
esconStationMaxMsgSizeReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: esconStationMaxMsgSizeReceived.setStatus('mandatory')
if mibBuilder.loadTexts: esconStationMaxMsgSizeReceived.setDescription('The maximum length of a message that can be received on this station. An update to this object takes effect the next time the station establishes communications with the host.')
esconStationMaxMsgSizeSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: esconStationMaxMsgSizeSent.setStatus('mandatory')
if mibBuilder.loadTexts: esconStationMaxMsgSizeSent.setDescription('The maximum length of a message that can be sent from this station to the host. An update to this object takes effect the next time the station establishes communications with the host.')
esconStationDataPacketsOkReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconStationDataPacketsOkReceived.setStatus('mandatory')
if mibBuilder.loadTexts: esconStationDataPacketsOkReceived.setDescription('The number of data packets received from the host by this station without Data Check.')
esconStationDataPacketsKoReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconStationDataPacketsKoReceived.setStatus('mandatory')
if mibBuilder.loadTexts: esconStationDataPacketsKoReceived.setDescription('The number of data packets received from the host by this station with Data Check.')
esconStationDataPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconStationDataPacketsSent.setStatus('mandatory')
if mibBuilder.loadTexts: esconStationDataPacketsSent.setDescription('The number of data packets sent to the host by this station.')
esconStationTotalFramesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconStationTotalFramesSent.setStatus('mandatory')
if mibBuilder.loadTexts: esconStationTotalFramesSent.setDescription('The number of data packets and control packets sent to the host by this station.')
esconStationDataPacketsRetransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconStationDataPacketsRetransmitted.setStatus('mandatory')
if mibBuilder.loadTexts: esconStationDataPacketsRetransmitted.setDescription('The number of data packets retransmitted by this station')
esconStationPositiveAckDataPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconStationPositiveAckDataPackets.setStatus('mandatory')
if mibBuilder.loadTexts: esconStationPositiveAckDataPackets.setDescription('The number of data packets sent by this station to the host that the host has positively acknowledged. When the host sends a positive acknowledgement for a group of n data packets, this counter is incremented by n.')
esconStationSecondChanceAttentions = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconStationSecondChanceAttentions.setStatus('mandatory')
if mibBuilder.loadTexts: esconStationSecondChanceAttentions.setDescription('The number of times this station has sent a Second Chance Attention signal to the host.')
esconStationCommandsRetried = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14, 3, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esconStationCommandsRetried.setStatus('mandatory')
if mibBuilder.loadTexts: esconStationCommandsRetried.setDescription('The number of times a command has been retried on this station')
mibBuilder.exportSymbols("IBMESCONCUB-MIB", esconStationPositiveAckDataPackets=esconStationPositiveAckDataPackets, esconStationState=esconStationState, esconPortOutFiberStatus=esconPortOutFiberStatus, esconStationSecondChanceAttentions=esconStationSecondChanceAttentions, esconStationAttentionTimeOut=esconStationAttentionTimeOut, esconPortInFiberStatus=esconPortInFiberStatus, esconStationControlUnitAddress=esconStationControlUnitAddress, esconLinkTable=esconLinkTable, esconLinkHostLinkAddress=esconLinkHostLinkAddress, esconPortTable=esconPortTable, esconStationAttentionDelay=esconStationAttentionDelay, esconStationPartitionNumber=esconStationPartitionNumber, ibmIROCescon=ibmIROCescon, esconStationDataPacketsRetransmitted=esconStationDataPacketsRetransmitted, esconLinkPartitionNumber=esconLinkPartitionNumber, esconStationTotalFramesSent=esconStationTotalFramesSent, esconStationData=esconStationData, esconStationMaxBfru=esconStationMaxBfru, esconPortData=esconPortData, esconStationMaxMsgSizeSent=esconStationMaxMsgSizeSent, esconStationDeviceAddress=esconStationDeviceAddress, esconPortEntry=esconPortEntry, esconStationCommandsRetried=esconStationCommandsRetried, esconConformance=esconConformance, esconStationHostLinkAddress=esconStationHostLinkAddress, esconStationDataPacketsOkReceived=esconStationDataPacketsOkReceived, esconLinkEntry=esconLinkEntry, esconStationMaxMsgSizeReceived=esconStationMaxMsgSizeReceived, esconStationUnitSize=esconStationUnitSize, esconLinkControlUnitAddress=esconLinkControlUnitAddress, esconLinkStatus=esconLinkStatus, esconStationEntry=esconStationEntry, esconStationDataPacketsKoReceived=esconStationDataPacketsKoReceived, esconStationDataPacketsSent=esconStationDataPacketsSent, esconLinkData=esconLinkData, esconStationTable=esconStationTable)