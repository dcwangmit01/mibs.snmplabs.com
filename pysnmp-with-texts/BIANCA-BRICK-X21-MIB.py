#
# PySNMP MIB module BIANCA-BRICK-X21-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BIANCA-BRICK-X21-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:38:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, TimeTicks, Counter64, Unsigned32, ModuleIdentity, ObjectIdentity, Bits, iso, NotificationType, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "Bits", "iso", "NotificationType", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
org = MibIdentifier((1, 3))
dod = MibIdentifier((1, 3, 6))
internet = MibIdentifier((1, 3, 6, 1))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
x21 = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 10))
class Date(Integer32):
    pass

class HexValue(Integer32):
    pass

x21IfTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 10, 1), )
if mibBuilder.loadTexts: x21IfTable.setStatus('mandatory')
if mibBuilder.loadTexts: x21IfTable.setDescription('The x21IfTable contains information relating to the interfaces found on the system. Each entry corresponds to a connected X21 interface. Entries can only be added or deleted by the system. Creating entries: Entries are created by the system only when a new X21 module is installed. Deleting entries: Entries are removed by the system after the appropriate X21 module is removed.')
x21IfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1), ).setIndexNames((0, "BIANCA-BRICK-X21-MIB", "x21IfIndex"))
if mibBuilder.loadTexts: x21IfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: x21IfEntry.setDescription('')
x21IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21IfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: x21IfIndex.setDescription('Unique index of the X21 interface.')
x21IfL1State = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dn", 1), ("up", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21IfL1State.setStatus('mandatory')
if mibBuilder.loadTexts: x21IfL1State.setDescription('The X21 physical layer state dn(1) physical layer is inactive; up(2) physical layer is active;')
x21IfL1Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dte", 1), ("dce", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21IfL1Mode.setStatus('mandatory')
if mibBuilder.loadTexts: x21IfL1Mode.setDescription('The physical layer (layer 1) mode. When configured as DCE(2) the X21 interface provides the clock.')
x21IfIfLeads = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21IfIfLeads.setStatus('mandatory')
if mibBuilder.loadTexts: x21IfIfLeads.setDescription("The value of IfLeads has influence on the state of the physical layer (L1State). When configured as IfLeads=enabled(1), the state of the physical layer depends on the signals of the X.21 interface pins `Indication' and `Control'. When configured as IfLeads=disabled(2), the state of the physical layer stays always up.")
x21IfSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("s2048k", 1), ("s1024k", 2), ("s512k", 3), ("s256k", 4), ("s128k", 5), ("s64000", 6), ("s38400", 7), ("s19200", 8), ("s14400", 9), ("s9600", 10), ("s2400", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21IfSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: x21IfSpeed.setDescription('The X21 interface speed in bits per second. The range can be configured between 2Mbits and 2400 Bits per second.')
x21IfL2Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dte", 1), ("dce", 2), ("auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21IfL2Mode.setStatus('mandatory')
if mibBuilder.loadTexts: x21IfL2Mode.setDescription('The layer 2 mode. This value has influence on the HDLC address field (first byte of a HDCL frame). When configured as DTE(1) the address in a command frame is 0x01, when configured as DCE(2) it is 0x03. For response frames it is vice versa. When configured as AUTO(3), layer 2 is set to the same mode like L1Mode is set.')
x21IfSpeedReal = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21IfSpeedReal.setStatus('mandatory')
if mibBuilder.loadTexts: x21IfSpeedReal.setDescription('The measured X21 interface speed in bits per second.')
x21IfRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21IfRxPackets.setStatus('mandatory')
if mibBuilder.loadTexts: x21IfRxPackets.setDescription('Count of received valid Frames.')
x21IfRxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21IfRxOctets.setStatus('mandatory')
if mibBuilder.loadTexts: x21IfRxOctets.setDescription('Count of received bytes.')
x21IfTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21IfTxPackets.setStatus('mandatory')
if mibBuilder.loadTexts: x21IfTxPackets.setDescription('Count of transmitted valid Frames.')
x21IfTxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21IfTxOctets.setStatus('mandatory')
if mibBuilder.loadTexts: x21IfTxOctets.setDescription('Count of transmitted bytes.')
x21IfRxResets = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21IfRxResets.setStatus('mandatory')
if mibBuilder.loadTexts: x21IfRxResets.setDescription('Count of receiver resets. Under rare circumstances it might be necessary to reset the receiver to work properly.')
x21IfRxAborts = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21IfRxAborts.setStatus('mandatory')
if mibBuilder.loadTexts: x21IfRxAborts.setDescription('Count of receiver aborts. The sender of a frame can indicate a frame as aborted with a special Abort sequence.')
x21IfRxOverruns = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21IfRxOverruns.setStatus('mandatory')
if mibBuilder.loadTexts: x21IfRxOverruns.setDescription('Count of receiver overruns. If the X21 card is unable to grant sufficiently soon/often the bus, the 32-character RxFIFO may fill up. This leads to loss of data.')
x21IfRxCRCErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21IfRxCRCErrors.setStatus('mandatory')
if mibBuilder.loadTexts: x21IfRxCRCErrors.setDescription('Count of corrupted frames. Errors due to interference on the X21 cable.')
x21IfRxGiantFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21IfRxGiantFrames.setStatus('mandatory')
if mibBuilder.loadTexts: x21IfRxGiantFrames.setDescription('Count of received frames with illegal framesize. This can occur if a frame delimiter is destroyed.')
x21IfTxResets = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21IfTxResets.setStatus('mandatory')
if mibBuilder.loadTexts: x21IfTxResets.setDescription('Count of transmitter resets. Under rare circumstances it might be necessary to reset the transmitter to work properly.')
x21IfTxAborts = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21IfTxAborts.setStatus('mandatory')
if mibBuilder.loadTexts: x21IfTxAborts.setDescription('Count of transmitter aborts. While sending a frame it might be necessary to indicate this frame as aborted. In this case the receiver regards this frame as illegal.')
x21IfTxUnderruns = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21IfTxUnderruns.setStatus('mandatory')
if mibBuilder.loadTexts: x21IfTxUnderruns.setDescription('Count of transmitter underruns. The serial data for the X21 card is supplied too slowly.')
x21IfTxGiantFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 10, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21IfTxGiantFrames.setStatus('mandatory')
if mibBuilder.loadTexts: x21IfTxGiantFrames.setDescription('Count of transmitted frames with illegal framesize. This can occur if an upper module creates packets with more than the maximum allowed packet size.')
mibBuilder.exportSymbols("BIANCA-BRICK-X21-MIB", x21IfL2Mode=x21IfL2Mode, x21IfTxOctets=x21IfTxOctets, x21IfTxGiantFrames=x21IfTxGiantFrames, x21IfRxResets=x21IfRxResets, internet=internet, bintec=bintec, x21IfSpeedReal=x21IfSpeedReal, x21IfTxResets=x21IfTxResets, x21IfEntry=x21IfEntry, x21IfIfLeads=x21IfIfLeads, x21IfTxUnderruns=x21IfTxUnderruns, x21IfTable=x21IfTable, dod=dod, HexValue=HexValue, x21IfL1State=x21IfL1State, private=private, x21IfL1Mode=x21IfL1Mode, x21IfRxCRCErrors=x21IfRxCRCErrors, x21IfTxAborts=x21IfTxAborts, enterprises=enterprises, Date=Date, x21=x21, x21IfTxPackets=x21IfTxPackets, x21IfRxOctets=x21IfRxOctets, bibo=bibo, x21IfRxOverruns=x21IfRxOverruns, x21IfSpeed=x21IfSpeed, org=org, x21IfRxAborts=x21IfRxAborts, x21IfRxGiantFrames=x21IfRxGiantFrames, x21IfRxPackets=x21IfRxPackets, x21IfIndex=x21IfIndex)