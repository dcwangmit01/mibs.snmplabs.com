#
# PySNMP MIB module CISCO-COMMON-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-COMMON-MGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:53:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
usmNoPrivProtocol, usmNoAuthProtocol = mibBuilder.importSymbols("SNMP-USER-BASED-SM-MIB", "usmNoPrivProtocol", "usmNoAuthProtocol")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, ObjectIdentity, Counter32, NotificationType, TimeTicks, dod, Gauge32, Counter64, Integer32, Bits, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Counter32", "NotificationType", "TimeTicks", "dod", "Gauge32", "Counter64", "Integer32", "Bits", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress")
DisplayString, TextualConvention, AutonomousType, DateAndTime, RowStatus, StorageType, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "AutonomousType", "DateAndTime", "RowStatus", "StorageType", "TruthValue")
ciscoCommonMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 443))
ciscoCommonMgmtMIB.setRevisions(('2008-06-13 00:00', '2005-06-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCommonMgmtMIB.setRevisionsDescriptions(("Added the following. - New mib object 'ccmCommonUserCacheTimeout'. - New Compliance 'ciscoCommonMgmtMIBCompliances' - New Object Group 'ccmCacheTimeoutConfigGroup'.", 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCommonMgmtMIB.setLastUpdated('200806130000Z')
if mibBuilder.loadTexts: ciscoCommonMgmtMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoCommonMgmtMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 -NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoCommonMgmtMIB.setDescription('MIB module for integrating different elements of managing a device. For example, different device access methods like SNMP, CLI, XML and so on have different set of users which are used to communicate with the device. The ccmCommonUserTable provides framework to create one set of users which is common across all the device access methods. So, this MIB serves as a framework to integrate management of different access methods.')
ciscoCommonMgmtNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 443, 0))
ciscoCommonMgmtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 443, 1))
ciscoCommonMgmtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 443, 2))
ccmUserConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1))
ccmCommonMaxUsers = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCommonMaxUsers.setStatus('current')
if mibBuilder.loadTexts: ccmCommonMaxUsers.setDescription('Maximum number of common users that can be configured on this device. i.e., the maximum number of entries in the ccmCommonUserTable. 0 means maximum number of users is dynamically determined, e.g., depending on memory availability.')
ccmCommonUsers = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCommonUsers.setStatus('current')
if mibBuilder.loadTexts: ccmCommonUsers.setDescription('Number of common users that are currently configured on this device. i.e., the number of entries in the ccmCommonUserTable.')
ccmCommonUsersGlobalEnforcePriv = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmCommonUsersGlobalEnforcePriv.setStatus('current')
if mibBuilder.loadTexts: ccmCommonUsersGlobalEnforcePriv.setDescription("This object specifies whether the SNMP agent enforces the use of encryption for SNMPv3 messages globally on all the users in the system. The 'vacmAccessSecurityLevel' determines the acceptable security levels per group and is set to noAuthnoPriv default unless otherwise configured. The actual access to the mib objects in a SNMP message is controlled by vacmAccessTable. This object provides the configuration at a higher level to enforce privacy without any introspection of the mib objects in the SNMP message. When the privacy is enforced globally, for any SNMPv3 PDU request with securityLevel of either 'noAuthNoPriv' and 'authNoPriv', the SNMP agent responds with an 'authorizationError'.")
ccmCommonUserLastChange = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCommonUserLastChange.setStatus('current')
if mibBuilder.loadTexts: ccmCommonUserLastChange.setDescription('The local date and time when the user database - ccmCommonUserTable configuration was last changed. This object will be set to zero on power cycle or on reboot of the system. Also, if the clock is changed on local system it is set to zero.')
ccmCommonUserTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5), )
if mibBuilder.loadTexts: ccmCommonUserTable.setStatus('current')
if mibBuilder.loadTexts: ccmCommonUserTable.setDescription("This table lists all the common users configured on this device. A common user is a user who is common across SNMP, CLI and other device access methods. Certain access methods might need the user created to be standard compliant. For example - for SNMP, the user created need to be compliant to RFC 3414 (SNMP-USER-BASED-SM-MIB). When a common user is created in this table, a corresponding SNMP user is created in the 'usmUserTable' with corresponding instance of usmUserStorageType set to readOnly . Similarly when a common user is deleted from this table, the corresponding entry in the 'usmUserTable' is deleted.")
ccmCommonUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5, 1), ).setIndexNames((0, "CISCO-COMMON-MGMT-MIB", "ccmCommonUserName"))
if mibBuilder.loadTexts: ccmCommonUserEntry.setStatus('current')
if mibBuilder.loadTexts: ccmCommonUserEntry.setDescription('An entry (conceptual row) in the ccmCommonUserTable.')
ccmCommonUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: ccmCommonUserName.setStatus('current')
if mibBuilder.loadTexts: ccmCommonUserName.setDescription('Name of the common user.')
ccmCommonUserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5, 1, 2), DisplayString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccmCommonUserPassword.setStatus('current')
if mibBuilder.loadTexts: ccmCommonUserPassword.setDescription('Password of the common user. For SNMP, this password is used for both authentication and privacy. For CLI and XML, it is used for authentication only. A zero-length string is always returned when this object is read.')
ccmCommonUserExpiryDate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5, 1, 3), DateAndTime().clone(hexValue="0000000000000000000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccmCommonUserExpiryDate.setStatus('current')
if mibBuilder.loadTexts: ccmCommonUserExpiryDate.setDescription("The date on which this user will expire. Note that non-date related octets in this object are ignored. If the all the date related octets have value '00'H, then user never expires.")
ccmCommonUserSshKeyFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccmCommonUserSshKeyFilename.setStatus('current')
if mibBuilder.loadTexts: ccmCommonUserSshKeyFilename.setDescription('The name of the file storing the SSH public key. The SSH public key is used to authenticate the SSH session for this user. Note that this object applies to only CLI user. The content within SSH Key file can be one of the following: - SSH Public Key in OpenSSH format - SSH Public Key in IETF SECSH (Commercial SSH public key format) - SSH Client Certificate in PEM (privacy-enhanced mail format) from which the public key will be extracted - SSH Client Certificate DN (Distinguished Name) for certificate based authentication This object is used to configure the SSH public key for a user. When this object is read, the agent may return a zero length string. However, the value of the corresponding instance of ccmCommonUserSshKeyConfigured should indicate if the key is configured or not.')
ccmCommonUserSshKeyConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCommonUserSshKeyConfigured.setStatus('current')
if mibBuilder.loadTexts: ccmCommonUserSshKeyConfigured.setDescription("This object specifies whether the user corresponding to this entry is configured with SSH public key. The value of 'true' indicates that the user is configured with SSH public key. The value of 'false' indicates the user is not configured with SSH public key.")
ccmCommonUserSNMPAuthProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5, 1, 6), AutonomousType().clone((1, 3, 6, 1, 6, 3, 10, 1, 1, 1))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccmCommonUserSNMPAuthProtocol.setStatus('current')
if mibBuilder.loadTexts: ccmCommonUserSNMPAuthProtocol.setDescription("An indication of whether messages sent on behalf of this user to/from the SNMP engine can be authenticated, and if so, the type of authentication protocol which is used. An instance of this object is created concurrently with the creation of any other object instance for the same user (i.e., as part of the processing of the set operation which creates the first object instance in the same conceptual row). If an initial set operation (i.e. at row creation time) tries to set a value for an unknown or unsupported protocol, then a 'wrongValue' error must be returned. Once instantiated, the value of such an instance of this object can only be changed via a set operation to the value of the usmNoAuthProtocol. If a set operation tries to change the value of an existing instance of this object to any value other than usmNoAuthProtocol, then an 'inconsistentValue' error must be returned. If a set operation tries to set the value to the usmNoAuthProtocol while the ccmCommonUserSNMPPrivProtocol value in the same row is not equal to usmNoPrivProtocol, then an 'inconsistentValue' error must be returned. That means that an SNMP command generator application must first ensure that the usmUserPrivProtocol is set to the usmNoPrivProtocol value before it can set the usmUserAuthProtocol value to usmNoAuthProtocol. The value of an instance of this object directly maps to a corresponding instance of usmUserAuthProtocol in the usmUserTable.")
ccmCommonUserSNMPPrivProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5, 1, 7), AutonomousType().clone((1, 3, 6, 1, 6, 3, 10, 1, 2, 1))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccmCommonUserSNMPPrivProtocol.setStatus('current')
if mibBuilder.loadTexts: ccmCommonUserSNMPPrivProtocol.setDescription("An indication of whether messages sent on behalf of this user to/from the SNMP engine can be protected from disclosure, and if so, the type of privacy protocol which is used. An instance of this object is created concurrently with the creation of any other object instance for the same user (i.e., as part of the processing of the set operation which creates the first object instance in the same conceptual row). If an initial set operation (i.e. at row creation time) tries to set a value for an unknown or unsupported protocol, then a 'wrongValue' error must be returned. Once instantiated, the value of such an instance of this object can only be changed via a set operation to the value of the usmNoPrivProtocol. If a set operation tries to change the value of an existing instance of this object to any value other than usmNoPrivProtocol, then an 'inconsistentValue' error must be returned. Note that if any privacy protocol is used, then you must also use an authentication protocol. In other words, if usmUserPrivProtocol is set to anything else than usmNoPrivProtocol, then the corresponding instance of usmUserAuthProtocol cannot have a value of usmNoAuthProtocol. If it does, then an 'inconsistentValue' error must be returned. The value of an instance of this object directly maps to a corresponding instance of usmUserPrivProtocol in the usmUserTable.")
ccmCommonUserCredType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("localCredentialStore", 2), ("remoteCredentialStore", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmCommonUserCredType.setStatus('current')
if mibBuilder.loadTexts: ccmCommonUserCredType.setDescription('The type of the credential store of the user. When a row is created in this table by a user, the user entry is created in a credential store local to the device. In case of remote authentication mechanism like AAA Server based authentication, credentials are stored in other(remote) system/device.')
ccmCommonUserStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5, 1, 9), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccmCommonUserStorageType.setStatus('current')
if mibBuilder.loadTexts: ccmCommonUserStorageType.setDescription("The storage type for this conceptual row. Conceptual rows having the value 'permanent' need not allow write-access to any columnar objects in the row.")
ccmCommonUserRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccmCommonUserRowStatus.setStatus('current')
if mibBuilder.loadTexts: ccmCommonUserRowStatus.setDescription('Status of the user.')
ccmCommonUserRoleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 6), )
if mibBuilder.loadTexts: ccmCommonUserRoleTable.setStatus('current')
if mibBuilder.loadTexts: ccmCommonUserRoleTable.setDescription('This table provides a mechanism to map a common user represented by ccmCommonUserName to one or more roles. These roles provide access control policies for a principal. Note that all the roles used in the this table have to be present in the commonRoleTable of CISCO-COMMON-ROLES-MIB. For Common User - Role assignments created in this table, for SNMP user access, the corresponding entries are created in the vacmSecurityToGroupTable (of SNMP-VIEW-BASED-ACM-MIB) in line with View-based Access Control Model (RFC3415) and cvacmSecurityToGroupTable (of CISCO-SNMP-VACM-EXT-MIB) to represent all the mappings. All such instances in SNMP tables are created with corresponding StorageType set to readOnly. Note that it is not necessary to update this table if the user-role mapping data is changed using corresponding access methods. e.g., if the SNMPv3 user-group mapping using vacmSecurityToGroupTable and cvacmSecurityToGroupTable is changed, it is not necessary to reflect that change in this table.')
ccmCommonUserRoleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 6, 1), ).setIndexNames((0, "CISCO-COMMON-MGMT-MIB", "ccmCommonUserName"), (0, "CISCO-COMMON-MGMT-MIB", "ccmCommonUserRoleName"))
if mibBuilder.loadTexts: ccmCommonUserRoleEntry.setStatus('current')
if mibBuilder.loadTexts: ccmCommonUserRoleEntry.setDescription('An entry (conceptual row) in the ccmCommonUserRoleTable.')
ccmCommonUserRoleName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 6, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: ccmCommonUserRoleName.setStatus('current')
if mibBuilder.loadTexts: ccmCommonUserRoleName.setDescription('Name of the role.')
ccmCommonUserRoleStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 6, 1, 2), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccmCommonUserRoleStorageType.setStatus('current')
if mibBuilder.loadTexts: ccmCommonUserRoleStorageType.setDescription("The storage type for this conceptual row. Conceptual rows having the value 'permanent' need not allow write-access to any columnar objects in the row.")
ccmCommonUserRoleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 6, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccmCommonUserRoleRowStatus.setStatus('current')
if mibBuilder.loadTexts: ccmCommonUserRoleRowStatus.setDescription('Status of the role list entry.')
ccmCommonUserCacheTimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 86400))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmCommonUserCacheTimeout.setStatus('current')
if mibBuilder.loadTexts: ccmCommonUserCacheTimeout.setDescription("This object specifies maximum timeout value for caching the user credentials in the local system. Such caching is used in remote authentication mechanism like AAA Server based authentication. This applies to the common user entries as represented by 'ccmCommonUserTable' where the value of 'ccmCommonUserCredType' is 'remoteCredentialStore'.")
ciscoCommonMgmtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 443, 2, 1))
ciscoCommonMgmtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 443, 2, 2))
ciscoCommonMgmtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 443, 2, 1, 1)).setObjects(("CISCO-COMMON-MGMT-MIB", "ccmConfigurationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCommonMgmtMIBCompliance = ciscoCommonMgmtMIBCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: ciscoCommonMgmtMIBCompliance.setDescription('The compliance statement for entities which implement the CISCO-COMMON-MGMT-MIB.')
ciscoCommonMgmtMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 443, 2, 1, 2)).setObjects(("CISCO-COMMON-MGMT-MIB", "ccmConfigurationGroup"), ("CISCO-COMMON-MGMT-MIB", "ccmCacheTimeoutConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCommonMgmtMIBCompliance1 = ciscoCommonMgmtMIBCompliance1.setStatus('current')
if mibBuilder.loadTexts: ciscoCommonMgmtMIBCompliance1.setDescription('The compliance statement for entities which implement the CISCO-COMMON-MGMT-MIB.')
ccmConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 443, 2, 2, 1)).setObjects(("CISCO-COMMON-MGMT-MIB", "ccmCommonMaxUsers"), ("CISCO-COMMON-MGMT-MIB", "ccmCommonUsers"), ("CISCO-COMMON-MGMT-MIB", "ccmCommonUsersGlobalEnforcePriv"), ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserLastChange"), ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserPassword"), ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserExpiryDate"), ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserSshKeyFilename"), ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserSshKeyConfigured"), ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserSNMPAuthProtocol"), ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserSNMPPrivProtocol"), ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserCredType"), ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserStorageType"), ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserRowStatus"), ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserRoleStorageType"), ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserRoleRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccmConfigurationGroup = ccmConfigurationGroup.setStatus('current')
if mibBuilder.loadTexts: ccmConfigurationGroup.setDescription('A collection of objects for Common Management configuration.')
ccmCacheTimeoutConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 443, 2, 2, 2)).setObjects(("CISCO-COMMON-MGMT-MIB", "ccmCommonUserCacheTimeout"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccmCacheTimeoutConfigGroup = ccmCacheTimeoutConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ccmCacheTimeoutConfigGroup.setDescription('A collection of objects for configuring timeout value for caching the user credentials in the local system.')
mibBuilder.exportSymbols("CISCO-COMMON-MGMT-MIB", ccmCommonUserRoleName=ccmCommonUserRoleName, ccmCommonUserRoleTable=ccmCommonUserRoleTable, ccmCommonUserStorageType=ccmCommonUserStorageType, ccmCommonUserRoleRowStatus=ccmCommonUserRoleRowStatus, ccmCommonUserName=ccmCommonUserName, ccmCommonUserSshKeyFilename=ccmCommonUserSshKeyFilename, ccmCommonUserLastChange=ccmCommonUserLastChange, ccmCommonUserPassword=ccmCommonUserPassword, ccmCommonUserRoleEntry=ccmCommonUserRoleEntry, ccmCommonUserSNMPAuthProtocol=ccmCommonUserSNMPAuthProtocol, ccmCommonUserCredType=ccmCommonUserCredType, ccmCommonUserRoleStorageType=ccmCommonUserRoleStorageType, ccmConfigurationGroup=ccmConfigurationGroup, ciscoCommonMgmtMIB=ciscoCommonMgmtMIB, ciscoCommonMgmtMIBCompliance1=ciscoCommonMgmtMIBCompliance1, ccmCommonMaxUsers=ccmCommonMaxUsers, ccmCommonUsers=ccmCommonUsers, ccmCommonUserSNMPPrivProtocol=ccmCommonUserSNMPPrivProtocol, ccmCommonUserSshKeyConfigured=ccmCommonUserSshKeyConfigured, ciscoCommonMgmtMIBObjects=ciscoCommonMgmtMIBObjects, ccmCommonUserEntry=ccmCommonUserEntry, ciscoCommonMgmtMIBGroups=ciscoCommonMgmtMIBGroups, ccmCommonUserRowStatus=ccmCommonUserRowStatus, ciscoCommonMgmtMIBCompliance=ciscoCommonMgmtMIBCompliance, ccmCommonUserTable=ccmCommonUserTable, ccmCommonUserCacheTimeout=ccmCommonUserCacheTimeout, ciscoCommonMgmtNotifs=ciscoCommonMgmtNotifs, ciscoCommonMgmtMIBConform=ciscoCommonMgmtMIBConform, ccmCacheTimeoutConfigGroup=ccmCacheTimeoutConfigGroup, ccmUserConfig=ccmUserConfig, ccmCommonUsersGlobalEnforcePriv=ccmCommonUsersGlobalEnforcePriv, ciscoCommonMgmtMIBCompliances=ciscoCommonMgmtMIBCompliances, ccmCommonUserExpiryDate=ccmCommonUserExpiryDate, PYSNMP_MODULE_ID=ciscoCommonMgmtMIB)