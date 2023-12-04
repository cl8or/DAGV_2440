from typing import Union, Optional, List, Tuple, Any

def ambientLight(*args, ambientShade: Optional[Union[float, bool]] = ..., discRadius: Optional[Union[float, bool]] = ..., exclusive: bool = ..., intensity: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., position: Optional[Union[Tuple[float, float, float], bool]] = ..., rgb: Optional[Union[Tuple[float, float, float], bool]] = ..., rotation: Optional[Union[Tuple[float, float, float], bool]] = ..., shadowColor: Optional[Union[Tuple[float, float, float], bool]] = ..., shadowDither: Optional[Union[float, bool]] = ..., shadowSamples: Optional[Union[int, bool]] = ..., softShadow: bool = ..., useRayTraceShadows: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    TlightCmd is the base class for other light commands.
    The ambientLight command is used to edit the parameters of
    existing ambientLights, or to create new ones. The default
    behaviour is to create a new ambientlight.
    
    This is the commmand that instantiates an ambientLight
    or edits the parameters of an existing one.
    TambientLightCmd inherits from TlightCmd which defines
    common flags like intensity, colour etc.
    See TlightCmd for a global picture of the light commands.
    Note that the flag fAmbientLightUsed indicates whether
    the command uses any ambient specific flags.
    That is, if a command doesn't use flags
    defined here, the boolean fAmbientLightUsed is set to
    false and thus the undo/redo information is not saved
    at this level.
    
    TambientLightCmd behaves like any other command, it
    has flags, saves undo information etc. the only slightly
    different behaviour is that it calls up to TlightCmd to
    complete the functionality of the command.
    Example	parseArgs:  TambientLightCmd defines
    ambientLight specific parameters like -ambientShade
    however, several other parameters are available in
    TlightCmd such as -intensity etc.  So when parsing
    the arguments, a call is made to TlightCmd::parseArgs
    to parse common parameters (like Intensity).

    Args:
        ambientShade: (create, edit, query) - ambientShade
        discRadius: (create, edit, query) - radius of the disc around the light
        exclusive: (create, query) - True if the light is exclusively assigned
        intensity: (create, query) - Intensity of the light
        name: (create, query) - Name of the light
        position: (create, query) - Position of the light
        rgb: (create, query) - RGB colour of the light
        rotation: (create, query) - Rotation of the light for orientation, where applicable
        shadowColor: (create, query) - Color of the light's shadow
        shadowDither: (create, edit, query) - dither the shadow
        shadowSamples: (create, edit, query) - number of shadow samples.
        softShadow: (create, edit, query) - soft shadow
        useRayTraceShadows: (create, query) - True if ray trace shadows are to be used
    """
    ...


def assignViewportFactories(*args, materialFactory: Optional[Union[str, bool]] = ..., nodeType: Optional[Union[str, bool]] = ..., textureFactory: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Sets viewport factories for displays as materials or textures.

    Args:
        materialFactory: (create, edit, query) - Set or query the materialFactory for the node type.
        nodeType: (create, edit, query) - The node type.
        textureFactory: (create, edit, query) - Set or query the textureFactory for the node type.
    """
    ...


def batchRender(*args, filename: Optional[Union[str, bool]] = ..., melCommand: Optional[Union[str, bool]] = ..., numProcs: Optional[Union[int, bool]] = ..., preRenderCommand: Optional[Union[str, bool]] = ..., remoteRenderMachine: Optional[Union[str, bool]] = ..., renderCommandOptions: Optional[Union[str, bool]] = ..., showImage: bool = ..., status: Optional[Union[str, bool]] = ..., useRemoteRender: bool = ..., useStandalone: bool = ..., verbosity: Optional[Union[int, bool]] = ...) -> Any:
    r"""
    The batchRender command is used to spawn off a separate
    rendering session of the current maya file. If no
    mayaFile is specified, it'll ask you whether you want the
    current job killed. 
    
    The batchRender will spawn a separate maya process in which
    commands will be communicated to it through a commandPort. If Maya
    is unable to find an available port an error will be
    produced. Maya will attempt to use ports 7835 through 7844.

    Args:
        filename: (create) - Filename to be rendered; if empty, a temporary filename will be created.
        melCommand: (create) - Mel command to execute to run a renderer other than the software renderer.
        numProcs: (create) - Number of processors to use (0 means use all available processors).
        preRenderCommand: (create) - Command to be run prior to invoking a batch render.
        remoteRenderMachine: (create) - Name of remote render machine. Not available on Windows.
        renderCommandOptions: (create) - Arguments to the render command for batch rendering.
        showImage: (create) - Show progress of the current rendering job.
        status: (create) - Status string for displaying the batch render status.
        useRemoteRender: (create) - If remote rendering is desired. Not available on Windows.
        useStandalone: (create) - Batch rendering is to be done by exporting the scene and rendering with a standalone renderer.
        verbosity: (create) - Defines the verbosity level to report the batch rendering status: 1: display only one start message, then one message when all frames are rendered. 2: display only start and end frame messages. 3: display all messages (default).
    """
    ...


def binMembership(*args, addToBin: Optional[Union[str, bool]] = ..., exists: Optional[Union[str, bool]] = ..., inheritBinsFromNodes: Optional[Union[str, bool]] = ..., isValidBinName: Optional[Union[str, bool]] = ..., listBins: bool = ..., makeExclusive: Optional[Union[str, bool]] = ..., notifyChanged: bool = ..., removeFromBin: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    Command to assign nodes to bins.

    Args:
        addToBin: (create) - Add the nodes in a node list to a bin.
        exists: (create) - Query if a node exists in a bin.  The exists flag can take only one node.
        inheritBinsFromNodes: (create) - Let the node in the flag's argument inherit bins from nodes in the specified node list.  The node list is specified as the object of the command.
        isValidBinName: (create) - Query if the specified bin name is valid.  If so, return true. Otherwise, return false.
        listBins: (create, query) - Query and return a list of bins a list of nodes belong to. If a bin contains any of the nodes in the selection list, then it should be included in the returned bin list.
        makeExclusive: (create) - Make the specified nodes belong exclusively in the specified bin.
        notifyChanged: (create) - This flag is used to notify that binMembership has been changed.
        removeFromBin: (create) - Remove the nodes in a node list from a bin.
    """
    ...


def camera(*args, aspectRatio: Optional[Union[float, bool]] = ..., cameraScale: Optional[Union[float, bool]] = ..., centerOfInterest: Optional[Union[float, bool]] = ..., clippingPlanes: bool = ..., depthOfField: bool = ..., displayFieldChart: bool = ..., displayFilmGate: bool = ..., displayFilmOrigin: bool = ..., displayFilmPivot: bool = ..., displayGateMask: bool = ..., displayResolution: bool = ..., displaySafeAction: bool = ..., displaySafeTitle: bool = ..., fStop: Optional[Union[float, bool]] = ..., farClipPlane: Optional[Union[float, bool]] = ..., farFocusDistance: Optional[Union[float, bool]] = ..., filmFit: Optional[Union[str, bool]] = ..., filmFitOffset: Optional[Union[float, bool]] = ..., filmRollOrder: Optional[Union[str, bool]] = ..., filmRollValue: Optional[Union[float, bool]] = ..., filmTranslateH: Optional[Union[float, bool]] = ..., filmTranslateV: Optional[Union[float, bool]] = ..., focalLength: Optional[Union[float, bool]] = ..., focusDistance: Optional[Union[float, bool]] = ..., homeCommand: Optional[Union[str, bool]] = ..., horizontalFieldOfView: Optional[Union[float, bool]] = ..., horizontalFilmAperture: Optional[Union[float, bool]] = ..., horizontalFilmOffset: Optional[Union[float, bool]] = ..., horizontalPan: Optional[Union[float, bool]] = ..., horizontalRollPivot: Optional[Union[float, bool]] = ..., horizontalShake: Optional[Union[float, bool]] = ..., journalCommand: bool = ..., lensSqueezeRatio: Optional[Union[float, bool]] = ..., lockTransform: bool = ..., motionBlur: bool = ..., name: Optional[Union[str, bool]] = ..., nearClipPlane: Optional[Union[float, bool]] = ..., nearFocusDistance: Optional[Union[float, bool]] = ..., orthographic: bool = ..., orthographicWidth: Optional[Union[float, bool]] = ..., overscan: Optional[Union[float, bool]] = ..., panZoomEnabled: bool = ..., position: Optional[Union[Tuple[float, float, float], bool]] = ..., postScale: Optional[Union[float, bool]] = ..., preScale: Optional[Union[float, bool]] = ..., renderPanZoom: bool = ..., rotation: Optional[Union[Tuple[float, float, float], bool]] = ..., shakeEnabled: bool = ..., shakeOverscan: Optional[Union[float, bool]] = ..., shakeOverscanEnabled: bool = ..., shutterAngle: Optional[Union[float, bool]] = ..., startupCamera: bool = ..., stereoHorizontalImageTranslate: Optional[Union[float, bool]] = ..., stereoHorizontalImageTranslateEnabled: bool = ..., verticalFieldOfView: Optional[Union[float, bool]] = ..., verticalFilmAperture: Optional[Union[float, bool]] = ..., verticalFilmOffset: Optional[Union[float, bool]] = ..., verticalLock: bool = ..., verticalPan: Optional[Union[float, bool]] = ..., verticalRollPivot: Optional[Union[float, bool]] = ..., verticalShake: Optional[Union[float, bool]] = ..., worldCenterOfInterest: Optional[Union[Tuple[float, float, float], bool]] = ..., worldUp: Optional[Union[Tuple[float, float, float], bool]] = ..., zoom: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create, edit, or query a camera with the specified properties. 
    
    The resulting camera can be repositioned using the viewPlace
    command. Many of the camera settings only affect the resulting
    rendered image. E.g. the F/Stop, shutter speed, the film related
    options, etc. Scaling the camera icon does not change any camera
    properties.

    Args:
        aspectRatio: (create, edit, query) - The ratio of the film back width to the film back height.
        cameraScale: (create, edit, query) - Scale the camera.
        centerOfInterest: (create, edit, query) - Set the linear distance from the camera's eye point to the center of interest.
        clippingPlanes: (create, edit, query) - Activate manual clipping planes.
        depthOfField: (create, edit, query) - Determines whether a depth of field calculation is performed to give varying focus depending on the distance of the objects.
        displayFieldChart: (create, edit, query) - Activate display of the video field chart when looking through the camera.
        displayFilmGate: (create, edit, query) - Activate display of the film gate icons when looking through the camera.
        displayFilmOrigin: (create, edit, query) - Activate the display of the film origin guide when looking through the camera.
        displayFilmPivot: (create, edit, query) - Activate display of the film pivot guide when looking through the camera.
        displayGateMask: (create, edit, query) - Display the gate mask, file or resolution, as a shaded area to the edge of the viewport.
        displayResolution: (create, edit, query) - Activate display of the current rendering resolution (as defined in the render globals) when looking through the camera.
        displaySafeAction: (create, edit, query) - Activate display of the video Safe Action guide when looking through the camera.
        displaySafeTitle: (create, edit, query) - Activate display of the video Safe Title guide when looking through the camera.
        fStop: (create, edit, query) - A real lens normally contains a diaphragm or other stop which blocks some of the light that would otherwise pass through it. This stop is usually approximately round, and its diameter as seen from the front of the lens is called the lens diameter. The lens diameter is often described by its relation to the focal length of the lens. A lens whose diameter is one-eighth its local length is said to have an F-stop of 8. This is an optical property of the lens.
        farClipPlane: (create, edit, query) - Specify the distance to the far clipping plane.
        farFocusDistance: (create, edit, query) - Linear distance to the far focus plane.
        filmFit: (create, edit, query) - This describes how the digital image (in pixels) relates to the film back. Since the film back is defined in terms of real numbers with some arbitrary film aspect, and the digital image is defined in integer pixels with an equally arbitrary (and different) resolution, relating the two can get complicated. There are 4 choices:   horizontal  In this case the digital image is made to fit the film back exactly in the horizontal direction. This then gives each pixel a horizontal size = (film back width) / (horizontal resolution). The pixel height is then = (pixel width) / (pixel aspect ratio). Now that the pixel has a size, resolution gives us a complete image. That image will match the film back exactly in width. It will almost never match in height, either being too tall or too short. By playing with the numbers you can get it pretty close though. vertical This is the same idea as horizontal fit, only applied vertically. Thus the digital image will match the film back exactly in height, but miss in width. fill This is a convenience item. The system calculates both horizontal and vertical fits and then applies the one that makes the digital image larger than the film back. overscan Overscanning the film gate in the camera view allows us to choreograph action outside of the frustum from within the camera view without having to resort to a dolly or zoom. This feature is also essential for animating image planes.
        filmFitOffset: (create, edit, query) - Since we know from the above that the digital image may not match the film back exactly, we now have the question of how to position one relative to the other. Thus fit offset. Normally the centers are aligned. Fit offset lets you move the smaller image within the larger one. Specify the distance for film offset (inches).
        filmRollOrder: (create, edit, query) - Specifies how the roll is applied with respect to the pivot value.  Rotate-Translate The film back is first rotated then translated by the pivot point value. Translate-Rotate The film back is first translated then rotated by the film roll value.
        filmRollValue: (create, edit, query) - This specifies that amount of rotation around the film back. The roll value is specified in degrees. The rotation occurs around the specified pivot point. This value is used to compute a film roll matrix, which is a component of the post-projection matrix.
        filmTranslateH: (create, edit, query) - The horizontal film translation. Values are normalized to the viewing area.
        filmTranslateV: (create, edit, query) - The vertical film translation. Values are normalized to the viewing area.
        focalLength: (create, edit, query) - This is the distance along the lens axis between the lens and the film plane when "focal distance" is infinitely large. This is an optical property of the lens. This double precision parameter is always specified in millimeters.
        focusDistance: (create, edit, query) - Set the focus at a certain distance in front of the camera.
        homeCommand: (create, edit, query) - Specify the command to execute when "viewSet -home" is applied to this camera. All occurances of "%camera" will be replaced with the cameras name before viewSet runs the command.
        horizontalFieldOfView: (create, edit, query) - This is the film back width as seen by the lens when focused at infinity (ie., focal length away) measured as an angle. Note that it has nothing to do with pixels or the digital image or any aspects. Angle of view is a derived field, that is, it is not used internally by Alias and can be completely determined from other information. It is included as a convenience for the user. Its derivation is aov = 2 * atan( fbw / (2 * f) ) where "aov" is the angle of view, "fbw" is the film back width and "f" is the focal length.
        horizontalFilmAperture: (create, edit, query) - The horizontal width of the camera's film plane. The camera's film is located on the film plane. The extent of the film which will be exposed to an image of the scene in front of the lens is limited to a rectangular area described by the film back. This double precision parameter is always specified in inches.
        horizontalFilmOffset: (create, edit, query) - Horizontal offset from the center of the film back. Normally the film back will be centered on the lens axis. However, this need not be so. Film offset is the displacement of the center of the film back from the lens axis, also measured in inches. Note that offsetting the film back will distort the image, but will not alter the focus. This double precision parameter is always specified in inches.
        horizontalPan: (create, edit, query) - Horizontal 2D camera pan (inches)
        horizontalRollPivot: (create, edit, query) - The horizontal pivot point from the center of the film back. The pivot point is used during rotation of the film back.  The pivot is the point where the rotation occurs around. This double precision parameter corresponds to the normalized viewport. This value is a part of the post projection matrix.
        horizontalShake: (create, edit, query) - Another horizontal offset from the center of the film back, which can be used and stored on the camera in addition to the horizonal film offset attribute.  This allows for film-based camera shake internal to the camera.  This works in exactly the same units and coordinates that the film offset attribute does. The effect of this attribute is toggled by the shake enabled attribute.
        journalCommand: (create, edit, query) - Journal interactive camera commands. Commands can be undone when a camera is journaled.
        lensSqueezeRatio: (create, edit, query) - This is presently just an information field in the camera editor is meant to convey the horizontal distortion of the anamorphic lens normally used with some film formats. If it were used, it would do something like pixel aspect. Remember however that lens distortion (intentional or not) is slightly different than the output hardware's quantization. The fact that a "net" distortion parameter could be used for both may or may not confuse the issue.
        lockTransform: (create, edit, query) - Lock the camera. When a camera is locked, its transformation information, that is, its Translate and Rotate properties cannot be adjusted, and the center of interest point cannot be moved. For orthographic cameras, Orthographic Width is also locked. For camera groups, Aim and Up locator's translate is also locked. For stereo cameras, the root camera is locked.
        motionBlur: (create, edit, query) - Determines whether the camera's image is motion blured (as opposed to an object's image). For example, if you want to blur the camera movement when you are performing a flyby.
        name: (create, edit, query) - Name of the camera.
        nearClipPlane: (create, edit, query) - Specify the distance to the NEAR clipping plane.
        nearFocusDistance: (create, edit, query) - Linear distance to the near focus plane.
        orthographic: (create, edit, query) - Activate the orthographic camera.
        orthographicWidth: (create, edit, query) - Set the orthographic projection width.
        overscan: (create, edit, query) - Set the percent of overscan.
        panZoomEnabled: (create, edit, query) - Toggle camera 2D pan and zoom
        position: (create, edit, query) - Three linear values can be specified to translate the camera.
        postScale: (create, edit, query) - The post-scale value.  This value multiplied against the computed projection matrix. It is applied after the the film roll.
        preScale: (create, edit, query) - The pre-scale value. The value is multiplied against the computed projection matrix. It is applied before the film roll.
        renderPanZoom: (create, edit, query) - Toggle camera 2D pan and zoom in render
        rotation: (create, edit, query) - Three angular values can be specified to rotate the camera.
        shakeEnabled: (create, edit, query) - Toggles the effect of the horizontal and vertical shake attributes.
        shakeOverscan: (create, edit, query) - Controls the amount of overscan in the output rendered image. For use when adding film-based camera shake.  Acts as a multiplier to the film aperture on the camera.
        shakeOverscanEnabled: (create, edit, query) - Toggles the effect of the shake overscan attribute.
        shutterAngle: (create, edit, query) - Specify the shutter angle (degrees).
        startupCamera: (create, edit, query) - A startup camera is marked undeletable and implicit. This flag can be used to set or query the startup state of a camera. There must always be at least one startup camera.
        stereoHorizontalImageTranslate: (create, edit, query) - A film-back offset for use in stereo camera rigs.
        stereoHorizontalImageTranslateEnabled: (create, edit, query) - Toggles the effect of the stereo HIT attribute.
        verticalFieldOfView: (create, edit, query) - Set the vertical field of view.
        verticalFilmAperture: (create, edit, query) - The vertical height of the camera's film plane. This double precision parameter is always specified in inches.
        verticalFilmOffset: (create, edit, query) - Vertical offset from the center of the film back. This double precision parameter is always specified in inches.
        verticalLock: (create, edit, query) - Lock the size of the vertical film aperture.
        verticalPan: (create, edit, query) - Vertical 2D camera pan (inches)
        verticalRollPivot: (create, edit, query) - Vertical pivot point used for rotating the film back. This double precision parameter corresponds to the normalized viewport. This value is used to compute the film roll matrix, which is a component of the post projection matrix.
        verticalShake: (create, edit, query) - Vertical offset from the center of the film back.  See horizontal shake attribute description.  This is toggled by the shake enabled attribute.
        worldCenterOfInterest: (create, edit, query) - Camera world center of interest point.
        worldUp: (create, edit, query) - Camera world up vector.
        zoom: (create, edit, query) - The percent over the film viewable frustum to display
    """
    ...


def cameraSet(*args, active: bool = ..., appendTo: bool = ..., camera: Optional[Union[str, bool]] = ..., clearDepth: bool = ..., deleteAll: bool = ..., deleteLayer: bool = ..., insertAt: bool = ..., layer: Optional[Union[int, bool]] = ..., name: Optional[Union[str, bool]] = ..., numLayers: bool = ..., objectSet: Optional[Union[str, bool]] = ..., order: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command manages camera set nodes. Camera sets allow the users to
    break a single camera shot into layers. Instead of drawing all objects
    with a single camera, you can isolate the camera to only focus on
    certain objects and layer another camera into the viewport that draws
    the other objects. The situation to use camera sets primarily occurs
    when building stereoscopic scenes.
    
    For example, a set of stereo parameters may make the background
    objects divergent beyond the tolerable range of the human perceptual
    system. However, you like the settings because the main focus is in
    the foreground and the depth is important to the visual look of the
    scene.  You can use camera sets to break apart the shot into a
    foreground stereo camera and background stereo camera. The foreground
    stereo camera will retain the original parameters; however, it will
    only focus on the foreground elements.  The background stereo camera
    will have a different set of stereo parameters and will only draw the
    background element.
    
    Camera sets can be viewed using the stereo viewer and are currently only
    designed to work with stereo camera rigs.

    Args:
        active: (create, edit, query) - Gets / sets the active camera layer.
        appendTo: (create, edit) - Append a new camera and/or object set to then end of the cameraSet layer list. This flag cannot be used in conjunction with insert flag. Additionally, it requires the camera and/or objectSet flag to be used.
        camera: (create, edit, query) - Set/get the camera for a particular layer. When in query mode, You must specify the layer with the layer flag.
        clearDepth: (create, edit, query) - Specifies if the drawing buffer should be cleared before beginning the draw for that layer.
        deleteAll: (create, edit) - Delete all camera layers
        deleteLayer: (create, edit) - Delete a layer from the camera set. You must specify the layer using the layer flag.
        insertAt: (create, edit) - Inserts the specified camera and/or object set at the specified layer. This flag cannot be used in conjunction with the append flag. Additionally, this flag requires layer and camera (or objectSet) flag to be used.
        layer: (create, edit, query) - Specifies the layer index to be used when accessing layer information
        name: (create, query) - Gets or sets the name for the created camera set.
        numLayers: (create, query) - Returns the number of layers defined in the specified cameraSet
        objectSet: (create, edit, query) - Set/get the objectSet for a particular layer. When in query mode, you must specify the layer with the layer flag.
        order: (create, edit, query) - Set the order in which a particular layer is processed. This flag must be used in conjunction with the layer flag.
    """
    ...


def cameraView(*args, addBookmark: bool = ..., animate: bool = ..., bookmarkType: Optional[Union[int, bool]] = ..., camera: str = ..., name: Optional[Union[str, bool]] = ..., removeBookmark: bool = ..., setCamera: bool = ..., setView: bool = ..., edit: bool = ...) -> Any:
    r"""
    This command creates a preset view for a camera which is then
    independent of the camera. The view stores a camera's eye point,
    center of interest point, up vector, tumble pivot, horizontal
    aperture, vertical aperature, focal length, orthographic width,
    and whether the camera is orthographic or perspective by default.
    Or you can only store 2D pan/zoom attributes by setting the
    bookmarkType to 1. These settings can be applied to any other
    camera through the set camera flag. 
    
    This command can be used for creation or edit of camera view
    objects.  This command can only be executed with one of the add
    bookmark, or remove bookmark and one of set camera, or the set
    view flags set.

    Args:
        addBookmark: (create, edit) - Associate this view with the camera specified or the camera in the active model panel. This flag can be used for creation or edit.
        animate: (create, edit) - Set the animation capability for view switches.
        bookmarkType: (create) - Specify the bookmark type, which can be: 0. 3D bookmark; 1. 2D Pan/Zoom bookmark.
        camera: (edit) - Specify the camera to use. This flag should be used in conjunction with the add bookmark, remove bookmark, set camera, or set view flags. If this flag is not specified the camera in the active model panel will be used.
        name: (create) - Set the name of the view. This flag can only be used for creation.
        removeBookmark: (edit) - Remove the association of this view with the camera specified or the camera in the active model panel. This can only be used with edit.
        setCamera: (edit) - Set this view into a camera specified by the camera flag or the camera in the active model panel. This flag can only be used with edit.
        setView: (edit) - Set the camera view to match a camera specified or the active model panel. This flag can only be used with edit.
    """
    ...


def checkDefaultRenderGlobals(*args, edit: bool = ..., query: bool = ...) -> Any:
    r"""
    To query whether or not the defaultRenderGlobals node has been modified since the last file save, use `ls -modified`. To force the scene to be dirty/clean use `file -modified`

    Args:
    """
    ...


def convertIffToPsd(*args, iffFileName: Optional[Union[str, bool]] = ..., psdFileName: Optional[Union[str, bool]] = ..., xResolution: Optional[Union[int, bool]] = ..., yResolution: Optional[Union[int, bool]] = ..., query: bool = ...) -> Any:
    r"""
    Converts iff file to PSD file of given size

    Args:
        iffFileName: (create, query) - Input iff file name
        psdFileName: (create, query) - Output file name
        xResolution: (create, query) - X resolution of the image
        yResolution: (create, query) - Y resolution of the image
    """
    ...


def convertSolidTx(*args, alpha: bool = ..., antiAlias: bool = ..., backgroundColor: Optional[Union[Tuple[int, int, int], bool]] = ..., backgroundMode: Optional[Union[str, bool]] = ..., camera: Optional[Union[str, bool]] = ..., componentRange: bool = ..., doubleSided: bool = ..., fileFormat: Optional[Union[str, bool]] = ..., fileImageName: Optional[Union[str, bool]] = ..., fillTextureSeams: bool = ..., force: bool = ..., fullUvRange: bool = ..., name: Optional[Union[str, bool]] = ..., pixelFormat: Optional[Union[str, bool]] = ..., resolutionX: Optional[Union[int, bool]] = ..., resolutionY: Optional[Union[int, bool]] = ..., reuseDepthMap: bool = ..., samplePlane: bool = ..., samplePlaneRange: Optional[Union[Tuple[float, float, float, float], bool]] = ..., shadows: bool = ..., uvBBoxIntersect: bool = ..., uvRange: Optional[Union[Tuple[float, float, float, float], bool]] = ..., uvSetName: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to convert a texture on a surface to a file texture. The first
    argument is a rendering node or attribute. If only the node is
    specified, the outColor attribute will be sampled. If the node does
    not have an outColor attribute, the first attribute on the node which
    is: readable, not writable, not hidden, connectable, and not a multi
    is used. If lighting is to be baked, a shading group must be specified
    as the texture.
    
    The current selection will be used if a texture and surface are not
    specified.
    
    An image file will be generated for each object and stored in your
    image segment of your project. The filename will be formatted using
    the texture and surface names as follows:
    
     {texture}-{surface}.{fileExtension} 
    
    However, if force is off and there is a name collision a version
    number will be determined and the filename will be formatted as
    follows:
    
     {texture}-{surface}.{version}.{fileExtension} 
    
    If uv/uvsetName option is specified the filename will include
    {surface}-{uvname} instead of {surface}.

    Args:
        alpha: (create) - Specify whether to compute the transparency when baking lighting. The conversion will sample both the color and transparency of the shading network; the alpha channel of the file texture will be set to correspond to the result from sampling the transparency. By default transparency is not computed.
        antiAlias: (create) - Perform anti-aliasing on the resulting image. Convert solid texture will generally take four times longer than without anti-aliasing. By default this flag is off.
        backgroundColor: (create) - Set the background color to a specific value. Default is to use the shader default color to fill the background. Valid values range from 0 to 255 if the pixel format is 8 bits per channel, or 0 to 65535 if the pixel format is 16 bits per channel. This flag automatically sets -backgroundMode to "color". Default is black: 0 0 0.
        backgroundMode: (create) - Defines how the background of the texture should be filled. Three modes are available: "shader" or 1: uses the default shader color. "color" or 2: uses the color given by -backgroundColor flag. "extend" or 3: extends outwards the color along the seam edges. Default is "shader".
        camera: (create) - Specify a camera to use in baking lighting. If a camera is not specified the camera in the active view will be used.
        componentRange: (create) - If one or more components have been selected to use, then if this flag is set, then the uv range of the components is used to fit into the texture map resolution. By default this flag is set to false.
        doubleSided: (create) - Specify whether the sampler should flip the surface normal if the sample point faces away from the camera. Note: flipping the normal will make the result dependent on the camera (ie. one camera may flip normals where different camera wouldn't). It's not recommended that doubleSided be used in combination with shadows. By default this flag is false.
        fileFormat: (create) - File format to be used for output. IFF is the default if unspecified. Other valid formats are: als: Alias PIX cin: Cineon eps: EPS gif: GIF iff: Maya IFF jpg: JPEG yuv: Quantel rla: Wavefront RLA sgi: SGI si: SoftImage (.pic) tga: Targa tif: TIFF bmp: Windows Bitmap
        fileImageName: (create) - Specify the output path and name of file texture image. If the file name doesn't contain a directory separator, the image will be written to source images of the current project. The file will not be versioned if it already exists.
        fillTextureSeams: (create) - Specify whether or not to overscan the polygon beyond its outer edges, when creating the file texture, in order to fill the texture seams. Default is true.
        force: (create) - If the output image already exists overwrite it. By default this flag is off.
        fullUvRange: (create) - Sample using the full uv range of the surface. This flag cannot be used with the -uvr flag. A 2D texture placement node will be created and connected to the file texture. The placement's translate and coverage will be set according to the full UV range of the surface.
        name: (create) - Set the name of the file texture node. Name conflict resolution will be used to determine valid names when multiple objects are specified.
        pixelFormat: (create) - Specifies the pixel format of the image. Note that not all file formats support all pixel formats. Available options: "8": 8 bits per channel, unsigned (0-255) "16": 16 bits per channel, unsigned (0-65535) Default is "8".
        resolutionX: (create) - Set the horizontal image resolution. If this flag is not specified, the resolution will be set to 256.
        resolutionY: (create) - Set the vertical image resolution. If this flag is not specified, the resolution will be set to 256.
        reuseDepthMap: (create) - Specify whether or not to reuse all the generated dmaps. Default is false.
        samplePlane: (create) - Specify whether to sample using a virtual plane. This virtual plane has texture coordinates in the rectangle defined by the -samplePlaneRange flag. If the -samplePlaneRange flag is not set then the virtual plane defaults to having texture coordinates in the (0,0) to (1,1) square. If this option is set than all surface based arguments will be ignored.
        samplePlaneRange: (create) - Specify the uv range of the texture coordinates used to sample if the -samplePlane option is set. There are four arguments corresponding to uMin, uMax, vMin and vMax. By default the virtual plane is from uMin 0 to uMax 1, and vMin 0 to vMax 1.
        shadows: (create) - Specify whether to compute shadows when baking lighting. Disk based shadow maps will be used. Only lights with depth map shadows enabled will contribute to the shading. By default shadows are not computed.
        uvBBoxIntersect: (create) - This flag is obsolete.
        uvRange: (create) - Specify the uv range in which samples will be computed. There are four arguments corresponding to uMin, uMax, vMin and vMax. Each value should be specified based on the surface's uv space. A 2D texture placement node will be created and connected to the file texture. The placement's frame translate and coverage will be set according to the uv range specified. By default the entire uv range of the surface will be used.
        uvSetName: (create) - Specify which uv set has to be used as the driving parametrization for convert solid.
    """
    ...


def convertTessellation(*args, allCameras: bool = ..., camera: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Command to translate the basic tessellation attributes to advanced.
    If a camera flag is specified the translation will be based on the distance
    the surface is from the camera. The closer the surface is to the camera the
    more triangles there will be in the tessellation. If the "-allCameras" flags
    is specified, the renderable camera closest to the surface will be used to
    set the tessellation. The camera tessellation estimate is also dependent on
    the current render resolution; a higher resolution the result in a more
    finely tessellated surface.
    Multiple NURB surfaces may be specified on the command line, or if no
    command arguments are specified the surfaces on the active list will be
    used.
    This command operates by calculating the chord height such that smooth
    tessellation is achieved when the surface is rendered.  The advanced
    tessellation setting will be enabled on each surface specified, the
    primary tessellation parameters will be set, and chord height will be
    used as the secondary criteria.

    Args:
        allCameras: (create) - Specifies that all renderable cameras should be used in calculating     the screen based tessellation.
        camera: (create) - Specifies the camera which should be used in calculating the screen     based tessellation.
    """
    ...


def createLayeredPsdFile(*args, imageFileName: Optional[Union[Tuple[str, str, str], bool]] = ..., psdFileName: Optional[Union[str, bool]] = ..., xResolution: Optional[Union[int, bool]] = ..., yResolution: Optional[Union[int, bool]] = ...) -> Any:
    r"""
    Creates a  layered PSD file with image names as input to individual layers

    Args:
        imageFileName: (create, multiuse) - Layer name, blend mode, Image file name  The image in the file will be transferred to layer specified. The image file specified can be in any of the formats supported by maya (ex. iff, jpg, gif, tif etc.). The blend mode options are : "Normal", "Dissolve", "Dark", "Multiply", "Color Burn", "Linear Burn", "Lighten", "Screen", "Color Dodge", "Linear Dogde", "Overlay", "Soft Light", "Hard Light", "Dissolve", "Vivid Light", "Linear Light", "Pin Light", "Hard Mix", "Difference", "Exclusion", "Hue", "Saturation", "Color",  "Luminosity"
        psdFileName: (create) - PSD file name.
        xResolution: (create) - X - resolution of the image.
        yResolution: (create) - Y - resolution of the image.
    """
    ...


def createRenderLayer(*args, empty: bool = ..., g: bool = ..., makeCurrent: bool = ..., name: Optional[Union[str, bool]] = ..., noRecurse: bool = ..., number: Optional[Union[int, bool]] = ...) -> Any:
    r"""
    Create a new render layer.  The render layer number will be assigned
    based on the first unassigned number not less than the base index number
    found in the render layer global parameters.  Normally all objects and
    their descendants will be added to the new render layer but if '-noRecurse'
    is specified then only the objects themselves will be added. Only transforms
    and geometry will be added to the new render layer.

    Args:
        empty: (create) - If set then create an empty render layer. The global flag or specified member list will take precidence over  use of this flag.
        g: (create) - If set then create a layer that contains all DAG objects in the scene. Any future objects created will also automatically become members of this layer. The global flag will take precidence over use of the empty flag or specified member list.
        makeCurrent: (create) - If set then make the new render layer the current one.
        name: (create) - Name of the new render layer being created.
        noRecurse: (create) - If set then only add specified objects to the render layer.  Otherwise all descendants will also be added.
        number: (create) - Number for the new render layer being created.
    """
    ...


def defaultLightListCheckBox(*args, annotation: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., fullPathName: bool = ..., height: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., isObscured: bool = ..., label: Optional[Union[str, bool]] = ..., manage: bool = ..., noBackground: bool = ..., numberOfPopupMenus: bool = ..., parent: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., shadingGroup: Optional[Union[str, bool]] = ..., statusBarMessage: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., visible: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a checkBox that controls whether a
    shadingGroup is connected/disconnected from the defaultLightList.

    Args:
        annotation: (create, edit, query) - Annotate the control with an extra string value.
        backgroundColor: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag: (create, edit, query) - Add a documentation flag to the control.  The documentation flag has a directory structure. (e.g., -dt render/multiLister/createNode/material)
        dragCallback: (create, edit) - Adds a callback that is called when the middle mouse button is pressed.  The MEL version of the callback is of the form:  global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  The proc returns a string array that is transferred to the drop site. By convention the first string in the array describes the user settable message type.  Controls that are application defined drag sources may ignore the callback. $mods allows testing for the key modifiers CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3 == CTRL + SHIFT.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def callbackName( dragControl, x, y, modifiers ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "x", "y", "modifiers".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")
        dropCallback: (create, edit) - Adds a callback that is called when a drag and drop operation is released above the drop site.  The MEL version of the callback is of the form:  global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  The proc receives a string array that is transferred from the drag source. The first string in the msgs array describes the user defined message type. Controls that are application defined drop sites may ignore the callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "dropControl", "messages", "x", "y", "type".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")
        enable: (create, edit, query) - The enable state of the control.  By default, this flag is set to true and the control is enabled.  Specify false and the control will appear dimmed or greyed-out indicating it is disabled.
        enableBackground: (create, edit, query) - Enables the background color of the control.
        enableKeyboardFocus: (create, edit, query) - If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse. This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls. If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        fullPathName: (query) - Return the full path name of the widget, which includes all the parents.
        height: (create, edit, query) - The height of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
        highlightColor: (create, edit, query) - The highlight color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.
        isObscured: (query) - Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.
        label: (create, edit) - Value of the checkbox label
        manage: (create, edit, query) - Manage state of the control.  An unmanaged control is not visible, nor does it take up any screen real estate.  All controls are created managed by default.
        noBackground: (create, edit) - Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
        numberOfPopupMenus: (query) - Return the number of popup menus attached to this control.
        parent: (create, query) - The parent layout for this control.
        popupMenuArray: (query) - Return the names of all the popup menus attached to this control.
        preventOverride: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        shadingGroup: (create, edit) - The shading group that is to be connected/disconnected from the defaultLightList.
        statusBarMessage: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
        visible: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def directionalLight(*args, decayRate: Optional[Union[int, bool]] = ..., discRadius: Optional[Union[float, bool]] = ..., exclusive: bool = ..., intensity: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., position: Optional[Union[Tuple[float, float, float], bool]] = ..., rgb: Optional[Union[Tuple[float, float, float], bool]] = ..., rotation: Optional[Union[Tuple[float, float, float], bool]] = ..., shadowColor: Optional[Union[Tuple[float, float, float], bool]] = ..., shadowDither: Optional[Union[float, bool]] = ..., shadowSamples: Optional[Union[int, bool]] = ..., softShadow: bool = ..., useRayTraceShadows: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    TlightCmd is the base class for other light commands.
    TnonAmbientLightCmd is a class that looks like a command but
    is not.  It is a base class for the extended/nonExtended
    lights.
    TnonExtendedLightCmd is a base class and not a real command. It is inherited by several
    lights: TpointLight, TdirectionalLight, TspotLight etc.
    The directionalLight command is used to edit the parameters
    of existing directionalLights, or to create new ones. The
    default behaviour is to create a new directionallight.
    
    This is the commmand that instantiates an directionalLight
    or edits the parameters of an existing one.
    TdirectionalLightCmd inherits from TnonExtendedLightCmd
    which defines softShadow flags.
    See TlightCmd for a global picture of the light commands.
    
    TdirectionalLightCmd behaves like any other command, it
    has flags, saves undo information etc. the only slightly
    different behaviour is that it calls up to
    TnonExtendedLightCmd to complete the functionality of
    the command.

    Args:
        decayRate: (create) - Decay rate of the light (0-no decay, 1-slow, 2-realistic, 3-fast)
        discRadius: (create, query) - Radius of shadow disc.
        exclusive: (create, query) - True if the light is exclusively assigned
        intensity: (create, query) - Intensity of the light
        name: (create, query) - Name of the light
        position: (create, query) - Position of the light
        rgb: (create, query) - RGB colour of the light
        rotation: (create, query) - Rotation of the light for orientation, where applicable
        shadowColor: (create, query) - Color of the light's shadow
        shadowDither: (create, query) - Shadow dithering value.
        shadowSamples: (create, query) - Numbr of shadow samples to use
        softShadow: (create, query) - True if soft shadowing is to be enabled
        useRayTraceShadows: (create, query) - True if ray trace shadows are to be used
    """
    ...


def displacementToPoly(*args, findBboxOnly: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command bakes geometry with displacement mapping into a polygonal object.

    Args:
        findBboxOnly: (create, edit, query) - When used, only the bounding box scale for the displaced object is found.
    """
    ...


def doBlur(*args, colorFile: Optional[Union[str, bool]] = ..., length: Optional[Union[float, bool]] = ..., memCapSize: Optional[Union[float, bool]] = ..., sharpness: Optional[Union[float, bool]] = ..., smooth: Optional[Union[float, bool]] = ..., smoothColor: bool = ..., vectorFile: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    The doBlur command  will invoke the blur2d, which is a Maya
    stand-alone application to do 2.5 motion blur given the color image
    and the motion vector file.  For a given input colorFile name, e.g.
    "xxx.iff", the output blurred image will be "xxx_blur.iff" in the
    same directory as the input colorFile.  There is currently no control
    over the name of the output blurred image.

    Args:
        colorFile: (create) - Name of the input color image to be blurred.
        length: (create) - Scale applied on the motion vector. Ranges from 0 to infinity.
        memCapSize: (create) - Size of the memory cap, in bytes
        sharpness: (create) - Determines  the shape of the blur filter. The higher the value, the narrower the filter, the sharper the blur. The lower the value, the wider the filter, the more spread out the blur. Ranges from 0 to infinity.
        smooth: (create) - Filter size to smooth the blurred image. The higher the value, the more anti-aliased the alpha channel. Ranges from 1.0 to 5.0.
        smoothColor: (create) - Whether to smooth the color or not.
        vectorFile: (create) - Name of the input motion vector file.
    """
    ...


def dolly(*args, absolute: bool = ..., distance: Optional[Union[float, bool]] = ..., dollyTowardsCenter: bool = ..., orthoScale: Optional[Union[float, bool]] = ..., relative: bool = ...) -> Any:
    r"""
    The dolly command moves a camera along the viewing direction in
    the world space. The viewing-direction and up-direction of the
    camera are not altered. There are two modes of operation: 
    
    Relative mode: for a perspective camera, the camera is moved along
    its viewing direction, and the distance of travel is computed with
    respect to the current position of the camera in the world
    space. In relative mode, when the camera is moved, its COI is
    moved along with it, and is kept at the same distance, in front of
    the camera, as before applying the dolly operation. For
    orthographic camera, the viewing width of the camera is changed by
    scaling its ortho width by the new value specified on the command
    line. 
    
    Absolute mode: for a perspective camera, the camera is moved along
    its viewing direction, to the distance that is computed with
    respect to the current position of the world center of interest
    (COI) of the camera. In the absolute mode, when the camera is
    moved, the COI of the camera is not moved with the camera, but it
    is fixed at its current location in space. For orthographic
    camera, the viewing width of the camera is changed by replacing
    its ortho width with the new value specified on the command
    line. This command may be applied to more than one cameras;
    objects that are not cameras are ignored. When no camera name
    supplied on the command line, this command is applied to all
    currently active cameras. 
    
    The dolly command can be applied to either a perspective or an
    orthographic camera.

    Args:
        absolute: (create) - This flag modifies the behavior of the distance and orthoScale flags. When used in conjunction with the distance flag, the distance argument specifies how far the camera's eye point should be set from the camera's center of interest. When used with the orthoScale flag, the orthoScale argument specifies the camera's new ortho width.
        distance: (create) - Unit distance to dolly a perspective camera.
        dollyTowardsCenter: (create) - This flag controls whether the dolly is performed towards the center of the view (if true), or towards the point where the user clicks (if false). By default, dollyTowardsCenter is on.
        orthoScale: (create) - Scale to change the ortho width of an orthographic camera.
        relative: (create) - This flag modifies the behavior of the distance and orthoScale flags. When used in conjunction with the distance flag, the camera eye and center of interest are both moved by the amount specified by the distance flag's argument. When used with the orthoScale flag, the orthoScale argument is used multiply the camera's ortho width.By default the relative flag is always on.
    """
    ...


def editRenderLayerAdjustment(*args, attributeLog: bool = ..., layer: Optional[Union[str, bool]] = ..., nodeLog: bool = ..., remove: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to create, edit, and query adjustments to render
    layers. An adjustment allows different attribute values or connections
    to be used depending on the active render layer.

    Args:
        attributeLog: (query) - Output all adjustments for the specified layer sorted by attribute name.
        layer: (create, query) - Specified layer in which the adjustments will be modified. If not specified the active render layer will be used.
        nodeLog: (query) - Output all adjustments for the specified layer sorted by node name.
        remove: (create) - Remove the specified adjustments from the render layer. If an adjustment is removed from the current layer, the specified plug will revert back to it's master value determined by the default render layer.
    """
    ...


def editRenderLayerGlobals(*args, baseId: Optional[Union[int, bool]] = ..., currentRenderLayer: Optional[Union[str, bool]] = ..., enableAutoAdjustments: bool = ..., mergeType: Optional[Union[int, bool]] = ..., useCurrent: bool = ..., query: bool = ...) -> Any:
    r"""
    Edit the parameter values common to all render layers.  Some of these
    paremeters, eg. baseId and mergeType, are stored as preferences and
    some, eg. currentRenderLayer, are stored in the file.

    Args:
        baseId: (create, query) - Set base layer ID.  This is the number at which new layers start searching for a unique ID.
        currentRenderLayer: (create, query) - Set current render layer. This will will update the renderLayerManger and all DAG objects to identify them as members of the render layer. This flag may also be used in conjunction with "useCurrent" to automatically add new DAG objects to the active layer. The "isCurrentRenderLayerChanging" condition can be used to determine when the current layer is being changed and adjustments are being applied to the scene.
        enableAutoAdjustments: (create, query) - Set whether or not to enable automatic creation of adjustments when certain attributes (ie. surface render stats, shading group assignment, or render settings) are changed.
        mergeType: (create, query) - Set file import merge type.  Valid values are 0, none, 1, by number, and 2, by name.
        useCurrent: (create, query) - Set whether or not to enable usage of the current render layer as the destination for all new nodes.
    """
    ...


def editRenderLayerMembers(*args, fullNames: bool = ..., noRecurse: bool = ..., remove: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to query and edit memberships to render layers. Only
    transform and geometry nodes may be members. At render time, all
    descendants of the members of a render layer will also be included in the
    render layer.

    Args:
        fullNames: (query) - (Query only.) If set then return the full DAG paths of the objects in the layer.  Otherwise return just the name of the object.
        noRecurse: (create) - If set then only add selected objects to the render layer.  Otherwise all descendants of the selected objects will also be added. This flag may be applied to adding or removing objects from the layer.
        remove: (create) - Remove the specified objects from the render layer.
    """
    ...


def exclusiveLightCheckBox(*args, annotation: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., fullPathName: bool = ..., height: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., isObscured: bool = ..., label: Optional[Union[str, bool]] = ..., light: Optional[Union[str, bool]] = ..., manage: bool = ..., noBackground: bool = ..., numberOfPopupMenus: bool = ..., parent: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., statusBarMessage: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., visible: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a checkBox that controls a light's exclusive
    non-exclusive status.  An exclusive light is one that is not
    hooked up to the default-light-list, thus it does not illuminate all
    objects be default.  However an exclusive light can be linked to
    an object.

    Args:
        annotation: (create, edit, query) - Annotate the control with an extra string value.
        backgroundColor: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag: (create, edit, query) - Add a documentation flag to the control.  The documentation flag has a directory structure. (e.g., -dt render/multiLister/createNode/material)
        dragCallback: (create, edit) - Adds a callback that is called when the middle mouse button is pressed.  The MEL version of the callback is of the form:  global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  The proc returns a string array that is transferred to the drop site. By convention the first string in the array describes the user settable message type.  Controls that are application defined drag sources may ignore the callback. $mods allows testing for the key modifiers CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3 == CTRL + SHIFT.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def callbackName( dragControl, x, y, modifiers ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "x", "y", "modifiers".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")
        dropCallback: (create, edit) - Adds a callback that is called when a drag and drop operation is released above the drop site.  The MEL version of the callback is of the form:  global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  The proc receives a string array that is transferred from the drag source. The first string in the msgs array describes the user defined message type. Controls that are application defined drop sites may ignore the callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "dropControl", "messages", "x", "y", "type".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")
        enable: (create, edit, query) - The enable state of the control.  By default, this flag is set to true and the control is enabled.  Specify false and the control will appear dimmed or greyed-out indicating it is disabled.
        enableBackground: (create, edit, query) - Enables the background color of the control.
        enableKeyboardFocus: (create, edit, query) - If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse. This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls. If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        fullPathName: (query) - Return the full path name of the widget, which includes all the parents.
        height: (create, edit, query) - The height of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
        highlightColor: (create, edit, query) - The highlight color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.
        isObscured: (query) - Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.
        label: (create, edit) - Value of the checkbox label
        light: (create) - The light that is to be made exclusive/non-exclusive.
        manage: (create, edit, query) - Manage state of the control.  An unmanaged control is not visible, nor does it take up any screen real estate.  All controls are created managed by default.
        noBackground: (create, edit) - Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
        numberOfPopupMenus: (query) - Return the number of popup menus attached to this control.
        parent: (create, query) - The parent layout for this control.
        popupMenuArray: (query) - Return the names of all the popup menus attached to this control.
        preventOverride: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        statusBarMessage: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
        visible: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def frameBufferName(*args, autoTruncate: bool = ..., camera: Optional[Union[str, bool]] = ..., renderLayer: Optional[Union[str, bool]] = ..., renderPass: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Returns the frame buffer name for a given renderPass renderLayer and
    camera combination. Optionally, this command can apply a name truncation
    algorithm so that the frameBuffer name will respect the maximum length
    imposed by the destination file format, if applicable.

    Args:
        autoTruncate: (create) - use this flag to apply a name truncation algorithm so that the frameBuffer name will respect the maximum length imposed by the destination file format, if applicable.
        camera: (create) - Specify a camera
        renderLayer: (create) - Specify a renderer layer
        renderPass: (create) - Specify a renderer pass
    """
    ...


def getRenderDependencies(*args) -> Any:
    r"""
    Command to return dependencies of an image source.  Image sources (such
    as render targets) can depend on other upstream image sources that result
    from renderings of 3D scene, or renderings of 2D compositing graphs.
    This command returns these dependencies, so that they can be analyzed and
    rendered.

    Args:
    """
    ...


def getRenderTasks(*args, camera: Optional[Union[str, bool]] = ..., renderLayer: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Command to return render tasks to render an image source.  Image
    source can depend on upstream image sources that result from
    renderings of 3D scene, or 2D renderings (e.g. render targets).
    This command obtains the graph of image source render dependencies,
    and creates render tasks according to these dependencies.  A render
    task has context, which can be camera, render layer, and resolution,
    or other, renderer-specific context.  Because of image source
    overrides, the render task context depends on the path through the
    render dependency graph, with the most upstream override for a context
    item applied.  As there can be multiple paths through a render
    dependency graph to a render dependency, there can be multiple render
    tasks for a given render dependency.

    Args:
        camera: (create) - Camera node to use in the render context for the image source render task.
        renderLayer: (create) - Render layer to use in the render context for the image source render task.
    """
    ...


def glRender(*args, accumBufferPasses: Optional[Union[int, bool]] = ..., alphaSource: Optional[Union[str, bool]] = ..., antiAliasMethod: Optional[Union[str, bool]] = ..., cameraIcons: bool = ..., clearClr: Optional[Union[Tuple[float, float, float], bool]] = ..., collisionIcons: bool = ..., crossingEffect: bool = ..., currentFrame: bool = ..., drawStyle: Optional[Union[str, bool]] = ..., edgeSmoothness: Optional[Union[float, bool]] = ..., emitterIcons: bool = ..., fieldIcons: bool = ..., flipbookCallback: Optional[Union[str, bool]] = ..., frameEnd: Optional[Union[int, bool]] = ..., frameIncrement: Optional[Union[int, bool]] = ..., frameStart: Optional[Union[int, bool]] = ..., fullResolution: bool = ..., grid: bool = ..., imageDirectory: Optional[Union[str, bool]] = ..., imageName: Optional[Union[str, bool]] = ..., imageSize: Optional[Union[Tuple[int, int, float], bool]] = ..., lightIcons: bool = ..., lightingMode: Optional[Union[str, bool]] = ..., lineSmoothing: bool = ..., offScreen: bool = ..., renderFrame: Optional[Union[str, bool]] = ..., renderSequence: Optional[Union[str, bool]] = ..., sharpness: Optional[Union[float, bool]] = ..., shutterAngle: Optional[Union[float, bool]] = ..., textureDisplay: bool = ..., transformIcons: bool = ..., useAccumBuffer: bool = ..., viewport: Optional[Union[Tuple[int, int, float], bool]] = ..., writeDepthMap: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command provides access to the Hardware Render Manager (HRM). There
    is one-and-only-one HRM in maya. The HRM controls the rendering performed
    in the hardware render buffer window. This command allows shell scripts,
    to modify the render state, and to initiate a render request.

    Args:
        accumBufferPasses: (edit, query) - Set the number of accum buffer render passes.
        alphaSource: (edit, query) - Control the alpha source when writing image files. Valid values include: off, alpha, red, green, blue, luminance, clamp, invClamp.
        antiAliasMethod: (edit, query) - Set the method used for anti-aliasing polygons: off, uniform, gaussian.
        cameraIcons: (edit, query) - Set display status of camera icons.
        clearClr: (edit, query) - Set the viewport clear color (0 - 1).
        collisionIcons: (edit, query) - Set display status of collison model icons.
        crossingEffect: (edit, query) - Enable/disable image filtering with a convolution filter.
        currentFrame: (query) - Returns the current frame being rendered.
        drawStyle: (edit, query) - Set the object drawing style: boundingBox, points, wireframe, flatShaded, smoothShaded.
        edgeSmoothness: (edit, query) - Controls the amount of edge smoothing. A value of 0.0 gives no smoothing, 1.0 gives default smoothing, and any other value scales the amount of default smoothing. Must enable the accumulation buffer.
        emitterIcons: (edit, query) - Set display status of emitter icons.
        fieldIcons: (edit, query) - Set display status of field icons.
        flipbookCallback: (edit, query) - Register a procedure to be called after the render sequence has completed. Used to build the flipbook pulldown menu. See the example section for more details about how to build this procedure.
        frameEnd: (edit, query) - Set the last frame to be rendered.
        frameIncrement: (edit, query) - Set the frame increment during rendering.
        frameStart: (edit, query) - Set the first frame to be rendered.
        fullResolution: (edit, query) - Enable/disable rendering to full image output resolution. Must set a valid image output resolution (-is).
        grid: (edit, query) - Set display status of the grid.
        imageDirectory: (edit, query) - Set the directory for the image files.
        imageName: (edit, query) - Set the base name of the image files.
        imageSize: (edit, query) - Set the image output size. Takes width, height and aspect ratio. Pass 0,0,0 to use current port size. The image size must be equal to or greater then the viewport size. Large images will be tiled if full resolution rendering has been enabled (-fr/fullResolution).
        lightIcons: (edit, query) - Set display status of light icons.
        lightingMode: (edit, query) - Set the lighting mode used for rendering: all, selected, default.
        lineSmoothing: (edit, query) - Enable/disable anti-aliased lines.
        offScreen: (edit, query) - When set, this toggle allow HRM to use an offscreen buffer to render the view. This allows HRM to work when the application is iconified, or obscured
        renderFrame: (edit, query) - Render the current frame. Requires the name of the view in which to render.
        renderSequence: (edit, query) - Render the current frame sequence. Requires the name of the view in which to render.
        sharpness: (edit, query) - Control the sharpness level of the convolution filter.
        shutterAngle: (edit, query) - Set the shutter angle used for motion blur (0 - 1). A value of 0.0 gives no blurring, 0.5 gives correct blurring, and 1.0 gives continuous blurring. Must enable the accumulation buffer.
        textureDisplay: (edit, query) - Enable/disable texture map display.
        transformIcons: (edit, query) - Set display status of transform icons.
        useAccumBuffer: (edit, query) - Enable/disable the accumulation buffer.
        viewport: (edit, query) - Set the viewport size. Pass in the width, height and aspect ratio. This size will be used for all test rendering and image output size unless full resolution (-fr) has been set and a valid image output size (-is) has been set.
        writeDepthMap: (edit, query) - Enable/disable writing of zdepth to image files.
    """
    ...


def glRenderEditor(*args, control: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., exists: bool = ..., filter: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., highlightConnection: Optional[Union[str, bool]] = ..., lockMainConnection: bool = ..., lookThru: Optional[Union[str, bool]] = ..., mainListConnection: Optional[Union[str, bool]] = ..., panel: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., selectionConnection: Optional[Union[str, bool]] = ..., stateString: bool = ..., unParent: bool = ..., unlockMainConnection: bool = ..., updateMainConnection: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., viewCameraName: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create a glRender view. This is a special view used for hardware
    rendering. This command is used to create and reparent the view
    as needed to support panels. See the glRender command for controlling
    the specific behavior of the hardware rendering.

    Args:
        control: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag: (create, edit, query) - Attaches a tag to the editor.
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        filter: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        forceMainConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        highlightConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        lockMainConnection: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        lookThru: (create, edit, query) - Specify which camera the glRender view should be using.
        mainListConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        panel: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        selectionConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        stateString: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        unParent: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
        viewCameraName: (query) - Returns the name of the current camera used by the glRenderPanel. This is a query only flag.
    """
    ...


def hwReflectionMap(*args, backTextureName: Optional[Union[str, bool]] = ..., bottomTextureName: Optional[Union[str, bool]] = ..., cubeMap: bool = ..., decalMode: bool = ..., enable: bool = ..., frontTextureName: Optional[Union[str, bool]] = ..., leftTextureName: Optional[Union[str, bool]] = ..., rightTextureName: Optional[Union[str, bool]] = ..., sphereMapTextureName: Optional[Union[str, bool]] = ..., topTextureName: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a hwReflectionMap node for having reflection on
    textured surfaces that currently have their boolean attribute
    displayHWEnvironment set to true.

    Args:
        backTextureName: (query) - This flag specifies the file texture name for the back side of the cube. Default is none When queried, this flag returns a string.
        bottomTextureName: (query) - This flag specifies the file texture name for the bottom side of the cube. Default is none When queried, this flag returns a string.
        cubeMap: (query) - If on, the reflection of the textures is done using the cube mapping. Default is false. The reflection is done using sphere mapping. When queried, this flag returns a boolean.
        decalMode: (query) - If on, the reflection color replaces the surface shading. Default is false. The reflection is multiplied to the surface shading. When queried, this flag returns a boolean.
        enable: (query) - If on, enable the corresponding hwReflectionMap node. Default is false. When queried, this flag returns a boolean.
        frontTextureName: (query) - This flag specifies the file texture name for the front side of the cube. Default is none When queried, this flag returns a string.
        leftTextureName: (query) - This flag specifies the file texture name for the left side of the cube. Default is none When queried, this flag returns a string.
        rightTextureName: (query) - This flag specifies the file texture name for the right side of the cube. Default is none When queried, this flag returns a string.
        sphereMapTextureName: (query) - This flag specifies the file texture name for the sphere mapping option. Default is none When queried, this flag returns a string.
        topTextureName: (query) - This flag specifies the file texture name for the top side of the cube. Default is none When queried, this flag returns a string.
    """
    ...


def hwRender(*args, acceleratedMultiSampleSupport: bool = ..., activeTextureCount: bool = ..., camera: Optional[Union[str, bool]] = ..., currentFrame: bool = ..., currentView: bool = ..., edgeAntiAliasing: Optional[Union[Tuple[int, int], bool]] = ..., fixFileNameNumberPattern: bool = ..., frame: Optional[Union[float, bool]] = ..., fullRenderSupport: bool = ..., height: Optional[Union[int, bool]] = ..., imageFileName: bool = ..., layer: Optional[Union[str, bool]] = ..., limitedRenderSupport: bool = ..., lowQualityLighting: bool = ..., noRenderView: bool = ..., notWriteToFile: bool = ..., printGeometry: bool = ..., renderHardwareName: bool = ..., renderRegion: Optional[Union[Tuple[int, int, int, int], bool]] = ..., renderSelected: bool = ..., textureResolution: Optional[Union[int, bool]] = ..., width: Optional[Union[int, bool]] = ..., writeAlpha: bool = ..., writeDepth: bool = ..., query: bool = ...) -> Any:
    r"""
    Renders an image or a sequence using the hardware rendering engine

    Args:
        acceleratedMultiSampleSupport: (query) - This flag when used with query will return whether the graphics supports     hardware accelerated multi-sampling.
        activeTextureCount: (query) - This flag when used with query will return the number of textures that     have been bound to the graphics by the hardware renderer.
        camera: (create, query) - Specify the camera to use.  Use the first available camera if the camera         given is not found.
        currentFrame: (create, query) - Render the current frame.
        currentView: (create, query) - When turned on, only the current view will be rendered.
        edgeAntiAliasing: (create, query) - Enables multipass rendering. Controls for the number of exposures rendered per frame are provided in the form of two associated flag arguments. The first specifies the sampling algorithm:  0 - Uniform Weighted Grid Sampling 1 - Rotated Grid Super Sampling (RGSS) 2 - Gaussian Weighted Sampling   Use of a sampling method other than the others listed above, will result in use of the default sample method of Uniform Weighted Grid Sampling. The second argument specifies a number of samples to use. For each sampling algorithm there is a fixed set of sample counts available:  0 - Uniform Weighted Grid Sampling 1 Sample 3 Samples 4 Samples 5 Samples 7 Samples 9 Samples 16 Samples 25 Samples 36 Samples 1 - Rotated Grid Super Sampling (RGSS) 1 Sample 4 Samples 5 Samples 2 - Gaussian Weighted Sampling 1 Sample 3 Samples 4 Samples 5 Samples 7 Samples 9 Samples 16 Samples 25 Samples 36 Samples   Using a sampling count other than the allowable options for the given sampling method will result in using the default sample count of 5. The values passed via the command will override settings stored in the hardwareRenderGlobals node.
        fixFileNameNumberPattern: (create, query) - This flag allows the user to take the hardwareRenderGlobals     filename as the initial filename pattern,     fix the frame number pattern in the filename in a unique way,     returns the new filename pattern.  This does not change the     hardwareRenderGlobals's filename.
        frame: (create) - Specify the frame to render.
        fullRenderSupport: (create, query) - This flag may be used in the create or query context.     In the create context, it will force the renderer to abort and not     render any frames if the hardware is not fully supported.         In the query context, it will return whether full quality rendering     is supported on the current graphics system. Please see the graphics     card qualification charts for an explanation of limited support.
        height: (create, query) - Height. If not used, the height is taken from the render globals settings.
        imageFileName: (create, query) - This flag let people query the image name for a specified frame.     The frame can be specified using the "-frame" flag.     When no "-frame" is used, the     current frame number is used.
        layer: (create, query) - Render the specified render layer.         Only this render layer will be rendered,         regardless of the renderable attribute value of the render layer.         The layer name will be appended to the output image file name.         The specified render layer becomes the current render layer before rendering,         and remains as current render layer after the rendering.
        limitedRenderSupport: (query) - This flag when used with query will return whether limited rendering is supported         on the current graphics system. Please see the graphics card qualification         charts for the current definition of limited support.
        lowQualityLighting: (create, query) - Disable lighting evaluation per pixel (fragment).         Note: The values passed via the command will override settings stored in     the hardware render globals node.
        noRenderView: (create, query) - When turned on, the render view is not updated after image computation
        notWriteToFile: (create, query) - This flag is set to true if the user does not want to write     the image to a file.  It is set to false, otherwise.     The default value of the flag is "false".
        printGeometry: (create, query) - Print the geomety objects as they get translated.
        renderHardwareName: (query) - This flag will create a graphics context and return the name of the     graphics hardware being used. The graphics hardware is determined by     creating an off screen buffer and querying the GL_RENDERER string     from OpenGL. If the off screen buffer cannot be created an empty     string is returned.
        renderRegion: (create, query) - Render region. The parameters are 4 integers, indicating             left right bottom top     of the region.
        renderSelected: (create, query) - Only renders the selected objects.
        textureResolution: (create, query) - Specify the desired resolution of baked textures.
        width: (create, query) - Width. If not used, the width is taken from the render globals settings.
        writeAlpha: (create, query) - Read the alpha channel of color buffer and return as tif file.
        writeDepth: (create, query) - Read the depth buffer and return as tif file.
    """
    ...


def hwRenderLoad(*args) -> Any:
    r"""
    Empty command used to force the dynamic load of HR render

    Args:
    """
    ...


def imagePlane(*args, camera: Optional[Union[str, bool]] = ..., counter: bool = ..., detach: bool = ..., dropFrame: bool = ..., fileName: Optional[Union[str, bool]] = ..., frameDuration: Optional[Union[int, bool]] = ..., height: Optional[Union[float, bool]] = ..., imageSize: Optional[Union[Tuple[int, int], bool]] = ..., lookThrough: Optional[Union[str, bool]] = ..., maintainRatio: bool = ..., name: Optional[Union[str, bool]] = ..., negTimesOK: bool = ..., numFrames: Optional[Union[int, bool]] = ..., quickTime: bool = ..., showInAllViews: bool = ..., timeCode: Optional[Union[int, bool]] = ..., timeCodeTrack: bool = ..., timeScale: Optional[Union[int, bool]] = ..., twentyFourHourMax: bool = ..., width: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The imagePlane command allows querying of various properties of
            an image plane and any movie in use by the image plane. It also supports
            creating and edit.
            The object passed to the command may either be an imagePlane node,
            or a camera, in which case the command uses the image plane attached
            to the camera (if any). If no object is passed in, the current
            selection is used.
            Currently, most movie related queries work only on 64 bit Windows systems.

    Args:
        camera: (create, edit, query) - When creating, it will try to attach the created image plane to the specified camera. If the given camera is invalid, creating will fail. When querying, it will query which camera current image plane is attaching to. If it has no camera attached to (free image plane), it will return an empty string. When edit, it will make the image plane attach to the new specified camera. If the camera given is invalid, it will do nothing. When the image plane is attached to a camera, the image plane's transform node will be set identity. The detach command will not restore the original position of the image plane. but the undo command will restore the original position of the image plane.
        counter: () - Query the 'counter' flag of the movie's timecode format. If this is true, the timecode returned by the -timeCode flag will be a simple counter. If false, the returned timecode will be an array of integers (hours, minutes, seconds, frames).
        detach: (edit) - This flag can only be used in the edit mode, when this flag is used in edit, it will detach current image plane from any camera it attaches to and make it a free image plane.
        dropFrame: (query) - Query the 'drop frame' flag of the movie's timecode format.
        fileName: (create, edit) - Set the image name for image plane to read.
        frameDuration: (query) - Query the frame duration of the movie's timecode format.
        height: (create, edit, query) - Height of the image plane. When creating, if this flag is not specified, it will use 10.0 as default height.
        imageSize: (query) - Get size of the loaded image.
        lookThrough: (create, edit, query) - The camera currently used for image plane to look through.
        maintainRatio: (create, edit, query) - Let the image plane respect the picture aspect ratio. When creating, if this flag is not specified, it will use true as default value.
        name: (create, query) - Set the image plane node name when creating or return the image plane name when querying.
        negTimesOK: (query) - Query the 'neg times OK' flag of the movie's timecode format.
        numFrames: (query) - Query the whole number of frames per second of the movie's timecode format.
        quickTime: (query) - Query whether the image plane is using a QuickTime movie.
        showInAllViews: (create, edit, query) - The flag is used to show the current image plane in all views or not.
        timeCode: (query) - Query the whole number of frames per second of the movie's timecode format.
        timeCodeTrack: (query) - Query whether the movie on the image plane has a timecode track.
        timeScale: (query) - Query the timescale of the movie's timecode format.
        twentyFourHourMax: (query) - Query the '24 hour max' flag of the movie's timecode format.
        width: (create, edit, query) - Width of the image plane. When creating, if this flag is not specified, it will use 10.0 as default width.
    """
    ...


def iprEngine(*args, copy: str = ..., defineTemplate: Optional[Union[str, bool]] = ..., diagnostics: bool = ..., estimatedMemory: bool = ..., exists: bool = ..., iprImage: Optional[Union[str, bool]] = ..., motionVectorFile: bool = ..., object: Optional[Union[str, bool]] = ..., region: Optional[Union[Tuple[int, int, int, int], bool]] = ..., relatedFiles: bool = ..., releaseIprImage: bool = ..., resolution: bool = ..., scanlineIncrement: Optional[Union[str, bool]] = ..., showProgressBar: bool = ..., startTuning: bool = ..., stopTuning: bool = ..., underPixel: Tuple[int, int] = ..., update: bool = ..., updateDepthOfField: bool = ..., updateLightGlow: bool = ..., updateMotionBlur: bool = ..., updatePort: Optional[Union[str, bool]] = ..., updateShaderGlow: bool = ..., updateShading: bool = ..., updateShadowMaps: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to create or edit an iprEngine.  A iprEngine
    is an object that watches for changes to shading
    networks and automatically reshades to generate an
    up-to-date image.

    Args:
        copy: (edit) - Copies the deep raster file, as well as its related files, to the new location.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        diagnostics: (edit) - The diagnostics should be shown
        estimatedMemory: (query) - Displays the estimated memory being used by IPR.
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        iprImage: (create, edit, query) - Specify the ipr image to use.
        motionVectorFile: (query) - Returns the name of the motion vector file used by IPR.
        object: (create, edit, query) - The objects to be tuned.
        region: (create, edit, query) - The coordinates of the region to be tuned. The integers are in the sequence left bottom right top or x1,y2  x2,y2
        relatedFiles: (query) - Returns the names for the related files, e.g, the non-glow-non-blur image, the motion vector file, and the depth-map files.
        releaseIprImage: (edit) - The ipr image should be released and memory should    be freed.
        resolution: (query) - The width and height of the ipr file.
        scanlineIncrement: (create, edit, query) - Set the scanline increment percentage.  If the height of the region being update is 240 pixels, and the scanlineIncrement is 10% then the image will refresh blocks of 24 scanlines.
        showProgressBar: (create, edit, query) - Show progress bar during tuning.
        startTuning: (create, edit, query) - An ipr image has been specified and now changes to shading    networks should force an image to be produced.
        stopTuning: (create, edit, query) - Tuning should cease but ipr image should not be closed.
        underPixel: (edit) - Get list of objects under the pixel sprcified.
        update: (create, edit) - Force an update.
        updateDepthOfField: (create, edit) - Force a refresh of depth-of-field.
        updateLightGlow: (create, edit, query) - Automatically update when light glow changes.
        updateMotionBlur: (create, edit, query) - Automatically update when 2.5D motion blur changes.
        updatePort: (create, edit, query) - The name of the port that is to be updated when pixel values are recomputed.  (not currently supported)
        updateShaderGlow: (create, edit, query) - Automatically update when shader glow changes.
        updateShading: (create, edit, query) - Automatically update shading.
        updateShadowMaps: (create, edit) - Force the shadow maps to be generated and an update to occur.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
    """
    ...


def layeredShaderPort(*args, annotation: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., fullPathName: bool = ..., height: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., isObscured: bool = ..., manage: bool = ..., noBackground: bool = ..., node: Optional[Union[str, bool]] = ..., numberOfPopupMenus: bool = ..., parent: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., selectedColorControl: Optional[Union[str, bool]] = ..., selectedTransparencyControl: Optional[Union[str, bool]] = ..., statusBarMessage: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., visible: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a 3dPort that displays an image representing
    the layered shader node specified.

    Args:
        annotation: (create, edit, query) - Annotate the control with an extra string value.
        backgroundColor: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag: (create, edit, query) - Add a documentation flag to the control.  The documentation flag has a directory structure. (e.g., -dt render/multiLister/createNode/material)
        dragCallback: (create, edit) - Adds a callback that is called when the middle mouse button is pressed.  The MEL version of the callback is of the form:  global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  The proc returns a string array that is transferred to the drop site. By convention the first string in the array describes the user settable message type.  Controls that are application defined drag sources may ignore the callback. $mods allows testing for the key modifiers CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3 == CTRL + SHIFT.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def callbackName( dragControl, x, y, modifiers ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "x", "y", "modifiers".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")
        dropCallback: (create, edit) - Adds a callback that is called when a drag and drop operation is released above the drop site.  The MEL version of the callback is of the form:  global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  The proc receives a string array that is transferred from the drag source. The first string in the msgs array describes the user defined message type. Controls that are application defined drop sites may ignore the callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "dropControl", "messages", "x", "y", "type".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")
        enable: (create, edit, query) - The enable state of the control.  By default, this flag is set to true and the control is enabled.  Specify false and the control will appear dimmed or greyed-out indicating it is disabled.
        enableBackground: (create, edit, query) - Enables the background color of the control.
        enableKeyboardFocus: (create, edit, query) - If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse. This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls. If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        fullPathName: (query) - Return the full path name of the widget, which includes all the parents.
        height: (create, edit, query) - The height of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
        highlightColor: (create, edit, query) - The highlight color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.
        isObscured: (query) - Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.
        manage: (create, edit, query) - Manage state of the control.  An unmanaged control is not visible, nor does it take up any screen real estate.  All controls are created managed by default.
        noBackground: (create, edit) - Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
        node: (create) - Specifies the name of the newLayeredShader node this port will represent.
        numberOfPopupMenus: (query) - Return the number of popup menus attached to this control.
        parent: (create, query) - The parent layout for this control.
        popupMenuArray: (query) - Return the names of all the popup menus attached to this control.
        preventOverride: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        selectedColorControl: (create) - Specifies the name of the UI-control that represents the currently selected layer's color.
        selectedTransparencyControl: (create) - Specifies the name of the UI-control that represents the currently selected layer's transparency.
        statusBarMessage: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
        visible: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def layeredTexturePort(*args, annotation: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., fullPathName: bool = ..., height: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., isObscured: bool = ..., manage: bool = ..., noBackground: bool = ..., node: Optional[Union[str, bool]] = ..., numberOfPopupMenus: bool = ..., parent: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., selectedAlphaControl: Optional[Union[str, bool]] = ..., selectedBlendModeControl: Optional[Union[str, bool]] = ..., selectedColorControl: Optional[Union[str, bool]] = ..., selectedIsVisibleControl: Optional[Union[str, bool]] = ..., statusBarMessage: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., visible: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a 3dPort that displays an image representing
    the layered texture node specified.

    Args:
        annotation: (create, edit, query) - Annotate the control with an extra string value.
        backgroundColor: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag: (create, edit, query) - Add a documentation flag to the control.  The documentation flag has a directory structure. (e.g., -dt render/multiLister/createNode/material)
        dragCallback: (create, edit) - Adds a callback that is called when the middle mouse button is pressed.  The MEL version of the callback is of the form:  global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  The proc returns a string array that is transferred to the drop site. By convention the first string in the array describes the user settable message type.  Controls that are application defined drag sources may ignore the callback. $mods allows testing for the key modifiers CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3 == CTRL + SHIFT.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def callbackName( dragControl, x, y, modifiers ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "x", "y", "modifiers".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")
        dropCallback: (create, edit) - Adds a callback that is called when a drag and drop operation is released above the drop site.  The MEL version of the callback is of the form:  global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  The proc receives a string array that is transferred from the drag source. The first string in the msgs array describes the user defined message type. Controls that are application defined drop sites may ignore the callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "dropControl", "messages", "x", "y", "type".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")
        enable: (create, edit, query) - The enable state of the control.  By default, this flag is set to true and the control is enabled.  Specify false and the control will appear dimmed or greyed-out indicating it is disabled.
        enableBackground: (create, edit, query) - Enables the background color of the control.
        enableKeyboardFocus: (create, edit, query) - If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse. This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls. If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        fullPathName: (query) - Return the full path name of the widget, which includes all the parents.
        height: (create, edit, query) - The height of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
        highlightColor: (create, edit, query) - The highlight color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.
        isObscured: (query) - Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.
        manage: (create, edit, query) - Manage state of the control.  An unmanaged control is not visible, nor does it take up any screen real estate.  All controls are created managed by default.
        noBackground: (create, edit) - Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
        node: (create) - Specifies the name of the newLayeredTexture node this port will represent.
        numberOfPopupMenus: (query) - Return the number of popup menus attached to this control.
        parent: (create, query) - The parent layout for this control.
        popupMenuArray: (query) - Return the names of all the popup menus attached to this control.
        preventOverride: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        selectedAlphaControl: (create) - Specifies the name of the UI-control that represents the currently selected layer's alpha.
        selectedBlendModeControl: (create) - Specifies the name of the UI-control that represents the currently selected layer's blend mode.
        selectedColorControl: (create) - Specifies the name of the UI-control that represents the currently selected layer's color.
        selectedIsVisibleControl: (create) - Specifies the name of the UI-control that represents the currently selected layer's visibility.
        statusBarMessage: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
        visible: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def lightlink(*args, b: bool = ..., hierarchy: bool = ..., light: Optional[Union[str, bool]] = ..., make: bool = ..., object: Optional[Union[str, bool]] = ..., sets: bool = ..., shadow: bool = ..., shapes: bool = ..., transforms: bool = ..., useActiveLights: bool = ..., useActiveObjects: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to make, break and query light linking
    relationships between lights/sets of lights and objects/sets of
    objects.
    
    If no make, break or query flag is specified and both lights and
    objects flags are present, the make flag is assumed to be specified.
    
    If no make, break or query flag is specified and only one of the
    lights and objects flags is present, the query flag is assumed to be
    specified.
    
    You can specify as many lights and objects as you like, using the
    multiuse -light and -object flags.
    
    A better way to perform light linking is to make sets of lights and
    sets of geometry. If you create a set which contains lights (such as
    the ceiling lights in your scene) and a set which contains geometry
    (such as the geometry of your character), you can then link the
    set containing lights with the set containing geometry
    in order to get those lights to illuminate those pieces of geometry.
    In addition, you can add and remove lights and geometry from their
    respective sets without having to make and break light links.

    Args:
        b: (create) - The presence of this flag on the command indicates that the command is being invoked to break links between lights and renderable objects.
        hierarchy: (create) - When querying, specifies whether the result should include the hierarchy of transforms above shapes linked to the queried light/object. The transforms considered part of the hierarchy do not include the transform immediately above the shape. Default is true.
        light: (create, multiuse) - The argument to the light flag specifies a node to be used by the command in performing the action as if the node is a light. This is a multiuse flag -- many light nodes can be specified in a single invocation of the lightlink command.
        make: (create) - The presence of this flag on the command indicates that the command is being invoked to make links between lights and renderable objects.
        object: (create, multiuse) - The argument to the object flag specifies a node to be used by the command in performing the action as if the node is an object. This is a multiuse flag -- many object nodes can be specified in a single invocation of the lightlink command.
        sets: (create) - When querying, specifies whether the result should include sets linked to the queried light/object. Default is true.
        shadow: (create) - Specify that shadows are to be linked.
        shapes: (create) - When querying, specifies whether the result should include shapes linked to the queried light/object. Default is true.
        transforms: (create) - When querying, specifies whether the result should include transforms immediately above shapes linked to the queried light/object. Default is true.
        useActiveLights: (create) - Specify that active lights are to be used.
        useActiveObjects: (create) - Specify that active objects are to be used.
    """
    ...


def lightList(*args, add: Optional[Union[str, bool]] = ..., remove: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Add/Remove a relationship between an object and the
    current light.
    Soon to be replaced by the connect-attribute command.

    Args:
        add: (create) - add object(s) to light list.
        remove: (create) - remove object(s) to light list.
    """
    ...


def listCameras(*args, orthographic: bool = ..., perspective: bool = ...) -> Any:
    r"""
    Command to list all cameras. If no flags are given, both
    perspective and orthographic cameras will be displayed. This
    command returns an array of camera names. When the transform name
    uniquely identifies the camera it is used, otherwise the shape
    name will be returned.

    Args:
        orthographic: (create) - Display all orthographic cameras.
        perspective: (create) - Display all perspective cameras.
    """
    ...


def lookThru(*args, farClip: Optional[Union[float, bool]] = ..., nearClip: Optional[Union[float, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command sets a particular camera to look through in a view. This
    command may also be used to view the negative z axis of lights or
    other DAG objects. The standard camera tools can then be used to place
    the object.
    
    Note: if there are multiple objects under the transform selected,
    cameras and lights take precedence.

    Args:
        farClip: (create) - Used when setting clip far plane for a new look thru camera. Will not affect the attributes of an existing camera. Clip values must come before shape or view.
        nearClip: (create) - Used when setting near clip plane for a new look thru camera. Will not affect the attributes of an existing camera. Clip values must come before shape or view.
    """
    ...


def lsThroughFilter(*args, item: Optional[Union[str, bool]] = ..., nodeArray: bool = ..., reverse: bool = ..., selection: bool = ..., sort: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    List all objects in the world that pass a given filter.

    Args:
        item: (create, multiuse) - Run the filter on specified node(s), using the fast version of this command.
        nodeArray: (create) - Fast version that runs an entire array of nodes through the filter at one time.
        reverse: (create) - Only available in conjunction with nodeArray flag. Reverses the order of nodes in the returned arrays if true.
        selection: (create) - Run the filter on selected nodes only, using the fast version of this command.
        sort: (create) - Only available in conjunction with nodeArray flag. Orders the nodes in the returned array. Current options are: "byName", "byType", and "byTime".
    """
    ...


def makebot(*args, checkdepends: bool = ..., checkres: Optional[Union[int, bool]] = ..., input: Optional[Union[str, bool]] = ..., nooverwrite: bool = ..., output: Optional[Union[str, bool]] = ..., verbose: bool = ...) -> Any:
    r"""
    The makebot command takes an image file and produces a block
    ordered texture (BOT) file, to be used for texture caching.
    If a relative pathname is specified for the input image file,
    project management rules apply.  If a relative pathname is
    specified for the output BOT file, project management rules
    apply and gets put into the sourceImages directory.

    Args:
        checkdepends: (create) - the BOT file should only be generated if it doesn't already exists, or if it is older than the source file
        checkres: (create) - the BOT file should only be generated if its resolution (maximum of width and height) is larger than the minimum value specified by the argument
        input: (create) - input image file
        nooverwrite: (create) - If -c and/or -r indicate that the BOT file should be generated but if already exists, then this flag will prevent the file from being overwritten
        output: (create) - output BOT file
        verbose: (create) - Makebot will provide feedback if this flag is specified
    """
    ...


def mayaHasRenderSetup(*args, enableCurrentSession: bool = ..., enableDuringTests: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command controls and queries render setup states.

    Args:
        enableCurrentSession: (edit, query) - Enables or disables render setup for this Maya session only. This flag should only be called during Maya intialization. This flag is for internal use only, may change at any time and is unsupported.
        enableDuringTests: (edit, query) - Switches render setup for this Maya session only, as legacy render layer mode is assumed during testing. This flag is for internal use only, may change at any time and is unsupported.
    """
    ...


def nodeIconButton(*args, align: Optional[Union[str, bool]] = ..., annotation: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., command: Optional[Union[str, bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., disabledImage: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., flipX: bool = ..., flipY: bool = ..., font: Optional[Union[str, bool]] = ..., fullPathName: bool = ..., height: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., image: Optional[Union[str, bool]] = ..., image1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., imageOverlayLabel: Optional[Union[str, bool]] = ..., isObscured: bool = ..., label: Optional[Union[str, bool]] = ..., labelOffset: Optional[Union[int, bool]] = ..., manage: bool = ..., marginHeight: Optional[Union[int, bool]] = ..., marginWidth: Optional[Union[int, bool]] = ..., noBackground: bool = ..., numberOfPopupMenus: bool = ..., overlayLabelBackColor: Optional[Union[Tuple[float, float, float, float], bool]] = ..., overlayLabelColor: Optional[Union[Tuple[float, float, float], bool]] = ..., parent: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., rotation: Optional[Union[float, bool]] = ..., statusBarMessage: Optional[Union[str, bool]] = ..., style: Optional[Union[str, bool]] = ..., useAlpha: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., version: Optional[Union[str, bool]] = ..., visible: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This control supports up to 3 icon images and 4 different display
    styles.  The icon image displayed is the one that best fits the
    current size of the control given its current style.
    
    This command creates a button that can be displayed with different
    icons, with or without a text label. If the button is drag and dropped
    onto other controls (e.g., HyperShade), the command will be executed and
    the return string will be used as the name of a dropped node.

    Args:
        align: (create, edit, query) - The label alignment.  Alignment values are "left", "right", and "center". By default, the label is aligned "center". Currently only available when -st/style is set to "iconAndTextCentered".
        annotation: (create, edit, query) - Annotate the control with an extra string value.
        backgroundColor: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        command: (create, edit, query) - Command executed when the control is pressed. The command should return a string which will be used to facilitate node drag and drop.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        disabledImage: (create, edit, query) - Image used when the button is disabled. Image size must be the same as the image specified with the i/image flag. This is a Windows only flag.
        docTag: (create, edit, query) - Add a documentation flag to the control.  The documentation flag has a directory structure. (e.g., -dt render/multiLister/createNode/material)
        dragCallback: (create, edit) - Adds a callback that is called when the middle mouse button is pressed.  The MEL version of the callback is of the form:  global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  The proc returns a string array that is transferred to the drop site. By convention the first string in the array describes the user settable message type.  Controls that are application defined drag sources may ignore the callback. $mods allows testing for the key modifiers CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3 == CTRL + SHIFT.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def callbackName( dragControl, x, y, modifiers ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "x", "y", "modifiers".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")
        dropCallback: (create, edit) - Adds a callback that is called when a drag and drop operation is released above the drop site.  The MEL version of the callback is of the form:  global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  The proc receives a string array that is transferred from the drag source. The first string in the msgs array describes the user defined message type. Controls that are application defined drop sites may ignore the callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "dropControl", "messages", "x", "y", "type".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")
        enable: (create, edit, query) - The enable state of the control.  By default, this flag is set to true and the control is enabled.  Specify false and the control will appear dimmed or greyed-out indicating it is disabled.
        enableBackground: (create, edit, query) - Enables the background color of the control.
        enableKeyboardFocus: (create, edit, query) - If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse. This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls. If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        flipX: (create, edit, query) - Is the image flipped horizontally?
        flipY: (create, edit, query) - Is the image flipped vertically?
        font: (create, edit, query) - The font for the text.  Valid values are "boldLabelFont", "smallBoldLabelFont", "tinyBoldLabelFont", "plainLabelFont", "smallPlainLabelFont", "obliqueLabelFont", "smallObliqueLabelFont", "fixedWidthFont" and "smallFixedWidthFont".
        fullPathName: (query) - Return the full path name of the widget, which includes all the parents.
        height: (create, edit, query) - The height of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
        highlightColor: (create, edit, query) - The highlight color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.
        image: (create, edit, query) - If you are not providing images with different sizes then you may use this flag for the control's image. If the "iconOnly" style is set, the icon will be scaled to the size of the control.
        image1: (create, edit, query) - First of three possible icons. The icon that best fits the current size of the control will be displayed.
        image2: (create, edit, query) - Second of three possible icons. The icon that best fits the current size of the control will be displayed.
        image3: (create, edit, query) - Third of three possible icons. The icon that best fits the current size of the control will be displayed.
        imageOverlayLabel: (create, edit, query) - A short string, up to 6 characters, representing a label that will be displayed on top of the image.
        isObscured: (query) - Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.
        label: (create, edit, query) - The text that appears in the control.
        labelOffset: (create, edit, query) - The label offset. Default is 0. Currently only available when -st/style is set to "iconAndTextCentered".
        manage: (create, edit, query) - Manage state of the control.  An unmanaged control is not visible, nor does it take up any screen real estate.  All controls are created managed by default.
        marginHeight: (create, edit, query) - The number of pixels above and below the control content. The default value is 1 pixel.
        marginWidth: (create, edit, query) - The number of pixels on either side of the control content. The default value is 1 pixel.
        noBackground: (create, edit) - Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
        numberOfPopupMenus: (query) - Return the number of popup menus attached to this control.
        overlayLabelBackColor: (create, edit, query) - The RGBA color of the shadow behind the label defined by imageOverlayLabel. Default is 50% transparent black: 0 0 0 .5
        overlayLabelColor: (create, edit, query) - The RGB color of the label defined by imageOverlayLabel. Default is a light grey: .8 .8 .8
        parent: (create, query) - The parent layout for this control.
        popupMenuArray: (query) - Return the names of all the popup menus attached to this control.
        preventOverride: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        rotation: (create, edit, query) - The rotation value of the image in radians.
        statusBarMessage: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        style: (create, edit, query) - The draw style of the control.  Valid styles are "iconOnly", "textOnly", "iconAndTextHorizontal", "iconAndTextVertical", and "iconAndTextCentered". (Note: "iconAndTextCentered" is only available on Windows). If the "iconOnly" style is set, the icon will be scaled to the size of the control.
        useAlpha: (create, edit, query) - Is the image using alpha channel?
        useTemplate: (create) - Forces the command to use a command template other than the current one.
        version: (create, edit, query) - Specify the version that this control feature was introduced. The argument should be given as a string of the version number (e.g. "2013", "2014"). Currently only accepts major version numbers (e.g. 2013 Ext 1, or 2013.5 should be given as "2014").
        visible: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def nodePreset(*args, attributes: Optional[Union[str, bool]] = ..., custom: Optional[Union[str, bool]] = ..., delete: Optional[Union[Tuple[str, str], bool]] = ..., exists: Optional[Union[Tuple[str, str], bool]] = ..., isValidName: Optional[Union[str, bool]] = ..., list: Optional[Union[str, bool]] = ..., load: Optional[Union[Tuple[str, str], bool]] = ..., save: Optional[Union[Tuple[str, str], bool]] = ...) -> Any:
    r"""
    Command to save and load preset settings for a node.
    This command allows you to take a snapshot of the values of all attributes of a
    node and save it to disk as a preset with user specified name. Later the saved
    preset can be loaded and applied onto a different node of the same type. The
    end result is that the node to which the preset is applied takes on the same
    values as the node from which the preset was generated had at the time of the
    snapshot.

    Args:
        attributes: (create) - A white space separated string of the named attributes to save to the preset file. If not specified, all attributes will be stored.
        custom: (create) - Specifies a MEL script for custom handling of node attributes that are not handled by the general save preset mechanism (ie. multis, dynamic attributes, or connections). The identifiers #presetName and #nodeName will be expanded before the script is run. The script must return an array of strings which will be saved to the preset file and issued as commands when the preset is applied to another node. The custom script can query #nodeName in determining what should be saved to the preset, or issue commands to query the selected node in deciding how the preset should be applied.
        delete: (create) - Deletes the existing preset for the node specified by the first argument with the name specified by the second argument.
        exists: (create) - Returns true if the node specified by the first argument already has a preset with a name specified by the second argument. This flag can be used to check if the user is about to overwrite an existing preset and thereby provide the user with an opportunity to choose a different name.
        isValidName: (create) - Returns true if the name consists entirely of valid characters for a preset name. Returns false if not. Because the preset name will become part of a file name and part of a MEL procedure name, some characters must be disallowed. Only alphanumeric characters and underscore are valid characters for the preset name.
        list: (create) - Lists the names of all presets which can be loaded onto the specified node.
        load: (create) - Sets the settings of the node specified by the first argument according to the preset specified by the second argument. Any attributes on the node which are the destinations of connections or whose children (multi children or compound children) are destinations of connections will not be changed by the preset.
        save: (create) - Saves the current settings of the node specified by the first argument to a preset of the name specified by the second argument. If a preset for that node with that name already exists, it will be overwritten with no warning. You can use the -exists flag to check if the preset already exists. If an attribute of the node is the destination of a connection, the value of the attribute will not be written as part of the preset.
    """
    ...


def ogsRender(*args, activeMultisampleType: Optional[Union[str, bool]] = ..., activeRenderOverride: Optional[Union[str, bool]] = ..., activeRenderTargetFormat: Optional[Union[str, bool]] = ..., availableFloatingPointTargetFormat: bool = ..., availableMultisampleType: bool = ..., availableRenderOverrides: bool = ..., camera: Optional[Union[str, bool]] = ..., currentFrame: bool = ..., currentView: bool = ..., enableFloatingPointRenderTarget: bool = ..., enableMultisample: bool = ..., frame: Optional[Union[float, bool]] = ..., height: Optional[Union[int, bool]] = ..., layer: Optional[Union[str, bool]] = ..., noRenderView: bool = ..., width: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Renders an image or a sequence using the OGS rendering engine

    Args:
        activeMultisampleType: (edit, query) - Query the current active multisample type.
        activeRenderOverride: (edit, query) - Set or query the current active render override.
        activeRenderTargetFormat: (edit, query) - Query the current active floating point target format.
        availableFloatingPointTargetFormat: (query) - Returns the names of available floating point render target format.
        availableMultisampleType: (query) - Returns the names of available multisample type.
        availableRenderOverrides: (query) - Returns the names of available render overrides.
        camera: (create, edit, query) - Specify the camera to use.  Use the first available camera if the camera given is not found.
        currentFrame: (create, edit, query) - Render the current frame.
        currentView: (create, edit, query) - When turned on, only the current view will be rendered.
        enableFloatingPointRenderTarget: (edit, query) - Enable/disable floating point render target.
        enableMultisample: (edit, query) - Enable/disable multisample.
        frame: (create, edit) - Specify the frame to render.
        height: (create, edit, query) - The height flag pass the height to the ogsRender command. If not used, the height is taken from the render globals settings.
        layer: (create, edit, query) - Render the specified legacy render layer. Only this render layer will be rendered, regardless of the renderable attribute value of the render layer. The layer name will be appended to the output image file name. The specified render layer becomes the current render layer before rendering, and remains as current render layer after the rendering. This argument uses legacy render layers as this command does not recognize the newer renderSetup render layer system introduced in Maya 2016.
        noRenderView: (create, edit, query) - When turned on, the render view is not updated after image computation
        width: (create, edit, query) - The width flag pass the width to the ogsRender command. If not used, the width is taken from the render globals settings.
    """
    ...


def orbit(*args, horizontalAngle: Optional[Union[float, bool]] = ..., pivotPoint: Optional[Union[Tuple[float, float, float], bool]] = ..., rotationAngles: Optional[Union[Tuple[float, float], bool]] = ..., verticalAngle: Optional[Union[float, bool]] = ...) -> Any:
    r"""
    The orbit command revolves the camera(s) horizontally and/or
    vertically in the perspective window. The rotation axis is with
    respect to the camera. 
    
    To revolve horizontally: the rotation axis is the camera up
    direction vector. To revolve vertically: the rotation axis is the
    camera left direction vector. 
    
    When both the horizontal and the vertical angles are supplied on
    the command line, the camera is firstly revolved horizontally,
    then revolved vertically. 
    
    This command may be applied to more than one camera; objects that
    are not cameras are ignored. When no camera name supplied, this command
    is applied to all currently active cameras.

    Args:
        horizontalAngle: (create) - Angle to revolve horizontally.
        pivotPoint: (create) - Used as the pivot point in the world space.
        rotationAngles: (create) - Angle to revolve horizontally and vertically.
        verticalAngle: (create) - Angle to revolve vertically.
    """
    ...


def panZoom(*args, absolute: bool = ..., downDistance: Optional[Union[float, bool]] = ..., leftDistance: Optional[Union[float, bool]] = ..., relative: bool = ..., rightDistance: Optional[Union[float, bool]] = ..., upDistance: Optional[Union[float, bool]] = ..., zoomRatio: Optional[Union[float, bool]] = ...) -> Any:
    r"""
    The panZoom command pans/zooms the 2D film.
    
    The panZoom command can be applied to either a perspective or an
    orthographic camera.
    
    When no camera name is supplied, this command is applied to the
    camera in the active view.

    Args:
        absolute: (create) - This flag modifies the behavior of the distance and zoomRatio flags. If specified, the distance and zoomRatio value will be applied directly.
        downDistance: (create) - Set the amount of down pan distance in inches
        leftDistance: (create) - Set the amount of left pan distance in inches
        relative: (create) - This flag modifies the behavior of the distance and zoomRatio flags. If specified, the distance or zoomRatio value is used multiply the camera's existing value. By default the relative flag is always on.
        rightDistance: (create) - Set the amount of right pan distance in inches
        upDistance: (create) - Set the amount of up pan distance in inches
        zoomRatio: (create) - Set the amount of zoom ratio
    """
    ...


def perCameraVisibility(*args, camera: Optional[Union[str, bool]] = ..., exclusive: bool = ..., hide: bool = ..., remove: bool = ..., removeAll: bool = ..., removeCamera: bool = ..., query: bool = ...) -> Any:
    r"""
    The perCameraVisibility command creates, queries and removes
    visibility relationships between DAG objects and cameras.
    These relationships are applied in any viewport that uses the cameras
    involved. (They are not used e.g. in rendering.)
    Objects can be set to be exclusive to a camera (meaning they will only
    be displayed in viewports using that camera; they will be hidden in other
    viewports) or hidden from a camera (meaning they will be not visible
    in any viewport using the camera).

    Args:
        camera: (create, query) - Specify the camera for the operation.
        exclusive: (create, query) - Set objects as being exclusive to the given camera.
        hide: (create, query) - Set objects as being hidden from the given camera.
        remove: (create) - Used with exclusive or hide, removes the objects instead of adding them.
        removeAll: (create) - Remove all exclusivity/hidden objects for all cameras.
        removeCamera: (create) - Remove all exclusivity/hidden objects for the given camera.
    """
    ...


def pointLight(*args, decayRate: Optional[Union[int, bool]] = ..., discRadius: Optional[Union[float, bool]] = ..., exclusive: bool = ..., intensity: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., position: Optional[Union[Tuple[float, float, float], bool]] = ..., rgb: Optional[Union[Tuple[float, float, float], bool]] = ..., rotation: Optional[Union[Tuple[float, float, float], bool]] = ..., shadowColor: Optional[Union[Tuple[float, float, float], bool]] = ..., shadowDither: Optional[Union[float, bool]] = ..., shadowSamples: Optional[Union[int, bool]] = ..., softShadow: bool = ..., useRayTraceShadows: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The pointLight command is used to edit the parameters of
    existing pointLights, or to create new ones. The default
    behaviour is to create a new pointlight.

    Args:
        decayRate: (create, edit, query) - decay rate of the light (0-no decay, 1-slow, 2-realistic, 3-fast)
        discRadius: (create, edit, query) - radius of the disc around the light
        exclusive: (create, edit, query) - This flag is obsolete.
        intensity: (create, edit, query) - intensity of the light (expressed as a percentage)
        name: (create, edit, query) - specify the name of the light
        position: (create, edit, query) - This flag is obsolete.
        rgb: (create, edit, query) - color of the light (0-1)
        rotation: (create, edit, query) - This flag is obsolete.
        shadowColor: (create, edit, query) - the shadow color
        shadowDither: (create, edit, query) - dither the shadow
        shadowSamples: (create, edit, query) - number of shadow samples.
        softShadow: (create, edit, query) - soft shadow
        useRayTraceShadows: (create, edit, query) - ray trace shadows
    """
    ...


def preferredRenderer(*args, fallback: Optional[Union[str, bool]] = ..., makeCurrent: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to set the preferred renderer. This command can be used
    to query the preferred renderer and to set the current renderer
    as the preferred one. It also allows users to specify a
    preferred fallback renderer.

    Args:
        fallback: (create, query) - Sets the preferred fallback renderer.
        makeCurrent: (create) - Sets the current renderer as the preferred one.
    """
    ...


def prepareRender(*args, defaultTraversalSet: Optional[Union[str, bool]] = ..., deregister: str = ..., invokePostRender: bool = ..., invokePostRenderFrame: bool = ..., invokePostRenderLayer: bool = ..., invokePreRender: bool = ..., invokePreRenderFrame: bool = ..., invokePreRenderLayer: bool = ..., invokeSettingsUI: bool = ..., label: Optional[Union[str, bool]] = ..., listTraversalSets: bool = ..., postRender: Optional[Union[str, bool]] = ..., postRenderFrame: Optional[Union[str, bool]] = ..., postRenderLayer: Optional[Union[str, bool]] = ..., preRender: Optional[Union[str, bool]] = ..., preRenderFrame: Optional[Union[str, bool]] = ..., preRenderLayer: Optional[Union[str, bool]] = ..., restore: bool = ..., saveAssemblyConfig: bool = ..., settingsUI: Optional[Union[str, bool]] = ..., setup: bool = ..., traversalSet: Optional[Union[str, bool]] = ..., traversalSetInit: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to register, manage and invoke render traversals.
    Render traversals are used to configure a scene to prepare it for rendering.
    This command has special support for scene assembly nodes.  To render scene
    assembly nodes, a rendering traversal can activate an appropriate
    representation, for each assembly node in the scene.  When rendering is
    done, this command can correspondingly restore the representation that was
    active before rendering on each assembly.
    Render traversals are grouped into traversal sets.  A render traversal set
    includes callbacks, or render traversals, for one or more of the following
    steps of rendering, ordered by decreasing level of granularity.
    A render traversal callback is an arbitrary script, either MEL or Python,
    that can transform the Maya scene for rendering purposes.
    
    preRender
    Traversal run once per render, before any rendering is performed.
    postRender
    Traversal run once per render, after all rendering has been performed.
    preRenderLayer
    Traversal run before rendering each render layer.
    postRenderLayer
    Traversal run after rendering each render layer.
    preRenderFrame
    Traversal run before rendering each frame.
    postRenderFrame
    Traversal run after rendering each frame.
    
    During a render view or batch render, Maya will run the render traversals from
    the same traversal set, the default traversal set.  Traversal sets are named,
    so multiple traversal sets can be registered with this command, and the
    default render traversal set can be switched to any one of these registered
    traversal sets.  When changing the default traversal set, the different
    render traversal callbacks (preRender, preRenderLayer, preRenderFrame,
    postRender, postRenderLayer, postRenderFrame) are switched as a unit.
    At render time, the software rendering code invokes the callbacks of the
    default traversal set.  The prepareRender scripting capability allows for the
    development of multiple rendering preparation scripts, including from plugins,
    to provide extensibility rather than being constrained to a single
    implementation.
    A special traversal set is the "null" traversal set.  It is the initial
    default traversal set, and cannot be deregistered.  It performs no work,
    and does not save and restore the assembly node active representation
    configuration.  It will provide WYSIWYG (What You See Is What You Get)
    rendering of assembly nodes, without switching to a different representation
    to render.
    Render traversals are invoked by Maya using this command's create mode.
    This is done by Maya's rendering infrastructure, and should not be required
    unless developing new render views or batch render code.  Most uses of this
    command will simply use the edit mode to register render traversals into a
    render traversal set, or the query mode to query the names of the render
    traversals in a render traversal set.
    Render Traversals versus Render MEL Scripts
    Render traversals are similar in intent to the user-specified pre- and
    post-render, pre- and post-render layer, pre- and post-render frame MEL
    script capability.  The difference with the user MEL scripts is
    that prepareRender is in addition to, and does not replace, the user
    MEL scripts, can register multiple render traversal sets and switch them,
    and supports both MEL and Python.  The MEL render scripts are run inside
    the scope of the render traversals, that is, the preRender traversal is
    run before the pre-render MEL script and the postRender traversal is run
    after the post-render MEL script, the preRenderLayer traversal is run before
    the pre-render layer MEL script and the postRenderLayer traversal is run
    after the post-render layer MEL script, and finally the preRenderFrame
    traversal is run before the pre-render frame MEL script and the
    postRenderFrame traversal is run after the post-render frame MEL script.
    Saving and Restoring State
    The prepareRender command has support for saving and restoring the active
    representation of assembly nodes in the scene.  Use the saveAssemblyConfig flag
    to indicate that the render traversal set requires saving the assembly node
    active representation before rendering begins, and should restore the
    assembly node active representation after rendering ends.
    It is the responsibility of render traversals that modify the scene in ways
    other than changing the active representation on assembly nodes to restore the
    scene to its previous state, most likely using the postRender, postRenderLayer,
    and postRenderFrame traversals.
    Note that Maya does not call the prepareRender -restore command on
    batch render completion, since batch rendering is done on a copy of the
    scene which is discarded once rendering terminates.  Implementors of
    render traversals may wish to check whether they are running in batch mode,
    to implement the same optimization.

    Args:
        defaultTraversalSet: (edit, query) - Set or query the default traversal set.  The prepareRender command performs operations on the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        deregister: (edit) - Deregister a registered traversal set.  If the deregistered traversal set is the default traversal set, the new default traversal set will be the "null" traversal set.
        invokePostRender: (create) - Invoke the postRender render traversal for a given traversal set.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        invokePostRenderFrame: (create) - Invoke the postRenderFrame render traversal for a given traversal set.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        invokePostRenderLayer: (create) - Invoke the postRenderLayer render traversal for a given traversal set.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        invokePreRender: (create) - Invoke the preRender render traversal for a given traversal set.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        invokePreRenderFrame: (create) - Invoke the preRenderFrame render traversal for a given traversal set.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        invokePreRenderLayer: (create) - Invoke the preRenderLayer render traversal for a given traversal set.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        invokeSettingsUI: (create) - Invoke the settings UI callback to populate a layout with UI controls, for a given traversal set.  The current UI parent will be a form layout, which the callback can query using the setParent command.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        label: (edit, query) - Set or query the label for a given traversal set.  The label is used for UI display purposes, and can be localized.  The traversal set will be the default, unless the -traversalSet flag is used to specify an explicit traversal set.
        listTraversalSets: (query) - Query the supported render traversal sets.
        postRender: (edit, query) - Set or query the postRender render traversal for a given traversal set.  This traversal is run after a render.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        postRenderFrame: (edit, query) - Set or query the postRenderFrame render traversal for a given traversal set.  This traversal is run after the render of a single frame, with a render layer.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        postRenderLayer: (edit, query) - Set or query the postRenderLayer render traversal for a given traversal set.  This traversal is run after a render layer is rendered, within a render.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        preRender: (edit, query) - Set or query the preRender render traversal for a given traversal set.  This traversal is run before a render.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        preRenderFrame: (edit, query) - Set or query the preRenderFrame render traversal for a given traversal set.  This traversal is run before the render of a single frame, with a render layer.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        preRenderLayer: (edit, query) - Set or query the preRenderLayer render traversal for a given traversal set.  This traversal is run before a render layer is rendered, within a render.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        restore: (create) - Clean up after rendering, including restoring the assembly active representation configuration for the whole scene, if the saveAssemblyConfig flag for the traversal set is true.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        saveAssemblyConfig: (edit, query) - Set or query whether or not the assembly active representation configuration for the whole scene should be saved for a given traversal set.  The traversal set will be the default, unless the -traversalSet flag is used to specify an explicit traversal set.
        settingsUI: (edit, query) - Set or query the settings UI callback for a given traversal set.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        setup: (create) - Setup render preparation, including saving the assembly active representation configuration for the whole scene, if the saveAssemblyConfig flag for the traversal set is true.  Any previously-saved configuration will be overwritten.  The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set.
        traversalSet: (create, edit, query) - Set or query properties for the specified registered traversal set. 			In query mode, this flag needs a value.
        traversalSetInit: (edit, query) - Set or query the traversal set initialisation callback for a given traversal set. The traversal set will be the default traversal set, unless the -traversalSet flag is used to specify an explicit traversal set. This callback is invoked whenever the specified traversal set becomes the default. traversal set.
    """
    ...


def projectionManip(*args, fitBBox: bool = ..., projType: Optional[Union[int, bool]] = ..., switchType: bool = ..., query: bool = ...) -> Any:
    r"""
    Various commands to set the manipulator to interesting positions.

    Args:
        fitBBox: (create) - Fit the projection manipulator size and position to the shading group bounding box. The orientation is not modified.
        projType: (create) - Set the projection type to the given value. Projection type values are:   1 = planar.  2 = spherical.  3 = cylindrical.  4 = ball.  5 = cubic.  6 = triplanar.  7 = concentric.  8 = camera.
        switchType: (create) - Loop over the allowed types. If the hardware shading is on, it loops over the hardware shadeable types (planar, cylindrical, spherical), otherwise, it loops over all the types. If there is no given value, it loops over the different projection types.
    """
    ...


def psdChannelOutliner(*args, addChild: Tuple[str, str] = ..., allItems: bool = ..., annotation: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., doubleClickCommand: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., fullPathName: bool = ..., height: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., isObscured: bool = ..., manage: bool = ..., noBackground: bool = ..., numberOfItems: bool = ..., numberOfPopupMenus: bool = ..., parent: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., psdParent: str = ..., removeAll: bool = ..., removeChild: str = ..., select: str = ..., selectCommand: Optional[Union[str, bool]] = ..., selectItem: bool = ..., statusBarMessage: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., visible: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create a psdChannelOutliner control which is capable of displaying
    a tree structure upto one level.

    Args:
        addChild: (edit, multiuse) - This flag should be used along with the "-psdParent/ppa" flag. A string item gets added as a child to the parent specifed with "-psdParent/ppa" flag. The next string assigns an associated image name.
        allItems: (query) - Returns all the items in the form parent.child.
        annotation: (create, edit, query) - Annotate the control with an extra string value.
        backgroundColor: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag: (create, edit, query) - Add a documentation flag to the control.  The documentation flag has a directory structure. (e.g., -dt render/multiLister/createNode/material)
        doubleClickCommand: (create, edit) - Specify the command to be executed when an item is double clicked.
        dragCallback: (create, edit) - Adds a callback that is called when the middle mouse button is pressed.  The MEL version of the callback is of the form:  global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  The proc returns a string array that is transferred to the drop site. By convention the first string in the array describes the user settable message type.  Controls that are application defined drag sources may ignore the callback. $mods allows testing for the key modifiers CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3 == CTRL + SHIFT.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def callbackName( dragControl, x, y, modifiers ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "x", "y", "modifiers".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")
        dropCallback: (create, edit) - Adds a callback that is called when a drag and drop operation is released above the drop site.  The MEL version of the callback is of the form:  global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  The proc receives a string array that is transferred from the drag source. The first string in the msgs array describes the user defined message type. Controls that are application defined drop sites may ignore the callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "dropControl", "messages", "x", "y", "type".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")
        enable: (create, edit, query) - The enable state of the control.  By default, this flag is set to true and the control is enabled.  Specify false and the control will appear dimmed or greyed-out indicating it is disabled.
        enableBackground: (create, edit, query) - Enables the background color of the control.
        enableKeyboardFocus: (create, edit, query) - If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse. This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls. If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        fullPathName: (query) - Return the full path name of the widget, which includes all the parents.
        height: (create, edit, query) - The height of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
        highlightColor: (create, edit, query) - The highlight color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.
        isObscured: (query) - Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.
        manage: (create, edit, query) - Manage state of the control.  An unmanaged control is not visible, nor does it take up any screen real estate.  All controls are created managed by default.
        noBackground: (create, edit) - Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
        numberOfItems: (query) - Total number of items in the control.
        numberOfPopupMenus: (query) - Return the number of popup menus attached to this control.
        parent: (create, query) - The parent layout for this control.
        popupMenuArray: (query) - Return the names of all the popup menus attached to this control.
        preventOverride: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        psdParent: (edit) - Adds an item string to the controls which is treated as parent.
        removeAll: (edit) - Removes all the items from the control.
        removeChild: (edit, multiuse) - Deletes the particular child of the parent as specifed in "-psdParent/ppa" flag.
        select: (edit) - Select the named item.
        selectCommand: (create, edit) - Specify the command to be executed when an item is selected.
        selectItem: (query) - Returns the selected items.
        statusBarMessage: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
        visible: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def psdEditTextureFile(*args, addChannel: Optional[Union[str, bool]] = ..., addChannelColor: Optional[Union[Tuple[str, float, float, float], bool]] = ..., addChannelImage: Optional[Union[Tuple[str, str], bool]] = ..., deleteChannel: Optional[Union[str, bool]] = ..., psdFileName: Optional[Union[str, bool]] = ..., snapShotImage: Optional[Union[str, bool]] = ..., uvSnapPostionTop: bool = ...) -> Any:
    r"""
    Edits the existing PSD file. Addition and deletion of the channels (layer sets) are
    supported.

    Args:
        addChannel: (create, multiuse) - Adds an empty layer set with the given name to a already existing PSD file.
        addChannelColor: (create, multiuse) - (M) Specifies the filled color of  the layer which is created in a layer set given by the layer name.
        addChannelImage: (create, multiuse) - (M) Specifies the image file name whose image needs to be added as a layer to a given layer set which is the first string.
        deleteChannel: (create, multiuse) - (M) Deletes the channels (layer sets) from a PSD file. This is a multiuse flag.
        psdFileName: (create) - PSD file name.
        snapShotImage: (create) - Image file name on the disk containing UV snapshot / reference image.
        uvSnapPostionTop: (create) - Specifies the position of UV snapshot image layer  in the PSD file. "True" positions this layer at the top and "False" positions the layer at the bottom next to the background layer in the PSD file
    """
    ...


def psdExport(*args, alphaChannelIdx: Optional[Union[int, bool]] = ..., bytesPerChannel: Optional[Union[int, bool]] = ..., emptyLayerSet: bool = ..., format: Optional[Union[str, bool]] = ..., layerName: Optional[Union[str, bool]] = ..., layerSetName: Optional[Union[str, bool]] = ..., outFileName: Optional[Union[str, bool]] = ..., preMultiplyAlpha: bool = ..., psdFileName: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    Writes the Photoshop file layer set into different formats.  The output
            file depth (bit per channel ) can be different from that of the input.
            If the input is 16 bpc and output is 8 bpc, there will be data loss.

    Args:
        alphaChannelIdx: (create, query) - Index of the alpha channel to output, if not supplied, writes out the default alpha channel.  The index is zero based. This is useful to write out specific alpha channels available as "Additional Alpha Channels" of Photoshop.
        bytesPerChannel: (create, query) - Output file depth. Any of these keyword:  0 for choosing depth based on input 1 for 8 bits per channel 2 for 16 bits per channel  Default is 0.
        emptyLayerSet: (create, query) - Option to check if the given layer set is empty or not.  This should be used in query mode and input file name and layer set names should be specified.
        format: (create, query) - Output file format. Any of these keyword: "iff", "sgi", "pic", "tif", "als", "gif", "rla", "jpg" Default is iff.
        layerName: (create, query) - Name of the layer to output.
        layerSetName: (create, query) - Name of the layer set to output, if not supplied, writes out the Composite image. 			In query mode, this flag needs a value.
        outFileName: (create, query) - Name(with path) of the output file.
        preMultiplyAlpha: (create, query) - Option to multiply RGB colors with alpha values.  If (r,g,b,a) is the value of pixel, it will be changed to (r*a, g*a, b*a, a) when this flag is used.
        psdFileName: (create, query) - Name(with path) of the input Photoshop file. 			In query mode, this flag needs a value.
    """
    ...


def psdTextureFile(*args, channelRGB: Optional[Union[Tuple[str, int, int, int, int], bool]] = ..., channels: Optional[Union[Tuple[str, int, bool], bool]] = ..., imageFileName: Optional[Union[Tuple[str, str, int], bool]] = ..., psdFileName: Optional[Union[str, bool]] = ..., snapShotImageName: Optional[Union[str, bool]] = ..., uvSnapPostionTop: bool = ..., xResolution: Optional[Union[int, bool]] = ..., yResolution: Optional[Union[int, bool]] = ...) -> Any:
    r"""
    Creates a Photoshop file with UVSnap shot image and the layer set
    names as the input.

    Args:
        channelRGB: (create, multiuse) - (M) Layer set names, index, red, green and blue values are given as input. Using this flag, the layers created can be filled with specified colors.  This is a multi use flag.  The index specifies the placement order of layer sets in the created file.
        channels: (create, multiuse) - (M) Layer set names and index are given as input. This is a multi use flag. A layer set with the given name will be created.  The second argument is the index which specifies the placement order of layer sets in the created file. The third argument is a boolean, if "true" a layer is created inside the layer set , "false" creates an  empty layer set
        imageFileName: (create, multiuse) - Image file name, Layerset name and index.  The image in the file will be transferred to layer set specified.  The index specifies the placement order of layer sets in the created psd file.  The image file specified can be in any of the formats supported by maya (ex. iff, jpg, gif, tif etc.)
        psdFileName: (create) - PSD file name.
        snapShotImageName: (create) - Image file name on the disk containing UV snapshot / reference image.
        uvSnapPostionTop: (create) - Specifies the position of UV snapshot image layer  in the PSD file. "True" positions this layer at the top and "False" positions the layer at the bottom next to the background layer in the PSD file
        xResolution: (create) - X - resolution of the image.
        yResolution: (create) - Y - resolution of the image.
    """
    ...


def rampColorPort(*args, annotation: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., fullPathName: bool = ..., height: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., isObscured: bool = ..., manage: bool = ..., noBackground: bool = ..., node: Optional[Union[str, bool]] = ..., numberOfPopupMenus: bool = ..., parent: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., selectedColorControl: Optional[Union[str, bool]] = ..., selectedInterpControl: Optional[Union[str, bool]] = ..., selectedPositionControl: Optional[Union[str, bool]] = ..., statusBarMessage: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., verticalLayout: bool = ..., visible: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a control that displays an image representing
    the ramp node specified, and supports editing of that node.

    Args:
        annotation: (create, edit, query) - Annotate the control with an extra string value.
        backgroundColor: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag: (create, edit, query) - Add a documentation flag to the control.  The documentation flag has a directory structure. (e.g., -dt render/multiLister/createNode/material)
        dragCallback: (create, edit) - Adds a callback that is called when the middle mouse button is pressed.  The MEL version of the callback is of the form:  global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  The proc returns a string array that is transferred to the drop site. By convention the first string in the array describes the user settable message type.  Controls that are application defined drag sources may ignore the callback. $mods allows testing for the key modifiers CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3 == CTRL + SHIFT.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def callbackName( dragControl, x, y, modifiers ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "x", "y", "modifiers".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")
        dropCallback: (create, edit) - Adds a callback that is called when a drag and drop operation is released above the drop site.  The MEL version of the callback is of the form:  global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  The proc receives a string array that is transferred from the drag source. The first string in the msgs array describes the user defined message type. Controls that are application defined drop sites may ignore the callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "dropControl", "messages", "x", "y", "type".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")
        enable: (create, edit, query) - The enable state of the control.  By default, this flag is set to true and the control is enabled.  Specify false and the control will appear dimmed or greyed-out indicating it is disabled.
        enableBackground: (create, edit, query) - Enables the background color of the control.
        enableKeyboardFocus: (create, edit, query) - If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse. This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls. If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        fullPathName: (query) - Return the full path name of the widget, which includes all the parents.
        height: (create, edit, query) - The height of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
        highlightColor: (create, edit, query) - The highlight color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.
        isObscured: (query) - Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.
        manage: (create, edit, query) - Manage state of the control.  An unmanaged control is not visible, nor does it take up any screen real estate.  All controls are created managed by default.
        noBackground: (create, edit) - Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
        node: (create) - Specifies the name of the newRamp texture node this port will represent.
        numberOfPopupMenus: (query) - Return the number of popup menus attached to this control.
        parent: (create, query) - The parent layout for this control.
        popupMenuArray: (query) - Return the names of all the popup menus attached to this control.
        preventOverride: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        selectedColorControl: (create, edit) - Set the name of the control (if any) which is to be used to show the color of the currently selected entry in the ramp. This control will automatically update as the user selects different entries in the ramp, and will modify the selected entry if edited. The type of control must be an attrColorSliderGrp.
        selectedInterpControl: (create, edit) - Set the name of the control (if any) which is to be used to show the interpolation of the currently selected entry in the ramp. This control will automatically update as the user selects different entries in the ramp, and will modify the selected entry if edited. The type of control must be an attrEnumOptionMenuGrp.
        selectedPositionControl: (create, edit) - Set the name of the control (if any) which is to be used to show the position of the currently selected entry in the ramp. This control will automatically update as the user selects different entries in the ramp, and will modify the selected entry if edited. The type of control must be an attrFieldSliderGrp.
        statusBarMessage: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
        verticalLayout: (create, edit, query) - Set the preview's layout.
        visible: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def render(*args, abortMissingTexture: bool = ..., batch: bool = ..., keepPreImage: bool = ..., layer: Optional[Union[str, bool]] = ..., nglowpass: bool = ..., nshadows: bool = ..., replace: bool = ..., xresolution: Optional[Union[int, bool]] = ..., yresolution: Optional[Union[int, bool]] = ...) -> Any:
    r"""
    The render command is used to start off a MayaSoftware rendering
    session of the currently active camera. If a rendering is already
    in progress, then this command stops the rendering. This command is
    not undoable.

    Args:
        abortMissingTexture: (create) - Abort renderer when encountered missing texture. Only available when -batch is set
        batch: (create) - Run in batch mode. Compute the images for all renderable cameras. This is the mel equivalent of running maya in batch mode with the -render flag set. All other flags are ignored when -batch is used.
        keepPreImage: (create) - Keep the renderings prior to post-process around. Only available when -batch is set
        layer: (create) - Render the specified render layer. Only this render layer will be rendered, regardless of the renderable attribute value of the render layer. The layer name will be appended to the output image file name. The specified render layer becomes the current render layer before rendering, and remains as current render layer after the rendering.
        nglowpass: (create) - Overwrite glow pass capabilities (can turn off glow pass globally by setting this value to false)
        nshadows: (create) - Shadowing capabilities (can turn off shadow globally by setting this value to false)
        replace: (create) - Replace the rendered image if it already exists. Only available when -batch is set
        xresolution: (create) - Overwrite x resolution
        yresolution: (create) - Overwrite y resolution
    """
    ...


def renderer(*args, addGlobalsNode: Optional[Union[str, bool]] = ..., addGlobalsTab: Optional[Union[Tuple[str, str, str], bool]] = ..., batchRenderOptionsProcedure: Optional[Union[str, bool]] = ..., batchRenderOptionsStringProcedure: Optional[Union[str, bool]] = ..., batchRenderProcedure: Optional[Union[str, bool]] = ..., cancelBatchRenderProcedure: Optional[Union[str, bool]] = ..., changeIprRegionProcedure: Optional[Union[str, bool]] = ..., commandRenderProcedure: Optional[Union[str, bool]] = ..., exists: bool = ..., globalsNodes: bool = ..., globalsTabCreateProcNames: bool = ..., globalsTabLabels: bool = ..., globalsTabUpdateProcNames: bool = ..., iprOptionsMenuLabel: Optional[Union[str, bool]] = ..., iprOptionsProcedure: Optional[Union[str, bool]] = ..., iprOptionsSubMenuProcedure: Optional[Union[str, bool]] = ..., iprRenderProcedure: Optional[Union[str, bool]] = ..., iprRenderSubMenuProcedure: Optional[Union[str, bool]] = ..., isRunningIprProcedure: Optional[Union[str, bool]] = ..., logoCallbackProcedure: Optional[Union[str, bool]] = ..., logoImageName: Optional[Union[str, bool]] = ..., materialViewRendererList: bool = ..., materialViewRendererPause: bool = ..., materialViewRendererSuspend: bool = ..., namesOfAvailableRenderers: bool = ..., pauseIprRenderProcedure: Optional[Union[str, bool]] = ..., polyPrelightProcedure: Optional[Union[str, bool]] = ..., refreshIprRenderProcedure: Optional[Union[str, bool]] = ..., renderDiagnosticsProcedure: Optional[Union[str, bool]] = ..., renderGlobalsProcedure: Optional[Union[str, bool]] = ..., renderMenuProcedure: Optional[Union[str, bool]] = ..., renderOptionsProcedure: Optional[Union[str, bool]] = ..., renderProcedure: Optional[Union[str, bool]] = ..., renderRegionProcedure: Optional[Union[str, bool]] = ..., renderSequenceProcedure: Optional[Union[str, bool]] = ..., rendererUIName: Optional[Union[str, bool]] = ..., renderingEditorsSubMenuProcedure: Optional[Union[str, bool]] = ..., showBatchRenderLogProcedure: Optional[Union[str, bool]] = ..., showBatchRenderProcedure: Optional[Union[str, bool]] = ..., showRenderLogProcedure: Optional[Union[str, bool]] = ..., startIprRenderProcedure: Optional[Union[str, bool]] = ..., stopIprRenderProcedure: Optional[Union[str, bool]] = ..., supportColorManagement: bool = ..., textureBakingProcedure: Optional[Union[str, bool]] = ..., unregisterRenderer: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to register renders.  This command allows you to
    specify the UI name and procedure names for renderers.
    The command also allow you to query the UI name and the procedure
    names for the registered renders.

    Args:
        addGlobalsNode: (create, edit, query) - This flag allows the user to add a globals node the specified renderer uses.
        addGlobalsTab: (create, edit) - Add a tab associated with the specified renderer for the unified render globals window.
        batchRenderOptionsProcedure: (create, edit, query) - Set or query the batch render options procedure associated with the specified renderer.
        batchRenderOptionsStringProcedure: (create, edit, query) - Set or query the argument string that will be used with the command line utility 'Render' when doing a batch render
        batchRenderProcedure: (create, edit, query) - Set or query the batch render procedure associated with the specified renderer.
        cancelBatchRenderProcedure: (create, edit, query) - Set or query returns the cancel batch render procedure associated with the specified renderer.
        changeIprRegionProcedure: (create, edit, query) - Set or query the change IPR region procedure associated with the specified renderer.
        commandRenderProcedure: (create, edit, query) - Set or query the command line rendering procedure associated with the specified renderer.
        exists: (edit, query) - The flag returns true if the specified renderer is registered in the registry, and it returns false otherwise.
        globalsNodes: (create, edit, query) - This flag returns the list of render globals nodes the specified renderer uses.
        globalsTabCreateProcNames: (create, edit, query) - This flag returns the names of procedures that are used to create the unified render globals window tabs that are associated with the specified renderer.
        globalsTabLabels: (create, edit, query) - This flag returns the labels of unified render globals window tabs that are associated with the specified renderer.
        globalsTabUpdateProcNames: (create, edit, query) - This flag returns the names of procedures that are used to update the unified render globals window tabs that are associated with the specified renderer.
        iprOptionsMenuLabel: (create, edit, query) - Set or query the label for the IPR update options menu which is under the render view's IPR menu.
        iprOptionsProcedure: (create, edit, query) - Set or query the IPR render options procedure associated with the specified renderer.
        iprOptionsSubMenuProcedure: (create, edit, query) - Set or query the procedure for creating the sub menu for the IPR update options menu which is under the render view's IPR menu.
        iprRenderProcedure: (create, edit, query) - Set or query the IPR render command associated with the specified renderer.
        iprRenderSubMenuProcedure: (create, edit, query) - Set or query the procedure for creating the sub menu for the IPR render menu which is under the render view's IPR menu.
        isRunningIprProcedure: (create, edit, query) - Set or query the isRunningIpr command associated with the specified renderer.
        logoCallbackProcedure: (create, edit, query) - Set or query the procedure which is a callback associated to the logo for the specified renderer.   For example, the logo and the callback can be used in the unified render globals window beside the "Render Using" optionMenu.
        logoImageName: (create, edit, query) - Set or query the logo image name for the specified renderer. The logo is a image representing the renderer.
        materialViewRendererList: (edit, query) - Returns the names of material view renderers that are currently registered.
        materialViewRendererPause: (edit, query) - Specifies whether to pause the material viewer. Useful for globally halting updates to the material viewer. The material view renderer will remain suspended while the viewer is paused.
        materialViewRendererSuspend: (edit, query) - Specifies whether to suspend or resume the material view renderer. Useful for temporarily stopping the material view renderer while another rendering task is running.
        namesOfAvailableRenderers: (edit, query) - Returns the names of renderers that are currently registered.
        pauseIprRenderProcedure: (create, edit, query) - Set or query the pause IPR render procedure associated with the specified renderer.
        polyPrelightProcedure: (create, edit, query) - Set or query the polygon prelight procedure associated with the specified renderer.
        refreshIprRenderProcedure: (create, edit, query) - Set or query the refresh IPR render procedure associated with the specified renderer.
        renderDiagnosticsProcedure: (create, edit, query) - Set or query the render diagnostics procedure associated with the specified renderer.
        renderGlobalsProcedure: (create, edit, query) - This flag is obsolete.  It will be removed in the next release.
        renderMenuProcedure: (create, edit, query) - This flag is obsolete. It will be removed in the next release.
        renderOptionsProcedure: (create, edit, query) - Set or query the render options procedure associated with the specified renderer.
        renderProcedure: (create, edit, query) - Set or query the render command associated with the specified renderer.
        renderRegionProcedure: (create, edit, query) - Set or query the render region procedure associated with the specified renderer.
        renderSequenceProcedure: (create, edit, query) - Set or query the sequence rendering procedure associated with the specified renderer.
        rendererUIName: (create, edit, query) - Set or query the rendererUIName for the specified renderer. The rendererUIName is the name of the renderer as it would appear in menus.
        renderingEditorsSubMenuProcedure: (create, edit, query) - Set or query the procedure reponsible for creating renderer specific editors submenu under the "Rendering Editors" menu for the specified renderer.
        showBatchRenderLogProcedure: (create, edit, query) - Set or query the log file batch procedure associated with the specified renderer.
        showBatchRenderProcedure: (create, edit, query) - Set or query the show batch render procedure associated with the specified renderer.
        showRenderLogProcedure: (create, edit, query) - Set or query the log file render procedure associated with the specified renderer.
        startIprRenderProcedure: (create, edit, query) - Set or query the start IPR render procedure associated with the specified renderer.
        stopIprRenderProcedure: (create, edit, query) - Set or query the stop IPR render procedure associated with the specified renderer.
        supportColorManagement: (edit, query) - Specifies whether the renderer supports color management.
        textureBakingProcedure: (create, edit, query) - Set or query the texture baking procedure associated with the specified renderer.
        unregisterRenderer: (edit, query) - Unregister the specified renderer.
    """
    ...


def renderGlobalsNode(*args, name: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., renderQuality: Optional[Union[str, bool]] = ..., renderResolution: Optional[Union[str, bool]] = ..., shared: bool = ..., skipSelect: bool = ...) -> Any:
    r"""
    This command creates a new node in the dependency graph of the
    specified type.
    
    The renderGlobalsNode creates a render globals node and registers it
    with the model. The createNode command will not register nodes of this
    type correctly.

    Args:
        name: (create) - Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace doesn't exist, we will create the namespace.
        parent: (create) - Specifies the parent in the DAG under which the new node belongs.
        renderQuality: (create) - Set the quality to be the renderQuality node with the given name.
        renderResolution: (create) - Set the resolution to be the resolution node with the given name.
        shared: (create) - This node is shared across multiple files, so only create it if it does not already exist.
        skipSelect: (create) - This node is not to be selected after creation, the original selection will be preserved.
    """
    ...


def renderInfo(*args, castShadows: bool = ..., chordHeight: Optional[Union[float, bool]] = ..., chordHeightRatio: Optional[Union[float, bool]] = ..., doubleSided: bool = ..., edgeSwap: bool = ..., minScreen: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., opposite: bool = ..., smoothShading: bool = ..., unum: Optional[Union[int, bool]] = ..., useChordHeight: bool = ..., useChordHeightRatio: bool = ..., useDefaultLights: bool = ..., useMinScreen: bool = ..., utype: Optional[Union[int, bool]] = ..., vnum: Optional[Union[int, bool]] = ..., vtype: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The renderInfo commands sets geometric properties of surfaces
    of the selected object.

    Args:
        castShadows: (create) - Determines if object casts shadow or not.
        chordHeight: (create) - Tessellation subdivision criteria.
        chordHeightRatio: (create) - Tessellation subdivision criteria.
        doubleSided: (create) - Determines if object double or single sided.
        edgeSwap: (create) - Tessellation subdivision criteria.
        minScreen: (create) - Tessellation subdivision criteria.
        name: (create) - Namespace to use.
        opposite: (create) - Determines if the normals of the object is to be reversed.
        smoothShading: (create) - Determines if smooth shaded, or flat shaded - applies only to polysets.
        unum: (create) - Tessellation subdivision criteria.
        useChordHeight: (create) - Tessellation subdivision criteria.
        useChordHeightRatio: (create) - Tessellation subdivision criteria.
        useDefaultLights: (create) - Obsolete flag.
        useMinScreen: (create) - Tessellation subdivision criteria.
        utype: (create) - Tessellation subdivision criteria.
        vnum: (create) - Tessellation subdivision criteria.
        vtype: (create) - Tessellation subdivision criteria.
    """
    ...


def renderLayerPostProcess(*args, keepImages: bool = ..., sceneName: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    Post process the results when rendering is done with. Presently this
    generates a layered PSD file using individual iff files.

    Args:
        keepImages: (create, query) - When set to on, the original iff images are kept after the conversion to PSD. Default is to remove them.
        sceneName: (create, query) - Specifies the scene name for interactive batch rendering.
    """
    ...


def renderManip(*args, camera: Optional[Union[Tuple[bool, bool, bool, bool, bool], bool]] = ..., light: Optional[Union[Tuple[bool, bool, bool], bool]] = ..., spotLight: Optional[Union[Tuple[bool, bool, bool, bool, bool, bool, bool], bool]] = ..., state: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates manipulators for cameras or lights.

    Args:
        camera: (edit, query) - Query or edit the visiblity status of the component camera manipulators. The order of components are: cycling index, center of interest, pivot, clipping planes, and unused.
        light: (edit, query) - Query or edit the visiblity status of the component light manipulators. The order of components are: cycling index, center of interest, and pivot.
        spotLight: (edit, query) - Query or edit the visiblity status of the component spot light manipulators. The order of components are: cycling index, center of interest, pivot, cone angle, penumbra, look through barn doors, and decay regions.
        state: (edit, query) - Query or edit the state of manipulators on an camera, ambient light, directional light, point light, or spot light. This flag's default value is on.
    """
    ...


def renderPartition(*args, query: bool = ...) -> Any:
    r"""
    Set or query the model's current partition. When flag q is
    not used, a partion name must be passed as an argument. In this
    case the current partition is set to that name.

    Args:
    """
    ...


def renderPassRegistry(*args, channels: Optional[Union[int, bool]] = ..., isPassSupported: bool = ..., passID: Optional[Union[str, bool]] = ..., passName: bool = ..., renderer: Optional[Union[str, bool]] = ..., supportedChannelCounts: bool = ..., supportedDataTypes: bool = ..., supportedPassSemantics: bool = ..., supportedRenderPassNames: bool = ..., supportedRenderPasses: bool = ...) -> Any:
    r"""
    query information related with render passes.

    Args:
        channels: (create) - Specify the number of channels for query.
        isPassSupported: (create) - Return whether the pass is supported by the renderer This flag must be specified by the flag -passID firstly. The renderer whose default value is the current renderer is specified by the flag renderer.
        passID: (create) - Specify the render pass ID for query.
        passName: (create) - Get the pass name for the passID. This flag must be specified by the flag -passID firstly.
        renderer: (create) - Specify a renderer when using this command. By default the current renderer is specified.
        supportedChannelCounts: (create) - List channel counts supported by the renderer(specified by the flag -renderer) and the specified pass ID. This flag must be specified by the flag -passID firstly.
        supportedDataTypes: (create) - List frame buffer types supported by the renderer(specified by the flag -renderer), the specified passID and channels. This flag must be specified by the flag -passID and -channels firstly.
        supportedPassSemantics: (create) - List pass semantics supported by the specified passID. This flag must be specified by the flag -passId firstly.
        supportedRenderPassNames: (create) - List render pass names supported by the renderer(specified by the flag -renderer).
        supportedRenderPasses: (create) - List render passes supported by the renderer(specified by the flag -renderer).
    """
    ...


def renderQualityNode(*args, name: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., shared: bool = ..., skipSelect: bool = ...) -> Any:
    r"""
    This command creates a new node in the dependency graph of the
    specified type.
    
    The renderQualityNode creates a render quality node
    and registers it with the model.  The createNode
    command will not register nodes of this type correctly.

    Args:
        name: (create) - Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace doesn't exist, we will create the namespace.
        parent: (create) - Specifies the parent in the DAG under which the new node belongs.
        shared: (create) - This node is shared across multiple files, so only create it if it does not already exist.
        skipSelect: (create) - This node is not to be selected after creation, the original selection will be preserved.
    """
    ...


def renderSettings(*args, camera: Optional[Union[str, bool]] = ..., customTokenString: Optional[Union[str, bool]] = ..., firstImageName: bool = ..., fullPath: bool = ..., fullPathTemp: bool = ..., genericFrameImageName: Optional[Union[str, bool]] = ..., imageGenericName: bool = ..., lastImageName: bool = ..., layer: Optional[Union[str, bool]] = ..., leaveUnmatchedTokens: bool = ...) -> Any:
    r"""
    Query interface to the common tab of the render settings

    Args:
        camera: (create) - Specify a camera that you want to replace the current renderable camera
        customTokenString: (create) - Specify a custom key-value string to use to replace custom tokens in the file name. Use with firstImageName or lastImageName. Basic tokens (Scene, Layer, RenderLayer, Camera, Version, Extension) will be automatically expanded. Any other tokens must be specified here to be expanded. The format of the string is a space separated list of tokens-value pairs. For example, if the file name string is "myFile_<myToken>_<myOtherToken>_v" then the argument to this flag string should take the form "myToken=myTokenValue myOtherToken=myOtherTokenValue".
        firstImageName: (create) - Returns the first image name
        fullPath: (create) - Returns the full path for the image using the current project. Use with firstImageName, lastImageName, or genericFrameImageName.
        fullPathTemp: (create) - Returns the full path for the preview render of the image using the current project. Use with firstImageName, lastImageName, or genericFrameImageName.
        genericFrameImageName: (create) - Returns the generic frame image name with the custom specified frame index token
        imageGenericName: (create) - Returns the image generic name
        lastImageName: (create) - Returns the last image name
        layer: (create) - Specify a render layer name that you want to replace the current render layer
        leaveUnmatchedTokens: (create) - Do not remove unmatched tokens from the name string. Use with firstImageName or lastImageName.
    """
    ...


def renderThumbnailUpdate(*args, forceUpdate: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    Toggle the updating of object thumbnails. These are visible in tools
    like the Attribute Editor and Hypershade. All thumbnails everywhere
    will not update to reflect changes to the object until this command is
    used to toggle to true unless a specific thumbnail is forced to render
    using the -forceUpdate flag.

    Args:
        forceUpdate: (create) - Force the thumbnail to update.
    """
    ...


def renderWindowEditor(*args, autoResize: bool = ..., blendMode: Optional[Union[int, bool]] = ..., caption: Optional[Union[str, bool]] = ..., changeCommand: Optional[Union[Tuple[str, str, str, str], bool]] = ..., clear: Optional[Union[Tuple[int, int, float, float, float], bool]] = ..., cmEnabled: bool = ..., colorManage: bool = ..., compDisplay: Optional[Union[int, bool]] = ..., compImageFile: Optional[Union[str, bool]] = ..., control: bool = ..., currentCamera: Optional[Union[str, bool]] = ..., currentCameraRig: Optional[Union[str, bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., displayImage: Optional[Union[int, bool]] = ..., displayImageViewCount: Optional[Union[int, bool]] = ..., displayStyle: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., doubleBuffer: bool = ..., drawAxis: bool = ..., editorName: bool = ..., exists: bool = ..., exposure: Optional[Union[float, bool]] = ..., filter: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., frameImage: bool = ..., frameRegion: bool = ..., gamma: Optional[Union[float, bool]] = ..., highlightConnection: Optional[Union[str, bool]] = ..., loadImage: str = ..., lockMainConnection: bool = ..., mainListConnection: Optional[Union[str, bool]] = ..., marquee: Optional[Union[Tuple[float, float, float, float], bool]] = ..., nbImages: bool = ..., nextViewImage: bool = ..., outputColorManage: bool = ..., panel: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., pcaption: Optional[Union[str, bool]] = ..., realSize: bool = ..., refresh: bool = ..., removeAllImages: bool = ..., removeImage: bool = ..., resetRegion: bool = ..., resetViewImage: bool = ..., saveImage: bool = ..., scaleBlue: Optional[Union[float, bool]] = ..., scaleGreen: Optional[Union[float, bool]] = ..., scaleRed: Optional[Union[float, bool]] = ..., selectionConnection: Optional[Union[str, bool]] = ..., showRegion: Optional[Union[Tuple[int, int], bool]] = ..., singleBuffer: bool = ..., snapshot: Optional[Union[Tuple[str, int, int], bool]] = ..., snapshotMode: bool = ..., stateString: bool = ..., stereo: Optional[Union[int, bool]] = ..., stereoImageOrientation: Optional[Union[Tuple[str, str], bool]] = ..., stereoMode: Optional[Union[str, bool]] = ..., toggle: bool = ..., unParent: bool = ..., unlockMainConnection: bool = ..., updateMainConnection: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., viewImageCount: Optional[Union[int, bool]] = ..., viewTransformName: Optional[Union[str, bool]] = ..., writeImage: str = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create a editor window that can receive the result of the
    rendering process

    Args:
        autoResize: (create, edit, query) - Lets the render view editor automatically resize the viewport or not.
        blendMode: (create, edit, query) - Sets the blend mode for the render view. New image sent to the render view will be blended with the previous image in the render view, and the composited image will appear.
        caption: (create, edit, query) - Sets the caption which appears at the bottom of the render view.
        changeCommand: (create, edit, query) - Parameters:  First string: command Second string: editorName Third string: editorCmd Fourth string: updateFunc   Call the command when something changes in the editor The command should have this prototype :  command(string $editor, string $editorCmd, string $updateFunc, int $reason)  The possible reasons could be :  0: no particular reason 1: scale color 2: buffer (single/double) 3: axis  4: image displayed 5: image saved in memory
        clear: (create, edit, query) - Clear the image with the given color at the given resolution. Arguments are respectively: width height red green blue.
        cmEnabled: (edit, query) - Turn on or off applying color management in the View.  If set, the color management configuration set in the current view is used.
        colorManage: (edit) - When used with the writeImage flag, causes the written image to be color-managed using the settings from the view color manager attached to the view.
        compDisplay: (create, edit, query) - 0 : disable compositing. 1 : displays the composited image immediately. For example, when foreground layer tile is sent to the render view window, the composited tile is displayed in the render view window, and the original foreground layer tile is not displayed. 2 : display the un-composited image, and keep the composited image for the future command. For example, when foreground layer tile is sent to the render view window, the original foreground layer tile is not displayed, and the composited tile is stored in a buffer. 3 : show the current composited image. If there is a composited image in the buffer, display it.
        compImageFile: (create, edit, query) - Open the given image file and blend with the buffer as if the image was just rendered.
        control: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        currentCamera: (create, edit, query) - Get or set the current camera. (used when redoing last render)
        currentCameraRig: (create, edit, query) - Get or set the current camera rig name. If a camera rig is specified, it will be used when redoing the last render as opposed to the currentCamera value, as the currentCamera value will hold the child camera last used for rendering the camera rig.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        displayImage: (edit, query) - Set a particular image in the Editor Image Stack as the current Editor Image. Images are added to the Editor Image Stack using the "si/saveImage" flag.
        displayImageViewCount: (query) - Query the number of views stored for a given image in the Editor Image Stack. This is not the same as querying using "viewImageCount" which returns the number of views for the current rendered image.
        displayStyle: (create, edit, query) - Set the mode to display the image. Valid values are:  "color" to display the basic RGB image "mask" to display the mask channel "lum" to display the luminance of the image
        docTag: (create, edit, query) - Attaches a tag to the editor.
        doubleBuffer: (create, edit, query) - Set the display in double buffer mode
        drawAxis: (create, edit, query) - Set or query whether the axis will be drawn.
        editorName: (query) - Returns the name of the editor, or an empty string if the editor has not been created yet.
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        exposure: (edit, query) - The exposure value used by the color management of the current view.
        filter: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        forceMainConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        frameImage: (create, edit, query) - Frames the image inside the window.
        frameRegion: (create, edit, query) - Frames the region inside the window.
        gamma: (edit, query) - The gamma value used by the color management of the current view.
        highlightConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        loadImage: (edit) - load an image from disk and set it as the current Editor Image
        lockMainConnection: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        mainListConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        marquee: (create, edit, query) - The arguments define the four corners of a rectangle: top left bottom right. The rectangle defines a marquee for the render computation.
        nbImages: (query) - returns the number of images
        nextViewImage: (create, edit) - The render editor has the capability to render multiple cameras within a single view. This is different from image binning where an image is saved. Multiple image views are useful for comparing two different camera renders side-by-side. The nextViewImage flag tells the editor that it should prepare its internal image storage mechanism to store to the next view location.
        outputColorManage: (edit) - When used with the writeImage flag, causes the written image to be color-managed using the outpute color space in the color preferences attached to the view.
        panel: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        pcaption: (create, edit, query) - Get or set the permanent caption which appears under the image that is currently showing in the render editor.
        realSize: (create, edit, query) - Display the image with a one to one pixel match.
        refresh: (edit) - requests a refresh of the current Editor Image.
        removeAllImages: (edit) - remove all the Editor Images from the Editor Image Stack
        removeImage: (edit) - remove the current Editor Image from the Editor Image Stack
        resetRegion: (create, edit, query) - Forces a reset of any marquee/region.
        resetViewImage: (create, edit) - The render editor has the capability to render multiple cameras within a single view. This is different from image binning where an image is saved. Multiple image views are useful for comparing two different camera renders side-by-side. The resetViewImage flag tells the editor that it should reset its internal image storage mechanism to the first image. This would happen at the very start of a render view render.
        saveImage: (edit) - save the current Editor Image to memory. Saved Editor Images are stored in an Editor Image Stack. The most recently saved image is stored in position 0, the second most recently saved image in position 1, and so on... To set the current Editor Image to a previously saved image use the "di/displayImage" flag.
        scaleBlue: (create, edit, query) - Define the scaling factor for the blue component in the View. The default value is 1 and can be between -1000 to +1000
        scaleGreen: (create, edit, query) - Define the scaling factor for the green component in the View. The default value is 1 and can be between -1000 to +1000
        scaleRed: (create, edit, query) - Define the scaling factor for the red component in the View. The default value is 1 and can be between -1000 to +1000
        selectionConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        showRegion: (create, edit, query) - Shows the current region at the given resolution. The two parameters define the width and height.
        singleBuffer: (create, edit, query) - Set the display in single buffer mode
        snapshot: (create, edit, query) - Makes a copy of the camera of the model editor at the given size. First argument is the editor name, second is the width, third is the height.
        snapshotMode: (create, edit, query) - Get or set the window's snapshot mode.
        stateString: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        stereo: (create, edit, query) - Puts the editor into stereo image mode.  The effective resolution of the output image is twice the size of the horizontal size. The orientation of the images can be set using the stereoOrientation flag.
        stereoImageOrientation: (create, edit, query) - Specifies the orientation of stereo camera renders.  The first argument specifies the orientation value for the firstleft image and the second argument specifies the orientation value for the right image. The orientation values are 'normal', the image appears as seen throught he camera, or 'mirrored', the image is mirrored horizontally.
        stereoMode: (create, edit, query) - Specifies how the image is displayed in the view.  By default the stereo is rendered with a side by side image.  The rendered image is a single image that is twice the size of a normal image, 'both'. Users can also choose to display as 'redcyan', 'redcyanlum', 'leftonly', 'rightonly', or 'stereo'.  both - displays both the left and right redcyan - displays the images as a red/cyan pair. redcyanlum - displays the luminance of the images as a red/cyan pair. leftonly - displays the left side only rightonly - displays the right side only stereo - mode that supports Crystal Eyes(tm) or Zscreen (tm) renders
        toggle: (create, edit, query) - Turns the ground plane display on/off.
        unParent: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
        viewImageCount: (create, edit, query) - The render editor has the capability to render multiple cameras within a single view. This is different from image binning where an image is saved. Multiple image views are useful for comparing two different camera renders side-by-side. The viewImageCount flag tells the editor that it should prepare its internal image storage mechanism for a given number of views.
        viewTransformName: (edit, query) - Sets/gets the view transform to be applied if color management is enabled in the current view.
        writeImage: (edit) - write the current Editor Image to disk
    """
    ...


def resolutionNode(*args, name: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., shared: bool = ..., skipSelect: bool = ...) -> Any:
    r"""
    This command creates a new node in the dependency graph of the
    specified type.
    
    The resolutionNode creates a render resolution node
    and registers it with the model.  The createNode
    command will not register nodes of this type correctly.

    Args:
        name: (create) - Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace doesn't exist, we will create the namespace.
        parent: (create) - Specifies the parent in the DAG under which the new node belongs.
        shared: (create) - This node is shared across multiple files, so only create it if it does not already exist.
        skipSelect: (create) - This node is not to be selected after creation, the original selection will be preserved.
    """
    ...


def roll(*args, absolute: bool = ..., degree: Optional[Union[float, bool]] = ..., relative: bool = ...) -> Any:
    r"""
    The roll command rotates a camera about its viewing direction, a
    positive angle produces clockwise camera rotation, while a
    negative angle produces counter-clockwise camera rotation.
    
    The default mode is relative and the rotation is applied with
    respect to the current orientation of the camera. When mode is set
    to absolute, the rotation is applied with respect to the plane
    constructed from the following three vectors in the world space:
    the world up vector, the camera view vector, and the camera up
    vector.
    
    The rotation angle is specified in degrees.
    
    The roll command can be applied to either a perspective or an
    orthographic camera.
    
    This command may be applied to more than one camera; objects that
    are not cameras are ignored. When no camera name supplied, this command
    is applied to all currently active cameras.

    Args:
        absolute: (create) - Set to absolute mode.
        degree: (create) - Set the amount of the rotation angle.
        relative: (create) - Set to relative mode.
    """
    ...


def sampleImage(*args, fastSample: bool = ..., resolution: Optional[Union[Tuple[int, str], bool]] = ...) -> Any:
    r"""
    The sampleImage command is used to control parameters of
    sample images, such as swatches in the multilister.
    The fast option turns on or off some rendering cheats which speed up the
    render but may cause edges to look ragged.
    The resolution option specifies the width in pixels of the image which will
    be rendered for the specified node. Note that the width of the image
    is also the height of the image since sample images are square.

    Args:
        fastSample: (create) - If fast but rough rendering for sampleImage is to be used
        resolution: (create) - The first argument to this flag specifies a resolution in pixels. The second argument specifies a dependency node. The effect of this flag is that further sample image renderings for the specified node will be made at the specified resolution.
    """
    ...


def setDefaultShadingGroup(*args, query: bool = ...) -> Any:
    r"""
    The setDefaultShadingGroup command is used to change which shading
    group is considered the current default shading group. Subsequently
    created objects will be assigned to the new default group.

    Args:
    """
    ...


def setRenderPassType(*args, defaultDataType: bool = ..., numChannels: Optional[Union[int, bool]] = ..., type: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This command will set the passID of a renderPass node and
    create the custom attributes specified by the corresponding render pass
    definition.  If the render pass
    node already has a passID assigned to it, attributes that are no longer
    required become hidden, and new attributes are unhidden and/or created as
    needed.  This allows passIDs to be changed back and forth without losing
    attribute data.  It also allows common attributes to be transported from one
    render pass type to another.

    Args:
        defaultDataType: (create) - If set, the render pass will use its default data type.
        numChannels: (create) - Specify the number of channels to use in the render pass. Note that this flag is only valid if there is an implementation supporting the requested number of channels.
        type: (create) - Specify the pass type to assign to the pass node(s).
    """
    ...


def shadingConnection(*args, connectionState: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Sets the connection state of a connection between nodes that are used
    in shading. Specify the destination attribute of the connection.

    Args:
        connectionState: (create, edit, query) - Specifies the state of the connection. On/True/1 means the connection is still active. Off/False/0 means the connection is inactive.
    """
    ...


def shadingNetworkCompare(*args, byName: bool = ..., byValue: bool = ..., delete: bool = ..., equivalent: bool = ..., network1: bool = ..., network2: bool = ..., upstreamOnly: bool = ..., query: bool = ...) -> Any:
    r"""
    This command allows you to compare two shading networks.

    Args:
        byName: (create) - Indicates whether the comparison should consider node names. If true, two shading networks will be considered equivalent only if the names of corresponding nodes are the same, ignoring namespaces. If false, two shading networks will be considered equivalent even if corresponding nodes are named differently. Default is 'false'.
        byValue: (create) - Indicates whether the comparison should consider the values of unconnected attributes. If true, two shading networks will be considered equivalent only if corresponding, unconnected attributes are the same type and have the same value. Only attributes of type 'int', 'bool', 'float', and 'string' will have their values compared. If false, two shading networks will be considered equivalent even if corresponding, unconnected attributes have different values or are different types. Default is 'true'.
        delete: (create) - Deletes the specified comparison from memory.
        equivalent: (query) - Returns an int. 1 if the shading networks in the specified comparison are equivalent. 0 otherwise.
        network1: (query) - Returns a string[]. Returns an empty string array if the shading networks in the specified comparison are not equivalent. Otherwise returns the nodes in the first shading network.
        network2: (query) - Returns a string[]. Returns an empty string array if the shading networks in the specified comparison are not equivalent. Otherwise returns the nodes in the second shading network.
        upstreamOnly: (create) - Indicates whether the comparison should consider nodes which are connected downstream from shading network nodes. If true, only those nodes which are upstream from the shading group will be considered. If, following only downstream connections, there is no connection path from a node to one of the shader attributes on the shading group, the node will not be considered. If false, a node will be considered if a connection path can found, following either upstream or downstream connections, which terminates with an input connection to one of the shading groups shader attributes. These dangling nodes do not directly contribute to the color, displacement, or volume characteristics of the shading group. Default is 'false'.
    """
    ...


def shadingNode(*args, asLight: bool = ..., asPostProcess: bool = ..., asRendering: bool = ..., asShader: bool = ..., asTexture: bool = ..., asUtility: bool = ..., isColorManaged: bool = ..., name: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., shared: bool = ..., skipSelect: bool = ...) -> Any:
    r"""
    This command creates a new node in the dependency graph of the
    specified type.
    
    The shadingNode command classifies any DG node as a shader, texture
    light, post process, or utility so that it can be properly organized
    in the multi-lister.  Recall that any DG node can be used a part of a
    a shader, texture or light - regardless of how it is classified by this.
    command. These classifications are provided for convenience in the UI.

    Args:
        asLight: (create) - classify the current DG node as a light
        asPostProcess: (create) - classify the current DG node as a post process
        asRendering: (create) - classify the current DG node as a rendering node
        asShader: (create) - classify the current DG node as a shader
        asTexture: (create) - classify the current DG node as a texture
        asUtility: (create) - classify the current DG node as a utility
        isColorManaged: (create) - classify the current DG node as being color managed
        name: (create) - Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace doesn't exist, we will create the namespace.
        parent: (create) - Specifies the parent in the DAG under which the new node belongs.
        shared: (create) - This node is shared across multiple files, so only create it if it does not already exist.
        skipSelect: (create) - This node is not to be selected after creation, the original selection will be preserved.
    """
    ...


def showShadingGroupAttrEditor(*args, query: bool = ...) -> Any:
    r"""
    The showShadingGroupAttrEditor command opens up the attribute
    editor for the current object's shading-group information.

    Args:
    """
    ...


def soloMaterial(*args, attr: Optional[Union[str, bool]] = ..., last: bool = ..., node: Optional[Union[str, bool]] = ..., unsolo: bool = ..., query: bool = ...) -> Any:
    r"""
    Shows a preview of a specified material node output attribute.

    Args:
        attr: (create, query) - The attr flag specifies a node attribute to solo.
        last: (create, query) - Whether to solo the last material node and attribute.
        node: (create, query) - The node flag specifies the node to solo.
        unsolo: (create, query) - Whether to remove soloing.
    """
    ...


def spotLight(*args, barnDoors: bool = ..., bottomBarnDoorAngle: Optional[Union[float, bool]] = ..., coneAngle: Optional[Union[float, bool]] = ..., decayRate: Optional[Union[int, bool]] = ..., discRadius: Optional[Union[float, bool]] = ..., dropOff: Optional[Union[float, bool]] = ..., exclusive: bool = ..., intensity: Optional[Union[float, bool]] = ..., leftBarnDoorAngle: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., penumbra: Optional[Union[float, bool]] = ..., position: Optional[Union[Tuple[float, float, float], bool]] = ..., rgb: Optional[Union[Tuple[float, float, float], bool]] = ..., rightBarnDoorAngle: Optional[Union[float, bool]] = ..., rotation: Optional[Union[Tuple[float, float, float], bool]] = ..., shadowColor: Optional[Union[Tuple[float, float, float], bool]] = ..., shadowDither: Optional[Union[float, bool]] = ..., shadowSamples: Optional[Union[int, bool]] = ..., softShadow: bool = ..., topBarnDoorAngle: Optional[Union[float, bool]] = ..., useRayTraceShadows: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    TlightCmd is the base class for other light commands.
    TnonAmbientLightCmd is a class that looks like a command but
    is not.  It is a base class for the extended/nonExtended
    lights.
    TnonExtendedLightCmd is a base class and not a real command. It is inherited by several
    lights: TpointLight, TdirectionalLight, TspotLight etc.
    The spotLight command is used to edit the parameters of
    existing spotLights, or to create new ones. The default
    behaviour is to create a new spotlight.

    Args:
        barnDoors: (create, edit, query) - Are the barn doors enabled?
        bottomBarnDoorAngle: (create, edit, query) - Angle of the bottom of the barn door.
        coneAngle: (create, edit, query) - angle of the spotLight
        decayRate: (create) - Decay rate of the light (0-no decay, 1-slow, 2-realistic, 3-fast)
        discRadius: (create, query) - Radius of shadow disc.
        dropOff: (create, edit, query) - dropOff of the spotLight
        exclusive: (create, query) - True if the light is exclusively assigned
        intensity: (create, query) - Intensity of the light
        leftBarnDoorAngle: (create, edit, query) - Angle of the left of the barn door.
        name: (create, query) - Name of the light
        penumbra: (create, edit, query) - specify penumbra region
        position: (create, query) - Position of the light
        rgb: (create, query) - RGB colour of the light
        rightBarnDoorAngle: (create, edit, query) - Angle of the right of the barn door.
        rotation: (create, query) - Rotation of the light for orientation, where applicable
        shadowColor: (create, query) - Color of the light's shadow
        shadowDither: (create, query) - Shadow dithering value.
        shadowSamples: (create, query) - Numbr of shadow samples to use
        softShadow: (create, query) - True if soft shadowing is to be enabled
        topBarnDoorAngle: (create, edit, query) - Angle of the top of the barn door.
        useRayTraceShadows: (create, query) - True if ray trace shadows are to be used
    """
    ...


def spotLightPreviewPort(*args, annotation: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., fullPathName: bool = ..., height: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., isObscured: bool = ..., manage: bool = ..., noBackground: bool = ..., numberOfPopupMenus: bool = ..., parent: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., spotLight: Optional[Union[str, bool]] = ..., statusBarMessage: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., visible: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., widthHeight: Optional[Union[Tuple[int, int], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a 3dPort that displays an image representing the
    illumination provided by the spotLight. It is a picture of a plane
    being illuminated by a light.
    
    The optional argument is the name of the 3dPort.

    Args:
        annotation: (create, edit, query) - Annotate the control with an extra string value.
        backgroundColor: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag: (create, edit, query) - Add a documentation flag to the control.  The documentation flag has a directory structure. (e.g., -dt render/multiLister/createNode/material)
        dragCallback: (create, edit) - Adds a callback that is called when the middle mouse button is pressed.  The MEL version of the callback is of the form:  global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  The proc returns a string array that is transferred to the drop site. By convention the first string in the array describes the user settable message type.  Controls that are application defined drag sources may ignore the callback. $mods allows testing for the key modifiers CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3 == CTRL + SHIFT.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def callbackName( dragControl, x, y, modifiers ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "x", "y", "modifiers".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")
        dropCallback: (create, edit) - Adds a callback that is called when a drag and drop operation is released above the drop site.  The MEL version of the callback is of the form:  global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  The proc receives a string array that is transferred from the drag source. The first string in the msgs array describes the user defined message type. Controls that are application defined drop sites may ignore the callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form:  def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  The values of these arguments are the same as those for the MEL version above.  The other way to specify the callback in Python is to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed in a dictionary with the keys "dragControl", "dropControl", "messages", "x", "y", "type".  The "dragControl" value is a string and the other values are integers (eg the callback string could be "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")
        enable: (create, edit, query) - The enable state of the control.  By default, this flag is set to true and the control is enabled.  Specify false and the control will appear dimmed or greyed-out indicating it is disabled.
        enableBackground: (create, edit, query) - Enables the background color of the control.
        enableKeyboardFocus: (create, edit, query) - If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse. This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls. If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        fullPathName: (query) - Return the full path name of the widget, which includes all the parents.
        height: (create, edit, query) - The height of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
        highlightColor: (create, edit, query) - The highlight color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0.
        isObscured: (query) - Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.
        manage: (create, edit, query) - Manage state of the control.  An unmanaged control is not visible, nor does it take up any screen real estate.  All controls are created managed by default.
        noBackground: (create, edit) - Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
        numberOfPopupMenus: (query) - Return the number of popup menus attached to this control.
        parent: (create, query) - The parent layout for this control.
        popupMenuArray: (query) - Return the names of all the popup menus attached to this control.
        preventOverride: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        spotLight: (create) - Name of the spotLight.
        statusBarMessage: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
        visible: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
        widthHeight: (create) - The width and height of the port.
    """
    ...


def stereoCameraView(*args, activeComponentsXray: bool = ..., activeCustomEnvironment: str = ..., activeCustomGeometry: Optional[Union[str, bool]] = ..., activeCustomLighSet: Optional[Union[str, bool]] = ..., activeCustomOverrideGeometry: Optional[Union[str, bool]] = ..., activeCustomRenderer: Optional[Union[str, bool]] = ..., activeOnly: bool = ..., activeShadingGraph: Optional[Union[str, bool]] = ..., activeSupported: bool = ..., activeView: bool = ..., addObjects: str = ..., addSelected: bool = ..., allObjects: bool = ..., backfaceCulling: bool = ..., bluePencil: bool = ..., bufferMode: Optional[Union[str, bool]] = ..., bumpResolution: Optional[Union[Tuple[int, int], bool]] = ..., camera: Optional[Union[str, bool]] = ..., cameraName: Optional[Union[str, bool]] = ..., cameraSet: Optional[Union[str, bool]] = ..., cameraSetup: bool = ..., cameras: bool = ..., capture: Optional[Union[str, bool]] = ..., captureSequenceNumber: Optional[Union[int, bool]] = ..., centerCamera: Optional[Union[str, bool]] = ..., colorMap: bool = ..., colorResolution: Optional[Union[Tuple[int, int], bool]] = ..., control: bool = ..., controlVertices: bool = ..., cullingOverride: Optional[Union[str, bool]] = ..., default: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., deformers: bool = ..., dimensions: bool = ..., displayAppearance: Optional[Union[str, bool]] = ..., displayLights: Optional[Union[str, bool]] = ..., displayMode: Optional[Union[str, bool]] = ..., displayTextures: bool = ..., docTag: Optional[Union[str, bool]] = ..., dynamicConstraints: bool = ..., dynamics: bool = ..., editorChanged: Optional[Union[str, bool]] = ..., exists: bool = ..., filter: Optional[Union[str, bool]] = ..., filteredObjectList: bool = ..., fluids: bool = ..., fogColor: Optional[Union[Tuple[float, float, float, float], bool]] = ..., fogDensity: Optional[Union[float, bool]] = ..., fogEnd: Optional[Union[float, bool]] = ..., fogMode: Optional[Union[str, bool]] = ..., fogSource: Optional[Union[str, bool]] = ..., fogStart: Optional[Union[float, bool]] = ..., fogging: bool = ..., follicles: bool = ..., forceMainConnection: Optional[Union[str, bool]] = ..., grid: bool = ..., hairSystems: bool = ..., handles: bool = ..., headsUpDisplay: bool = ..., height: bool = ..., highlightConnection: Optional[Union[str, bool]] = ..., hulls: bool = ..., ignorePanZoom: bool = ..., ikHandles: bool = ..., imagePlane: bool = ..., interactive: bool = ..., interactiveBackFaceCull: bool = ..., interactiveDisableShadows: bool = ..., isFiltered: bool = ..., jointXray: bool = ..., joints: bool = ..., leftCamera: Optional[Union[str, bool]] = ..., lights: bool = ..., lineWidth: Optional[Union[float, bool]] = ..., locators: bool = ..., lockMainConnection: bool = ..., lowQualityLighting: bool = ..., mainListConnection: Optional[Union[str, bool]] = ..., manipulators: bool = ..., maxConstantTransparency: Optional[Union[float, bool]] = ..., maximumNumHardwareLights: bool = ..., modelPanel: Optional[Union[str, bool]] = ..., motionTrails: bool = ..., nCloths: bool = ..., nParticles: bool = ..., nRigids: bool = ..., noUndo: bool = ..., nurbsCurves: bool = ..., nurbsSurfaces: bool = ..., objectFilter: Optional[Union[str, bool]] = ..., objectFilterList: Optional[Union[str, bool]] = ..., objectFilterListUI: Optional[Union[str, bool]] = ..., objectFilterShowInHUD: bool = ..., objectFilterUI: Optional[Union[str, bool]] = ..., occlusionCulling: bool = ..., panel: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., pivots: bool = ..., planes: bool = ..., pluginObjects: Tuple[str, bool] = ..., pluginShapes: bool = ..., polymeshes: bool = ..., queryPluginObjects: Optional[Union[str, bool]] = ..., removeSelected: bool = ..., rendererDeviceName: bool = ..., rendererList: bool = ..., rendererListUI: bool = ..., rendererName: Optional[Union[str, bool]] = ..., rendererOverrideList: bool = ..., rendererOverrideListUI: bool = ..., rendererOverrideName: Optional[Union[str, bool]] = ..., resetCustomCamera: bool = ..., rigRoot: Optional[Union[str, bool]] = ..., rightCamera: Optional[Union[str, bool]] = ..., sceneRenderFilter: Optional[Union[str, bool]] = ..., selectionConnection: Optional[Union[str, bool]] = ..., selectionHiliteDisplay: bool = ..., setSelected: bool = ..., shadingModel: Optional[Union[int, bool]] = ..., shadows: bool = ..., smallObjectCulling: bool = ..., smallObjectThreshold: Optional[Union[float, bool]] = ..., smoothWireframe: bool = ..., sortTransparent: bool = ..., stateString: bool = ..., stereoDrawMode: bool = ..., strokes: bool = ..., subdivSurfaces: bool = ..., swapEyes: bool = ..., textureAnisotropic: bool = ..., textureCompression: bool = ..., textureDisplay: Optional[Union[str, bool]] = ..., textureEnvironmentMap: bool = ..., textureHilight: bool = ..., textureMaxSize: Optional[Union[int, bool]] = ..., textureMemoryUsed: bool = ..., textureSampling: Optional[Union[int, bool]] = ..., textures: bool = ..., transpInShadows: bool = ..., transparencyAlgorithm: Optional[Union[str, bool]] = ..., twoSidedLighting: bool = ..., unParent: bool = ..., unlockMainConnection: bool = ..., updateColorMode: bool = ..., updateMainConnection: bool = ..., useBaseRenderer: bool = ..., useColorIndex: bool = ..., useCustomBackground: bool = ..., useDefaultMaterial: bool = ..., useInteractiveMode: bool = ..., useRGBImagePlane: bool = ..., useReducedRenderer: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., userNode: Optional[Union[str, bool]] = ..., viewColor: Optional[Union[Tuple[float, float, float, float], bool]] = ..., viewObjects: bool = ..., viewSelected: bool = ..., viewType: bool = ..., width: bool = ..., wireframeBackingStore: bool = ..., wireframeOnShaded: bool = ..., xray: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create, edit or query a model editor.
    
    Note that some of the flags of this command may have different settings
    for normal mode and for interactive/playback mode.  For example, a
    modelEditor can be set to use shaded mode normally, but to use wireframe
    during playback for greater speed.  Some flags also support having
    defaults set so that new model editors will be created with those settings.
    
    This is the main command for creating stereo editors. This commands
    only acts as an interface to the actual viewport. It is derived off of
    MPxModelEditorCommand. This command manages the set of stereo rig
    tools.

    Args:
        activeComponentsXray: (edit, query) - Turns on or off Xray mode for active components.
        activeCustomEnvironment: (edit) - Specifies a path to an image file to be used as environment map. It is only enabled when a valid scene render filter is specified.
        activeCustomGeometry: (edit, query) - Specifies an identifier for custom geometry to override the geometry to display. It is only enabled when a valid scene render filter is specified.
        activeCustomLighSet: (edit, query) - Specifies an identifier for the light set to use with a scene render filter. It is only enabled when a valid scene render filter is specified.
        activeCustomOverrideGeometry: (edit, query) - Specifies an identifier for an override on the custom geometry for a scene render filter.
        activeCustomRenderer: (edit, query) - Specifies an identifier for custom renderer to use when a valid scene render filter is also specified.
        activeOnly: (edit, query) - Sets whether only active objects should appear shaded in shaded display.
        activeShadingGraph: (edit, query) - Specifies the shading graph to use to override material display. Only enabled when a valid scene render filter is specified.
        activeSupported: (query) - True if the viewer is capable of drawing in active mode which takes advantage of the graphics card's built-in stereoscopic support. This includes support for shutter glasses and stereo support in clone mode.
        activeView: (edit, query) - Sets this model editor to be the active view.  Returns true if successful.  On query this flag will return whether the view is the active view.
        addObjects: (edit) - This flag causes the objects contained within the selection connection to be added to the list of objects visible in the view (if viewSelected is true).
        addSelected: (edit) - This flag causes the currently active objects to be added to the list of objects visible in the view (if viewSelected is true).
        allObjects: (edit, query) - Turn on/off the display of all objects for the view of the model editor. This excludes NURBS, CVs, hulls, grids and manipulators.
        backfaceCulling: (edit, query) - Turns on or off backface culling for the whole view.  This setting overrides the culling settings of individual objects.  All objects draw in the view will be backface culled.  When backface culling is turned on, surfaces becomes invisible in areas where the normal is pointing away from the camera.
        bluePencil: (create, edit, query) - Define whether the blue pencil should be added or not
        bufferMode: (edit, query) - Deprecated: this is not supported in Viewport 2.0.  Sets the graphic buffer mode.  Possible values are "single" or "double".
        bumpResolution: (edit, query) - Set the resolution for "baked" bump map textures when using the hardware renderer. The default value is 512, 512 respectively.
        camera: (edit, query) - Change or query the name of the camera in model editor.
        cameraName: (create, edit) - Set the name of the panel's camera transform and shape. The shape name is computed by appending the string "Shape" to the transform name. This flag may not be queried.
        cameraSet: (create, edit, query) - Name of the camera set
        cameraSetup: (query) - Based on the model editor name passed in will returns a string list containing camera setups. A camera setup can contain one or more cameras which are associated with each other. Camera setups are defined as pairs of consecutive strings in the list. Each pair is comprised of: a string which identifies an active camera, and a string which defines a script to set up a given active camera. As many pairs of strings can be returned as the number of active cameras. If nothing is returned then it is assumed that no set up is required to activate a given camera.
        cameras: (edit, query) - Turn on/off the display of cameras for the view of the model editor.
        capture: (edit, query) - Perform an one-time capture of the viewport to the named image file on disk.
        captureSequenceNumber: (edit, query) - When a number greater or equal to 0 is specified each subsequent refresh will save an image file to disk if the capture flag has been enabled.  The naming of the file is:  {root name}.#.{extension}  if the name {root name}.{extension} is used for the capture flag argument.  The value of # starts at the number specified to for this argument and increments for each subsequent refresh.  Sequence capture can be disabled by specifying a number less than 0 or an empty file name for the capture flag.
        centerCamera: (query) - Only available in query mode: returns the current center camera of this view.
        colorMap: (query) - Queries the color map style for the model panel. Possible values are "colorIndex" and "rgb".
        colorResolution: (edit, query) - Set the resolution for "baked" color textures when using the hardware renderer. The default value is 256, 256 respectively.
        control: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        controlVertices: (edit, query) - Turn on/off the display of NURBS CVs for the view of the model editor.
        cullingOverride: (edit, query) - Set whether to override the culling attributes on objects when using the hardware renderer. The options are:  "none" : Use the culling object attributes per object. "doubleSided" : Force all objects to be double sided. "singleSided": Force all objects to be single sided.  The default value is "none".
        default: (edit, query) - Causes this command to modify the default value of this setting. Newly created model editors will inherit the values.  This flag may be used with the -interactive to set default interactive settings.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        deformers: (edit, query) - Turn on/off the display of deformer objects for the view of the model editor.
        dimensions: (edit, query) - Turn on/off the display of dimension objects for the view of the model editor.
        displayAppearance: (edit, query) - Sets the display appearance of the model panel.  Possible values are "wireframe", "points", "boundingBox", "smoothShaded", "flatShaded".  This flag may be used with the -interactive and -default flags.  Note that only "wireframe", "points", and "boundingBox" are valid for the interactive mode.
        displayLights: (edit, query) - Sets the lighting for shaded mode.  Possible values are "selected", "active", "all", "default", "none".
        displayMode: (create, edit, query) - Defines the display mode for this view. Some modes are available only for certain types of graphics hardware. Valid values are:  active: uses the graphics card's built-in stereoscopic mode is available leftEye: displays only the view from the left camera. rightEye: displays only the view from the rigth camera. centerEye: displays only the view from the center camera. anaglyph: displays both left and right cameras, filtered using red and blue anaglyphLum: same as anaglyph, except the luminance is computed before the red and blue filtering interlace: displays an interlaced view of left and right cameras checkerboard: Same as interlace, except a checkerboard pattern is used to mix both images freeview: displays both left and right images, half size next to each other freeviewX: same as freeview, except left and right cameras are swapped
        displayTextures: (edit, query) - Turns on or off display of textures in shaded mode
        docTag: (create, edit, query) - Attaches a tag to the editor.
        dynamicConstraints: (edit, query) - Turn on/off the display of dynamicConstraints for the view of the model editor.
        dynamics: (edit, query) - Turn on/off the display of dynamics objects for the view of the model editor.
        editorChanged: (create, edit, query) - An optional script callback which is called when the editors options have changed.  This is useful in a situation where a scripted panel contains a modelEditor and wants to be notified when the contained editor changes its options.
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        filter: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        filteredObjectList: (query) - For model editors with filtering on (either using an object filter, or isolate select), this flag returns a string list of the objects which are displayed in this editor. Note that this list does not take into account visibility (based on camera frustum or flags), it purely captures the objects which are considered when rendering the view.
        fluids: (edit, query) - Turn on/off the display of fluids for the view of the model editor.
        fogColor: (edit, query) - The color used for hardware fogging.
        fogDensity: (edit, query) - Determines the density of hardware fogging.
        fogEnd: (edit, query) - The end location of hardware fogging.
        fogMode: (edit, query) - This determines the drop-off mode for fog. The possibilities are:  "linear" : linear drop-off "exponent" : exponential drop-off "exponent2" : squared exponential drop-off
        fogSource: (edit, query) - Set the type of fog algorithm to use. If the argument is "fragment" (default) then fog is computed per pixel. If the argument is "coordinate" then if the geometry has specified vertex fog coordinates, and the OpenGL extension for vertex fog is supported by the graphics system, then fog is computed per vertex.
        fogStart: (edit, query) - The start location of hardware fogging.
        fogging: (edit, query) - Set whether hardware fogging is enabled or not.
        follicles: (edit, query) - Turn on/off the display of follicles for the view of the model editor.
        forceMainConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        grid: (edit, query) - Turn on/off the display of the grid for the view of the model editor.
        hairSystems: (edit, query) - Turn on/off the display of hairSystems for the view of the model editor.
        handles: (edit, query) - Turn on/off the display of select handles for the view of the model editor.
        headsUpDisplay: (edit, query) - Sets whether the model panel will draw any enabled heads up display	elements in this window (if true).  Currently this requires the HUD elements to be globally enabled.
        height: (query) - Return the height of the associated viewport in pixels
        highlightConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        hulls: (edit, query) - Turn on/off the display of NURBS hulls for the view of the model editor.
        ignorePanZoom: (edit, query) - Sets whether the model panel will ignore the 2D pan/zoom value to give an overview of the scene.
        ikHandles: (edit, query) - Turn on/off the display of ik handles and end effectors for the view of the model editor.
        imagePlane: (edit, query) - Turn on/off the display of image plane for the view
        interactive: (edit, query) - Causes this command to modify the interactive refresh settings of the view.  In this way it is possible to change the behavior of the model editor during playback for improved performance.
        interactiveBackFaceCull: (create, edit, query) - Define whether interactive backface culling should be on or not
        interactiveDisableShadows: (create, edit, query) - Define whether interactive shadows should be disabled or not
        isFiltered: (query) - Returns true for model editors with filtering applied to their view of the scene. This could either be an explicit object filter, or a display option such as isolate select which filters the objects that are displayed.
        jointXray: (edit, query) - Turns on or off Xray mode for joints.
        joints: (edit, query) - Turn on/off the display of joints for the view of the model editor.
        leftCamera: (query) - Only available in query mode: returns the current left camera of this view.
        lights: (edit, query) - Turn on/off the display of lights for the view of the model editor.
        lineWidth: (edit, query) - Set width of lines for display
        locators: (edit, query) - Turn on/off the display of locator objects for the view of the model editor.
        lockMainConnection: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        lowQualityLighting: (edit, query) - Set whether to use "low quality lighting" when using the hardware renderer. The default value is false.
        mainListConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        manipulators: (edit, query) - Turn on/off the display of manipulator objects for the view of the model editor.
        maxConstantTransparency: (edit, query) - Sets the maximum constant transparency.  Setting this value remaps constant transparency values from the range [0.0, 1.0] to the range [0.0, maxConstantTransparency]. All transparency values are shifted linearly to the new range, so a fully transparency object (transparency 1.0) would appear with a transparency of maxConstantTransparency in the viewport, allowing highly transparent objects to be made visible.  This flag only affects constant (non-textured) transparent objects.
        maximumNumHardwareLights: (create, edit, query) - Define whether the hardware light maximum should be respected or not
        modelPanel: (create) - Allows the created model editor to be embedded in the named model panel. Intended for use with custom model editors created via the API (i.e. the flag would be used on the derived MPxModelEditorCommand), though the flag may also be used on the base modelEditor command to restore a default Maya model editor to the panel. Note that the model editor previously owned by the panel is deleted.
        motionTrails: (edit, query) - Turn on/off the Motion Trail display in the Viewport.
        nCloths: (edit, query) - Turn on/off the display of nCloths for the view of the model editor.
        nParticles: (edit, query) - Turn on/off the display of nParticles for the view of the model editor.
        nRigids: (edit, query) - Turn on/off the display of nRigids for the view of the model editor.
        noUndo: (edit) - This flag prevents some viewport operations (such as isolate select) from being added to the undo queue.
        nurbsCurves: (edit, query) - Turn on/off the display of nurbs curves for the view of the model editor.
        nurbsSurfaces: (edit, query) - Turn on/off the display of nurbs surfaces for the view of the model editor.
        objectFilter: (edit, query) - Set or query the current object filter name. An object filter is required to have already been registered.
        objectFilterList: (query) - Return a list of names of registered filters.
        objectFilterListUI: (query) - Return a list of UI names of registered filters.
        objectFilterShowInHUD: (edit, query) - Sets whether or not to display the object filter UI name in the heads up display when an object filter is active. This string is concatenated with the camera name.
        objectFilterUI: (query) - Query the current object filter UI name. The object filter is required to have already been registered.
        occlusionCulling: (edit, query) - Set whether to enable occlusion culling testing when using the hardware renderer. The default value is false.
        panel: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        pivots: (edit, query) - Turn on/off the display of transform pivots for the view of the model editor.
        planes: (edit, query) - Turn on/off the display of sketch planes for the view of the model editor.
        pluginObjects: (edit, multiuse) - Turn on/off the display of plug-in objects for the view. It depends on the plug-in implementation whether to respect this flag.
        pluginShapes: (edit) - Turn on/off the display of plug-in shapes for the view. It depends on the plug-in implementation whether to respect this flag.
        polymeshes: (edit, query) - Turn on/off the display of polygon meshes for the view of the model editor.
        queryPluginObjects: (query) - Query the on/off state of plug-in objects display for the view. To set the on/off state, use -pluginObjects instead.
        removeSelected: (edit) - This flag causes the currently active objects to be removed from the list of objects visible in the view (if viewSelected is true).
        rendererDeviceName: (query) - Query for the name of the draw API used by the Viewport 2.0 renderer for a 3d modeling viewport. The possible return values are "VirtualDeviceGL" if Maya is set to use "OpenGL - Legacy" for Viewport 2.0, "VirtualDeviceGLCore" if Maya is set to use "OpenGL - Core Profile" (either Compatibility or Strict) for Viewport 2.0, or "VirtualDeviceDx11" if Maya is set to use DirectX for Viewport 2.0. If the renderer for the 3d modeling viewport is not Viewport 2.0, an empty string will be returned.
        rendererList: (query) - Query for a list of the internal names for renderers available for use with the 3d modeling viewport. The default list contains at least "vp2Renderer", if supported. See rendererName for more details on these renderers. Any plug-in viewport renderers will also appear in this list.
        rendererListUI: (query) - Query for a list of the UI names for renderers available for use with the 3d modeling viewport. The default list consists of the UI name for "vp2Renderer", if it is supported. Any plug-in viewport renderer's UI names will also appear in this list. This list and the list returned from rendererList have a 1:1 correspondance.
        rendererName: (edit, query) - Set or get the renderer used for a 3d modeling viewport. The name provided should be an internal name of a renderer. The 'rendererList' flag can be used to query for a list of available names. The default renderer is "vp2Renderer": Viewport 2.0.
        rendererOverrideList: (query) - Query for a list of the internal names for renderer overrides for a 3d viewport renderer. Currently only the "Viewport 2" renderer supports renderer overrides.
        rendererOverrideListUI: (query) - Query for a list of the UI names for renderer overrides for a 3d viewport renderer. Currently only the "Viewport 2" renderer supports renderer overrides.
        rendererOverrideName: (edit, query) - Set or get the override used for a 3d viewport renderer. The name provided should be the internal name for an override.  The 'rendererOverrideList' flag can be used to query for a list of available names. Currently only the "Viewport 2" renderer  supports renderer overrides. Setting an empty string will unset any currently active override.
        resetCustomCamera: (edit) - When specified will reset the camera transform for the active custom camera used for a scene render filter. It is only enabled when a valid scene render filter is specified.
        rigRoot: (create, edit, query) - Defines the rig root associated with this view.
        rightCamera: (query) - Only available in query mode: returns the current right camera of this view.
        sceneRenderFilter: (edit, query) - Specifies the name of a scene render filter
        selectionConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        selectionHiliteDisplay: (edit, query) - Sets whether the model panel will draw any selection hiliting on the objects in this window.
        setSelected: (edit) - This flag causes the currently active objects to be the only objects visible in the view (if viewSelected is true).
        shadingModel: (create, edit, query) - Shading model to use
        shadows: (edit, query) - Turn on/off the display of hardware shadows in shaded mode.
        smallObjectCulling: (create, edit, query) - Define whether small object culling should be enabled or not
        smallObjectThreshold: (create, edit, query) - Threshold used for small object culling
        smoothWireframe: (edit, query) - Turns on or off smoothing of wireframe lines and points
        sortTransparent: (edit, query) - This flag turns on/off sorting of transparent objects during shaded mode refresh. Normally, objects are sorted according to their origin in camera space but when this flag is turned off they will be drawn according to their (depth-first traversal) order in the scene graph. This is a global flag that affects all model editors.
        stateString: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        stereoDrawMode: (create, edit, query) - If this flag is used then set stereo draw mode
        strokes: (edit, query) - Turn on/off the display of Paint Effects strokes for the view
        subdivSurfaces: (edit, query) - Turn on/off the display of subdivision surfaces for the view of the model editor.
        swapEyes: (create, edit, query) - Swap the display of the left and right cameras. The left camera becomes the right draw pass and the right camera becomes the left draw pass. This flag is intended for advanced users, for situations where the hardware uses the opposite left/right convention.
        textureAnisotropic: (edit, query) - Set whether to perform anisotropic texture filtering. Will work only if the anisotropic texture filtering extension is supported in OpenGL on the graphics system.
        textureCompression: (create, edit, query) - Defines whether texture compression should be used or not
        textureDisplay: (edit, query) - Set the type of blending to use for textures. The blend is performed between the destination fragment and the texture fragment. The source is usually the material color. Argument options are: "modulate" : multiply the destination and texture fragment "decal" : overwrite the destination with the texture fragment
        textureEnvironmentMap: (create, edit, query) - If true then use a texture environment map
        textureHilight: (edit, query) - Set whether to show specular hilighting when the display is in shaded textured mode.
        textureMaxSize: (edit, query) - Set maximum texture size for hardware texturing.  The integer value must be a power of 2.  Recommended values are 128 or 256.  If the value specified is larger than the OpenGL maximim textures size for the graphics hardware it will be clamped to the OpenGL size.  If many large textures are used in a scene reducing this value improves performance.  On Impact texture memory is pinned in RAM so using large textures can cause reliability and performance problems. Again reducing this value will help. Software rendering does not use this value. This flag is obsolete as of Maya 6.5. The maxTextureResolution/mtr argument on the displayPref command should be used instead.
        textureMemoryUsed: (query) - Returns the total number of bytes used by all texture maps.  This is typicly width*height*channels for all texture objects in the scene If the texture is mip mapped all mip map levels are included in the total though not never more than two level will be in use at one time
        textureSampling: (edit, query) - Set the type of sampling to be used for texture display. The argument can be either:  1 : means to perform point sample 2 : means to perform bilinear interpolation (default)
        textures: (edit, query) - Turn on/off the display of texture objects for the view
        transpInShadows: (edit, query) - Set whether to enable display of transparency in shadows when using the hardware renderer. The default value is false.
        transparencyAlgorithm: (edit, query) - Set the transparency algorithm. The options are:  1) "frontAndBackCull" : Two pass front and back culling technique. 2) "perPolygonSort" : Draw transparent polygons in back-to-front order technique.  transparency pptions 1) and 2) are supported by the hardware renderer. Options 1) is supported by the interactive modeling viewports. The default value is "frontAndBackCull".
        twoSidedLighting: (edit, query) - Turns on or off two sided lighting.  This may be used with the -default flag.
        unParent: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateColorMode: (edit) - Using this flag tells the model panel to check which color mode it should be in, and to switch accordingly.  This flag may be used to update a model panel after a camera image plane has been added or removed.
        updateMainConnection: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useBaseRenderer: (edit, query) - Set whether to use the "base" renderer when using the hardware renderer and in "interactive display mode" (-useInteractiveMode) The default value is false.
        useColorIndex: (edit, query) - Sets whether the model panel will attempt to use color index mode when possible.  Color index mode can provide a performance increase for point, bounding box, and wireframe display modes. This may be used with the -default flag.
        useCustomBackground: (create, edit, query) - When set to true, instead of using the standard background, draw a solid background using the viewColor.
        useDefaultMaterial: (edit, query) - Sets whether the model panel will draw all the shaded surfaces using the default material as opposed to using the material(s) currently assigned to the surfaces.
        useInteractiveMode: (edit, query) - Turns on or off the use of the special interaction settings during playback.  This flag may be used with the -default flag.
        useRGBImagePlane: (edit, query) - Sets whether the model panel will be forced into RGB mode when there is an image plane attached to the panel's camera.
        useReducedRenderer: (create, edit, query) - Set true if using the reduced renderer
        useTemplate: (create) - Forces the command to use a command template other than the current one.
        userNode: (edit, query) - Allows the user to associate a node name with the modelEditor. The value is automatically updated in the event the node is deleted or renamed.
        viewColor: (create, edit, query) - Specifies the background color for the stereoscopic model editor. The default value is black which provides optimal stereoscopic viewing. This only applies if 'useCustomBackground' is on (which is the default).
        viewObjects: (query) - Returns the name (if any) of the objectSet which contains the list of objects visible in the view if viewSelected is true and the list of objects being displayed does not come from the active list.
        viewSelected: (edit, query) - This flag turns on/off viewing of selected objects. When the flag is set to true, the currently active objects are captured and used as the list of objects to view.
        viewType: (query) - Returns a string indicating the type of the model editor. For the default model editor, returns the empty string. For custom model editor types created via the API, returns the same string as is returned via the method MPx3dModelView::viewType().
        width: (query) - Return the width of the associated viewport in pixels.
        wireframeBackingStore: (edit, query) - Sets whether a backing store is used to optimization the drawing of active objects. This mode can provide a performance increase in wireframe mode for certain scenes.
        wireframeOnShaded: (edit, query) - Sets whether the model panel will draw the wireframe on all shaded objects (if true) or only for active objects (if false).
        xray: (edit, query) - Turns on or off Xray mode.  This may be used with the -default flag.
    """
    ...


def stereoRigManager(*args, addRig: Optional[Union[Tuple[str, str, str], bool]] = ..., cameraSetFunc: Optional[Union[Tuple[str, str], bool]] = ..., creationProcedure: Optional[Union[Tuple[str, str], bool]] = ..., defaultRig: Optional[Union[str, bool]] = ..., delete: Optional[Union[str, bool]] = ..., language: Optional[Union[Tuple[str, str], bool]] = ..., listRigs: bool = ..., rigDefinition: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command manages the set of stereo rig tools.

    Args:
        addRig: (create) - Adds a new stereo rig definition. This flag takes 3 arguments: name, language, create:  name: A unique name for the rig type. lang: The language used for the callback. Valid values are "Python" and "MEL". Use the Python interface when possible. create: Procedure used to create a new rig of this type. This procedure takes no argument, and must return an array of strings. The first element is the root DAG node of the rig. The second and third elements are respectively the left and right cameras.
        cameraSetFunc: (create) - Specifies the function to call when a rig is about to be added to a camera set. This function must be the same language as originally defined by the tool.
        creationProcedure: (create) - Changes the creation procedure of an existing rig definition.  This flag takes 2 arguments: the name of the existing rig definition and the procedure.
        defaultRig: (create, query) - Sets the default rig tool. The argument must be the name of one of the rigs added using the add flag.  Returns True if the default could be set, False otherwise.
        delete: (create) - Removes the definition of a stereo rig. The argument must be the name of one of the rigs added using the add flag.
        language: (create) - Changes the language of an existing rig definition. Valid values are "Python" and "MEL".  This flag takes 2 arguments: the name of the existing rig definition and the language keyword.
        listRigs: (create) - When present, returns the list of all defined rigs. All other flags are ignored.
        rigDefinition: (create) - Returns the definition of a rig, in the same format as the add flag. A string array containing lang, create cameraSet.  If an empty string is passed as the argument, then the default rig is used.
    """
    ...


def surfaceSampler(*args, camera: Optional[Union[str, bool]] = ..., fileFormat: Optional[Union[str, bool]] = ..., filename: Optional[Union[str, bool]] = ..., filterSize: Optional[Union[float, bool]] = ..., filterType: Optional[Union[int, bool]] = ..., flipU: bool = ..., flipV: bool = ..., ignoreMirroredFaces: bool = ..., ignoreTransforms: bool = ..., mapHeight: Optional[Union[int, bool]] = ..., mapMaterials: bool = ..., mapOutput: Optional[Union[str, bool]] = ..., mapSpace: Optional[Union[str, bool]] = ..., mapWidth: Optional[Union[int, bool]] = ..., maxSearchDistance: Optional[Union[float, bool]] = ..., maximumValue: Optional[Union[float, bool]] = ..., overscan: Optional[Union[int, bool]] = ..., searchCage: Optional[Union[str, bool]] = ..., searchMethod: Optional[Union[int, bool]] = ..., searchOffset: Optional[Union[float, bool]] = ..., shadows: bool = ..., source: Optional[Union[str, bool]] = ..., sourceUVSpace: Optional[Union[str, bool]] = ..., superSampling: Optional[Union[int, bool]] = ..., target: Optional[Union[str, bool]] = ..., targetUVSpace: Optional[Union[str, bool]] = ..., useGeometryNormals: bool = ..., uvSet: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Maps surface detail from a source surface to a new texture map on a target
    surface. Both objects must be selected when the command is invoked, with
    the source surface selected first, and the target last.

    Args:
        camera: (create) - Specify the camera to use for camera specific lighting calculations such as specular highlights or reflections.
        fileFormat: (create, multiuse) - The image format as a file extension (e.g. "dds"). This must be included once for every output map specified.
        filename: (create, multiuse) - The filename to use when creating the map. This must be included once for every output map specified.
        filterSize: (create) - The filter size to use in pixels. Larger values (e.g. over 2.0) will produce smoother/softer results, while values closer to 1.0 will produce sharper results.
        filterType: (create) - The filter type to use. 0 is a Guassian filter, 1 is a triangular filter, 2 is a box filter.
        flipU: (create) - Flip the U coordinate of the generated image.
        flipV: (create) - Flip the V coordinate of the generated image.
        ignoreMirroredFaces: (create) - Stops reverse wound (i.e. mirrored) faces from contributing to the map generation.
        ignoreTransforms: (create) - Controls whether transforms are used (meaning the search is performed in worldspace), or not (meaning the search is performed in object space).
        mapHeight: (create, multiuse) - Pixel width of the generated map. This must be included once for every output map specified.
        mapMaterials: (create, multiuse) - Where appropriate (e.g. normal maps), this controls whether the material should be included when sampling the map attribute. This must be included once for every output map specified.
        mapOutput: (create, multiuse) - Specifies a new output map to create. One of "normal", "displacement" "diffuseRGB", "litAndShadedRGB", or "alpha"
        mapSpace: (create, multiuse) - The space to generate the map in. Valid keyword is "object". Default is tangent space. This must be included once for every output map specified.
        mapWidth: (create, multiuse) - Pixel width of the generated map. Some output image formats require even or power of 2. This must be included once for every output map specified.
        maxSearchDistance: (create, multiuse) - Controls the maximum distance away from a target surface that will be searched for source surfaces. A value of 0 indicates no limit. When generated maps include artifacts from the "other side" of an object, try setting this value to a distance approximately equal to the radius of the object. If this flag is included, it must be included once for every target.
        maximumValue: (create, multiuse) - The maximum value to include in the map. This allows control of how floating point values (like displacement) are quantised into integer image formats.
        overscan: (create) - The number of additional pixels to render around UV borders. This will help to minimise texel filtering artifacts on UV seams. When mipmaps are going to be generated for the texture a higher value may be necessary (in addition to a filterSize greater than 1).
        searchCage: (create, multiuse) - Specifies a search envelope surface to use as a search guide when looking for source surfaces. If this flag is included, it must be included once for every target.
        searchMethod: (create) - Controls the search method used to match sample points on a target surface to points on the sources. 0 is closest to envelope, 1 is prefer any intersection inside envelope to intersections outside it, and 2 is only use intersections inside envelope.
        searchOffset: (create, multiuse) - Specifies a fixed offset from a target surface to use as the starting point when looking for source surfaces. This value is only used when no search cage is specified for a given target. If this flag is included, it must be included once for every target.
        shadows: (create, multiuse) - Where appropriate (e.g. lit and shaded), this controls whether shadows are included in the calculation. Currently only depth map shadows are supported.
        source: (create, multiuse) - Specifies a surface to use as a sampling source
        sourceUVSpace: (create, multiuse) - Specifies that the transfer of data between the surfaces should be done in UV space and specifies the name of the UV set on the source surface(s) that should be used as the transfer space.
        superSampling: (create) - Controls the number of sampling points calculated for each output value. The algorithm will use 2 ^ n squared samples for each point (so a value of 0 will use a single sample, while a value of 3 will calculate 64 samples for each point).
        target: (create, multiuse) - Specified a surface to sample output information for.
        targetUVSpace: (create, multiuse) - Specifies that the transfer of data between the surfaces should be done in UV space and specifies the name of the UV set on the target surface(s) that should be used as the transfer space.
        useGeometryNormals: (create) - Controls whether geometry or surface normals are used for surface searching. Using geometry normals will ensure a smooth mapping but can introduce distorted mappings where there are large distances between the source and target surfaces. Surface normals can introduce overlapping or discontinuous mappings, but does allow map distortion to be influenced by surface normal direction.
        uvSet: (create, multiuse) - The name of the UV set to use when creating output maps. If this flag is included, it must be included once for every target.
    """
    ...


def surfaceShaderList(*args, add: Optional[Union[str, bool]] = ..., remove: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Add/Remove a relationship between an object and the
    current shading group.

    Args:
        add: (create) - add object(s) to shader group list.
        remove: (create) - remove object(s) to shader group list.
    """
    ...


def swatchRefresh(*args) -> Any:
    r"""
    The swatchRefresh command causes image source node swatches to be
    refreshed on screen.  The purpose of this command is to provide a mechanism
    to trigger a swatch refresh in cases that are not subject to dirty propagation
    in the dependency graph.  This command only works with imageSource-derived
    node types. Invoking this command with no arguments will cause all imageSource
    swatches to be refreshed.

    Args:
    """
    ...


def textureWindow(*args, activeSelectionOnTop: bool = ..., axesColor: Optional[Union[Tuple[float, float, float], bool]] = ..., backFacingColor: Optional[Union[Tuple[float, float, float, float], bool]] = ..., capture: str = ..., captureSequenceNumber: int = ..., changeCommand: Optional[Union[Tuple[str, str, str, str], bool]] = ..., checkerColor1: Optional[Union[Tuple[float, float, float], bool]] = ..., checkerColor2: Optional[Union[Tuple[float, float, float], bool]] = ..., checkerColorMode: Optional[Union[int, bool]] = ..., checkerDensity: Optional[Union[int, bool]] = ..., checkerDrawTileLabels: bool = ..., checkerGradient1: Optional[Union[Tuple[float, float, float], bool]] = ..., checkerGradient2: Optional[Union[Tuple[float, float, float], bool]] = ..., checkerGradientOverlay: bool = ..., checkerTileLabelColor: Optional[Union[Tuple[float, float, float], bool]] = ..., clearImage: bool = ..., cmEnabled: bool = ..., control: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., displayAxes: bool = ..., displayCheckered: bool = ..., displayDistortion: bool = ..., displayDivisionLines: bool = ..., displayGridLines: bool = ..., displayImage: Optional[Union[int, bool]] = ..., displayIsolateSelectHUD: bool = ..., displayLabels: bool = ..., displayOverlappingUVCountHUD: bool = ..., displayPreselection: bool = ..., displayReversedUVCountHUD: bool = ..., displaySolidMap: bool = ..., displayStyle: Optional[Union[str, bool]] = ..., displayTextureBorder: bool = ..., displayUVPositionHUD: bool = ..., displayUVShellCountHUD: bool = ..., displayUVStatisticsHUD: bool = ..., displayUsedPercentageHUD: bool = ..., distortionAlpha: Optional[Union[float, bool]] = ..., distortionPerObject: bool = ..., divisions: Optional[Union[int, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., doubleBuffer: bool = ..., drawAxis: bool = ..., drawSubregions: bool = ..., exists: bool = ..., exposure: Optional[Union[float, bool]] = ..., filter: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., forceRebake: bool = ..., frameAll: bool = ..., frameSelected: bool = ..., frontFacingColor: Optional[Union[Tuple[float, float, float, float], bool]] = ..., gamma: Optional[Union[float, bool]] = ..., gridLinesColor: Optional[Union[Tuple[float, float, float], bool]] = ..., gridNumbersColor: Optional[Union[Tuple[float, float, float], bool]] = ..., highlightConnection: Optional[Union[str, bool]] = ..., imageBaseColor: Optional[Union[Tuple[float, float, float], bool]] = ..., imageDim: bool = ..., imageDisplay: bool = ..., imageNames: bool = ..., imageNumber: Optional[Union[int, bool]] = ..., imagePixelSnap: bool = ..., imageRatio: bool = ..., imageRatioValue: Optional[Union[float, bool]] = ..., imageSize: bool = ..., imageTileRange: Optional[Union[Tuple[float, float, float, float], bool]] = ..., imageUnfiltered: bool = ..., internalFaces: bool = ..., labelPosition: Optional[Union[str, bool]] = ..., loadImage: str = ..., lockMainConnection: bool = ..., mainListConnection: Optional[Union[str, bool]] = ..., maxResolution: Optional[Union[int, bool]] = ..., multiColorAlpha: Optional[Union[float, bool]] = ..., nbImages: bool = ..., nextView: bool = ..., numUvSets: bool = ..., numberOfImages: Optional[Union[int, bool]] = ..., numberOfTextures: Optional[Union[int, bool]] = ..., panel: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., previousView: bool = ..., realSize: bool = ..., refresh: bool = ..., relatedFaces: bool = ..., removeAllImages: bool = ..., removeImage: bool = ..., rendererString: Optional[Union[str, bool]] = ..., reset: bool = ..., saveImage: bool = ..., scaleBlue: Optional[Union[float, bool]] = ..., scaleGreen: Optional[Union[float, bool]] = ..., scaleRed: Optional[Union[float, bool]] = ..., selectInternalFaces: bool = ..., selectRelatedFaces: bool = ..., selectionConnection: Optional[Union[str, bool]] = ..., setUvSet: Optional[Union[int, bool]] = ..., singleBuffer: bool = ..., size: Optional[Union[float, bool]] = ..., solidMap3dView: bool = ..., solidMapColorSeed: Optional[Union[int, bool]] = ..., solidMapPerShell: bool = ..., spacing: Optional[Union[float, bool]] = ..., stateString: bool = ..., style: Optional[Union[int, bool]] = ..., subdivisionLinesColor: Optional[Union[Tuple[float, float, float], bool]] = ..., textureBorder3dView: bool = ..., textureBorderColor: Optional[Union[Tuple[float, float, float], bool]] = ..., textureBorderWidth: Optional[Union[int, bool]] = ..., textureNames: bool = ..., textureNumber: Optional[Union[int, bool]] = ..., tileLabels: bool = ..., tileLinesColor: Optional[Union[Tuple[float, float, float], bool]] = ..., toggle: bool = ..., toggleExposure: bool = ..., toggleGamma: bool = ..., unParent: bool = ..., unlockMainConnection: bool = ..., updateMainConnection: bool = ..., useFaceGroup: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., usedPercentageHUDRange: Optional[Union[Tuple[float, float, float, float], bool]] = ..., uvSets: bool = ..., viewPortImage: bool = ..., viewTransformName: Optional[Union[str, bool]] = ..., wireframeComponentColor: Optional[Union[Tuple[float, float, float, float], bool]] = ..., wireframeObjectColor: Optional[Union[Tuple[float, float, float, float], bool]] = ..., writeImage: str = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to create a UV Editor and to query or edit
    the texture editor settings.
    
    The UV Editor displays texture mapped polygon objects in 2D
    texture space. Only active objects are visible in this window.
    
    The UV Editor has the ability to display two types of images. The
    Texture Image is a visualisation of the current texture and associated
    placement parameters. The Editor Image is a user specified image loaded
    from disk.
    
    A UV Editor can be invoked by selecting the "Window -> UV
    Texture Editor..." menu item from the main maya menu listing that
    appears at the top of the maya window. It can also be invoked by
    selecting the "Panel -> UV Editor" item under the "Panels"
    menu item that appears at the top right hand corner of the view.
    
    As a UV Editor typically exists at start-up time, and as only
    one of these can exist at any given time, this command is normally
    used to query and edit the editor settings.

    Args:
        activeSelectionOnTop: (create, edit, query) - Display the solid map / distortion of active selection on top of others.
        axesColor: (create, edit, query) - The color of axes, default is 0.0 0.0 1.0
        backFacingColor: (create, edit, query) - Sets or queries the RGBA back facing color.
        capture: (edit) - Perform an one-time capture of the viewport to the named image file on disk.
        captureSequenceNumber: (edit) - When a number greater or equal to 0 is specified each subsequent refresh will save an image file to disk if the capture flag has been enabled.  The naming of the file is:  {root name}.#.{extension}  if the name {root name}.{extension} is used for the capture flag argument. The value of # starts at the number specified to for this argument and increments for each subsequent refresh.  Sequence capture can be disabled by specifying a number less than 0 or an empty file name for the capture flag.
        changeCommand: (create, edit, query) - Parameters:  First string: command Second string: editorName Third string: editorCmd Fourth string: updateFunc   Call the command when something changes in the editor The command should have this prototype :  command(string $editor, string $editorCmd, string $updateFunc, int $reason)  The possible reasons could be :  0: no particular reason 1: scale color 2: buffer (single/double) 3: axis  4: image displayed 5: image saved in memory
        checkerColor1: (create, edit, query) - Sets the first color of the checker and identification pattern, when color mode is 2-colors.
        checkerColor2: (create, edit, query) - Sets the second color of the checker and identification pattern, when color mode is 2-colors.
        checkerColorMode: (create, edit, query) - Sets the color mode of the checker and identification pattern. 0: multi-colors; 1: 2-colors;
        checkerDensity: (create, edit, query) - Sets the density of the checker and identification pattern.
        checkerDrawTileLabels: (create, edit, query) - Toggles the checker tile label display.
        checkerGradient1: (create, edit, query) - Sets the first gradient of the checker and identification pattern, when color mode is 2-colors.
        checkerGradient2: (create, edit, query) - Sets the second gradient of the checker and identification pattern, when color mode is 2-colors.
        checkerGradientOverlay: (create, edit, query) - Toggle application of the gradient.
        checkerTileLabelColor: (create, edit, query) - Sets the checker tile label color.
        clearImage: (edit) - Clears the current Editor Image.
        cmEnabled: (edit, query) - Turn on or off applying color management in the editor.  If set, the color management configuration set in the current editor is used.
        control: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        displayAxes: (edit, query) - Specify true to display the grid axes.
        displayCheckered: (create, edit, query) - Display a unique checker and identification pattern for each UV tiles.
        displayDistortion: (create, edit, query) - Display the layout in shaded colors to indentify areas with stretched/squashed UVs
        displayDivisionLines: (edit, query) - Specify true to display the subdivision lines between grid lines.
        displayGridLines: (edit, query) - Specify true to display the grid lines.
        displayImage: (edit, query) - Set a particular image in the Editor Image Stack as the current Editor Image. Images are added to the Editor Image Stack using the "si/saveImage" flag.
        displayIsolateSelectHUD: (create, edit, query) - Show heads-up display of isolate selection
        displayLabels: (edit, query) - Specify true to display the grid line numeric labels.
        displayOverlappingUVCountHUD: (create, edit, query) - Show heads-up display of overlapping UV count, as a part UV Statistics HUD
        displayPreselection: (create, edit, query) - Toggles the pre-selection display.
        displayReversedUVCountHUD: (create, edit, query) - Show heads-up display of UV Shells, as a part UV Statistics HUD
        displaySolidMap: (create, edit, query) - Display a solid overlay for the active texture map.
        displayStyle: (create, edit, query) - Set the mode to display the image. Valid values are:  "color" to display the basic RGB image "mask" to display the mask channel "lum" to display the luminance of the image
        displayTextureBorder: (create, edit, query) - Toggles the texture borders display.
        displayUVPositionHUD: (create, edit, query) - Show heads-up display of UV positions
        displayUVShellCountHUD: (create, edit, query) - Show heads-up display of UV Shell count, as a part UV Statistics HUD
        displayUVStatisticsHUD: (create, edit, query) - Show heads-up display of UV Statistics
        displayUsedPercentageHUD: (create, edit, query) - Show heads-up display of used UV space percentage, as a part UV Statistics HUD
        distortionAlpha: (create, edit, query) - Set or query the distortion display alpha.
        distortionPerObject: (create, edit, query) - Toggles the per-object distortion display.
        divisions: (create, edit, query) - Sets the number of subdivisions between main grid lines.
        docTag: (create, edit, query) - Attaches a tag to the editor.
        doubleBuffer: (create, edit, query) - Set the display in double buffer mode
        drawAxis: (create, edit, query) - Set or query whether the axis will be drawn.
        drawSubregions: (create, edit, query) - Toggles the subregion display.
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        exposure: (edit, query) - The exposure value used by the color management of the current editor.
        filter: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        forceMainConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        forceRebake: (create, edit) - Forces the current cache texture to refresh.
        frameAll: (create) - This will zoom on the whole scene.
        frameSelected: (create) - This will zoom on the currently selected objects.
        frontFacingColor: (create, edit, query) - Sets or queries the RGBA front facing color.
        gamma: (edit, query) - The gamma value used by the color management of the current editor.
        gridLinesColor: (create, edit, query) - The color of grid lines, default is 0.325 0.325 0.325
        gridNumbersColor: (create, edit, query) - The color of grid numbers, default is 0.2 0.2 0.2
        highlightConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        imageBaseColor: (create, edit, query) - The base color of the image, default is white 1.0 1.0 1.0
        imageDim: (create, edit, query) - Toggles the image dimming.
        imageDisplay: (edit, query) - Toggles the Texture Image display.
        imageNames: (query) - List image names for all Texture Images available for display, if any.
        imageNumber: (edit, query) - Sets the number of Texture Images to display. This depends on the number of textures corresponding to the current selection. If there are N textures, then the possible Texture Image numbers are 0 to N-1.
        imagePixelSnap: (edit, query) - Sets a mode so that UV transformations in the UV Texture Editor will cause UV values to snap to image pixel corners. Which pixels are used depends on whether a Texture Image or an Editor Image is being displayed. If both are displayed, the Texture Image pixels will be used.
        imageRatio: (edit, query) - Sets the window to draw using the Texture Image's height versus width ratio. If the width is greater than the height, then the width is set to be 1 "unit" in the window, and the height is adjusted by width divided by height. This only affects the display of a Texture Image, not an Editor Image.
        imageRatioValue: (query) - Query current image ratio value in UV Editor.
        imageSize: (query) - Returns the size of the Texture Image currently being displayed. The values returned are width followed by height. Image size can only be queried.
        imageTileRange: (edit, query) - Sets the UV range of the display. The 4 values specify the minimum U, V and maximum U, V in that order. When viewing a texture image, these values affect how many times the image is tiled based on appropriate parameters (e.g. Repeat UV, Mirror, Wrap, etc...) When viewing an Editor Image these values determine the visible size of the image. For example, setting the range to ( 0, 0, 2, 1 ) will cause the Editor Image to be loaded into a 2x1 rectangle, distorting it as necessary to fill the available space.
        imageUnfiltered: (edit, query) - Sets the Texture Image to draw unfiltered. The image will appear "pixelated" when the display resolution is higher than the resolution of the image.
        internalFaces: (create, edit, query) - Display contained faces by the selected components.
        labelPosition: (edit, query) - The position of the grid's numeric labels. Valid values are "axis" and "edge".
        loadImage: (edit) - load an image from disk and set it as the current Editor Image
        lockMainConnection: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        mainListConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        maxResolution: (create, edit, query) - This flag will set the current cached texture's maximum resolution.
        multiColorAlpha: (create, edit, query) - Sets the multi-color alpha of shaded UVs.
        nbImages: (query) - returns the number of images
        nextView: (edit) - Switches to the next view.
        numUvSets: (create, edit, query) - This flag will return the number of UV sets for selected objects in the texture window.
        numberOfImages: (query) - The number of Texture Images currently available. for display.
        numberOfTextures: (query) - The number of textures currently available. for display.
        panel: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        previousView: (edit) - Switches to the previous view.
        realSize: (create) - This will display the image with the size of the internal buffer. Note: This argument no long has any affect on image display.
        refresh: (edit) - requests a refresh of the current Editor Image.
        relatedFaces: (create, edit, query) - Display connected faces by the selected components.
        removeAllImages: (edit) - remove all the Editor Images from the Editor Image Stack
        removeImage: (edit) - remove the current Editor Image from the Editor Image Stack
        rendererString: (create, edit, query) - Set or query the string describing the current renderer.
        reset: (create) - Resets the ground plane to its default values.
        saveImage: (edit) - save the current Editor Image to memory. Saved Editor Images are stored in an Editor Image Stack. The most recently saved image is stored in position 0, the second most recently saved image in position 1, and so on... To set the current Editor Image to a previously saved image use the "di/displayImage" flag.
        scaleBlue: (create, edit, query) - Define the scaling factor for the blue component in the View. The default value is 1 and can be between -1000 to +1000
        scaleGreen: (create, edit, query) - Define the scaling factor for the green component in the View. The default value is 1 and can be between -1000 to +1000
        scaleRed: (create, edit, query) - Define the scaling factor for the red component in the View. The default value is 1 and can be between -1000 to +1000
        selectInternalFaces: (create, edit, query) - Add to selectionList the faces which are contained by (internal to) selected components.
        selectRelatedFaces: (create) - Add to selectionList the faces which are connected to (non-internally related to) selected components.
        selectionConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        setUvSet: (create, edit) - This flag will set the current UV set on one given selected object within the texture window.
        singleBuffer: (create, edit, query) - Set the display in single buffer mode
        size: (create, edit, query) - Sets the size of the grid.
        solidMap3dView: (create, edit, query) - Display a solid overlay for the active texture map in 3D viewport.
        solidMapColorSeed: (create, edit, query) - Sets the multi-color seed of shaded UVs.
        solidMapPerShell: (create, edit, query) - Display a solid overlay with a random color per shell.
        spacing: (create) - Sets the spacing between main grid lines.
        stateString: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        style: (edit, query) - This flag is obsolete and should not be used.
        subdivisionLinesColor: (create, edit, query) - The color of subdivision lines, default is 0.25 0.25 0.25
        textureBorder3dView: (create, edit, query) - Toggles the texture borders display in 3d viewport.
        textureBorderColor: (create, edit, query) - Sets the display color of texture border.
        textureBorderWidth: (create, edit, query) - Set the display edge width of texture border.
        textureNames: (query) - Texture names for all Texture Images available for display, if any.
        textureNumber: (edit, query) - Sets the number of textures to display This depends on the number of textures corresponding to the current selection. If there are N textures, then the possible Texture Image numbers are 0 to N-1.
        tileLabels: (create, edit, query) - Toggles the texture tile label display.
        tileLinesColor: (create, edit, query) - The color of tile lines, default is 0.0 0.0 0.0
        toggle: (create, edit, query) - Toggles the ground plane display.
        toggleExposure: (edit) - Toggles between the current and the default exposure value of the editor.
        toggleGamma: (edit) - Toggles between the current and the default gamma value of the editor.
        unParent: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useFaceGroup: (create, edit, query) - Display faces that are associated with the groupId that is set on the mesh node that is drawn. (The attribute "displayFacesWithGroupId")
        useTemplate: (create) - Forces the command to use a command template other than the current one.
        usedPercentageHUDRange: (create, edit, query) - Sets the range when calculating used UV space percentage. The 4 values specify the minimum U, V and maximum U, V in that order., default is 0 0 1 1.
        uvSets: (create, edit, query) - This flag will return strings containing UV set and object name pairs for selected objects in the texture window. The syntax of each pair is "objectName | uvSetName", where | is a literal character.
        viewPortImage: (create, edit) - Toggles the view port/ caching Texture Images.
        viewTransformName: (edit, query) - Sets the view pipeline to be applied if color management is enabled in the current editor.
        wireframeComponentColor: (create, edit, query) - Sets or queries the RGBA component wireframe color.
        wireframeObjectColor: (create, edit, query) - Sets or queries the RGBA object wireframe color.
        writeImage: (edit) - write the current Editor Image to disk
    """
    ...


def track(*args, down: Optional[Union[float, bool]] = ..., left: Optional[Union[float, bool]] = ..., right: Optional[Union[float, bool]] = ..., upDistance01: Optional[Union[float, bool]] = ..., upDistance02: Optional[Union[float, bool]] = ...) -> Any:
    r"""
    The track command translates a camera horizontally or vertically
    in the world space. The viewing-direction and up-direction of the
    camera are not altered. There is no translation in the viewing
    direction.
    
    The track command can be applied to either a perspective or an
    orthographic camera.
    
    When no camera name is supplied, this command is applied to the
    camera in the active view.

    Args:
        down: (create) - Set the amount of down translation in unit distance.
        left: (create) - Set the amount of left translation in unit distance.
        right: (create) - Set the amount of right translation in unit distance.
        upDistance01: (create) - Set the amount of up translation in unit distance. This is equivalent to using up/upDistance02 flag.
        upDistance02: (create) - Set the amount of up translation in unit distance. This is equivalent to using u/upDistance01 flag.
    """
    ...


def tumble(*args, azimuthAngle: Optional[Union[float, bool]] = ..., elevationAngle: Optional[Union[float, bool]] = ..., localTumble: Optional[Union[int, bool]] = ..., pivotPoint: Optional[Union[Tuple[float, float, float], bool]] = ..., rotationAngles: Optional[Union[Tuple[float, float], bool]] = ...) -> Any:
    r"""
    The tumble command revolves the camera(s) by varying the azimuth
    and elevation angles in the perspective window. When both the
    azimuth and the elevation angles are supplied on the command line,
    the camera is firstly tumbled for the azimuth angle, then tumbled
    for the elevation angle. 
    
    When no camera name is supplied, this command is applied to the
    camera in the active view. 
    
    The camera's rotate pivot will override a specified pivot point if
    the rotate pivot is not at the camera's eye point.

    Args:
        azimuthAngle: (create) - Degrees to change the azimuth angle.
        elevationAngle: (create) - Degrees to change the elevation angle.
        localTumble: (create) - Describes what point the camera will tumble around: 0 for the camera's tumble pivot, 1 for the camera's center of interest, and 2 for the camera's local axis, offset by its tumble pivot.
        pivotPoint: (create) - Three dimensional point used as the pivot point in the world space.
        rotationAngles: (create) - Two values in degrees to change the azimuth and elevation angles.
    """
    ...


def uvLink(*args, b: bool = ..., isValid: bool = ..., make: bool = ..., queryObject: Optional[Union[str, bool]] = ..., texture: Optional[Union[str, bool]] = ..., uvSet: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command is used to make, break and query UV linking
    relationships between UV sets on objects and textures that use those
    UV sets.
    
    If no make, break or query flag is specified and both uvSet and
    texture flags are present, the make flag is assumed to be specified.
    
    If no make, break or query flag is specified and only one of the
    uvSet and texture flags is present, the query flag is assumed to be
    specified.
    
    The term "texture" in the context of UV linking is a bit of an
    oversimplification. In fact, UV sets can be linked to any node which
    takes UV coordinates as input. However in most cases it will be a
    texture to which you wish to link a UV set.

    Args:
        b: (create) - The presence of this flag on the command indicates that the command is being invoked to break links between UV sets and textures.
        isValid: (create) - This flag is used to verify whether or not a texture or UV set is valid for the purposes of UV linking. It should be used in conjunction with either the -texture flag or the -uvSet flag, but not both at the same time.
        make: (create) - The presence of this flag on the command indicates that the command is being invoked to make links between UV sets and textures.
        queryObject: (create) - This flag should only be used in conjunction with a query of a texture. This flag is used to indicate that the results of the query should be limited to UV sets of the object specified by this flag.
        texture: (create) - The argument to the texture flag specifies the texture to be used by the command in performing the action.
        uvSet: (create) - The argument to the uvSet flag specifies the UV set to be used by the command in performing the action.
    """
    ...


def vectorize(*args, browserView: bool = ..., byFrame: Optional[Union[float, bool]] = ..., camera: Optional[Union[str, bool]] = ..., combineFillsEdges: bool = ..., currentFrame: bool = ..., curveTolerance: Optional[Union[float, bool]] = ..., customExtension: Optional[Union[str, bool]] = ..., detailLevel: Optional[Union[int, bool]] = ..., edgeColor: Optional[Union[Tuple[int, int, int], bool]] = ..., edgeDetail: bool = ..., edgeStyle: Optional[Union[str, bool]] = ..., edgeWeight: Optional[Union[float, bool]] = ..., endFrame: Optional[Union[float, bool]] = ..., filenameFormat: Optional[Union[str, bool]] = ..., fillStyle: Optional[Union[str, bool]] = ..., flashVersion: Optional[Union[int, bool]] = ..., frameRate: Optional[Union[int, bool]] = ..., height: Optional[Union[int, bool]] = ..., hiddenEdges: bool = ..., highlightLevel: Optional[Union[int, bool]] = ..., highlights: bool = ..., imageFormat: Optional[Union[str, bool]] = ..., layer: Optional[Union[str, bool]] = ..., minEdgeAngle: Optional[Union[float, bool]] = ..., outlinesAtIntersections: bool = ..., outputFileName: Optional[Union[str, bool]] = ..., pixelAspectRatio: Optional[Union[float, bool]] = ..., reflectionDepth: Optional[Union[int, bool]] = ..., reflections: bool = ..., renderLayers: bool = ..., renderOptimization: Optional[Union[str, bool]] = ..., renderView: bool = ..., secondaryCurveFitting: bool = ..., shadows: bool = ..., showBackFaces: bool = ..., startFrame: Optional[Union[float, bool]] = ..., svgAnimation: Optional[Union[str, bool]] = ..., svgCompression: bool = ..., width: Optional[Union[int, bool]] = ...) -> Any:
    r"""
    This command renders Maya scenes to various vector and raster formats
    using the Maya Vector renderer.

    Args:
        browserView: (create) - Specifies whether to preview the render in the browser.  This option is swf only.
        byFrame: (create) - Specifies the frame increment.
        camera: (create) - Specifies the camera to render.
        combineFillsEdges: (create) - Specifies whether fills and edges should be combined as a single object in Flash. This option is swf only.
        currentFrame: (create) - Specifies whether to render the current frame only.
        curveTolerance: (create) - Specifies the curve tolerance.  Valid values are in the range: 0.0 to 15.0.  The curve tolerance determines how aggressively the renderer tries to fit a series of connected, consecutive line segments to a curve. A value of 0.0 causes all line segments to be drawn without curve fitting.  A value of 15.0 causes aggressive curve fitting.
        customExtension: (create) - Specifies a custom extension to use for the filename. Any non-empty string is valid.
        detailLevel: (create) - Specifies the detail level.  Valid values are:  0 to 50.  The smaller the value, the more polygons may be combined to produce smaller files.  A higher value results in a more accurate render, but also larger files and longer render times.
        edgeColor: (create) - Specifies the red, green, and blue components of the edge color.  Valid values are: 0 to 255 for each color component.
        edgeDetail: (create) - Specifies whether edge detail should be rendered; ie. edges that have an angle between the face normals of any two adjacent polygons sharing an edge that is greater than the minimum edge angle (specified by the -mea flag).
        edgeStyle: (create) - Specifies the edge style.  Valid values are:  "Outline", "EntireMesh", "None".
        edgeWeight: (create) - Specifies the edge weight to be used for all edges in points.  There are 72 points per inch.  A value of 0.0 specifies hairline edge weight.
        endFrame: (create) - Specifies the end frame.
        filenameFormat: (create) - Specifies the file name format.  Valid values are:  "name", "name.ext", "name.#.ext", "name.ext.#", "name.#", "name#.ext", "name_#.ext".
        fillStyle: (create) - Specifies the fill style.  Valid values are:  "SingleColor", "TwoColor", "FourColor", "FullColor", "AverageColor", "AreaGradient", "MeshGradient", "None".  AreaGradient and MeshGradient are not available for the eps and ai image formats.
        flashVersion: (create) - Specifies the Flash version of the swf output.  Valid values are:  3, 4, 5.  This option is swf only.
        frameRate: (create) - Specifies the frame rate.  This option is for svg and swf only.
        height: (create) - Specifies the height of the output image in pixels.
        hiddenEdges: (create) - Specifies whether hidden edges should be rendered; ie. edges that have are not visible from the camera.
        highlightLevel: (create) - Specifies the highlight level.  Valid values are:  1 to 8.  The value specifies how many concentric rings will be used to render an object's highlight.  This option is for the SingleColor, AverageColor, and AreaGradient fill styles only.
        highlights: (create) - Specifies whether highlights should be rendered.  This option has no effect for ai, eps, and svg.  This option is for the SingleColor, AverageColor, and AreaGradient fill styles only.
        imageFormat: (create) - Specifies the image format to render. Valid values for the Windows and Mac platforms are: "swf", "eps", "ai", "svg", "jpg", "iff", "sgi", "tga", "tif", "bmp". Additional valid values for the Windows platform are: "als", "cin", "gif", "yuv", "rla", "si".  Additional valid values for the Mac platform are: "pntg", "ps", "png", "pict", "qtif", "qt".
        layer: (create) - Render the specified render layer.         Only this render layer will be rendered,         regardless of the renderable attribute value of the render layer.         The layer name will be appended to the output image file name.         The specified render layer becomes the current render layer before rendering,         and remains as current render layer after the rendering.
        minEdgeAngle: (create) - Specifies the minimum edge angle in degrees.  Valid values are: 0.0 to 90.0.  This angle is the minimum angle between adjacent polygon face normals that is used to determine if the edge is rendered when the -ed flag is specified.
        outlinesAtIntersections: (create) - Specifies if edges should be drawn when two polygons intersect. By default this flag is enabled.
        outputFileName: (create) - Specifies the output file name.
        pixelAspectRatio: (create) - Specifes the pixel aspect ratio.
        reflectionDepth: (create) - Specifies the reflection depth.  Valid values are:  1 to 4.  The value specifies how many levels of reflection will be applied.  This option has no effect for ai, eps, and svg.
        reflections: (create) - Specifies whether reflections should be rendered.  This option has no effect for ai, eps, and svg.
        renderLayers: (create) - Specifies whether render layers should be rendered into separate files.
        renderOptimization: (create) - Specifies the render optimization. Valid values are:  "Safe", "Good", "Aggressive". "Safe"  will  remove redundant geometry. "Good" removes redundant geometry as well as sub-pixel geometry that would not be visible without zooming into the high detail area. "Agressive" removes all of the geometry that "Good" removes but will also remove geometry at slightly above the single pixel level making it possible to visibly detect the removed geometry without zooming in on the affected region.
        renderView: (create) - Specifies whether to display the rendered image to the render view.  This option is not applicable when batch rendering.
        secondaryCurveFitting: (create) - Specifies whether to do secondary curve fitting.
        shadows: (create) - Specifies whether shadows should be rendered.  This option has no effect for ai, eps, and svg.
        showBackFaces: (create) - Specifies whether back faces will should be rendered; ie. faces whose normals are pointed away from the camera.
        startFrame: (create) - Specifies the start frame.
        svgAnimation: (create) - Specifies the SVG animation type.  Valid values are:  "Native", "HTMLScript".  This option is SVG only.
        svgCompression: (create) - Specifies whether the SVG output should be compressed.  This option is svg only.
        width: (create) - Specifies the width of the output image in pixels.
    """
    ...


def viewCamera(*args, move: Optional[Union[str, bool]] = ..., sideView: bool = ..., topView: bool = ...) -> Any:
    r"""
    The viewCamera command is used to position a camera to look
    directly at the side or top of another camera. This is primarily
    useful for the user when he or she is setting depth-of-field and
    clipping planes, if they are being used.
    
    The default behaviour: If no other flags are specified, the camera
    in the active panel is moved and the -t is presumed. If there is a
    camera selected, it is used as the target camera.

    Args:
        move: (create) - Specifies which camera needs to move.
        sideView: (create) - Position camera to look at the side of the target camera.
        topView: (create) - Position camera to look at the top of the target camera (default).
    """
    ...


def viewClipPlane(*args, autoClipPlane: bool = ..., farClipPlane: Optional[Union[float, bool]] = ..., nearClipPlane: Optional[Union[float, bool]] = ..., surfacesOnly: bool = ..., query: bool = ...) -> Any:
    r"""
    The viewClipPlane command can be used to query or set a camera's
    clip planes. If a camera is not specified, the camera in the
    active view will be used. The near and far clip plane flags may be
    used in conjunction with the auto clip plane flag.

    Args:
        autoClipPlane: (create, query) - Compute the clip planes such that all object's in the camera's viewing frustum will be visible.
        farClipPlane: (create, query) - Set or query the far clip plane.
        nearClipPlane: (create, query) - Set or query the near clip plane.
        surfacesOnly: (create) - This flag is to be used in conjunction with the auto clip plane flag. Only the bounding boxes of surfaces will be used to compute the camera's clipping planes.
    """
    ...


def viewFit(*args, allObjects: bool = ..., animate: bool = ..., center: bool = ..., fitClipPlanes: bool = ..., fitFactor: Optional[Union[float, bool]] = ..., namespace: Optional[Union[str, bool]] = ..., noChildren: bool = ...) -> Any:
    r"""
    The viewFit command positions the specified camera so its
    point-of-view contains all selected objects other than itself. If
    no objects are selected, everything is fit to the view (excepting
    cameras, lights, and sketching plannes). The fit-factor, if
    specified, determines how much of the view should be filled. If a
    camera is not specified, the camera in the active view will be
    used. After the camera is moved, its center of interest is set to
    the center of the bounding box of the objects.
    
    Additionally, a list of objects can be passed as arguments.
    If a camera is specified it must be the first argument. Objects
    passed as arguments to the command will be used instead of the
    selected objects.

    Args:
        allObjects: (create) - Specifies that all objects are to be fit regardless of the active list.
        animate: (create) - Specifies that the transition between camera positions should be animated.
        center: (create) - Specifies that the camera moves to the center of the selected object, but does not move the camera closer.
        fitClipPlanes: (create) - Fit orthographic clipping planes in order to contain selection bounding box in the view frustum
        fitFactor: (create) - Specifies how much of the view should be filled with the "fitted" items.
        namespace: (create) - Specifies a namespace that should be excluded. All objects in the specified namespace will be excluded from the fit process.
        noChildren: (create) - Specifies that the children of fitted objects should be ignored when determining the fit.
    """
    ...


def viewHeadOn(*args) -> Any:
    r"""
    The viewHeadOn command positions the specified camera so it is
    looking "down" the normal of the live object, and fitted to the
    live object. If the live object is a surface, an arbitrary normal
    is chosen.

    Args:
    """
    ...


def viewLookAt(*args, position: Optional[Union[Tuple[float, float, float], bool]] = ...) -> Any:
    r"""
    The viewLookAt command positions the specified camera so it is
    looking at the centroid of all selected objects. If no objects are
    specified the camera will look at the ground plane.

    Args:
        position: (create) - Position in world space to make the camera look at.
    """
    ...


def viewPlace(*args, animate: bool = ..., eyePoint: Optional[Union[Tuple[float, float, float], bool]] = ..., fieldOfView: Optional[Union[float, bool]] = ..., lookAt: Optional[Union[Tuple[float, float, float], bool]] = ..., ortho: bool = ..., perspective: bool = ..., upDirection: Optional[Union[Tuple[float, float, float], bool]] = ..., viewDirection: Optional[Union[Tuple[float, float, float], bool]] = ...) -> Any:
    r"""
    This command positions the camera as specified. The lookAt and
    viewDirection flags are mutually exclusive, as are the ortho and
    perspective flags. If this command switches a camera from ortho to
    perspective or the other way around without specifying a new field
    of view, then one is calculated based on a heuristic involving the
    selected objects. 
    
    If the camera is not specified on the command line, the command
    will check to see if there is a camera on the active list. 
    
    The user should be aware that some positions will be
    unattainable. For example, using a new camera located at the
    origin and specifying a lookAt of [0 0 -5] and an up of [1 1
    1]. In these cases, the camera will always aim at the lookAt, and
    the new up direction will be determined by transforming the
    specified up into camera space and then projecting this vector
    onto a plane defined by the camera's up and right vectors. Using
    the example above, the new up vector will be [1 1 0].

    Args:
        animate: (create) - If set to true then animate the camera transition from current position to the final one.
        eyePoint: (create) - The new eye point in world coordinates.
        fieldOfView: (create) - The new field of view (in degrees, for perspective cameras, and in world distance for ortho cameras)
        lookAt: (create) - The new look-at point in world coordinates.
        ortho: (create) - Sets the camera to be orthgraphic.
        perspective: (create) - Sets the camera to be perspective.
        upDirection: (create) - The new up direction vector.
        viewDirection: (create) - The new view direction vector.
    """
    ...


def viewSet(*args, animate: bool = ..., back: bool = ..., bottom: bool = ..., fit: bool = ..., fitFactor: Optional[Union[float, bool]] = ..., front: bool = ..., home: bool = ..., keepRenderSettings: bool = ..., leftSide: bool = ..., namespace: Optional[Union[str, bool]] = ..., nextView: bool = ..., persp: bool = ..., previousView: bool = ..., rightSide: bool = ..., side: bool = ..., top: bool = ..., viewNegativeX: bool = ..., viewNegativeY: bool = ..., viewNegativeZ: bool = ..., viewX: bool = ..., viewY: bool = ..., viewZ: bool = ..., query: bool = ...) -> Any:
    r"""
    This command positions the camera to one of the pre-defined
    positions. If the fit flag is set in conjunction with persp, top,
    side, or front, the view is "fit" based on the list of selected
    objects (if there are any) or on all the objects if nothing is
    selected. Notice that the fit flag cannot be set in conjunction with
    view along axis commands like viewX. If a camera is not specified,
    the camera in the active view will be used. If no flag is specified,
    the camera is set to the home position.

    Args:
        animate: (create) - Specifies that the transition between camera positions should be animated.
        back: (create) - Moves the camera to the back position.
        bottom: (create) - Moves the camera to the bottom position.
        fit: (create, query) - Apply a viewFit after positioning camera to persp, top, side, or front.
        fitFactor: (create) - Specifies how much of the view should be filled with the "fitted" items
        front: (create) - Moves the camera to the front position.
        home: (create) - Executes the camera's home attribute command. Before the string is executed, all occurances of "%camera" will be replaced by the camera's name. Use the camera command to set a camera's home command.
        keepRenderSettings: (create, query) - Retain the 'renderable' flag vaue on the view. Especially important if it switches from perspective to orthographic and then back again.
        leftSide: (create) - Moves the camera to the left side position.
        namespace: (create) - Specifies a namespace that should be excluded. All objects in the specified namespace will be excluded from the fit process.
        nextView: (create, query) - Moves the camera to the next position.
        persp: (create) - Moves the camera to the persp position.
        previousView: (create, query) - Moves the camera to the previous position.
        rightSide: (create) - Moves the camera to the right side position.
        side: (create) - Moves the camera to the (right) side position (deprecated).
        top: (create) - Moves the camera to the top position.
        viewNegativeX: (create) - Moves the camera to view along negative X axis.
        viewNegativeY: (create) - Moves the camera to view along negative Y axis.
        viewNegativeZ: (create) - Moves the camera to view along negative Z axis.
        viewX: (create) - Moves the camera to view along X axis.
        viewY: (create) - Moves the camera to view along Y axis.
        viewZ: (create) - Moves the camera to view along Z axis.
    """
    ...


