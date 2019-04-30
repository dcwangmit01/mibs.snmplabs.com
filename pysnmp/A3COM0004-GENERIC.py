#
# PySNMP MIB module A3COM0004-GENERIC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM0004-GENERIC
# Produced by pysmi-0.3.4 at Mon Apr 29 16:53:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
generic, = mibBuilder.importSymbols("A3Com-products-MIB", "generic")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, IpAddress, MibIdentifier, TimeTicks, NotificationType, ObjectIdentity, Counter32, Integer32, iso, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "MibIdentifier", "TimeTicks", "NotificationType", "ObjectIdentity", "Counter32", "Integer32", "iso", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
setup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 2))
sysLoader = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 3))
security = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 4))
gauges = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 5))
asciiAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 6))
serialIf = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 7))
repeaterMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 8))
endStation = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 9))
localSnmp = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 10))
manager = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 11))
unusedGeneric12 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 12))
chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 14))
mrmResilience = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 15))
tokenRing = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 16))
multiRepeater = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 17))
bridgeMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 18))
fault = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 19))
poll = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 20))
powerSupply = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 21))
securePort = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 22))
alertLed = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 23))
remoteControl = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 24))
rmonExtensions = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 25))
rfc1516extensions = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 26))
superStackIIconfig = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 27))
extendedIfInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 28))
a3ComVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 29))
vlanServerClient = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 30))
segmentLoadBalancing = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 31))
virtualFileSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 32))
smartAutosensing = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 33))
brasica2 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 34))
smaVlanSupport = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 35))
a3ComBridgeExt = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 36))
igmpMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 37))
mibSummary = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 38))
qosProfiles = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 39))
l4Redirect = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 40))
a3ComTrafficStats = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 41))
a3ComRadiusMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 42))
a3ComBackup_mib = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 43)).setLabel("a3ComBackup-mib")
a3comLicenseGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 44))
a3ComPowerEthernetExt = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 45))
mibBuilder.exportSymbols("A3COM0004-GENERIC", endStation=endStation, poll=poll, alertLed=alertLed, securePort=securePort, tokenRing=tokenRing, superStackIIconfig=superStackIIconfig, qosProfiles=qosProfiles, extendedIfInfo=extendedIfInfo, repeaterMgmt=repeaterMgmt, mrmResilience=mrmResilience, manager=manager, l4Redirect=l4Redirect, bridgeMgmt=bridgeMgmt, segmentLoadBalancing=segmentLoadBalancing, smaVlanSupport=smaVlanSupport, unusedGeneric12=unusedGeneric12, remoteControl=remoteControl, serialIf=serialIf, smartAutosensing=smartAutosensing, multiRepeater=multiRepeater, vlanServerClient=vlanServerClient, setup=setup, a3comLicenseGroup=a3comLicenseGroup, powerSupply=powerSupply, rfc1516extensions=rfc1516extensions, igmpMIB=igmpMIB, a3ComBridgeExt=a3ComBridgeExt, chassis=chassis, a3ComTrafficStats=a3ComTrafficStats, a3ComPowerEthernetExt=a3ComPowerEthernetExt, mibSummary=mibSummary, sysLoader=sysLoader, gauges=gauges, asciiAgent=asciiAgent, a3ComRadiusMIB=a3ComRadiusMIB, fault=fault, a3ComVlan=a3ComVlan, rmonExtensions=rmonExtensions, localSnmp=localSnmp, security=security, virtualFileSystem=virtualFileSystem, a3ComBackup_mib=a3ComBackup_mib, brasica2=brasica2)