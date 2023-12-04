from typing import Union, Optional, List, Tuple, Any

def aaf2fcp(*args, deleteFile: bool = ..., df: bool = ..., dstPath: Optional[Union[str, bool]] = ..., dst: Optional[Union[str, bool]] = ..., getFileName: Optional[Union[int, bool]] = ..., gfn: Optional[Union[int, bool]] = ..., progress: Optional[Union[int, bool]] = ..., pr: Optional[Union[int, bool]] = ..., srcFile: Optional[Union[str, bool]] = ..., src: Optional[Union[str, bool]] = ..., terminate: Optional[Union[int, bool]] = ..., t: Optional[Union[int, bool]] = ..., waitCompletion: Optional[Union[int, bool]] = ..., wc: Optional[Union[int, bool]] = ...) -> Any:
    r"""
    This command is used to convert an aff file to a Final Cut Pro (fcp) xml file
    The conversion process can take several seconds to complete and the command is meant
    to be run asynchronously

    Args:
        deleteFile | df: (create) - Delete temporary file. Can only be used with the terminate option
        dstPath | dst: (create) - Specifiy a destination path
        getFileName | gfn: (create) - Query output file name
        progress | pr: (create) - Request progress report
        srcFile | src: (create) - Specifiy a source file
        terminate | t: (create) - Complete the task
        waitCompletion | wc: (create) - Wait for the conversion process to complete
    """
    ...


def allNodeTypes(*args, includeAbstract: bool = ..., ia: bool = ...) -> Any:
    r"""
    This command returns a list containing the type names of every kind of
    creatable node registered with the system. Note that some node types are
    abstract and cannot be created. These will not show up on this list.
    (e.g. transform and polyShape both inherit from dagObject, but dagObject
     cannot be created directly so it will not appear on this list.)

    Args:
        includeAbstract | ia: (create) - Show every node type, even the abstract ones which cannot be created via the 'createNode' command. These will have the suffix "(abstract)" appended to them in the list.
    """
    ...


def assignInputDevice(*args, clutch: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., continuous: bool = ..., ct: bool = ..., device: Optional[Union[str, bool]] = ..., d: Optional[Union[str, bool]] = ..., immediate: bool = ..., im: bool = ..., multiple: bool = ..., m: bool = ..., query: bool = ...) -> Any:
    r"""
    This command associates a command string (i.e. a mel script)
    with the input device.  When the device moves or a button on
    the device is pressed, the command string is executed as if
    you typed it into the window.  If the command string contains
    the names of buttons or axes of the device, the current value
    of these buttons/axes are substituted in.  Buttons are reported
    as booleans and axes as doubles.
    
    This command is most useful for associating buttons on a device
    with commands.  For using a device to capture continous movements
    it is much more efficient to attach the device directly into
    the dependency graph.

    Args:
        clutch | c: (create) - specify a clutch button.  This button must be down for the command string to be executed. If no clutch is specified the command string is executed everytime the device state changes
        continuous | ct: (create) - if this flag is set the command string is continously (once for everytime the device changes state).  By default if a clutch button is specified the command string is only executed once when the button is pressed.
        device | d: (create) - specify which device to assign the command string.
        immediate | im: (create) - Immediately executes the command, without using the queue.
        multiple | m: (create) - if this flag is set the other command strings associated with this device are not deleted. By default, when a new command string is attached to the device, all other command strings are deleted.
    """
    ...


def attachDeviceAttr(*args, attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., axis: Optional[Union[str, bool]] = ..., ax: Optional[Union[str, bool]] = ..., camera: bool = ..., cam: bool = ..., cameraRotate: bool = ..., cr: bool = ..., cameraTranslate: bool = ..., ct: bool = ..., clutch: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., device: Optional[Union[str, bool]] = ..., d: Optional[Union[str, bool]] = ..., selection: bool = ..., sl: bool = ..., query: bool = ...) -> Any:
    r"""
    This command associates a device/axis pair with a node/attribute pair.
    When the device axis moves, the value of the attribute is set to the
    value of the axis. This value can be scaled and offset using
    the setAttrScale command.

    Args:
        attribute | at: (create, multiuse) - specify the attribute to attach to
        axis | ax: (create) - specify the axis to attach from.
        camera | cam: (create) - This flag attaches the device/axis to the current camera. The mapping between device axes and camera controls is uses a heuristic based on the device descripton. The interaction is a copy of the mouse camera navigation controls.
        cameraRotate | cr: (create) - This flag attaches the device/axis to the current cameras rotation controls.
        cameraTranslate | ct: (create) - This flag attaches the device/axis to the current cameras translate controls.
        clutch | c: (create) - specify a clutch button.  This button must be down for the command string to be executed. If no clutch is specified the command string is executed everytime the device state changes
        device | d: (create) - specify which device to assign the command string.
        selection | sl: (create) - This flag attaches to the nodes in the selection list. This is different from the default arguments of the command since changing the selection will change the attachments.
    """
    ...


def audioTrack(*args, insertTrack: Optional[Union[int, bool]] = ..., it: Optional[Union[int, bool]] = ..., lock: bool = ..., l: bool = ..., mute: bool = ..., m: bool = ..., numTracks: Optional[Union[int, bool]] = ..., nt: Optional[Union[int, bool]] = ..., removeEmptyTracks: bool = ..., ret: bool = ..., removeTrack: Optional[Union[int, bool]] = ..., rt: Optional[Union[int, bool]] = ..., solo: bool = ..., so: bool = ..., swapTracks: Optional[Union[Tuple[int, int], bool]] = ..., st: Optional[Union[Tuple[int, int], bool]] = ..., title: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ..., track: Optional[Union[int, bool]] = ..., tr: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used for inserting and removing tracks related to the audio clips displayed in the sequencer. It can also be used to modify the track state, for example, to lock or mute a track.

    Args:
        insertTrack | it: (create) - This flag is used to insert a new empty track at the track index specified. Indices are 1-based.
        lock | l: (create, edit, query) - This flag specifies whether all audio clips on the same track as the specified audio node are to be locked at their current location and track.
        mute | m: (create, edit, query) - This flag specifies whether all audio clips on the same track as the specified audio node are to be muted or not.
        numTracks | nt: (query) - To query the number of audio tracks
        removeEmptyTracks | ret: (create) - This flag is used to remove all tracks that have no clips.
        removeTrack | rt: (create) - This flag is used to remove the track with the specified index.  The track must have no clips on it before it can be removed.
        solo | so: (create, edit, query) - This flag specifies whether all audio clips on the same track as the specified audio node are to be soloed or not.
        swapTracks | st: (create) - This flag is used to swap the contents of two specified tracks. Indices are 1-based.
        title | t: (create, edit, query) - This flag specifies the title for the track.
        track | tr: (create, edit, query) - Specify the track on which to operate by using the track's trackNumber. 			In query mode, this flag needs a value.
    """
    ...


def autoSave(*args, destination: Optional[Union[int, bool]] = ..., dst: Optional[Union[int, bool]] = ..., destinationFolder: bool = ..., df: bool = ..., enable: bool = ..., en: bool = ..., folder: Optional[Union[str, bool]] = ..., fol: Optional[Union[str, bool]] = ..., interval: Optional[Union[float, bool]] = ..., int: Optional[Union[float, bool]] = ..., limitBackups: bool = ..., lim: bool = ..., maxBackups: Optional[Union[int, bool]] = ..., max: Optional[Union[int, bool]] = ..., perform: bool = ..., p: bool = ..., prompt: bool = ..., prm: bool = ..., query: bool = ...) -> Any:
    r"""
    Provides an interface to the auto-save mechanism.

    Args:
        destination | dst: (create, query) - Sets the option for where auto-save files go. 0 - auto-saves go into the workspace autosave folder 1 - auto-saves go into the named folder (set with the -folder flag) 2 - auto-saves go into a folder set by an environment variable (MAYA_AUTOSAVE_FOLDER)
        destinationFolder | df: (query) - Queries the actual destination folder for auto-saves, based on the current setting of the -destination flag, workspace rules and environment variables. Resolves environment variables etc. and makes any relative path absolute (resolved relative to the workspace root). The returned string will end with a trailing separator ('/').
        enable | en: (create, query) - Enables or disables auto-saves.
        folder | fol: (create, query) - Sets the folder for auto-saves used if the destination option is 1.
        interval | int: (create, query) - Sets the interval between auto-saves (in seconds). The default interval is 600 seconds (10 minutes).
        limitBackups | lim: (create, query) - Sets whether the number of auto-save files is limited.
        maxBackups | max: (create, query) - Sets the maximum number of auto-save files, if limiting is in effect.
        perform | p: (create) - Invokes the auto-save process.
        prompt | prm: (create, query) - Sets whether the auto-save prompts the user before auto-saving.
    """
    ...


def cacheFile(*args, appendFrame: bool = ..., apf: bool = ..., attachFile: bool = ..., af: bool = ..., cacheFileNode: Optional[Union[str, bool]] = ..., cfn: Optional[Union[str, bool]] = ..., cacheFormat: Optional[Union[str, bool]] = ..., cf: Optional[Union[str, bool]] = ..., cacheInfo: Optional[Union[str, bool]] = ..., ci: Optional[Union[str, bool]] = ..., cacheableAttrs: Optional[Union[str, bool]] = ..., cat: Optional[Union[str, bool]] = ..., cacheableNode: Optional[Union[str, bool]] = ..., cnd: Optional[Union[str, bool]] = ..., channelIndex: bool = ..., chi: bool = ..., channelName: Optional[Union[str, bool]] = ..., cnm: Optional[Union[str, bool]] = ..., convertPc2: bool = ..., pc2: bool = ..., createCacheNode: bool = ..., ccn: bool = ..., creationChannelName: Optional[Union[str, bool]] = ..., cch: Optional[Union[str, bool]] = ..., dataSize: bool = ..., dsz: bool = ..., deleteCachedFrame: bool = ..., dcf: bool = ..., descriptionFileName: bool = ..., dfn: bool = ..., directory: Optional[Union[str, bool]] = ..., dir: Optional[Union[str, bool]] = ..., doubleToFloat: bool = ..., dtf: bool = ..., endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., et: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., fileName: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., format: Optional[Union[str, bool]] = ..., fm: Optional[Union[str, bool]] = ..., geometry: bool = ..., gm: bool = ..., inAttr: Optional[Union[str, bool]] = ..., ia: Optional[Union[str, bool]] = ..., inTangent: Optional[Union[str, bool]] = ..., it: Optional[Union[str, bool]] = ..., interpEndTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., iet: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., interpStartTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., ist: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., noBackup: bool = ..., nb: bool = ..., outAttr: Optional[Union[str, bool]] = ..., oa: Optional[Union[str, bool]] = ..., outTangent: Optional[Union[str, bool]] = ..., ot: Optional[Union[str, bool]] = ..., pc2File: Optional[Union[str, bool]] = ..., pcf: Optional[Union[str, bool]] = ..., pointCount: bool = ..., pc: bool = ..., points: Optional[Union[str, bool]] = ..., pts: Optional[Union[str, bool]] = ..., pointsAndNormals: Optional[Union[str, bool]] = ..., pan: Optional[Union[str, bool]] = ..., prefix: bool = ..., p: bool = ..., refresh: bool = ..., r: bool = ..., replaceCachedFrame: bool = ..., rcf: bool = ..., replaceWithoutSimulating: bool = ..., rws: bool = ..., runupFrames: Optional[Union[int, bool]] = ..., rf: Optional[Union[int, bool]] = ..., sampleMultiplier: Optional[Union[int, bool]] = ..., spm: Optional[Union[int, bool]] = ..., simulationRate: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., smr: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., singleCache: bool = ..., sch: bool = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., st: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., staticCache: bool = ..., sc: bool = ..., worldSpace: bool = ..., ws: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Creates one or more cache files on disk to store attribute data for a span of
    frames. The caches can be created for points/normals on a geometry (using
    the pts/points or pan/pointsAndNormals flag), for vectorArray output data
    (using the oa/outAttr flag), or for additional node specific data (using the
    cnd/cacheableNode flag for those nodes that support it).
    
    When the ia/inAttr flag is used, connects a cacheFile node that
    associates the data file on disk with the attribute.
    
    Frames can be replaced/appended to an existing cache with the
    rcf/replaceCachedFrame and apf/appendFrame flag.  Replaced frames are never deleted.
    They are stored in the same directory as the original cache files with the
    name provided by the f/fileName flag. If no file name is provided,
    the cacheFile name is prefixed with "backup" followed by a unique number.
    
    Single file caches are backed up in their entirety. To revert to an older
    version, simply attach to this cache. One file per frame caches only backup
    the description file and the frames that were replaced. To recover these
    types of caches, the user must rename these files to the original name.

    Args:
        appendFrame | apf: (create) - Appends data to the cache for the times specified by the startTime and endTime flags. If no time is provided, appends the current time. Must be used in conjunction with the pts/points or cnd/cacheableNode flag. Any overwritten frames will not be deleted, but renamed as specified by the f/fileName flag.
        attachFile | af: (create) - Used to indicate that rather than creating a cache file, that an existing cache file on disk should be attached to an attribute in the scene. The inAttr flag is used to specify the attribute.
        cacheFileNode | cfn: (create, multiuse) - Specifies the name of the cache file node(s) we are appending/replacing to if more than one cache is attached to the specified geometries. 			In query mode, this flag needs a value.
        cacheFormat | cf: (create, query) - Cache file format, default is Maya's .mcx format, but others available via plugin
        cacheInfo | ci: (create, multiuse, query) - In create mode, used to specify a mel script returning a string array. When creating the cache, this mel script will be executed and the returned strings will be written to the .xml description file of the cache. In query mode, returns descriptive info stored in the cacheFile such as the user name, Maya scene name and maya version number.
        cacheableAttrs | cat: (query) - Returns the list of cacheable attributes defined on the accompanying cache node. This argument requires the use of the cacheableNode flag.
        cacheableNode | cnd: (create, multiuse) - Specifies the name of a cacheable node whose contents will be cached. A cacheable node is a node that is specially designed to work with the caching mechanism.  An example of a cacheable node is a nCloth node. 			In query mode, this flag needs a value.
        channelIndex | chi: (create, query) - A query-only flag which returns the channel index for the selected geometry for the cacheFile node specified using the cacheFileNode flag.
        channelName | cnm: (create, multiuse, query) - When attachFile is used, used to indicate the channel in the file that should be attached to inAttr.  If not specified, the first channel in the file is used. In query mode, allows user to query the channels associated with a description file.
        convertPc2 | pc2: (create) - Convert a PC2 file to the Maya cache format (true), or convert Maya cache to pc2 format (false)
        createCacheNode | ccn: (create) - Used to indicate that rather than creating a cache file, that a cacheFile node should be created related to an existing cache file on disk.
        creationChannelName | cch: (create, multiuse) - When creating a new cache, this multi-use flag specifies the channels to be cached. The names come from the cacheable channel names defined by the object being cached. If this flag is not used when creating a cache, then all cacheable channels are cached.
        dataSize | dsz: (query) - This is a query-only flag that returns the size of the data being cached per frame. This flag is to be used in conjunction with the cacheableNode, points, pointsAndNormals and outAttr flags.
        deleteCachedFrame | dcf: (create) - Deletes cached data for the times specified by the startTime/endTime flags. If no time is provided, deletes the current frame. Must be used in conjunction with the pts/points or cnd/cacheableNode flag. Deleted frames will not be removed from disk, but renamed as specified by the f/fileName flag.
        descriptionFileName | dfn: (query) - This is a query-only flag that returns the name of the description file for an existing cacheFile node. Or if no cacheFile node is specified, it returns the description file name that would be created based on the other flags specified.
        directory | dir: (create, query) - Specifies the directory where the cache files will be located. If the directory flag is not specified, the cache files will be placed in the project data directory.
        doubleToFloat | dtf: (create) - During cache creation, double data is stored in the file as floats.  This helps cut down file size.
        endTime | et: (create) - Specifies the end frame of the cache range.
        fileName | f: (create, query) - Specifies the base file name for the cache files. If more than one object is being cached and the format is OneFilePerFrame, each cache file will be prefixed with this base file name. In query mode, returns the files associated with the specified cacheFile node. When used with rpf/replaceCachedFrame or apf/appendFrame specifies the name of the backup files. If not specified, replaced frames will be stored with a default name. 			In query mode, this flag can accept a value.
        format | fm: (create) - Specifies the distribution format of the cache.  Valid values are "OneFile" and "OneFilePerFrame"
        geometry | gm: (query) - A query flag which returns the geometry controlled by the specified cache node
        inAttr | ia: (create, multiuse) - Specifies the name of the attribute that the cache file will drive. This file is optional when creating cache files. If this flag is not used during create mode, the cache files will be created on disk, but will not be driving anything in the scene. This flag is required when the attachFile flag is used.
        inTangent | it: (create) - Specifies the in-tangent type when interpolating frames before the replaced frame(s). Must be used with the ist/interpStartTime and iet/interpEndTime flags. Valid values are "linear", "smooth" and "step".
        interpEndTime | iet: (create) - Specifies the frame until which there will be linear interpolation, beginning at endTime. Must be used with the rpf/replaceCachedFrame or apf/appendFrame flag. Interpolation is achieved by removing frames between endTime and interpEndTime from the cache. Removed frames will be renamed as specified by the f/fileName flag.
        interpStartTime | ist: (create) - Specifies the frame from which to begin linear interpolation, ending at startTime. Must be used with the rpf/replaceCachedFrame or apf/appendFrame flags. Interpolation is achieved by removing  frames between interpStartTime and startTime from the cache. These removed frames will will be renamed as specified by the f/fileName flag.
        noBackup | nb: (create) - Specifies that backup files should not be created for any files that may be over-written during append, replace or delete cache frames. Can only be used with the apf/appendFrame, rpf/replaceCachedFrame or dcf/deleteCachedFrame flags.
        outAttr | oa: (create, multiuse) - Specifies the name of the attribute that will be cached to disk. 			In query mode, this flag needs a value.
        outTangent | ot: (create) - Specifies the out-tangent type when interpolating frames after the replaced frame(s). Must be used with the ist/interpStartTime and iet/interpEndTime flags. Valid values are "linear", "smooth" and "step".
        pc2File | pcf: (create) - Specifies the full path to the pc2 file.  Must be used in conjunction with the pc2 flag.
        pointCount | pc: (query) - A query flag which returns the number of points stored in the cache file. The channelName flag should be used to specify the channel to be queried.
        points | pts: (create, multiuse) - Specifies the name of a geometry whose points will be cached. 			In query mode, this flag needs a value.
        pointsAndNormals | pan: (create, multiuse) - Specifies the name of a geometry whose points and normals will be cached. The normals is per-vertex per-polygon. The normals cache cannot be imported back to geometry. This flag can only be used to export cache file. It cannot be used with the apf/appendFrame, dcf/deleteCachedFrame and rpf/replaceCachedFrame flags. 			In query mode, this flag needs a value.
        prefix | p: (create) - Indicates that the specified fileName should be used as a prefix for the cacheName.
        refresh | r: (create) - When used during cache creation, forces a screen refresh during caching. This causes the cache creation to be slower but allows you to see how the simulation is progressing during the cache.
        replaceCachedFrame | rcf: (create) - Replaces cached data for the times specified by the startTime/endTime flags. If no time is provided, replaces cache file for the current time. Must be used in conjunction with the pts/points or cnd/cacheableNode flag. Replaced frames will not be deleted, but renamed as specified by the f/fileName flag.
        replaceWithoutSimulating | rws: (edit) - When replacing cached frames, this flag specifies whether the replacement should come from the cached node without simulating or from advancing time and letting the simulation run.  This flag is valid only when neither the startTime nor endTime flags are used or when both the startTime and endTime flags specify the same time value.
        runupFrames | rf: (create, edit, query) - Specifies the number of frames of runup to simulate ahead of the starting frame. The value must be greater than or equal to 0.  The default is 2.
        sampleMultiplier | spm: (create, edit, query) - Specifies the sample rate when caches are being created as a multiple of simulation Rate. If the value is 1, then a sample will be cached everytime the time is advanced.  If the value is 2, then every other sample will be cached, and so on.  The default is 1.
        simulationRate | smr: (create, edit, query) - Specifies the simulation rate when caches are being created.  During cache creation, the time will be advanced by the simulation rate, until the end time of the cache is reached or surpassed.  The value is given in frames. The default value is 1 frame.
        singleCache | sch: (create) - When used in conjunction with the points, pointsAndNormal or cacheableNode flag, specifies whether multiple geometries should be put into a single cache or to create one cache per geometry (default).
        startTime | st: (create) - Specifies the start frame of the cache range.
        staticCache | sc: (create, query) - If false, during cache creation, do not save a cache for the object if it appears to have no animation or deformation. If true, save a cache even if the object appears to have no animation or deformation. Default is true. In query mode, when supplied a shape, the flag returns true if the shape appears to have no animation or deformation.
        worldSpace | ws: (create) - If the points flag is used, turning on this flag will result in the world space positions of the points being written. The expected use of this flag is for cache export.
    """
    ...


def cacheFileCombine(*args, cacheIndex: bool = ..., ci: bool = ..., channelName: str = ..., cnm: str = ..., connectCache: Optional[Union[str, bool]] = ..., cc: Optional[Union[str, bool]] = ..., keepWeights: bool = ..., kw: bool = ..., layerNode: bool = ..., ln: bool = ..., nextAvailable: bool = ..., na: bool = ..., object: Optional[Union[str, bool]] = ..., obj: Optional[Union[str, bool]] = ..., objectIndex: Optional[Union[int, bool]] = ..., oi: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Creates a cacheBlend node that can be used to combine, layer or blend multiple cacheFiles for a given object.

    Args:
        cacheIndex | ci: (query) - A query only flag that returns the index related to the cache specified with the connectCache flag.
        channelName | cnm: (edit, multiuse) - Used in conjunction with the connectCache flag to indicate the channel(s) that should be connected.  If not specified, the first channel in the file is used.
        connectCache | cc: (edit, query) - An edit flag that specifies a cacheFile node that should be connected to the next available index on the specified cacheBlend node. As a query flag, it returns a string array containing the cacheFiles that feed into the specified cacheBlend node. 			In query mode, this flag can accept a value.
        keepWeights | kw: (edit) - This is a flag for use in combination with the connectCache flag only. By default, the connectCache flag will set all weights other than the newly added cacheWeight to 0 so that the new cache gets complete control. This flag disables that behavior so that all existing blend weights are retained.
        layerNode | ln: (query) - A query flag that returns a string array of the existing cacheBlends on the selected object(s). Returns an empty string array if no cacheBlends are found.
        nextAvailable | na: (query) - A query flag that returns the next available index on the selected cacheBlend node.
        object | obj: (query) - This flag is used in combination with the objectIndex flag. It is used to specify the object whose index you wish to query. 			In query mode, this flag needs a value.
        objectIndex | oi: (edit, query) - In edit mode, used in conjunction with the connectCache flag to indicate the objectIndex to be connected. In query mode, returns the index related to the object specified with the object flag.
    """
    ...


def cacheFileMerge(*args, endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., et: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., geometry: bool = ..., g: bool = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., st: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    If selected/specified caches can be successfully merged, will return the start/end frames of the new cache followed by the
    start/end frames of any gaps in the merged cache for which no data should be written to file. In query mode, will return
    the names of geometry associated with the specified cache file nodes.

    Args:
        endTime | et: (create) - Specifies the end frame of the merge range. If not specified, will figure out range from times of caches being merged.
        geometry | g: (query) - Query-only flag used to find the geometry nodes associated with the specified cache files.
        startTime | st: (create) - Specifies the start frame of the merge range. If not specified, will figure out range from the times of the caches being merged.
    """
    ...


def cacheFileTrack(*args, insertTrack: Optional[Union[int, bool]] = ..., it: Optional[Union[int, bool]] = ..., lock: bool = ..., l: bool = ..., mute: bool = ..., m: bool = ..., removeEmptyTracks: bool = ..., ret: bool = ..., removeTrack: Optional[Union[int, bool]] = ..., rt: Optional[Union[int, bool]] = ..., solo: bool = ..., so: bool = ..., track: Optional[Union[int, bool]] = ..., t: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used for inserting and removing tracks related to the caches displayed in the trax editor. It can also be used to modify the track state, for example, to lock or mute a track.

    Args:
        insertTrack | it: (create) - This flag is used to insert a new empty track at the track index specified.
        lock | l: (create, edit, query) - This flag specifies whether clips on a track are to be locked or not.
        mute | m: (create, edit, query) - This flag specifies whether clips on a track are to be muted or not.
        removeEmptyTracks | ret: (create) - This flag is used to remove all tracks that have no clips.
        removeTrack | rt: (create) - This flag is used to remove the track with the specified index.  The track must have no clips on it before it can be removed.
        solo | so: (create, edit, query) - This flag specifies whether clips on a track are to be soloed or not.
        track | t: (create, edit, query) - Used to specify a new track index for a cache to be displayed. Track-indices are 1-based.
    """
    ...


def clearCache(*args, allNodes: bool = ..., all: bool = ..., computed: bool = ..., c: bool = ..., dirty: bool = ..., d: bool = ...) -> Any:
    r"""
    Even though dependency graph values are computed or dirty they may still
    occupy space temporarily within the nodes.  This command goes in to all of
    the data that can be regenerated if required and removes it from the caches (datablocks), thus clearing up space in memory.

    Args:
        allNodes | all: (create) - If toggled then all nodes in the graph are cleared.  Otherwise only those nodes that are selected are cleared.
        computed | c: (create) - If toggled then remove all data that is computable.  (Warning: If the data is requested for redraw then the recompute will immediately fill the data back in.)
        dirty | d: (create) - If toggled then remove all heavy data that is dirty.
    """
    ...


def cmdFileOutput(*args, close: Optional[Union[int, bool]] = ..., c: Optional[Union[int, bool]] = ..., closeAll: bool = ..., ca: bool = ..., open: Optional[Union[str, bool]] = ..., o: Optional[Union[str, bool]] = ..., status: Optional[Union[int, bool]] = ..., s: Optional[Union[int, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command will open a text file to receive all of the commands
    and results that normally get printed to the Script Editor
    window or console. The file will stay open until an explicit -close
    with the correct file descriptor or a -closeAll, so care should be
    taken not to leave a file open.
    
    To enable logging to commence as soon as Maya starts up, the
    environment variable MAYA_CMD_FILE_OUTPUT may be specified prior
    to launching Maya. Setting MAYA_CMD_FILE_OUTPUT to a filename
    will create and output to that given file. To access the descriptor
    after Maya has started, use the -query and -open flags together.

    Args:
        close | c: (create) - Closes the file corresponding to the given descriptor. If -3 is returned, the file did not exist. -1 is returned on error, 0 is returned on successful close.
        closeAll | ca: (create) - Closes all open files.
        open | o: (create, query) - Opens the given file for writing (will overwrite if it exists and is writable). If successful, a value is returned to enable status queries and file close. -1 is returned if the file cannot be opened for writing. The -open flag can also be specified in -query mode. In query mode, if the named file is currently opened, the descriptor for the specified file is returned, otherwise -1 is returned. This is an easy way to check if a given file is currently open.       In query mode, this flag needs a value.
        status | s: (create, query) - Queries the status of the given descriptor. -3 is returned if no such file exists, -2 indicates the file is not open, -1 indicates an error condition, 0 indicates file is ready for writing.
    """
    ...


def convertUnit(*args, fromUnit: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., toUnit: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This command converts values between different units of measure.  The
    command takes a string, because a string can incorporate unit
    names as well as values (see examples).

    Args:
        fromUnit | f: (create) - The unit to convert from.  If not supplied, it is assumed to be the system default.  The from unit may also be supplied as part of the value e.g. 11.2m (11.2 meters).
        toUnit | t: (create) - The unit to convert to.  If not supplied, it is assumed to be the system default
    """
    ...


def crashInfo(*args, crashFile: bool = ..., cf: bool = ..., crashLog: bool = ..., cl: bool = ..., savedBeforeCrash: bool = ..., sbc: bool = ..., query: bool = ...) -> Any:
    r"""
    Provides an interface to the crash file information.

    Args:
        crashFile | cf: (query) - Return the crash file full path name.
        crashLog | cl: (query) - Return the crash log full path name.
        savedBeforeCrash | sbc: (query) - Return the saved file full path name before crash.
    """
    ...


def dagObjectCompare(*args, attribute: bool = ..., a: bool = ..., bail: Optional[Union[str, bool]] = ..., b: Optional[Union[str, bool]] = ..., connection: bool = ..., c: bool = ..., namespace: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., relative: bool = ..., r: bool = ..., short: bool = ..., s: bool = ..., type: bool = ..., t: bool = ...) -> Any:
    r"""
    dagObjectCompare can be used to compare to compare objects based on:
    
    type -  Currently supports transform nodes and shape nodes
    relatives - Compares DAG objects' children and parents
    connections - Checks to make sure the two dags are connected to the same sources and destinations
    attributes - Checks to make sure that the properties of active attributes are the same

    Args:
        attribute | a: (create) - Compare dag object attributes
        bail | b: (create) - Bail on first error or bail on category. Legal values are "never", "first", and "category".
        connection | c: (create) - Compare dag connections
        namespace | n: (create) - The baseline namespace
        relative | r: (create) - dag relatives
        short | s: (create) - Compress output to short form (not as verbose)
        type | t: (create) - Compare based on dag object type
    """
    ...


def date(*args, date: bool = ..., d: bool = ..., format: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., shortDate: bool = ..., sd: bool = ..., shortTime: bool = ..., st: bool = ..., time: bool = ..., t: bool = ...) -> Any:
    r"""
    Returns information about current time and date. Use the predefined formats, or the -format flag to specify the output format.

    Args:
        date | d: (create) - Returns the current date. Format is YYYY/MM/DD
        format | f: (create) - Specifies a string defining how the date and time should be represented. All occurences of the keywords below will be replaced with the corresponding values:  KeywordBecomes YYYYCurrent year, using 4 digits YYLast two digits of the current year MMCurrent month, with leading 0 if necessary DDCurrent day, with leading 0 if necessary hhCurrent hour, with leading 0 if necessary mmCurrent minute, with leading 0 if necessary ssCurrent second, with leading 0 if necessary
        shortDate | sd: (create) - Returns the current date. Format is MM/DD
        shortTime | st: (create) - Returns the current time. Format is hh:mm
        time | t: (create) - Returns the current time. Format is hh:mm:ss
    """
    ...


def dbcount(*args, enabled: bool = ..., e: bool = ..., file: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., keyword: Optional[Union[str, bool]] = ..., k: Optional[Union[str, bool]] = ..., list: bool = ..., l: bool = ..., maxdepth: Optional[Union[int, bool]] = ..., md: Optional[Union[int, bool]] = ..., quick: bool = ..., q: bool = ..., reset: bool = ..., r: bool = ..., spreadsheet: bool = ..., s: bool = ...) -> Any:
    r"""
    The dbcount command is used to print and manage a list of statistics
    collected for counting operations.  These statistics are displayed
    as a list of hits on a particular location in code, with added reference
    information for pointers/strings/whatever.
    If -reset is not specified then statistics are printed.

    Args:
        enabled | e: (create) - Set the enabled state of the counters ('on' to enable, 'off' to disable). Returns the list of all counters affected.
        file | f: (create) - Destination file of the enabled count objects.  Use the special names stdout and stderr to redirect to your command window.  As well, the special name msdev is available on NT to direct your output to the debug tab in the output window of Developer Studio.
        keyword | k: (create) - Print only the counters whose name matches this keyword (default is all).
        list | l: (create) - List all available counters and their current enabled status. (The only thing you can do when counters are disabled.)
        maxdepth | md: (create) - Maximum number of levels down to traverse and report. 0 is the default and it means continue recursing as many times as are requested.
        quick | q: (create) - Display only a summary for each counter type instead of the full details.
        reset | r: (create) - Reset all counters back to 0 and remove all but the top level counters. Returns the list of all counters affected.
        spreadsheet | s: (create) - Display in spreadsheet format instead of the usual nested braces. This will include a header row that contains 'Count Level1 Level2 Level3...', making the data suitable for opening directly in a spreadsheet table.
    """
    ...


def dbfootprint(*args, allObjects: bool = ..., all: bool = ..., outputFile: Optional[Union[str, bool]] = ..., of: Optional[Union[str, bool]] = ..., type: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command lets you explore the memory usage of specific parts of the
    scene. Query the 'type' flag to see what all of the different types are,
    and query a specific type to get a description of what information it will
    provide.
    All output is in JSON format so that it can easily be processed and formatted
    to highlight areas of interest.

    Args:
        allObjects | all: (create) - Ignore any specified or selected objects and measure all applicable objects. The definition of "allObjects" will vary based on the type of objects being measured - see the type documentation for details on what it means for that type. By default if no objects are selected or specified then it will behave as though this flag were set.
        outputFile | of: (create) - Specify the location of a file to which the information is to be dumped. Default will return the value from the command.  Use the special names stdout, cout, stderr, or cerr to redirect to the standard output or error locations.
        type | t: (create, query) - Specify the type of object footprint to measure. The various types are registered at run time and can be listed by querying this flag without a value. If you query it with a value then you get a description of what that particular type is going to measure. 			In query mode, this flag can accept a value.
    """
    ...


def dbmessage(*args, file: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., list: bool = ..., l: bool = ..., monitor: bool = ..., m: bool = ..., type: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    The dbmessage command is used to install monitors for certain
    message types, dumping debug information as they are sent so that the
    flow of messages can be examined.

    Args:
        file | f: (create) - Destination file of the message monitoring information.  Use the special names stdout and stderr to redirect to your command window.  As well, the special name msdev is available on NT to direct your output to the debug tab in the output window of Developer Studio. Default value is stdout.
        list | l: (create) - List all available message types and their current enabled status.
        monitor | m: (create) - Set the monitoring state of the message type ('on' to enable, 'off' to disable). Returns the list of all message types being monitored after the change in state.
        type | t: (create) - Monitor only the messages whose name matches this keyword (default is all).
    """
    ...


def dbpeek(*args, allObjects: bool = ..., all: bool = ..., argument: Optional[Union[str, bool]] = ..., a: Optional[Union[str, bool]] = ..., count: Optional[Union[int, bool]] = ..., c: Optional[Union[int, bool]] = ..., evaluationGraph: bool = ..., eg: bool = ..., operation: Optional[Union[str, bool]] = ..., op: Optional[Union[str, bool]] = ..., outputFile: Optional[Union[str, bool]] = ..., of: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    The dbpeek command is used to analyze the Maya data for
    information of interest. See a description of the flags for details
    on what types of things can be analyzed.

    Args:
        allObjects | all: (create, query) - Ignore any specified or selected objects and peek into all applicable objects. The definition of "allObjects" will vary based on the peek operation being performed - see the flag documentation for details on what it means for a given operation. By default if no objects are selected or specified then it will behave as though this flag were set.
        argument | a: (create, multiuse, query) - Specify one or more arguments to be passed to the operation. The acceptable values for the argument string are documented in the flag to which they will be applied. If the argument itself takes a value then the value will be of the form "argname=argvalue". 			In query mode, this flag needs a value.
        count | c: (create, query) - Specify a count to be used by the test. Different tests make different use of the count, query the operation to find out how it interprets the value. For example a performance test might use it as the number of iterations to run in the test, an output operation might use it to limit the amount of output it produces.
        evaluationGraph | eg: (create, query) - Ignore any nodes that are not explicitly part of the evaluation graph. Usually this means nodes that are affected either directly or indirectly by animation. May also tailor the operation to be EM-specific in the areas where the structure of the DG differs from the structure of the EM, for example, plug configurations. This is a filter on the currently selected nodes, including the use of the "allObjects" flag.
        operation | op: (create, query) - Specify the peeking operation to perform. The various operations are registered at run time and can be listed by querying this flag without a value. If you query it with a value then you get the detail values that peek operation accepts and a description of what it does. 			In query mode, this flag can accept a value.
        outputFile | of: (create, query) - Specify the location of a file to which the information is to be dumped. Default will return the value from the command.  Use the special names stdout and stderr to redirect to your command window. The special name msdev is available when debugging on Windows to direct your output to the debug tab in the output window of Visual Studio.
    """
    ...


def dbtrace(*args, filter: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., info: bool = ..., i: bool = ..., keyword: Optional[Union[str, bool]] = ..., k: Optional[Union[str, bool]] = ..., mark: bool = ..., m: bool = ..., off: bool = ..., output: Optional[Union[str, bool]] = ..., o: Optional[Union[str, bool]] = ..., timed: bool = ..., tm: bool = ..., title: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ..., verbose: bool = ..., v: bool = ..., query: bool = ...) -> Any:
    r"""
    The dbtrace command is used to manipulate trace objects.
              The keyword is the only mandatory argument, indicating which trace
              object is to be altered.
              
    Trace Objects to affect (keyword KEY)
    Optional filtering criteria (filter FILTER)
    Function (off, output FILE, mark, title TITLE, timed : default operation is to enable traces)
    
              You can use the query mode to find out which keywords are currently
              active (query with no arguments) or inactive (query with the off
              argument).
              You can enhance that query with or without a keyword argument to find
              out where their output is going (query with the output
              argument), out what filters are currently applied (query with the
              filter argument), or if their output will be
              timestamped (query with the timed argument).

    Args:
        filter | f: (create, query) - Set the filter object for these trace objects (see 'dgfilter')
        info | i: (query) - In query mode return a brief description of the trace object.
        keyword | k: (create, multiuse, query) - Keyword of the trace objects to affect 			In query mode, this flag can accept a value.
        mark | m: (create) - Display a mark for all outputs of defined trace objects
        off: (create) - Toggle the traces off.  If omitted it will turn them on.
        output | o: (create, query) - Destination file of the affected trace objects.  Use the special names stdout and stderr to redirect to your command window. The special name msdev is available on Windows to direct your output to the debug tab in the output window of Visual Studio.
        timed | tm: (create, query) - Turn on/off timing information in the output of the specified trace objects.
        title | t: (create) - Display a title mark for all outputs of defined trace objects
        verbose | v: (create) - Include all traces in output and filter queries, not just those turned on.
    """
    ...


def detachDeviceAttr(*args, all: bool = ..., attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., axis: Optional[Union[str, bool]] = ..., ax: Optional[Union[str, bool]] = ..., device: Optional[Union[str, bool]] = ..., d: Optional[Union[str, bool]] = ..., selection: bool = ..., sl: bool = ..., query: bool = ...) -> Any:
    r"""
    This command detaches connections between device axes and node
    attributes.  The command line arguments are the same as for
    the corresponding attachDeviceAttr except for the clutch argument
    which can not be used in this command.

    Args:
        all | all: (create) - Delete all attachments on every device.
        attribute | at: (create) - The attribute to detach. This flag must be used with the -d/device flag.
        axis | ax: (create) - The axis to detach. This flag must be used with the -d/device flag.
        device | d: (create) - Delete the attachment for this device. If the -ax/axis flag is not used, all of the attachments connected to this device are detached.
        selection | sl: (create) - Detaches selection attachments.
    """
    ...


def deviceEditor(*args, control: bool = ..., ctl: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., exists: bool = ..., ex: bool = ..., filter: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., fmc: Optional[Union[str, bool]] = ..., highlightConnection: Optional[Union[str, bool]] = ..., hlc: Optional[Union[str, bool]] = ..., lockMainConnection: bool = ..., lck: bool = ..., mainListConnection: Optional[Union[str, bool]] = ..., mlc: Optional[Union[str, bool]] = ..., panel: Optional[Union[str, bool]] = ..., pnl: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., selectionConnection: Optional[Union[str, bool]] = ..., slc: Optional[Union[str, bool]] = ..., stateString: bool = ..., sts: bool = ..., takePath: Optional[Union[str, bool]] = ..., tp: Optional[Union[str, bool]] = ..., unParent: bool = ..., up: bool = ..., unlockMainConnection: bool = ..., ulk: bool = ..., updateMainConnection: bool = ..., upd: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This creates an editor for creating/modifying attachments to
    input devices.

    Args:
        control | ctl: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag | dtg: (create, edit, query) - Attaches a tag to the editor.
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        filter | f: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        forceMainConnection | fmc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        highlightConnection | hlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        lockMainConnection | lck: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        mainListConnection | mlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        panel | pnl: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent | p: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        selectionConnection | slc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        stateString | sts: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        takePath | tp: (edit, query) - The path used for writing/reading take data through the editor.
        unParent | up: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection | ulk: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection | upd: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
    """
    ...


def devicePanel(*args, control: bool = ..., ctl: bool = ..., copy: str = ..., cp: str = ..., createString: bool = ..., cs: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., editString: bool = ..., es: bool = ..., exists: bool = ..., ex: bool = ..., init: bool = ..., isUnique: bool = ..., iu: bool = ..., label: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., menuBarRepeatLast: bool = ..., mrl: bool = ..., menuBarVisible: bool = ..., mbv: bool = ..., needsInit: bool = ..., ni: bool = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., popupMenuProcedure: Optional[Union[str, bool]] = ..., pmp: Optional[Union[str, bool]] = ..., replacePanel: str = ..., rp: str = ..., tearOff: bool = ..., to: bool = ..., tearOffCopy: Optional[Union[str, bool]] = ..., toc: Optional[Union[str, bool]] = ..., tearOffRestore: bool = ..., tor: bool = ..., unParent: bool = ..., up: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is now obsolete. It is included only for the purpose of file compatibility. It creates a blank panel.

    Args:
        control | ctl: (query) - Returns the top level control for this panel. Usually used for getting a parent to attach popup menus. CAUTION: panels may not have controls at times.  This flag can return "" if no control is present.
        copy | cp: (edit) - Makes this panel a copy of the specified panel.  Both panels must be of the same type.
        createString | cs: (edit) - Command string used to create a panel
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag | dtg: (create, edit, query) - Attaches a tag to the Maya panel.
        editString | es: (edit) - Command string used to edit a panel
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        init | init: (create, edit) - Initializes the panel's default state.  This is usually done automatically on file -new and file -open.
        isUnique | iu: (query) - Returns true if only one instance of this panel type is allowed.
        label | l: (edit, query) - Specifies the user readable label for the panel.
        menuBarRepeatLast | mrl: (create, edit, query) - Controls whether clicking on the menu header with the middle mouse button would repeat the last selected menu item.
        menuBarVisible | mbv: (create, edit, query) - Controls whether the menu bar for the panel is displayed.
        needsInit | ni: (edit, query) - (Internal) On Edit will mark the panel as requiring initialization. Query will return whether the panel is marked for initialization.  Used during file -new and file -open.
        parent | p: (create) - Specifies the parent layout for this panel.
        popupMenuProcedure | pmp: (edit, query) - Specifies the procedure called for building the panel's popup menu(s). The default value is "buildPanelPopupMenu".  The procedure should take one string argument which is the panel's name.
        replacePanel | rp: (edit) - Will replace the specified panel with this panel.  If the target panel is within the same layout it will perform a swap.
        tearOff | to: (edit, query) - Will tear off this panel into a separate window with a paneLayout as the parent of the panel. When queried this flag will return if the panel has been torn off into its own window.
        tearOffCopy | toc: (create) - Will create this panel as a torn of copy of the specified source panel.
        tearOffRestore | tor: (create, edit) - Restores panel if it is torn off and focus is given to it. If docked, becomes the active panel in the docked window. This should be the default flag that is added to all panels instead of -to/-tearOff flag which should only be used to tear off the panel.
        unParent | up: (edit) - Specifies that the panel should be removed from its layout. This (obviously) cannot be used with query.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
    """
    ...


def dgdirty(*args, allPlugs: bool = ..., a: bool = ..., clean: bool = ..., c: bool = ..., implicit: bool = ..., i: bool = ..., list: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., propagation: bool = ..., p: bool = ..., showTiming: bool = ..., st: bool = ..., verbose: bool = ..., v: bool = ..., query: bool = ...) -> Any:
    r"""
    The dgdirty command is used to force a dependency graph
    dirty message on a node or plug.  Used for debugging to find
    evaluation problems.  If no nodes are specified then the current
    selection list is used.
    If the list flag is used it will return the list of things
    currently marked as dirty (or clean if the clean flag was
    also used). The returned values will be the names of plugs either
    clean/dirty themselves, at both ends of a clean/dirty connection,
    or representing the location of clean/dirty data on the node.
    Be careful using this option in conjunction with
    the all flag, the list could be huge.

    Args:
        allPlugs | a: (create, query) - Ignore the selected or specified objects and dirty (or clean) all plugs.
        clean | c: (create, query) - If this flag is set then the attributes are cleaned.  Otherwise they are set to dirty.
        implicit | i: (create, query) - If this flag is set then allow the implicit or default nodes to be processed as well. Otherwise they will be skipped for efficiency.
        list | l: (create, query) - When this flag is specified then instead of sending out dirty/clean messages the list of currently dirty/clean objects will be returned. The allPlugs and clean flags are respected to narrow guide the values to be returned. The value of the flag tells what will be reported.  "data" or "d" = show plugs that have dirty/clean data "plug" or "p" = show plugs that have dirty/clean states "connection" or "c" = show plugs with connections that have dirty/clean states Query this flag to find all legal values of the flag. Query this flag with its value already set to get a description of what that value means.  Note that "p" and "c" modes are restricted to plugs that have connections or non-standard state information. Other attributes will not have state information to check, though they will have data. In the case of array attributes only the children that have values currently set will be considered. No attempt will be made to evaluate them in order to update the available child lists. e.g. if you have a DAG with transform T1 and shape S1 the instanced attribute S1.wm[0] will be reported. If in a script you create a second instance T2->S1 and immediately list the plugs again before evaluation you will still only see S1.wm[0]. The new S1.wm[1] won't be reported until it is created through an evaluation, usually caused by refresh, a specific getAttr command, or an editor update. Note that the list is only for selected nodes. Unlike when dirty messages are sent this does not travel downstream.
        propagation | p: (create, query) - If this flag is set then the ability of dirty messages to flow through the graph is left enabled.
        showTiming | st: (create, query) - If this flag is used then show how long the dirty messages took to propagate.
        verbose | v: (create, query) - Prints out all of the plugs being set dirty on stdout.
    """
    ...


def dgeval(*args, src: bool = ..., verbose: bool = ..., v: bool = ...) -> Any:
    r"""
    The dgeval command is used to force a dependency graph
    evaluate of a node or plug.  Used for debugging to find
    propagation problems.
    
    Normally the selection list is used to determine which objects to
    evaluate, but you can add to the selection list by specifying which
    objects you want on the command line.

    Args:
        src | src: (create) - This flag is obsolete. Do not use.
        verbose | v: (create) - If this flag is used then the results of the evaluation(s) is/are printed on stdout.
    """
    ...


def dgfilter(*args, attribute: Optional[Union[str, bool]] = ..., atr: Optional[Union[str, bool]] = ..., list: bool = ..., l: bool = ..., logicalAnd: Optional[Union[Tuple[str, str], bool]] = ..., logicalNot: Optional[Union[str, bool]] = ..., logicalOr: Optional[Union[Tuple[str, str], bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., node: Optional[Union[str, bool]] = ..., nd: Optional[Union[str, bool]] = ..., nodeType: Optional[Union[str, bool]] = ..., nt: Optional[Union[str, bool]] = ..., plug: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    The dgfilter command is used to define Dependency Graph filters
    that select DG objects based on certain criteria.  The command itself
    can be used to filter objects or it can be attached to a
    dbtrace object to selectively filter what output is traced.
    If objects are specified then apply the filter to those objects and
    return a boolean indicating whether they passed or not, otherwise
    return the name of the filter.  An invalid filter will pass all
    objects.  For multiple objects the return value is the logical
    "AND" of all object's return values.

    Args:
        attribute | atr: (create) - Select objects whose attribute names match the pattern.
        list | l: (create) - List the available filters.  If used in conjunction with the -name flag it will show a description of what the filter is.
        logicalAnd | logicalAnd: (create) - Logical AND of two filters.
        logicalNot | logicalNot: (create) - Logical inverse of filter.
        logicalOr | logicalOr: (create) - Logical OR of two filters.
        name | n: (create) - Use filter named FILTER (or create new filter with that name). If no objects are specified then the name given to the filter will be returned.
        node | nd: (create) - Select objects whose node names match the pattern.
        nodeType | nt: (create) - Select objects whose node type names match the pattern.
        plug | p: (create) - Select objects whose plug names match the pattern.
    """
    ...


def dgInfo(*args, allNodes: bool = ..., all: bool = ..., connections: bool = ..., c: bool = ..., dirty: bool = ..., d: bool = ..., nodes: bool = ..., n: bool = ..., nonDeletable: bool = ..., nd: bool = ..., outputFile: Optional[Union[str, bool]] = ..., of: Optional[Union[str, bool]] = ..., propagation: bool = ..., p: bool = ..., short: bool = ..., s: bool = ..., size: bool = ..., sz: bool = ..., subgraph: bool = ..., sub: bool = ..., type: Optional[Union[str, bool]] = ..., nt: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This command prints information about the DG in plain text.
    The scope of the information printed is the entire graph
    if the all flag is used, the nodes/plugs on the command line if
    they were specified, and the selection list, in that order.
    Each plug on a connection will have two pieces of state information
    displayed together at the end of the line on which they are printed.
    There are two possible values for each of the two states displayed.
    The values are updated when the DG pulls data across them, usually
    through evaluation, or pushes a dirty message through them. There
    are some subtleties in how the data is pulled through the connection
    but for simplicity it will be referred to as "evaluation".
    The values displayed will be CLEAN or DIRTY followed by PROP or BLOCK.
    The first keyword has these meanings:
    
    CLEAN means that evaluation of the plug's connection
    succeeded and no dirty messages have come through it since then.
    It also implies that the destination end of the connection has
    received the value from the source end.
    
    DIRTY means that a dirty message has passed through the
    plug's connection since the last time an evaluation was made on the
    destination side of that connection.
    
    
    Note: the data on the node has its own dirty state that depends
    on other factors so having a clean connection doesn't necessarily
    mean the plug's data is clean, and vice versa.
    The second keyword has these meanings:
    
    PROP means that the connection will allow dirty messages
    to pass through and forwards them to all destinations.
    
    BLOCK means that a dirty message will stop at this connection
    and not continue on to any destinations. This is an optimization that
    prevents excessive dirty flag propagation when many values are changing,
    for example, a frame change in an animated sequece.
    
    
    The combination CLEAN BLOCK should never be seen in a valid DG.
    This indicates that while the plug connection has been evaluated since
    the last dirty message it will not propagate any new dirty messages
    coming in to it. That in turn means downstream nodes will not be
    notified that the graph is changing and they will not evaluate properly.
    Recovering from this invalid state requires entering the command
    dgdirty -a to mark everything dirty and restart proper evaluation.
    Think of this command as the reset/reboot of the DG world.
    Both state types behave differently depending on your connection type.
    
    Simple A -> B : Plugs at both ends of the connection
    share the same state information. The state information updates when an
    evaluation request comes to A from B, or a dirty message is sent from
    A to B.
    
    Fan-Out A -> B, A -> C : Each of A, B, and
    C have their own unique state information. B and C behave as described above.
    A has its state information linked to B and C - it will have CLEAN
    only when both B and C have CLEAN, it will have BLOCK only
    when both B and C have BLOCK.
    
    In-Out A -> B, C -> A : Each of A, B, and
    C have their own unique state information. B and C behave as described above.
    A has its state information linked to B and C. The CLEAN|DIRTY flag
    looks backwards, then forwards:
    
    if( C == CLEAN ) A = CLEAN
    else if( B == CLEAN ) A = CLEAN
    
    The BLOCK state is set when a dirty message passes through A, and
    the PROP state is set either when A is set clean or an evaluation
    passes through A.
    
    
    There are some other exceptions to these rules:
    
    
    All of this state change information only applies to dirty messages and
    evaluations that use the normal context. Any changes in other contexts,
    for example, through the getAttr -t TIME command, does not affect the
    state in the connections.
    
    
    Param curves and other passive inputs, for example blend nodes coming from
    param curves, will not disable propagation. Doing so would make the keyframing
    workflow impossible.
    
    
    Certain messages can choose to completely ignore the connection state
    information. For example when a node's state attribute changes a connection
    may change to a blocking one so the message has to be propagated at least
    one step further to all of its destinations. This way they can update their
    information.
    
    
    Certain operations can globally disable the use of the propagaton state
    to reduce message flow.  The simplest example is when the evaluation
    manager is building its graph. It has to visit all nodes so the propagation
    cannot be blocked.
    
    
    The messaging system has safeguards against cyclic messages flowing through
    connections but sometimes a message bypasses the connection completely and
    goes directly to the node. DAG parents do this to send messages to their
    children. So despite connections into a node all having the BLOCK
    state it could still receive dirty messages.

    Args:
        allNodes | all: (create) - Use the entire graph as the context
        connections | c: (create) - Print the connection information
        dirty | d: (create) - Only print dirty/clean nodes/plugs/connections.  Default is both
        nodes | n: (create) - Print the specified nodes (or the entire graph if -all is used)
        nonDeletable | nd: (create) - Include non-deletable nodes as well (normally not of interest)
        outputFile | of: (create) - Send the output to the file FILE instead of STDERR
        propagation | p: (create) - Only print propagating/not propagating nodes/plugs/connections. Default is both.
        short | s: (create) - Print using short format instead of long
        size | sz: (create) - Show datablock sizes for all specified nodes. Return value is tuple of all selected nodes (NumberOfNodes, NumberOfDatablocks, TotalDatablockMemory)
        subgraph | sub: (create) - Print the subgraph affected by the node or plugs (or all nodes in the graph grouped in subgraphs if -all is used)
        type | nt: (create) - Filter output to only show nodes of type NODETYPE
    """
    ...


def dgmodified(*args) -> Any:
    r"""
    The dgmodified command is used to find out which nodes in the
              dependency graph have been modified.  This is mostly useful for fixing
              instances where file new asks you to save when no changes have been
              made to the scene.

    Args:
    """
    ...


def dgtimer(*args, combineType: bool = ..., ct: bool = ..., hide: Optional[Union[str, bool]] = ..., hi: Optional[Union[str, bool]] = ..., hierarchy: bool = ..., h: bool = ..., maxDisplay: Optional[Union[int, bool]] = ..., m: Optional[Union[int, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., noHeader: bool = ..., nh: bool = ..., outputFile: Optional[Union[str, bool]] = ..., o: Optional[Union[str, bool]] = ..., overhead: bool = ..., oh: bool = ..., rangeLower: Optional[Union[float, bool]] = ..., rgl: Optional[Union[float, bool]] = ..., rangeUpper: Optional[Union[float, bool]] = ..., rgu: Optional[Union[float, bool]] = ..., reset: bool = ..., r: bool = ..., returnCode: Optional[Union[str, bool]] = ..., rc: Optional[Union[str, bool]] = ..., returnType: Optional[Union[str, bool]] = ..., rt: Optional[Union[str, bool]] = ..., show: Optional[Union[str, bool]] = ..., sh: Optional[Union[str, bool]] = ..., sortMetric: Optional[Union[str, bool]] = ..., sm: Optional[Union[str, bool]] = ..., sortType: Optional[Union[str, bool]] = ..., st: Optional[Union[str, bool]] = ..., threshold: Optional[Union[float, bool]] = ..., th: Optional[Union[float, bool]] = ..., timerOff: bool = ..., off: bool = ..., timerOn: bool = ..., on: bool = ..., trace: bool = ..., tr: bool = ..., type: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ..., uniqueName: bool = ..., un: bool = ..., updateHeatMap: Optional[Union[int, bool]] = ..., uhm: Optional[Union[int, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command measures dependency graph node performance by managing
    timers on a per-node basis. Logically, each DG node has a timer
    associated with it which records the amount of real time spent
    in various operations on its plugs. The time measurement includes the cost
    of copying data to the node on behalf of the operation, MEL commands
    executed by an expression contained in an expression invoked by the
    node, and includes
    any wait time such as when a fileTexture node loads an image file from
    disk. Most DG operations are reported including compute, draw, and dirty
    propagation.
    
    The various operations we measure are called "metrics" and the types of
    timers are called "timer types". The various metrics are always measured
    when timing is on, but are only queried when specified via the -show and
    -hide flags. The metrics currently supported are listed in detail under
    the -show flag below. For each metric we support a standard set of timer
    types. There are three of these:
    "self" for self time (the time specific to the node and not its children),
    "inclusive" (time including children of the node), and
    "count" (number of operations of the given metric on the node).
    
    The timing mechanism which is used by dgtimer is built into the DG
    itself, thus ALL depend nodes can be timed and there is no need for
    programmers writing plug-ins using the OpenMaya API to add any special
    code in order for their nodes to be timed -- its all
    handled transparently.
    
    The dgtimer command allows node timers to be turned on, off, reset
    to zero, and have their current value displayed, and these operations
    can be performed globally on all nodes or on a specific set of nodes
    defined by name, type or parentage. Note that all timer measurements are
    computed in "real time" (the same time measurement you get from a
    wristwatch) as opposed to "CPU time" (which only measures time when the
    processor is executing your code). All times are displayed in seconds.
    
    Use the -query flag to display the current timer values on a node,
    
    use -on to turn on timing,
    
    use -off to turn off timing,
    
    and -reset to reset timers to zero.
    
    To display the values measured during timing, there are two approaches.
    The first method is to use the -query flag can be used to report the information which
    has been measured. The second method is to use the query methods available on
    the OpenMaya class MFnDependencyNode (see the OpenMaya documentation for details).
    
    What follows is a description of what is generated via -query. The output
    is broken out into several sections and these are described as follows:
    
    SECTION 1:
    Section 1 of the dgtimer output contains global information. This section
    can be disabled via the -hoHeader flag.
    These values are reset whenever a global timer reset
    occurs (i.e. dgtimer -reset; is specified). The global values which are
    reported are:
    
    
    Total real time: the total wall-clock time since the
    last global timer reset. This is the actual time which has been spent as you
    might measure it measure it with your watch.
    On a multi-processing system, this value will always remain true to to real
    time (unlike user and sys time).
    Total user time: the total time the CPU(s) spent
    processing Maya not including any system time since the last global
    timer reset.
    Total sys time: the total time the CPU(s) spent in
    operating system calls on behalf of Maya since the last global timer reset.
    
    Summary of each metric for all nodes: a summary of self and count for each metric
    that we measure:
    
    Real time in callbacks reports the self time and count for the "callback" metric.
    Real time in compute reports the self time and count for the "compute" metric.
    Real time in dirty propagation reports the self time and count for the "dirty" metric.
    Real time in drawing reports the self time and count for the "draw" metric.
    Real time fetching data from plugs reports the self time and count for the "fetch" metric.
    
    Breakdown of select metrics in greater detail: a reporting of certain combinations of
    metrics that we measure:
    
    
    Real time in compute invoked from callback reports the self time spent in compute
    when invoked either directly or indirectly by a callback.
    Real time in compute not invoked from callback reports the self time spent in compute
    not invoked either directly or indirectly by a callback.
    
    SECTION 2:
    Section 2 of the dgtimer -query output contains per-node information. There is a header which
    describes the meaning of each column, followed by the actual per-node data, and this is
    ultimately followed by a footer which summarises the totals per column. Note that the data
    contained in the footer is the global total for each metric and will include any nodes that
    have been deleted since the last reset, so the value in the footer MAY exceed what you get when you total the
    individual values in the column. To prevent the header
    and footer from appearing, use the -noHeader flag to just display the per-node data.
    
    The columns which are displayed are as follows:
    
    Rank: The order of this node in the sorted list of all nodes, where the list
    is sorted by -sortMetric and -sortType flag values (if these are omitted the default
    is to sort by self compute time).
    ON: Tells you if the timer for that node is currently on or off. (With
    dgtimer, you have the ability to turn timing on and off on a per-node basis).
    Per-metric information: various columns are reported for each metric. The
    name of the metric is reported at in the header in capital letters (e.g. "DRAW"). The standard
    columns for each metric are:
    
    Self: The amount of real time (i.e. elapsed time as you might measure
    it with a stopwatch) spent performing the operation (thus if the metric is "DRAW", then
    this will be time spent drawing the node).
    Inclusive: The amount of real time (i.e. elapsed time as you might measure
    it with a stopwatch) spent performing the operation including any child operations
    that were invoked on behalf of the operation (thus if the metric is "DRAW", then
    this will be the total time taken to draw the node including any child operations).
    Count: The number of operations that occued on this node (thus if the metric
    is "DRAW", then the number of draw operations on the node will be reported).
    
    Sort information if a column is the one being used to sort all the per-node
    dgtimer information, then that column is followed by a Percent and Cumulative
    column which describe a running total through the listing. Note that "-sortType none"
    prevents these two columns from appearing and implicitely sorts on "self" time.
    
    After the per-metric columns, the node name and type are reported:
    
    Type The node type.
    Name The name of the node. If the node is file referenced and you
    are using namespaces, the namespace will be included. You can also force the
    dagpath to be displayed by specifying the -uniqueName flag.
    Plug-in name If the node was implemented in an OpenMaya plug-in, the
    name of that plug-in is reported.
    
    
    SECTION 3:
    Section 3 of the dgtimer -query output describes time spent in callbacks. Note that
    section 3 only appears when the CALLBACK metric is shown (see the -show flag).
    
    The first part is SECTION 3.1 lists the time per callback with each entry comprising:
    
    The name of the callback, such as "attributeChangedMsg". These names are internal
    Maya names, and in the cases where the callback is available through the OpenMaya API,
    the API access to the callback is similarly named.
    The name is followed by a breakdown per callbackId. The callbackId is an identifying
    number which is unique to each client that is registered to a callback and can
    be deduced by the user, such as through the OpenMaya API. You can cross-reference by finding
    the same callbackId value listed in SECTIONs 3.1 and 3.3.
    
    Self time (i.e. real time spent within that callbackId type not including any child
    operations which occur while processing the callback).
    Percent (see the -sortType flag). Note that the percent values are listed to sum up to
    100% for that callback. This is not a global percent.
    Cumulative (see the -sortType flag).
    Inclusive time (i.e. real time spent within that callbackId including any child operations).
    Count (number of times the callbackId was invoked).
    API lists "Y" if the callbackId was defined through the OpenMaya API, and "N" if the
    callbackId was defined internally within Maya.
    Node lists the name of the node this callbackId was associated with. If the callbackId was
    associated with more than one node, the string "*multiple*" is printed. If there was no node
    associated with the callbackId (or its a callback type in which the node is hard to deduce),
    the entry is blank.
    
    After the callbackId entries are listed, a dashed line is printed followed by a single
    line listing the self, inclusive and count values for the callback. Note that the percent
    is relative to the global callback time.
    
    At the bottom of SECTION 3.1 is the per-column total. The values printed match the summation at
    the bottom of the listing in section 2. Note that the values from SECTION 3.1
    include any nodes that have been deleted since the last reset. The thresholding parameters
    (-threshold, -rangeLower, -rangeUpper and -maxDisplay) are honoured when generating the listing.
    The sorting of the
    rows and display of the Percent and Cumulative columns obeys the -sortType flag. As the listing
    can be long, zero entries are not displayed.
    
    The second part is SECTION 3.2 which lists the data per callbackId. As noted earlier, the
    callbackId is an identifying
    number which is unique to each client that is registered to a callback and can
    be deduced by the user, such as through the OpenMaya API. The entries in SECTION 3.2 appear
    as follows:
    
    CallbackId the numeric identifier for the callback. You can cross reference by
    finding the same callbackId value listed in SECTIONs 3.1 and 3.3.
    For each callbackId, the data is broken down per-callback:
    
    Callback the name of the callback, e.g. "attributeChangedMsg".
    Percent, Cumulative, Inclusive, Count, API and Node entries as described in SECTION 3.1.
    
    After the callback entries are listed for the callbackId, a dashed followed by a summary line is
    printed. The summary line lists the self, inclusive and count values for the callback. Note that
    the percent is relative to the global callback time.
    
    
    The third part is SECTION 3.3 which lists data per-callback per-node. The
    nodes are sorted based on the -sortType flag, and for each node, the
    callbacks are listed, also sorted based on the -sortType flag. As this
    listing can be long, zero entries are not displayed. An important note for SECTION 3.3 is
    that only nodes which still exist are displayed. If a node has been deleted, no infromation
    is listed.

    Args:
        combineType | ct: (query) - Causes all nodes of the same type (e.g. animCurveTA) to be combined in the output display.
        hide | hi: (create, multiuse, query) - This flag is the converse of -show. As with -show, it is a query-only flag which can be specified multiple times. If you do specify -hide, we display all columns except those listed by the -hide flags.
        hierarchy | h: (create, query) - Used to specify that a hierarchy of the dependency graph be affected, thus "-reset -hierarchy -name ball" will reset the timers on the node named "ball" and all of its descendents in the dependency graph.
        maxDisplay | m: (query) - Truncates the display so that only the most expenive "n" entries are printed in the output display.
        name | n: (create, query) - Used in conjunction with -reset or -query to specify the name of the node to reset or print timer values for. When querying a single timer, only a single line of output is generated (i.e. the global timers and header information is omitted). Note that one can force output to the script editor window via the "-outputFile MEL" option to make it easy to grab the values in a MEL script. Note: the -name and -type flag cannot be used together.
        noHeader | nh: (create, query) - Used in conjunction with -query to prevent any header or footer information from being printed. All that will be output is the per-node timing data. This option makes it easier to parse the output such as when you output the query to a file on disk using the -outputFile option.
        outputFile | o: (query) - Specifies where the output of timing or tracing is displayed. The flag takes a string argument which accepts three possible values:   The name of a file on disk. Or the keyword "stdout", which causes output to be displayed on the terminal window (Linux and Macintosh), and the status window on Windows. Or the keyword "MEL", which causes output to be displayed in the Maya Script Editor (only supported with -query).  The "stdout" setting is the default behaviour.  This flag can be used with the -query flag as well as the -trace flag.  When used with the -trace flag, any tracing output will be displayed on the destination specified by the -outputFile (or stdout if -outputFile is omitted). Tracing operations will continue to output to the destination until you specify the -trace and -outputFile flags again.  When used with the -query flag, timing output will be displayed to the destination specified by the -outputFile (or "stdout" if -outputFile is omitted).  Here are some examples of how to use the -query, -trace and -outputFile flags:  Example: output the timing information to a single file on disk:   dgtimer -on;                                       // Turn on timing create some animated scene content; play -wait;                                        // Play the scene through dgtimer -query -outputFile "/tmp/timing.txt"       // Output node timing information to a file on disk   Example: output the tracing information to a single file on disk:   dgtimer -on;                                       // Turn on timing create some animated scene content; dgtimer -trace on -outputFile "/tmp/trace.txt"     // Turn on tracing and output the results to file play -wait;                                        // Play the scene through; trace info goes to /tmp/trace.txt dgtimer -query;                                    // But the timing info goes to the terminal window play -wait;                                        // Play the scene again, trace info still goes to /tmp/trace.txt   Example: two runs, outputting the trace information and timing information to separate files:   dgtimer -on;                                       // Turn on timing create some animated scene content; dgtimer -trace on -outputFile "/tmp/trace1.txt"    // Turn on tracing and output the results to file play -wait;                                        // Play the scene through dgtimer -query -outputFile "/tmp/query1.txt"       // Output node timing information to another file dgtimer -reset; dgtimer -trace on -outputFile "/tmp/trace2.txt"    // Output tracing results to different file play -wait;                                        // Play the scene through dgtimer -query -outputFile "/tmp/query2.txt"       // Output node timing information to another file   Tips and tricks:   Outputting the timing results to the script editor makes it easy to use the results in MEL e.g. string $timing[] = `dgtimer -query -outputFile MEL`. It is important to note that the -outputFile you specify with -trace is totally independent from the one you specify with -query. If the file you specify already exists, Maya will empty the file first before outputting data to it (and if the file is not writable, an error is generated instead).  In query mode, this flag needs a value.
        overhead | oh: (create, query) - Turns on and off the measurement of timing overhead. Under ordinary circumstances the amount of timing overhead is minimal compared with the events being measured, but in complex scenes, one might find the overhead to be measurable. By default this option is turned off. To enable it, specify "dgtimer -overhead true" prior to starting timing. When querying timing, the overhead is reported in SECTION 1.2 of the dgtimer output and is not factored out of each individual operation.
        rangeLower | rgl: (create) - This flag can be specified to limit the range of nodes which are displayed in a query, or the limits of the heat map with -updateHeatMap. The value is the lower percentage cutoff for the nodes which are processed. There is also a -rangeLower flag which sets the lower range limit. The default value is 0, meaning that all nodes with timing value below the upper range limit are considered.
        rangeUpper | rgu: (create) - This flag can be specified to limit the range of nodes which are displayed in a query, or the limits of the heat map with -updateHeatMap. The value is the upper percentage cutoff for the nodes which are processed. There is also a -rangeLower flag which sets the lower range limit. The default value is 100, meaning that all nodes with timing value above the lower range limit are considered.
        reset | r: (create) - Resets the node timers to zero. By default, the timers on all nodes as well as the global timers are reset, but if specified with the -name or -type flags, only the timers on specified nodes are reset.
        returnCode | rc: (create, query) - This flag has been replaced by the more general -returnType flag. The -returnCode flag was unfortunately specific to the compute metric only. It exists only for backwards compatability purposes. It will be removed altogether in a future release.  Here are some handy equivalences:  To get the total number of nodes: OLD WAY: dgtimer -rc nodecount -q; // Result:325//  NEW WAY: dgtimer -returnType total -sortType none -q; // Result:325//  OLD WAY: dgtimer -rc count -q; // Result:1270//  To get the sum of the compute count column: NEW WAY: dgtimer -returnType total -sortMetric compute -sortType count -q; // Result:1270//  OLD WAY: dgtimer -rc selftime -q; // Result:0.112898//  To get the sum of the compute self column: NEW WAY: dgtimer -returnType total -sortMetric compute -sortType self -q; // Result:0.112898//
        returnType | rt: (query) - This flag specifies what the double value returned by the dgtimer command represents. By default, the value returned is the global total as displayed in SECTION 1 for the column we are sorting on in the per-node output (the sort column can be specified via the -sortMetric and -sortType flags). However, instead of the total being returned, the user can instead request the individual entries for the column. This flag is useful mainly for querying without forcing any output. The flag accepts the values "total", to just display the column total, or "all" to display all entries individually.  For example, if you want to get the total of draw self time without any other output simply specify the following:  dgtimer -returnType total -sortMetric draw -sortType self -threshold 100 -noHeader -query; // Result: 7718.01 //  To instead get each individual entry, change the above query to:  dgtimer -returnType all -sortMetric draw -sortType self -threshold 100 -noHeader -query; // Result: 6576.01 21.91 11.17 1108.92 //  To get the inclusive dirty time for a specific node, use -name as well as -returnType all:  dgtimer -name "virginia" -returnType all -sortMetric dirty -sortType inclusive -threshold 100 -noHeader -query;  Note: to get the total number of nodes, use "-sortType none -returnType total".  To get the on/off status for each node, use "-sortType none -returnType all".
        show | sh: (create, multiuse, query) - Used in conjunction with -query to specify which columns are to be displayed in the per-node section of the output. -show takes an argument, which can be "all" (to display all columns), "callback" (to display the time spent during any callback processing on the node not due to evaluation), "compute" (to display the time spent in the node's compute methods), "dirty" (to display time spent propagating dirtiness on behalf of the node), "draw" (to display time spent drawing the node), "compcb" (to display time spent during callback processing on node due to compute), and "compncb" (to display time spent during callback processing on node NOT due to compute). The -show flag can be used multiple times, but cannot be specified with -hide. By default, if neither -show, -hide, or -sort are given, the effective display mode is: "dgtimer -show compute -query".
        sortMetric | sm: (create, query) - Used in conjunction with -query to specify which metric is to be sorted on when the per-node section of the output is generated, for example "draw" time. Note that the -sortType flag can also be specified to define which timer is sorted on: for example "dgtimer -sortMetric draw -sortType count -query" will sort the output by the number of times each node was drawn. Both -sortMetric and -sortType are optional and you can specify one without the other. The -sortMetric flag can only be specified at most once. The flag takes the following arguments: "callback" (to sort on time spent during any callback processing on the node), "compute" (to sort on the time spent in the node's compute methods), "dirty" (to sort on the time spent propagating dirtiness on behalf of the node), "draw" (to sort on time spent drawing the node), "fetch" (to sort on time spent copying data from the datablock), The default, if -sortMetric is omitted, is to sort on the first displayed column. Note that the sortMetric is independent of which columns are displayed via -show and -hide. Sort on a hidden column is allowed. The column selected by -sortMetric and -sortType specifies which total is returned by the dgtimer command on the MEL command line. This flag is also used with -updateHeatMap to specify which metric to build the heat map for.
        sortType | st: (create, query) - Used in conjunction with -query to specify which timer is to be sorted on when the per-node section of the output is generated, for example "self" time. Note that the -sortMetric flag can also be specified to define which metric is sorted on: for example "dgtimer -sortMetric draw -sortType count -query" will sort the output by the number of times each node was drawn. Both -sortMetric and -sortType are optional and you can specify one without the other. The -sortType flag can be specified at most once. The flag takes the following arguments: "self" (to sort on self time, which is the time specific to the node and not its children), "inclusive" (to sort on the time including children of the node), "count" (to sort on the number of times the node was invoked). and "none" (to sort on self time, but do not display the Percent and Cumulative columns in the per-node display, as well as cause the total number of nodes in Maya to be returned on the command line). The default, if -sortType is omitted, is to sort on self time. The column selected by -sortMetric and -sortType specifies which total is returned by the dgtimer command on the MEL command line. The global total as displayed in SECTION 1 of the listing is returned. The special case of "-sortType none" causes the number of nodes in Maya to instead be returned. This flag is also used with -updateHeatMap to specify which metric to build the heat map for.
        threshold | th: (query) - Truncates the display once the value falls below the threshold value. The threshold applies to whatever timer is being used for sorting. For example, if our sort key is self compute time (i.e. -sortMetric is "compute" and -sortType is "self") and the threshold parameter is 20.0, then only nodes with a compute self-time of 20.0 or higher will be displayed. (Note that -threshold uses absolute time. There are the similar -rangeUpper and -rangeLower parameters which specify a range using percentage).
        timerOff | off: (create, query) - Turns off node timing. By default, the timers on all nodes are turned off, but if specified with the -name or -type flags, only the timers on specified nodes are turned off. If the timers on all nodes become turned off, then global timing is also turned off as well.
        timerOn | on: (create, query) - Turns on node timing. By default, the timers on all nodes are turned on, but if specified with the -name or -type flags, only the timers on specified nodes are turned on. The global timers are also turned on by this command. Note that turning on timing does NOT reset the timers to zero. Use the -reset flag to reset the timers. The idea for NOT resetting the timers is to allow the user to arbitrarily turn timing on and off and continue to add to the existing timer values.
        trace | tr: (create) - Turns on or off detailed execution tracing. By default, tracing is off. If enabled, each timeable operation is logged when it starts and again when it ends. This flag can be used in conjunction with -outputFile to specify where the output is generated to. The following example shows how the output is formatted:  dgtimer:begin: compute 3 particleShape1Deformed particleShape1Deformed.lastPosition  The above is an example of the output when -trace is true that marks the start of an operation. For specific details on each field: the "dgtimer:begin:" string is an identifying marker to flag that this is a begin operation record. The second argument, "compute" in our example, is the operation metric. You can view the output of each given metric via "dgtimer -q" by specifying the -show flag. The integer which follows (3 in this case) is the depth in the operation stack, and the third argument is the name of the node (particleShape1Deformed). The fourth argument is specific to the metric. For "compute", it gives the name of the plug being computed. For "callback", its the internal Maya name of the callback. For "dirty", its the name of the plug that dirtiness is being propagated from.  dgtimer:end: compute 3 particleShape1Deformed 0.000305685 0.000305685  The above is the end operation record. The "compute", "3" and "particleShapeDeformed" arguments were described in the "dgtimer:begin" overview earlier. The two floating-point arguments are self time and inclusive time for the operation measured in seconds. The inclusive measure lists the total time since the matching "dgtimer:begin:" entry for this operation, while the self measure lists the inclusive time minus any time consumed by child operations which may have occurred during execution of the current operation. As noted elsewhere in this document, these two times are "wall clock times", measuring elapsed time including any time in which Maya was idle or performing system calls.  Since dgtimer can measure some non-node qualities in Maya, such as global message callbacks, a "-" is displayed where the node name would ordinarily be displayed. The "-" means "not applicable".
        type | t: (create, query) - Used in conjunction with -reset or -query to specify the type of the node(s) (e.g. animCurveTA) to reset or print timer values for. When querying, use of the -combineType flag will cause all nodes of the same type to be combined into one entry, and only one line of output is generated (i.e. the global timers and header information is omitted). Note: the -name and -type flag cannot be used together.
        uniqueName | un: (create, query) - Used to specify that the DAG nodes listed in the output should be listed by their unique names.  The full DAG path to the object will be printed out instead of just the node name.
        updateHeatMap | uhm: (create) - Forces Maya's heat map to rebuild based on the specified parameters. The heat map is an internal dgtimer structure used in mapping intensity values to colourmap entries during display by the HyperGraph Editor. There is one heat map shared by all editors that are using heat map display mode. Updating the heat map causes the timer values on all nodes to be analysed to compose the distribution of entries in the heat map. The parameter is the integer number of divisions in the map and should equal the number of available colours for displaying the heat map. This flag can be specified with the -rangeLower and -rangeUpper flags to limit the range of displayable to lie between the percentile range. The dgtimer command returns the maximum timing value for all nodes in Maya for the specified metric and type. Note: when the display range includes 0, the special zeroth (exactly zero) slot in the heat map is avilable.
    """
    ...


def dgValidateCurve(*args, allCurves: bool = ..., a: bool = ..., verbose: bool = ..., v: bool = ...) -> Any:
    r"""
    The dgValidateCurve command is used to make sure the curve internal
    status matches their actual state.
    It forces checks on curves that might not be tagged as static, even if they are.
    The DG tracks static curves in order to optimize evaluation by not
    considering them animated.  Once keys are added and modified on the
    curve, it is no longer static.  Certain operations on the curve might
    make it flat / without animation, but the DG will not treat it as
    static because it expects it to be modified again soon.
    This command allows to explicitly request checks for the static state
    of animation curves.

    Args:
        allCurves | a: (create) - Ignore the selected or specified objects and work on all curves.
        verbose | v: (create) - Prints out all of the curves set static or not.
    """
    ...


def dirmap(*args, convertDirectory: Optional[Union[str, bool]] = ..., cd: Optional[Union[str, bool]] = ..., enable: bool = ..., en: bool = ..., getAllMappings: bool = ..., gam: bool = ..., getMappedDirectory: Optional[Union[str, bool]] = ..., gmd: Optional[Union[str, bool]] = ..., mapDirectory: Optional[Union[Tuple[str, str], bool]] = ..., m: Optional[Union[Tuple[str, str], bool]] = ..., unmapDirectory: Optional[Union[str, bool]] = ..., um: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    Use this command to map a directory to another directory. The first
    argument is the directory to map, and the second is the destination
    directory to map to.
    
    Directories
    must both be absolute paths, and should be separated with forward
    slashes ('/'). The mapping is case-sensitive on all platforms.
    This command can be useful when moving projects to
    another machine where some textures may not be contained in the Maya
    project, or when a texture archive moves to a new location. This
    command is not necessary when moving a (self-contained) project from
    one machine to another - instead copy the entire project over and set
    the Maya project to the new location. 
    For one-time directory moves, if the command is enabled and the mapping
    configured correctly, when a scene is opened and saved the mapped
    locations will be reflected in the filenames saved with the file.
    To set up a permanent mapping the command should
    be enabled and the mappings set up in a script which is executed every
    time you launch Maya (userSetup.mel is sourced on startup).
    The directory mappings and enabled state are not preserved between
    Maya sessions.
    This command requires one "main" flag that specifies the action to take.
    Flags are:
    -[m|um|gmd|gam|cd|en]

    Args:
        convertDirectory | cd: (create) - Convert a file or directory. Returns the name of the mapped file or directory, if the command is enabled. If the given string contains one of the mapped directories, the return value will have that substring replaced with the mapped one. Otherwise the given argument string will be returned. If the command is disabled the given argument is always returned. Checks are not made for whether the file or directory exists. If the given string is a directory it should have a trailing '/'.
        enable | en: (create, query) - Enable directory mapping. Directory mapping is off when you start Maya. If enabled, when opening Maya scenes, file texture paths (and other file paths) will be converted when the scene is opened. The -cd flag only returns mapped directories when -enable is true. Query returns whether mapping has been enabled.
        getAllMappings | gam: (create) - Get all current mappings. Returns string array of current mappings in format: [redirect1, replacement1, ... redirectN, replacementN]
        getMappedDirectory | gmd: (create) - Get the mapped redirected directory. The given argument must exactly match the first string used with the -mapDirectory flag.
        mapDirectory | m: (create) - Map a directory - the first argument is mapped to the second. Neither directory needs to exist on the local machine at the time of invocation.
        unmapDirectory | um: (create) - Unmap a directory. The given argument must exactly match the argument used with the -mapDirectory flag.
    """
    ...


def diskCache(*args, append: bool = ..., a: bool = ..., cacheType: Optional[Union[str, bool]] = ..., ct: Optional[Union[str, bool]] = ..., close: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., closeAll: bool = ..., ca: bool = ..., delete: Optional[Union[str, bool]] = ..., d: Optional[Union[str, bool]] = ..., deleteAll: bool = ..., da: bool = ..., empty: Optional[Union[str, bool]] = ..., e: Optional[Union[str, bool]] = ..., emptyAll: bool = ..., ea: bool = ..., enabledCachesOnly: bool = ..., eco: bool = ..., endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., et: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., frameRangeType: Optional[Union[str, bool]] = ..., frt: Optional[Union[str, bool]] = ..., overSample: bool = ..., os: bool = ..., samplingRate: Optional[Union[int, bool]] = ..., sr: Optional[Union[int, bool]] = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., st: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., tempDir: bool = ..., tmp: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to create, clear, or close disk cache(s).

    Args:
        append | a: (create, query) - Append at the end and not to flush the existing cache
        cacheType | ct: (create, query) - Specifies the type of cache to overwrite.  "mcfp" for particle playback cache, "mcfi" for particle initial cache. "mcj" for jiggle cache. This option is only activated during the cache creation.
        close | c: (create, query) - Close the cache given the disk cache node name.  If -eco/enabledCachesOnly is "true" only enabled disk cache nodes are affected.
        closeAll | ca: (create, query) - Close all disk cache files. If -eco/enabledCachesOnly is "true" only enabled disk cache nodes are affected.
        delete | d: (create, query) - Delete the cache given the disk cache node name.  If -eco/enabledCachesOnly is "true" only enabled disk cache nodes are affected.
        deleteAll | da: (create, query) - Delete all disk cache files.  If -eco/enabledCachesOnly is "true" only enabled disk cache nodes are affected.
        empty | e: (create, query) - Clear the content of the disk cache with the given disk cache node name.  If -eco/enabledCachesOnly is "true" only enabled disk cache nodes are affected.
        emptyAll | ea: (create, query) - Clear the content of all disk caches.  If -eco/enabledCachesOnly is "true" only enabled disk cache nodes are affected.
        enabledCachesOnly | eco: (create, query) - When present, this flag restricts the -ea/emptyAll, so that only "enabled" disk caches (i.e., disk cache nodes with the ".enable" attribute set to "true") are affected.
        endTime | et: (create, query) - Specifies the end frame of the cache range.
        frameRangeType | frt: (create, query) - Specifies the type of frame range to use, namely "Render Globals", "Time Slider", and "Start/End".  In the case of "Time Slider", startFrame and endFrame need to be specified.  (This flag is now obsolete.  Please use the -startTime and -endTime flags to specify the frame range explicitly.)
        overSample | os: (create, query) - Over sample if true. Otherwise, under sample.
        samplingRate | sr: (create, query) - Specifies how frequently to sample relative to each frame. When over-sampling (-overSample has been specified), this parameter determines how many times per frame the runup will be evaluated. When under-sampling (the default, when -overSample has not been specified), the runup will evaluate only once per sr frames, where sr is the value specified to this flag.
        startTime | st: (create, query) - Specifies the start frame of the cache range.
        tempDir | tmp: (create, query) - Query-only flag for the location of temporary diskCache files.
    """
    ...


def displayString(*args, delete: bool = ..., d: bool = ..., exists: bool = ..., ex: bool = ..., keys: bool = ..., k: bool = ..., replace: bool = ..., r: bool = ..., value: Optional[Union[str, bool]] = ..., v: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    Assign a string value to a string identifier. Allows you define a string in
    one location and then refer to it by its identifier in many other locations.
    Formatted strings are also supported (NOTE however, this functionality is now
    provided in a more general fashion by the format command, use of format
    is recommended). You may embed up to 3 special character sequences
    ^1s, ^2s, and ^3s to perform automatic string replacement. The
    embedded characters will be replaced with the extra command arguments. See
    example section for more detail. Note the extra command arguments do not need
    to be display string identifiers.

    Args:
        delete | d: (create) - This flag is used to remove an identifer string. The command will fail if the identifier does not exist.
        exists | ex: (create) - Returns true or false depending upon whether the specified identifier exists.
        keys | k: (create, query) - List all displayString keys that match the identifier string. The identifier string may be a whole or partial key string. The command will return a list of all identifier keys that contain this identifier string as a substring.
        replace | r: (create, query) - Since a displayString command will fail if it tries to assign a new value to an existing identifer, this flag is required to allow updates to the value of an already-existing identifier.  If the identifier does not already exist, a new identifier is added as if the -replace flag were not present.
        value | v: (create, query) - The display string\'s value. If you do not specify this flag when creating a display string then the value will be the same as the identifier.
    """
    ...


def dynamicLoad(*args, query: bool = ...) -> Any:
    r"""
    Dynamically load the DLL passed as argument.

    Args:
    """
    ...


def error(*args, noContext: bool = ..., n: bool = ..., showLineNumber: bool = ..., sl: bool = ...) -> Any:
    r"""
    The error command is provided so that the user can issue
    error messages from his/her scripts and
    control execution in the event of runtime errors.
    
    
    The string argument is displayed in the command window
    (or stdout if running in batch mode) after
    being prefixed with an error message heading and
    surrounded by //.
    
    
    The error command also causes execution to terminate with an error.
    Using error is like raising an exception because the error will
    propagate up through the call chain. You can use catch to
    handle the error from the caller side. If you don't want
    execution to end, then you probably want to use the warning
    command instead.

    Args:
        noContext | n: (create) - Do not include the context information with the error message.
        showLineNumber | sl: (create) - Obsolete. Will be deleted in the next version of Maya. Use the checkbox in the script editor that enables line number display instead.
    """
    ...


def exportEdits(*args, excludeHierarchy: bool = ..., ehr: bool = ..., excludeNode: Optional[Union[str, bool]] = ..., en: Optional[Union[str, bool]] = ..., exportSelected: bool = ..., exs: bool = ..., force: bool = ..., f: bool = ..., includeAnimation: bool = ..., ian: bool = ..., includeConstraints: bool = ..., ic: bool = ..., includeDeformers: bool = ..., idf: bool = ..., includeNetwork: bool = ..., inw: bool = ..., includeNode: Optional[Union[str, bool]] = ..., includeSetAttrs: bool = ..., isa: bool = ..., includeSetDrivenKeys: bool = ..., sdk: bool = ..., includeShaders: bool = ..., ish: bool = ..., selected: bool = ..., sel: bool = ..., type: Optional[Union[str, bool]] = ..., typ: Optional[Union[str, bool]] = ..., editCommand: Optional[Union[str, bool]] = ..., ec: Optional[Union[str, bool]] = ..., onReferenceNode: Optional[Union[str, bool]] = ..., orn: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    Use this command to export edits made in the scene to a file.
    The exported file can be subsequently imported to another scene.
    Edits may include: nodes, connections and reference edits such as value changes.
    The nodes that are included in the exported file will be based on the
    options used.
    At least one option flag that describes the set of target nodes to include in the
    exported file must be specified (e.g. 'selected', 'onReferenceNode').
    Use the inclusion flags ('includeAnimation', 'includeShaders', 'includeNetwork') to
    specify which additional related nodes will be added to the export list.
    In export mode, when the command completes successfully, the name of the exported file will
    be returned.
    In query mode, this command will return information about the contents of the exported
    file.
    The query mode will return the list of nodes that will be considered for
    inclusion in the exported file based on the specified flags.

    Args:
        excludeHierarchy | ehr: (create, query) - By default, all DAG parents and DAG history are written to the export file. To prevent any DAG relations not otherwise connected to the target nodes to be included, specify the -excludeHierarchy flag.
        excludeNode | en: (create, multiuse, query) - Prevent the node from being included in the list of nodes being exported. This flag is useful to exclude specific scene nodes that might otherwise be exported. In the case where more than one Maya node has the same name, the DAG path can be specified to uniquely identify the node.
        exportSelected | exs: (create, query) - The selected nodes and their connections to each other will be exported. Additionally, any dangling connections to non-exported nodes will be exported. Default nodes are ignored and never exported. Note that when using the exportSelected flag, only selected nodes are exported, and -include/-exclude flags such as -includeHierarchy are ignored.
        force | f: (create, query) - Force the export action to take place. This flag is required to overwrite an existing file.
        includeAnimation | ian: (create, query) - Additionally include animation nodes and animation helper nodes associated with the target nodes being exported.
        includeConstraints | ic: (create, query) - Additionally include constraint-related nodes associated with the target nodes being exported.
        includeDeformers | idf: (create, query) - Additionally include deformer networks associated with the target nodes being exported.
        includeNetwork | inw: (create, query) - Additionally include the network of nodes connected to the target nodes being exported.
        includeNode | includeNode: (create, multiuse, query) - Additionally include the named node in the list of nodes being exported. In the case where more than one Maya node has the same name, the DAG path can be specified to uniquely identify the node.
        includeSetAttrs | isa: (create, query) - When using the -selected/-sel flag, if any of the selected nodes are referenced, also include/exclude any setAttr edits on those nodes. If used with the -onReferenceNode/-orn flag, include/exclude any setAttr edits on the reference.
        includeSetDrivenKeys | sdk: (create, query) - Additionally include setDrivenKey-related nodes associated with the target nodes being exported.
        includeShaders | ish: (create, query) - Additionally include shaders associated with the target nodes being exported.
        selected | sel: (create, query) - Export will operate on the list of nodes currently selected. This flag differs from the exportSelected flag in that the selected nodes are not exported, only the edits on them, and any nodes found via the include flags that are used (such as includeAnimation, includeNetwork and so on).
        type | typ: (create, query) - Set the type of the exported file. Valid values are "editMA" or "editMB". Note that this command respects the global "defaultExtensions" setting for file naming that is controlled with the file command defaultExtensions option.  See the file command for more information.
        editCommand | ec: (create, multiuse, query) - This is a secondary flag used to indicate which type of reference edits should be considered by the command. If this flag is not specified all edit types will be included. This flag requires a string parameter. Valid values are: "addAttr", "connectAttr", "deleteAttr", "disconnectAttr", "parent", "setAttr", "lock" and "unlock". In some contexts, this flag may be specified more than once to specify multiple edit types to consider.
        onReferenceNode | orn: (create, multiuse, query) - This is a secondary flag used to indicate that only those edits which are stored on the indicated reference node should be considered. This flag only supports multiple uses when specified with the "exportEdits" command.
    """
    ...


def fcheck(*args) -> Any:
    r"""
    Invokes the fcheck program to display images in a separate window.

    Args:
    """
    ...


def file(*args, absoluteName: bool = ..., an: bool = ..., activate: bool = ..., a: bool = ..., activeProxy: bool = ..., ap: bool = ..., add: bool = ..., anyModified: bool = ..., amf: bool = ..., applyTo: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., buildLoadSettings: bool = ..., bls: bool = ..., channels: bool = ..., chn: bool = ..., cleanReference: Optional[Union[str, bool]] = ..., cr: Optional[Union[str, bool]] = ..., command: Optional[Union[Tuple[str, str], bool]] = ..., c: Optional[Union[Tuple[str, str], bool]] = ..., compress: bool = ..., cmp: bool = ..., constraints: bool = ..., con: bool = ..., constructionHistory: bool = ..., ch: bool = ..., copyNumberList: bool = ..., cnl: bool = ..., defaultExtensions: bool = ..., de: bool = ..., defaultNamespace: bool = ..., dns: bool = ..., deferReference: bool = ..., dr: bool = ..., editCommand: Optional[Union[str, bool]] = ..., ec: Optional[Union[str, bool]] = ..., errorStatus: bool = ..., err: bool = ..., executeScriptNodes: bool = ..., esn: bool = ..., exists: bool = ..., ex: bool = ..., expandName: bool = ..., exn: bool = ..., exportAll: bool = ..., ea: bool = ..., exportAnim: bool = ..., ean: bool = ..., exportAnimFromReference: bool = ..., ear: bool = ..., exportAsReference: bool = ..., er: bool = ..., exportAsSegment: bool = ..., exs: bool = ..., exportSelected: bool = ..., es: bool = ..., exportSelectedAnim: bool = ..., eas: bool = ..., exportSelectedAnimFromReference: bool = ..., esa: bool = ..., exportSelectedNoReference: bool = ..., esr: bool = ..., exportSelectedStrict: bool = ..., ess: bool = ..., exportSnapshotCallback: Optional[Union[Tuple[str, str], bool]] = ..., esc: Optional[Union[Tuple[str, str], bool]] = ..., exportUnloadedReferences: bool = ..., eur: bool = ..., expressions: bool = ..., exp: bool = ..., fileMetaData: bool = ..., fmd: bool = ..., flushReference: Optional[Union[str, bool]] = ..., fr: Optional[Union[str, bool]] = ..., force: bool = ..., f: bool = ..., groupLocator: bool = ..., gl: bool = ..., groupName: Optional[Union[str, bool]] = ..., gn: Optional[Union[str, bool]] = ..., groupReference: bool = ..., gr: bool = ..., ignoreVersion: bool = ..., iv: bool = ..., i: bool = ..., importFrameRate: bool = ..., ifr: bool = ..., importReference: bool = ..., ir: bool = ..., importTimeRange: Optional[Union[str, bool]] = ..., itr: Optional[Union[str, bool]] = ..., lastFileOption: bool = ..., lfo: bool = ..., lastTempFile: bool = ..., ltf: bool = ..., list: bool = ..., l: bool = ..., loadAllDeferred: bool = ..., lad: bool = ..., loadAllReferences: bool = ..., lar: bool = ..., loadNoReferences: bool = ..., lnr: bool = ..., loadReference: Optional[Union[str, bool]] = ..., lr: Optional[Union[str, bool]] = ..., loadReferenceDepth: Optional[Union[str, bool]] = ..., lrd: Optional[Union[str, bool]] = ..., loadReferencePreview: Optional[Union[str, bool]] = ..., lrp: Optional[Union[str, bool]] = ..., loadSettings: Optional[Union[str, bool]] = ..., ls: Optional[Union[str, bool]] = ..., location: bool = ..., loc: bool = ..., lockContainerUnpublished: bool = ..., lcu: bool = ..., lockFile: bool = ..., lf: bool = ..., lockReference: bool = ..., lck: bool = ..., mapPlaceHolderNamespace: Optional[Union[Tuple[str, str], bool]] = ..., mns: Optional[Union[Tuple[str, str], bool]] = ..., mergeBaseAnimLayer: bool = ..., mbl: bool = ..., mergeNamespaceWithParent: bool = ..., mnp: bool = ..., mergeNamespaceWithRoot: bool = ..., mnr: bool = ..., mergeNamespacesOnClash: bool = ..., mnc: bool = ..., modified: bool = ..., mf: bool = ..., moveSelected: bool = ..., ms: bool = ..., namespace: str = ..., ns: str = ..., newFile: bool = ..., new: bool = ..., open: bool = ..., o: bool = ..., options: Optional[Union[str, bool]] = ..., op: Optional[Union[str, bool]] = ..., parentNamespace: bool = ..., pns: bool = ..., postSaveScript: Optional[Union[str, bool]] = ..., pos: Optional[Union[str, bool]] = ..., preSaveScript: Optional[Union[str, bool]] = ..., prs: Optional[Union[str, bool]] = ..., preserveName: bool = ..., pn: bool = ..., preserveReferences: bool = ..., pr: bool = ..., preview: bool = ..., pv: bool = ..., prompt: bool = ..., pmt: bool = ..., proxyManager: Optional[Union[str, bool]] = ..., pm: Optional[Union[str, bool]] = ..., proxyTag: Optional[Union[str, bool]] = ..., pt: Optional[Union[str, bool]] = ..., reference: bool = ..., r: bool = ..., referenceDepthInfo: Optional[Union[int, bool]] = ..., rdi: Optional[Union[int, bool]] = ..., referenceNode: Optional[Union[str, bool]] = ..., rfn: Optional[Union[str, bool]] = ..., relativeNamespace: Optional[Union[str, bool]] = ..., rns: Optional[Union[str, bool]] = ..., removeDuplicateNetworks: bool = ..., rdn: bool = ..., removeReference: bool = ..., rr: bool = ..., rename: Optional[Union[str, bool]] = ..., rn: Optional[Union[str, bool]] = ..., renameAll: bool = ..., ra: bool = ..., renameToSave: bool = ..., rts: bool = ..., renamingPrefix: Optional[Union[str, bool]] = ..., rpr: Optional[Union[str, bool]] = ..., renamingPrefixList: bool = ..., rpl: bool = ..., replaceName: Optional[Union[Tuple[str, str], bool]] = ..., rep: Optional[Union[Tuple[str, str], bool]] = ..., reserveNamespaces: bool = ..., rvn: bool = ..., resetError: bool = ..., rer: bool = ..., returnNewNodes: bool = ..., rnn: bool = ..., save: bool = ..., s: bool = ..., saveDiskCache: Optional[Union[str, bool]] = ..., sdc: Optional[Union[str, bool]] = ..., saveReference: bool = ..., sr: bool = ..., saveReferencesUnloaded: bool = ..., sru: bool = ..., saveTextures: Optional[Union[str, bool]] = ..., stx: Optional[Union[str, bool]] = ..., sceneName: bool = ..., sn: bool = ..., segment: str = ..., seg: str = ..., selectAll: bool = ..., sa: bool = ..., shader: bool = ..., sh: bool = ..., sharedNodes: Optional[Union[str, bool]] = ..., shd: Optional[Union[str, bool]] = ..., sharedReferenceFile: bool = ..., srf: bool = ..., shortName: bool = ..., shn: bool = ..., strict: bool = ..., str: bool = ..., swapNamespace: Optional[Union[Tuple[str, str], bool]] = ..., sns: Optional[Union[Tuple[str, str], bool]] = ..., type: Optional[Union[str, bool]] = ..., typ: Optional[Union[str, bool]] = ..., uiConfiguration: bool = ..., uc: bool = ..., uiLoadConfiguration: bool = ..., ulc: bool = ..., unloadReference: Optional[Union[str, bool]] = ..., ur: Optional[Union[str, bool]] = ..., unresolvedName: bool = ..., un: bool = ..., usingNamespaces: bool = ..., uns: bool = ..., withoutCopyNumber: bool = ..., wcn: bool = ..., writable: bool = ..., w: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Opening, importing, exporting, referencing, saving, or renaming a
    file
    
    
    This command needs a single main flag that specifies the action to take.
    Some of the main flags also take optional secondary flags to modify
    that action.
    
    
    
    The main flags are:
    
    cr ea
    ean ear eas
    er esa es
    
    
    esn ex
    fr i ir
    l lr lrp
    
    
    loc ltf
    mf new o
    op ot pmt
    
    
    r rdi
    rn rr rts
    s sa sdx
    
    
    st stx
    typ uc ur
    w
    
    
    
    
    
    o/open can be modified by the following secondary flags:
    
    f lad
    lad lnr rnn
    
    
    
    
    
    es/exportSelected can be modified by the following
    secondary flags:
    
    ch chn
    con exp sh
    
    
    
    
    
    r/reference can be modified by the following secondary
    flags:
    
    dns dr
    gr gl gn
    mnc
    ns rfn rpr
    sns srf shd
    rnn
    
    
    
    
    
    i/import can be modified by the following secondary
    flags:
    
    dns dr
    gr gn
    mnc
    pr
    ra rdn rnn
    rpr sns
    
    
    
    
    
    n/new and s/save can be modified by the following
    secondary flags:
    
    f
    
    
    
    
    
    er/exportAsReference can be modified by the following
    secondary flags:
    
    ns rpr
    
    
    
    
    
    ea/exportAll and es/exportSelected can be modified by
    the following secondary flags:
    
    f pr
    
    
    
    
    
    ean/exportAnim,  eas/exportSelectedAnim
    can be modified by the following secondary flags:
    
    f
    
    
    
    
    
    ear/exportAnimFromReference, esa/exportSelectedAnimFromReference
    can be modified by the following secondary flags:
    
    f rfn
    
    
    
    
    Querying information about a file
    
    
    This command needs a single main query flag that specifies the query to take
    and then optional secondary flags to modify that query.
    
    
    
    The main query flags are:
    
    amf ch
    chn con dr
    err ex exn
    
    
    exp l
    loc ltf mf
    ns op ot
    
    
    pmt pns
    r rfn rpl
    rpr rts sdc
    
    
    sh sn
    stx typ uc
    w
    
    
    
    
    
    dr/deferReference can be modified by the following
    secondary flags:
    
    rfn
    
    
    
    
    
    exn/expandName, l/list, r/reference, sn/sceneName can
    be modified by the following secondary flags:
    
    un shn
    wcn
    
    
    
    Querying file names
    
    
    When querying a file name there are a number of ways to format the result:
    
    Resolved vs. unresolved name:
    When a file is loaded into Maya (e.g., by opening or referencing it),
    the file path provided may not be complete. It could, for example, be
    a relative path (ex: "scenes/myScene.ma"), it could contain environment
    variables (ex: "$PRODUCTION_DIR/myScene.ma"), and it could even be a path
    which simply doesn't exist on the local disk. In each of these cases Maya
    goes through a number of steps to resolve the path and find the file on disk.
    By default the 'file' command will return the resolved file name (i.e., the
    location from which Maya is actually reading the file), but if the
    un/unresolved flag is used, the unresolved file (e.g., the one that
    was originally specified) will be returned. When providing a file path with
    an environment variable; for example, when using the -rename flag, the
    environment variable should be set to a relative path ( such as "/scenes/scenesSetA"; ).
    Providing a path using an environment variable that is set to an absolute path
    ( for example, "C:/scenes/" ) is not supported.
    
    Full vs. short name:
    By default the 'file' command will return the full
    path to a file, but if the shn/shortName flag is used just the
    file name will be returned.
    
    With vs. without copy number:
    When the same file is loaded into Maya more
    than once (for example by referencing the same file twice), Maya
    distinguishes between the various copies by appending a copy number to the
    end of the file name. The first time the file is loaded, no copy number is
    appended. The second time the file is loaded a "{1}" is appended, the third
    time a "{2}" is used, and so on. By default the 'file' command will return
    the file name with the copy number appended, but if the
    wcn/withoutCopyNumber flag is used the file name will be returned
    without the copy number.
    
    Additional Details
    
    The file command usually expects a file name as its argument, if none
    is specified then the root scene is used.
    See the individual flag descriptions for details and limitations.

    Args:
        absoluteName | an: (create, query) - This is a general flag which can be used to specify the desired format for the namespace(s) returned by the command. The absolute name of the namespace is a full namespace path, starting from the root namespace ":" and including all parent namespaces.  For example ":ns:ball" is an absolute namespace name while "ns:ball" is not.
        activate | a: () - This flag is obsolete.
        activeProxy | ap: (create) - This flag is intended for internal use by Maya during file referencing. It specifes which file is the active proxy when the file is loaded when used with the reference flag. It is also used to specify which file is the active proxy in the file referencing preload information when used with the referenceDepthInfo flag.
        add | add: (create) - When used with selectAll it indicates that the specified items should be added to the active list without removing existing items from the active list.
        anyModified | amf: (query) - This flag is obsolete. Please use file -q -modified instead.
        applyTo | at: (create) - When importing or referencing an offline edit file, apply it to to the given reference (i.e., determine what <main> gets mapped to). Specify the reference node name as argument. To apply the edits to nodes in the main scene (i.e., the root namespace), pass in ":". To collapse <main> (i.e., map it to "None"), pass in "". May only be used with the file -i/import or -r/reference flags.
        buildLoadSettings | bls: (create) - When used with the "o/open" flag it indicates that the specified file should be read for reference hierarchy information only. This information will be stored in temporary load settings under the name "implicitLoadSettings". When this flag is used the specified scene file will not be loaded: no objects/nodes will be created or modified. Note: most users will not need to use this flag or the "implicitLoadSettings" it builds. They can access the same functionality by setting the "Selective Load" option in the File > Open Option Box.
        channels | chn: (create, query) - For use with exportSelected to specify whether attached channels should be included in the export.
        cleanReference | cr: (create) - Remove edits from the passed in reference node. The reference must be in an unloaded state. To remove a particular type of edit, use the editCommand flag. If no flag is specified, all edits will be removed.
        command | c: (create, query) - Specifies the callback to execute before any file operation. This is an internal flag used only in the file format.
        compress | cmp: (create) - When used with save, it will compress (gzip) the file on output.
        constraints | con: (create, query) - For use with exportSelected to specify whether attached constraints should be included in the export.
        constructionHistory | ch: (create, query) - For use with exportSelected to specify whether attached construction history should be included in the export.
        copyNumberList | cnl: (query) - When queried, this flag returns a string array containing a number that uniquely identifies each instance the file is used.
        defaultExtensions | de: (create, query) - Use the default extensions to rename the files. This defaults to true, but is a persistent setting within a given session of Maya, meaning that if you set it to true or false, that value will continue to be used in subsequent file commands until a new value is set.
        defaultNamespace | dns: (create) - Use the default name space for import and referencing.  This is an advanced option.  If set, then on import or reference, Maya will attempt to place all nodes from the imported or referenced file directly into the root (default) name space, without invoking any name clash resolution algorithms.  If the names of any of the new objects    already exist in the root namespace, then errors will result. The user of this flag is responsible for creating a name clash resolution mechanism outside of Maya to avoid such errors. Note: This flag    is intended only for use with custom file translators written through    the API. Use at your own risk.
        deferReference | dr: (create, query) - When used in conjunction with the -reference flag, this flag determines if the reference is loaded, or if loading is deferred. C: The default is false. Q: When queried, this flag returns true if the reference is deferred, or false if the reference is not deferred. If this is used with -rfn/referenceNode, the -rfn flag must come before -q.
        editCommand | ec: (create) - For use with cleanReference. Remove only this type of edit. Supported edits are: setAttr addAttr deleteAttr connectAttr disconnectAttr and parent
        errorStatus | err: (query) - Query the error status of the last file read. Returns true if and error occurred during the last file read.
        executeScriptNodes | esn: (create) - If true, allow the appropriate script nodes to execute. If false, do not allow any script node scripts to run. For more information, see the documentation for script nodes. Default: true.
        exists | ex: (query) - Query if the file exists. Returns true if the file exists.
        expandName | exn: (query) - This is a query only flag that can be used to query for the file path name of the file.
        exportAll | ea: (create) - Export everything into a single file. Returns the name of the exported file.
        exportAnim | ean: (create) - Export all animation nodes and animation helper nodes from all objects in the scene. The resulting animation export file will contain connections to objects that are not included in the animation file. As a result, importing/referencing this file back in will require objects of the same name to be present, else errors will occur. The -sns/swapNamespace flag is available for swapping the namespaces of given objects to another namespace. This use of namespaces can be used to re-purpose the animation file to multiple targets using a consistent naming scheme.  The exportAnim flag will not export animation layers. For generalized file export of animLayers and other types of nodes, refer to the exportEdits command. Or use the Export Layers functionality.
        exportAnimFromReference | ear: (create) - Export the main scene animation nodes and animation helper nodes from all referenced objects. This flag, when used in conjunction with the -rfn/referenceNode flag, can be constrained to only export animation nodes from the specified reference file. See -ean/exportAnim flag description for details on usage of animation files.
        exportAsReference | er: (create) - Export the selected objects into a reference file with the given name. The file is saved on disk during the process. Returns the name of the reference created.
        exportAsSegment | exs: () - This flag is obsolete.
        exportSelected | es: (create) - Export the selected items into the specified file. Returns the name of the exported file.
        exportSelectedAnim | eas: (create) - Export all animation nodes and animation helper nodes from the selected objects in the scene. See -ean/exportAnim flag description for details on usage of animation files.
        exportSelectedAnimFromReference | esa: (create) - Export the main scene animation nodes and animation helper nodes from the selected referenced objects. This flag, when used in conjunction with the -rfn/referenceNode flag, can be constrained to only export animation nodes from the selected nodes of a specified reference file. See -ean/exportAnim flag description for details on usage of animation files.
        exportSelectedNoReference | esr: () - This flag is obsolete.
        exportSelectedStrict | ess: (create) - Export the selected items into the specified file. This flag differs from exportSelected in that it will only export the nodes that are explicitly on the selection list. Related nodes (both history and DAG related) are not automatically exported unless those nodes are also on the selection list. Node relationships are only preserved if both nodes in the relationship (parent/child, source/destination) are exported. It is important to note that there is potential for scene data loss in the exported scene since not all related nodes are not exported by default. The user is responsible for selecting all relevant nodes before exporting. Returns the name of the exported file.
        exportSnapshotCallback | esc: (create) - When specified alongside -ea/exportAll, es/exportSelected and -ess/exportSelectedStrict, this flag enables Maya to temporarily duplicate the export targets into a specified namespace and invoke a callback to interact with the duplicate export targets before writing the duplicate export targets to disk. Once written to disk, the duplicate export targets, new nodes created by the callback and temporary namespace are removed from the scene. Implicitly created nodes (eg. persp, top, etc.) are not duplicated.  For the duration of the callback: 1. The specified namespace will be made current. 2. All nodes added by the callback are tracked as a temporary export target. 3. Although the intent of the callback is to only operate on the duplicate export targets, there is nothing limiting the callback from modifying the main scene. Thus, the callback should be written with care.  This flag accepts two arguments: a. [string] Callback to invoke prior to write to disk. b. [string] Temporary namespace to store duplicate export targets.  This flag can only be used in conjunction with -ea/exportAll, -es/exportSelected and -ess/exportSelectedStrict.  Note that the -pv/preview flag still only previews the contents of the export targets _prior_ to the snapshot duplication. It does not preview the final output after the callback.  Referenced nodes are duplicated in the same manner as duplicating those nodes manually in the scene. Similarly, scene assembly nodes will duplicate as they would if manually duplicated, however scene assembly nodes have special duplication behavior, so the callback should be aware of these differences when anticipating the duplicate export targets.
        exportUnloadedReferences | eur: (create) - Only effective when preserveReferences is used. When used with the exportAll flag, tells the exporter to include all unloaded references in the export. When used with the exportSelected flag, tells the exporter to include all unloaded proxy references that are related to any node in the selection.
        expressions | exp: (create, query) - For use with exportSelected to specify whether attached expressions should be included in the export.
        fileMetaData | fmd: (query) - This is a query only flag to get the file metadata for audio files. It returns the referenceTime. This field is only extracted from BWAVE files, for other files it returns 0
        flushReference | fr: (create) - This flag will unload the reference file associated with the passed reference node, retaining all associated reference nodes and scene files. ** This option only works when using namespaces **. More Details: This flag is primarily intended to be used as part of a custom asset management system. It can be used to defer loading of a reference which contains child references without losing information about those child references. Prior to reloading a flushed    reference which contains child references, the 'createNode reference' lines should be manually removed from the children's Maya ASCII files. If this is not done, extra reference nodes will be created.
        force | f: (create) - Force an action to take place. (new, open, save, remove reference, unload reference) Used with removeReference to force remove reference namespace even if it has contents. Cannot be used with removeReference if the reference resides in the root namespace. Used with unloadReference to force unload reference even if the reference node is locked, without prompting a dialog that warns user about the lost of edits.
        groupLocator | gl: (create) - Used only with the -r and the -gr flag. Used to group the output of groupReference under a locator
        groupName | gn: (create) - Used only with the -gr flag. Optionally used to set the name of the transform node that the imported/referenced items will be grouped under.
        groupReference | gr: (create) - Used only with the -r or the -i flag. Used to group all the imported/referenced items under a single transform.
        ignoreVersion | iv: (create) - Used to open files with versions other than those officially supported. Success is not guaranteed. Data loss, data corruption or failure to open are all possible outcomes. Can only be used with the -o and -i flags.
        i | i: (create) - Import the specified file. Returns the name of the imported file.
        importFrameRate | ifr: (create) - Used only with the -i flag. Used to import the frame rate and set it as Maya's frame rate.
        importReference | ir: (create) - Remove the encapsulation of the reference around the data within the specified file.    This makes the contents of the specified file part of the current scene and all references to the original file are lost. Returns the name of the reference that was imported.
        importTimeRange | itr: (create) - Used only with the -i flag. Used to import the time range and apply it to Maya's playback range in one of three different ways as specified by the string.  The valid strings are "keep", which keeps Maya's playback range untouched, "override", which overrides Maya's playback range with the imported range, and "combine", which extends Maya's playback range to encompass the imported range.
        lastFileOption | lfo: (query) - On query, returns the last option string used by the file command.
        lastTempFile | ltf: (query) - When queried, this flag returns the temp file name used during file save. The temp file will be left in the same directory as the intended file name if the save fails.
        list | l: (query) - List all files. Returns a string array of the names of all segment/reference files. Duplicates will be removed. So if a file is referenced more than once, and the -withoutCopyNumber flag is set, it will only be listed once. in the scene.
        loadAllDeferred | lad: (create) - This flag is obsolete, and has been replaced by the loadReferenceDepth flag. When used with the -open flag, determines if the -deferReference flag is respected when reading in the file. If true is passed, all of the references are loaded. If false is passed, the -deferReference flag is respected.
        loadAllReferences | lar: (create) - This flag is obsolete and has been replaced with the loadReferenceDepth flag. When used with the -open flag, this will cause all references to be loaded.
        loadNoReferences | lnr: (create) - This flag is obsolete and has been replaced witht the loadReferenceDepth flag. When used with the -open flag, no references will be loaded. When used with -i/import, -r/reference or -lr/loadReference flags, will load the top-most reference only.
        loadReference | lr: (create, query) - This flag loads a file and associates it with the passed reference node. If the reference node does not exist, the command will fail. If the file is already loaded, then this flag will reload the same file. If a file is not given, the command will load (or reload) the last used reference file.
        loadReferenceDepth | lrd: (create) - Used to specify which references should be loaded. Valid types are "all", "none" and "topOnly", which will load all references, no references and top-level references only, respectively. May only be used with the -o/open, -i/import, -r/reference or -lr/loadReference flags. When "none" is used with -lr/loadReference, only path validation is performed. This can be used to replace a reference without triggering reload. Not using loadReferenceDepth will load references in the same loaded or unloaded state that they were in when the file was saved. Additionally, the -lr/loadReference flag supports a fourth type, "asPrefs". This will force any nested references to be loaded according to the state (if any) stored in the current scene file, rather than according to the state saved in the reference file itself.
        loadReferencePreview | lrp: (create) - This flag will perform a special preview-only load of a reference file. A preview-only reference file is not completely loaded, but instead is partially loaded so that certain information, such as nested references it contains, can be determined. Nested references that are previewed remain in a special preview-only state.
        loadSettings | ls: (create) - When used with the "o/open" flag this flag specifies which reference load settings should be used. Reference load settings specify which references should be brought in loaded and which unloaded. Those reference files that are brought in unloaded will usually not need to be read and interpreted by Maya. This can potentially reduce the time it takes Maya to load the whole scene. If no "ls/loadSettings" flag is specified, or the empty string ("") is used as the flag argument, the default load settings are used. The default load settings represent the state of all references when the file was last saved. The load settings "implicitLoadSettings" refer to the temporary load settings generated by the "bls/buildLoadSettings" flag and edited with the "loadSettings" command. Currently on the default and implicit load settings are supported.
        location | loc: (query) - Query the location of the given file name.
        lockContainerUnpublished | lcu: (create) - Set the unpublised lock state for all containers in this file. This will not lock the attributes in the main scene directly, but any file that references this scene will have all its containers come in as unpublished locked.
        lockFile | lf: (create) - Lock or unlock the main scene. Any file referencing this scene will automatically lock all attributes and nodes. Also prevents reference edits from being saved to it from a parent file.
        lockReference | lck: (create) - Locks attributes and nodes from the referenced file.
        mapPlaceHolderNamespace | mns: (create, edit, multiuse, query) - Map a placeHolderNamespace to the given reference. Must be used with the file -i/import, -r/reference flags in create mode. The first string is the place holder namespace, including the angle brackets (ex: "<foo>"). The second string is the reference node whose namespace it should be mapped to (ex: "refRN"). If the namespace should be mapped to the root namespace, use ":". To collapse the namespace (i.e., map it to "None"), use "". When queried, namespaces that are mapped to "None" will return "(None)" for clarity.
        mergeBaseAnimLayer | mbl: (create) - When set, Maya will merge the base animation layer imported from the file with the base layer already existing in the scene.
        mergeNamespaceWithParent | mnp: (create) - Used with the removeReference flag. When removing a file reference and its namespace, move the rest of the namespace content to parent namespace. Cannot be used if the reference resides in the root namespace.
        mergeNamespaceWithRoot | mnr: (create) - Used with the removeReference flag. When removing a file reference and its namespace, move the rest of the namespace content to root namespace. Cannot be used if the reference resides in the root namespace.
        mergeNamespacesOnClash | mnc: (create) - Used with the import, reference or edit flags, this option will prevent new namespaces from being created when namespaces of the same name already exist within Maya. The default value is false. For example, if an object "pSphere1", which is being imported, refers to the namespace "ref" and there is already a namespace called "ref" defined in Maya. If mergeNamespacesOnClash is true, the existing "ref" namespace will be reused and pSphere1 will be moved into the existing namespace; and if the namespace has another object which is also named "pSphere1", then the imported one will be renamed with an incremental number("pSphere2"). On the other hand, if mergeNamespacesOnClash is false, a new namespace will be created with an incremental number (in first case is "ref1") and pSphere1 will be moved into the "ref1" namespace. This flag also support nested namespace, for example, if an object "pSphere1" which is imported and refers to namespace "ref:foo" and mergeNamespacesOnClash is true this time, then the existing "ref:foo" will be reused and the object will be moved into "ref:foo". Also if mergeNamespacesOnClash is false, then a new namespace "ref:foo1" will be created and "pSphere1" will be moved into that new namespace.
        modified | mf: (create, query) - Set the modified state of the entire scene. If the scene is modified it will need to be saved before a new file is opened or created. Normally there is no need to edit this flag as the state of the file is updated automatically whenever an object is created or modified. If editing of the state is desired, it is done without use of the edit flag as covered in the example section below. In query mode, if the scene has been modified 1 is returned. Otherwise 0 is returned.
        moveSelected | ms: (edit) - This flag is obsolete.
        namespace | ns: (edit) - The namespace name to use that will group all objects during importing and referencing. Change the namespace used to group all the objects from the specified referenced file. The reference must have been created with the "Using Namespaces" option, and must be loaded. Non-referenced nodes contained in the existing namespace will also be moved to the new namespace. The new namespace will be created by this command and can not already exist. The old namespace will be removed.
        newFile | new: (create) - Initialize the scene. Returns untitled scene with default location.
        open | o: (create) - Open the specified file. Returns the name of the opened file.
        options | op: (create, query) - Set/query the currently set file options. file options are used while saving a maya file. Two file option flags supported in current file command are v and p.  v(verbose) indicates whether long or short attribute names and command flags names are used when saving the file. Used by both maya ascii and maya binary file formats. It only can be 0 or 1. Setting v=1 indicates that long attribute names and command flag names will be used. By default, or by setting v=0, short attribute names will be used.   p(precision) defines the maya file IO's precision when saving the file. Only used by maya ascii file format. It is an integer value. The default value is 17.  The option format is "flag1=XXX;flag2=XXX".Maya uses the last v and p as the final result. Note: 1. Use a semicolon(";") to separate several flags. 2. No blank space(" ") in option string.
        parentNamespace | pns: (query) - Returns the name(s) of a referenced file's parent namespaces.
        postSaveScript | pos: (create) - When used with the save flag, the specified script will be executed after the file is saved.
        preSaveScript | prs: (create) - When used with the save flag, the specified script will be executed before the file is saved.
        preserveName | pn: (create) - When used with compress, it will retain the regular extension rather than appending .gz.
        preserveReferences | pr: (create) - Modifies the various import/export flags such that references are imported/exported as actual references rather than copies of those references.
        preview | pv: (create) - Used in conjunction with any of the -exportXXX flags, causes Maya to return a list of the nodes that would be exported, without actually writing the exported file to disk.
        prompt | pmt: (create, query) - This flag controls the display of file prompting dialogs. Some examples of file prompting dialogs include error messages that require user confirmation and missing file reference dialogs. Once this flag is used, every instance of the file command will use the last set value of this flag. Some interactive file operations may post dialogs even when the flag is set to false, but every scripted file command will not display any dialogs when this flag is set to false.  The default value is true.
        proxyManager | pm: (create) - When a one or more proxy references are added to an existing file reference, the proxy manage node is used to define the proxies associated with that reference. This flag is used in conjunction with the activeProxy and proxyTag flag to specify the proxyManager of interest. This flag is also used to specify the proxyManager for a proxy reference in the file referencing preload information, when used in conjunction with the referenceDepthInfo flag.
        proxyTag | pt: (create) - This flag is intended for internal use only during file load or preload. Proxy tags are names you assign to proxy references to more easily manage the proxy references from the reference editor. Proxy tags are unique within a given proxy set. This flag must be  used in conjunction with the proxyManager flag.
        reference | r: (query) - Create a reference to the specified file. Returns the name of the file referenced. Query all file references from the specified file.
        referenceDepthInfo | rdi: (create) - This flag is used to store reference loading preferences associated with a Maya ascii file (.ma). This flag is only useful during file I/O so users should not have any need to use this flag.
        referenceNode | rfn: (query) - This flag is only used during queries. In MEL, if it appears before -query then it must be followed by the name of one of the scene's reference nodes. That will determine the reference to be queried by whatever flags appear after -query. If the named reference node does not exist within the scene the command will fail with an error.  In Python the equivalent behavior is obtained by passing the name of the reference node as the flag's value.  In MEL, if this flag appears after -query then it takes no argument and will cause the command to return the name of the reference node associated with the file given as the command's argument. If the file is not a reference or for some reason does not have a reference node (e.g., the user deleted it) then an empty string will be returned. If the file is not part of the current scene then the command will fail with an error.  In Python the equivalent behavior is obtained by passing True as the flag's value.       In query mode, this flag can accept a value.
        relativeNamespace | rns: (create) - This flag can be used with the exportSelected, exportSelectedStrict and exportAll operations to specify that the nodes in the exported file are to be written out relative to a specified namespace. This provides the ability to remove undesired levels of namespacing from the node names as they are exported. The relativeNamespace value specifies the namespace to use as the relative root for the exported nodes, and must be specified as an absolute namespace. Nodes in the exported file not residing within the specified relative namespace will be written out using absolute namespace names. Note: this flag cannot be used in conjunction with the preserveReferences flag.
        removeDuplicateNetworks | rdn: (create) - When set, Maya will remove imported networks if the same network is also detected in the current scene. You can explicitly specify that certain types of networks be exempted from removal by this flag. For example, if you set to the optionVar removeDuplicateShadingNetworksOnImport to 0 (or disable the option Remove Duplicate Shading Networks from the File > Import options), then shading networks will be exempted from removal by this flag.This flag can only be used in conjunction with the -i/import flag.
        removeReference | rr: (create) - Remove the given file reference from its parent. This will also Remove everything this file references. Returns the name of the file removed. If the reference is alone in its namespace, remove the namespace. If there are objects remaining in the namespace after the file reference is removed, by default, keep the remaining objects in the namespace. To merge the objects remaining in the namespace to the parent or root namespace, use flags mergeNamespaceWithParent or mergeNamespaceWithRoot. The empty file reference namespace is then removed. To forcibly delete all objects, use flag force. The empty file reference namespace is then removed.
        rename | rn: (create) - Rename the scene. Used mostly during save to set the saveAs name. Returns the new name of the scene.
        renameAll | ra: (create) - If true, rename all newly-created nodes, not just those whose names clash with existing nodes. Only available with -i/import.
        renameToSave | rts: (create, query) - If true, the scene will need to be renamed before it can be saved. When queried this flag returns true if the scene must be renamed before it can be saved.  The default is false.
        renamingPrefix | rpr: (create, query) - The string to use as a prefix for all objects from this file. This flag has been replaced by -ns/namespace.
        renamingPrefixList | rpl: (query) - This flag returns a list of all of the renaming prefixes used by the file.
        replaceName | rep: (create, edit, multiuse, query) - Define a search and replace string. Will apply search and replace to leaf node names. The search string can include namespaces and wild-cards, but will only apply to leaf nodes in a dag hierarchy. Intended for use with offline edits files. May only be used with file -i/import or -r/reference. If a nested reference also defines a substitution, it will become the active substitution table while loading the nested reference. Note: if used with the -e/edit flag, the replacement will only be applied the next time the reference is loaded Examples: -replace "*pCube1" "prop" will change "foo:pCube1" to "foo:prop" and "|A:pCube1|B:pCube1" to "|A:pCube1|prop".
        reserveNamespaces | rvn: (create) - When this flag is enabled namespaces for unloaded references will be created after loading the file to reduce the chances of unexpected namespace collisions when loading or adding references later on.
        resetError | rer: (create) - Turn off any pre-existing global file errors.
        returnNewNodes | rnn: (create) - Used to control the return value in open, import, loadReference, and reference operations. It will force the file command to return a list of new nodes added to the current scene.
        save | s: (create) - Save the specified file. Returns the name of the saved file.
        saveDiskCache | sdc: (create, query) - This flag sets the saveAs option for Jiggle disk caches. The valid inputs are "always" - always copy a file texture to a new location, "never" - do not copy at all.  C: The default is "always".  Q: When queried it returns a string ("always", "never").
        saveReference | sr: (create) - Save reference node edits and connections to reference file. This includes newly added history and animation, provided that these do not apply to any objects outside the reference being saved.
        saveReferencesUnloaded | sru: (create) - This flag can only be used in conjunction with the save flag. It specifies that the saved file will be saved with all references unloaded.
        saveTextures | stx: (create, query) - This flag sets the saveAs option for 3d Paint file textures. The valid inputs are "always" - always copy a file texture to a new location, "unlessRef" - copy only if this is not a referenced file texture, "never" - do not copy at all.  C: The default is "unlessRef".  Q: When queried it returns a string ("always", unlessRef", "never").
        sceneName | sn: (query) - return the name of the current scene.
        segment | seg: () - This flag is obsolete.
        selectAll | sa: (create) - Select all the components of this file as well as its child files.  Note that the file specified must be one that is already opened in this Maya session. The default behavior is to replace the existing selection. Use with the "add" flag to keep the active selection list.
        shader | sh: (create, query) - For use with exportSelected to specify whether attached shaders should be included in the export.
        sharedNodes | shd: (create, multiuse) - This flag modifies the '-r/reference' flag to indicate that certain    types of nodes within that reference should be treated as shared nodes. All shared nodes will be placed in the default namespace. New copies of those nodes will not be created if a copy already exists in the default namespace, instead the shared node will be merged with the    existing node. The specifics of what happens when two nodes are merged depends on the node type. In general attribute values will not be merged, meaning the values set on any existing shared nodes will be retained, and the values of the nodes being merged in will be ignored. The valid options are "displayLayers", "shadingNetworks", "renderLayersByName", and "renderLayersById". This flag is multi-use; it may be specified multiple times to for example, share both display layers and shading networks. Two shading networks will only be merged if    they are identical: the network    of nodes feeding into the shading group must be arranged identically with equivalent nodes have the same name and node type. Additionally if a network is animated or contains a DAG object or expression it will not be mergeable. This flag cannot be used in conjunction with -srf/sharedReferenceFile.
        sharedReferenceFile | srf: (create) - Can only be used in conjunction with the -r/reference flag and the -ns/namespace flag (there is no prefix support). This flag modifies the '-r/reference' flag to indicate that all nodes within that reference should be treated as shared nodes. New copies    of those nodes will not be created if a copy already exists. Instead, the shared node will be merged with the existing node. The specifics of what happens when two nodes are merged depends on the node type. This flag cannot be used in conjunction with -shd/sharedNodes.
        shortName | shn: (query) - When used with a main query flag it indicates that the file name returned will be the short name (i.e., just a file name without any directory paths). If this flag is not present, the full name and directory path will be returned.
        strict | str: (create) - Set strict file path resolution. If true, all paths will be matched exactly, both relative and absolute. Relative paths will be considered relative to the project root directory. May only be used with the -o/open, -i/import, -ir/importReference or -r/reference flags.
        swapNamespace | sns: (create, multiuse) - Can only be used in conjunction with the -r/reference or -i/import flags. This flag will replace any occurrences of a given namespace to an alternate specified namespace. This namespace "swap" will occur as the file is referenced in. It takes in two string arguments. The first argument specifies the namespace to replace. The second argument specifies the replacement namespace. Use of this flag, implicitly enables the use of namespaces and cannot be used with deferReference.
        type | typ: (create, query) - Set the type of this file.  By default this can be any one of: "mayaAscii", "mayaBinary", "mel",  "OBJ", "directory", "plug-in", "audio", "move", "EPS", "Adobe(R) Illustrator(R)", "image" plug-ins may define their own types as well. Return a string array of file types that match this file.
        uiConfiguration | uc: (create, query) - Save the ui configuration with the scene in a uiConfiguration script node. (eg. panes, etc.) The current default is on and is set in initialStartup.mel.
        uiLoadConfiguration | ulc: (create, query) - Load the scene's ui configuration. (eg. panes, etc.) The current default is on and is set in initialStartup.mel.
        unloadReference | ur: (create) - This flag will unload the reference file associated with the passed reference node.
        unresolvedName | un: (query) - When used with a main query flag it indicates that the file name returned will be unresolved (i.e., it will be the path originally specified when the file was loaded into Maya; this path may contain environment variables and may not exist on disk). If this flag is not present, the resolved name will be returned.
        usingNamespaces | uns: (query) - Returns boolean. Queries whether the specified reference file uses namespaces or renaming prefixes.
        withoutCopyNumber | wcn: (query) - When used with a main query flag it indicates that the file name returned will not have a copy number appended to the end. If this flag is not present, the file name returned may have a copy number appended to the end.
        writable | w: (query) - Query whether the given file is writable in the current scene. For main scene files this indicates writable to the file system by the current user. Files referenced by the main scene file are always not writable (referenced files are by nature read only). Files not present in the current scene always return false.
    """
    ...


def fileBrowserDialog(*args, actionName: Optional[Union[str, bool]] = ..., an: Optional[Union[str, bool]] = ..., dialogStyle: Optional[Union[int, bool]] = ..., ds: Optional[Union[int, bool]] = ..., fileCommand: Optional[Union[str, bool]] = ..., fc: Optional[Union[str, bool]] = ..., fileType: Optional[Union[str, bool]] = ..., ft: Optional[Union[str, bool]] = ..., filterList: Optional[Union[str, bool]] = ..., fl: Optional[Union[str, bool]] = ..., includeName: Optional[Union[str, bool]] = ..., mode: Optional[Union[int, bool]] = ..., m: Optional[Union[int, bool]] = ..., operationMode: Optional[Union[str, bool]] = ..., om: Optional[Union[str, bool]] = ..., tipMessage: Optional[Union[str, bool]] = ..., tm: Optional[Union[str, bool]] = ..., windowTitle: Optional[Union[str, bool]] = ..., wt: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    The fileBrowserDialog and fileDialog commands have now been deprecated.
    Both commands are still callable, but it is recommended that the fileDialog2 command
    be used instead.  To maintain some backwards compatibility, both fileBrowserDialog and
    fileDialog will convert the flags/values passed to them into the appropriate flags/values
    that the fileDialog2 command uses and will call that command internally.  It is not
    guaranteed that this compatibility will be able to be maintained in future versions so
    any new scripts that are written should use fileDialog2.
    
    See below for an example of how to change a script to use fileDialog2.

    Args:
        actionName | an: (create) - Script to be called when the file is validated.
        dialogStyle | ds: (create) - 0 for old style dialog 1 for Windows 2000 style Explorer style 2 for Explorer style with "Shortcut" tip at bottom
        fileCommand | fc: (create) - The script to run on command action
        fileType | ft: (create) - Set the type of file to filter.  By default this can be any one of: "mayaAscii", "mayaBinary", "mel", "OBJ", "directory", "plug-in", "audio", "move", "EPS", "Illustrator", "image". plug-ins may define their own types as well.
        filterList | fl: (create, multiuse) - Specify file filters. Used with dialog style 1 and 2. Each string should be a description followed by a comma followed by a semi-colon separated list of file extensions with wildcard.
        includeName | includeName: (create) - Include the given string after the actionName in parentheses. If the name is too long, it will be shortened to fit on the dialog (for example, /usr/alias/commands/scripts/fileBrowser.mel might be shortened to /usr/...pts/fileBrowser.mel)
        mode | m: (create) - Defines the mode in which to run the file brower:  0 for read 1 for write 2 for write without paths (segmented files) 4 for directories have meaning when used with the action  +100 for returning short names
        operationMode | om: (create) - Enables the option dialog. Valid strings are:  "Import" "Reference" "SaveAs" "ExportAll" "ExportActive"
        tipMessage | tm: (create) - Message to be displayed at the bottom of the style 2 dialog box.
        windowTitle | wt: (create) - Set the window title of a style 1 or 2 dialog box
    """
    ...


def fileDialog(*args, application: bool = ..., app: bool = ..., defaultFileName: Optional[Union[str, bool]] = ..., dfn: Optional[Union[str, bool]] = ..., directoryMask: Optional[Union[str, bool]] = ..., dm: Optional[Union[str, bool]] = ..., mode: Optional[Union[int, bool]] = ..., m: Optional[Union[int, bool]] = ..., title: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    The fileBrowserDialog and fileDialog commands have now been deprecated.
    Both commands are still callable, but it is recommended that the fileDialog2 command
    be used instead.  To maintain some backwards compatibility, both fileBrowserDialog and
    fileDialog will convert the flags/values passed to them into the appropriate flags/values
    that the fileDialog2 command uses and will call that command internally.  It is not
    guaranteed that this compatibility will be able to be maintained in future versions so
    any new scripts that are written should use fileDialog2.
    
    See below for an example of how to change a script to use fileDialog2.

    Args:
        application | app: (create) - This is a "Mac" only flag. This brings up the dialog which selects only the application bundle.
        defaultFileName | dfn: (create) - Set default file name. This flag is available under "write" mode
        directoryMask | dm: (create) - This can be used to specify what directory and file names will be displayed in the dialog.  If not specified, the current directory will be used, with all files displayed. The string may contain a path name, and must contain a wild-carded file specifier. (eg "*.cc" or "/usr/u/*") If just a path is specified, then the last directory in the path is taken to be a file specifier, and this will not produce the desired results.
        mode | m: (create) - Defines the mode in which to run the file dialog:  0 for read 1 for write  Write mode can not be used in conjunction with the -application flag.
        title | t: (create) - Set title text. The default value under "write" mode is "Save As". The default value under "read" mode is "Open".
    """
    ...


def fileDialog2(*args, buttonBoxOrientation: Optional[Union[int, bool]] = ..., bbo: Optional[Union[int, bool]] = ..., cancelCaption: Optional[Union[str, bool]] = ..., cc: Optional[Union[str, bool]] = ..., caption: Optional[Union[str, bool]] = ..., cap: Optional[Union[str, bool]] = ..., dialogStyle: Optional[Union[int, bool]] = ..., ds: Optional[Union[int, bool]] = ..., fileFilter: Optional[Union[str, bool]] = ..., ff: Optional[Union[str, bool]] = ..., fileMode: Optional[Union[int, bool]] = ..., fm: Optional[Union[int, bool]] = ..., fileTypeChanged: Optional[Union[str, bool]] = ..., ftc: Optional[Union[str, bool]] = ..., hideNameEdit: bool = ..., hne: bool = ..., okCaption: Optional[Union[str, bool]] = ..., okc: Optional[Union[str, bool]] = ..., optionsUICancel: Optional[Union[str, bool]] = ..., oca: Optional[Union[str, bool]] = ..., optionsUICommit: Optional[Union[str, bool]] = ..., ocm: Optional[Union[str, bool]] = ..., optionsUICommit2: Optional[Union[str, bool]] = ..., oc2: Optional[Union[str, bool]] = ..., optionsUICreate: Optional[Union[str, bool]] = ..., ocr: Optional[Union[str, bool]] = ..., optionsUIInit: Optional[Union[str, bool]] = ..., oin: Optional[Union[str, bool]] = ..., optionsUITitle: Optional[Union[str, bool]] = ..., oti: Optional[Union[str, bool]] = ..., returnFilter: bool = ..., rf: bool = ..., selectFileFilter: Optional[Union[str, bool]] = ..., sff: Optional[Union[str, bool]] = ..., selectionChanged: Optional[Union[str, bool]] = ..., sc: Optional[Union[str, bool]] = ..., setProjectBtnEnabled: bool = ..., spe: bool = ..., startingDirectory: Optional[Union[str, bool]] = ..., dir: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This command provides a dialog that allows users to select files or directories.

    Args:
        buttonBoxOrientation | bbo: (create) - 1 Vertical button box layout. Cancel button is below the accept button.  2 Horizontal button box layout. Cancel button is to the right of the accept button.
        cancelCaption | cc: (create) - If the dialogStyle flag is set to 2 then this provides a caption for the Cancel button within the dialog.
        caption | cap: (create) - Provide a title for the dialog.
        dialogStyle | ds: (create) - 1 On Windows or Mac OS X will use a native style file dialog. 2 Use a custom file dialog with a style that is consistent across platforms.
        fileFilter | ff: (create) - Provide a list of file type filters to the dialog.  Multiple filters should be separated by double semi-colons.  See the examples section.
        fileMode | fm: (create) - Indicate what the dialog is to return.  0 Any file, whether it exists or not. 1 A single existing file. 2 The name of a directory.  Both directories and files are displayed in the dialog. 3 The name of a directory.  Only directories are displayed in the dialog. 4 The names of one or more existing files.
        fileTypeChanged | ftc: (create) - MEL only.  The string is interpreted as a MEL callback, to be called when the user-selected file type changes.  The callback is of the form:  global proc MyCustomFileTypeChanged(string $parent, string $newType)  The parent argument is the parent layout into which controls have been added using the optionsUICreate flag.  The newType argument is the new file type.
        hideNameEdit | hne: (create) - Hide name editing input field.
        okCaption | okc: (create) - If the dialogStyle flag is set to 2 then this provides a caption for the OK, or Accept, button within the dialog.
        optionsUICancel | oca: (create) - MEL only.  The string is interpreted as a MEL callback, to be called when the dialog is cancelled (with Cancel button or close button to close window). The callback is of the form:  global proc MyCustomOptionsUICancel()
        optionsUICommit | ocm: (create) - MEL only.  The string is interpreted as a MEL callback, to be called when the dialog is successfully dismissed.  It will not be called if the user cancels the dialog, or closes the window using window title bar controls or other window system means.  The callback is of the form:  global proc MyCustomOptionsUICommit(string $parent)  The parent argument is the parent layout into which controls have been added using the optionsUICreate flag.
        optionsUICommit2 | oc2: (create) - MEL only.  As optionsUICommit, the given string is interpreted as a MEL callback, to be called when the dialog is successfully dismissed. The difference is that this callback takes one additional argument which is the file name selected by the user before the dialog validation. It will not be called if the user cancels the dialog, or closes the window using window title bar controls or other window system means.  The callback is of the form:  global proc MyCustomOptionsUICommit(string $parent, string $selectedFile)  The parent argument is the parent layout into which controls have been added using the optionsUICreate flag.
        optionsUICreate | ocr: (create) - MEL only.  The string is interpreted as a MEL callback, to be called on creation of the file dialog.  The callback is of the form:  global proc MyCustomOptionsUISetup(string $parent)  The parent argument is the parent layout into which controls can be added.  This parent is the right-hand pane of the file dialog.
        optionsUIInit | oin: (create) - MEL only.  The string is interpreted as a MEL callback, to be called just after file dialog creation, to initialize controls.  The callback is of the form:  global proc MyCustomOptionsUIInitValues(string $parent, string $filterType)  The parent argument is the parent layout into which controls have been added using the optionsUICreate flag.  The filterType argument is the initial file filter.
        optionsUITitle | oti: (create) - MEL only. If optionsUICreate is set, user can set a custom title to their option window using this flag. If no title is desired, an empty string i.e. "" can be used.
        returnFilter | rf: (create) - If true, the selected filter will be returned as the last item in the string array along with the selected files.
        selectFileFilter | sff: (create) - Specify the initial file filter to select.  Specify just the begining text and not the full wildcard spec.
        selectionChanged | sc: (create) - MEL only.  The string is interpreted as a MEL callback, to be called when the user changes the file selection in the file dialog.  The callback is of the form:  global proc MyCustomSelectionChanged(string $parent, string $selection)  The parent argument is the parent layout into which controls have been added using the optionsUICreate flag.  The selection argument is the full path to the newly-selected file.
        setProjectBtnEnabled | spe: (create) - Define whether the project button should be enabled
        startingDirectory | dir: (create) - Provide the starting directory for the dialog.
    """
    ...


def fileInfo(*args, referenceNode: Optional[Union[str, bool]] = ..., rfn: Optional[Union[str, bool]] = ..., remove: Optional[Union[str, bool]] = ..., rm: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    fileInfo provides a mechanism for keeping information related
    to a Maya scene file.
    Each invocation of the command consists of a keyword/value pair,
    where both the keyword and the associated value are strings.
    The command may be invoked multiple times with different keywords.
    Maya emits this command several times into each file it creates,
    primarily to provide details such as
    which productization or packaging of the program was used
    (e.g "Complete", "Unlimited"), the specific version and build identification
    that was run, and the operating system on which it was run.
    Maya may make use of this information when present in files it reads.
    All keyword/value pairs defined by use of the fileInfo command are
    preserved when Maya saves the scene, whether to an ASCII or binary file.

    Args:
        referenceNode | rfn: (query) - Specify the name of a referenceNode to indicate the scene file to query. This flag is only valid during query. 			In query mode, this flag needs a value.
        remove | rm: (create, query) - If the remove flag is specified, the string following it is a keyword to remove from the list of fileInfo to be saved with the scene file.
    """
    ...


def filePathEditor(*args, attributeOnly: bool = ..., ao: bool = ..., attributeType: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., byType: Optional[Union[str, bool]] = ..., bt: Optional[Union[str, bool]] = ..., copyAndRepath: Optional[Union[Tuple[str, str], bool]] = ..., cr: Optional[Union[Tuple[str, str], bool]] = ..., deregisterType: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., force: bool = ..., f: bool = ..., listDirectories: Optional[Union[str, bool]] = ..., ld: Optional[Union[str, bool]] = ..., listFiles: Optional[Union[str, bool]] = ..., lf: Optional[Union[str, bool]] = ..., listRegisteredTypes: bool = ..., lrt: bool = ..., preview: bool = ..., p: bool = ..., recursive: bool = ..., rc: bool = ..., refresh: bool = ..., rf: bool = ..., registerType: Optional[Union[str, bool]] = ..., rt: Optional[Union[str, bool]] = ..., relativeNames: bool = ..., rel: bool = ..., repath: Optional[Union[str, bool]] = ..., r: Optional[Union[str, bool]] = ..., replaceAll: bool = ..., ra: bool = ..., replaceField: Optional[Union[str, bool]] = ..., rfd: Optional[Union[str, bool]] = ..., replaceString: Optional[Union[Tuple[str, str], bool]] = ..., rs: Optional[Union[Tuple[str, str], bool]] = ..., status: bool = ..., s: bool = ..., temporary: bool = ..., tmp: bool = ..., typeLabel: Optional[Union[str, bool]] = ..., tl: Optional[Union[str, bool]] = ..., unresolved: bool = ..., u: bool = ..., withAttribute: bool = ..., wa: bool = ..., query: bool = ...) -> Any:
    r"""
    Maya can reference and use external files, such as textures or other Maya
    scenes. This command is used to get the information about those file paths and
    modify them in bulk.
    By default, only the most frequently used types of files are presented to the
    user:
    
    
    Texture
    Scene reference
    Audio
    Image plane
    
    
    For the command to manage more file types, those must be explicitly requested by
    the caller using the "registerType" flag. This flag tells the command about
    attributes or nodes that are to reveal their paths when the command is used.
    
    
    Currently, the attributes specified through this flag must have the
    "usedAsFileName" property. Supported nodes are "reference" and plug-in nodes.
    For example: "brush.flowerImage" or "reference" can be used as value for this
    flag.
    
    
    Conversely, the "deregisterType" flag can be used to tell the command to stop
    handling certain attributes or nodes.
    
    
    Once the set of attributes and nodes to be searched for external files is
    selected, the command can be used to obtain a list of plugs that contain file
    names. Additional information can be obtained, such as each file's name,
    directory, and report whether the file exists. Additional information about the
    associated node or plug can also be obtained, such as its name, type and label.
    
    
    Finally, the command can be used to perform various manipulations such as
    editing the paths, remapping the files or verifying the presence of
    identically-named files in target directories. See the "repath",
    "copyAndRepath" and "replaceField" flags for more information.
    
    
    The results of these manipulations can be previewed before they are applied
    using the "preview" flag.

    Args:
        attributeOnly | ao: (query) - Used with "listFiles" to return the node and attribute name that are using the files.
        attributeType | at: (query) - Query the attribute type for the specified plug.
        byType | bt: (query) - Used with "listFiles" to query files that are used by the specified node type or attribute type. 			In query mode, this flag needs a value.
        copyAndRepath | cr: (create) - Copy a source file to the destination path and repath the plug data to the new file. The source file must have the same name as the one in the plug. The command will look for the file at the specified location first. If not found, the command will try to use the original file in the plug. If the file is still not found, nothing is done.
        deregisterType | dt: (create) - Deregister a file type from the list of registered types so the command stops handling it. Unless the "temporary" flag is used, the type will be removed from the preferences will not reappear on application restart. When the "temporary" flag is specified, the deregistration is only effective for the current session. The deregistration will be rejected if the type has already been unregistered. However, it is valid to deregister permanently (without the "temporary" flag) a type after it has been temporarily deregistered.
        force | f: (create) - Used with flag "repath" to repath all files to the new location, including the resolved files. Otherwise, "repath" will only deal with the missing files. Used with flag "copyAndRepath" to overwrite any colliding file at the destination. Otherwise, "copyAndRepath" will use the existing file at the destination instead of overwriting it. The default value is off.
        listDirectories | ld: (query) - List all sub directories of the specified directory.  Only directories containing at least one file whose type is registered (see "registerType") will be listed. If no directory is provided, all directories applicable to the scene will be returned. 			In query mode, this flag needs a value.
        listFiles | lf: (query) - List files in the specified directory. No recursion in subdirectories will be performed. 			In query mode, this flag needs a value.
        listRegisteredTypes | lrt: (query) - Query the list of registered attribute types. The registered types include the auto-loaded types from the preference file and the types explicitly registered by the user, both with and without the "temporary" flag.
        preview | p: (create) - Used with "repath", "replaceString" or "copyAndRepath" to preview the result of the operation instead of excuting it. When it is used with "repath" or "replaceString", the command returns the new file path and a status flag indicating whether the new file exists (1) or not (0). The path name and the file status are listed in pairs. When it is used with "copyAndRepath", the command returns the files that need copying.
        recursive | rc: (create) - Used with flag "repath" to search the files in the target directory and its subdirectories recursively. If the flag is on, the command will repath the plug to a file that has the same name in the target directory or sub directories. If the flag is off, the command will apply the directory change without verifying that the resulting file exists.
        refresh | rf: (create) - Clear and re-collect the file information in the scene. The command does not automatically track file path modifications in the scene. So it is the users responsibility to cause refreshes in order to get up-to-date information.
        registerType | rt: (create) - Register a new file type that the command will handle and recognize from now on. Unless the "temporary" flag is used, the registered type is saved in the preferences and reappears on application restart. The new type will be rejected if it collides with an existing type or label. One exception to this is when registering a type without the "temporary" flag after the type has been registered with it. This is considered as modifying the persistent/temporary property of the existing type, rather than registering a new type.
        relativeNames | rel: (query) - Used with "listDirectories" or "listFiles" to return the relative path of each directory or file.  Paths are relative to the current project folder. If a file or the directory is not under the current project folder, the returned path will still be a full path.
        repath | r: (create) - Replace the directory part of a file path with a specified location. The file name will be preserved.
        replaceAll | ra: (create) - Used with flag "replaceString", specifies how many times the matched string will be replaced. When the flag is false, only the first matched string will be replaced. Otherwise, all matched strings will be replaced. The default value is false.
        replaceField | rfd: (create) - Used with the "replaceString" flag to control the scope of the replacement. Possible values are: "pathOnly" - only replace strings in the directory part. "nameOnly" - only replace strings in the file name, without the directory. "fullPath" - replace strings anywhere in the full name. The default argument is "fullPath".
        replaceString | rs: (create) - Replace the target string with the new string in the file paths. The flag needs two arguments: the first one is the target string and the second one is the new string. See the "replaceField" and "replaceAll" flags to control how the replacement is performed.
        status | s: (query) - Used with "listFiles", this will cause the returned list of files to include one status flag per file: 0 if it cannot be resolved and 1 if it can. Used with "listDirectories", this will cause the returned list of directories to include one status flag per directory: 0 if it cannot be resolved, 1 if it can and 2 if the resolution is partial. The status will be interleaved with the file/directory names, with the name appearing first. See the example for "listFiles".  See the "withAttribute" flag for another way of getting per-file information.  When multiple per-entry items appear in the list (e.g.: plug name), the status is always last.
        temporary | tmp: (create) - Make the effect of the "register"/"deregister" flag only applicable in the current session. Normally, a type registration/deregistration is permanent and is made persistent via a preference file. When the "temporary" flag is specified, the changes will not be saved to the preference file. When the application restarts, any type that has been previously temporarily registered will not appear and any type that was temporarily deregistered will re-appear.
        typeLabel | tl: (create, query) - Used with "registerType" to set the label name for the new file type. Used with "query" to return the type label for the specified attribute type. For default types, the type label is the localized string. For other types, the type label is supplied by user. 			In query mode, this flag needs a value.
        unresolved | u: (query) - Used with "listFiles" to query the unresolved files that are being used in the scene.
        withAttribute | wa: (query) - Used with "listFiles" to return the name of the plug using a given file. For example, if "file.jpg" is used by the plug "node1.fileTextureName", then the returned string will become the pair "file.jpg node1.fileTextureName".  See the "status" flag for another way to get per-file information.
    """
    ...


def filterStudioImport(*args, convertShellToPoly: bool = ..., sp: bool = ..., includeCameras: bool = ..., ic: bool = ..., includeLights: bool = ..., il: bool = ..., transferDirectoryName: Optional[Union[str, bool]] = ..., td: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Directly sets the filter options on the studioImport plugin from
        anywhere in MEL without having to use the UI.  This is used by ViCE.

    Args:
        convertShellToPoly | sp: (create) - If true, shells in the input will be converted to triangular meshes.     If false, any/all shells encountered will be groups of surfaces.
        includeCameras | ic: (create) - If true, cameras in the input to "studioImport" will be translated.     If false, any/all cameras encountered by "studioImport" will be ignored.
        includeLights | il: (create) - If true, lights in the input to "studioImport" will be translated.     If false, any/all lights encountered by "studioImport" will be ignored.
        transferDirectoryName | td: (create) - If set (non-empty), use as directory for storing imbedded binary files,     else use the directory given by "theTempDirectory->fullName()".
    """
    ...


def findType(*args, deep: bool = ..., d: bool = ..., exact: bool = ..., e: bool = ..., forward: bool = ..., f: bool = ..., type: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    The findType command is used to search through a dependency
    subgraph on a certain node to find all nodes of the given type.
    The search can go either upstream (input connections) or downstream (output
    connections). The plug/attribute dependencies are not taken into account
    when searching for matching nodes, only the connections.

    Args:
        deep | d: (create) - Find all nodes of the given type instead of just the first.
        exact | e: (create) - Match node types exactly instead of any in a node hierarchy.
        forward | f: (create) - Look forwards (downstream) through the graph rather than backwards (upstream) for matching nodes.
        type | t: (create) - Type of node to look for (e.g. "transform"). This flag is mandatory.
    """
    ...


def flushUndo(*args) -> Any:
    r"""
    Removes everything from the undo queue, freeing up memory.

    Args:
    """
    ...


def format(*args, stringArg: Optional[Union[str, bool]] = ..., s: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This command takes a format string, where the format string contains
    format specifiers.  The format specifiers have a number associated
    with them relating to which parameter they represent to allow for
    alternate ordering of the passed-in values for other
    languages by merely changing the format string

    Args:
        stringArg | s: (create, multiuse) - Specify the arguments for the format string.
    """
    ...


def getFileList(*args, filespec: Optional[Union[str, bool]] = ..., fs: Optional[Union[str, bool]] = ..., folder: Optional[Union[str, bool]] = ..., fld: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Returns a list of files matching an optional wildcard pattern.
    Note that this command works directly on raw system files and does not go through standard Maya file path resolution.

    Args:
        filespec | fs: (create) - wildcard specifier for search.
        folder | fld: (create) - return a directory listing
    """
    ...


def getInputDeviceRange(*args, maxValue: bool = ..., max: bool = ..., minValue: bool = ..., min: bool = ...) -> Any:
    r"""
    This command lists the minimum and maximum values the device
    axis can return.  This value is the raw device values before
    any mapping is applied.  If you don't specify an axis the
    values for all axes of the device are returned.

    Args:
        maxValue | max: (create) - list only the maximum value of the axis
        minValue | min: (create) - list only the minimum value of the axis
    """
    ...


def getModifiers(*args) -> Any:
    r"""
    This command returns the current state of the modifier keys. The state
    of each modifier can be obtained by testing for the modifier's
    corresponding bit value in the return value. Shift is bit 1,
    Ctrl is bit 3, Alt is bit 4, and bit 5 is the 'Windows' key on Windows keyboards
    and the Command key on Mac keyboards.  See the provided
    example for more details on testing for each modifier's bit value.

    Args:
    """
    ...


def getModulePath(*args, moduleName: Optional[Union[str, bool]] = ..., mn: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Returns the module path for a given module name.

    Args:
        moduleName | mn: (create) - The name of the module whose path you want to retrieve.
    """
    ...


def hardware(*args, brdType: bool = ..., brd: bool = ..., cpuType: bool = ..., cpu: bool = ..., graphicsType: bool = ..., gfx: bool = ..., megaHertz: bool = ..., mhz: bool = ..., numProcessors: bool = ..., npr: bool = ...) -> Any:
    r"""
    Return description of the hardware available in the machine.

    Args:
        brdType | brd: (create) - Returns IP number identifying the CPU motherboard
        cpuType | cpu: (create) - Returns type of CPU
        graphicsType | gfx: (create) - Returns string identifying graphics hardware type
        megaHertz | mhz: (create) - Returns string identifying the speed of the CPU chip
        numProcessors | npr: (create) - Returns string identifying the number of processors
    """
    ...


def help(*args, documentation: bool = ..., doc: bool = ..., language: Optional[Union[str, bool]] = ..., lng: Optional[Union[str, bool]] = ..., list: bool = ..., l: bool = ..., popupDisplayTime: Optional[Union[int, bool]] = ..., pdt: Optional[Union[int, bool]] = ..., popupMode: bool = ..., pm: bool = ..., popupPauseTime: Optional[Union[int, bool]] = ..., ppt: Optional[Union[int, bool]] = ..., popupSimpleMode: bool = ..., psm: bool = ..., rolloverMode: bool = ..., rm: bool = ..., syntaxOnly: bool = ..., so: bool = ..., query: bool = ...) -> Any:
    r"""
    With no arguments, help tells how to use help. If a command name is
    specified, help will return the quick help for that command. Other
    flags can be used to open the online documentation, or to list
    available commands based on a pattern.
    
    Pattern follows the following syntax:
    
    
    *            matches any string
    ?            matches any character
    [agj]        matches a, g or j
    [^0-9]       matches anything but a digit
    x+           matches any number of subsequent x
    a{3}         matches aaa
    a{3,}        matches aaa, aaaa, ...
    a{3,5}       matches aaa, aaaa, or aaaaa
    (ab)(CD)\2\1 matches abCDCDab (\1 to \9 available)

    Args:
        documentation | doc: (create) - Use a browser to show the documentation associated with the single command name given. A pattern cannot be used with this flag. If no command name is specified, then this flag will go to the main documentation index.
        language | lng: (create) - Show the help for this command in the specified language. Valid values are "mel" and "python". The default is Mel. Used with the doc flag.
        list | l: (create) - List all the commands whose names match the regular expression. Pass the regular expression as the first argument to the command specified.
        popupDisplayTime | pdt: (create, query) - Set the amount of time, in seconds, that the popup help will be displayed.  The default is 4 seconds. This flag is mutually exclusive of the list and doc flags.
        popupMode | pm: (create, query) - Turn on or off popup help mode.  This flag is mutually exclusive of the list and doc flags.
        popupPauseTime | ppt: (create, query) - Set the amount of time, in milliseconds, before the popup help will be displayed. The default is 800 milliseconds. This flag is mutually exclusive of the list and doc flags.
        popupSimpleMode | psm: (create, query) - Turn on or off simple popup help mode. If set, ToolClips will display only name and keyboard shortcut.
        rolloverMode | rm: (create, query) - Turn on or off rollover help mode.  This flag is mutually exclusive with the list and doc flags.
        syntaxOnly | so: (create) - When no other flag is specified, return only the syntax part of the quick help.
    """
    ...


def hitTest(*args) -> Any:
    r"""
    The hitTest command hit-tests a point in the named control and returns
    a list of items underneath the point. The point is specified in pixels with
    the origin (0,0) at the top-left corner. This position is compatible
    with the coordinates provided by a drop-callback. The types of items
    that may be returned depends upon the specific control; not all
    controls currently support hit-testing.

    Args:
    """
    ...


def imfPlugins(*args, extension: Optional[Union[str, bool]] = ..., ext: Optional[Union[str, bool]] = ..., keyword: Optional[Union[str, bool]] = ..., key: Optional[Union[str, bool]] = ..., multiFrameSupport: Optional[Union[str, bool]] = ..., mfs: Optional[Union[str, bool]] = ..., pluginName: Optional[Union[str, bool]] = ..., pn: Optional[Union[str, bool]] = ..., readSupport: Optional[Union[str, bool]] = ..., rs: Optional[Union[str, bool]] = ..., writeSupport: Optional[Union[str, bool]] = ..., ws: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command queries all the available imf plugins for its
    name, keyword or image file extension.
    Only one of the attributes (name, keyword or extension) can be queried at a time.
    If no flags are specified, this command returns a list of all available plugin
    names.

    Args:
        extension | ext: (create, query) - image file extension
        keyword | key: (create, query) - imf keyword
        multiFrameSupport | mfs: (create, query) - multi frame IO is supported
        pluginName | pn: (create, query) - imf plugin name
        readSupport | rs: (create, query) - read operation is supported
        writeSupport | ws: (create, query) - write operation is supported
    """
    ...


def internalVar(*args, mayaInstallDir: bool = ..., mid: bool = ..., userAppDir: bool = ..., uad: bool = ..., userBitmapsDir: bool = ..., ubd: bool = ..., userHotkeyDir: bool = ..., uhk: bool = ..., userMarkingMenuDir: bool = ..., umm: bool = ..., userPrefDir: bool = ..., upd: bool = ..., userPresetsDir: bool = ..., ups: bool = ..., userScriptDir: bool = ..., usd: bool = ..., userShelfDir: bool = ..., ush: bool = ..., userTmpDir: bool = ..., utd: bool = ..., userWorkspaceDir: bool = ..., uwd: bool = ...) -> Any:
    r"""
    This command returns the values of internal variables.  No modification
    of these variables is supported.

    Args:
        mayaInstallDir | mid: (create) - Return the Maya installation directory.
        userAppDir | uad: (create) - Return the user application directory.
        userBitmapsDir | ubd: (create) - Return the user bitmaps prefs directory.
        userHotkeyDir | uhk: (create) - Return the user hotkey directory.
        userMarkingMenuDir | umm: (create) - Return the user marking menu directory.
        userPrefDir | upd: (create) - Return the user preference directory.
        userPresetsDir | ups: (create) - Return the user presets directory.
        userScriptDir | usd: (create) - Return the user script directory.
        userShelfDir | ush: (create) - Return the user shelves directory.
        userTmpDir | utd: (create) - Return a temp directory.  Will check for TMPDIR environment variable, otherwise will return the current directory.
        userWorkspaceDir | uwd: (create) - Return the user workspace directory (also known as the projects directory).
    """
    ...


def launch(*args, directory: Optional[Union[str, bool]] = ..., dir: Optional[Union[str, bool]] = ..., movie: Optional[Union[str, bool]] = ..., mov: Optional[Union[str, bool]] = ..., pdfFile: Optional[Union[str, bool]] = ..., pdf: Optional[Union[str, bool]] = ..., webPage: Optional[Union[str, bool]] = ..., web: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Launch the appropriate application to open the document, web page or directory
    specified.

    Args:
        directory | dir: (create) - A directory.
        movie | mov: (create) - A movie file. The only acceptable movie file formats are MPEG, Quicktime, and Windows Media file. The file's name must end with .mpg, .mpeg, .mp4, .wmv, .mov, or .qt.
        pdfFile | pdf: (create) - A PDF (Portable Document Format) document. The file's name must end with .pdf.
        webPage | web: (create) - A web page.
    """
    ...


def launchImageEditor(*args, editImageFile: Optional[Union[str, bool]] = ..., eif: Optional[Union[str, bool]] = ..., viewImageFile: Optional[Union[str, bool]] = ..., vif: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Launch the appropriate application to edit/view the image files specified.
    This command works only on the Macintosh and Windows platforms.

    Args:
        editImageFile | eif: (create) - If the file is a PSD, then the specified verison of Photoshop is launched, and the file is opened in it. If file is any other image type, then the preferred image editor is launched, and the file is opened in it.
        viewImageFile | vif: (create) - Opens up an Image editor to view images.
    """
    ...


def listDeviceAttachments(*args, attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., axis: Optional[Union[str, bool]] = ..., ax: Optional[Union[str, bool]] = ..., clutch: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., device: Optional[Union[str, bool]] = ..., d: Optional[Union[str, bool]] = ..., file: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., selection: bool = ..., sl: bool = ..., write: bool = ..., w: bool = ...) -> Any:
    r"""
    This command lists the current set of device attachments.
    The listing is in the form of the commands required to
    recreate them.  This includes both attachments and device
    mappings.

    Args:
        attribute | at: (create) - specify the attribute attachments to list
        axis | ax: (create) - specify the axis attachments to list
        clutch | c: (create) - List only attachment clutched with this button
        device | d: (create) - specify which device attachments to list
        file | f: (create) - Specify the name of the file to write out device attachments.
        selection | sl: (create) - This flag list only attachments on selection
        write | w: (create) - Write out device attachments to a file specified by the -f flag, is set.  If -f is not set, it'll write out to a file named for the device.
    """
    ...


def listInputDeviceAxes(*args) -> Any:
    r"""
    This command lists all of the axes of the specified
    input device.

    Args:
    """
    ...


def listInputDeviceButtons(*args) -> Any:
    r"""
    This command lists all of the buttons of the specified
    input device specified as an argument.

    Args:
    """
    ...


def listInputDevices(*args, free: bool = ..., f: bool = ..., primary: bool = ..., p: bool = ..., secondary: bool = ..., s: bool = ...) -> Any:
    r"""
    This command lists all input devices that maya knows about.

    Args:
        free | f: (create) - List the free devices
        primary | p: (create) - List the primary devices
        secondary | s: (create) - List the secondary devices
    """
    ...


def loadModule(*args, allModules: bool = ..., a: bool = ..., load: Optional[Union[str, bool]] = ..., ld: Optional[Union[str, bool]] = ..., scan: bool = ..., sc: bool = ...) -> Any:
    r"""
    Maya plug-ins may be installed individually within one of Maya's standard plug-in directories, or they may be packaged up with other resources in a "module". Each module resides in its own directory and provides a module definition file to make Maya aware of the plug-ins it provides.
    
    When Maya starts up it loads all of the module files it finds, making the module's plug-ins, scripts and other resources available for use. Note that the plug-ins themselves are not loaded at this time, Maya is simply made aware of them so that they can be loaded if needed.
    
    The loadModule command provides the ability to list and load any new modules which have been added since Maya started up, thereby avoiding the need to restart Maya before being able to use them.

    Args:
        allModules | a: (create) - Load all new modules not yet loaded in Maya. New modules are the one returned by the -scan option.
        load | ld: (create) - Load the module specified by the module definition file.
        scan | sc: (create) - Rescan module presence. Returns the list of module definition files found and not yet loaded into Maya. Does not load any of these newly found modules, nor change the Maya state.
    """
    ...


def loadPlugin(*args, addCallback: Optional[Union[str, bool]] = ..., ac: Optional[Union[str, bool]] = ..., allPlugins: bool = ..., a: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., quiet: bool = ..., qt: bool = ..., removeCallback: Optional[Union[str, bool]] = ..., rc: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Load plug-ins into Maya. The parameter(s) to this command
    are either the names or pathnames of plug-in files.  The
    convention for naming plug-ins is to use a .so extension
    on Linux, a .mll extension on Windows and .bundle
    extension on Mac OS X. If no extension is provided then the default
    extension for the platform will be used. To load a Python plugin
    you must explicitly supply the '.py' extension.
    
    If the plugin was specified with a pathname then that is
    where the plugin will be searched for. If no pathname was
    provided then the current working directory (i.e. the one
    returned by Maya's 'pwd' command) will be searched, followed
    by the directories in the MAYA_PLUG_IN_PATH environment variable.
    
    When the plug-in is loaded, the name used in Maya's
    internal plug-in registry for the plug-in information will
    be the file name with the extension removed.  For example,
    if you load the plug-in "newNode.mll" the name used in
    the Maya's registry will be "newNode".  This value as
    well as that value with either a ".so", ".mll" or ".bundle"
    extension can be used as valid arguments to either the
    unloadPlugin or pluginInfo commands.

    Args:
        addCallback | ac: (create) - Add a MEL or Python callback script to be called after a plug-in is loaded.  For MEL, the procedure should have the following signature: global proc procedureName(string $pluginName).  For Python, you may specify either a script as a string, or a Python callable object such as a function.  If you specify a string, then put the formatting specifier "%s" where you want the name of the plug-in to be inserted.  If you specify a callable such as a function, then the name of the plug-in will be passed as an argument.
        allPlugins | a: (create) - Cause all plug-ins in the search path specified in MAYA_PLUG_IN_PATH to be loaded.
        name | n: (create) - Set a user defined name for the plug-ins that are loaded.  If the name is already taken, then a number will be added to the end of the name to make it unique.
        quiet | qt: (create) - Don't print a warning if you attempt to load a plug-in that is already loaded.
        removeCallback | rc: (create) - Removes a procedure which was previously added with -addCallback.
    """
    ...


def melInfo(*args) -> Any:
    r"""
    This command returns the names of all global MEL procedures that are currently
    defined as a string array. The user can query the definition of each MEL
    procedure using the "whatIs" command.

    Args:
    """
    ...


def memory(*args, adjustedVirtualMemory: bool = ..., av: bool = ..., asFloat: bool = ..., af: bool = ..., debug: bool = ..., dbg: bool = ..., freeMemory: bool = ..., fr: bool = ..., gigaByte: bool = ..., gb: bool = ..., heapMemory: bool = ..., he: bool = ..., kiloByte: bool = ..., kb: bool = ..., megaByte: bool = ..., mb: bool = ..., pageFaults: bool = ..., pf: bool = ..., pageReclaims: bool = ..., pr: bool = ..., physicalMemory: bool = ..., phy: bool = ..., processVirtualMemory: bool = ..., pv: bool = ..., summary: bool = ..., sum: bool = ..., swapFree: bool = ..., swf: bool = ..., swapLogical: bool = ..., swl: bool = ..., swapMax: bool = ..., swm: bool = ..., swapPhysical: bool = ..., swp: bool = ..., swapReserved: bool = ..., swr: bool = ..., swapVirtual: bool = ..., swv: bool = ..., swaps: bool = ..., sw: bool = ...) -> Any:
    r"""
    Used to query essential statistics on memory availability and usage.
    
    By default memory sizes are returned in bytes. Since Maya's command engine
    only supports 32-bit signed integers, any returned value which cannot fit
    into 31 bits will be truncated to 2,147,483,647 and a warning message displayed.
    To avoid having memory sizes truncated use one of the memory size flags to
    return the value in larger units (e.g. megabytes) or use the asFloat flag to
    return the value as a float.

    Args:
        adjustedVirtualMemory | av: (create) - Returns size of adjusted virtual memory allocated by the process. The adjustment is done by computing an offset when the application is launched that will be subtracted from the process virtual memory in order to give the adjusted value.  The returned size is an approximation of the memory used by the process that can be more reliable in some cases, for instance on platforms where display drivers can reserve large ranges of memory addresses, therefore increasing the size of the process virtual memory, even though those addresses are actually not used.
        asFloat | af: (create) - Causes numeric values to be returned as floats rather than ints. This can be useful if you wish to retain some of the significant digits lost when using the unit size flags.
        debug | dbg: (create) - Print debugging statistics on arena memory (if it exists)
        freeMemory | fr: (create) - Returns size of free memory
        gigaByte | gb: (create) - Return memory sizes in gigabytes (1024*1024*1024 bytes)
        heapMemory | he: (create) - Returns size of memory heap
        kiloByte | kb: (create) - Return memory sizes in kilobytes (1024 bytes)
        megaByte | mb: (create) - Return memory sizes in megabytes (1024*1024 bytes)
        pageFaults | pf: (create) - Returns number of page faults
        pageReclaims | pr: (create) - Returns number of page reclaims
        physicalMemory | phy: (create) - Returns size of physical memory
        processVirtualMemory | pv: (create) - Returns size of virtual memory allocated by the process
        summary | sum: (create) - Returns a summary of memory usage. The size flags are ignored and all memory sizes are given in megabytes.
        swapFree | swf: (create) - Returns size of free swap
        swapLogical | swl: (create) - Returns size of logical swap
        swapMax | swm: (create) - Returns maximum swap size
        swapPhysical | swp: (create) - Returns size of physical swap
        swapReserved | swr: (create) - Returns size of reserved swap
        swapVirtual | swv: (create) - Returns size of virtual swap
        swaps | sw: (create) - Returns number of swaps
    """
    ...


def moduleInfo(*args, definition: bool = ..., d: bool = ..., listModules: bool = ..., lm: bool = ..., moduleName: Optional[Union[str, bool]] = ..., mn: Optional[Union[str, bool]] = ..., path: bool = ..., p: bool = ..., version: bool = ..., v: bool = ...) -> Any:
    r"""
    Returns information on modules found by Maya.

    Args:
        definition | d: (create) - Returns module definition file name for the module specified by the -moduleName parameter.
        listModules | lm: (create) - Returns an array containing the names of all currently loaded modules.
        moduleName | mn: (create) - The name of the module whose information you want to retrieve. Has to be used with either -definition / -path / -version flags.
        path | p: (create) - Returns the module path for the module specified by the -moduleName parameter.
        version | v: (create) - Returns the module version for the module specified by the -moduleName parameter.
    """
    ...


def mouse(*args, enableScrollWheel: bool = ..., esw: bool = ..., mouseButtonTracking: Optional[Union[int, bool]] = ..., mbt: Optional[Union[int, bool]] = ..., mouseButtonTrackingStatus: bool = ..., mbs: bool = ..., scrollWheelStatus: bool = ..., sws: bool = ...) -> Any:
    r"""
    This command allows to configure mouse.

    Args:
        enableScrollWheel | esw: (create) - Enable or disable scroll wheel support.
        mouseButtonTracking | mbt: (create) - Set the number (1, 2 or 3) of mouse buttons to track. Note: this is only supported on Macintosh
        mouseButtonTrackingStatus | mbs: (create) - returns the current number of mouse buttons being tracked.
        scrollWheelStatus | sws: (create) - returns the current status of scroll wheel support.
    """
    ...


def namespace(*args, absoluteName: bool = ..., an: bool = ..., addNamespace: Optional[Union[str, bool]] = ..., add: Optional[Union[str, bool]] = ..., collapseAncestors: Optional[Union[str, bool]] = ..., ch: Optional[Union[str, bool]] = ..., deleteNamespaceContent: bool = ..., dnc: bool = ..., exists: Optional[Union[str, bool]] = ..., ex: Optional[Union[str, bool]] = ..., force: bool = ..., f: bool = ..., isRootNamespace: Optional[Union[str, bool]] = ..., ir: Optional[Union[str, bool]] = ..., mergeNamespaceWithOther: Optional[Union[str, bool]] = ..., mno: Optional[Union[str, bool]] = ..., mergeNamespaceWithParent: bool = ..., mnp: bool = ..., mergeNamespaceWithRoot: bool = ..., mnr: bool = ..., moveNamespace: Optional[Union[Tuple[str, str], bool]] = ..., mv: Optional[Union[Tuple[str, str], bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., recurse: bool = ..., r: bool = ..., relativeNames: bool = ..., rel: bool = ..., removeNamespace: Optional[Union[str, bool]] = ..., rm: Optional[Union[str, bool]] = ..., rename: Optional[Union[Tuple[str, str], bool]] = ..., ren: Optional[Union[Tuple[str, str], bool]] = ..., setNamespace: Optional[Union[str, bool]] = ..., set: Optional[Union[str, bool]] = ..., validateName: Optional[Union[str, bool]] = ..., vn: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command allows a namespace to be created, set or removed.
    
    A namespace is a simple grouping of objects under a given name.
    Namespaces are primarily used to resolve name-clash issues in Maya,
    where a new object has the same name as an existing object (from
    importing a file, for example).  Using namespaces, you can have two
    objects with the same name, as long as they are contained in
    differenct namespaces.
    
    Namespaces are reminiscent of hierarchical structures like file
    systems where namespaces are analogous to directories and objects are
    analogous to files. The colon (':') character is the separator used to
    separate the names of namespaces and nodes instead of the slash ('/')
    or backslash ('\') character.  Namespaces can contain other namespaces
    as well as objects.  Like objects, the names of namespaces must be
    unique within another namespace. Objects and namespaces can be in only
    one namespace. Namespace names and object names don't clash so a
    namespace and an object contained in another namespace can have the
    same name.
    
    There is an unnamed root namespace specified with a leading colon
    (':').  Any object not in a named namespace is in the root namespace.
    Normally, the leading colon is omitted from the name of an object as
    it's presence is implied. The presence of a leading colon is
    important when moving objects between namespaces using the 'rename'
    command.  For the 'rename' command, the new name is relative to the
    current namespace unless the new name is fully qualified with a
    leading colon.
    
    Namespaces are created using the 'add/addNamespace' flag. By default they are
    created under the current namespace. Changing the current namespace is
    done with the 'set/setNamespace' flag. To reset the current namespace to
    the root namespace, use 'namespace -set ":";'. Whenever an object is
    created, it is added by default to the current namespace.
    
    When creating a new namespace using a qualified name, any intervening namespaces which do
    not yet exist will be automatically created. For example, if the name of
    the new namespace is specified as "A:B" and the current namespace already
    has a child namespace named "A" then a new child namespace named "B" will
    be created under "A". But if the current namespace does not yet have a
    child named "A" then it will be created automatically. This applies
    regardless of the number of levels in the provided name (e.g. "A:B:C:D").
    
    The 'p/parent' flag can be used to explicitly specify the parent namespace
    under which the new one should be created, rather than just defaulting to
    the current namespace.
    
    If the name given for the new namespace is absolute (i.e. it begins with a
    colon, as in ":A:B") then both the current namespace and the 'parent' flag
    will be ignored and the new namespace will be created under the root namespace.
    
    The relativeNamespace flag can be used to change the way node names
    are displayed in the UI and returned by the 'ls' command. Here are
    some specific details on how the return from the 'ls' command works in
    relativeNamespace mode:
    
    List all mesh objects in the scene:
    ls -type "mesh";
    The above command lists all mesh objects in the root and any child namespaces. In relative name lookup mode, all names will be displayed relative to the current namespace. When not in relative name lookup mode (the default behaviour in Maya), results are printed relative to the root namespace.
    
    Using a "*" wildcard:
    namespace -set myNS;
    ls -type "mesh "*";
    
    In relative name lookup mode, the "*" will match to the current namespace and thus the ls command will list only those meshes defined within the current namespace (i.e. myNs). If relative name lookup is off (the default behaviour in Maya), names are root-relative and thus "*" matches the root namespace, with the net result being that only thoses meshes defined in the root namespace will be listed.
    
    You can force the root namespace to be listed when in relative name lookup mode by specifying ":*" as your search pattern (i.e.
    ls -type mesh ":*" which lists those meshes defined in the root namespace only). Note that you can also use ":*" when relative name lookup mode is off to match the root if you want a consistent way to list the root.
    
    Listing child namespace contents:
    ls -type mesh "*:*";
    
    For an example to list all meshes in immediate child namespaces, use "*:*". In relative name lookup mode "*:*" lists those meshes in immediate child namespaces of the current namespaces. When not in relative name lookup mode, "*:*" lists meshes in namespaces one level below the root.
    
    Recursive listing of namespace contents:
    Example: ls -type mesh -recurse on "*"
    
    The 'recurse' flag is provided on the "ls" command to recursively traverse any child namespaces. In relative name lookup mode, the above example command will list all meshes in the current and any child namespaces of current. When not in relative name lookup mode, the above example command works from the root downwards and is thus equivalent to "ls -type mesh".

    Args:
        absoluteName | an: (create, query) - This is a general flag which can be used to specify the desired format for the namespace(s) returned by the command. The absolute name of the namespace is a full namespace path, starting from the root namespace ":" and including all parent namespaces.  For example ":ns:ball" is an absolute namespace name while "ns:ball" is not.
        addNamespace | add: (create) - Create a new namespace with the given name. Both qualified names ("A:B") and unqualified names ("A") are acceptable. If any of the higher-level namespaces in a qualified name do not yet exist, they will be created. If the supplied name contains invalid characters it will first be modified as per the validateName flag.
        collapseAncestors | ch: (create) - Delete all empty ancestors of the given namespace. An empty namespace is a a namespace that does not contain any objects or other nested namespaces
        deleteNamespaceContent | dnc: (create) - Used with the 'rm/removeNamespace' flag to indicate that when removing a namespace the contents of the namespace will also be removed.
        exists | ex: (create) - Returns true if the specified namespace exists, false if not.
        force | f: (create) - Used with 'mv/moveNamespace' to force the move operation to ignore name clashes.
        isRootNamespace | ir: (query) - Returns true if the specified namespace is root, false if not.
        mergeNamespaceWithOther | mno: (create) - Used with the 'rm/removeNamespace' flag. When removing a namespace, move the rest of the namespace content to the specified namespace.
        mergeNamespaceWithParent | mnp: (create) - Used with the 'rm/removeNamespace' flag. When removing a namespace, move the rest of the namespace content to the parent namespace.
        mergeNamespaceWithRoot | mnr: (create) - Used with the 'rm/removeNamespace' flag. When removing a namespace, move the rest of the namespace content to the root namespace.
        moveNamespace | mv: (create) - Move the contents of the first namespace into the second namespace. Child namespaces will also be moved.  Attempting to move a namespace containing referenced nodes will result in an error; use the 'file' command ('file -edit -namespace') to change a reference namespace.  If there are objects in the source namespace with the same name as objects in the destination namespace, an error will be issued. Use the 'force' flag to override this error - name clashes will be resolved by renaming the objects to ensure uniqueness.
        parent | p: (create) - Used with the 'addNamespace' or 'rename' flags to specifiy the parent of the new namespace. The full namespace parent path is required. When using 'addNamespace' with an absolute name, the 'parent' will be ignored and the command will display a warning
        recurse | r: (query) - Can be used with the 'exists' flag to recursively look for the specified namespace
        relativeNames | rel: (create, query) - Turns on relative name lookup, which causes name lookups within Maya to be relative to the current namespace. By default this is off, meaning that name lookups are always relative to the root namespace. Be careful turning this feature on since commands such as setAttr will behave differently. It is wise to only turn this feature on while executing custom procedures that you have written to be namespace independent and turning relativeNames off when returning control from your custom procedures. Note that Maya will turn on relative naming during file I/O. Although it is not recommended to leave relativeNames turned on, if you try to toggle the value during file I/O you may notice that the value stays "on" because Maya has already temporarily enabled it internally.  When relativeNames are enabled, the returns provided by the 'ls' command will be relative to the current namespace. See the main description of this command for more details.
        removeNamespace | rm: (create) - Deletes the given namespace.  The namespace must be empty for it to be deleted.
        rename | ren: (create) - Rename the first namespace to second namespace name. Child namespaces will also be renamed. Both names are relative to the current namespace. Use the 'parent' flag to specify a parent namespace for the renamed namespace. An error is issued if the second namespace name already exists. If the supplied name contains invalid characters it will first be modified as per the validateName flag.
        setNamespace | set: (create) - Sets the current namespace.
        validateName | vn: (create) - Convert the specified name to a valid name to make it contain no illegal characters. The leading illegal characters will be removed and other illegal characters will be converted to '_'. Specially, the leading numeric characters and trailing space characters will be also removed.  Full name path can be validated as well. However, if the namespace of the path does not exist, command will only return the base name. For example, ":nonExistentNS:name" will be converted to "name".  If the entire name consists solely of illegal characters, e.g. "123" which contains only leading digits, then the returned string will be empty.
    """
    ...


def namespaceInfo(*args, absoluteName: bool = ..., an: bool = ..., baseName: bool = ..., bn: bool = ..., currentNamespace: bool = ..., cur: bool = ..., dagPath: bool = ..., dp: bool = ..., fullName: bool = ..., fn: bool = ..., internal: bool = ..., int: bool = ..., isRootNamespace: bool = ..., ir: bool = ..., listNamespace: bool = ..., ls: bool = ..., listOnlyDependencyNodes: bool = ..., lod: bool = ..., listOnlyNamespaces: bool = ..., lon: bool = ..., parent: bool = ..., p: bool = ..., recurse: bool = ..., r: bool = ..., shortName: bool = ..., sn: bool = ...) -> Any:
    r"""
    This command displays information about a namespace. The target namespace can optionally be specified on the command line.
    If no namespace is specified, the command will display information about the current namespace.
    
    
    A namespace is a simple grouping of objects under a given name.
    Each item in a namespace can then be identified by its own name, along
    with what namespace it belongs to.  Namespaces can contain other
    namespaces like sets, with the restriction that all namespaces
    are disjoint.
    
    Namespaces are primarily used to resolve name-clash issues in Maya,
    where a new object has the same name as an existing object
    (from importing a file, for example).
    Using namespaces, you can have two objects with the same name, as long as
    they are contained in different namespaces.
    
    Note that namespaces are a simple grouping of names, so
    they do not effect selection, the DAG, the Dependency Graph, or any other
    aspect of Maya.  All namespace names are colon-separated.
    
    
    The namespace format flags are: baseName(shortName), fullName and absoluteName.
    The flags are used in conjunction with the main query flags to specify the desired namespace format of the returned result. They can also be used to return the different formats of a specified namespace.
    By default, when no format is specified, the result will be returned as a full name.

    Args:
        absoluteName | an: (create) - This is a general flag which can be used to specify the desired format for the namespace(s) returned by the command. The absolute name of the namespace is a full namespace path, starting from the root namespace ":" and including all parent namespaces.  For example ":ns:ball" is an absolute namespace name while "ns:ball" is not. The absolute namespace name is invariant and is not affected by the current namespace or relative namespace modes. See also other format modifiers 'baseName', 'fullName', etc
        baseName | bn: (create) - This is a general flag which can be used to specify the desired format for the namespace(s) returned by the command. The base name of the namespace contains only the leaf level name and does not contain its parent namespace(s). For example the base name of an object named "ns:ball" is "ball". This mode will always return the base name in the same manner, and is not affected by the current namespace or relative namespace mode. See also other format modifiers 'absoluteName', 'fullName', etc The flag 'shortName' is a synonym for 'baseName'.
        currentNamespace | cur: (create) - Display the name of the current namespace.
        dagPath | dp: (create) - This flag modifies the 'listNamespace' and 'listOnlyDependencyNodes' flags to indicate that the names of any dag objects returned will include as much of the dag path as is necessary to make the names unique. If this flag is not present, the names returned will not include any dag paths.
        fullName | fn: (create) - This is a general flag which can be used to specify the desired format for the namespace(s) returned by the command. The full name of the namespace contains both the namespace path and the base name, but without the leading colon representing the root namespace. For example "ns:ball" is a full name, whereas ":ns:ball" is an absolute name. This mode is affected by the current namespace and relative namespace modes. See also other format modifiers 'baseName', 'absoluteName', etc.
        internal | int: (create) - This flag is used together with the 'listOnlyDependencyNodes' flag. When this flag is set, the returned list will include internal nodes (for example itemFilters) that are not listed by default.
        isRootNamespace | ir: (create) - Returns true if the namespace is root(":"), false if not.
        listNamespace | ls: (create) - List the contents of the namespace.
        listOnlyDependencyNodes | lod: (create) - List all dependency nodes in the namespace.
        listOnlyNamespaces | lon: (create) - List all namespaces in the namespace.
        parent | p: (create) - Display the parent of the namespace. By default, the list returned will not include internal nodes (such as itemFilters). To include the internal nodes, use the 'internal' flag.
        recurse | r: (create) - Can be specified with 'listNamespace', 'listOnlyNamespaces' or 'listOnlyDependencyNode' to cause the listing to recursively include any child namespaces of the namespaces;
        shortName | sn: (create) - This flag is deprecated and may be removed in future releases of Maya. It is a synonym for the baseName flag. Please use the baseName flag instead.
    """
    ...


def ogs(*args, deviceInformation: bool = ..., di: bool = ..., disposeReleasableTextures: bool = ..., drt: bool = ..., dumpTexture: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., enableHardwareInstancing: bool = ..., hwi: bool = ..., fragmentEditor: Optional[Union[str, bool]] = ..., fe: Optional[Union[str, bool]] = ..., fragmentXML: Optional[Union[str, bool]] = ..., xml: Optional[Union[str, bool]] = ..., gpuMemoryTotal: Optional[Union[int, bool]] = ..., gmt: Optional[Union[int, bool]] = ..., gpuMemoryUsed: bool = ..., gpu: bool = ..., isLegacyViewportEnabled: bool = ..., lve: bool = ..., isRemoteGLSessionEnabled: bool = ..., rgl: bool = ..., isWinRemoteSession: bool = ..., irs: bool = ..., pause: bool = ..., p: bool = ..., rebakeTextures: bool = ..., rbt: bool = ..., regenerateUVTilePreview: Optional[Union[str, bool]] = ..., rup: Optional[Union[str, bool]] = ..., reloadTextures: bool = ..., rlt: bool = ..., reset: bool = ..., r: bool = ..., shaderSource: Optional[Union[str, bool]] = ..., ss: Optional[Union[str, bool]] = ..., toggleTexturePaging: bool = ..., ttp: bool = ..., traceRenderPipeline: bool = ..., trp: bool = ..., query: bool = ...) -> Any:
    r"""
    OGS is one of the viewport renderers. As there is a lot of effort involved
    in migrating functionality it will evolve over several releases. As it
    evolves it is prudent to provide safeguards to get the database back to a
    known state. That is the function of this command, similar to how
    'dgdirty' is used to restore state to the dependency graph.

    Args:
        deviceInformation | di: (create) - If used then output the current device information.
        disposeReleasableTextures | drt: (create) - Clear up all the releasable file textures in GPU memory that are not required for rendering.
        dumpTexture | dt: (create) - If used then dump GPU texture memory usage info (in MB), must be used with FLAG gpuMemoryUsed. The final info detail is specified by the string parameter. Current available values are: "full" , "total".
        enableHardwareInstancing | hwi: (create) - Enables/disables new gpu instancing of instanceable render items in OGS.
        fragmentEditor | fe: (create) - If used then launch the fragment editor UI.
        fragmentXML | xml: (create) - Get the fragment XML associated with a shading node.
        gpuMemoryTotal | gmt: (create, query) - Get or set the total amount of GPU memory which Maya is allowed to use (in MB).
        gpuMemoryUsed | gpu: (create) - If used then output the estimated amount of GPU memory in use (in MB).
        isLegacyViewportEnabled | lve: (query) - To query if the legacy viewport is enabled.
        isRemoteGLSessionEnabled | rgl: (query) - Query if remote gl is allowed
        isWinRemoteSession | irs: (query) - Query if this is a remote session.
        pause | p: (create, query) - Toggle pausing VP2 display update
        rebakeTextures | rbt: (create) - If used then re-bake all baked textures for OGS.
        regenerateUVTilePreview | rup: (create) - If used then regenerate all UV tiles preview textures for OGS.
        reloadTextures | rlt: (create) - If used then reload all textures for OGS.
        reset | r: (create, query) - If used then reset the entire OGS database for all viewports using it. In query mode the number of viewports that would be affected is returned but the reset is not actually done.  If no viewport is using OGS then OGS will stop listening to DG changes.
        shaderSource | ss: (query) - Get the shader source for the specified material.
        toggleTexturePaging | ttp: (create) - If used then toggle the default OGS Texture paging mechanism.
        traceRenderPipeline | trp: (create) - Enable debug tracing of the renderer pipeline.
    """
    ...


def openCLInfo(*args, limitMinimumVerts: bool = ..., lmv: bool = ..., minVertexBuffer: Optional[Union[int, bool]] = ..., mvb: Optional[Union[int, bool]] = ..., supportsDoublePrecision: bool = ..., dbl: bool = ..., valid: bool = ..., v: bool = ..., query: bool = ...) -> Any:
    r"""
    Query OpenCL information.

    Args:
        limitMinimumVerts | lmv: (create, query) - Specifies whether the limit on the minimum vert count of the geometry is used or not. The system configuration determines a certain minimum size for geometries to be allowed on GPU. When this flag is on this limit is obeyed. When this flag is off this limit is ignored. This is only used for debugging purposes and is not saved to the file or any preferences.
        minVertexBuffer | mvb: (create, query) - Set the minimum vert count under which the geometry will not be allowed on the GPU (unless in a network with qualifying geometries). This is only used for debugging purposes and is not saved to the file or any preferences.
        supportsDoublePrecision | dbl: (create, query) - Specifies whether double precision can be used in OpenCL. If the platform can not allow double precision this can not be set to "on".
        valid | v: (query) - Valid in query mode only. Checks if OpenCL is initialized.
    """
    ...


def openGLExtension(*args, extension: Optional[Union[str, bool]] = ..., ext: Optional[Union[str, bool]] = ..., renderer: bool = ..., rnd: bool = ..., vendor: bool = ..., vnd: bool = ..., version: bool = ..., ver: bool = ...) -> Any:
    r"""
    Command returns the extension name depending on whether a given
    OpenGL extension is supported or not. The input is the
    extension string to the -extension flag.
    If the -extension flag is not used, or if
    the string argument to this flag is an empty string
    than all extension names are returned in a single string.
    If the extension exists it is not necessary true that
    the extension is supported.
    This command can only be used when a modeling
    view has been created. Otherwise no extensions
    will have been initialized and the resulting
    string will always be the empty string.

    Args:
        extension | ext: (create) - Specifies the OpenGL extension to query.
        renderer | rnd: (create) - Specifies to query the OpenGL renderer.
        vendor | vnd: (create) - Specifies to query the company responsible for the OpenGL implementation.
        version | ver: (create) - Specifies to query the OpenGL version.
    """
    ...


def openMayaPref(*args, errlog: bool = ..., el: bool = ..., lazyLoad: bool = ..., lz: bool = ..., oldPluginWarning: bool = ..., ow: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Set or query API preferences.

    Args:
        errlog | el: (create, edit, query) - toggles whether or not an error log of failed API method calls will be created.  When set to true, a file called "OpenMayaErrorLog" will be created in Maya's current working directory.  Each time an API method fails, a detailed description of the error will be written to the file along with a mini-stack trace that indicates the routine that called the failing method. Defaults to false(off).
        lazyLoad | lz: (create, edit, query) - toggles whether or not plugins will be loaded with the RTLD_NOW flag or the RTLD_LAZY flag of dlopen(3C).  If set to true, RTLD_LAZY will be used.  In this mode references to functions that cannot be resolved at load time will not be considered an error.  However, if one of these symbols is actually dereferenced by the plug-in at run time, Maya will crash. Defaults to false(off).
        oldPluginWarning | ow: (create, edit, query) - toggles whether or not loadPlugin will generate a warning when plug-ins are loaded that were compiled against an older, and possibly incompatible Maya release. Defaults to true(on).
    """
    ...


def pluginDisplayFilter(*args, classification: Optional[Union[str, bool]] = ..., cls: Optional[Union[str, bool]] = ..., deregister: bool = ..., dr: bool = ..., exists: bool = ..., ex: bool = ..., label: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., listFilters: bool = ..., lf: bool = ..., register: bool = ..., r: bool = ..., query: bool = ...) -> Any:
    r"""
    Register, deregister or query a plugin display filter.
    Plug-ins can use this command to register their own display filters which
    will appear in the 'Show' menus on Maya's model panels.

    Args:
        classification | cls: (create, query) - The classification used to filter objects in Viewport 2.0. This classification is the same as MFnPlugin::registerNode(). If the node was registered with multiple classifications, use the one beginning with "drawdb". The default value of this flag is an empty string (""). It will not filter any objects in Viewport 2.0.
        deregister | dr: (create) - Deregister a plugin display filter.
        exists | ex: (create) - Returns true if the specified filter exists, false otherwise. Other flags are ignored.
        label | l: (create, query) - The string to be displayed for this filter in the UI. E.g. in the 'Show' menu of a model panel. The default value of this flag is the same as the plugin display filter name.
        listFilters | lf: (query) - Returns an array of all plugin display filters.
        register | r: (create) - Register a plugin display filter. The -register is implied if both -register and -deregister flags are missing in create mode. You are responsible for deregistering any filters which you register. Filters are reference counted, meaning that if you register the same filter twice then you will have to deregister it twice as well.
    """
    ...


def pluginInfo(*args, activeFile: bool = ..., af: bool = ..., allEvaluators: bool = ..., ae: bool = ..., animCurveInterp: Optional[Union[str, bool]] = ..., aci: Optional[Union[str, bool]] = ..., apiVersion: bool = ..., av: bool = ..., autoload: bool = ..., a: bool = ..., cacheFormat: bool = ..., cf: bool = ..., changedCommand: Optional[Union[str, bool]] = ..., cc: Optional[Union[str, bool]] = ..., command: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., constraintCommand: bool = ..., cnc: bool = ..., controlCommand: bool = ..., ctc: bool = ..., data: Optional[Union[Tuple[str, str], bool]] = ..., d: Optional[Union[Tuple[str, str], bool]] = ..., dependNode: bool = ..., dn: bool = ..., dependNodeByType: Optional[Union[str, bool]] = ..., dnt: Optional[Union[str, bool]] = ..., dependNodeId: Optional[Union[str, bool]] = ..., dni: Optional[Union[str, bool]] = ..., device: bool = ..., dv: bool = ..., dragAndDropBehavior: bool = ..., ddb: bool = ..., evaluator: bool = ..., e: bool = ..., iksolver: bool = ..., ik: bool = ..., listPlugins: bool = ..., ls: bool = ..., listPluginsPath: bool = ..., lsp: bool = ..., loadPluginPrefs: bool = ..., lpp: bool = ..., loaded: bool = ..., l: bool = ..., modelEditorCommand: bool = ..., mec: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., path: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., pluginsInUse: bool = ..., pu: bool = ..., referenceTranslators: bool = ..., rtr: bool = ..., registered: bool = ..., r: bool = ..., remove: bool = ..., rm: bool = ..., renderer: bool = ..., rdr: bool = ..., savePluginPrefs: bool = ..., spp: bool = ..., serviceDescriptions: bool = ..., sd: bool = ..., settings: bool = ..., set: bool = ..., tool: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ..., translator: bool = ..., tr: bool = ..., unloadOk: bool = ..., uo: bool = ..., userNamed: bool = ..., u: bool = ..., vendor: Optional[Union[str, bool]] = ..., vd: Optional[Union[str, bool]] = ..., version: bool = ..., v: bool = ..., writeRequires: bool = ..., wr: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command provides access to the plug-in registry of the
    application. It is used mainly to query the characteristics of
    registered plug-ins. Plugins automatically become registered the first
    time that they are loaded.
    
    The argument is either the internal name of the plug-in or the path to
    access it.

    Args:
        activeFile | af: (query) - Restricts the command to the active file only, not the entire scene. This only affects the dependNode/dn and pluginsInUse/pu flags. For use during export selected.
        allEvaluators | ae: (query) - Returns a string array containing the names of all of the evaluator types registered to any plug-in.
        animCurveInterp | aci: (query) - Returns a string array containing the names of all of the animation curve interpolators registered by this plug-in.
        apiVersion | av: (query) - Returns a string containing the version of the API that this plug-in was compiled with.  See the comments in MTypes.h for the details on how to interpret this value.
        autoload | a: (create, edit, query) - Sets whether or not this plug-in should be loaded every time the application starts up. Returns a boolean in query mode.
        cacheFormat | cf: (query) - Returns a string array containing the names of all of the registered geometry cache formats
        changedCommand | cc: (create) - Adds a callback that will get executed every time the plug-in registry changes. Any other previously registered callbacks will also get called.
        command | c: (multiuse, query) - Returns a string array containing the names of all of the normal commands registered by this plug-in. Constraint, control, context and model editor commands are not included.
        constraintCommand | cnc: (query) - Returns a string array containing the names of all of the constraint commands registered by this plug-in.
        controlCommand | ctc: (query) - Returns a string array containing the names of all of the control commands registered by this plug-in.
        data | d: (multiuse, query) - Returns a string array containing the names of all of the data types registered by this plug-in.
        dependNode | dn: (multiuse, query) - Returns a string array containing the names of all of the custom nodes types registered by this plug-in.
        dependNodeByType | dnt: (query) - Returns a string array of all registered node types within a specified class of nodes.  Each custom node type registered by a plug-in belongs to a more general class of node types as specified by its MPxNode::Type. The flag's argument is an MPxNode::Type as a string.  For example, if you want to list all registered Locator nodes, you should specify kLocatorNode as a argument to this flag.
        dependNodeId | dni: (query) - Returns an integer array containing the ids of all of the custom node types registered by this plug-in.
        device | dv: (query) - Returns a string array containing the names of all of the devices registered by this plug-in.
        dragAndDropBehavior | ddb: (query) - Returns a string array containing the names of all of the drag and drop behaviors registered by this plug-in.
        evaluator | e: (query) - Returns a string array containing the names of all of the evaluator types registered by this plug-in.
        iksolver | ik: (query) - Returns a string array containing the names of all of the ik solvers registered by this plug-in.
        listPlugins | ls: (query) - Returns a string array containing all the plug-ins that are currently loaded.
        listPluginsPath | lsp: (query) - Returns a string array containing the full paths of all the plug-ins that are currently loaded.
        loadPluginPrefs | lpp: (create) - Loads the plug-in preferences (ie. autoload) from pluginPrefs.mel into Maya.
        loaded | l: (query) - Returns a boolean specifying whether or not the plug-in is loaded.
        modelEditorCommand | mec: (query) - Returns a string array containing the names of all of the model editor commands registered by this plug-in.
        name | n: (query) - Returns a string containing the internal name by which the plug-in is registered.
        path | p: (query) - Returns a string containing the absolute path name to the plug-in.
        pluginsInUse | pu: (query) - Returns a string array containing all the plug-ins that are currently being used in the scene.
        referenceTranslators | rtr: (query) - If this flag is used in conjunction with the pluginsInUse/pu flag then it will modify the output. When true it will only show plug-ins currently in use containing translators that are used to load referenced files. When false it will only show plug-ins not containing such translators.
        registered | r: (query) - Returns a boolean specifying whether or not plug-in is currently registered with the system.
        remove | rm: (edit) - Removes the given plug-in's record from the registry. There is no return value.
        renderer | rdr: (query) - Returns a string array containing the names of all of the renderers registered by this plug-in.
        savePluginPrefs | spp: (create) - Saves the plug-in preferences (ie. autoload) out to pluginPrefs.mel
        serviceDescriptions | sd: (query) - If there are services in use, then this flag will return a string array containing short descriptions saying what those services are.
        settings | set: (query) - Returns an array of values with the loaded, autoload, registered flags
        tool | t: (multiuse, query) - Returns a string array containing the names of all of the tool contexts registered by this plug-in.
        translator | tr: (query) - Returns a string array containing the names of all of the file translators registered by this plug-in.
        unloadOk | uo: (query) - Returns a boolean that specifies whether or not the plug-in can be safely unloaded.  It will return false if the plug-in is currently in use.  For example, if the plug-in adds a new dependency node type, and an instance of that node type is present in the scene, then this query will return false.
        userNamed | u: (query) - Returns a boolean specifying whether or not the plug-in has been assigned a name by the user.
        vendor | vd: (query) - Returns a string containing the vendor of the plug-in.
        version | v: (query) - Returns a string containing the version the plug-in.
        writeRequires | wr: (create, edit, query) - Sets whether or not this plug-in should write "requires" command into the saved file. "requires" command could autoload the plug-in when you open or import that saved file. This way, Maya will load the plug-in when a file is being loaded for some specified reason, such as to create a customized UI or to load some plug-in data that is not saved in any node or attributes. For example, "stereoCamera" is using this flag for its customized UI.
    """
    ...


def preloadRefEd(*args, control: bool = ..., ctl: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., exists: bool = ..., ex: bool = ..., filter: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., fmc: Optional[Union[str, bool]] = ..., highlightConnection: Optional[Union[str, bool]] = ..., hlc: Optional[Union[str, bool]] = ..., lockMainConnection: bool = ..., lck: bool = ..., mainListConnection: Optional[Union[str, bool]] = ..., mlc: Optional[Union[str, bool]] = ..., panel: Optional[Union[str, bool]] = ..., pnl: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., selectCommand: Optional[Union[str, bool]] = ..., sc: Optional[Union[str, bool]] = ..., selectFileNode: bool = ..., sf: bool = ..., selectionConnection: Optional[Union[str, bool]] = ..., slc: Optional[Union[str, bool]] = ..., stateString: bool = ..., sts: bool = ..., unParent: bool = ..., up: bool = ..., unlockMainConnection: bool = ..., ulk: bool = ..., updateMainConnection: bool = ..., upd: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This creates an editor for managing which references will be read in
    (loaded) and which deferred (unloaded) upon opening a file.

    Args:
        control | ctl: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag | dtg: (create, edit, query) - Attaches a tag to the editor.
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        filter | f: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        forceMainConnection | fmc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        highlightConnection | hlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        lockMainConnection | lck: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        mainListConnection | mlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        panel | pnl: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent | p: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        selectCommand | sc: (create, edit, query) - A script to be executed when an item is selected.
        selectFileNode | sf: (query) - Query the currently selected load setting. Returns the id of the currently selected load setting. This id can be used as an argument to the selLoadSettings command.
        selectionConnection | slc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        stateString | sts: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        unParent | up: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection | ulk: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection | upd: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
    """
    ...


def profiler(*args, addCategory: Optional[Union[str, bool]] = ..., a: Optional[Union[str, bool]] = ..., allCategories: bool = ..., ac: bool = ..., bufferSize: Optional[Union[int, bool]] = ..., b: Optional[Union[int, bool]] = ..., categoryIndex: Optional[Union[int, bool]] = ..., ci: Optional[Union[int, bool]] = ..., categoryIndexToName: Optional[Union[int, bool]] = ..., cin: Optional[Union[int, bool]] = ..., categoryInfo: Optional[Union[str, bool]] = ..., cf: Optional[Union[str, bool]] = ..., categoryName: Optional[Union[str, bool]] = ..., cn: Optional[Union[str, bool]] = ..., categoryNameToIndex: Optional[Union[str, bool]] = ..., cni: Optional[Union[str, bool]] = ..., categoryRecording: bool = ..., cr: bool = ..., clearAllMelInstrumentation: bool = ..., cam: bool = ..., colorIndex: Optional[Union[int, bool]] = ..., coi: Optional[Union[int, bool]] = ..., eventCPUId: bool = ..., eci: bool = ..., eventCategory: bool = ..., eca: bool = ..., eventColor: bool = ..., eco: bool = ..., eventCount: bool = ..., ec: bool = ..., eventDescription: bool = ..., ed: bool = ..., eventDuration: bool = ..., edu: bool = ..., eventIndex: Optional[Union[int, bool]] = ..., ei: Optional[Union[int, bool]] = ..., eventName: bool = ..., en: bool = ..., eventStartTime: bool = ..., et: bool = ..., eventThreadId: bool = ..., eti: bool = ..., instrumentMel: bool = ..., load: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., output: Optional[Union[str, bool]] = ..., o: Optional[Union[str, bool]] = ..., procedureDescription: Optional[Union[str, bool]] = ..., pd: Optional[Union[str, bool]] = ..., procedureName: Optional[Union[str, bool]] = ..., pn: Optional[Union[str, bool]] = ..., removeCategory: Optional[Union[str, bool]] = ..., rc: Optional[Union[str, bool]] = ..., reset: bool = ..., r: bool = ..., sampling: bool = ..., s: bool = ..., signalEvent: bool = ..., sig: bool = ..., signalMelEvent: bool = ..., sim: bool = ..., query: bool = ...) -> Any:
    r"""
    The profiler is used to record timing information from key events within Maya,
    as an aid in tuning the performance of scenes, scripts and plug-ins.
    User written plug-ins and Python scripts can also generate profiling information
    for their own code through the MProfilingScope (C++), MProfilingContextManager
    (Python) and MProfiler classes in the API.
    
    This command provides the ability to control the collection of profiling data and
    to query information about the recorded events. The recorded information can also
    be viewed graphically in the Profiler window.
    
    The buffer size cannot be changed while sampling is active, it will return an error
    The reset flag cannot be called while sampling is active, it will return an error.
    Any changes to the buffer size will only be applied on start of the next recording.
    You can't save and load in the same command, save has priority, load would be ignored.

    Args:
        addCategory | a: (create) - Add a new category for the profiler. Returns the index of the new category.
        allCategories | ac: (query) - Query the names of all categories. If the categoryInfo flag is set then alternate the name of the category with the description of the category.
        bufferSize | b: (create, query) - Toggled : change the buffer size to fit the specified number of events (requires that sampling is off) Query : return the current buffer size The new buffer size will only take effect when next sampling starts. When the buffer is full, the recording stops.
        categoryIndex | ci: (create, query) - Used in conjunction with other flags, to indicate the index of the category. 			In query mode, this flag needs a value.
        categoryIndexToName | cin: (create, query) - Returns the name of the category with a given index. 			In query mode, this flag needs a value.
        categoryInfo | cf: (create, query) - When used with the addCategory flag set the description of the added profiler category. In query mode return the description of the category referenced by either the categoryIndex or categoryName flags. 			In query mode, this flag can accept a value.
        categoryName | cn: (query) - Used in conjunction with other flags, to indicate the name of the category. 			In query mode, this flag needs a value.
        categoryNameToIndex | cni: (create, query) - Returns the index of the category with a given name. 			In query mode, this flag needs a value.
        categoryRecording | cr: (create, query) - Toggled : Enable/disable the recording of the category. Query : return if the recording of the category is On. Requires the -categoryIndex or -categoryName flag to specify the category to be queried.
        clearAllMelInstrumentation | cam: (create) - Clear all MEL command or procedure instrumentation.
        colorIndex | coi: (create) - Used with "-instrumentMel true" to specify the color index to show the profiling result.
        eventCPUId | eci: (query) - Query the CPU ID of the event at the given index. Requires the -eventIndex flag to specify the event to be queried.
        eventCategory | eca: (query) - Query the category index the event at the given index belongs to. Requires the -eventIndex flag to specify the event to be queried.
        eventColor | eco: (query) - Query the color of the event at the given index. Requires the -eventIndex flag to specify the event to be queried.
        eventCount | ec: (query) - Query the number of events in the buffer
        eventDescription | ed: (query) - Query the description of the event at the given index. Requires the -eventIndex flag to specify the event to be queried.
        eventDuration | edu: (query) - Query the duration of the event at the given index, the time unit is microsecond. Note that a signal event has a 0 duration. Requires the -eventIndex flag to specify the event to be queried.
        eventIndex | ei: (query) - Used usually in conjunction with other flags, to indicate the index of the event. 			In query mode, this flag needs a value.
        eventName | en: (query) - Query the name of the event at the given index. Requires the -eventIndex flag to specify the event to be queried.
        eventStartTime | et: (query) - Query the time of the event at the given index, the time unit is microsecond. Requires the -eventIndex flag to specify the event to be queried.
        eventThreadId | eti: (query) - Query the thread ID of the event at the given index. Requires the -eventIndex flag to specify the event to be queried.
        instrumentMel | instrumentMel: (create) - Enable/Diable the instrumentation of a MEL command or procedure. When the instrumentation is enabled, the execution of MEL command or procedure can be profiled and shown in the Profiler window. To enable the instrumentation requires the -procedureName, -colorIndex and -categoryIndex flags. To disable the instrumentation requires the -procedureName flag.
        load | l: (create, query) - Read the recorded events from the specified file
        output | o: (create, query) - Output the recorded events to the specified file
        procedureDescription | pd: (create) - Used with "-instrumentMel true" to provide a description of the MEL command or procedure being instrumented. This description can be viewed in the Profiler Tool window.
        procedureName | pn: (create) - Used with -instrumentMel to specify the name of the procedure to be enabled/disabled the instrumentation.
        removeCategory | rc: (create) - Remove an existing category for the profiler. Returns the index of the removed category.
        reset | r: (create, query) - reset the profiler's data (requires that sampling is off)
        sampling | s: (create, query) - Toggled : Enable/disable the recording of events Query : return if the recording of events is On.
        signalEvent | sig: (query) - Query if the event at the given index is a signal event. Requires the -eventIndex flag to specify the event to be queried. A Signal Event only remembers the start moment and has no knowledge about duration. It can be used in cases when the user does not care about the duration but only cares if this event does happen.
        signalMelEvent | sim: (create) - Used with "-instrumentMel true", inform profiler that this instrumented MEL command or procedure will be taken as a signal event during profiling. A Signal Event only remembers the start moment and has no knowledge about duration. It can be used in cases when the user does not care about the duration but only cares if this event does happen.
    """
    ...


def profilerTool(*args, categoryView: bool = ..., cat: bool = ..., collapseSelectedEvents: bool = ..., cs: bool = ..., collapseSelectedEventsRepetition: bool = ..., csr: bool = ..., cpuView: bool = ..., cpu: bool = ..., destroy: bool = ..., dtr: bool = ..., eventTypes: bool = ..., et: bool = ..., exists: bool = ..., ex: bool = ..., expandSelectedEvents: bool = ..., es: bool = ..., expandSelectedEventsRepetition: bool = ..., esr: bool = ..., findNext: bool = ..., fn: bool = ..., findPrevious: bool = ..., fp: bool = ..., frameAll: bool = ..., fa: bool = ..., frameSelected: bool = ..., fs: bool = ..., isolateSegment: int = ..., make: bool = ..., mk: bool = ..., matchWholeWord: bool = ..., mww: bool = ..., searchEvent: Optional[Union[str, bool]] = ..., se: Optional[Union[str, bool]] = ..., segmentCount: bool = ..., sc: bool = ..., showAllEvent: bool = ..., sa: bool = ..., showCriticalPath: bool = ..., scp: bool = ..., showHotspot: bool = ..., sh: bool = ..., showSelectedEvents: bool = ..., ss: bool = ..., showSelectedEventsRepetition: bool = ..., ssr: bool = ..., threadView: bool = ..., thd: bool = ..., unisolateSegment: bool = ..., uis: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This script is intended to be used by the profilerPanel to interact with the profiler tool's view (draw region).
    It can be used to control some behaviors about the profiler Tool.

    Args:
        categoryView | cat: (edit) - Change view mode to category view
        collapseSelectedEvents | cs: (edit) - Hide all sub-events of selected events so that only top-level events show
        collapseSelectedEventsRepetition | csr: (edit) - Hide all sub-events repetition of selected events based on their comment
        cpuView | cpu: (edit) - Change view mode to cpu view
        destroy | dtr: (create) - Destroy the profiler tool Internal flag. Should not be used by user.
        eventTypes | et: (query) - Return JSON data containing the list of event types on currently existing events. If the value of the flag is true then show only event types for selected events, otherwise show them for all events.  The JSON return string will contain the event type information in the following format:  {     "eventSummary" : [         { "type"        : EVENT_TYPE_NAME,         , "description" : EVENT_TYPE_DESCRIPTION,         , "color"       : [ RED_AS_FLOAT, GREEN_AS_FLOAT, BLUE_AS_FLOAT ]         , "category"    : CATEGORY_NAME         , "count"       : EVENT_TYPE_COUNT         }     ] }  "type" and "description" may be omitted, indicating that the results correspond to anonymous events.
        exists | ex: (query) - Query if the profiler tool view exists. Profiler tool can only exist after "profilerTool -make" is called.
        expandSelectedEvents | es: (edit) - Show all sub-events of selected events
        expandSelectedEventsRepetition | esr: (edit) - Show all sub-events repetition of selected events based on their comment
        findNext | fn: (query) - This flag is used along with flag -searchEvent.
        findPrevious | fp: (query) - This flag is used along with flag -searchEvent.
        frameAll | fa: (edit) - Frame on all events in the profilerToolView
        frameSelected | fs: (edit) - Frame on all selected events in the profilerToolView
        isolateSegment | isolateSegment: (edit) - Isolate a specified segment. A segment is a set of events that happened in one animation frame. You can use flag -segmentCount to query the number of segments in the event buffer. The segment index starts from 0. If the specified segment does not exist, an error will be thrown.
        make | mk: (create) - Make the profiler tool and parent it to the most recent layout created Internal flag. Should not be used by user.
        matchWholeWord | mww: (edit) - Tells profiler tool if it should match whole word when searching event(s). The default value is false.
        searchEvent | se: (query) - Search event(s). You can set -matchWholeWord before you use -searchEvent. If -matchWholeWord has been set to true, the profiler tool will search event(s) whose name exactly matches with the string. If -matchWholeWord has been set to false, the profiler tool will search event(s) whose name contains the string. If -findNext is also used along with this flag, the profiler tool will find the first event next to the current selected event. If -findPrevious is also used along with this flag, the profiler tool will find the first event previous to the current selected event. If currently don't have a selected event or there are multiple selected events, the search will start at the first event in profiler buffer. If -findNext and -findPrevious are not used along with this flag, the profiler tool will find all events. 			In query mode, this flag needs a value.
        segmentCount | sc: (query) - Returns the number of segments in the event buffer.
        showAllEvent | sa: (edit) - Show all events (if events were hidden by filtering) (true) or Hide all events (false)
        showCriticalPath | scp: (edit) - Show critical path of selected frame
        showHotspot | sh: (edit) - Show hotspot of selected frame
        showSelectedEvents | ss: (edit) - Show only the selected events (true) or hide all selected events (false)
        showSelectedEventsRepetition | ssr: (edit) - Show only the selected events repetition based on their comment (true) or Hide all selected events repetition based on their comment (false)
        threadView | thd: (edit) - Change view mode to thread view
        unisolateSegment | uis: (edit) - Unisolate current isolated segment. If no segment is currently isolated, nothing will happen.
    """
    ...


def recordAttr(*args, attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., delete: bool = ..., d: bool = ..., query: bool = ...) -> Any:
    r"""
    This command sets up an attribute to be recorded.  When
    the record command is executed, any changes to this attribute
    are recorded.  When recording stops these changes are turned
    into keyframes.
    
    If no attributes are specified all attributes of the node
    are recorded.
    
    When the query flag is used, a list of the attributes being recorded will be returned.

    Args:
        attribute | at: (create, multiuse) - specify the attribute to record
        delete | d: (create) - Do not record the specified attributes
    """
    ...


def redo(*args) -> Any:
    r"""
    Takes the most recently undone command from the undo list
    and redoes it.

    Args:
    """
    ...


def referenceEdit(*args, applyFailedEdits: bool = ..., afe: bool = ..., changeEditTarget: Optional[Union[Tuple[str, str], bool]] = ..., cet: Optional[Union[Tuple[str, str], bool]] = ..., failedEdits: bool = ..., fld: bool = ..., removeEdits: bool = ..., r: bool = ..., successfulEdits: bool = ..., scs: bool = ..., editCommand: Optional[Union[str, bool]] = ..., ec: Optional[Union[str, bool]] = ..., onReferenceNode: Optional[Union[str, bool]] = ..., orn: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Use this command to remove and change the modifications which have
    been applied to references. A valid commandTarget is either a reference node,
    a reference file, a node in a reference, or a plug from a reference.
    Only modifications that have been made from the currently open scene can
    be changed or removed. The 'referenceQuery -topReference' command can be used
    to determine what modifications have been made to a given commandTarget.
    Additionally only unapplied edits will be affected. Edits are unapplied
    when the node(s) which they affect are unloaded, or when they could
    not be successfully applied. By default this command only works on failed
    edits (this can be adjusted using the "-failedEdits" and
    "-successfulEdits" flags).
    Specifying a reference node as the command target is equivalent to
    specifying every node in the target reference file as a target. In this
    situation the results may differ depending on whether the target
    reference is loaded or unloaded. When it is unloaded, edits that affect both
    a node in the target reference and a node in one of its descendant references
    may be missed (e.g. those edits may not be removed). This is because when a
    reference is unloaded Maya no longer retains detailed information about which
    nodes belong to it. However, edits that only affect nodes in the target reference
    or in one of its ancestral references should be removed as expected.
    When the flags -removeEdits and -editCommand are used together, by default
    all connectAttr edits are removed from the specified source object. To remove
    only edits that connect to a specific target object, the target object can be
    passed as an additional argument to the command. This narrows the match criteria,
    so that only edits that connect the source object to the provided target in this
    additional argument are removed. See the example below.
    NOTE:
    When specifying a plug it is important to use the appropriate long attribute
    name.

    Args:
        applyFailedEdits | afe: (create) - Attempts to apply any unapplied edits. This flag is useful if previously failing edits have been fixed using the -changeEditTarget flag. This flag can only be used on loaded references. If the command target is a referenced node, the associated reference is used instead.
        changeEditTarget | cet: (create) - Used to change a target of the specified edits. This flag takes two parameters: the old target of the edits, and the new target to change it to. The target can either be a node name ("node"), a node and attribute name ("node.attr"), or just an attribute name (".attr"). If an edit currently affects the old target, it will be changed to affect the new target. Flag 'referenceQuery' should be used to determine the format of the edit targets. As an example most edits store the long name of the attribute (e.g. "translateX"), so when specifying the old target, a long name must also be used. If the short name is specified (e.g. "tx"), chances are the edit won't be retargeted.
        failedEdits | fld: (create) - This is a secondary flag used to indicate whether or not failed edits should be acted on (e.g. queried, removed, etc...). A failed edit is an edit which could not be successfully applied the last time its reference was loaded. An edit can fail for a variety of reasons (e.g. the referenced node to which it applies was removed from the referenced file). By default failed edits will be acted on.
        removeEdits | r: (create) - Remove edits which affect the specified unloaded commandTarget.
        successfulEdits | scs: (create) - This is a secondary flag used to indicate whether or not successful edits should be acted on (e.g. queried, removed, etc...). A successful edit is any edit which was successfully applied the last time its reference was loaded. This flag will have no affect if the commandTarget is loaded. By default successful edits will not be acted on.
        editCommand | ec: (create, multiuse, query) - This is a secondary flag used to indicate which type of reference edits should be considered by the command. If this flag is not specified all edit types will be included. This flag requires a string parameter. Valid values are: "addAttr", "connectAttr", "deleteAttr", "disconnectAttr", "parent", "setAttr", "lock" and "unlock". In some contexts, this flag may be specified more than once to specify multiple edit types to consider.
        onReferenceNode | orn: (create, multiuse, query) - This is a secondary flag used to indicate that only those edits which are stored on the indicated reference node should be considered. This flag only supports multiple uses when specified with the "exportEdits" command.
    """
    ...


def referenceQuery(*args, child: bool = ..., ch: bool = ..., isExportEdits: bool = ..., iee: bool = ..., isLoaded: bool = ..., il: bool = ..., liveEdits: bool = ..., le: bool = ..., dagPath: bool = ..., dp: bool = ..., editAttrs: bool = ..., ea: bool = ..., editNodes: bool = ..., en: bool = ..., editStrings: bool = ..., es: bool = ..., failedEdits: bool = ..., fld: bool = ..., filename: bool = ..., f: bool = ..., isNodeReferenced: bool = ..., inr: bool = ..., isPreviewOnly: bool = ..., ipo: bool = ..., namespace: bool = ..., ns: bool = ..., nodes: bool = ..., n: bool = ..., parent: bool = ..., p: bool = ..., parentNamespace: bool = ..., pns: bool = ..., referenceNode: bool = ..., rfn: bool = ..., shortName: bool = ..., shn: bool = ..., showDagPath: bool = ..., sdp: bool = ..., showFullPath: bool = ..., sfp: bool = ..., showNamespace: bool = ..., sns: bool = ..., successfulEdits: bool = ..., scs: bool = ..., topReference: bool = ..., tr: bool = ..., unresolvedName: bool = ..., un: bool = ..., withoutCopyNumber: bool = ..., wcn: bool = ..., editCommand: Optional[Union[str, bool]] = ..., ec: Optional[Union[str, bool]] = ..., onReferenceNode: Optional[Union[str, bool]] = ..., orn: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Use this command to find out information about references and referenced nodes.
    A valid target is either a reference node, a reference file, or a referenced node.
    Some flags don't require a target, see flag descriptions for more information
    on what effect this has.
    When a scene contains multiple levels of file references, those edits which
    affect a nested reference may be stored on several different reference nodes.
    For example:
    A.ma has a reference to B.ma which has a reference to C.ma which contains
    a poly sphere (pSphere1).
    If you were to open B.ma and translate the sphere, an edit would be stored
    on CRN which refers to a node named "C:pSphere1".
    If you were then to open A.ma and parent the sphere, an edit would be
    stored on BRN which refers to a node named "B:C:pSphere1".
    It is important to note that when querying edits which affect a nested
    reference, the edits will be returned in the same format that they were
    applied. In the above example, opening A.ma and querying all edits which affect
    C.ma, would return two edits a parent edit affecting "B:C:pSphere1", and a
    setAttr edit affecting "C:pSphere1". Since there is currently no node named
    C:pSphere1 (only B:C:pSphere1) care will have to be taken when interpreting the
    returned information.
    The same care should be taken when referenced DAG nodes have been parented or
    instanced. Continuing with the previous example, let's say that you were to
    open A.ma and, instead of simply parenting pSphere1, you were to instance it.
    While A.ma is open, "B:C:pSphere1" may now be an amibiguous name, replaced by
    "|B:C:pSphere1" and "group1|B:C:pSphere1". However querying the edits which
    affect C.ma would still return a setAttr edit affecting "C:pSphere1" since it
    was applied prior to B:C:pSphere1 being instanced.
    Some tips:
    1. Use the '-topReference' flag to query only those edits which were applied
       from the currently open file.
    2. Use the '-onReferenceNode' flag to limit the results to those edits where
       are stored on a given reference node. You can then use various string
       manipulation techniques to extrapolate the current name of any affected
       nodes.

    Args:
        child | ch: (create) - This flag modifies the '-rfn/-referenceNode' and '-f/-filename' flags to indicate the the children of the target reference will be returned. Returns a string array.
        isExportEdits | iee: (create) - Returns a boolean indicating whether the specified reference node or file name is an edits file (created with the Export Edits feature)
        isLoaded | il: (create) - Returns a boolean indicating whether the specified reference node or file name refers to a loaded or unloaded reference.
        liveEdits | le: (create) - Specifies that the edits should be returned based on the live edits database. Only valid when used in conjunction with the editStrings flag.
        dagPath | dp: (create) - This flag modifies the '-n/-nodes' flag to indicate that the names of any dag objects returned will include as much of the dag path as is necessary to make the names unique. If this flag is not present, the names returned will not include any dag paths.
        editAttrs | ea: (create) - Returns string array. A main flag used to query the edits that have been applied to the target. Only the names of the attributes involved in the reference edit will be returned. If an edit involves multiple attributes (e.g. "connectAttr" edits) the nodes will be returned as separate, consecutive entries in the string array. A valid target is either a reference node, a reference file, or a referenced node. If a referenced node is specified, only those edits which affect that node will be returned. If a reference file or reference node is specified any edit which affects a node in that reference will be returned. If no target is specified all edits are returned. This command can be used on both loaded and unloaded references. By default it will return all the edits, formatted as MEL commands, which apply to the target. This flag can be used in combination with the '-ea/-editAttrs' flag to indicate that the names of both the involved nodes and attributes will be returned in the format 'node.attribute'.
        editNodes | en: (create) - Returns string array. A main flag used to query the edits that have been applied to the target. Only the names of the nodes involved in the reference edit will be returned. If an edit involves multiple nodes (e.g. "connectAttr" edits) the nodes will be returned as separate, consecutive entries in the string array. A valid target is either a reference node, a reference file, or a referenced node. If a referenced node is specified, only those edits which affect that node will be returned. If a reference file or reference node is specified any edit which affects a node in that reference will be returned. If no target is specified all edits are returned. This command can be used on both loaded and unloaded references. By default it will return all the edits, formatted as MEL commands, which apply to the target. This flag can be used in combination with the '-ea/-editAttrs' flag to indicate that the names of both the involved nodes and attributes will be returned in the format 'node.attribute'.
        editStrings | es: (create) - Returns string array. A main flag used to query the edits that have been applied to the target. The edit will be returned as a valid MEL command. A valid target is either a reference node, a reference file, or a referenced node. If a referenced node is specified, only those edits which affect that node will be returned. If a reference file or reference node is specified any edit which affects a node in that reference will be returned. If no target is specified all edits are returned. This command can be used on both loaded and unloaded references. By default it will return all the edits, formatted as MEL commands, which apply to the target. This flag cannot be used with either the '-en/-editNodes' or '-ea/-editAttrs' flags.
        failedEdits | fld: (create) - This is a secondary flag used to indicate whether or not failed edits should be acted on (e.g. queried, removed, etc...). A failed edit is an edit which could not be successfully applied the last time its reference was loaded. An edit can fail for a variety of reasons (e.g. the referenced node to which it applies was removed from the referenced file). By default failed edits will not be acted on.
        filename | f: (create) - Returns string. A main flag used to query the filename associated with the target reference.
        isNodeReferenced | inr: (create) - Returns boolean. A main flag used to determine whether or not the target node comes from a referenced file. true if the target node comes from a referenced file, false if not.
        isPreviewOnly | ipo: (create) - Returns boolean. This flag is used to determine whether or not the target reference node is only a preview reference node.
        namespace | ns: (create) - Returns string. This flag returns the full namespace path of the target reference, starting from the root namespace ":". It can be combined with the shortName flag to return just the base name of the namespace.
        nodes | n: (create) - Returns string array. A main flag used to query the contents of the target reference.
        parent | p: (create) - This flag modifies the '-rfn/-referenceNode' and '-f/-filename' flags to indicate the the parent of the target reference will be returned.
        parentNamespace | pns: (create) - A main flag used to query and return the parent namespace of the target reference.
        referenceNode | rfn: (create) - Returns string. A main flag used to query the reference node associated with the target reference.
        shortName | shn: (create) - This flag modifies the '-f/-filename' and '-ns/-namespace' flags. Used with the '-f/-filename' flag indicates that the file name returned will be the short name (i.e. just a file name without any directory paths). If this flag is not present, the full name and directory path will be returned. Used with the '-ns/-namespace' flag indicates that the namespace returned will be the base name of the namespace. (i.e. the base name of the full namespace path ":AAA:BBB:CCC" is "CCC"  )
        showDagPath | sdp: (create) - Shows/hides the full dag path for edits. If false only displays the node-name of reference edits. Must be used with the -editNodes, -editStrings or -editAttrs flag.
        showFullPath | sfp: (create) - Return the full path from the root namespace for reference edits. Must be used with the -editNodes, -editStrings or -editAttrs flags.
        showNamespace | sns: (create) - Shows/hides the namespaces on nodes in the reference edits. Must be used with the -editNodes, -editStrings or -editAttrs flag
        successfulEdits | scs: (create) - This is a secondary flag used to indicate whether or not successful edits should be acted on (e.g. queried, removed, etc...). A successful edit is any edit which was successfully applied the last time its reference was loaded. By default successful edits will be acted on.
        topReference | tr: (create) - This flag modifies the '-rfn/-referenceNode' flag to indicate the top level ancestral reference of the target reference will be returned.
        unresolvedName | un: (create) - This flag modifies the '-f/-filename' flag to indicate that the file name returned will be unresolved (i.e. it will be the path originally specified when the file was loaded into Maya; this path may contain environment variables and may not exist on disk). If this flag is not present, the resolved name will     be returned.
        withoutCopyNumber | wcn: (create) - This flag modifies the '-f/-filename' flag to indicate that the file name returned will not have a copy number (e.g. '{1}') appended to the end. If this flag is not present, the file name returned may have a copy number appended to the end.
        editCommand | ec: (create, multiuse, query) - This is a secondary flag used to indicate which type of reference edits should be considered by the command. If this flag is not specified all edit types will be included. This flag requires a string parameter. Valid values are: "addAttr", "connectAttr", "deleteAttr", "disconnectAttr", "parent", "setAttr", "lock" and "unlock". In some contexts, this flag may be specified more than once to specify multiple edit types to consider.
        onReferenceNode | orn: (create, multiuse, query) - This is a secondary flag used to indicate that only those edits which are stored on the indicated reference node should be considered. This flag only supports multiple uses when specified with the "exportEdits" command.
    """
    ...


def reloadImage(*args) -> Any:
    r"""
    This command reloads an xpm image from disk. This can be used when the
    file has changed on disk and needs to be reloaded.
    
    The first string argument is the file name of the .xpm file. The
    second string argument is the name of a control using the specified
    pixmap.

    Args:
    """
    ...


def requires(*args, dataType: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., nodeType: Optional[Union[str, bool]] = ..., nt: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This command is used during file I/O to specify the requirements
    needed to load the given file.  It defines what file format
    version was used to write the file, or what plug-ins are required to
    load the scene.
    
    The first string names a product (either "maya", or a plug-in name)
    
    The second string gives the version. This command is only useful during
    file I/O, so users should not have any need to use this command themselves.
    
    The flags "-nodeType" and "-dataType" specify the node types
    and data types defined by the plug-in. When Maya open a scene file, it
    runs "requires" command in the file and load required plug-ins. But some
    plug-ins may be not loaded because they are missing. The flags "-nodeType"
    and "-dataType" are used by the missing plug-ins. If one plug-in is missing,
    nodes and data created by this plug-in are created as unknown nodes and
    unknown data. Maya records their original types for these unknown nodes
    and data. When these nodes and data are saved back to file, it will be
    possible to determine the associated missing plug-ins. And when export
    selected nodes, Maya can write out the exact required plug-ins.
    The flags "-nodeType" and "-dataType" is optional. In this command, if these
    flags are not given for one plug-in and the plug-in is missing, the "requires"
    command of this plug-in will always be saved back.

    Args:
        dataType | dt: (create, multiuse) - Specify a data type defined by this plug-in. The data type is specified by MFnPlugin::registerData() when register the plug-in.
        nodeType | nt: (create, multiuse) - Specify a node type defined by this plug-in. The node type is specified by MFnPlugin::registerNode() when register the plug-in.
    """
    ...


def saveImage(*args, annotation: Optional[Union[str, bool]] = ..., ann: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., bgc: Optional[Union[Tuple[float, float, float], bool]] = ..., currentView: bool = ..., cv: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dgc: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., dpc: Optional[Union[str, bool]] = ..., enable: bool = ..., en: bool = ..., enableBackground: bool = ..., ebg: bool = ..., enableKeyboardFocus: bool = ..., ekf: bool = ..., exists: bool = ..., ex: bool = ..., fullPathName: bool = ..., fpn: bool = ..., height: Optional[Union[int, bool]] = ..., h: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., hlc: Optional[Union[Tuple[float, float, float], bool]] = ..., image: Optional[Union[str, bool]] = ..., i: Optional[Union[str, bool]] = ..., isObscured: bool = ..., io: bool = ..., manage: bool = ..., m: bool = ..., noBackground: bool = ..., nbg: bool = ..., numberOfPopupMenus: bool = ..., npm: bool = ..., objectThumbnail: str = ..., ot: str = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., pma: bool = ..., preventOverride: bool = ..., po: bool = ..., sceneFile: str = ..., sf: str = ..., statusBarMessage: Optional[Union[str, bool]] = ..., sbm: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., visible: bool = ..., vis: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., vcc: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., w: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a static image for non-xpm files.
    Any image file format supported by the file texture node is supported by
    this command.
    
    This command creates a static image control for non-xpm files used to
    display a thumbnail image of the scene file.

    Args:
        annotation | ann: (create, edit, query) - Annotate the control with an extra string value.
        backgroundColor | bgc: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        currentView | cv: (edit) - Generate the image from the current view.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag | dtg: (create, edit, query) - Add a documentation flag to the control.  The documentation flag has a directory structure. (e.g., -dt render/multiLister/createNode/material)
        dragCallback | dgc: (create, edit) - Adds a callback that is called when the middle mouse button is pressed.  The MEL version of the callback is of the form:  global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  The proc returns a string array that is transferred to the drop site. By convention the first string in the array describes the user settable message type.  Controls that are application defined drag sources may ignore the callback. $mods allows testing for the key modifiers CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3 == CTRL + SHIFT.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def callbackName( dragControl, x, y, modifiers ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "x", "y", "modifiers".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")
        dropCallback | dpc: (create, edit) - Adds a callback that is called when a drag and drop operation is released above the drop site.  The MEL version of the callback is of the form:  global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  The proc receives a string array that is transferred from the drag source. The first string in the msgs array describes the user defined message type. Controls that are application defined drop sites may ignore the callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "dropControl", "messages", "x", "y", "type".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")
        enable | en: (create, edit, query) - The enable state of the control.  By default, this flag is set to true and the control is enabled.  Specify false and the control will appear dimmed or greyed-out indicating it is disabled.
        enableBackground | ebg: (create, edit, query) - Enables the background color of the control.
        enableKeyboardFocus | ekf: (create, edit, query) - If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse. This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls. If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        fullPathName | fpn: (query) - Return the full path name of the widget, which includes all the parents.
        height | h: (create, edit, query) - The height of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
        highlightColor | hlc: (create, edit, query) - The highlight color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.
        image | i: (create, edit, query) - Sets the image given the file name.
        isObscured | io: (query) - Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.
        manage | m: (create, edit, query) - Manage state of the control.  An unmanaged control is not visible, nor does it take up any screen real estate.  All controls are created managed by default.
        noBackground | nbg: (create, edit) - Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
        numberOfPopupMenus | npm: (query) - Return the number of popup menus attached to this control.
        objectThumbnail | ot: (edit) - Use an image of the named object, if possible.
        parent | p: (create, query) - The parent layout for this control.
        popupMenuArray | pma: (query) - Return the names of all the popup menus attached to this control.
        preventOverride | po: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        sceneFile | sf: (edit) - The name of the file that the icon is to be associated with.
        statusBarMessage | sbm: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
        visible | vis: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand | vcc: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width | w: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def sceneEditor(*args, control: bool = ..., ctl: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., exists: bool = ..., ex: bool = ..., filter: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., fmc: Optional[Union[str, bool]] = ..., highlightConnection: Optional[Union[str, bool]] = ..., hlc: Optional[Union[str, bool]] = ..., lockMainConnection: bool = ..., lck: bool = ..., mainListConnection: Optional[Union[str, bool]] = ..., mlc: Optional[Union[str, bool]] = ..., onlyParents: bool = ..., op: bool = ..., panel: Optional[Union[str, bool]] = ..., pnl: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., refreshReferences: bool = ..., rr: bool = ..., selectCommand: Optional[Union[str, bool]] = ..., sc: Optional[Union[str, bool]] = ..., selectItem: Optional[Union[int, bool]] = ..., si: Optional[Union[int, bool]] = ..., selectReference: Optional[Union[str, bool]] = ..., sr: Optional[Union[str, bool]] = ..., selectionConnection: Optional[Union[str, bool]] = ..., slc: Optional[Union[str, bool]] = ..., shortName: bool = ..., shn: bool = ..., stateString: bool = ..., sts: bool = ..., unParent: bool = ..., up: bool = ..., unlockMainConnection: bool = ..., ulk: bool = ..., unresolvedName: bool = ..., un: bool = ..., updateMainConnection: bool = ..., upd: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., withoutCopyNumber: bool = ..., wcn: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This creates an editor for managing the files in a scene.

    Args:
        control | ctl: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag | dtg: (create, edit, query) - Attaches a tag to the editor.
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        filter | f: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        forceMainConnection | fmc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        highlightConnection | hlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        lockMainConnection | lck: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        mainListConnection | mlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        onlyParents | op: (query) - When used with the 'selectItem' or 'selectReference' queries it indicates that, if both a parent and a child file or reference are selected, only the parent will be returned.
        panel | pnl: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent | p: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        refreshReferences | rr: (edit) - Force refresh of references
        selectCommand | sc: (create, edit, query) - A script to be executed when an item is selected.
        selectItem | si: (edit, query) - Query or change the currently selected item. When queried, the currently selected file name will be return.
        selectReference | sr: (query) - Query the currently selected reference. Returns the name of the currently selected reference node.
        selectionConnection | slc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        shortName | shn: (query) - When used with the 'selectItem' query it indicates that the file name returned will be the short name (i.e. just a file name without any directory paths). If this flag is not present, the full name and directory path will be returned.
        stateString | sts: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        unParent | up: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection | ulk: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        unresolvedName | un: (query) - When used with the 'selectItem' query it indicates that the file name returned will be unresolved (i.e. it will be the path originally specified when the file was loaded into Maya; this path may contain environment variables and may not exist on disk). If this flag is not present, the resolved name will    be returned.
        updateMainConnection | upd: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
        withoutCopyNumber | wcn: (query) - When used with the 'selectItem' query it indicates that the file name returned will not have a copy number appended to the end. If this flag is not present, the file name returned may have a copy number appended to the end.
    """
    ...


def sceneUIReplacement(*args, clear: bool = ..., cl: bool = ..., deleteRemaining: bool = ..., dr: bool = ..., getNextFilter: Optional[Union[Tuple[str, str], bool]] = ..., gf: Optional[Union[Tuple[str, str], bool]] = ..., getNextPanel: Optional[Union[Tuple[str, str], bool]] = ..., gp: Optional[Union[Tuple[str, str], bool]] = ..., getNextScriptedPanel: Optional[Union[Tuple[str, str], bool]] = ..., gsp: Optional[Union[Tuple[str, str], bool]] = ..., update: Optional[Union[str, bool]] = ..., u: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This command returns existing scene based UI that can be utilized by
    the scene that is being loaded. It can also delete any such UI that is
    not used by the loading scene.

    Args:
        clear | cl: (create) - Frees any resources allocated by the command.
        deleteRemaining | dr: (create) - Delete any UI that is scene dependent and has not been referenced by this command since the last update.
        getNextFilter | gf: (create) - Returns the next filter of the specified type with the specified name.
        getNextPanel | gp: (create) - Returns the next panel of the specified type, preferably with the specified label.
        getNextScriptedPanel | gsp: (create) - Returns the next scripted panel of the specified scripted panel type, preferably with the specified label.
        update | u: (create) - Updates the state of the command to reflect the current state of the application.  The string argument is the name of the main window pane layout holding the panels.
    """
    ...


def scriptNode(*args, afterScript: Optional[Union[str, bool]] = ..., beforeScript: Optional[Union[str, bool]] = ..., bs: Optional[Union[str, bool]] = ..., executeAfter: bool = ..., ea: bool = ..., executeBefore: bool = ..., eb: bool = ..., ignoreReferenceEdits: bool = ..., ire: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., scriptType: Optional[Union[int, bool]] = ..., st: Optional[Union[int, bool]] = ..., sourceType: Optional[Union[str, bool]] = ..., stp: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    scriptNodes contain scripts that are executed when a file is loaded or
    when the script node is deleted. If a script modifies a referenced node,
    the changes will be tracked as reference edits unless the scriptNode was
    created with the ignoreReferenceEdits flag. The scriptNode command is used
    to create, edit, query, and test scriptNodes.

    Args:
        afterScript | afterScript: (create, edit, query) - The script executed when the script node is deleted.  C: The default is an empty string.  Q: When queried, this flag returns a string.
        beforeScript | bs: (create, edit, query) - The script executed during file load.  C: The default is an empty string.  Q: When queried, this flag returns a string.
        executeAfter | ea: (create) - Execute the script stored in the .after attribute of the scriptNode. This script is normally executed when the script node is deleted.
        executeBefore | eb: (create) - Execute the script stored in the .before attribute of the scriptNode. This script is normally executed when the file is loaded.
        ignoreReferenceEdits | ire: (create) - Sets whether changes made to referenced nodes during the execution of the script should be recorded as reference edits. This flag must be set when the scriptNode is created. If this flag is not set, changes to referenced nodes will be recorded as edits by default.
        name | n: (create) - When creating a new scriptNode, this flag specifies the name of the node. If a non-unique name is used, the name will be modified to ensure uniqueness.
        scriptType | st: (create, edit, query) - Specifies when the script is executed. The following values may be used:   0 Execute on demand.   1 Execute on file load or on node deletion.   2 Execute on file load or on node deletion when not in batch mode.    3 Internal   4 Execute on software render   5 Execute on software frame render   6 Execute on scene configuration   7 Execute on time changed   C: The default value is 0.  Q: When queried, this flag returns an int.
        sourceType | stp: (create, edit, query) - Sets the language type for both the attached scripts. Valid values are "mel" (enabled by default), and "python".
    """
    ...


def selLoadSettings(*args, activeProxy: Optional[Union[str, bool]] = ..., ap: Optional[Union[str, bool]] = ..., deferReference: bool = ..., dr: bool = ..., fileName: Optional[Union[str, bool]] = ..., fn: Optional[Union[str, bool]] = ..., numSettings: Optional[Union[int, bool]] = ..., ns: Optional[Union[int, bool]] = ..., proxyManager: Optional[Union[str, bool]] = ..., pm: Optional[Union[str, bool]] = ..., proxySetFiles: Optional[Union[str, bool]] = ..., psf: Optional[Union[str, bool]] = ..., proxySetTags: Optional[Union[str, bool]] = ..., pst: Optional[Union[str, bool]] = ..., proxyTag: Optional[Union[str, bool]] = ..., pt: Optional[Union[str, bool]] = ..., referenceNode: Optional[Union[str, bool]] = ..., rfn: Optional[Union[str, bool]] = ..., shortName: bool = ..., shn: bool = ..., unresolvedName: bool = ..., un: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to edit and query information about the implicit load
    settings. Currently this is primarily intended for internal use within the
    Preload Reference Editor.
    selLoadSettings acts on load setting IDs. When implict load settings are
    built for a target scene, there will be one load setting for each reference
    in the target scene. Each load setting has a numerical ID which is its index
    in a pre-order traversal of the target reference hierarchy (with the root
    scenefile being assigned an ID of 0). Although the IDs are numerical they must
    be passed to the command as string array.
    Example:
    Given the scene:
    
            a
           / \
          b   c
             / \
            d   e
    
    where:
    a references b and c
    c references d and e
    the IDs will be as follows:
    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    selLoadSettings can be used to change the load state of a reference:
    whether it will be loaded or unloaded (deferred) when the target scene is
    opened.
    Note: selLoadSettings can accept multiple command parameters, but the order
    must be selected carefully such that no reference is set to the loaded state
    while its parent is in the unlaoded state.
    Given the scene:
    
    a
    |
    b [-]
    |
    c [-]
    
    where:
    a references b
    b references c
    a = 0
    b = 1
    c = 2
    and b and c are currently in the unloaded state.
    The following command will succeed and change both b and c to the loaded state:
    selLoadSettings -e -deferReference 0 "1" "2";
    whereas the following command will fail and leave both b and c in the unloaded
    state:
    selLoadSettings -e -deferReference 0 "2" "1";
    Bear in mind that the following command will also change both b and c to the
    loaded state:
    selLoadSettings -e -deferReference 0 "1";
    This is because setting a reference to the loaded state automatically sets all
    child references to the loaded state as well. And vice versa, setting a reference
    the the unloaded state automatically sets all child reference to the unloaded state.

    Args:
        activeProxy | ap: (create, edit, query) - Change or query the active proxy of a proxy set. In query mode, returns the proxyTag of the active proxy; in edit mode, finds the proxy in the proxySet with the given tag and makes it the active proxy.
        deferReference | dr: (create, edit, query) - Change or query the load state of a reference.
        fileName | fn: (create, query) - Return the file name reference file(s) associated with the indicated load setting(s).
        numSettings | ns: (create, query) - Return the number of settings in the group of implicit load settings. This is equivalent to number of references in the scene plus 1.
        proxyManager | pm: (create, query) - Return the name(s) of the proxy manager(s) associated with the indicated load setting(s).
        proxySetFiles | psf: (create, query) - Return the name(s) of the proxy(ies) available in the proxy set associated with the indicated load setting(s).
        proxySetTags | pst: (create, query) - Return the name(s) of the proxy tag(s) available in the proxy set associated with the indicated load setting(s).
        proxyTag | pt: (create, query) - Return the name(s) of the proxy tag(s) associated with the indicated load setting(s).
        referenceNode | rfn: (create, query) - Return the name(s) of the reference node(s) associated with the indicated load setting(s).
        shortName | shn: (create, query) - Formats the return value of the 'fileName' query flag to only return the short name(s) of the reference file(s).
        unresolvedName | un: (create, query) - Formats the return value of the 'fileName' query flag to return the unresolved name(s) of the reference file(s). The unresolved file name is the file name used when the reference was created, whether or not that file actually exists on disk. When Maya encounters a file name which does not exist on disk it attempts to resolve the name by looking for the file in a number of other locations. By default the 'fileName' flag will return this resolved value.
    """
    ...


def setAttrMapping(*args, absolute: bool = ..., a: bool = ..., attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., axis: Optional[Union[str, bool]] = ..., ax: Optional[Union[str, bool]] = ..., clutch: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., device: Optional[Union[str, bool]] = ..., d: Optional[Union[str, bool]] = ..., offset: Optional[Union[float, bool]] = ..., o: Optional[Union[float, bool]] = ..., relative: bool = ..., r: bool = ..., scale: Optional[Union[float, bool]] = ..., s: Optional[Union[float, bool]] = ..., selection: bool = ..., sl: bool = ..., query: bool = ...) -> Any:
    r"""
    This command applies an offset and scale to a specified device
    attachment. This command is different than the setInputDeviceMapping
    command, which applies a mapping to a device axis.
    
    The value from the device is multiplied by the scale and the
    offset is added to this product. With an absolute mapping, the
    attached attribute gets the resulting value. If the mapping is
    relative, the resulting value is added to the previous calculated
    value. The calculated value will also take into account the
    setInputDeviceMapping, if it was defined.
    
    As an example, if the space ball is setup with absolute attachment
    mappings, pressing in one direction will cause the
    attached attribute to get a constant value. If a relative mapping
    is used, and the spaceball is pressed in one direction, the
    attached attribute will get a constantly increasing (or constantly
    decreasing) value.
    
    Note that the definition of relative is different than the definition
    used by the setInputDeviceMapping command. In general, both
    a relative attachment mapping (this command) and a relative
    device mapping (setInputDeviceMapping) should not be used together
    one the same axis.

    Args:
        absolute | a: (create) - Make the mapping absolute.
        attribute | at: (create, multiuse) - The attribute used in the attachment.
        axis | ax: (create) - The axis on the device used in the attachment.
        clutch | c: (create) - The clutch button used in the attachment.
        device | d: (create) - The device used in the attachment.
        offset | o: (create) - Specify the offset value.
        relative | r: (create) - Make the mapping relative.
        scale | s: (create) - Specify the scale value.
        selection | sl: (create) - This flag specifies the mapping should be on the selected objects
    """
    ...


def setInputDeviceMapping(*args, absolute: bool = ..., a: bool = ..., axis: Optional[Union[str, bool]] = ..., ax: Optional[Union[str, bool]] = ..., device: Optional[Union[str, bool]] = ..., d: Optional[Union[str, bool]] = ..., offset: Optional[Union[float, bool]] = ..., o: Optional[Union[float, bool]] = ..., relative: bool = ..., r: bool = ..., scale: Optional[Union[float, bool]] = ..., s: Optional[Union[float, bool]] = ..., view: bool = ..., v: bool = ..., world: bool = ..., w: bool = ...) -> Any:
    r"""
    The command sets a scale and offset for all attachments made
    to a specified device axis. Any attachment made to a mapped
    device axis will have the scale and offset applied to its values.
    
    The value from the device is multiplied by the scale and the
    offset is added to this product. With an absolute mapping, the
    attached attribute gets the resulting value. If the mapping is
    relative, the final value is the offset added to the scaled
    difference between the current device value and the previous
    device value.
    
    This mapping will be applied to the device data before any
    mappings defined by the setAttrMapping command. A typical use
    would be to scale a device's input so that it is within a usable
    range. For example, the device mapping can be used to calibrate
    a spaceball to work in a specific section of a scene.
    
    As an example, if the space ball is setup with absolute device
    mappings, constantly pressing in one direction will cause the
    attached attribute to get a constant value. If a relative mapping
    is used, and the spaceball is pressed in one direction, the
    attached attribute will jump a constantly increasing (or constantly
    decreasing) value and will find a rest value equal to the offset.
    
    There are important differences between how the relative flag
    is handled by this command and the setAttrMapping command. (See
    the setAttrMapping documentation for specifics on how it calculates
    relative values). In general,
    both a relative device mapping (this command) and a relative
    attachment mapping (setAttrMapping) should not be used together
    on the same axis.

    Args:
        absolute | a: (create) - report absolute axis values
        axis | ax: (create, multiuse) - specify the axis to map
        device | d: (create) - specify which device to map
        offset | o: (create) - specify the axis offset value
        relative | r: (create) - report the change in axis value since the last sample
        scale | s: (create) - specify the axis scale value
        view | v: (create) - translate the device coordinates into the coordinates of the active camera
        world | w: (create) - translate the device coordinates into world space coordinates
    """
    ...


def shotTrack(*args, insertTrack: Optional[Union[int, bool]] = ..., it: Optional[Union[int, bool]] = ..., lock: bool = ..., l: bool = ..., mute: bool = ..., m: bool = ..., numTracks: Optional[Union[int, bool]] = ..., nt: Optional[Union[int, bool]] = ..., removeEmptyTracks: bool = ..., ret: bool = ..., removeTrack: Optional[Union[int, bool]] = ..., rt: Optional[Union[int, bool]] = ..., selfmute: bool = ..., sm: bool = ..., solo: bool = ..., so: bool = ..., swapTracks: Optional[Union[Tuple[int, int], bool]] = ..., st: Optional[Union[Tuple[int, int], bool]] = ..., title: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ..., track: Optional[Union[int, bool]] = ..., tr: Optional[Union[int, bool]] = ..., unsolo: bool = ..., uso: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used for inserting and removing tracks related to the shots displayed in the Sequencer. It can also be used to modify the track state, for example, to lock or mute a track.

    Args:
        insertTrack | it: (create) - This flag is used to insert a new empty track at the track index specified.
        lock | l: (create, edit, query) - This flag specifies whether shots on a track are to be locked or not.
        mute | m: (create, edit, query) - This flag specifies whether shots on a track are to be muted or not.
        numTracks | nt: (query) - To query the number of tracks
        removeEmptyTracks | ret: (create) - This flag is used to remove all tracks that have no clips.
        removeTrack | rt: (create) - This flag is used to remove the track with the specified index.  The track must have no clips on it before it can be removed.
        selfmute | sm: (create, edit, query) - This flag specifies whether shots on a track are to be muted or not (unlike mute, this disregards soloing).
        solo | so: (create, edit, query) - This flag specifies whether shots on a track are to be soloed or not.
        swapTracks | st: (create) - This flag is used to swap the contents of two specified tracks.
        title | t: (create, edit, query) - This flag specifies the title for the track.
        track | tr: (create, edit, query) - Specify the track on which to operate by using the track's trackNumber. 			In query mode, this flag needs a value.
        unsolo | uso: (query) - This flag specifies whether shots on a track are to be unsoloed or not.
    """
    ...


def showHelp(*args, absolute: bool = ..., a: bool = ..., docs: bool = ..., d: bool = ..., helpTable: bool = ..., ht: bool = ..., version: bool = ..., v: bool = ..., query: bool = ...) -> Any:
    r"""
    Invokes a web browser to open the on-line documentation and help files.
    It will open the help page for a given topic, or open a browser
    to a specific URL.

    Args:
        absolute | a: (create) - The specified "URL" is an absolute URL that should be passed directly to the web browser.
        docs | d: (create, query) - Use this flag to directly specify a help file relative to the on-line documentation root.
        helpTable | ht: (create, query) - Use this flag to specify which file will be used to search for help topics when the -d/docs and -a/absolute flags are not used. If only a file name is specified and not a path, then the file is assumed to be in the maya application directory. If this flag does not accept an argument if it is queried. The default value is "helpTable".
        version | v: (query) - Use this flag to get the Maya version that the showHelp command uses.
    """
    ...


def sysFile(*args, copy: Optional[Union[str, bool]] = ..., cp: Optional[Union[str, bool]] = ..., delete: bool = ..., makeDir: bool = ..., md: bool = ..., move: Optional[Union[str, bool]] = ..., mov: Optional[Union[str, bool]] = ..., removeEmptyDir: bool = ..., red: bool = ..., rename: Optional[Union[str, bool]] = ..., ren: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This command provides a system independent way to create a directory
    or to rename or delete a file.

    Args:
        copy | cp: (create) - Copy the file to the name given by the newFileName paramter.
        delete | delete: (create) - Deletes the file.
        makeDir | md: (create) - Create the directory path given in the parameter. This will create the entire path if more than one directory needs to be created.
        move | mov: (create) - Behaves identically to the -rename flag and remains for compatibility with old scripts
        removeEmptyDir | red: (create) - Delete the directory path given in the parameter if the directory is empty. The command will not delete a directory which is not empty.
        rename | ren: (create) - Rename the file to the name given by the newFileName parameter.
    """
    ...


def timer(*args, endTimer: bool = ..., e: bool = ..., lapTime: bool = ..., lap: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., startTimer: bool = ..., s: bool = ...) -> Any:
    r"""
    Allow simple timing of scripts and commands. The resolution of this timer
    is at the level of your OS's gettimeofday() function.
    
    
    Note:This command does not handle stacked calls. For
    example, this code below will give an incorrect answer on the
    second timer -e call.
    timer -s;
    timer -s;
    timer -e;
    timer -e;
    
    To do this use named timers:
    timer -s;
    timer -s -name "innerTimer";
    timer -e -name "innerTimer";
    timer -e;
    
    
    I the -e flag or -lap flag return the time elapsed since
    the last 'timer -s' call.
    I the -s flag has no return value.

    Args:
        endTimer | e: (create) - Stop the timer and return the time elapsed since the timer was started (in seconds). Once a timer is turned off it no longer exists, though it can be recreated with a new start
        lapTime | lap: (create) - Get the lap time of the timer (time elapsed since start in seconds). Unlike the end flag this keeps the timer running.
        name | n: (create) - Use a named timer for the operation. If this is omitted then the default timer is assumed.
        startTimer | s: (create) - Start the timer.
    """
    ...


def timerX(*args, startTime: Optional[Union[float, bool]] = ..., st: Optional[Union[float, bool]] = ...) -> Any:
    r"""
    Used to calculate elapsed time. This command returns
    sub-second accurate time values. It is useful from scripts
    for timing the length of operations. Call this command
    before and after the operation you wish to time. On the
    first call, do not use any flags. It will return the start
    time. Save this value. After the operation, call this
    command a second time, and pass the saved start time using
    the -st flag. The elapsed time will be returned.

    Args:
        startTime | st: (create) - When this flag is used, the command returns the elapsed time since the specified start time.
    """
    ...


def translator(*args, defaultFileRule: bool = ..., dfr: bool = ..., defaultOptions: Optional[Union[str, bool]] = ..., do: Optional[Union[str, bool]] = ..., extension: bool = ..., ext: bool = ..., fileCompression: Optional[Union[str, bool]] = ..., cmp: Optional[Union[str, bool]] = ..., filter: bool = ..., f: bool = ..., list: bool = ..., l: bool = ..., loaded: bool = ..., ld: bool = ..., objectType: bool = ..., ot: bool = ..., optionsScript: bool = ..., os: bool = ..., readSupport: bool = ..., rs: bool = ..., writeSupport: bool = ..., ws: bool = ..., query: bool = ...) -> Any:
    r"""
    Set or query parameters associated with the file translators specified
    in as the argument.

    Args:
        defaultFileRule | dfr: (query) - Returns the default file rule value, can return "" as well
        defaultOptions | do: (query) - Return/set a string of default options used by this translator.
        extension | ext: (query) - Returns the default file extension for this translator.
        fileCompression | cmp: (query) - Specifies the compression action to take when a file is saved. Possible values are "compressed", "uncompressed" "asCompressed".
        filter | f: (query) - Returns the filter string used for this translator.
        list | l: (query) - Return a string array of all the translators that are loaded.
        loaded | ld: (query) - Returns true if the given translator is currently loaded.
        objectType | ot: (query) - This flag is obsolete. This will now return the same results as defaultFileRule going forward.
        optionsScript | os: (query) - Query the name of the options script to use to post the user options UI. When this script is invoked it will expect the name of the parent layout in which the options will be displayed as well as the name of the callback to be invoked once the apply button has been depressed in the options area.
        readSupport | rs: (query) - Returns true if this translator supports read operations.
        writeSupport | ws: (query) - Returns true if this translator supports write operations.
    """
    ...


def unassignInputDevice(*args, clutch: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., device: Optional[Union[str, bool]] = ..., d: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command deletes all command strings associated with this
    device.

    Args:
        clutch | c: (create) - Only delete command attachments with this clutch.
        device | d: (create) - Specifies the device to work on.
    """
    ...


def undo(*args) -> Any:
    r"""
    Takes the most recent command from the undo list and undoes it.

    Args:
    """
    ...


def undoInfo(*args, chunkName: Optional[Union[str, bool]] = ..., cn: Optional[Union[str, bool]] = ..., closeChunk: bool = ..., cck: bool = ..., infinity: bool = ..., length: Optional[Union[int, bool]] = ..., l: Optional[Union[int, bool]] = ..., openChunk: bool = ..., ock: bool = ..., printQueue: bool = ..., pq: bool = ..., printRedoQueue: bool = ..., prq: bool = ..., redoName: Optional[Union[str, bool]] = ..., rn: Optional[Union[str, bool]] = ..., redoQueueEmpty: bool = ..., rqe: bool = ..., state: bool = ..., st: bool = ..., stateWithoutFlush: bool = ..., swf: bool = ..., undoName: Optional[Union[str, bool]] = ..., un: Optional[Union[str, bool]] = ..., undoQueueEmpty: bool = ..., uqe: bool = ..., query: bool = ...) -> Any:
    r"""
    This command controls the undo/redo parameters.
    
    In query mode, if invoked without flags (other than the query flag), this
    command will return the number of items currently on the undo queue.

    Args:
        chunkName | cn: (create, query) - Sets the name used to identify a chunk for undo/redo purposes when opening a chunk.
        closeChunk | cck: (create) - Closes the chunk that was opened earlier by openChunk. Once close chunk is called, all undoable operations in the chunk will undo as a single undo operation. Use with CAUTION!! Improper use of this command can leave the undo queue in a bad state.
        infinity | infinity: (create, query) - Set the queue length to infinity.
        length | l: (create, query) - Specifies the maximum number of items in the undo queue. The infinity flag overrides this one.
        openChunk | ock: (create) - Opens a chunk so that all undoable operations after this call will fall into the newly opened chunk, until close chunk is called. Once close chunk is called, all undoable operations in the chunk will undo as a single undo operation. Use with CAUTION!! Improper use of this command can leave the undo queue in a bad state.
        printQueue | pq: (query) - Prints to the Script Editor the contents of the undo queue.
        printRedoQueue | prq: (query) - Prints to the Script Editor the contents of the redo queue.
        redoName | rn: (query) - Returns what will be redone (if anything)
        redoQueueEmpty | rqe: (query) - Return true if the redo queue is empty. Return false if there is at least one command in the queue to be redone.
        state | st: (create, query) - Turns undo/redo on or off.
        stateWithoutFlush | swf: (create, query) - Turns undo/redo on or off without flushing the queue. Use with CAUTION!! Note that if you  perform destructive operations while stateWithoutFlush is disabled, and you then enable it again, subsequent undo operations that try to go past the  destructive operations may be unstable since undo will not be able to properly reconstruct the former state of the scene.
        undoName | un: (query) - Returns what will be undone (if anything)
        undoQueueEmpty | uqe: (query) - Return true if the undo queue is empty. Return false if there is at least one command in the queue to be undone.
    """
    ...


def unknownNode(*args, plugin: bool = ..., p: bool = ..., realClassName: bool = ..., rcn: bool = ..., realClassTag: bool = ..., rct: bool = ..., query: bool = ...) -> Any:
    r"""
    Allows querying of the data stored for unknown nodes
    (nodes that are defined by a plug-in that Maya could not
    load when loading a scene file).

    Args:
        plugin | p: (query) - In query mode return the name of the plug-in from which the unknown node originated. If no plug-in then the empty string is returned.
        realClassName | rcn: (query) - Return the real class name of the node.
        realClassTag | rct: (query) - Return the real class IFF tag of the node.
    """
    ...


def unknownPlugin(*args, dataTypes: bool = ..., dt: bool = ..., list: bool = ..., l: bool = ..., nodeTypes: bool = ..., nt: bool = ..., remove: bool = ..., r: bool = ..., version: bool = ..., v: bool = ..., query: bool = ...) -> Any:
    r"""
    Allows querying of the unknown plug-ins used by the scene,
    and provides a means to remove them.

    Args:
        dataTypes | dt: (query) - Returns the data types associated with the given unknown plug-in. This will always be empty for pre-Maya 2014 files.
        list | l: (query) - Lists the unknown plug-ins in the scene.
        nodeTypes | nt: (query) - Returns the node types associated with the given unknown plug-in. This will always be empty for pre-Maya 2014 files.
        remove | r: (create) - Removes the given unknown plug-in from the scene. For Maya 2014 files and onwards, this will fail if node or data types defined by the plug-in are still in use.
        version | v: (query) - Returns the version string of the given unknown plug-in.
    """
    ...


def unloadPlugin(*args, addCallback: Optional[Union[str, bool]] = ..., ac: Optional[Union[str, bool]] = ..., force: bool = ..., f: bool = ..., removeCallback: Optional[Union[str, bool]] = ..., rc: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Unload plug-ins from Maya. After the successful execution of
    this command, plug-in services will no longer be available.

    Args:
        addCallback | ac: (create) - Add a procedure to be called just before a plugin is unloaded. The procedure should have one string argument, which will be the plugin's name.
        force | f: (create) - Unload the plugin even if it is providing services.  This is not recommended.  If you unload a plug-in that implements a node or data type in the scene, those instances will be converted to unknown nodes or data and the scene will no longer behave properly. Maya may become unstable or even crash. If you use this flag you are advised to save your scene in MayaAscii format and restart Maya as soon as possible.
        removeCallback | rc: (create) - Remove a procedure which was previously added with -addCallback.
    """
    ...


def warning(*args, noContext: bool = ..., n: bool = ..., showLineNumber: bool = ..., sl: bool = ...) -> Any:
    r"""
    The warning command is provided so that the user can issue warning
    messages from his/her scripts.
    The string argument is displayed in the command window (or stdout if
    running in batch mode) after being prefixed with a warning message heading
    and surrounded by the appropriate language separators
    (# for Python, // for Mel).

    Args:
        noContext | n: (create) - Do not include the context information with the warning message.
        showLineNumber | sl: (create) - Obsolete. Will be deleted in the next version of Maya. Use the checkbox in the script editor that enables line number display instead.
    """
    ...


def whatsNewHighlight(*args, highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., hc: Optional[Union[Tuple[float, float, float], bool]] = ..., highlightOn: bool = ..., ho: bool = ..., showStartupDialog: bool = ..., ssd: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to toggle the What's New highlighting feature,
    and the display of the settings dialog for the feature that appears
    on startup.

    Args:
        highlightColor | hc: (create, query) - Set the color of the What's New highlight. The arguments correspond to the red, green, and blue color components. Each color component ranges in value from 0.0 to 1.0.
        highlightOn | ho: (create, query) - Toggle the What's New highlighting feature. When turned on, menu items and buttons introduced in the latest version will be highlighted.
        showStartupDialog | ssd: (create, query) - Set whether the settings dialog for this feature appears on startup.
    """
    ...


def workspace(*args, active: bool = ..., act: bool = ..., baseWorkspace: Optional[Union[str, bool]] = ..., bw: Optional[Union[str, bool]] = ..., create: Optional[Union[str, bool]] = ..., cr: Optional[Union[str, bool]] = ..., directory: Optional[Union[str, bool]] = ..., dir: Optional[Union[str, bool]] = ..., expandName: Optional[Union[str, bool]] = ..., en: Optional[Union[str, bool]] = ..., fileRule: Optional[Union[Tuple[str, str], bool]] = ..., fr: Optional[Union[Tuple[str, str], bool]] = ..., fileRuleEntry: Optional[Union[str, bool]] = ..., fre: Optional[Union[str, bool]] = ..., fileRuleList: bool = ..., frl: bool = ..., filter: bool = ..., f: bool = ..., fullName: bool = ..., fn: bool = ..., list: bool = ..., l: bool = ..., listFullWorkspaces: bool = ..., lfw: bool = ..., listWorkspaces: bool = ..., lw: bool = ..., newWorkspace: bool = ..., n: bool = ..., objectType: Optional[Union[Tuple[str, str], bool]] = ..., ot: Optional[Union[Tuple[str, str], bool]] = ..., objectTypeEntry: Optional[Union[str, bool]] = ..., ote: Optional[Union[str, bool]] = ..., objectTypeList: bool = ..., otl: bool = ..., openWorkspace: bool = ..., o: bool = ..., projectPath: Optional[Union[str, bool]] = ..., pp: Optional[Union[str, bool]] = ..., removeFileRuleEntry: Optional[Union[str, bool]] = ..., rfr: Optional[Union[str, bool]] = ..., removeVariableEntry: Optional[Union[str, bool]] = ..., rve: Optional[Union[str, bool]] = ..., renderType: Optional[Union[Tuple[str, str], bool]] = ..., rt: Optional[Union[Tuple[str, str], bool]] = ..., renderTypeEntry: Optional[Union[str, bool]] = ..., rte: Optional[Union[str, bool]] = ..., renderTypeList: bool = ..., rtl: bool = ..., rootDirectory: bool = ..., rd: bool = ..., saveWorkspace: bool = ..., s: bool = ..., shortName: bool = ..., sn: bool = ..., update: bool = ..., u: bool = ..., updateAll: bool = ..., ua: bool = ..., variable: Optional[Union[Tuple[str, str], bool]] = ..., v: Optional[Union[Tuple[str, str], bool]] = ..., variableEntry: Optional[Union[str, bool]] = ..., ve: Optional[Union[str, bool]] = ..., variableList: bool = ..., vl: bool = ..., query: bool = ...) -> Any:
    r"""
    Create, open, or edit a workspace associated with a given workspace
    file.
    
    The string argument represents the workspace. If no workspace is
    specified then the current workspace is assumed.
    
    A workspace provides the underlying definition of a Maya Project.
    Each project has an associated workspace file, named workspace.mel, which is stored in the project root directory.
    The workspace file defines a set of rules that map file types to their storage, either relative to the
    project root or as an absolute location.  These rules are used when resolving file paths at runtime.
    
    The workspace command operates directly on the low-level definition of the workspace to read, change and store
    the definition to the underlying file.  Use of this command is not generally required, for most purposes
    it is recommended that project definition changes be done via the Project Window in the User Interface. Multiple
    actions go under the assumption that given paths exist.

    Args:
        active | act: (create, query) - This flag is a synonym for -o/openWorkspace.
        baseWorkspace | bw: (query) - A workspace may be based on another workspace.  This means that all the file rules and variables in the base workspace apply to this workspace unless they are explicitly overridden. By default, a new workspace has the workspace "default" as it's base workspace. Note that "duplicated" file rules containing relative paths are not verified nor created when creating a new workspace or when changing the base workspace.
        create | cr: (create) - Create a new directory.  If the directory name is not a full path name, it will be created as a subdirectory of the "current" directory set with the -dir flag. Note that this flag does not create a workspace.
        directory | dir: (create, query) - This option will set the current workspace directory to the path specified. When queried it will return the current workspace directory. This directory is used as an initial directory for the fileBrowser and is part of the search path used for locating files. It should not be confused with the current working directory as used by the pwd and chdir commands. When the file browser is used, it will set this value to the last location navigated to.
        expandName | en: (create, query) - Query for the full path location of a filename using the current workspace definition. The path may be a project relative file name, a full path name or a variable name. The return value is always a full path name. If the path is an empty string, the return value will be the project root directory. Variable expansion is supported, and will consider both variables defined in the workspace as well as environment variables. There are three formats supported for expanding variable names: %variableName%, $variableName, ${variableName}. Maya will first attempt to find matching variables defined in the current workspace, then search for a matching environment variable. The tilde character ('~') is also supported. If a tilde is located at the beginning of a variable, Maya will only consider and expand environment variables, and will leave the tilde in the expanded result. On linux and mac platforms, a tilde can be used to expand a user's home directory, using the form ~username, ~, or ~/.  When specified as ~username, it will be replaced with the corresponding user's home directory.  When specified as ~ or ~/, it will be replaced with the value of the HOME environment variable.
        fileRule | fr: (create, query) - Set the default location for a file. The first parameter is the fileRule name(scenes, images, etc) and the second is the location. When queried, it returns a list of strings.  The elements of the returned list alternate between fileRule names and the corresponding location.  There is typically one file rule for each available translator. Environment variables are supported. You can set multiple path for the file rule by separating them with semicolons (;) on Windows and colons(:) on MacOSX and Linux. Note that whitespace at the beginning and end of each item in the separated sequence is significant and will be included as part of the path name (which is not usually desired unless the pathname does actually start or end with spaces). A valid filerule name cannot contain multiple byte characters. Note that creating a filerule does not create any directories. It is the user's responsibility to ensure that all paths are valid.
        fileRuleEntry | fre: (create, query) - Return the location for the given fileRule.
        fileRuleList | frl: (create, query) - Returns a list of the currently defined file rules.
        filter | f: () - This flag is obsolete.
        fullName | fn: (create, query) - Return the full name of the workspace.
        list | l: (create, query) - This option will list the current workspace directory. If a path is specified for the "workspaceFile" then the contents of that directory will be listed.  Otherwise, the contents of the directory set with the -dir flag will be listed.
        listFullWorkspaces | lfw: (create, query) - Returns a list of the full path names of all the currently defined workspaces.
        listWorkspaces | lw: (create, query) - Returns a list of all the currently defined workspace names.
        newWorkspace | n: (create) - This specifies that a new workspace is being created with a given path (full path or relative to "current" directory). If a workspace with this path already exists, the command will fail. Note that the application is creating a virtual workspace without creating any new directories. If given a relative path, it will map the new workspace to the "current" directory set with the -dir flag concatenated with the given path. If the path does not exist, it will default the workspace root directory -rd to the system's root path (e.g. C:\ or '/'). It is the user's responsibility to ensure that all paths exist.
        objectType | ot: (create, query) - This flag is obsolete. All default locations will be added to the fileRules going forward.
        objectTypeEntry | ote: (create, query) - This flag is obsolete. This will now return the same as fileRuleEntry.
        objectTypeList | otl: (create, query) - This flag is obsolete. This will now return the same results as fileRuleList going forward.
        openWorkspace | o: (create, query) - Open the workspace.  The workspace becomes the current workspace.
        projectPath | pp: (create, query) - Convert filePath passed as argument to a filename that is relative to the project root directory (if possible) and return it.  If the filePath is not under the project root directory, a full path name will be returned.
        removeFileRuleEntry | rfr: (create) - Remove the given file rule from the specified workspace. If the workspace name is not specified, the given file rule will be removed from the current workspace.
        removeVariableEntry | rve: (create) - Remove the given variable from the specified workspace. If the workspace name is not specified, the given variable will be removed from the current workspace.
        renderType | rt: (create, query) - This flag is obsolete. All default render types will be added to fileRules going forward.
        renderTypeEntry | rte: (create, query) - This flag is obsolete, use fileRuleEntry going forward
        renderTypeList | rtl: (create, query) - This flag is obsolete, use fileRuleList going forward.
        rootDirectory | rd: (query) - Returns the root directory of the workspace.
        saveWorkspace | s: (create) - Save the workspace.  Workspaces are normally saved when Maya exits but this flag will make sure that the data is flushed to disk.
        shortName | sn: (create, query) - Query the short name of the workspace.
        update | u: (create) - This flag reads all the workspace definitions from the project directory.  It is used by Maya at startup time to find the available workspaces.
        updateAll | ua: (create) - This flag is a synonym for -u/update.
        variable | v: (create, query) - Set or query the value of a project variable. Project variables are used when expanding names. See the -en/expandName flag below.
        variableEntry | ve: (create, query) - Given a variable name, will return its value.
        variableList | vl: (create, query) - Return a list of all variables in the workspace.
    """
    ...


def xpmPicker(*args, fileName: Optional[Union[str, bool]] = ..., fn: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Open a dialog and ask you to choose a xpm file

    Args:
        fileName | fn: (create) - default filename to display in dialog
        parent | p: (create) - parent window for modal dialog
    """
    ...


