#
# PySNMP MIB module CISCO-MGX82XX-CARD-FEATURE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MGX82XX-CARD-FEATURE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:07:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
cardSpecific, = mibBuilder.importSymbols("BASIS-MIB", "cardSpecific")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, Counter32, ModuleIdentity, ObjectIdentity, MibIdentifier, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, Integer32, Bits, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "Integer32", "Bits", "Counter64", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMgx82xxCardFeatureMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 74))
ciscoMgx82xxCardFeatureMIB.setRevisions(('2003-05-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMgx82xxCardFeatureMIB.setRevisionsDescriptions(('Initial version of the MIB. The content of this MIB was originally available in CISCO-WAN-AXIPOP-MIB defined using SMIv1. The applicable objects from CISCO-WAN-AXIPOP-MIB are defined using SMIv2 in this MIB. Also the descriptions of some of the objects have been modified.',))
if mibBuilder.loadTexts: ciscoMgx82xxCardFeatureMIB.setLastUpdated('200305050000Z')
if mibBuilder.loadTexts: ciscoMgx82xxCardFeatureMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMgx82xxCardFeatureMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoMgx82xxCardFeatureMIB.setDescription('The MIB module which describes the features supported in MGX82XX products. This MIB Module provides the features supported in Controller Cards in MGX8250 and MGX8220. Terminologies used: PXM : Processor Switch Module. This is controller card in MGX8250. ASC : AXIS Shelf Controller. This is controller card in MGX8220. VSI : Virtual Switch Interface, a hardware-independent switch control protocol. This allows a Switch to be controlled by a multiple controllers such as PNNI, MPLS. These control planes can be internal or external to the switch.The VSI interface defines the messages and associated functions which allow communication between the controller and the switch.This interface is expected to support all types of connections (voice,data,frame relay,ATM) for PVCs, SPVCs and SVCs. Controller - Software ( and possibly hardware) which manages topology and network resources and performs VSI Master function. This performs source routing for end-to-end SVCs, including general call acceptance GCAC,setup calls with other controllers. PNNI and MPLS are examples of controllers.')
ascFeatures = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 3, 5))
pxmFeatures = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 3, 15))
coreCardCommands = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 3, 20))
vsiControllersAllowed = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 15, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiControllersAllowed.setStatus('current')
if mibBuilder.loadTexts: vsiControllersAllowed.setDescription('This respesents bit map of the VSI Controllers supported. The bit positions are : BIT 0 - PAR(Portable AutoRoute Controller) BIT 1 - PNNI(Private network to network Interface) BIT 2 - TAG(Tag Switching or MPLS Controller) (e.g. A value of 1 in BIT 0 indicates the presence of PAR ) Remaining bits are set to 0.')
apsCardAttributes = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 15, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsCardAttributes.setStatus('current')
if mibBuilder.loadTexts: apsCardAttributes.setDescription('This respesents bit map of the APS card attributes supported. The bit position supported are: BITs 0, 1 - unused BIT 2 - APS standard protocol configured (1 = TRUE ; 0 = FALSE) BIT 3, 4 ,5 - unused BIT 6 - Card HW supports APS 1+1 on two cards (1 = TRUE ; 0 = FALSE) BIT 7 - Card FW supports APS (1 = TRUE ; 0 = FALSE) Remaining bits are set to 0.')
trkCACEnable = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 15, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkCACEnable.setStatus('current')
if mibBuilder.loadTexts: trkCACEnable.setDescription('This MIB variable allows to add a new connection on the feeder trunk even if it is over-subscribed.')
pxmCardCacMode = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 15, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pcrBasedCac", 1), ("scrBasedCac", 2))).clone('pcrBasedCac')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pxmCardCacMode.setStatus('current')
if mibBuilder.loadTexts: pxmCardCacMode.setDescription('This object identifies the CAC mode set on a card. If this is set to pcrBasedCAC(1) then the CAC calculations will be done based on PCR on the connection. If this set to scrBasedCAC(2) then the CAC calculations are done based on the scr of the connections. This will be applicable only if CAC is enabled (i.e trkCACEnable is set to enable(2)).')
redundancyAllowed = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("redNotAllowed", 1), ("redAllowed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyAllowed.setStatus('current')
if mibBuilder.loadTexts: redundancyAllowed.setDescription('This object identifies whether redundancy is allowed in MGX82XX shelf.')
switchCoreCard = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 20, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noAction", 1), ("doswitchcc", 2), ("instswitchcc", 3), ("fallbackswitchcc", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: switchCoreCard.setStatus('current')
if mibBuilder.loadTexts: switchCoreCard.setDescription('This object is used for performing switchover of core card set. The core card set includes Controller Card and Service Redundancy Module(SRM). The possible values are : noAction (1): No operation doswitchcc (2): Perform switchover operation instswitchcc (3): Perform switchover operation fallbackswitchcc(4): ')
cmCardFeatureMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 74, 2))
cmCardFeatureMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 1))
cmCardFeatureMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 2))
cmCardFeatureCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 2, 1)).setObjects(("CISCO-MGX82XX-CARD-FEATURE-MIB", "cmPxmCardFeatureGroup"), ("CISCO-MGX82XX-CARD-FEATURE-MIB", "cmAscCardFeatureGroup"), ("CISCO-MGX82XX-CARD-FEATURE-MIB", "cmCoreCardFeatureGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmCardFeatureCompliance = cmCardFeatureCompliance.setStatus('current')
if mibBuilder.loadTexts: cmCardFeatureCompliance.setDescription('The compliance statement for objects related to Frame Relay Ports.')
cmPxmCardFeatureGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 1, 1)).setObjects(("CISCO-MGX82XX-CARD-FEATURE-MIB", "vsiControllersAllowed"), ("CISCO-MGX82XX-CARD-FEATURE-MIB", "apsCardAttributes"), ("CISCO-MGX82XX-CARD-FEATURE-MIB", "trkCACEnable"), ("CISCO-MGX82XX-CARD-FEATURE-MIB", "pxmCardCacMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPxmCardFeatureGroup = cmPxmCardFeatureGroup.setStatus('current')
if mibBuilder.loadTexts: cmPxmCardFeatureGroup.setDescription('The collection of objects which are used to represent Processor Module(PXM) Features.')
cmAscCardFeatureGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 1, 2)).setObjects(("CISCO-MGX82XX-CARD-FEATURE-MIB", "redundancyAllowed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAscCardFeatureGroup = cmAscCardFeatureGroup.setStatus('current')
if mibBuilder.loadTexts: cmAscCardFeatureGroup.setDescription('The collection of objects which are used to represent Axis Shelf Controller(ASC) Features.')
cmCoreCardFeatureGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 1, 3)).setObjects(("CISCO-MGX82XX-CARD-FEATURE-MIB", "switchCoreCard"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmCoreCardFeatureGroup = cmCoreCardFeatureGroup.setStatus('current')
if mibBuilder.loadTexts: cmCoreCardFeatureGroup.setDescription('The collection of objects which are used to represent core card related objects.')
mibBuilder.exportSymbols("CISCO-MGX82XX-CARD-FEATURE-MIB", ciscoMgx82xxCardFeatureMIB=ciscoMgx82xxCardFeatureMIB, PYSNMP_MODULE_ID=ciscoMgx82xxCardFeatureMIB, cmAscCardFeatureGroup=cmAscCardFeatureGroup, cmCardFeatureMIBConformance=cmCardFeatureMIBConformance, cmCardFeatureMIBCompliances=cmCardFeatureMIBCompliances, coreCardCommands=coreCardCommands, pxmCardCacMode=pxmCardCacMode, cmPxmCardFeatureGroup=cmPxmCardFeatureGroup, switchCoreCard=switchCoreCard, cmCardFeatureCompliance=cmCardFeatureCompliance, apsCardAttributes=apsCardAttributes, pxmFeatures=pxmFeatures, trkCACEnable=trkCACEnable, redundancyAllowed=redundancyAllowed, vsiControllersAllowed=vsiControllersAllowed, cmCoreCardFeatureGroup=cmCoreCardFeatureGroup, cmCardFeatureMIBGroups=cmCardFeatureMIBGroups, ascFeatures=ascFeatures)