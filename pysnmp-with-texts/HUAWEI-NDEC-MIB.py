#
# PySNMP MIB module HUAWEI-NDEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-NDEC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:47:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
mlsr, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "mlsr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, IpAddress, NotificationType, Bits, ObjectIdentity, Integer32, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, Gauge32, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "NotificationType", "Bits", "ObjectIdentity", "Integer32", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "Gauge32", "TimeTicks", "Counter32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
huaweiNDEC = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2))
huaweiNDEC.setRevisions(('2004-09-15 10:52',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: huaweiNDEC.setRevisionsDescriptions(('The initial version of this MIB module',))
if mibBuilder.loadTexts: huaweiNDEC.setLastUpdated('200409150000Z')
if mibBuilder.loadTexts: huaweiNDEC.setOrganization('HUAWEI Technologies Co., Ltd.')
if mibBuilder.loadTexts: huaweiNDEC.setContactInfo('HUAWEI Technologies Co.,Ltd. Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China http://www.huawei.com Zip:100085')
if mibBuilder.loadTexts: huaweiNDEC.setDescription('This MIB contains objects to manage the NDEC device. ')
hipsNDECSAListTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 1), )
if mibBuilder.loadTexts: hipsNDECSAListTable.setStatus('current')
if mibBuilder.loadTexts: hipsNDECSAListTable.setDescription('The table containing the list of all SA entries configured on NDEC by the operator.')
hipsNDECSAListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 1, 1), ).setIndexNames((0, "HUAWEI-NDEC-MIB", "hipsPeerIpAddr"), (0, "HUAWEI-NDEC-MIB", "hipsProtocol"), (0, "HUAWEI-NDEC-MIB", "hipsSPI"))
if mibBuilder.loadTexts: hipsNDECSAListEntry.setStatus('current')
if mibBuilder.loadTexts: hipsNDECSAListEntry.setDescription("Each entry contains the attributes associated with a single NDEC'S SA entry.")
hipsPeerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsPeerIpAddr.setStatus('current')
if mibBuilder.loadTexts: hipsPeerIpAddr.setDescription('The peer IP address of this SA entry. ')
hipsProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(50, 51))).clone(namedValues=NamedValues(("ipsecEsp", 50), ("ipsecAh", 51)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsProtocol.setStatus('current')
if mibBuilder.loadTexts: hipsProtocol.setDescription('The Protocol of this SA entry. ')
hipsSPI = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 1, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(256, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsSPI.setStatus('current')
if mibBuilder.loadTexts: hipsSPI.setDescription('The SPI of this SA entry. ')
hipsEncAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("ealgNone", 1), ("ealgDescbc", 2), ("ealg3desCbc", 3), ("ealgXBlf", 4), ("ealgXCast", 5), ("ealgXSkipjack", 6), ("ealgXAes", 7), ("ealgXQc5", 8), ("ealgXNsa", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsEncAlgorithm.setStatus('current')
if mibBuilder.loadTexts: hipsEncAlgorithm.setDescription('The encrypt algorithm of this SA entry. ')
hipsAuthAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("aalgNone", 1), ("aalgMd5Hmac", 2), ("aalgSha1Hmac", 3), ("aalgMd5Hmac96", 4), ("aalgSha1Hmac96", 5), ("aalgXRipeMd160Hmac96", 6), ("aalgXMd5", 7), ("aalgXSha1", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsAuthAlgorithm.setStatus('current')
if mibBuilder.loadTexts: hipsAuthAlgorithm.setDescription('The authentication algorithm of this SA entry. ')
hipsLocalIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsLocalIpAddr.setStatus('current')
if mibBuilder.loadTexts: hipsLocalIpAddr.setDescription('The local IP address of this SA entry. ')
hipsSaLifeKBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsSaLifeKBytes.setStatus('current')
if mibBuilder.loadTexts: hipsSaLifeKBytes.setDescription('The lifetime of this SA entry in bytes. ')
hipsSaLifeSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsSaLifeSecond.setStatus('current')
if mibBuilder.loadTexts: hipsSaLifeSecond.setDescription('The lifetime of this SA entry in seconds. ')
hipsByCard = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsByCard.setStatus('current')
if mibBuilder.loadTexts: hipsByCard.setDescription('The flag of this SA on NDEC or not. ')
hipsNegotiateSaMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("isakmp", 2), ("manual", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsNegotiateSaMode.setStatus('current')
if mibBuilder.loadTexts: hipsNegotiateSaMode.setDescription('The type of key used by the IPSec Phase-2 Tunnel. ')
hipsExpBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 1, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsExpBytes.setStatus('current')
if mibBuilder.loadTexts: hipsExpBytes.setDescription('This object specifies the lifetime in bytes of the tunnels generated using this policy specification.')
hipsSoftBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 1, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsSoftBytes.setStatus('current')
if mibBuilder.loadTexts: hipsSoftBytes.setDescription('This object specifies the lifetime in bytes of the tunnels generated using this policy specification.')
hipsExpTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 1, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsExpTimeout.setStatus('current')
if mibBuilder.loadTexts: hipsExpTimeout.setDescription('This object specifies the lifetime in seconds of the tunnels generated using this policy specification.')
hipsSoftTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 1, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsSoftTimeout.setStatus('current')
if mibBuilder.loadTexts: hipsSoftTimeout.setDescription('This object specifies the lifetime in seconds of the tunnels generated using this policy specification.')
hikeSATable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 2), )
if mibBuilder.loadTexts: hikeSATable.setStatus('current')
if mibBuilder.loadTexts: hikeSATable.setDescription('The table containing IKE SA entities configured on NDEC by the operator. ')
hikeSAEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 2, 1), ).setIndexNames((0, "HUAWEI-NDEC-MIB", "hikeConnId"))
if mibBuilder.loadTexts: hikeSAEntry.setStatus('current')
if mibBuilder.loadTexts: hikeSAEntry.setDescription('Each entry contains the attributes associated with a single IKE SA entity.')
hikeConnId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hikeConnId.setStatus('current')
if mibBuilder.loadTexts: hikeConnId.setDescription('The identifier of IKE SA connection.')
hikePeerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hikePeerIpAddr.setStatus('current')
if mibBuilder.loadTexts: hikePeerIpAddr.setDescription('The peer IP address of this IKE SA. ')
hikeFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hikeFlag.setStatus('current')
if mibBuilder.loadTexts: hikeFlag.setDescription('The status of this IKE SA. ')
hikePhase = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unkown", 1), ("phase1", 2), ("phase2", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hikePhase.setStatus('current')
if mibBuilder.loadTexts: hikePhase.setDescription('The phase of this IKE SA. ')
hikeDoi = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unkown", 1), ("ipsec", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hikeDoi.setStatus('current')
if mibBuilder.loadTexts: hikeDoi.setDescription('The domain of this IKE SA ')
hikeClearSA = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 2, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hikeClearSA.setStatus('current')
if mibBuilder.loadTexts: hikeClearSA.setDescription('Clear this IKE SA or not. ')
hipsIKEPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 3), )
if mibBuilder.loadTexts: hipsIKEPolicyTable.setStatus('current')
if mibBuilder.loadTexts: hipsIKEPolicyTable.setDescription('List of all ISAKMP policy entries.')
hipsIKEPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 3, 1), ).setIndexNames((0, "HUAWEI-NDEC-MIB", "hipsIsakmpPolPriority"))
if mibBuilder.loadTexts: hipsIKEPolicyEntry.setStatus('current')
if mibBuilder.loadTexts: hipsIKEPolicyEntry.setDescription('Each entry includes the properties of a ISAKMP Policy entry.')
hipsIsakmpPolPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsIsakmpPolPriority.setStatus('current')
if mibBuilder.loadTexts: hipsIsakmpPolPriority.setDescription("ISAKMP Policy entry's priority.")
hipsIsakmpPolEncr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("ikeEncryptNone", 1), ("ikeEncryptDesCbc", 2), ("ikeEncryptIdeaCbc", 3), ("ikeEncryptBlowfishcbc", 4), ("ikeEncryptRc5R16B64cbc", 5), ("ikeEncrypt3DesCbc", 6), ("ikeEncryptCastCbc", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsIsakmpPolEncr.setStatus('current')
if mibBuilder.loadTexts: hipsIsakmpPolEncr.setDescription('The specified encryption transform. It is used by Internet Key Exchange(IKE) tunnels to protect the ISAKMP PDUs.')
hipsIsakmpPolHash = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ikeHashNone", 1), ("ikeHashMd5", 2), ("ikeHashSha", 3), ("ikeHashTiger", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsIsakmpPolHash.setStatus('current')
if mibBuilder.loadTexts: hipsIsakmpPolHash.setDescription('The specified hash transform. It is used by Internet Key Exchange(IKE) tunnels to protect the ISAKMP PDUs.')
hipsIsakmpPolAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ikeAuthPreNone", 1), ("ikeAuthPreShared", 2), ("ikeAuthDss", 3), ("ikeAuthRsaSig", 4), ("ikeAuthRsaEnc", 5), ("ikeAuthRsaEncRev", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsIsakmpPolAuth.setStatus('current')
if mibBuilder.loadTexts: hipsIsakmpPolAuth.setDescription('The specified peer authentication method. The local entity would authenticate the peer using the method specified by this object when this policy entity is selected to negotiate with a peer.')
hipsIsakmpPolGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("dhGroup1", 2), ("dhGroup2", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsIsakmpPolGroup.setStatus('current')
if mibBuilder.loadTexts: hipsIsakmpPolGroup.setDescription('This object is used to specify the Oakley group which is used for Diffie Hellman exchange in the Main Mode. The local entity selects the group specified by this object to perform Diffie Hellman exchange with the peer when this policy item is chosen to negotiate the Main Mode with an IKE peer.')
hipsIsakmpPolLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 3, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsIsakmpPolLifetime.setStatus('current')
if mibBuilder.loadTexts: hipsIsakmpPolLifetime.setDescription('This object indicates the lifetime of the IKE tunnels in seconds.')
hipsStaticCryptomapTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4), )
if mibBuilder.loadTexts: hipsStaticCryptomapTable.setStatus('current')
if mibBuilder.loadTexts: hipsStaticCryptomapTable.setDescription('The table includes the list of the member cryptomaps of the cryptomap sets which are set on the specific entity.')
hipsStaticCryptomapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1), ).setIndexNames((0, "HUAWEI-NDEC-MIB", "hipsStaticCryptomapName"), (0, "HUAWEI-NDEC-MIB", "hipsStaticCryptomapSN"))
if mibBuilder.loadTexts: hipsStaticCryptomapEntry.setStatus('current')
if mibBuilder.loadTexts: hipsStaticCryptomapEntry.setDescription('Each entry contains properites of a single static cryptomap entry. The members of dynamic cryptomap sets, which may be linked with the parent static cryptomap set, are not included in this table.')
hipsStaticCryptomapName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsStaticCryptomapName.setStatus('current')
if mibBuilder.loadTexts: hipsStaticCryptomapName.setDescription('The name of the cryptomap entry in the cryptomap set. This is the first index component of this table.')
hipsStaticCryptomapSN = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsStaticCryptomapSN.setStatus('current')
if mibBuilder.loadTexts: hipsStaticCryptomapSN.setDescription('The sequence number of the cryptomap entry in the cryptomap set. This is the second index component of this table.')
hipsStaticCryptomapNegMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("isakmp", 2), ("manual", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsStaticCryptomapNegMode.setStatus('current')
if mibBuilder.loadTexts: hipsStaticCryptomapNegMode.setDescription('Type of the cryptomap entry. This object may be an ISAKMP cryptomap or manual.')
hipsStaticCryptomapMatchAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsStaticCryptomapMatchAddr.setStatus('current')
if mibBuilder.loadTexts: hipsStaticCryptomapMatchAddr.setDescription('The access list number entered by the operatoir while creating this cryptomap. ')
hipsStaticCryptomapPeerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsStaticCryptomapPeerIpAddr.setStatus('current')
if mibBuilder.loadTexts: hipsStaticCryptomapPeerIpAddr.setDescription('The IP address of the current peer. Traffic protected by this cryptomap is protected by a tunnel terminating at the device whose IP address is the value of this object.')
hipsStaticCryptomapTransforName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsStaticCryptomapTransforName.setStatus('current')
if mibBuilder.loadTexts: hipsStaticCryptomapTransforName.setDescription('The transform associated with this cryptomap entry.')
hipsStaticCryptomapLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsStaticCryptomapLifetime.setStatus('current')
if mibBuilder.loadTexts: hipsStaticCryptomapLifetime.setDescription('This object indicates the lifetime of the IPSec SA which is created using this IPSec policy entry.')
hipsStaticCryptomapLifesize = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsStaticCryptomapLifesize.setStatus('current')
if mibBuilder.loadTexts: hipsStaticCryptomapLifesize.setDescription('This object identifies the lifesize of the IPSec SAs generated using this IPSec policy entry. Lifesize means maximum traffic in bytes that may be carried. ')
hipsStaticCryptomapLocalIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsStaticCryptomapLocalIpAddr.setStatus('current')
if mibBuilder.loadTexts: hipsStaticCryptomapLocalIpAddr.setDescription('The value of this object is the local IP address of the IPSec SAs generated using this IPSec policy entry. ')
hipsIfNameUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsIfNameUsed.setStatus('current')
if mibBuilder.loadTexts: hipsIfNameUsed.setDescription('This object indicates the name of the interface which uses this IPSec policy entry. ')
hipsInAHSPI = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsInAHSPI.setStatus('current')
if mibBuilder.loadTexts: hipsInAHSPI.setDescription('This object indicates the inbound AH SPI IPSec SAs generated using this IPSec policy entry.')
hipsInESPSPI = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsInESPSPI.setStatus('current')
if mibBuilder.loadTexts: hipsInESPSPI.setDescription('This object indicates the inbound ESP SPI IPSec SAs generated using this IPSec policy entry. ')
hipsOutAHSPI = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsOutAHSPI.setStatus('current')
if mibBuilder.loadTexts: hipsOutAHSPI.setDescription('This object indicates the outbound AH SPI IPSec SAs generated using this IPSec policy entry. ')
hipsOutESPSPI = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsOutESPSPI.setStatus('current')
if mibBuilder.loadTexts: hipsOutESPSPI.setDescription('This object indicates the outbound ESP SPI IPSec SAs generated using this IPSec policy entry. ')
hipsInAhHexKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsInAhHexKeyString.setStatus('current')
if mibBuilder.loadTexts: hipsInAhHexKeyString.setDescription('This object indicates the inbound AH authentication key IPSec SAs generated using this IPSec policy entry. The AH authentication key is in hex. ')
hipsInEspCipherHexKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsInEspCipherHexKeyString.setStatus('current')
if mibBuilder.loadTexts: hipsInEspCipherHexKeyString.setDescription('This object indicates the inbound ESP authentication key IPSec SAs generated using this IPSec policy entry. The ESP authentication key is hex. ')
hipsInEspAuthenHexKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsInEspAuthenHexKeyString.setStatus('current')
if mibBuilder.loadTexts: hipsInEspAuthenHexKeyString.setDescription('This object indicates the inbound ESP authentication key IPSec SAs generated using this IPSec policy entry. The ESP authentication key is hex. ')
hipsInAhStringKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsInAhStringKeyString.setStatus('current')
if mibBuilder.loadTexts: hipsInAhStringKeyString.setDescription('This object indicates the inbound ESP authentication key IPSec SAs generated using this IPSec policy entry. The key is in string. ')
hipsInEspStringKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsInEspStringKeyString.setStatus('current')
if mibBuilder.loadTexts: hipsInEspStringKeyString.setDescription('This object indicates the inbound ESP authentication key IPSec SAs generated using this IPSec policy entry. The key is in string. ')
hipsOutAhHexKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsOutAhHexKeyString.setStatus('current')
if mibBuilder.loadTexts: hipsOutAhHexKeyString.setDescription('This object indicates the outbound AH authentication key IPSec SAs generated using this IPSec policy entry. The key is in hex. ')
hipsOutEspCipherHexKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 21), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsOutEspCipherHexKeyString.setStatus('current')
if mibBuilder.loadTexts: hipsOutEspCipherHexKeyString.setDescription('This object indicates the outbound ESP authentication key IPSec SAs generated using this IPSec policy entry. The key is in hex. ')
hipsOutEspAuthenHexKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 22), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsOutEspAuthenHexKeyString.setStatus('current')
if mibBuilder.loadTexts: hipsOutEspAuthenHexKeyString.setDescription('This object indicates the outbound ESP authentication key IPSec SAs generated using this IPSec policy entry. The key is in hex. ')
hipsOutAhStringKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 23), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsOutAhStringKeyString.setStatus('current')
if mibBuilder.loadTexts: hipsOutAhStringKeyString.setDescription('This object indicates the outbound AH authentication key IPSec SAs generated using this IPSec policy entry. The key is in string. ')
hipsOutEspStringKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 4, 1, 24), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsOutEspStringKeyString.setStatus('current')
if mibBuilder.loadTexts: hipsOutEspStringKeyString.setDescription('This object indicates the outbound ESP authentication key IPSec SAs generated using this IPSec policy entry. The key is in string. ')
hipsTransformNameSetTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 5), )
if mibBuilder.loadTexts: hipsTransformNameSetTable.setStatus('current')
if mibBuilder.loadTexts: hipsTransformNameSetTable.setDescription('Transform set table.')
hipsTransformNameSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 5, 1), ).setIndexNames((0, "HUAWEI-NDEC-MIB", "hipsTransformName"))
if mibBuilder.loadTexts: hipsTransformNameSetEntry.setStatus('current')
if mibBuilder.loadTexts: hipsTransformNameSetEntry.setDescription('Each entry refers to properties of a transform.')
hipsTransformName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 5, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsTransformName.setStatus('current')
if mibBuilder.loadTexts: hipsTransformName.setDescription('Name of the transform entry.')
hipsTransformMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tunnel", 1), ("transport", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsTransformMode.setStatus('current')
if mibBuilder.loadTexts: hipsTransformMode.setDescription('Mode of the transform entry.')
hipsTransformProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("ipsecNone", 1), ("ipsecAhNew", 2), ("ipsecAhEspNew", 3), ("ipsecAhEspOld", 4), ("ipsecAhOld", 5), ("ipsecEspNew", 6), ("ipsecEspAhNew", 7), ("ipsecEspAhOld", 8), ("ipsecEspOld", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsTransformProtocol.setStatus('current')
if mibBuilder.loadTexts: hipsTransformProtocol.setDescription('Transform protocol.')
hipsAH = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("aalgNone", 1), ("aalgMd5Hmac", 2), ("aalgSha1Hmac", 3), ("aalgMd5Hmac96", 4), ("aalgSha1Hmac96", 5), ("aalgXRipeMd160Hmac96", 6), ("aalgXMd5", 7), ("aalgXSha1", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsAH.setStatus('current')
if mibBuilder.loadTexts: hipsAH.setDescription('Algorithm of AH protocol.')
hipsEespEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("ealgNone", 1), ("ealgDescbc", 2), ("ealg3desCbc", 3), ("ealgXBlf", 4), ("ealgXCast", 5), ("ealgXSkipjack", 6), ("ealgXAes", 7), ("ealgXQc5", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsEespEn.setStatus('current')
if mibBuilder.loadTexts: hipsEespEn.setDescription('Encryption algorithm of ESP protocol.')
hipsEspAu = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("aalgNone", 1), ("aalgMd5Hmac", 2), ("aalgSha1Hmac", 3), ("aalgMd5Hmac96", 4), ("aalgSha1Hmac96", 5), ("aalgXRipeMd160Hmac96", 6), ("aalgXMd5", 7), ("aalgXSha1", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsEspAu.setStatus('current')
if mibBuilder.loadTexts: hipsEspAu.setDescription('Authentication algorithm of ESP protocol.')
hipsIsCardTransform = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 5, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsIsCardTransform.setStatus('current')
if mibBuilder.loadTexts: hipsIsCardTransform.setDescription('This object indicates the flag of the NDEC is used for IPSec SAs generated using this IPSec policy entry. ')
hipsNDECInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 6), )
if mibBuilder.loadTexts: hipsNDECInfoTable.setStatus('current')
if mibBuilder.loadTexts: hipsNDECInfoTable.setDescription('Table of NDEC set.')
hipsNDECInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 6, 1), ).setIndexNames((0, "HUAWEI-NDEC-MIB", "hipsCardSlot"))
if mibBuilder.loadTexts: hipsNDECInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hipsNDECInfoEntry.setDescription('Properties of each NDEC. ')
hipsCardSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsCardSlot.setStatus('current')
if mibBuilder.loadTexts: hipsCardSlot.setDescription('Slot number of NDEC .')
hipsInPac = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsInPac.setStatus('current')
if mibBuilder.loadTexts: hipsInPac.setDescription('Total packets of the NDEC recieved.')
hipsOutPac = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsOutPac.setStatus('current')
if mibBuilder.loadTexts: hipsOutPac.setDescription('Total packets of the NDEC sent.')
hipsInByte = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsInByte.setStatus('current')
if mibBuilder.loadTexts: hipsInByte.setDescription('Total bytes of the NDEC sent.')
hipsOutByte = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsOutByte.setStatus('current')
if mibBuilder.loadTexts: hipsOutByte.setDescription('Total bytes of the NDEC sent.')
hipsDropPac = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsDropPac.setStatus('current')
if mibBuilder.loadTexts: hipsDropPac.setDescription('Total packets of the NDEC dropped .')
hipsCardStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ecStateInvalid", 1), ("ecStateReady", 2), ("ecStateResetting", 3), ("ecStateProgramUpdating", 4), ("ecStateDisable", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsCardStatus.setStatus('current')
if mibBuilder.loadTexts: hipsCardStatus.setDescription('State of the NDEC.')
hipsCardHardVer = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 6, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsCardHardVer.setStatus('current')
if mibBuilder.loadTexts: hipsCardHardVer.setDescription('Hardware version of the NDEC.')
hipsCardSoftVer = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 6, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsCardSoftVer.setStatus('current')
if mibBuilder.loadTexts: hipsCardSoftVer.setDescription('Software version of the NDEC.')
hipsCardCPLDVer = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 6, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsCardCPLDVer.setStatus('current')
if mibBuilder.loadTexts: hipsCardCPLDVer.setDescription('CPLD version of the NDEC.')
hipsCardOperate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 6, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("cardClearStatic", 1), ("cardReset", 2), ("cardSynTime", 3), ("cardSysLogOn", 4), ("cardSysLogOff", 5), ("cardSysLogClear", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hipsCardOperate.setStatus('current')
if mibBuilder.loadTexts: hipsCardOperate.setDescription("The version of the NDEC's CPLD. cardClearStatic(1): clear the statistics of the card cardReset(2): rest the card cardSynTime(3): synchoronize the clock of the card cardSysLogOn(4):turn on the log of the card cardSysLogOff(5):turn off the log of the card cardSysLogClear(6):clear the log of the card")
hipsDropPacInUnitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 6, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsDropPacInUnitTime.setStatus('current')
if mibBuilder.loadTexts: hipsDropPacInUnitTime.setDescription('Dropped packets in unit interval.')
hipsNDECLeaf = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 7))
hipsNDECConnections = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 7, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsNDECConnections.setStatus('current')
if mibBuilder.loadTexts: hipsNDECConnections.setDescription('Total connections of the system at this time.')
hipsNDECBackup = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 7, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hipsNDECBackup.setStatus('current')
if mibBuilder.loadTexts: hipsNDECBackup.setDescription('The flag that NDEC using backup. The value 1 represents using backup The value 0 represents not using backup')
hipsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 8))
hipsNDECNormalResetTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 8, 1)).setObjects(("HUAWEI-NDEC-MIB", "hipsCardSlot"), ("HUAWEI-NDEC-MIB", "hipsCardHardVer"), ("HUAWEI-NDEC-MIB", "hipsCardSoftVer"), ("HUAWEI-NDEC-MIB", "hipsCardCPLDVer"))
if mibBuilder.loadTexts: hipsNDECNormalResetTrap.setStatus('current')
if mibBuilder.loadTexts: hipsNDECNormalResetTrap.setDescription('This trap is generated when the NDEC card is reset.')
hipsNDECStateChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 8, 2)).setObjects(("HUAWEI-NDEC-MIB", "hipsCardSlot"), ("HUAWEI-NDEC-MIB", "hipsCardStatus"))
if mibBuilder.loadTexts: hipsNDECStateChangeTrap.setStatus('current')
if mibBuilder.loadTexts: hipsNDECStateChangeTrap.setDescription("This trap is generated when the NDEC card's state changes.")
hipsNDECFlowTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 2, 8, 3)).setObjects(("HUAWEI-NDEC-MIB", "hipsCardSlot"), ("HUAWEI-NDEC-MIB", "hipsDropPacInUnitTime"))
if mibBuilder.loadTexts: hipsNDECFlowTrap.setStatus('current')
if mibBuilder.loadTexts: hipsNDECFlowTrap.setDescription('This trap is generated when a NDEC card is overloaded.')
mibBuilder.exportSymbols("HUAWEI-NDEC-MIB", hipsCardSlot=hipsCardSlot, hipsPeerIpAddr=hipsPeerIpAddr, hipsNDECSAListEntry=hipsNDECSAListEntry, hipsSoftTimeout=hipsSoftTimeout, hipsByCard=hipsByCard, hipsIsCardTransform=hipsIsCardTransform, hikeClearSA=hikeClearSA, hipsOutESPSPI=hipsOutESPSPI, hipsNDECFlowTrap=hipsNDECFlowTrap, hipsOutAHSPI=hipsOutAHSPI, hipsStaticCryptomapNegMode=hipsStaticCryptomapNegMode, hipsStaticCryptomapLocalIpAddr=hipsStaticCryptomapLocalIpAddr, hipsNDECStateChangeTrap=hipsNDECStateChangeTrap, hipsNDECBackup=hipsNDECBackup, hipsExpBytes=hipsExpBytes, hipsTransformProtocol=hipsTransformProtocol, hipsSoftBytes=hipsSoftBytes, hipsOutEspCipherHexKeyString=hipsOutEspCipherHexKeyString, hipsIKEPolicyEntry=hipsIKEPolicyEntry, hipsSaLifeSecond=hipsSaLifeSecond, hipsNDECSAListTable=hipsNDECSAListTable, hikePeerIpAddr=hikePeerIpAddr, huaweiNDEC=huaweiNDEC, hipsOutEspStringKeyString=hipsOutEspStringKeyString, hipsTraps=hipsTraps, hipsIsakmpPolEncr=hipsIsakmpPolEncr, hipsStaticCryptomapEntry=hipsStaticCryptomapEntry, hipsTransformMode=hipsTransformMode, hipsIKEPolicyTable=hipsIKEPolicyTable, hipsSPI=hipsSPI, hipsStaticCryptomapPeerIpAddr=hipsStaticCryptomapPeerIpAddr, hipsLocalIpAddr=hipsLocalIpAddr, hikeSATable=hikeSATable, hipsNegotiateSaMode=hipsNegotiateSaMode, hipsTransformNameSetTable=hipsTransformNameSetTable, hipsOutByte=hipsOutByte, PYSNMP_MODULE_ID=huaweiNDEC, hikeSAEntry=hikeSAEntry, hipsDropPacInUnitTime=hipsDropPacInUnitTime, hikeConnId=hikeConnId, hipsStaticCryptomapLifesize=hipsStaticCryptomapLifesize, hipsTransformNameSetEntry=hipsTransformNameSetEntry, hipsInByte=hipsInByte, hikePhase=hikePhase, hikeDoi=hikeDoi, hipsTransformName=hipsTransformName, hipsEespEn=hipsEespEn, hipsNDECInfoEntry=hipsNDECInfoEntry, hipsExpTimeout=hipsExpTimeout, hipsCardCPLDVer=hipsCardCPLDVer, hipsInAhStringKeyString=hipsInAhStringKeyString, hipsCardOperate=hipsCardOperate, hipsInEspAuthenHexKeyString=hipsInEspAuthenHexKeyString, hipsInAhHexKeyString=hipsInAhHexKeyString, hipsEncAlgorithm=hipsEncAlgorithm, hipsInEspCipherHexKeyString=hipsInEspCipherHexKeyString, hipsNDECNormalResetTrap=hipsNDECNormalResetTrap, hipsStaticCryptomapSN=hipsStaticCryptomapSN, hipsNDECInfoTable=hipsNDECInfoTable, hipsStaticCryptomapTransforName=hipsStaticCryptomapTransforName, hipsCardStatus=hipsCardStatus, hipsOutPac=hipsOutPac, hipsStaticCryptomapLifetime=hipsStaticCryptomapLifetime, hipsIsakmpPolAuth=hipsIsakmpPolAuth, hipsIfNameUsed=hipsIfNameUsed, hipsOutAhStringKeyString=hipsOutAhStringKeyString, hipsOutAhHexKeyString=hipsOutAhHexKeyString, hipsInESPSPI=hipsInESPSPI, hipsInPac=hipsInPac, hipsProtocol=hipsProtocol, hipsInAHSPI=hipsInAHSPI, hikeFlag=hikeFlag, hipsCardHardVer=hipsCardHardVer, hipsCardSoftVer=hipsCardSoftVer, hipsStaticCryptomapTable=hipsStaticCryptomapTable, hipsNDECConnections=hipsNDECConnections, hipsIsakmpPolLifetime=hipsIsakmpPolLifetime, hipsSaLifeKBytes=hipsSaLifeKBytes, hipsOutEspAuthenHexKeyString=hipsOutEspAuthenHexKeyString, hipsIsakmpPolPriority=hipsIsakmpPolPriority, hipsInEspStringKeyString=hipsInEspStringKeyString, hipsStaticCryptomapName=hipsStaticCryptomapName, hipsEspAu=hipsEspAu, hipsStaticCryptomapMatchAddr=hipsStaticCryptomapMatchAddr, hipsNDECLeaf=hipsNDECLeaf, hipsAH=hipsAH, hipsIsakmpPolHash=hipsIsakmpPolHash, hipsAuthAlgorithm=hipsAuthAlgorithm, hipsDropPac=hipsDropPac, hipsIsakmpPolGroup=hipsIsakmpPolGroup)