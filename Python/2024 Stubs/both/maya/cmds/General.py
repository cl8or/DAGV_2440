from typing import Union, Optional, List, Tuple, Any

def about(*args, apiVersion: bool = ..., api: bool = ..., application: bool = ..., a: bool = ..., arm64: bool = ..., a64: bool = ..., batch: bool = ..., b: bool = ..., buildDirectory: bool = ..., bd: bool = ..., buildVariant: bool = ..., bv: bool = ..., codeset: bool = ..., cs: bool = ..., compositingManager: bool = ..., cm: bool = ..., connected: bool = ..., cnt: bool = ..., creativeVersion: bool = ..., cre: bool = ..., ctime: bool = ..., cti: bool = ..., currentDate: bool = ..., cd: bool = ..., currentTime: bool = ..., ct: bool = ..., customVersion: bool = ..., cv: bool = ..., customVersionClient: bool = ..., cvc: bool = ..., customVersionMajor: bool = ..., cvm: bool = ..., customVersionMinor: bool = ..., cvn: bool = ..., customVersionString: bool = ..., cvs: bool = ..., cutIdentifier: bool = ..., c: bool = ..., date: bool = ..., d: bool = ..., environmentFile: bool = ..., env: bool = ..., evalVersion: bool = ..., ev: bool = ..., file: bool = ..., f: bool = ..., fontInfo: bool = ..., foi: bool = ..., helpDataDirectory: bool = ..., hdd: bool = ..., installedVersion: bool = ..., iv: bool = ..., ioVersion: bool = ..., io: bool = ..., irix: bool = ..., ir: bool = ..., is64: bool = ..., x64: bool = ..., languageResources: bool = ..., lr: bool = ..., linux: bool = ..., li: bool = ..., linux64: bool = ..., l64: bool = ..., liveUpdate: bool = ..., lu: bool = ..., localizedResourceLocation: bool = ..., lrl: bool = ..., ltVersion: bool = ..., lt: bool = ..., macOS: bool = ..., mac: bool = ..., macOSASi: bool = ..., asi: bool = ..., macOSppc: bool = ..., ppc: bool = ..., macOSx86: bool = ..., x86: bool = ..., majorVersion: bool = ..., mjv: bool = ..., minorVersion: bool = ..., mnv: bool = ..., ntOS: bool = ..., nt: bool = ..., operatingSystem: bool = ..., os: bool = ..., operatingSystemVersion: bool = ..., osv: bool = ..., patchVersion: bool = ..., pv: bool = ..., preferences: bool = ..., pd: bool = ..., product: bool = ..., p: bool = ..., qtVersion: bool = ..., qt: bool = ..., tablet: bool = ..., tab: bool = ..., tabletMode: bool = ..., tm: bool = ..., uiLanguage: bool = ..., uil: bool = ..., uiLanguageForStartup: bool = ..., uis: bool = ..., uiLanguageIsLocalized: bool = ..., uii: bool = ..., uiLocaleLanguage: bool = ..., ull: bool = ..., version: bool = ..., v: bool = ..., win64: bool = ..., w64: bool = ..., windowManager: bool = ..., wm: bool = ..., windows: bool = ..., win: bool = ...) -> Any:
    r"""
    This command displays version information about the application if it is
    executed without flags.  If one of the above flags is specified
    then the specified version information is returned.

    Args:
        apiVersion | api: (create) - Returns the api version.
        application | a: (create) - Returns the application name string.
        arm64 | a64: (create) - Returns true if the CPU is arm64 based.
        batch | b: (create) - Returns true if application is in batch mode.
        buildDirectory | bd: (create) - Returns the build directory string.
        buildVariant | bv: (create) - Returns the build variant string.
        codeset | cs: (create) - Returns a string identifying the codeset (codepage) of the locale that Maya is running in. Example return values include "UTF-8", "ISO-8859-1", "1252". Note that the codeset values and naming conventions are highly platform dependent.  They may differ in format even if they have the same meaning (e.g. "utf8" vs. "UTF-8").
        compositingManager | cm: (create) - On Linux, returns true if there is a compositing manager running; on all other platforms, it always returns true.
        connected | cnt: (create) - Return whether the user is connected or not to the Internet.
        creativeVersion | cre: (create) - Returns true if this is the Maya Creative version of the application.
        ctime | cti: (create) - Returns the current time in the format Wed Jan 02 02:03:55 1980\n\0
        currentDate | cd: (create) - Returns the current date in the format yyyy/mm/dd, e.g. 2003/05/04.
        currentTime | ct: (create) - Returns the current time in the format hh:mm:ss, e.g. 14:27:53.
        customVersion | cv: (create) - Returns true if this is a custom version of Maya.
        customVersionClient | cvc: (create) - Returns the custom client version string for Maya or an empty string if this is not a custom version.
        customVersionMajor | cvm: (create) - Returns the custom major version of Maya or 0 if this is not a custom version.
        customVersionMinor | cvn: (create) - Returns the custom minor version of Maya or 0 if this is not a custom version.
        customVersionString | cvs: (create) - Returns the custom version string for Maya or an empty string if this is not a custom version.
        cutIdentifier | c: (create) - Returns the cut string.
        date | d: (create) - Returns the build date string.
        environmentFile | env: (create) - Returns the location of the application defaults file.
        evalVersion | ev: (create) - This flag is now deprecated. Always returns false, as the eval version is no longer supported.
        file | f: (create) - Returns the file version string.
        fontInfo | foi: (create) - Returns a string of the specifications of the fonts requested, and the specifications of the fonts that are actually being used.
        helpDataDirectory | hdd: (create) - Returns the help data directory.
        installedVersion | iv: (create) - Returns the product version string.
        ioVersion | io: (create) - Returns true if this is the Maya IO version of the application.
        irix | ir: (create) - Returns true if the operating system is Irix. Always false with support for Irix removed.
        is64 | x64: (create) - Returns true if the application is 64 bit.
        languageResources | lr: (create) - Returns a string array of the currently installed language resources. Each string entry consists of three elements delimited with a colon (':'). The first token is the locale code (ISO 639-1 language code followed by ISO 3166-1 country code).  The second token is the language name in English. This third token is the alpha-3 code (ISO 639-2).  For example English is represented as "en_US:English:enu".
        linux | li: (create) - Returns true if the operating system is Linux.
        linux64 | l64: (create) - Returns true if the operating system is Linux 64 bit.
        liveUpdate | lu: (create) - This flag is deprecated(2019) and may be removed in future releases of Maya. Returns Autodesk formatted product information.
        localizedResourceLocation | lrl: (create) - Returns the path to the top level of the localized resource directory, if we are running in an alternate language. Returns an empty string if we are running in the default language.
        ltVersion | lt: (create) - Deprecated. Returns true if this is the Maya LT version of the application.
        macOS | mac: (create) - Returns true if the operating system is Macintosh.
        macOSASi | asi: (create) - Returns true if the operating system is an Apple Silicon Mac.
        macOSppc | ppc: (create) - Returns true if the operating system is a PowerPC Macintosh.
        macOSx86 | x86: (create) - Returns true if the operating system is an Intel Macintosh.
        majorVersion | mjv: (create) - Returns the major version of Maya.
        minorVersion | mnv: (create) - Returns the minor version of Maya.
        ntOS | nt: (create) - Returns true if the operating system is Windows.
        operatingSystem | os: (create) - Returns the operating system type. Valid return types are "nt", "win64", "mac", "linux" and "linux64"
        operatingSystemVersion | osv: (create) - Returns the operating system version. on Linux this returns the equivalent of uname -srvm
        patchVersion | pv: (create) - Returns the patch version of Maya.
        preferences | pd: (create) - Returns the location of the preferences directory.
        product | p: (create) - Returns the license product name.
        qtVersion | qt: (create) - Returns Qt version string.
        tablet | tab: (create) - Windows only.  Returns true if the PC is a Tablet PC.
        tabletMode | tm: (create) - Windows 8 (and above) only.  If your device is a Tablet PC, then the convertible mode the device is currently running in.  Returns  either: tablet or laptop (keyboard attached). See the tablet flag.
        uiLanguage | uil: (create) - Returns the language that Maya's running in.  Example return values include "en_US" for English and "ja_JP" for Japanese.
        uiLanguageForStartup | uis: (create) - Returns the language that is used for Maya's next start up. This is read from config file and is rewritten after setting ui language in preference.
        uiLanguageIsLocalized | uii: (create) - Returns true if we are running in an alternate language, not the default (English).
        uiLocaleLanguage | ull: (create) - Returns the language locale of the OS. English is default.
        version | v: (create) - Returns the version string.
        win64 | w64: (create) - Returns true if the operating system is Windows x64 based.
        windowManager | wm: (create) - Returns the name of the Window Manager that is assumed to be running.
        windows | win: (create) - Returns true if the operating system is Windows based.
    """
    ...


def addAttr(*args, attributeType: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., binaryTag: Optional[Union[str, bool]] = ..., bt: Optional[Union[str, bool]] = ..., cachedInternally: bool = ..., ci: bool = ..., category: Optional[Union[str, bool]] = ..., ct: Optional[Union[str, bool]] = ..., dataType: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., defaultValue: Optional[Union[float, bool]] = ..., dv: Optional[Union[float, bool]] = ..., disconnectBehaviour: Optional[Union[int, bool]] = ..., dcb: Optional[Union[int, bool]] = ..., enumName: Optional[Union[str, bool]] = ..., en: Optional[Union[str, bool]] = ..., exists: bool = ..., ex: bool = ..., fromPlugin: bool = ..., fp: bool = ..., hasMaxValue: bool = ..., hxv: bool = ..., hasMinValue: bool = ..., hnv: bool = ..., hasSoftMaxValue: bool = ..., hsx: bool = ..., hasSoftMinValue: bool = ..., hsn: bool = ..., hidden: bool = ..., h: bool = ..., indexMatters: bool = ..., im: bool = ..., internalSet: bool = ..., keyable: bool = ..., k: bool = ..., longName: Optional[Union[str, bool]] = ..., ln: Optional[Union[str, bool]] = ..., maxValue: Optional[Union[float, bool]] = ..., max: Optional[Union[float, bool]] = ..., minValue: Optional[Union[float, bool]] = ..., min: Optional[Union[float, bool]] = ..., multi: bool = ..., m: bool = ..., niceName: Optional[Union[str, bool]] = ..., nn: Optional[Union[str, bool]] = ..., numberOfChildren: Optional[Union[int, bool]] = ..., nc: Optional[Union[int, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., proxy: Optional[Union[str, bool]] = ..., pxy: Optional[Union[str, bool]] = ..., readable: bool = ..., r: bool = ..., shortName: Optional[Union[str, bool]] = ..., sn: Optional[Union[str, bool]] = ..., softMaxValue: Optional[Union[float, bool]] = ..., smx: Optional[Union[float, bool]] = ..., softMinValue: Optional[Union[float, bool]] = ..., smn: Optional[Union[float, bool]] = ..., storable: bool = ..., s: bool = ..., usedAsColor: bool = ..., uac: bool = ..., usedAsFilename: bool = ..., uaf: bool = ..., usedAsProxy: bool = ..., uap: bool = ..., worldSpace: bool = ..., ws: bool = ..., writable: bool = ..., w: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to add a dynamic attribute to a node or nodes.
    Either the longName or the shortName or both must be specified.
    If neither a dataType nor an attributeType is specified, a double
    attribute will be added.  The dataType flag can be specified more than
    once indicating that any of the supplied types will be accepted (logical-or).
    
    
    To add a non-double attribute the following criteria
    can be used to determine whether the dataType or the attributeType
    flag is appropriate.  Some types, such as double3 can use either.
    In these cases the -dt flag should be used when you only wish to
    access the data as an atomic entity (eg. you never want to access the
    three individual values that make up a double3).  In general it
    is best to use the -at in these cases for maximum flexibility.
    In most cases the -dt version will not display in the attribute
    editor as it is an atomic type and you are not allowed to change
    individual parts of it.
    
    
    All attributes flagged as "(compound)" below or the compound attribute itself
    are not actually added to the node until all of the children are defined
    (using the "-p" flag to set their parent to the compound being created).  See
    the EXAMPLES section for more details.
    
    
    
     Type of attribute               Flag and argument to use      
     boolean                                                 -at bool                      
     32 bit integer                                  -at long                      
     16 bit integer                                  -at short                     
     8 bit integer                                   -at byte                      
     char                                                    -at char                      
      enum                                                   -at enum (specify the enum names using the enumName flag)  
     float                                                   -at "float" (use quotes
                                                                            since float is a mel keyword)   
     double                                                  -at double            
     angle value                                     -at doubleAngle       
     linear value                                    -at doubleLinear      
     string                                                  -dt "string" (use quotes
                                                                            since string is a mel keyword)  
     array of strings                                -dt stringArray       
     compound                                                -at compound          
     message (no data)                               -at message           
     time                                                    -at time                      
     4x4 double matrix                               -dt "matrix" (use quotes
                                                                            since matrix is a mel keyword)  
     4x4 float matrix                                -at fltMatrix         
     reflectance                                     -dt reflectanceRGB
     reflectance (compound)                  -at reflectance       
     spectrum                                                -dt spectrumRGB       
     spectrum (compound)                     -at spectrum          
     2 floats                                                -dt float2            
     2 floats (compound)                     -at float2            
     3 floats                                                -dt float3            
     3 floats (compound)                     -at float3            
     2 doubles                                               -dt double2           
     2 doubles (compound)                    -at double2           
     3 doubles                                               -dt double3           
     3 doubles (compound)                    -at double3           
     2 32-bit integers                               -dt long2                     
     2 32-bit integers (compound)    -at long2                     
     3 32-bit integers                               -dt long3                     
     3 32-bit integers (compound)    -at long3                     
     2 16-bit integers                               -dt short2            
     2 16-bit integers (compound)    -at short2            
     3 16-bit integers                               -dt short3            
     3 16-bit integers (compound)    -at short3            
     array of doubles                                -dt doubleArray       
     array of floats                                 -dt floatArray        
     array of 32-bit ints                    -dt Int32Array        
     array of vectors                                -dt vectorArray       
     nurbs curve                                     -dt nurbsCurve        
     nurbs surface                                   -dt nurbsSurface      
     polygonal mesh                                  -dt mesh                      
     lattice                                                 -dt lattice           
     array of double 4D points               -dt pointArray

    Args:
        attributeType | at: (create, query) - Specifies the attribute type, see above table for more details. Note that the attribute types "float", "matrix" and "string" are also MEL keywords and must be enclosed in quotes.
        binaryTag | bt: (create, query) - This flag is obsolete and does not do anything any more
        cachedInternally | ci: (create, query) - Whether or not attribute data is cached internally in the node. This flag defaults to true for writable attributes and false for non-writable attributes. A warning will be issued if users attempt to force a writable attribute to be uncached as this will make it impossible to set keyframes.
        category | ct: (create, edit, multiuse, query) - An attribute category is a string associated with the attribute to identify it. (e.g. the name of a plugin that created the attribute, version information, etc.) Any attribute can be associated with an arbitrary number of categories however categories can not be removed once associated.
        dataType | dt: (create, multiuse, query) - Specifies the data type.  See "setAttr" for more information on data type names.
        defaultValue | dv: (create, edit, query) - Specifies the default value for the attribute (can only be used for numeric attributes).
        disconnectBehaviour | dcb: (create, query) - defines the Disconnect Behaviour 2 Nothing, 1 Reset, 0 Delete
        enumName | en: (create, edit, query) - Flag used to specify the ui names corresponding to the enum values. The specified string should contain a colon-separated list of the names, with optional values. If values are not specified, they will treated as sequential integers starting with 0. For example: -enumName "A:B:C" would produce options: A,B,C with values of 0,1,2; -enumName "zero:one:two:thousand=1000" would produce four options with values 0,1,2,1000; and -enumName "solo=1:triplet=3:quintet=5" would produce three options with values 1,3,5.  (Note that there is a current limitation of the Channel Box that will sometimes incorrectly display an enumerated attribute's pull-down menu.  Extra menu items can appear that represent the numbers inbetween non-sequential option values.  To avoid this limitation, specify sequential values for the options of any enumerated attributes that will appear in the Channel Box.  For example: "solo=1:triplet=2:quintet=3".)
        exists | ex: (create, query) - Returns true if the attribute queried is a user-added, dynamic attribute; false if not.
        fromPlugin | fp: (create, query) - Was the attribute originally created by a plugin? Normally set automatically when the API call is made - only added here to support storing it in a file independently from the creating plugin.
        hasMaxValue | hxv: (create, edit, query) - Flag indicating whether an attribute has a maximum value. (can only be used for numeric attributes).
        hasMinValue | hnv: (create, edit, query) - Flag indicating whether an attribute has a minimum value. (can only be used for numeric attributes).
        hasSoftMaxValue | hsx: (create, query) - Flag indicating whether a numeric attribute has a soft maximum.
        hasSoftMinValue | hsn: (create, query) - Flag indicating whether a numeric attribute has a soft minimum.
        hidden | h: (create, query) - Will this attribute be hidden from the UI?
        indexMatters | im: (create, query) - Sets whether an index must be used when connecting to this multi-attribute. Setting indexMatters to false forces the attribute to non-readable.
        internalSet | internalSet: (create, query) - Whether or not the internal cached value is set when this attribute value is changed.  This is an internal flag used for updating UI elements.
        keyable | k: (create, query) - Is the attribute keyable by default?
        longName | ln: (create, query) - Sets the long name of the attribute.
        maxValue | max: (create, edit, query) - Specifies the maximum value for the attribute (can only be used for numeric attributes).
        minValue | min: (create, edit, query) - Specifies the minimum value for the attribute (can only be used for numeric attributes).
        multi | m: (create, query) - Makes the new attribute a multi-attribute.
        niceName | nn: (create, edit, query) - Sets the nice name of the attribute for display in the UI.  Setting the attribute's nice name to a non-empty string overrides the default behaviour of looking up the nice name from Maya's string catalog.   (Use the MEL commands "attributeNiceName" and "attributeQuery -niceName" to lookup an attribute's nice name in the catalog.)
        numberOfChildren | nc: (create, query) - How many children will the new attribute have?
        parent | p: (create, query) - Attribute that is to be the new attribute's parent.
        proxy | pxy: (create, query) - Proxy another node's attribute. Proxied plug will be connected as source. The UsedAsProxy flag is automatically set in this case.
        readable | r: (create, query) - Can outgoing connections be made from this attribute?
        shortName | sn: (create, query) - Sets the short name of the attribute.
        softMaxValue | smx: (create, edit, query) - Soft maximum, valid for numeric attributes only.  Specifies the upper default limit used in sliders for this attribute.
        softMinValue | smn: (create, edit, query) - Soft minimum, valid for numeric attributes only.  Specifies the lower default limit used in sliders for this attribute.
        storable | s: (create, query) - Can the attribute be stored out to a file?
        usedAsColor | uac: (create, query) - Is the attribute to be used as a color definition? Must have 3 DOUBLE or 3 FLOAT children to use this flag.  The attribute type "-at" should be "double3" or "float3" as appropriate.  It can also be used to less effect with data types "-dt" as "double3" or "float3" as well but some parts of the code do not support this alternative.  The special attribute types/data "spectrum" and "reflectance" also support the color flag and on them it is set by default.
        usedAsFilename | uaf: (create, query) - Is the attribute to be treated as a filename definition? This flag is only supported on attributes with data type "-dt" of "string".
        usedAsProxy | uap: (create, query) - Set if the specified attribute should be treated as a proxy to another attributes.
        worldSpace | ws: (create, query) - Sets whether this attribute should be treated as worldspace. Being worldspace indicates the attribute is dependent on the worldSpace transformation of this node, and will be marked dirty by any attribute changes in the hierarchy that affects the worldSpace transformation. The attribute needs to be an array since during instancing there are multiple worldSpace paths to the node and Maya requires one array element per path for worldSpace attributes. Remarks: 1. Can only be used on array attributes. 2. This property is ignored on non-dag nodes. 3. The attribute should be affected by another attribute or have a connection.    Otherwise, the attribute will not get computed and will not get dirty again.
        writable | w: (create, query) - Can incoming connections be made to this attribute?
    """
    ...


def addExtension(*args, nodeType: Optional[Union[str, bool]] = ..., nt: Optional[Union[str, bool]] = ..., attributeType: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., binaryTag: Optional[Union[str, bool]] = ..., bt: Optional[Union[str, bool]] = ..., cachedInternally: bool = ..., ci: bool = ..., category: Optional[Union[str, bool]] = ..., ct: Optional[Union[str, bool]] = ..., dataType: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., defaultValue: Optional[Union[float, bool]] = ..., dv: Optional[Union[float, bool]] = ..., disconnectBehaviour: Optional[Union[int, bool]] = ..., dcb: Optional[Union[int, bool]] = ..., enumName: Optional[Union[str, bool]] = ..., en: Optional[Union[str, bool]] = ..., exists: bool = ..., ex: bool = ..., fromPlugin: bool = ..., fp: bool = ..., hasMaxValue: bool = ..., hxv: bool = ..., hasMinValue: bool = ..., hnv: bool = ..., hasSoftMaxValue: bool = ..., hsx: bool = ..., hasSoftMinValue: bool = ..., hsn: bool = ..., hidden: bool = ..., h: bool = ..., indexMatters: bool = ..., im: bool = ..., internalSet: bool = ..., keyable: bool = ..., k: bool = ..., longName: Optional[Union[str, bool]] = ..., ln: Optional[Union[str, bool]] = ..., maxValue: Optional[Union[float, bool]] = ..., max: Optional[Union[float, bool]] = ..., minValue: Optional[Union[float, bool]] = ..., min: Optional[Union[float, bool]] = ..., multi: bool = ..., m: bool = ..., niceName: Optional[Union[str, bool]] = ..., nn: Optional[Union[str, bool]] = ..., numberOfChildren: Optional[Union[int, bool]] = ..., nc: Optional[Union[int, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., proxy: Optional[Union[str, bool]] = ..., pxy: Optional[Union[str, bool]] = ..., readable: bool = ..., r: bool = ..., shortName: Optional[Union[str, bool]] = ..., sn: Optional[Union[str, bool]] = ..., softMaxValue: Optional[Union[float, bool]] = ..., smx: Optional[Union[float, bool]] = ..., softMinValue: Optional[Union[float, bool]] = ..., smn: Optional[Union[float, bool]] = ..., storable: bool = ..., s: bool = ..., usedAsColor: bool = ..., uac: bool = ..., usedAsFilename: bool = ..., uaf: bool = ..., usedAsProxy: bool = ..., uap: bool = ..., worldSpace: bool = ..., ws: bool = ..., writable: bool = ..., w: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to add an extension attribute to a node type.
    Either the longName or the shortName or both must be specified.
    If neither a dataType nor an attributeType is specified, a double
    attribute will be added.  The dataType flag can be specified more than
    once indicating that any of the supplied types will be accepted (logical-or).
    
    
    To add a non-double attribute the following criteria
    can be used to determine whether the dataType or the attributeType
    flag is appropriate.  Some types, such as double3 can use either.
    In these cases the -dt flag should be used when you only wish to
    access the data as an atomic entity (eg. you never want to access the
    three individual values that make up a double3).  In general it
    is best to use the -at in these cases for maximum flexibility.
    In most cases the -dt version will not display in the attribute
    editor as it is an atomic type and you are not allowed to change
    individual parts of it.
    
    
    All attributes flagged as "(compound)" below or the compound attribute itself
    are not actually added to the node until all of the children are defined
    (using the "-p" flag to set their parent to the compound being created).  See
    the EXAMPLES section for more details.
    
    
    
     Type of attribute               Flag and argument to use      
     boolean                                                 -at bool                      
     32 bit integer                                  -at long                      
     16 bit integer                                  -at short                     
     8 bit integer                                   -at byte                      
     char                                                    -at char                      
      enum                                                   -at enum (specify the enum names using the enumName flag)  
     float                                                   -at "float" (use quotes
                                                                            since float is a mel keyword)   
     double                                                  -at double            
     angle value                                     -at doubleAngle       
     linear value                                    -at doubleLinear      
     string                                                  -dt "string" (use quotes
                                                                            since string is a mel keyword)  
     array of strings                                -dt stringArray       
     compound                                                -at compound          
     message (no data)                               -at message           
     time                                                    -at time                      
     4x4 double matrix                               -dt "matrix" (use quotes
                                                                            since matrix is a mel keyword)  
     4x4 float matrix                                -at fltMatrix         
     reflectance                                     -dt reflectanceRGB
     reflectance (compound)                  -at reflectance       
     spectrum                                                -dt spectrumRGB       
     spectrum (compound)                     -at spectrum          
     2 floats                                                -dt float2            
     2 floats (compound)                     -at float2            
     3 floats                                                -dt float3            
     3 floats (compound)                     -at float3            
     2 doubles                                               -dt double2           
     2 doubles (compound)                    -at double2           
     3 doubles                                               -dt double3           
     3 doubles (compound)                    -at double3           
     2 32-bit integers                               -dt long2                     
     2 32-bit integers (compound)    -at long2                     
     3 32-bit integers                               -dt long3                     
     3 32-bit integers (compound)    -at long3                     
     2 16-bit integers                               -dt short2            
     2 16-bit integers (compound)    -at short2            
     3 16-bit integers                               -dt short3            
     3 16-bit integers (compound)    -at short3            
     array of doubles                                -dt doubleArray       
     array of floats                                 -dt floatArray        
     array of 32-bit ints                    -dt Int32Array        
     array of vectors                                -dt vectorArray       
     nurbs curve                                     -dt nurbsCurve        
     nurbs surface                                   -dt nurbsSurface      
     polygonal mesh                                  -dt mesh                      
     lattice                                                 -dt lattice           
     array of double 4D points               -dt pointArray

    Args:
        nodeType | nt: (create, edit, query) - Specifies the type of node to which the attribute will be added. See the nodeType command for the names of different node types.
        attributeType | at: (create, query) - Specifies the attribute type, see above table for more details. Note that the attribute types "float", "matrix" and "string" are also MEL keywords and must be enclosed in quotes.
        binaryTag | bt: (create, query) - This flag is obsolete and does not do anything any more
        cachedInternally | ci: (create, query) - Whether or not attribute data is cached internally in the node. This flag defaults to true for writable attributes and false for non-writable attributes. A warning will be issued if users attempt to force a writable attribute to be uncached as this will make it impossible to set keyframes.
        category | ct: (create, edit, multiuse, query) - An attribute category is a string associated with the attribute to identify it. (e.g. the name of a plugin that created the attribute, version information, etc.) Any attribute can be associated with an arbitrary number of categories however categories can not be removed once associated.
        dataType | dt: (create, multiuse, query) - Specifies the data type.  See "setAttr" for more information on data type names.
        defaultValue | dv: (create, edit, query) - Specifies the default value for the attribute (can only be used for numeric attributes).
        disconnectBehaviour | dcb: (create, query) - defines the Disconnect Behaviour 2 Nothing, 1 Reset, 0 Delete
        enumName | en: (create, edit, query) - Flag used to specify the ui names corresponding to the enum values. The specified string should contain a colon-separated list of the names, with optional values. If values are not specified, they will treated as sequential integers starting with 0. For example: -enumName "A:B:C" would produce options: A,B,C with values of 0,1,2; -enumName "zero:one:two:thousand=1000" would produce four options with values 0,1,2,1000; and -enumName "solo=1:triplet=3:quintet=5" would produce three options with values 1,3,5.  (Note that there is a current limitation of the Channel Box that will sometimes incorrectly display an enumerated attribute's pull-down menu.  Extra menu items can appear that represent the numbers inbetween non-sequential option values.  To avoid this limitation, specify sequential values for the options of any enumerated attributes that will appear in the Channel Box.  For example: "solo=1:triplet=2:quintet=3".)
        exists | ex: (create, query) - Returns true if the attribute queried is a user-added, dynamic attribute; false if not.
        fromPlugin | fp: (create, query) - Was the attribute originally created by a plugin? Normally set automatically when the API call is made - only added here to support storing it in a file independently from the creating plugin.
        hasMaxValue | hxv: (create, edit, query) - Flag indicating whether an attribute has a maximum value. (can only be used for numeric attributes).
        hasMinValue | hnv: (create, edit, query) - Flag indicating whether an attribute has a minimum value. (can only be used for numeric attributes).
        hasSoftMaxValue | hsx: (create, query) - Flag indicating whether a numeric attribute has a soft maximum.
        hasSoftMinValue | hsn: (create, query) - Flag indicating whether a numeric attribute has a soft minimum.
        hidden | h: (create, query) - Will this attribute be hidden from the UI?
        indexMatters | im: (create, query) - Sets whether an index must be used when connecting to this multi-attribute. Setting indexMatters to false forces the attribute to non-readable.
        internalSet | internalSet: (create, query) - Whether or not the internal cached value is set when this attribute value is changed.  This is an internal flag used for updating UI elements.
        keyable | k: (create, query) - Is the attribute keyable by default?
        longName | ln: (create, query) - Sets the long name of the attribute.
        maxValue | max: (create, edit, query) - Specifies the maximum value for the attribute (can only be used for numeric attributes).
        minValue | min: (create, edit, query) - Specifies the minimum value for the attribute (can only be used for numeric attributes).
        multi | m: (create, query) - Makes the new attribute a multi-attribute.
        niceName | nn: (create, edit, query) - Sets the nice name of the attribute for display in the UI.  Setting the attribute's nice name to a non-empty string overrides the default behaviour of looking up the nice name from Maya's string catalog.   (Use the MEL commands "attributeNiceName" and "attributeQuery -niceName" to lookup an attribute's nice name in the catalog.)
        numberOfChildren | nc: (create, query) - How many children will the new attribute have?
        parent | p: (create, query) - Attribute that is to be the new attribute's parent.
        proxy | pxy: (create, query) - Proxy another node's attribute. Proxied plug will be connected as source. The UsedAsProxy flag is automatically set in this case.
        readable | r: (create, query) - Can outgoing connections be made from this attribute?
        shortName | sn: (create, query) - Sets the short name of the attribute.
        softMaxValue | smx: (create, edit, query) - Soft maximum, valid for numeric attributes only.  Specifies the upper default limit used in sliders for this attribute.
        softMinValue | smn: (create, edit, query) - Soft minimum, valid for numeric attributes only.  Specifies the lower default limit used in sliders for this attribute.
        storable | s: (create, query) - Can the attribute be stored out to a file?
        usedAsColor | uac: (create, query) - Is the attribute to be used as a color definition? Must have 3 DOUBLE or 3 FLOAT children to use this flag.  The attribute type "-at" should be "double3" or "float3" as appropriate.  It can also be used to less effect with data types "-dt" as "double3" or "float3" as well but some parts of the code do not support this alternative.  The special attribute types/data "spectrum" and "reflectance" also support the color flag and on them it is set by default.
        usedAsFilename | uaf: (create, query) - Is the attribute to be treated as a filename definition? This flag is only supported on attributes with data type "-dt" of "string".
        usedAsProxy | uap: (create, query) - Set if the specified attribute should be treated as a proxy to another attributes.
        worldSpace | ws: (create, query) - Sets whether this attribute should be treated as worldspace. Being worldspace indicates the attribute is dependent on the worldSpace transformation of this node, and will be marked dirty by any attribute changes in the hierarchy that affects the worldSpace transformation. The attribute needs to be an array since during instancing there are multiple worldSpace paths to the node and Maya requires one array element per path for worldSpace attributes. Remarks: 1. Can only be used on array attributes. 2. This property is ignored on non-dag nodes. 3. The attribute should be affected by another attribute or have a connection.    Otherwise, the attribute will not get computed and will not get dirty again.
        writable | w: (create, query) - Can incoming connections be made to this attribute?
    """
    ...


def affectedNet(*args, type: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command gets the list of attributes on a node or node type and
    creates nodes of type TdnAffect, one for each attribute, that are
    connected iff the source node's attribute affects the destination node's
    attribute.

    Args:
        type | t: (create) - Get information from the given node type instead of one node
    """
    ...


def affects(*args, by: bool = ..., type: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This command returns the list of attributes on a node or node type which
    affect the named attribute.

    Args:
        by: (create) - Show attributes that are affected by the given one rather than the ones that affect it.
        type | t: (create) - static node type from which to get 'affects' information
    """
    ...


def aliasAttr(*args, remove: bool = ..., rm: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Allows aliases (alternate names) to be defined for any attribute of
    a specified node. When an attribute is aliased, the alias will be
    used by the system to display information about the attribute.
    The user may, however, freely use either the alias or the original
    name of the attribute. Only a single alias can be specified for an
    attribute so setting an alias on an already-aliased attribute destroys
    the old alias.

    Args:
        remove | rm: (create) - Specifies that aliases listed should be removed (otherwise new aliases are added).
    """
    ...


def align(*args, alignToLead: bool = ..., atl: bool = ..., coordinateSystem: Optional[Union[str, bool]] = ..., cs: Optional[Union[str, bool]] = ..., xAxis: Optional[Union[str, bool]] = ..., x: Optional[Union[str, bool]] = ..., yAxis: Optional[Union[str, bool]] = ..., y: Optional[Union[str, bool]] = ..., zAxis: Optional[Union[str, bool]] = ..., z: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Align or spread objects along X Y and Z axis.

    Args:
        alignToLead | atl: (create) - When set, the min, center or max values are computed from the lead object. Otherwise, the values are averaged for all objects. Default is false
        coordinateSystem | cs: (create) - Defines the X, Y, and Z coordinates. Default is the world coordinates
        xAxis | x: (create) - Any of none, min, mid, max, dist, stack. This defines the kind of alignment to perfom, default is none.
        yAxis | y: (create) - Any of none, min, mid, max, dist, stack. This defines the kind of alignment to perfom, default is none.
        zAxis | z: (create) - Any of none, min, mid, max, dist, stack. This defines the kind of alignment to perfom, default is none.
    """
    ...


def alignCtx(*args, align: bool = ..., a: bool = ..., anchorFirstObject: bool = ..., afo: bool = ..., distribute: bool = ..., d: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., showAlignTouch: bool = ..., sat: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The alignCtx command creates a tool for aligning and
    distributing objects.

    Args:
        align | a: (create, edit, query) - Align objects
        anchorFirstObject | afo: (create, edit, query) - Anchor first or last selected object. Default false. Only applicable when aligning objects.
        distribute | d: (create, edit, query) - Distribute objects
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        showAlignTouch | sat: (create, edit, query) - Show or hide align touching handles. Default true. Only applicable when aligning objects.
    """
    ...


def applyAttrPattern(*args, nodeType: Optional[Union[str, bool]] = ..., nt: Optional[Union[str, bool]] = ..., patternName: Optional[Union[str, bool]] = ..., pn: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Take the attribute structure described by a pre-defined pattern and apply it either to a
    node (as dynamic attributes) or a node type (as extension attributes). The same pattern
    can be applied more than once to different nodes or node types as the operation duplicates
    the attribute structure described by the pattern.  See the 'createAttrPatterns' command
    for a description of how to create a pattern.

    Args:
        nodeType | nt: (create) - Name of the node type to which the attribute pattern is to be applied. This flag will cause a new extension attribute tree to be created, making the new attributes available on all nodes of the given type. If it is not specified then either a node name must be specified or a node must be selected for application of dynamic attributes.
        patternName | pn: (create) - The name of the pattern to apply. The pattern with this name must have been previously created using the createAttrPatterns command.
    """
    ...


def arcLenDimContext(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command used to register the arcLenDimCtx tool.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def art3dPaintCtx(*args, accopacity: bool = ..., aco: bool = ..., afterStrokeCmd: Optional[Union[str, bool]] = ..., asc: Optional[Union[str, bool]] = ..., alphablendmode: Optional[Union[str, bool]] = ..., abm: Optional[Union[str, bool]] = ..., assigntxt: bool = ..., ast: bool = ..., attrnames: Optional[Union[str, bool]] = ..., atn: Optional[Union[str, bool]] = ..., beforeStrokeCmd: Optional[Union[str, bool]] = ..., bsc: Optional[Union[str, bool]] = ..., brushalignment: bool = ..., bra: bool = ..., brushdepth: Optional[Union[float, bool]] = ..., bd: Optional[Union[float, bool]] = ..., brushfeedback: bool = ..., brf: bool = ..., brushtype: Optional[Union[str, bool]] = ..., brt: Optional[Union[str, bool]] = ..., clear: bool = ..., clr: bool = ..., commonattr: Optional[Union[str, bool]] = ..., cat: Optional[Union[str, bool]] = ..., dragSlider: Optional[Union[str, bool]] = ..., dsl: Optional[Union[str, bool]] = ..., dynclonemode: bool = ..., dcm: bool = ..., exists: bool = ..., ex: bool = ..., expandfilename: bool = ..., eef: bool = ..., extendFillColor: bool = ..., efc: bool = ..., fileformat: Optional[Union[str, bool]] = ..., eff: Optional[Union[str, bool]] = ..., filetxtaspectratio: Optional[Union[float, bool]] = ..., far: Optional[Union[float, bool]] = ..., filetxtsizex: Optional[Union[int, bool]] = ..., ftx: Optional[Union[int, bool]] = ..., filetxtsizey: Optional[Union[int, bool]] = ..., fty: Optional[Union[int, bool]] = ..., floodOpacity: Optional[Union[float, bool]] = ..., fop: Optional[Union[float, bool]] = ..., floodall: bool = ..., fal: bool = ..., floodselect: bool = ..., fsl: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., keepaspectratio: bool = ..., kar: bool = ..., lastRecorderCmd: Optional[Union[str, bool]] = ..., lrc: Optional[Union[str, bool]] = ..., lastStampName: Optional[Union[str, bool]] = ..., lsn: Optional[Union[str, bool]] = ..., lowerradius: Optional[Union[float, bool]] = ..., lr: Optional[Union[float, bool]] = ..., makeStroke: Optional[Union[int, bool]] = ..., mst: Optional[Union[int, bool]] = ..., mappressure: Optional[Union[str, bool]] = ..., mp: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., opacity: Optional[Union[float, bool]] = ..., op: Optional[Union[float, bool]] = ..., outline: bool = ..., o: bool = ..., outwhilepaint: bool = ..., owp: bool = ..., paintmode: Optional[Union[str, bool]] = ..., pm: Optional[Union[str, bool]] = ..., paintoperationtype: Optional[Union[str, bool]] = ..., pot: Optional[Union[str, bool]] = ..., painttxtattr: Optional[Union[str, bool]] = ..., pta: Optional[Union[str, bool]] = ..., painttxtattrname: Optional[Union[str, bool]] = ..., ptn: Optional[Union[str, bool]] = ..., pfxScale: Optional[Union[float, bool]] = ..., psc: Optional[Union[float, bool]] = ..., pfxWidth: Optional[Union[float, bool]] = ..., pwd: Optional[Union[float, bool]] = ..., pickColor: bool = ..., pcm: bool = ..., pickValue: bool = ..., pv: bool = ..., playbackCursor: Optional[Union[Tuple[float, float], bool]] = ..., plc: Optional[Union[Tuple[float, float], bool]] = ..., playbackPressure: Optional[Union[float, bool]] = ..., plp: Optional[Union[float, bool]] = ..., preserveclonesource: bool = ..., pcs: bool = ..., pressureMapping1: Optional[Union[int, bool]] = ..., pm1: Optional[Union[int, bool]] = ..., pressureMapping2: Optional[Union[int, bool]] = ..., pm2: Optional[Union[int, bool]] = ..., pressureMapping3: Optional[Union[int, bool]] = ..., pm3: Optional[Union[int, bool]] = ..., pressureMax1: Optional[Union[float, bool]] = ..., px1: Optional[Union[float, bool]] = ..., pressureMax2: Optional[Union[float, bool]] = ..., px2: Optional[Union[float, bool]] = ..., pressureMax3: Optional[Union[float, bool]] = ..., px3: Optional[Union[float, bool]] = ..., pressureMin1: Optional[Union[float, bool]] = ..., ps1: Optional[Union[float, bool]] = ..., pressureMin2: Optional[Union[float, bool]] = ..., ps2: Optional[Union[float, bool]] = ..., pressureMin3: Optional[Union[float, bool]] = ..., ps3: Optional[Union[float, bool]] = ..., profileShapeFile: Optional[Union[str, bool]] = ..., psf: Optional[Union[str, bool]] = ..., projective: bool = ..., prm: bool = ..., radius: Optional[Union[float, bool]] = ..., r: Optional[Union[float, bool]] = ..., record: bool = ..., rec: bool = ..., reflection: bool = ..., rn: bool = ..., reflectionaboutorigin: bool = ..., rno: bool = ..., reflectionaxis: Optional[Union[str, bool]] = ..., ra: Optional[Union[str, bool]] = ..., reloadtexfile: bool = ..., rtf: bool = ..., resizeratio: Optional[Union[float, bool]] = ..., rr: Optional[Union[float, bool]] = ..., resizetxt: bool = ..., rft: bool = ..., rgbcolor: Optional[Union[Tuple[float, float, float], bool]] = ..., rgb: Optional[Union[Tuple[float, float, float], bool]] = ..., rgbflood: Optional[Union[Tuple[float, float, float], bool]] = ..., fc: Optional[Union[Tuple[float, float, float], bool]] = ..., saveTextureOnStroke: bool = ..., sts: bool = ..., saveonstroke: bool = ..., sos: bool = ..., savetexture: bool = ..., stx: bool = ..., screenRadius: Optional[Union[float, bool]] = ..., scR: Optional[Union[float, bool]] = ..., selectclonesource: bool = ..., scs: bool = ..., shadernames: Optional[Union[str, bool]] = ..., hnm: Optional[Union[str, bool]] = ..., shapeattr: bool = ..., spa: bool = ..., shapenames: Optional[Union[str, bool]] = ..., shn: Optional[Union[str, bool]] = ..., showactive: bool = ..., sa: bool = ..., soloAsDiffuse: bool = ..., sod: bool = ..., stampDepth: Optional[Union[float, bool]] = ..., stD: Optional[Union[float, bool]] = ..., stampProfile: Optional[Union[str, bool]] = ..., stP: Optional[Union[str, bool]] = ..., stampSpacing: Optional[Union[float, bool]] = ..., stS: Optional[Union[float, bool]] = ..., strokesmooth: Optional[Union[str, bool]] = ..., ssm: Optional[Union[str, bool]] = ..., surfaceConformedBrushVertices: bool = ..., scv: bool = ..., tablet: bool = ..., tab: bool = ..., tangentOutline: bool = ..., to: bool = ..., textureFilenames: bool = ..., tfn: bool = ..., updateEraseTex: bool = ..., uet: bool = ..., usepressure: bool = ..., up: bool = ..., worldRadius: Optional[Union[float, bool]] = ..., wlR: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This is a tool context command for 3d Paint tool.

    Args:
        accopacity | aco: (create, edit, query) - Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        afterStrokeCmd | asc: (create, edit, query) - The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        alphablendmode | abm: (create, edit, query) - Specifies the blend mode used while painting RGB channel. Currently, we support the following blend modes: "Default" "Lighten" "Darken" "Difference" "Exclusion" "Hard Light" "Soft Light" "Multiply" "Screen" "Overlay" "Constant" Default is "Default".
        assigntxt | ast: (edit) - Sends a request to the tool to allocate and assign file textures to the specified attibute on the selected shaders.
        attrnames | atn: (create, edit, query) - Name of attributes
        beforeStrokeCmd | bsc: (create, edit, query) - The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        brushalignment | bra: (create, edit, query) - Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        brushdepth | bd: (create, edit, query) - Depth of the brush
        brushfeedback | brf: (create, edit, query) - Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        brushtype | brt: (create, edit, query) - Name of the brush type
        clear | clr: (create, edit) - Floods all cvs/vertices to the current value.
        commonattr | cat: (query) - Returns a string with the names of all common to all the shaders paintable attributes and supported by the Paint Texture Tool.
        dragSlider | dsl: (create, edit) - Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".
        dynclonemode | dcm: (create, edit, query) - Enable or disable dynamic clone mode.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        expandfilename | eef: (create, edit) - If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        extendFillColor | efc: (create, edit, query) - States if the painted textures will be automatically postprocessed on each stroke to fill in the background color. Default is true.
        fileformat | eff: (create, edit, query) - Name of the file format
        filetxtaspectratio | far: (create, edit, query) - Specifies the aspect ration of the texture width and height. Default is 1.
        filetxtsizex | ftx: (create, edit, query) - Specifies the width of the texture. Default is 256.
        filetxtsizey | fty: (create, edit, query) - Specifies the height of the texture. Default is 256.
        floodOpacity | fop: (create, edit, query) - Value of the flood opacity
        floodall | fal: (create, edit, query) - Turn on to flood everything
        floodselect | fsl: (create, edit, query) - Should the selected area be flooded?
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        keepaspectratio | kar: (create, edit, query) - States if the aspect ratio of the file texture sizes should remain constant. Default is true. boolean.
        lastRecorderCmd | lrc: (create, edit, query) - Value of last recorded command.
        lastStampName | lsn: (create, edit, query) - Value of the last stamp name.
        lowerradius | lr: (create, edit, query) - Sets the lower size of the brush (only apply on tablet).
        makeStroke | mst: (create, edit, multiuse, query) - Stroke point values.
        mappressure | mp: (create, edit, query) - Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        opacity | op: (create, edit, query) - Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        outline | o: (create, edit, query) - Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        outwhilepaint | owp: (create, edit, query) - Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        paintmode | pm: (create, edit, query) - Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        paintoperationtype | pot: (create, edit, query) - Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        painttxtattr | pta: (create, edit, query) - Specifies the attribute on the shader which the user wants to paint. Currently, we support the following attributes: "Color", "Transparency", "Ambient", "Incandescence", "BumpMap", "Diffuse", "Translucence" "Eccentricity" "SpecularColor", "Reflectivity", "ReflectedColor", and user-defined float, float3, double, and double3 attributes. Default is "Color".
        painttxtattrname | ptn: (edit, query) - Returns a string with the names of all paintable attributes supported by the Paint Texture Tool.
        pfxScale | psc: (edit, query) - Specifies the scale for Paint Effect brushes.
        pfxWidth | pwd: (edit, query) - Specifies the width for Paint Effect brushes.
        pickColor | pcm: (create, edit, query) - Set pick color mode on or off
        pickValue | pv: (create, edit, query) - Toggle for picking
        playbackCursor | plc: (create, edit, multiuse, query) - Values for the playback cursor.
        playbackPressure | plp: (create, edit, multiuse, query) - Valus for the playback pressure.
        preserveclonesource | pcs: (create, edit, query) - Whether or not to preserve a clone source.
        pressureMapping1 | pm1: (create, edit, query) - First pressure mapping value
        pressureMapping2 | pm2: (create, edit, query) - Second pressure mapping value
        pressureMapping3 | pm3: (create, edit, query) - Third pressure mapping value
        pressureMax1 | px1: (create, edit, query) - First pressure maximum value
        pressureMax2 | px2: (create, edit, query) - Second pressure maximum value
        pressureMax3 | px3: (create, edit, query) - Third pressure maximum value
        pressureMin1 | ps1: (create, edit, query) - First pressure minimum value
        pressureMin2 | ps2: (create, edit, query) - Second pressure minimum value
        pressureMin3 | ps3: (create, edit, query) - Third pressure minimum value
        profileShapeFile | psf: (edit, query) - Passes a name of the image file for the stamp shape profile.
        projective | prm: (create, edit, query) - Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        radius | r: (create, edit, query) - Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        record | rec: (create, edit, query) - Toggle on for recording.
        reflection | rn: (create, edit, query) - Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        reflectionaboutorigin | rno: (create, edit, query) - Toggle on to reflect about the origin
        reflectionaxis | ra: (create, edit, query) - Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        reloadtexfile | rtf: (edit) - Sends a request to the tool to reload the texture from the disc.
        resizeratio | rr: (edit, query) - Specifies the scale by which to resize the current textures.
        resizetxt | rft: (edit) - Sends a request to the tool to resize all the currently in use textures.
        rgbcolor | rgb: (create, edit, query) - Colour value
        rgbflood | fc: (create, edit, query) - Color of the flood
        saveTextureOnStroke | sts: (create, edit, query) - States if the original texture will be automatically saved on each stroke. Default is false.
        saveonstroke | sos: (create, edit, query) - States if the temporary texture will be automatically saved on each stroke. Default is false.
        savetexture | stx: (edit) - Sends a request to the tool to save the texture to the disc.
        screenRadius | scR: (create, edit, query) - Brush radius on the screen
        selectclonesource | scs: (create, edit, query) - Toggle on to select the clone source
        shadernames | hnm: (query) - Returns a string with the names of all shaders assigned to selected surfaces.
        shapeattr | spa: (edit, query) - States if the attribute to paint is an attribute of the shape and not the shader. Default is false.
        shapenames | shn: (query) - Returns a string with the names of all surfaces which are being painted on.
        showactive | sa: (create, edit, query) - Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        soloAsDiffuse | sod: (edit, query) - States if the currently paintable texture will be rendered as as diffuse texture in the viewport. Default is false.
        stampDepth | stD: (create, edit, query) - Depth of the stamps
        stampProfile | stP: (create, edit, query) - Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        stampSpacing | stS: (create, edit, query) - Specifies the stamp spacing. Default is 1.0.
        strokesmooth | ssm: (create, edit, query) - Stroke smoothing type name
        surfaceConformedBrushVertices | scv: (create, edit, query) - Enables/disables the the display of the effective brush area as affected vertices.
        tablet | tab: (query) - Returns true if the tablet device is present, false if it is absent
        tangentOutline | to: (create, edit, query) - Enables/disables the display of the brush circle tangent to the surface.
        textureFilenames | tfn: (query) - Returns a string array with the names of all the painted file textures.
        updateEraseTex | uet: (create, edit, query) - Should the erase texture update?
        usepressure | up: (create, edit, query) - Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        worldRadius | wlR: (create, edit, query) - Radius in worldspace
    """
    ...


def artAttrCtx(*args, accopacity: bool = ..., aco: bool = ..., activeListChangedProc: Optional[Union[str, bool]] = ..., alp: Optional[Union[str, bool]] = ..., afterStrokeCmd: Optional[Union[str, bool]] = ..., asc: Optional[Union[str, bool]] = ..., alphaclamp: Optional[Union[str, bool]] = ..., alc: Optional[Union[str, bool]] = ..., alphaclamplower: Optional[Union[float, bool]] = ..., acl: Optional[Union[float, bool]] = ..., alphaclampupper: Optional[Union[float, bool]] = ..., acu: Optional[Union[float, bool]] = ..., attrSelected: Optional[Union[str, bool]] = ..., asl: Optional[Union[str, bool]] = ..., beforeStrokeCmd: Optional[Union[str, bool]] = ..., bsc: Optional[Union[str, bool]] = ..., brushalignment: bool = ..., bra: bool = ..., brushfeedback: bool = ..., brf: bool = ..., clamp: Optional[Union[str, bool]] = ..., cl: Optional[Union[str, bool]] = ..., clamplower: Optional[Union[float, bool]] = ..., cll: Optional[Union[float, bool]] = ..., clampupper: Optional[Union[float, bool]] = ..., clu: Optional[Union[float, bool]] = ..., clear: bool = ..., clr: bool = ..., colorAlphaValue: Optional[Union[float, bool]] = ..., cl1: Optional[Union[float, bool]] = ..., colorRGBAValue: Optional[Union[Tuple[float, float, float, float], bool]] = ..., cl4: Optional[Union[Tuple[float, float, float, float], bool]] = ..., colorRGBValue: Optional[Union[Tuple[float, float, float], bool]] = ..., cl3: Optional[Union[Tuple[float, float, float], bool]] = ..., colorRamp: Optional[Union[str, bool]] = ..., cr: Optional[Union[str, bool]] = ..., colorfeedback: bool = ..., cf: bool = ..., colorfeedbackOverride: bool = ..., cfo: bool = ..., colorrangelower: Optional[Union[float, bool]] = ..., crl: Optional[Union[float, bool]] = ..., colorrangeupper: Optional[Union[float, bool]] = ..., cru: Optional[Union[float, bool]] = ..., dataTypeIndex: Optional[Union[int, bool]] = ..., dti: Optional[Union[int, bool]] = ..., disablelighting: bool = ..., dl: bool = ..., dragSlider: Optional[Union[str, bool]] = ..., dsl: Optional[Union[str, bool]] = ..., duringStrokeCmd: Optional[Union[str, bool]] = ..., dsk: Optional[Union[str, bool]] = ..., dynclonemode: bool = ..., dcm: bool = ..., exists: bool = ..., ex: bool = ..., expandfilename: bool = ..., eef: bool = ..., exportaspectratio: Optional[Union[float, bool]] = ..., ear: Optional[Union[float, bool]] = ..., exportfilemode: Optional[Union[str, bool]] = ..., efm: Optional[Union[str, bool]] = ..., exportfilesave: str = ..., esf: str = ..., exportfilesizex: Optional[Union[int, bool]] = ..., fsx: Optional[Union[int, bool]] = ..., exportfilesizey: Optional[Union[int, bool]] = ..., fsy: Optional[Union[int, bool]] = ..., exportfiletype: Optional[Union[str, bool]] = ..., eft: Optional[Union[str, bool]] = ..., filterNodes: bool = ..., fon: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., importfileload: str = ..., ifl: str = ..., importfilemode: Optional[Union[str, bool]] = ..., ifm: Optional[Union[str, bool]] = ..., importreassign: bool = ..., irm: bool = ..., interactiveUpdate: bool = ..., iu: bool = ..., lastRecorderCmd: Optional[Union[str, bool]] = ..., lrc: Optional[Union[str, bool]] = ..., lastStampName: Optional[Union[str, bool]] = ..., lsn: Optional[Union[str, bool]] = ..., lowerradius: Optional[Union[float, bool]] = ..., lr: Optional[Union[float, bool]] = ..., makeStroke: Optional[Union[int, bool]] = ..., mst: Optional[Union[int, bool]] = ..., mappressure: Optional[Union[str, bool]] = ..., mp: Optional[Union[str, bool]] = ..., maxvalue: Optional[Union[float, bool]] = ..., mxv: Optional[Union[float, bool]] = ..., minvalue: Optional[Union[float, bool]] = ..., miv: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., numericColorRamp: Optional[Union[str, bool]] = ..., ncr: Optional[Union[str, bool]] = ..., numericDisplayColor: Optional[Union[Tuple[float, float, float], bool]] = ..., ndc: Optional[Union[Tuple[float, float, float], bool]] = ..., numericDisplayPrecision: Optional[Union[int, bool]] = ..., ndp: Optional[Union[int, bool]] = ..., numericMaxColor: Optional[Union[Tuple[float, float, float], bool]] = ..., nxc: Optional[Union[Tuple[float, float, float], bool]] = ..., numericMinColor: Optional[Union[Tuple[float, float, float], bool]] = ..., nmc: Optional[Union[Tuple[float, float, float], bool]] = ..., objattrArray: Optional[Union[str, bool]] = ..., oaa: Optional[Union[str, bool]] = ..., objattrArrayNoMenu: Optional[Union[str, bool]] = ..., oan: Optional[Union[str, bool]] = ..., opacity: Optional[Union[float, bool]] = ..., op: Optional[Union[float, bool]] = ..., outline: bool = ..., o: bool = ..., outwhilepaint: bool = ..., owp: bool = ..., paintNodeArray: Optional[Union[str, bool]] = ..., pna: Optional[Union[str, bool]] = ..., paintattrselected: str = ..., pas: str = ..., paintmode: Optional[Union[str, bool]] = ..., pm: Optional[Union[str, bool]] = ..., paintoperationtype: Optional[Union[str, bool]] = ..., pot: Optional[Union[str, bool]] = ..., pickColor: bool = ..., pcm: bool = ..., pickValue: bool = ..., pv: bool = ..., playbackCursor: Optional[Union[Tuple[float, float], bool]] = ..., plc: Optional[Union[Tuple[float, float], bool]] = ..., playbackPressure: Optional[Union[float, bool]] = ..., plp: Optional[Union[float, bool]] = ..., preserveclonesource: bool = ..., pcs: bool = ..., profileShapeFile: Optional[Union[str, bool]] = ..., psf: Optional[Union[str, bool]] = ..., projective: bool = ..., prm: bool = ..., radius: Optional[Union[float, bool]] = ..., r: Optional[Union[float, bool]] = ..., rampMaxColor: Optional[Union[Tuple[float, float, float], bool]] = ..., rxc: Optional[Union[Tuple[float, float, float], bool]] = ..., rampMinColor: Optional[Union[Tuple[float, float, float], bool]] = ..., rmc: Optional[Union[Tuple[float, float, float], bool]] = ..., record: bool = ..., rec: bool = ..., reflection: bool = ..., rn: bool = ..., reflectionaboutorigin: bool = ..., rno: bool = ..., reflectionaxis: Optional[Union[str, bool]] = ..., ra: Optional[Union[str, bool]] = ..., screenRadius: Optional[Union[float, bool]] = ..., scR: Optional[Union[float, bool]] = ..., selectclonesource: bool = ..., scs: bool = ..., selectedattroper: Optional[Union[str, bool]] = ..., sao: Optional[Union[str, bool]] = ..., showactive: bool = ..., sa: bool = ..., stampDepth: Optional[Union[float, bool]] = ..., stD: Optional[Union[float, bool]] = ..., stampProfile: Optional[Union[str, bool]] = ..., stP: Optional[Union[str, bool]] = ..., stampSpacing: Optional[Union[float, bool]] = ..., stS: Optional[Union[float, bool]] = ..., strokesmooth: Optional[Union[str, bool]] = ..., ssm: Optional[Union[str, bool]] = ..., surfaceConformedBrushVertices: bool = ..., scv: bool = ..., tablet: bool = ..., tab: bool = ..., tangentOutline: bool = ..., to: bool = ..., toolOffProc: Optional[Union[str, bool]] = ..., tfp: Optional[Union[str, bool]] = ..., toolOnProc: Optional[Union[str, bool]] = ..., top: Optional[Union[str, bool]] = ..., useColorRamp: bool = ..., ucr: bool = ..., useMaxMinColor: bool = ..., umc: bool = ..., useNumericColorRamp: bool = ..., unr: bool = ..., useNumericDisplay: bool = ..., und: bool = ..., usepressure: bool = ..., up: bool = ..., value: Optional[Union[float, bool]] = ..., val: Optional[Union[float, bool]] = ..., whichTool: Optional[Union[str, bool]] = ..., wst: Optional[Union[str, bool]] = ..., worldRadius: Optional[Union[float, bool]] = ..., wlR: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This is a context command to set the flags on the artAttrContext,
    which is the base context for attribute painting operations. All
    commands require the name of the context as the last argument as
    this provides the name of the context to create, edit or query.
    
    This is a context command to set the flags on the
    Attribute Paint Tool context.

    Args:
        accopacity | aco: (create, edit, query) - Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        activeListChangedProc | alp: (create, edit, query) - Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        afterStrokeCmd | asc: (create, edit, query) - The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        alphaclamp | alc: (create, edit, query) - Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        alphaclamplower | acl: (create, edit, query) - Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When queried, it returns a float.
        alphaclampupper | acu: (create, edit, query) - Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When queried, it returns a float.
        attrSelected | asl: (query) - Returns a name of the currently selected attribute. Q: When queried, it returns a string.
        beforeStrokeCmd | bsc: (create, edit, query) - The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        brushalignment | bra: (create, edit, query) - Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        brushfeedback | brf: (create, edit, query) - Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        clamp | cl: (create, edit, query) - Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        clamplower | cll: (create, edit, query) - Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried, it returns a float.
        clampupper | clu: (create, edit, query) - Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried, it returns a float.
        clear | clr: (create, edit) - Floods all cvs/vertices to the current value.
        colorAlphaValue | cl1: (create, edit, query) - The Alpha value of the color.
        colorRGBAValue | cl4: (create, edit, query) - The RGBA value of the color.
        colorRGBValue | cl3: (create, edit, query) - The RGB value of the color.
        colorRamp | cr: (create, edit, query) - Allows a user defined color ramp to be used to map values to colors.
        colorfeedback | cf: (create, edit, query) - Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorfeedbackOverride | cfo: (create, edit, query) - Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorrangelower | crl: (create, edit, query) - Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0.  Q: When queried, it returns a float.
        colorrangeupper | cru: (create, edit, query) - Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0.  Q: When queried, it returns a float.
        dataTypeIndex | dti: (edit, query) - When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
        disablelighting | dl: (create, edit, query) - If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE.  Q: When queried, it returns a boolean.
        dragSlider | dsl: (create, edit) - Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".
        duringStrokeCmd | dsk: (create, edit, query) - The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command
        dynclonemode | dcm: (create, edit, query) - Enable or disable dynamic clone mode.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        expandfilename | eef: (create, edit) - If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        exportaspectratio | ear: (create, edit, query) - Value of aspect ratio for export
        exportfilemode | efm: (create, edit, query) - Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        exportfilesave | esf: (edit) - Exports the attribute map and saves to a specified file.
        exportfilesizex | fsx: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfilesizey | fsy: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfiletype | eft: (create, edit, query) - Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        filterNodes | fon: (edit) - Sets the node filter.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        importfileload | ifl: (edit) - Load the attribute map a specified file.
        importfilemode | ifm: (create, edit, query) - Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        importreassign | irm: (create, edit, query) - Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        interactiveUpdate | iu: (create, edit, query) - Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When queried, it returns a boolean.
        lastRecorderCmd | lrc: (create, edit, query) - Value of last recorded command.
        lastStampName | lsn: (create, edit, query) - Value of the last stamp name.
        lowerradius | lr: (create, edit, query) - Sets the lower size of the brush (only apply on tablet).
        makeStroke | mst: (create, edit, multiuse, query) - Stroke point values.
        mappressure | mp: (create, edit, query) - Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        maxvalue | mxv: (create, edit, query) - Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When queried, it returns a float.
        minvalue | miv: (create, edit, query) - Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        numericColorRamp | ncr: (create, edit, query) - Allows a user defined color ramp to be used to map values to colors for the numeric display.
        numericDisplayColor | ndc: (create, edit, query) - Defines a color to be used when displaying numeric values.
        numericDisplayPrecision | ndp: (create, edit, query) - Specifies how many decimal points of precision should be used for the numeric display.
        numericMaxColor | nxc: (create, edit, query) - Defines a special color to be used when the value is greater than or equal to the maximum value.
        numericMinColor | nmc: (create, edit, query) - Defines a special color to be used when the value is less than or equal to the minimum value.
        objattrArray | oaa: (query) - An array of all paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.MenuType *MenuType: type (level) of the item in the Menu (UI). Q: When queried, it returns a string.
        objattrArrayNoMenu | oan: (query) - Returns an array of all paintable attributes in their original order. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName
        opacity | op: (create, edit, query) - Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        outline | o: (create, edit, query) - Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        outwhilepaint | owp: (create, edit, query) - Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        paintNodeArray | pna: (query) - An array of paintable nodes. Q: When queried, it returns a string.
        paintattrselected | pas: (edit) - An array of selected paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.
        paintmode | pm: (create, edit, query) - Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        paintoperationtype | pot: (create, edit, query) - Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        pickColor | pcm: (create, edit, query) - Set pick color mode on or off
        pickValue | pv: (create, edit, query) - Toggle for picking
        playbackCursor | plc: (create, edit, multiuse, query) - Values for the playback cursor.
        playbackPressure | plp: (create, edit, multiuse, query) - Valus for the playback pressure.
        preserveclonesource | pcs: (create, edit, query) - Whether or not to preserve a clone source.
        profileShapeFile | psf: (edit, query) - Passes a name of the image file for the stamp shape profile.
        projective | prm: (create, edit, query) - Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        radius | r: (create, edit, query) - Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        rampMaxColor | rxc: (create, edit, query) - Defines a special color to be used when the value is greater than or equal to the maximum value.
        rampMinColor | rmc: (create, edit, query) - Defines a special color to be used when the value is less than or equal to the minimum value.
        record | rec: (create, edit, query) - Toggle on for recording.
        reflection | rn: (create, edit, query) - Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        reflectionaboutorigin | rno: (create, edit, query) - Toggle on to reflect about the origin
        reflectionaxis | ra: (create, edit, query) - Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        screenRadius | scR: (create, edit, query) - Brush radius on the screen
        selectclonesource | scs: (create, edit, query) - Toggle on to select the clone source
        selectedattroper | sao: (create, edit, query) - Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of the weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C: Default is "absolute".  Q: When queried, it returns a string.
        showactive | sa: (create, edit, query) - Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        stampDepth | stD: (create, edit, query) - Depth of the stamps
        stampProfile | stP: (create, edit, query) - Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        stampSpacing | stS: (create, edit, query) - Specifies the stamp spacing. Default is 1.0.
        strokesmooth | ssm: (create, edit, query) - Stroke smoothing type name
        surfaceConformedBrushVertices | scv: (create, edit, query) - Enables/disables the the display of the effective brush area as affected vertices.
        tablet | tab: (query) - Returns true if the tablet device is present, false if it is absent
        tangentOutline | to: (create, edit, query) - Enables/disables the display of the brush circle tangent to the surface.
        toolOffProc | tfp: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        toolOnProc | top: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        useColorRamp | ucr: (create, edit, query) - Specifies whether the user defined color ramp should be used to map values from to colors.  If this is turned off, the default greyscale feedback will be used.
        useMaxMinColor | umc: (create, edit, query) - Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        useNumericColorRamp | unr: (create, edit, query) - Specifies whether the user defined color ramp should be used to map values from to colors on the numeric display. If this is turned off, the set single numeric color will be used.
        useNumericDisplay | und: (create, edit, query) - Specifies whether numerical weight values should be displayed next to their associated control points.
        usepressure | up: (create, edit, query) - Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        value | val: (create, edit, query) - Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        whichTool | wst: (create, edit, query) - The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last when specifying a flag that takes arguments.
        worldRadius | wlR: (create, edit, query) - Radius in worldspace
    """
    ...


def artAttrPaintVertexCtx(*args, accopacity: bool = ..., aco: bool = ..., activeListChangedProc: Optional[Union[str, bool]] = ..., alp: Optional[Union[str, bool]] = ..., afterStrokeCmd: Optional[Union[str, bool]] = ..., asc: Optional[Union[str, bool]] = ..., alphaclamp: Optional[Union[str, bool]] = ..., alc: Optional[Union[str, bool]] = ..., alphaclamplower: Optional[Union[float, bool]] = ..., acl: Optional[Union[float, bool]] = ..., alphaclampupper: Optional[Union[float, bool]] = ..., acu: Optional[Union[float, bool]] = ..., attrSelected: Optional[Union[str, bool]] = ..., asl: Optional[Union[str, bool]] = ..., beforeStrokeCmd: Optional[Union[str, bool]] = ..., bsc: Optional[Union[str, bool]] = ..., brushalignment: bool = ..., bra: bool = ..., brushfeedback: bool = ..., brf: bool = ..., clamp: Optional[Union[str, bool]] = ..., cl: Optional[Union[str, bool]] = ..., clamplower: Optional[Union[float, bool]] = ..., cll: Optional[Union[float, bool]] = ..., clampupper: Optional[Union[float, bool]] = ..., clu: Optional[Union[float, bool]] = ..., clear: bool = ..., clr: bool = ..., colorAlphaValue: Optional[Union[float, bool]] = ..., cl1: Optional[Union[float, bool]] = ..., colorRGBAValue: Optional[Union[Tuple[float, float, float, float], bool]] = ..., cl4: Optional[Union[Tuple[float, float, float, float], bool]] = ..., colorRGBValue: Optional[Union[Tuple[float, float, float], bool]] = ..., cl3: Optional[Union[Tuple[float, float, float], bool]] = ..., colorRamp: Optional[Union[str, bool]] = ..., cr: Optional[Union[str, bool]] = ..., colorfeedback: bool = ..., cf: bool = ..., colorfeedbackOverride: bool = ..., cfo: bool = ..., colorrangelower: Optional[Union[float, bool]] = ..., crl: Optional[Union[float, bool]] = ..., colorrangeupper: Optional[Union[float, bool]] = ..., cru: Optional[Union[float, bool]] = ..., dataTypeIndex: Optional[Union[int, bool]] = ..., dti: Optional[Union[int, bool]] = ..., disablelighting: bool = ..., dl: bool = ..., dragSlider: Optional[Union[str, bool]] = ..., dsl: Optional[Union[str, bool]] = ..., duringStrokeCmd: Optional[Union[str, bool]] = ..., dsk: Optional[Union[str, bool]] = ..., dynclonemode: bool = ..., dcm: bool = ..., exists: bool = ..., ex: bool = ..., expandfilename: bool = ..., eef: bool = ..., exportaspectratio: Optional[Union[float, bool]] = ..., ear: Optional[Union[float, bool]] = ..., exportfilemode: Optional[Union[str, bool]] = ..., efm: Optional[Union[str, bool]] = ..., exportfilesave: str = ..., esf: str = ..., exportfilesizex: Optional[Union[int, bool]] = ..., fsx: Optional[Union[int, bool]] = ..., exportfilesizey: Optional[Union[int, bool]] = ..., fsy: Optional[Union[int, bool]] = ..., exportfiletype: Optional[Union[str, bool]] = ..., eft: Optional[Union[str, bool]] = ..., filterNodes: bool = ..., fon: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., importfileload: str = ..., ifl: str = ..., importfilemode: Optional[Union[str, bool]] = ..., ifm: Optional[Union[str, bool]] = ..., importreassign: bool = ..., irm: bool = ..., interactiveUpdate: bool = ..., iu: bool = ..., lastRecorderCmd: Optional[Union[str, bool]] = ..., lrc: Optional[Union[str, bool]] = ..., lastStampName: Optional[Union[str, bool]] = ..., lsn: Optional[Union[str, bool]] = ..., lowerradius: Optional[Union[float, bool]] = ..., lr: Optional[Union[float, bool]] = ..., makeStroke: Optional[Union[int, bool]] = ..., mst: Optional[Union[int, bool]] = ..., mappressure: Optional[Union[str, bool]] = ..., mp: Optional[Union[str, bool]] = ..., maxvalue: Optional[Union[float, bool]] = ..., mxv: Optional[Union[float, bool]] = ..., minvalue: Optional[Union[float, bool]] = ..., miv: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., numericColorRamp: Optional[Union[str, bool]] = ..., ncr: Optional[Union[str, bool]] = ..., numericDisplayColor: Optional[Union[Tuple[float, float, float], bool]] = ..., ndc: Optional[Union[Tuple[float, float, float], bool]] = ..., numericDisplayPrecision: Optional[Union[int, bool]] = ..., ndp: Optional[Union[int, bool]] = ..., numericMaxColor: Optional[Union[Tuple[float, float, float], bool]] = ..., nxc: Optional[Union[Tuple[float, float, float], bool]] = ..., numericMinColor: Optional[Union[Tuple[float, float, float], bool]] = ..., nmc: Optional[Union[Tuple[float, float, float], bool]] = ..., objattrArray: Optional[Union[str, bool]] = ..., oaa: Optional[Union[str, bool]] = ..., objattrArrayNoMenu: Optional[Union[str, bool]] = ..., oan: Optional[Union[str, bool]] = ..., opacity: Optional[Union[float, bool]] = ..., op: Optional[Union[float, bool]] = ..., outline: bool = ..., o: bool = ..., outwhilepaint: bool = ..., owp: bool = ..., paintChannel: Optional[Union[str, bool]] = ..., pch: Optional[Union[str, bool]] = ..., paintComponent: Optional[Union[int, bool]] = ..., pc: Optional[Union[int, bool]] = ..., paintNodeArray: Optional[Union[str, bool]] = ..., pna: Optional[Union[str, bool]] = ..., paintNumChannels: Optional[Union[int, bool]] = ..., pnc: Optional[Union[int, bool]] = ..., paintRGBA: bool = ..., pc4: bool = ..., paintVertexFace: bool = ..., pvf: bool = ..., paintattrselected: str = ..., pas: str = ..., paintmode: Optional[Union[str, bool]] = ..., pm: Optional[Union[str, bool]] = ..., paintoperationtype: Optional[Union[str, bool]] = ..., pot: Optional[Union[str, bool]] = ..., pickColor: bool = ..., pcm: bool = ..., pickValue: bool = ..., pv: bool = ..., playbackCursor: Optional[Union[Tuple[float, float], bool]] = ..., plc: Optional[Union[Tuple[float, float], bool]] = ..., playbackPressure: Optional[Union[float, bool]] = ..., plp: Optional[Union[float, bool]] = ..., preserveclonesource: bool = ..., pcs: bool = ..., profileShapeFile: Optional[Union[str, bool]] = ..., psf: Optional[Union[str, bool]] = ..., projective: bool = ..., prm: bool = ..., radius: Optional[Union[float, bool]] = ..., r: Optional[Union[float, bool]] = ..., rampMaxColor: Optional[Union[Tuple[float, float, float], bool]] = ..., rxc: Optional[Union[Tuple[float, float, float], bool]] = ..., rampMinColor: Optional[Union[Tuple[float, float, float], bool]] = ..., rmc: Optional[Union[Tuple[float, float, float], bool]] = ..., record: bool = ..., rec: bool = ..., reflection: bool = ..., rn: bool = ..., reflectionaboutorigin: bool = ..., rno: bool = ..., reflectionaxis: Optional[Union[str, bool]] = ..., ra: Optional[Union[str, bool]] = ..., screenRadius: Optional[Union[float, bool]] = ..., scR: Optional[Union[float, bool]] = ..., selectclonesource: bool = ..., scs: bool = ..., selectedattroper: Optional[Union[str, bool]] = ..., sao: Optional[Union[str, bool]] = ..., showactive: bool = ..., sa: bool = ..., stampDepth: Optional[Union[float, bool]] = ..., stD: Optional[Union[float, bool]] = ..., stampProfile: Optional[Union[str, bool]] = ..., stP: Optional[Union[str, bool]] = ..., stampSpacing: Optional[Union[float, bool]] = ..., stS: Optional[Union[float, bool]] = ..., strokesmooth: Optional[Union[str, bool]] = ..., ssm: Optional[Union[str, bool]] = ..., surfaceConformedBrushVertices: bool = ..., scv: bool = ..., tablet: bool = ..., tab: bool = ..., tangentOutline: bool = ..., to: bool = ..., toolOffProc: Optional[Union[str, bool]] = ..., tfp: Optional[Union[str, bool]] = ..., toolOnProc: Optional[Union[str, bool]] = ..., top: Optional[Union[str, bool]] = ..., useColorRamp: bool = ..., ucr: bool = ..., useMaxMinColor: bool = ..., umc: bool = ..., useNumericColorRamp: bool = ..., unr: bool = ..., useNumericDisplay: bool = ..., und: bool = ..., usepressure: bool = ..., up: bool = ..., value: Optional[Union[float, bool]] = ..., val: Optional[Union[float, bool]] = ..., vertexColorRange: bool = ..., vcr: bool = ..., vertexColorRangeLower: Optional[Union[float, bool]] = ..., vcl: Optional[Union[float, bool]] = ..., vertexColorRangeUpper: Optional[Union[float, bool]] = ..., vcu: Optional[Union[float, bool]] = ..., whichTool: Optional[Union[str, bool]] = ..., wst: Optional[Union[str, bool]] = ..., worldRadius: Optional[Union[float, bool]] = ..., wlR: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This is a context command to set the flags on the artAttrContext,
    which is the base context for attribute painting operations. All
    commands require the name of the context as the last argument as
    this provides the name of the context to create, edit or query.
    
    This is a context command to set the flags on the
    Paint color on vertex Tool context.

    Args:
        accopacity | aco: (create, edit, query) - Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        activeListChangedProc | alp: (create, edit, query) - Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        afterStrokeCmd | asc: (create, edit, query) - The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        alphaclamp | alc: (create, edit, query) - Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        alphaclamplower | acl: (create, edit, query) - Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When queried, it returns a float.
        alphaclampupper | acu: (create, edit, query) - Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When queried, it returns a float.
        attrSelected | asl: (query) - Returns a name of the currently selected attribute. Q: When queried, it returns a string.
        beforeStrokeCmd | bsc: (create, edit, query) - The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        brushalignment | bra: (create, edit, query) - Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        brushfeedback | brf: (create, edit, query) - Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        clamp | cl: (create, edit, query) - Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        clamplower | cll: (create, edit, query) - Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried, it returns a float.
        clampupper | clu: (create, edit, query) - Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried, it returns a float.
        clear | clr: (create, edit) - Floods all cvs/vertices to the current value.
        colorAlphaValue | cl1: (create, edit, query) - The Alpha value of the color.
        colorRGBAValue | cl4: (create, edit, query) - The RGBA value of the color.
        colorRGBValue | cl3: (create, edit, query) - The RGB value of the color.
        colorRamp | cr: (create, edit, query) - Allows a user defined color ramp to be used to map values to colors.
        colorfeedback | cf: (create, edit, query) - Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorfeedbackOverride | cfo: (create, edit, query) - Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorrangelower | crl: (create, edit, query) - Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0.  Q: When queried, it returns a float.
        colorrangeupper | cru: (create, edit, query) - Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0.  Q: When queried, it returns a float.
        dataTypeIndex | dti: (edit, query) - When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
        disablelighting | dl: (create, edit, query) - If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE.  Q: When queried, it returns a boolean.
        dragSlider | dsl: (create, edit) - Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".
        duringStrokeCmd | dsk: (create, edit, query) - The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command
        dynclonemode | dcm: (create, edit, query) - Enable or disable dynamic clone mode.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        expandfilename | eef: (create, edit) - If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        exportaspectratio | ear: (create, edit, query) - Value of aspect ratio for export
        exportfilemode | efm: (create, edit, query) - Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        exportfilesave | esf: (edit) - Exports the attribute map and saves to a specified file.
        exportfilesizex | fsx: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfilesizey | fsy: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfiletype | eft: (create, edit, query) - Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        filterNodes | fon: (edit) - Sets the node filter.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        importfileload | ifl: (edit) - Load the attribute map a specified file.
        importfilemode | ifm: (create, edit, query) - Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        importreassign | irm: (create, edit, query) - Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        interactiveUpdate | iu: (create, edit, query) - Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When queried, it returns a boolean.
        lastRecorderCmd | lrc: (create, edit, query) - Value of last recorded command.
        lastStampName | lsn: (create, edit, query) - Value of the last stamp name.
        lowerradius | lr: (create, edit, query) - Sets the lower size of the brush (only apply on tablet).
        makeStroke | mst: (create, edit, multiuse, query) - Stroke point values.
        mappressure | mp: (create, edit, query) - Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        maxvalue | mxv: (create, edit, query) - Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When queried, it returns a float.
        minvalue | miv: (create, edit, query) - Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        numericColorRamp | ncr: (create, edit, query) - Allows a user defined color ramp to be used to map values to colors for the numeric display.
        numericDisplayColor | ndc: (create, edit, query) - Defines a color to be used when displaying numeric values.
        numericDisplayPrecision | ndp: (create, edit, query) - Specifies how many decimal points of precision should be used for the numeric display.
        numericMaxColor | nxc: (create, edit, query) - Defines a special color to be used when the value is greater than or equal to the maximum value.
        numericMinColor | nmc: (create, edit, query) - Defines a special color to be used when the value is less than or equal to the minimum value.
        objattrArray | oaa: (query) - An array of all paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.MenuType *MenuType: type (level) of the item in the Menu (UI). Q: When queried, it returns a string.
        objattrArrayNoMenu | oan: (query) - Returns an array of all paintable attributes in their original order. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName
        opacity | op: (create, edit, query) - Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        outline | o: (create, edit, query) - Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        outwhilepaint | owp: (create, edit, query) - Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        paintChannel | pch: (create, edit, query) - Channel to paint - RGB, RGBA, R, G, B, A
        paintComponent | pc: (create, edit, query) - Specifies whether face or vertex or vertex face is being painted. 1 - Vertex 2 - VertexFace 3 - Face C: Default is Vertex.  Q: When queried, it returns a int.
        paintNodeArray | pna: (query) - An array of paintable nodes. Q: When queried, it returns a string.
        paintNumChannels | pnc: (create, edit, query) - Number of channels to paint - 1 (alpha), 3 (RGB), or 4 (RGBA)
        paintRGBA | pc4: (create, edit, query) - Specifies whether RGB or RGBA channels are being painted. TRUE: RGBA channels. FALSE: RGB channels. Alpha channel remains unaffected. C: Default is FALSE (Painting RGB channels). Q: When queried, it returns a int.
        paintVertexFace | pvf: (create, edit, query) - Specifies whether vertex face is being painted. TRUE: Vertex face being painted. (Allows each face connected to the vertex to be painted) FALSE: Vertex being painted.(affects all connected faces) C: Default is FALSE.  Q: When queried, it returns a int.
        paintattrselected | pas: (edit) - An array of selected paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.
        paintmode | pm: (create, edit, query) - Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        paintoperationtype | pot: (create, edit, query) - Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        pickColor | pcm: (create, edit, query) - Set pick color mode on or off
        pickValue | pv: (create, edit, query) - Toggle for picking
        playbackCursor | plc: (create, edit, multiuse, query) - Values for the playback cursor.
        playbackPressure | plp: (create, edit, multiuse, query) - Valus for the playback pressure.
        preserveclonesource | pcs: (create, edit, query) - Whether or not to preserve a clone source.
        profileShapeFile | psf: (edit, query) - Passes a name of the image file for the stamp shape profile.
        projective | prm: (create, edit, query) - Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        radius | r: (create, edit, query) - Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        rampMaxColor | rxc: (create, edit, query) - Defines a special color to be used when the value is greater than or equal to the maximum value.
        rampMinColor | rmc: (create, edit, query) - Defines a special color to be used when the value is less than or equal to the minimum value.
        record | rec: (create, edit, query) - Toggle on for recording.
        reflection | rn: (create, edit, query) - Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        reflectionaboutorigin | rno: (create, edit, query) - Toggle on to reflect about the origin
        reflectionaxis | ra: (create, edit, query) - Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        screenRadius | scR: (create, edit, query) - Brush radius on the screen
        selectclonesource | scs: (create, edit, query) - Toggle on to select the clone source
        selectedattroper | sao: (create, edit, query) - Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of the weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C: Default is "absolute".  Q: When queried, it returns a string.
        showactive | sa: (create, edit, query) - Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        stampDepth | stD: (create, edit, query) - Depth of the stamps
        stampProfile | stP: (create, edit, query) - Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        stampSpacing | stS: (create, edit, query) - Specifies the stamp spacing. Default is 1.0.
        strokesmooth | ssm: (create, edit, query) - Stroke smoothing type name
        surfaceConformedBrushVertices | scv: (create, edit, query) - Enables/disables the the display of the effective brush area as affected vertices.
        tablet | tab: (query) - Returns true if the tablet device is present, false if it is absent
        tangentOutline | to: (create, edit, query) - Enables/disables the display of the brush circle tangent to the surface.
        toolOffProc | tfp: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        toolOnProc | top: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        useColorRamp | ucr: (create, edit, query) - Specifies whether the user defined color ramp should be used to map values from to colors.  If this is turned off, the default greyscale feedback will be used.
        useMaxMinColor | umc: (create, edit, query) - Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        useNumericColorRamp | unr: (create, edit, query) - Specifies whether the user defined color ramp should be used to map values from to colors on the numeric display. If this is turned off, the set single numeric color will be used.
        useNumericDisplay | und: (create, edit, query) - Specifies whether numerical weight values should be displayed next to their associated control points.
        usepressure | up: (create, edit, query) - Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        value | val: (create, edit, query) - Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        vertexColorRange | vcr: (create, edit, query) - Specifies whether the vertex color range should be applied to the currently selected object. C: Default is false  Q: When queried, it returns a boolean.
        vertexColorRangeLower | vcl: (create, edit, query) - Specifies the min value of the vertex color range. C: Default is 0.0.  Q: When queried, it returns a float.
        vertexColorRangeUpper | vcu: (create, edit, query) - Specifies the max value of the vertex color range. C: Default is 1.0.  Q: When queried, it returns a float.
        whichTool | wst: (create, edit, query) - The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last when specifying a flag that takes arguments.
        worldRadius | wlR: (create, edit, query) - Radius in worldspace
    """
    ...


def artAttrSkinPaintCtx(*args, accopacity: bool = ..., aco: bool = ..., activeListChangedProc: Optional[Union[str, bool]] = ..., alp: Optional[Union[str, bool]] = ..., afterStrokeCmd: Optional[Union[str, bool]] = ..., asc: Optional[Union[str, bool]] = ..., alphaclamp: Optional[Union[str, bool]] = ..., alc: Optional[Union[str, bool]] = ..., alphaclamplower: Optional[Union[float, bool]] = ..., acl: Optional[Union[float, bool]] = ..., alphaclampupper: Optional[Union[float, bool]] = ..., acu: Optional[Union[float, bool]] = ..., attrSelected: Optional[Union[str, bool]] = ..., asl: Optional[Union[str, bool]] = ..., beforeStrokeCmd: Optional[Union[str, bool]] = ..., bsc: Optional[Union[str, bool]] = ..., brushalignment: bool = ..., bra: bool = ..., brushfeedback: bool = ..., brf: bool = ..., clamp: Optional[Union[str, bool]] = ..., cl: Optional[Union[str, bool]] = ..., clamplower: Optional[Union[float, bool]] = ..., cll: Optional[Union[float, bool]] = ..., clampupper: Optional[Union[float, bool]] = ..., clu: Optional[Union[float, bool]] = ..., clear: bool = ..., clr: bool = ..., colorAlphaValue: Optional[Union[float, bool]] = ..., cl1: Optional[Union[float, bool]] = ..., colorRGBAValue: Optional[Union[Tuple[float, float, float, float], bool]] = ..., cl4: Optional[Union[Tuple[float, float, float, float], bool]] = ..., colorRGBValue: Optional[Union[Tuple[float, float, float], bool]] = ..., cl3: Optional[Union[Tuple[float, float, float], bool]] = ..., colorRamp: Optional[Union[str, bool]] = ..., cr: Optional[Union[str, bool]] = ..., colorfeedback: bool = ..., cf: bool = ..., colorfeedbackOverride: bool = ..., cfo: bool = ..., colorrangelower: Optional[Union[float, bool]] = ..., crl: Optional[Union[float, bool]] = ..., colorrangeupper: Optional[Union[float, bool]] = ..., cru: Optional[Union[float, bool]] = ..., dataTypeIndex: Optional[Union[int, bool]] = ..., dti: Optional[Union[int, bool]] = ..., disablelighting: bool = ..., dl: bool = ..., dragSlider: Optional[Union[str, bool]] = ..., dsl: Optional[Union[str, bool]] = ..., duringStrokeCmd: Optional[Union[str, bool]] = ..., dsk: Optional[Union[str, bool]] = ..., dynclonemode: bool = ..., dcm: bool = ..., exists: bool = ..., ex: bool = ..., expandfilename: bool = ..., eef: bool = ..., exportaspectratio: Optional[Union[float, bool]] = ..., ear: Optional[Union[float, bool]] = ..., exportfilemode: Optional[Union[str, bool]] = ..., efm: Optional[Union[str, bool]] = ..., exportfilesave: str = ..., esf: str = ..., exportfilesizex: Optional[Union[int, bool]] = ..., fsx: Optional[Union[int, bool]] = ..., exportfilesizey: Optional[Union[int, bool]] = ..., fsy: Optional[Union[int, bool]] = ..., exportfiletype: Optional[Union[str, bool]] = ..., eft: Optional[Union[str, bool]] = ..., filterNodes: bool = ..., fon: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., importfileload: str = ..., ifl: str = ..., importfilemode: Optional[Union[str, bool]] = ..., ifm: Optional[Union[str, bool]] = ..., importreassign: bool = ..., irm: bool = ..., influence: Optional[Union[str, bool]] = ..., inf: Optional[Union[str, bool]] = ..., interactiveUpdate: bool = ..., iu: bool = ..., lastRecorderCmd: Optional[Union[str, bool]] = ..., lrc: Optional[Union[str, bool]] = ..., lastStampName: Optional[Union[str, bool]] = ..., lsn: Optional[Union[str, bool]] = ..., lowerradius: Optional[Union[float, bool]] = ..., lr: Optional[Union[float, bool]] = ..., makeStroke: Optional[Union[int, bool]] = ..., mst: Optional[Union[int, bool]] = ..., mappressure: Optional[Union[str, bool]] = ..., mp: Optional[Union[str, bool]] = ..., maxvalue: Optional[Union[float, bool]] = ..., mxv: Optional[Union[float, bool]] = ..., minvalue: Optional[Union[float, bool]] = ..., miv: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., numericColorRamp: Optional[Union[str, bool]] = ..., ncr: Optional[Union[str, bool]] = ..., numericDisplayColor: Optional[Union[Tuple[float, float, float], bool]] = ..., ndc: Optional[Union[Tuple[float, float, float], bool]] = ..., numericDisplayPrecision: Optional[Union[int, bool]] = ..., ndp: Optional[Union[int, bool]] = ..., numericMaxColor: Optional[Union[Tuple[float, float, float], bool]] = ..., nxc: Optional[Union[Tuple[float, float, float], bool]] = ..., numericMinColor: Optional[Union[Tuple[float, float, float], bool]] = ..., nmc: Optional[Union[Tuple[float, float, float], bool]] = ..., objattrArray: Optional[Union[str, bool]] = ..., oaa: Optional[Union[str, bool]] = ..., objattrArrayNoMenu: Optional[Union[str, bool]] = ..., oan: Optional[Union[str, bool]] = ..., opacity: Optional[Union[float, bool]] = ..., op: Optional[Union[float, bool]] = ..., outline: bool = ..., o: bool = ..., outwhilepaint: bool = ..., owp: bool = ..., paintNodeArray: Optional[Union[str, bool]] = ..., pna: Optional[Union[str, bool]] = ..., paintSelectMode: Optional[Union[int, bool]] = ..., psm: Optional[Union[int, bool]] = ..., paintattrselected: str = ..., pas: str = ..., paintmode: Optional[Union[str, bool]] = ..., pm: Optional[Union[str, bool]] = ..., paintoperationtype: Optional[Union[str, bool]] = ..., pot: Optional[Union[str, bool]] = ..., pickColor: bool = ..., pcm: bool = ..., pickValue: bool = ..., pv: bool = ..., playbackCursor: Optional[Union[Tuple[float, float], bool]] = ..., plc: Optional[Union[Tuple[float, float], bool]] = ..., playbackPressure: Optional[Union[float, bool]] = ..., plp: Optional[Union[float, bool]] = ..., preserveclonesource: bool = ..., pcs: bool = ..., profileShapeFile: Optional[Union[str, bool]] = ..., psf: Optional[Union[str, bool]] = ..., projective: bool = ..., prm: bool = ..., radius: Optional[Union[float, bool]] = ..., r: Optional[Union[float, bool]] = ..., rampMaxColor: Optional[Union[Tuple[float, float, float], bool]] = ..., rxc: Optional[Union[Tuple[float, float, float], bool]] = ..., rampMinColor: Optional[Union[Tuple[float, float, float], bool]] = ..., rmc: Optional[Union[Tuple[float, float, float], bool]] = ..., record: bool = ..., rec: bool = ..., reflection: bool = ..., rn: bool = ..., reflectionaboutorigin: bool = ..., rno: bool = ..., reflectionaxis: Optional[Union[str, bool]] = ..., ra: Optional[Union[str, bool]] = ..., screenRadius: Optional[Union[float, bool]] = ..., scR: Optional[Union[float, bool]] = ..., selectclonesource: bool = ..., scs: bool = ..., selectedattroper: Optional[Union[str, bool]] = ..., sao: Optional[Union[str, bool]] = ..., showactive: bool = ..., sa: bool = ..., skinPaintMode: Optional[Union[int, bool]] = ..., spm: Optional[Union[int, bool]] = ..., stampDepth: Optional[Union[float, bool]] = ..., stD: Optional[Union[float, bool]] = ..., stampProfile: Optional[Union[str, bool]] = ..., stP: Optional[Union[str, bool]] = ..., stampSpacing: Optional[Union[float, bool]] = ..., stS: Optional[Union[float, bool]] = ..., strokesmooth: Optional[Union[str, bool]] = ..., ssm: Optional[Union[str, bool]] = ..., surfaceConformedBrushVertices: bool = ..., scv: bool = ..., tablet: bool = ..., tab: bool = ..., tangentOutline: bool = ..., to: bool = ..., toolOffProc: Optional[Union[str, bool]] = ..., tfp: Optional[Union[str, bool]] = ..., toolOnProc: Optional[Union[str, bool]] = ..., top: Optional[Union[str, bool]] = ..., useColorRamp: bool = ..., ucr: bool = ..., useMaxMinColor: bool = ..., umc: bool = ..., useNumericColorRamp: bool = ..., unr: bool = ..., useNumericDisplay: bool = ..., und: bool = ..., usepressure: bool = ..., up: bool = ..., value: Optional[Union[float, bool]] = ..., val: Optional[Union[float, bool]] = ..., whichTool: Optional[Union[str, bool]] = ..., wst: Optional[Union[str, bool]] = ..., worldRadius: Optional[Union[float, bool]] = ..., wlR: Optional[Union[float, bool]] = ..., xrayJoints: bool = ..., xry: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This is a context command to set the flags on the artAttrContext,
    which is the base context for attribute painting operations. All
    commands require the name of the context as the last argument as
    this provides the name of the context to create, edit or query.
    
    This is a context command to set the flags on the
    Paint skin weights tool context.

    Args:
        accopacity | aco: (create, edit, query) - Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        activeListChangedProc | alp: (create, edit, query) - Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        afterStrokeCmd | asc: (create, edit, query) - The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        alphaclamp | alc: (create, edit, query) - Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        alphaclamplower | acl: (create, edit, query) - Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When queried, it returns a float.
        alphaclampupper | acu: (create, edit, query) - Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When queried, it returns a float.
        attrSelected | asl: (query) - Returns a name of the currently selected attribute. Q: When queried, it returns a string.
        beforeStrokeCmd | bsc: (create, edit, query) - The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        brushalignment | bra: (create, edit, query) - Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        brushfeedback | brf: (create, edit, query) - Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        clamp | cl: (create, edit, query) - Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        clamplower | cll: (create, edit, query) - Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried, it returns a float.
        clampupper | clu: (create, edit, query) - Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried, it returns a float.
        clear | clr: (create, edit) - Floods all cvs/vertices to the current value.
        colorAlphaValue | cl1: (create, edit, query) - The Alpha value of the color.
        colorRGBAValue | cl4: (create, edit, query) - The RGBA value of the color.
        colorRGBValue | cl3: (create, edit, query) - The RGB value of the color.
        colorRamp | cr: (create, edit, query) - Allows a user defined color ramp to be used to map values to colors.
        colorfeedback | cf: (create, edit, query) - Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorfeedbackOverride | cfo: (create, edit, query) - Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorrangelower | crl: (create, edit, query) - Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0.  Q: When queried, it returns a float.
        colorrangeupper | cru: (create, edit, query) - Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0.  Q: When queried, it returns a float.
        dataTypeIndex | dti: (edit, query) - When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
        disablelighting | dl: (create, edit, query) - If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE.  Q: When queried, it returns a boolean.
        dragSlider | dsl: (create, edit) - Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".
        duringStrokeCmd | dsk: (create, edit, query) - The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command
        dynclonemode | dcm: (create, edit, query) - Enable or disable dynamic clone mode.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        expandfilename | eef: (create, edit) - If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        exportaspectratio | ear: (create, edit, query) - Value of aspect ratio for export
        exportfilemode | efm: (create, edit, query) - Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        exportfilesave | esf: (edit) - Exports the attribute map and saves to a specified file.
        exportfilesizex | fsx: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfilesizey | fsy: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfiletype | eft: (create, edit, query) - Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        filterNodes | fon: (edit) - Sets the node filter.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        importfileload | ifl: (edit) - Load the attribute map a specified file.
        importfilemode | ifm: (create, edit, query) - Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        importreassign | irm: (create, edit, query) - Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        influence | inf: (edit, query) - Specifies which joint has been selected by the user for painting. Q: When queried, it returns a string.
        interactiveUpdate | iu: (create, edit, query) - Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When queried, it returns a boolean.
        lastRecorderCmd | lrc: (create, edit, query) - Value of last recorded command.
        lastStampName | lsn: (create, edit, query) - Value of the last stamp name.
        lowerradius | lr: (create, edit, query) - Sets the lower size of the brush (only apply on tablet).
        makeStroke | mst: (create, edit, multiuse, query) - Stroke point values.
        mappressure | mp: (create, edit, query) - Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        maxvalue | mxv: (create, edit, query) - Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When queried, it returns a float.
        minvalue | miv: (create, edit, query) - Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        numericColorRamp | ncr: (create, edit, query) - Allows a user defined color ramp to be used to map values to colors for the numeric display.
        numericDisplayColor | ndc: (create, edit, query) - Defines a color to be used when displaying numeric values.
        numericDisplayPrecision | ndp: (create, edit, query) - Specifies how many decimal points of precision should be used for the numeric display.
        numericMaxColor | nxc: (create, edit, query) - Defines a special color to be used when the value is greater than or equal to the maximum value.
        numericMinColor | nmc: (create, edit, query) - Defines a special color to be used when the value is less than or equal to the minimum value.
        objattrArray | oaa: (query) - An array of all paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.MenuType *MenuType: type (level) of the item in the Menu (UI). Q: When queried, it returns a string.
        objattrArrayNoMenu | oan: (query) - Returns an array of all paintable attributes in their original order. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName
        opacity | op: (create, edit, query) - Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        outline | o: (create, edit, query) - Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        outwhilepaint | owp: (create, edit, query) - Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        paintNodeArray | pna: (query) - An array of paintable nodes. Q: When queried, it returns a string.
        paintSelectMode | psm: (edit, query) - Specifies whether the paint select tool: adds to selection (1) removes from selection (2), toggles selection (3) Q: When queried, it returns an int as defined above.
        paintattrselected | pas: (edit) - An array of selected paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.
        paintmode | pm: (create, edit, query) - Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        paintoperationtype | pot: (create, edit, query) - Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        pickColor | pcm: (create, edit, query) - Set pick color mode on or off
        pickValue | pv: (create, edit, query) - Toggle for picking
        playbackCursor | plc: (create, edit, multiuse, query) - Values for the playback cursor.
        playbackPressure | plp: (create, edit, multiuse, query) - Valus for the playback pressure.
        preserveclonesource | pcs: (create, edit, query) - Whether or not to preserve a clone source.
        profileShapeFile | psf: (edit, query) - Passes a name of the image file for the stamp shape profile.
        projective | prm: (create, edit, query) - Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        radius | r: (create, edit, query) - Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        rampMaxColor | rxc: (create, edit, query) - Defines a special color to be used when the value is greater than or equal to the maximum value.
        rampMinColor | rmc: (create, edit, query) - Defines a special color to be used when the value is less than or equal to the minimum value.
        record | rec: (create, edit, query) - Toggle on for recording.
        reflection | rn: (create, edit, query) - Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        reflectionaboutorigin | rno: (create, edit, query) - Toggle on to reflect about the origin
        reflectionaxis | ra: (create, edit, query) - Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        screenRadius | scR: (create, edit, query) - Brush radius on the screen
        selectclonesource | scs: (create, edit, query) - Toggle on to select the clone source
        selectedattroper | sao: (create, edit, query) - Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of the weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C: Default is "absolute".  Q: When queried, it returns a string.
        showactive | sa: (create, edit, query) - Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        skinPaintMode | spm: (edit, query) - Specifies whether the skin paint tool is in paint skin weights mode (1) Marquee select mode (0), or paint select mode (2) Q: When queried, it returns an int as defined above.
        stampDepth | stD: (create, edit, query) - Depth of the stamps
        stampProfile | stP: (create, edit, query) - Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        stampSpacing | stS: (create, edit, query) - Specifies the stamp spacing. Default is 1.0.
        strokesmooth | ssm: (create, edit, query) - Stroke smoothing type name
        surfaceConformedBrushVertices | scv: (create, edit, query) - Enables/disables the the display of the effective brush area as affected vertices.
        tablet | tab: (query) - Returns true if the tablet device is present, false if it is absent
        tangentOutline | to: (create, edit, query) - Enables/disables the display of the brush circle tangent to the surface.
        toolOffProc | tfp: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        toolOnProc | top: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        useColorRamp | ucr: (create, edit, query) - Specifies whether the user defined color ramp should be used to map values from to colors.  If this is turned off, the default greyscale feedback will be used.
        useMaxMinColor | umc: (create, edit, query) - Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        useNumericColorRamp | unr: (create, edit, query) - Specifies whether the user defined color ramp should be used to map values from to colors on the numeric display. If this is turned off, the set single numeric color will be used.
        useNumericDisplay | und: (create, edit, query) - Specifies whether numerical weight values should be displayed next to their associated control points.
        usepressure | up: (create, edit, query) - Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        value | val: (create, edit, query) - Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        whichTool | wst: (create, edit, query) - The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last when specifying a flag that takes arguments.
        worldRadius | wlR: (create, edit, query) - Radius in worldspace
        xrayJoints | xry: (edit, query) - Specifies whether joints should be displayed in xray mode while painting Q: When queried, it returns a boolean.
    """
    ...


def artAttrTool(*args, add: Optional[Union[str, bool]] = ..., exists: Optional[Union[str, bool]] = ..., ex: Optional[Union[str, bool]] = ..., remove: Optional[Union[str, bool]] = ..., rm: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    The artAttrTool command manages the list of tool types which are
            used for attribute painting. This command supports querying the
            list contents as well as adding new tools to the list. Note that
            there is a set of built-in tools. The list of built-ins can
            be queried by starting Maya and doing an "artAttrTool -q".
    
            The tools which are managed by this command are all intended for
            attribute painting via Artisan: when you create a new context via
            artAttrCtx you specify the tool name via artAttrCtx's -whichTool
            flag. Typically the user may wish to simply use one of the built-in
            tools. However, if you need to have custom Properties and Values sheets
            asscociated with your tool, you will need to define a custom tool
            via artAttrTool -add "toolName". For an example of a custom
            attribute painting tool, see the devkit example customtoolPaint.mel.

    Args:
        add: (create) - Adds the named tool to the internal list of tools.
        exists | ex: (create, query) - Checks if the named tool exists, returning true if found, and false otherwise.
        remove | rm: (create) - Removes the named tool from the internal list of tools.
    """
    ...


def artFluidAttrCtx(*args, accopacity: bool = ..., aco: bool = ..., activeListChangedProc: Optional[Union[str, bool]] = ..., alp: Optional[Union[str, bool]] = ..., afterStrokeCmd: Optional[Union[str, bool]] = ..., asc: Optional[Union[str, bool]] = ..., alphaclamp: Optional[Union[str, bool]] = ..., alc: Optional[Union[str, bool]] = ..., alphaclamplower: Optional[Union[float, bool]] = ..., acl: Optional[Union[float, bool]] = ..., alphaclampupper: Optional[Union[float, bool]] = ..., acu: Optional[Union[float, bool]] = ..., attrSelected: Optional[Union[str, bool]] = ..., asl: Optional[Union[str, bool]] = ..., autoSave: Optional[Union[str, bool]] = ..., beforeStrokeCmd: Optional[Union[str, bool]] = ..., bsc: Optional[Union[str, bool]] = ..., brushalignment: bool = ..., bra: bool = ..., brushfeedback: bool = ..., brf: bool = ..., clamp: Optional[Union[str, bool]] = ..., cl: Optional[Union[str, bool]] = ..., clamplower: Optional[Union[float, bool]] = ..., cll: Optional[Union[float, bool]] = ..., clampupper: Optional[Union[float, bool]] = ..., clu: Optional[Union[float, bool]] = ..., clear: bool = ..., clr: bool = ..., colorAlphaValue: Optional[Union[float, bool]] = ..., cl1: Optional[Union[float, bool]] = ..., colorRGBAValue: Optional[Union[Tuple[float, float, float, float], bool]] = ..., cl4: Optional[Union[Tuple[float, float, float, float], bool]] = ..., colorRGBValue: Optional[Union[Tuple[float, float, float], bool]] = ..., cl3: Optional[Union[Tuple[float, float, float], bool]] = ..., colorRamp: Optional[Union[str, bool]] = ..., cr: Optional[Union[str, bool]] = ..., colorfeedback: bool = ..., cf: bool = ..., colorfeedbackOverride: bool = ..., cfo: bool = ..., colorrangelower: Optional[Union[float, bool]] = ..., crl: Optional[Union[float, bool]] = ..., colorrangeupper: Optional[Union[float, bool]] = ..., cru: Optional[Union[float, bool]] = ..., currentPaintableFluid: Optional[Union[str, bool]] = ..., cpf: Optional[Union[str, bool]] = ..., dataTypeIndex: Optional[Union[int, bool]] = ..., dti: Optional[Union[int, bool]] = ..., delaySelectionChanged: bool = ..., dsc: bool = ..., disablelighting: bool = ..., dl: bool = ..., displayAsRender: bool = ..., dar: bool = ..., displayVelocity: bool = ..., dv: bool = ..., doAutoSave: bool = ..., das: bool = ..., dragSlider: Optional[Union[str, bool]] = ..., dsl: Optional[Union[str, bool]] = ..., duringStrokeCmd: Optional[Union[str, bool]] = ..., dsk: Optional[Union[str, bool]] = ..., dynclonemode: bool = ..., dcm: bool = ..., exists: bool = ..., ex: bool = ..., expandfilename: bool = ..., eef: bool = ..., exportaspectratio: Optional[Union[float, bool]] = ..., ear: Optional[Union[float, bool]] = ..., exportfilemode: Optional[Union[str, bool]] = ..., efm: Optional[Union[str, bool]] = ..., exportfilesave: str = ..., esf: str = ..., exportfilesizex: Optional[Union[int, bool]] = ..., fsx: Optional[Union[int, bool]] = ..., exportfilesizey: Optional[Union[int, bool]] = ..., fsy: Optional[Union[int, bool]] = ..., exportfiletype: Optional[Union[str, bool]] = ..., eft: Optional[Union[str, bool]] = ..., filterNodes: bool = ..., fon: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., importfileload: str = ..., ifl: str = ..., importfilemode: Optional[Union[str, bool]] = ..., ifm: Optional[Union[str, bool]] = ..., importreassign: bool = ..., irm: bool = ..., interactiveUpdate: bool = ..., iu: bool = ..., lastRecorderCmd: Optional[Union[str, bool]] = ..., lrc: Optional[Union[str, bool]] = ..., lastStampName: Optional[Union[str, bool]] = ..., lsn: Optional[Union[str, bool]] = ..., lowerradius: Optional[Union[float, bool]] = ..., lr: Optional[Union[float, bool]] = ..., makeStroke: Optional[Union[int, bool]] = ..., mst: Optional[Union[int, bool]] = ..., mappressure: Optional[Union[str, bool]] = ..., mp: Optional[Union[str, bool]] = ..., maxvalue: Optional[Union[float, bool]] = ..., mxv: Optional[Union[float, bool]] = ..., minvalue: Optional[Union[float, bool]] = ..., miv: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., numericColorRamp: Optional[Union[str, bool]] = ..., ncr: Optional[Union[str, bool]] = ..., numericDisplayColor: Optional[Union[Tuple[float, float, float], bool]] = ..., ndc: Optional[Union[Tuple[float, float, float], bool]] = ..., numericDisplayPrecision: Optional[Union[int, bool]] = ..., ndp: Optional[Union[int, bool]] = ..., numericMaxColor: Optional[Union[Tuple[float, float, float], bool]] = ..., nxc: Optional[Union[Tuple[float, float, float], bool]] = ..., numericMinColor: Optional[Union[Tuple[float, float, float], bool]] = ..., nmc: Optional[Union[Tuple[float, float, float], bool]] = ..., objattrArray: Optional[Union[str, bool]] = ..., oaa: Optional[Union[str, bool]] = ..., objattrArrayNoMenu: Optional[Union[str, bool]] = ..., oan: Optional[Union[str, bool]] = ..., opacity: Optional[Union[float, bool]] = ..., op: Optional[Union[float, bool]] = ..., outline: bool = ..., o: bool = ..., outwhilepaint: bool = ..., owp: bool = ..., paintNodeArray: Optional[Union[str, bool]] = ..., pna: Optional[Union[str, bool]] = ..., paintattrselected: str = ..., pas: str = ..., paintmode: Optional[Union[str, bool]] = ..., pm: Optional[Union[str, bool]] = ..., paintoperationtype: Optional[Union[str, bool]] = ..., pot: Optional[Union[str, bool]] = ..., pickColor: bool = ..., pcm: bool = ..., pickValue: bool = ..., pv: bool = ..., playbackCursor: Optional[Union[Tuple[float, float], bool]] = ..., plc: Optional[Union[Tuple[float, float], bool]] = ..., playbackPressure: Optional[Union[float, bool]] = ..., plp: Optional[Union[float, bool]] = ..., preserveclonesource: bool = ..., pcs: bool = ..., profileShapeFile: Optional[Union[str, bool]] = ..., psf: Optional[Union[str, bool]] = ..., projective: bool = ..., prm: bool = ..., property: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., radius: Optional[Union[float, bool]] = ..., r: Optional[Union[float, bool]] = ..., rampMaxColor: Optional[Union[Tuple[float, float, float], bool]] = ..., rxc: Optional[Union[Tuple[float, float, float], bool]] = ..., rampMinColor: Optional[Union[Tuple[float, float, float], bool]] = ..., rmc: Optional[Union[Tuple[float, float, float], bool]] = ..., record: bool = ..., rec: bool = ..., reflection: bool = ..., rn: bool = ..., reflectionaboutorigin: bool = ..., rno: bool = ..., reflectionaxis: Optional[Union[str, bool]] = ..., ra: Optional[Union[str, bool]] = ..., rgbValue: Optional[Union[Tuple[float, float, float], bool]] = ..., rgb: Optional[Union[Tuple[float, float, float], bool]] = ..., screenRadius: Optional[Union[float, bool]] = ..., scR: Optional[Union[float, bool]] = ..., selectclonesource: bool = ..., scs: bool = ..., selectedattroper: Optional[Union[str, bool]] = ..., sao: Optional[Union[str, bool]] = ..., showactive: bool = ..., sa: bool = ..., stampDepth: Optional[Union[float, bool]] = ..., stD: Optional[Union[float, bool]] = ..., stampProfile: Optional[Union[str, bool]] = ..., stP: Optional[Union[str, bool]] = ..., stampSpacing: Optional[Union[float, bool]] = ..., stS: Optional[Union[float, bool]] = ..., strokesmooth: Optional[Union[str, bool]] = ..., ssm: Optional[Union[str, bool]] = ..., surfaceConformedBrushVertices: bool = ..., scv: bool = ..., tablet: bool = ..., tab: bool = ..., tangentOutline: bool = ..., to: bool = ..., toolOffProc: Optional[Union[str, bool]] = ..., tfp: Optional[Union[str, bool]] = ..., toolOnProc: Optional[Union[str, bool]] = ..., top: Optional[Union[str, bool]] = ..., useColorRamp: bool = ..., ucr: bool = ..., useMaxMinColor: bool = ..., umc: bool = ..., useNumericColorRamp: bool = ..., unr: bool = ..., useNumericDisplay: bool = ..., und: bool = ..., useStrokeDirection: bool = ..., usd: bool = ..., usepressure: bool = ..., up: bool = ..., value: Optional[Union[float, bool]] = ..., val: Optional[Union[float, bool]] = ..., velocity: Optional[Union[Tuple[float, float, float], bool]] = ..., v: Optional[Union[Tuple[float, float, float], bool]] = ..., whichTool: Optional[Union[str, bool]] = ..., wst: Optional[Union[str, bool]] = ..., worldRadius: Optional[Union[float, bool]] = ..., wlR: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This is a context command to set the flags on the artAttrContext,
    which is the base context for attribute painting operations. All
    commands require the name of the context as the last argument as
    this provides the name of the context to create, edit or query.
    
    This command is used to paint properties
    (such as density) of selected fluid volumes.

    Args:
        accopacity | aco: (create, edit, query) - Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        activeListChangedProc | alp: (create, edit, query) - Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        afterStrokeCmd | asc: (create, edit, query) - The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        alphaclamp | alc: (create, edit, query) - Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        alphaclamplower | acl: (create, edit, query) - Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When queried, it returns a float.
        alphaclampupper | acu: (create, edit, query) - Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When queried, it returns a float.
        attrSelected | asl: (query) - Returns a name of the currently selected attribute. Q: When queried, it returns a string.
        autoSave | autoSave: (create, edit, query) - A MEL command to save the fluid state.  Called before an event which could overwrite unsaved values of painted fluid properties.  Such events include: changing current time, changing the current paintable property, and exiting the paint tool.  (To turn auto-save off, pass in an empty-valued string argument: e.g., "".)
        beforeStrokeCmd | bsc: (create, edit, query) - The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        brushalignment | bra: (create, edit, query) - Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        brushfeedback | brf: (create, edit, query) - Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        clamp | cl: (create, edit, query) - Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        clamplower | cll: (create, edit, query) - Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried, it returns a float.
        clampupper | clu: (create, edit, query) - Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried, it returns a float.
        clear | clr: (create, edit) - Floods all cvs/vertices to the current value.
        colorAlphaValue | cl1: (create, edit, query) - The Alpha value of the color.
        colorRGBAValue | cl4: (create, edit, query) - The RGBA value of the color.
        colorRGBValue | cl3: (create, edit, query) - The RGB value of the color.
        colorRamp | cr: (create, edit, query) - Allows a user defined color ramp to be used to map values to colors.
        colorfeedback | cf: (create, edit, query) - Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorfeedbackOverride | cfo: (create, edit, query) - Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorrangelower | crl: (create, edit, query) - Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0.  Q: When queried, it returns a float.
        colorrangeupper | cru: (create, edit, query) - Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0.  Q: When queried, it returns a float.
        currentPaintableFluid | cpf: (query) - Query the name of the fluid on which this context is currently painting.  Returns string.
        dataTypeIndex | dti: (edit, query) - When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
        delaySelectionChanged | dsc: (create, edit, query) - Internal use only.  Under normal conditions, the tool responds to changes to the selection list so it can update its list of paintable geometry.  When -dsl true is used, the tool will not update its paintable list until a corresponding -dsl false is called.
        disablelighting | dl: (create, edit, query) - If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE.  Q: When queried, it returns a boolean.
        displayAsRender | dar: (create, edit, query) - When true, sets the "Shaded Display" attribute of the fluid to "AsRender": all fluid properties displayed as hardware rendered.  When false, displays only the currently selected paintable attribute of the fluid.
        displayVelocity | dv: (create, edit, query) - Turns on/off velocity display, independently of the above "dar/displayAsRender" setting.  Use this flag to enable velocity display while only displaying density, for example.
        doAutoSave | das: (edit) - Execute the -autoSave command if there are unsaved painted fluid properties.
        dragSlider | dsl: (create, edit) - Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".
        duringStrokeCmd | dsk: (create, edit, query) - The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command
        dynclonemode | dcm: (create, edit, query) - Enable or disable dynamic clone mode.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        expandfilename | eef: (create, edit) - If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        exportaspectratio | ear: (create, edit, query) - Value of aspect ratio for export
        exportfilemode | efm: (create, edit, query) - Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        exportfilesave | esf: (edit) - Exports the attribute map and saves to a specified file.
        exportfilesizex | fsx: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfilesizey | fsy: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfiletype | eft: (create, edit, query) - Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        filterNodes | fon: (edit) - Sets the node filter.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        importfileload | ifl: (edit) - Load the attribute map a specified file.
        importfilemode | ifm: (create, edit, query) - Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        importreassign | irm: (create, edit, query) - Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        interactiveUpdate | iu: (create, edit, query) - Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When queried, it returns a boolean.
        lastRecorderCmd | lrc: (create, edit, query) - Value of last recorded command.
        lastStampName | lsn: (create, edit, query) - Value of the last stamp name.
        lowerradius | lr: (create, edit, query) - Sets the lower size of the brush (only apply on tablet).
        makeStroke | mst: (create, edit, multiuse, query) - Stroke point values.
        mappressure | mp: (create, edit, query) - Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        maxvalue | mxv: (create, edit, query) - Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When queried, it returns a float.
        minvalue | miv: (create, edit, query) - Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        numericColorRamp | ncr: (create, edit, query) - Allows a user defined color ramp to be used to map values to colors for the numeric display.
        numericDisplayColor | ndc: (create, edit, query) - Defines a color to be used when displaying numeric values.
        numericDisplayPrecision | ndp: (create, edit, query) - Specifies how many decimal points of precision should be used for the numeric display.
        numericMaxColor | nxc: (create, edit, query) - Defines a special color to be used when the value is greater than or equal to the maximum value.
        numericMinColor | nmc: (create, edit, query) - Defines a special color to be used when the value is less than or equal to the minimum value.
        objattrArray | oaa: (query) - An array of all paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.MenuType *MenuType: type (level) of the item in the Menu (UI). Q: When queried, it returns a string.
        objattrArrayNoMenu | oan: (query) - Returns an array of all paintable attributes in their original order. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName
        opacity | op: (create, edit, query) - Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        outline | o: (create, edit, query) - Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        outwhilepaint | owp: (create, edit, query) - Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        paintNodeArray | pna: (query) - An array of paintable nodes. Q: When queried, it returns a string.
        paintattrselected | pas: (edit) - An array of selected paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.
        paintmode | pm: (create, edit, query) - Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        paintoperationtype | pot: (create, edit, query) - Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        pickColor | pcm: (create, edit, query) - Set pick color mode on or off
        pickValue | pv: (create, edit, query) - Toggle for picking
        playbackCursor | plc: (create, edit, multiuse, query) - Values for the playback cursor.
        playbackPressure | plp: (create, edit, multiuse, query) - Valus for the playback pressure.
        preserveclonesource | pcs: (create, edit, query) - Whether or not to preserve a clone source.
        profileShapeFile | psf: (edit, query) - Passes a name of the image file for the stamp shape profile.
        projective | prm: (create, edit, query) - Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        property | p: (create, edit, query) - Specifies a property to paint on the fluid. Valid values are "color", "density", "densityAndColor," "densityAndFuel," "temperature," "fuel", "velocity".
        radius | r: (create, edit, query) - Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        rampMaxColor | rxc: (create, edit, query) - Defines a special color to be used when the value is greater than or equal to the maximum value.
        rampMinColor | rmc: (create, edit, query) - Defines a special color to be used when the value is less than or equal to the minimum value.
        record | rec: (create, edit, query) - Toggle on for recording.
        reflection | rn: (create, edit, query) - Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        reflectionaboutorigin | rno: (create, edit, query) - Toggle on to reflect about the origin
        reflectionaxis | ra: (create, edit, query) - Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        rgbValue | rgb: (create, edit, query) - Specifies the values of the red, green, and blue components of the color to use when painting the property "color."
        screenRadius | scR: (create, edit, query) - Brush radius on the screen
        selectclonesource | scs: (create, edit, query) - Toggle on to select the clone source
        selectedattroper | sao: (create, edit, query) - Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of the weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C: Default is "absolute".  Q: When queried, it returns a string.
        showactive | sa: (create, edit, query) - Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        stampDepth | stD: (create, edit, query) - Depth of the stamps
        stampProfile | stP: (create, edit, query) - Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        stampSpacing | stS: (create, edit, query) - Specifies the stamp spacing. Default is 1.0.
        strokesmooth | ssm: (create, edit, query) - Stroke smoothing type name
        surfaceConformedBrushVertices | scv: (create, edit, query) - Enables/disables the the display of the effective brush area as affected vertices.
        tablet | tab: (query) - Returns true if the tablet device is present, false if it is absent
        tangentOutline | to: (create, edit, query) - Enables/disables the display of the brush circle tangent to the surface.
        toolOffProc | tfp: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        toolOnProc | top: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        useColorRamp | ucr: (create, edit, query) - Specifies whether the user defined color ramp should be used to map values from to colors.  If this is turned off, the default greyscale feedback will be used.
        useMaxMinColor | umc: (create, edit, query) - Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        useNumericColorRamp | unr: (create, edit, query) - Specifies whether the user defined color ramp should be used to map values from to colors on the numeric display. If this is turned off, the set single numeric color will be used.
        useNumericDisplay | und: (create, edit, query) - Specifies whether numerical weight values should be displayed next to their associated control points.
        useStrokeDirection | usd: (create, edit, query) - Applicable only during "velocity" painting.  Specifies whether the value of the painted velocity should come from the direction of the brush stroke, overriding the value specified by the -v/-velocity flag.
        usepressure | up: (create, edit, query) - Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        value | val: (create, edit, query) - Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        velocity | v: (create, edit, query) - Specifies the values of the x, y, and z components of the velocity to use when painting the property "velocity".
        whichTool | wst: (create, edit, query) - The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last when specifying a flag that takes arguments.
        worldRadius | wlR: (create, edit, query) - Radius in worldspace
    """
    ...


def artPuttyCtx(*args, accopacity: bool = ..., aco: bool = ..., activeListChangedProc: Optional[Union[str, bool]] = ..., alp: Optional[Union[str, bool]] = ..., afterStrokeCmd: Optional[Union[str, bool]] = ..., asc: Optional[Union[str, bool]] = ..., alphaclamp: Optional[Union[str, bool]] = ..., alc: Optional[Union[str, bool]] = ..., alphaclamplower: Optional[Union[float, bool]] = ..., acl: Optional[Union[float, bool]] = ..., alphaclampupper: Optional[Union[float, bool]] = ..., acu: Optional[Union[float, bool]] = ..., attrSelected: Optional[Union[str, bool]] = ..., asl: Optional[Union[str, bool]] = ..., autosmooth: bool = ..., asm: bool = ..., beforeStrokeCmd: Optional[Union[str, bool]] = ..., bsc: Optional[Union[str, bool]] = ..., brushStrength: Optional[Union[float, bool]] = ..., bs: Optional[Union[float, bool]] = ..., brushalignment: bool = ..., bra: bool = ..., brushfeedback: bool = ..., brf: bool = ..., clamp: Optional[Union[str, bool]] = ..., cl: Optional[Union[str, bool]] = ..., clamplower: Optional[Union[float, bool]] = ..., cll: Optional[Union[float, bool]] = ..., clampupper: Optional[Union[float, bool]] = ..., clu: Optional[Union[float, bool]] = ..., clear: bool = ..., clr: bool = ..., collapsecvtol: Optional[Union[float, bool]] = ..., clc: Optional[Union[float, bool]] = ..., colorAlphaValue: Optional[Union[float, bool]] = ..., cl1: Optional[Union[float, bool]] = ..., colorRGBAValue: Optional[Union[Tuple[float, float, float, float], bool]] = ..., cl4: Optional[Union[Tuple[float, float, float, float], bool]] = ..., colorRGBValue: Optional[Union[Tuple[float, float, float], bool]] = ..., cl3: Optional[Union[Tuple[float, float, float], bool]] = ..., colorRamp: Optional[Union[str, bool]] = ..., cr: Optional[Union[str, bool]] = ..., colorfeedback: bool = ..., cf: bool = ..., colorfeedbackOverride: bool = ..., cfo: bool = ..., colorrangelower: Optional[Union[float, bool]] = ..., crl: Optional[Union[float, bool]] = ..., colorrangeupper: Optional[Union[float, bool]] = ..., cru: Optional[Union[float, bool]] = ..., dataTypeIndex: Optional[Union[int, bool]] = ..., dti: Optional[Union[int, bool]] = ..., disablelighting: bool = ..., dl: bool = ..., dispdecr: bool = ..., dde: bool = ..., dispincr: bool = ..., din: bool = ..., dragSlider: Optional[Union[str, bool]] = ..., dsl: Optional[Union[str, bool]] = ..., duringStrokeCmd: Optional[Union[str, bool]] = ..., dsk: Optional[Union[str, bool]] = ..., dynclonemode: bool = ..., dcm: bool = ..., erasesrfupd: bool = ..., eut: bool = ..., exists: bool = ..., ex: bool = ..., expandfilename: bool = ..., eef: bool = ..., exportaspectratio: Optional[Union[float, bool]] = ..., ear: Optional[Union[float, bool]] = ..., exportfilemode: Optional[Union[str, bool]] = ..., efm: Optional[Union[str, bool]] = ..., exportfilesave: str = ..., esf: str = ..., exportfilesizex: Optional[Union[int, bool]] = ..., fsx: Optional[Union[int, bool]] = ..., exportfilesizey: Optional[Union[int, bool]] = ..., fsy: Optional[Union[int, bool]] = ..., exportfiletype: Optional[Union[str, bool]] = ..., eft: Optional[Union[str, bool]] = ..., filterNodes: bool = ..., fon: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., importfileload: str = ..., ifl: str = ..., importfilemode: Optional[Union[str, bool]] = ..., ifm: Optional[Union[str, bool]] = ..., importreassign: bool = ..., irm: bool = ..., interactiveUpdate: bool = ..., iu: bool = ..., invertrefvector: bool = ..., irv: bool = ..., lastRecorderCmd: Optional[Union[str, bool]] = ..., lrc: Optional[Union[str, bool]] = ..., lastStampName: Optional[Union[str, bool]] = ..., lsn: Optional[Union[str, bool]] = ..., lowerradius: Optional[Union[float, bool]] = ..., lr: Optional[Union[float, bool]] = ..., makeStroke: Optional[Union[int, bool]] = ..., mst: Optional[Union[int, bool]] = ..., mappressure: Optional[Union[str, bool]] = ..., mp: Optional[Union[str, bool]] = ..., maxdisp: Optional[Union[float, bool]] = ..., md: Optional[Union[float, bool]] = ..., maxvalue: Optional[Union[float, bool]] = ..., mxv: Optional[Union[float, bool]] = ..., minvalue: Optional[Union[float, bool]] = ..., miv: Optional[Union[float, bool]] = ..., mouldtypehead: Optional[Union[str, bool]] = ..., mth: Optional[Union[str, bool]] = ..., mouldtypemouse: Optional[Union[str, bool]] = ..., mtm: Optional[Union[str, bool]] = ..., mouldtypetail: Optional[Union[str, bool]] = ..., mtt: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., numericColorRamp: Optional[Union[str, bool]] = ..., ncr: Optional[Union[str, bool]] = ..., numericDisplayColor: Optional[Union[Tuple[float, float, float], bool]] = ..., ndc: Optional[Union[Tuple[float, float, float], bool]] = ..., numericDisplayPrecision: Optional[Union[int, bool]] = ..., ndp: Optional[Union[int, bool]] = ..., numericMaxColor: Optional[Union[Tuple[float, float, float], bool]] = ..., nxc: Optional[Union[Tuple[float, float, float], bool]] = ..., numericMinColor: Optional[Union[Tuple[float, float, float], bool]] = ..., nmc: Optional[Union[Tuple[float, float, float], bool]] = ..., objattrArray: Optional[Union[str, bool]] = ..., oaa: Optional[Union[str, bool]] = ..., objattrArrayNoMenu: Optional[Union[str, bool]] = ..., oan: Optional[Union[str, bool]] = ..., opacity: Optional[Union[float, bool]] = ..., op: Optional[Union[float, bool]] = ..., outline: bool = ..., o: bool = ..., outwhilepaint: bool = ..., owp: bool = ..., paintNodeArray: Optional[Union[str, bool]] = ..., pna: Optional[Union[str, bool]] = ..., paintattrselected: str = ..., pas: str = ..., paintmode: Optional[Union[str, bool]] = ..., pm: Optional[Union[str, bool]] = ..., paintoperationtype: Optional[Union[str, bool]] = ..., pot: Optional[Union[str, bool]] = ..., pickColor: bool = ..., pcm: bool = ..., pickValue: bool = ..., pv: bool = ..., playbackCursor: Optional[Union[Tuple[float, float], bool]] = ..., plc: Optional[Union[Tuple[float, float], bool]] = ..., playbackPressure: Optional[Union[float, bool]] = ..., plp: Optional[Union[float, bool]] = ..., polecv: bool = ..., pcv: bool = ..., preserveclonesource: bool = ..., pcs: bool = ..., profileShapeFile: Optional[Union[str, bool]] = ..., psf: Optional[Union[str, bool]] = ..., projective: bool = ..., prm: bool = ..., radius: Optional[Union[float, bool]] = ..., r: Optional[Union[float, bool]] = ..., rampMaxColor: Optional[Union[Tuple[float, float, float], bool]] = ..., rxc: Optional[Union[Tuple[float, float, float], bool]] = ..., rampMinColor: Optional[Union[Tuple[float, float, float], bool]] = ..., rmc: Optional[Union[Tuple[float, float, float], bool]] = ..., record: bool = ..., rec: bool = ..., reflection: bool = ..., rn: bool = ..., reflectionaboutorigin: bool = ..., rno: bool = ..., reflectionaxis: Optional[Union[str, bool]] = ..., ra: Optional[Union[str, bool]] = ..., refsurface: bool = ..., rs: bool = ..., refvector: Optional[Union[str, bool]] = ..., rv: Optional[Union[str, bool]] = ..., refvectoru: Optional[Union[float, bool]] = ..., rvu: Optional[Union[float, bool]] = ..., refvectorv: Optional[Union[float, bool]] = ..., rvv: Optional[Union[float, bool]] = ..., screenRadius: Optional[Union[float, bool]] = ..., scR: Optional[Union[float, bool]] = ..., selectclonesource: bool = ..., scs: bool = ..., selectedattroper: Optional[Union[str, bool]] = ..., sao: Optional[Union[str, bool]] = ..., showactive: bool = ..., sa: bool = ..., smoothiters: Optional[Union[int, bool]] = ..., si: Optional[Union[int, bool]] = ..., stampDepth: Optional[Union[float, bool]] = ..., stD: Optional[Union[float, bool]] = ..., stampProfile: Optional[Union[str, bool]] = ..., stP: Optional[Union[str, bool]] = ..., stampSpacing: Optional[Union[float, bool]] = ..., stS: Optional[Union[float, bool]] = ..., stitchcorner: bool = ..., stc: bool = ..., stitchedgeflood: bool = ..., sef: bool = ..., stitchtype: Optional[Union[str, bool]] = ..., stt: Optional[Union[str, bool]] = ..., strokesmooth: Optional[Union[str, bool]] = ..., ssm: Optional[Union[str, bool]] = ..., surfaceConformedBrushVertices: bool = ..., scv: bool = ..., tablet: bool = ..., tab: bool = ..., tangentOutline: bool = ..., to: bool = ..., toolOffProc: Optional[Union[str, bool]] = ..., tfp: Optional[Union[str, bool]] = ..., toolOnProc: Optional[Union[str, bool]] = ..., top: Optional[Union[str, bool]] = ..., updateerasesrf: bool = ..., ues: bool = ..., updaterefsrf: bool = ..., urs: bool = ..., useColorRamp: bool = ..., ucr: bool = ..., useMaxMinColor: bool = ..., umc: bool = ..., useNumericColorRamp: bool = ..., unr: bool = ..., useNumericDisplay: bool = ..., und: bool = ..., usepressure: bool = ..., up: bool = ..., value: Optional[Union[float, bool]] = ..., val: Optional[Union[float, bool]] = ..., whichTool: Optional[Union[str, bool]] = ..., wst: Optional[Union[str, bool]] = ..., worldRadius: Optional[Union[float, bool]] = ..., wlR: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This is a context command to set the flags on the artAttrContext,
    which is the base context for attribute painting operations. All
    commands require the name of the context as the last argument as
    this provides the name of the context to create, edit or query.
    
    This command is used to modify NURBS surfaces using a brush based
    interface (Maya Artisan). This is accomplished by moving the control
    vertices (CVs) under the brush in the specified direction.

    Args:
        accopacity | aco: (create, edit, query) - Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        activeListChangedProc | alp: (create, edit, query) - Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        afterStrokeCmd | asc: (create, edit, query) - The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        alphaclamp | alc: (create, edit, query) - Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        alphaclamplower | acl: (create, edit, query) - Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When queried, it returns a float.
        alphaclampupper | acu: (create, edit, query) - Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When queried, it returns a float.
        attrSelected | asl: (query) - Returns a name of the currently selected attribute. Q: When queried, it returns a string.
        autosmooth | asm: (create, edit, query) - Sets up the auto smoothing option. When the brush is in the smooth mode, adjusting the strength will adjust how fast the surfaces is smoothed out. C: Default is FALSE.  Q: When queried, it returns a boolean.
        beforeStrokeCmd | bsc: (create, edit, query) - The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        brushStrength | bs: (create, edit, query) - Sets the strength of the brush. Brush strength is supported by the pinch and slide brushes. In pinch mode, adjusting the strength will adjust how quickly the surface converges on the brush center. In slide mode, the strength scales the motion of the brush. C: Default is 1.0.  Q: When queried, it returns a float.
        brushalignment | bra: (create, edit, query) - Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        brushfeedback | brf: (create, edit, query) - Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        clamp | cl: (create, edit, query) - Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        clamplower | cll: (create, edit, query) - Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried, it returns a float.
        clampupper | clu: (create, edit, query) - Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried, it returns a float.
        clear | clr: (create, edit) - Floods all cvs/vertices to the current value.
        collapsecvtol | clc: (create, edit, query) - Specifies the tolerance for the collapse cv detection. C: Default is 0.005 cm.  Q: When queried, it returns a float.
        colorAlphaValue | cl1: (create, edit, query) - The Alpha value of the color.
        colorRGBAValue | cl4: (create, edit, query) - The RGBA value of the color.
        colorRGBValue | cl3: (create, edit, query) - The RGB value of the color.
        colorRamp | cr: (create, edit, query) - Allows a user defined color ramp to be used to map values to colors.
        colorfeedback | cf: (create, edit, query) - Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorfeedbackOverride | cfo: (create, edit, query) - Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorrangelower | crl: (create, edit, query) - Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0.  Q: When queried, it returns a float.
        colorrangeupper | cru: (create, edit, query) - Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0.  Q: When queried, it returns a float.
        dataTypeIndex | dti: (edit, query) - When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
        disablelighting | dl: (create, edit, query) - If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE.  Q: When queried, it returns a boolean.
        dispdecr | dde: (create, edit) - Decreases a maximum displacement by 10%.
        dispincr | din: (create, edit) - Increases a maximum displacement by 10%.
        dragSlider | dsl: (create, edit) - Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".
        duringStrokeCmd | dsk: (create, edit, query) - The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command
        dynclonemode | dcm: (create, edit, query) - Enable or disable dynamic clone mode.
        erasesrfupd | eut: (create, edit, query) - Toggles the update for the erase surface
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        expandfilename | eef: (create, edit) - If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        exportaspectratio | ear: (create, edit, query) - Value of aspect ratio for export
        exportfilemode | efm: (create, edit, query) - Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        exportfilesave | esf: (edit) - Exports the attribute map and saves to a specified file.
        exportfilesizex | fsx: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfilesizey | fsy: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfiletype | eft: (create, edit, query) - Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        filterNodes | fon: (edit) - Sets the node filter.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        importfileload | ifl: (edit) - Load the attribute map a specified file.
        importfilemode | ifm: (create, edit, query) - Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        importreassign | irm: (create, edit, query) - Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        interactiveUpdate | iu: (create, edit, query) - Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When queried, it returns a boolean.
        invertrefvector | irv: (create, edit, query) - Sets the invert of the reference vector option when the reflection is ON. If it is true, the reference vector for the reflected stroke is negated with respect to the original one. C: Default is FALSE. Q: When queried, it returns a boolean.
        lastRecorderCmd | lrc: (create, edit, query) - Value of last recorded command.
        lastStampName | lsn: (create, edit, query) - Value of the last stamp name.
        lowerradius | lr: (create, edit, query) - Sets the lower size of the brush (only apply on tablet).
        makeStroke | mst: (create, edit, multiuse, query) - Stroke point values.
        mappressure | mp: (create, edit, query) - Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        maxdisp | md: (create, edit, query) - Defines a maximum displacement ( maxDisp in [0.0..5.0] ). C: Default is 1.0.  Q: When queried, it returns a float.
        maxvalue | mxv: (create, edit, query) - Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When queried, it returns a float.
        minvalue | miv: (create, edit, query) - Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        mouldtypehead | mth: (create, edit, query) - Type of type mould to use
        mouldtypemouse | mtm: (create, edit, query) - Specifies the putty operations/mode ("push" - pushes CVs along the given direction (see refvector flag), "pull" - pulls CVs along the specified direction, "smooth" - smooths the sculpt, "erase" - erases the paint). C: Default is "push".  Q: When queried, it returns a string.
        mouldtypetail | mtt: (create, edit, query) - Type of eraser mould to use
        name | n: (create) - If this is a tool command, name the tool appropriately.
        numericColorRamp | ncr: (create, edit, query) - Allows a user defined color ramp to be used to map values to colors for the numeric display.
        numericDisplayColor | ndc: (create, edit, query) - Defines a color to be used when displaying numeric values.
        numericDisplayPrecision | ndp: (create, edit, query) - Specifies how many decimal points of precision should be used for the numeric display.
        numericMaxColor | nxc: (create, edit, query) - Defines a special color to be used when the value is greater than or equal to the maximum value.
        numericMinColor | nmc: (create, edit, query) - Defines a special color to be used when the value is less than or equal to the minimum value.
        objattrArray | oaa: (query) - An array of all paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.MenuType *MenuType: type (level) of the item in the Menu (UI). Q: When queried, it returns a string.
        objattrArrayNoMenu | oan: (query) - Returns an array of all paintable attributes in their original order. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName
        opacity | op: (create, edit, query) - Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        outline | o: (create, edit, query) - Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        outwhilepaint | owp: (create, edit, query) - Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        paintNodeArray | pna: (query) - An array of paintable nodes. Q: When queried, it returns a string.
        paintattrselected | pas: (edit) - An array of selected paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.
        paintmode | pm: (create, edit, query) - Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        paintoperationtype | pot: (create, edit, query) - Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        pickColor | pcm: (create, edit, query) - Set pick color mode on or off
        pickValue | pv: (create, edit, query) - Toggle for picking
        playbackCursor | plc: (create, edit, multiuse, query) - Values for the playback cursor.
        playbackPressure | plp: (create, edit, multiuse, query) - Valus for the playback pressure.
        polecv | pcv: (create, edit, query) - Pull all the pole CVs to the same position.
        preserveclonesource | pcs: (create, edit, query) - Whether or not to preserve a clone source.
        profileShapeFile | psf: (edit, query) - Passes a name of the image file for the stamp shape profile.
        projective | prm: (create, edit, query) - Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        radius | r: (create, edit, query) - Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        rampMaxColor | rxc: (create, edit, query) - Defines a special color to be used when the value is greater than or equal to the maximum value.
        rampMinColor | rmc: (create, edit, query) - Defines a special color to be used when the value is less than or equal to the minimum value.
        record | rec: (create, edit, query) - Toggle on for recording.
        reflection | rn: (create, edit, query) - Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        reflectionaboutorigin | rno: (create, edit, query) - Toggle on to reflect about the origin
        reflectionaxis | ra: (create, edit, query) - Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        refsurface | rs: (create, edit, query) - Sets on/off the update of the reference surface. If it is true the reference surface is automatically updated on the per stroke bases. If it is false, the user has to update the reference surface explicitly by pressing the update button (see updaterefsrf). C: Default is TRUE.  Q: When queried, it returns a boolean.
        refvector | rv: (create, edit, query) - Specifies the direction of the push/pull operation ("normal" - sculpt along normals, "firstnormal" - sculpt along the first normal of the stroke, "view" - sculpt along the view direction, "xaxis", "yaxis", "zaxis" - sculpt along a given axis directions, "uisoparm", "visoparm" - sculpt along U or V isoparametric lines), "uvvector" - sculpt along an arbitrary vector in UV space. C: Default is "normal".  Q: When queried, it returns a string.
        refvectoru | rvu: (create, edit, query) - Specifies the U component of the UV vector to be used when -refVector is set to "uvvector".
        refvectorv | rvv: (create, edit, query) - Specifies the V component of the UV vector to be used when -refVector is set to "uvvector".
        screenRadius | scR: (create, edit, query) - Brush radius on the screen
        selectclonesource | scs: (create, edit, query) - Toggle on to select the clone source
        selectedattroper | sao: (create, edit, query) - Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of the weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C: Default is "absolute".  Q: When queried, it returns a string.
        showactive | sa: (create, edit, query) - Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        smoothiters | si: (create, edit, query) - Sets the quality of the smoothing operation (number of iterations). C: Default is 3.  Q: When queried, it returns an int.
        stampDepth | stD: (create, edit, query) - Depth of the stamps
        stampProfile | stP: (create, edit, query) - Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        stampSpacing | stS: (create, edit, query) - Specifies the stamp spacing. Default is 1.0.
        stitchcorner | stc: (create, edit, query) - Sets on/off the stitching corner mode C: Default is "off".  Q: When queried, it returns a boolean.
        stitchedgeflood | sef: (edit) - Triggers postprocessing stitching edge procedure.
        stitchtype | stt: (create, edit, query) - Sets on/off the stitching mode ( "off" - stitching is turned off, "position" - position stitching is done without taking care about the tangent continuity C0, "tan" - C1 continuity is preserved). C: Default is "position".  Q: When queried, it returns a string.
        strokesmooth | ssm: (create, edit, query) - Stroke smoothing type name
        surfaceConformedBrushVertices | scv: (create, edit, query) - Enables/disables the the display of the effective brush area as affected vertices.
        tablet | tab: (query) - Returns true if the tablet device is present, false if it is absent
        tangentOutline | to: (create, edit, query) - Enables/disables the display of the brush circle tangent to the surface.
        toolOffProc | tfp: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        toolOnProc | top: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        updateerasesrf | ues: (create, edit) - Updates the erase surface.
        updaterefsrf | urs: (create, edit) - Updates the reference surface.
        useColorRamp | ucr: (create, edit, query) - Specifies whether the user defined color ramp should be used to map values from to colors.  If this is turned off, the default greyscale feedback will be used.
        useMaxMinColor | umc: (create, edit, query) - Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        useNumericColorRamp | unr: (create, edit, query) - Specifies whether the user defined color ramp should be used to map values from to colors on the numeric display. If this is turned off, the set single numeric color will be used.
        useNumericDisplay | und: (create, edit, query) - Specifies whether numerical weight values should be displayed next to their associated control points.
        usepressure | up: (create, edit, query) - Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        value | val: (create, edit, query) - Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        whichTool | wst: (create, edit, query) - The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last when specifying a flag that takes arguments.
        worldRadius | wlR: (create, edit, query) - Radius in worldspace
    """
    ...


def artSelectCtx(*args, accopacity: bool = ..., aco: bool = ..., addselection: bool = ..., ads: bool = ..., afterStrokeCmd: Optional[Union[str, bool]] = ..., asc: Optional[Union[str, bool]] = ..., beforeStrokeCmd: Optional[Union[str, bool]] = ..., bsc: Optional[Union[str, bool]] = ..., brushalignment: bool = ..., bra: bool = ..., brushfeedback: bool = ..., brf: bool = ..., clear: bool = ..., clr: bool = ..., dragSlider: Optional[Union[str, bool]] = ..., dsl: Optional[Union[str, bool]] = ..., dynclonemode: bool = ..., dcm: bool = ..., exists: bool = ..., ex: bool = ..., expandfilename: bool = ..., eef: bool = ..., exportaspectratio: Optional[Union[float, bool]] = ..., ear: Optional[Union[float, bool]] = ..., exportfilemode: Optional[Union[str, bool]] = ..., efm: Optional[Union[str, bool]] = ..., exportfilesave: str = ..., esf: str = ..., exportfilesizex: Optional[Union[int, bool]] = ..., fsx: Optional[Union[int, bool]] = ..., exportfilesizey: Optional[Union[int, bool]] = ..., fsy: Optional[Union[int, bool]] = ..., exportfiletype: Optional[Union[str, bool]] = ..., eft: Optional[Union[str, bool]] = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., importfileload: str = ..., ifl: str = ..., importfilemode: Optional[Union[str, bool]] = ..., ifm: Optional[Union[str, bool]] = ..., importreassign: bool = ..., irm: bool = ..., importthreshold: Optional[Union[float, bool]] = ..., ift: Optional[Union[float, bool]] = ..., lastRecorderCmd: Optional[Union[str, bool]] = ..., lrc: Optional[Union[str, bool]] = ..., lastStampName: Optional[Union[str, bool]] = ..., lsn: Optional[Union[str, bool]] = ..., lowerradius: Optional[Union[float, bool]] = ..., lr: Optional[Union[float, bool]] = ..., makeStroke: Optional[Union[int, bool]] = ..., mst: Optional[Union[int, bool]] = ..., mappressure: Optional[Union[str, bool]] = ..., mp: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., opacity: Optional[Union[float, bool]] = ..., op: Optional[Union[float, bool]] = ..., outline: bool = ..., o: bool = ..., outwhilepaint: bool = ..., owp: bool = ..., paintmode: Optional[Union[str, bool]] = ..., pm: Optional[Union[str, bool]] = ..., paintoperationtype: Optional[Union[str, bool]] = ..., pot: Optional[Union[str, bool]] = ..., pickColor: bool = ..., pcm: bool = ..., pickValue: bool = ..., pv: bool = ..., playbackCursor: Optional[Union[Tuple[float, float], bool]] = ..., plc: Optional[Union[Tuple[float, float], bool]] = ..., playbackPressure: Optional[Union[float, bool]] = ..., plp: Optional[Union[float, bool]] = ..., preserveclonesource: bool = ..., pcs: bool = ..., profileShapeFile: Optional[Union[str, bool]] = ..., psf: Optional[Union[str, bool]] = ..., projective: bool = ..., prm: bool = ..., radius: Optional[Union[float, bool]] = ..., r: Optional[Union[float, bool]] = ..., record: bool = ..., rec: bool = ..., reflection: bool = ..., rn: bool = ..., reflectionaboutorigin: bool = ..., rno: bool = ..., reflectionaxis: Optional[Union[str, bool]] = ..., ra: Optional[Union[str, bool]] = ..., screenRadius: Optional[Union[float, bool]] = ..., scR: Optional[Union[float, bool]] = ..., selectall: bool = ..., sal: bool = ..., selectclonesource: bool = ..., scs: bool = ..., selectop: Optional[Union[str, bool]] = ..., sop: Optional[Union[str, bool]] = ..., showactive: bool = ..., sa: bool = ..., stampDepth: Optional[Union[float, bool]] = ..., stD: Optional[Union[float, bool]] = ..., stampProfile: Optional[Union[str, bool]] = ..., stP: Optional[Union[str, bool]] = ..., stampSpacing: Optional[Union[float, bool]] = ..., stS: Optional[Union[float, bool]] = ..., strokesmooth: Optional[Union[str, bool]] = ..., ssm: Optional[Union[str, bool]] = ..., surfaceConformedBrushVertices: bool = ..., scv: bool = ..., tablet: bool = ..., tab: bool = ..., tangentOutline: bool = ..., to: bool = ..., toggleall: bool = ..., tal: bool = ..., unselectall: bool = ..., ual: bool = ..., usepressure: bool = ..., up: bool = ..., worldRadius: Optional[Union[float, bool]] = ..., wlR: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to select/deselect/toggle components on
    selected surfaces using a brush interface (Maya Artisan). Since,
    it selects components of the surface, it only works in the
    component mode.

    Args:
        accopacity | aco: (create, edit, query) - Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        addselection | ads: (create, edit, query) - If true, each new stroke adds cvs to the active list. If false, each stroke replaces the previous selection. C: Default is true. Q: When queried, it returns a boole
        afterStrokeCmd | asc: (create, edit, query) - The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        beforeStrokeCmd | bsc: (create, edit, query) - The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        brushalignment | bra: (create, edit, query) - Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        brushfeedback | brf: (create, edit, query) - Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        clear | clr: (create, edit) - Floods all cvs/vertices to the current value.
        dragSlider | dsl: (create, edit) - Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".
        dynclonemode | dcm: (create, edit, query) - Enable or disable dynamic clone mode.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        expandfilename | eef: (create, edit) - If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        exportaspectratio | ear: (create, edit, query) - Value of aspect ratio for export
        exportfilemode | efm: (create, edit, query) - Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        exportfilesave | esf: (edit) - Exports the attribute map and saves to a specified file.
        exportfilesizex | fsx: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfilesizey | fsy: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfiletype | eft: (create, edit, query) - Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        importfileload | ifl: (edit) - Load the attribute map a specified file.
        importfilemode | ifm: (create, edit, query) - Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        importreassign | irm: (create, edit, query) - Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        importthreshold | ift: (create, edit, query) - Specifies the threshold for the import of the attribute maps. C: Default is 0.5.  Q: When queried, it returns a float.
        lastRecorderCmd | lrc: (create, edit, query) - Value of last recorded command.
        lastStampName | lsn: (create, edit, query) - Value of the last stamp name.
        lowerradius | lr: (create, edit, query) - Sets the lower size of the brush (only apply on tablet).
        makeStroke | mst: (create, edit, multiuse, query) - Stroke point values.
        mappressure | mp: (create, edit, query) - Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        opacity | op: (create, edit, query) - Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        outline | o: (create, edit, query) - Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        outwhilepaint | owp: (create, edit, query) - Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        paintmode | pm: (create, edit, query) - Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        paintoperationtype | pot: (create, edit, query) - Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        pickColor | pcm: (create, edit, query) - Set pick color mode on or off
        pickValue | pv: (create, edit, query) - Toggle for picking
        playbackCursor | plc: (create, edit, multiuse, query) - Values for the playback cursor.
        playbackPressure | plp: (create, edit, multiuse, query) - Valus for the playback pressure.
        preserveclonesource | pcs: (create, edit, query) - Whether or not to preserve a clone source.
        profileShapeFile | psf: (edit, query) - Passes a name of the image file for the stamp shape profile.
        projective | prm: (create, edit, query) - Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        radius | r: (create, edit, query) - Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        record | rec: (create, edit, query) - Toggle on for recording.
        reflection | rn: (create, edit, query) - Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        reflectionaboutorigin | rno: (create, edit, query) - Toggle on to reflect about the origin
        reflectionaxis | ra: (create, edit, query) - Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        screenRadius | scR: (create, edit, query) - Brush radius on the screen
        selectall | sal: (create, edit) - Selects all vertices/egdes/faces/uvs.
        selectclonesource | scs: (create, edit, query) - Toggle on to select the clone source
        selectop | sop: (create, edit, query) - Specifies the selection operation ("select", "unselect", "toggle"). C: Default is "select". Q: When queried, it returns a string.
        showactive | sa: (create, edit, query) - Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        stampDepth | stD: (create, edit, query) - Depth of the stamps
        stampProfile | stP: (create, edit, query) - Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        stampSpacing | stS: (create, edit, query) - Specifies the stamp spacing. Default is 1.0.
        strokesmooth | ssm: (create, edit, query) - Stroke smoothing type name
        surfaceConformedBrushVertices | scv: (create, edit, query) - Enables/disables the the display of the effective brush area as affected vertices.
        tablet | tab: (query) - Returns true if the tablet device is present, false if it is absent
        tangentOutline | to: (create, edit, query) - Enables/disables the display of the brush circle tangent to the surface.
        toggleall | tal: (create, edit) - Toggle all vertices/egdes/faces/uvs.
        unselectall | ual: (create, edit) - Unselects all vertices/egdes/faces/uvs.
        usepressure | up: (create, edit, query) - Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        worldRadius | wlR: (create, edit, query) - Radius in worldspace
    """
    ...


def artSetPaintCtx(*args, accopacity: bool = ..., aco: bool = ..., afterStrokeCmd: Optional[Union[str, bool]] = ..., asc: Optional[Union[str, bool]] = ..., beforeStrokeCmd: Optional[Union[str, bool]] = ..., bsc: Optional[Union[str, bool]] = ..., brushalignment: bool = ..., bra: bool = ..., brushfeedback: bool = ..., brf: bool = ..., clear: bool = ..., clr: bool = ..., dragSlider: Optional[Union[str, bool]] = ..., dsl: Optional[Union[str, bool]] = ..., dynclonemode: bool = ..., dcm: bool = ..., exists: bool = ..., ex: bool = ..., expandfilename: bool = ..., eef: bool = ..., exportaspectratio: Optional[Union[float, bool]] = ..., ear: Optional[Union[float, bool]] = ..., exportfilemode: Optional[Union[str, bool]] = ..., efm: Optional[Union[str, bool]] = ..., exportfilesave: str = ..., esf: str = ..., exportfilesizex: Optional[Union[int, bool]] = ..., fsx: Optional[Union[int, bool]] = ..., exportfilesizey: Optional[Union[int, bool]] = ..., fsy: Optional[Union[int, bool]] = ..., exportfiletype: Optional[Union[str, bool]] = ..., eft: Optional[Union[str, bool]] = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., importfileload: str = ..., ifl: str = ..., importfilemode: Optional[Union[str, bool]] = ..., ifm: Optional[Union[str, bool]] = ..., importreassign: bool = ..., irm: bool = ..., lastRecorderCmd: Optional[Union[str, bool]] = ..., lrc: Optional[Union[str, bool]] = ..., lastStampName: Optional[Union[str, bool]] = ..., lsn: Optional[Union[str, bool]] = ..., lowerradius: Optional[Union[float, bool]] = ..., lr: Optional[Union[float, bool]] = ..., makeStroke: Optional[Union[int, bool]] = ..., mst: Optional[Union[int, bool]] = ..., mappressure: Optional[Union[str, bool]] = ..., mp: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., objectsetnames: Optional[Union[str, bool]] = ..., osn: Optional[Union[str, bool]] = ..., opacity: Optional[Union[float, bool]] = ..., op: Optional[Union[float, bool]] = ..., outline: bool = ..., o: bool = ..., outwhilepaint: bool = ..., owp: bool = ..., paintmode: Optional[Union[str, bool]] = ..., pm: Optional[Union[str, bool]] = ..., paintoperationtype: Optional[Union[str, bool]] = ..., pot: Optional[Union[str, bool]] = ..., pickColor: bool = ..., pcm: bool = ..., pickValue: bool = ..., pv: bool = ..., playbackCursor: Optional[Union[Tuple[float, float], bool]] = ..., plc: Optional[Union[Tuple[float, float], bool]] = ..., playbackPressure: Optional[Union[float, bool]] = ..., plp: Optional[Union[float, bool]] = ..., preserveclonesource: bool = ..., pcs: bool = ..., profileShapeFile: Optional[Union[str, bool]] = ..., psf: Optional[Union[str, bool]] = ..., projective: bool = ..., prm: bool = ..., radius: Optional[Union[float, bool]] = ..., r: Optional[Union[float, bool]] = ..., record: bool = ..., rec: bool = ..., reflection: bool = ..., rn: bool = ..., reflectionaboutorigin: bool = ..., rno: bool = ..., reflectionaxis: Optional[Union[str, bool]] = ..., ra: Optional[Union[str, bool]] = ..., screenRadius: Optional[Union[float, bool]] = ..., scR: Optional[Union[float, bool]] = ..., selectclonesource: bool = ..., scs: bool = ..., setcolorfeedback: bool = ..., scf: bool = ..., setdisplaycvs: bool = ..., dcv: bool = ..., setopertype: Optional[Union[str, bool]] = ..., sot: Optional[Union[str, bool]] = ..., settomodify: Optional[Union[str, bool]] = ..., stm: Optional[Union[str, bool]] = ..., showactive: bool = ..., sa: bool = ..., stampDepth: Optional[Union[float, bool]] = ..., stD: Optional[Union[float, bool]] = ..., stampProfile: Optional[Union[str, bool]] = ..., stP: Optional[Union[str, bool]] = ..., stampSpacing: Optional[Union[float, bool]] = ..., stS: Optional[Union[float, bool]] = ..., strokesmooth: Optional[Union[str, bool]] = ..., ssm: Optional[Union[str, bool]] = ..., surfaceConformedBrushVertices: bool = ..., scv: bool = ..., tablet: bool = ..., tab: bool = ..., tangentOutline: bool = ..., to: bool = ..., usepressure: bool = ..., up: bool = ..., worldRadius: Optional[Union[float, bool]] = ..., wlR: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This tool allows the user to modify the set membership
    (add, transfer, remove cvs) on nurbs surfaces using Maya
    Artisan's interface.

    Args:
        accopacity | aco: (create, edit, query) - Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        afterStrokeCmd | asc: (create, edit, query) - The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        beforeStrokeCmd | bsc: (create, edit, query) - The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        brushalignment | bra: (create, edit, query) - Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        brushfeedback | brf: (create, edit, query) - Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        clear | clr: (create, edit) - Floods all cvs/vertices to the current value.
        dragSlider | dsl: (create, edit) - Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".
        dynclonemode | dcm: (create, edit, query) - Enable or disable dynamic clone mode.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        expandfilename | eef: (create, edit) - If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        exportaspectratio | ear: (create, edit, query) - Value of aspect ratio for export
        exportfilemode | efm: (create, edit, query) - Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        exportfilesave | esf: (edit) - Exports the attribute map and saves to a specified file.
        exportfilesizex | fsx: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfilesizey | fsy: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfiletype | eft: (create, edit, query) - Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        importfileload | ifl: (edit) - Load the attribute map a specified file.
        importfilemode | ifm: (create, edit, query) - Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        importreassign | irm: (create, edit, query) - Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        lastRecorderCmd | lrc: (create, edit, query) - Value of last recorded command.
        lastStampName | lsn: (create, edit, query) - Value of the last stamp name.
        lowerradius | lr: (create, edit, query) - Sets the lower size of the brush (only apply on tablet).
        makeStroke | mst: (create, edit, multiuse, query) - Stroke point values.
        mappressure | mp: (create, edit, query) - Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        objectsetnames | osn: (create, edit, query) - Default name of object sets
        opacity | op: (create, edit, query) - Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        outline | o: (create, edit, query) - Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        outwhilepaint | owp: (create, edit, query) - Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        paintmode | pm: (create, edit, query) - Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        paintoperationtype | pot: (create, edit, query) - Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        pickColor | pcm: (create, edit, query) - Set pick color mode on or off
        pickValue | pv: (create, edit, query) - Toggle for picking
        playbackCursor | plc: (create, edit, multiuse, query) - Values for the playback cursor.
        playbackPressure | plp: (create, edit, multiuse, query) - Valus for the playback pressure.
        preserveclonesource | pcs: (create, edit, query) - Whether or not to preserve a clone source.
        profileShapeFile | psf: (edit, query) - Passes a name of the image file for the stamp shape profile.
        projective | prm: (create, edit, query) - Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        radius | r: (create, edit, query) - Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        record | rec: (create, edit, query) - Toggle on for recording.
        reflection | rn: (create, edit, query) - Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        reflectionaboutorigin | rno: (create, edit, query) - Toggle on to reflect about the origin
        reflectionaxis | ra: (create, edit, query) - Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        screenRadius | scR: (create, edit, query) - Brush radius on the screen
        selectclonesource | scs: (create, edit, query) - Toggle on to select the clone source
        setcolorfeedback | scf: (create, edit, query) - Specifies if the color feedback is on or off. C: Default is ON.  Q: When queried, it returns a boolean.
        setdisplaycvs | dcv: (create, edit, query) - Specifies if the active cvs are displayed. C: Default is ON. Q: When queried, it returns a boolean.
        setopertype | sot: (create, edit, query) - Specifies the setEdit operation ("add", "transfer", "remove"). C: Default is "add". Q: When queried, it returns a string.
        settomodify | stm: (create, edit, query) - Specifies the name of the set to modify. Q: When queried, it returns a string.
        showactive | sa: (create, edit, query) - Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        stampDepth | stD: (create, edit, query) - Depth of the stamps
        stampProfile | stP: (create, edit, query) - Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        stampSpacing | stS: (create, edit, query) - Specifies the stamp spacing. Default is 1.0.
        strokesmooth | ssm: (create, edit, query) - Stroke smoothing type name
        surfaceConformedBrushVertices | scv: (create, edit, query) - Enables/disables the the display of the effective brush area as affected vertices.
        tablet | tab: (query) - Returns true if the tablet device is present, false if it is absent
        tangentOutline | to: (create, edit, query) - Enables/disables the display of the brush circle tangent to the surface.
        usepressure | up: (create, edit, query) - Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        worldRadius | wlR: (create, edit, query) - Radius in worldspace
    """
    ...


def artUserPaintCtx(*args, accopacity: bool = ..., aco: bool = ..., activeListChangedProc: Optional[Union[str, bool]] = ..., alp: Optional[Union[str, bool]] = ..., afterStrokeCmd: Optional[Union[str, bool]] = ..., asc: Optional[Union[str, bool]] = ..., alphaclamp: Optional[Union[str, bool]] = ..., alc: Optional[Union[str, bool]] = ..., alphaclamplower: Optional[Union[float, bool]] = ..., acl: Optional[Union[float, bool]] = ..., alphaclampupper: Optional[Union[float, bool]] = ..., acu: Optional[Union[float, bool]] = ..., attrSelected: Optional[Union[str, bool]] = ..., asl: Optional[Union[str, bool]] = ..., beforeStrokeCmd: Optional[Union[str, bool]] = ..., bsc: Optional[Union[str, bool]] = ..., brushalignment: bool = ..., bra: bool = ..., brushfeedback: bool = ..., brf: bool = ..., chunkCommand: Optional[Union[str, bool]] = ..., cc: Optional[Union[str, bool]] = ..., clamp: Optional[Union[str, bool]] = ..., cl: Optional[Union[str, bool]] = ..., clamplower: Optional[Union[float, bool]] = ..., cll: Optional[Union[float, bool]] = ..., clampupper: Optional[Union[float, bool]] = ..., clu: Optional[Union[float, bool]] = ..., clear: bool = ..., clr: bool = ..., colorAlphaValue: Optional[Union[float, bool]] = ..., cl1: Optional[Union[float, bool]] = ..., colorRGBAValue: Optional[Union[Tuple[float, float, float, float], bool]] = ..., cl4: Optional[Union[Tuple[float, float, float, float], bool]] = ..., colorRGBValue: Optional[Union[Tuple[float, float, float], bool]] = ..., cl3: Optional[Union[Tuple[float, float, float], bool]] = ..., colorRamp: Optional[Union[str, bool]] = ..., cr: Optional[Union[str, bool]] = ..., colorfeedback: bool = ..., cf: bool = ..., colorfeedbackOverride: bool = ..., cfo: bool = ..., colorrangelower: Optional[Union[float, bool]] = ..., crl: Optional[Union[float, bool]] = ..., colorrangeupper: Optional[Union[float, bool]] = ..., cru: Optional[Union[float, bool]] = ..., dataTypeIndex: Optional[Union[int, bool]] = ..., dti: Optional[Union[int, bool]] = ..., disablelighting: bool = ..., dl: bool = ..., dragSlider: Optional[Union[str, bool]] = ..., dsl: Optional[Union[str, bool]] = ..., duringStrokeCmd: Optional[Union[str, bool]] = ..., dsk: Optional[Union[str, bool]] = ..., dynclonemode: bool = ..., dcm: bool = ..., exists: bool = ..., ex: bool = ..., expandfilename: bool = ..., eef: bool = ..., exportaspectratio: Optional[Union[float, bool]] = ..., ear: Optional[Union[float, bool]] = ..., exportfilemode: Optional[Union[str, bool]] = ..., efm: Optional[Union[str, bool]] = ..., exportfilesave: str = ..., esf: str = ..., exportfilesizex: Optional[Union[int, bool]] = ..., fsx: Optional[Union[int, bool]] = ..., exportfilesizey: Optional[Union[int, bool]] = ..., fsy: Optional[Union[int, bool]] = ..., exportfiletype: Optional[Union[str, bool]] = ..., eft: Optional[Union[str, bool]] = ..., filterNodes: bool = ..., fon: bool = ..., finalizeCmd: Optional[Union[str, bool]] = ..., fc: Optional[Union[str, bool]] = ..., fullpaths: bool = ..., fp: bool = ..., getArrayAttrCommand: Optional[Union[str, bool]] = ..., gac: Optional[Union[str, bool]] = ..., getSurfaceCommand: Optional[Union[str, bool]] = ..., gsc: Optional[Union[str, bool]] = ..., getValueCommand: Optional[Union[str, bool]] = ..., gvc: Optional[Union[str, bool]] = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., importfileload: str = ..., ifl: str = ..., importfilemode: Optional[Union[str, bool]] = ..., ifm: Optional[Union[str, bool]] = ..., importreassign: bool = ..., irm: bool = ..., initializeCmd: Optional[Union[str, bool]] = ..., ic: Optional[Union[str, bool]] = ..., interactiveUpdate: bool = ..., iu: bool = ..., lastRecorderCmd: Optional[Union[str, bool]] = ..., lrc: Optional[Union[str, bool]] = ..., lastStampName: Optional[Union[str, bool]] = ..., lsn: Optional[Union[str, bool]] = ..., lowerradius: Optional[Union[float, bool]] = ..., lr: Optional[Union[float, bool]] = ..., makeStroke: Optional[Union[int, bool]] = ..., mst: Optional[Union[int, bool]] = ..., mappressure: Optional[Union[str, bool]] = ..., mp: Optional[Union[str, bool]] = ..., maxvalue: Optional[Union[float, bool]] = ..., mxv: Optional[Union[float, bool]] = ..., minvalue: Optional[Union[float, bool]] = ..., miv: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., numericColorRamp: Optional[Union[str, bool]] = ..., ncr: Optional[Union[str, bool]] = ..., numericDisplayColor: Optional[Union[Tuple[float, float, float], bool]] = ..., ndc: Optional[Union[Tuple[float, float, float], bool]] = ..., numericDisplayPrecision: Optional[Union[int, bool]] = ..., ndp: Optional[Union[int, bool]] = ..., numericMaxColor: Optional[Union[Tuple[float, float, float], bool]] = ..., nxc: Optional[Union[Tuple[float, float, float], bool]] = ..., numericMinColor: Optional[Union[Tuple[float, float, float], bool]] = ..., nmc: Optional[Union[Tuple[float, float, float], bool]] = ..., objattrArray: Optional[Union[str, bool]] = ..., oaa: Optional[Union[str, bool]] = ..., objattrArrayNoMenu: Optional[Union[str, bool]] = ..., oan: Optional[Union[str, bool]] = ..., opacity: Optional[Union[float, bool]] = ..., op: Optional[Union[float, bool]] = ..., outline: bool = ..., o: bool = ..., outwhilepaint: bool = ..., owp: bool = ..., paintNodeArray: Optional[Union[str, bool]] = ..., pna: Optional[Union[str, bool]] = ..., paintattrselected: str = ..., pas: str = ..., paintmode: Optional[Union[str, bool]] = ..., pm: Optional[Union[str, bool]] = ..., paintoperationtype: Optional[Union[str, bool]] = ..., pot: Optional[Union[str, bool]] = ..., pickColor: bool = ..., pcm: bool = ..., pickValue: bool = ..., pv: bool = ..., playbackCursor: Optional[Union[Tuple[float, float], bool]] = ..., plc: Optional[Union[Tuple[float, float], bool]] = ..., playbackPressure: Optional[Union[float, bool]] = ..., plp: Optional[Union[float, bool]] = ..., preserveclonesource: bool = ..., pcs: bool = ..., profileShapeFile: Optional[Union[str, bool]] = ..., psf: Optional[Union[str, bool]] = ..., projective: bool = ..., prm: bool = ..., radius: Optional[Union[float, bool]] = ..., r: Optional[Union[float, bool]] = ..., rampMaxColor: Optional[Union[Tuple[float, float, float], bool]] = ..., rxc: Optional[Union[Tuple[float, float, float], bool]] = ..., rampMinColor: Optional[Union[Tuple[float, float, float], bool]] = ..., rmc: Optional[Union[Tuple[float, float, float], bool]] = ..., record: bool = ..., rec: bool = ..., reflection: bool = ..., rn: bool = ..., reflectionaboutorigin: bool = ..., rno: bool = ..., reflectionaxis: Optional[Union[str, bool]] = ..., ra: Optional[Union[str, bool]] = ..., screenRadius: Optional[Union[float, bool]] = ..., scR: Optional[Union[float, bool]] = ..., selectclonesource: bool = ..., scs: bool = ..., selectedattroper: Optional[Union[str, bool]] = ..., sao: Optional[Union[str, bool]] = ..., setArrayValueCommand: Optional[Union[str, bool]] = ..., sac: Optional[Union[str, bool]] = ..., setValueCommand: Optional[Union[str, bool]] = ..., svc: Optional[Union[str, bool]] = ..., showactive: bool = ..., sa: bool = ..., stampDepth: Optional[Union[float, bool]] = ..., stD: Optional[Union[float, bool]] = ..., stampProfile: Optional[Union[str, bool]] = ..., stP: Optional[Union[str, bool]] = ..., stampSpacing: Optional[Union[float, bool]] = ..., stS: Optional[Union[float, bool]] = ..., strokesmooth: Optional[Union[str, bool]] = ..., ssm: Optional[Union[str, bool]] = ..., surfaceConformedBrushVertices: bool = ..., scv: bool = ..., tablet: bool = ..., tab: bool = ..., tangentOutline: bool = ..., to: bool = ..., toolCleanupCmd: Optional[Union[str, bool]] = ..., tcc: Optional[Union[str, bool]] = ..., toolOffProc: Optional[Union[str, bool]] = ..., tfp: Optional[Union[str, bool]] = ..., toolOnProc: Optional[Union[str, bool]] = ..., top: Optional[Union[str, bool]] = ..., toolSetupCmd: Optional[Union[str, bool]] = ..., tsc: Optional[Union[str, bool]] = ..., useColorRamp: bool = ..., ucr: bool = ..., useMaxMinColor: bool = ..., umc: bool = ..., useNumericColorRamp: bool = ..., unr: bool = ..., useNumericDisplay: bool = ..., und: bool = ..., usepressure: bool = ..., up: bool = ..., value: Optional[Union[float, bool]] = ..., val: Optional[Union[float, bool]] = ..., whichTool: Optional[Union[str, bool]] = ..., wst: Optional[Union[str, bool]] = ..., worldRadius: Optional[Union[float, bool]] = ..., wlR: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This is a context command to set the flags on the artAttrContext,
    which is the base context for attribute painting operations. All
    commands require the name of the context as the last argument as
    this provides the name of the context to create, edit or query.
    
    This command executes a scriptable paint (Maya Artisan). It
    allows the user to apply Mel commands/scripts to modify cvs'
    attributes for all cvs under the paint brush.

    Args:
        accopacity | aco: (create, edit, query) - Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        activeListChangedProc | alp: (create, edit, query) - Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        afterStrokeCmd | asc: (create, edit, query) - The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        alphaclamp | alc: (create, edit, query) - Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        alphaclamplower | acl: (create, edit, query) - Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When queried, it returns a float.
        alphaclampupper | acu: (create, edit, query) - Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When queried, it returns a float.
        attrSelected | asl: (query) - Returns a name of the currently selected attribute. Q: When queried, it returns a string.
        beforeStrokeCmd | bsc: (create, edit, query) - The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        brushalignment | bra: (create, edit, query) - Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        brushfeedback | brf: (create, edit, query) - Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        chunkCommand | cc: (create, edit, query) - Specifies th name of the Mel script/procedure that is called once for every selected surface when a chunk is received on that surface. Q: When queried, it returns a string.
        clamp | cl: (create, edit, query) - Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        clamplower | cll: (create, edit, query) - Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried, it returns a float.
        clampupper | clu: (create, edit, query) - Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried, it returns a float.
        clear | clr: (create, edit) - Floods all cvs/vertices to the current value.
        colorAlphaValue | cl1: (create, edit, query) - The Alpha value of the color.
        colorRGBAValue | cl4: (create, edit, query) - The RGBA value of the color.
        colorRGBValue | cl3: (create, edit, query) - The RGB value of the color.
        colorRamp | cr: (create, edit, query) - Allows a user defined color ramp to be used to map values to colors.
        colorfeedback | cf: (create, edit, query) - Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorfeedbackOverride | cfo: (create, edit, query) - Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorrangelower | crl: (create, edit, query) - Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0.  Q: When queried, it returns a float.
        colorrangeupper | cru: (create, edit, query) - Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0.  Q: When queried, it returns a float.
        dataTypeIndex | dti: (edit, query) - When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
        disablelighting | dl: (create, edit, query) - If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE.  Q: When queried, it returns a boolean.
        dragSlider | dsl: (create, edit) - Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".
        duringStrokeCmd | dsk: (create, edit, query) - The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command
        dynclonemode | dcm: (create, edit, query) - Enable or disable dynamic clone mode.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        expandfilename | eef: (create, edit) - If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        exportaspectratio | ear: (create, edit, query) - Value of aspect ratio for export
        exportfilemode | efm: (create, edit, query) - Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        exportfilesave | esf: (edit) - Exports the attribute map and saves to a specified file.
        exportfilesizex | fsx: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfilesizey | fsy: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfiletype | eft: (create, edit, query) - Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        filterNodes | fon: (edit) - Sets the node filter.
        finalizeCmd | fc: (create, edit, query) - Specifies the name of the Mel script/procedure that is called at the end of each stroke. Q: When queried, it returns a string.
        fullpaths | fp: (create, edit, query) - Specifies whether full path names should be used when surface names are passed to scripts. If false, just the surface name is passed. C: Default is false  Q: When queried, it returns a boolean.
        getArrayAttrCommand | gac: (create, edit, query) - Specifies the name of the Mel script/procedure that is called once for every surface that is selected for painting. This procedure returns a string, which is interpreted as a list of names referring to double array attributes on some dependency node. Q: When queried, it returns a string.
        getSurfaceCommand | gsc: (create, edit, query) - Specifies the name of the Mel script/procedure that is called once for every dependency node on the selection list, whenever Artisan processes the selection list. It returns the name of the surface to paint on. Q: When queried, it returns a string.
        getValueCommand | gvc: (create, edit, query) - Specifies the name of the Mel script/procedure that is called every time a value on the surface is needed by the scriptable paint tool. Q: When queried, it returns a string.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        importfileload | ifl: (edit) - Load the attribute map a specified file.
        importfilemode | ifm: (create, edit, query) - Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        importreassign | irm: (create, edit, query) - Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        initializeCmd | ic: (create, edit, query) - Specifies the name of the Mel script/procedure that is called in the beginning of each stroke. Q: When queried, it returns a string.
        interactiveUpdate | iu: (create, edit, query) - Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When queried, it returns a boolean.
        lastRecorderCmd | lrc: (create, edit, query) - Value of last recorded command.
        lastStampName | lsn: (create, edit, query) - Value of the last stamp name.
        lowerradius | lr: (create, edit, query) - Sets the lower size of the brush (only apply on tablet).
        makeStroke | mst: (create, edit, multiuse, query) - Stroke point values.
        mappressure | mp: (create, edit, query) - Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        maxvalue | mxv: (create, edit, query) - Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When queried, it returns a float.
        minvalue | miv: (create, edit, query) - Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        numericColorRamp | ncr: (create, edit, query) - Allows a user defined color ramp to be used to map values to colors for the numeric display.
        numericDisplayColor | ndc: (create, edit, query) - Defines a color to be used when displaying numeric values.
        numericDisplayPrecision | ndp: (create, edit, query) - Specifies how many decimal points of precision should be used for the numeric display.
        numericMaxColor | nxc: (create, edit, query) - Defines a special color to be used when the value is greater than or equal to the maximum value.
        numericMinColor | nmc: (create, edit, query) - Defines a special color to be used when the value is less than or equal to the minimum value.
        objattrArray | oaa: (query) - An array of all paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.MenuType *MenuType: type (level) of the item in the Menu (UI). Q: When queried, it returns a string.
        objattrArrayNoMenu | oan: (query) - Returns an array of all paintable attributes in their original order. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName
        opacity | op: (create, edit, query) - Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        outline | o: (create, edit, query) - Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        outwhilepaint | owp: (create, edit, query) - Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        paintNodeArray | pna: (query) - An array of paintable nodes. Q: When queried, it returns a string.
        paintattrselected | pas: (edit) - An array of selected paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.
        paintmode | pm: (create, edit, query) - Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        paintoperationtype | pot: (create, edit, query) - Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        pickColor | pcm: (create, edit, query) - Set pick color mode on or off
        pickValue | pv: (create, edit, query) - Toggle for picking
        playbackCursor | plc: (create, edit, multiuse, query) - Values for the playback cursor.
        playbackPressure | plp: (create, edit, multiuse, query) - Valus for the playback pressure.
        preserveclonesource | pcs: (create, edit, query) - Whether or not to preserve a clone source.
        profileShapeFile | psf: (edit, query) - Passes a name of the image file for the stamp shape profile.
        projective | prm: (create, edit, query) - Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        radius | r: (create, edit, query) - Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        rampMaxColor | rxc: (create, edit, query) - Defines a special color to be used when the value is greater than or equal to the maximum value.
        rampMinColor | rmc: (create, edit, query) - Defines a special color to be used when the value is less than or equal to the minimum value.
        record | rec: (create, edit, query) - Toggle on for recording.
        reflection | rn: (create, edit, query) - Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        reflectionaboutorigin | rno: (create, edit, query) - Toggle on to reflect about the origin
        reflectionaxis | ra: (create, edit, query) - Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        screenRadius | scR: (create, edit, query) - Brush radius on the screen
        selectclonesource | scs: (create, edit, query) - Toggle on to select the clone source
        selectedattroper | sao: (create, edit, query) - Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of the weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C: Default is "absolute".  Q: When queried, it returns a string.
        setArrayValueCommand | sac: (create, edit, query) - Specifies the name of the Mel script/procedure that is called for each paint stamp. A stamp may affect one or more values on the surface. This call rolls up all the calls that would be made to setValueCommand for the stamp into one call with array arguments. Q: When queried, it returns a string.
        setValueCommand | svc: (create, edit, query) - Specifies the name of the Mel script/procedure that is called every time a value on the surface is changed. Q: When queried, it returns a string.
        showactive | sa: (create, edit, query) - Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        stampDepth | stD: (create, edit, query) - Depth of the stamps
        stampProfile | stP: (create, edit, query) - Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        stampSpacing | stS: (create, edit, query) - Specifies the stamp spacing. Default is 1.0.
        strokesmooth | ssm: (create, edit, query) - Stroke smoothing type name
        surfaceConformedBrushVertices | scv: (create, edit, query) - Enables/disables the the display of the effective brush area as affected vertices.
        tablet | tab: (query) - Returns true if the tablet device is present, false if it is absent
        tangentOutline | to: (create, edit, query) - Enables/disables the display of the brush circle tangent to the surface.
        toolCleanupCmd | tcc: (create, edit, query) - Specifies the name of the Mel script/procedure that is called when this tool is exited. Q: When queried, it returns a string.
        toolOffProc | tfp: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        toolOnProc | top: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        toolSetupCmd | tsc: (create, edit, query) - Specifies the name of the Mel script/procedure that is called once for every selected surface when an initial click is received on that surface. Q: When queried, it returns a string.
        useColorRamp | ucr: (create, edit, query) - Specifies whether the user defined color ramp should be used to map values from to colors.  If this is turned off, the default greyscale feedback will be used.
        useMaxMinColor | umc: (create, edit, query) - Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        useNumericColorRamp | unr: (create, edit, query) - Specifies whether the user defined color ramp should be used to map values from to colors on the numeric display. If this is turned off, the set single numeric color will be used.
        useNumericDisplay | und: (create, edit, query) - Specifies whether numerical weight values should be displayed next to their associated control points.
        usepressure | up: (create, edit, query) - Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        value | val: (create, edit, query) - Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        whichTool | wst: (create, edit, query) - The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last when specifying a flag that takes arguments.
        worldRadius | wlR: (create, edit, query) - Radius in worldspace
    """
    ...


def assembly(*args, active: Optional[Union[str, bool]] = ..., a: Optional[Union[str, bool]] = ..., activeLabel: Optional[Union[str, bool]] = ..., al: Optional[Union[str, bool]] = ..., canCreate: Optional[Union[str, bool]] = ..., cc: Optional[Union[str, bool]] = ..., createOptionBoxProc: Optional[Union[str, bool]] = ..., cob: Optional[Union[str, bool]] = ..., createRepresentation: str = ..., cr: str = ..., defaultType: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., deleteRepresentation: str = ..., dr: str = ..., deregister: str = ..., d: str = ..., input: str = ..., isAType: Optional[Union[str, bool]] = ..., isa: Optional[Union[str, bool]] = ..., isTrackingMemberEdits: Optional[Union[str, bool]] = ..., ite: Optional[Union[str, bool]] = ..., label: Optional[Union[str, bool]] = ..., lbl: Optional[Union[str, bool]] = ..., listRepTypes: bool = ..., lrt: bool = ..., listRepTypesProc: Optional[Union[str, bool]] = ..., lrp: Optional[Union[str, bool]] = ..., listRepresentations: bool = ..., lr: bool = ..., listTypes: bool = ..., lt: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., newRepLabel: str = ..., nrl: str = ..., postCreateUIProc: Optional[Union[str, bool]] = ..., aoc: Optional[Union[str, bool]] = ..., proc: str = ..., prc: str = ..., renameRepresentation: str = ..., rnr: str = ..., repLabel: Optional[Union[str, bool]] = ..., rl: Optional[Union[str, bool]] = ..., repName: str = ..., rnm: str = ..., repNamespace: Optional[Union[str, bool]] = ..., rns: Optional[Union[str, bool]] = ..., repPostCreateUIProc: Optional[Union[str, bool]] = ..., poc: Optional[Union[str, bool]] = ..., repPreCreateUIProc: Optional[Union[str, bool]] = ..., pec: Optional[Union[str, bool]] = ..., repType: Optional[Union[str, bool]] = ..., rt: Optional[Union[str, bool]] = ..., repTypeLabel: Optional[Union[str, bool]] = ..., rtl: Optional[Union[str, bool]] = ..., repTypeLabelProc: Optional[Union[str, bool]] = ..., rtp: Optional[Union[str, bool]] = ..., type: Optional[Union[str, bool]] = ..., typ: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to register assemblies for the scene assembly
    framework, to create them, and to edit and query them.
    Assembly nodes are DAG nodes, and are therefore shown in the various
    DAG editors (Outliner, Hypergraph, Node Editor). At assembly creation time,
    the node name defaults to the node type name.
    The assembly command can create any node that is derived from the assembly
    node base class.  It also acts as a registry of these types, so that various
    scripting callbacks can be defined and registered with the assembly
    command.  These callbacks are invoked by Maya during operations on
    assembly nodes, and can be used to customize behavior.
    Registering a new assembly type
    When defining a new type of assembly derived from the assembly node
    base class, a number of procedures can be defined through the assembly
    command to properly integrate the new assembly node type into Maya.
    Most of these procedures are used to integrate the assembly type with the
    Maya user interface, and are not required for non-interactive
    scripting use.  For more information, see the MPxAssembly class
    description in the Maya API documentation.
    Some of the important procedures that can be registered through the assembly
    command are the following:
    
    listRepTypesProc
    Procedure to list the representation types that the new
    assembly type can create.  This allows Maya to query representation
    types that can be created by an assembly without actually creating an
    assembly node.
    
    repTypeLabelProc
    Procedure to return a (possibly localized) label which is shown in
    the user interface for the representation types the assembly can
    create.  The label should be a short, user-friendly, readable
    description of the representation type.
    createOptionBoxProc
    Procedure to populate an option box for creation options for the
    assembly type.  If defined, this procedure will populate an option box
    that is available for creation of that assembly's type.
    repPreCreateUIProc
    Procedure to provide a dialog before representation creation.  If
    defined, will be invoked by Maya so that the user can interactively
    make choices before the creation of a type of representation for the
    assembly.
    postCreateUIProc
    Procedure to provide a dialog after assembly creation.  If
    defined, will be invoked by Maya so that the user can interactively
    make choices and apply them to the assembly after its creation.

    Args:
        active | a: (edit, query) - Set the active representation by name, or query the name of the active representation. Edit mode can be applied to more than one assembly. Query mode will return a single string when only a single assembly is specified, and will return an array of strings when multiple assemblies are specified. Using an empty string as name means to inactivate the currently active representation.
        activeLabel | al: (edit, query) - Set the active representation by label, or query the label of the active representation. Edit mode can be applied to more than one assembly. Query mode will return a single string when only a single assembly is specified, and will return an array of strings when multiple assemblies are specified.
        canCreate | cc: (query) - Query the representation types the specific assembly can create.
        createOptionBoxProc | cob: (edit, query) - Set or query the option box menu procedure for a specific assembly type. The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        createRepresentation | cr: (edit) - Create and add a specific type of representation for an assembly. If the representation type needs additional parameters, they must be specified using the "input" flag. For example, the Maya scene assembly reference implementation Cache and Scene representations need an input file.
        defaultType | dt: (edit, query) - Set or query the default type of assembly.  When the assembly command is used to perform an operation on an assembly type rather than on an assembly object, it will be performed on the default type, unless the -type flag is used to specify an explicit assembly type.
        deleteRepresentation | dr: (edit) - Delete a specific representation from an assembly.
        deregister | d: (edit) - Deregister a registered assembly type. If the deregistered type is the default type, the default type will be set to the empty string.
        input | input: (edit) - Specify the additional parameters of representation creation procedure when creating a representation. This flag must be used with createRepresentation flag.
        isAType | isa: (query) - Query whether the given object is of an assembly type.
        isTrackingMemberEdits | ite: (query) - Query whether the given object is tracking member edits.
        label | lbl: (edit, query) - Set or query the label for an assembly type. Assembly type is specified with flag "type". If no type specified, the default type is used.
        listRepTypes | lrt: (query) - Query the supported representation types for a given assembly type.  The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        listRepTypesProc | lrp: (edit, query) - Set or query the procedure that provides the representation type list which an assembly type supports.  This procedure takes no argument, and returns a string array of representation types that represents the full set of representation types this assembly type can create.  The assembly type for which this procedure applies will be the default type, unless the type flag is used to specify an explicit assembly type.
        listRepresentations | lr: (query) - Query the created representations list for a specific assembly.  The -repType flag can be used to filter the list and return representations for a single representation type.  If the -repType flag is not used, all created representations will be returned.
        listTypes | lt: (query) - Query the supported assembly types.
        name | n: (create) - Specify the name of the assembly when creating it.
        newRepLabel | nrl: (edit) - Specify the representation label to set on representation label edit.
        postCreateUIProc | aoc: (edit, query) - Set or query the UI post-creation procedure for a given assembly type. This procedure will be invoked by Maya immediately after an assembly of the specified type is created from the UI, but not through scripting.  It can be used to invoke a dialog, to obtain and set initial parameters on a newly-created assembly.  The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        proc | prc: (edit) - Specify the procedure when setting the representation UI post- or pre-creation procedure, for a given assembly type.  The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        renameRepresentation | rnr: (edit) - Renames the representation that is the argument to this flag.  The repName flag must be used to provide the new name.
        repLabel | rl: (edit, query) - Query or edit the label of the representation that is the argument to this flag, for a given assembly.  In both query and edit modes, the -repLabel flag specifies the name of the representation.  In edit mode, the -newRepLabel flag must be used to specify the new representation label. 			In query mode, this flag needs a value.
        repName | rnm: (edit) - Specify the representation name to set on representation creation or rename. This flag is optional with the createRepresentation flag: if omitted, the assembly will name the representation.  It is mandatory with the renameRepresentation flag.
        repNamespace | rns: (query) - Query the representation namespace of this assembly node. The value returned is used by Maya for creating the namespace where nodes created by the activation of a representation will be added. If a name clash occurs when the namespace is added to its parent namespace, Maya will update repNamespace with the new name. Two namespaces are involved when dealing with an assembly node: the namespace of the assembly node itself (which this flag does not affect or query), and the namespace of its representations. The representation namespace is a child of its assembly node's namespace. The assembly node's namespace is set by its containing assembly, if it is nested, or by the top-level file. Either the assembly node's namespace, or the representation namespace, or both, can be the empty string. It should be noted that if the assembly node is nested, the assembly node's namespace will be (by virtue of its nesting) the representation namespace of its containing assembly.
        repPostCreateUIProc | poc: (edit, query) - Set or query the UI post-creation procedure for a specific representation type, and for a specific assembly type.  This procedure takes two arguments, the first the DAG path to the assembly, and the second the name of the representation.  It returns no value.  It will be invoked by Maya immediately after a representation of the specified type is created from the UI, but not through scripting.  It can be used to invoke a dialog, to obtain and set initial parameters on a newly-created representation.  The representation type is the argument of this flag. The -proc flag must be used to specify the procedure name.  The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type. 			In query mode, this flag needs a value.
        repPreCreateUIProc | pec: (edit, query) - Set or query the UI pre-creation procedure for a specific representation type, and for a specific assembly type.  This procedure takes no argument, and returns a string that is passed as an argument to the -input flag when Maya invokes the assembly command with the -createRepresentation flag. The representation pre-creation procedure is invoked by Maya immediately before creating a representation of the specified type from the UI, but not through scripting.  It can be used to invoke a dialog, to obtain the creation argument for a new representation.  The representation type is the argument of this flag.  The -proc flag must be used to specify the procedure name.  The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type. 			In query mode, this flag needs a value.
        repType | rt: (query) - Specify a representation type to use as a filter for the -listRepresentations query.  The representation type is the argument to this flag. 			In query mode, this flag needs a value.
        repTypeLabel | rtl: (query) - Query the label of the specific representation type. 			In query mode, this flag needs a value.
        repTypeLabelProc | rtp: (edit, query) - Set or query the procedure that provides the representation type label, for a given assembly type.  The procedure takes the representation type as its sole argument, and returns a localized representation type label. The assembly type for which this procedure applies will be the default type, unless the -type flag is used to specify an explicit assembly type.
        type | typ: (create, edit, query) - Set or query properties for the specified registered assembly type. 			In query mode, this flag needs a value.
    """
    ...


def attributeInfo(*args, allAttributes: bool = ..., all: bool = ..., bool: bool = ..., b: bool = ..., enumerated: bool = ..., e: bool = ..., hidden: bool = ..., h: bool = ..., inherited: bool = ..., internal: bool = ..., i: bool = ..., leaf: bool = ..., l: bool = ..., logicalAnd: bool = ..., multi: bool = ..., m: bool = ..., short: bool = ..., s: bool = ..., userInterface: bool = ..., ui: bool = ..., writable: bool = ..., w: bool = ..., type: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This command lists all of the attributes that are marked with certain
    flags.  Combinations of flags may be specified and all will be considered.
    (The method of combination depends on the state of the "logicalAnd/and" flag.)
    When the "allAttributes/all" flag is specified, attributes of all
    types will be listed.

    Args:
        allAttributes | all: (create) - Show all attributes associated with the node regardless of type. Use of this flag overrides any other attribute type flags and logical operation that may be specified on the command.
        bool | b: (create) - Show the attributes that are of type boolean. Use the 'on' state to get only boolean attributes; the 'off' state to ignore boolean attributes.
        enumerated | e: (create) - Show the attributes that are of type enumerated. Use the 'on' state to get only enumerated attributes; the 'off' state to ignore enumerated attributes.
        hidden | h: (create) - Show the attributes that are marked as hidden. Use the 'on' state to get hidden attributes; the 'off' state to get non-hidden attributes.
        inherited | inherited: (create) - Filter the attributes based on whether they belong to the node type directly or have been inherited from a root type (e.g. meshShape/direct or dagObject/inherited). Use the 'on' state to get only inherited attributes, the 'off' state to get only directly owned attributes, and leave the flag unspecified to get both.
        internal | i: (create) - Show the attributes that are marked as internal to the node. Use the 'on' state to get internal attributes; the 'off' state to get non-internal attributes.
        leaf | l: (create) - Show the attributes that are complex leaves (ie. that have parent attributes and have no children themselves). Use the 'on' state to get leaf attributes; the 'off' state to get non-leaf attributes.
        logicalAnd | logicalAnd: (create) - The default is to take the logical 'or' of the above conditions. Specifying this flag switches to the logical 'and' instead.
        multi | m: (create) - Show the attributes that are multis. Use the 'on' state to get multi attributes; the 'off' state to get non-multi attributes.
        short | s: (create) - Show the short attribute names instead of the long names.
        userInterface | ui: (create) - Show the UI-friendly attribute names instead of the Maya ASCII names. Takes precedence over the -s/-short flag if both are specified.
        writable | w: (create) - Show the attributes that are writable (ie. can have input connections). Use the 'on' state to get writable attributes; the 'off' state to get non-writable attributes.
        type | t: (create) - static node type from which to get 'affects' information
    """
    ...


def attributeName(*args, leaf: bool = ..., lf: bool = ..., long: bool = ..., l: bool = ..., nice: bool = ..., n: bool = ..., short: bool = ..., s: bool = ...) -> Any:
    r"""
    This command takes one "node.attribute"-style specifier on the command line
    and returns either the attribute's long, short, or nice name.  (The "nice" name,
    or UI name, is the name used to display the attribute in Maya's interface, and
    may be localized when running Maya in a language other than English.)
    If more than one "node.attribute" specifier is given on the command line,
    only the first valid specifier is processed.

    Args:
        leaf | lf: (create) - When false, shows parent multi attributes (like "controlPoints[2].xValue").  When true, shows only the leaf-level attribute name (like "xValue").  Default is true. Note that for incomplete attribute strings, like a missing multi-parent index ("controlPoints.xValue") or an incorrectly named compound (cntrlPnts[2].xValue), this flag defaults to true and provides a result as long as the named leaf-level attribute is defined for the node.
        long | l: (create) - Returns names in "long name" format like "translateX"
        nice | n: (create) - Returns names in "nice name" format like "Translate X"
        short | s: (create) - Returns names in "short name" format like "tx"
    """
    ...


def attributeQuery(*args, affectsAppearance: bool = ..., aa: bool = ..., affectsWorldspace: bool = ..., aws: bool = ..., attributeType: bool = ..., at: bool = ..., cachedInternally: bool = ..., ci: bool = ..., categories: bool = ..., ct: bool = ..., channelBox: bool = ..., ch: bool = ..., connectable: bool = ..., c: bool = ..., enum: bool = ..., e: bool = ..., exists: bool = ..., ex: bool = ..., hidden: bool = ..., h: bool = ..., indeterminant: bool = ..., idt: bool = ..., indexMatters: bool = ..., im: bool = ..., internal: bool = ..., i: bool = ..., internalGet: bool = ..., ig: bool = ..., internalSet: bool = ..., keyable: bool = ..., k: bool = ..., listChildren: bool = ..., lc: bool = ..., listDefault: bool = ..., ld: bool = ..., listEnum: bool = ..., le: bool = ..., listParent: bool = ..., lp: bool = ..., listSiblings: bool = ..., ls: bool = ..., localizedListEnum: bool = ..., lz: bool = ..., longName: bool = ..., ln: bool = ..., maxExists: bool = ..., mxe: bool = ..., maximum: bool = ..., max: bool = ..., message: bool = ..., msg: bool = ..., minExists: bool = ..., mne: bool = ..., minimum: bool = ..., min: bool = ..., multi: bool = ..., m: bool = ..., niceName: bool = ..., nn: bool = ..., node: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., numberOfChildren: bool = ..., nc: bool = ..., range: bool = ..., r: bool = ..., rangeExists: bool = ..., re: bool = ..., readable: bool = ..., rd: bool = ..., renderSource: bool = ..., rs: bool = ..., shortName: bool = ..., sn: bool = ..., softMax: bool = ..., smx: bool = ..., softMaxExists: bool = ..., sxe: bool = ..., softMin: bool = ..., smn: bool = ..., softMinExists: bool = ..., sme: bool = ..., softRange: bool = ..., s: bool = ..., softRangeExists: bool = ..., se: bool = ..., storable: bool = ..., st: bool = ..., type: Optional[Union[str, bool]] = ..., typ: Optional[Union[str, bool]] = ..., typeExact: Optional[Union[str, bool]] = ..., tex: Optional[Union[str, bool]] = ..., usedAsColor: bool = ..., uac: bool = ..., usedAsFilename: bool = ..., uaf: bool = ..., usesMultiBuilder: bool = ..., umb: bool = ..., worldspace: bool = ..., ws: bool = ..., writable: bool = ..., w: bool = ...) -> Any:
    r"""
    attributeQuery returns information about the configuration of an attribute.
    It handles both boolean flags, returning true or false, as well as other return values.
    Specifying more than one boolean flag will return the logical "and"
    of all the specified boolean flags.  You may not specify any two flags when both do not
    provide a boolean return type.  (eg. "-internal -hidden" is okay but "-range -hidden" or
    "-range -softRange" is not.)

    Args:
        affectsAppearance | aa: (create) - Return true if the attribute affects the appearance of the node
        affectsWorldspace | aws: (create) - Return the status of the attribute flag marking attributes affecting worldspace
        attributeType | at: (create) - Return the name of the attribute type (will be the same type names as described in the addAttr and addExtension commands).
        cachedInternally | ci: (create) - Return whether the attribute is cached within the node as well as in the datablock
        categories | ct: (create) - Return the categories to which the attribute belongs or an empty list if it does not belong to any.
        channelBox | ch: (create) - Return whether the attribute should show up in the channelBox or not
        connectable | c: (create) - Return the connectable status of the attribute
        enum | e: (create) - Return true if the attribute is a enum attribute
        exists | ex: (create) - Return true if the attribute exists
        hidden | h: (create) - Return the hidden status of the attribute
        indeterminant | idt: (create) - Return true if this attribute might be used in evaluation but it's not known for sure until evaluation time
        indexMatters | im: (create) - Return the indexMatters status of the attribute
        internal | i: (create) - Return true if the attribute is either internalSet or internalGet
        internalGet | ig: (create) - Return true if the attribute come from getCachedValue
        internalSet | internalSet: (create) - Return true if the attribute must be set through setCachedValue
        keyable | k: (create) - Return the keyable status of the attribute
        listChildren | lc: (create) - Return the list of children attributes of the given attribute.
        listDefault | ld: (create) - Return the default values of numeric and compound numeric attributes.
        listEnum | le: (create) - Return the list of enum strings for the given attribute.
        listParent | lp: (create) - Return the parent of the given attribute.
        listSiblings | ls: (create) - Return the list of sibling attributes of the given attribute.
        localizedListEnum | lz: (create) - Return the list of localized enum strings for the given attribute.
        longName | ln: (create) - Return the long name of the attribute.
        maxExists | mxe: (create) - Return true if the attribute has a hard maximum. A min does not have to be present.
        maximum | max: (create) - Return the hard maximum of the attribute's value
        message | msg: (create) - Return true if the attribute is a message attribute
        minExists | mne: (create) - Return true if the attribute has a hard minimum. A max does not have to be present.
        minimum | min: (create) - Return the hard minimum of the attribute's value
        multi | m: (create) - Return true if the attribute is a multi-attribute
        niceName | nn: (create) - Return the nice name (or "UI name") of the attribute.
        node | n: (create) - Use all attributes from node named NAME
        numberOfChildren | nc: (create) - Return the number of children the attribute has
        range | r: (create) - Return the hard range of the attribute's value
        rangeExists | re: (create) - Return true if the attribute has a hard range. Both min and max must be present.
        readable | rd: (create) - Return the readable status of the attribute
        renderSource | rs: (create) - Return whether this attribute is marked as a render source or not
        shortName | sn: (create) - Return the short name of the attribute.
        softMax | smx: (create) - Return the soft max (slider range) of the attribute's value
        softMaxExists | sxe: (create) - Return true if the attribute has a soft maximum. A min does not have to be present.
        softMin | smn: (create) - Return the soft min (slider range) of the attribute's value
        softMinExists | sme: (create) - Return true if the attribute has a soft minimum. A max does not have to be present.
        softRange | s: (create) - Return the soft range (slider range) of the attribute's value
        softRangeExists | se: (create) - Return true if the attribute has a soft range. Both min and max must be present.
        storable | st: (create) - Return true if the attribute is storable
        type | typ: (create) - Use static attributes from nodes of type TYPE.  Includes attributes inherited from parent class nodes.
        typeExact | tex: (create) - Use static attributes only from nodes of type TYPE.  Does not included inherited attributes.
        usedAsColor | uac: (create) - Return true if the attribute should bring up a color picker
        usedAsFilename | uaf: (create) - Return true if the attribute should bring up a file browser
        usesMultiBuilder | umb: (create) - Return true if the attribute is a multi-attribute and it uses the multi-builder to handle its data
        worldspace | ws: (create) - Return the status of the attribute flag marking worldspace attribute
        writable | w: (create) - Return the writable status of the attribute
    """
    ...


def bakePartialHistory(*args, allShapes: bool = ..., all: bool = ..., postSmooth: bool = ..., nps: bool = ..., preCache: bool = ..., pc: bool = ..., preDeformers: bool = ..., pre: bool = ..., prePostDeformers: bool = ..., ppt: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to bake sections of the construction history of a shape node
    when possible. A typical usage would be on a shape that has both modelling operations
    and deformers in its history. Using this command with the -prePostDeformers flag will
    bake the modeling portions of the graph, so that only the deformers remain.
    
    Note that not all modeling operations can be baked such that they create exactly the
    same effect after baking. For example, imagine the history contains a skinning operation
    followed by a smooth. Before baking, the smooth operation is performed each time
    the skin deforms, so it will smooth differently depending on the output of the skin.
    When the smooth operation is baked into the skinning, the skin will be reweighted
    based on the smooth points to attempt to approximate the original behavior. However,
    the skin node does not perform the smooth operation, it merely performs skinning with
    the newly calculated weights and the result will not be identical to before the bake.
    
    In general, modeling operations that occur before deformers can be baked precisely.
    Those which occur after can only be approximated. The -pre and -post flags allow you
    to control whether only the operations before or after the deformers are baked.
    
    When the command is used on an object with no deformers, the entire history
    will be deleted.

    Args:
        allShapes | all: (create, query) - Specifies that the bake operation should be performed on all shapes in the entire scene. By default, only selected objects are baked. If this option is specified and there are no shapes in the scene, then this command will do nothing and end successfully.
        postSmooth | nps: (create, query) - Specifies whether or not a smoothing operation should be done on skin vertices. This smoothing is only done on vertices that are found to deviate largely from other vertex values.  The default is false.
        preCache | pc: (create, query) - Specifies baking of any history operations that occur before the caching operation, including deformers. In query mode, returns a list of the nodes that will be baked.
        preDeformers | pre: (create, query) - Specifies baking of any modeling operations in the history that occur before the deformers. In query mode, returns a list of the nodes that will be baked.
        prePostDeformers | ppt: (create, query) - Specifies baking of all modeling operations in the history whether they are before or after the deformers in the history. If neither the -prePostDeformers nor the -preDeformers flag is specified, prePostDeformers will be used as the default. In query mode, returns a list of the nodes that will be baked.
    """
    ...


def baseTemplate(*args, exists: bool = ..., ex: bool = ..., fileName: Optional[Union[str, bool]] = ..., fn: Optional[Union[str, bool]] = ..., force: bool = ..., f: bool = ..., load: bool = ..., l: bool = ..., matchFile: Optional[Union[str, bool]] = ..., mf: Optional[Union[str, bool]] = ..., silent: bool = ..., si: bool = ..., unload: bool = ..., u: bool = ..., viewList: Optional[Union[str, bool]] = ..., vl: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This is the class for the commands that edit and/or query templates.

    Args:
        exists | ex: (query) - Returns true or false depending upon whether the specified template exists. When used with the matchFile argument, the query will return true if the template exists and the filename it was loaded from matches the filename given.
        fileName | fn: (create, query) - Specifies the filename associated with the template.  This argument can be used in conjunction with load, save or query modes. If no filename is associated with a template, a default file name based on the template name will be used.  It is recommended but not required that the filename and template name correspond.
        force | f: (create) - This flag is used with some actions to allow them to proceed with an overwrite or destructive operation. When used with load, it will allow an existing template to be reloaded from a file.  When used in create mode, it will allow an existing template to be recreated (for example when using fromContainer argument to regenerate a template).
        load | l: () - Load an existing template from a file. If a filename is specified for the template, the entire file (and all templates in it) will be loaded. If no file is specified, a default filename will be assumed, based on the template name.
        matchFile | mf: (query) - Used in query mode in conjunction with other flags this flag specifies an optional file name that is to be matched as part of the query operation. 			In query mode, this flag needs a value.
        silent | si: (create, edit, query) - Silent mode will suppress any error or warning messages that would normally be reported from the command execution.  The return values are unaffected.
        unload | u: (create) - Unload the specified template.  This action will not delete the associated template file if one exists, it merely removes the template definition from the current session.
        viewList | vl: (create, query) - Used in query mode, returns a list of all views defined on the template.
    """
    ...


def baseView(*args, itemInfo: Optional[Union[str, bool]] = ..., ii: Optional[Union[str, bool]] = ..., itemList: bool = ..., il: bool = ..., viewDescription: bool = ..., vd: bool = ..., viewLabel: bool = ..., vb: bool = ..., viewList: bool = ..., vl: bool = ..., viewName: Optional[Union[str, bool]] = ..., vn: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    A view defines the layout information for the attributes of a
    particular node type or container.  Views can be selected from a set of
    built-in views or may be defined on an associated container template.
    This command queries the view-related information for a container node or
    for a given template.  The information returned from this command will be
    based on the view-related settings in force on the container node at the time
    of the query (i.e. the container's view mode, template name, view name
    attributes), when applicable.

    Args:
        itemInfo | ii: (query) - Used in query mode in conjunction with the itemList flag. The command will return a list of information for each item in the view, the information fields returned for each item are determined by this argument value. The information fields will be listed in the string array returned. The order in which the keyword is specified will determine the order in which the data will be returned by the command. One or more of the following keywords, separated by colons ':' are used to specify the argument value.  itemIndex  : sequential item number (0-based) itemName   : item name (string) itemLabel  : item display label (string) itemDescription : item description field (string) itemLevel  : item hierarchy level (0-n) itemIsGroup : (boolean 0 or 1) indicates whether or not this item is a group itemIsAttribute : (boolean 0 or 1) indicates whether or not this item is an attribute itemNumChildren: number of immediate children (groups or attributes) of this item itemAttrType : item attribute type (string) itemCallback : item callback field (string)  In query mode, this flag needs a value.
        itemList | il: (query) - Used in query mode, the command will return a list of information for each item in the view.  The viewName flag is used to select the view to query. The information returned about each item is determined by the itemInfo argument value. For efficiency, it is best to query all necessary item information at one time (to avoid recomputing the view information on each call).
        viewDescription | vd: (query) - Used in query mode, returns the description field associated with the selected view. If no description was defined for this view, the value will be empty.
        viewLabel | vb: (query) - Used in query mode, returns the display label associated with the view. An appropriate label suitable for the user interface will be returned based on the selected view.  Use of the view label is usually more suitable than the view name for display purposes.
        viewList | vl: (query) - Used in query mode, command will return a list of all views defined for the given target (container or template).
        viewName | vn: (query) - Used in query mode, specifies the name of the queried view when used in conjunction with a template target. When used in conjunction with a container target, it requires no string argument, and returns the name of the currently active view associated with the container; this value may be empty if the current view is not a valid template view or is generated by one of the built-in views modes. For this reason, the view label is generally more suitable for display purposes. 			In query mode, this flag can accept a value.
    """
    ...


def boxDollyCtx(*args, alternateContext: bool = ..., ac: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., toolName: Optional[Union[str, bool]] = ..., tn: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create, edit, or query a dolly
    context.

    Args:
        alternateContext | ac: (create, query) - Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        toolName | tn: (create, query) - Name of the specific tool to which this command refers.
    """
    ...


def boxZoomCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., zoomScale: Optional[Union[float, bool]] = ..., zs: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create, edit, or query a box zoom
    context. If this context is used on a perspective camera, the
    field of view and view direction are changed. If the camera is
    orthographic, the orthographic width and eye point are
    changed. The left and middle mouse interactively zoom the
    view. The control key can be used to enable box zoom. A box
    starting from left to right will zoom in, and a box starting from
    right to left will zoom out.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        zoomScale | zs: (create, edit, query) - Scale the zoom.
    """
    ...


def clipEditorCurrentTimeCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context which may be used to change current time
    within the track area of a clip editor.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def color(*args, rgbColor: Optional[Union[Tuple[float, float, float], bool]] = ..., rgb: Optional[Union[Tuple[float, float, float], bool]] = ..., userDefined: Optional[Union[int, bool]] = ..., ud: Optional[Union[int, bool]] = ...) -> Any:
    r"""
    This command sets the dormant wireframe color of the specified
    objects to be their class color or if the -ud/userDefined flag is
    specified, one of the user defined colors. The -rgb/rgbColor flags
    can be specified if the user requires floating point RGB colors.

    Args:
        rgbColor | rgb: (create) - Specifies and rgb color to set the selected object to.
        userDefined | ud: (create) - Specifies the user defined color index to set selected object to. The valid range of numbers is [1-8].
    """
    ...


def colorIndex(*args, active: bool = ..., atv: bool = ..., dormant: bool = ..., dor: bool = ..., hueSaturationValue: bool = ..., hsv: bool = ..., resetToFactory: bool = ..., rf: bool = ..., resetToSaved: bool = ..., rs: bool = ..., userColor: bool = ..., uc: bool = ..., query: bool = ...) -> Any:
    r"""
    The index specifies a color index in the color palette.
    The r, g, and b values (between 0-1) specify the RGB values
    (or the HSV values if the -hsv flag is used) for the color.

    Args:
        active | atv: (create) - Combined with query mode, with given index, query the active color palette.
        dormant | dor: (create) - Combined with query mode, with given index, query the dormant color palette.
        hueSaturationValue | hsv: (create, query) - Indicates that rgb values are really hsv values. Upon query, returns the HSV valuses as an array of 3 floats.
        resetToFactory | rf: (create) - Resets all color index palette entries to their factory defaults.
        resetToSaved | rs: (create) - Resets all color palette entries to their saved values.
        userColor | uc: (create) - Combined with query mode, with given index, query the user color palette.
    """
    ...


def colorManagementCatalog(*args, addTransform: Optional[Union[str, bool]] = ..., adt: Optional[Union[str, bool]] = ..., editUserTransformPath: Optional[Union[str, bool]] = ..., eut: Optional[Union[str, bool]] = ..., listSupportedExtensions: bool = ..., lse: bool = ..., listTransformConnections: bool = ..., ltc: bool = ..., path: Optional[Union[str, bool]] = ..., pth: Optional[Union[str, bool]] = ..., queryUserTransformPath: bool = ..., qut: bool = ..., removeTransform: Optional[Union[str, bool]] = ..., rmt: Optional[Union[str, bool]] = ..., transformConnection: Optional[Union[str, bool]] = ..., tcn: Optional[Union[str, bool]] = ..., type: Optional[Union[str, bool]] = ..., typ: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This non-undoable action performs additions and removals of custom color
    transforms from the Autodesk native color transform catalog.  Once a custom
    color transform has been added to the catalog, it can be used in the same way
    as the builtin Autodesk native color transforms.

    Args:
        addTransform | adt: (create) - Add transform to collection.
        editUserTransformPath | eut: (create) - Edit the user transform directory. By changing the directory, all custom transforms currently added could be changed, and new ones could appear.
        listSupportedExtensions | lse: (create) - List the file extensions that are supported by add transform.  This list is valid for all transform types, and therefore this flag does not require use of the type flag.
        listTransformConnections | ltc: (create) - List the transforms that can be used as source (for "view" and "output" types) or destination (for "input" and "rendering space" types) to connect a custom transform to the rest of the transform collection.
        path | pth: (create) - In addTransform mode, the path to the transform data file.
        queryUserTransformPath | qut: (create) - Query the user transform directory.
        removeTransform | rmt: (create) - Remove transform from collection.
        transformConnection | tcn: (create) - In addTransform mode, an existing transform to which the added transform will be connected. For an input transform or rendering space transform, this will be a destination. For a view or output transform, this will be a source.
        type | typ: (create) - The type of transform added, removed, or whose transform connections are to be listed. Must be one of "view", "rendering space", "input", or "output".
    """
    ...


def colorManagementConvert(*args, toDisplaySpace: Optional[Union[Tuple[float, float, float], bool]] = ..., tds: Optional[Union[Tuple[float, float, float], bool]] = ...) -> Any:
    r"""
    This command can be used to convert rendering (a.k.a. working) space color values to display space
    color values. This is useful if you create custom UI with colors painted to screen, where you need
    to handle color management yourself. The current view transform set in the Color Management user
    preferences will be used.

    Args:
        toDisplaySpace | tds: (create) - Converts the given RGB value to display space.
    """
    ...


def colorManagementFileRules(*args, addRule: Optional[Union[str, bool]] = ..., add: Optional[Union[str, bool]] = ..., colorSpace: Optional[Union[str, bool]] = ..., cs: Optional[Union[str, bool]] = ..., colorSpaceDescription: Optional[Union[str, bool]] = ..., csd: Optional[Union[str, bool]] = ..., colorSpaceFamilies: Optional[Union[str, bool]] = ..., csf: Optional[Union[str, bool]] = ..., colorSpaceNames: bool = ..., csn: bool = ..., down: Optional[Union[str, bool]] = ..., dwn: Optional[Union[str, bool]] = ..., enabled: bool = ..., ena: bool = ..., evaluate: Optional[Union[str, bool]] = ..., ev: Optional[Union[str, bool]] = ..., extension: Optional[Union[str, bool]] = ..., ext: Optional[Union[str, bool]] = ..., listRules: bool = ..., lsr: bool = ..., load: bool = ..., ld: bool = ..., moveUp: Optional[Union[str, bool]] = ..., up: Optional[Union[str, bool]] = ..., pattern: Optional[Union[str, bool]] = ..., pat: Optional[Union[str, bool]] = ..., remove: Optional[Union[str, bool]] = ..., rm: Optional[Union[str, bool]] = ..., restoreDefaults: bool = ..., rde: bool = ..., save: bool = ..., sav: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This non-undoable action manages the list of rules that Maya uses to assign
    an initial input color space to dependency graph nodes that read in color
    information from a file.  Rules are structured in a chain of
    responsibility, from highest priority rule to lowest priority rule, each
    rule matching a file path pattern and extension.  If a rule matches a given
    file path, its color space is returned as the result of rules evaluation,
    and no further rule is considered.  The lowest priority rule will always
    return a match.
    Rules can be added, removed, and changed in priority in the list.  Each
    rule can have its file path pattern, extension, and color space changed.
    The rule list can be saved to user preferences, and loaded from user
    preferences.

    Args:
        addRule | add: (create) - Add a rule with the argument name to the list of rules, as the highest-priority rule.  If this flag is used, the pattern, extension, and colorSpace flags must be used as well, to specify the file rule pattern, extension, and color space, respectively.
        colorSpace | cs: (create, edit, query) - The input color space for the rule.  If the rule matches a file path, this is the color space that is returned.  This color space must match an existing color space in the input color space list.
        colorSpaceDescription | csd: (query) - Returns the description for a specific color space. 			In query mode, this flag needs a value.
        colorSpaceFamilies | csf: (query) - Returns the list of families for a specific color space. Used to add submenus when populating the color spaces UI popup of a rule. 			In query mode, this flag needs a value.
        colorSpaceNames | csn: (query) - Returns the list of available color spaces. Used to populate the color spaces UI popup of a rule.
        down | dwn: (create) - Move the rule with the argument name down one position towards lower priority.
        enabled | ena: (query) - Are the file rules enabled?
        evaluate | ev: (create) - Evaluates the list of rules and returns the input color space name that corresponds to the argument file path.
        extension | ext: (create, edit, query) - The file extension for the rule is case insensitive
        listRules | lsr: (create) - Returns an array of rule name strings, in order, from lowest-priority (rule 0) to highest-priority (last rule in array).
        load | ld: (create) - Read the rules from Maya preferences.  Any existing rules are cleared.
        moveUp | up: (create) - Move the rule with the argument name up one position towards higher priority.
        pattern | pat: (create, edit, query) - The file path pattern for the rule.  This is the substring to match in the file path, expressed as a glob pattern: for example, '*' matches all files. For more information about glob pattern syntax, see http://en.wikipedia.org/wiki/Glob_%28programming%29.
        remove | rm: (create) - Remove the rule with the argument name from the list of rules.
        restoreDefaults | rde: (create) - Restore the list of rules to the default ones only.
        save | sav: (create) - Save the rules to Maya preferences.
    """
    ...


def colorManagementPrefs(*args, cmConfigFileEnabled: bool = ..., cfe: bool = ..., cmEnabled: bool = ..., cme: bool = ..., colorManageAllNodes: bool = ..., cma: bool = ..., colorManagePots: bool = ..., cmp: bool = ..., colorManagedNodes: bool = ..., cmn: bool = ..., colorManagementSDKVersion: Optional[Union[str, bool]] = ..., cmv: Optional[Union[str, bool]] = ..., configFilePath: Optional[Union[str, bool]] = ..., cfp: Optional[Union[str, bool]] = ..., configFileVersion: Optional[Union[str, bool]] = ..., cfv: Optional[Union[str, bool]] = ..., defaultInputSpaceName: Optional[Union[str, bool]] = ..., din: Optional[Union[str, bool]] = ..., displayName: Optional[Union[str, bool]] = ..., dn: Optional[Union[str, bool]] = ..., displayNames: bool = ..., dns: bool = ..., equalsToPolicyFile: Optional[Union[str, bool]] = ..., etp: Optional[Union[str, bool]] = ..., exportPolicy: Optional[Union[str, bool]] = ..., epy: Optional[Union[str, bool]] = ..., inhibitEvents: bool = ..., ie: bool = ..., inputSpaceDescription: Optional[Union[str, bool]] = ..., isd: Optional[Union[str, bool]] = ..., inputSpaceFamilies: Optional[Union[str, bool]] = ..., isf: Optional[Union[str, bool]] = ..., inputSpaceNames: bool = ..., iss: bool = ..., loadPolicy: Optional[Union[str, bool]] = ..., lpy: Optional[Union[str, bool]] = ..., loadedDefaultInputSpaceName: Optional[Union[str, bool]] = ..., ldn: Optional[Union[str, bool]] = ..., loadedDisplayName: Optional[Union[str, bool]] = ..., ld: Optional[Union[str, bool]] = ..., loadedOutputTransformName: Optional[Union[str, bool]] = ..., lon: Optional[Union[str, bool]] = ..., loadedRenderingSpaceName: Optional[Union[str, bool]] = ..., lrn: Optional[Union[str, bool]] = ..., loadedViewName: Optional[Union[str, bool]] = ..., lv: Optional[Union[str, bool]] = ..., loadedViewTransformName: Optional[Union[str, bool]] = ..., lvn: Optional[Union[str, bool]] = ..., missingColorSpaceNodes: bool = ..., mcn: bool = ..., ocioRulesEnabled: bool = ..., ore: bool = ..., ociov2Enabled: bool = ..., oci: bool = ..., outputTarget: Optional[Union[str, bool]] = ..., ott: Optional[Union[str, bool]] = ..., outputTransformEnabled: bool = ..., ote: bool = ..., outputTransformName: Optional[Union[str, bool]] = ..., otn: Optional[Union[str, bool]] = ..., outputTransformNames: bool = ..., ots: bool = ..., outputTransformUseColorConversion: bool = ..., otc: bool = ..., outputUseViewTransform: bool = ..., ovt: bool = ..., policyFileName: Optional[Union[str, bool]] = ..., pfn: Optional[Union[str, bool]] = ..., popupOnError: bool = ..., poe: bool = ..., refresh: bool = ..., rfr: bool = ..., renderingSpaceName: Optional[Union[str, bool]] = ..., rsn: Optional[Union[str, bool]] = ..., renderingSpaceNames: bool = ..., rss: bool = ..., restoreDefaults: bool = ..., rde: bool = ..., viewDisplayNames: Optional[Union[str, bool]] = ..., vds: Optional[Union[str, bool]] = ..., viewName: Optional[Union[str, bool]] = ..., vn: Optional[Union[str, bool]] = ..., viewNames: bool = ..., vns: bool = ..., viewTransformName: Optional[Union[str, bool]] = ..., vtn: Optional[Union[str, bool]] = ..., viewTransformNames: bool = ..., vts: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command allows querying and editing the color management global data in a
    scene.  It also allows for setting the view transform and rendering space which
    automatically configures the color processing in the enabled views.

    Args:
        cmConfigFileEnabled | cfe: (edit, query) - Turn on or off applying an OCIO configuration file.  If set, the color management configuration set in the preferences is used.
        cmEnabled | cme: (edit, query) - Turn on or off color management in general.  If set, the color management configuration set in the preferences is used.
        colorManageAllNodes | cma: (create) - Adds color management to all input nodes such as file texture nodes
        colorManagePots | cmp: (edit, query) - Turn on or off color management of color pots in the UI.  If set, colors in color pots are taken to be in rendering space, and are displayed after being transformed by the view transform set in the preferences.
        colorManagedNodes | cmn: (query) - Gets the names of all nodes that apply color management to bring pixels from an input color space to the rendering space. Examples include file texture node.
        colorManagementSDKVersion | cmv: (query) - Obtain the version of the color management SDK used by Maya.
        configFilePath | cfp: (edit, query) - The configuration file to be used, if color management is enabled.
        configFileVersion | cfv: (query) - Obtain the version of the config version.
        defaultInputSpaceName | din: (edit, query) - This flag is obsolete.  See the colorManagementFileRules command for more information.
        displayName | dn: (edit, query) - The display from the (display, view) pair, to be applied by color managed viewers and color managed UI controls.
        displayNames | dns: (query) - Returns the list of available displays.  Used to populate the color management preference UI popup.
        equalsToPolicyFile | etp: (query) - Query if the current loaded policy settings is the same with the settings described in the policy file which is the argument of the command. 			In query mode, this flag needs a value.
        exportPolicy | epy: (create) - Export the color management parameters to policy file
        inhibitEvents | ie: (create) - Inhibit client-server notifications and event triggers which occur when changing the color management settings.
        inputSpaceDescription | isd: (query) - Returns the description for a specific input color space. 			In query mode, this flag needs a value.
        inputSpaceFamilies | isf: (query) - Returns the list of families for a specific input color space. Used to add submenus when populating the input color spaces UI popup. 			In query mode, this flag needs a value.
        inputSpaceNames | iss: (query) - Returns the list of available input color spaces. Used to populate the input color spaces UI popup.
        loadPolicy | lpy: (create) - Load the color management policy file. This file overides the color management settings.
        loadedDefaultInputSpaceName | ldn: (query) - This flag is obsolete.
        loadedDisplayName | ld: (query) - Gets the loaded display from the (display, view) pair.  Used by file open, import, and reference to check for missing color spaces or transforms.
        loadedOutputTransformName | lon: (query) - Gets the loaded output transform.  Used by file open, import, and reference to check for missing color spaces or transforms.
        loadedRenderingSpaceName | lrn: (query) - Gets the loaded rendering space.  Used by file open, import, and reference to check for missing color spaces or transforms.
        loadedViewName | lv: (query) - Gets the loaded view from the (display, view) pair.  Used by file open, import, and reference to check for missing color spaces or transforms.
        loadedViewTransformName | lvn: (query) - Gets the loaded view transform.  Used by file open, import, and reference to check for missing color spaces or transforms.
        missingColorSpaceNodes | mcn: (query) - Gets the names of the nodes that have color spaces not defined in the selected transform collection or in the selected config file. Note that an inactive color space is not a missing color space.
        ocioRulesEnabled | ore: (edit, query) - Turn on or off the use of colorspace assignment rules from the OCIO library.
        ociov2Enabled | oci: (query) - Is OCIOv2 the colour management system by default.
        outputTarget | ott: (edit, query) - Indicates to which output the outputTransformEnabled or the outputTransformName flags are to be applied. Valid values are "renderer" or "playblast". 			In query mode, this flag needs a value.
        outputTransformEnabled | ote: (edit, query) - Turn on or off applying the output transform for out of viewport renders. If set, the output transform set in the preferences is used.
        outputTransformName | otn: (edit, query) - The output transform to be applied for out of viewport renders.  Disables output use view transform mode.
        outputTransformNames | ots: (query) - Returns the list of available output transforms.
        outputTransformUseColorConversion | otc: (edit, query) - Turn on or off selecting the color space conversion for the output color space of viewport renders.  If set, a conversion color space is used; otherwise, a view transform is used.
        outputUseViewTransform | ovt: (edit, query) - Turns use view transform mode on.  In this mode, the output transform is set to match the view transform.  To turn the mode off, set an output transform using the outputTransformName flag.
        policyFileName | pfn: (edit, query) - Set the policy file name
        popupOnError | poe: (edit) - Turn on or off displaying a modal popup on error (as well as the normal script editor reporting of the error), for this invocation of the command.  Default is off.
        refresh | rfr: (create) - Refresh the color management.
        renderingSpaceName | rsn: (edit, query) - The color space to be used during rendering.  This is the source color space to the viewing transform, for color managed viewers and color managed UI controls, and the destination color space for color managed input pixels.
        renderingSpaceNames | rss: (query) - Returns the list of available rendering spaces.  Used to populate the color management preference UI popup.
        restoreDefaults | rde: (create) - Restore the color management settings to their default value.
        viewDisplayNames | vds: (query) - Returns the list of available views for a specific display. Used to populate the view name list UI for file and image plane nodes. 			In query mode, this flag needs a value.
        viewName | vn: (edit, query) - The view from the (display, view) pair, to be applied by color managed viewers and color managed UI controls.
        viewNames | vns: (query) - Returns the list of available views from the selected display.  Used to populate the color management preference UI popup.
        viewTransformName | vtn: (edit, query) - The view transform to be applied by color managed viewers and color managed UI controls.
        viewTransformNames | vts: (query) - Returns the list of available view transforms.  Used to populate the color management preference UI popup.
    """
    ...


def commandLogging(*args, historySize: Optional[Union[int, bool]] = ..., hs: Optional[Union[int, bool]] = ..., logCommands: bool = ..., lc: bool = ..., logFile: Optional[Union[str, bool]] = ..., lf: Optional[Union[str, bool]] = ..., recordCommands: bool = ..., rc: bool = ..., resetLogFile: bool = ..., rl: bool = ..., query: bool = ...) -> Any:
    r"""
    This command controls logging of Maya commands,
    in memory and on disk.
    
    Note that if commands are logged in memory, they will
    be available to the crash reporter and appear in crash logs.

    Args:
        historySize | hs: (create, query) - Sets the number of entries in the in-memory command history.
        logCommands | lc: (create, query) - Enables or disables the on-disk logging of commands.
        logFile | lf: (create, query) - Sets the filename to use for the on-disk log. If logging is active, the current file will be closed before the new one is opened.
        recordCommands | rc: (create, query) - Enables or disables the in-memory logging of commands.
        resetLogFile | rl: (create, query) - Reset the log filename to the default ('mayaCommandLog.txt' in the application folder, alongside 'Maya.env' and the default projects folder).
    """
    ...


def commandPort(*args, bufferSize: Optional[Union[int, bool]] = ..., bs: Optional[Union[int, bool]] = ..., close: bool = ..., cl: bool = ..., echoOutput: bool = ..., eo: bool = ..., listPorts: bool = ..., lp: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., noreturn: bool = ..., nr: bool = ..., pickleOutput: bool = ..., po: bool = ..., prefix: Optional[Union[str, bool]] = ..., pre: Optional[Union[str, bool]] = ..., returnNumCommands: bool = ..., rnc: bool = ..., securityWarning: bool = ..., sw: bool = ..., sourceType: Optional[Union[str, bool]] = ..., stp: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    Opens or closes the Maya command port. The command port comprises a socket
    to which a client program may connect. An example command port client
    "mcp" is included in the Motion Capture developers kit.
    
    It supports multi-byte commands and uses utf-8 as its transform
    format. It will receive utf8 command string and decode it to Maya native
    coding. The result will also be encoded to utf-8 before sending back.
    
    Care should be taken regarding INET domain sockets as no user
    identification, or authorization is required to connect to a given
    socket, and all commands (including "system(...)") are allowed and
    executed with the user id and permissions of the Maya user. The prefix
    flag can be used to reduce this security risk, as only the prefix
    command is executed.
    
    The query flag can be used to determine if a given command port exists.
    See examples below.

    Args:
        bufferSize | bs: (create) - Commands and results are each subject to size limits. This option allows the user to specify the size of the buffer used to communicate with Maya. If unspecified the default buffer size is 4096 characters. Commands longer than bufferSize characters will cause the client connection to close. Results longer that bufferSize characters are replaced with an error message.
        close | cl: (create) - Closes the commandPort, deletes the pipes
        echoOutput | eo: (create) - Sends a copy of all command output to the command port. Typically only the result is transmitted. This option provides a copy of all output.
        listPorts | lp: (create) - Returns the available ports
        name | n: (create) - Specifies the name of the command port which this command creates. CommandPort names of the form name create a UNIX domain socket on the localhost corresponding to name. If name does not begin with "/", then /tmp/name is used. If name begins with "/", name denotes the full path to the socket.  Names of the form :port number create an INET domain on the local host at the given port.
        noreturn | nr: (create) - Do not write the results from executed commands back to the command port socket. Instead, the results from executed commands are written to the script editor window. As no information passes back to the command port client regarding the execution of the submitted commands, care must be taken not to overflow the command buffer, which would cause the connection to close.
        pickleOutput | po: (create) - Python output will be pickled.
        prefix | pre: (create) - The string argument is the name of a Maya command taking one string argument. This command is called each time data is sent to the command port. The data written to the command port is passed as the argument to the prefix command. The data from the command port is encoded as with enocodeString and enclosed in quotes.  If newline characters are embedded in the command port data, the input is split into individual lines. These lines are treated as if they were separate writes to the command port. Only the result to the last prefix command is returned.
        returnNumCommands | rnc: (create) - Ignore the result of the command, but return the number of commands that have been read and executed in this call. This is a simple way to track buffer overflow. This flag is ignored when the noreturn flag is specified.
        securityWarning | sw: (create) - Enables security warning on command port input.
        sourceType | stp: (create) - The string argument is used to indicate which source type would be passed to the commandPort, like "mel", "python". The default source type is "mel".
    """
    ...


def connectAttr(*args, force: bool = ..., f: bool = ..., lock: bool = ..., l: bool = ..., nextAvailable: bool = ..., na: bool = ..., referenceDest: Optional[Union[str, bool]] = ..., rd: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Connect the attributes of two dependency nodes and return the
    names of the two connected attributes. The connected
    attributes must be be of compatible types. First argument is the
    source attribute, second one is the destination.
    
    Refer to dependency node documentation.

    Args:
        force | f: (create) - Forces the connection.  If the destination is already connected, the old connection is broken and the new one made.
        lock | l: (create) - If the argument is true, the destination attribute is locked after making the connection. If the argument is false, the connection is unlocked before making the connection.
        nextAvailable | na: (create) - If the destination multi-attribute has set the indexMatters to be false with this flag specified, a connection is made to the next available index. No index need be specified.
        referenceDest | rd: (create) - This flag is used for file io only. The flag indicates that the connection replaces a connection made in a referenced file, and the flag argument indicates the original destination from the referenced file. This flag is used so that if the reference file is modified, maya can still attempt to make the appropriate connections in the main scene to the referenced object.
    """
    ...


def connectionInfo(*args, destinationFromSource: bool = ..., dfs: bool = ..., getExactDestination: bool = ..., ged: bool = ..., getExactSource: bool = ..., ges: bool = ..., getLockedAncestor: bool = ..., gla: bool = ..., isDestination: bool = ..., id: bool = ..., isExactDestination: bool = ..., ied: bool = ..., isExactSource: bool = ..., ies: bool = ..., isLocked: bool = ..., il: bool = ..., isSource: bool = ..., sourceFromDestination: bool = ..., sfd: bool = ...) -> Any:
    r"""
    The connectionInfo command is used to get information about
    connection sources and destinations.  Unlike the isConnected command,
    this command needs only one end of the connection.

    Args:
        destinationFromSource | dfs: (create) - If the specified plug (or its ancestor) is a source, this flag returns the list of destinations connected from the source. (array of strings, empty array if none)
        getExactDestination | ged: (create) - If the plug or its ancestor is connection destination, this returns the name of the plug that is the exact destination. (empty string if there is no such connection).
        getExactSource | ges: (create) - If the plug or its ancestor is a connection source, this returns the name of the plug that is the exact source. (empty string if there is no such connection).
        getLockedAncestor | gla: (create) - If the specified plug is locked, its name is returned.  If an ancestor of the plug is locked, its name is returned.  If more than one ancestor is locked, only the name of the closest one is returned.  If neither this plug nor any ancestors are locked, an empty string is returned.
        isDestination | id: (create) - Returns true if the plug (or its ancestor) is the destination of a connection, false otherwise.
        isExactDestination | ied: (create) - Returns true if the plug is the exact destination of a connection, false otherwise.
        isExactSource | ies: (create) - Returns true if the plug is the exact source of a connection, false otherwise.
        isLocked | il: (create) - Returns true if this plug (or its ancestor) is locked
        isSource | isSource: (create) - Returns true if the plug (or its ancestor) is the source of a connection, false otherwise.
        sourceFromDestination | sfd: (create) - If the specified plug (or its ancestor) is a destination, this flag returns the source of the connection. (string, empty if none)
    """
    ...


def container(*args, addNode: Optional[Union[List[str], bool]] = ..., an: Optional[Union[List[str], bool]] = ..., asset: Optional[Union[List[str], bool]] = ..., a: Optional[Union[List[str], bool]] = ..., assetMember: Optional[Union[str, bool]] = ..., am: Optional[Union[str, bool]] = ..., bindAttr: Optional[Union[Tuple[str, str], bool]] = ..., ba: Optional[Union[Tuple[str, str], bool]] = ..., connectionList: bool = ..., cl: bool = ..., current: bool = ..., c: bool = ..., fileName: Optional[Union[List[str], bool]] = ..., fn: Optional[Union[List[str], bool]] = ..., findContainer: Optional[Union[List[str], bool]] = ..., fc: Optional[Union[List[str], bool]] = ..., force: bool = ..., f: bool = ..., includeHierarchyAbove: bool = ..., iha: bool = ..., includeHierarchyBelow: bool = ..., ihb: bool = ..., includeNetwork: bool = ..., inc: bool = ..., includeNetworkDetails: Optional[Union[str, bool]] = ..., ind: Optional[Union[str, bool]] = ..., includeShaders: bool = ..., isd: bool = ..., includeShapes: bool = ..., ish: bool = ..., includeTransform: bool = ..., it: bool = ..., isContainer: bool = ..., isc: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., nodeList: bool = ..., nl: bool = ..., nodeNamePrefix: bool = ..., nnp: bool = ..., parentContainer: bool = ..., par: bool = ..., preview: bool = ..., p: bool = ..., publishAndBind: Tuple[str, str] = ..., pb: Tuple[str, str] = ..., publishAsChild: Optional[Union[Tuple[str, str], bool]] = ..., pac: Optional[Union[Tuple[str, str], bool]] = ..., publishAsParent: Optional[Union[Tuple[str, str], bool]] = ..., pap: Optional[Union[Tuple[str, str], bool]] = ..., publishAsRoot: Optional[Union[Tuple[str, bool], bool]] = ..., pro: Optional[Union[Tuple[str, bool], bool]] = ..., publishAttr: Optional[Union[str, bool]] = ..., pa: Optional[Union[str, bool]] = ..., publishConnections: bool = ..., pc: bool = ..., publishName: Optional[Union[str, bool]] = ..., pn: Optional[Union[str, bool]] = ..., removeContainer: bool = ..., rc: bool = ..., removeNode: List[str] = ..., rn: List[str] = ..., type: Optional[Union[str, bool]] = ..., typ: Optional[Union[str, bool]] = ..., unbindAndUnpublish: str = ..., ubp: str = ..., unbindAttr: Optional[Union[Tuple[str, str], bool]] = ..., ua: Optional[Union[Tuple[str, str], bool]] = ..., unbindChild: str = ..., unc: str = ..., unbindParent: str = ..., unp: str = ..., unpublishChild: str = ..., upc: str = ..., unpublishName: str = ..., un: str = ..., unpublishParent: str = ..., upp: str = ..., unsortedOrder: bool = ..., uso: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create and query container
    nodes. It is also used to perform operations on containers such as:
    
     add and remove nodes from the container
     publish attributes from nodes inside the container
     replace the connections and values from one container onto another one
     remove a container without removing its member nodes

    Args:
        addNode | an: (create, edit) - Specifies the list of nodes to add to container.
        asset | a: (query) - When queried, if all the nodes in nodeList belong to the same container, returns container's name. Otherwise returns empty string. This flag is functionally equivalent to the findContainer flag.
        assetMember | am: (query) - Can be used during query in conjunction with the bindAttr flag to query for the only published attributes related to the specified node within the container.       In query mode, this flag needs a value.
        bindAttr | ba: (edit, query) - Bind a contained attribute to an unbound published name on the interface of the container; returns a list of bound published names. The first string specifies the node and attribute name to be bound in "node.attr" format. The second string specifies the name of the unbound published name. In query mode, returns a string array of the published names and their corresponding attributes. The flag can also be used in query mode in conjunction with the -publishName, -publishAsParent, and -publishAsChild flags.
        connectionList | cl: (query) - Returns a list of the exterior connections to the container node.
        current | c: (create, edit, query) - In create mode, specify that the newly created asset should be current. In edit mode, set the selected asset as current. In query, return the current asset.
        fileName | fn: (query) - Used to query for the assets associated with a given file name.       In query mode, this flag needs a value.
        findContainer | fc: (query) - When queried, if all the nodes in nodeList belong to the same container, returns container's name. Otherwise returns empty string.       In query mode, this flag needs a value.
        force | f: (create, edit) - This flag can be used in conjunction with -addNode and -removeNode flags only. If specified with -addNode, nodes will be disconnected from their current containers before they are added to new one. If specified with -removeNode, nodes will be removed from all containers, instead of remaining in the parent container if being removed from a nested container.
        includeHierarchyAbove | iha: (create, edit) - Used to specify that the parent hierarchy of the supplied node list should also be included in the container (or deleted from the container). Hierarchy inclusion will stop at nodes which are members of other containers.
        includeHierarchyBelow | ihb: (create, edit) - Used to specify that the hierarchy below the supplied node list should also be included in the container (or delete from the container). Hierarchy inclusion will stop at nodes which are members of other containers.
        includeNetwork | inc: (create, edit) - Used to specify that the node network connected to supplied node list should also be included in the container. Network traversal will stop at default nodes and nodes which are members of other containers.
        includeNetworkDetails | ind: (create, edit, multiuse) - Used to specify specific parts of the network that should be included. Valid arguments to this flag are: "channels", "sdk", "constraints", "history" and "expressions", "inputs", "outputs". The difference between this flag and the includeNetwork flag, is that it will include all connected nodes regardless of their type. Note that dag containers include their children, so they will always include constraint nodes that are parented beneath the selected objects, even when constraints are not specified as an input.
        includeShaders | isd: (create, edit) - Used to specify that for any shapes included, their shaders will also be included in the container.
        includeShapes | ish: (create, edit) - Used to specify that for any transforms selected, their direct child shapes will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyBelow is used since the child shapes and all other descendents will automatically be included.
        includeTransform | it: (create, edit) - Used to specify that for any shapes selected, their parent transform will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyAbove is used since the parent transform and all of its parents will automatically be included.
        isContainer | isc: (query) - Return true if the selected or specified node is a container node. If multiple containers are queried, only the state of the first will be returned.
        name | n: (create) - Sets the name of the newly-created container.
        nodeList | nl: (query) - When queried, returns a list of nodes in container. The list will be sorted in the order they were added to the container. This will also display any reordering done with the reorderContainer command.
        nodeNamePrefix | nnp: (create, edit) - Specifies that the name of published attributes should be of the form "node_attr". Must be used with the -publishConnections/-pc flag.
        parentContainer | par: (query) - Flag to query the parent container of a specified container.
        preview | p: (create) - This flag is valid in create mode only. It indicates that you do not want the container to be created, instead you want to preview its contents. When this flag is used, Maya will select the nodes that would be put in the container if you did create the container. For example you can see what would go into the container with -includeNetwork, then modify your selection as desired, and do a create container with the selected objects only.
        publishAndBind | pb: (edit) - Publish the given name and bind the attribute to the given name. First string specifies the node and attribute name in "node.attr" format. Second string specifies the name it should be published with.
        publishAsChild | pac: (edit, query) - Publish contained node to the interface of the container to indicate it can be a child of external nodes. The second string is the name of the published node. In query mode, returns a string of the published names and the corresponding nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.
        publishAsParent | pap: (edit, query) - Publish contained node to the interface of the container to indicate it can be a parent to external nodes. The second string is the name of the published node. In query mode, returns a string of array of the published names and the corresponding nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.
        publishAsRoot | pro: (edit, query) - Publish or unpublish a node as a root. The significance of root transform node is twofold. When container-centric selection is enabled, the root transform will be selected if a container node in the hierarchy below it is selected in the main scene view. Also, when exporting a container proxy, any published root transformation attributes such as translate, rotate or scale will be hooked up to attributes on a stand-in node. In query mode, returns the node that has been published as root.
        publishAttr | pa: (query) - In query mode, can only be used with the -publishName(-pn) flag, and takes an attribute as an argument; returns the published name of the attribute, if any.       In query mode, this flag needs a value.
        publishConnections | pc: (create, edit) - Publish all connections from nodes inside the container to nodes outside the container.
        publishName | pn: (edit, query) - Publish a name to the interface of the container, and returns the actual name published to the interface.  In query mode, returns the published names for the container. If the -bindAttr flag is specified, returns only the names that are bound; if the -unbindAttr flag is specified, returns only the names that are not bound; if the -publishAsParent/-publishAsChild flags are specified, returns only names of published parents/children. if the -publishAttr is specified with an attribute argument in the "node.attr" format, returns the published name for that attribute, if any.
        removeContainer | rc: (edit) - Disconnects all the nodes from container and deletes container node.
        removeNode | rn: (edit) - Specifies the list of nodes to remove from container. If node is a member of a nested container, it will be added to the parent container. To remove from all containers completely, use the -force flag.
        type | typ: (create, query) - By default, a container node will be created. Alternatively, the type flag can be used to indicate that a different type of container should be created. At the present time, the only other valid type of container node is "dagContainer".
        unbindAndUnpublish | ubp: (edit) - Unbind the given attribute (in "node.attr" format) and unpublish its associated name. Unbinding a compound may trigger unbinds of its compound parents/children. So the advantage of using this one flag is that it will automatically unpublish the names associated with these automatic unbinds.
        unbindAttr | ua: (edit, query) - Unbind a published attribute from its published name on the interface of the container, leaving an unbound published name on the interface of the container; returns a list of unbound published names. The first string specifies the node and attribute name to be unbound in "node.attr" format, and the second string specifies the name of the bound published name. In query mode, can only be used with the -publishName, -publishAsParent and -publishAsChild flags.
        unbindChild | unc: (edit) - Unbind the node published as child, but do not remove its published name from the interface of the container.
        unbindParent | unp: (edit) - Unbind the node published as parent, but do not remove its published name from the interface of the container.
        unpublishChild | upc: (edit) - Unpublish node published as child from the interface of the container
        unpublishName | un: (edit) - Unpublish an unbound name from the interface of the container.
        unpublishParent | upp: (edit) - Unpublish node published as parent from the interface of the container
        unsortedOrder | uso: (query) - This flag has no effect on the operation of the container command (OBSOLETE).
    """
    ...


def containerBind(*args, allNames: bool = ..., all: bool = ..., bindingSet: Optional[Union[str, bool]] = ..., bs: Optional[Union[str, bool]] = ..., bindingSetConditions: bool = ..., bsc: bool = ..., bindingSetList: bool = ..., bsl: bool = ..., force: bool = ..., f: bool = ..., preview: bool = ..., p: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This is an accessory command to the container command which is used
    for some automated binding operations on the container. A container's
    published interface can be bound using a bindingSet on the
    associated container template.

    Args:
        allNames | all: (create) - Specifies that all published names on the container should be considered during the binding operation.  By default only unbound published names will be operated on.  Additionally specifying the 'force' option with 'all' will cause all previously bound published names to be reset (or unbound) before the binding operation is performed; in the event that there is no appropriate binding found for the published name, it will be left in the unbound state.
        bindingSet | bs: (query) - Specifies the name of the template binding set to use for the bind or query operation. This flag is not available in query mode. 			In query mode, this flag needs a value.
        bindingSetConditions | bsc: (query) - Used in query mode, returns a list of binding set condition entries from the specified template binding set.  The list returned is composed of of all published name / condition string pairs for each entry in the binding set. This flag returns all entries in the associated binding set and does not take into account the validity of each entry with respect to the container's list of published names, bound or unbound state, etc.
        bindingSetList | bsl: (edit, query) - Used in query mode, returns a list of available binding sets that are defined on the associated container template.
        force | f: (create) - This flag is used to force certain operations to proceed that would normally not be performed.
        preview | p: (create) - This flag will provide a preview of the results of a binding operation but will not actually perform it.  A list of publishedName/boundName pairs are returned for each published name that would be affected by the binding action. If the binding of a published name will not change as a result of the action it will not be listed. Published names that were bound but will become unbound are also listed, in this case the associated boundName will be indicated by an empty string.
    """
    ...


def containerProxy(*args, fromTemplate: Optional[Union[str, bool]] = ..., ft: Optional[Union[str, bool]] = ..., type: Optional[Union[str, bool]] = ..., typ: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Creates a new container with the same published interface, dynamic attributes
    and attribute values as the specified container but with fewer container
    members. This proxy container can be used as a reference proxy so that values
    can be set on container attributes without loading in the full container.
    The proxy container will contain one or more locator nodes. The first locator
    has dynamic attributes that serve as stand-ins for the original published
    attributes. The remaining locators serve as stand-ins for any dag nodes
    that have been published as parent or as child and will be placed at the
    world space location of the published parent/child nodes.
    The expected usage of container proxies is to serve as a reference proxy
    for a referenced container. For automated creation, export and setup
    of the proxy see the doExportContainerProxy.mel script which is
    invoked by the "Export Container Proxy" menu item.

    Args:
        fromTemplate | ft: (create) - Specifies the name of a template file which will be used to create the new container proxy. Stand-in attributes will be created and published for all the numeric attributes on the proxy.
        type | typ: (create) - Specifies the type of container node to use for the proxy. This flag is only valid in conjunction with the fromTemplate flag. When creating a proxy for an existing container, the type created will always be identical to that of the source container. The default value for this flag is 'container'.
    """
    ...


def containerPublish(*args, bindNode: Optional[Union[Tuple[str, str], bool]] = ..., bn: Optional[Union[Tuple[str, str], bool]] = ..., bindTemplateStandins: bool = ..., bts: bool = ..., inConnections: bool = ..., ic: bool = ..., mergeShared: bool = ..., ms: bool = ..., outConnections: bool = ..., oc: bool = ..., publishNode: Optional[Union[Tuple[str, str], bool]] = ..., pn: Optional[Union[Tuple[str, str], bool]] = ..., unbindNode: Optional[Union[str, bool]] = ..., ubn: Optional[Union[str, bool]] = ..., unpublishNode: Optional[Union[str, bool]] = ..., upn: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This is an accessory command to the container command which is used
    for some advanced publishing operations on the container. For example,
    the "publishConnections" flag on the container will publish all the
    connections, but this command can be used to publish just the inputs,
    outputs, or to collapse the shared inputs into a single attribute
    before publishing.

    Args:
        bindNode | bn: (create, edit, query) - Bind the specified node to the published node name.
        bindTemplateStandins | bts: (create, edit, query) - This flag will create a temporary stand-in attribute for any attributes that exist in the template but are not already bound. This enables you to set values for unbound attributes.
        inConnections | ic: (create) - Specifies that the unpublished connections to nodes in the container from external nodes should be published.
        mergeShared | ms: (create) - For use with the inConnections flag. Indicates that when an external attribute connects to multiple internal attributes within the container, a single published attribute should be used to correspond to all of the internal attributes.
        outConnections | oc: (create) - Specifies that the unpublished connections from nodes in the container to external nodes should be published.
        publishNode | pn: (create, edit, query) - Publish a name and type. When first published, nothing will be bound. To bind a node to the published name, use the bindNode flag.
        unbindNode | ubn: (create, edit, query) - Unbind the node that is published with the name specified by the flag.
        unpublishNode | upn: (create, edit, query) - Unpublish the specified published node name.
    """
    ...


def containerTemplate(*args, addBindingSet: Optional[Union[str, bool]] = ..., abs: Optional[Union[str, bool]] = ..., addNames: bool = ..., an: bool = ..., addView: Optional[Union[str, bool]] = ..., av: Optional[Union[str, bool]] = ..., allKeyable: bool = ..., ak: bool = ..., attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., attributeList: Optional[Union[str, bool]] = ..., al: Optional[Union[str, bool]] = ..., baseName: Optional[Union[str, bool]] = ..., bn: Optional[Union[str, bool]] = ..., bindingSetList: Optional[Union[str, bool]] = ..., bsl: Optional[Union[str, bool]] = ..., childAnchor: bool = ..., can: bool = ..., delete: bool = ..., d: bool = ..., expandCompounds: bool = ..., ec: bool = ..., fromContainer: Optional[Union[str, bool]] = ..., fc: Optional[Union[str, bool]] = ..., fromSelection: bool = ..., fs: bool = ..., layoutMode: Optional[Union[int, bool]] = ..., lm: Optional[Union[int, bool]] = ..., matchName: Optional[Union[str, bool]] = ..., mn: Optional[Union[str, bool]] = ..., parentAnchor: bool = ..., pan: bool = ..., publishedNodeList: Optional[Union[str, bool]] = ..., pnl: Optional[Union[str, bool]] = ..., removeBindingSet: Optional[Union[str, bool]] = ..., rbs: Optional[Union[str, bool]] = ..., removeView: Optional[Union[str, bool]] = ..., rv: Optional[Union[str, bool]] = ..., rootTransform: bool = ..., rtn: bool = ..., save: bool = ..., s: bool = ..., searchPath: Optional[Union[str, bool]] = ..., sp: Optional[Union[str, bool]] = ..., templateList: Optional[Union[str, bool]] = ..., tl: Optional[Union[str, bool]] = ..., updateBindingSet: Optional[Union[str, bool]] = ..., ubs: Optional[Union[str, bool]] = ..., useHierarchy: bool = ..., uh: bool = ..., exists: bool = ..., ex: bool = ..., fileName: Optional[Union[str, bool]] = ..., fn: Optional[Union[str, bool]] = ..., force: bool = ..., f: bool = ..., load: bool = ..., l: bool = ..., matchFile: Optional[Union[str, bool]] = ..., mf: Optional[Union[str, bool]] = ..., silent: bool = ..., si: bool = ..., unload: bool = ..., u: bool = ..., viewList: Optional[Union[str, bool]] = ..., vl: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    A container template is a description of a container's published interface.
    This command provides the ability to create and save a template file for a
    container or load an existing template file.  Once a template exists,
    the user can query the template information.

    Args:
        addBindingSet | abs: (create, edit) - This argument is used to add a new binding set with the given name to a template. A default binding set will be created. If the binding set already exists, the force flag must be used to replace the existing binding set. When used with the fromContainer option, default bindings will be entered based on the current bindings of the designated container. When used without a reference container, the binding set will be made with placeholder entries. The template must be saved before the new binding set is permanently stored with the template file.
        addNames | an: (edit) - In edit mode, when used with the fromContainer flag, any published name on the container not present as an attribute on the template will be added to the template.
        addView | av: (create, edit) - This argument is used to add a new view with the given name to a template. By default a view containing a flat list of all template attributes will be created.  The layoutMode flag provides more layout options. The template must be saved before the new view is permanently stored with the template file.
        allKeyable | ak: (create, edit) - Used when the fromSelection flag is true and fromContainer is false. If true we will use all keyable attributes to define the template or the view, if false we use the attributes passed in with the attribute flag.
        attribute | at: (create, edit, multiuse) - If fromSelection is true and allKeyable is false, this attribute name will be used to create an attribute item in the template file.
        attributeList | al: (create, edit, query) - Used in query mode, returns a list of attributes contained in the template definition.
        baseName | bn: (create, query) - Used in query mode, returns the base name of the template. The basename is the template name with any package qualifiers stripped off.
        bindingSetList | bsl: (create, query) - Used in query mode, returns a list of all binding sets defined on the template.
        childAnchor | can: (create, query) - This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only childAnchor published nodes.
        delete | d: (create) - Delete the specified template and its file. All objects that are associated with this template or contained in the same template file will be deleted. To simply unload a template without permanently deleting its file, use unload instead.
        expandCompounds | ec: (create, edit) - This argument is used to determine how compound parent attributes and their children will be added to generated views when both are published to the container. When true, the compound parent and all compound child attributes published to the container will be included in the view. When false, only the parent attribute is included in the view. Note: if only the child attributes are published and not the parent, the children will be included in the view, this flag is only used in the situation where both parent and child attributes are published to the container. The default value is false.
        fromContainer | fc: (create) - This argument is used in create or edit mode to specify a container node to be used for generating the template contents. In template creation mode, the template definition will be created based on the list of published attributes in the specified container. In edit mode, when used with the addNames flag or with no other flag, any published name on the container not present as an attribute on the template will be added to the template. This flag is also used in conjunction with flags such as addView.
        fromSelection | fs: (create, edit) - If true, we will use the active selection list to create the template or the view. If allKeyable is also true then we will create the template from all keyable attributes in the selection, otherwise we will create the template using the attributes specified with the attribute flag.
        layoutMode | lm: (create) - This argument is used to specify the layout mode when creating a view. Values correspond as follows: 0: layout in flat list (default when not creating view from container) 1: layout grouped by node (default if creating view from container) The fromContainer or fromSelection argument is required to provide the reference container or selection for layout modes that require node information.  Note that views can only refer to defined template attributes. This means that when using the fromContainer or from Selection flag to add a view to an existing template, only attributes that are defined on both the template and the container or the current selection will be included in the view (i.e. published attributes on the container that are not defined in the template will be ignored).
        matchName | mn: (query) - Used in query mode in conjunction with other flags this flag specifies an optional template name that is to be matched as part of the query operation. The base template name is used for matching, any template with the same basename will be matched even across different packages. 			In query mode, this flag needs a value.
        parentAnchor | pan: (create, query) - This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only parentAnchor published nodes.
        publishedNodeList | pnl: (create, edit, query) - Used in query mode, returns a list of published nodes contained in the template definition. By default all published nodes on the template will be returned. The list of published nodes can be limited to only include certain types of published nodes using one of the childAnchor, parentAnchor or rootTransform flags. If an optional flag is are specified, only nodes of the specified type will be returned.
        removeBindingSet | rbs: (create, edit) - This argument is used to remove the named binding set from the template. The template must be saved before the binding set is permanently removed from the template file.
        removeView | rv: (create, edit) - This argument is used to remove the named view from the template. The template must be saved before the view is permanently removed from the template file.
        rootTransform | rtn: (create, query) - This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only rootTransform published nodes.
        save | s: (create) - Save the specified template to a file. If a filename is specified for the template, the entire file (and all templates associated with it) will be saved. If no file name is specified, a default filename will be assumed, based on the template name.
        searchPath | sp: (edit, query) - The template searchPath is an ordered list of all locations that are being searched to locate template files (first location searched to last location searched). The template search path setting is stored in the current workspace and can also be set and queried as the file rule entry for 'templates' (see the workspace command for more information). In edit mode, this flag allows the search path setting to be customized. When setting the search path value, the list should conform to a path list format expected on the current platform.  This means that paths should be separated by a semicolon (;) on Windows and a colon (:) on Linux and MacOSX. Environment variables can also be used. Additional built-in paths may be added automatically by maya to the customized settings. In query mode, this flag returns the current contents of the search path; all paths, both customized and built-in, will be included in the query return value.
        templateList | tl: (query) - Used in query mode, returns a list of all loaded templates. This query can be used with optional matchFile and matchName flags. When used with the matchFile flag, the list of templates will be restricted to those associated with the specified file.  When used with the matchName flag, the list of templates will be restricted to those matching the specified template name.
        updateBindingSet | ubs: (create, edit) - This argument is used to update an existing binding set with new bindings. When used with the fromContainer argument binding set entries with be replaced or merged in the binding set based on the bindings of the designated container. If the force flag is used, existing entries in the binding set are replaced with new values. When force is not used, only new entries are merged into the binding set, any existing entries will be left as-is. When used without a reference container, the binding set will be updated with placeholder entries. The template must be saved before the new binding set is permanently stored with the template file.
        useHierarchy | uh: (create, edit) - If true, and the fromSelection flag is set, the selection list will expand to include it's hierarchy also.
        exists | ex: (query) - Returns true or false depending upon whether the specified template exists. When used with the matchFile argument, the query will return true if the template exists and the filename it was loaded from matches the filename given.
        fileName | fn: (create, query) - Specifies the filename associated with the template.  This argument can be used in conjunction with load, save or query modes. If no filename is associated with a template, a default file name based on the template name will be used.  It is recommended but not required that the filename and template name correspond.
        force | f: (create) - This flag is used with some actions to allow them to proceed with an overwrite or destructive operation. When used with load, it will allow an existing template to be reloaded from a file.  When used in create mode, it will allow an existing template to be recreated (for example when using fromContainer argument to regenerate a template).
        load | l: () - Load an existing template from a file. If a filename is specified for the template, the entire file (and all templates in it) will be loaded. If no file is specified, a default filename will be assumed, based on the template name.
        matchFile | mf: (query) - Used in query mode in conjunction with other flags this flag specifies an optional file name that is to be matched as part of the query operation. 			In query mode, this flag needs a value.
        silent | si: (create, edit, query) - Silent mode will suppress any error or warning messages that would normally be reported from the command execution.  The return values are unaffected.
        unload | u: (create) - Unload the specified template.  This action will not delete the associated template file if one exists, it merely removes the template definition from the current session.
        viewList | vl: (create, query) - Used in query mode, returns a list of all views defined on the template.
    """
    ...


def containerView(*args, itemInfo: Optional[Union[str, bool]] = ..., ii: Optional[Union[str, bool]] = ..., itemList: bool = ..., il: bool = ..., viewDescription: bool = ..., vd: bool = ..., viewLabel: bool = ..., vb: bool = ..., viewList: bool = ..., vl: bool = ..., viewName: Optional[Union[str, bool]] = ..., vn: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    A container view defines the layout information for the published attributes of a
    particular container.  Container views can be selected from a set of
    built-in views or may be defined on an associated container template.
    This command queries the view-related information for a container node.
    The information returned from this command will be based on the view-related
    settings in force on the container node at the time of the query
    (i.e. the container's view mode, template name, view name attributes).

    Args:
        itemInfo | ii: (query) - Used in query mode in conjunction with the itemList flag. The command will return a list of information for each item in the view, the information fields returned for each item are determined by this argument value. The information fields will be listed in the string array returned. The order in which the keyword is specified will determine the order in which the data will be returned by the command. One or more of the following keywords, separated by colons ':' are used to specify the argument value.  itemIndex  : sequential item number (0-based) itemName   : item name (string) itemLabel  : item display label (string) itemDescription : item description field (string) itemLevel  : item hierarchy level (0-n) itemIsGroup : (boolean 0 or 1) indicates whether or not this item is a group itemIsAttribute : (boolean 0 or 1) indicates whether or not this item is an attribute itemNumChildren: number of immediate children (groups or attributes) of this item itemAttrType : item attribute type (string) itemCallback : item callback field (string)  In query mode, this flag needs a value.
        itemList | il: (query) - Used in query mode, the command will return a list of information for each item in the view.  The viewName flag is used to select the view to query. The information returned about each item is determined by the itemInfo argument value. For efficiency, it is best to query all necessary item information at one time (to avoid recomputing the view information on each call).
        viewDescription | vd: (query) - Used in query mode, returns the description field associated with the selected view. If no description was defined for this view, the value will be empty.
        viewLabel | vb: (query) - Used in query mode, returns the display label associated with the view. An appropriate label suitable for the user interface will be returned based on the selected view.  Use of the view label is usually more suitable than the view name for display purposes.
        viewList | vl: (query) - Used in query mode, command will return a list of all views defined for the given target (container or template).
        viewName | vn: (query) - Used in query mode, specifies the name of the queried view when used in conjunction with a template target. When used in conjunction with a container target, it requires no string argument, and returns the name of the currently active view associated with the container; this value may be empty if the current view is not a valid template view or is generated by one of the built-in views modes. For this reason, the view label is generally more suitable for display purposes. 			In query mode, this flag can accept a value.
    """
    ...


def contextInfo(*args, c: bool = ..., escapeContext: bool = ..., esc: bool = ..., exists: bool = ..., ex: bool = ..., image1: bool = ..., i1: bool = ..., image2: bool = ..., i2: bool = ..., image3: bool = ..., i3: bool = ..., title: bool = ..., t: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command allows you to get information on named contexts.

    Args:
        c | c: (create) - Return the class type of the named context.
        escapeContext | esc: (create) - Return the command string that will allow you to exit the current tool.
        exists | ex: (create) - Return true if the context exists, false if it does not exists (or is internal and therefore untouchable)
        image1 | i1: (create) - Returns the name of an xpm associated with the named context.
        image2 | i2: (create) - Returns the name of an xpm associated with the named context.
        image3 | i3: (create) - Returns the name of an xpm associated with the named context.
        title | t: (create) - Return the title string of the named context.
    """
    ...


def copyAttr(*args, attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., containerParentChild: bool = ..., cpc: bool = ..., inConnections: bool = ..., ic: bool = ..., keepSourceConnections: bool = ..., ksc: bool = ..., outConnections: bool = ..., oc: bool = ..., renameTargetContainer: bool = ..., rtc: bool = ..., values: bool = ..., v: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Given two nodes, transfer the connections and/or the values from the first
    node to the second for all attributes whose names and data types match. When
    values are transferred, they are transferred directly. They are not mapped or
    modified in any way. The transferAttributes command can be used to transfer
    and remap some mesh attributes.
    The attributes flag can be used to specify a list of attributes to be
    processed. If the attributes flag is unused, all attributes will be
    processed. For dynamic attributes, the values and/or connections will only
    be transferred if the attributes names on both nodes match.
    This command does not support geometry shape nodes such as meshes, subds and
    nurbs. This command does not support transfer of multi-attribute values such
    as weight arrays.

    Args:
        attribute | at: (create, multiuse) - The name of the attribute(s) for which connections and/or values will be transferred. If no attributes are specified, then all attributes will be transferred.
        containerParentChild | cpc: (create) - For use when copying from one container to another only. This option indicates that the published parent and/or child relationships on the original container should be transferred to the target container if the published names match.
        inConnections | ic: (create) - Indicates that incoming connections should be transferred.
        keepSourceConnections | ksc: (create) - For use with the outConnections flag only. Indicates that the connections should be maintained on the first node, in addition to making them to the second node. If outConnections is used and keepSourceConnections is not used, the out connections on the source node will be broken and made to the target node.
        outConnections | oc: (create) - Indicates that outgoing connections should be transferred.
        renameTargetContainer | rtc: (create) - For use when copying from one container to another only. This option will rename the target container to the name of the original container, and rename the original container to its old name + "Orig". You would want to use this option if your original container was referenced and edited, and you want those edits from the main scene to now apply to the new container.
        values | v: (create) - Indicates that values should be transferred.
    """
    ...


def createAttrPatterns(*args, patternDefinition: Optional[Union[str, bool]] = ..., pd: Optional[Union[str, bool]] = ..., patternFile: Optional[Union[str, bool]] = ..., pf: Optional[Union[str, bool]] = ..., patternType: Optional[Union[str, bool]] = ..., pt: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Create a new instance of an attribute pattern given a pattern type (e.g. XML) and a string or data file
    containing the description of the attribute tree in the pattern's format.

    Args:
        patternDefinition | pd: (create) - Hardcoded string containing the pattern definition, for simpler formats that don't really need a separate file for definition.
        patternFile | pf: (create) - File where the pattern information can be found
        patternType | pt: (create) - Name of the pattern definition type to use in creating this instance of the pattern.
    """
    ...


def createDisplayLayer(*args, empty: bool = ..., e: bool = ..., makeCurrent: bool = ..., mc: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., noRecurse: bool = ..., nr: bool = ..., number: Optional[Union[int, bool]] = ..., num: Optional[Union[int, bool]] = ...) -> Any:
    r"""
    Create a new display layer.  The display layer number will be assigned
    based on the first unassigned number not less than the base index number
    found in the display layer global parameters.  Normally all objects and
    their descendants will be added to the new display layer but if the '-nr'
    flag is specified then only the objects themselves will be added.

    Args:
        empty | e: (create) - If set then create an empty display layer.  ie. Do not add the selected items to the new display layer.
        makeCurrent | mc: (create) - If set then make the new display layer the current one.
        name | n: (create) - Name of the new display layer being created.
        noRecurse | nr: (create) - If set then only add selected objects to the display layer.  Otherwise all descendants of the selected objects will also be added.
        number | num: (create) - Number for the new display layer being created.
    """
    ...


def createNode(*args, name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., shared: bool = ..., s: bool = ..., skipSelect: bool = ..., ss: bool = ...) -> Any:
    r"""
    This command creates a new node in the dependency graph of the
    specified type.

    Args:
        name | n: (create) - Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace doesn't exist, we will create the namespace.
        parent | p: (create) - Specifies the parent in the DAG under which the new node belongs.
        shared | s: (create) - This node is shared across multiple files, so only create it if it does not already exist.
        skipSelect | ss: (create) - This node is not to be selected after creation, the original selection will be preserved.
    """
    ...


def ctxAbort(*args) -> Any:
    r"""
    This command tells the current context to reset itself, losing
    what has been done so far.  If a escape context has been set
    it then makes that context current.

    Args:
    """
    ...


def ctxCompletion(*args) -> Any:
    r"""
    This command tells the current context to finish what it is
    doing and create any objects that is is working on.

    Args:
    """
    ...


def ctxEditMode(*args, buttonDown: bool = ..., btd: bool = ..., buttonUp: bool = ..., btu: bool = ...) -> Any:
    r"""
    This command tells the current context to switch edit modes.
    It acts as a toggle.

    Args:
        buttonDown | btd: (create) - Edit mode is being invoked from a hotkey press event.
        buttonUp | btu: (create) - Edit mode is being invoked from a hotkey release event.
    """
    ...


def ctxTraverse(*args, down: bool = ..., d: bool = ..., left: bool = ..., l: bool = ..., right: bool = ..., r: bool = ..., up: bool = ...) -> Any:
    r"""
    This command tells the current context to do a traversal.
    
    Some contexts will ignore this command. Individual contexts
    determine what up/down left/right mean.

    Args:
        down | d: (create) - Move "down" as defined by the current context.
        left | l: (create) - Move "left" as defined by the current context.
        right | r: (create) - Move "right" as defined by the current context.
        up | up: (create) - Move "up" as defined by the current context.
    """
    ...


def currentCtx(*args) -> Any:
    r"""
    This command returns the currently selected tool context.

    Args:
    """
    ...


def currentTimeCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context which may be used to change current time
    within the graph editor

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def currentUnit(*args, angle: Optional[Union[str, bool]] = ..., a: Optional[Union[str, bool]] = ..., fullName: bool = ..., f: bool = ..., linear: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., time: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ..., updateAnimation: bool = ..., ua: bool = ..., query: bool = ...) -> Any:
    r"""
    This command allows you to change the units in which you will work
    in Maya. There are three types of units: linear, angular and time.
    
    The current unit affects how all commands in Maya interpret their
    numeric values. For example, if the current linear unit is cm,
    then the command:
    
    move 5 -2 3;
    sphere -radius 4;
    
    will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as
    creating a sphere with radius 4cm. Similarly, if the current time unit
    is Film (24 frames per second), then the command:
    
    currentTime 6;
    
    will be interpreted as setting the current time to frame 6 in the Film
    unit, which is 6/24 or 0.25 seconds.
    
    You can always override the unit of a particular numeric value to a
    command be specifying it one the command. For example, using the above
    examples:
    
    move 5m -2mm 3cm;
    sphere -radius 4inch;
    currentTime 6ntsc;
    
    would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters
    in Z, create a sphere of radius 4 inches, and change the current time
    to 6 frames in the NTSC unit, which would be 0.2 seconds, or 4.8 frames
    in the current (Film) unit.

    Args:
        angle | a: (create, query) - Set the current angular unit. Valid strings are:  [deg | degree | rad | radian]  When queried, returns a string which is the current angular unit
        fullName | f: (query) - A query only flag. When specified in conjunction with any of the -linear/-angle/-time flags, will return the long form of the unit. For example, mm and millimeter are the same unit, but the former is the short form of the unit name, and the latter is the long form of the unit name.
        linear | l: (create, query) - Set the current linear unit. Valid strings are:  [mm | millimeter | cm | centimeter | m | meter | km | kilometer | in | inch | ft | foot | yd | yard | mi | mile]  When queried, returns a string which is the current linear unit
        time | t: (create, query) - Set the current time unit. Valid strings are:  [hour | min | sec | millisec | game | film | pal | ntsc | show | palf | ntscf | 23.976fps | 29.97fps | 29.97df | 47.952fps | 59.94fps | 44100fps | 48000fps]  When queried, returns a string which is the current time unit  Note that there is no long form for any of the time units. The non-seconds based time units are interpreted as the following frames per second:  game: 15 fps film: 24 fps pal: 25 fps ntsc: 30 fps show: 48 fps palf: 50 fps ntscf: 60 fps
        updateAnimation | ua: (create) - An edit only flag.  When specified in conjunction with the -time flag indicates that times for keys are not updated.  By default when the current time unit is changed, the times for keys are modified so that playback timing is preserved.  For example a key set a frame 12film is changed to frame 15ntsc when the current time unit is changed to ntsc, since they both represent a key at a time of 0.5 seconds.  Specifying -updateAnimation false would leave the key at frame 12ntsc. Default is -updateAnimation true.
    """
    ...


def curveAddPtCtx(*args, exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The curveAddPtCtx command creates a new curve add points context,
    which adds either control vertices (CVs) or edit points to an
    existing curve.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
    """
    ...


def curveCVCtx(*args, bezier: bool = ..., bez: bool = ..., degree: Optional[Union[int, bool]] = ..., d: Optional[Union[int, bool]] = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., multEndKnots: bool = ..., me: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., preserveShape: bool = ..., ps: bool = ..., rational: bool = ..., rl: bool = ..., refit: bool = ..., rf: bool = ..., symmetry: bool = ..., sm: bool = ..., uniform: bool = ..., un: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The curveCVCtx command creates a new context for creating curves
    by placing control vertices (CVs).

    Args:
        bezier | bez: (create, edit, query) - 
        degree | d: (create, edit, query) - Curve degree
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        multEndKnots | me: (create, edit, query) - Specify if multiple end knots are to be created.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        preserveShape | ps: (create, edit, query) - Set this flag to make the operation preserve the shape
        rational | rl: (create, edit, query) - Should the curve be rational?
        refit | rf: (create, edit, query) - Set this flag to refit the curve
        symmetry | sm: (create, edit, query) - Specify if symmetry is to be used
        uniform | un: (create, edit, query) - Should the curve use uniform parameterization?
    """
    ...


def curveEditorCtx(*args, direction: Optional[Union[int, bool]] = ..., dir: Optional[Union[int, bool]] = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., relativeTangentSize: Optional[Union[float, bool]] = ..., rts: Optional[Union[float, bool]] = ..., title: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The curveEditorCtx command creates a new NURBS editor context, which
    is used to edit a NURBS curve or surface.

    Args:
        direction | dir: (query) - Query the current direction of the tangent control.  Always zero for the curve case.  In the surface case, its 0 for the normal direction, 1 for U direction and 2 for V direction.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        relativeTangentSize | rts: (create, edit, query) - Relative size of the tangent manipulator handle.  Helps to adjust as the surface parameterization controls the size of the tangent, even if the shape of the surface remains the same. The default is 4.
        title | t: (edit, query) - The title for the tool.
    """
    ...


def curveEPCtx(*args, bezier: bool = ..., bez: bool = ..., degree: Optional[Union[int, bool]] = ..., d: Optional[Union[int, bool]] = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., preserveShape: bool = ..., ps: bool = ..., preserveShapeFraction: Optional[Union[float, bool]] = ..., pf: Optional[Union[float, bool]] = ..., refit: bool = ..., rf: bool = ..., uniform: bool = ..., un: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The curveEPCtx command creates a new context for creating curves
    by placing edit points.

    Args:
        bezier | bez: (create, edit, query) - Use bezier curves
        degree | d: (create, edit, query) - Curve degree
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        preserveShape | ps: (create, edit, query) - Set this flag to make the operation preserve the shape
        preserveShapeFraction | pf: (create, edit, query) - Fraction value used when preserving the shape
        refit | rf: (create, edit, query) - Set this flag to refit the curve
        uniform | un: (create, edit, query) - Should the curve use uniform parameterization?
    """
    ...


def curveMoveEPCtx(*args, exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The curveMoveEPCtx command creates a new context for moving
    curve edit points using a manipulator.  Edit points can only be
    moved one at a time.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
    """
    ...


def curveSketchCtx(*args, degree: Optional[Union[int, bool]] = ..., d: Optional[Union[int, bool]] = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The curveSketchCtx command creates a new curve sketch context,
    also known as the "pencil context".

    Args:
        degree | d: (create, edit, query) - Valid values are 1 or 3
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def cycleCheck(*args, all: bool = ..., children: bool = ..., c: bool = ..., dag: bool = ..., evaluation: bool = ..., e: bool = ..., firstCycleOnly: bool = ..., fco: bool = ..., firstPlugPerNode: bool = ..., fpn: bool = ..., lastPlugPerNode: bool = ..., lpn: bool = ..., list: bool = ..., l: bool = ..., listSeparator: Optional[Union[str, bool]] = ..., ls: Optional[Union[str, bool]] = ..., parents: bool = ..., p: bool = ..., secondary: bool = ..., s: bool = ..., timeLimit: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., tl: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command searches for plug cycles in the dependency graph. If
    a plug or node is selected then it searches for cycles that
    that plug or node is involved with. Plugs or nodes can also be passed
    as arguments. If the -all flag is used then the entire graph is searched.
    
    Normally the return value is a boolean indicating whether or not the
    given items were involved in a cycle.  If the -list flag is used then
    the return value is the list of all plugs in cycles (involving the
    selected plug or node if any).
    
    Note that it is possible for evaluation cycles to occur even where
    no DG connections exist. Here are some examples:
    
    1) Nodes with evaluation-time dependent connections: An example is
    expression nodes, because we cannot tell what an expression
    node is actually referring to until it is evaluated, and such
    evaluation-time dependent nodes may behave differently based on
    the context (e.g. time) they are evaluated at. If you suspect a
    cycle due to such a connection, the best way to detect the
    cycle is through manual inspection.
    
    2) Cycles due to DAG hierarchy: noting that DAG nodes are implicitely
    connected through parenting, if a child DAG node connects an output into
    the input of a parent node, a cycle will exist if the plugs involved
    also affect each other. In order to enable detection of cycles
    involving the DAG, add the -dag flag to the command line.
    
    Note also that this command may incorrectly report a cycle on
    an instanced skeleton where some of the instances use IK.
    You will have to examine the reported cycle yourself to determine
    if it is truly a cycle or not.
    The evaluation time cycle checking will not report false cycles.

    Args:
        all | all: (create) - search the entire graph for cycles instead of the selection list. (Note: if nothing is selected, -all is assumed).
        children | c: (create) - Do not consider cycles on the children, only the specified plugs
        dag | dag: (create) - Also look for cycles due to relationships in the DAG. For each DAG node, the parenting connection on its children is also considered when searching for cycles.
        evaluation | e: (create, query) - Turn on and off cycle detection during graph evaluation
        firstCycleOnly | fco: (create) - When -list is used to return a plug list, the list may contain multiple cycles or partial cycles. When -firstCycleOnly is specified only the first such cycle (which will be a full cycle) is returned.
        firstPlugPerNode | fpn: (create) - When -list is used to return a plug list, the list will typically contain multiple plugs per node (e.g. ... A.output B.input B.output C.input ...), reflecting internal "affects" relationships rather than external DG connections. When -firstPlugPerNode is specified, only the first plug in the list for each node is returned (B.input in the example).
        lastPlugPerNode | lpn: (create) - When -list is used to return a plug list, the list will typically contain multiple plugs per node (e.g. ... A.output B.input B.output C.input ...), reflecting internal "affects" relationships rather than external DG connections. When -lastPlugPerNode is specified, only the last plug in the list for each node is returned (B.output in the example).
        list | l: (create) - Return all plugs involved in one or more cycles.  If not specified, returns a boolean indicating whether a cycle exists.
        listSeparator | ls: (create) - When -list is used to return a plug list, the list may contain multiple cycles or partial cycles. Use -listSeparator to specify a string that will be inserted into the returned string array to separate the cycles.
        parents | p: (create) - Do not consider cycles on the parents, only the specified plugs
        secondary | s: (create) - Look for cycles on related plugs as well as the specified plugs Default is "on" for the "-all" case and "off" for others
        timeLimit | tl: (create) - Limit the search to the given amount of time
    """
    ...


def delete(*args, all: bool = ..., attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., channels: bool = ..., c: bool = ..., constraints: bool = ..., cn: bool = ..., constructionHistory: bool = ..., ch: bool = ..., controlPoints: bool = ..., cp: bool = ..., expressions: bool = ..., e: bool = ..., hierarchy: Optional[Union[str, bool]] = ..., hi: Optional[Union[str, bool]] = ..., inputConnectionsAndNodes: bool = ..., icn: bool = ..., motionPaths: bool = ..., mp: bool = ..., shape: bool = ..., s: bool = ..., staticChannels: bool = ..., sc: bool = ..., timeAnimationCurves: bool = ..., tac: bool = ..., unitlessAnimationCurves: bool = ..., uac: bool = ...) -> Any:
    r"""
    This command is used to delete selected objects, or all objects, or
    objects specified along with the command. Flags are available to
    filter the type of objects that the command acts on.
    
    At times, more than just specified items will be deleted.  For
    example, deleting two CVs in the same "row" on a NURBS surface
    will delete the whole row.

    Args:
        all | all: (create) - Remove all objects of specified kind, in the scene. This flag is to be used in conjunction with the following flags.
        attribute | at: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        channels | c: (create) - Remove animation channels in the scene. Either all channels can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
        constraints | cn: (create) - Remove selected constraints and constraints attached to the selected nodes, or remove all constraints in the scene.
        constructionHistory | ch: (create) - Remove the construction history on the objects specified or selected.
        controlPoints | cp: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        expressions | e: (create) - Remove expressions in the scene. Either all expressions can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
        hierarchy | hi: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        inputConnectionsAndNodes | icn: (create) - Break input connection to specified attribute and delete all unconnected nodes that are left behind. The graph will be traversed until a node that cannot be deleted is encountered.
        motionPaths | mp: (create) - Remove motion paths in the scene. Either all motion paths can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
        shape | s: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        staticChannels | sc: (create) - Remove static animation channels in the scene. Either all static channels can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
        timeAnimationCurves | tac: (create) - Modifies the -c/channels and -sc/staticChannels flags. When true, only channels connected to time-input animation curves (for instance, those created by 'setKeyframe' will be deleted.  When false, no time-input animation curves will be deleted. Default: true.
        unitlessAnimationCurves | uac: (create) - Modifies the -c/channels and -sc/staticChannels flags. When true, only channels connected to unitless-input animation curves (for instance, those created by 'setDrivenKeyframe' will be deleted.  When false, no unitless-input animation curves will be deleted.  Default: true.
    """
    ...


def deleteAttr(*args, attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to delete a dynamic attribute
    from a node or nodes. The attribute can be specified
    by using either the long or short name. Only one
    dynamic attribute can be deleted at a time. Static
    attributes cannot be deleted. Children of a compound
    attribute cannot be deleted. You must delete the
    complete compound attribute. This command has no
    edit capabilities. The only query ability is to list
    all the dynamic attributes of a node.

    Args:
        attribute | at: (create) - Specify either the long or short name of the attribute.
    """
    ...


def deleteAttrPattern(*args, allPatterns: bool = ..., all: bool = ..., patternName: Optional[Union[str, bool]] = ..., pn: Optional[Union[str, bool]] = ..., patternType: Optional[Union[str, bool]] = ..., pt: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    After a while the list of attribute patterns could become cluttered.
    This command provides a way to remove patterns from memory so that only
    the ones of interest will show.

    Args:
        allPatterns | all: (create) - If specified it means delete all known attribute patterns.
        patternName | pn: (create) - The name of the pattern to be deleted.
        patternType | pt: (create) - Delete all patterns of the given type.
    """
    ...


def deleteExtension(*args, attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., forceDelete: bool = ..., fd: bool = ..., nodeType: Optional[Union[str, bool]] = ..., nt: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This command is used to delete an extension attribute
    from a node type. The attribute can be specified
    by using either the long or short name. Only one
    extension attribute can be deleted at a time.
    Children of a compound attribute cannot be deleted,
    you must delete the complete compound attribute.
    This command has no undo, edit, or query capabilities.

    Args:
        attribute | at: (create) - Specify either the long or short name of the attribute.
        forceDelete | fd: (create) - If this flag is set and turned ON then data values for the extension attributes are all deleted without confirmation. If it's set and turned OFF then any extension attributes that have non-default values set on any node will remain in place. If this flag is not set at all then the user will be asked if they wish to preserve non-default values on this attribute.
        nodeType | nt: (create) - The name of the node type.
    """
    ...


def directKeyCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., option: Optional[Union[str, bool]] = ..., o: Optional[Union[str, bool]] = ..., selectedOnly: bool = ..., so: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context which may be used to directly manipulate keyframes
    within the graph editor

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        option | o: (create, edit, query) - Valid values are "move," "insert," "over," and "segmentOver." When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to make room for the segment.
        selectedOnly | so: (create, edit, query) - Controls whether only selected curves/keys can be moved, or all.
    """
    ...


def disconnectAttr(*args, nextAvailable: bool = ..., na: bool = ...) -> Any:
    r"""
    Disconnects two connected attributes. First argument is the source
    attribute, second is the destination.

    Args:
        nextAvailable | na: (create) - If the destination multi-attribute has set the indexMatters to be false, the command will disconnect the first matching connection.  No index needs to be specified.
    """
    ...


def displayAffected(*args, query: bool = ...) -> Any:
    r"""
    Turns on/off the special coloring of objects that are affected by the
    objects that are currently in the selection list.
    
    If one of the curves in a loft were selected and this feature were
    turned on, then the lofted surface would be highlighted because it
    is affected by the loft curve.

    Args:
    """
    ...


def displayColor(*args, active: bool = ..., a: bool = ..., create: bool = ..., c: bool = ..., dormant: bool = ..., d: bool = ..., list: bool = ..., l: bool = ..., queryIndex: Optional[Union[int, bool]] = ..., qi: Optional[Union[int, bool]] = ..., resetToFactory: bool = ..., rf: bool = ..., resetToSaved: bool = ..., rs: bool = ..., query: bool = ...) -> Any:
    r"""
    This command changes or queries the display color for anything
    in the application that allows the user to set its color.
    The color is defined by a color index into either the dormant
    or active color palette.
    These colors are part of the UI and not part of the saved
    data for a model.  This command is not undoable.

    Args:
        active | a: (create) - Specifies the color index applies to active color palette. name Specifies the name of color to change. index The color index for the color.
        create | c: (create) - Creates a new display color which can be queried or set. If is used only when saving color preferences.
        dormant | d: (create) - Specifies the color index applies to dormant color palette. If neither of the dormant or active flags is specified, dormant is the default.
        list | l: (create) - Writes out a list of all color names and their value.
        queryIndex | qi: (create) - Allows you to obtain a list of color names with the given color indices.
        resetToFactory | rf: (create) - Resets all display colors to their factory defaults.
        resetToSaved | rs: (create) - Resets all display colors to their saved values.
    """
    ...


def displayCull(*args, backFaceCulling: bool = ..., bfc: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is responsible for setting the display culling
    property of back faces of surfaces.

    Args:
        backFaceCulling | bfc: (create, query) - Enable/disable culling of back faces.
    """
    ...


def displayLevelOfDetail(*args, levelOfDetail: bool = ..., lod: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is responsible for setting the display level-of-detail
    for edit refreshes.  If enabled, objects will draw with lower detail
    based on their distance from the camera. When disabled objects will
    display at full resolution at all times.  This is not an undoable
    command

    Args:
        levelOfDetail | lod: () - Enable/disable level of detail.
    """
    ...


def displayPref(*args, activeObjectPivots: bool = ..., aop: bool = ..., displayAffected: bool = ..., da: bool = ..., displayGradient: bool = ..., dgr: bool = ..., ghostFrames: Optional[Union[Tuple[int, int, int], bool]] = ..., gf: Optional[Union[Tuple[int, int, int], bool]] = ..., materialLoadingMode: Optional[Union[str, bool]] = ..., mld: Optional[Union[str, bool]] = ..., maxHardwareTextureResolution: bool = ..., mhr: bool = ..., maxTextureResolution: Optional[Union[int, bool]] = ..., mtr: Optional[Union[int, bool]] = ..., purgeExistingTextures: bool = ..., pet: bool = ..., regionOfEffect: bool = ..., roe: bool = ..., shadeTemplates: bool = ..., st: bool = ..., textureDrawPixel: bool = ..., tdp: bool = ..., wireframeOnShadedActive: Optional[Union[str, bool]] = ..., wsa: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command sets/queries the state of global display parameters.

    Args:
        activeObjectPivots | aop: (create, query) - Sets the display state for drawing pivots for active objects.
        displayAffected | da: (create, query) - Turns on/off the special coloring of objects that are affected by the objects that are currently in the selection list. If one of the curves in a loft were selected and this feature were turned on, then the lofted surface would be highlighted because it is affected by the loft curve.
        displayGradient | dgr: (create, query) - Set whether to display the background using a colored gradient as opposed to a constant background color.
        ghostFrames | gf: (create, query) - Obsolete - use the "ghosting" command to set these values.
        materialLoadingMode | mld: (create, query) - Sets the material loading mode when loading the scene.  Possible values for the string argument are "immediate", "deferred" and "parallel".
        maxHardwareTextureResolution | mhr: (query) - Query the maximum allowable hardware texture resolution available on the current video card. This maximum can vary between different video cards and different operating systems.
        maxTextureResolution | mtr: (create, query) - Sets the maximum hardware texture resolution to be used when creating hardware textures for display. The maximum will be clamped to the maximum allowable texture determined for the hardware at the time this command is invoked. Use the -maxHardwareTextureResolution to retrieve this maximum value. Existing hardware textures are not affected. Only newly created textures will be clamped to this maximum.
        purgeExistingTextures | pet: (create) - Purge any existing hardware textures. This will force a re-evaluation of hardware textures used for display, and thus may take some time to evaluate.
        regionOfEffect | roe: (create, query) - Turns on/off the display of the region of curves/surfaces that is affected by changes to selected CVs and edit points.
        shadeTemplates | st: (create, query) - Turns on/off the display of templated surfaces as shaded in shaded display mode. If its off, templated surfaces appear in wireframe.
        textureDrawPixel | tdp: (create, query) - Sets the display mode for drawing image planes. True for use of gltexture calls for perspective views. This flag should not normally be needed. Image Planes may display faster on Windows but can result in some display artifacts.
        wireframeOnShadedActive | wsa: (create, query) - Sets the display state for drawing the wireframe on active shaded objects.  Possible values for the string argument are "full", "reduced" and "none".
    """
    ...


def displayRGBColor(*args, alpha: bool = ..., a: bool = ..., create: bool = ..., c: bool = ..., hueSaturationValue: bool = ..., hsv: bool = ..., list: bool = ..., l: bool = ..., resetToFactory: bool = ..., rf: bool = ..., resetToSaved: bool = ..., rs: bool = ..., query: bool = ...) -> Any:
    r"""
    This command changes or queries the display color for anything
    in the application that allows the user to set its color.
    These colors are part of the UI and not part of the saved
    data for a model.  This command is not undoable.

    Args:
        alpha | a: (query) - Indicates that we want to query the alpha value of the color. Upon query, returns RGBA or HSVA as an array of 4 floats.
        create | c: (create) - Creates a new RGB display color which can be queried or set. If is used only when saving color preferences. name Specifies the name of color to change.
        hueSaturationValue | hsv: (create, query) - Indicates that rgb values are really hsv values. Upon query, returns the HSV values as an array of 3 floats. h s v The HSV values for the color.  (Between 0-1)
        list | l: (create) - Writes out a list of all RGB color names and their value.
        resetToFactory | rf: (create) - Resets all the RGB display colors to their factory defaults.
        resetToSaved | rs: (create) - Resets all the RGB display colors to their saved values.
    """
    ...


def displaySmoothness(*args, all: bool = ..., boundary: bool = ..., bn: bool = ..., defaultCreation: bool = ..., dc: bool = ..., divisionsU: Optional[Union[int, bool]] = ..., du: Optional[Union[int, bool]] = ..., divisionsV: Optional[Union[int, bool]] = ..., dv: Optional[Union[int, bool]] = ..., full: bool = ..., f: bool = ..., hull: bool = ..., hl: bool = ..., pointsShaded: Optional[Union[int, bool]] = ..., ps: Optional[Union[int, bool]] = ..., pointsWire: Optional[Union[int, bool]] = ..., pw: Optional[Union[int, bool]] = ..., polygonObject: Optional[Union[int, bool]] = ..., po: Optional[Union[int, bool]] = ..., renderTessellation: bool = ..., rt: bool = ..., simplifyU: Optional[Union[int, bool]] = ..., su: Optional[Union[int, bool]] = ..., simplifyV: Optional[Union[int, bool]] = ..., sv: Optional[Union[int, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command is responsible for setting the display smoothness
    of NURBS curves and surfaces to either predefined or custom values.
    It also sets display modes for smoothness such as hulls and the
    hull simplification factors.
    At present, this command is NOT un-doable.

    Args:
        all | all: (create, query) - Change smoothness for all curves and surfaces
        boundary | bn: (create, query) - Display wireframe surfaces using only the boundaries of the surface Not fully implemented yet
        defaultCreation | dc: (create, query) - The default values at creation (applies only -du, -dv, -pw, -ps)
        divisionsU | du: (create, query) - Number of isoparm divisions per span in the U direction. The valid range of values is [0,64].
        divisionsV | dv: (create, query) - Number of isoparm divisions per span in the V direction. The valid range of values is [0,64].
        full | f: (create, query) - Display surface at full resolution - the default.
        hull | hl: (create, query) - Display surface using the hull (control points are drawn rather than surface knot points). This mode is a useful display performance improvement when modifying a surface since it doesn't require evaluating points on the surface.
        pointsShaded | ps: (create, query) - Number of points per surface span in shaded mode. The valid range of values is [1,64].
        pointsWire | pw: (create, query) - Number of points per surface isoparm span or the number of points per curve span in wireframe mode. The valid range of values is [1,128]. Note: This is the only flag that also applies to nurbs curves.
        polygonObject | po: (create, query) - Display the polygon objects with the given resolution
        renderTessellation | rt: (create, query) - Display using render tesselation parameters when in shaded mode.
        simplifyU | su: (create, query) - Number of spans to skip in the U direction when in hull display mode.
        simplifyV | sv: (create, query) - Number of spans to skip in the V direction when in hull display mode.
    """
    ...


def displaySurface(*args, flipNormals: bool = ..., flp: bool = ..., twoSidedLighting: bool = ..., two: bool = ..., xRay: bool = ..., x: bool = ..., query: bool = ...) -> Any:
    r"""
    This command toggles display options on the specified or active
    surfaces. Typically this command applies to NURBS or poly mesh
    surfaces and ignores other type of objects.

    Args:
        flipNormals | flp: (query) - flip normal direction on the surface
        twoSidedLighting | two: (query) - toggle if the surface should be considered two-sided.  If it's single-sided, drawing and rendering may use single sided lighting and back face cull to improve performance.
        xRay | x: (query) - toggle X ray mode (make surface transparent)
    """
    ...


def distanceDimContext(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command used to register the distanceDimCtx tool.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def distanceDimension(*args, endPoint: Optional[Union[Tuple[float, float, float], bool]] = ..., ep: Optional[Union[Tuple[float, float, float], bool]] = ..., startPoint: Optional[Union[Tuple[float, float, float], bool]] = ..., sp: Optional[Union[Tuple[float, float, float], bool]] = ...) -> Any:
    r"""
    This command is used to create a distance dimension to display the
    distance between two specified points.

    Args:
        endPoint | ep: (create) - Specifies the point to measure distance to, from the startPoint.
        startPoint | sp: (create) - Specifies the point to start measuring distance from.
    """
    ...


def dollyCtx(*args, alternateContext: bool = ..., ac: bool = ..., boxDollyType: Optional[Union[str, bool]] = ..., bdt: Optional[Union[str, bool]] = ..., centerOfInterestDolly: bool = ..., cd: bool = ..., dollyTowardsCenter: bool = ..., dtc: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., localDolly: bool = ..., ld: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., orthoZoom: bool = ..., oz: bool = ..., scale: Optional[Union[float, bool]] = ..., s: Optional[Union[float, bool]] = ..., toolName: Optional[Union[str, bool]] = ..., tn: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create, edit, or query a dolly
    context.

    Args:
        alternateContext | ac: (create, query) - Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        boxDollyType | bdt: (create, edit, query) - Set the behavior of where the camera's center of interest is set to after the box dolly. In surface mode, the center of interest will be snapped to the surface point at the center of the marquee. In bbox mode, the closest bounding box to the camera will be used. Bounding box mode will use the selection mask to determine which objects to include into the calculation.
        centerOfInterestDolly | cd: (create, edit, query) - Set the translate the camera's center of interest. Left and right drag movements with the mouse will translate the center of interest towards or away respectively from the camera. The center of interest can be snapped to objects by using the left mouse button for selection. The default select mask will be used.
        dollyTowardsCenter | dtc: (create, edit, query) - Dolly towards center (if true), else dolly towards point where user clicks in the view.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        localDolly | ld: (create, edit, query) - Dolly with respect to the camera's center of interest. The camera will not pass through the center of interest. Local dolly only applies to perspective cameras.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        orthoZoom | oz: (create, edit, query) - Zoom orthographic view (if true), else dolly orthographic camera. Default value is true.
        scale | s: (create, edit, query) - The sensitivity for dollying the camera.
        toolName | tn: (create, query) - Name of the specific tool to which this command refers.
    """
    ...


def dragAttrContext(*args, connectTo: Optional[Union[str, bool]] = ..., ct: Optional[Union[str, bool]] = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., reset: bool = ..., r: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The dragAttrContext allows a user to manipulate the attributes of an object by using
    a virtual slider within the viewport.  The virtual slider is used by dragging in a
    viewport with the middle mouse button.  The speed at which the attributes are changed
    can be controlled by holding down the Ctrl key to slow it down and the Shift key to
    speed it up.

    Args:
        connectTo | ct: (create, edit, multiuse, query) - Specifies an attribute to which to connect the context. This is a multi-use flag, but all attributes used must be from one object.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        reset | r: (create, edit) - Resets the list of attributes to which the context is connected.
    """
    ...


def draggerContext(*args, anchorPoint: Optional[Union[Tuple[float, float, float], bool]] = ..., ap: Optional[Union[Tuple[float, float, float], bool]] = ..., button: Optional[Union[int, bool]] = ..., bu: Optional[Union[int, bool]] = ..., currentStep: Optional[Union[int, bool]] = ..., cs: Optional[Union[int, bool]] = ..., cursor: Optional[Union[str, bool]] = ..., cur: Optional[Union[str, bool]] = ..., dragCommand: Optional[Union[str, bool]] = ..., dc: Optional[Union[str, bool]] = ..., dragPoint: Optional[Union[Tuple[float, float, float], bool]] = ..., dp: Optional[Union[Tuple[float, float, float], bool]] = ..., drawString: Optional[Union[str, bool]] = ..., ds: Optional[Union[str, bool]] = ..., exists: bool = ..., ex: bool = ..., finalize: Optional[Union[str, bool]] = ..., fnz: Optional[Union[str, bool]] = ..., helpString: Optional[Union[str, bool]] = ..., hs: Optional[Union[str, bool]] = ..., history: bool = ..., ch: bool = ..., holdCommand: Optional[Union[str, bool]] = ..., hc: Optional[Union[str, bool]] = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., initialize: Optional[Union[str, bool]] = ..., inz: Optional[Union[str, bool]] = ..., modifier: Optional[Union[str, bool]] = ..., mo: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., plane: Optional[Union[Tuple[float, float, float], bool]] = ..., pl: Optional[Union[Tuple[float, float, float], bool]] = ..., prePressCommand: Optional[Union[str, bool]] = ..., ppc: Optional[Union[str, bool]] = ..., pressCommand: Optional[Union[str, bool]] = ..., pc: Optional[Union[str, bool]] = ..., projection: Optional[Union[str, bool]] = ..., pr: Optional[Union[str, bool]] = ..., releaseCommand: Optional[Union[str, bool]] = ..., rc: Optional[Union[str, bool]] = ..., snapping: bool = ..., snp: bool = ..., space: Optional[Union[str, bool]] = ..., sp: Optional[Union[str, bool]] = ..., stepsCount: Optional[Union[int, bool]] = ..., sc: Optional[Union[int, bool]] = ..., undoMode: Optional[Union[str, bool]] = ..., um: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The draggerContext allows the user to program the behavior of the mouse
    or an equivalent dragging device in MEL.

    Args:
        anchorPoint | ap: (query) - Anchor point (double array) where dragger was initially pressed.
        button | bu: (query) - Returns the current mouse button (1,2,3).
        currentStep | cs: (query) - Current step (press-drag-release sequence) for dragger context. When queried before first press event happened, returns 0.
        cursor | cur: (create, edit, query) - Cursor displayed while context is active.  Valid values are: "default", "hand", "crossHair", "dolly", "track", and "tumble".
        dragCommand | dc: (create, edit, query) - Command called when mouse dragger is dragged.
        dragPoint | dp: (query) - Drag point (double array) current position of dragger during drag.
        drawString | ds: (create, edit) - A string to be drawn at the current position of the pointer.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        finalize | fnz: (create, edit, query) - Command called when the tool is exited.
        helpString | hs: (query) - Help string for context
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        holdCommand | hc: (create, edit, query) - Command called when mouse dragger is held.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        initialize | inz: (create, edit, query) - Command called when the tool is entered.
        modifier | mo: (query) - Returns the current modifier type:  ctrl, alt or none.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        plane | pl: (create, edit) - Provide normal of projection plane (see -projection flag for details).
        prePressCommand | ppc: (create, edit, query) - Command called when mouse dragger is pressed. It is called before pressCommand, so it can be used for initialization of context.
        pressCommand | pc: (create, edit, query) - Command called when mouse dragger is pressed.
        projection | pr: (create, edit, query) - Sets current projection of drag point. Valid types are:   viewPlane project to view plane   objectViewPlane project to object plane (parallel to view plane)   objectPlane project to specified plane defined by object location and normal (default) 0,1,0   plane project to specified plane defined by origin and normal (default) 0,1,0   sketchPlane project to sketch plane   xAxis project to closest point on X axis   yAxis project to closest point on Y axis   zAxis project to closest point on Z axis   boundingSphere project to closest point on object sphere bounds   boundingBox project to closest point on object bounding box
        releaseCommand | rc: (create, edit, query) - Command called when mouse dragger is released.
        snapping | snp: (create, edit, query) - Enable/disable snapping for dragger context.
        space | sp: (create, edit, query) - Sets current space that coordinates are reported in. Types are:   world world space (global)   object object space (local)   screen screen space
        stepsCount | sc: (create, edit, query) - Number of steps (press-drag-release sequences) for dragger context. When combined with undoMode flag, several steps might be recorded as single undo action.
        undoMode | um: (create, edit, query) - Undo queue mode for the context actions. Acceptable values are:  "all" default behaviour when every action that happens during dragger context activity is recorded as an individual undo chunk. "step" - all the actions that happen between each press and release are combined into one undo chunk. "sequence" - all the actions that happen between very first press and very last release are combined into single undo chunk. This works exactly the same as "step" for a single step dragger context.
    """
    ...


def duplicate(*args, fullPath: bool = ..., f: bool = ..., inputConnections: bool = ..., ic: bool = ..., instanceLeaf: bool = ..., ilf: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., parentOnly: bool = ..., po: bool = ..., renameChildren: bool = ..., rc: bool = ..., returnRootsOnly: bool = ..., rr: bool = ..., smartTransform: bool = ..., st: bool = ..., transformsOnly: bool = ..., to: bool = ..., upstreamNodes: bool = ..., un: bool = ...) -> Any:
    r"""
    This command duplicates the given objects. If no objects are
    given, then the selected list is duplicated.
    
    The smart transform feature allows duplicate to transform
    newly duplicated objects based on previous transformations
    between duplications.
    
    Example: Duplicate an object and move it to a new
    location. Duplicate it again with the smart duplicate
    flag. It should have moved once again the distance you had
    previously moved it.
    
    Note: changing the selected list between smart duplications
    will cause the transform information to be deleted
    
    The upstream Nodes option forces duplication of all
    upstream nodes leading upto the selected objects.. Upstream nodes
    are defined as all nodes feeding into selected nodes. During traversal
    of Dependency graph, if another dagObject is encountered, then that
    node and all it's parent transforms are also duplicated.
    
    The inputConnections option forces the duplication of input connections
    to the nodes that are to be duplicated. This is very useful especially
    in cases where two nodes that are connected to each other are
    specified as nodes to be duplicated. In that situation, the connection
    between the nodes is also duplicated.
    
    See also: instance

    Args:
        fullPath | f: (create) - ADDED 2023 Return full pathnames instead of object names.
        inputConnections | ic: (create) - Input connections to the node to be duplicated, are also duplicated. This would result in a fan-out scenario as the nodes at the input side are not duplicated (unlike the -un option).
        instanceLeaf | ilf: (create) - instead of duplicating leaf DAG nodes, instance them.
        name | n: (create) - name to give duplicated object(s)
        parentOnly | po: (create) - Duplicate only the specified DAG node and not any of its children.
        renameChildren | rc: (create) - rename the child nodes of the hierarchy, to make them unique.
        returnRootsOnly | rr: (create) - return only the root nodes of the new hierarchy. When used with upstreamNodes flag, the upstream nodes will be omitted in the result.  This flag controls only what is returned in the output string[], and it does NOT change the behaviour of the duplicate command.
        smartTransform | st: (create) - remembers last transformation and applies it to duplicated object(s)
        transformsOnly | to: (create) - Duplicate only transform nodes and not any shapes.
        upstreamNodes | un: (create) - the upstream nodes leading upto the selected nodes (along with their connections) are also duplicated.
    """
    ...


def dynParticleCtx(*args, conserve: Optional[Union[float, bool]] = ..., c: Optional[Union[float, bool]] = ..., cursorPlacement: bool = ..., cp: bool = ..., exists: bool = ..., ex: bool = ..., grid: bool = ..., gr: bool = ..., gridSpacing: Optional[Union[float, bool]] = ..., grs: Optional[Union[float, bool]] = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., jitterRadius: Optional[Union[float, bool]] = ..., jr: Optional[Union[float, bool]] = ..., lowerLeftX: Optional[Union[float, bool]] = ..., llx: Optional[Union[float, bool]] = ..., lowerLeftY: Optional[Union[float, bool]] = ..., lly: Optional[Union[float, bool]] = ..., lowerLeftZ: Optional[Union[float, bool]] = ..., llz: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., nucleus: bool = ..., nc: bool = ..., numJitters: Optional[Union[int, bool]] = ..., nj: Optional[Union[int, bool]] = ..., particleName: Optional[Union[str, bool]] = ..., pn: Optional[Union[str, bool]] = ..., sketch: bool = ..., sk: bool = ..., sketchInterval: Optional[Union[int, bool]] = ..., ski: Optional[Union[int, bool]] = ..., textPlacement: bool = ..., tp: bool = ..., upperRightX: Optional[Union[float, bool]] = ..., urx: Optional[Union[float, bool]] = ..., upperRightY: Optional[Union[float, bool]] = ..., ury: Optional[Union[float, bool]] = ..., upperZ: Optional[Union[float, bool]] = ..., urz: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The particle context command creates a particle context. The particle
    context provides an interactive means to create particle
    objects. The particle context command also provides an interactive
    means to set the option values, through the Tool Property Sheet, for
    the "particle" command that the context will issue.

    Args:
        conserve | c: (edit, query) - Conservation of momentum control (between 0 and 1). For smaller values, the field will tend to erase any existing velocity the object has (in other words, will not conserve momentum from frame to frame). A value of 1 (the default) corresponds to the true physical law of conservation of momentum.
        cursorPlacement | cp: (edit, query) - Use the cursor to place the lower left and upper right of the grid.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        grid | gr: (edit, query) - Create a particle grid.
        gridSpacing | grs: (edit, query) - Spacing between particles in the grid.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        jitterRadius | jr: (edit, query) - Max radius from the center to place the particle instances.
        lowerLeftX | llx: (edit, query) - Lower left X position of the particle grid.
        lowerLeftY | lly: (edit, query) - Lower left Y position of the particle grid.
        lowerLeftZ | llz: (edit, query) - Lower left Z position of the particle grid.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        nucleus | nc: (edit, query) - If set true then an nParticle is generated with a nucleus node connection. Otherwise a standard particle is created.
        numJitters | nj: (edit, query) - Number of jitters (instances) per particle.
        particleName | pn: (edit, query) - Particle name.
        sketch | sk: (edit, query) - Create particles in sketch mode.
        sketchInterval | ski: (edit, query) - Interval between particles, when in sketch mode.
        textPlacement | tp: (edit, query) - Use the textfields to specify the lower left and upper right of/ the grid.
        upperRightX | urx: (edit, query) - Upper right X position of the particle grid.
        upperRightY | ury: (edit, query) - Upper right Y position of the particle grid.
        upperZ | urz: (edit, query) - Upper right Z position of the particle grid.
    """
    ...


def editDisplayLayerGlobals(*args, baseId: Optional[Union[int, bool]] = ..., bi: Optional[Union[int, bool]] = ..., currentDisplayLayer: Optional[Union[str, bool]] = ..., cdl: Optional[Union[str, bool]] = ..., mergeType: Optional[Union[int, bool]] = ..., mt: Optional[Union[int, bool]] = ..., useCurrent: bool = ..., uc: bool = ..., query: bool = ...) -> Any:
    r"""
    Edit the parameter values common to all display layers.  Some of these
    paremeters, eg. baseId and mergeType, are stored as preferences and
    some, eg. currentDisplayLayer, are stored in the file.

    Args:
        baseId | bi: (create, query) - Set base layer ID.  This is the number at which new layers start searching for a unique ID.
        currentDisplayLayer | cdl: (create, query) - Set current display layer; ie. the one that all new objects are added to.
        mergeType | mt: (create, query) - Set file import merge type.  Valid values are 0, none, 1, by number, and 2, by name.
        useCurrent | uc: (create, query) - Set whether or not to enable usage of the current display layer as the destination for all new nodes.
    """
    ...


def editDisplayLayerMembers(*args, clear: bool = ..., clr: bool = ..., fullNames: bool = ..., fn: bool = ..., noRecurse: bool = ..., nr: bool = ..., ufeObjects: bool = ..., ufe: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to query and edit membership of display layers.  No
    equivalent 'remove' command is necessary since all objects must be in exactly
    one display layer.  Removing an object from a layer can be accomplished by
    adding it to a different layer.

    Args:
        clear | clr: (create) - Remove all the objects contained in the layer by moving them to the default layer.
        fullNames | fn: (query) - (Query only.) If set then return the full DAG paths of the objects in the layer.  Otherwise return just the name of the object.
        noRecurse | nr: (create, query) - If set then only add selected objects to the display layer.  Otherwise all descendants of the selected objects will also be added.
        ufeObjects | ufe: (query) - (Query only.) If set will return objects that are defined through the UFE interface as well as native Maya objects.
    """
    ...


def exactWorldBoundingBox(*args, calculateExactly: bool = ..., ce: bool = ..., ignoreInvisible: bool = ..., ii: bool = ...) -> Any:
    r"""
    This command figures out an exact-fit bounding box for the
    specified objects (or selected objects if none are specified)
    This bounding box is always in world space.

    Args:
        calculateExactly | ce: (create) - Should the bounding box calculation be exact?
        ignoreInvisible | ii: (create) - Should the bounding box calculation include or exclude invisible objects?
    """
    ...


def excludeObjectDisplayPreset(*args, edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This commands creates named presets of objects that can be used
    with the modelEditor command to exclude objects from beind displayed
    in a viewport.

    Args:
    """
    ...


def expandedSelection(*args, depth: Optional[Union[int, bool]] = ..., d: Optional[Union[int, bool]] = ..., expansionType: Optional[Union[str, bool]] = ..., et: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Examines the current selection list and returns that list, expanded to meet certain
    criteria. See the command flags for the exact criteria that will be used.

    Args:
        depth | d: (create) - Number of steps away from current selection to expand to. A value of 0 will not expand the selection at all.
        expansionType | et: (create) - The type of graph along which to expand the selection. Legal values are: DG : Use the normal DG connections EG : Use the evaluation graph connections SG : Use the scheduling graph connections within the evaluation graph  If the actual selected node is not included in the graph being expanded on, e.g. there is no evaluation node when using the EG type, then the selected node will not appear in the output. If this flag is not specified then the type defaults to DG.
    """
    ...


def filterButterworthCtx(*args, apply: bool = ..., a: bool = ..., cutoffFrequency: Optional[Union[float, bool]] = ..., cof: Optional[Union[float, bool]] = ..., endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., e: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., keepKeysOnFrame: bool = ..., kof: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., samplingRate: Optional[Union[float, bool]] = ..., sr: Optional[Union[float, bool]] = ..., selectedKeys: bool = ..., sk: bool = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., s: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Creates/edits a Butterworth filter context. This context can be used
    to interactively preview/edit the Butterworth filter on a set of
    animation curves.

    Args:
        apply | a: (edit) - When specified, finalizes the current context state and records the command for the operation. This is equivalent to completing the tool action without exiting the current tool context.
        cutoffFrequency | cof: (edit, query) - Specifies the cutoff frequency setting of the Butterworth filter. Default is 7.0.
        endTime | e: (edit, query) - Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        keepKeysOnFrame | kof: (edit, query) - When true, the Butterworth filter will reposition output keys to whole frames for the specified sampling rate.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        samplingRate | sr: (edit, query) - Specifies the sampling rate setting of the Butterworth filter. Default is 30.0.
        selectedKeys | sk: (edit, query) - If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        startTime | s: (edit, query) - Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
    """
    ...


def filterGaussianCtx(*args, apply: bool = ..., a: bool = ..., endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., e: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., sampleCount: Optional[Union[int, bool]] = ..., sc: Optional[Union[int, bool]] = ..., selectedKeys: bool = ..., sk: bool = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., s: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., useQuaternion: bool = ..., uq: bool = ..., width: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., w: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Creates a smooth (gaussian) filter context. This context can ben used
    to interactively preview/edit the smooth (gaussian) filter on a set of
    animation curves.

    Args:
        apply | a: (edit) - When specified, finalizes the current context state and records the command for the operation. This is equivalent to completing the tool action without exiting the current tool context.
        endTime | e: (edit, query) - Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        sampleCount | sc: (edit, query) - This parameter specifies the number of neighbor will be sampled.
        selectedKeys | sk: (edit, query) - If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        startTime | s: (edit, query) - Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
        useQuaternion | uq: (edit, query) - When this is enabled, the filter will first convert the curves (rotation channel curves, 3 sibling requires at the same time) from Euler space to quaternions. Then apply the gaussian filter on it. Convert it back from Quaternions back to Euler space eventually.
        width | w: (edit, query) - This parameter specifies the width of the gaussian kernel shape. Wider width will
    """
    ...


def filterInstances(*args, shapes: bool = ..., s: bool = ..., query: bool = ...) -> Any:
    r"""
    This command filters the selection list to remove duplicate instances
    that refer to the same object/components. If any such instances are
    found they will be merged with the first selected instance.
    
    Returns a string array containing all matching selection items or
    true/false if the query flag is used.

    Args:
        shapes | s: (create) - If this is true then the command will check for an instanced shapes below the selected transform(s) and use them to decide whether the parent transforms should be considered instances. Default is false.
    """
    ...


def filterKeyReducerCtx(*args, apply: bool = ..., a: bool = ..., endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., e: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., keySync: bool = ..., ks: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., precision: Optional[Union[float, bool]] = ..., pre: Optional[Union[float, bool]] = ..., precisionMode: Optional[Union[int, bool]] = ..., pm: Optional[Union[int, bool]] = ..., preserveKeyTangent: Optional[Union[str, bool]] = ..., pkt: Optional[Union[str, bool]] = ..., selectedKeys: bool = ..., sk: bool = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., s: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Creates/edits a KeyReducer filter context. This context can be used
    to interactively preview/edit the KeyReducer filter on a set of
    animation curves.

    Args:
        apply | a: (edit) - When specified, finalizes the current context state and records the command for the operation. This is equivalent to completing the tool action without exiting the current tool context.
        endTime | e: (edit, query) - Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        keySync | ks: (edit, query) - When true, a secondary filter pass is applied that adds a key to sibling curves (X,Y,Z) for each key that is encountered.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        precision | pre: (edit, query) - Defines the precision parameter.  For the Key Reducer filter, this parameter specifies the error limit between the source and output curves. Greater values reduce precision. Lower values increase precision.
        precisionMode | pm: (edit, query) - Specifies the precision mode for the Key Reducer filter. Avaiable modes are:  0: Absolute value. 1: Percentage  Default is 1 (percentage mode).
        preserveKeyTangent | pkt: (edit, multiuse, query) - When specified, keys whose in or out tangent type match the specified type are preserved.  Supported tangent types:  fixed linear flat smooth step clamped plateau stepnext auto
        selectedKeys | sk: (edit, query) - If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        startTime | s: (edit, query) - Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
    """
    ...


def geometryAttrInfo(*args, boundingBox: bool = ..., bb: bool = ..., castToEdges: bool = ..., cte: bool = ..., castToFaces: bool = ..., ctf: bool = ..., castToVerts: bool = ..., ctv: bool = ..., componentTagCategory: bool = ..., ccy: bool = ..., componentTagExpression: Optional[Union[str, bool]] = ..., cex: Optional[Union[str, bool]] = ..., componentTagHash: bool = ..., hsh: bool = ..., componentTagHistory: bool = ..., cth: bool = ..., componentTagHistoryHash: bool = ..., chh: bool = ..., componentTagNames: bool = ..., cnm: bool = ..., components: bool = ..., cmp: bool = ..., deformerChain: bool = ..., dch: bool = ..., elementCount: bool = ..., ec: bool = ..., groupId: Optional[Union[int, bool]] = ..., gid: Optional[Union[int, bool]] = ..., matrix: bool = ..., mtx: bool = ..., nodeChain: bool = ..., nch: bool = ..., originalGeometry: bool = ..., og: bool = ..., outputPlugChain: bool = ..., och: bool = ..., plugChain: bool = ..., pch: bool = ..., pointCount: bool = ..., pc: bool = ..., pointIndices: bool = ..., pi: bool = ..., points: bool = ..., pnt: bool = ..., subsetState: bool = ..., sbs: bool = ...) -> Any:
    r"""
    This command provides information about the geometry in an attribute. This
    command therefore only works on attributes that contain geometry.
    A variety of types of information can be requested, like the number of verts,
    the boundingbox, which componentTags exist, etc.
    
    The requests can be made on a subset of the geometry, either limited by a
    specific groupId or by a componentTag expression. For example, when a componentTag
    expression is used, the requested indices will be the indices that match the
    subset as defined by that expression.

    Args:
        boundingBox | bb: (create) - Returns the bounding box of the geometry
        castToEdges | cte: (create) - Ensures the componentTag expression will be resolved to edge components
        castToFaces | ctf: (create) - Ensures the componentTag expression will be resolved to face components
        castToVerts | ctv: (create) - Ensures the componentTag expression will be resolved to vert components
        componentTagCategory | ccy: (create) - This flag will return the component tag category of the resulting components. Verts are "v", edges are "e", faces are "f". In case the the category can not be determined "unknown" is returned
        componentTagExpression | cex: (create) - Specifies the componentTagExpression we want to query. When specified all answers to the information requests will be limited to the subset of the geometry as is contained in the combination of these componentTags
        componentTagHash | hsh: (create) - This flag will return a unique hash value for the state of all the componentTags contained in the geometry. If a hash is different from before it means that something has changed, either tags have been added/removed/renamed and/or their component contents have been altered.
        componentTagHistory | cth: (create) - This flag will return a description of the componentTags and the nodes in the chain where they were added to the geometry.
        componentTagHistoryHash | chh: (create) - This flag will return a unique hash value for the componentTag history of the geometry in the plug. If a hash is different from before it means that something has changed, either different nodes have created the tags or the contents of the tags have been altered.
        componentTagNames | cnm: (create) - Returns the names of the componentTags on the geometry
        components | cmp: (create) - Returns the components of the geometry
        deformerChain | dch: (create) - This flag will return the list of deformer nodes through which the geometry passes to the specified plug
        elementCount | ec: (create) - Returns the element count of the components
        groupId | gid: (create) - Specifies the groupId we want to query. When specified all answers to the information requests will be limited to the subset of the geometry as is contained in this groupId
        matrix | mtx: (create) - Returns the matrix associated with the geometry
        nodeChain | nch: (create) - This flag will return the list of nodes through which the geometry passes to the specified plug
        originalGeometry | og: (create) - This flag will return the name of a plug on a node upstream (likely at the front end) that is the best candidate to be used as the originalGeometry. This can return an empty plug when none exists.
        outputPlugChain | och: (create) - This flag will return the chain of plugs upstream of the specified plug (including only output plugs)
        plugChain | pch: (create) - This flag will return the chain of plugs upstream of the specified plug (including both input and output plugs)
        pointCount | pc: (create) - Returns the point count of the geometry
        pointIndices | pi: (create) - Returns the indices of the geometry
        points | pnt: (create) - Returns a list of points of the geometry
        subsetState | sbs: (create) - Returns the state of the specified subset -1 means the subset was invalid 0 means the subset contains none of the points of the geometry 1 means the subset contains some (but not all) of the points of the geometry 2 means the subset contains all the points of the geometry
    """
    ...


def getAttr(*args, asString: bool = ..., caching: bool = ..., ca: bool = ..., channelBox: bool = ..., cb: bool = ..., expandEnvironmentVariables: bool = ..., x: bool = ..., keyable: bool = ..., k: bool = ..., lock: bool = ..., l: bool = ..., multiIndices: bool = ..., mi: bool = ..., settable: bool = ..., se: bool = ..., silent: bool = ..., sl: bool = ..., size: bool = ..., s: bool = ..., time: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., t: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., type: bool = ..., typ: bool = ...) -> Any:
    r"""
    This command returns the value of the named object's attribute.
    
    For Ufe attributes, the input attribute string should be
    "<ufe_path_string>.<ufe_attribute_name>".
    
    UI units are used where applicable.
    
    Currently, the types of attributes that can be displayed are:
    
    
     numeric attributes
     string attributes
     matrix attributes
     numeric compound attributes (whose children are all numeric)
     vector array attributes
     double array attributes
     int32 array attributes
     point array attributes
     data component list attributes
     Ufe attributes
    
    
    Other data types cannot be retrieved. No result is returned if the
    attribute contains no data.

    Args:
        asString | asString: (create) - This flag is only valid for enum attributes. It allows you to get the attribute values as strings instead of integer values. Note that the returned string value is dependent on the UI language Maya is running in (about -uiLanguage). Not supported for Ufe attributes.
        caching | ca: (create) - Returns whether the attribute is set to be cached internally Not supported for Ufe attributes.
        channelBox | cb: (create) - Returns whether the attribute is set to show in the Channel Box. Keyable attributes also show in the Channel Box. Not supported for Ufe attributes. The display of Ufe attributes in the Channel Box is controlled using the channelBox command flag -ual/ufeFixedAttrList.
        expandEnvironmentVariables | x: (create) - Expand any environment variable and (tilde characters on UNIX) found in string attributes which are returned. Not supported for Ufe attributes.
        keyable | k: (create) - Returns the keyable state of the attribute. Not supported for Ufe attributes.
        lock | l: (create) - Returns the lock state of the attribute.
        multiIndices | mi: (create) - If the attribute is a multi, this will return a list containing all of the valid indices for the attribute. Not supported for Ufe attributes.
        settable | se: (create) - Returns 1 if this attribute is currently settable by setAttr, 0 otherwise. An attribute is settable if it's not locked and either not connected, or has only keyframed animation. For Ufe attributes an attribute is settable if it's not locked.
        silent | sl: (create) - When evaluating an attribute that is not a numeric or string value, suppress the error message saying that the data cannot be displayed. The attribute will be evaluated even though its data cannot be displayed. This flag does not suppress all error messages, only those that are benign. Not supported for Ufe attributes.
        size | s: (create) - Returns the size of a multi-attribute array.  Returns 1 if non-multi. Not supported for Ufe attributes.
        time | t: (create) - Evaluate the attribute at the given time instead of the current time. Not supported for Ufe attributes.
        type | typ: (create) - Returns the type of data currently in the attribute.  Attributes of simple types such as strings and numerics always contain data, but attributes of complex types (arrays, meshes, etc) may contain no data if none has ever been assigned to them. When this happens the command will return with no result: not an empty string, but no result at all. Attempting to directly compare this non-result to another value or use it in an expression will result in an error, but you can assign it to a variable in which case the variable will be set to the default value for its type (e.g. an empty string for a string variable, zero for an integer variable, an empty array for an array variable). So to be safe when using this flag, always assign its result to a string variable, never try to use it directly.
    """
    ...


def getClassification(*args, satisfies: Optional[Union[str, bool]] = ..., sat: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Returns the classification string for a given node type.
    
    Classification strings look like file pathnames ("shader/reflective" or "texture/2D", for
    example).  Multiple classifications can be combined into a single compound
    classification string by joining the individual classifications with ':'.
    For example, the classification string "shader/reflective:texture/2D" means
    that the node is both a reflective shader and a 2D texture.
    
    The classification string is used to determine how rendering nodes
    are categorized in various UI, such as the Create Render Node and HyperShade
    windows:
    
    
    CategoryClassification String
    2D Textures"texture/2d"
    3D Textures"texture/3d"
    Env Textures"texture/environment"
    Surface Materials"shader/surface"
    Volumetric Materials"shader/volume"
    Displacement Materials"shader/displacement"
    Lights"light"
    General Utilities"utility/general"
    Color Utilities"utility/color
    Particle Utilities"utility/particle"
    Image Planes"imageplane"
    Glow"postprocess/opticalFX"
    
    
    The classification string is also used to determine how Viewport 2.0
    will interpret the node.
    
    
    CategoryClassification String
    Geometry"drawdb/geometry"
    Transform"drawdb/geometry/transform"
    Sub-Scene Object"drawdb/subscene"
    Shader"drawdb/shader"
    Surface Shader"drawdb/shader/surface"

    Args:
        satisfies | sat: (create) - Returns true if the given node type's classification satisfies the classification string which is passed with the flag.  A non-compound classification string A is said to satisfy a non-compound classification string B if A is a subclassification of B (for example, "shaders/reflective" satisfies "shaders").  A compound classification string A satisfies a compound classification string B iff:   every component of A satisfies at least one component of B and  every component of B is satisfied by at least one component of A   Hence, "shader/reflective/phong:texture" satisfies "shader:texture", but "shader/reflective/phong" does not satisfy "shader:texture".
    """
    ...


def graphDollyCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create a dolly context
    for the graph editor.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def graphSelectContext(*args, exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create a selection context for the
    hypergraph editor.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
    """
    ...


def graphTrackCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create a track context
    for the graph editor.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def group(*args, absolute: bool = ..., a: bool = ..., empty: bool = ..., em: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., relative: bool = ..., r: bool = ..., useAsGroup: Optional[Union[str, bool]] = ..., uag: Optional[Union[str, bool]] = ..., world: bool = ..., w: bool = ...) -> Any:
    r"""
    This command groups the specified objects under a new group
    and returns the name of the new group.
    
    If the -em flag is specified, then an empty group (with no
    objects) is created.
    
    If the -w flag is specified then the new group is placed under the
    world, otherwise if -p is specified it is placed under the
    specified node. If neither -w or -p is specified the new group is
    placed under the lowest common group they have in common. (or the
    world if no such group exists)
    
    If an object is grouped with another object that has the same name
    then one of the objects will be renamed by this command.

    Args:
        absolute | a: (create) - preserve existing world object transformations (overall object transformation is preserved by modifying the objects local transformation) [default]
        empty | em: (create) - create an empty group (with no objects in it)
        name | n: (create) - Assign given name to new group node.
        parent | p: (create) - put the new group under the given parent
        relative | r: (create) - preserve existing local object transformations (relative to the new group node)
        useAsGroup | uag: (create) - Use the specified node as the group node. The specified node must be derived from the transform node and must not have any existing parents or children.
        world | w: (create) - put the new group under the world
    """
    ...


def hide(*args, allObjects: bool = ..., all: bool = ..., clearLastHidden: bool = ..., clh: bool = ..., clearSelection: bool = ..., cs: bool = ..., invertComponents: bool = ..., ic: bool = ..., returnHidden: bool = ..., rh: bool = ..., testVisibility: bool = ..., tv: bool = ...) -> Any:
    r"""
    The hide command is used to make objects invisible. If no flags are
    used, the objects specified, or the active objects if none are specified,
    will be made invisible.

    Args:
        allObjects | all: (create) - Make everything invisible (top level objects).
        clearLastHidden | clh: (create) - Clear the last hidden list.
        clearSelection | cs: (create) - Clear selection after the operation.
        invertComponents | ic: (create) - Hide components that are not specified.
        returnHidden | rh: (create) - Hide objects, but also return list of hidden objects.
        testVisibility | tv: (create) - Do not change visibility, just test it (returns 1 is invisible, 2 if visible, 3 if partially visible).
    """
    ...


def hilite(*args, replace: bool = ..., r: bool = ..., toggle: bool = ..., tgl: bool = ..., unHilite: bool = ..., u: bool = ...) -> Any:
    r"""
    Hilites/Unhilites the specified object(s).  Hiliting an object makes
    it possible to select the components of the object.  If no objects
    are specified then the selection list is used.

    Args:
        replace | r: (create) - Hilite the specified objects.  Any objects previously hilited will no longer be hilited.
        toggle | tgl: (create) - Toggle the hilite state of the specified objects.
        unHilite | u: (create) - Remove the specified objects from the hilite list.
    """
    ...


def ikHandleCtx(*args, autoPriorityH: bool = ..., apH: bool = ..., createCurve: bool = ..., ccv: bool = ..., createRootAxis: bool = ..., cra: bool = ..., exists: bool = ..., ex: bool = ..., forceSolverH: bool = ..., fsH: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., numSpans: int = ..., ns: int = ..., parentCurve: bool = ..., pcv: bool = ..., poWeightH: Optional[Union[float, bool]] = ..., pwH: Optional[Union[float, bool]] = ..., priorityH: Optional[Union[int, bool]] = ..., pH: Optional[Union[int, bool]] = ..., rootOnCurve: bool = ..., roc: bool = ..., rootTwistMode: bool = ..., rtm: bool = ..., simplifyCurve: bool = ..., scv: bool = ..., snapCurve: bool = ..., snc: bool = ..., snapHandleH: bool = ..., snH: bool = ..., solverTypeH: Optional[Union[str, bool]] = ..., stH: Optional[Union[str, bool]] = ..., stickyH: Optional[Union[str, bool]] = ..., sH: Optional[Union[str, bool]] = ..., twistType: str = ..., tws: str = ..., weightH: Optional[Union[float, bool]] = ..., wH: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The ikHandle context command (ikHandleCtx) updates parameters of
    ikHandle tool.  The options for the tool will be set to the flags that
    the user specifies.

    Args:
        autoPriorityH | apH: (create, edit, query) - Specifies that this handle's priority is assigned automatically. C: The default is off. Q: When queried, this flag returns an int.
        createCurve | ccv: (create, edit, query) - Specifies if a curve should be automatically created for the ikSplineHandle. The flag is ignored in the ikHandleCtx. C: The default is on.  Q: When queried, this flag returns an int.
        createRootAxis | cra: (edit) - Specifies if a root transform should automatically be created above the joints affected by the ikSplineHandle. This option is used to prevent the root flipping singularity on a motion path. This flag is ignored in the ikHandleCtx. C: The default is off.  Q: When queried, this flag returns an int.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        forceSolverH | fsH: (create, edit, query) - Specifies if the ikSolver is enabled for the ikHandle. C: The default is on.  Q: When queried, this flag returns an int.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        numSpans | ns: (edit) - Specifies the number of spans in the automatically generated curve of the ikSplineHandle. This flag is ignored in the ikHandleCtx. C: The default is 1.  Q: When queried, this flag returns an int.
        parentCurve | pcv: (edit) - Specifies if the curve should automatically be parented to the parent of the first joint affected by the ikSplineHandle. The flag is ignored in the ikHandleCtx. C: The default is on.  Q: When queried, this flag returns an int.
        poWeightH | pwH: (create, edit, query) - Specifies the position/orientation weight of the ikHandle. C: The default is 1. Q: When queried, this flag returns a float.
        priorityH | pH: (create, edit, query) - Specifies the priority of the ikHandle. C: The default is 1. Q: When queried, this flag returns an int.
        rootOnCurve | roc: (edit) - Specifies if the root is locked onto the curve of the ikSplineHandle. This flag is ignored in the ikHandleCtx.  C: The default is on.  Q: When queried, this flag returns an int.
        rootTwistMode | rtm: (edit) - Specifies whether the start joint is allowed to twist or not. If not, then the required twist is distributed over the remaining joints. This applies to all the twist types. This flag is ignored in the ikHandleCtx.  C: The default is off.  Q: When queried, this flag returns an int.
        simplifyCurve | scv: (edit) - Specifies if the ikSplineHandle curve should be simplified. This flag is ignored in the ikHandleCtx. C: The default is on.  Q: When queried, this returns an int.
        snapCurve | snc: (edit) - Specifies if the curve should automatically snap to the first joint affected by the ikSplineHandle. This flag is ignored in the ikHandleCtx. C: The default is off.  Q: When queried, this flag returns an int.
        snapHandleH | snH: (create, edit, query) - Specifies if the ikHandle snapping is on. C: The default is on. Q: When queried, this flag returns an int.
        solverTypeH | stH: (create, edit, query) - Lists what ikSolver is being used. The ikSplineSolver may not be selected. To use an ikSplineSolver use the ikSplineHandleCtx command.  C: The default solver is the default set by the user preferences. Q: When queried, this flag returns a string.
        stickyH | sH: (create, edit, query) - Specifies if the ikHandle is sticky or not. Valid strings are "sticky" and "off". C: The default is "off". Q: When queried, this flag returns a string.
        twistType | tws: (edit) - Specifies the type of interpolation to be used by the ikSplineHandle. This flag is ignored in the ikHandleCtx. The interpolation options are "linear", "easeIn", "easeOut", and "easeInOut".  C: The default is "linear".  Q: When queried, this flag returns a string.
        weightH | wH: (create, edit, query) - Specifies the weight of the ikHandle. C: The default is 1. Q: When queried, this flag returns a float.
    """
    ...


def ikSplineHandleCtx(*args, autoPriorityH: bool = ..., apH: bool = ..., createCurve: bool = ..., ccv: bool = ..., createRootAxis: bool = ..., cra: bool = ..., exists: bool = ..., ex: bool = ..., forceSolverH: bool = ..., fsH: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., numSpans: int = ..., ns: int = ..., parentCurve: bool = ..., pcv: bool = ..., poWeightH: Optional[Union[float, bool]] = ..., pwH: Optional[Union[float, bool]] = ..., priorityH: Optional[Union[int, bool]] = ..., pH: Optional[Union[int, bool]] = ..., rootOnCurve: bool = ..., roc: bool = ..., rootTwistMode: bool = ..., rtm: bool = ..., simplifyCurve: bool = ..., scv: bool = ..., snapCurve: bool = ..., snc: bool = ..., snapHandleH: bool = ..., snH: bool = ..., solverTypeH: Optional[Union[str, bool]] = ..., stH: Optional[Union[str, bool]] = ..., stickyH: Optional[Union[str, bool]] = ..., sH: Optional[Union[str, bool]] = ..., twistType: str = ..., tws: str = ..., weightH: Optional[Union[float, bool]] = ..., wH: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The ikSplineHandle context command (ikSplineHandleCtx) updates parameters of
    ikSplineHandle tool.  The options for the tool will be set to the flags
    the user specifies.

    Args:
        autoPriorityH | apH: (create, edit, query) - Specifies that this handle's priority is assigned automatically. C: The default is off. Q: When queried, this flag returns an int.
        createCurve | ccv: (create, edit, query) - Specifies if a curve should be automatically created for the ikSplineHandle.  C: The default is on.  Q: When queried, this flag returns an int.
        createRootAxis | cra: (edit) - Specifies if a root transform should automatically be created above the joints affected by the ikSplineHandle. This option is used to prevent the root flipping singularity on a motion path.  C: The default is off.  Q: When queried, this flag returns an int.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        forceSolverH | fsH: (create, edit, query) - Specifies if the ikSolver is enabled for the ikHandle. C: The default is on.  Q: When queried, this flag returns an int.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        numSpans | ns: (edit) - Specifies the number of spans in the automatically generated curve of the ikSplineHandle.  C: The default is 1.  Q: When queried, this flag returns an int.
        parentCurve | pcv: (edit) - Specifies if the curve should automatically be parented to the parent of the first joint affected by the ikSplineHandle.  C: The default is on.  Q: When queried, this flag returns an int.
        poWeightH | pwH: (create, edit, query) - Specifies the position/orientation weight of the ikHandle. C: The default is 1. Q: When queried, this flag returns a float.
        priorityH | pH: (create, edit, query) - Specifies the priority of the ikHandle. C: The default is 1. Q: When queried, this flag returns an int.
        rootOnCurve | roc: (edit) - Specifies if the root is locked onto the curve of the ikSplineHandle.  C: The default is on.  Q: When queried, this flag returns an int.
        rootTwistMode | rtm: (edit) - Specifies whether the start joint is allowed to twist or not. If not, then the required twist is distributed over the remaining joints. This applies to all the twist types. C: The default is off.  Q: When queried, this flag returns an int.
        simplifyCurve | scv: (edit) - Specifies if the ikSplineHandle curve should be simplified.  C: The default is on.  Q: When queried, this returns an int.
        snapCurve | snc: (edit) - Specifies if the curve should automatically snap to the first joint affected by the ikSplineHandle.  C: The default is off.  Q: When queried, this flag returns an int.
        snapHandleH | snH: (create, edit, query) - Specifies if the ikHandle snapping is on. This flag is ignored for the ikSplineSolver. C: The default is on. Q: When queried, this flag returns an int.
        solverTypeH | stH: (create, edit, query) - Lists what ikSolver is being used. For the ikSplineContext the solver can only be the ikSplineSolver and this flag is ignored.  C: The default solver is the ikSplineSolver. Q: When queried, this flag returns a string.
        stickyH | sH: (create, edit, query) - Specifies if the ikHandle is sticky or not. Valid strings are "sticky" and "off". This flag is ignored for the ikSplineSolver. C: The default is "off". Q: When queried, this flag returns a string.
        twistType | tws: (edit) - Specifies the type of interpolation to be used by the ikSplineHandle.  The interpolation options are "linear", "easeIn", "easeOut", and "easeInOut". C: The default is "linear".  Q: When queried, this flag returns a string.
        weightH | wH: (create, edit, query) - Specifies the weight of the ikHandle. This flag is ignored in the ikSplineHandleCtx. C: The default is 1. Q: When queried, this flag returns a float.
    """
    ...


def inheritTransform(*args, off: bool = ..., on: bool = ..., preserve: bool = ..., p: bool = ..., toggle: bool = ..., tgl: bool = ..., query: bool = ...) -> Any:
    r"""
    This command toggles the inherit state of an object. If this
    flag is off the object will not inherit transformations from
    its parent. In other words transformations applied to the
    parent node will not affect the object and it will act as
    though it is under the world.
    
    If the -p flag is specified then the object's transformation will
    be modified to compensate when changing the inherit flag so the
    object will not change its world-space location.

    Args:
        off | off: (create, query) - turn off inherit state for the given object(s)
        on | on: (create, query) - turn on inherit state for the given object(s)
        preserve | p: (create, query) - preserve the objects world-space position by modifying the object(s) transformation matrix.
        toggle | tgl: (create, query) - toggle the inherit state for the given object(s) (default if no flags are given) -on turn on inherit state for the given object(s) -off turn off inherit state for the given object(s)
    """
    ...


def insertJointCtx(*args, exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The command will create an insert joint context. The insert joint tool
    inserts joints into an existing chain of joints.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
    """
    ...


def insertKeyCtx(*args, breakdown: bool = ..., bd: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., preserveTangent: bool = ..., pt: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context which may be used to insert keys
    within the graph editor

    Args:
        breakdown | bd: (edit, query) - Specifies whether or not to create breakdown keys
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        preserveTangent | pt: (edit, query) - Specifies whether or not to preserve tangent
    """
    ...


def instance(*args, leaf: bool = ..., lf: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., smartTransform: bool = ..., st: bool = ...) -> Any:
    r"""
    Instancing is a way of making the same object appear twice in the
    scene. This is accomplished by creation of a new transform node
    that points to an exisiting object. Changes to the transform
    are independent but changes to the "instanced" object affect
    all instances since the node is shared.
    
    If no objects are given, then the selected list is instanced.
    When an object is instanced a  new transform node is created
    that points to the selected object.
    
    The smart transform feature allows instance to transform newly
    instanced objects based on previous transformations between instances.
    
    Example: Instance an object and move it to a new location.  Instance
    it again with the smart transform flag.  It should have moved once
    again the distance you had previously moved it.
    
    Note: changing the selected list between smart instances will cause
    the transform information to be deleted.
    
    It returns a list of the new objects created by the instance operation.
    
    See also: duplicate

    Args:
        leaf | lf: (create) - Instances leaf-level objects. Acts like duplicate except leaf-level objects are instanced.
        name | n: (create) - Name to give new instance
        smartTransform | st: (create) - Transforms instances item based on movements between transforms
    """
    ...


def instanceable(*args, allow: bool = ..., a: bool = ..., recursive: bool = ..., r: bool = ..., shape: bool = ..., s: bool = ..., query: bool = ...) -> Any:
    r"""
    Flags one or more DAG nodes so that they can (or cannot) be instanced.
    This command sets an internal state on the specified DAG nodes which is
    checked whenever Maya attempts an instancing operation.
    If no node names are provided on the command line then the current selection list is used.
    
    
    Sets are automatically expanded to their constituent objects. Nodes which are already
    instanced (or have children which are already instanced) cannot be marked as non-instancable.

    Args:
        allow | a: (create, query) - Specifies the new instanceable state for the node. Specify true to allow the node to be instanceable, and false to prevent it from being instanced. The default is true (i.e. nodes can be instanced by default).
        recursive | r: (create) - Can be specified with the -allow flag in create or edit mode to recursively apply the -allow setting to all non-shape children of the selected node(s). To also affect shapes, also specify the -shape flag along with -recursive.
        shape | s: (create) - Can be specified with the -allow flag in create or edit mode to apply the -allow setting to all shape children of the selected node(s). This flag can be specified in conjunction with the -recursive flag.
    """
    ...


def instancer(*args, addObject: bool = ..., a: bool = ..., cycle: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., cycleStep: Optional[Union[float, bool]] = ..., cs: Optional[Union[float, bool]] = ..., cycleStepUnits: Optional[Union[str, bool]] = ..., csu: Optional[Union[str, bool]] = ..., index: Optional[Union[int, bool]] = ..., i: Optional[Union[int, bool]] = ..., levelOfDetail: Optional[Union[str, bool]] = ..., lod: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., object: Optional[Union[str, bool]] = ..., obj: Optional[Union[str, bool]] = ..., objectPosition: Optional[Union[str, bool]] = ..., op: Optional[Union[str, bool]] = ..., objectRotation: Optional[Union[str, bool]] = ..., objectScale: Optional[Union[str, bool]] = ..., os: Optional[Union[str, bool]] = ..., pointDataSource: bool = ..., pds: bool = ..., removeObject: bool = ..., rm: bool = ..., rotationOrder: Optional[Union[str, bool]] = ..., ro: Optional[Union[str, bool]] = ..., rotationUnits: Optional[Union[str, bool]] = ..., ru: Optional[Union[str, bool]] = ..., valueName: Optional[Union[str, bool]] = ..., vn: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to create a instancer node and set the proper
    attributes in the node.

    Args:
        addObject | a: (create, edit) - This flag indicates that objects specified by the -object flag will be added to the instancer node as instanced objects.
        cycle | c: (create, edit, query) - This flag sets or queries the cycle attribute for the instancer node. The options are "none" or "sequential".  The default is "none".
        cycleStep | cs: (create, edit, query) - This flag sets or queries the cycle step attribute for the instancer node.  This attribute indicates the size of the step in frames or seconds (see cycleStepUnit).
        cycleStepUnits | csu: (create, edit, query) - This flag sets or queries the cycle step unit attribute for the instancer node.  The options are "frames" or "seconds".  The default is "frames".
        index | i: (query) - This flag is used to query the name of the ith instanced object.
        levelOfDetail | lod: (create, edit, query) - This flag sets or queries the level of detail of the instanced objects.  The options are "geometry", "boundingBox", "boundingBoxes".  The default is "geometry".
        name | n: (create, query) - This flag sets or queries the name of the instancer node.
        object | obj: (create, edit, multiuse, query) - This flag indicates which objects will be add/removed from the list of instanced objects.  The flag is used in conjuction with the -add and -remove flags.  If neither of these flags is specified on the command line then -add is assumed.
        objectPosition | op: (query) - This flag queries the given objects position.  This object can be any instanced object or sub-object.
        objectRotation | objectRotation: (query) - This flag queries the given objects rotation.  This object can be any instanced object or sub-object.
        objectScale | os: (query) - This flag queries the given objects scale.  This object can be any instanced object or sub-object.
        pointDataSource | pds: (query) - This flag is used to query the source node supply the data for the input points.
        removeObject | rm: (edit) - This flag indicates that objects specified by the -object flag will be removed from the instancer node as instanced objects.
        rotationOrder | ro: (create, edit, query) - This flag specifies the rotation order associated with the rotation flag.  The options are XYZ, XZY, YXZ, YZX, ZXY, or ZYX.  By default the attribute is XYZ.
        rotationUnits | ru: (create, edit, query) - This flag specifies the rotation units associated with the rotation flag.  The options are degrees or radians.  By default the attribute is degrees.
        valueName | vn: (query) - This flag is used to query the value(s) of the array associated with the given name.  If the -index flag is used in conjuction with this flag then the ith value will be returned.  Otherwise, the entire array will be returned.
    """
    ...


def isConnected(*args, ignoreUnitConversion: bool = ..., iuc: bool = ...) -> Any:
    r"""
    The isConnected command is used to check if two plugs are
    connected in the dependency graph. The return value is false
    if they are not and true if they are.
    
    The first string specifies the source plug to check for connection.
    The second one specifies the destination plug to check for connection.

    Args:
        ignoreUnitConversion | iuc: (create) - In looking for connections, skip past unit conversion nodes.
    """
    ...


def isDirty(*args, connection: bool = ..., c: bool = ..., datablock: bool = ..., d: bool = ...) -> Any:
    r"""
    The isDirty command is used to check if a plug is dirty.  The
    return value is 0 if it is not and 1 if it is.  If more than one plug
    is specified then the result is the logical "or" of all objects
    (ie. returns 1 if *any* of the plugs are dirty).

    Args:
        connection | c: (create) - Check the connection of the plug (default).
        datablock | d: (create) - Check the datablock entry for the plug.
    """
    ...


def isolateSelect(*args, addDagObject: str = ..., ado: str = ..., addSelected: bool = ..., addSelectedObjects: bool = ..., aso: bool = ..., loadSelected: bool = ..., ls: bool = ..., removeDagObject: str = ..., rdo: str = ..., removeSelected: bool = ..., rs: bool = ..., state: bool = ..., s: bool = ..., update: bool = ..., u: bool = ..., viewObjects: bool = ..., vo: bool = ..., query: bool = ...) -> Any:
    r"""
    This command turns on/off isolate select mode in a specified modeling
    view, specified as the argument. Isolate select mode is a display mode
    where the currently selected objects are added to a list and only
    those objects are displayed in the view. It allows for selective
    viewing of specific objects and object components.

    Args:
        addDagObject | ado: () - Add the specified object to the set of objects to be displayed in the view.
        addSelected | addSelected: () - Add the currently active objects to the set of objects to be displayed in the view.
        addSelectedObjects | aso: () - Add selected objects to the set of objects to be displayed in the view. This flag differs from addSelected in that it will ignore selected components and add the entire object.
        loadSelected | ls: () - Replace the objects being displayed with the currently active objects.
        removeDagObject | rdo: () - Remove the specified object from the set of objects to be displayed in the view.
        removeSelected | rs: () - Remove the currently active objects to the set of objects to be displayed in the view.
        state | s: (query) - Turns isolate select mode on/off.
        update | u: () - Update the view's list of objects due to a change to the set of objects to be displayed.
        viewObjects | vo: (query) - Returns the name (if any) of the objectSet which contains the list of objects visible in the view if isolate select mode is on. If isolate select mode is off, an empty string is returned.
    """
    ...


def jointCtx(*args, autoJointOrient: Optional[Union[str, bool]] = ..., ajo: Optional[Union[str, bool]] = ..., autoPriorityH: bool = ..., apH: bool = ..., createIKHandle: bool = ..., ikh: bool = ..., degreeOfFreedomJ: Optional[Union[str, bool]] = ..., dJ: Optional[Union[str, bool]] = ..., exists: bool = ..., ex: bool = ..., forceSolverH: bool = ..., fsH: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., jointAutoLimits: bool = ..., jal: bool = ..., jointOrientationJ: Optional[Union[Tuple[float, float, float], bool]] = ..., joJ: Optional[Union[Tuple[float, float, float], bool]] = ..., largeBoneLength: Optional[Union[float, bool]] = ..., lbl: Optional[Union[float, bool]] = ..., largeBoneRadius: Optional[Union[float, bool]] = ..., lbr: Optional[Union[float, bool]] = ..., poWeightH: Optional[Union[float, bool]] = ..., pwH: Optional[Union[float, bool]] = ..., priorityH: Optional[Union[int, bool]] = ..., pH: Optional[Union[int, bool]] = ..., scaleCompensateJ: bool = ..., scJ: bool = ..., scaleJ: Optional[Union[Tuple[float, float, float], bool]] = ..., sJ: Optional[Union[Tuple[float, float, float], bool]] = ..., scaleOrientationJ: Optional[Union[Tuple[float, float, float], bool]] = ..., soJ: Optional[Union[Tuple[float, float, float], bool]] = ..., secondaryAxisOrient: Optional[Union[str, bool]] = ..., sao: Optional[Union[str, bool]] = ..., smallBoneLength: Optional[Union[float, bool]] = ..., sbl: Optional[Union[float, bool]] = ..., smallBoneRadius: Optional[Union[float, bool]] = ..., sbr: Optional[Union[float, bool]] = ..., snapHandleH: bool = ..., snH: bool = ..., solverTypeH: Optional[Union[str, bool]] = ..., stH: Optional[Union[str, bool]] = ..., stickyH: Optional[Union[str, bool]] = ..., sH: Optional[Union[str, bool]] = ..., symmetry: bool = ..., sym: bool = ..., symmetryAxis: Optional[Union[str, bool]] = ..., sa: Optional[Union[str, bool]] = ..., variableBoneSize: bool = ..., vbs: bool = ..., weightH: Optional[Union[float, bool]] = ..., wH: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The joint context command (jointCtx) updates the parameters of the
    joint tool. The options for the tool will be set by the flags the user
    specifies.

    Args:
        autoJointOrient | ajo: (create, edit, query) - Specifies the joint orientation. Valid string choices are permutations of the axes; "none", "xyz", "yzx", "zxy", "xzy", "yxz", "zyx". The first letter determines which axis is aligned with the bone. C: The default is "xyz". Q: When queried, this flag returns a string.
        autoPriorityH | apH: (create, edit, query) - Specifies if the ikHandle's priority is assigned automatically. C: The default is off. Q: When queried, this flag returns an int.
        createIKHandle | ikh: (create, edit, query) - Enables the joint tool to create an ikHandle when the tool is completed. C: The default is off. Q: When queried, this flag returns an int.
        degreeOfFreedomJ | dJ: (create, edit, query) - Specifies the degrees of freedom for all of the joints created by the tool. Valid string choices are the free axes; "x", "y", "z", "xy", "xz", "yz", "xyz", and "none". C: The default is "xyz". Q: When queried, this flag returns a string.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        forceSolverH | fsH: (create, edit, query) - Specifies if the ikSolver for the ikHandle is enabled. C: The default is on. Q: When queried, this flag returns an int.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        jointAutoLimits | jal: (create, edit, query) - Automatically computes the joint limits based on the kind of joint created.  C: The default is off. Q: When queried, this flag returns an int.
        jointOrientationJ | joJ: (create, edit, query) - Sets the orientation of the joints created by the tool. If autoJointOrient in on, these values will be ignored. C: The default is 0 0 0. Q: When queried, this flag returns an array of three floats.
        largeBoneLength | lbl: (create, edit, query) - Specifies the length above which bones should be assigned the largeBoneRadius.
        largeBoneRadius | lbr: (create, edit, query) - Specifies the radius for bones whose length is above the largeBoneLength
        poWeightH | pwH: (create, edit, query) - Specifies the position/orientation weight of the ikHandle. C: The default is 1. Q: When queried, this flag returns a float.
        priorityH | pH: (create, edit, query) - Specifies the priority of the ikHandle. C: The default is on. Q: When queried, this flag returns an int.
        scaleCompensateJ | scJ: (create, edit, query) - Specifies if scale compensate is enabled. C: The default is on. Q: When queried, this flag returns an int.
        scaleJ | sJ: (create, edit, query) - Sets the scale for the joints created by the tool. C: The default is 1 1 1. Q: When queried, this flag returns an array of three floats.
        scaleOrientationJ | soJ: (create, edit, query) - Sets the current value for the scale orientation. If autoJointOrient in on, these values will be ignored. C: The default is 0 0 0. Q: When queried, this flag returns an array of three floats.
        secondaryAxisOrient | sao: (create, edit, query) - Specifies the orientation of the secondary rotate axis. Valid string choices are: "xup", "xdown", "yup", "ydown", "zup", "zdown", "none".
        smallBoneLength | sbl: (create, edit, query) - Specifies the length below which bones should be assigned the smallBoneRadius.
        smallBoneRadius | sbr: (create, edit, query) - Specifies the radius for bones whose length is below the smallBoneLength.
        snapHandleH | snH: (create, edit, query) - Sepcifies if snapping is enabled for the ikHandle.  C: The default is on. Q: When queried, this flag returns an int.
        solverTypeH | stH: (create, edit, query) - Sets the name of the solver to use with the ikHandle.  C: The default is the solver set to the default in the user preferences. Q: When queried, this flag returns a string.
        stickyH | sH: (create, edit, query) - Specifies if the ikHandle is sticky or not. If "sticky" is passed then the ikHandle will be sticky. If "off" is used then ikHandle stickiness will be turned off. C: The default is "off". Q: When queried, this flag returns a string.
        symmetry | sym: (create, edit, query) - Automaticaly create a symmetry joint based if symmetry is on.  C: The default is off. Q: When queried, this flag returns an int.
        symmetryAxis | sa: (create, edit, query) - Automaticaly create a symmetry joint use x, y , z axis or combination to do the symmetry.  C: The default is x. Q: When queried, this flag returns a string.
        variableBoneSize | vbs: (create, edit, query) - Specifies whether or not variable bone length and radius settings should be used.
        weightH | wH: (create, edit, query) - Specifies the weight of the ikHandle. The weight is relative to the other ikHandles in the scene. C: The default is 1. Q: When queried, this flag returns a float.
    """
    ...


def keyframeRegionCurrentTimeCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context which may be used to change current time
    within the keyframe region of the dope sheet editor.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def keyframeRegionDirectKeyCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., option: Optional[Union[str, bool]] = ..., o: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context which may be used to directly manipulate keyframes
    within the dope sheet editor

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        option | o: (create) - Valid values are "move," "insert," "over," and "segmentOver." When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to make room for the segment.
    """
    ...


def keyframeRegionDollyCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create a dolly context
    for the dope sheet editor.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def keyframeRegionInsertKeyCtx(*args, breakdown: bool = ..., bd: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context which may be used to insert keys
    within the keyframe region of the dope sheet editor

    Args:
        breakdown | bd: (edit, query) - Specifies whether or not to create breakdown keys
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def keyframeRegionMoveKeyCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., option: Optional[Union[str, bool]] = ..., o: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context which may be used to move keyframes
    within the keyframe region of the dope sheet editor

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        option | o: (create, edit, query) - Valid values are "move," "insert," "over," and "segmentOver". Specifies the keyframe -option to use.  When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to make room for the segment.
    """
    ...


def keyframeRegionScaleKeyCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., scaleSpecifiedKeys: bool = ..., ssk: bool = ..., type: str = ..., typ: str = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context which may be used to scale keyframes
    within the keyframe region of the dope sheet editor

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        scaleSpecifiedKeys | ssk: (edit, query) - Determines if only the specified keys should be scaled. If false, the non-selected keys will be adjusted during the scale. The default is true.
        type | typ: (edit) - rect | manip Specifies the type of scale manipulator to use
    """
    ...


def keyframeRegionSelectKeyCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context which may be used to select keyframes
    within the keyframe region of the dope sheet editor

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def keyframeRegionSetKeyCtx(*args, breakdown: bool = ..., bd: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context which may be used to set keys
    within the keyframe region of the dope sheet editor

    Args:
        breakdown | bd: (edit, query) - Specifies whether or not to create breakdown keys
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def keyframeRegionTrackCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create a track context
    for the dope sheet editor.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def lassoContext(*args, drawClosed: bool = ..., dc: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Creates a context to perform selection via a "lasso".  Use for
    irregular selection regions, where the "marquee-style" select
    of the "selectContext" is inappropriate.

    Args:
        drawClosed | dc: (create, edit, query) - Turns the closed display of the lasso on/off.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def latticeDeformKeyCtx(*args, envelope: Optional[Union[float, bool]] = ..., ev: Optional[Union[float, bool]] = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., latticeColumns: Optional[Union[int, bool]] = ..., lc: Optional[Union[int, bool]] = ..., latticeRows: Optional[Union[int, bool]] = ..., lr: Optional[Union[int, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., scaleLatticePts: bool = ..., slp: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context which may be used to
    deform key frames with lattice manipulator.  This context
    only works in the graph editor.

    Args:
        envelope | ev: (edit, query) - Specifies the influence of the lattice.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        latticeColumns | lc: (edit, query) - Specifies the number column points the lattice contains.
        latticeRows | lr: (edit, query) - Specifies the number of rows the lattice contains.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        scaleLatticePts | slp: (edit, query) - Specifies if the selected lattice points should scale around the pick point. If this value is false the the default operation is 'move'
    """
    ...


def license(*args, borrow: bool = ..., b: bool = ..., info: bool = ..., i: bool = ..., isBorrowed: bool = ..., ib: bool = ..., isExported: bool = ..., ie: bool = ..., isTrial: bool = ..., it: bool = ..., licenseMethod: bool = ..., lm: bool = ..., productChoice: bool = ..., pc: bool = ..., r: bool = ..., showBorrowInfo: bool = ..., sbi: bool = ..., showProductInfoDialog: bool = ..., spi: bool = ..., status: bool = ..., s: bool = ..., usage: bool = ..., u: bool = ...) -> Any:
    r"""
    This command displays version information about the application if it is
    executed without flags.  If one of the above flags is specified
    then the specified version information is returned.

    Args:
        borrow | b: (create) - This flag is obsolete and no longer supported.
        info | i: (create) - This flag is obsolete and no longer supported.
        isBorrowed | ib: (create) - This flag is obsolete and no longer supported.
        isExported | ie: (create) - This flag is obsolete and no longer supported.
        isTrial | it: (create) - This flag is obsolete and no longer supported.
        licenseMethod | lm: (create) - This flag is obsolete and no longer supported.
        productChoice | pc: (create) - This flag is obsolete and no longer supported.
        r | r: (create) - This flag is obsolete and no longer supported.
        showBorrowInfo | sbi: (create) - This flag is obsolete and no longer supported.
        showProductInfoDialog | spi: (create) - Show the Product Information Dialog
        status | s: (create) - This flag is obsolete and no longer supported.
        usage | u: (create) - This flag is obsolete and no longer supported.
    """
    ...


def listAttr(*args, array: bool = ..., a: bool = ..., attributeType: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., caching: bool = ..., ca: bool = ..., category: Optional[Union[str, bool]] = ..., ct: Optional[Union[str, bool]] = ..., changedSinceFileOpen: bool = ..., cfo: bool = ..., channelBox: bool = ..., cb: bool = ..., connectable: bool = ..., c: bool = ..., extension: bool = ..., ex: bool = ..., fromPlugin: bool = ..., fp: bool = ..., fullNodeName: bool = ..., fnn: bool = ..., hasData: bool = ..., hd: bool = ..., hasNullData: bool = ..., hnd: bool = ..., inUse: bool = ..., iu: bool = ..., keyable: bool = ..., k: bool = ..., leaf: bool = ..., lf: bool = ..., locked: bool = ..., l: bool = ..., multi: bool = ..., m: bool = ..., nodeName: bool = ..., nn: bool = ..., output: bool = ..., o: bool = ..., ramp: bool = ..., ra: bool = ..., read: bool = ..., r: bool = ..., readOnly: bool = ..., ro: bool = ..., scalar: bool = ..., s: bool = ..., scalarAndArray: bool = ..., sa: bool = ..., settable: bool = ..., se: bool = ..., shortNames: bool = ..., sn: bool = ..., string: Optional[Union[str, bool]] = ..., st: Optional[Union[str, bool]] = ..., unlocked: bool = ..., u: bool = ..., usedAsFilename: bool = ..., uf: bool = ..., userDefined: bool = ..., ud: bool = ..., visible: bool = ..., v: bool = ..., write: bool = ..., w: bool = ...) -> Any:
    r"""
    This command lists the attributes of a node.  If no flags are specified
    all attributes are listed.

    Args:
        array | a: (create) - only list array (not multi) attributes
        attributeType | at: (create, multiuse) - Return attributes of a particular type.
        caching | ca: (create) - only show attributes that are cached internally
        category | ct: (create, multiuse) - only show attributes belonging to the given category. Category string can be a regular expression.
        changedSinceFileOpen | cfo: (create) - Only list the attributes that have been changed since the file they came from was opened. Typically useful only for objects/attributes coming from referenced files.
        channelBox | cb: (create) - only show non-keyable attributes that appear in the channelbox
        connectable | c: (create) - only show connectable attributes
        extension | ex: (create) - list user-defined attributes for all nodes of this type (extension attributes)
        fromPlugin | fp: (create) - only show attributes that were created by a plugin
        fullNodeName | fnn: (create) - Return full node name in result.
        hasData | hd: (create) - list only attributes that have data (all attributes except for message attributes)
        hasNullData | hnd: (create) - list only attributes that have null data. This will list all attributes that have data (see hasData flag) but the data value is uninitialized. A common example where an attribute may have null data is when a string attribute is created but not yet assigned an initial value. Similarly array attribute data is often null until it is initialized.
        inUse | iu: (create) - only show attributes that are currently marked as in use. This flag indicates that an attribute affects the scene data in some way. For example it has a non-default value or it is connected to another attribute.  This is the general concept though the precise implementation is subject to change.
        keyable | k: (create) - only show attributes that can be keyframed
        leaf | lf: (create) - Only list the leaf-level name of the attribute. controlPoints[44].xValue would be listed as "xValue".
        locked | l: (create) - list only attributes which are locked
        multi | m: (create) - list each currently existing element of a multi-attribute
        nodeName | nn: (create) - Return node name in result.
        output | o: (create) - List only the attributes which are numeric or which are compounds of numeric attributes.
        ramp | ra: (create) - list only attributes which are ramps
        read | r: (create) - list only attributes which are readable
        readOnly | ro: (create) - List only the attributes which are readable and not writable.
        scalar | s: (create) - only list scalar numerical attributes
        scalarAndArray | sa: (create) - only list scalar and array attributes
        settable | se: (create) - list attribute which are settable
        shortNames | sn: (create) - list short attribute names (default is to list long names)
        string | st: (create, multiuse) - List only the attributes that match the other criteria AND match the string(s) passed from this flag. String can be a regular expression.
        unlocked | u: (create) - list only attributes which are unlocked
        usedAsFilename | uf: (create) - list only attributes which are designated to be treated as filenames
        userDefined | ud: (create) - list user-defined (dynamic) attributes
        visible | v: (create) - only show visible or non-hidden attributes
        write | w: (create) - list only attributes which are writable
    """
    ...


def listAttrPatterns(*args, patternType: bool = ..., pt: bool = ..., verbose: bool = ..., v: bool = ...) -> Any:
    r"""
    Attribute patterns are plain text descriptions of an entire Maya attribute forest. ("forest"
    because there could be an arbitrary number of root level attributes, it's not restricted to
    having a single common parent though in general that practice is a good idea.)
    This command lists the various pattern types available, usually created via plugin, as well as
    any specific patterns that have already been instantiated. A pattern type is a thing that knows
    how to take some textual description of an attribute tree, e.g. XML or plaintext, and convert it
    into an attribute pattern that can be applied to any node or node type in Maya.

    Args:
        patternType | pt: (create) - If turned on then show the list of pattern types rather than actual instantiated patterns.
        verbose | v: (create) - If turned on then show detailed information about the patterns or pattern types. The same list of instance or pattern names is returned as for the non-verbose case.
    """
    ...


def listConnections(*args, connections: bool = ..., c: bool = ..., destination: bool = ..., d: bool = ..., exactType: bool = ..., et: bool = ..., fullNodeName: bool = ..., fnn: bool = ..., plugs: bool = ..., p: bool = ..., shapes: bool = ..., sh: bool = ..., skipConversionNodes: bool = ..., scn: bool = ..., source: bool = ..., s: bool = ..., type: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This command returns a list of all attributes/objects of
    a specified type that are connected to the given object(s).
    If no objects are specified then the command lists the connections
    on selected nodes.

    Args:
        connections | c: (create) - If true, return both attributes involved in the connection. The one on the specified object is given first.  Default false.
        destination | d: (create) - Give the attributes/objects that are on the "destination" side of connection to the given object.  Default true.
        exactType | et: (create) - When set to true, -t/type only considers node of this exact type. Otherwise, derived types are also taken into account.
        fullNodeName | fnn: (create) - Return full node name in result.
        plugs | p: (create) - If true, return the connected attribute names; if false, return the connected object names only.  Default false;
        shapes | sh: (create) - Actually return the shape name instead of the transform when the shape is "selected".  Default false.
        skipConversionNodes | scn: (create) - If true, skip over unit conversion nodes and return the node connected to the conversion node on the other side.  Default false.
        source | s: (create) - Give the attributes/objects that are on the "source" side of connection to the given object.  Default true.
        type | t: (create) - If specified, only take objects of a specified type.
    """
    ...


def listHistory(*args, allConnections: bool = ..., ac: bool = ..., allFuture: bool = ..., af: bool = ..., allGraphs: bool = ..., ag: bool = ..., breadthFirst: bool = ..., bf: bool = ..., fastIteration: bool = ..., fi: bool = ..., fullNodeName: bool = ..., fnn: bool = ..., future: bool = ..., f: bool = ..., futureLocalAttr: bool = ..., fl: bool = ..., futureWorldAttr: bool = ..., fw: bool = ..., groupLevels: bool = ..., gl: bool = ..., historyAttr: bool = ..., ha: bool = ..., interestLevel: Optional[Union[int, bool]] = ..., il: Optional[Union[int, bool]] = ..., leaf: bool = ..., lf: bool = ..., levels: Optional[Union[int, bool]] = ..., lv: Optional[Union[int, bool]] = ..., pruneDagObjects: bool = ..., pdo: bool = ..., query: bool = ...) -> Any:
    r"""
    This command traverses backwards or forwards in the graph from
    the specified node and returns all of the nodes whose construction
    history it passes through. The construction history consists of
    connections to specific attributes of a node defined as the
    creators and results of the node's main data, eg. the curve for
    a Nurbs Curve node.
    
    For information on history connections through specific plugs use
    the "listConnections" command first to find where the history begins
    then use this command on the resulting node.

    Args:
        allConnections | ac: (create) - If specified, the traversal that searches for the history or future will not restrict its traversal across nodes to only dependent plugs. Thus it will reach all upstream nodes (or all downstream nodes for f/future).
        allFuture | af: (create) - If listing the future, list all of it. Otherwise if a shape has an attribute that represents its output geometry data, and that plug is connected, only list the future history downstream from that connection.
        allGraphs | ag: (create) - This flag is obsolete and has no effect.
        breadthFirst | bf: (create) - The breadth first traversal will return the closest nodes in the traversal first. The depth first traversal will follow a complete path away from the node, then return to any other paths from the node. Default is depth first.
        fastIteration | fi: (create) - This flag enables a faster iteration mode that offers more scalable performance, especially when traversing nodes with numerous connections.  However, the results can be slightly different, especially in cases with transitive dependencies between attributes (attribute A is affected by B which is affected by C, but A is not directly affected by C).
        fullNodeName | fnn: (create) - Return full node name in result.
        future | f: (create) - List the future instead of the history.
        futureLocalAttr | fl: (query) - This flag allows querying of the local-space future-related attribute(s) on shape nodes.
        futureWorldAttr | fw: (query) - This flag allows querying of the world-space future-related attribute(s) on shape nodes.
        groupLevels | gl: (create) - The node names are grouped depending on the level.  > 1 is the lead, the rest are grouped with it.
        historyAttr | ha: (query) - This flag allows querying of the attribute where history connects on shape nodes.
        interestLevel | il: (create) - If this flag is set, only nodes whose historicallyInteresting attribute value is not less than the value will be listed. The historicallyInteresting attribute is 0 on nodes which are not of interest to non-programmers.  1 for the TDs, 2 for the users.
        leaf | lf: (create) - If transform is selected, show history for its leaf shape. Default is true.
        levels | lv: (create) - Levels deep to traverse. Setting the number of levels to 0 means do all levels. All levels is the default.
        pruneDagObjects | pdo: (create) - If this flag is set, prune at dag objects.
    """
    ...


def listNodesWithIncorrectNames(*args) -> Any:
    r"""
    List all nodes with incorrect names in the Script Editor.

    Args:
    """
    ...


def listNodeTypes(*args, exclude: Optional[Union[str, bool]] = ..., ex: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Lists dependency node types satisfying a specified classification string.
    
    See the 'getClassification' command for a list of the standard classification
    strings.

    Args:
        exclude | ex: (create) - Nodes that satisfies this exclude classification will be filtered out.
    """
    ...


def listRelatives(*args, allDescendents: bool = ..., ad: bool = ..., allParents: bool = ..., ap: bool = ..., children: bool = ..., c: bool = ..., fullPath: bool = ..., f: bool = ..., noIntermediate: bool = ..., ni: bool = ..., parent: bool = ..., p: bool = ..., path: bool = ..., pa: bool = ..., shapes: bool = ..., s: bool = ..., type: Optional[Union[str, bool]] = ..., typ: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This command lists parents and children of DAG objects. The flags
    -c/children, -ad/allDescendents, -s/shapes, -p/parent and -ap/allParents
    are mutually exclusive. Only one can be used in a command.
    
    
    Unlike ls, this command does not return a unique path but simply returns
    the object's name by default. To get a unique path the -path flag must
    be used.
    
    
    When listing parents of objects directly under the world, the command
    will return an empty parent list. Listing parents of objects directly
    under a shape (underworld objects) will return their containing shape
    node in the list of parents. Listing parents of components of objects
    will return the object.
    
    
    When listing children, shape nodes will return their underworld
    objects in the list of children. Listing children of components of
    objects returns nothing.
    
    
    The -ni/noIntermediate flag works with the -s/shapes flag.
    It causes any intermediate shapes among the descendents to be ignored.

    Args:
        allDescendents | ad: (create) - Returns all the children, grand-children etc. of this dag node.  If a descendent is instanced, it will appear only once on the list returned. Note that it lists grand-children before children.
        allParents | ap: (create) - Returns all the parents of this dag node. Normally, this command only returns the parent corresponding to the first instance of the object
        children | c: (create) - List all the children of this dag node (default).
        fullPath | f: (create) - Return full pathnames instead of object names.
        noIntermediate | ni: (create) - No intermediate objects
        parent | p: (create) - Returns the parent of this dag node
        path | pa: (create) - Return a proper object name that can be passed to other commands.
        shapes | s: (create) - List all the children of this dag node that are shapes (ie, not transforms)
        type | typ: (create, multiuse) - List all relatives of the specified type.
    """
    ...


def listSets(*args, allSets: bool = ..., extendToShape: bool = ..., ets: bool = ..., object: Optional[Union[str, bool]] = ..., o: Optional[Union[str, bool]] = ..., type: Optional[Union[int, bool]] = ..., t: Optional[Union[int, bool]] = ...) -> Any:
    r"""
    The listSets command is used to get a list of all the sets an
    object belongs to. To get sets of a specific type for an object
    use the type flag as well.
    
    To get a list of all sets in the scene then don't use an object
    in the command line but use one of the flags instead.

    Args:
        allSets | allSets: (create) - Returns all sets in the scene.
        extendToShape | ets: (create) - When requesting a transform's sets also walk down to the shape immediately below it for its sets.
        object | o: (create) - Returns all sets which this object is a member of.
        type | t: (create) - Returns all sets in the scene of the given type:  1 - all rendering sets 2 - all deformer sets
    """
    ...


def lockNode(*args, ignoreComponents: bool = ..., ic: bool = ..., lock: bool = ..., l: bool = ..., lockName: bool = ..., ln: bool = ..., lockUnpublished: bool = ..., lu: bool = ..., query: bool = ...) -> Any:
    r"""
    Locks or unlocks one or more dependency nodes. A locked node is restricted
    in the following ways:
    
    
    It may not be deleted.
    It may not be renamed.
    Its parenting may not be changed.
    Attributes may not be added to or removed from it.
    Locked attributes may not be unlocked.
    Unlocked attributes may not be locked.
    
    
    Note that an unlocked attribute of a locked node may still have its value
    set, or connections to it made or broken. For more information on attribute
    locking, see the setAttr command.
    
    
    If no node names are specified then the current selection list is used.
    
    
    There are a few special behaviors when locking containers. Containers are
    automatically expanded to their constituent objects. When a container is
    locked, members of the container may not be unlocked and the container
    membership may not be modified. Containers may also be set to lock unpublished
    attributes. When in this state, unpublished member attributes may not have
    existing connections broken, new connections cannot be made, and values on unconnected
    attributes may not be modified. Parenting is allowed to change on members of locked
    containers that have been published as parent or child anchors.

    Args:
        ignoreComponents | ic: (create, query) - Normally, the presence of a component in the list of objects to be locked will cause the command to fail with an error. But if this flag is supplied then components will be silently ignored.
        lock | l: (create, query) - Specifies the new lock state for the node. The default is true.
        lockName | ln: (create, query) - Specifies the new lock state for the node's name.
        lockUnpublished | lu: (create, query) - Used in conjunction with the lock flag. On a container, lock or unlock all unpublished attributes on the members of the container. For non-containers, lock or unlock unpublished attributes on the specified node.
    """
    ...


def ls(*args, absoluteName: bool = ..., an: bool = ..., allPaths: bool = ..., ap: bool = ..., assemblies: bool = ..., cameras: bool = ..., ca: bool = ..., containerType: Optional[Union[str, bool]] = ..., ct: Optional[Union[str, bool]] = ..., containers: bool = ..., con: bool = ..., dagObjects: bool = ..., dag: bool = ..., defaultNodes: bool = ..., dn: bool = ..., dependencyNodes: bool = ..., dep: bool = ..., exactType: Optional[Union[str, bool]] = ..., et: Optional[Union[str, bool]] = ..., excludeType: Optional[Union[str, bool]] = ..., ext: Optional[Union[str, bool]] = ..., flatten: bool = ..., fl: bool = ..., geometry: bool = ..., g: bool = ..., ghost: bool = ..., gh: bool = ..., head: Optional[Union[int, bool]] = ..., hd: Optional[Union[int, bool]] = ..., hilite: bool = ..., hl: bool = ..., intermediateObjects: bool = ..., io: bool = ..., invisible: bool = ..., iv: bool = ..., leaf: bool = ..., lf: bool = ..., lights: bool = ..., lt: bool = ..., live: bool = ..., lv: bool = ..., lockedNodes: bool = ..., ln: bool = ..., long: bool = ..., l: bool = ..., materials: bool = ..., mat: bool = ..., modified: bool = ..., mod: bool = ..., noIntermediate: bool = ..., ni: bool = ..., nodeTypes: bool = ..., nt: bool = ..., objectsOnly: bool = ..., o: bool = ..., orderedSelection: bool = ..., os: bool = ..., partitions: bool = ..., pr: bool = ..., persistentNodes: bool = ..., pn: bool = ..., planes: bool = ..., pl: bool = ..., preSelectHilite: bool = ..., psh: bool = ..., readOnly: bool = ..., ro: bool = ..., recursive: bool = ..., r: bool = ..., referencedNodes: bool = ..., rn: bool = ..., references: bool = ..., rf: bool = ..., renderGlobals: bool = ..., rg: bool = ..., renderQualities: bool = ..., rq: bool = ..., renderResolutions: bool = ..., rr: bool = ..., renderSetups: bool = ..., rs: bool = ..., selection: bool = ..., sl: bool = ..., sets: bool = ..., set: bool = ..., shapes: bool = ..., s: bool = ..., shortNames: bool = ..., sn: bool = ..., showNamespace: bool = ..., sns: bool = ..., showType: bool = ..., st: bool = ..., tail: Optional[Union[int, bool]] = ..., tl: Optional[Union[int, bool]] = ..., templated: bool = ..., tm: bool = ..., textures: bool = ..., tex: bool = ..., transforms: bool = ..., tr: bool = ..., type: Optional[Union[str, bool]] = ..., typ: Optional[Union[str, bool]] = ..., ufeObjects: bool = ..., ufe: bool = ..., undeletable: bool = ..., ud: bool = ..., untemplated: bool = ..., ut: bool = ..., uuid: bool = ..., uid: bool = ..., visible: bool = ..., v: bool = ...) -> Any:
    r"""
    The ls command returns the names (and
    optionally the type names) of objects in the scene.
    
    The most common use of ls is to filter or
    match objects based on their name (using wildcards) or based on their
    type.
    By default ls will match any object in the
    scene but it can also be used to filter or list the selected
    objects when used in conjunction with the -selection flag.
    
    If type names are requested, using the showType flag, they
    will be interleaved with object names so the result will be
    pairs of <object, type> values.
    
    Internal nodes (for example itemFilter nodes) are typically filtered
    so that only scene objects are returned. However, using a wildcard
    will cause all the nodes matching the wild card to show up, including
    internal nodes.  For example, ls * will list all
    nodes whether internal or not.
    
    Use the syntax "::" to denote a recursive namespace search when listing nodes.
    For example, ls "::pSphere1" would match objects named
    "pSphere1" in any namespace, at any depth. ls "ns::*"
    would match any node in namespace "ns" or children namespaces.
    
    When Maya is in relativeNames mode, the ls command
    will return names relative to the current namespace and
    ls * will list from the the current namespace.
    For more details, please refer to the -relativeNames
    flag of the namespace command.
    
    The command may also be passed node UUIDs instead of names/paths, and
    can return UUIDs instead of names via the -uuid flag.

    Args:
        absoluteName | an: (create) - This flag can be used in conjunction with the showNamespace flag to specify that the namespace(s) returned by the command be in absolute namespace format. The absolute name of the namespace is a full namespace path, starting from the root namespace ":" and including all parent namespaces.  For example ":ns:ball" is an absolute namespace name while "ns:ball" is not. The absolute namespace name is invariant and is not affected by the current namespace or relative namespace modes.
        allPaths | ap: (create) - List all paths to nodes in DAG. This flag only works if -dag is also specified or if an object name is supplied.
        assemblies | assemblies: (create) - List top level transform Dag objects
        cameras | ca: (create) - List camera shapes.
        containerType | ct: (create, multiuse) - List containers with the specified user-defined type.  This flag cannot be used in conjunction with the type or exactType flag.
        containers | con: (create) - List containers. Includes both standard containers as well as other types of containers such as dagContainers.
        dagObjects | dag: (create) - List Dag objects of any type. If object name arguments are passed to the command then this flag will list all Dag objects below the specified object(s).
        defaultNodes | dn: (create) - Returns default nodes. A default node is one that Maya creates automatically and does not get saved out with the scene, although some of its attribute values may.
        dependencyNodes | dep: (create) - List dependency nodes. (including Dag objects)
        exactType | et: (create, multiuse) - List all objects of the specified type, but not objects that are descendents of that type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.  This flag cannot be used in conjunction with the type or excludeType flag.
        excludeType | ext: (create, multiuse) - List all objects that are not of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.  This flag cannot be used in conjunction with the type or exactType flag.
        flatten | fl: (create) - Flattens the returned list of objects so that each component is identified individually.
        geometry | g: (create) - List geometric Dag objects.
        ghost | gh: (create) - List ghosting objects.
        head | hd: (create) - This flag  specifies the maximum number of elements to be returned from the beginning of the list of items. Note: each type flag will return at most this many items so if multiple type flags are specified then the number of items returned can be greater than this amount.
        hilite | hl: (create) - List objects that are currently hilited for component selection.
        intermediateObjects | io: (create) - List only intermediate dag nodes.
        invisible | iv: (create) - List only invisible dag nodes.
        leaf | lf: (create) - List all leaf nodes in Dag. This flag is a modifier and must be used in conjunction with the -dag flag.
        lights | lt: (create) - List light shapes.
        live | lv: (create) - List objects that are currently live.
        lockedNodes | ln: (create) - Returns locked nodes, which cannot be deleted or renamed. However, their status may change.
        long | l: (create) - Return full path names for Dag objects. By default the shortest unique name is returned.
        materials | mat: (create) - List materials or shading groups.
        modified | mod: (create) - When this flag is set, only nodes modified since the last save will be returned.
        noIntermediate | ni: (create) - List only non intermediate dag nodes.
        nodeTypes | nt: (create) - Lists all registered node types.
        objectsOnly | o: (create) - When this flag is set only object names will be returned and components/attributes will be ignored.
        orderedSelection | os: (create) - List objects and components that are currently selected in their order of selection.  This flag depends on the value of the -tso/trackSelectionOrder flag of the selectPref command.  If that flag is not enabled than this flag will return the same thing as the -sl/selection flag would.
        partitions | pr: (create) - List partitions.
        persistentNodes | pn: (create) - Returns persistent nodes, which are nodes that stay in the Maya session after a file > new. These are a special class of default nodes that do not get reset on file > new. Ex: itemFilter and selectionListOperator nodes.
        planes | pl: (create) - List construction plane shapes.
        preSelectHilite | psh: (create) - List components that are currently hilited for pre-selection.
        readOnly | ro: (create) - Returns referenced nodes. Referenced nodes are read only. NOTE: Obsolete. Please use "-referencedNodes".
        recursive | r: (create) - When set to true, this command will look for name matches in all namespaces. When set to false, this command will only look for matches in namespaces that are requested (e.g. by specifying a name containing the ':'... "ns1:pSphere1").
        referencedNodes | rn: (create) - Returns referenced nodes. Referenced nodes are read only.
        references | rf: (create) - List references associated with files. Excludes special reference nodes such as the sharedReferenceNode and unknown reference nodes.
        renderGlobals | rg: (create) - List render globals.
        renderQualities | rq: (create) - List named render qualities.
        renderResolutions | rr: (create) - List render resolutions.
        renderSetups | rs: (create) - Alias for -renderGlobals.
        selection | sl: (create) - List objects that are currently selected.
        sets | set: (create) - List sets.
        shapes | s: (create) - List shape objects.
        shortNames | sn: (create) - Return short attribute names. By default long attribute names are returned.
        showNamespace | sns: (create) - Show the namespace of each object after the object name.  This flag cannot be used in conjunction with the showType flag.
        showType | st: (create) - List the type of each object after its name.
        tail | tl: (create) - This flag specifies the maximum number of elements to be returned from the end of the list of items. Note: each    type flag will return at most this many items so if multiple type flags are specified then the number of items returned can be greater than this amount
        templated | tm: (create) - List only templated dag nodes.
        textures | tex: (create) - List textures.
        transforms | tr: (create) - List transform objects.
        type | typ: (create, multiuse) - List all objects of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag. Note: some selection items in Maya do not have a specific object/data type associated with them and will return "untyped" when listed with this flag.  This flag cannot be used in conjunction with the exactType or excludeType flag.
        ufeObjects | ufe: (create) - When used in conjunction with the -sl/selection flag, will return objects that are defined through the UFE interface as well as native Maya objects.
        undeletable | ud: (create) - Returns nodes that cannot be deleted (which includes locked nodes). These nodes also cannot be renamed.
        untemplated | ut: (create) - List only un-templated dag nodes.
        uuid | uid: (create) - Return node UUIDs instead of names. Note that there are no "UUID paths" - combining this flag with e.g. the -long flag will not result in a path formed of node UUIDs.
        visible | v: (create) - List only visible dag nodes.
    """
    ...


def makeIdentity(*args, apply: bool = ..., a: bool = ..., jointOrient: bool = ..., jo: bool = ..., normal: Optional[Union[int, bool]] = ..., n: Optional[Union[int, bool]] = ..., preserveNormals: bool = ..., pn: bool = ..., rotate: bool = ..., r: bool = ..., scale: bool = ..., s: bool = ..., translate: bool = ..., t: bool = ...) -> Any:
    r"""
    The makeIdentity command is a quick way to reset the selected
    transform and all of its children down to the shape level by the
    identity transformation.  You can also specify which of transform,
    rotate or scale is applied down from the selected transform.
    The identity transformation means:
    
    translate = 0, 0, 0
    rotate = 0, 0, 0
    scale = 1, 1, 1
    shear = 1, 1, 1
    
    
    If a transform is a joint, then the "translate" attribute may not be 0,
    but will be used to position the joints so that they preserve their
    world space positions.  The translate flag doesn't apply to joints,
    since joints must preserve their world space positions.  Only the rotate
    and scale flags are meaningful when applied to joints.
    
    If the -a/apply flag is true, then the transforms that are reset
    are accumulated and applied to the all shapes below the modified
    transforms, so that the shapes will not move. The pivot positions are
    recalculated so that they also will not move in world space.
    If this flag is false, then the transformations are reset to identity,
    without any changes to preserve position.

    Args:
        apply | a: (create) - If this flag is true, the accumulated transforms are applied to the shape after the transforms are made identity, such that the world space positions of the transforms pivots are preserved, and the shapes do not move. The default is false.
        jointOrient | jo: (create) - If this flag is set, the joint orient on joints will be reset to align with worldspace.
        normal | n: (create) - If this flag is set to 1, the normals on polygonal objects will be frozen.  This flag is valid only when the -apply flag is on. If this flag is set to 2, the normals on polygonal objects will be frozen only if its a non-rigid transformation matrix. ie, a transformation that does not contain shear, skew or non-proportional scaling. The default behaviour is not to freeze normals.
        preserveNormals | pn: (create) - If this flag is true, the normals on polygonal objects will be reversed if the objects are negatively scaled (reflection). This flag is valid only when the -apply flag is on.
        rotate | r: (create) - If this flag is true, only the rotation is applied to the shape. The rotation will be changed to 0, 0, 0. If neither translate nor rotate nor scale flags are specified, then all (t, r, s) are applied.
        scale | s: (create) - If this flag is true, only the scale is applied to the shape. The scale factor will be changed to 1, 1, 1. If neither translate nor rotate nor scale flags are specified, then all (t, r, s) are applied.
        translate | t: (create) - If this flag is true, only the translation is applied to the shape. The translation will be changed to 0, 0, 0. If neither translate nor rotate nor scale flags are specified, then all (t, r, s)  are applied.  (Note: the translate flag is not meaningful when applied to joints, since joints are made to preserve their world space position.  This flag will have no effect on joints.)
    """
    ...


def makeLive(*args, addObjects: bool = ..., ao: bool = ..., none: bool = ..., n: bool = ..., registry: Optional[Union[int, bool]] = ..., r: Optional[Union[int, bool]] = ..., registryCount: bool = ..., rc: bool = ..., registryReset: bool = ..., rr: bool = ..., registrySize: Optional[Union[int, bool]] = ..., rs: Optional[Union[int, bool]] = ..., removeObjects: bool = ..., ro: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This commmand makes one or several objects live.  A live object defines the
    surface on which to create objects and to move objects relative to.
    Only construction planes, nurbs surfaces and polygon meshes can be made live.
    
    The makeLive command expects one of these types of objects as an explicit
    argument.  If no argument is explicitly specified, then there are a number
    of default behaviours based on what is currently active.  The command will
    fail if the active object(s) is/are not one of the valid types of objects.
    If there is nothing active, the current live object(s) will become dormant.
    Otherwise, the active object(s) will become the live object(s).
    
    The command allows for a limited number of objects collections to be saved
    in a registry entry. These collections can be queried and/or made live.

    Args:
        addObjects | ao: (edit) - Add the listed object(s) to the current live list. If an object is already in the live list, it is ignored.
        none | n: (create) - If the -n/none flag, the live object(s) will become dormant. Use of this flag causes any arguments to be ignored.
        registry | r: (create, query) - Make live the objects defined in the specified registry entry. In Query mode, return the list of objects defined in the specified registry entry.
        registryCount | rc: (query) - Return the actual number of registry entries. This number ranges from 0 to 'registrySize' - 1.
        registryReset | rr: (create) - Reset the maximum number of registry entries to the default value and clear all stored data.
        registrySize | rs: (create, query) - Defines the maximum number of registry entries that are remembered by the command. In Query mode, returns the maximum number currently set.
        removeObjects | ro: (edit) - Remove the listed object(s) from the current live list. If an object is not in the list, it is ignored.
    """
    ...


def makePaintable(*args, activate: bool = ..., ac: bool = ..., activateAll: bool = ..., aca: bool = ..., altAttribute: Optional[Union[str, bool]] = ..., aa: Optional[Union[str, bool]] = ..., attrType: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., clearAll: bool = ..., ca: bool = ..., remove: bool = ..., rm: bool = ..., shapeMode: Optional[Union[str, bool]] = ..., sm: Optional[Union[str, bool]] = ..., uiName: Optional[Union[str, bool]] = ..., ui: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    Make attributes of nodes paintable to Attribute Paint Tool.
    This command is used to register new attributes to the
    Attribute Paint tool as paintable. Once registered the
    attributes will be recognized by the Attribute Paint tool
    and the user will be able to paint them.

    Args:
        activate | ac: (create, query) - Activate / deactivate the given paintable attribute. Used to filter out some nodes in the attribute paint tool.
        activateAll | aca: (create, query) - Activate / deactivate all the registered paintable attributes. Used to filter out some nodes in the attribute paint tool.
        altAttribute | aa: (create, multiuse, query) - Define an alternate attribute which will also receive the same values. There can be multiple such flags.
        attrType | at: (create, query) - Paintable attribute type.    Supported types: intArray, doubleArray, vectorArray, multiInteger, multiFloat, multiDouble, multiVector.
        clearAll | ca: (create, query) - Removes all paintable attribute definitions.
        remove | rm: (create, query) - Make the attribute not paintable any more.
        shapeMode | sm: (create, query) - This flag controls how Artisan correlates the paintable node to a corresponding shape node.  It is used for attributes of type multi of multi, where the first multi dimension corresponds to the shape index (i.e. cluster nodes). At present, only one value of this flag is supported: "deformer". By default this flag is an empty string, which means that there is a direct indexing (no special mapping required) of the attribute with respect to vertices on the shape.
        uiName | ui: (create, query) - UI name. Default is the attribute name.
    """
    ...


def manipMoveContext(*args, activeHandle: Optional[Union[int, bool]] = ..., ah: Optional[Union[int, bool]] = ..., activeHandleNormal: Optional[Union[int, bool]] = ..., ahn: Optional[Union[int, bool]] = ..., alignAlong: Optional[Union[Tuple[float, float, float], bool]] = ..., aa: Optional[Union[Tuple[float, float, float], bool]] = ..., bakePivotOri: bool = ..., bpo: bool = ..., constrainAlongNormal: bool = ..., xn: bool = ..., currentActiveHandle: Optional[Union[int, bool]] = ..., cah: Optional[Union[int, bool]] = ..., editPivotMode: bool = ..., epm: bool = ..., editPivotPosition: bool = ..., epp: bool = ..., exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., interactiveUpdate: bool = ..., iu: bool = ..., lastMode: Optional[Union[int, bool]] = ..., lm: Optional[Union[int, bool]] = ..., manipVisible: bool = ..., vis: bool = ..., mode: Optional[Union[int, bool]] = ..., m: Optional[Union[int, bool]] = ..., orientAxes: Optional[Union[Tuple[float, float, float], bool]] = ..., oa: Optional[Union[Tuple[float, float, float], bool]] = ..., orientJoint: Optional[Union[str, bool]] = ..., oj: Optional[Union[str, bool]] = ..., orientJointEnabled: bool = ..., oje: bool = ..., orientObject: Optional[Union[str, bool]] = ..., oo: Optional[Union[str, bool]] = ..., orientTowards: Optional[Union[Tuple[float, float, float], bool]] = ..., ot: Optional[Union[Tuple[float, float, float], bool]] = ..., pinPivot: bool = ..., pin: bool = ..., pivotOriHandle: bool = ..., poh: bool = ..., position: bool = ..., p: bool = ..., postCommand: Optional[Union[str, bool]] = ..., psc: Optional[Union[str, bool]] = ..., postDragCommand: Optional[Union[Tuple[str, str], bool]] = ..., pod: Optional[Union[Tuple[str, str], bool]] = ..., preCommand: Optional[Union[str, bool]] = ..., prc: Optional[Union[str, bool]] = ..., preDragCommand: Optional[Union[Tuple[str, str], bool]] = ..., prd: Optional[Union[Tuple[str, str], bool]] = ..., preserveChildPosition: bool = ..., pcp: bool = ..., preserveUV: bool = ..., puv: bool = ..., reflection: bool = ..., rfl: bool = ..., reflectionAbout: int = ..., rab: int = ..., reflectionAxis: int = ..., rfa: int = ..., reflectionTolerance: float = ..., rft: float = ..., secondaryAxisOrient: Optional[Union[str, bool]] = ..., sao: Optional[Union[str, bool]] = ..., snap: bool = ..., s: bool = ..., snapComponentsRelative: bool = ..., scr: bool = ..., snapLiveFaceCenter: bool = ..., slf: bool = ..., snapLivePoint: bool = ..., slp: bool = ..., snapPivotOri: bool = ..., spo: bool = ..., snapPivotPos: bool = ..., spp: bool = ..., snapRelative: bool = ..., sr: bool = ..., snapValue: Optional[Union[float, bool]] = ..., sv: Optional[Union[float, bool]] = ..., translate: Optional[Union[Tuple[float, float, float], bool]] = ..., tr: Optional[Union[Tuple[float, float, float], bool]] = ..., tweakMode: bool = ..., twk: bool = ..., xformConstraint: Optional[Union[str, bool]] = ..., xc: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create, edit, or query a move
    manip context.
    Note that the flags -s, -sv, -sr, -scr, -slp, -slf control
    the global behaviour of all move manip context.  Changing one
    context independently is not allowed.  Changing a context's
    behaviour using the above flags, will change all existing move
    manip context.

    Args:
        activeHandle | ah: (edit, query) - Sets the default active handle for the manip.  That is, the handle which should be initially active when the tool is activated. Values can be:  0 - X axis handle is active 1 - Y axis handle is active 2 - Z axis handle is active 3 - Center handle (all 3 axes) is active (default)
        activeHandleNormal | ahn: (edit, query) - 0 - U axis handle is active 1 - V axis handle is active 2 - N axis handle is active ( default ) 3 - Center handle (all 3 axes) is active  applicable only when the manip mode is 3.
        alignAlong | aa: (create, edit) - Aligns active handle along vector.
        bakePivotOri | bpo: (edit, query) - Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.
        constrainAlongNormal | xn: (edit, query) - When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        currentActiveHandle | cah: (edit, query) - Sets the active handle for the manip. Values can be:  0 - X axis handle is active 1 - Y axis handle is active 2 - Z axis handle is active 3 - Center handle (all 3 axes) is active 4 - XY plane handle is active 5 - YZ plane handle is active 6 - XZ plane handle is active
        editPivotMode | epm: (query) - Returns true manipulator is in edit pivot mode
        editPivotPosition | epp: (query) - Returns the current position of the edit pivot manipulator.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        interactiveUpdate | iu: (edit, query) - Value can be : true or false. This flag value is valid only if the mode is 3 i.e. move vertex normal.
        lastMode | lm: (query) - Returns the previous translation mode.
        manipVisible | vis: (query) - Returns true if the main translate manipulator is visible.
        mode | m: (edit, query) - Translate mode:  0 - Object Space 1 - Local Space 2 - World Space (default) 3 - Move Along Vertex Normal 4 - Move Along Rotation Axis 5 - Move Along Live Object Axis 6 - Custom Axis Orientation 10 - Component Space
        orientAxes | oa: (edit, query) - Orients manipulator rotating around axes by specified angles
        orientJoint | oj: (edit, query) - Specifies the type of orientation for joint orientation. Valid options are: none, xyz, xzy, yxz, yzx, zxy, zyx.
        orientJointEnabled | oje: (edit, query) - Specifies if joints should be reoriented when moved.
        orientObject | oo: (create, edit) - Orients manipulator to the passed in object/component
        orientTowards | ot: (create, edit) - Orients active handle towards world point
        pinPivot | pin: (edit, query) - Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.
        pivotOriHandle | poh: (edit, query) - When true, the pivot manipulator will show the orientation handle during editing. Default is true.
        position | p: (query) - Returns the current position of the manipulator
        postCommand | psc: (create, edit) - Specifies a command to be executed when the tool is exited.
        postDragCommand | pod: (create, edit) - Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.
        preCommand | prc: (create, edit) - Specifies a command to be executed when the tool is entered.
        preDragCommand | prd: (create, edit) - Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.
        preserveChildPosition | pcp: (edit, query) - When false, the children objects move when their parent is moved. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.
        preserveUV | puv: (edit, query) - When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.
        reflection | rfl: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        reflectionAbout | rab: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        reflectionAxis | rfa: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        reflectionTolerance | rft: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        secondaryAxisOrient | sao: (edit, query) - Specifies the global axis (in world coordinates) that should be used to should be used to align the second axis of the orientJointType triple. Valid options are xup, yup, zup, xdown, ydown, zdown, none.
        snap | s: (edit, query) - Value can be : true or false. Enable/Disable the discrete move. If set to true, the move manipulator of all the move contexts would snap at discrete points along the active handle during mouse drag.  The interval between the points can be controlled using the 'snapValue' flag.
        snapComponentsRelative | scr: (edit, query) - Value can be : true or false. If true, while snapping a group of CVs/Vertices, the relative spacing between them will be preserved. If false, all the CVs/Vertices will be snapped to the target point (is used during grid snap(hotkey 'x'), and point snap(hotkey 'v')) Depress the 'x' key before click-dragging the manip handle and check to see the behaviour of moving a bunch of CVs, with this flag ON and OFF.
        snapLiveFaceCenter | slf: (edit, query) - Value can be : true or false. If true, while moving on the live polygon object, the move manipulator will snap to the face centers of the object.
        snapLivePoint | slp: (edit, query) - Value can be : true or false. If true, while moving on the live polygon object, the move manipulator will snap to the vertices of the object.
        snapPivotOri | spo: (edit, query) - Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.
        snapPivotPos | spp: (edit, query) - Snap pivot position. Modify pivot position when snapping the pivot to a component.
        snapRelative | sr: (edit, query) - Value can be : true or false. Applicable only when the snap is enabled. If true, the snapValue is treated relative to the original position before moving. If false, the snapValue is treated relative to the world origin. NOTE:    If in local/object Space Mode, the snapRelative should be ON. Absolute discrete move is not supported in local/object mode.
        snapValue | sv: (edit, query) - Applicable only when the snap is enabled. The manipulator of all move contexts would move in steps of 'snapValue'
        translate | tr: (edit, query) - Returns the translation of the manipulator for its current orientation/mode.
        tweakMode | twk: (edit, query) - When true, the manipulator is hidden and highlighted components can be selected and moved in one step using a click-drag interaction.
        xformConstraint | xc: (edit, query) - none - no transform constraint edge - edge transform constraint surface - surface transform constraint
    """
    ...


def manipMoveLimitsCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create a context for the translate limits manipulator.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def manipRotateContext(*args, activeHandle: Optional[Union[int, bool]] = ..., ah: Optional[Union[int, bool]] = ..., alignAlong: Optional[Union[Tuple[float, float, float], bool]] = ..., aa: Optional[Union[Tuple[float, float, float], bool]] = ..., bakePivotOri: bool = ..., bpo: bool = ..., centerTrackball: bool = ..., ctb: bool = ..., constrainAlongNormal: bool = ..., xn: bool = ..., currentActiveHandle: Optional[Union[int, bool]] = ..., cah: Optional[Union[int, bool]] = ..., editPivotMode: bool = ..., epm: bool = ..., editPivotPosition: bool = ..., epp: bool = ..., exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., lastMode: Optional[Union[int, bool]] = ..., lm: Optional[Union[int, bool]] = ..., manipVisible: bool = ..., vis: bool = ..., mode: Optional[Union[int, bool]] = ..., m: Optional[Union[int, bool]] = ..., modifyTranslation: bool = ..., mt: bool = ..., orientAxes: Optional[Union[Tuple[float, float, float], bool]] = ..., oa: Optional[Union[Tuple[float, float, float], bool]] = ..., orientObject: Optional[Union[str, bool]] = ..., oo: Optional[Union[str, bool]] = ..., orientTowards: Optional[Union[Tuple[float, float, float], bool]] = ..., ot: Optional[Union[Tuple[float, float, float], bool]] = ..., pinPivot: bool = ..., pin: bool = ..., pivotOriHandle: bool = ..., poh: bool = ..., position: bool = ..., p: bool = ..., postCommand: Optional[Union[str, bool]] = ..., psc: Optional[Union[str, bool]] = ..., postDragCommand: Optional[Union[Tuple[str, str], bool]] = ..., pod: Optional[Union[Tuple[str, str], bool]] = ..., preCommand: Optional[Union[str, bool]] = ..., prc: Optional[Union[str, bool]] = ..., preDragCommand: Optional[Union[Tuple[str, str], bool]] = ..., prd: Optional[Union[Tuple[str, str], bool]] = ..., preserveChildPosition: bool = ..., pcp: bool = ..., preserveUV: bool = ..., puv: bool = ..., reflection: bool = ..., rfl: bool = ..., reflectionAbout: int = ..., rab: int = ..., reflectionAxis: int = ..., rfa: int = ..., reflectionTolerance: float = ..., rft: float = ..., rotate: Optional[Union[Tuple[float, float, float], bool]] = ..., ro: Optional[Union[Tuple[float, float, float], bool]] = ..., snap: bool = ..., s: bool = ..., snapPivotOri: bool = ..., spo: bool = ..., snapPivotPos: bool = ..., spp: bool = ..., snapRelative: bool = ..., sr: bool = ..., snapValue: Optional[Union[float, bool]] = ..., sv: Optional[Union[float, bool]] = ..., tweakMode: bool = ..., twk: bool = ..., useCenterPivot: bool = ..., ucp: bool = ..., useManipPivot: bool = ..., ump: bool = ..., useObjectPivot: bool = ..., uop: bool = ..., xformConstraint: Optional[Union[str, bool]] = ..., xc: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create, edit, or query a rotate manip context.

    Args:
        activeHandle | ah: (edit, query) - Sets the default active handle for the manip.  That is, the handle which should be initially active when the tool is activated. Values can be:  0 - X axis handle is active 1 - Y axis handle is active 2 - Z axis handle is active 3 - View rotation handle (outer ring) is active (default)
        alignAlong | aa: (create, edit) - Aligns active handle along vector.
        bakePivotOri | bpo: (edit, query) - Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.
        centerTrackball | ctb: (create, edit, query) - Specify if the center is to be handled like a trackball
        constrainAlongNormal | xn: (edit, query) - When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        currentActiveHandle | cah: (edit, query) - Sets the active handle for the manip. Values can be:  0 - X axis handle is active 1 - Y axis handle is active 2 - Z axis handle is active 3 - View rotation handle (outer ring) is active 4 - Arc Ball is active
        editPivotMode | epm: (query) - Returns true manipulator is in edit pivot mode
        editPivotPosition | epp: (query) - Returns the current position of the edit pivot manipulator.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        lastMode | lm: (query) - Returns the previous rotation mode.
        manipVisible | vis: (query) - Returns true if the rotate manipulator is visible.
        mode | m: (edit, query) - Rotate mode:  0 - Object Space (default) 1 - World Space 2 - Gimbal Mode 3 - Custom Axis Orientation 10 - Component Space
        modifyTranslation | mt: (edit, query) - When false, and an object is rotated about a point other than its rotate pivot, its rotateTranslate attribute is modified to put the object at the correct position. When true, its translate attribute is used instead. Default is false.
        orientAxes | oa: (edit, query) - Orients manipulator rotating around axes by specified angles
        orientObject | oo: (create, edit) - Orients manipulator to the passed in object/component
        orientTowards | ot: (create, edit) - Orients active handle towards world point
        pinPivot | pin: (edit, query) - Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.
        pivotOriHandle | poh: (edit, query) - When true, the pivot manipulator will show the orientation handle during editing. Default is true.
        position | p: (query) - Returns the current position of the manipulator.
        postCommand | psc: (create, edit) - Specifies a command to be executed when the tool is exited.
        postDragCommand | pod: (create, edit) - Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.
        preCommand | prc: (create, edit) - Specifies a command to be executed when the tool is entered.
        preDragCommand | prd: (create, edit) - Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.
        preserveChildPosition | pcp: (edit, query) - When false, the children objects move when their parent is rotated. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.
        preserveUV | puv: (edit, query) - When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.
        reflection | rfl: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        reflectionAbout | rab: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        reflectionAxis | rfa: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        reflectionTolerance | rft: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        rotate | ro: (edit, query) - Returns the rotation of the manipulator for its current orientation/mode.
        snap | s: (create, edit, query) - Specify that the manipulation is to use absolute snap
        snapPivotOri | spo: (edit, query) - Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.
        snapPivotPos | spp: (edit, query) - Snap pivot position. Modify pivot position when snapping the pivot to a component.
        snapRelative | sr: (create, edit, query) - Specify that the manipulation is to use relative snap
        snapValue | sv: (create, edit, query) - Specify the snapping value
        tweakMode | twk: (edit, query) - When true, the manipulator is hidden and highlighted components can be selected and rotated in one step using a click-drag interaction.
        useCenterPivot | ucp: (edit, query) - When true, use the center of the selection's bounding box as the center of the rotation (for all objects).
        useManipPivot | ump: (edit, query) - When true, use the manipulator's center as the center of the rotation (for all objects).
        useObjectPivot | uop: (edit, query) - When true, use each object's pivot as the center of its rotation.
        xformConstraint | xc: (edit, query) - none - no transform constraint edge - edge transform constraint surface - surface transform constraint
    """
    ...


def manipRotateLimitsCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create a context for the rotate limits manipulator.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def manipScaleContext(*args, activeHandle: Optional[Union[int, bool]] = ..., ah: Optional[Union[int, bool]] = ..., alignAlong: Optional[Union[Tuple[float, float, float], bool]] = ..., aa: Optional[Union[Tuple[float, float, float], bool]] = ..., bakePivotOri: bool = ..., bpo: bool = ..., constrainAlongNormal: bool = ..., xn: bool = ..., currentActiveHandle: Optional[Union[int, bool]] = ..., cah: Optional[Union[int, bool]] = ..., editPivotMode: bool = ..., epm: bool = ..., editPivotPosition: bool = ..., epp: bool = ..., exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., lastMode: Optional[Union[int, bool]] = ..., lm: Optional[Union[int, bool]] = ..., manipVisible: bool = ..., vis: bool = ..., mode: Optional[Union[int, bool]] = ..., m: Optional[Union[int, bool]] = ..., orientAxes: Optional[Union[Tuple[float, float, float], bool]] = ..., oa: Optional[Union[Tuple[float, float, float], bool]] = ..., orientObject: Optional[Union[str, bool]] = ..., oo: Optional[Union[str, bool]] = ..., orientTowards: Optional[Union[Tuple[float, float, float], bool]] = ..., ot: Optional[Union[Tuple[float, float, float], bool]] = ..., pinPivot: bool = ..., pin: bool = ..., pivotOriHandle: bool = ..., poh: bool = ..., position: bool = ..., p: bool = ..., postCommand: Optional[Union[str, bool]] = ..., psc: Optional[Union[str, bool]] = ..., postDragCommand: Optional[Union[Tuple[str, str], bool]] = ..., pod: Optional[Union[Tuple[str, str], bool]] = ..., preCommand: Optional[Union[str, bool]] = ..., prc: Optional[Union[str, bool]] = ..., preDragCommand: Optional[Union[Tuple[str, str], bool]] = ..., prd: Optional[Union[Tuple[str, str], bool]] = ..., preserveChildPosition: bool = ..., pcp: bool = ..., preserveUV: bool = ..., puv: bool = ..., preventNegativeScale: bool = ..., pns: bool = ..., reflection: bool = ..., rfl: bool = ..., reflectionAbout: int = ..., rab: int = ..., reflectionAxis: int = ..., rfa: int = ..., reflectionTolerance: float = ..., rft: float = ..., scale: Optional[Union[Tuple[float, float, float], bool]] = ..., sc: Optional[Union[Tuple[float, float, float], bool]] = ..., snap: bool = ..., s: bool = ..., snapPivotOri: bool = ..., spo: bool = ..., snapPivotPos: bool = ..., spp: bool = ..., snapRelative: bool = ..., sr: bool = ..., snapValue: Optional[Union[float, bool]] = ..., sv: Optional[Union[float, bool]] = ..., tweakMode: bool = ..., twk: bool = ..., useManipPivot: bool = ..., ump: bool = ..., useObjectPivot: bool = ..., uop: bool = ..., xformConstraint: Optional[Union[str, bool]] = ..., xc: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create, edit, or query a scale manip context.

    Args:
        activeHandle | ah: (edit, query) - Sets the default active handle for the manip.  That is, the handle which should be initially active when the tool is activated. Values can be:  0 - X axis handle is active 1 - Y axis handle is active 2 - Z axis handle is active 3 - Center handle (all axes) is active (default)
        alignAlong | aa: (create, edit) - Aligns active handle along vector.
        bakePivotOri | bpo: (edit, query) - Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.
        constrainAlongNormal | xn: (edit, query) - When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        currentActiveHandle | cah: (edit, query) - Sets the active handle for the manip. Values can be:  0 - X axis handle is active 1 - Y axis handle is active 2 - Z axis handle is active 3 - Center handle (all axes) is active 4 - XY plane handle is active 5 - YZ plane handle is active 6 - XZ plane handle is active
        editPivotMode | epm: (query) - Returns true manipulator is in edit pivot mode
        editPivotPosition | epp: (query) - Returns the current position of the edit pivot manipulator.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        lastMode | lm: (query) - Returns the previous scaling mode.
        manipVisible | vis: (query) - Returns true if the scale manipulator is visible.
        mode | m: (edit, query) - Scale mode:  0 - Object Space 1 - Local Space 2 - World Space (default) 3 - Scale Along Vertex Normal 4 - Scale Along Rotation Axis 5 - Scale Along Live Object Axis 6 - Custom Axis Orientation 10 - Component Space
        orientAxes | oa: (edit, query) - Orients manipulator rotating around axes by specified angles
        orientObject | oo: (create, edit) - Orients manipulator to the passed in object/component
        orientTowards | ot: (create, edit) - Orients active handle towards world point
        pinPivot | pin: (edit, query) - Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.
        pivotOriHandle | poh: (edit, query) - When true, the pivot manipulator will show the orientation handle during editing. Default is true.
        position | p: (query) - Returns the current position of the manipulator.
        postCommand | psc: (create, edit) - Specifies a command to be executed when the tool is exited.
        postDragCommand | pod: (create, edit) - Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.
        preCommand | prc: (create, edit) - Specifies a command to be executed when the tool is entered.
        preDragCommand | prd: (create, edit) - Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.
        preserveChildPosition | pcp: (edit, query) - When false, the children objects move when their parent is rotated. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.
        preserveUV | puv: (edit, query) - When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.
        preventNegativeScale | pns: (query) - When this is true, negative scale is not allowed.
        reflection | rfl: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        reflectionAbout | rab: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        reflectionAxis | rfa: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        reflectionTolerance | rft: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        scale | sc: (edit, query) - Returns the scale of the manipulator for its current orientation/mode.
        snap | s: (create, edit, query) - Specify that the manipulation is to use absolute snap
        snapPivotOri | spo: (edit, query) - Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.
        snapPivotPos | spp: (edit, query) - Snap pivot position. Modify pivot position when snapping the pivot to a component.
        snapRelative | sr: (create, edit, query) - Specify that the manipulation is to use relative snap
        snapValue | sv: (create, edit, query) - Specify the snapping value
        tweakMode | twk: (edit, query) - When true, the manipulator is hidden and highlighted components can be selected and scaled in one step using a click-drag interaction.
        useManipPivot | ump: (create, edit, query) - Specify whether to pivot on the manip
        useObjectPivot | uop: (create, edit, query) - Specify whether to pivot on the object
        xformConstraint | xc: (edit, query) - none - no transform constraint edge - edge transform constraint surface - surface transform constraint
    """
    ...


def manipScaleLimitsCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create a context for the scale limits manipulator.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def matchTransform(*args, pivots: bool = ..., piv: bool = ..., position: bool = ..., pos: bool = ..., positionX: bool = ..., px: bool = ..., positionY: bool = ..., py: bool = ..., positionZ: bool = ..., pz: bool = ..., rotatePivot: bool = ..., rp: bool = ..., rotation: bool = ..., rot: bool = ..., rotationX: bool = ..., rx: bool = ..., rotationY: bool = ..., ry: bool = ..., rotationZ: bool = ..., rz: bool = ..., scale: bool = ..., scl: bool = ..., scaleBox: bool = ..., box: bool = ..., scalePivot: bool = ..., sp: bool = ..., scaleX: bool = ..., sx: bool = ..., scaleY: bool = ..., sy: bool = ..., scaleZ: bool = ..., sz: bool = ...) -> Any:
    r"""
    This command modifies the source object's transform to match the
    target object's transform.
    
    If no flags are specified then the command will match position,
    rotation and scaling.

    Args:
        pivots | piv: (create) - Match the source object(s) scale/rotate pivot positions to the target transform's pivot.
        position | pos: (create) - Match the source object(s) position to the target object.
        positionX | px: (create) - Match the source object(s) X position to the target object.
        positionY | py: (create) - Match the source object(s) Y position to the target object.
        positionZ | pz: (create) - Match the source object(s) Z position to the target object.
        rotatePivot | rp: (create) - Match the source object(s) rotate pivot position to the target transform's pivot.
        rotation | rot: (create) - Match the source object(s) rotation to the target object.
        rotationX | rx: (create) - Match the source object(s) X rotation to the target object.
        rotationY | ry: (create) - Match the source object(s) Y rotation to the target object.
        rotationZ | rz: (create) - Match the source object(s) Z rotation to the target object.
        scale | scl: (create) - Match the source object(s) scale to the target transform.
        scaleBox | box: (create) - Use the source/target object's child bounding box size when matching scaling.
        scalePivot | sp: (create) - Match the source object(s) scale pivot position to the target transform's pivot.
        scaleX | sx: (create) - Match the source object(s) X scale to the target object.
        scaleY | sy: (create) - Match the source object(s) Y scale to the target object.
        scaleZ | sz: (create) - Match the source object(s) Z scale to the target object.
    """
    ...


def modelCurrentTimeCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., percent: Optional[Union[float, bool]] = ..., per: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context which may be used to change current time
    within the model views.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        percent | per: (edit, query) - Percent of the screen space that represents the full time slider range (default is 50%)
    """
    ...


def move(*args, absolute: bool = ..., a: bool = ..., componentOffset: bool = ..., co: bool = ..., componentSpace: bool = ..., cs: bool = ..., constrainAlongNormal: bool = ..., xn: bool = ..., deletePriorHistory: bool = ..., dph: bool = ..., localSpace: bool = ..., ls: bool = ..., moveX: bool = ..., x: bool = ..., moveXY: bool = ..., xy: bool = ..., moveXYZ: bool = ..., xyz: bool = ..., moveXZ: bool = ..., xz: bool = ..., moveY: bool = ..., y: bool = ..., moveYZ: bool = ..., yz: bool = ..., moveZ: bool = ..., z: bool = ..., objectSpace: bool = ..., os: bool = ..., orientJoint: Optional[Union[str, bool]] = ..., oj: Optional[Union[str, bool]] = ..., parameter: bool = ..., p: bool = ..., preserveChildPosition: bool = ..., pcp: bool = ..., preserveGeometryPosition: bool = ..., pgp: bool = ..., preserveUV: bool = ..., puv: bool = ..., reflection: bool = ..., rfl: bool = ..., reflectionAboutBBox: bool = ..., rab: bool = ..., reflectionAboutOrigin: bool = ..., rao: bool = ..., reflectionAboutX: bool = ..., rax: bool = ..., reflectionAboutY: bool = ..., ray: bool = ..., reflectionAboutZ: bool = ..., raz: bool = ..., reflectionTolerance: Optional[Union[float, bool]] = ..., rft: Optional[Union[float, bool]] = ..., relative: bool = ..., r: bool = ..., rotatePivotRelative: bool = ..., rpr: bool = ..., scalePivotRelative: bool = ..., spr: bool = ..., secondaryAxisOrient: Optional[Union[str, bool]] = ..., sao: Optional[Union[str, bool]] = ..., symNegative: bool = ..., smn: bool = ..., worldSpace: bool = ..., ws: bool = ..., worldSpaceDistance: bool = ..., wd: bool = ..., xformConstraint: Optional[Union[str, bool]] = ..., xc: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    The move command is used to change the positions of geometric
    objects.
    
    The default behaviour, when no objects or flags are passed, is
    to do a absolute move on each currently selected object in the
    world space. The value of the coordinates are interpreted as
    being defined in the current linear unit unless the unit is
    explicitly mentioned.
    
    When using -objectSpace there are two ways to use this command.
    If numbers are typed without units then the internal values of
    the object are set to these values. If, on the other hand a
    unit is specified then the internal value is set to the equivalent
    internal value that represents that world-space distance.
    
    The -localSpace flag moves the object in its parent space. In this
    space the x,y,z values correspond directly to the tx, ty, tz
    channels on the object.
    
    The -rotatePivotRelative/-scalePivotRelative flags can be used
    with the -absolute flag to translate an object so that its
    pivot point ends up at the given absolute position. These
    flags will be ignored if components are specified.
    
    The -worldSpaceDistance flag is a modifier flag that may be used
    in conjunction with the -objectSpace/-localSpace flags. When this
    flag is specified the command treats the x,y,z values as world
    space units so the object will move the specified world space
    distance but it will move along the axis specified by the
    -objectSpace/-localSpace flag. The default behaviour, without
    this flag, is to treat the x,y,z values as units in object
    space or local space. In other words, the worldspace distance
    moved will depend on the transformations applied to the object
    unless this flag is specified.

    Args:
        absolute | a: (create) - Perform an absolute operation.
        componentOffset | co: (create) - Move components individually in local space
        componentSpace | cs: (create) - Move in local component space
        constrainAlongNormal | xn: (create) - When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        deletePriorHistory | dph: (create) - If true then delete the history prior to the current operation.
        localSpace | ls: (create) - Move in local space
        moveX | x: (create) - Move in X direction
        moveXY | xy: (create) - Move in XY direction
        moveXYZ | xyz: (create) - Move in all directions (default)
        moveXZ | xz: (create) - Move in XZ direction
        moveY | y: (create) - Move in Y direction
        moveYZ | yz: (create) - Move in YZ direction
        moveZ | z: (create) - Move in Z direction
        objectSpace | os: (create) - Move in object space
        orientJoint | oj: (create) - Default is xyz.
        parameter | p: (create) - Move in parametric space
        preserveChildPosition | pcp: (create) - When true, transforming an object will apply an opposite transform to its child transform to keep them at the same world-space position. Default is false.
        preserveGeometryPosition | pgp: (create) - When true, transforming an object will apply an opposite transform to its geometry points to keep them at the same world-space position. Default is false.
        preserveUV | puv: (create) - When true, UV values on translated components are projected along the translation in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected vertices. Default is false.
        reflection | rfl: (create) - To move the corresponding symmetric components also.
        reflectionAboutBBox | rab: (create) - Sets the position of the reflection axis  at the geometry bounding box
        reflectionAboutOrigin | rao: (create) - Sets the position of the reflection axis  at the origin
        reflectionAboutX | rax: (create) - Specifies the X=0 as reflection plane
        reflectionAboutY | ray: (create) - Specifies the Y=0 as reflection plane
        reflectionAboutZ | raz: (create) - Specifies the Z=0 as reflection plane
        reflectionTolerance | rft: (create) - Specifies the tolerance to findout the corresponding reflected components
        relative | r: (create) - Perform a operation relative to the object's current position
        rotatePivotRelative | rpr: (create) - Move relative to the object's rotate pivot point.
        scalePivotRelative | spr: (create) - Move relative to the object's scale pivot point.
        secondaryAxisOrient | sao: (create) - Default is xyz.
        symNegative | smn: (create) - When set the component transformation is flipped so it is relative to the negative side of the symmetry plane. The default (no flag) is to transform components relative to the positive side of the symmetry plane.
        worldSpace | ws: (create) - Move in world space
        worldSpaceDistance | wd: (create) - Move is specified in world space units
        xformConstraint | xc: (create) - Apply a transform constraint to moving components.  none - no constraint surface - constrain components to the surface edge - constrain components to surface edges live - constraint components to the live surface
    """
    ...


def moveKeyCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., moveFunction: Optional[Union[str, bool]] = ..., mf: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., option: Optional[Union[str, bool]] = ..., o: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context which may be used to move keyframes
    within the graph editor

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        moveFunction | mf: (edit, query) - linear | power | constant. Specifies how the keys are dragged. The default move type is constant where all keys move the same amount as controlled by user movement. Power provides a fall-off function where the center of the drag moves the most and the keys around the drag move less.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        option | o: (create, edit, query) - Valid values are "move," "insert," "over," and "segmentOver." When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to make room for the segment.
    """
    ...


def nodeCast(*args, copyDynamicAttrs: bool = ..., cda: bool = ..., disableAPICallbacks: bool = ..., dsa: bool = ..., disableScriptJobCallbacks: bool = ..., dsj: bool = ..., disconnectUnmatchedAttrs: bool = ..., dua: bool = ..., force: bool = ..., f: bool = ..., swapNames: bool = ..., sn: bool = ..., swapValues: bool = ..., sv: bool = ...) -> Any:
    r"""
    Given two nodes, a source node of type A and a target node of type B,
    where type A is either type B or a sub-type of B, this command will replace the
    target node with the source node. That is, all node connections, DAG hierarchy
    and attribute values on the target node will be removed from the target node
    and placed on the source node. This operation will fail if either object is
    referenced, locked or if the nodes do not share a common sub-type.
    This operation is atomic. If the given parameters fail, then the source and
    target nodes will remain in their initial state prior to execution of the
    command.
    IMPORTANT: the command will currently ignore instance connections and
    instance objects.  It will also ignore reference nodes.

    Args:
        copyDynamicAttrs | cda: (create) - If the target node contains any dynamic attributes that are not defined on the source node, then create identical dynamic attricutes on the source node and copy the values and connections from the target node into them.
        disableAPICallbacks | dsa: (create) - add comment
        disableScriptJobCallbacks | dsj: (create) - add comment
        disconnectUnmatchedAttrs | dua: (create) - If the node that is being swapped out has any connections that do not exist on the target node, then indicate if the connection should be disconnected. By default these connections are not removed because they cannot be restored if the target node is swapped back with the source node.
        force | f: (create) - Forces the command to do the node cast operation even if the nodes do not share a common base object. When this flag is specified the command will try to do the best possible attribute matching when swapping the command.  It is not recommended to use the '-swapValues/sv' flag with this flag.
        swapNames | sn: (create) - Swap the names of the nodes. By default names are not swapped.
        swapValues | sv: (create) - Indicates if the commands should exchange attributes on the common attributes between the two nodes.  For example, if the nodes are the same base type as a transform node, then rotate, scale, translate values would be copied over.
    """
    ...


def nodeType(*args, apiType: bool = ..., api: bool = ..., derived: bool = ..., d: bool = ..., inherited: bool = ..., i: bool = ..., isTypeName: bool = ..., itn: bool = ..., ufeRuntimeName: bool = ..., urn: bool = ...) -> Any:
    r"""
    This command returns a string which identifies the given node's type.
    
    When no flags are used, the unique type name is returned.  This can be
    useful for seeing if two nodes are of the same type.
    
    When the api flag is used, the MFn::Type of the node is returned.
    This can be useful for seeing if a plug-in node belongs to a given
    class. The api flag cannot be used in conjunction with any other
    flags.
    
    When the derived flag is used, the command returns a string array
    containing the names of all the currently known node types which derive
    from the node type of the given object.
    
    When the inherited flag is used, the command returns a string array
    containing the names of all the base node types inherited by the
    the given node.
    
    If the isTypeName flag is present then the argument provided to the
    command is taken to be the name of a node type rather than the name of a
    specific node. This makes it possible to query the hierarchy of node types
    without needing to have instances of each node type.

    Args:
        apiType | api: (create) - Return the MFn::Type value (as a string) corresponding to the given node.  This is particularly useful when the given node is defined by a plug-in, since in this case, the MFn::Type value corresponds to the underlying proxy class.  This flag cannot be used in combination with any of the other flags.
        derived | d: (create) - Return a string array containing the names of all the currently known node types which derive from the type of the specified node.
        inherited | i: (create) - Return a string array containing the names of all the base node types inherited by the specified node.
        isTypeName | itn: (create) - If this flag is present, then the argument provided to the command is the name of a node type rather than the name of a specific node.
        ufeRuntimeName | urn: (create) - Return the UFE Runtime name corresponding to the given node. This is particularly useful to filter between native Maya objects and non-native objects exposed to Maya through the UFE interface.
    """
    ...


def objectCenter(*args, gl: bool = ..., local: bool = ..., l: bool = ..., x: bool = ..., y: bool = ..., z: bool = ...) -> Any:
    r"""
    This command returns the coordinates of the center of the bounding box
    of the specified object. If one coordinate only is specified, it will
    be returned as a float. If no coordinates are specified, an array of
    floats is returned, containing x, y, and z. If you specify multiple
    coordinates, only one will be returned.

    Args:
        gl | gl: (create) - Return positional values in global coordinates (default).
        local | l: (create) - Return positional values in local coordinates.
        x | x: (create) - Return X value only
        y | y: (create) - Return Y value only
        z | z: (create) - Return Z value only
    """
    ...


def objectType(*args, isAType: Optional[Union[str, bool]] = ..., isa: Optional[Union[str, bool]] = ..., isType: Optional[Union[str, bool]] = ..., i: Optional[Union[str, bool]] = ..., tagFromType: Optional[Union[str, bool]] = ..., tgt: Optional[Union[str, bool]] = ..., typeFromTag: Optional[Union[int, bool]] = ..., tpt: Optional[Union[int, bool]] = ..., typeTag: bool = ..., tt: bool = ...) -> Any:
    r"""
    This command returns the type of elements. Warning: This command is
    incomplete and may not be supported by all object types.

    Args:
        isAType | isa: (create) - Returns true if the object is the specified type or derives from an object that is of the specified type. This flag will only work with dependency nodes.
        isType | i: (create) - Returns true if the object is exactly of the specified type. False otherwise.
        tagFromType | tgt: (create) - Returns the type tag given a type name.
        typeFromTag | tpt: (create) - Returns the type name given an integer type tag.
        typeTag | tt: (create) - Returns an integer tag that is unique for that object type.  Not all object types will have tags.  This is the unique 4-byte value that is used to identify nodes of a given type in the binary file format.
    """
    ...


def objExists(*args) -> Any:
    r"""
    This command simply returns true or false depending on whether
    an object with the given name exists.

    Args:
    """
    ...


def orbitCtx(*args, alternateContext: bool = ..., ac: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., localOrbit: bool = ..., lo: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., orbitScale: Optional[Union[float, bool]] = ..., os: Optional[Union[float, bool]] = ..., toolName: Optional[Union[str, bool]] = ..., tn: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create, edit, or query an orbit context.

    Args:
        alternateContext | ac: (create, query) - Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        localOrbit | lo: (create, edit, query) - Orbit around the camera's center of interest.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        orbitScale | os: (create, edit, query) - In degrees of rotation per 100 pixels of cursor drag.
        toolName | tn: (create, query) - Name of the specific tool to which this command refers.
    """
    ...


def panZoomCtx(*args, alternateContext: bool = ..., ac: bool = ..., buttonDown: bool = ..., btd: bool = ..., buttonUp: bool = ..., btu: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., panMode: bool = ..., pm: bool = ..., toolName: Optional[Union[str, bool]] = ..., tn: Optional[Union[str, bool]] = ..., zoomMode: bool = ..., zm: bool = ..., zoomScale: Optional[Union[float, bool]] = ..., zs: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create camera 2D pan/zoom context.

    Args:
        alternateContext | ac: (create, query) - Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        buttonDown | btd: (create) - Perform the button down operation
        buttonUp | btu: (create) - Perform the button up operation
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        panMode | pm: (create) - Specify to create a camera 2D pan context, which is the default.
        toolName | tn: (create, query) - Name of the specific tool to which this command refers.
        zoomMode | zm: (create) - Specify to create a camera 2D zoom context.
        zoomScale | zs: (create, edit, query) - Scale the zoom. The smaller the scale the slower the drag.
    """
    ...


def paramDimContext(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command used to register the paramDimCtx tool.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def paramDimension(*args) -> Any:
    r"""
    This command is used to create a param dimension to display the
    parameter value of a curve/surface at a specified point on the
    curve/surface.

    Args:
    """
    ...


def paramLocator(*args, position: bool = ..., p: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The command creates a locator in the underworld of a NURBS curve or
    NURBS surface at the specified parameter value.  If no object is
    specified, then a locator will be created on the first valid selected item
    (either a curve point or a surface point).

    Args:
        position | p: (create) - Whether to set the locator position in normalized space.
    """
    ...


def parent(*args, absolute: bool = ..., a: bool = ..., addObject: bool = ..., add: bool = ..., noConnections: bool = ..., nc: bool = ..., noInvScale: bool = ..., nis: bool = ..., relative: bool = ..., r: bool = ..., removeObject: bool = ..., rm: bool = ..., shape: bool = ..., s: bool = ..., world: bool = ..., w: bool = ...) -> Any:
    r"""
    This command parents (moves) objects under a new group, removes
    objects from an existing group, or adds/removes parents.
    
    If the -w flag is specified all the selected or specified objects
    are parented to the world (unparented first).
    
    If the -rm flag is specified then all the selected or specified
    instances are removed.
    
    If there are more than two objects specified all the objects are
    parented to the last object specified.
    
    If the -add flag is specified, the objects are not reparented but
    also become children of the last object specified.
    
    If there is only a single object specified then the selected objects
    are parented to that object.
    
    If an object is parented under a different group and there is
    an object in that group with the same name then this command
    will rename the parented object.

    Args:
        absolute | a: (create) - preserve existing world object transformations (overall object transformation is preserved by modifying the objects local transformation) If the object to parent is a joint, it will alter the translation and joint orientation of the joint to preserve the world object transformation if this suffices. Otherwise, a transform will be inserted between the joint and the parent for this purpose. In this case, the transformation inside the joint is not altered. [default]
        addObject | add: (create) - preserve existing local object transformations but don't reparent, just add the object(s) under the parent. Use -world to add the world as a parent of the given objects.
        noConnections | nc: (create) - The parent command will normally generate new instanced set connections when adding instances. (ie. make a connection to the shading engine for new instances) This flag suppresses this behaviour and is primarily used by the file format.
        noInvScale | nis: (create) - The parent command will normally connect inverseScale to its parent scale on joints. This is used to compensate scale on joint. The connection of inverseScale will occur if both child and parent are joints and no connection is present on child's inverseScale. In case of a reparenting, the old inverseScale will only get broken if the old parent is a joint. Otherwise connection will remain intact. This flag suppresses this behaviour.
        relative | r: (create) - preserve existing local object transformations (relative to the parent node)
        removeObject | rm: (create) - Remove the immediate parent of every object specified. To remove only a single instance of a shape from a parent, the path to the shape should be specified. Note: if there is a single parent then the object is effectively deleted from the scene. Use -world to remove the world as a parent of the given object.
        shape | s: (create) - The parent command usually only operates on transforms.  Using this flags allows a shape that is specified to be directly parented under the given transform.  This is used to instance a shape node. (ie. "parent -add -shape"    is equivalent to the "instance" command). This flag is primarily used by the file format.
        world | w: (create) - unparent given object(s) (parent to world)
    """
    ...


def partition(*args, addSet: Optional[Union[str, bool]] = ..., add: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., removeSet: Optional[Union[str, bool]] = ..., rm: Optional[Union[str, bool]] = ..., render: bool = ..., re: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to create, query or add/remove sets to a
    partition. If a partition name needs to be specified, it is the first
    argument, other arguments represent the set names.
    
    Without any flags, the command will create a
    partition with a default name.  Any sets which are arguments
    to the command will be added to the partition.
    
    A set can be added to a partition only if none of its members
    are in any of the other sets in the partition. If the -re/render
    flag is specified when the partition is created, only 'renderable'
    sets can be added to the partition.
    
    Sets can be added and removed from a partition by using the
    -addSet or -removeSet flags.
    
    Note: If a set is already selected, and the partition command is
    executed, the set will be added to the created partition.

    Args:
        addSet | add: (create) - Adds the list of sets to the named partition.
        name | n: (create) - Assigns the given name to new partition. Valid only for create mode.
        removeSet | rm: (create) - Removes the list of sets from the named partition.
        render | re: (create, query) - New partition can contain render sets. For use in creation mode only. Default is false.  Can also be used with query flag - returns boolean.
    """
    ...


def performanceOptions(*args, clusterResolution: Optional[Union[float, bool]] = ..., cr: Optional[Union[float, bool]] = ..., disableStitch: Optional[Union[str, bool]] = ..., ds: Optional[Union[str, bool]] = ..., disableTrimBoundaryDisplay: Optional[Union[str, bool]] = ..., dtb: Optional[Union[str, bool]] = ..., disableTrimDisplay: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., latticeResolution: Optional[Union[float, bool]] = ..., lr: Optional[Union[float, bool]] = ..., passThroughBindSkinAndFlexors: Optional[Union[str, bool]] = ..., pbf: Optional[Union[str, bool]] = ..., passThroughBlendShape: Optional[Union[str, bool]] = ..., pbs: Optional[Union[str, bool]] = ..., passThroughCluster: Optional[Union[str, bool]] = ..., pc: Optional[Union[str, bool]] = ..., passThroughDeltaMush: Optional[Union[str, bool]] = ..., pdm: Optional[Union[str, bool]] = ..., passThroughFlexors: Optional[Union[str, bool]] = ..., pf: Optional[Union[str, bool]] = ..., passThroughLattice: Optional[Union[str, bool]] = ..., pl: Optional[Union[str, bool]] = ..., passThroughMeshBoolean: Optional[Union[str, bool]] = ..., pmb: Optional[Union[str, bool]] = ..., passThroughPaintEffects: Optional[Union[str, bool]] = ..., pp: Optional[Union[str, bool]] = ..., passThroughSculpt: Optional[Union[str, bool]] = ..., ps: Optional[Union[str, bool]] = ..., passThroughWire: Optional[Union[str, bool]] = ..., pw: Optional[Union[str, bool]] = ..., regionOfEffect: Optional[Union[str, bool]] = ..., roe: Optional[Union[str, bool]] = ..., skipHierarchyTraversal: bool = ..., sht: bool = ..., useClusterResolution: Optional[Union[str, bool]] = ..., ucr: Optional[Union[str, bool]] = ..., useLatticeResolution: Optional[Union[str, bool]] = ..., ulr: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    Sets the global performance options for the application.  The options allow
    the disabling of features such as stitch surfaces or deformers to
    cut down on computation time in the scene.
    
    Performance options that are in effect may be on all the time, or they can be
    turned on only for interaction.  In the latter case, the options will only
    take effect during UI interaction or playback.
    
    Note that none of these performance options will affect rendering.

    Args:
        clusterResolution | cr: (query) - Sets the global cluster resolution.  This value may range between 0.0 (exact calculation) and 10.0 (rough approximation)
        disableStitch | ds: (query) - Sets the state of stitch surface disablement.  Setting this to "on" suppresses the generation of stitch surfaces. Valid values are "on", "off", "interactive".
        disableTrimBoundaryDisplay | dtb: (query) - Sets the state of trim boundary drawing disablement.  Setting this to "on" suppresses the drawing of surface trim boundaries. Valid values are "on", "off", "interactive".
        disableTrimDisplay | dt: (query) - Sets the state of trim drawing disablement.  Setting this to "on" suppresses the drawing of surface trims. Valid values are "on", "off", "interactive".
        latticeResolution | lr: (query) - Sets the global lattice resolution.  This value may range between 0.0 (exact calculation) and 1.0 (rough approximation)
        passThroughBindSkinAndFlexors | pbf: (query) - Sets the state of bind skin and all flexors pass through. Valid values are "on", "off", "interactive".
        passThroughBlendShape | pbs: (query) - Sets the state of blend shape deformer pass through. Valid values are "on", "off", "interactive".
        passThroughCluster | pc: (query) - Sets the state of cluster deformer pass through. Valid values are "on", "off", "interactive".
        passThroughDeltaMush | pdm: (query) - Sets the state of delta mush deformer pass through. Valid values are "on", "off", "interactive".
        passThroughFlexors | pf: (query) - Sets the state of flexor pass through. Valid values are "on", "off", "interactive".
        passThroughLattice | pl: (query) - Sets the state of lattice deformer pass through. Valid values are "on", "off", "interactive".
        passThroughMeshBoolean | pmb: (query) - Sets the state of mesh booleans pass through. Valid values are "on", "off", "interactive".
        passThroughPaintEffects | pp: (query) - Sets the state of paint effects pass through. Valid values are "on", "off", "interactive".
        passThroughSculpt | ps: (query) - Sets the state of sculpt deformer pass through. Valid values are "on", "off", "interactive".
        passThroughWire | pw: (query) - Sets the state of wire deformer pass through. Valid values are "on", "off", "interactive".
        regionOfEffect | roe: (query) - When enabled, an interactive update of translation commands will attempt to determine which components are being changed and only update effected components as a performance optimization while dragging a manip.
        skipHierarchyTraversal | sht: (query) - When enabled, hierarchy traversal of invisible objects in the scene will be disabled in order to increase performance however this has a side effect of performing redundant viewport refreshes on certain actions such as manipulations, start/end of playback, idle refresh calls, etc.
        useClusterResolution | ucr: (query) - Sets the state of cluster deformer global resolution.  This allows clusters to be calculated at a lower resolution. Valid values are "on", "off", "interactive".
        useLatticeResolution | ulr: (query) - Sets the state of lattice deformer global resolution.  This allows lattices to be calculated at a lower resolution. Valid values are "on", "off", "interactive".
    """
    ...


def pickWalk(*args, direction: Optional[Union[str, bool]] = ..., d: Optional[Union[str, bool]] = ..., recurse: bool = ..., r: bool = ..., type: Optional[Union[str, bool]] = ..., typ: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    The pickWalk command allows you to quickly change the selection list
    relative to the nodes that are currently selected. It is called
    pickWalk, because it walks from one selection list to another
    by unselecting what's currently selected, and selecting nodes that
    are in the specified direction from the currently selected list.
    If you specify objects on the command line, the pickWalk command
    will walk from those objects instead of the selected list.
    
    If the -type flag is instances, then the left and right direction will
    walk to the previous or next instance of the same selected dag node.

    Args:
        direction | d: (create) - The direction to walk from the node. The choices are up | down | left | right | in | out. up walks to the parent node, down to the child node, and left and right to the sibling nodes. If a CV on a surface is selected, the left and right directions walk in the U parameter direction of the surface, and the up and down directions walk in the V parameter direction. In and out are only used if the type flag is 'latticepoints'. Default is right.
        recurse | r: (create) - If specified then recurse down when walking
        type | typ: (create) - The choices are nodes | instances | edgeloop | edgering | faceloop | keys | latticepoints | motiontrailpoints. If type is nodes, then the left and right direction walk to the next dag siblings. If type is instances, the left and right direction walk to the previous or next instance of the same dag node. If type is edgeloop, then the edge loop starting at the first selected edge will be selected. If type is edgering, then the edge ring starting at the first selected edge will be selected. If type is faceloop, and there are two connected quad faces selected which define a face loop, then that face loop will be selected.  edgeloop, edgering and faceloop all remember which was the first edge or faces selected for as long as consecutive selections are made by this command.  They use this information to determine what the "next" loop or ring selection should be.  Users can make selections forwards and backwards by using the direction flag with "left" or "right".  If type is motiontrailpoints, then the left and right direction walk to the previous or next motion trail points respectively.  Default is nodes.
    """
    ...


def pixelMove(*args) -> Any:
    r"""
    The pixelMove command moves objects by what appears as pixel units
    based on the current view. It takes two integer arguments which
    specify the direction in screen space an object should appear to
    move. The vector between the center pixel of the view and the
    specified offset is mapped to some world space vector which defines
    the relative amount to move the selected objects. The mapping is
    dependent upon the view.

    Args:
    """
    ...


def polyAppendFacetCtx(*args, append: bool = ..., ap: bool = ..., exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., isRotateAvailable: bool = ..., isr: bool = ..., maximumNumberOfPoints: Optional[Union[int, bool]] = ..., mp: Optional[Union[int, bool]] = ..., planarConstraint: bool = ..., pc: bool = ..., rotate: Optional[Union[float, bool]] = ..., r: Optional[Union[float, bool]] = ..., subdivision: Optional[Union[int, bool]] = ..., s: Optional[Union[int, bool]] = ..., texture: Optional[Union[int, bool]] = ..., tx: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create a new context to append facets on polygonal objects

    Args:
        append | ap: (create, edit, query) - Allows to switch to polyCreateFacetCtx tool
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        isRotateAvailable | isr: (query) - Tells if the control associated to rotate flag is available. If several edges are already selected and they are not aligned (thus there is no "rotation axis") the rotation is no longer available.
        maximumNumberOfPoints | mp: (create, edit, query) - Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.
        planarConstraint | pc: (create, edit, query) - Allows/avoid new facet to be non-planar. If on, all new points will be projected onto current facet plane. Selected edges will be checked as well.
        rotate | r: (create, edit, query) - Rotate current facet around the first edge selected.
        subdivision | s: (create, edit, query) - Number of sub-edges created for each new edge. Default is 1.
        texture | tx: (create, edit, query) - Number of textures. Default is 1.
    """
    ...


def polyCreaseCtx(*args, createSet: str = ..., cs: str = ..., exists: bool = ..., ex: bool = ..., extendSelection: bool = ..., es: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., relative: bool = ..., r: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create a new context to crease components on polygonal objects

    Args:
        createSet | cs: (edit) - Creates a set for the selected components.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        extendSelection | es: (create, edit, query) - Enable/disable extending selection to all connected creased components.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        relative | r: (create, edit, query) - Enable/disable applying value relative to existing crease value. If disabled, absolute value is applied.
    """
    ...


def polyCreateFacetCtx(*args, append: bool = ..., ap: bool = ..., exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., maximumNumberOfPoints: Optional[Union[int, bool]] = ..., mp: Optional[Union[int, bool]] = ..., planarConstraint: bool = ..., pc: bool = ..., subdivision: Optional[Union[int, bool]] = ..., s: Optional[Union[int, bool]] = ..., texture: Optional[Union[int, bool]] = ..., tx: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create a new context to create polygonal objects

    Args:
        append | ap: (create, edit, query) - Allows to switch to polyAppendFacetCtx tool
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        maximumNumberOfPoints | mp: (create, edit, query) - Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.
        planarConstraint | pc: (create, edit, query) - allows/avoid new facet to be non-planar. If on, all new points will be projected onto current facet plane.
        subdivision | s: (create, edit, query) - Number of subdivisions for each edge. Default: 1
        texture | tx: (create, edit, query) - What texture mechanism to be applied 0=No textures, 1=Normalized, Undistorted textures 2=Unitized textures Default: 0
    """
    ...


def polyCutCtx(*args, deleteFaces: bool = ..., df: bool = ..., exists: bool = ..., ex: bool = ..., extractFaces: bool = ..., ef: bool = ..., extractOffset: Optional[Union[Tuple[float, float, float], bool]] = ..., eo: Optional[Union[Tuple[float, float, float], bool]] = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create a new context to cut facets on polygonal objects

    Args:
        deleteFaces | df: (create, edit, query) - whether to delete the one-half of the cut-faces of the poly.  If true, they are deleted. Default: false
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        extractFaces | ef: (create, edit, query) - whether to extract the cut-faces of the poly into a separate shell.  If true, they are extracted. Default: false
        extractOffset | eo: (create, edit, query) - The displacement offset of the cut faces. Default: 0.5, 0.5, 0.5
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
    """
    ...


def polyCutUVCtx(*args, loopSpeed: Optional[Union[int, bool]] = ..., ls: Optional[Union[int, bool]] = ..., mapBordersColor: Optional[Union[Tuple[float, float, float], bool]] = ..., mbc: Optional[Union[Tuple[float, float, float], bool]] = ..., showCheckerMap: bool = ..., scm: bool = ..., showTextureBorders: bool = ..., stb: bool = ..., showUVShellColoring: bool = ..., ssc: bool = ..., steadyStroke: bool = ..., ss: bool = ..., steadyStrokeDistance: Optional[Union[float, bool]] = ..., ssd: Optional[Union[float, bool]] = ..., symmetry: Optional[Union[int, bool]] = ..., sym: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create a new context to cut UVs on polygonal objects

    Args:
        loopSpeed | ls: (edit, query) - Edit the speed of loop cutting.
        mapBordersColor | mbc: (edit, query) - Color of UV map border edges in 3d view.
        showCheckerMap | scm: (edit, query) - Display checker map.
        showTextureBorders | stb: (edit, query) - Display texture border edges.
        showUVShellColoring | ssc: (edit, query) - Turn on UV shell coloring or not.
        steadyStroke | ss: (edit, query) - Turn on steady stroke or not.
        steadyStrokeDistance | ssd: (edit, query) - The distance for steady stroke.
        symmetry | sym: (edit, query) - Symmetric modeling.
    """
    ...


def polyMergeEdgeCtx(*args, activeNodes: bool = ..., anq: bool = ..., exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., immediate: bool = ..., im: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., previous: bool = ..., pv: bool = ..., reset: bool = ..., rs: bool = ..., toolNode: bool = ..., tnq: bool = ..., caching: bool = ..., cch: bool = ..., constructionHistory: bool = ..., ch: bool = ..., firstEdge: Optional[Union[int, bool]] = ..., fe: Optional[Union[int, bool]] = ..., mergeMode: Optional[Union[int, bool]] = ..., mm: Optional[Union[int, bool]] = ..., mergeTexture: bool = ..., mt: bool = ..., nodeState: Optional[Union[int, bool]] = ..., nds: Optional[Union[int, bool]] = ..., secondEdge: Optional[Union[int, bool]] = ..., se: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Sews two border edges together.
    The new edge is located either on the first, last,
    or between both selected edges, depending on the mode.
    
    Both edges must belong to the same object, and orientations must match
    (i.e. normals on corresponding faces must point in the same direction).
    Edge flags are mandatory.
    
    Create a new context to merge edges on polygonal objects

    Args:
        activeNodes | anq: (query) - Return the active nodes in the tool
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        immediate | im: (edit) - Acts on the object not the tool defaults
        name | n: (create) - If this is a tool command, name the tool appropriately.
        previous | pv: (edit) - Reset to previously stored values
        reset | rs: (edit) - Reset to default values
        toolNode | tnq: (query) - Return the node used for tool defaults
        caching | cch: (create, edit, query) - Toggle caching for all attributes so that no recomputation is needed
        constructionHistory | ch: (create, query) - Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.  Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.
        firstEdge | fe: (create, edit, query) - First edge to merge. Invalid default value to force the value to be set. Default: -1
        mergeMode | mm: (create, edit, query) - Merge mode : 0=first, 1=halfway between both edges, 2=second. Default: 1
        mergeTexture | mt: (create, edit, query) - Boolean which is used to decide if uv coordinates should be merged or not - along with the geometry. Default: false
        nodeState | nds: (create, edit, query) - Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.    The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.    The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute.  Additional details about each of these 3 states follow.     State Description   Normal The normal node state. This is the default.   HasNoEffect   The HasNoEffect option (a.k.a. pass-through), is used in cases where there is an operation on an input producing an output of the same data type. Nearly all deformers support this state, as do a few other nodes. As stated earlier, it is not supported by all nodes.   It’s typical to implement support for the HasNoEffect state in the node’s compute method and to perform appropriate operations. Plug-ins can also support HasNoEffect.   The usual implementation of this state is to copy the input directly to the matching output without applying the algorithm in the node. For deformers, applying this state leaves the input geometry undeformed on the output.     Blocking   This is implemented in the depend node base class and applies to all nodes. Blocking is applied during the evaluation phase to connections. An evaluation request to a blocked connection will return as failures, causing the destination plug to retain its current value. Dirty propagation is indirectly affected by this state since blocked connections are never cleaned.   When a node is set to Blocking the behavior is supposed to be the same as if all outgoing connections were broken. As long as nobody requests evaluation of the blocked node directly it won’t evaluate after that. Note that a blocked node will still respond to getAttr requests but a getAttr on a downstream node will not reevaluate the blocked node.   Setting the root transform of a hierarchy to Blocking won’t automatically influence child transforms in the hierarchy. To do this, you’d need to explicitly set all child nodes to the Blocking state.   For example, to set all child transforms to Blocking, you could use the following script.    import maya.cmds as cmds def blockTree(root): nodesToBlock = [] for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock += cmds.listConnections(node, source=True, destination=True ) for node in {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' % node, 2 )    Applying this script would continue to draw objects but things would not be animated.     Default: kdnNormal
        secondEdge | se: (create, edit, query) - Second edge to merge. Invalid default value to force the value to be set. Default: -1
    """
    ...


def polyMergeFacetCtx(*args, activeNodes: bool = ..., anq: bool = ..., exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., immediate: bool = ..., im: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., previous: bool = ..., pv: bool = ..., reset: bool = ..., rs: bool = ..., toolNode: bool = ..., tnq: bool = ..., caching: bool = ..., cch: bool = ..., constructionHistory: bool = ..., ch: bool = ..., firstFacet: Optional[Union[int, bool]] = ..., ff: Optional[Union[int, bool]] = ..., mergeMode: Optional[Union[int, bool]] = ..., mm: Optional[Union[int, bool]] = ..., nodeState: Optional[Union[int, bool]] = ..., nds: Optional[Union[int, bool]] = ..., secondFacet: Optional[Union[int, bool]] = ..., sf: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The second face becomes a hole in the first face.
    The new holed face is located either on the first, last,
    or between both selected faces, depending on the mode.
    
    Both faces must belong to the same object.
    Facet flags are mandatory.
    
    Create a new context to merge facets on polygonal objects

    Args:
        activeNodes | anq: (query) - Return the active nodes in the tool
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        immediate | im: (edit) - Acts on the object not the tool defaults
        name | n: (create) - If this is a tool command, name the tool appropriately.
        previous | pv: (edit) - Reset to previously stored values
        reset | rs: (edit) - Reset to default values
        toolNode | tnq: (query) - Return the node used for tool defaults
        caching | cch: (create, edit, query) - Toggle caching for all attributes so that no recomputation is needed
        constructionHistory | ch: (create, query) - Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.  Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.
        firstFacet | ff: (create, edit, query) - The number of the first (outer) face to merge.
        mergeMode | mm: (create, edit, query) - This flag specifies how faces are merged: 0: moves second face to first one 1: moves both faces to average 2: moves first face to second one 3, 4, 5: same as above, except faces are projected but not centred 6: Nothing moves. C: Default is None (6).
        nodeState | nds: (create, edit, query) - Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.    The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.    The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute.  Additional details about each of these 3 states follow.     State Description   Normal The normal node state. This is the default.   HasNoEffect   The HasNoEffect option (a.k.a. pass-through), is used in cases where there is an operation on an input producing an output of the same data type. Nearly all deformers support this state, as do a few other nodes. As stated earlier, it is not supported by all nodes.   It’s typical to implement support for the HasNoEffect state in the node’s compute method and to perform appropriate operations. Plug-ins can also support HasNoEffect.   The usual implementation of this state is to copy the input directly to the matching output without applying the algorithm in the node. For deformers, applying this state leaves the input geometry undeformed on the output.     Blocking   This is implemented in the depend node base class and applies to all nodes. Blocking is applied during the evaluation phase to connections. An evaluation request to a blocked connection will return as failures, causing the destination plug to retain its current value. Dirty propagation is indirectly affected by this state since blocked connections are never cleaned.   When a node is set to Blocking the behavior is supposed to be the same as if all outgoing connections were broken. As long as nobody requests evaluation of the blocked node directly it won’t evaluate after that. Note that a blocked node will still respond to getAttr requests but a getAttr on a downstream node will not reevaluate the blocked node.   Setting the root transform of a hierarchy to Blocking won’t automatically influence child transforms in the hierarchy. To do this, you’d need to explicitly set all child nodes to the Blocking state.   For example, to set all child transforms to Blocking, you could use the following script.    import maya.cmds as cmds def blockTree(root): nodesToBlock = [] for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock += cmds.listConnections(node, source=True, destination=True ) for node in {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' % node, 2 )    Applying this script would continue to draw objects but things would not be animated.     Default: kdnNormal
        secondFacet | sf: (create, edit, query) - The number of the second (hole) face to merge.
    """
    ...


def polySelectCtx(*args, exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., mode: Optional[Union[int, bool]] = ..., m: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create a new context to select polygon components

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        mode | m: (create, edit, query) - Edge loop or Edge ring or Border edge mode
    """
    ...


def polySelectEditCtx(*args, adjustEdgeFlow: Optional[Union[float, bool]] = ..., aef: Optional[Union[float, bool]] = ..., divisions: Optional[Union[int, bool]] = ..., div: Optional[Union[int, bool]] = ..., exists: bool = ..., ex: bool = ..., fixQuads: bool = ..., fq: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., insertWithEdgeFlow: bool = ..., ief: bool = ..., smoothingAngle: Optional[Union[float, bool]] = ..., sma: Optional[Union[float, bool]] = ..., splitType: Optional[Union[int, bool]] = ..., stp: Optional[Union[int, bool]] = ..., useEqualMultiplier: bool = ..., uem: bool = ..., absoluteOffset: bool = ..., abo: bool = ..., autoComplete: bool = ..., ac: bool = ..., deleteEdge: bool = ..., de: bool = ..., endVertexOffset: Optional[Union[float, bool]] = ..., evo: Optional[Union[float, bool]] = ..., mode: Optional[Union[int, bool]] = ..., m: Optional[Union[int, bool]] = ..., startVertexOffset: Optional[Union[float, bool]] = ..., svo: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create a new context to select and edit polygonal objects

    Args:
        adjustEdgeFlow | aef: (create, edit, query) - The weight value of the edge vertices to be positioned. Default: 1.0f
        divisions | div: (create, edit, query) - Number of divisions. Default: 2
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        fixQuads | fq: (create, edit, query) - Fixes splits which go across a quad face leaving a 5 and 3 sided faces by splitting from the middle of the new edge to the vertex accross from the edge on the 5 sided face. Default: false
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        insertWithEdgeFlow | ief: (create, edit, query) - True to enable edge flow. Otherwise, the edge flow is disabled. Default: false
        smoothingAngle | sma: (create, edit, query) - Angle below which new edges will be smoothed Default: kPi
        splitType | stp: (create, edit, query) - Format: 0 - Absolute, 1 - Relative, 2 - Multi Default: TdnpolySplitRing::Relative
        useEqualMultiplier | uem: (create, edit, query) - Changes how the profile curve effects the offset when doing a multisplit.  If true then the verts will be offset the same distance based on the shortest edge being split.  If false then each inserted edge loop will be offset a distance relative to the length of the edge that is being split. Default: true
        absoluteOffset | abo: (create, edit, query) - This flag is deprecated. Use splitType/stp instead. This flag is deprecated. Use splitType/stp instead.
        autoComplete | ac: (create) - If true then use auto completion on selections
        deleteEdge | de: (create, edit, query) - When true, the end edges are deleted so the end triangles are converted to quads.
        endVertexOffset | evo: (create, edit, query) - Weight value controlling the offset of the end vertex of the edgeloop.
        mode | m: (create, edit, query) - which mode to work on.  Available modes are 1-loop and 2-ring
        startVertexOffset | svo: (create, edit, query) - Weight value controlling the offset of the start vertex of the edgeloop.
    """
    ...


def polyShortestPathCtx(*args, exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Creates a new context to select shortest edge path
    between two vertices or UVs in the 3d viewport.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
    """
    ...


def polySplitCtx(*args, enablesnap: bool = ..., es: bool = ..., exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., magnetsnap: Optional[Union[int, bool]] = ..., ms: Optional[Union[int, bool]] = ..., precsnap: Optional[Union[float, bool]] = ..., ps: Optional[Union[float, bool]] = ..., smoothingangle: Optional[Union[float, bool]] = ..., sma: Optional[Union[float, bool]] = ..., snaptoedge: bool = ..., ste: bool = ..., subdivision: Optional[Union[int, bool]] = ..., s: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create a new context to split facets on polygonal objects

    Args:
        enablesnap | es: (create, edit, query) - Enable/disable custom magnet snapping to start/middle/end of edge
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        magnetsnap | ms: (create, edit, query) - number of extra magnets to snap onto, regularly spaced along the edge
        precsnap | ps: (create, edit, query) - precision for custom magnet snapping. Range[0,100]. Value 100 means any click on an edge will snap to either extremities or magnets.
        smoothingangle | sma: (create, edit, query) - the threshold that controls whether newly created edges are hard or soft
        snaptoedge | ste: (create, edit, query) - Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to snap to certain points along the edge.
        subdivision | s: (create, edit, query) - number of sub-edges to add between 2 consecutive edge points. Default is 1.
    """
    ...


def polySplitCtx2(*args, exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., adjustEdgeFlow: Optional[Union[float, bool]] = ..., aef: Optional[Union[float, bool]] = ..., constrainToEdges: bool = ..., cte: bool = ..., edgeMagnets: Optional[Union[int, bool]] = ..., em: Optional[Union[int, bool]] = ..., insertWithEdgeFlow: bool = ..., ief: bool = ..., snapTolerance: Optional[Union[float, bool]] = ..., st: Optional[Union[float, bool]] = ..., snappedToEdgeColor: Optional[Union[Tuple[float, float, float], bool]] = ..., sec: Optional[Union[Tuple[float, float, float], bool]] = ..., snappedToFaceColor: Optional[Union[Tuple[float, float, float], bool]] = ..., sfc: Optional[Union[Tuple[float, float, float], bool]] = ..., snappedToMagnetColor: Optional[Union[Tuple[float, float, float], bool]] = ..., smc: Optional[Union[Tuple[float, float, float], bool]] = ..., snappedToVertexColor: Optional[Union[Tuple[float, float, float], bool]] = ..., svc: Optional[Union[Tuple[float, float, float], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create a new context to split facets on polygonal objects

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        adjustEdgeFlow | aef: (create, edit, query) - The weight value of the edge vertices to be positioned.
        constrainToEdges | cte: (create, edit, query) - Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to snap to certain points along the edge.
        edgeMagnets | em: (create, edit, query) - number of extra magnets to snap onto, regularly spaced along the edge
        insertWithEdgeFlow | ief: (create, edit, query) - True to enable edge flow. Otherwise, the edge flow is disabled.
        snapTolerance | st: (create, edit, query) - precision for custom magnet snapping. Range[0,1]. Value 1 means any click on an edge will snap to either extremities or magnets.
        snappedToEdgeColor | sec: (create, edit, query) - Color for edge snapping.
        snappedToFaceColor | sfc: (create, edit, query) - Color for face snapping.
        snappedToMagnetColor | smc: (create, edit, query) - Color for magnet snapping.
        snappedToVertexColor | svc: (create, edit, query) - Color for vertex snapping.
    """
    ...


def projectionContext(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Set the context for projection manips

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def propModCtx(*args, animCurve: Optional[Union[str, bool]] = ..., ac: Optional[Union[str, bool]] = ..., animCurveFalloff: Optional[Union[Tuple[float, float], bool]] = ..., acf: Optional[Union[Tuple[float, float], bool]] = ..., animCurveParam: Optional[Union[str, bool]] = ..., acp: Optional[Union[str, bool]] = ..., direction: Optional[Union[Tuple[float, float, float], bool]] = ..., d: Optional[Union[Tuple[float, float, float], bool]] = ..., exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., linear: Optional[Union[float, bool]] = ..., l: Optional[Union[float, bool]] = ..., linearParam: Optional[Union[Tuple[float, float], bool]] = ..., lp: Optional[Union[Tuple[float, float], bool]] = ..., nurbsCurve: Optional[Union[str, bool]] = ..., nc: Optional[Union[str, bool]] = ..., powerCutoff: Optional[Union[float, bool]] = ..., pc: Optional[Union[float, bool]] = ..., powerCutoffParam: Optional[Union[Tuple[float, float], bool]] = ..., pcp: Optional[Union[Tuple[float, float], bool]] = ..., powerDegree: Optional[Union[float, bool]] = ..., pd: Optional[Union[float, bool]] = ..., powerDegreeParam: Optional[Union[float, bool]] = ..., pdp: Optional[Union[float, bool]] = ..., script: Optional[Union[str, bool]] = ..., s: Optional[Union[str, bool]] = ..., scriptParam: Optional[Union[str, bool]] = ..., sp: Optional[Union[str, bool]] = ..., type: Optional[Union[int, bool]] = ..., t: Optional[Union[int, bool]] = ..., worldspace: bool = ..., ws: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Controls the proportional move context.

    Args:
        animCurve | ac: (create, edit, query) - Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds".  The profile of the curve will be used as the profile for propmod function.
        animCurveFalloff | acf: (create, edit, query) - The profile of the curve will be used as the profile for propmod function in both U and V. This will be scaled in U, V according to the paramters provided. The ratio of the U, V scaling parameters will dictate the footprint of the fuction while the curve itself provides the magnitudes.
        animCurveParam | acp: (create, edit, query) - Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds", where 1 second maps to 0.01 units in parametric space.
        direction | d: (create, edit, query) - Direction along which to compute the distance for the distance based drop-off functions.  The default is (1 1 1)
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        linear | l: (create, edit, query) - If using linear drop-off function, this is its slope.  The default of -0.1 means the point at the locator moves with it and the point 10 units away doesn't move at all.
        linearParam | lp: (create, edit, query) - If using parametric linear drop-off function, these specify its limits along the U and V directions.
        nurbsCurve | nc: (create, edit, query) - Name of the nurbs curve to use as a drop-off curve. The closest point distance would be used as the drop off percentage.
        powerCutoff | pc: (create, edit, query) - If using the power drop-off function, this is its distance cutoff value.  The default is 10.0.
        powerCutoffParam | pcp: (create, edit, query) - If using the power drop-off function, these specify one of it's limits, 0 for U, and 1 and V.  The default cutoff is 10.0.
        powerDegree | pd: (create, edit, query) - If using the power drop-off function, this is its degree.  The default is 3.
        powerDegreeParam | pdp: (create, edit, query) - If using the power drop-off function, this is its degree.  The default is 3.
        script | s: (create, edit, query) - The name of the script to use to compute the drop-off. The script takes 6 floats as input - first 3 are the position of the move locator, the next 3 the position of the point to be manipulated.  The script should return a drop-off coefficient which could be negative or zero.
        scriptParam | sp: (create, edit, query) - The name of the script to use to compute the drop-off. The script takes 4 floats as input - first 2 are the parametric position of the move locator, the next 2 the parametric position of the point to be manipulated.  The script should return a drop-off coefficient which could be negative or zero.
        type | t: (create, edit, query) - Choose the type for the drop-off function.  Legal values are 1 for linear, 2 for power, 3 for script, 4 for anim curve. The default is 1.
        worldspace | ws: (create, edit, query) - Set the space in which the tool works. True for world space, false for parametric space.
    """
    ...


def quit(*args, abort: bool = ..., a: bool = ..., exitCode: Optional[Union[int, bool]] = ..., ec: Optional[Union[int, bool]] = ..., force: bool = ..., f: bool = ...) -> Any:
    r"""
    This command is used to exit the application.

    Args:
        abort | a: (create) - Will quit without saving like -force, but will also prevent preferences/hotkeys/colors from being saved.  Use at your own risk.
        exitCode | ec: (create) - Specifies the exit code to be returned once the application exits.  The default exit code is 0.
        force | f: (create) - If specified, this flag will force a quit without saving or prompting for saving changes. Use at your own risk.
    """
    ...


def regionSelectKeyCtx(*args, bottomManip: Optional[Union[float, bool]] = ..., bot: Optional[Union[float, bool]] = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., leftManip: Optional[Union[float, bool]] = ..., lft: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., rightManip: Optional[Union[float, bool]] = ..., rgt: Optional[Union[float, bool]] = ..., topManip: Optional[Union[float, bool]] = ..., top: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context which may be used to scale keyframes
    within the graph editor using the region select tool.

    Args:
        bottomManip | bot: (query) - Get a point located inside the bottom manipulator of the region box, in screen space.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        leftManip | lft: (query) - Get a point located inside the left manipulator of the region box, in screen space.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        rightManip | rgt: (query) - Get a point located inside the right manipulator of the region box, in screen space.
        topManip | top: (query) - Get a point located inside the top manipulator of the region box, in screen space.
    """
    ...


def relationship(*args, b: bool = ..., relationshipData: Optional[Union[str, bool]] = ..., rd: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This is primarily for use with file IO. Rather than write out the specific attributes/connections required to maintain a relationship, a description of the related nodes/plugs is written instead. The relationship must have an owner node, and have a specific type. During file read, maya will make the connections and/or set the data necessary to represent the realtionship in the dependency graph.

    Args:
        b | b: (create, edit, query) - Break the specified relationship instead of creating it
        relationshipData | rd: (create, edit, multiuse, query) - Provide relationship data to be used when creating the relationship.
    """
    ...


def rememberCtxSettings(*args) -> Any:
    r"""
    This command restores a tool to its saved settings. This command must
    only be called once for each tool created and should be called at the
    point the tool is created.

    Args:
    """
    ...


def removeMultiInstance(*args, allChildren: bool = ..., all: bool = ..., b: bool = ...) -> Any:
    r"""
    Removes a particular instance of a multiElement. This is only
    useful for input attributes since outputs will get regenerated the
    next time the node gets executed. This command will remove the
    instance and optionally break all incoming and outgoing connections
    to that instance. If the connections are not broken (with the -b
    true) flag, then the command will fail if connections exist.

    Args:
        allChildren | all: (create) - If the argument is true, remove all children of the multi parent.
        b | b: (create) - If the argument is true, all connections to the attribute will be broken before the element is removed. If false, then the command will fail if the element is connected.
    """
    ...


def rename(*args, ignoreShape: bool = ..., uuid: bool = ..., uid: bool = ...) -> Any:
    r"""
    Renames the given object to have the new name. If only one
    argument is supplied the command will rename the (first) selected
    object. If the new name conflicts with an existing name, the
    object will be given a unique name based on the supplied name.
    It is not legal to rename an object to the empty string.
    
    When a transform is renamed then any shape nodes beneath the
    transform that have the same prefix as the old transform name
    are renamed. For example, "rename nurbsSphere1 ball" would
    rename "nurbsSphere1|nurbsSphereShape1" to "ball|ballShape".
    
    If the new name ends in a single '#' then the rename command
    will replace the  trailing '#' with a number that ensures
    the new name is unique.
    
    Notes
    If the name has an absolute namespace part, it will be considered.
    Namespaces that do not exist will be created automatically as needed.
    If the name has a relative namespace part, it will be ignored.
    In that case, the object will be put under the current namespace.
    (see example below).

    Args:
        ignoreShape | ignoreShape: (create) - Indicates that renaming of shape nodes below transform nodes should be prevented.
        uuid | uid: (create) - Indicates that the new name is actually a UUID, and that the command should change the node's UUID. (In which case its name remains unchanged.)
    """
    ...


def renameAttr(*args) -> Any:
    r"""
    Renames the given user-defined attribute to the name given in the
    string argument. If the new name conflicts with an existing name then
    this command will fail.
    Note that it is not legal to rename an attribute to the empty string.

    Args:
    """
    ...


def renderWindowSelectContext(*args, exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Set the selection context for the render view panel.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
    """
    ...


def reorder(*args, back: bool = ..., b: bool = ..., front: bool = ..., f: bool = ..., relative: Optional[Union[int, bool]] = ..., r: Optional[Union[int, bool]] = ...) -> Any:
    r"""
    This command reorders (moves) objects relative to their siblings.
    
    For relative moves, both positive and negative numbers may be
    specified.  Positive numbers move the object forward and
    negative numbers move the object backward amoung its
    siblings. When an object is at the end (beginning) of the list
    of siblings, a relative move of 1 (-1) will put the object at
    the beginning (end) of the list of siblings.  That is,
    relative moves will wrap if necessary.
    
    If a shape is specified and it is the only child then its parent
    will be reordered.

    Args:
        back | b: (create) - Move object(s) to back of sibling list.
        front | f: (create) - Move object(s) to front of sibling list.
        relative | r: (create) - Move object(s) relative to other siblings.
    """
    ...


def reorderContainer(*args, back: bool = ..., b: bool = ..., front: bool = ..., f: bool = ..., relative: Optional[Union[int, bool]] = ..., r: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command reorders (moves) objects relative to their siblings in
    a container.
    
    For relative moves, both positive and negative numbers may be
    specified.  Positive numbers move the object forward and
    negative numbers move the object backward amoung its
    siblings. When an object is at the end (beginning) of the list
    of siblings, a relative move of 1 (-1) will put the object at
    the beginning (end) of the list of siblings.  That is,
    relative moves will wrap if necessary.
    
    Only nodes within one container can be moved at a time.
    Note: The container command's -nodeList flag will return a sorted list of
    contained nodes. To see the effects of reordering, use the -unsortedOrder flag
    in conjunction with the -nodeList flag.

    Args:
        back | b: (create, edit, query) - Move object(s) to back of container contents list
        front | f: (create, edit, query) - Move object(s) to front of container contents list
        relative | r: (create, edit, query) - Move object(s) relative to other container contents
    """
    ...


def resetTool(*args) -> Any:
    r"""
    This command resets a tool back to its "factory settings"

    Args:
    """
    ...


def retimeKeyCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., moveByFrame: int = ..., mbf: int = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., snapOnFrame: bool = ..., sof: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context which may be used to scale keyframes
    within the graph editor using the retime tool.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        moveByFrame | mbf: (edit) - Move the selected retime bar by the specified number of frames
        name | n: (create) - If this is a tool command, name the tool appropriately.
        snapOnFrame | sof: (edit, query) - When set, the retime markers will snap on frames as they are moved.
    """
    ...


def rollCtx(*args, alternateContext: bool = ..., ac: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., rollScale: Optional[Union[float, bool]] = ..., rs: Optional[Union[float, bool]] = ..., toolName: Optional[Union[str, bool]] = ..., tn: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create, edit, or query a roll context.

    Args:
        alternateContext | ac: (create, query) - Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        rollScale | rs: (create, edit, query) - In degrees of rotation per 100 pixels of cursor drag.
        toolName | tn: (create, query) - Name of the specific tool to which this command refers.
    """
    ...


def rotate(*args, absolute: bool = ..., a: bool = ..., centerPivot: bool = ..., cp: bool = ..., componentSpace: bool = ..., cs: bool = ..., constrainAlongNormal: bool = ..., xn: bool = ..., deletePriorHistory: bool = ..., dph: bool = ..., euler: bool = ..., eu: bool = ..., forceOrderXYZ: bool = ..., fo: bool = ..., objectCenterPivot: bool = ..., ocp: bool = ..., objectSpace: bool = ..., os: bool = ..., orientAxes: Optional[Union[Tuple[float, float, float], bool]] = ..., oa: Optional[Union[Tuple[float, float, float], bool]] = ..., pivot: Optional[Union[Tuple[float, float, float], bool]] = ..., p: Optional[Union[Tuple[float, float, float], bool]] = ..., preserveChildPosition: bool = ..., pcp: bool = ..., preserveGeometryPosition: bool = ..., pgp: bool = ..., preserveUV: bool = ..., puv: bool = ..., reflection: bool = ..., rfl: bool = ..., reflectionAboutBBox: bool = ..., rab: bool = ..., reflectionAboutOrigin: bool = ..., rao: bool = ..., reflectionAboutX: bool = ..., rax: bool = ..., reflectionAboutY: bool = ..., ray: bool = ..., reflectionAboutZ: bool = ..., raz: bool = ..., reflectionTolerance: Optional[Union[float, bool]] = ..., rft: Optional[Union[float, bool]] = ..., relative: bool = ..., r: bool = ..., rotateX: bool = ..., x: bool = ..., rotateXY: bool = ..., xy: bool = ..., rotateXYZ: bool = ..., xyz: bool = ..., rotateXZ: bool = ..., xz: bool = ..., rotateY: bool = ..., y: bool = ..., rotateYZ: bool = ..., yz: bool = ..., rotateZ: bool = ..., z: bool = ..., symNegative: bool = ..., smn: bool = ..., translate: bool = ..., t: bool = ..., worldSpace: bool = ..., ws: bool = ..., xformConstraint: Optional[Union[str, bool]] = ..., xc: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    The rotate command is used to change the rotation of
    geometric objects. The rotation values are specified as
    Euler angles (rx, ry, rz). The values are interpreted based
    on the current working unit for Angular measurements. Most
    often this is degrees.
    
    The default behaviour, when no objects or flags are passed,
    is to do a absolute rotate on each currently selected object
    in the world space.

    Args:
        absolute | a: (create) - Perform an absolute operation.
        centerPivot | cp: (create) - Let the pivot be the center of the bounding box of all objects
        componentSpace | cs: (create) - Rotate in local component space
        constrainAlongNormal | xn: (create) - When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        deletePriorHistory | dph: (create) - If true then delete the history prior to the current operation.
        euler | eu: (create) - Modifer for -relative flag that specifies rotation values should be added to current XYZ rotation values.
        forceOrderXYZ | fo: (create) - When true, euler rotation value will be understood in XYZ rotation order not per transform node basis.
        objectCenterPivot | ocp: (create) - Let the pivot be the center of the bounding box of each object
        objectSpace | os: (create) - Perform rotation about object-space axis.
        orientAxes | oa: (create) - Euler axis for orientation.
        pivot | p: (create) - Define the pivot point for the transformation
        preserveChildPosition | pcp: (create) - When true, transforming an object will apply an opposite transform to its child transform to keep them at the same world-space position. Default is false.
        preserveGeometryPosition | pgp: (create) - When true, transforming an object will apply an opposite transform to its geometry points to keep them at the same world-space position. Default is false.
        preserveUV | puv: (create) - When true, UV values on rotated components are projected across the rotation in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected vertices. Default is false.
        reflection | rfl: (create) - To move the corresponding symmetric components also.
        reflectionAboutBBox | rab: (create) - Sets the position of the reflection axis  at the geometry bounding box
        reflectionAboutOrigin | rao: (create) - Sets the position of the reflection axis  at the origin
        reflectionAboutX | rax: (create) - Specifies the X=0 as reflection plane
        reflectionAboutY | ray: (create) - Specifies the Y=0 as reflection plane
        reflectionAboutZ | raz: (create) - Specifies the Z=0 as reflection plane
        reflectionTolerance | rft: (create) - Specifies the tolerance to findout the corresponding reflected components
        relative | r: (create) - Perform a operation relative to the object's current position
        rotateX | x: (create) - Rotate in X direction
        rotateXY | xy: (create) - Rotate in X and Y direction
        rotateXYZ | xyz: (create) - Rotate in all directions (default)
        rotateXZ | xz: (create) - Rotate in X and Z direction
        rotateY | y: (create) - Rotate in Y direction
        rotateYZ | yz: (create) - Rotate in Y and Z direction
        rotateZ | z: (create) - Rotate in Z direction
        symNegative | smn: (create) - When set the component transformation is flipped so it is relative to the negative side of the symmetry plane. The default (no flag) is to transform components relative to the positive side of the symmetry plane.
        translate | t: (create) - When true, the command will modify the node's translate attribute instead of its rotateTranslate attribute, when rotating around a pivot other than the object's own rotate pivot.
        worldSpace | ws: (create) - Perform rotation about global world-space axis.
        xformConstraint | xc: (create) - Apply a transform constraint to moving components.  none - no constraint surface - constrain components to the surface edge - constrain components to surface edges live - constraint components to the live surface
    """
    ...


def saveToolSettings(*args) -> Any:
    r"""
    This command causes all the tools not on the
    shelf to save their settings as optionVars.  This
    is called automatically by the system when Maya exits.

    Args:
    """
    ...


def scale(*args, absolute: bool = ..., a: bool = ..., centerPivot: bool = ..., cp: bool = ..., componentSpace: bool = ..., cs: bool = ..., constrainAlongNormal: bool = ..., xn: bool = ..., deletePriorHistory: bool = ..., dph: bool = ..., distanceOnly: bool = ..., dso: bool = ..., localSpace: bool = ..., ls: bool = ..., objectCenterPivot: bool = ..., ocp: bool = ..., objectSpace: bool = ..., os: bool = ..., orientAxes: Optional[Union[Tuple[float, float, float], bool]] = ..., oa: Optional[Union[Tuple[float, float, float], bool]] = ..., pivot: Optional[Union[Tuple[float, float, float], bool]] = ..., p: Optional[Union[Tuple[float, float, float], bool]] = ..., preserveChildPosition: bool = ..., pcp: bool = ..., preserveGeometryPosition: bool = ..., pgp: bool = ..., preserveUV: bool = ..., puv: bool = ..., reflection: bool = ..., rfl: bool = ..., reflectionAboutBBox: bool = ..., rab: bool = ..., reflectionAboutOrigin: bool = ..., rao: bool = ..., reflectionAboutX: bool = ..., rax: bool = ..., reflectionAboutY: bool = ..., ray: bool = ..., reflectionAboutZ: bool = ..., raz: bool = ..., reflectionTolerance: Optional[Union[float, bool]] = ..., rft: Optional[Union[float, bool]] = ..., relative: bool = ..., r: bool = ..., scaleX: bool = ..., x: bool = ..., scaleXY: bool = ..., xy: bool = ..., scaleXYZ: bool = ..., xyz: bool = ..., scaleXZ: bool = ..., xz: bool = ..., scaleY: bool = ..., y: bool = ..., scaleYZ: bool = ..., yz: bool = ..., scaleZ: bool = ..., z: bool = ..., symNegative: bool = ..., smn: bool = ..., worldSpace: bool = ..., ws: bool = ..., xformConstraint: Optional[Union[str, bool]] = ..., xc: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    The scale command is used to change the sizes of geometric
    objects.
    
    The default behaviour, when no objects or flags are passed,
    is to do a relative scale on each currently selected object
    object using each object's existing scale pivot point.

    Args:
        absolute | a: (create) - Perform an absolute operation.
        centerPivot | cp: (create) - Let the pivot be the center of the bounding box of all objects
        componentSpace | cs: (create) - Move in local component space
        constrainAlongNormal | xn: (create) - When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        deletePriorHistory | dph: (create) - If true then delete the history prior to the current operation.
        distanceOnly | dso: (create) - Scale only the distance between the objects.
        localSpace | ls: (create) - Use local space for scaling
        objectCenterPivot | ocp: (create) - Let the pivot be the center of the bounding box of each object
        objectSpace | os: (create) - Use object space for scaling
        orientAxes | oa: (create) - Use the angles for the orient axes.
        pivot | p: (create) - Define the pivot point for the transformation
        preserveChildPosition | pcp: (create) - When true, transforming an object will apply an opposite transform to its child transform to keep them at the same world-space position. Default is false.
        preserveGeometryPosition | pgp: (create) - When true, transforming an object will apply an opposite transform to its geometry points to keep them at the same world-space position. Default is false.
        preserveUV | puv: (create) - When true, UV values on scaled components are projected along the axis of scaling in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected vertices. Default is false.
        reflection | rfl: (create) - To move the corresponding symmetric components also.
        reflectionAboutBBox | rab: (create) - Sets the position of the reflection axis  at the geometry bounding box
        reflectionAboutOrigin | rao: (create) - Sets the position of the reflection axis  at the origin
        reflectionAboutX | rax: (create) - Specifies the X=0 as reflection plane
        reflectionAboutY | ray: (create) - Specifies the Y=0 as reflection plane
        reflectionAboutZ | raz: (create) - Specifies the Z=0 as reflection plane
        reflectionTolerance | rft: (create) - Specifies the tolerance to findout the corresponding reflected components
        relative | r: (create) - Perform a operation relative to the object's current position
        scaleX | x: (create) - Scale in X direction
        scaleXY | xy: (create) - Scale in X and Y direction
        scaleXYZ | xyz: (create) - Scale in all directions (default)
        scaleXZ | xz: (create) - Scale in X and Z direction
        scaleY | y: (create) - Scale in Y direction
        scaleYZ | yz: (create) - Scale in Y and Z direction
        scaleZ | z: (create) - Scale in Z direction
        symNegative | smn: (create) - When set the component transformation is flipped so it is relative to the negative side of the symmetry plane. The default (no flag) is to transform components relative to the positive side of the symmetry plane.
        worldSpace | ws: (create) - Use world space for scaling
        xformConstraint | xc: (create) - Apply a transform constraint to moving components.  none - no constraint surface - constrain components to the surface edge - constrain components to surface edges live - constraint components to the live surface
    """
    ...


def scaleComponents(*args, pivot: Optional[Union[Tuple[float, float, float], bool]] = ..., p: Optional[Union[Tuple[float, float, float], bool]] = ..., rotation: Optional[Union[Tuple[float, float, float], bool]] = ..., ro: Optional[Union[Tuple[float, float, float], bool]] = ...) -> Any:
    r"""
    This is a limited version of the scale command.  First, it
    only works on selected components. You provide a pivot in
    world space, and you can provide a rotation.  This rotation
    affects the scaling, so that rather than scaling in X, Y, Z,
    this is scaling in X, Y, and Z after they have been rotated
    by the given rotation.
    
    This allows selected components to be scaled in any arbitrary
    space, not just object or world space as the regular scale
    allows.
    
    Scale values are always relative, not absolute.

    Args:
        pivot | p: (create) - The pivot position in world space (default is origin)
        rotation | ro: (create) - The rotational offset for the scaling (default is none)
    """
    ...


def scaleKeyCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., scaleSpecifiedKeys: bool = ..., ssk: bool = ..., type: Optional[Union[str, bool]] = ..., typ: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context which may be used to scale keyframes
    within the graph editor

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        scaleSpecifiedKeys | ssk: (edit, query) - Determines if only the specified keys should be scaled. If false, the non-selected keys will be adjusted during the scale. The default is true.
        type | typ: (edit, query) - rect | manip Specifies the type of scale manipulator to use (Note: "rect" is a manipulator style context, and "manip" is a gestural style context)
    """
    ...


def sceneLint(*args, issueType: Optional[Union[str, bool]] = ..., i: Optional[Union[str, bool]] = ..., verbose: bool = ..., v: bool = ..., query: bool = ...) -> Any:
    r"""
    {
            "sceneLint" : {
                    "ISSUE_CODE" : {
                            "description" : "DETAILED_DESCRIPTION_OF_ISSUE",
                            "mitigation" : [        // List of mitigations that can be applied
                                    {
                                            "objects"     : [ LIST_OF_STRINGS_NAMING_OBJECTS_TO_WHICH_IT_APPLIES ],
                                            "benefit"     : DESCRIPTION_OF_HOW_THE_CODE_MAKES_THE_SCENE_BETTER,
                                            "description" : DESCRIPTION_OF_WHAT_THE_CODE_DOES,
                                            "code"        : PYTHON_MITIGATION_CODE_WITH_LOOP_OVER_INSTANCES
                                    }
                            ]
                    }
            }
    }
    
    The sceneLint command is used to analyze the currently loaded scene
    to find potential areas for improvement in performance, memory use, or reduction
    of clutter.
    
    
    In the query mode it will report back the list of available checks it can do.
    Each check will have an associated short-form which can be passed to the command
    to run specific checks.
    
    
    In create mode the returned string is a JSON format list of issues and mitigations
    that suggest a way to solve the problem it describes.
    
    
    Mitigation can be automatically performed by extracting the mitigation code and arguments
    then running the Python code exec(code, {}, {'OBJECTS' : objects})

    Args:
        issueType | i: (create, multiuse, query) - Specify a set of issue types to be checked. If omitted then all known issue types are checked. In query mode returns a description of what a particular issue type is checking. 			In query mode, this flag can accept a value.
        verbose | v: (create, query) - If set then include both name and description when querying the list of available issue types.
    """
    ...


def scriptCtx(*args, allComponents: bool = ..., alc: bool = ..., allObjects: bool = ..., alo: bool = ..., animBreakdown: bool = ..., abd: bool = ..., animCurve: bool = ..., ac: bool = ..., animInTangent: bool = ..., ait: bool = ..., animKeyframe: bool = ..., ak: bool = ..., animOutTangent: bool = ..., aot: bool = ..., baseClassName: Optional[Union[str, bool]] = ..., bcn: Optional[Union[str, bool]] = ..., camera: bool = ..., ca: bool = ..., cluster: bool = ..., cl: bool = ..., collisionModel: bool = ..., clm: bool = ..., controlVertex: bool = ..., cv: bool = ..., cumulativeLists: bool = ..., cls: bool = ..., curve: bool = ..., c: bool = ..., curveKnot: bool = ..., ck: bool = ..., curveOnSurface: bool = ..., cos: bool = ..., curveParameterPoint: bool = ..., cpp: bool = ..., dimension: bool = ..., dim: bool = ..., dynamicConstraint: bool = ..., dc: bool = ..., edge: bool = ..., eg: bool = ..., editPoint: bool = ..., ep: bool = ..., emitter: bool = ..., em: bool = ..., enableRootSelection: bool = ..., ers: bool = ..., escToQuit: bool = ..., esc: bool = ..., exists: bool = ..., ex: bool = ..., exitUponCompletion: bool = ..., euc: bool = ..., expandSelectionList: bool = ..., esl: bool = ..., facet: bool = ..., fc: bool = ..., field: bool = ..., fi: bool = ..., finalCommandScript: Optional[Union[str, bool]] = ..., fcs: Optional[Union[str, bool]] = ..., fluid: bool = ..., fl: bool = ..., follicle: bool = ..., fo: bool = ..., forceAddSelect: bool = ..., fas: bool = ..., hairSystem: bool = ..., hs: bool = ..., handle: bool = ..., ha: bool = ..., history: bool = ..., ch: bool = ..., hull: bool = ..., hl: bool = ..., ignoreInvalidItems: bool = ..., iii: bool = ..., ikEndEffector: bool = ..., iee: bool = ..., ikHandle: bool = ..., ikh: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., imagePlane: bool = ..., ip: bool = ..., implicitGeometry: bool = ..., ig: bool = ..., isoparm: bool = ..., iso: bool = ..., joint: bool = ..., j: bool = ..., jointPivot: bool = ..., jp: bool = ..., lastAutoComplete: bool = ..., lac: bool = ..., lattice: bool = ..., la: bool = ..., latticePoint: bool = ..., lp: bool = ..., light: bool = ..., lt: bool = ..., localRotationAxis: bool = ..., ra: bool = ..., locator: bool = ..., lc: bool = ..., locatorUV: bool = ..., luv: bool = ..., locatorXYZ: bool = ..., xyz: bool = ..., nCloth: bool = ..., ncl: bool = ..., nParticle: bool = ..., npr: bool = ..., nParticleShape: bool = ..., nps: bool = ..., nRigid: bool = ..., nr: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., nonlinear: bool = ..., nl: bool = ..., nurbsCurve: bool = ..., nc: bool = ..., nurbsSurface: bool = ..., ns: bool = ..., objectComponent: bool = ..., ocm: bool = ..., orientationLocator: bool = ..., ol: bool = ..., particle: bool = ..., pr: bool = ..., particleShape: bool = ..., ps: bool = ..., plane: bool = ..., pl: bool = ..., polymesh: bool = ..., p: bool = ..., polymeshEdge: bool = ..., pe: bool = ..., polymeshFace: bool = ..., pf: bool = ..., polymeshFreeEdge: bool = ..., pfe: bool = ..., polymeshUV: bool = ..., puv: bool = ..., polymeshVertex: bool = ..., pv: bool = ..., polymeshVtxFace: bool = ..., pvf: bool = ..., rigidBody: bool = ..., rb: bool = ..., rigidConstraint: bool = ..., rc: bool = ..., rotatePivot: bool = ..., rp: bool = ..., scalePivot: bool = ..., sp: bool = ..., sculpt: bool = ..., sc: bool = ..., selectHandle: bool = ..., sh: bool = ..., setAllowExcessCount: bool = ..., sae: bool = ..., setAutoComplete: bool = ..., sac: bool = ..., setAutoToggleSelection: bool = ..., sat: bool = ..., setDoneSelectionPrompt: Optional[Union[str, bool]] = ..., dsp: Optional[Union[str, bool]] = ..., setNoSelectionHeadsUp: Optional[Union[str, bool]] = ..., snh: Optional[Union[str, bool]] = ..., setNoSelectionPrompt: Optional[Union[str, bool]] = ..., snp: Optional[Union[str, bool]] = ..., setSelectionCount: Optional[Union[int, bool]] = ..., ssc: Optional[Union[int, bool]] = ..., setSelectionHeadsUp: Optional[Union[str, bool]] = ..., ssh: Optional[Union[str, bool]] = ..., setSelectionPrompt: Optional[Union[str, bool]] = ..., ssp: Optional[Union[str, bool]] = ..., showManipulators: bool = ..., sm: bool = ..., spring: bool = ..., spr: bool = ..., springComponent: bool = ..., spc: bool = ..., stroke: bool = ..., str: bool = ..., subdiv: bool = ..., sd: bool = ..., subdivMeshEdge: bool = ..., sme: bool = ..., subdivMeshFace: bool = ..., smf: bool = ..., subdivMeshPoint: bool = ..., smp: bool = ..., subdivMeshUV: bool = ..., smu: bool = ..., surfaceEdge: bool = ..., se: bool = ..., surfaceFace: bool = ..., sf: bool = ..., surfaceKnot: bool = ..., sk: bool = ..., surfaceParameterPoint: bool = ..., spp: bool = ..., surfaceRange: bool = ..., sr: bool = ..., surfaceUV: bool = ..., suv: bool = ..., texture: bool = ..., tx: bool = ..., title: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ..., toolCursorType: Optional[Union[str, bool]] = ..., tct: Optional[Union[str, bool]] = ..., toolFinish: Optional[Union[str, bool]] = ..., tf: Optional[Union[str, bool]] = ..., toolStart: Optional[Union[str, bool]] = ..., ts: Optional[Union[str, bool]] = ..., totalSelectionSets: Optional[Union[int, bool]] = ..., tss: Optional[Union[int, bool]] = ..., vertex: bool = ..., v: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command allows a user to create their own tools based on
    the selection tool. A number of selection lists can be collected,
    the behaviour of the selection and the selection masks are fully
    customizable, etc.
    
    The command is processed prior to being executed.  The keyword
    "$Selection#" where # is a number 1 or greater specifies
    a selection set.  The context can specify several selection sets
    which are substituted in place of the $Selection# keyword in the form
    of a Mel string array.  Items that are specific per set need to
    be specified in each set, if they are going to be specified for any of
    the sets.  See examples below.
    
    In addition, in order to specify the type of selection you need
    to be making, any of the selection type flags from "selectType" command
    can be used here.

    Args:
        allComponents | alc: (create, multiuse, query) - Set all component selection masks on/off
        allObjects | alo: (create, multiuse, query) - Set all object selection masks on/off
        animBreakdown | abd: (create, multiuse, query) - Set animation breakdown selection mask on/off.
        animCurve | ac: (create, multiuse, query) - Set animation curve selection mask on/off.
        animInTangent | ait: (create, multiuse, query) - Set animation in-tangent selection mask on/off.
        animKeyframe | ak: (create, multiuse, query) - Set animation keyframe selection mask on/off.
        animOutTangent | aot: (create, multiuse, query) - Set animation out-tangent selection mask on/off.
        baseClassName | bcn: (create, edit, query) - This string will be used to produce MEL function names for the property sheets for the tool.  For example, if "myScriptTool" was given, the functions "myScriptToolValues" and "myScriptToolProperties" will be used for the property sheets.  The default is "scriptTool".
        camera | ca: (create, multiuse, query) - Set camera selection mask on/off. (object flag)
        cluster | cl: (create, multiuse, query) - Set cluster selection mask on/off. (object flag)
        collisionModel | clm: (create, multiuse, query) - Set collision model selection mask on/off. (object flag)
        controlVertex | cv: (create, multiuse, query) - Set control vertex selection mask on/off. (component flag)
        cumulativeLists | cls: (create, edit, query) - If set, the selection lists will be cumulative.  For example, the second list will contain all the items from the first list, the third all the items from the second list etc.  Make sure your script specified above takes that into account.  Relevant if there is more than one selection set.
        curve | c: (create, multiuse, query) - Set curve selection mask on/off. (object flag)
        curveKnot | ck: (create, multiuse, query) - Set curve knot selection mask on/off. (component flag)
        curveOnSurface | cos: (create, multiuse, query) - Set curve-on-surface selection mask on/off. (object flag)
        curveParameterPoint | cpp: (create, multiuse, query) - Set curve parameter point selection mask on/off. (component flag)
        dimension | dim: (create, multiuse, query) - Set dimension shape selection mask on/off. (object flag)
        dynamicConstraint | dc: (create, multiuse, query) - Set dynamicConstraint selection mask on/off. (object flag)
        edge | eg: (create, multiuse, query) - Set mesh edge selection mask on/off. (component flag)
        editPoint | ep: (create, multiuse, query) - Set edit-point selection mask on/off. (component flag)
        emitter | em: (create, multiuse, query) - Set emitter selection mask on/off. (object flag)
        enableRootSelection | ers: (create, edit, query) - If set, the items to be selected are at their root transform level. Default is false.
        escToQuit | esc: (create, edit, query) - If set to true, exit the tool when press "Esc". Default is false.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        exitUponCompletion | euc: (create, edit, query) - If set, completing the last selection set will exit the tool.  Default is true.
        expandSelectionList | esl: (create, edit, query) - If set, the selection lists will expand to have a single component in each item.  You probably want this as a default, otherwise two isoparms on the same surface will show up as 1 item.  To ensure that components on the same object are returned in the order in which they are selected, use the selectPref -trackSelectionOrder on command in your -toolStart script to enable ordered selection, then restore it to its original value in your -toolFinish script.
        facet | fc: (create, multiuse, query) - Set mesh face selection mask on/off. (component flag)
        field | fi: (create, multiuse, query) - Set field selection mask on/off. (object flag)
        finalCommandScript | fcs: (create, edit, query) - Supply the script that will be run when the user presses the enter key and the context is completed.  Depending on the number of selection sets you have, the script can make use of variables string $Selection1[], $Selection2[], ...
        fluid | fl: (create, multiuse, query) - Set fluid selection mask on/off. (object flag)
        follicle | fo: (create, multiuse, query) - Set follicle selection mask on/off. (object flag)
        forceAddSelect | fas: (create, edit, query) - If set to true, together with -setAutoToggleSelection (see below) on the first selection set, causes the first selection after the computation of the previous result to be "shift" selection, unless a modifier key is pressed.  Default is false. Flags for each selection set.  These flags are multi-use.
        hairSystem | hs: (create, multiuse, query) - Set hairSystem selection mask on/off. (object flag)
        handle | ha: (create, multiuse, query) - Set object handle selection mask on/off. (object flag)
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        hull | hl: (create, multiuse, query) - Set hull selection mask on/off. (component flag)
        ignoreInvalidItems | iii: (create, edit, query) - If you have multiple selection sets, the state of the selection set is recorded at the time you "complete it".  You could then delete some of the items in that list and end up with invalid items in one or more of your selection sets.  If this flag is set, those items will be detected and ignored.  You will never know it happened.  Its as if they were never selected in the first place, except that your selection set now does not have as many items as it may need.  If this flag is not set, you will get a warning and your final command callback script will likely not execute because of an error condition.
        ikEndEffector | iee: (create, multiuse, query) - Set ik end effector selection mask on/off. (object flag)
        ikHandle | ikh: (create, multiuse, query) - Set ik handle selection mask on/off. (object flag)
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        imagePlane | ip: (create, multiuse, query) - Set image plane selection mask on/off. (component flag)
        implicitGeometry | ig: (create, multiuse, query) - Set implicit geometry selection mask on/off. (object flag)
        isoparm | iso: (create, multiuse, query) - Set surface iso-parm selection mask on/off. (component flag)
        joint | j: (create, multiuse, query) - Set ik handle selection mask on/off. (object flag)
        jointPivot | jp: (create, multiuse, query) - Set joint pivot selection mask on/off. (component flag)
        lastAutoComplete | lac: (create, edit, query) - True if auto complete is set for the last selection set, false otherwise.  Mostly used for query, but if present in conjuction with -sac/setAutoComplete flag, -sac flag takes precedence.
        lattice | la: (create, multiuse, query) - Set lattice selection mask on/off. (object flag)
        latticePoint | lp: (create, multiuse, query) - Set lattice point selection mask on/off. (component flag)
        light | lt: (create, multiuse, query) - Set light selection mask on/off. (object flag)
        localRotationAxis | ra: (create, multiuse, query) - Set local rotation axis selection mask on/off. (component flag)
        locator | lc: (create, multiuse, query) - Set locator (all types) selection mask on/off. (object flag)
        locatorUV | luv: (create, multiuse, query) - Set uv locator selection mask on/off. (object flag)
        locatorXYZ | xyz: (create, multiuse, query) - Set xyz locator selection mask on/off. (object flag)
        nCloth | ncl: (create, multiuse, query) - Set nCloth selection mask on/off. (object flag)
        nParticle | npr: (create, multiuse, query) - Set nParticle point selection mask on/off. (component flag)
        nParticleShape | nps: (create, multiuse, query) - Set nParticle shape selection mask on/off. (object flag)
        nRigid | nr: (create, multiuse, query) - Set nRigid selection mask on/off. (object flag)
        name | n: (create) - If this is a tool command, name the tool appropriately.
        nonlinear | nl: (create, multiuse, query) - Set nonlinear selection mask on/off. (object flag)
        nurbsCurve | nc: (create, multiuse, query) - Set nurbs-curve selection mask on/off. (object flag)
        nurbsSurface | ns: (create, multiuse, query) - Set nurbs-surface selection mask on/off. (object flag)
        objectComponent | ocm: (create, query) - Component flags apply to object mode.
        orientationLocator | ol: (create, multiuse, query) - Set orientation locator selection mask on/off. (object flag)
        particle | pr: (create, multiuse, query) - Set particle point selection mask on/off. (component flag)
        particleShape | ps: (create, multiuse, query) - Set particle shape selection mask on/off. (object flag)
        plane | pl: (create, multiuse, query) - Set sketch plane selection mask on/off. (object flag)
        polymesh | p: (create, multiuse, query) - Set poly-mesh selection mask on/off. (object flag)
        polymeshEdge | pe: (create, multiuse, query) - Set poly-mesh edge selection mask on/off. (component flag)
        polymeshFace | pf: (create, multiuse, query) - Set poly-mesh face selection mask on/off. (component flag)
        polymeshFreeEdge | pfe: (create, multiuse, query) - Set poly-mesh free-edge selection mask on/off. (component flag)
        polymeshUV | puv: (create, multiuse, query) - Set poly-mesh UV point selection mask on/off. (component flag)
        polymeshVertex | pv: (create, multiuse, query) - Set poly-mesh vertex selection mask on/off. (component flag)
        polymeshVtxFace | pvf: (create, multiuse, query) - Set poly-mesh vertexFace selection mask on/off. (component flag)
        rigidBody | rb: (create, multiuse, query) - Set rigid body selection mask on/off. (object flag)
        rigidConstraint | rc: (create, multiuse, query) - Set rigid constraint selection mask on/off. (object flag)
        rotatePivot | rp: (create, multiuse, query) - Set rotate pivot selection mask on/off. (component flag)
        scalePivot | sp: (create, multiuse, query) - Set scale pivot selection mask on/off. (component flag)
        sculpt | sc: (create, multiuse, query) - Set sculpt selection mask on/off. (object flag)
        selectHandle | sh: (create, multiuse, query) - Set select handle selection mask on/off. (component flag)
        setAllowExcessCount | sae: (create, edit, multiuse) - If set, the number if items is to be interpreted as the minimum.
        setAutoComplete | sac: (create, edit, multiuse) - If set to true, as soon as the specified number of items is selected the tool will start the next selection set or run the command.
        setAutoToggleSelection | sat: (create, edit, multiuse) - If set to true, it is as if "shift" key is pressed when there are no modifiers pressed.  That means that you get the "toggle select" behaviour by default.  This only applies to the 3D view, and the selection done in the hypergraph, outliner or elsewhere is still a subject to the usual rules.
        setDoneSelectionPrompt | dsp: (create, edit, multiuse) - If setAutoComplete is not set (see below) this string will be shown as soon as the tool has enough items for a particular selection set.  If this is not set, but is needed, the same string as set with -setSelectionPrompt flag will be used.
        setNoSelectionHeadsUp | snh: (create, edit, multiuse) - Supply a string that will be shown as a heads up prompt when there is nothing selected.  This must be set separately for each selection set.
        setNoSelectionPrompt | snp: (create, edit, multiuse) - Supply a string that will be shown as help when there is nothing selected.  This must be set separately for each selection set.
        setSelectionCount | ssc: (create, edit, multiuse) - The number of items in this selection set.  0 means as many as you need until completion.
        setSelectionHeadsUp | ssh: (create, edit, multiuse) - Supply a string that will be shown as a heads up prompt when there is something selected.  This must be set separately for each selection set.
        setSelectionPrompt | ssp: (create, edit, multiuse) - Supply a string that will be shown as help when there is something selected.  This must be set separately for each selection set.
        showManipulators | sm: (create, edit, query) - If set, the manipulators will be shown for any active objects. Basically, it is as if you are in the Show Manipulator tool.
        spring | spr: (create, multiuse, query) - Set spring shape selection mask on/off. (object flag)
        springComponent | spc: (create, multiuse, query) - Set individual spring selection mask on/off. (component flag)
        stroke | str: (create, multiuse, query) - Set the Paint Effects stroke selection mask on/off. (object flag)
        subdiv | sd: (create, multiuse, query) - Set subdivision surfaces selection mask on/off. (object flag)
        subdivMeshEdge | sme: (create, multiuse, query) - Set subdivision surfaces mesh edge selection mask on/off. (component flag)
        subdivMeshFace | smf: (create, multiuse, query) - Set subdivision surfaces mesh face selection mask on/off. (component flag)
        subdivMeshPoint | smp: (create, multiuse, query) - Set subdivision surfaces mesh point selection mask on/off. (component flag)
        subdivMeshUV | smu: (create, multiuse, query) - Set subdivision surfaces mesh UV map selection mask on/off. (component flag)
        surfaceEdge | se: (create, multiuse, query) - Set surface edge selection mask on/off. (component flag)
        surfaceFace | sf: (create, multiuse, query) - Set surface face selection mask on/off. (component flag)
        surfaceKnot | sk: (create, multiuse, query) - Set surface knot selection mask on/off. (component flag)
        surfaceParameterPoint | spp: (create, multiuse, query) - Set surface parameter point selection mask on/off. (component flag)
        surfaceRange | sr: (create, multiuse, query) - Set surface range selection mask on/off. (component flag)
        surfaceUV | suv: (create, multiuse, query) - Set surface uv selection mask on/off. (component flag)
        texture | tx: (create, multiuse, query) - Set texture selection mask on/off. (object flag)
        title | t: (create, edit, query) - Supply a string that will be used as a precursor to all the messages; i.e., the "name" of the tool.
        toolCursorType | tct: (create, edit, query) - Supply the string identifier to set the tool cursor type when inside of tool. The following are the valid ids: "create", "dolly", "edit", "pencil", "track", "trackHorizontal", "trackVertical", "transformation", "tumble", "zoom", "zoomIn", "zoomOut", "flyThrough", "dot", "fleur", "leftArrow", "question", "doubleHorizArrow", "doubleVertArrow", "sizing", "dollyIn", "dollyOut", "brush", "camera", "noAccess", "input", "output", "leftCycle", "rightCycle", "rightExpand", "knife".
        toolFinish | tf: (create, edit, query) - Supply the script that will be run when the user exits the script.
        toolStart | ts: (create, edit, query) - Supply the script that will be run when the user first enters the script
        totalSelectionSets | tss: (create, edit, query) - Total number of selection sets.
        vertex | v: (create, multiuse, query) - Set mesh vertex selection mask on/off. (component flag)
    """
    ...


def sculptKeyCtx(*args, activeMode: Optional[Union[int, bool]] = ..., am: Optional[Union[int, bool]] = ..., brushScaling: Optional[Union[int, bool]] = ..., brs: Optional[Union[int, bool]] = ..., editingRadius: bool = ..., er: bool = ..., editingStrength: bool = ..., es: bool = ..., exists: bool = ..., ex: bool = ..., falloffCurve: Optional[Union[str, bool]] = ..., fc: Optional[Union[str, bool]] = ..., falloffCurveAll: Optional[Union[str, bool]] = ..., fca: Optional[Union[str, bool]] = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., minRadius: Optional[Union[float, bool]] = ..., mr: Optional[Union[float, bool]] = ..., minStrength: Optional[Union[float, bool]] = ..., ms: Optional[Union[float, bool]] = ..., minStrengthAll: Optional[Union[str, bool]] = ..., msa: Optional[Union[str, bool]] = ..., mode: Optional[Union[int, bool]] = ..., m: Optional[Union[int, bool]] = ..., modeMinStrength: Optional[Union[Tuple[int, float], bool]] = ..., mms: Optional[Union[Tuple[int, float], bool]] = ..., modeStrength: Optional[Union[Tuple[int, float], bool]] = ..., mst: Optional[Union[Tuple[int, float], bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., radius: Optional[Union[float, bool]] = ..., r: Optional[Union[float, bool]] = ..., reset: bool = ..., rs: bool = ..., strength: Optional[Union[float, bool]] = ..., s: Optional[Union[float, bool]] = ..., strengthAll: Optional[Union[str, bool]] = ..., sa: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context which may be used to
    deform key frames with a sculpt brush. This context
    only works in the graph editor.

    Args:
        activeMode | am: (query) - Used to query the current active sculpt mode. This can differ from the base mode if the user is holding down the shift hotkey to temporarily switch to smooth mode.
        brushScaling | brs: (create, edit, query) - Specifies how the sculpt brush scales relative to the Graph Editor. 1 = no scaling, 2 = scaling based on time, 3 = scaling based on value
        editingRadius | er: (create, edit) - Enables or disables interactive radius scaling.
        editingStrength | es: (create, edit) - Enables or disables interactive strength scaling.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        falloffCurve | fc: (create, edit, query) - Specifies the falloff curve of the sculpting effect.
        falloffCurveAll | fca: (create, edit, query) - Internal flag used to save/restore falloff curves for all modes.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        minRadius | mr: (create, edit, query) - Specifies the minumum radius the sculpt brush will take due to stylus pressure. Cannot be more than the base brush radius.
        minStrength | ms: (create, edit, query) - Specifies the minumum strength of sculpting due to stylus pressure. Cannot be more than the base strength.
        minStrengthAll | msa: (create, edit, query) - Internal flag used to save/restore min strength for all modes.
        mode | m: (create, edit, query) - Specifies the base sculpt mode. 0 = grab, 1 = smooth 2 = smear
        modeMinStrength | mms: (create, edit, multiuse) - Specifies the min strength for the specified mode.
        modeStrength | mst: (create, edit, multiuse) - Specifies the strength for the specified mode.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        radius | r: (create, edit, query) - Specifies the radius of the sculpt brush.
        reset | rs: (edit, query) - Internal flag used to reset current tool mode settings.
        strength | s: (create, edit, query) - Specifies the strength of the sculpting effect for the current mode. Each mode can have a different strength.
        strengthAll | sa: (create, edit, query) - Internal flag used to save/restore strength for all modes.
    """
    ...


def sculptMeshCacheChangeCloneSource(*args, blendShape: Optional[Union[str, bool]] = ..., bs: Optional[Union[str, bool]] = ..., target: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command changes the source blend shape and target for the
    clone target tool. Used internally for undo/redo, and should not be called directly.

    Args:
        blendShape | bs: (create, edit, query) - Set which blend shape should be used as the source when using the clone tool. When queried, returns the current blend shape name as a string.
        target | t: (create, edit, query) - Set which blend shape should be used as the target when using the clone tool. When queried, returns the current blend shape target name as a string.
    """
    ...


def sculptMeshCacheCtx(*args, adjustSize: bool = ..., asz: bool = ..., adjustStrength: bool = ..., ast: bool = ..., affectAllLayers: bool = ..., aal: bool = ..., brushDirection: Optional[Union[int, bool]] = ..., bd: Optional[Union[int, bool]] = ..., brushSize: Optional[Union[float, bool]] = ..., bsz: Optional[Union[float, bool]] = ..., brushStrength: Optional[Union[float, bool]] = ..., bst: Optional[Union[float, bool]] = ..., buildUpRate: Optional[Union[float, bool]] = ..., bur: Optional[Union[float, bool]] = ..., cloneHideSource: bool = ..., chs: bool = ..., cloneMethod: Optional[Union[int, bool]] = ..., cm: Optional[Union[int, bool]] = ..., cloneShapeSource: Optional[Union[str, bool]] = ..., css: Optional[Union[str, bool]] = ..., cloneTargetSource: Optional[Union[str, bool]] = ..., cas: Optional[Union[str, bool]] = ..., constrainToSurface: bool = ..., cts: bool = ..., direction: Optional[Union[int, bool]] = ..., d: Optional[Union[int, bool]] = ..., displayFrozen: bool = ..., df: bool = ..., displayMask: bool = ..., dm: bool = ..., displayWireframe: bool = ..., dw: bool = ..., falloffType: Optional[Union[int, bool]] = ..., ft: Optional[Union[int, bool]] = ..., flood: Optional[Union[float, bool]] = ..., fl: Optional[Union[float, bool]] = ..., floodFreeze: Optional[Union[float, bool]] = ..., ff: Optional[Union[float, bool]] = ..., frame: bool = ..., frm: bool = ..., freezeSelection: bool = ..., fsl: bool = ..., grabFollowPath: bool = ..., gfp: bool = ..., grabSilhouette: bool = ..., gs: bool = ..., grabTwist: bool = ..., gtw: bool = ..., inverted: bool = ..., inv: bool = ..., lastMode: Optional[Union[str, bool]] = ..., lm: Optional[Union[str, bool]] = ..., lockShellBorder: bool = ..., lsb: bool = ..., makeStroke: Tuple[int, int, int, float, float] = ..., mt: Tuple[int, int, int, float, float] = ..., minSize: Optional[Union[float, bool]] = ..., msz: Optional[Union[float, bool]] = ..., minStrength: Optional[Union[float, bool]] = ..., mst: Optional[Union[float, bool]] = ..., mirror: Optional[Union[int, bool]] = ..., mr: Optional[Union[int, bool]] = ..., mode: Optional[Union[str, bool]] = ..., m: Optional[Union[str, bool]] = ..., orientToSurface: bool = ..., ots: bool = ..., recordStroke: bool = ..., rcs: bool = ..., sculptFalloffCurve: Optional[Union[str, bool]] = ..., sfc: Optional[Union[str, bool]] = ..., size: Optional[Union[float, bool]] = ..., sz: Optional[Union[float, bool]] = ..., stampDistance: Optional[Union[float, bool]] = ..., s: Optional[Union[float, bool]] = ..., stampFile: Optional[Union[str, bool]] = ..., stp: Optional[Union[str, bool]] = ..., stampFlipX: bool = ..., sfx: bool = ..., stampFlipY: bool = ..., sfy: bool = ..., stampOrientToStroke: bool = ..., sos: bool = ..., stampPlacement: Optional[Union[int, bool]] = ..., sp: Optional[Union[int, bool]] = ..., stampRandomization: bool = ..., srd: bool = ..., stampRandomizationSeed: int = ..., sre: int = ..., stampRandomizeFlipX: bool = ..., srx: bool = ..., stampRandomizeFlipY: bool = ..., sry: bool = ..., stampRandomizePosX: Optional[Union[float, bool]] = ..., spx: Optional[Union[float, bool]] = ..., stampRandomizePosY: Optional[Union[float, bool]] = ..., spy: Optional[Union[float, bool]] = ..., stampRandomizeRotation: Optional[Union[float, bool]] = ..., srr: Optional[Union[float, bool]] = ..., stampRandomizeScale: Optional[Union[float, bool]] = ..., src: Optional[Union[float, bool]] = ..., stampRandomizeStrength: Optional[Union[float, bool]] = ..., srs: Optional[Union[float, bool]] = ..., stampRotation: Optional[Union[float, bool]] = ..., sr: Optional[Union[float, bool]] = ..., steadyStrokeDistance: Optional[Union[float, bool]] = ..., ssd: Optional[Union[float, bool]] = ..., strength: Optional[Union[float, bool]] = ..., st: Optional[Union[float, bool]] = ..., updatePlane: bool = ..., upl: bool = ..., useGlobalSize: bool = ..., ugs: bool = ..., useScreenSpace: bool = ..., ssp: bool = ..., useStampDistance: bool = ..., usd: bool = ..., useStampImage: bool = ..., usi: bool = ..., useSteadyStroke: bool = ..., uss: bool = ..., wholeStroke: bool = ..., wst: bool = ..., wireframeAlpha: Optional[Union[float, bool]] = ..., wa: Optional[Union[float, bool]] = ..., wireframeColor: Optional[Union[Tuple[float, float, float], bool]] = ..., wc: Optional[Union[Tuple[float, float, float], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This is a tool context command for mesh cache sculpting tool.

    Args:
        adjustSize | asz: (edit) - If true, puts the tool into the mode where dragging the mouse will edit the brush size. If false, puts the tool back into the previous sculpt mode.
        adjustStrength | ast: (edit) - If true, puts the tool into the mode where dragging the mouse will edit the brush strength. If false, puts the tool back into the previous sculpt mode.
        affectAllLayers | aal: (create, edit, query) - If true, the brush affects all layers at once.
        brushDirection | bd: (edit, query) - Specifies the direction of the named brush.
        brushSize | bsz: (edit, query) - Specifies the world-space size of the named brush.
        brushStrength | bst: (edit, query) - Specifies the world-space strength of the named brush.
        buildUpRate | bur: (edit, query) - Specifies the brush strength increasing along the stroke.
        cloneHideSource | chs: (create, edit, query) - True if the cloned source should be hidden.
        cloneMethod | cm: (create, edit, query) - Controls how the source delta vectors should change the target. 0=copy 1=add
        cloneShapeSource | css: (create, edit, query) - Name of the shape source to clone.
        cloneTargetSource | cas: (create, edit, query) - Name of the target source of the clone.
        constrainToSurface | cts: (create, edit, query) - If true, the modification keeps the surface curvature.
        direction | d: (edit, query) - Specifies the direction in which the vertices are moved.
        displayFrozen | df: (create, edit, query) - If false, turns off the display of frozen area on the object.
        displayMask | dm: (create, edit, query) - If false, turns off the display of masked area on the object.
        displayWireframe | dw: (create, edit, query) - If false, turns off the wireframe display of the object.
        falloffType | ft: (edit, query) - Specifies how the brush determines which vertices to affect.
        flood | fl: (create, edit) - Sets the brush effect for each vertex to the given value.
        floodFreeze | ff: (create, edit) - Sets the freeze value for each vertex to the given value.
        frame | frm: (create, edit) - Frames on the sculpted area.
        freezeSelection | fsl: (create, edit) - Freezes selected components.
        grabFollowPath | gfp: (create, edit, query) - If true, the grab brush effect follows mouse movement.
        grabSilhouette | gs: (create, edit, query) - If true, the grab brush uses paint-through mode.
        grabTwist | gtw: (create, edit, query) - If true, the grab brush twists the vertices.
        inverted | inv: (create, edit, query) - If true, inverts the effect of the brush.
        lastMode | lm: (edit, query) - Specifies the type of the last active sculpting brush.
        lockShellBorder | lsb: (create, edit, query) - Lock the shell borders so that they won't be moved by a UV texture brush.
        makeStroke | mt: (edit, multiuse) - Specify a surface point patch for a brush stroke. Multiple patches can be specified to form a brush stroke. The first argument is the mesh index. The second argument is the side index. use 0 for the original side, and 1 for the mirrored side The third argument is the face index within the specified mesh. The fourth and fifth arguments are the face coordinates within the specified face.
        minSize | msz: (edit, query) - Specifies the minimum size percentage of the current brush.
        minStrength | mst: (edit, query) - Specifies the minimum strength percentage of the current brush.
        mirror | mr: (edit, query) - Specifies the mirror mode of the brush.
        mode | m: (edit, query) - Specifies the type of sculpting effect the brush will perform.
        orientToSurface | ots: (create, edit, query) - If true, aligns the brush display to the surface of the mesh.
        recordStroke | rcs: (edit, query) - Set this flag to true to enable stroke recording that can be later played back with the makeStroke flag.
        sculptFalloffCurve | sfc: (edit, query) - Specifies the falloff curve of sculpting effect the brush will perform.
        size | sz: (edit, query) - Specifies the world-space size of the current brush.
        stampDistance | s: (edit, query) - Specifies the stamping distance of the brush.
        stampFile | stp: (edit, query) - Specifies an image file to use as stamp.
        stampFlipX | sfx: (create, edit, query) - Specifies if the brush stamp is flipped on the X axis.
        stampFlipY | sfy: (create, edit, query) - Specifies if the brush stamp is flipped on the Y axis.
        stampOrientToStroke | sos: (create, edit, query) - Specifies if the brush stamp is aligned to the stroke direction.
        stampPlacement | sp: (edit, query) - Specifies the placement mode of the stamp image.
        stampRandomization | srd: (create, edit, query) - Specifies if the brush stamp is randomized.
        stampRandomizationSeed | sre: (edit) - Specifies the stamp randomization seed value. Use a value of 0 to generate a random seed value.
        stampRandomizeFlipX | srx: (create, edit, query) - Specifies if the brush stamp flipping is randomized on the X axis.
        stampRandomizeFlipY | sry: (create, edit, query) - Specifies if the brush stamp flipping is randomized on the Y axis.
        stampRandomizePosX | spx: (edit, query) - Specifies the stamp X position value is randomized.
        stampRandomizePosY | spy: (edit, query) - Specifies the stamp Y position value is randomized.
        stampRandomizeRotation | srr: (edit, query) - Specifies the stamp rotation value is randomized.
        stampRandomizeScale | src: (edit, query) - Specifies the stamp scale value is randomized.
        stampRandomizeStrength | srs: (edit, query) - Specifies the stamp strength value is randomized.
        stampRotation | sr: (edit, query) - Specifies the rotation value of the stamp image.
        steadyStrokeDistance | ssd: (edit, query) - Specifies the distance for the steady stroke.
        strength | st: (edit, query) - Specifies the world-space strength of the current brush.
        updatePlane | upl: (create, edit, query) - Recalculates the underlying tool plane for each stamp in a stroke.
        useGlobalSize | ugs: (create, edit, query) - If true, all the brushes have a shared size property; otherwise size is local.
        useScreenSpace | ssp: (create, edit, query) - If true, the brush size is in screen space pixels.
        useStampDistance | usd: (create, edit, query) - Force the stamps to be spread out along the stroke, rather than building up continually.
        useStampImage | usi: (create, edit, query) - Specifies if the brush uses a stamp image.
        useSteadyStroke | uss: (create, edit, query) - Turns using steady stroke on/off.
        wholeStroke | wst: (create, edit, query) - Continuously recalculates the underlying tool plane from all the vertices affected during the stroke.
        wireframeAlpha | wa: (create, edit, query) - Sets the alpha value of the wireframe for the object that is being sculpted.
        wireframeColor | wc: (create, edit, query) - Sets the color of the wireframe for the object that is being sculpted. Values should be 0-1 RGB.
    """
    ...


def select(*args, add: bool = ..., addFirst: bool = ..., af: bool = ..., all: bool = ..., allDagObjects: bool = ..., ado: bool = ..., allDependencyNodes: bool = ..., adn: bool = ..., clear: bool = ..., cl: bool = ..., containerCentric: bool = ..., cc: bool = ..., deselect: bool = ..., d: bool = ..., hierarchy: bool = ..., hi: bool = ..., noExpand: bool = ..., ne: bool = ..., replace: bool = ..., r: bool = ..., symmetry: bool = ..., sym: bool = ..., symmetrySide: Optional[Union[int, bool]] = ..., sys: Optional[Union[int, bool]] = ..., toggle: bool = ..., tgl: bool = ..., visible: bool = ..., vis: bool = ...) -> Any:
    r"""
    This command is used to put objects onto or off of the active list.
    If none of the five flags [-add, -af, -r, -d, -tgl] are specified, the
    default is to replace the objects on the active list with the
    given list of objects.
    
    When selecting a set as in "select set1", the behaviour is for all
    the members of the set to become selected instead of the set itself.
    If you want to select a set, the "-ne/noExpand" flag must be used.
    
    With the advent of namespaces, selection by name may be
    confusing.  To clarify, without a qualified namespace, name
    lookup is limited to objects in the root namespace ":". There
    are really two parts of a name: the namespace and the name
    itself which is unique within the namespace. If you want to
    select objects in a specific namespace, you need to include
    the namespace separator ":".
    
    For example, 'select -r "foo*"' is trying to look for an
    object with the "foo" prefix in the root namespace. It is not
    trying to look for all objects in the namespace with the "foo"
    prefix. If you want to select all objects in a namespace
    (foo), use 'select "foo:*"'.
    
    Note: When the application starts up, there are several dependency nodes
    created by the system which must exist. These objects are not deletable
    but are selectable.  All objects (dag and dependency nodes) in the scene
    can be obtained using the "ls" command without any arguments. When using
    the "-all", "adn/allDependencyNodes" or "-ado/allDagObjects" flags, only
    the deletable objects are selected.  The non deletable object can still
    be selected by explicitly specifying their name as in "select time1;".

    Args:
        add | add: (create) - Indicates that the specified items should be added to the active list without removing existing items from the active list.
        addFirst | af: (create) - Indicates that the specified items should be added to the front of the active list without removing existing items from the active list.
        all | all: (create) - Indicates that all deletable root level dag objects and all deletable non-dag dependency nodes should be selected.
        allDagObjects | ado: (create) - Indicates that all deletable root level dag objects should be selected.
        allDependencyNodes | adn: (create) - Indicates that all deletable dependency nodes including all deletable dag objects should be selected.
        clear | cl: (create) - Clears the active list.  This is more efficient than "select -d;".  Also "select -d;" will not remove sets from the active list unless the "-ne" flag is also specified.
        containerCentric | cc: (create) - Specifies that the same selection rules as apply to selection in the main viewport will also be applied to the select command. In particular, if the specified objects are members of a black-boxed container and are not published as nodes, Maya will not select them. Instead, their first parent valid for selection will be selected.
        deselect | d: (create) - Indicates that the specified items should be removed from the active list if they are on the active list.
        hierarchy | hi: (create) - Indicates that all children, grandchildren, ... of the specified dag objects should also be selected.
        noExpand | ne: (create) - Indicates that any set which is among the specified items should not be expanded to its list of members. This allows sets to be selected as opposed to the members of sets which is the default behaviour.
        replace | r: (create) - Indicates that the specified items should replace the existing items on the active list.
        symmetry | sym: (create) - Specifies that components should be selected symmetrically using the current symmetricModelling command settings. If symmetric modeling is not enabled then this flag has no effect.
        symmetrySide | sys: (create) - Indicates that components involved in the current symmetry object should be selected, according to the supplied parameter. Valid values for the parameter are: -1 : Select components in the unsymmetrical region. 0 : Select components on the symmetry seam. 1 : Select components on side 1. 2 : Select components on side 2. If symmetric modeling is not enabled then this flag has no effect. Note: currently only works for topological symmetry.
        toggle | tgl: (create) - Indicates that those items on the given list which are on the active list should be removed from the active list and those items on the given list which are not on the active list should be added to the active list.
        visible | vis: (create) - Indicates that of the specified items only those that are visible should be affected.
    """
    ...


def selectContext(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Creates a context to perform selection.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def selectKey(*args, addTo: bool = ..., add: bool = ..., animation: Optional[Union[str, bool]] = ..., an: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., clear: bool = ..., cl: bool = ..., controlPoints: bool = ..., cp: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., f: Optional[Union[Tuple[float, float], bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., hi: Optional[Union[str, bool]] = ..., inTangent: bool = ..., it: bool = ..., includeUpperBound: bool = ..., iub: bool = ..., index: Optional[Union[int, bool]] = ..., keyframe: bool = ..., k: bool = ..., outTangent: bool = ..., ot: bool = ..., remove: bool = ..., rm: bool = ..., replace: bool = ..., r: bool = ..., shape: bool = ..., s: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., t: Optional[Union[Tuple[float, float], bool]] = ..., toggle: bool = ..., tgl: bool = ..., unsnappedKeys: Optional[Union[float, bool]] = ..., uk: Optional[Union[float, bool]] = ...) -> Any:
    r"""
    This command operates on a keyset.  A keyset is
    defined as a group of keys within a specified time range on one or
    more animation curves.
    
    The animation curves comprising a keyset depend on the value
    of the "-animation" flag:
    
    
    keysOrObjects:
    
    Any active keys, when no target objects or -attribute
    flags appear on the command line, or
    
    All animation curves connected to all keyframable
    attributes of objects specified as the command line's
    targetList, when there are no active keys.
    
    
    
    
    keys:
    Only act on active keys or tangents.
    If there are no active keys or tangents, don't do anything.
    
    
    
    objects:
    Only act on specified objects.  If there are no objects specified, don't
    do anything.
    
    
    
    Note that the "-animation" flag can be used to override
    the curves uniquely identified by the multi-use
    "-attribute" flag, which takes an argument of the form
    attributeName, such as "translateX".
    
    Keys on animation curves are identified by either
    their time values or their indices.  Times and indices can
    be given individually or as part of a list or range (see Examples).
    
    This command places keyframes and/or keyframe tangents
    on the active list.

    Args:
        addTo | add: (create) - Add to the current selection of keyframes/tangents
        animation | an: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute | at: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        clear | cl: (create) - Remove all keyframes and tangents from the active list.
        controlPoints | cp: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        float | f: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        hierarchy | hi: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        inTangent | it: (create) - Select in-tangents of keyframes in the specified time range
        includeUpperBound | iub: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index | index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        keyframe | k: (create) - select only keyframes (cannot be combined with -in/-out)
        outTangent | ot: (create) - Select out-tangents of keyframes in the specified time range
        remove | rm: (create) - Remove from the current selection of keyframes/tangents
        replace | r: (create) - Replace the current selection of keyframes/tangents
        shape | s: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        time | t: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
        toggle | tgl: (create) - Toggle the picked state of the specified keyset
        unsnappedKeys | uk: (create) - Select only keys that have times that are not a multiple of the specified numeric value.
    """
    ...


def selectKeyCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context which may be used to select keyframes
    within the graph editor

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def selectKeyframeRegionCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context which may be used to select keyframes
    within the keyframe region of the dope sheet editor

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def selectMode(*args, component: bool = ..., co: bool = ..., hierarchical: bool = ..., h: bool = ..., leaf: bool = ..., l: bool = ..., object: bool = ..., o: bool = ..., preset: bool = ..., p: bool = ..., root: bool = ..., r: bool = ..., template: bool = ..., t: bool = ..., query: bool = ...) -> Any:
    r"""
    The selectMode command is used to change the selection
    mode.  Object, component, root, leaf and template modes are
    mutually exclusive.

    Args:
        component | co: (create, query) - Set component selection on. Component selection mode allows filtered selection based on the component selection mask. The component selection mask is the set of selection masks related to objects that indicate which components are selectable.
        hierarchical | h: (create, query) - Set hierarchical selection on. There are three types of hierarchical selection: root, leaf and template.  Hierarchical mode is set if root, leaf or template mode is set. Setting to hierarchical mode will set the mode to whichever of root, leaf, or template was last on.
        leaf | l: (create, query) - Set leaf selection mode on.  This mode allows the leaf level objects to be selected.  It is similar to object selection mode but ignores the object selection mask.
        object | o: (create, query) - Set object selection on. Object selection mode allows filtered selection based on the object selection mask. The object selection mask is the set of selection masks related to objects that indicate which objects are selectable.  The masks are controlled by the "selectType" command.  Object selection mode selects the leaf level objects.
        preset | p: (create, query) - Allow selection of anything with the mask set, independent of it being an object or a component.
        root | r: (create, query) - Set root selection mode on.  This mode allows the root of a hierarchy to be selected by selecting any of its descendents.  It ignores the object selection mask.
        template | t: (create, query) - Set template selection mode on.  This mode allows selection of templated objects.  It selects the templated object closest to the root of the hierarchy.
    """
    ...


def selectPref(*args, affectsActive: bool = ..., aa: bool = ..., allowHiliteSelection: bool = ..., ahs: bool = ..., autoSelectContainer: bool = ..., asc: bool = ..., autoSelectOutlinerSetMembers: bool = ..., asm: bool = ..., autoUseDepth: bool = ..., aud: bool = ..., clickBoxSize: Optional[Union[int, bool]] = ..., cbs: Optional[Union[int, bool]] = ..., clickDrag: bool = ..., cld: bool = ..., containerCentricSelection: bool = ..., ccs: bool = ..., disableComponentPopups: bool = ..., dcp: bool = ..., expandPopupList: bool = ..., epl: bool = ..., ignoreSelectionPriority: bool = ..., isp: bool = ..., manipClickBoxSize: Optional[Union[int, bool]] = ..., mcb: Optional[Union[int, bool]] = ..., paintSelect: bool = ..., ps: bool = ..., paintSelectWithDepth: bool = ..., psd: bool = ..., popupMenuSelection: bool = ..., pms: bool = ..., preSelectBackfacing: bool = ..., psb: bool = ..., preSelectClosest: bool = ..., psc: bool = ..., preSelectDeadSpace: Optional[Union[int, bool]] = ..., pds: Optional[Union[int, bool]] = ..., preSelectHilite: bool = ..., psh: bool = ..., preSelectHiliteSize: Optional[Union[float, bool]] = ..., phs: Optional[Union[float, bool]] = ..., preSelectTweakDeadSpace: Optional[Union[int, bool]] = ..., pdt: Optional[Union[int, bool]] = ..., selectTypeChangeAffectsActive: bool = ..., stc: bool = ..., selectionChildHighlightMode: Optional[Union[int, bool]] = ..., sch: Optional[Union[int, bool]] = ..., singleBoxSelection: bool = ..., sbs: bool = ..., straightLineDistance: bool = ..., sld: bool = ..., trackSelectionOrder: bool = ..., tso: bool = ..., useDepth: bool = ..., ud: bool = ..., xformNoSelect: bool = ..., xns: bool = ..., query: bool = ...) -> Any:
    r"""
    This command controls state variables used to selection UI behavior.

    Args:
        affectsActive | aa: (create, query) - Set affects-active toggle which when on causes the active list to be affected when changing between object and component selection mode.
        allowHiliteSelection | ahs: (create, query) - When in component selection mode, allow selection of objects for editing.  If an object is selected for editing, it appears in the hilite color and its selectable components are automatically displayed.
        autoSelectContainer | asc: (query) - When enabled, with container centric selection also on, whenever the root transform is selected in the viewport, the container node will automatically be selected as well.
        autoSelectOutlinerSetMembers | asm: (query) - When enabled selecting a set in the Outliner will automatically select the set members instead.
        autoUseDepth | aud: (query) - When enabled, useDepth and paintSelectWithDepth will be automatically enabled in shaded display mode and disabled in wireframe display mode.
        clickBoxSize | cbs: (create, query) - When click selecting, this value defines the size of square picking region surrounding the cursor. The size of the square is twice the specified value. That is, the value defines the amount of space on all four sides of the cursor position. The size must be positive.
        clickDrag | cld: (create, query) - Set click/drag selection interaction on/off
        containerCentricSelection | ccs: (query) - When enabled, selecting any DAG node in a container in the viewport will select the container's root transform if there is one.  If there is no root transform then the highest DAG node in the container will be selected.  There is no effect when selecting nodes which are not in a container.
        disableComponentPopups | dcp: (create, query) - A separate preference to allow users to disable popup menus when selecting components.  This pref is only meaningful if the popupMenuSelection pref is enabled.
        expandPopupList | epl: (create, query) - When in popup selection mode, if this is set then all selection items that contain multiple objects or components will be be expanded such that each object or component will be a single new selection item.
        ignoreSelectionPriority | isp: (create, query) - If this is set, selection priority will be ignored when performing selection.
        manipClickBoxSize | mcb: (create, query) - When selecting a manipulator, this value defines the size of square picking region surrounding the cursor. The size of the square is twice the specified value. That is, the value defines the amount of space on all four sides of the cursor position. The size must be positive.
        paintSelect | ps: (query) - When enabled, the select tool will use drag selection instead of marquee selection.
        paintSelectWithDepth | psd: (query) - When enabled, paint selection will not select components that are behind the surface in the current camera view.
        popupMenuSelection | pms: (create, query) - If this is set, a popup menu will be displayed and used to determine the object to select. The menu lists the current user box (marquee) of selected candidate objects.
        preSelectBackfacing | psb: (query) - When enabled preselection will highlight backfacing components whose normals face away from the camera.
        preSelectClosest | psc: (query) - When enabled and the cursor is over a surface, preselection highlighting will try to preselect the closest component to the cursor regardless of distance.
        preSelectDeadSpace | pds: (query) - This value defines the size of the region around the cursor used for preselection highlighting when the cursor is outside the surface.
        preSelectHilite | psh: (query) - When enabled, the closest component under the cursor will be highlighted to indicate that clicking will select that component.
        preSelectHiliteSize | phs: (query) - This value defines the size of the region around the cursor used for preselection highlighting. Within this region the closest component to the cursor will be highlighted.
        preSelectTweakDeadSpace | pdt: (query) - This value defines the size of the region around the cursor used for preselection highlighting when the cursor is outside the surface in tweak mode.
        selectTypeChangeAffectsActive | stc: (query) - If true then the active list will be updated according to the new selection preferences.
        selectionChildHighlightMode | sch: (create, query) - Controls the highlighting of the children of a selected object. Valid modes are:  0: Always highlight children 1: Never highlight children 2: Use per-object "Selection Child Highlight" setting.  Default mode is (0): Always highlight children.  For (2), each DAG object has an individual "Selection Child Highlight" boolean flag. By default, this flag will be TRUE. When mode (2) is enabled, the control is deferred to the selected object's "Selection Child Highlight" flag.
        singleBoxSelection | sbs: (create, query) - Set single box selection on/off. This flag indicates whether just single object will be selected when the user box (marquee) selects several objects if flag set to true.  Otherwise, all those objects inside the box will be selected.
        straightLineDistance | sld: (query) - If true then use straight line distances for selection proximity.
        trackSelectionOrder | tso: (query) - When enabled, the order of selected objects and components will be tracked.  The 'ls' command will be able to return the active list in the order of selection which will allow scripts to be written that depend on the order.
        useDepth | ud: (query) - When enabled, marquee selection will not select components that are behind the surface in the current camera view.
        xformNoSelect | xns: (create, query) - Disable selection in xform tools
    """
    ...


def selectPriority(*args, allComponents: Optional[Union[int, bool]] = ..., alc: Optional[Union[int, bool]] = ..., allObjects: Optional[Union[int, bool]] = ..., alo: Optional[Union[int, bool]] = ..., animBreakdown: Optional[Union[int, bool]] = ..., abd: Optional[Union[int, bool]] = ..., animCurve: Optional[Union[int, bool]] = ..., ac: Optional[Union[int, bool]] = ..., animInTangent: Optional[Union[int, bool]] = ..., ait: Optional[Union[int, bool]] = ..., animKeyframe: Optional[Union[int, bool]] = ..., ak: Optional[Union[int, bool]] = ..., animOutTangent: Optional[Union[int, bool]] = ..., aot: Optional[Union[int, bool]] = ..., byName: Optional[Union[Tuple[str, bool], bool]] = ..., bn: Optional[Union[Tuple[str, bool], bool]] = ..., camera: Optional[Union[int, bool]] = ..., ca: Optional[Union[int, bool]] = ..., cluster: Optional[Union[int, bool]] = ..., cl: Optional[Union[int, bool]] = ..., collisionModel: Optional[Union[int, bool]] = ..., clm: Optional[Union[int, bool]] = ..., controlVertex: Optional[Union[int, bool]] = ..., cv: Optional[Union[int, bool]] = ..., curve: Optional[Union[int, bool]] = ..., c: Optional[Union[int, bool]] = ..., curveKnot: Optional[Union[int, bool]] = ..., ck: Optional[Union[int, bool]] = ..., curveOnSurface: Optional[Union[int, bool]] = ..., cos: Optional[Union[int, bool]] = ..., curveParameterPoint: Optional[Union[int, bool]] = ..., cpp: Optional[Union[int, bool]] = ..., dimension: Optional[Union[int, bool]] = ..., dim: Optional[Union[int, bool]] = ..., dynamicConstraint: Optional[Union[int, bool]] = ..., dc: Optional[Union[int, bool]] = ..., edge: Optional[Union[int, bool]] = ..., eg: Optional[Union[int, bool]] = ..., editPoint: Optional[Union[int, bool]] = ..., ep: Optional[Union[int, bool]] = ..., emitter: Optional[Union[int, bool]] = ..., em: Optional[Union[int, bool]] = ..., facet: Optional[Union[int, bool]] = ..., fc: Optional[Union[int, bool]] = ..., field: Optional[Union[int, bool]] = ..., fi: Optional[Union[int, bool]] = ..., fluid: Optional[Union[int, bool]] = ..., fl: Optional[Union[int, bool]] = ..., follicle: Optional[Union[int, bool]] = ..., fo: Optional[Union[int, bool]] = ..., hairSystem: Optional[Union[int, bool]] = ..., hs: Optional[Union[int, bool]] = ..., handle: Optional[Union[int, bool]] = ..., ha: Optional[Union[int, bool]] = ..., hull: Optional[Union[int, bool]] = ..., hl: Optional[Union[int, bool]] = ..., ikEndEffector: Optional[Union[int, bool]] = ..., iee: Optional[Union[int, bool]] = ..., ikHandle: Optional[Union[int, bool]] = ..., ikh: Optional[Union[int, bool]] = ..., imagePlane: Optional[Union[int, bool]] = ..., ip: Optional[Union[int, bool]] = ..., implicitGeometry: Optional[Union[int, bool]] = ..., ig: Optional[Union[int, bool]] = ..., isoparm: Optional[Union[int, bool]] = ..., iso: Optional[Union[int, bool]] = ..., joint: Optional[Union[int, bool]] = ..., j: Optional[Union[int, bool]] = ..., jointPivot: Optional[Union[int, bool]] = ..., jp: Optional[Union[int, bool]] = ..., lattice: Optional[Union[int, bool]] = ..., la: Optional[Union[int, bool]] = ..., latticePoint: Optional[Union[int, bool]] = ..., lp: Optional[Union[int, bool]] = ..., light: Optional[Union[int, bool]] = ..., lt: Optional[Union[int, bool]] = ..., localRotationAxis: Optional[Union[int, bool]] = ..., ra: Optional[Union[int, bool]] = ..., locator: Optional[Union[int, bool]] = ..., lc: Optional[Union[int, bool]] = ..., locatorUV: Optional[Union[int, bool]] = ..., luv: Optional[Union[int, bool]] = ..., locatorXYZ: Optional[Union[int, bool]] = ..., xyz: Optional[Union[int, bool]] = ..., meshUVShell: Optional[Union[int, bool]] = ..., msh: Optional[Union[int, bool]] = ..., motionTrailPoint: Optional[Union[int, bool]] = ..., mtp: Optional[Union[int, bool]] = ..., motionTrailTangent: Optional[Union[int, bool]] = ..., mtt: Optional[Union[int, bool]] = ..., nCloth: Optional[Union[int, bool]] = ..., ncl: Optional[Union[int, bool]] = ..., nParticle: Optional[Union[int, bool]] = ..., npr: Optional[Union[int, bool]] = ..., nParticleShape: Optional[Union[int, bool]] = ..., nps: Optional[Union[int, bool]] = ..., nRigid: Optional[Union[int, bool]] = ..., nr: Optional[Union[int, bool]] = ..., nonlinear: Optional[Union[int, bool]] = ..., nl: Optional[Union[int, bool]] = ..., nurbsCurve: Optional[Union[int, bool]] = ..., nc: Optional[Union[int, bool]] = ..., nurbsSurface: Optional[Union[int, bool]] = ..., ns: Optional[Union[int, bool]] = ..., orientationLocator: Optional[Union[int, bool]] = ..., ol: Optional[Union[int, bool]] = ..., particle: Optional[Union[int, bool]] = ..., pr: Optional[Union[int, bool]] = ..., particleShape: Optional[Union[int, bool]] = ..., ps: Optional[Union[int, bool]] = ..., plane: Optional[Union[int, bool]] = ..., pl: Optional[Union[int, bool]] = ..., polymesh: Optional[Union[int, bool]] = ..., p: Optional[Union[int, bool]] = ..., polymeshEdge: Optional[Union[int, bool]] = ..., pe: Optional[Union[int, bool]] = ..., polymeshFace: Optional[Union[int, bool]] = ..., pf: Optional[Union[int, bool]] = ..., polymeshFreeEdge: Optional[Union[int, bool]] = ..., pfe: Optional[Union[int, bool]] = ..., polymeshUV: Optional[Union[int, bool]] = ..., puv: Optional[Union[int, bool]] = ..., polymeshVertex: Optional[Union[int, bool]] = ..., pv: Optional[Union[int, bool]] = ..., polymeshVtxFace: Optional[Union[int, bool]] = ..., pvf: Optional[Union[int, bool]] = ..., queryByName: Optional[Union[str, bool]] = ..., qbn: Optional[Union[str, bool]] = ..., rigidBody: Optional[Union[int, bool]] = ..., rb: Optional[Union[int, bool]] = ..., rigidConstraint: Optional[Union[int, bool]] = ..., rc: Optional[Union[int, bool]] = ..., rotatePivot: Optional[Union[int, bool]] = ..., rp: Optional[Union[int, bool]] = ..., scalePivot: Optional[Union[int, bool]] = ..., sp: Optional[Union[int, bool]] = ..., sculpt: Optional[Union[int, bool]] = ..., sc: Optional[Union[int, bool]] = ..., selectHandle: Optional[Union[int, bool]] = ..., sh: Optional[Union[int, bool]] = ..., spring: Optional[Union[int, bool]] = ..., spr: Optional[Union[int, bool]] = ..., springComponent: Optional[Union[int, bool]] = ..., spc: Optional[Union[int, bool]] = ..., stroke: Optional[Union[int, bool]] = ..., str: Optional[Union[int, bool]] = ..., subdiv: Optional[Union[int, bool]] = ..., sd: Optional[Union[int, bool]] = ..., subdivMeshEdge: Optional[Union[int, bool]] = ..., sme: Optional[Union[int, bool]] = ..., subdivMeshFace: Optional[Union[int, bool]] = ..., smf: Optional[Union[int, bool]] = ..., subdivMeshPoint: Optional[Union[int, bool]] = ..., smp: Optional[Union[int, bool]] = ..., subdivMeshUV: Optional[Union[int, bool]] = ..., smu: Optional[Union[int, bool]] = ..., surfaceEdge: Optional[Union[int, bool]] = ..., se: Optional[Union[int, bool]] = ..., surfaceFace: Optional[Union[int, bool]] = ..., sf: Optional[Union[int, bool]] = ..., surfaceKnot: Optional[Union[int, bool]] = ..., sk: Optional[Union[int, bool]] = ..., surfaceParameterPoint: Optional[Union[int, bool]] = ..., spp: Optional[Union[int, bool]] = ..., surfaceRange: Optional[Union[int, bool]] = ..., sr: Optional[Union[int, bool]] = ..., texture: Optional[Union[int, bool]] = ..., tx: Optional[Union[int, bool]] = ..., vertex: Optional[Union[int, bool]] = ..., v: Optional[Union[int, bool]] = ..., query: bool = ...) -> Any:
    r"""
    The selectPriority command is used to change the selection
    priority of particular types of objects that can be selected when using
    the select tool. It accepts no other arguments besides the flags.
    These flags are the same as used by the 'selectType' command.

    Args:
        allComponents | alc: (create, query) - Set all component selection priority
        allObjects | alo: (create, query) - Set all object selection priority
        animBreakdown | abd: (create, query) - Set animation breakdown selection priority
        animCurve | ac: (create, query) - Set animation curve selection priority
        animInTangent | ait: (create, query) - Set animation in-tangent selection priority
        animKeyframe | ak: (create, query) - Set animation keyframe selection priority
        animOutTangent | aot: (create, query) - Set animation out-tangent selection priority
        byName | bn: (create, multiuse) - Set selection priority for the specified user-defined selection type
        camera | ca: (create, query) - Set camera selection priority
        cluster | cl: (create, query) - Set cluster selection priority
        collisionModel | clm: (create, query) - Set collision model selection priority
        controlVertex | cv: (create, query) - Set control vertex selection priority
        curve | c: (create, query) - Set curve selection priority
        curveKnot | ck: (create, query) - Set curve knot selection priority
        curveOnSurface | cos: (create, query) - Set curve-on-surface selection priority
        curveParameterPoint | cpp: (create, query) - Set curve parameter point selection priority
        dimension | dim: (create, query) - Set dimension shape selection priority
        dynamicConstraint | dc: (create, query) - Set dynamicConstraint selection priority
        edge | eg: (create, query) - Set mesh edge selection priority
        editPoint | ep: (create, query) - Set edit-point selection priority
        emitter | em: (create, query) - Set emitter selection priority
        facet | fc: (create, query) - Set mesh face selection priority
        field | fi: (create, query) - Set field selection priority
        fluid | fl: (create, query) - Set fluid selection priority
        follicle | fo: (create, query) - Set follicle selection priority
        hairSystem | hs: (create, query) - Set hairSystem selection priority
        handle | ha: (create, query) - Set object handle selection priority
        hull | hl: (create, query) - Set hull selection priority
        ikEndEffector | iee: (create, query) - Set ik end effector selection priority
        ikHandle | ikh: (create, query) - Set ik handle selection priority
        imagePlane | ip: (create, query) - Set image plane selection mask priority
        implicitGeometry | ig: (create, query) - Set implicit geometry selection priority
        isoparm | iso: (create, query) - Set surface iso-parm selection priority
        joint | j: (create, query) - Set ik handle selection priority
        jointPivot | jp: (create, query) - Set joint pivot selection priority
        lattice | la: (create, query) - Set lattice selection priority
        latticePoint | lp: (create, query) - Set lattice point selection priority
        light | lt: (create, query) - Set light selection priority
        localRotationAxis | ra: (create, query) - Set local rotation axis selection priority
        locator | lc: (create, query) - Set locator (all types) selection priority
        locatorUV | luv: (create, query) - Set uv locator selection priority
        locatorXYZ | xyz: (create, query) - Set xyz locator selection priority
        meshUVShell | msh: (create, query) - Set uv shell component mask on/off.
        motionTrailPoint | mtp: (create, query) - Set motion point selection priority
        motionTrailTangent | mtt: (create, query) - Set motion point tangent priority
        nCloth | ncl: (create, query) - Set nCloth selection priority
        nParticle | npr: (create, query) - Set nParticle point selection priority
        nParticleShape | nps: (create, query) - Set nParticle shape selection priority
        nRigid | nr: (create, query) - Set nRigid selection priority
        nonlinear | nl: (create, query) - Set nonlinear selection priority
        nurbsCurve | nc: (create, query) - Set nurbs-curve selection priority
        nurbsSurface | ns: (create, query) - Set nurbs-surface selection priority
        orientationLocator | ol: (create, query) - Set orientation locator selection priority
        particle | pr: (create, query) - Set particle point selection priority
        particleShape | ps: (create, query) - Set particle shape selection priority
        plane | pl: (create, query) - Set sketch plane selection priority
        polymesh | p: (create, query) - Set poly-mesh selection priority
        polymeshEdge | pe: (create, query) - Set poly-mesh edge selection priority
        polymeshFace | pf: (create, query) - Set poly-mesh face selection priority
        polymeshFreeEdge | pfe: (create, query) - Set poly-mesh free-edge selection priority
        polymeshUV | puv: (create, query) - Set poly-mesh UV point selection priority
        polymeshVertex | pv: (create, query) - Set poly-mesh vertex selection priority
        polymeshVtxFace | pvf: (create, query) - Set poly-mesh vtxFace selection priority
        queryByName | qbn: (query) - Query selection priority for the specified user-defined selection type       In query mode, this flag needs a value.
        rigidBody | rb: (create, query) - Set rigid body selection priority
        rigidConstraint | rc: (create, query) - Set rigid constraint selection priority
        rotatePivot | rp: (create, query) - Set rotate pivot selection priority
        scalePivot | sp: (create, query) - Set scale pivot selection priority
        sculpt | sc: (create, query) - Set sculpt selection priority
        selectHandle | sh: (create, query) - Set select handle selection priority
        spring | spr: (create, query) - Set spring shape selection priority
        springComponent | spc: (create, query) - Set individual spring selection priority
        stroke | str: (create, query) - Set stroke selection priority
        subdiv | sd: (create, query) - Set subdivision surface selection priority
        subdivMeshEdge | sme: (create, query) - Set subdivision surface mesh edge selection priority
        subdivMeshFace | smf: (create, query) - Set subdivision surface mesh face selection priority
        subdivMeshPoint | smp: (create, query) - Set subdivision surface mesh point selection priority
        subdivMeshUV | smu: (create, query) - Set subdivision surface mesh UV map selection priority
        surfaceEdge | se: (create, query) - Set surface edge selection priority
        surfaceFace | sf: (create, query) - Set surface face selection priority
        surfaceKnot | sk: (create, query) - Set surface knot selection priority
        surfaceParameterPoint | spp: (create, query) - Set surface parameter point selection priority
        surfaceRange | sr: (create, query) - Set surface range selection priority
        texture | tx: (create, query) - Set texture selection priority
        vertex | v: (create, query) - Set mesh vertex selection priority
    """
    ...


def selectType(*args, allComponents: bool = ..., alc: bool = ..., allObjects: bool = ..., alo: bool = ..., animBreakdown: bool = ..., abd: bool = ..., animCurve: bool = ..., ac: bool = ..., animInTangent: bool = ..., ait: bool = ..., animKeyframe: bool = ..., ak: bool = ..., animOutTangent: bool = ..., aot: bool = ..., byName: Optional[Union[Tuple[str, bool], bool]] = ..., bn: Optional[Union[Tuple[str, bool], bool]] = ..., camera: bool = ..., ca: bool = ..., cluster: bool = ..., cl: bool = ..., collisionModel: bool = ..., clm: bool = ..., controlVertex: bool = ..., cv: bool = ..., curve: bool = ..., c: bool = ..., curveKnot: bool = ..., ck: bool = ..., curveOnSurface: bool = ..., cos: bool = ..., curveParameterPoint: bool = ..., cpp: bool = ..., dimension: bool = ..., dim: bool = ..., dynamicConstraint: bool = ..., dc: bool = ..., edge: bool = ..., eg: bool = ..., editPoint: bool = ..., ep: bool = ..., emitter: bool = ..., em: bool = ..., facet: bool = ..., fc: bool = ..., field: bool = ..., fi: bool = ..., fluid: bool = ..., fl: bool = ..., follicle: bool = ..., fo: bool = ..., hairSystem: bool = ..., hs: bool = ..., handle: bool = ..., ha: bool = ..., hull: bool = ..., hl: bool = ..., ikEndEffector: bool = ..., iee: bool = ..., ikHandle: bool = ..., ikh: bool = ..., imagePlane: bool = ..., ip: bool = ..., implicitGeometry: bool = ..., ig: bool = ..., isoparm: bool = ..., iso: bool = ..., joint: bool = ..., j: bool = ..., jointPivot: bool = ..., jp: bool = ..., lattice: bool = ..., la: bool = ..., latticePoint: bool = ..., lp: bool = ..., light: bool = ..., lt: bool = ..., localRotationAxis: bool = ..., ra: bool = ..., locator: bool = ..., lc: bool = ..., locatorUV: bool = ..., luv: bool = ..., locatorXYZ: bool = ..., xyz: bool = ..., meshUVShell: bool = ..., msh: bool = ..., motionTrailPoint: bool = ..., mtp: bool = ..., motionTrailTangent: bool = ..., mtt: bool = ..., nCloth: bool = ..., ncl: bool = ..., nParticle: bool = ..., npr: bool = ..., nParticleShape: bool = ..., nps: bool = ..., nRigid: bool = ..., nr: bool = ..., nonlinear: bool = ..., nl: bool = ..., nurbsCurve: bool = ..., nc: bool = ..., nurbsSurface: bool = ..., ns: bool = ..., objectComponent: bool = ..., ocm: bool = ..., orientationLocator: bool = ..., ol: bool = ..., particle: bool = ..., pr: bool = ..., particleShape: bool = ..., ps: bool = ..., plane: bool = ..., pl: bool = ..., polymesh: bool = ..., p: bool = ..., polymeshEdge: bool = ..., pe: bool = ..., polymeshFace: bool = ..., pf: bool = ..., polymeshFreeEdge: bool = ..., pfe: bool = ..., polymeshUV: bool = ..., puv: bool = ..., polymeshVertex: bool = ..., pv: bool = ..., polymeshVtxFace: bool = ..., pvf: bool = ..., queryByName: Optional[Union[str, bool]] = ..., qbn: Optional[Union[str, bool]] = ..., rigidBody: bool = ..., rb: bool = ..., rigidConstraint: bool = ..., rc: bool = ..., rotatePivot: bool = ..., rp: bool = ..., scalePivot: bool = ..., sp: bool = ..., sculpt: bool = ..., sc: bool = ..., selectHandle: bool = ..., sh: bool = ..., spring: bool = ..., spr: bool = ..., springComponent: bool = ..., spc: bool = ..., stroke: bool = ..., str: bool = ..., subdiv: bool = ..., sd: bool = ..., subdivMeshEdge: bool = ..., sme: bool = ..., subdivMeshFace: bool = ..., smf: bool = ..., subdivMeshPoint: bool = ..., smp: bool = ..., subdivMeshUV: bool = ..., smu: bool = ..., surfaceEdge: bool = ..., se: bool = ..., surfaceFace: bool = ..., sf: bool = ..., surfaceKnot: bool = ..., sk: bool = ..., surfaceParameterPoint: bool = ..., spp: bool = ..., surfaceRange: bool = ..., sr: bool = ..., surfaceUV: bool = ..., suv: bool = ..., texture: bool = ..., tx: bool = ..., vertex: bool = ..., v: bool = ..., query: bool = ...) -> Any:
    r"""
    The selectType command is used to change the set of
    allowable types of objects that can be selected when using
    the select tool. It accepts no other arguments besides the flags.
    
    There are basically two different types of items that are selectable
    when interactively selecting objects in the 3D views.  They are
    classified as objects (entire objects) or components (parts of
    objects).  The object and component command flags
    control which class of objects are selectable.
    
    It is possible to select components while in the object selection mode.
    To set the components which are selectable in object
    selection mode you must use the -ocm flag when specifying the component
    flags.

    Args:
        allComponents | alc: (create, query) - Set all component selection masks on/off
        allObjects | alo: (create, query) - Set all object selection masks on/off
        animBreakdown | abd: (create, query) - Set animation breakdown selection mask on/off.
        animCurve | ac: (create, query) - Set animation curve selection mask on/off.
        animInTangent | ait: (create, query) - Set animation in-tangent selection mask on/off.
        animKeyframe | ak: (create, query) - Set animation keyframe selection mask on/off.
        animOutTangent | aot: (create, query) - Set animation out-tangent selection mask on/off.
        byName | bn: (create, multiuse) - Set the specified user-defined selection mask on/off. (object flag)
        camera | ca: (create, query) - Set camera selection mask on/off. (object flag)
        cluster | cl: (create, query) - Set cluster selection mask on/off. (object flag)
        collisionModel | clm: (create, query) - Set collision model selection mask on/off. (object flag)
        controlVertex | cv: (create, query) - Set control vertex selection mask on/off. (component flag)
        curve | c: (create, query) - Set curve selection mask on/off. (object flag)
        curveKnot | ck: (create, query) - Set curve knot selection mask on/off. (component flag)
        curveOnSurface | cos: (create, query) - Set curve-on-surface selection mask on/off. (object flag)
        curveParameterPoint | cpp: (create, query) - Set curve parameter point selection mask on/off. (component flag)
        dimension | dim: (create, query) - Set dimension shape selection mask on/off. (object flag)
        dynamicConstraint | dc: (create, query) - Set dynamicConstraint selection mask on/off. (object flag)
        edge | eg: (create, query) - Set mesh edge selection mask on/off. (component flag)
        editPoint | ep: (create, query) - Set edit-point selection mask on/off. (component flag)
        emitter | em: (create, query) - Set emitter selection mask on/off. (object flag)
        facet | fc: (create, query) - Set mesh face selection mask on/off. (component flag)
        field | fi: (create, query) - Set field selection mask on/off. (object flag)
        fluid | fl: (create, query) - Set fluid selection mask on/off. (object flag)
        follicle | fo: (create, query) - Set follicle selection mask on/off. (object flag)
        hairSystem | hs: (create, query) - Set hairSystem selection mask on/off. (object flag)
        handle | ha: (create, query) - Set object handle selection mask on/off. (object flag)
        hull | hl: (create, query) - Set hull selection mask on/off. (component flag)
        ikEndEffector | iee: (create, query) - Set ik end effector selection mask on/off. (object flag)
        ikHandle | ikh: (create, query) - Set ik handle selection mask on/off. (object flag)
        imagePlane | ip: (create, query) - Set image plane selection mask on/off. (component flag)
        implicitGeometry | ig: (create, query) - Set implicit geometry selection mask on/off. (object flag)
        isoparm | iso: (create, query) - Set surface iso-parm selection mask on/off. (component flag)
        joint | j: (create, query) - Set ik handle selection mask on/off. (object flag)
        jointPivot | jp: (create, query) - Set joint pivot selection mask on/off. (component flag)
        lattice | la: (create, query) - Set lattice selection mask on/off. (object flag)
        latticePoint | lp: (create, query) - Set lattice point selection mask on/off. (component flag)
        light | lt: (create, query) - Set light selection mask on/off. (object flag)
        localRotationAxis | ra: (create, query) - Set local rotation axis selection mask on/off. (component flag)
        locator | lc: (create, query) - Set locator (all types) selection mask on/off. (object flag)
        locatorUV | luv: (create, query) - Set uv locator selection mask on/off. (object flag)
        locatorXYZ | xyz: (create, query) - Set xyz locator selection mask on/off. (object flag)
        meshUVShell | msh: (create, query) - Set uv shell component mask on/off.
        motionTrailPoint | mtp: (create, query) - Set motion point selection mask on/off.
        motionTrailTangent | mtt: (create, query) - Set motion point tangent mask on/off.
        nCloth | ncl: (create, query) - Set nCloth selection mask on/off. (object flag)
        nParticle | npr: (create, query) - Set nParticle point selection mask on/off. (component flag)
        nParticleShape | nps: (create, query) - Set nParticle shape selection mask on/off. (object flag)
        nRigid | nr: (create, query) - Set nRigid selection mask on/off. (object flag)
        nonlinear | nl: (create, query) - Set nonlinear selection mask on/off. (object flag)
        nurbsCurve | nc: (create, query) - Set nurbs-curve selection mask on/off. (object flag)
        nurbsSurface | ns: (create, query) - Set nurbs-surface selection mask on/off. (object flag)
        objectComponent | ocm: (create, query) - Component flags apply to object mode.
        orientationLocator | ol: (create, query) - Set orientation locator selection mask on/off. (object flag)
        particle | pr: (create, query) - Set particle point selection mask on/off. (component flag)
        particleShape | ps: (create, query) - Set particle shape selection mask on/off. (object flag)
        plane | pl: (create, query) - Set sketch plane selection mask on/off. (object flag)
        polymesh | p: (create, query) - Set poly-mesh selection mask on/off. (object flag)
        polymeshEdge | pe: (create, query) - Set poly-mesh edge selection mask on/off. (component flag)
        polymeshFace | pf: (create, query) - Set poly-mesh face selection mask on/off. (component flag)
        polymeshFreeEdge | pfe: (create, query) - Set poly-mesh free-edge selection mask on/off. (component flag)
        polymeshUV | puv: (create, query) - Set poly-mesh UV point selection mask on/off. (component flag)
        polymeshVertex | pv: (create, query) - Set poly-mesh vertex selection mask on/off. (component flag)
        polymeshVtxFace | pvf: (create, query) - Set poly-mesh vertexFace selection mask on/off. (component flag)
        queryByName | qbn: (query) - Query the specified user-defined selection mask. (object flag)       In query mode, this flag needs a value.
        rigidBody | rb: (create, query) - Set rigid body selection mask on/off. (object flag)
        rigidConstraint | rc: (create, query) - Set rigid constraint selection mask on/off. (object flag)
        rotatePivot | rp: (create, query) - Set rotate pivot selection mask on/off. (component flag)
        scalePivot | sp: (create, query) - Set scale pivot selection mask on/off. (component flag)
        sculpt | sc: (create, query) - Set sculpt selection mask on/off. (object flag)
        selectHandle | sh: (create, query) - Set select handle selection mask on/off. (component flag)
        spring | spr: (create, query) - Set spring shape selection mask on/off. (object flag)
        springComponent | spc: (create, query) - Set individual spring selection mask on/off. (component flag)
        stroke | str: (create, query) - Set the Paint Effects stroke selection mask on/off. (object flag)
        subdiv | sd: (create, query) - Set subdivision surfaces selection mask on/off. (object flag)
        subdivMeshEdge | sme: (create, query) - Set subdivision surfaces mesh edge selection mask on/off. (component flag)
        subdivMeshFace | smf: (create, query) - Set subdivision surfaces mesh face selection mask on/off. (component flag)
        subdivMeshPoint | smp: (create, query) - Set subdivision surfaces mesh point selection mask on/off. (component flag)
        subdivMeshUV | smu: (create, query) - Set subdivision surfaces mesh UV map selection mask on/off. (component flag)
        surfaceEdge | se: (create, query) - Set surface edge selection mask on/off. (component flag)
        surfaceFace | sf: (create, query) - Set surface face selection mask on/off. (component flag)
        surfaceKnot | sk: (create, query) - Set surface knot selection mask on/off. (component flag)
        surfaceParameterPoint | spp: (create, query) - Set surface parameter point selection mask on/off. (component flag)
        surfaceRange | sr: (create, query) - Set surface range selection mask on/off. (component flag)
        surfaceUV | suv: (create, query) - Set surface uv selection mask on/off. (component flag)
        texture | tx: (create, query) - Set texture selection mask on/off. (object flag)
        vertex | v: (create, query) - Set mesh vertex selection mask on/off. (component flag)
    """
    ...


def setAttr(*args, alteredValue: bool = ..., av: bool = ..., caching: bool = ..., ca: bool = ..., capacityHint: Optional[Union[int, bool]] = ..., ch: Optional[Union[int, bool]] = ..., channelBox: bool = ..., cb: bool = ..., clamp: bool = ..., c: bool = ..., keyable: bool = ..., k: bool = ..., lock: bool = ..., l: bool = ..., size: Optional[Union[int, bool]] = ..., s: Optional[Union[int, bool]] = ..., type: Optional[Union[str, bool]] = ..., typ: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Sets the value of a dependency node attribute.  No value for
    the attribute is needed when the -l/-k/-s flags are used.
    The -type flag is only required when setting a non-numeric attribute.
    
    For Ufe attributes, the input attribute string should be
    "<ufe_path_string>.<ufe_attribute_name>".
    
    The following chart outlines the syntax of setAttr for non-numeric
    data types:
    
    {TYPE} below means any number of values of type TYPE,
    separated by a space
    [TYPE] means that the value of type TYPE is optional
    A|B means that either of A or B may appear
    
    
    In order to run its examples, first execute these commands to
    create the sample attribute types:
    
    sphere -n node;
    addAttr -ln short2Attr -at short2;
    addAttr -ln short2a -p short2Attr -at short;
    addAttr -ln short2b -p short2Attr -at short;
    addAttr -ln short3Attr -at short3;
    addAttr -ln short3a -p short3Attr -at short;
    addAttr -ln short3b -p short3Attr -at short;
    addAttr -ln short3c -p short3Attr -at short;
    addAttr -ln long2Attr -at long2;
    addAttr -ln long2a -p long2Attr -at long;
    addAttr -ln long2b -p long2Attr -at long;
    addAttr -ln long3Attr -at long3;
    addAttr -ln long3a -p long3Attr -at long;
    addAttr -ln long3b -p long3Attr -at long;
    addAttr -ln long3c -p long3Attr -at long;
    addAttr -ln float2Attr -at float2;
    addAttr -ln float2a -p float2Attr -at "float";
    addAttr -ln float2b -p float2Attr -at "float";
    addAttr -ln float3Attr -at float3;
    addAttr -ln float3a -p float3Attr -at "float";
    addAttr -ln float3b -p float3Attr -at "float";
    addAttr -ln float3c -p float3Attr -at "float";
    addAttr -ln double2Attr -at double2;
    addAttr -ln double2a -p double2Attr -at double;
    addAttr -ln double2b -p double2Attr -at double;
    addAttr -ln double3Attr -at double3;
    addAttr -ln double3a -p double3Attr -at double;
    addAttr -ln double3b -p double3Attr -at double;
    addAttr -ln double3c -p double3Attr -at double;
    addAttr -ln int32ArrayAttr -dt Int32Array;
    addAttr -ln doubleArrayAttr -dt doubleArray;
    addAttr -ln pointArrayAttr -dt pointArray;
    addAttr -ln vectorArrayAttr -dt vectorArray;
    addAttr -ln stringArrayAttr -dt stringArray;
    addAttr -ln stringAttr -dt "string";
    addAttr -ln matrixAttr -dt "matrix";
    addAttr -ln sphereAttr -dt sphere;
    addAttr -ln coneAttr -dt cone;
    addAttr -ln meshAttr -dt mesh;
    addAttr -ln latticeAttr -dt lattice;
    addAttr -ln spectrumRGBAttr -dt spectrumRGB;
    addAttr -ln reflectanceRGBAttr -dt reflectanceRGB;
    addAttr -ln componentListAttr -dt componentList;
    addAttr -ln attrAliasAttr -dt attributeAlias;
    addAttr -ln curveAttr -dt nurbsCurve;
    addAttr -ln surfaceAttr -dt nurbsSurface;
    addAttr -ln trimFaceAttr -dt nurbsTrimface;
    addAttr -ln polyFaceAttr -dt polyFaces;
    
    
    
    
    
    -type short2
    
    
    Array of two short integers
    
    
    Value Syntax
    short short
    
    
    Value Meaning
    value1 value2
    
    
    Mel Example
    setAttr node.short2Attr -type short2 1 2;
    
    
    Python Example
    cmds.setAttr('node.short2Attr',1,2,type='short2')
    
    
    
    
    
    -type short3
    
    
    Array of three short integers
    
    
    Value Syntax
    short short short
    
    
    Value Meaning
    value1 value2 value3
    
    
    Mel Example
    setAttr node.short3Attr -type short3 1 2 3;
    
    
    Python Example
    cmds.setAttr('node.short3Attr',1,2,3,type='short3')
    
    
    
    
    
    -type long2
    
    
    Array of two long integers
    
    
    Value Syntax
    long long
    
    
    Value Meaning
    value1 value2
    
    
    Mel Example
    setAttr node.long2Attr -type long2 1000000 2000000;
    
    
    Python Example
    cmds.setAttr('node.long2Attr',1000000,2000000,type='long2')
    
    
    
    
    
    -type long3
    
    
    Array of three long integers
    
    
    Value Syntax
    long long long
    
    
    Value Meaning
    value1 value2 value3
    
    
    Mel Example
    setAttr node.long3Attr -type long3 1000000 2000000 3000000;
    
    
    Python Example
    cmds.setAttr('node.long3Attr',1000000,2000000,3000000,type='long3')
    
    
    
    
    
    -type Int32Array
    
    
    Variable length array of long integers
    
    
    Value Syntax
    int {int}
    
    
    Value Meaning
    numberOfArrayValues {arrayValue}
    
    
    Mel Example
    setAttr node.int32ArrayAttr -type Int32Array 2 12 75;
    
    
    Python Example
    cmds.setAttr('node.int32ArrayAttr',[2,12,75],type='Int32Array')
    
    
    
    
    
    -type float2
    
    
    Array of two floats
    
    
    Value Syntax
    float float
    
    
    Value Meaning
    value1 value2
    
    
    Mel Example
    setAttr node.float2Attr -type float2 1.1 2.2;
    
    
    Python Example
    cmds.setAttr('node.float2Attr',1.1,2.2,type='float2')
    
    
    
    
    
    -type float3
    
    
    Array of three floats
    
    
    Value Syntax
    float float float
    
    
    Value Meaning
    value1 value2 value3
    
    
    Mel Example
    setAttr node.float3Attr -type float3 1.1 2.2 3.3;
    
    
    Python Example
    cmds.setAttr('node.float3Attr',1.1,2.2,3.3,type='float3')
    
    
    
    
    
    -type double2
    
    
    Array of two doubles
    
    
    Value Syntax
    double double
    
    
    Value Meaning
    value1 value2
    
    
    Mel Example
    setAttr node.double2Attr -type double2 1.1 2.2;
    
    
    Python Example
    cmds.setAttr('node.double2Attr',1.1,2.2,type='double2')
    
    
    
    
    
    -type double3
    
    
    Array of three doubles
    
    
    Value Syntax
    double double double
    
    
    Value Meaning
    value1 value2 value3
    
    
    Mel Example
    setAttr node.double3Attr -type double3 1.1 2.2 3.3;
    
    
    Python Example
    cmds.setAttr('node.double3Attr',1.1,2.2,3.3,type='double3')
    
    
    
    
    
    -type doubleArray
    
    
    Variable length array of doubles
    
    
    Value Syntax
    int {double}
    
    
    Value Meaning
    numberOfArrayValues {arrayValue}
    
    
    Mel Example
    setAttr node.doubleArrayAttr -type doubleArray 2 3.14159 2.782;
    
    
    Python Example
    cmds.setAttr( "node.doubleArrayAttr", (2, 3.14159, 2.782,), type="doubleArray")
    
    
    
    
    
    -type matrix
    
    
    4x4 matrix of doubles
    
    
    Value Syntax
    double double double double
    double double double double
    double double double double
    double double double double
    
    
    Value Meaning
    row1col1 row1col2 row1col3 row1col4
    row2col1 row2col2 row2col3 row2col4
    row3col1 row3col2 row3col3 row3col4
    row4col1 row4col2 row4col3 row4col4
    
    
    Alternate Syntax
    string double double double
    double double double
    integer
    double double double
    double double double
    double double double
    double double double
    double double double
    double double double
    double double double double
    double double double double
    double double double
    boolean
    
    
    Alternate Meaning
    "xform" scaleX scaleY scaleZ
    rotateX rotateY rotateZ
    rotationOrder (0=XYZ, 1=YZX, 2=ZXY, 3=XZY, 4=YXZ, 5=ZYX)
    translateX translateY translateZ
    shearXY shearXZ shearYZ
    scalePivotX scalePivotY scalePivotZ
    scaleTranslationX scaleTranslationY scaleTranslationZ
    rotatePivotX rotatePivotY rotatePivotZ
    rotateTranslationX rotateTranslationY rotateTranslationZ
    rotateOrientW rotateOrientX rotateOrientY rotateOrientZ
    jointOrientW jointOrientX jointOrientY jointOrientZ
    inverseParentScaleX inverseParentScaleY inverseParentScaleZ
    compensateForParentScale
    
    
    
    Mel Example
    setAttr node.matrixAttr -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2 3 4 1;
    setAttr node.matrixAttr -type "matrix" "xform" 1 1 1 0 0 0 0 2 3 4 0 0 00 0 0 0 0 0 0 0 0 0 0 1 1 0 0 1 0 1 0 1 1 1 0 false;
    
    
    Python Example
    cmds.setAttr('node.matrixAttr',(1,0,0,0,0,1,0,0,0,0,1,0,2,3,4,1),type='matrix')
    cmds.setAttr('node.matrixAttr','xform',(1,1,1),(0,0,0),0,(2,3,4),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,1,1),(0,0,1,0),(1,0,1,0),(1,2,3),False,type="matrix")
    
    
    
    
    
    -type pointArray
    
    
    Variable length array of points
    
    
    Value Syntax
    int {double double double double}
    
    
    Value Meaning
    numberOfArrayValues {xValue yValue zValue wValue}
    
    
    Mel Example
    setAttr node.pointArrayAttr -type pointArray 2 1 1 1 1 2 2 2 1;
    
    
    Python Example
    cmds.setAttr('node.pointArrayAttr',2,(1,1,1,1),(2,2,2,1),type='pointArray')
    
    
    
    
    
    -type vectorArray
    
    
    Variable length array of vectors
    
    
    Value Syntax
    int {double double double}
    
    
    Value Meaning
    numberOfArrayValues {xValue yValue zValue}
    
    
    Mel Example
    setAttr node.vectorArrayAttr -type vectorArray 2 1 1 1 2 2 2;
    
    
    Python Example
    cmds.setAttr('node.vectorArrayAttr',2,(1,1,1),(2,2,2),type='vectorArray')
    
    
    
    
    
    -type "string"
    
    
    Character string
    
    
    Value Syntax
    string
    
    
    Value Meaning
    characterStringValue
    
    
    Mel Example
    setAttr node.stringAttr -type "string" "blarg";
    
    
    Python Example
    cmds.setAttr('node.stringAttr',"blarg",type="string")
    
    
    
    
    
    -type stringArray
    
    
    Variable length array of strings
    
    
    Value Syntax
    int {string}
    
    
    Value Meaning
    numberOfArrayValues {arrayValue}
    
    
    Mel Example
    setAttr node.stringArrayAttr -type stringArray 3 "a" "b" "c";
    
    
    Python Example
    cmds.setAttr('node.stringArrayAttr',3,"a","b","c",type='stringArray')
    
    
    
    
    
    -type sphere
    
    
    Sphere data
    
    
    Value Syntax
    double
    
    
    Value Meaning
    sphereRadius
    
    
    Example
    setAttr node.sphereAttr -type sphere 5.0;
    
    
    
    
    
    -type cone
    
    
    Cone data
    
    
    Value Syntax
    double double
    
    
    Value Meaning
    coneAngle coneCap
    
    
    Mel Example
    setAttr node.coneAttr -type cone 45.0 5.0;
    
    
    Python Example
    cmds.setAttr('node.coneAttr',45.0,5.0,type='cone')
    
    
    
    
    
    -type reflectanceRGB
    
    
    Reflectance data
    
    
    Value Syntax
    double double double
    
    
    Value Meaning
    redReflect greenReflect blueReflect
    
    
    Mel Example
    setAttr node.reflectanceRGBAttr -type reflectanceRGB 0.5 0.5 0.1;
    
    
    Python Example
    cmds.setAttr('node.reflectanceRGBAttr',0.5,0.5,0.1,type='reflectanceRGB')
    
    
    
    
    
    -type spectrumRGB
    
    
    Spectrum data
    
    
    Value Syntax
    double double double
    
    
    Value Meaning
    redSpectrum greenSpectrum blueSpectrum
    
    
    Mel Example
    setAttr node.spectrumRGBAttr -type spectrumRGB 0.5 0.5 0.1;
    
    
    Python Example
    cmds.setAttr('node.spectrumRGBAttr',0.5,0.5,0.1,type='spectrumRGB')
    
    
    
    
    
    -type componentList
    
    
    Variable length array of components
    
    
    Value Syntax
    int {string}
    
    
    Value Meaning
    numberOfComponents {componentName}
    
    
    Mel Example
    setAttr node.componentListAttr -type componentList 3 cv[1] cv[12] cv[3];
    
    
    Python Example
    cmds.setAttr('node.componentListAttr',3,'cv[1]','cv[12]','cv[3]',type='componentList')
    
    
    
    
    
    -type attributeAlias
    
    
    String alias data
    
    
    Value Syntax
    string string
    
    
    Value Meaning
    newAlias currentName
    
    
    Mel Example
    setAttr node.attrAliasAttr -type attributeAlias
    {"GoUp", "translateY", "GoLeft", "translateX"};
    
    
    Python Example
    cmds.setAttr('node.attrAliasAttr',("GoUp", "translateY","GoLeft", "translateX"),type='attributeAlias')
    
    
    
    
    
    -type nurbsCurve
    
    
    NURBS curve data
    
    
    Value Syntax
    int int int bool int int {double}
    int {double double double}
    
    
    Value Meaning
    degree spans form isRational dimension knotCount {knotValue}
    cvCount {xCVValue yCVValue [zCVValue] [wCVValue]}
    
    
    Mel Example
    // degree is the degree of the curve(range 1-7)
    // spans is the number of spans 
    // form is open (0), closed (1), periodic (2)
    // isRational is true if the curve CVs contain a rational component 
    // dimension is 2 or 3, depending on the dimension of the curve
    // knotCount is the size of the knot list
    //  knotValue is a single entry in the knot list
    // cvCount is the number of CVs in the curve
    //  xCVValue,yCVValue,[zCVValue] [wCVValue] is a single CV.
    //  zCVValue is only present when dimension is 3.
    //  wCVValue is only present when isRational is true.
    //
    $curve = `createNode nurbsCurve`;
    setAttr ($curve+".cc") -type nurbsCurve 3 1 0 no 3
    6 0 0 0 1 1 1
    4 -2 3 0 -2 1 0 -2 -1 0 -2 -3 0;
    
    
    Python Example
    # degree is the degree of the curve(range 1-7)
    # spans is the number of spans 
    # form is open (0), closed (1), periodic (2)
    # isRational is true if the curve CVs contain a rational component
    # dimension is 2 or 3, depending on the dimension of the curve
    # knotList is the list of knots
    # next argument is unused and can be set to 0
    # cvCount is the number of CVs in the curve
    #  (xCVValue,yCVValue,[zCVValue] [wCVValue]) is a single CV.
    #  zCVValue is only present when dimension is 3.
    #  wCVValue is only present when isRational is true.
    #
    curve = maya.cmds.createNode("nurbsCurve")
    maya.cmds.setAttr(curve+".cc",
    3, 1, 0, False, 3,
    (0, 0, 0, 1, 1, 1), 0,
    4,
    (-2, 3, 0), (-2, 1, 0), (-2, -1, 0), (-2, -3, 0),
    type="nurbsCurve")
    
    
    
    
    
    -type nurbsSurface
    
    
    NURBS surface data
    
    
    Value Syntax
    int int int int bool 
    int {double} 
    int {double} 
    [string] int {double double double}
    
    
    Value Meaning
    uDegree vDegree uForm vForm isRational
    uKnotCount {uKnotValue}
    vKnotCount {vKnotValue} ["TRIM"|"NOTRIM"] cvCount {xCVValue yCVValue
    zCVValue [wCVValue]}
    
    
    Mel Example
    // uDegree is degree of the surface in U direction (range 1-7)
    // vDegree is degree of the surface in V direction (range 1-7)
    // uForm is open (0), closed (1), periodic (2) in U direction
    // vForm is open (0), closed (1), periodic (2) in V direction
    // isRational is true if the surface CVs contain a rational component
    // uKnotCount is the size of the U knot list
    //  uKnotValue is a single entry in the U knot list
    // vKnotCount is the size of the V knot list
    //  vKnotValue is a single entry in the V knot list
    // If "TRIM" is specified then additional trim information is expected
    // If "NOTRIM" is specified then the surface is not trimmed
    // cvCount is the number of CVs in the surface
    //  xCVValue,yCVValue,zCVValue [wCVValue]is a single CV.
    //  zCVValue is only present when dimension is 3.
    //  wCVValue is only present when isRational is true
    //
    $surface = `createNode nurbsSurface`;
    setAttr ($surface+".cc") -type nurbsSurface 3 3 0 0 no
    6 0 0 0 1 1 1
    6 0 0 0 1 1 1
    16 -2 3 0 -2 1 0 -2 -1 0 -2 -3 0
    -1 3 0 -1 1 0 -1 -1 0 -1 -3 0
    1 3 0 1 1 0 1 -1 0 1 -3 0
    3 3 0 3 1 0 3 -1 0 3 -3 0;
    
    
    Python Example
    # uDegree is degree of the surface in U direction (range 1-7)
    # vDegree is degree of the surface in V direction (range 1-7)
    # uForm is open (0), closed (1), periodic (2) in U direction
    # vForm is open (0), closed (1), periodic (2) in V direction
    # isRational is true if the surface CVs contain a rational component
    # uKnotList is the list of knots in U
    # next argument is unused and can be set to 0
    # vKnotList is the list of knots in V
    # next argument is unused and can be set to 0
    # If "TRIM" is specified then additional trim information is expected
    # If "NOTRIM" is specified then the surface is not trimmed
    # cvCount is the number of CVs in the surface
    #  (xCVValue,yCVValue,zCVValue [wCVValue])is a single CV.
    #  zCVValue is only present when dimension is 3.
    #  wCVValue is only present when isRational is true
    #
    surface = maya.cmds.createNode("nurbsSurface")
    maya.cmds.setAttr(surface+".cc",
    3, 3, 0, 0, False,
    (0, 0, 0, 1, 1, 1), 0,
    (0, 0, 0, 1, 1, 1), 0,
    16,
    (-2, 3, 0), (-2, 1, 0), (-2, -1, 0), (-2, -3, 0),
    (-1, 3, 0), (-1, 1, 0), (-1, -1, 0), (-1, -3, 0),
    (1, 3, 0), (1, 1, 0), (1, -1, 0), (1, -3, 0),
    (3, 3, 0), (3, 1, 0), (3, -1, 0), (3, -3, 0),
    type="nurbsSurface")
    
    
    
    
    
    -type nurbsTrimface
    
    
    NURBS trim face data
    
    
    Value Syntax
    bool int {int {int {double bool bool} int {bool double}}}
    
    
    Value Meaning
    flipNormal boundaryCount {boundaryType tedgeCountOnBoundary
    {splineCountOnEdge {edgeTolerance isEdgeReversed geometricContinuity}
    {splineCountOnPedge {isMonotone pedgeTolerance}}}
    
    
    
    Example
    // flipNormal if true turns the surface inside out
    // boundaryCount: number of boundaries
    // boundaryType: 
    // tedgeCountOnBoundary    : number of edges in a boundary
    // splineCountOnEdge    : number of splines in an edge in
    // edgeTolerance        : tolerance used to build the 3d edge
    // isEdgeReversed        : if true, the edge is backwards
    // geometricContinuity    : if true, the edge is tangent continuous
    // splineCountOnPedge    : number of splines in a 2d edge
    // isMonotone            : if true, curvature is monotone
    // pedgeTolerance        : tolerance for the 2d edge
    //
    
    
    
    
    
    
    -type polyFaces
    
    
    Polygon face data
    
    
    Value Syntax
    {"f" int {int}}
    {"h" int {int}}
    {"mf" int {int}}
    {"mh" int {int}}
    {"mu" int int {int}}
    {"mc" int int {int}}
    
    
    Value Meaning
    {"f" faceEdgeCount {edgeIdValue}}
    {"h" holeEdgeCount {edgeIdValue}}
    {"mf" faceUVCount {uvIdValue}}
    {"mh" holeUVCount {uvIdValue}}
    {"mu" uvSet faceUVCount {uvIdValue}}
    {"mc" colorIndex multiColorCount {colorIdValue}}
    
    
    
    Example
    // This data type (polyFace) is meant to be used in file I/O
    // after setAttrs have been written out for vertex position
    // arrays, edge connectivity arrays (with corresponding start
    // and end vertex descriptions), texture coordinate arrays and
    // color arrays.  The reason is that this data type references
    // all of its data through ids created by the former types.
    //
    // "f" specifies the ids of the edges making up a face -
    //     negative value if the edge is reversed in the face
    // "h" specifies the ids of the edges making up a hole -
    //     negative value if the edge is reversed in the face
    // "mf" specifies the ids of texture coordinates (uvs) for a face.
    //     This data type is obsolete as of version 3.0. It is replaced by "mu".
    // "mh" specifies the ids of texture coordinates (uvs) for a hole
    //     This data type is obsolete as of version 3.0. It is replaced by "mu".
    // "mu" The  first argument refers to the uv set. This is a zero-based
    //     integer number. The second argument refers to the number of vertices (n)
    //     on the face which have valid uv values. The last n values are the uv
    //     ids of the texture coordinates (uvs) for the face. These indices
    //     are what used to be represented by the "mf" and "mh" specification.
    //     There may be more than one "mu" specification, one for each unique uv set.
    // "mc" specifies the color index values for a face. The first argument
    //     is color index. The second argument is the number of color ids to follow.
    //     Rest of the arguments are color ids for the face.
    //
    setAttr node.polyFaceAttr -type polyFaces "f" 3 1 2 3 "mc" 0 4 0 1 2 3;
    
    
    
    
    
    -type mesh
    
    
    Polygonal mesh
    
    
    Value Syntax
    {string [int {double double double}]}
    {string [int {double double double}]}
    [{string [int {double double}]}]
    {string [int {double double string}]}
    
    
    
    Value Meaning
    "v" [vertexCount {vertexX vertexY vertexZ}]
    "vn" 0
    ["vt" [uvCount {uValue vValue}]]
    "e" [edgeCount {startVertex endVertex "smooth"|"hard"}]
    "face" ["l" edgeLoopCount edgeIndex1...] ]"lt" uvCount uvIndex1...]"
    "face"...
    
    
    
    Mel Example
    // "v" specifies the vertices of the polygonal mesh
    // "vn"must be set to 0
    // "vt" is optional and specifies a U,V texture coordinate for
    each vertex
    // "e" specifies the edge connectivity information between
    vertices
    // "face" specifies face connectivity (edges/UVs) for a single face
    //
    $mesh = `createNode mesh`;
    setAttr ($mesh+".o")
    -type mesh "v" 3 0 0 0 0 1 0 0 0 1
    "vn" 3 1 0 0 1 0 0 1 0 0
    "vt" 3 0 0 0 1 1 0
    "e" 3 0 1 "hard" 1 2 "hard" 2 0 "hard"
    "face" "l" 3 0 1 2 "lt" 3 0 1 2;
    
    
    Python Example
    # "v" specifies the vertices of the polygonal mesh
    # "vn"must be set to 0
    # "vt" is optional and specifies a U,V texture coordinate for
    each vertex
    # "e" specifies the edge connectivity information between
    vertices
    # "face" specifies face connectivity (edges/UVs) for a single face
    #
    mesh = maya.cmds.createNode("mesh")
    maya.cmds.setAttr(mesh+".o",
    "v", 3, (0, 0, 0), (0, 1, 0), (0, 0, 1),
    "vn", 0,
    "vt", 3, (0, 0), (0, 1), (1, 0),
    "e", 3, 0, 1, "hard", 1, 2, "hard", 2, 0, "hard",
    "face", "l", 3, 0, 1, 2, "lt", 3, 0, 1, 2,
    type="mesh")
    
    
    
    
    
    -type lattice
    
    
    Lattice data
    
    
    Value Syntax
    int int int int {double double double}
    
    
    Value Meaning
    sDivisionCount tDivisionCount uDivisionCount
    pointCount {pointX pointY pointZ}
    
    
    Mel Example
    // sDivisionCount is the horizontal lattice division count
    // tDivisionCount is the vertical lattice division count
    // uDivisionCount is the depth lattice division count
    // pointCount is the total number of lattice points
    // pointX,pointY,pointZ is one lattice point.  The list is
    //   specified varying first in S, then in T, last in U so the
    //   first two entries are (S=0,T=0,U=0) (s=1,T=0,U=0)
    //
    $lattice = `createNode lattice`;
    setAttr ($lattice+".cc") -type lattice 2 5 2 20
    -2 -2 -2 2 -2 -2 -2 -1 -2 2 -1 -2 -2 0 -2
    2 0 -2 -2 1 -2 2 1 -2 -2 2 -2 2 2 -2
    -2 -2 2 2 -2 2 -2 -1 2 2 -1 2 -2 0 2
    2 0 2 -2 1 2 2 1 2 -2 2 2 2 2 2;
    
    
    Python Example
    # sDivisionCount is the horizontal lattice division count
    # tDivisionCount is the vertical lattice division count
    # uDivisionCount is the depth lattice division count
    # pointCount is the total number of lattice points
    # (pointX,pointY,pointZ) is one lattice point.  The list is
    #   specified varying first in S, then in T, last in U so the
    #   first two entries are (S=0,T=0,U=0) (s=1,T=0,U=0)
    #
    lattice = maya.cmds.createNode("lattice")
    maya.cmds.setAttr(lattice+".cc",
    2, 5, 2, 20,
    (-2, -2, -2), (2, -2, -2), (-2, -1, -2), (2, -1, -2), (-2, 0, -2),
    (2, 0, -2), (-2, 1, -2), (2, 1, -2), (-2, 2, -2), (2, 2, -2),
    (-2, -2, 2), (2, -2, 2), (-2, -1, 2), (2, -1, 2), (-2, 0, 2),
    (2, 0, 2), (-2, 1, 2), (2, 1, 2), (-2, 2, 2), (2, 2, 2),
    type="lattice")

    Args:
        alteredValue | av: (create) - The value is only the current value, which may change in the next evalution (if the attribute has an incoming connection). This flag is only used during file I/O, so that attributes with incoming connections do not have their data overwritten during the first evaluation after a file is opened. Not supported for Ufe attributes.
        caching | ca: (create) - Sets the attribute's internal caching on or off. Not all attributes can be defined as caching. Only those attributes that are not defined by default to be cached can be made caching.  As well, multi attribute elements cannot be made caching. Caching also affects child attributes for compound attributes. Not supported for Ufe attributes.
        capacityHint | ch: (create) - Used to provide a memory allocation hint to attributes where the -size flag cannot provide enough information. This flag is optional and is primarily intended to be used during file I/O. Only certain attributes make use of this flag, and the interpretation of the flag value varies per attribute. Not supported for Ufe attributes. This flag is currently used by (node.attribute):  mesh.face - hints the total number of elements in the face edge lists
        channelBox | cb: (create) - Sets the attribute's display in the channelBox on or off. Keyable attributes are always display in the channelBox regardless of the channelBox settting. Not supported for Ufe attributes. The display of Ufe attributes in the Channel Box is controlled using the channelBox command flag -ual/ufeFixedAttrList.
        clamp | c: (create) - For numeric attributes, if the value is outside the range of the attribute, clamp it to the min or max instead of failing. Not supported for Ufe attributes.
        keyable | k: (create) - Sets the attribute's keyable state on or off. Not supported for Ufe attributes.
        lock | l: (create) - Sets the attribute's lock state on or off.
        size | s: (create) - Defines the size of a multi-attribute array. This is only a hint, used to help allocate memory as efficiently as possible. Not supported for Ufe attributes.
        type | typ: (create) - Identifies the type of data.  If the -type flag is not present, a numeric type is assumed. Not supported for Ufe attributes.
    """
    ...


def setEditCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a tool that can be used to
    modify set membership.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def setKeyCtx(*args, breakdown: bool = ..., bd: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., preserveTangent: bool = ..., pt: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context which may be used to set keys
    within the graph editor

    Args:
        breakdown | bd: (edit, query) - Specifies whether or not to create breakdown keys
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        preserveTangent | pt: (edit, query) - Specifies whether or not to preserve tangent
    """
    ...


def sets(*args, addElement: str = ..., add: str = ..., afterFilters: bool = ..., af: bool = ..., anyMember: Optional[Union[str, bool]] = ..., am: Optional[Union[str, bool]] = ..., clear: str = ..., cl: str = ..., color: Optional[Union[int, bool]] = ..., co: Optional[Union[int, bool]] = ..., copy: Optional[Union[str, bool]] = ..., cp: Optional[Union[str, bool]] = ..., edges: bool = ..., eg: bool = ..., editPoints: bool = ..., ep: bool = ..., empty: bool = ..., em: bool = ..., facets: bool = ..., fc: bool = ..., flatten: str = ..., fl: str = ..., forceElement: str = ..., fe: str = ..., include: str = ..., intersection: Optional[Union[str, bool]] = ..., int: Optional[Union[str, bool]] = ..., isIntersecting: Optional[Union[str, bool]] = ..., ii: Optional[Union[str, bool]] = ..., isMember: Optional[Union[str, bool]] = ..., im: Optional[Union[str, bool]] = ..., layer: bool = ..., l: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., noIntermediate: bool = ..., ni: bool = ..., noSurfaceShader: bool = ..., nss: bool = ..., noWarnings: bool = ..., nw: bool = ..., nodesOnly: bool = ..., no: bool = ..., remove: str = ..., rm: str = ..., renderable: bool = ..., r: bool = ..., size: bool = ..., s: bool = ..., split: Optional[Union[str, bool]] = ..., sp: Optional[Union[str, bool]] = ..., subtract: Optional[Union[str, bool]] = ..., sub: Optional[Union[str, bool]] = ..., text: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ..., union: Optional[Union[str, bool]] = ..., un: Optional[Union[str, bool]] = ..., vertices: bool = ..., v: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to create a set, query some state of
    a set, or perform operations to update the membership of a set.
    A set is a logical grouping of an arbitrary collection of objects,
    attributes, or components of objects. Sets are dependency nodes.
    Connections from objects to a set define membership in the set.
    
    Sets are used throughout Maya in a multitude of ways. They are used
    to define an association of material properties to objects, to define
    an association of lights to objects, to define a bookmark or named
    collection of objects, to define a character, and to define the
    components to be deformed by some deformation operation.
    
    Sets can be connected to any number of partitions. A partition is
    a node which enforces mutual exclusivity amoung the sets in the
    partition. That is, if an object is in a
    set which is in a partition, that object cannot be a member of any
    other set that is in the partition.
    
    Without any flags, the sets command will create a set with a
    default name of "set#" (where # is an integer). If no items are
    specified on the command line, the currently selected items are added
    to the set. The -em/empty flag can be used to create an empty
    set and not have the selected items added to the set.
    
    Sets can be created to have certain restrictions on membership. There
    can be "renderable" sets which only allow renderable objects (such as
    nurbs geometry or polymesh faces) to be members of the set. There can
    also be vertex (or control point), edit point, edge, or face sets
    which only allow those types of components to be members of a set.
    Note that for these sets, if an object with a valid type of component
    is to be added to a set, the components of the object are
    added to the set instead.
    
    Sets can have an associated color which is only of use
    when creating vertex sets. The color can be one of the eight user
    defined colors defined in the color preferences. This color can
    be used, for example to distinguish which vertices are being deformed
    by a particular deformation.
    
    Objects, components, or attributes can be added to a set using one of
    three flags. The -add/addElement flag will add the objects to a set as
    long as this won't break any mutual exclusivity constraints. If there
    are any items which can't be added, the command will fail. The
    -in/include flag will only add those items which can be added and
    warn of those which can't. The -fe/forceElement flag will add all the
    items to the set but will also remove any of those items that are in
    any other set which is in the same partition as the set.
    
    There are several operations on sets that can be performed with the
    sets command. Membership can be queried. Tests for whether
    an item is in a set or whether two sets share the same item
    can be performed. Also, the union, intersection and
    difference of sets can be performed which returns a list of members
    of the sets which are a result of the operation.

    Args:
        addElement | add: (edit) - Adds the list of items to the given set.  If some of the items cannot be added to the set because they are in another set which is in the same partition as the set to edit, the command will fail.
        afterFilters | af: (edit) - Default state is false. This flag is valid in edit mode only. This flag is for use on sets that are acted on by deformers such as sculpt, lattice, blendShape. The default edit mode is to edit the membership of the group acted on by the deformer. If you want to edit the group but not change the membership of the deformer, set the flag to true.
        anyMember | am: (create) - An operation which tests whether any of the given items are members of the given set.
        clear | cl: (edit) - An operation which removes all items from the given set making the set empty.
        color | co: (create, edit, query) - Defines the hilite color of the set. Must be a value in range [-1, 7] (one of the user defined colors).  -1 marks the color has being undefined and therefore not having any affect. Only the vertices of a vertex set will be displayed in this color.
        copy | cp: (create) - Copies the members of the given set to a new set. This flag is for use in creation mode only.
        edges | eg: (create, query) - Indicates the new set can contain edges only. This flag is for use in creation or query mode only. The default value is false.
        editPoints | ep: (create, query) - Indicates the new set can contain editPoints only. This flag is for use in creation or query mode only. The default value is false.
        empty | em: (create) - Indicates that the set to be created should be empty. That is, it ignores any arguments identifying objects to be added to the set. This flag is only valid for operations that create a new set.
        facets | fc: (create, query) - Indicates the new set can contain facets only. This flag is for use in creation or query mode only. The default value is false.
        flatten | fl: (edit) - An operation that flattens the structure of the given set. That is, any sets contained by the given set will be replaced by its members so that the set no longer contains other sets but contains the other sets' members.
        forceElement | fe: (edit) - For use in edit mode only. Forces addition of the items to the set. If the items are in another set which is in the same partition as the given set, the items will be removed from the other set in order to keep the sets in the partition mutually exclusive with respect to membership.
        include | include: (edit) - Adds the list of items to the given set.  If some of the items cannot be added to the set, a warning will be issued. This is a less strict version of the -add/addElement operation.
        intersection | int: (create) - An operation that returns a list of items which are members of all the sets in the list.
        isIntersecting | ii: (create) - An operation which tests whether the sets in the list have common members.
        isMember | im: (create) - An operation which tests whether all the given items are members of the given set.
        layer | l: (create) - OBSOLETE. DO NOT USE.
        name | n: (create) - Assigns string as the name for a new set. This flag is only valid for operations that create a new set.
        noIntermediate | ni: (create, query) - Excludes intermediate objects when querying set members or using the subtract, union, itersection, or isIntersecting flags.
        noSurfaceShader | nss: (create) - If set is renderable, do not connect it to the default surface shader.  Flag has no meaning or effect for non renderable sets. This flag is for use in creation mode only. The default value is false.
        noWarnings | nw: (create) - Indicates that warning messages should not be reported such as when trying to add an invalid item to a set. (used by UI)
        nodesOnly | no: (query) - This flag is usable with the -q/query flag but is ignored if used with another queryable flags. This flag modifies the results of the set membership query such that when there are attributes (e.g. sphere1.tx) or components of nodes included in the set, only the nodes will be listed. Each node will only be listed once, even if more than one attribute or component of the node exists in the set.
        remove | rm: (edit) - Removes the list of items from the given set.
        renderable | r: (create, query) - This flag indicates that a special type of set should be created. This type of set (shadingEngine as opposed to objectSet) has certain restrictions on its membership in that it can only contain renderable elements such as lights and geometry. These sets are referred to as shading groups and are automatically connected to the "renderPartition" node when created (to ensure mutual exclusivity of the set's members with the other sets in the partition). This flag is for use in creation or query mode only. The default value is false which means a normal set is created.
        size | s: (query) - Use the size flag to query the length of the set.
        split | sp: (create) - Produces a new set with the list of items and removes each item in the list of items from the given set.
        subtract | sub: (create) - An operation between two sets which returns the members of the first set that are not in the second set.
        text | t: (create, edit, query) - Defines an annotation string to be stored with the set.
        union | un: (create) - An operation that returns a list of all the members of all sets listed.
        vertices | v: (create, query) - Indicates the new set can contain vertices only. This flag is for use in creation or query mode only. The default value is false.
    """
    ...


def setToolTo(*args) -> Any:
    r"""
    This command switches control to the named context.

    Args:
    """
    ...


def shadingGeometryRelCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., offCommand: Optional[Union[str, bool]] = ..., ofc: Optional[Union[str, bool]] = ..., onCommand: Optional[Union[str, bool]] = ..., onc: Optional[Union[str, bool]] = ..., shadingCentric: bool = ..., s: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context that can be used for associating geometry
    to shading groups.  You can put the context into shading-centric mode
    by using the -shadingCentric flag and specifying true.  This means that the
    shading group is selected first then geometry associated with the shading
    group are highlighted.  Subsequent selections result in assignments.
    
    Specifying -shadingCentric false means that the geometry is to be selected
    first.  The shading group associated with the geometry will then be selected
    and subsequent selections will result in assignments being made.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        offCommand | ofc: (create, edit, query) - command to be issued when context is turned on
        onCommand | onc: (create, edit, query) - command to be issued when context is turned on
        shadingCentric | s: (create, edit, query) - shading-centric mode.
    """
    ...


def shadingLightRelCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., offCommand: Optional[Union[str, bool]] = ..., ofc: Optional[Union[str, bool]] = ..., onCommand: Optional[Union[str, bool]] = ..., onc: Optional[Union[str, bool]] = ..., shadingCentric: bool = ..., s: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context that can be used for associating lights
    to shading groups.  You can put the context into shading-centric mode
    by using the -shadingCentric flag and specifying true.  This means that the
    shading group is selected first then lights associated with the shading
    group are highlighted.  Subsequent selections result in assignments.
    
    Specifying -shadingCentric false means that the light is to be selected
    first. The shading groups associated with the light will then be selected
    and subsequent selections will result in assignments being made.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        offCommand | ofc: (create, edit, query) - command to be issued when context is turned on
        onCommand | onc: (create, edit, query) - command to be issued when context is turned on
        shadingCentric | s: (create, edit, query) - shading-centric mode.
    """
    ...


def shapeCompare(*args) -> Any:
    r"""
    Compares two shapes.
    If no shapes are specified in the command line, then the
    shapes from the active list are used.

    Args:
    """
    ...


def showHidden(*args, above: bool = ..., a: bool = ..., allObjects: bool = ..., all: bool = ..., below: bool = ..., b: bool = ..., lastHidden: bool = ..., lh: bool = ...) -> Any:
    r"""
    The showHidden command is used to make invisible
    objects visible.  If no flags are specified, only the objects
    given to the command will be made visible. If a parent of an object
    is invisible, the object will still be invisible. Invisibility
    is inherited. To ensure the object becomes visible, use the
    -a/above flag. This forces all invisible ancestors of the object(s)
    to be visible. If the -b/below flag is used, any invisible objects
    below the object will be made visible.  To make all objects visible,
    use the -all/allObjects flag.
    
    See also: hide

    Args:
        above | a: (create) - Make objects and all their invisible ancestors visible.
        allObjects | all: (create) - Make all invisible objects visible.
        below | b: (create) - Make objects and all their invisible descendants visible.
        lastHidden | lh: (create) - Show everything that was hidden with the last hide command.
    """
    ...


def showManipCtx(*args, addAttr: str = ..., aa: str = ..., currentNodeName: bool = ..., cnn: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., incSnap: Optional[Union[Tuple[int, bool], bool]] = ..., incSnapRelative: Optional[Union[Tuple[int, bool], bool]] = ..., isr: Optional[Union[Tuple[int, bool], bool]] = ..., incSnapUI: bool = ..., isu: bool = ..., incSnapValue: Optional[Union[Tuple[int, float], bool]] = ..., isv: Optional[Union[Tuple[int, float], bool]] = ..., iveVisible: bool = ..., iv: bool = ..., lockSelection: bool = ..., ls: bool = ..., moveActiveAttrDown: bool = ..., md: bool = ..., moveActiveAttrToTop: bool = ..., mtt: bool = ..., moveActiveAttrUp: bool = ..., mu: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., removeAttr: str = ..., ra: str = ..., resetActiveAttr: bool = ..., raa: bool = ..., selectedAttributes: bool = ..., sa: bool = ..., setAttrActive: str = ..., saa: str = ..., setNextAttrActive: bool = ..., sna: bool = ..., setPreviousAttrActive: bool = ..., spa: bool = ..., toggleIncSnap: bool = ..., tis: bool = ..., toolFinish: Optional[Union[str, bool]] = ..., tf: Optional[Union[str, bool]] = ..., toolStart: Optional[Union[str, bool]] = ..., ts: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create a show manip context.  The show manip
    context will display manips for all selected objects that have valid
    manips defined for them.

    Args:
        addAttr | aa: (edit) - Add a specific attribute to the In View Editor attribute list.
        currentNodeName | cnn: (query) - Returns the name of the first node that the context is attached to.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        incSnap | incSnap: (create, edit, multiuse, query) - If true, the manipulator owned by the context will use incremental snapping for specified mode.
        incSnapRelative | isr: (create, edit, multiuse, query) - If true, the manipulator owned by the context will use relative incremental snapping for specified mode.
        incSnapUI | isu: (query) - Returns an array of elements indicating what kind of incremental snap UI is required by the manipulator owned by the context. If no UI is required, the result array will contain a single element of with the value 0. The other values and their meanings are:  1 - UI for linear incremental translate 2 - UI for incremental rotate 3 - UI for inclremental scale
        incSnapValue | isv: (create, edit, multiuse, query) - Supply the step value which the manipulator owned by the context will use for specified mode.
        iveVisible | iv: (edit, query) - Set the In View Editor visible or not.
        lockSelection | ls: (create, edit, query) - If true, this context will never change the current selection. By default this is set to false.
        moveActiveAttrDown | md: (edit) - Move the In View Editor active attribute down one in the list.
        moveActiveAttrToTop | mtt: (edit) - Move the In View Editor active attribute to the top of the list.
        moveActiveAttrUp | mu: (edit) - Move the In View Editor active attribute up one in the list.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        removeAttr | ra: (edit) - Remove a specific attribute from the In View Editor attribute list.
        resetActiveAttr | raa: (edit) - Reset the In View Editor active attribute to its default value.
        selectedAttributes | sa: (query) - Returns a list of the names of the attributes that are currently visible in the In View Editor.
        setAttrActive | saa: (edit) - Set a specific attribute from the In View Editor attribute list active.
        setNextAttrActive | sna: (edit) - Set the next attribute in the In View Editor attribute list active.
        setPreviousAttrActive | spa: (edit) - Set the previous attribute in the In View Editor attribute list active.
        toggleIncSnap | tis: (create, edit) - Toggles (enables/disables) snapping for all modes.
        toolFinish | tf: (create, edit, query) - Supply the script that will be run when the user exits the script.
        toolStart | ts: (create, edit, query) - Supply the script that will be run when the user first enters the script
    """
    ...


def skinBindCtx(*args, about: Optional[Union[str, bool]] = ..., a: Optional[Union[str, bool]] = ..., axis: Optional[Union[str, bool]] = ..., ax: Optional[Union[str, bool]] = ..., colorRamp: Optional[Union[str, bool]] = ..., cr: Optional[Union[str, bool]] = ..., currentInfluence: Optional[Union[str, bool]] = ..., ci: Optional[Union[str, bool]] = ..., displayInactiveMode: Optional[Union[int, bool]] = ..., di: Optional[Union[int, bool]] = ..., displayNormalized: bool = ..., dn: bool = ..., exists: bool = ..., ex: bool = ..., falloffCurve: Optional[Union[str, bool]] = ..., fc: Optional[Union[str, bool]] = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., symmetry: bool = ..., s: bool = ..., tolerance: Optional[Union[float, bool]] = ..., t: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a tool that can be used to edit volumes from an interactive bind.

    Args:
        about | a: (create, edit, query) - The space in which the axis should be mirrored. Valid values are: "world" and "object".
        axis | ax: (create, edit, query) - The mirror axis. Valid values are: "x","y", and "z".
        colorRamp | cr: (create, edit, query) - Set the values on the color ramp used to display the weight values.
        currentInfluence | ci: (create, edit, query) - Set the index of the current influence or volume to be adjusted by the manipulator.
        displayInactiveMode | di: (create, edit, query) - Determines the display mode for drawing volumes that are not selected, in particular which volume cages if any are displayed. 0 - None 1 - Nearby volumes 2 - All volumes
        displayNormalized | dn: (create, edit, query) - Display raw select weights (false) or finalized normalized weights (true).
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        falloffCurve | fc: (create, edit, query) - Set the values on the falloff curve control.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        symmetry | s: (create, edit, query) - Controls whether or not the tool operates in symmetric (mirrored) mode.
        tolerance | t: (create, edit, query) - The tolerance setting for determining whether another influence is symmetric to the the current influence.
    """
    ...


def snapMode(*args, curve: bool = ..., c: bool = ..., distanceIncrement: Optional[Union[float, bool]] = ..., dsi: Optional[Union[float, bool]] = ..., edgeMagnet: Optional[Union[int, bool]] = ..., em: Optional[Union[int, bool]] = ..., edgeMagnetTolerance: Optional[Union[float, bool]] = ..., emt: Optional[Union[float, bool]] = ..., grid: bool = ..., gr: bool = ..., liveFaceCenter: bool = ..., lfc: bool = ..., livePoint: bool = ..., lp: bool = ..., meshCenter: bool = ..., mc: bool = ..., pixelCenter: bool = ..., pc: bool = ..., pixelSnap: bool = ..., ps: bool = ..., point: bool = ..., p: bool = ..., tolerance: Optional[Union[int, bool]] = ..., t: Optional[Union[int, bool]] = ..., useTolerance: bool = ..., ut: bool = ..., uvTolerance: Optional[Union[int, bool]] = ..., uvt: Optional[Union[int, bool]] = ..., viewPlane: bool = ..., vp: bool = ..., query: bool = ...) -> Any:
    r"""
    The snapMode command is used to control snapping.  It toggles the
    snapping modes in effect and sets information used for snapping.

    Args:
        curve | c: (create, query) - Set curve snap mode
        distanceIncrement | dsi: (create, query) - Set the distance for the snapping to objects such as a lines or planes.
        edgeMagnet | em: (create, query) - Number of extra magnets to snap onto, regularly spaced along the edge.
        edgeMagnetTolerance | emt: (create, query) - Precision for edge magnet snapping.
        grid | gr: (create, query) - Set grid snap mode
        liveFaceCenter | lfc: (create, query) - While moving on live polygon objects, snap to its face centers.
        livePoint | lp: (create, query) - While moving on live polygon objects, snap to its vertices.
        meshCenter | mc: (create, query) - While moving, snap on the center of the mesh that intersect the line from the camera to the cursor.
        pixelCenter | pc: (create, query) - Snap UV to the center of the pixel instead of the corner.
        pixelSnap | ps: (create, query) - Snap UVs to the nearest pixel center or corner.
        point | p: (create, query) - Set point snap mode
        tolerance | t: (create, query) - Tolerance defines the size of the square region in which points must lie in order to be snapped to. The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).
        useTolerance | ut: (create, query) - If useTolerance is set, then point snapping is limited to points that are within a square region surrounding the cursor position. The size of the square is determined by the tolerance value.
        uvTolerance | uvt: (create, query) - uvTolerance defines the size of the square region in which points must lie in order to be snapped to, in the UV Editor.  The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).
        viewPlane | vp: (create, query) - Set view-plane snap mode
    """
    ...


def snapTogetherCtx(*args, clearSelection: bool = ..., cs: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., setOrientation: bool = ..., so: bool = ..., snapPolygonFace: bool = ..., spf: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The snapTogetherCtx command creates a tool for snapping surfaces
    together.

    Args:
        clearSelection | cs: (create, edit, query) - Sets whether the tool should clear the selection on entry to the tool. Default true.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        setOrientation | so: (create, edit, query) - Sets whether the tool should orient as well as moving an item. Default true.
        snapPolygonFace | spf: (create, edit, query) - Sets whether the tool should snap the cursor to polygon face centers. Default false.
    """
    ...


def softModCtx(*args, dragSlider: str = ..., ds: str = ..., exists: bool = ..., ex: bool = ..., falseColor: bool = ..., fc: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., reset: bool = ..., rst: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Controls the softMod context.

    Args:
        dragSlider | ds: (edit) - Specify the slider mode for hotkey radius resizing.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        falseColor | fc: (edit) - Enable or disable false color display on the soft mod manipulator.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        reset | rst: (edit, query) - Reset the tool options to their default values.
    """
    ...


def softSelect(*args, compressUndo: Optional[Union[int, bool]] = ..., cu: Optional[Union[int, bool]] = ..., enableFalseColor: Optional[Union[int, bool]] = ..., efc: Optional[Union[int, bool]] = ..., softSelectColorCurve: Optional[Union[str, bool]] = ..., scc: Optional[Union[str, bool]] = ..., softSelectCurve: Optional[Union[str, bool]] = ..., ssc: Optional[Union[str, bool]] = ..., softSelectDistance: Optional[Union[float, bool]] = ..., ssd: Optional[Union[float, bool]] = ..., softSelectEnabled: Optional[Union[int, bool]] = ..., sse: Optional[Union[int, bool]] = ..., softSelectFalloff: Optional[Union[int, bool]] = ..., ssf: Optional[Union[int, bool]] = ..., softSelectReset: bool = ..., ssr: bool = ..., softSelectUVDistance: Optional[Union[float, bool]] = ..., sud: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command allows you to change the soft modelling options.
    
    Soft modelling is an option that allows for reflection of basic
    manipulator actions such as move, rotate, and scale.

    Args:
        compressUndo | cu: (create, edit, query) - Controls how soft selection settings behave in undo:  0 means all changes undo individually 1 means all consecutive changes undo as a group 2 means only interactive changes undo as a group  When queried, returns an int indicating the current undo behaviour.
        enableFalseColor | efc: (create, edit, query) - Set soft select color feedback on or off. When queried, returns an int indicating whether color feedback is currently enabled.
        softSelectColorCurve | scc: (create, edit, query) - Sets the color ramp used to display false color feedback for soft selected components in the viewport. The color curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is represented by 5 successive values: 3 RGB values (the color to use), an input value (the selection weight), and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current color feedback curve.
        softSelectCurve | ssc: (create, edit, query) - Sets the falloff curve used to calculate selection weights for components within the falloff distance. The curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is represented by 3 successive values: an output value (the selection weight at this point), an input value (the normalised falloff distance) and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current falloff curve.
        softSelectDistance | ssd: (create, edit, query) - Sets the falloff distance (radius) used for world and object space soft selection. When queried, returns a float indicating the current falloff distance.
        softSelectEnabled | sse: (create, edit, query) - Sets soft selection based modeling on or off. When queried, returns an int indicating the current state of the option.
        softSelectFalloff | ssf: (create, edit, query) - Sets the falloff mode:  0 for volume based falloff 1 for surface based falloff 2 for global falloff  When queried, returns an int indicating the falloff mode.
        softSelectReset | ssr: (create, edit) - Resets soft selection to its default settings.
        softSelectUVDistance | sud: (create, edit, query) - Sets the falloff distance (radius) used for UV space soft selection. When queried, returns a float indicating the current falloff distance.
    """
    ...


def spaceLocator(*args, absolute: bool = ..., a: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., position: Optional[Union[Tuple[float, float, float], bool]] = ..., p: Optional[Union[Tuple[float, float, float], bool]] = ..., relative: bool = ..., r: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The command creates a locator at the specified position
    in space. By default it is created at (0,0,0).

    Args:
        absolute | a: (create, edit) - If set, the locator's position is in world space.
        name | n: (create, edit) - Name for the locator.
        position | p: (create, edit, query) - Location in  3-dimensional space where locator is to be created.
        relative | r: (create, edit) - If set, the locator's position is relative to its local space. The locator is created in relative mode by default.
    """
    ...


def srtContext(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create a combined transform
    (translate/scale/rotate) context.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def suitePrefs(*args, applyToSuite: Optional[Union[str, bool]] = ..., ats: Optional[Union[str, bool]] = ..., installedAsSuite: bool = ..., ias: bool = ..., isCompleteSuite: bool = ..., ics: bool = ...) -> Any:
    r"""
    This command sets the mouse and keyboard interaction mode
    for Maya and other Suites applications (if Maya is part of
    a Suites install).

    Args:
        applyToSuite | ats: (create) - Apply the mouse and keyboard interaction settings for the given application to all applications in the Suite (if Maya is part of a Suites install). Valid values are "Maya", "3dsMax", or "undefined", which signifies that each app is to use their own settings.
        installedAsSuite | ias: (create) - Returns true if Maya is part of a Suites install, false otherwise.
        isCompleteSuite | ics: (create) - Returns true if the Suites install contains all Entertainment Creation Suite products, false otherwise.
    """
    ...


def symmetricModelling(*args, about: Optional[Union[str, bool]] = ..., a: Optional[Union[str, bool]] = ..., allowPartial: bool = ..., ap: bool = ..., axis: Optional[Union[str, bool]] = ..., ax: Optional[Union[str, bool]] = ..., preserveSeam: Optional[Union[int, bool]] = ..., ps: Optional[Union[int, bool]] = ..., reset: bool = ..., r: bool = ..., seamFalloffCurve: Optional[Union[str, bool]] = ..., sf: Optional[Union[str, bool]] = ..., seamTolerance: Optional[Union[float, bool]] = ..., st: Optional[Union[float, bool]] = ..., symmetry: Optional[Union[int, bool]] = ..., s: Optional[Union[int, bool]] = ..., tolerance: Optional[Union[float, bool]] = ..., t: Optional[Union[float, bool]] = ..., topoSymmetry: bool = ..., ts: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command allows you to change the symmetric modelling options.
    
    Symmetric modelling is an option that allows for reflection of basic
    manipulator actions such as move, rotate, and scale.

    Args:
        about | a: (create, edit, query) - Set the space in which symmetry should be calculated (object or world or topo). When queried, returns a string which is the current space being used.
        allowPartial | ap: (create, edit, query) - Specifies whether partial symmetry should be allowed when enabling topological symmetry.
        axis | ax: (create, edit, query) - Set the current axis to be reflected over. When queried, returns a string which is the current axis.
        preserveSeam | ps: (create, edit, query) - Controls whether selection or symmetry should take priority on the plane of symmetry. When queried, returns an int for the option.
        reset | r: (create, edit) - Reset the redo information before starting.
        seamFalloffCurve | sf: (create, edit, query) - Set the seam's falloff curve, used to control the seam strength within the seam tolerance. The string is a comma separated list of sets of 3 values for each curve point. When queried, returns a string which is the current space being used.
        seamTolerance | st: (create, edit, query) - Set the seam tolerance used for reflection. When preserveSeam is enabled, this tolerance controls the width of the enforced seam. When queried, returns a float of the seamTolerance.
        symmetry | s: (create, edit, query) - Set the symmetry option on or off. When queried, returns an int for the option.
        tolerance | t: (create, edit, query) - Set the tolerance of reflection. When queried, returns a float of the tolerance.
        topoSymmetry | ts: (create, edit, query) - Enable/disable topological symmetry. When enabled, the supplied component/active list will be used to define the topological symmetry seam. When queried, returns the name of the active topological symmetry object.
    """
    ...


def targetWeldCtx(*args, exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., mergeToCenter: bool = ..., mtc: bool = ..., preserveUV: bool = ..., puv: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create a new context to weld vertices together on a poly object.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        mergeToCenter | mtc: (create, edit, query) - If mergeToCenter is set to true then the source and target vertices's will be moved to the center before doing the merge.  If set to false the source vertex will be moved to the target vertex before doing the merge.
        preserveUV | puv: (edit, query) - When false, UVs are not changed when welding components. When true, the UVs are modified to stop texture swimming when welding components. Default is true.
    """
    ...


def texCutContext(*args, adjustSize: bool = ..., asz: bool = ..., displayShellBorders: bool = ..., dsb: bool = ..., edgeSelectSensitive: Optional[Union[float, bool]] = ..., ess: Optional[Union[float, bool]] = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., mode: Optional[Union[str, bool]] = ..., m: Optional[Union[str, bool]] = ..., moveRatio: Optional[Union[float, bool]] = ..., mvr: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., size: Optional[Union[float, bool]] = ..., sz: Optional[Union[float, bool]] = ..., steadyStroke: bool = ..., ss: bool = ..., steadyStrokeDistance: Optional[Union[float, bool]] = ..., ssd: Optional[Union[float, bool]] = ..., touchToSew: bool = ..., tts: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context for cut uv tool.  This
    context only works in the UV editor.

    Args:
        adjustSize | asz: (edit) - If true, puts the tool into the mode where dragging the mouse will edit the brush size. If false, puts the tool back into the previous mode.
        displayShellBorders | dsb: (edit, query) - Toggle the display of shell borders.
        edgeSelectSensitive | ess: (edit, query) - Set the value of the edge selection sensitivity.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        mode | m: (edit, query) - Specifies the type of effect the brush will perform, Cut or Sew.
        moveRatio | mvr: (edit, query) - The cut open ratio relative to edge length.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        size | sz: (edit, query) - Brush size value of the brush ring.
        steadyStroke | ss: (edit, query) - Turn on steady stroke or not.
        steadyStrokeDistance | ssd: (edit, query) - The distance for steady stroke.
        touchToSew | tts: (edit, query) - Toggle the touch to sew mode.
    """
    ...


def texLatticeDeformContext(*args, envelope: Optional[Union[float, bool]] = ..., ev: Optional[Union[float, bool]] = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., latticeColumns: Optional[Union[int, bool]] = ..., lc: Optional[Union[int, bool]] = ..., latticeRows: Optional[Union[int, bool]] = ..., lr: Optional[Union[int, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., showMoveManipulator: bool = ..., smm: bool = ..., snapPixelMode: bool = ..., spm: bool = ..., useBoundingRect: bool = ..., ubr: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context which may be used to
    deform UV maps with lattice manipulator.  This context
    only works in the texture UV editor.

    Args:
        envelope | ev: (create, edit, query) - Specifies the influence of the lattice.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        latticeColumns | lc: (create, edit, query) - Specifies the number column points the lattice contains.  The maximum size lattice is restricted to 8 columns.
        latticeRows | lr: (create, edit, query) - Specifies the number of rows the lattice contains. The maximum size lattice is restricted to 8 rows.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        showMoveManipulator | smm: (create, edit, query) - Specifies whether show move manipulator in UV Editor
        snapPixelMode | spm: (create, edit, query) - Specifies the influenced uv points should be snapped to a pixel center or corner.
        useBoundingRect | ubr: (create, edit, query) - When constructing the lattice use the bounding box of the selected UVs for the extents of the lattice.  When this is disabled the extents of the marquee selections are used as the extents for the lattice.
    """
    ...


def texManipContext(*args, exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command used to register the texSelectCtx tool.
    Command used to register the texManipCtx tool.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
    """
    ...


def texMoveContext(*args, editPivotMode: bool = ..., epm: bool = ..., exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., position: bool = ..., p: bool = ..., snap: bool = ..., s: bool = ..., snapComponentsRelative: bool = ..., scr: bool = ..., snapPixelMode: Optional[Union[int, bool]] = ..., spm: Optional[Union[int, bool]] = ..., snapValue: Optional[Union[float, bool]] = ..., sv: Optional[Union[float, bool]] = ..., tweakMode: bool = ..., twk: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create, edit, or query a texture editor
    move manip context.
    Note that the above flags control the global behaviour of all texture
    editor move manip contexts.  Changing one context independently is not
    allowed.  Changing a context's behaviour using the above flags, will
    change all existing texture editor move manip contexts.

    Args:
        editPivotMode | epm: (query) - Returns true when the manipulator is in edit pivot mode.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        position | p: (query) - Returns the current position of the manipulator
        snap | s: (edit, query) - Sets or queries whether snapping is to be used.
        snapComponentsRelative | scr: (edit, query) - Value can be : true or false. If true, while snapping a group of UVs, the relative spacing between them will be preserved. If false, all the UVs will be snapped to the target point
        snapPixelMode | spm: (edit, query) - Sets the snapping mode to be the pixel center or upper left corner.
        snapValue | sv: (edit, query) - Sets or queries the size of the snapping increment.
        tweakMode | twk: (edit, query) - When true, the manipulator is hidden and highlighted components can be selected and moved in one step using a click-drag interaction.
    """
    ...


def texMoveUVShellContext(*args, exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., iterations: Optional[Union[int, bool]] = ..., it: Optional[Union[int, bool]] = ..., mask: bool = ..., m: bool = ..., position: bool = ..., p: bool = ..., shellBorder: Optional[Union[float, bool]] = ..., sb: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create, edit, or query a texture editor
    move manip context.
    Note that the above flags control the global behaviour of all texture
    editor move manip contexts.  Changing one context independently is not
    allowed.  Changing a context's behaviour using the above flags, will
    change all existing texture editor move manip contexts.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        iterations | it: (edit, query) - Sets or queries the number of iterations to perform.
        mask | m: (edit, query) - Sets or queries masking on the shell.
        position | p: (query) - Returns the current position of the manipulator
        shellBorder | sb: (edit, query) - Sets or queries the size of the shell border.
    """
    ...


def texRotateContext(*args, editPivotMode: bool = ..., epm: bool = ..., exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., position: bool = ..., p: bool = ..., snap: bool = ..., s: bool = ..., snapRelative: bool = ..., sr: bool = ..., snapValue: Optional[Union[float, bool]] = ..., sv: Optional[Union[float, bool]] = ..., tweakMode: bool = ..., twk: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create, edit, or query a
    rotate context for the UV Editor.
    Note that the above flag controls the global behaviour of all texture
    editor rotate contexts.  Changing one context independently is not
    allowed.  Changing a context's behaviour using the above flag, will
    change all existing texture editor rotate contexts.

    Args:
        editPivotMode | epm: (query) - Returns true when the manipulator is in edit pivot mode.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        position | p: (query) - Returns the current position of the manipulator.
        snap | s: (edit, query) - Sets or queries whether snapping is to be used.
        snapRelative | sr: (edit, query) - Sets or queries whether snapping is relative.
        snapValue | sv: (edit, query) - Sets or queries the size of the snapping increment.
        tweakMode | twk: (edit, query) - When true, the manipulator is hidden and highlighted components can be selected and rotated in one step using a click-drag interaction.
    """
    ...


def texScaleContext(*args, editPivotMode: bool = ..., epm: bool = ..., exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., position: bool = ..., p: bool = ..., preventNegativeScale: bool = ..., pns: bool = ..., snap: bool = ..., s: bool = ..., snapRelative: bool = ..., sr: bool = ..., snapValue: Optional[Union[float, bool]] = ..., sv: Optional[Union[float, bool]] = ..., tweakMode: bool = ..., twk: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create, edit, or query a
    scale context for the UV Editor.
    Note that the above flag controls the global behaviour of all texture
    editor scale contexts.  Changing one context independently is not
    allowed.  Changing a context's behaviour using the above flag, will
    change all existing texture editor scale contexts.

    Args:
        editPivotMode | epm: (query) - Returns true when manipulator is in edit pivot mode.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        position | p: (query) - Returns the current position of the manipulator.
        preventNegativeScale | pns: (edit, query) - Prevent negative scale for components.
        snap | s: (edit, query) - Sets or queries whether snapping is to be used.
        snapRelative | sr: (edit, query) - Sets or queries whether snapping is relative.
        snapValue | sv: (edit, query) - Sets or queries the size of the snapping increment.
        tweakMode | twk: (edit, query) - When true, the manipulator is hidden and highlighted components can be selected and scaled in one step using a click-drag interaction.
    """
    ...


def texSculptCacheContext(*args, adjustSize: bool = ..., asz: bool = ..., adjustStrength: bool = ..., ast: bool = ..., direction: Optional[Union[int, bool]] = ..., d: Optional[Union[int, bool]] = ..., falloffType: Optional[Union[int, bool]] = ..., ft: Optional[Union[int, bool]] = ..., floodPin: Optional[Union[float, bool]] = ..., fp: Optional[Union[float, bool]] = ..., grabTwist: bool = ..., gtw: bool = ..., inverted: bool = ..., inv: bool = ..., mode: Optional[Union[str, bool]] = ..., m: Optional[Union[str, bool]] = ..., sculptFalloffCurve: Optional[Union[str, bool]] = ..., sfc: Optional[Union[str, bool]] = ..., showBrushRingDuringStroke: bool = ..., sbr: bool = ..., size: Optional[Union[float, bool]] = ..., sz: Optional[Union[float, bool]] = ..., strength: Optional[Union[float, bool]] = ..., st: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This is a tool context command for uv cache sculpting tool.

    Args:
        adjustSize | asz: (edit) - If true, puts the tool into the mode where dragging the mouse will edit the brush size. If false, puts the tool back into the previous sculpt mode.
        adjustStrength | ast: (edit) - If true, puts the tool into the mode where dragging the mouse will edit the brush strength. If false, puts the tool back into the previous sculpt mode.
        direction | d: (edit, query) - Specifies how the brush determines where the uvs go.
        falloffType | ft: (edit, query) - Specifies how the brush determines which uvs to affect.
        floodPin | fp: (create, edit) - Sets the pin value for each UV to the given value
        grabTwist | gtw: (create, edit, query) - If true, the grab brush twists the UVs
        inverted | inv: (create, edit, query) - If true, inverts the effect of the brush.
        mode | m: (edit, query) - Specifies the type of sculpting effect the brush will perform.
        sculptFalloffCurve | sfc: (edit, query) - Specifies the falloff curve that affects the brush.
        showBrushRingDuringStroke | sbr: (edit, query) - Specifies whether or not to show the brush ring during stroke.
        size | sz: (edit, query) - Specifies the world-space size of the current brush.
        strength | st: (edit, query) - Specifies the world-space strength of the current brush.
    """
    ...


def texSelectContext(*args, exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command used to register the texSelectCtx tool.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
    """
    ...


def texSelectShortestPathCtx(*args, exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Creates a new context to select shortest edge path
    between two vertices or UVs in the texture editor window.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
    """
    ...


def texSmudgeUVContext(*args, dragSlider: Optional[Union[str, bool]] = ..., ds: Optional[Union[str, bool]] = ..., effectType: Optional[Union[str, bool]] = ..., et: Optional[Union[str, bool]] = ..., exists: bool = ..., ex: bool = ..., functionType: Optional[Union[str, bool]] = ..., ft: Optional[Union[str, bool]] = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., pressure: Optional[Union[float, bool]] = ..., prs: Optional[Union[float, bool]] = ..., radius: Optional[Union[float, bool]] = ..., r: Optional[Union[float, bool]] = ..., smudgeIsMiddle: bool = ..., sim: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context for smudge UV tool.  This
    context only works in the texture UV editor.

    Args:
        dragSlider | ds: (edit, query) - radius | none Enables the drag slider mode. This is to support brush resizing while holding the 'b' or 'B' button.
        effectType | et: (edit, query) - fixed | smudge Specifies the effect of the tool. In fixed mode, the UVs move as if they are attached by a rubber band. In smudge mode the UVs are moved as the cursor is dragged over the UVs.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        functionType | ft: (edit, query) - exponential | linear | constant. Specifies how UVs fall off from the center of influence.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        pressure | prs: (edit, query) - Pressure value when effect type is set to smudge.
        radius | r: (edit, query) - Radius of the smudge tool. All UVs within this radius are affected by the tool
        smudgeIsMiddle | sim: (edit, query) - By default, the left mouse button initiates the smudge. However, this conflicts with selection. When smudgeIsMiddle is on, smudge mode is activated by the middle mouse button instead of the left mouse button.
    """
    ...


def texturePlacementContext(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., labelMapping: bool = ..., lm: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create a command for creating new texture placement contexts. By
    default label mapping is on when the context is created.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        labelMapping | lm: (create, edit, query) - Set the context to label mapping.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def texTweakUVContext(*args, exists: bool = ..., ex: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., position: bool = ..., p: bool = ..., tolerance: Optional[Union[float, bool]] = ..., t: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create, edit, or query a texture editor
    move manip context.
    Note that the above flags control the global behaviour of all texture
    editor move manip contexts.  Changing one context independently is not
    allowed.  Changing a context's behaviour using the above flags, will
    change all existing texture editor move manip contexts.

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        position | p: (query) - Returns the current position of the manipulator
        tolerance | t: (create, edit, query) - Controls the initial selection snapping tolerance.
    """
    ...


def texWinToolCtx(*args, alternateContext: bool = ..., ac: bool = ..., boxzoom: bool = ..., bz: bool = ..., dolly: bool = ..., do: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., toolName: Optional[Union[str, bool]] = ..., tn: Optional[Union[str, bool]] = ..., track: bool = ..., tr: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This class creates a context for the View Tools "track", "dolly",
    and "box zoom" in the texture window.

    Args:
        alternateContext | ac: (create, query) - Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        boxzoom | bz: (create, edit, query) - Perform Box Zoom
        dolly | do: (create, edit, query) - Dollies the view
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        toolName | tn: (create, query) - Name of the specific tool to which this command refers.
        track | tr: (create, edit, query) - Tracks the view
    """
    ...


def threadCount(*args, numberOfThreads: Optional[Union[int, bool]] = ..., n: Optional[Union[int, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command sets the number of threads to be used by Maya in
    regions of code that are multithreaded. By default the number
    of threads is equal to the number of logical CPUs, not the
    number of physical CPUs. Logical CPUs are different from
    physical CPUs in the following ways:
    
    A physical CPU with hyperthreading counts as two logical CPUs
    A dual-core CPU counts as two logical CPUs
    
    With some workloads, using one thread per logical CPU may
    not perform well. This is sometimes the case with
    hyperthreading. It is worth experimenting with different
    numbers of threads to see which gives the best performance.
    Note that having more threads can mean Maya uses more memory.
    
    Setting a value of zero means the number of threads used will
    equal the number of logical processors in the system.

    Args:
        numberOfThreads | n: (create, query) - Sets the number of threads to use
    """
    ...


def threePointArcCtx(*args, degree: Optional[Union[int, bool]] = ..., d: Optional[Union[int, bool]] = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., spans: Optional[Union[int, bool]] = ..., s: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The threePointArcCtx command creates a new context for creating 3 point arcs

    Args:
        degree | d: (create, edit, query) - VAlid values are 1 or 3. Default degree 3.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        spans | s: (create, edit, query) - Default is 8.
    """
    ...


def timeCode(*args, mayaStartFrame: Optional[Union[float, bool]] = ..., msf: Optional[Union[float, bool]] = ..., productionStartFrame: Optional[Union[float, bool]] = ..., psf: Optional[Union[float, bool]] = ..., productionStartHour: Optional[Union[float, bool]] = ..., psh: Optional[Union[float, bool]] = ..., productionStartMinute: Optional[Union[float, bool]] = ..., psm: Optional[Union[float, bool]] = ..., productionStartSecond: Optional[Union[float, bool]] = ..., pss: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Use this command to query and set the time code information in the file

    Args:
        mayaStartFrame | msf: (create, edit, query) - Sets the Maya start time of the time code, in frames. In query mode, returns the Maya start frame of the time code.
        productionStartFrame | psf: (create, edit, query) - Sets the production start time of the time code, in terms of frames. In query mode, returns the sub-second frame of production start time.
        productionStartHour | psh: (create, edit, query) - Sets the production start time of the time code, in terms of hours. In query mode, returns the hour of production start time.
        productionStartMinute | psm: (create, edit, query) - Sets the production start time of the time code, in terms of minutes. In query mode, returns the minute of production start time.
        productionStartSecond | pss: (create, edit, query) - Sets the production start time of the time code, in terms of seconds. In query mode, returns the second of production start time.
    """
    ...


def toggle(*args, above: bool = ..., a: bool = ..., below: bool = ..., b: bool = ..., boundary: bool = ..., bn: bool = ..., boundingBox: bool = ..., box: bool = ..., controlVertex: bool = ..., cv: bool = ..., doNotWrite: bool = ..., dnw: bool = ..., editPoint: bool = ..., ep: bool = ..., extent: bool = ..., et: bool = ..., facet: bool = ..., f: bool = ..., geometry: bool = ..., g: bool = ..., gl: bool = ..., highPrecisionNurbs: bool = ..., hpn: bool = ..., hull: bool = ..., hl: bool = ..., latticePoint: bool = ..., lp: bool = ..., latticeShape: bool = ..., ls: bool = ..., localAxis: bool = ..., la: bool = ..., newCurve: bool = ..., nc: bool = ..., newPolymesh: bool = ..., np: bool = ..., newSurface: bool = ..., ns: bool = ..., normal: bool = ..., nr: bool = ..., origin: bool = ..., o: bool = ..., point: bool = ..., pt: bool = ..., pointDisplay: bool = ..., pd: bool = ..., pointFacet: bool = ..., pf: bool = ..., rotatePivot: bool = ..., rp: bool = ..., scalePivot: bool = ..., sp: bool = ..., selectHandle: bool = ..., sh: bool = ..., state: bool = ..., st: bool = ..., surfaceFace: bool = ..., sf: bool = ..., template: bool = ..., te: bool = ..., uvCoords: bool = ..., uv: bool = ..., vertex: bool = ..., vt: bool = ..., query: bool = ...) -> Any:
    r"""
    The toggle command is used to toggle the display of various
    object features for objects which have these components. For
    example, CV and edit point display may be toggled for those
    listed     NURB curves or surfaces.
    
    Note: This command is not undoable.

    Args:
        above | a: (create) - Toggle state for all objects above listed objects.
        below | b: (create) - Toggle state for all objects below listed objects.
        boundary | bn: (create, query) - Toggle boundary display of listed mesh objects.
        boundingBox | box: (create, query) - Toggle or query the bounding box display of listed objects.
        controlVertex | cv: (create, query) - Toggle CV display of listed curves and surfaces.
        doNotWrite | dnw: (create, query) - Toggle the "this should be written to the file" state.
        editPoint | ep: (create, query) - Toggle edit point display of listed curves and surfaces.
        extent | et: (create, query) - Toggle display of extents of listed mesh objects.
        facet | f: (create, query) - For use with normal flag. Set the normal display style to facet display.
        geometry | g: (create, query) - Toggle geometry display of listed objects.
        gl | gl: (create) - Toggle state for all objects
        highPrecisionNurbs | hpn: (create, query) - Toggle high precision display for Nurbs
        hull | hl: (create, query) - Toggle hull display of listed curves and surfaces.
        latticePoint | lp: (create, query) - Toggle point display of listed lattices
        latticeShape | ls: (create, query) - Toggle display of listed lattices
        localAxis | la: (create, query) - Toggle local axis display of listed objects.
        newCurve | nc: (create, query) - Set component display state of new curve objects
        newPolymesh | np: (create, query) - Set component display state of new polymesh objects
        newSurface | ns: (create, query) - Set component display state of new surface objects
        normal | nr: (create, query) - Toggle display of normals of listed surface and mesh objects.
        origin | o: (create, query) - Toggle origin display of listed surfaces.
        point | pt: (create, query) - For use with normal flag. Set the normal display style to vertex display.
        pointDisplay | pd: (create, query) - Toggle point display of listed surfaces.
        pointFacet | pf: (create, query) - For use with normal flag. Set the normal display style to vertex and face display.
        rotatePivot | rp: (create, query) - Toggle rotate pivot display of listed objects.
        scalePivot | sp: (create, query) - Toggle scale pivot display of listed objects.
        selectHandle | sh: (create, query) - Toggle select handle display of listed objects.
        state | st: (create) - Explicitly set the state to true or false instead of toggling the state. Can not be queried.
        surfaceFace | sf: (create, query) - Toggle surface face handle display of listed surfaces.
        template | te: (create, query) - Toggle template state of listed objects
        uvCoords | uv: (create, query) - Toggle display uv coords of listed mesh objects.
        vertex | vt: (create, query) - Toggle vertex display of listed mesh objects.
    """
    ...


def toggleAxis(*args, origin: bool = ..., o: bool = ..., view: bool = ..., v: bool = ..., query: bool = ...) -> Any:
    r"""
    Toggles the state of the display axis.
    
    Note: the display of the axis in the bottom left corner has
    been rendered obsolete by the headsUpDisplay command.

    Args:
        origin | o: (create, query) - Turns display of the axis at the origin of the ground plane on or off.
        view | v: (create, query) - Turns display of the axis at the bottom left of each view on or off. (Obsolete - refer to the headsUpDisplay command)
    """
    ...


def toggleDisplacement(*args) -> Any:
    r"""
    This command toggles the displacement preview of the polygon.
    This command is NOT un-doable.

    Args:
    """
    ...


def toolDropped(*args) -> Any:
    r"""
    This command builds and executes the commands necessary to recreate the
    specified tool button.  It is invoked when a tool is dropped on the shelf.

    Args:
    """
    ...


def toolHasOptions(*args) -> Any:
    r"""
    This command queries a tool to see if it has options. If it does,
    it returns true. Otherwise it returns false.

    Args:
    """
    ...


def toolPropertyWindow(*args, field: Optional[Union[str, bool]] = ..., fld: Optional[Union[str, bool]] = ..., helpButton: Optional[Union[str, bool]] = ..., hb: Optional[Union[str, bool]] = ..., icon: Optional[Union[str, bool]] = ..., icn: Optional[Union[str, bool]] = ..., inMainWindow: bool = ..., imw: bool = ..., location: Optional[Union[str, bool]] = ..., loc: Optional[Union[str, bool]] = ..., noviceMode: bool = ..., nm: bool = ..., resetButton: Optional[Union[str, bool]] = ..., rb: Optional[Union[str, bool]] = ..., restore: bool = ..., rs: bool = ..., selectCommand: Optional[Union[str, bool]] = ..., sel: Optional[Union[str, bool]] = ..., showCommand: Optional[Union[str, bool]] = ..., shw: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    End users should only call this command as 1. a query (in the
    custom tool property sheet code) or 2. with no arguments
    to create the default tool property sheet.  The more complex
    uses of it are internal.

    Args:
        field | fld: (edit, query) - Sets/returns the name of the text field used to store the tool name in the property sheet.
        helpButton | hb: (edit, query) - Sets/returns the name of the button used to show help on the tool in the property sheet.
        icon | icn: (edit, query) - Sets/returns the name of the static picture object (used to display the tool icon in the property sheet).
        inMainWindow | imw: (create) - Specify true if you want the tool settings to appear in the main window rather than a separate window.
        location | loc: (edit, query) - Sets/returns the location of the current tool property sheet, or an empty string if there is none.
        noviceMode | nm: (edit, query) - Sets/returns the 'novice mode' flag.(unused at the moment)
        resetButton | rb: (edit, query) - Sets/returns the name of the button used to restore the tool settings in the property sheet.
        restore | rs: (create) - Reopens the tool settings window. This flag can be used with the flag inMainWindow for the fall back location if the tool settings can't be restored.
        selectCommand | sel: (edit, query) - Sets/returns the property sheet's select command.
        showCommand | shw: (edit, query) - Sets/returns the property sheet's display command.
    """
    ...


def trackCtx(*args, alternateContext: bool = ..., ac: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., toolName: Optional[Union[str, bool]] = ..., tn: Optional[Union[str, bool]] = ..., trackGeometry: bool = ..., tg: bool = ..., trackScale: Optional[Union[float, bool]] = ..., ts: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create a track context.

    Args:
        alternateContext | ac: (create, query) - Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        toolName | tn: (create, query) - Name of the specific tool to which this command refers.
        trackGeometry | tg: (create, edit, query) - Toggle whether the drag should try to track geometry. The context will compute a track plane by intersecting the initial press with geometry or the live object.
        trackScale | ts: (create, edit, query) - Specify the distance to the track plane from the camera. The smaller the scale the slower the drag.
    """
    ...


def transformCompare(*args, root: bool = ..., r: bool = ...) -> Any:
    r"""
    Compares two transforms passed as arguments. If they are the same,
    returns 0. If they are different, returns 1. If no transforms are
    specified in the command line, then the transforms from the active
    list are used.

    Args:
        root | r: (create) - Compare the root only, rather than the entire hierarchy below the roots.
    """
    ...


def transformLimits(*args, enableRotationX: Optional[Union[Tuple[bool, bool], bool]] = ..., erx: Optional[Union[Tuple[bool, bool], bool]] = ..., enableRotationY: Optional[Union[Tuple[bool, bool], bool]] = ..., ery: Optional[Union[Tuple[bool, bool], bool]] = ..., enableRotationZ: Optional[Union[Tuple[bool, bool], bool]] = ..., erz: Optional[Union[Tuple[bool, bool], bool]] = ..., enableScaleX: Optional[Union[Tuple[bool, bool], bool]] = ..., esx: Optional[Union[Tuple[bool, bool], bool]] = ..., enableScaleY: Optional[Union[Tuple[bool, bool], bool]] = ..., esy: Optional[Union[Tuple[bool, bool], bool]] = ..., enableScaleZ: Optional[Union[Tuple[bool, bool], bool]] = ..., esz: Optional[Union[Tuple[bool, bool], bool]] = ..., enableTranslationX: Optional[Union[Tuple[bool, bool], bool]] = ..., etx: Optional[Union[Tuple[bool, bool], bool]] = ..., enableTranslationY: Optional[Union[Tuple[bool, bool], bool]] = ..., ety: Optional[Union[Tuple[bool, bool], bool]] = ..., enableTranslationZ: Optional[Union[Tuple[bool, bool], bool]] = ..., etz: Optional[Union[Tuple[bool, bool], bool]] = ..., remove: bool = ..., rm: bool = ..., rotationX: Optional[Union[Tuple[float, float], bool]] = ..., rx: Optional[Union[Tuple[float, float], bool]] = ..., rotationY: Optional[Union[Tuple[float, float], bool]] = ..., ry: Optional[Union[Tuple[float, float], bool]] = ..., rotationZ: Optional[Union[Tuple[float, float], bool]] = ..., rz: Optional[Union[Tuple[float, float], bool]] = ..., scaleX: Optional[Union[Tuple[float, float], bool]] = ..., sx: Optional[Union[Tuple[float, float], bool]] = ..., scaleY: Optional[Union[Tuple[float, float], bool]] = ..., sy: Optional[Union[Tuple[float, float], bool]] = ..., scaleZ: Optional[Union[Tuple[float, float], bool]] = ..., sz: Optional[Union[Tuple[float, float], bool]] = ..., translationX: Optional[Union[Tuple[float, float], bool]] = ..., tx: Optional[Union[Tuple[float, float], bool]] = ..., translationY: Optional[Union[Tuple[float, float], bool]] = ..., ty: Optional[Union[Tuple[float, float], bool]] = ..., translationZ: Optional[Union[Tuple[float, float], bool]] = ..., tz: Optional[Union[Tuple[float, float], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The transformLimits command allows us to set, edit, or query
    the limits of the transformation that can be applied to objects.
    
    We can also turn any limits off which may have been previously set.
    When an object is first created, all the transformation limits are off
    by default.
    
    Transformation limits allow us to control how much an object can
    be transformed. This is most useful for joints, although it can be
    used any place we would like to limit the movement of an object.
    
    Default values are:
    ( -1, 1) for translation,
    ( -1, 1) for scaling, and
    (-45,45) for rotation.

    Args:
        enableRotationX | erx: (query) - enable/disable the lower and upper x-rotation limits When queried, it returns boolean boolean
        enableRotationY | ery: (query) - enable/disable the lower and upper y-rotation limits When queried, it returns boolean boolean
        enableRotationZ | erz: (query) - enable/disable the lower and upper z-rotation limits When queried, it returns boolean boolean
        enableScaleX | esx: (query) - enable/disable the lower and upper x-scale limits When queried, it returns boolean boolean
        enableScaleY | esy: (query) - enable/disable the lower and upper y-scale limits When queried, it returns boolean boolean
        enableScaleZ | esz: (query) - enable/disable the lower and upper z-scale limits When queried, it returns boolean boolean
        enableTranslationX | etx: (query) - enable/disable the  ower and upper x-translation limits When queried, it returns boolean boolean
        enableTranslationY | ety: (query) - enable/disable the lower and upper y-translation limits When queried, it returns boolean boolean
        enableTranslationZ | etz: (query) - enable/disable the lower and upper z-translation limits When queried, it returns boolean boolean
        remove | rm: (create) - turn all the limits off and reset them to their default values
        rotationX | rx: (query) - set the lower and upper x-rotation limits When queried, it returns angle angle
        rotationY | ry: (query) - set the lower and upper y-rotation limits When queried, it returns angle angle
        rotationZ | rz: (query) - set the lower and upper z-rotation limits When queried, it returns angle angle
        scaleX | sx: (query) - set the lower and upper x-scale limits When queried, it returns float float
        scaleY | sy: (query) - set the lower and upper y-scale limits When queried, it returns float float
        scaleZ | sz: (query) - set the lower and upper z-scale limits When queried, it returns float float
        translationX | tx: (query) - set the lower and upper x-translation limits When queried, it returns linear linear
        translationY | ty: (query) - set the lower and upper y-translation limits When queried, it returns linear linear
        translationZ | tz: (query) - set the lower and upper z-translation limits When queried, it returns linear linear
    """
    ...


def tumbleCtx(*args, alternateContext: bool = ..., ac: bool = ..., autoOrthoConstrain: bool = ..., aoc: bool = ..., autoSetPivot: bool = ..., asp: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., localTumble: Optional[Union[int, bool]] = ..., lt: Optional[Union[int, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., objectTumble: bool = ..., ot: bool = ..., orthoLock: bool = ..., ol: bool = ..., orthoStep: Optional[Union[float, bool]] = ..., os: Optional[Union[float, bool]] = ..., toolName: Optional[Union[str, bool]] = ..., tn: Optional[Union[str, bool]] = ..., tumbleScale: Optional[Union[float, bool]] = ..., ts: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create, edit, or query a tumble
    context.

    Args:
        alternateContext | ac: (create, query) - Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        autoOrthoConstrain | aoc: (create, edit, query) - Automatically constrain horizontal and vertical rotations when the camera is orthographic. The shift key can be used to unconstrain the rotation.
        autoSetPivot | asp: (create, edit, query) - Automatically set the camera pivot to the selection or tool effect region
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        localTumble | lt: (create, edit, query) - Describes what point the camera will tumble around:  0 for the camera's tumble pivot 1 for the camera's center of interest 2 for the camera's local axis, offset by its tumble pivot
        name | n: (create) - If this is a tool command, name the tool appropriately.
        objectTumble | ot: (create, edit, query) - Make the camera tumble around the selected object, if true.
        orthoLock | ol: (create, edit, query) - Orthographic cameras cannot be tumbled while orthoLock is on.
        orthoStep | os: (create, edit, query) - Specify the angular step in degrees for orthographic rotation. If camera is orthographic and autoOrthoConstrain is toggled on the rotation will be stepped by this amount.
        toolName | tn: (create, query) - Name of the specific tool to which this command refers.
        tumbleScale | ts: (create, edit, query) - Set the rotation speed. A tumble scale of 1.0 will result in in 40 degrees of rotation per 100 pixels of cursor drag.
    """
    ...


def twoPointArcCtx(*args, degree: Optional[Union[int, bool]] = ..., d: Optional[Union[int, bool]] = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., spans: Optional[Union[int, bool]] = ..., s: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The twoPointArcCtx command creates a new context for creating two point circular arcs

    Args:
        degree | d: (create, edit, query) - Valid values are 1 or 3. Default degree 3.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        spans | s: (create, edit, query) - Default is 4.
    """
    ...


def ungroup(*args, absolute: bool = ..., a: bool = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., relative: bool = ..., r: bool = ..., world: bool = ..., w: bool = ...) -> Any:
    r"""
    This command ungroups the specified objects.
    
    The objects will be placed at the same level in the hierarchy the
    group node occupied unless the -w flag is specified, in which case
    they will be placed under the world.
    
    If an object is ungrouped and there is an object in the new group
    with the same name then this command will rename the ungrouped
    object.
    
    See also: group, parent, instance, duplicate

    Args:
        absolute | a: (create) - preserve existing world object transformations (overall object transformation is preserved by modifying the objects local transformation) [default]
        parent | p: (create) - put the ungrouped objects under the given parent
        relative | r: (create) - preserve existing local object transformations (don't modify local transformation)
        world | w: (create) - put the ungrouped objects under the world
    """
    ...


def upAxis(*args, axis: Optional[Union[str, bool]] = ..., ax: Optional[Union[str, bool]] = ..., rotateView: bool = ..., rv: bool = ..., query: bool = ...) -> Any:
    r"""
    The upAxis command changes the world up direction.
    Current implementation provides only two choices of axis (the Y-axis
    or the Z-axis) as the world up direction.
    
    By default, the ground plane in Maya is on the XY plane.
    Hence, the default up-direction is the direction of the positive Z-axis.
    
    The -ax flag is mandatory. In conjunction with the -ax flag,
    when the -rv flag is specified, the camera of currently active view is
    revolved about the X-axis such that the position of the groundplane in
    the view will remain the same as before the the up direction is changed.
    
    The screen update is applied to all cameras of all views.

    Args:
        axis | ax: (query) - This flag specifies the axis as the world up direction. The valid axis are either "y" or "z". When queried, it returns a string.
        rotateView | rv: (create) - This flag specifies to rotate the view as well.
    """
    ...


def view2dToolCtx(*args, alternateContext: bool = ..., ac: bool = ..., boxzoom: bool = ..., bz: bool = ..., dolly: bool = ..., do: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., toolName: Optional[Union[str, bool]] = ..., tn: Optional[Union[str, bool]] = ..., track: bool = ..., tr: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This class creates a context for the View Tools "track", "dolly",
    and "box zoom" in the Hypergraph.

    Args:
        alternateContext | ac: (create, query) - Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        boxzoom | bz: (create, query) - Perform Box Zoom
        dolly | do: (create, query) - Dollies the view
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        toolName | tn: (create, query) - Name of the specific tool to which this command refers.
        track | tr: (create, query) - Tracks the view
    """
    ...


def walkCtx(*args, alternateContext: bool = ..., ac: bool = ..., crouchCount: Optional[Union[float, bool]] = ..., wcc: Optional[Union[float, bool]] = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., toolName: Optional[Union[str, bool]] = ..., tn: Optional[Union[str, bool]] = ..., walkHeight: Optional[Union[float, bool]] = ..., wh: Optional[Union[float, bool]] = ..., walkSensitivity: Optional[Union[float, bool]] = ..., wsv: Optional[Union[float, bool]] = ..., walkSpeed: Optional[Union[float, bool]] = ..., ws: Optional[Union[float, bool]] = ..., walkToolHud: bool = ..., wth: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create, edit, or query a walk
    context.

    Args:
        alternateContext | ac: (create, query) - Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        crouchCount | wcc: (create, edit, query) - The camera crouch count.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        toolName | tn: (create, query) - Name of the specific tool to which this command refers.
        walkHeight | wh: (create, edit, query) - The camera initial height.
        walkSensitivity | wsv: (create, edit, query) - The camera rotate sensitivity.
        walkSpeed | ws: (create, edit, query) - The camera move speed.
        walkToolHud | wth: (create, edit, query) - Control whether show walk tool HUD.
    """
    ...


def weightsColor(*args, colorRamp: Optional[Union[str, bool]] = ..., cr: Optional[Union[str, bool]] = ..., deformer: Optional[Union[str, bool]] = ..., dfm: Optional[Union[str, bool]] = ..., falseColor: bool = ..., fc: bool = ..., outOfRangeColor: Optional[Union[Tuple[float, float, float], bool]] = ..., orc: Optional[Union[Tuple[float, float, float], bool]] = ..., rampMaxColor: Optional[Union[Tuple[float, float, float], bool]] = ..., rxc: Optional[Union[Tuple[float, float, float], bool]] = ..., rampMinColor: Optional[Union[Tuple[float, float, float], bool]] = ..., rmc: Optional[Union[Tuple[float, float, float], bool]] = ..., useColorRamp: bool = ..., ucr: bool = ..., useMaxMinColor: bool = ..., umc: bool = ..., query: bool = ...) -> Any:
    r"""
    Controls the coloring of deformer weights.

    Args:
        colorRamp | cr: (query) - Allows a user defined color ramp to be used to map values to colors.
        deformer | dfm: (query) - Specify the deformer that needs to be visualized.
        falseColor | fc: (query) - Enable or disable false color display on the geometry.
        outOfRangeColor | orc: (query) - Defines a special color to be used for the areas outside the deformers subset.
        rampMaxColor | rxc: (query) - Defines a special color to be used when the value is greater than or equal to the maximum value.
        rampMinColor | rmc: (query) - Defines a special color to be used when the value is less than or equal to the minimum value.
        useColorRamp | ucr: (query) - Specifies whether the user defined color ramp should be used to map values from to colors. If this is turned off, the default greyscale feedback will be used.
        useMaxMinColor | umc: (query) - Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
    """
    ...


def wireContext(*args, crossingEffect: Optional[Union[float, bool]] = ..., ce: Optional[Union[float, bool]] = ..., deformationOrder: Optional[Union[str, bool]] = ..., do: Optional[Union[str, bool]] = ..., dropoffDistance: Optional[Union[float, bool]] = ..., dds: Optional[Union[float, bool]] = ..., envelope: Optional[Union[float, bool]] = ..., en: Optional[Union[float, bool]] = ..., exclusive: bool = ..., exc: bool = ..., exclusivePartition: Optional[Union[str, bool]] = ..., ep: Optional[Union[str, bool]] = ..., exists: bool = ..., ex: bool = ..., groupWithBase: bool = ..., gw: bool = ..., history: bool = ..., ch: bool = ..., holder: bool = ..., ho: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., localInfluence: Optional[Union[float, bool]] = ..., li: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a tool that can be used to
    create a wire deformer.

    Args:
        crossingEffect | ce: (create, edit, query) - Set the amount of convolution filter effect. Varies from fully convolved at 0 to a simple additive effect at 1. Default is 0.
        deformationOrder | do: (create, edit, query) - Set the appropriate flag that determines the position in in the deformation hierarchy.
        dropoffDistance | dds: (create, edit, query) - Set the dropoff Distance for the wires.
        envelope | en: (create, edit, query) - Set the envelope value for the deformer. Default is 1.0
        exclusive | exc: (create, edit, query) - Set exclusive mode on or off.
        exclusivePartition | ep: (create, edit, query) - Set the name of an exclusive partition.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        groupWithBase | gw: (create, edit, query) - Groups the wire with the base wire so that they can easily be moved together to create a ripple effect. Default is false.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        holder | ho: (create, edit) - Controls whether the user can specify holders for the wires from the wire context. A holder is a curve that you can use to limit the wire's deformation region. Default is false.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        localInfluence | li: (create, edit, query) - Set the amount of local influence a wire has with respect to other wires. Default is 0.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def wrinkleContext(*args, branchCount: Optional[Union[int, bool]] = ..., brc: Optional[Union[int, bool]] = ..., branchDepth: Optional[Union[int, bool]] = ..., bd: Optional[Union[int, bool]] = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., randomness: Optional[Union[float, bool]] = ..., rnd: Optional[Union[float, bool]] = ..., style: Optional[Union[str, bool]] = ..., st: Optional[Union[str, bool]] = ..., thickness: Optional[Union[float, bool]] = ..., th: Optional[Union[float, bool]] = ..., wrinkleCount: Optional[Union[int, bool]] = ..., wc: Optional[Union[int, bool]] = ..., wrinkleIntensity: Optional[Union[float, bool]] = ..., wi: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a context that creates wrinkles.

    Args:
        branchCount | brc: (create, edit, query) - Set the number of branches spawned from a crease for radial wrinkles. Default is 2.
        branchDepth | bd: (create, edit, query) - Set the depth of branching for radial wrinkles. Defaults to 0.
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
        randomness | rnd: (create, edit, query) - Set the deviation of the wrinkle creases from straight lines and other elements of the wrinkle structure. Defaults to 0.2.
        style | st: (create, edit, query) - Set the wrinkle characteristic shape."lines"|"radial"|"custom. Default is "radial".
        thickness | th: (create, edit, query) - Set the thickness of wrinkle creases by setting the dropoff distance on the underlying wires.
        wrinkleCount | wc: (create, edit, query) - Set the number of wrinkle creases. Default is 3.
        wrinkleIntensity | wi: (create, edit, query) - Set the depth intensity of the wrinkle furrows. Defaults to 0.5.
    """
    ...


def xform(*args, absolute: bool = ..., a: bool = ..., boundingBox: bool = ..., bb: bool = ..., boundingBoxInvisible: bool = ..., bbi: bool = ..., centerPivots: bool = ..., cp: bool = ..., centerPivotsOnComponents: bool = ..., cpc: bool = ..., deletePriorHistory: bool = ..., dph: bool = ..., euler: bool = ..., eu: bool = ..., matrix: Optional[Union[Tuple[float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float], bool]] = ..., m: Optional[Union[Tuple[float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float], bool]] = ..., objectSpace: bool = ..., os: bool = ..., pivots: Optional[Union[Tuple[float, float, float], bool]] = ..., piv: Optional[Union[Tuple[float, float, float], bool]] = ..., preserve: bool = ..., p: bool = ..., preserveUV: bool = ..., puv: bool = ..., reflection: bool = ..., rfl: bool = ..., reflectionAboutBBox: bool = ..., rab: bool = ..., reflectionAboutOrigin: bool = ..., rao: bool = ..., reflectionAboutX: bool = ..., rax: bool = ..., reflectionAboutY: bool = ..., ray: bool = ..., reflectionAboutZ: bool = ..., raz: bool = ..., reflectionTolerance: Optional[Union[float, bool]] = ..., rft: Optional[Union[float, bool]] = ..., relative: bool = ..., r: bool = ..., rotateAxis: Optional[Union[Tuple[float, float, float], bool]] = ..., ra: Optional[Union[Tuple[float, float, float], bool]] = ..., rotateOrder: Optional[Union[str, bool]] = ..., roo: Optional[Union[str, bool]] = ..., rotatePivot: Optional[Union[Tuple[float, float, float], bool]] = ..., rp: Optional[Union[Tuple[float, float, float], bool]] = ..., rotateTranslation: Optional[Union[Tuple[float, float, float], bool]] = ..., rt: Optional[Union[Tuple[float, float, float], bool]] = ..., rotation: Optional[Union[Tuple[float, float, float], bool]] = ..., ro: Optional[Union[Tuple[float, float, float], bool]] = ..., scale: Optional[Union[Tuple[float, float, float], bool]] = ..., s: Optional[Union[Tuple[float, float, float], bool]] = ..., scalePivot: Optional[Union[Tuple[float, float, float], bool]] = ..., sp: Optional[Union[Tuple[float, float, float], bool]] = ..., scaleTranslation: Optional[Union[Tuple[float, float, float], bool]] = ..., st: Optional[Union[Tuple[float, float, float], bool]] = ..., shear: Optional[Union[Tuple[float, float, float], bool]] = ..., sh: Optional[Union[Tuple[float, float, float], bool]] = ..., translation: Optional[Union[Tuple[float, float, float], bool]] = ..., t: Optional[Union[Tuple[float, float, float], bool]] = ..., worldSpace: bool = ..., ws: bool = ..., worldSpaceDistance: bool = ..., wd: bool = ..., zeroTransformPivots: bool = ..., ztp: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used query/set any element in a
    transformation node. It can also be used to query some values
    that cannot be set directly such as the transformation matrix
    or the bounding box. It can also set both pivot points to
    convenient values.
    
    All values are specified in transformation coordinates.
    (attribute-space)
    
    In addition, the attributes are applied/returned in the order in
    which they appear in the flags section. (which corresponds to the
    order they appear in the transformation matrix as given below)
    
    See also: move, rotate, scale
    
    Notes
    The transformation matrix for a node is built by post-multiplying
    the following matrices in the given order (Note: rotations are
    applied according to the rotation order parameter and the 6
    different rotation possibilities are not shown below)
    
    -1                       -1
    [M]  = [sp]x[s]x[sh]x[sp]x[st]x[rp]x[ar]x[ro]x[rp]x[rt]x[t]
    
    where:
    
    [sp] = |  1      0        0       0 | = scale pivot matrix
    |  0      1        0       0 |
    |  0      0        1       0 |
    | -spx   -spy     -spz     1 |
    
    
    [s]  = |  sx     0        0       0 | = scale matrix
    |  0      sy       0       0 |
    |  0      0        sz      0 |
    |  0      0        0       1 |
    
    
    [sh] = |  1      0        0       0 | = shear matrix
    |  xy     1        0       0 |
    |  xz     yz       1       0 |
    |  0      0        0       1 |
    
    -1
    [sp] = |  1       0       0       0 | = scale pivot inverse matrix
    |  0       1       0       0 |
    |  0       0       1       0 |
    |  spx     spy     spz     1 |
    
    
    [st] = |  1       0       0       0 | = scale translate matrix
    |  0       1       0       0 |
    |  0       0       1       0 |
    |  stx     sty     stz     1 |
    
    
    [rp] = |  1       0       0       0 | = rotate pivot matrix
    |  0       1       0       0 |
    |  0       0       1       0 |
    | -rpx    -rpy    -rpz     1 |
    
    
    [ar] = |  *       *       *       0 | = axis rotation matrix
    |  *       *       *       0 |   (composite rotation,
    |  *       *       *       0 |    see [rx], [ry], [rz]
    |  0       0       0       1 |    below for details)
    
    
    [rx] = |  1       0       0       0 | = rotate X matrix
    |  0       cos(x)  sin(x)  0 |
    |  0      -sin(x)  cos(x)  0 |
    |  0       0       0       1 |
    
    
    [ry] = |  cos(y)  0      -sin(y)  0 | = rotate Y matrix
    |  0       1       0       0 |
    |  sin(y)  0       cos(y)  0 |
    |  0       0       0       1 |
    
    
    [rz] = |  cos(z)  sin(z)  0       0 | = rotate Z matrix
    | -sin(z)  cos(z)  0       0 |
    |  0       0       1       0 |
    |  0       0       0       1 |
    
    -1
    [rp] = |  1       0       0       0 | = rotate pivot matrix
    |  0       1       0       0 |
    |  0       0       1       0 |
    |  rpx     rpy     rpz     1 |
    
    
    [rt] = |  1       0       0       0 | = rotate translate matrix
    |  0       1       0       0 |
    |  0       0       1       0 |
    |  rtx     rty     rtz     1 |
    
    
    [t]  = |  1       0       0       0 | = translation matrix
    |  0       1       0       0 |
    |  0       0       1       0 |
    |  tx      ty      tz      1 |

    Args:
        absolute | a: (create) - perform absolute transformation (default)
        boundingBox | bb: (query) - Returns the bounding box of an object. The values returned are in the following order: xmin ymin zmin xmax ymax zmax.
        boundingBoxInvisible | bbi: (query) - Returns the bounding box of an object. This includes the bounding boxes of all invisible children which are not included using the boundingBox flag. The values returned are in following order: xmin ymin zmin xmax ymax zmax.
        centerPivots | cp: (create) - Set pivot points to the center of the object's bounding box. (see -p flag)
        centerPivotsOnComponents | cpc: (create) - Set pivot points to the center of the component's bounding box. (see -p flag)
        deletePriorHistory | dph: (create) - If true then delete the construction history before the operation is performed.
        euler | eu: (create) - modifer for -relative flag that specifies rotation values should be added to current XYZ rotation values.
        matrix | m: (create, query) - Sets/returns the composite transformation matrix. *Note* the matrix is represented by 16 double arguments that are specified in row order.
        objectSpace | os: (create, query) - treat values as object-space transformation values (only works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags)
        pivots | piv: (create, query) - convenience method that changes both the rotate and scale pivots simultaneously. (see -rp -sp flags for more info)
        preserve | p: (create) - preserve overall transformation. used to prevent object from "jumping" when changing pivots or rotation order. the default value is true. (used with -sp, -rp, -roo, -cp, -ra)
        preserveUV | puv: (create) - When true, UV values on rotated components are projected across the rotation in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected vertices. Default is false.
        reflection | rfl: (create) - To move the corresponding symmetric components also.
        reflectionAboutBBox | rab: (create) - Sets the position of the reflection axis  at the geometry bounding box
        reflectionAboutOrigin | rao: (create) - Sets the position of the reflection axis  at the origin
        reflectionAboutX | rax: (create) - Specifies the X=0 as reflection plane
        reflectionAboutY | ray: (create) - Specifies the Y=0 as reflection plane
        reflectionAboutZ | raz: (create) - Specifies the Z=0 as reflection plane
        reflectionTolerance | rft: (create) - Specifies the tolerance to findout the corresponding reflected components
        relative | r: (create) - perform relative transformation
        rotateAxis | ra: (create, query) - rotation axis orientation (when used with the -p flag the overall rotation is preserved by modifying the rotation to compensate for the axis rotation)
        rotateOrder | roo: (create, query) - rotation order (when used with the -p flag the overall rotation is preserved by modifying the local rotation to be quivalent to the old one) Valid values for this flag are <xyz | yzx | zxy | xzy | yxz | zyx>
        rotatePivot | rp: (create, query) - rotate pivot point transformation (when used with the -p flag the overall transformation is preserved by modifying the rotation translation)
        rotateTranslation | rt: (create, query) - rotation translation
        rotation | ro: (create, query) - rotation transformation
        scale | s: (create, query) - scale transformation
        scalePivot | sp: (create, query) - scale pivot point transformation (when used with the -p flag the overall transformation is preserved by modifying the scale translation)
        scaleTranslation | st: (create, query) - scale translation
        shear | sh: (create, query) - shear transformation. The values represent the shear <xy,xz,yz>
        translation | t: (create, query) - translation
        worldSpace | ws: (create, query) - (works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags). Note that, when querying the scale, that this calculation is cumulative and is only valid if there are all uniform scales and no rotation. In a hierarchy with non-uniform scale and rotation, this value may not correspond entirely with the perceived global scale.
        worldSpaceDistance | wd: (create, query) - Values for -sp, -rp, -st, -rt, -t, -piv flags are treated as world space distances to move along the local axis. (where the local axis depends on whether the command is operating in local-space or object-space. This flag has no effect for world space.
        zeroTransformPivots | ztp: (create) - reset pivot points and pivot translations without changing the overall matrix by applying these values into the translation channel.
    """
    ...


def xformConstraint(*args, alongNormal: Optional[Union[int, bool]] = ..., n: Optional[Union[int, bool]] = ..., live: bool = ..., l: bool = ..., type: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command allows you to change the transform constraint used by the
    transform tools during component transforms.

    Args:
        alongNormal | n: (edit, query) - When set the transform constraint will first be applied along the vertex normals of the components being transformed. When queried, returns the current state of this option.
        live | l: (query) - Query-only flag that can be used to check whether the current live surface will be used as a transform constraint.
        type | t: (create, edit, query) - Set the type of transform constraint to use. When queried, returns the current transform constraint as a string.  none - no constraint surface - constrain components to their surface edge - constrain components to surface edges
    """
    ...


