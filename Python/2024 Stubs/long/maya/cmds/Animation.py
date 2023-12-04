from typing import Union, Optional, List, Tuple, Any

def aimConstraint(*args, aimVector: Optional[Union[Tuple[float, float, float], bool]] = ..., layer: Optional[Union[str, bool]] = ..., maintainOffset: bool = ..., name: Optional[Union[str, bool]] = ..., offset: Optional[Union[Tuple[float, float, float], bool]] = ..., remove: bool = ..., skip: Optional[Union[str, bool]] = ..., targetList: bool = ..., upVector: Optional[Union[Tuple[float, float, float], bool]] = ..., weight: Optional[Union[float, bool]] = ..., weightAliasList: bool = ..., worldUpObject: Optional[Union[str, bool]] = ..., worldUpType: Optional[Union[str, bool]] = ..., worldUpVector: Optional[Union[Tuple[float, float, float], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Constrain an object's orientation to point at a target object or
    at the average position of a number of targets.
    
    An aimConstraint takes as input one or more "target" DAG transform
    nodes at which to aim the single "constraint object" DAG transform
    node.  The aimConstraint orients the constrained object such that
    the aimVector (in the object's local coordinate system) points to
    the in weighted average of the world space position target
    objects.  The upVector (again the the object's local coordinate
    system) is aligned in world space with the worldUpVector.

    Args:
        aimVector: (create, edit, query) - Set the aim vector.  This is the vector in local coordinates that points at the target.  If not given at creation time, the default value of (1.0, 0.0, 0.0) is used.
        layer: (create, edit) - Specify the name of the animation layer where the constraint should be added.
        maintainOffset: (create) - The offset necessary to preserve the constrained object's initial rotation will be calculated and used as the offset.
        name: (create, edit, query) - Sets the name of the constraint node to the specified name.  Default name is constrainedObjectName_constraintType
        offset: (create, edit, query) - Sets or queries the value of the offset. Default is 0,0,0.
        remove: (edit) - removes the listed target(s) from the constraint.
        skip: (create, edit, multiuse) - Specify the axis to be skipped. Valid values are "x", "y", "z" and "none". During creation, "none" is the default.
        targetList: (query) - Return the list of target objects.
        upVector: (create, edit, query) - Set local up vector.  This is the vector in local coordinates that aligns with the world up vector.  If not given at creation time, the default value of (0.0, 1.0, 0.0) is used.
        weight: (create, edit, query) - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
        weightAliasList: (query) - Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
        worldUpObject: (create, edit, query) - Set the DAG object use for worldUpType "object" and "objectrotation". See worldUpType for greater detail. The default value is no up object, which is interpreted as world space.
        worldUpType: (create, edit, query) - Set the type of the world up vector computation. The worldUpType can have one of 5 values: "scene", "object", "objectrotation", "vector", or "none". If the value is "scene", the upVector is aligned with the up axis of the scene and worldUpVector and worldUpObject are ignored. If the value is "object", the upVector is aimed as closely as possible to the origin of the space of the worldUpObject and the worldUpVector is ignored. If the value is "objectrotation" then the worldUpVector is interpreted as being in the coordinate space of the worldUpObject, transformed into world space and the upVector is aligned as closely as possible to the result. If the value is "vector", the upVector is aligned with worldUpVector as closely as possible and worldUpMatrix is ignored. Finally, if the value is "none" no twist calculation is performed by the constraint, with the resulting "upVector" orientation based previous orientation of the constrained object, and the "great circle" rotation needed to align the aim vector with its constraint. The default worldUpType is "vector".
        worldUpVector: (create, edit, query) - Set world up vector.  This is the vector in world coordinates that up vector should align with. See -wut/worldUpType (below)for greater detail. If not given at creation time, the default value of (0.0, 1.0, 0.0) is used.
    """
    ...


def animCurveEditor(*args, areCurvesSelected: bool = ..., autoFit: Optional[Union[str, bool]] = ..., autoFitTime: Optional[Union[str, bool]] = ..., classicMode: bool = ..., clipTime: Optional[Union[str, bool]] = ..., constrainDrag: Optional[Union[int, bool]] = ..., control: bool = ..., curvesShown: bool = ..., curvesShownForceUpdate: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., denormalizeCurvesCommand: Optional[Union[str, bool]] = ..., displayActiveKeyTangents: str = ..., displayActiveKeys: str = ..., displayInfinities: str = ..., displayKeys: str = ..., displayNormalized: bool = ..., displayTangents: str = ..., displayValues: str = ..., docTag: Optional[Union[str, bool]] = ..., exists: bool = ..., filter: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., highlightAffectedCurves: bool = ..., highlightConnection: Optional[Union[str, bool]] = ..., keyMinScale: Optional[Union[float, bool]] = ..., keyScale: Optional[Union[float, bool]] = ..., keyingTime: Optional[Union[str, bool]] = ..., lockMainConnection: bool = ..., lockPlayRangeShades: Optional[Union[str, bool]] = ..., lookAt: str = ..., mainListConnection: Optional[Union[str, bool]] = ..., menu: Optional[Union[str, bool]] = ..., normalizeCurvesCommand: Optional[Union[str, bool]] = ..., outliner: Optional[Union[str, bool]] = ..., panel: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., preSelectionHighlight: bool = ..., renormalizeCurves: bool = ..., resultSamples: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., resultScreenSamples: Optional[Union[int, bool]] = ..., resultUpdate: Optional[Union[str, bool]] = ..., selectionConnection: Optional[Union[str, bool]] = ..., showActiveCurveNames: bool = ..., showBufferCurves: Optional[Union[str, bool]] = ..., showCurveNames: bool = ..., showPlayRangeShades: Optional[Union[str, bool]] = ..., showResults: Optional[Union[str, bool]] = ..., showUpstreamCurves: bool = ..., simpleKeyView: bool = ..., smoothness: Optional[Union[str, bool]] = ..., snapTime: Optional[Union[str, bool]] = ..., snapValue: Optional[Union[str, bool]] = ..., stackedCurves: bool = ..., stackedCurvesMax: Optional[Union[float, bool]] = ..., stackedCurvesMin: Optional[Union[float, bool]] = ..., stackedCurvesSpace: Optional[Union[float, bool]] = ..., stateString: bool = ..., timelinePositionTop: bool = ..., unParent: bool = ..., unlockMainConnection: bool = ..., updateMainConnection: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., valueLinesToggle: str = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Edit a characteristic of a graph editor

    Args:
        areCurvesSelected: (query) - Returns a boolean to know if at least one curve is selected in the graph editor.
        autoFit: (edit, query) - on | off | tgl Auto fit-to-view.
        autoFitTime: (edit, query) - on | off | tgl Auto fit-to-view along the time axis, as well.
        classicMode: (edit, query) - When on, the graph editor is displayed in "Classic Mode", otherwise "Suites Mode" is used.
        clipTime: (edit, query) - Valid values: "on" "off" Display the clips with their offset and scale applied to the anim curves in the clip.
        constrainDrag: (create, edit, query) - Constrains all Graph Editor animation curve drag operations to either the X-axis, the Y-axis, or to neither of those axes. Values to supply are: 0 for not constraining any axis, 1 for constraing the X-axis, or 2 for constraining the Y-axis. When used in queries, this flag returns the latter values and these values have the same interpretation as above. Note: when the shift key is pressed before dragging the animation curve, the first mouse movement will instead determine (and override) any prior set constrained axis.
        control: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        curvesShown: (query) - Returns a string array containing the names of the animCurve nodes currently displayed in the graph editor.
        curvesShownForceUpdate: (query) - Returns a string array containing the names of the animCurve nodes currently displayed in the graph editor. Unlike the curvesShown flag, this will force an update of the graph editor for the case where the mainListConnection has been modified since the last refresh.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        denormalizeCurvesCommand: (create, edit) - Sets the script that is run to denormalize curves in the graph editor. This is intended for internal use only.
        displayActiveKeyTangents: (edit) - on | off | tgl Display active key tangents in the editor.
        displayActiveKeys: (edit) - on | off | tgl Display active keys in the editor.
        displayInfinities: (edit) - on | off | tgl Display infinities in the editor.
        displayKeys: (edit) - on | off | tgl Display keyframes in the editor.
        displayNormalized: (edit, query) - When on, display all curves normalized to the range -1 to +1.
        displayTangents: (edit) - on | off | tgl Display tangents in the editor.
        displayValues: (edit) - on | off | tgl Display active keys and tangents values in the editor.
        docTag: (create, edit, query) - Attaches a tag to the editor.
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        filter: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        forceMainConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        highlightAffectedCurves: (edit, query) - When on, highlights the curve segment affected by the selected key/tangent
        highlightConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        keyMinScale: (edit, query) - The minimum key selection size in the graph editor. A value of 0.0 means there is no minimum size. A value of 1.0 means the minimum size is the size of a key with keyScale set to 1.0
        keyScale: (edit, query) - Scales the key size in the graph editor
        keyingTime: (query) - The current time in the given curve to be keyed in the graph editor.
        lockMainConnection: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        lockPlayRangeShades: (edit, query) - Valid values: "on" "off" "tgl" Lock Play Range Shades.
        lookAt: (edit) - all | selected | currentTime FitView helpers.
        mainListConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        menu: (create) - Specify a script to be run when the editor is created.  The function will be passed one string argument which is the new editor's name.
        normalizeCurvesCommand: (create, edit) - Sets the script that is run to normalize curves in the graph editor. This is intended for internal use only.
        outliner: (edit, query) - The name of the outliner that is associated with the graph editor.
        panel: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        preSelectionHighlight: (edit, query) - When on, the curve/key/tangent under the mouse pointer is highlighted to ease selection.
        renormalizeCurves: (edit) - This flag causes the curve normalization factors to be recalculated.
        resultSamples: (edit, query) - Specify the sampling for result curves Note: the smaller this number is, the longer it will take to update the display.
        resultScreenSamples: (edit, query) - Specify the screen base result sampling for result curves. If 0, then results are sampled in time.
        resultUpdate: (edit, query) - Valid values: "interactive" "delayed" Controls how changes to animCurves are reflected in the result curves (if results are being shown).  If resultUpdate is "interactive", then as interactive changes are being made to the animCurve, the result curves will be updated.  If modelUpdate is delayed (which is the default setting), then result curves are updated once the final change to an animCurve has been made.
        selectionConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        showActiveCurveNames: (edit, query) - Display the active curve(s)'s name.
        showBufferCurves: (edit, query) - Valid values: "on" "off" "tgl" Display buffer curves.
        showCurveNames: (edit, query) - Display the curves's name.
        showPlayRangeShades: (edit, query) - Valid values: "on" "off" "tgl" Display Play Range Shades.
        showResults: (edit, query) - Valid values: "on" "off" "tgl" Display result curves from expression or other non-keyed action.
        showUpstreamCurves: (edit, query) - If true, the dependency graph is searched upstream for all curves that drive the selected plugs (showing multiple curves for example in a typical driven key setup, where first the driven key curve is encountered, followed by the actual animation curve that drives the source object). If false, only the first curves encountered will be shown. Note that, even if false, multiple curves can be shown if e.g. a blendWeighted node is being used to combine multiple curves.
        simpleKeyView: (edit, query) - on | off Display simpler and smaller key.
        smoothness: (edit, query) - Valid values: "coarse" "rough" "medium" "fine" Specify the display smoothness of animation curves.
        snapTime: (edit, query) - none | integer | keyframe Keyframe move snap in time.
        snapValue: (edit, query) - none | integer | keyframe Keyframe move snap in values.
        stackedCurves: (edit, query) - Switches the display mode between normal (all curves sharing one set of axes) to stacked (each curve on its own value axis, stacked vertically).
        stackedCurvesMax: (edit, query) - Sets the maximum value on the per-curve value axis when in stacked mode.
        stackedCurvesMin: (edit, query) - Sets the minimum value on the per-curve value axis when in stacked mode.
        stackedCurvesSpace: (edit, query) - Sets the spacing between curves when in stacked mode.
        stateString: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        timelinePositionTop: (edit, query) - on | off | tgl Display timeline either at the top or bottom.
        unParent: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
        valueLinesToggle: (edit) - on | off | tgl Display the value lines for high/low/zero of selected curves in the editor
    """
    ...


def animDisplay(*args, modelUpdate: Optional[Union[str, bool]] = ..., refAnimCurvesEditable: bool = ..., timeCode: Optional[Union[str, bool]] = ..., timeCodeOffset: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command changes certain display options used by
    animation windows.

    Args:
        modelUpdate: (create, edit, query) - Controls how changes to animCurves are propagated through the dependency graph. Valid modes are "none", "interactive" or "delayed". If modelUpdate is "none" then changing an animCurve will not cause the model to be updated (change currentTime in order to update the model).  If modelUpdate is "interactive" (which is the default setting), then as interactive changes are being made to the animCurve, the model will be updated.  If modelUpdate is delayed, then the model is updated once the final change to an animCurve has been made.  With modelUpdate set to either "interactive" or "delayed", changes to animCurves made via commands will also cause the model to be updated.
        refAnimCurvesEditable: (create, edit, query) - Specify if animation curves from referenced files are editable.
        timeCode: (create, edit, query) - Controls how time value are display. Valid values are "frame", "timecode", "fulltimecode". If the value is "frame" maya will display time in frame everywhere. If the value is "timecode" maya will display time in timecode in time slider, graph editor and dope sheet. If the value is "fulltimecode" maya will display time in timecode everywhere.
        timeCodeOffset: (create, edit, query) - This flag has now been deprecated.  It still exists to not break legacy scripts, but it will now do nothing.  See the new timeCode command to set and query timeCodes.
    """
    ...


def animLayer(*args, addRelatedKG: bool = ..., addSelectedObjects: bool = ..., affectedLayers: bool = ..., animCurves: bool = ..., attribute: Optional[Union[str, bool]] = ..., baseAnimCurves: bool = ..., bestAnimLayer: bool = ..., bestLayer: bool = ..., blendNodes: bool = ..., children: Optional[Union[str, bool]] = ..., collapse: bool = ..., copy: str = ..., copyAnimation: Optional[Union[str, bool]] = ..., copyNoAnimation: str = ..., excludeBoolean: bool = ..., excludeDynamic: bool = ..., excludeEnum: bool = ..., excludeProxy: bool = ..., excludeRotate: bool = ..., excludeScale: bool = ..., excludeTranslate: bool = ..., excludeVisibility: bool = ..., exists: bool = ..., extractAnimation: Optional[Union[str, bool]] = ..., findCurveForPlug: Optional[Union[str, bool]] = ..., forceUIRebuild: bool = ..., forceUIRefresh: bool = ..., layeredPlug: Optional[Union[str, bool]] = ..., lock: bool = ..., maxLayers: bool = ..., moveLayerAfter: str = ..., moveLayerBefore: str = ..., mute: bool = ..., override: bool = ..., parent: Optional[Union[str, bool]] = ..., passthrough: bool = ..., preferred: bool = ..., removeAllAttributes: bool = ..., removeAttribute: str = ..., removeSelectedObjects: bool = ..., root: Optional[Union[str, bool]] = ..., selected: bool = ..., solo: bool = ..., weight: Optional[Union[float, bool]] = ..., writeBlendnodeDestinations: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates and edits animation layers.

    Args:
        addRelatedKG: (create, edit, query) - When adding or removing selected object(s) from the layer, adds associated keying group(s) to the object(s).
        addSelectedObjects: (create, edit, query) - Adds selected object(s) to the layer.
        affectedLayers: (query) - Return the layers that the currently selected object(s) are members of
        animCurves: (create, edit, query) - In query mode returns the anim curves associated with this layer
        attribute: (create, edit, multiuse, query) - Adds a specific attribute on a object to the layer.
        baseAnimCurves: (create, edit, query) - In query mode returns the base layer anim curves associated with this layer, if any.
        bestAnimLayer: (create, edit, query) - In query mode returns the best anim layers for keying for the selected objects. If used in conjunction with -at, will return the best anim layers for keying for the specific plugs (attributes) specified.
        bestLayer: (query) - Return the layer that will be keyed for specified attribute.
        blendNodes: (create, edit, query) - In query mode returns the blend nodes associated with this layer
        children: (query) - Get the list of children layers. Return value is a string array.
        collapse: (create, edit, query) - Determine if a layer is collapse in the layer editor.
        copy: (edit) - Copy from the layer.
        copyAnimation: (create, edit) - Copy animation from specified layer to destination layer, only animation that are on attribute layered by both layer that are concerned.
        copyNoAnimation: (edit) - Copy from layer without the animation curves.
        excludeBoolean: (create, edit, query) - When adding or removing selected object(s) from the layer, excludes any boolean attributes.
        excludeDynamic: (create, edit, query) - When adding or removing selected object(s) from the layer, excludes any dynamic attributes.
        excludeEnum: (create, edit, query) - When adding or removing selected object(s) from the layer, excludes any enum attributes.
        excludeProxy: (create, edit, query) - When adding or removing selected object(s) from the layer, excludes any proxy attributes.
        excludeRotate: (create, edit, query) - When adding or removing selected object(s) from the layer, excludes the rotate attribute.
        excludeScale: (create, edit, query) - When adding or removing selected object(s) from the layer, excludes the scale attribute.
        excludeTranslate: (create, edit, query) - When adding or removing selected object(s) from the layer, excludes the translate attribute.
        excludeVisibility: (create, edit, query) - When adding or removing selected object(s) from the layer, excludes the visibility attribute.
        exists: (query) - Determine if a layer exists.
        extractAnimation: (create, edit) - Transfer animation from specified layer to destination layer, only animation that are on attribute layered by both layer that are concerned.
        findCurveForPlug: (edit, query) - Finds the parameter curve containing the animation data for the specified plug on the given layer. 			In query mode, this flag needs a value.
        forceUIRebuild: (create) - Rebuilds the animation layers user interface.
        forceUIRefresh: (create) - Refreshes the animation layers user interface.
        layeredPlug: (query) - Returns the plug on the blend node corresponding to the specified layer 			In query mode, this flag needs a value.
        lock: (create, edit, query) - Set the lock state of the specified layer. A locked layer cannot receive key. Default is false.
        maxLayers: (query) - Returns the maximum number of anim layers supported by this product.
        moveLayerAfter: (edit) - Move layer after the specified layer
        moveLayerBefore: (edit) - Move layer before the specified layer
        mute: (create, edit, query) - Set the mute state of the specified layer. Default is false.
        override: (create, edit, query) - Set the overide state of the specified layer. Default is false.
        parent: (create, edit, query) - Set the parent of the specified layer. Default is the animation layer root.
        passthrough: (create, edit, query) - Set the passthrough state of the specified layer. Default is true.
        preferred: (create, edit, query) - Determine if a layer is a preferred layer, the best layer algorithm will try to set keyframe in preferred layer first.
        removeAllAttributes: (edit) - Remove all objects from the layer.
        removeAttribute: (edit, multiuse) - Remove object from the layer.
        removeSelectedObjects: (edit) - Removes selected object(s) from the layer.
        root: (query) - Return the base layer if it exist
        selected: (create, edit, query) - Determine if a layer is selected, a selected layer will be show in the timecontrol, graph editor.
        solo: (create, edit, query) - Set the solo state of the specified layer. Default is false.
        weight: (create, edit, query) - Set the weight of the specified layer between 0.0 and 1.0. Default is 1.
        writeBlendnodeDestinations: (edit) - In edit mode writes the destination plugs of the blend nodes that belong to the layer into the blend node. This is used for layer import/export purposes and is not for general use.
    """
    ...


def animView(*args, endTime: Union[float, Tuple[float, float]] = ..., maxValue: float = ..., minValue: float = ..., nextView: bool = ..., previousView: bool = ..., startTime: Union[float, Tuple[float, float]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command allows you to specify the current view range within
    an animation editor.

    Args:
        endTime: () - End time to display within the editor
        maxValue: () - Upper value to display within the editor
        minValue: () - Lower value to display within the editor
        nextView: (edit) - Switches to the next view.
        previousView: (edit) - Switches to the previous view.
        startTime: () - Start time to display within the editor
    """
    ...


def applyTake(*args, channel: Optional[Union[str, bool]] = ..., device: Optional[Union[str, bool]] = ..., filter: Optional[Union[str, bool]] = ..., preview: bool = ..., recurseChannel: bool = ..., reset: bool = ..., specifyChannel: bool = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ...) -> Any:
    r"""
    This command takes data in a device (refered to as a take) and converts
    it into a form that may be played back and reviewed. The take can either
    be imported through the readTake action, or recorded by the recordDevice
    action. The take is either converted into animation curves or if the
    -preview flag is used, into blendDevice nodes.
    
    The command looks for animation curves attached to the target attributes
    of a device attachment. If animation curves exist, the take is
    pasted over the existing curves. If the curves do not exist, new
    animation curves are created.
    
    If devices are not specified, all of the devices with take data and that
    are enabled for applyTake, will have their data applied.
    
    See also: recordDevice, enableDevice, readTake, writeTake

    Args:
        channel: (create, multiuse) - This flag overrides the set channel enable value. If a channel is specified, it will be enabled.  C: The default is all applyTake enabled channels for the device(s).
        device: (create, multiuse) - Specifies which device contains the take.  C: The default is all applyTake enabled devices.
        filter: (create, multiuse) - This flag specifies the filters to use during the applyTake. If this flag is used multiple times, the ordering of the filters is from left to right.  C: The default is no filters.
        preview: (create) - Applies the take to blendDevice nodes attached to the target attributes connected to the device attachments. Animation curves attached to the attributes will not be altered, but for the time that preview data is defined, the preview data will be the data used during playback.  C: The default is to not preview.
        recurseChannel: (create) - When this flag is used, the children of the channel(s) specified by -c/channel are also applied. C: The default is all of the enabled channels.
        reset: (create) - Resets the blendDevice nodes affected by -preview. The preview data is removed and if animation curves exist, they are used during playback.
        specifyChannel: (create) - This flag is used with -c/channel flag. When used, applyTake will only work on the channels listed with the -c/channel flag.  C: The default is all of the enabled channels.
        startTime: (create) - The default start time for a take is determined at record time. The startTime option sets the starting time of the take in the current animation units.  C: The default is the first time stamp of the take. If a time stamp does not exist for the take, 0 is used.
    """
    ...


def autoKeyframe(*args, addAttr: str = ..., characterOption: Optional[Union[str, bool]] = ..., listAttr: bool = ..., noReset: bool = ..., state: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    With no flags, this command will set keyframes on all
    attributes that have been modified since an "autoKeyframe -state on"
    command was issued.  To stop keeping track of modified attributes,
    use "autoKeyframe -state off"
    
    autoKeyframe does not create new animation curves.  An attribute
    must have already been keyframed (with the setKeyframe command)
    for autoKeyframe to  add new keyframes for modified attributes.
    
    You can also query the current state of autoKeyframing
    with "autoKeyframe -query -state".

    Args:
        addAttr: (edit) - Add to the list of plugs (node.attribute) that autoKeyframe is currently considering for auto keying.  This list is transient and short-lived, and is reset as soon as autoKeyframe sets the keyframe or decides that no keyframe is to be set, on completion of the next set attribute.
        characterOption: (create, edit, query) - Valid options are: "standard", "all". Dictates whether when auto-keying characters the auto-key works as usual or whether it keys all of the character attributes. Default is "standard".
        listAttr: (query) - Returns the list of plugs (node.attribute) that autoKeyframe is currently considering for auto keying.  This list is transient and short-lived, and is reset as soon as autoKeyframe sets the keyframe or decides that no keyframe is to be set, on completion of the next set attribute.
        noReset: (create, edit) - Must be used in conjunction with the state/st flag. When noReset/nr is specified, the list of plugs to be autokeyed is not cleared when the state changes
        state: (create, edit, query) - turns on/off remembering of modified attributes
    """
    ...


def backgroundEvaluationManager(*args, interrupt: bool = ..., mode: Optional[Union[str, bool]] = ..., pause: bool = ..., resume: bool = ..., query: bool = ...) -> Any:
    r"""
    Allows user to pause and restart background evaluations.

    Args:
        interrupt: (create, query) - Enable or disable fast interrupt of background execution during interactive workflow.
        mode: (create, query) - Changes the current evaluation mode in the evaluation manager. Supported values are "serial" and "parallel".
        pause: (create, query) - Pause background evaluation. Will block till background evaluation is fully stopped. Can be queried to get the current state.
        resume: (create) - Resume background evaluation. Will start suspended evaluations unless someones else requested it.
    """
    ...


def bakeClip(*args, blend: Optional[Union[Tuple[int, int], bool]] = ..., clipIndex: Optional[Union[int, bool]] = ..., keepOriginals: bool = ..., name: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This command is used to bake clips and blends into a single clip.

    Args:
        blend: (create) - Specify the indices of the clips being blended.
        clipIndex: (create, multiuse) - Specify the index of the clip to bake.
        keepOriginals: (create) - Keep original clips in the trax editor and place the merged clip into the visor. The default is to schedule the merged clip, and to keep the original clips in the visor.
        name: (create) - Specify the name of the new clip to create.
    """
    ...


def bakeDeformer(*args, colorizeSkeleton: bool = ..., customRangeOfMotion: Optional[Union[Tuple[float, float], bool]] = ..., dstMeshName: Optional[Union[str, bool]] = ..., dstSkeletonName: Optional[Union[str, bool]] = ..., hierarchy: bool = ..., influences: Optional[Union[List[str], bool]] = ..., maxInfluences: Optional[Union[int, bool]] = ..., pruneWeights: Optional[Union[float, bool]] = ..., smoothWeights: Optional[Union[int, bool]] = ..., srcMeshName: Optional[Union[str, bool]] = ..., srcSkeletonName: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Given a rigged character, whose mesh shape is determined by a set of deformers, bakeDeformer calculates linear blend skin weights most closely approximating observed deformations. To do this, a test set of examples is generated by moving the rig through a range of motion. Results mesh and pose pairs are then used to solve a constrained optimization, solving for skinning weights. bakeDeformer automatically binds and applies resulting weights to the destination geometry. If the source and destination mesh/skeleton are identical, the command will replace the original deformations with a skinCluster and computed weights. See the below examples for sample usage.

    Args:
        colorizeSkeleton: (create) - The new skin cluster created will have its skeleton colorized. Must be used with the -srcSkeletonName and -dstSkeletonName flags.
        customRangeOfMotion: (create) - When this flag is specified with the frames for the range of motion to be used, the tool will step through each frame as a separate pose. Otherwise the tool will use the existing range of motion in the tool that rotates each influence 45 degrees.      Usage examples:       -rom "10:20" means all frames in the range from 10 to 20, inclusive, in the current time unit.   Omitting one end of a range means using either end of the animation range (or both), as in the following examples:   -rom "10:" means all frames from time 10 (in the current time unit) onwards to the maximum time in the animation range (on the timeline).   -rom ":10" means all frames from the minimum time on the animation range (on the timeline) up to (and including) time 10 (in the current time unit).   -rom ":" is a short form to specify all frames, from minimum to maximum time on the current animation range.    When using this flag, some of the joints in the specified range of motion may not have changed sufficiently. To improve bakeDeformer results or avoid algorithm errors, the command will return a list of influences that do not move enough in the specified range of motion. To detect these joints, the local transformation of each joint is compared between subsequent frames. We consider that a joint has sufficiently changed if any of the below criteria are met:      There is a rotation of at least 5 degrees, as determined by the shortest rotation between transforms. There is a translation of 1% or greater of the size of the largest bounding box containing all joints for each frame. There is a scaling change of at least 1%. This percentage represents the smallest scaling value over the largest scaling value (in absolute value).       If a joint has not met any of the criteria, it will be added to the warning of joints that have not moved enough.        The custom range of motion should be considered experimental.
        dstMeshName: (create) - The destination mesh name.
        dstSkeletonName: (create) - The destination skeleton name.
        hierarchy: (create) - All children of the passed joints that are used in the influences flag are used.
        influences: (create) - A list of joints that are used as the influences to determine new weights.
        maxInfluences: (create) - The maximum number of influences per vertex.
        pruneWeights: (create) - On the newly created skin cluster, set any weight below the given the value to zero (post-processing). This will call the skinPercent command as follows: "skinPercent -pruneWeights [value] [skinClusterName] [dstMeshName]" where [value] is the value passed into this flag, [skinClusterName] is the name of the new skinCluster node created after running this tool, and [dstMeshName] is the mesh provided in the -dstMeshName flag.
        smoothWeights: (create) - The number of smoothing iterations for smoothing weights (post-processing). This also renormalizes the remaining the weights.
        srcMeshName: (create) - The source mesh name.
        srcSkeletonName: (create) - The source skeleton name.
    """
    ...


def bakeResults(*args, animation: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., bakeOnOverrideLayer: bool = ..., controlPoints: bool = ..., destinationLayer: Optional[Union[str, bool]] = ..., disableImplicitControl: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., includeUpperBound: bool = ..., index: Optional[Union[int, bool]] = ..., minimizeRotation: bool = ..., oversamplingRate: Optional[Union[int, bool]] = ..., preserveOutsideKeys: bool = ..., removeBakedAnimFromLayer: bool = ..., removeBakedAttributeFromLayer: bool = ..., resolveWithoutLayer: Optional[Union[str, bool]] = ..., sampleBy: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., shape: bool = ..., simulation: bool = ..., smart: Optional[Union[List[Union[bool, float]], bool]] = ..., sparseAnimCurveBake: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command allows the user to replace a chain of dependency nodes
    which define the value for an attribute with a single animation curve.
    Command allows the user to specify the range and frequency of sampling.
    
    This command operates on a keyset. A keyset is
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
    If there are no active keys or tangents, do not do anything.
    
    
    
    objects:
    Only act on specified objects. If there are no objects specified, do not
    do anything.
    
    
    
    Note that the "-animation" flag can be used to override
    the curves uniquely identified by the multi-use
    "-attribute" flag, which takes an argument of the form
    attributeName, such as "translateX".
    
    Keys on animation curves are identified by either
    their time values or their indices. Times and indices should
    be specified as a range, as shown below.
    
    -time "10:20" means all keys in the range from 10 to 20,
    inclusive, in the current time unit.
    -index "1:5" means the 2nd, 3rd, 4th, 5th, and 6th keys of
    each animation curve.

    Args:
        animation: (create) - Where this command should get the animation to act on. Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects." See command description for details.
        attribute: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        bakeOnOverrideLayer: (create) - If true, all layered and baked attribute will be added as a top override layer.
        controlPoints: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        destinationLayer: (create) - This flag can be used to specify an existing layer where the baked results should be stored. Use this flag with caution. If the destination layer already has animation on it that contributes to the final result, it will be replaced by the output of the bake. As a result, it is possible that the combined animation visible in the scene is different before / after the baking process.
        disableImplicitControl: (create) - Whether to disable implicit control after the anim curves are obtained as the result of this command. An implicit control to an attribute is some function that affects the attribute without using an explicit dependency graph connection. The control of IK, via ik handles, is an example.
        float: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve. Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        hierarchy: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        includeUpperBound: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true. This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound. Note: when used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace." This flag has no effect on the curve pasted from the clipboard.
        index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        minimizeRotation: (create) - Specify whether to minimize the local Euler component from key to key during baking of rotation channels.
        oversamplingRate: (create) - Amount of samples per sampleBy period. Default is 1.
        preserveOutsideKeys: (create) - Whether to preserve keys that are outside the bake range when there are directly connected animation curves or a pairBlend node which has an animation curve as its direct input. The default (false) is to remove frames outside the bake range. If the channel that you are baking is not controlled by a single animation curve, then a new animation curve will be created with keys only in the bake range. In the case of pairBlend-driven channels, setting pok to true will retain both the pairBlend and its input animCurve. The blended values will be baked onto the animCurve and the weight of the pairBlend weight will be keyed to the animCurve during the baked range.
        removeBakedAnimFromLayer: (create) - If true, all baked animation will be removed from the layer. Otherwise all layer associated with the baked animation will be muted.
        removeBakedAttributeFromLayer: (create) - If true, all baked attribute will be removed from the layer. Otherwise all layer associated with the baked attribute will be muted.
        resolveWithoutLayer: (create, multiuse) - This flag can be used to specify a list of layers to be merged together during the bake process. This is a multi-use flag. Its name refers to the fact that when solving for the value to key, it determines the proper value to key on the destination layer to achieve the same result as the merged layers.
        sampleBy: (create) - Amount to sample by. Default is 1.0 in current timeUnit.
        shape: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        simulation: (create) - Using this flag instructs the command to preform a simulation instead of just evaluating each attribute separately over the range of time. The simulation flag is required to bake animation that depends on the whole scene being evaluated at each time step such as dynamics. The default is false.
        smart: (create) - Specify whether to enable smart bake and the optional smart bake tolerance.
        sparseAnimCurveBake: (create) - When this is true and anim curves are being baked, do not insert any keys into areas of the curve where animation is defined. And, use as few keys as possible to bake the pre and post infinity behavior. When this is false, one key will be inserted at each time step. The default is false.
        time: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
    """
    ...


def bakeSimulation(*args, animation: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., bakeOnOverrideLayer: bool = ..., controlPoints: bool = ..., destinationLayer: Optional[Union[str, bool]] = ..., disableImplicitControl: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., includeUpperBound: bool = ..., index: Optional[Union[int, bool]] = ..., minimizeRotation: bool = ..., preserveOutsideKeys: bool = ..., removeBakedAnimFromLayer: bool = ..., removeBakedAttributeFromLayer: bool = ..., resolveWithoutLayer: Optional[Union[str, bool]] = ..., sampleBy: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., shape: bool = ..., simulation: bool = ..., smart: Optional[Union[List[Union[bool, float]], bool]] = ..., sparseAnimCurveBake: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
    
    The bakeSimulation command is obsolete.  Instead, "bakeResults
    -simulation true" should be used.  The bakeSimulation command has
    retained for backwards compatibility.
    
    This command allows the user to replace a chain of dependency
    nodes, or implicit relationship, such as those between joints
    and IK handles, which define the value of an attribute, with a
    single animation curve. Command allows the user to specify the
    range and frequency of sampling. Unlike the bakeResults
    command, this command will actually set the time of the
    current scene to all the times, in sequence, inside the given time
    interval before it sets the time back to when it is started.
    As a result, it may modify the scene.

    Args:
        animation: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        bakeOnOverrideLayer: (create) - If true, all layered and baked attributes will be added as a top override layer.
        controlPoints: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        destinationLayer: (create) - This flag can be used to specify an existing layer where the baked results should be stored.
        disableImplicitControl: (create) - Whether to disable implicit control after the anim curves are obtained as the result of this command. An implicit control to an attribute is some function that affects the attribute without using an explicit dependency graph connection. The control of IK, via ik handles, is an example.
        float: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        hierarchy: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        includeUpperBound: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        minimizeRotation: (create) - Specify whether to minimize the local euler component from key to key during baking of rotation channels.
        preserveOutsideKeys: (create) - Whether to preserve keys that are outside the bake range when there are directly connected animation curves.  The default (false) is to remove frames outside the bake range.  If the channel that you are baking is not controlled by a single animation curve, then a new animation curve will be created with keys only in the bake range.
        removeBakedAnimFromLayer: (create) - If true, all baked animation will be removed from the layer.
        removeBakedAttributeFromLayer: (create) - If true, all baked attributes will be removed from the layer.
        resolveWithoutLayer: (create, multiuse) - This flag can be used to specify a list of layers to be merged together during the bake process. This is a multi-use flag. Its name refers to the fact that when solving for the value to key, it determines the proper value to key on the destination layer to achieve the same result as the merged layers.
        sampleBy: (create) - Amount to sample by. Default is 1.0 in current timeUnit
        shape: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        simulation: (create) - Using this flag instructs the command to preform a simulation instead of just evaluating each attribute separately over the range of time. The simulation flag is required to bake animation that that depends on the whole scene being evaluated at each time step such as dynamics. The default is true.
        smart: (create) - Specify whether to enable smart bake and the optional smart bake tolerance.
        sparseAnimCurveBake: (create) - When baking anim curves, do not insert any keys into areas of the curve where animation is defined.  And, use as few keys as possible to bake the pre and post infinity behaviors.  When this is false, one key will be inserted at each time step.  The default is false.
        time: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
    """
    ...


def bindSkin(*args, byClosestPoint: bool = ..., byPartition: bool = ..., colorJoints: bool = ..., delete: bool = ..., doNotDescend: bool = ..., enable: bool = ..., name: Optional[Union[str, bool]] = ..., partition: Optional[Union[str, bool]] = ..., toAll: bool = ..., toSelectedBones: bool = ..., toSkeleton: bool = ..., unbind: bool = ..., unbindKeepHistory: bool = ..., unlock: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command binds the currently selected objects to the
    currently selected skeletons.  Shapes which can be bound are:
    meshes, nurbs curves, nurbs surfaces, lattices, subdivision
    surfaces, and API shapes. Multiple shapes and multiple skeletons can be
    bound at once by selecting them or specifying them on the command
    line. Selection order is not important.
    
    The skin is bound using the so-called "rigid" bind, in which
    the components are rigidly attached to the closest bone in the
    skeleton. Flexors can later be added to the skeleton to
    smooth out the skinning around joints.
    
    The skin(s) can be bound either to the entire skeleton hierarchy
    of the selected joint(s), or to only the selected joints. The
    entire hierarchy is the default. The -tsb/-toSelectedBones flag
    allows binding to only the selected bones.
    
    This command can also be used to detach the skin from the skeleton.
    Detaching the skin is useful in a variety of situations, such as:
    inserting additional bones, deleting bones, changing the bind
    position of the skeleton or skin, or simply getting rid of the
    skinning nodes altogether. The options to use when detaching the
    skin depend on how much of the skinning info you want to get rid
    of. Namely: (1) -delete or -unbind: remove all skinning nodes, (2) -unbindKeepHistory: remove the skinning sets, but keep the weights, (3) -disable: disable the skinning but keep the skinning sets and the weights.

    Args:
        byClosestPoint: (create) - bind each point in the object to the segment closest to the point. The byClosestPoint and byPartition flags are mutually exclusive.  The byClosestPoint flag is the default.
        byPartition: (create) - bind each group in the partition to the segment closest to the group's centroid. A partition must be specified with the -p/-partition flag
        colorJoints: (create) - In bind mode, this flag assigns colors to the joints based on the colors assigned to the joint's skin set. In delete and unlock mode, this flag removes the colors from joints that are no longer bound as skin. In disable and unbindKeepHistory mode, this flag does nothing.
        delete: (create) - Detach the skin on the selected skeletons and remove all bind- related construction history.
        doNotDescend: (create) - Do not descend to shapes that are parented below the selected object(s). Bind only the selected objects.
        enable: (create) - Enable or disable a bind that has been disabled on the selected skeletons. To enable the bind on selected bones only, select the bones and use the -tsb flag with the -en flag. This flag is used when you want to temporarily disable the bind without losing the set information or the weight information of the skinning, for example if you want to modify the bindPose.
        name: (create) - This flag is obsolete.
        partition: (create) - Specify a partition to bind by. This is only valid when used with the -bp/-byPartition flag.
        toAll: (create) - objects will be bound to the entire selected skeletons. Even bones with zero influence will be bound, whereas the toSkeleton will only bind non-zero influences.
        toSelectedBones: (create) - objects will be bound to the selected bones only.
        toSkeleton: (create) - objects will be bound to the selected skeletons. The toSkeleton, toAll and toSelectedBones flags are mutually exclusive. The toSkeleton flag is the default.
        unbind: (create) - unbind the selected objects. They will no longer move with the skeleton. Any bindSkin history that is no longer used will be deleted.
        unbindKeepHistory: (create) - unbind the selected objects. They will no longer move with the skeleton. However, existing weights on the skin will be kept for use the next time the skin is bound. This option is appropriate if you want to modify the skeleton without losing the weighting information on the skin.
        unlock: (create) - unlock the selected objects. Since bindSkin will no longer give normal results if bound objects are moved away from the skeleton, bindSkin locks translate, rotate and scale. This command unlocks the selected objects translate, rotate and scale.
    """
    ...


def blendShape(*args, after: bool = ..., afterReference: bool = ..., automatic: bool = ..., before: bool = ..., components: bool = ..., copyDelta: Tuple[int, int, int] = ..., copyInBetweenDelta: Tuple[int, int, int, int] = ..., copyWeights: Tuple[int, int, int] = ..., deformerTools: bool = ..., envelope: Optional[Union[float, bool]] = ..., exclusive: Optional[Union[str, bool]] = ..., export: str = ..., exportTarget: Tuple[int, int] = ..., flipTarget: Tuple[int, int] = ..., frontOfChain: bool = ..., geometry: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., ignoreSelected: bool = ..., ip: str = ..., inBetween: bool = ..., inBetweenIndex: int = ..., inBetweenType: Optional[Union[str, bool]] = ..., includeHiddenSelections: bool = ..., mergeSource: int = ..., mergeTarget: int = ..., mirrorDirection: int = ..., mirrorTarget: Tuple[int, int] = ..., name: Optional[Union[str, bool]] = ..., normalizationGroups: bool = ..., origin: Optional[Union[str, bool]] = ..., parallel: bool = ..., prune: bool = ..., remove: bool = ..., resetTargetDelta: Tuple[int, int] = ..., selectedComponents: bool = ..., split: bool = ..., suppressDialog: bool = ..., symmetryAxis: Optional[Union[str, bool]] = ..., symmetryEdge: Optional[Union[str, bool]] = ..., symmetrySpace: Optional[Union[int, bool]] = ..., tangentSpace: bool = ..., target: Optional[Union[Tuple[str, int, str, float], bool]] = ..., topologyCheck: bool = ..., transform: Optional[Union[str, bool]] = ..., useComponentTags: bool = ..., weight: Optional[Union[Tuple[int, float], bool]] = ..., weightCount: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a blendShape deformer, which blends in specified
    amounts of each target shape to the initial base shape.
    Each base shape is deformed by its own set of target shapes.
    Every target shape has an index that associates it with one of
    the shape weight values.
    
    In the create mode the first item on the selection list is treated
    as the base and the remaining inputs as targets. If the first item
    on the list has multiple shapes grouped beneath it, the targets must
    have an identical shape hierarchy. Additional base shapes
    can be added in edit mode using the deformers -g flag.

    Args:
        after: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        automatic: (create, edit) - The -automatic flag is used to specify deformer ordering in a way that choses between -frontOfChain and -before automatically. If the geometry being deformed is only affected by invertible deformers, the -frontOfChain mode is used, otherwise the -before mode is used.
        before: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        components: (query) - Returns the components used by the deformer
        copyDelta: (edit) - Set the base, source, and destination delta index values.
        copyInBetweenDelta: (edit) - Set the base, target, source, and destination delta index values.
        copyWeights: (edit) - Copy base, source, and destination weight index values.
        deformerTools: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        envelope: (create, edit, query) - Set the envelope value for the deformer, controlling how much of the total deformation gets applied. Default is 1.0.
        exclusive: (create, query) - Puts the deformation set in a deform partition.
        export: (edit) - Export the shapes to the named file path.
        exportTarget: (edit, multiuse) - Specify the base and target index pairs for the export.
        flipTarget: (edit, multiuse) - Flip the list of base and target pairs.
        frontOfChain: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        ip: (edit) - Import the shapes from the named file path.
        inBetween: (create, edit) - Indicate that the specified target should serve as an inbetween. An inbetween target is one that serves as an intermediate target between the base shape and another target.
        inBetweenIndex: (edit) - Only used with the -rtd/-resetTargetDelta flag to remove delta values for points in the inbetween target geometry defined by this index.
        inBetweenType: (create, edit) - Specify if the in-between target to be created is relative to the hero target or if it is absolute. If it is relative to hero targets, the in-between target will get any changes made to the hero target. Valid values are "relative" and "absolute". This flag should always be used with the -ib/-inBetween and -t/-target flags.
        includeHiddenSelections: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        mergeSource: (edit, multiuse) - List of source indexes for a merge.
        mergeTarget: (edit) - Target index of a merge
        mirrorDirection: (edit) - Mirror direction; 0 = negative, 1 = positive
        mirrorTarget: (edit, multiuse) - Mirror the list of base and target pairs.
        name: (create) - Used to specify the name of the node being created.
        normalizationGroups: (query) - Returns a list of the used normalization group IDs.
        origin: (create) - blendShape will be performed with respect to the world by default. Valid values are "world" and "local". The local flag will cause the blend shape to be performed with respect to the shape's local origin.
        parallel: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        prune: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        remove: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        resetTargetDelta: (edit, multiuse) - Remove all delta values for points in the target geometry, including all sequential targets defined by target index. Parameter list:  uint: the base object index uint: the target index
        selectedComponents: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        split: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        suppressDialog: (create, edit) - Suppress dialog box and run the command as defined by the user.
        symmetryAxis: (edit, query) - Axis for symmetry. Valid values are "X", "Y", and "Z".
        symmetryEdge: (edit, multiuse, query) - One or two symmetry edge names, separated by a ".". See the blendShape node's symmetryEdge attribute for legal values.
        symmetrySpace: (edit, query) - Space for symmetry. 0 = Topological, 1 = Object, 2 = UV
        tangentSpace: (create, edit) - Indicate that the delta of the specified target should be relative to the tangent space of the surface.
        target: (create, edit, multiuse, query) - Set target object as the index target shape for the base shape base object. The full influence of target shape takes effect when its shape weight is targetValue. Parameter list:  string: the base object int: index string: the target object double: target value
        topologyCheck: (create) - Set the state of checking for a topology match between the shapes being blended. Default is on.
        transform: (edit, query) - Set transform for target, then the deltas will become relative to a post transform. Typically the best workflow for this option is to choose a joint that is related to the fix you have introduced. This flag should be used only if the "Deformation order" of blendShape node is "Before".
        useComponentTags: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
        weight: (create, edit, multiuse, query) - Set the weight value (second parameter) at index (first parameter).
        weightCount: (create, edit, query) - Set the number of shape weight values.
    """
    ...


def blendShapeEditor(*args, control: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., exists: bool = ..., filter: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., highlightConnection: Optional[Union[str, bool]] = ..., lockMainConnection: bool = ..., mainListConnection: Optional[Union[str, bool]] = ..., panel: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., selectionConnection: Optional[Union[str, bool]] = ..., stateString: bool = ..., targetControlList: bool = ..., targetList: bool = ..., unParent: bool = ..., unlockMainConnection: bool = ..., updateMainConnection: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., verticalSliders: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates an editor that derives from the base editor
    class that has controls for blendShape, control nodes.

    Args:
        control: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag: (create, edit, query) - Attaches a tag to the editor.
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        filter: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        forceMainConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        highlightConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        lockMainConnection: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        mainListConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        panel: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        selectionConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        stateString: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        targetControlList: (query) - 
        targetList: (query) - 
        unParent: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
        verticalSliders: (create, edit, query) - 
    """
    ...


def blendShapePanel(*args, blendShapeEditor: bool = ..., control: bool = ..., copy: str = ..., createString: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., editString: bool = ..., exists: bool = ..., init: bool = ..., isUnique: bool = ..., label: Optional[Union[str, bool]] = ..., menuBarRepeatLast: bool = ..., menuBarVisible: bool = ..., needsInit: bool = ..., parent: Optional[Union[str, bool]] = ..., popupMenuProcedure: Optional[Union[str, bool]] = ..., replacePanel: str = ..., tearOff: bool = ..., tearOffCopy: Optional[Union[str, bool]] = ..., tearOffRestore: bool = ..., unParent: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a panel that derives from the base panel
    class that houses a blendShapeEditor.

    Args:
        blendShapeEditor: (query) - Query only flag that returns the name of an editor to be associated with the panel.
        control: (query) - Returns the top level control for this panel. Usually used for getting a parent to attach popup menus. CAUTION: panels may not have controls at times.  This flag can return "" if no control is present.
        copy: (edit) - Makes this panel a copy of the specified panel.  Both panels must be of the same type.
        createString: (edit) - Command string used to create a panel
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag: (create, edit, query) - Attaches a tag to the Maya panel.
        editString: (edit) - Command string used to edit a panel
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        init: (create, edit) - Initializes the panel's default state.  This is usually done automatically on file -new and file -open.
        isUnique: (query) - Returns true if only one instance of this panel type is allowed.
        label: (edit, query) - Specifies the user readable label for the panel.
        menuBarRepeatLast: (create, edit, query) - Controls whether clicking on the menu header with the middle mouse button would repeat the last selected menu item.
        menuBarVisible: (create, edit, query) - Controls whether the menu bar for the panel is displayed.
        needsInit: (edit, query) - (Internal) On Edit will mark the panel as requiring initialization. Query will return whether the panel is marked for initialization.  Used during file -new and file -open.
        parent: (create) - Specifies the parent layout for this panel.
        popupMenuProcedure: (edit, query) - Specifies the procedure called for building the panel's popup menu(s). The default value is "buildPanelPopupMenu".  The procedure should take one string argument which is the panel's name.
        replacePanel: (edit) - Will replace the specified panel with this panel.  If the target panel is within the same layout it will perform a swap.
        tearOff: (edit, query) - Will tear off this panel into a separate window with a paneLayout as the parent of the panel. When queried this flag will return if the panel has been torn off into its own window.
        tearOffCopy: (create) - Will create this panel as a torn of copy of the specified source panel.
        tearOffRestore: (create, edit) - Restores panel if it is torn off and focus is given to it. If docked, becomes the active panel in the docked window. This should be the default flag that is added to all panels instead of -to/-tearOff flag which should only be used to tear off the panel.
        unParent: (edit) - Specifies that the panel should be removed from its layout. This (obviously) cannot be used with query.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
    """
    ...


def blendTwoAttr(*args, attribute: Optional[Union[str, bool]] = ..., attribute0: Optional[Union[str, bool]] = ..., attribute1: Optional[Union[str, bool]] = ..., blender: Optional[Union[str, bool]] = ..., controlPoints: bool = ..., driver: Optional[Union[int, bool]] = ..., name: Optional[Union[str, bool]] = ..., shape: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    A blendTwoAttr nodes takes two inputs, and blends the values of the inputs
    from one to the other, into an output value. The blending of the two
    inputs uses a blending function, and the following formula:
    
         (1 - blendFunction) * input[0]  +  blendFunction * input[1] 
    
    The blendTwoAttr command can be used to blend the animation of an
    object to transition smoothly between the animation of two other
    objects.
    
    When the blendTwoAttr command is issued, it creates a blendTwoAttr
    node on the specified attributes, and reconnects whatever was previously
    connected to the attributes to the new blend nodes. You may also
    specify which two attributes should be used to blend together.
    
    The driver is used when you want to keyframe an object after it is
    being animated by a blend node. The current driver index specifies
    which of the two blended attributes should be keyframed.

    Args:
        attribute: (create, multiuse) - A list of attributes for the selected nodes for which a blendTwoAttr node will be created.       In query mode, this flag needs a value.
        attribute0: (create, edit, query) - The attribute that should be connected to the first input of the new blendTwoAttr node. When queried, it returns a string.
        attribute1: (create, edit, query) - The attribute that should be connected to the second input of the new blendTwoAttr node. When queried, it returns a string.
        blender: (create, edit, query) - The blender attribute. This is the attribute that will be connected to the newly created blendTwoAttr node(s) blender attribute. This attribute controls how much of each of the two attributes to use in the blend. If this flag is not specified, a new animation curve is created whose value goes from 1 to 0 throughout the time range specified by the -t flag. If -t is not specified, an abrupt change from the value of the first to the value of the second attribute will occur at the current time when this command is issued.
        controlPoints: (create) - Explicitly specify whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.
        driver: (create, edit, query) - The index of the driver attribute for this blend node (0 or 1) When queried, it returns an integer.
        name: (create, query) - name for the new blend node(s)
        shape: (create) - Consider all attributes of shapes below transforms as well, except "controlPoints". Default: true
        time: (create) - The time range between which the blending between the 2 attributes should occur. If a single time is specified, then the blend will cause an abrupt change from the first to the second attribute at that time.  If a range is specified, a smooth blending will occur over that time range. The default is to make a sudden transition at the current time.
    """
    ...


def bluePencilDrawCtx(*args, edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to create the blue pencil drawing context.

    Args:
    """
    ...


def bluePencilFrame(*args, activeViewport: bool = ..., clear: bool = ..., copy: bool = ..., cutFrame: bool = ..., delete: bool = ..., duplicate: bool = ..., exportFrames: bool = ..., importFrames: bool = ..., insert: bool = ..., move: Optional[Union[Tuple[int, int, int], bool]] = ..., moveCopy: Optional[Union[Tuple[int, int, int], bool]] = ..., moveToNext: bool = ..., paste: bool = ..., relative: bool = ..., retime: Optional[Union[int, bool]] = ..., scale: Optional[Union[Tuple[float, bool, int, int], bool]] = ..., scaleCopy: Optional[Union[Tuple[float, bool, int, int], bool]] = ..., stepBack: bool = ..., stepForward: bool = ...) -> Any:
    r"""
    Command to create or edit blue pencil frames.

    Args:
        activeViewport: (create) - Create the frame in the active viewport's camera.
        clear: (create) - Erase the data from one or more frames using the highlighted range in Maya's time slider.
        copy: (create) - Copy the frame data in the selected range to the clipboard.
        cutFrame: (create) - Copy the frame data in the selected range to the clipboard and remove the frames.
        delete: (create) - Remove one or more frames using the highlighted range in Maya's time slider.
        duplicate: (create) - Insert a frame at the current time that is a duplicate of the previous frame.
        exportFrames: (create) - Show blue pencil export frame dialog.
        importFrames: (create) - Show blue pencil import frame dialog.
        insert: (create) - Insert one or more empty frames using the highlighted range in the time slider.
        move: (create) - Move the frames in the specified range by the given offset. Arguments are offset, range start, range end.
        moveCopy: (create) - Copy then move the frames in the specified range by the given offset. Arguments are offset, range start, range end.
        moveToNext: (create) - Move the current time to the next frame after retiming.
        paste: (create) - Create new frames using the data in the clipboard at the current time.
        relative: (create) - Set the retime action to shift the frames by a relative amount to add or remove space between frames. When the flag is not set, the spacing between the frames is set to the retime value.
        retime: (create) - Shift frames or change the frame spacing in a selected range.
        scale: (create) - Scale the frames in the specified range by the given factor. Arguments are scale factor, scale from end (true) or beginning (false), range start, range end.
        scaleCopy: (create) - Copy then scale the frames in the specified range by the given factor. Arguments are scale factor, scale from end (true) or beginning (false), range start, range end.
        stepBack: (create) - Set the current time to the previous blue pencil frame's time.
        stepForward: (create) - Set the current time to the next blue pencil frame's time.
    """
    ...


def bluePencilLayer(*args, active: Optional[Union[int, bool]] = ..., addLayer: bool = ..., count: bool = ..., delete: int = ..., deleteAll: bool = ..., editLocked: Tuple[bool, int] = ..., editName: Tuple[str, int] = ..., editOpacity: Tuple[float, int] = ..., editState: Tuple[int, int] = ..., editVis: Tuple[bool, int] = ..., insert: int = ..., layerState: Tuple[int, int] = ..., move: Tuple[int, int] = ..., moveAll: bool = ..., name: Tuple[str, int] = ..., newCamera: str = ..., queryLocked: int = ..., queryName: int = ..., queryOpacity: int = ..., queryState: int = ..., queryVis: int = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to manage blue pencil layers. The command requires a camera name as argument.

    Args:
        active: (create, edit, query) - Sets the active layer index. Query returns the active layer index.
        addLayer: () - Creates a new layer.
        count: () - Returns the number of layers.
        delete: () - Removes the layer at the specified index.
        deleteAll: () - Removes all layers.
        editLocked: () - Edit the layer's locked state.
        editName: () - Sets name of the layer at the specified index.
        editOpacity: () - Sets the opacity of the layer at the specified index.
        editState: () - Edits the layer's state. 0: animated, 1: static.
        editVis: () - Sets the visibility of the layer at the specified index.
        insert: () - Creates a new layer at the given index.
        layerState: () - Sets the layer state when adding a new layer. 0: animated, 1: static.
        move: () - Moves a layer from one index to another.
        moveAll: () - Moves all layers from the current camera to the given camera.
        name: () - Sets the name of the new layer when using addLayer or insertLayer.
        newCamera: () - Sets a new camera to move layers to when using the move test.
        queryLocked: () - Query the layer's locked state.
        queryName: () - Returns the specified layer's name.
        queryOpacity: () - Returns the specified layer's opacity.
        queryState: () - Queries the layer's state. 0: animated, 1: static.
        queryVis: () - Returns the specified layer's visibility.
    """
    ...


def bluePencilNode(*args, camera: Optional[Union[str, bool]] = ..., exists: bool = ..., frame: bool = ..., layer: bool = ..., layerName: Optional[Union[str, bool]] = ..., layerState: Optional[Union[int, bool]] = ..., refresh: bool = ..., refreshGhosting: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to create the blue pencil node.

    Args:
        camera: (create, query) - Specifies the camera on which to create a new layer when creating the node. Query returns the name of the active camera.
        exists: (create) - Returns true if the blue pencil node has been created.
        frame: (create) - Creates a new frame when creating the new layer when creating the node.
        layer: (create) - Create a new layer when creating the node.
        layerName: (create) - Specifies the layer name of the new layer when creating the node.
        layerState: (create) - Specifies the layer state of the new layer. 0: Animated, 1: Static.
        refresh: (create) - Refresh the viewport of the active camera.
        refreshGhosting: (create) - Refresh the ghosting information.
    """
    ...


def bluePencilStroke(*args, frameAdded: bool = ..., layerAdded: Optional[Union[int, bool]] = ...) -> Any:
    r"""
    Command used to commit active blue pencil strokes.

    Args:
        frameAdded: (create) - The index of the frame added for the new stroke. This is set to remove it when undoing.
        layerAdded: (create) - Sets the index of the added layer to remove it when undoing.
    """
    ...


def bluePencilUtil(*args, adjustBrushSize: bool = ..., adjustOpacity: bool = ..., arrowOptions: Optional[Union[Tuple[int, int], bool]] = ..., arrowTool: bool = ..., brushOptions: Optional[Union[Tuple[int, int, int, int, int], bool]] = ..., brushTool: bool = ..., draw: bool = ..., drawColor: Optional[Union[Tuple[int, int, int], bool]] = ..., ellipseOptions: Optional[Union[Tuple[int, int], bool]] = ..., ellipseTool: bool = ..., eraserOptions: Optional[Union[Tuple[int, int, int, int, int], bool]] = ..., eraserTool: bool = ..., ghostColorNext: Optional[Union[Tuple[int, int, int], bool]] = ..., ghostColorOverride: bool = ..., ghostColorPrevious: Optional[Union[Tuple[int, int, int], bool]] = ..., ghostNext: bool = ..., ghostNextCount: Optional[Union[int, bool]] = ..., ghostPrevious: bool = ..., ghostPreviousCount: Optional[Union[int, bool]] = ..., layerManager: bool = ..., layerProperties: bool = ..., lineOptions: Optional[Union[Tuple[int, int], bool]] = ..., lineTool: bool = ..., pencilOptions: Optional[Union[Tuple[int, int, int, int], bool]] = ..., pencilTool: bool = ..., rectangleOptions: Optional[Union[Tuple[int, int], bool]] = ..., rectangleTool: bool = ..., refreshLayerManager: bool = ..., refreshTimelineDisplay: bool = ..., resetTool: bool = ..., textFontFamily: Optional[Union[str, bool]] = ..., textOptions: Optional[Union[Tuple[int, int, str], bool]] = ..., textTool: bool = ..., timelineFrameDisplay: Optional[Union[int, bool]] = ..., transform: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Utility commands for blue pencil tool.

    Args:
        adjustBrushSize: (create, edit, query) - Activates or deactivates the mode to adujst the brush size by dragging.
        adjustOpacity: (create, edit, query) - Activates or deactivates the mode to adujst the brush opacity by dragging.
        arrowOptions: (create, edit, query) - Set the arrow options. The arguments are size, opacity.
        arrowTool: (create, edit, query) - Activates the arrow tool. When queried, returns true if the arrow tool is active.
        brushOptions: (create, edit, query) - Sets the brush options. The arguments in order are size, opacity, hardness pressure opacity, pressure size.
        brushTool: (create, edit, query) - Activates the brush tool. When queried, returns true if the brush tool is active.
        draw: (create, edit, query) - Activates the drawing tool context. When queried, returns true if the drawing tool context is active.
        drawColor: (create, edit, query) - Sets the current drawing color. Color format is RGB with values from 0-255. When queried, returns the current drawing color.
        ellipseOptions: (create, edit, query) - Sets the ellipse options. The arguments are size, opacity.
        ellipseTool: (create, edit, query) - Activates the ellipse tool. When queried, returns true if the ellipse tool is active.
        eraserOptions: (create, edit, query) - Sets the brush options. The arguments in order are size, opacity, hardness pressure opacity, pressure size.
        eraserTool: (create, edit, query) - Activates the eraser tool. When queried, returns true if the eraser tool is active.
        ghostColorNext: (create, edit, query) - Sets the color for the ghosts of next frames.
        ghostColorOverride: (create, edit, query) - Activates or deactivates the color override for the ghosts.
        ghostColorPrevious: (create, edit, query) - Sets the color for the ghosts of previous frames.
        ghostNext: (create, edit, query) - Activates or deactivates the ghosting of next frames.
        ghostNextCount: (create, edit, query) - Sets the number of ghosts of next frames.
        ghostPrevious: (create, edit, query) - Activates or deactivates the ghosting of previous frames.
        ghostPreviousCount: (create, edit, query) - Sets the number of ghosts of previous frames.
        layerManager: (create, edit, query) - Shows the layer manager by showing the tool settings window. Query returns if the layer manager is shown.
        layerProperties: (create, edit, query) - Show the layer properties dialog.
        lineOptions: (create, edit, query) - Sets the line options. The arguments are size, opacity.
        lineTool: (create, edit, query) - Activates the line tool. When queried, returns true if the line tool is active.
        pencilOptions: (create, edit, query) - Sets the pencil options. The arguments in order are size, opacity, pressure opacity, pressure size.
        pencilTool: (create, edit, query) - Activates the pencil tool. When queried, returns true if the pencil tool is active.
        rectangleOptions: (create, edit, query) - Sets the rectangle options. The arguments are size, opacity.
        rectangleTool: (create, edit, query) - Activates the rectangle tool. When queried, returns true if the rectangle tool is active.
        refreshLayerManager: (create, edit, query) - Refresh the layer manager.
        refreshTimelineDisplay: (create, edit, query) - Refresh the timeline display frames.
        resetTool: (create, edit, query) - Restore tool settings to default values.
        textFontFamily: (create, edit, query) - Sets the text font family.
        textOptions: (create, edit, query) - Sets the text options. The arguments in order are size, opacity, font family name.
        textTool: (create, edit, query) - Activates the text tool. When queried, returns true if the text tool is active.
        timelineFrameDisplay: (create, edit, query) - Sets the display mode for blue pencil frames in the timeline. Modes:  0 Show always 1 Show when context is active 2 Hide
        transform: (create, edit, query) - Activates the transform tool context. When queried, returns true if the transform tool context is active.
    """
    ...


def boneLattice(*args, after: bool = ..., afterReference: bool = ..., before: bool = ..., bicep: Optional[Union[float, bool]] = ..., components: bool = ..., deformerTools: bool = ..., exclusive: Optional[Union[str, bool]] = ..., frontOfChain: bool = ..., geometry: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., joint: Optional[Union[str, bool]] = ..., lengthIn: Optional[Union[float, bool]] = ..., lengthOut: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., parallel: bool = ..., prune: bool = ..., remove: bool = ..., selectedComponents: bool = ..., split: bool = ..., transform: Optional[Union[str, bool]] = ..., tricep: Optional[Union[float, bool]] = ..., useComponentTags: bool = ..., widthLeft: Optional[Union[float, bool]] = ..., widthRight: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates/edits/queries a boneLattice deformer. The name of
    the created/edited object is returned. Usually you would make use of
    this functionality through the higher level flexor command.

    Args:
        after: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        bicep: (create, edit, query) - Affects the bulging of lattice points on the inside of the bend. Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.
        components: (query) - Returns the components used by the deformer
        deformerTools: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        exclusive: (create, query) - Puts the deformation set in a deform partition.
        frontOfChain: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        joint: (create, edit, query) - Specifies which joint will be used to drive the bulging behaviors.
        lengthIn: (create, edit, query) - Affects the location of lattice points along the upper half of the bone. Positive/negative values cause the points to move away/towards the center of the bone.  Changing this parameter also modifies the regions affected by the creasing, rounding and width parameters. Default value is 0.0. When queried, this flag returns a float.
        lengthOut: (create, edit, query) - Affects the location of lattice points along the lower half of the bone. Positive/negative values cause the points to move away/towards the center of the bone.  Changing this parameter also modifies the regions affected by the creasing, rounding and width parameters. Default value is 0.0. When queried, this flag returns a float.
        name: (create) - Used to specify the name of the node being created.
        parallel: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        prune: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        remove: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        selectedComponents: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        split: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        transform: (create) - Specifies which dag node is being used to rigidly transform the lattice which this node is going to deform.  If this flag is not specified an identity matrix will be assumed.
        tricep: (create, edit, query) - Affects the bulging of lattice points on the outside of the bend. Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.
        useComponentTags: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
        widthLeft: (create, edit, query) - Affects the bulging of lattice points on the left side of the bend. Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.
        widthRight: (create, edit, query) - Affects the bulging of lattice points on the right side of the bend. Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.
    """
    ...


def bufferCurve(*args, animation: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., controlPoints: bool = ..., exists: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., includeUpperBound: bool = ..., index: Optional[Union[int, bool]] = ..., overwrite: bool = ..., shape: bool = ..., swap: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., useReferencedCurve: bool = ..., query: bool = ...) -> Any:
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
    
    This command helps manage buffer curve for animated objects

    Args:
        animation: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        controlPoints: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        exists: (query) - Returns true if a buffer curve currently exists on the specified attribute; false otherwise.
        float: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        hierarchy: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        includeUpperBound: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        overwrite: (create) - Create a buffer curve.  "true" means create a buffer curve whether or not one already existed.  "false" means if a buffer curve exists already then leave it alone.  If no flag is specified, then the command defaults to -overwrite false
        shape: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        swap: (create) - For animated attributes which have buffer curves, swap the buffer curve with the current animation curve
        time: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
        useReferencedCurve: (create, query) - In create mode, sets the buffer curve to the referenced curve. Curves which are not from file references will ignore this flag. In query mode, returns true if the selected keys are displaying their referenced curve as the buffer curve, and false if they are not.
    """
    ...


def buildBookmarkMenu(*args, editor: Optional[Union[str, bool]] = ..., type: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This command handles building the "dynamic" Bookmark
    menu, to show all bookmarks ("sets") of a specified
    type ("sets -text")
    
    menuName is the string returned by the "menu" command.

    Args:
        editor: (create) - Name of the editor which this menu belongs to
        type: (create) - Type of bookmark (sets -text) to display
    """
    ...


def buildKeyframeMenu(*args) -> Any:
    r"""
    This command handles building the "dynamic" Keyframe
    menu, to show attributes of currently selected objects,
    filtered by the current manipulator.
    
    menuName is the string returned by the "menu" command.
    The target menu will entries appended to it (and deleted from it) to always
    show what's currently keyframable.

    Args:
    """
    ...


def cacheEvaluator(*args, cacheFillMode: Optional[Union[str, bool]] = ..., cacheFillOrder: Optional[Union[str, bool]] = ..., cacheInvalidate: Optional[Union[Tuple[float, float], bool]] = ..., cacheName: Optional[Union[str, bool]] = ..., cachedFrames: bool = ..., cachingPoints: bool = ..., creationParameters: bool = ..., delegateEvaluation: bool = ..., dynamicsAsyncRefresh: bool = ..., dynamicsSupportActive: bool = ..., dynamicsSupportEnabled: bool = ..., flushCache: Optional[Union[str, bool]] = ..., flushCacheRange: Optional[Union[Tuple[Tuple[float, float], bool], bool]] = ..., flushCacheSync: bool = ..., flushCacheWait: bool = ..., hybridCacheMode: Optional[Union[str, bool]] = ..., layeredEvaluationActive: bool = ..., layeredEvaluationCachingPoints: bool = ..., layeredEvaluationEnabled: bool = ..., listCacheNames: bool = ..., listCachedNodes: bool = ..., listValueNames: bool = ..., newAction: Optional[Union[str, bool]] = ..., newActionParam: Optional[Union[str, bool]] = ..., newFilter: Optional[Union[str, bool]] = ..., newFilterParam: Optional[Union[str, bool]] = ..., newRule: Optional[Union[str, bool]] = ..., newRuleParam: Optional[Union[str, bool]] = ..., pauseInvalidation: bool = ..., preventFrameSkip: bool = ..., resetRules: bool = ..., resourceUsage: bool = ..., resumeInvalidation: bool = ..., safeMode: bool = ..., safeModeMessages: bool = ..., safeModeTriggered: bool = ..., valueName: Optional[Union[str, bool]] = ..., waitForCache: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command controls caching configuration.  It allows interaction with the
    caching system.
    
    
    Caching configuration is done through a set of rules.  Most rules are composed
    of a "filter", which is the test to be perform in order to determine if the rule
    should be applied, and an "action", which is the effect that the rule application
    should have on nodes that satisfy the criteria.
    
    
    A caching mode is therefore a set of rules that determines which nodes are
    being cached.  This mode can be serialized to a JSON string using the
    "creationParameters" flag in query mode.
    
    Built-in Cache Configuration Modes
    A few cache configuration rules, filters and actions are provided in order to
    support the built-in default caching modes.
    Built-in Filters
    
    
    evaluationCacheNodes
    This filter matches all nodes for which the node type is in the default supported
    list for evaluation cache.  See the code example below for the current list of
    supported types.
    
    
    
    nodeTypes
    This filter matches all nodes for which the node type is in the list provided with
    the newFilterParam flag.  The parameter string is a list of comma-separated
    node types, prefixed with either '-' or '+'.  The filter will go through the list
    in order and will stop if the node is of the given node type (or any derived node type).
    If the prefix is '-', the filter will return that the node did not match and stop
    processing.  If the prefix is '+', the filter will return a match and stop processing.
    
    
    
    downstreamNodeTypes
    This filter matches all nodes for which the node type is in the list provided with
    the newFilterParam flag if they also have immediate downstream nodes of the right node type(s).
    The parameter string is in the form "type=+type1,+type2 downstreamTypes=+type3,+type3",
    where the list of node types uses the same semantic as the nodeTypes filter.
    
    
    
    vp2CacheNodes
    This filter matches all nodes for which the node type is in the list of node types
    supported by VP2 caching.  Enabling VP2 caching for other node types will have no effect.
    See the comments in the code example below for the current list of supported types.
    
    
    
    vp2FallbackNodes
    This filter matches all nodes for which VP2 caching should revert to evaluation
    caching because of unsupported features.  Namely, it matches nodes for which VP2
    caching is enabled but which have animated visibility or animated topology
    (potentially changing number of vertices, edges, faces, etc.).  It also matches nodes
    with static geometry, i.e. for which nothing needs to be cached in VP2 format for
    each frame.
    
    
    
    hybridCache
    This filter matches all nodes already grabbed by the deformer evaluator, according
    to a parameter controlling which meshes are considered.  The newFilterParam
    can take the following values for the "mode" parameter: "mode=disabled" turns this filter into a no-op that always
    return false, "mode=smp" will return true for nodes that are part of a deformer evaluator
    cluster with at least one mesh using Smooth Mesh Preview, "mode=all" will return true for
    all nodes that are part of a deformer evaluator cluster, "mode=usePreference" will use
    the "Hybrid cache" preference from the Cached Playback preferences.  The newFilterParam
    also accepts the "allowAnimatedInput" parameter with the following values: "allowAnimatedInput=0"
    (the default value) will not consider the mesh if it is part of a cluster for which one of the
    input geometry is animated.  Such setups lose the benefits of hybrid cache, since the input
    geometry needs to be cached in order to be fed to the GPU deformer, but since the geometry is
    animated, it takes about the same amount of memory as caching the output.  "allowAnimatedInput=1"
    removes this filtering and allows meshes to be grabbed regardless of whether the input is animated
    or not.
    
    
    
    Built-in Actions
    
    
    enableEvaluationCache
    This action enables evaluation cache on the matched node.  If the evaluation cache
    is already enabled, it has no effect.
    
    
    
    disableEvaluationCache
    This action disables evaluation cache on the matched node.  If the evaluation cache
    is already disabled, it has no effect.
    
    
    
    disableAllCache
    This action disables all types of caching on the matched node.
    
    
    
    enableVP2Cache
    This action enables VP2 cache on the matched node.  "useHardware=1" can be
    passed to the newActionParam in order to enable the VP2 hardware cache,
    while "useHardware=0" will use the VP2 software cache.
    This action disables the evaluation cache (to only keep VP2 cache)
    on the matched node to save memory.  Specifying "useEvaluation=1"
    to turn on evaluation cache (along with VP2 cache). For example, NURBS surfaces
    keep the evaluation cache to make the selection highlighting more efficient.
    This action also automatically applies the fallback to evaluation cache rule for
    safety if required.  This fallback will be applied if the node matches the criteria
    from the "vp2FallbackNodes" filter and will then apply the action from the
    "fallbackFromVP2CacheToEvaluationCache" action.  "fallback=0" can be used to
    disable this fallback, but doing so can cause correctness issues,instabilities and
    even crashes.  "useEvaluation=0" does not affect the fallback behavior.
    To use multiple parameters, separate them with ' ' like
    "useHardware=1 fallback=0 useEvaluation=1".
    
    
    
    disableVP2Cache
    This action disables the VP2 cache on the matched node.  If the VP2 cache
    is already disabled, it has no effect.
    
    
    
    fallbackFromVP2CacheToEvaluationCache
    This action disables the VP2 cache on the matched node and enables the evaluation
    cache instead.
    
    
    
    delegateEvaluation
    This action enables delegate evaluation on the matched nodes and all nodes in
    the same cluster.  This means that these nodes will not be cached and will be evaluated
    at every frame.  As a result, nodes set to delegate to evaluation must not have any downstream
    node that is not also set to delegate evaluation.  Also, all input (i.e. direct parent or upstream)
    nodes to the delegate evaluation nodes will be added as caching points to make sure the data is ready
    for the downstream nodes to be evaluated.
    
    
    
    Built-in Rules
    
    
    evaluationCache
    This rule has the same effect as using the evaluationCacheNodes filter
    with the enableEvaluationCache action.
    
    
    
    customEvaluators
    This rule ensures proper behavior for nodes claimed by a custom evaluator of
    a higher priority than the cache evaluator.  First, it makes sure that caching is
    disabled for nodes claimed by a custom evaluator of a higher priority.  Secondly,
    it makes sure input nodes to clusters belonging to a custom evaluator of a higher
    priority are marked as evaluation caching points if the evaluator needs data.  This
    prevents pull evaluation from happening when the evaluator is evaluated.
    
    
    
    
    Note that any combination of cache configuration rules other than the default modes
    is considered unsupported and to be used at one's own risk.  The default modes
    are "Evaluation cache", "VP2 software cache" and "VP2 hardware cache".  The sets
    of rules used to enable each mode are listed in the code examples.
    
    Querying Cache Configuration Values
    
    In order to get a cache configuration value for a given node or list of nodes,
    the cacheName flag can be used in query mode.  Without any additional
    parameters, this query is the same as if the valueName flag was set to
    "active", i.e. it queries whether the given cache is active or not.
    
    
    If the queried node is not a caching point, there will be no caching
    configuration information associated with it and the query will return an
    empty string (which is basically the same as all cache modes being inactive).
    If the queried node is a caching point, the returned string will be the
    requested information from the given cache.  For example, querying the
    "active" value can return "0" or "1".

    Args:
        cacheFillMode: (create, query) - Specifies the cache fill mode. Valid values are: "syncOnly" to fill cache during playback, "syncAsync" to cache during playback and in background,  and "asyncOnly" to fill cache only in background. Query returns current mode.
        cacheFillOrder: (create, query) - Specifies in which order the cache fills the timeline. Valid values are: "forward" to fill cache in forward direction, "backward" to fill cache backwards, "bidirectional" to fill cache in forward and backward directions simultaneously,  and "forwardFromBegin" to fill cache in forward direction from animation start.  Query returns current cache fill mode.
        cacheInvalidate: (create) - Specifies the frame range in which cache should be invalidated. The range should be specified as a pair of positive integers.      Usage examples:       -ci "10:20"{Python equivalent: ('10','20')} means all frames         in the range from 10 to 20, inclusive, in the current time unit.        Omitting one end of a range means using either end of the animation range      (or both), as in the following examples:       -ci "10:" means all frames from time 10 (in the current time unit)         onwards to the maximum time in the animation range (on the timeline).   -ci ":10" means all frames from the minimum time on the animation range         (on the timeline) up to (and including) time 10 (in the current time unit).   -ci ":" is a short form to specify all frames, from minimum to         maximum time on the current animation range.
        cacheName: (query) - Specifies the name of the cache from which to query a value. 			In query mode, this flag needs a value.
        cachedFrames: (query) - Get the list of frames with valid cache data. The result is an integer array containing multiple triplets of (cache-status, begin-frame, end-frame) For example, The result is an array of 9 integers [(0b01, 1, 3), (0b10, 7, 10), (0b11, 13, 15)]. In MEL, the result is typed as "int[9]". In Python, the result is typed as "Tuple[int,int,int][3]". The result suggests frames 1:3 (1,2,3), 7:10 (7,8,9,19), and 13:15 (13,14,15) are cached. No other frames contain valid cache data. The cache-status numbers are always 1 if "layeredEvaluationActive" is false. The cache-status can be one of {1,2,3}, when "layeredEvaluationActive" is true. It represents whether the frame is valid on animation cache or dynamics cache, the encoding is:  1 (0b01) : only animation cache is valid 2 (0b10) : only dynamics cache is valid 3 (0b11) : both animation and dynamics cache are valid  In the above example, it suggests: frames 1:3 are only valid in animation cache. frames 7:10 are only valid in dynamics cache. frames 13:15 are valid in both and considered as 'fully-cached'.
        cachingPoints: (query) - Get list of nodes marked as caching points, i.e. nodes with at least one type of cache active.
        creationParameters: (query) - Get the current mode creation parameters.  The result is a JSON string which represents an array with an element for each rule.  Each element is an association between the parameter name and its value when creating the rule.
        delegateEvaluation: (query) - Returns whether the specified node(s) are delegating to evaluation.
        dynamicsAsyncRefresh: (create, query) - Enable / Disable Asynchronous Refresh in Dynamics Support mode. Traditionally, edits related to the simulation system require the user to re-playback the scene to see the result. When Asynchronous Refresh is active, Maya will process the simulation in the background and refresh the viewport once the result is ready. Note, the automatic refresh will not happen if the frame contains temproary edits. For example, an object is moved without setting the keyframe.
        dynamicsSupportActive: (query) - Query if the Dynamics Support mode is active. Dynamics Support mode is used to support Physics Simulation, such as Hair, or Fluid. It will be activated if such nodes are detected in the scene, and "enableDynamicsSupport" is set to true. When Dynamics Support mode is active, you will notice the following behavior:  Dynamics nodes will be frozen for uncached frame A separate dynamics cache line will appear on the Time Slider Dynamics cache starts after the animation cache was filled Dynamics cache only fills in the background Dynamics cache always fills forward from the beginning Dynamics cache evaluation may refresh foreground dynamics nodes (see the flag "dynamicsAsyncRefresh")
        dynamicsSupportEnabled: (create, query) - Specifies if Dynamics nodes are allowed to participate in Cached Playback When disabled, Dynamics nodes will trigger "Safe mode" and prevent caching. When enabled, Dynamics nodes will participate in caching and trigger "Dynamics support mode". For more information check flag "dynamicsSupportActive".
        flushCache: (create) - Specifies to flush the current cache. Valid values are: "keep" to store the existing cache as backup, and "destroy" to delete the current cache.
        flushCacheRange: (create) - Specifies the frame range in which cache should be flushed. By default it will destroy the cache - if the 'flushCache' is also set then it will define what to do with the cache range being flushed. The range should be specified as a pair of positive integers and a boolean.      Usage examples:       -flushCacheRange "10:20" on {Python equivalent: ('10','20',True)}                 means all frames in the range from 10 to 20, inclusive, in the current time unit.   -flushCacheRange "12:18" off {Python equivalent: ('12','18',False)}                 means all frames before 12 and after 18, not inclusive, in the current time unit.        Omitting one end of a range means using either end of the animation range      (or both), as in the following examples:       -flushCacheRange "10:" on means all frames from time 10 (in the current time unit)         onwards to the maximum time in the animation range (on the timeline).   -flushCacheRange ":10" on means all frames from the minimum time on the animation range         (on the timeline) up to (and including) time 10 (in the current time unit).   -flushCacheRange ":" on is a short form to specify all frames, from minimum to         maximum time on the current animation range.
        flushCacheSync: (create, query) - Specifies how to flush the cache: synchronously or asynchronously. True for synchronous, False for asynchronous.
        flushCacheWait: (create) - Wait for the cache destruction to be completed.
        hybridCacheMode: (create, query) - Specifies the hybrid cache mode. Valid values are: "disabled", not to use hybrid cache; "smp", to evaluate on the GPU meshes with GPU-supported deformation stacks if they use Smooth Mesh Preview (instead of caching them); "all", to evaluate on the GPU all meshes with PU-supported deformation stacks (instead of caching them). Query returns current mode.
        layeredEvaluationActive: (query) - Query if the Layered Evaluation mode is active. When Layered Evaluation is active, the background cache fill process will be split into multiple passes for different contents (evaluation nodes). These contents are referred as different 'evaluation layers', representing different level of details (LoD) in animation evaluation. For example:  The first layer contains regular animations like a character motion.  The second layer contains dynamics simulations like a character's hair and cloth.   Maya will create separated cache and cache fill pass for each of the layers. Additional cache bars will be added to the Time Slider UI to represent these layers. The background cache fill pass for each of the layer will start in order. In the above example, two passes of background cache fill will be observed. In the first pass of background-cache-fill or playback-fill, only Character motions will be evaluated and filled, Hair and Clothes are frozen in-place. After the cache for first layer have been filled for all the frames, the second pass of cache fill will start to simulate Hairs and Clothes physics and fill the cache for the 2nd layer. Once the cache for the 2nd layer is filled for a frame, users can scrub the timeline to view the fully updated effects. Note, when layered evaluation is active, any foreground playback or manipulation will only evaluate the first evaluation layer, and all the FX contents will be frozen in the viewport until the background simulation is complete. For example, when rotating a character’s head, its hair will not follow in real time. If the flag "dynamicsAsyncRefresh" is enabled, the FX contents will be updated automatically after simulation cached up. Please refer to the flag for more detail.
        layeredEvaluationCachingPoints: (query) - Get the list of nodes marked as caching points because of layered evaluation.
        layeredEvaluationEnabled: (create, query) - Enable / Disable Layered Evaluation in Dynamics Support mode. Refering to flags "dynamicsSupportActive" and "layeredEvaluationActive" for details about layered evaluation enabled behavior. This flag is provided to support plugin developers for testing purpose. Disabling this option in production is not recommended. When disabled, dynamics nodes will share the same cache with regular animation. Allows dynamics nodes to be evaluated and stored to cache in the foreground. Background "cacheFillOrder" option will be locked to "forwardFromBegin". When used with cacheFillMode="syncOnly", it can also be used to support legacy dynamics nodes that cannot evaluate in the background.
        listCacheNames: (query) - Return the list of existing cache names.
        listCachedNodes: (query) - Returns the list of cached nodes.
        listValueNames: (query) - Return the list of value names that can be queried for the given cache.
        newAction: (create) - Specifies the name of the new action to create in the new filter/action rule.
        newActionParam: (create) - Specifies the parameter string to pass to the new action to create in the new filter/action rule.
        newFilter: (create) - Specifies the name of the new filter to create in the new filter/action rule.
        newFilterParam: (create) - Specifies the parameter string to pass to the new filter to create in the new filter/action rule.
        newRule: (create) - Specifies the name of the new rule to create.
        newRuleParam: (create) - Specifies the parameter string to pass to the new rule to create.
        pauseInvalidation: (create, query) - Pause all incoming invalidation of the cache. Work in symmetry with resumeInvalidation flag. PauseInvalidation can be called several time, useful in nesting situation. The same number of resume need to be called to resume the invalidation. If queried it will return how much time caching is paused, 0 means it is resumed.
        preventFrameSkip: (create, query) - Specifies if frame skipping is enabled. Following behavior is seen when frame skipping is enabled, and playback is set to play in real-time.  If cache can't be filled at real-time frame rate, frames will NOT be skipped. Once all frames have been looped over(and therefore all frames are cached), and if     playing back from cache still can't be done at real-time frame rate; frames WILL be skipped. If memory limit is reached before all frames are cached, frames WILL be skipped. If cache is invalidated will playing(like flushing it), frames will NOT     be skipped(until the cache is full again).
        resetRules: (create) - Reset the cache configuration rules to an empty set of rules.
        resourceUsage: (query) - Returns the current state of the resource usage as a string. 'unlimited' = the resource limits are being ignored, 'out' = the memory limit has been reached, 'low' = the memory usage is at 90% of the specified limit, 'okay' = memory usage is under 90% of the specified limit.
        resumeInvalidation: (create, query) - Resume all incoming invalidation of the cache. Work in symmetry with pauseInvalidation flag. PauseInvalidation can be called several time, useful in nesting situation. The same number of resume need to be called to resume the invalidation. If queried it will return true if cache is resumed, false otherwise.
        safeMode: (create, query) - Turns safe mode on or off. In query mode, it returns the status of the safe mode for cache evaluator.
        safeModeMessages: (query) - Prints the safe mode messages to the console.
        safeModeTriggered: (query) - Returns if the safe mode was triggered for cache evaluator.
        valueName: (query) - Specifies the name of the parameter for which to query the value. 			In query mode, this flag needs a value.
        waitForCache: (create) - Specifies to wait for cache to fill in background, with [Time to wait in seconds] timeout.
    """
    ...


def character(*args, addElement: str = ..., addOffsetObject: Optional[Union[str, bool]] = ..., anyMember: Optional[Union[str, bool]] = ..., characterPlug: bool = ..., clear: str = ..., empty: bool = ..., excludeDynamic: bool = ..., excludeRotate: bool = ..., excludeScale: bool = ..., excludeTranslate: bool = ..., excludeVisibility: bool = ..., flatten: str = ..., forceElement: str = ..., include: str = ..., intersection: Optional[Union[str, bool]] = ..., isIntersecting: Optional[Union[str, bool]] = ..., isMember: Optional[Union[str, bool]] = ..., library: bool = ..., memberIndex: Optional[Union[int, bool]] = ..., name: Optional[Union[str, bool]] = ..., noWarnings: bool = ..., nodesOnly: bool = ..., offsetNode: bool = ..., remove: str = ..., removeOffsetObject: str = ..., root: Optional[Union[str, bool]] = ..., scheduler: bool = ..., split: Optional[Union[str, bool]] = ..., subtract: Optional[Union[str, bool]] = ..., text: Optional[Union[str, bool]] = ..., union: Optional[Union[str, bool]] = ..., userAlias: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to manage the membership of a character.  Characters
    are a type of set that gathers together the attributes of a node or nodes
    that a user wishes to animate as a single entity.

    Args:
        addElement: (edit) - Adds the list of items to the given character.  If some of the items cannot be added to the character because they are in another character, the command will fail.  When another character is passed to to -addElement, is is added as a sub character.  When a node is passed in, it is expanded into its keyable attributes, which are then added to the character.
        addOffsetObject: (edit, query) - Indicates that the selected character member objects should be used when calculating and applying offsets. The flag argument is used to specify the character.
        anyMember: (create) - An operation which tests whether any of the given items are members of the given set.
        characterPlug: (query) - Returns the plug on the character that corresponds to the specified character member.
        clear: (edit) - An operation which removes all items from the given character.
        empty: (create) - Indicates that the character to be created should be empty. (i.e. it ignores any arguments identifying objects to be added to the character.
        excludeDynamic: (create) - When creating the character, exclude dynamic attributes.
        excludeRotate: (create) - When creating the character, exclude rotate attributes from transform-type nodes.
        excludeScale: (create) - When creating the character, exclude scale attributes from transform-type nodes.
        excludeTranslate: (create) - When creating the character, exclude translate attributes from transform-type nodes. For example, if your character contains joints only, perhaps you only want to include rotations in the character.
        excludeVisibility: (create) - When creating the character, exclude visibility attribute from transform-type nodes.
        flatten: (edit) - An operation that flattens the structure of the given character. That is, any characters contained by the given character will be replaced by its members so that the character no longer contains other characters but contains the other characters' members.
        forceElement: (edit) - For use in edit mode only. Forces addition of the items to the character. If the items are in another character which is in the character partition, the items will be removed from the other character in order to keep the characters in the character partition mutually exclusive with respect to membership.
        include: (edit) - Adds the list of items to the given character.  If some of the items cannot be added to the character, a warning will be issued. This is a less strict version of the -add/addElement operation.
        intersection: (query) - An operation that returns a list of items which are members of all the character in the list.  In general, characters should be mutually exclusive.
        isIntersecting: (query) - An operation which tests whether or not the characters in the list have common members.  In general, characters should be mutually exclusive, so this should always return false.
        isMember: (query) - An operation which tests whether or not all the given items are members of the given character.
        library: (query) - Returns the clip library associated with this character, if there is one. A clip library will only exist if you have created clips on your character.
        memberIndex: (query) - Returns the memberIndex of the specified character member if used after the query flag. Or if used before the query flag, returns the member that corresponds to the specified index.
        name: (create) - Assigns string as the name for a new character. Valid for operations that create a new character.
        noWarnings: (create) - Indicates that warning messages should not be reported such as when trying to add an invalid item to a character. (used by UI)
        nodesOnly: (query) - This flag modifies the results of character membership queries. When listing the attributes (e.g. sphere1.tx) contained in the character, list only the nodes.  Each node will only be listed once, even if more than one attribute or component of the node exists in the character.
        offsetNode: (query) - Returns the name of the characterOffset node used to add offsets to the root of the character.
        remove: (edit) - Removes the list of items from the given character.
        removeOffsetObject: (edit) - Indicates that the selected character offset objects should be removed as offsets. The flag argument is used to specify the character.
        root: (create) - Specifies the transform node which will act as the root of the character being created. This creates a characterOffset node in addition to the character node, which can be used to add offsets to the character to change the direction of the character's animtion without inserting additional nodes in its hierarchy.
        scheduler: (query) - Returns the scheduler associated with this character, if there is one. A scheduler will only exist if you have created clips on your character.
        split: (create) - Produces a new set with the list of items and removes each item in the list of items from the given set.
        subtract: (query) - An operation between two characters which returns the members of the first character that are not in the second character. In general, characters should be mutually exclusive.
        text: (create, edit, query) - Defines an annotation string to be stored with the character.
        union: (query) - An operation that returns a list of all the members of all characters listed.
        userAlias: (query) - Returns the user defined alias for the given attribute on the character or and empty string if there is not one.  Characters automatically alias the attributes where character animation data is stored.  A user alias will exist when the automatic aliases are overridden using the aliasAttr command.
    """
    ...


def characterize(*args, activatePivot: bool = ..., addAuxEffector: bool = ..., addFloorContactPlane: bool = ..., addMissingEffectors: bool = ..., attributeFromHIKProperty: Optional[Union[str, bool]] = ..., attributeFromHIKPropertyMode: Optional[Union[str, bool]] = ..., autoActivateBodyPart: bool = ..., changePivotPlacement: bool = ..., effectors: Optional[Union[str, bool]] = ..., fkSkeleton: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., pinHandFeet: bool = ..., placeNewPivot: bool = ..., posture: Optional[Union[str, bool]] = ..., sourceSkeleton: Optional[Union[str, bool]] = ..., stancePose: Optional[Union[str, bool]] = ..., type: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to scan a joint hierarchy for predefined joint names or
    labels. If the required joints are found, human IK effectors will be created
    to control the skeleton using full-body IK.
    Alternatively, you can manually create all of the components
    required for fullbody IK, and use this command to hook them up.
    Fullbody IK needs 3 major components: the
    user input skeleton (sk), the fk skeleton on which keys are set (fk) and the
    hik effectors (ik).  Together fk and ik provide parameters to the fullbody IK
    engine, which solves for the output and plots it onto sk. This command usage
    is used internally by Maya when importing data from fbx files, but is not generally recommended.
    
    Note that a minimum set of required joint names or joint labels  must be
    found in order for the characterize command to succeed. Please refer to the
    Maya documentation for details on properly naming or labeling your skeleton.
    The skeleton should also be z-facing, with its y-axis up, its
    left hand parallel to positive x-axis and right hand parallel to
    negative x-axis.
    END_COMMENT

    Args:
        activatePivot: (edit) - Activates a pivot that has been properly placed.  After activating this new pivot, you will now be able to rotate and translate about this pivot. A pivot behaves in all ways the same as an effector (it IS an effector, except that it is offset from the normal position of the effector to allow one to rotate about a different point.
        addAuxEffector: (edit) - Adds an auxilliary (secondary) effector to an existing effector.
        addFloorContactPlane: (edit) - Adds a floor contact plane to one of the hands or feet.  With this plane, you will be able to adjust the floor contact height.  Select a hand or foot effector and then issue the characterize command with this flag.
        addMissingEffectors: (edit) - This flag tells the characterize command to look for any effectors that can be added to the skeleton. For example, if the user has deleted some effectors or added fingers to an existing skeleton, "characterize -e -addMissingEffectors" can be used to restore them.
        attributeFromHIKProperty: (query) - Query for the attribute name associated with a MotionBuilder property.
        attributeFromHIKPropertyMode: (query) - Query for the attribute name associated with a MotionBuilder property mode.
        autoActivateBodyPart: (edit, query) - Query or change whether auto activation of character nodes representing body parts should be enabled.
        changePivotPlacement: (edit) - Reverts a pivot back into pivot placement mode.  A pivot that is in placement mode will not participate in full body manipulation until it has been activated with the -activatePivot flag.
        effectors: (create) - Specify the effectors to be used by human IK by providing 2 pieces of information for each effector:  1) the partial path of the effector and 2) the name of the full body effector this represents.  1) and 2) are to be separated by white space, and multiple entries separated by ",". Normally, the effectors are automatically created.  This flag is for advanced users only.
        fkSkeleton: (create, edit) - Specify the fk skeleton to be used by human IK by providing 2 pieces of information for each joint of the FK skeleton:  1) the partial path of the joint and 2) the name of the full body joint this represents.  1) and 2) are to be separated by white space, and multiple entries separated by ",". Normally, the fk control skeleton is automatically created.  This flag is for advanced users only.
        name: (create) - At characterization (FBIK creation) time, use this flag to name your FBIK character. This will affect the name of the hikHandle node and the control rig will be put into a namespace that matches the name of your character.  If you do not specify the character name, a default one will be used. At the moment edit and query of the character name is not supported.
        pinHandFeet: (create) - When the character is first being characterized, pin the hands and feet by default.
        placeNewPivot: (edit) - Creates a new pivot and puts it into placement mode.  Note that you will not be able to do full body manipulation about this pivot until you have activated it with the -activatePivot flag. A pivot behaves in all ways the same as an effector (it IS an effector, except that it is offset from the normal position of the effector to allow one to rotate about a different point). A new pivot created with this flag allow you to adjust the offset interactively before activating it.
        posture: (create) - Specifies the posture of the character. Valid options are "biped" and "quadruped". The default is "biped".
        sourceSkeleton: (create, edit) - This flag can be used to characterize a skeleton that has not been named or labelled according to the FBIK guidelines. It specifies the association between the actual joint names and the expected FBIK joint names. The format of the string is as follows: For each joint that the user wants to involve in the solve:  1) the partial path of the joint and 2) the name of the full body joint this represents.  1) and 2) are to be separated by white space, and multiple entries separated by ",".
        stancePose: (create, query) - Specify the default stance pose to be used by human IK.  The stance pose is specified by providing 2 pieces of information for each joint involved in the solve: 1) the partial path to the joint and 2) 9 numbers representing translation rotation and scale. 1) and 2) are to be separated by white space, and multiple entries separated by ",". Normally, the stance pose is taken from the selected skeleton.  This flag is for advanced users only.
        type: (create) - Specifies the technique used by the characterization to identify the joint type. Valid options are "label" and "name". When "label" is used, the joints must be labelled using the guidelines described in the Maya documentation. When name is used, the joint names must follow the naming conventions described in the Maya documentation. The default is "name". This flag cannot be used in conjunction with the sourceSkeleton flag.
    """
    ...


def characterMap(*args, mapAttr: Optional[Union[Tuple[str, str], bool]] = ..., mapMethod: Optional[Union[str, bool]] = ..., mapNode: Optional[Union[Tuple[str, str], bool]] = ..., mapping: Optional[Union[str, bool]] = ..., proposedMapping: bool = ..., unmapAttr: Optional[Union[Tuple[str, str], bool]] = ..., unmapNode: Optional[Union[Tuple[str, str], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to create a correlation between the attributes of 2 or more characters.

    Args:
        mapAttr: (create, edit, query) - In query mode, this flag can be used to query the mapping stored by the specified map node. It returns an array of strings. In non-query mode, this flag can be used to create a mapping between the specified character members. Any previous mapping on the attributes is removed in favor of the newly specified mapping.
        mapMethod: (create) - This is is valid in create mode only. It specifies how the mapping should be done. Valid options are: "byNodeName", "byAttrName", and "byAttrOrder". "byAttrOrder" is the default. The flags mean the following: "byAttrOrder" maps using the order that the character stores the attributes internally, "byAttrName" uses the attribute name to find a correspondence, "byNodeName" uses the node name *and* the attribute name to find a correspondence.
        mapNode: (create, query) - This flag can be used to map all the attributes on the source node to their matching attributes on the destination node.
        mapping: (query) - This flag is valid in query mode only. It must be used before the query flag with a string argument. It is used for querying the mapping for a particular attribute.  A string array is returned.
        proposedMapping: (query) - This flag is valid in query mode only. It is used to get an array of the mapping that the character map would prvide if called with the specified characters and the (optional) specified mappingMethod. If a character map exists on the characters, the map is not affected by the query operation.  A string array is returned.
        unmapAttr: (create, edit) - This flag can be used to unmap the mapping stored by the specified map node.
        unmapNode: (create) - This flag can be used to unmap all the attributes on the source node to their matching attributes on the destination node. Note that mapped attributes which do not have matching names, will not be unmapped.
    """
    ...


def choice(*args, attribute: Optional[Union[str, bool]] = ..., controlPoints: bool = ..., index: Optional[Union[int, bool]] = ..., name: Optional[Union[str, bool]] = ..., selector: Optional[Union[str, bool]] = ..., shape: bool = ..., sourceAttribute: Optional[Union[str, bool]] = ..., time: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The choice command provides a mechanism for changing the inputs
    to an attribute based on some (usually time-based) criteria.
    For example, an object could be animated from
    frames 1 to 30 by a motion path, then from frames 30 to 50 it
    follows keyframe animation, and after frame 50 it returns to
    the motion path. Or, a revolve surface could change its input
    curve depending on some transform's rotation value.
    
    The choice command creates a choice node (if one does not already
    exist) on all specified attributes of the selected objects.
    If the attribute was already connected to something, that something
    is now reconnected to the i'th index of the choice node's input (or
    the next available input if the -in/index flag is not specified).
    If a source attribute is specified, then that attribute is connected
    to the choice node's i'th input instead.
    
    The choice node operates by using the value of its selector attribute
    to determine which of its input attributes to pass through to its output.
    The input attributes can be of any type. For example, if the selector
    attribute was connected by an animation curve with keyframes at
    (1,1), (30,2) and (50,1), then that would mean that the choice node
    would pass on the data from input[1] from time 1 to 30, and after time 50,
    and the data from input[2] between times 30 and 50.
    
    This command returns the names of the created or modified choice nodes,
    and if a keyframe was added to the animation curve, it specifies the
    index (or value on the animation curve).

    Args:
        attribute: (create, multiuse) - specifies the attributes onto which choice node(s) should be created. The default is all keyable attributes of the given objects. Note that although this flag is not queryable, it can be used to qualify which attributes of the given objects to query.       In query mode, this flag needs a value.
        controlPoints: (create) - Explicitly specify whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.
        index: (create, query) - specifies the multi-input index of the choice node to connect the source attribute to. When queried, returns a list of integers one per specified -t/time that indicates the multi-index of the choice node to use at that time.
        name: (create, query) - the name to give to any newly created choice node(s). When queried, returns a list of strings.
        selector: (create, query) - specifies the attribute to be used as the choice node's selector. The value of the selector at a given time determines which of the choice node's multi-indices should be used as the output of the choice node at that time. This flag is only editable (it cannot be specified at creation time). When queried, returns a list of strings.
        shape: (create) - Consider all attributes of shapes below transforms as well, except "controlPoints". Default: true
        sourceAttribute: (create) - specifies the attribute to connect to the choice node that will be selected at the given time(s) specified by -t/time.
        time: (create, multiuse) - specifies the time at which the choice should use the given source attribute, or the currently connected attribute if source attribute is not specified. The default is the curren time. Note that although this flag is not queryable, it can be used to qualify the times at which to query the other attributes.       In query mode, this flag needs a value.
    """
    ...


def clip(*args, absolute: bool = ..., absoluteRotations: bool = ..., active: Optional[Union[str, bool]] = ..., addTrack: bool = ..., allAbsolute: bool = ..., allClips: bool = ..., allRelative: bool = ..., allSourceClips: bool = ..., animCurveRange: bool = ..., character: bool = ..., constraint: bool = ..., copy: bool = ..., defaultAbsolute: bool = ..., duplicate: bool = ..., endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., expression: bool = ..., ignoreSubcharacters: bool = ..., isolate: bool = ..., leaveOriginal: bool = ..., mapMethod: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., newName: Optional[Union[str, bool]] = ..., paste: bool = ..., pasteInstance: bool = ..., remove: bool = ..., removeTrack: bool = ..., rotationOffset: Optional[Union[Tuple[float, float, float], bool]] = ..., rotationsAbsolute: bool = ..., scheduleClip: bool = ..., sourceClipName: bool = ..., split: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., translationOffset: Optional[Union[Tuple[float, float, float], bool]] = ..., useChannel: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to create, edit and query character clips.

    Args:
        absolute: (create) - This flag is now deprecated.  Use aa/allAbsolute, ar/allRelative, ra/rotationsAbsolute, or da/defaultAbsolute instead.  This flag controls whether the clip follows its keyframe values or whether they are offset by a value to maintain a smooth path. Default is true.
        absoluteRotations: (create) - This flag is now deprecated.  Use aa/allAbsolute, ar/allRelative, ra/rotationsAbsolute, or da/defaultAbsolute instead. If true, this overrides the -absolute flag so that rotation channels are always calculated with absolute offsets. This allows you to have absolute offsets on rotations and relative offsets on all other channels.
        active: (edit, query) - Query or edit the active clip. This flag is not valid in create mode. Making a clip active causes its animCurves to be hooked directly to the character attributes in addition to being attached to the clip library node. This makes it easier to access the animCurves if you want to edit, delete or add additional animCruves to the clip.
        addTrack: () - This flag is now obsolete. Use the insertTrack flag on the clipSchedule command instead.
        allAbsolute: (create) - Set all channels to be calculated with absolute offsets.  This flag cannot be used in conjunction with the ar/allRelative, ra/rotationsAbsolute or da/defaultAbsolute flags.
        allClips: (query) - This flag is used to query all the clips in the scene. Nodes of type "animClip" that are storing poses, are not returned by this command.
        allRelative: (create) - Set all channels to be calculated with relative offsets.  This flag cannot be used in conjunction with the aa/allAbsolute, ra/rotationsAbsolute or da/defaultAbsolute flags.
        allSourceClips: (query) - This flag is used to query all the source clips in the scene. Nodes of type "animClip" that are storing poses or clip instances, are not returned by this command.
        animCurveRange: (create) - This flag can be used at the time you create the clip instead of the startTime and endTime flags. It specifies that you want the range of the clip to span the range of keys in the clips associated animCurves.
        character: (query) - This is a query only flag which operates on the specified clip. It returns the names of any characters that a clip is associated with.
        constraint: (create) - This creates a clip out of any constraints on the character. The constraint will be moved off of the character and into the clip, so that it is only active for the duration of the clip, and its value can be scaled/offset/cycled according to the clip attributes.
        copy: (create, query) - This flag is used to copy a clip or clips to the clipboard. It should be used in conjunction with the name flag to copy the named clips on the specified character and its subcharacters. In query mode, this flag allows you to query what, if anything, has been copied into the clip clipboard.
        defaultAbsolute: (create) - Sets all top-level channels except rotations in the clip to relative, and the remaining channels to absolute. This is the default during clip creation if no offset flag is specified.  This flag cannot be used in conjunction with the aa/allAbsolute, ar/allRelative, or ra/rotationsAbsolute flags.
        duplicate: (query) - Duplicate the clip specified by the name flag. The start time of the new clip should be specified with the startTime flag.
        endTime: (create, edit, query) - Specify the clip end
        expression: (create) - This creates a clip out of any expressions on the character. The expression will be moved off of the character and into the clip, so that it is only active for the duration of the clip, and its value can be scaled/offset/cycled according to the clip attributes.
        ignoreSubcharacters: (create) - During clip creation, duplication and isolation, subcharacters are included by default. If you want to create a clip on the top level character only, or you want to duplicate the clip on the top level character without including subCharacters, use the ignoreSubcharacters flag.
        isolate: (create) - This flag should be used in conjunction with the name flag to specify that a clip or clips should be copied to a new clip library. The most common use of this flag is for export, when you want to only export certain clips from the character, without exporting all of the clips.
        leaveOriginal: (create) - This flag is used when creating a clip to specify that the animation curves should be copied to the clip library, and left on the character.
        mapMethod: (create) - This is is valid with the paste and pasteInstance flags only. It specifies how the mapping should be done. Valid options are: "byNodeName", "byAttrName", "byCharacterMap", "byAttrOrder", "byMapOrAttrName" and "byMapOrNodeName". "byAttrName" is the default. The flags mean the following: "byAttrOrder" maps using the order that the character stores the attributes internally, "byAttrName" uses the attribute name to find a correspondence, "byNodeName" uses the node name *and* the attribute name to find a correspondence, "byCharacterMap" uses the existing characterMap node to do the mapping. "byMapOrAttrName" uses a character map if one exists, otherwise uses the attribute name. "byMapOrNodeName" uses a character map if one exists, otherwise uses the attribute name.
        name: (create, multiuse, query) - In create mode, specify the clip name. In query mode, return a list of all the clips. In duplicate mode, specify the clip to be duplicated. In copy mode, specify the clip to be copied. This flag is multi-use, but multiple use is only supported with the copy flag. For use during create and with all other flags, only the first instance of the name flag will be utilized. 			In query mode, this flag can accept a value.
        newName: (create) - Rename a clip. Must be used in conjunction with the clip name flag, which is used to specify the clip to be renamed.
        paste: (create) - This flag is used to paste a clip or clips from the clipboard to a character. Clips are added to the clipboard using the c/copy flag.
        pasteInstance: (create) - This flag is used to paste an instance of a clip or clips from the clipboard to a character. Unlike the p/paste flag, which duplicates the animCurves from the original source clip, the pi/pasteInstance flag shares the animCurves from the source clip.
        remove: (query) - Remove the clip specified by the name flag. The clip will be permanently removed from the library and deleted from any times where it has been scheduled.
        removeTrack: (create) - This flag is now obsolete. Use removeTrack flag on the clipSchedule command instead.
        rotationOffset: (create, query) - Return the channel offsets used to modify the clip's rotation.
        rotationsAbsolute: (create) - Set all channels except rotations to be calculated with relative offsets.  Rotation channels will be calculated with absolute offsets.  This flag cannot be used in conjunction with the aa/allAbsolute, ar/allRelative or da/defaultAbsolute flags.
        scheduleClip: (create) - This flag is used when creating a clip to specify whether or not the clip should immediately be scheduled at the current time. If the clip is not scheduled, the clip will be placed in the library for future use, but will not be placed on the timeline. This flag is for use only when creating a new clip or duplicating an existing. The default is true.
        sourceClipName: (query) - This flag is for query only. It returns the name of the source clip that controls an instanced clip.
        split: (create, edit) - Split an existing clip into two clips. The split occurs around the specified time.
        startTime: (create, edit, query) - Specify the clip start
        translationOffset: (create, query) - Return the channel offsets used to modify the clip's translation.
        useChannel: (create, multiuse) - Specify which channels should be acted on. This flag is valid only in conjunction with clip creation, and the isolate flag. The specified channels must be members of the character.
    """
    ...


def clipEditor(*args, allTrackHeights: int = ..., autoFit: Optional[Union[str, bool]] = ..., autoFitTime: Optional[Union[str, bool]] = ..., clipDropCmd: str = ..., clipStyle: Optional[Union[int, bool]] = ..., control: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., deleteCmd: str = ..., deselectAll: bool = ..., displayActiveKeyTangents: str = ..., displayActiveKeys: str = ..., displayInfinities: str = ..., displayKeys: str = ..., displayTangents: str = ..., displayValues: str = ..., docTag: Optional[Union[str, bool]] = ..., exists: bool = ..., filter: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., frameAll: bool = ..., frameRange: Optional[Union[Tuple[float, float], bool]] = ..., highlightConnection: Optional[Union[str, bool]] = ..., highlightedBlend: Optional[Union[Tuple[str, str], bool]] = ..., highlightedClip: Optional[Union[Tuple[str, str], bool]] = ..., initialized: bool = ..., listAllCharacters: bool = ..., listCurrentCharacters: bool = ..., lockMainConnection: bool = ..., lookAt: str = ..., mainListConnection: Optional[Union[str, bool]] = ..., manageSequencer: bool = ..., menuContext: Optional[Union[str, bool]] = ..., panel: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., selectBlend: Optional[Union[Tuple[str, str, str], bool]] = ..., selectClip: Optional[Union[Tuple[str, str], bool]] = ..., selectionConnection: Optional[Union[str, bool]] = ..., snapTime: Optional[Union[str, bool]] = ..., snapValue: Optional[Union[str, bool]] = ..., stateString: bool = ..., unParent: bool = ..., unlockMainConnection: bool = ..., updateMainConnection: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create a clip editor with the given name.

    Args:
        allTrackHeights: () - OBSOLETE flag. Use clipStyle instead.
        autoFit: (edit, query) - on | off | tgl Auto fit-to-view.
        autoFitTime: (edit, query) - on | off | tgl Auto fit-to-view along the time axis, as well.
        clipDropCmd: (edit) - Command executed when clip node is dropped on the TraX editor
        clipStyle: (edit, query) - Set/return the clip track style in the specified editor. Default is 2. Valid values are 1-3.
        control: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        deleteCmd: (edit) - Command executed when backspace key is pressed
        deselectAll: (edit) - Deselect all clips and blends in the editor.
        displayActiveKeyTangents: (edit) - on | off | tgl Display active key tangents in the editor.
        displayActiveKeys: (edit) - on | off | tgl Display active keys in the editor.
        displayInfinities: (edit) - on | off | tgl Display infinities in the editor.
        displayKeys: (edit) - on | off | tgl Display keyframes in the editor.
        displayTangents: (edit) - on | off | tgl Display tangents in the editor.
        displayValues: (edit) - on | off | tgl Display active keys and tangents values in the editor.
        docTag: (create, edit, query) - Attaches a tag to the editor.
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        filter: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        forceMainConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        frameAll: (edit) - Frame view around all clips in the editor.
        frameRange: (edit, query) - The editor's current frame range.
        highlightConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        highlightedBlend: (query) - Returns the highlighted blend, listed as scheduler and index
        highlightedClip: (query) - Returns the highlighted clip, listed as scheduler and index
        initialized: (query) - Returns whether the clip editor is fully initialized, and has a port to draw through. If not, the -frameRange and -frameAll flags will fail.
        listAllCharacters: (edit) - List all characters in the editor and outliner.
        listCurrentCharacters: (edit) - List only the characters in the editor and outliner.
        lockMainConnection: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        lookAt: (edit) - all | selected | currentTime FitView helpers.
        mainListConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        manageSequencer: (create, edit, query) - Sets/returns whether the clip editor should manage sequencer nodes.  If so, animation clips and characters are not represented.
        menuContext: (query) - Returns a string array denoting the type of data object the cursor is over.  Returned values are: {"timeSlider"} {"nothing"} {"track", "track index", "character node name", "group name"} {"clip", "clip node name"}
        panel: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        selectBlend: (edit, query) - Select the blends specified by the scheduler name and the indicies of the two clips used in the blend. When queried, a string containing the scheduler name and the two clip indicies for all of the selected blends is returned.
        selectClip: (edit, query) - Selects the clip specified by the scheduler name and the clip index. When queried, a string containing the scheduler and clip index of all of the selected clips is returned.
        selectionConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        snapTime: (edit, query) - none | integer | keyframe Keyframe move snap in time.
        snapValue: (edit, query) - none | integer | keyframe Keyframe move snap in values.
        stateString: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        unParent: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
    """
    ...


def clipMatching(*args, clipDst: Optional[Union[Tuple[str, float], bool]] = ..., clipSrc: Optional[Union[Tuple[str, float], bool]] = ..., matchRotation: Optional[Union[int, bool]] = ..., matchTranslation: Optional[Union[int, bool]] = ...) -> Any:
    r"""
    This command is used to compute an offset to apply on a source clip in order to
    automatically align it to a destination clip at a specified match element.
    For this command to work, offset objects must be specified for the character.

    Args:
        clipDst: (create) - The clip to match so that the source clip can be offsetted correctly.  This flag takes in a clip name and the percentage value ranging from 0.0 to 1.0 in order to have the source clip match at a certain time in the destination clip.
        clipSrc: (create) - The clip to offset so that it aligns with the destination clip.  This flag takes in a clip name and the percentage value ranging from 0.0 to 1.0 in order to have it match at a certain time in the clip.
        matchRotation: (create) - This flag sets the rotation match type. By default, it is set to not match the rotation. 0 - None 1 - Match full rotation 2 - Match projected rotation on ground plane
        matchTranslation: (create) - This flag sets the translation match type. By default, it is set to not match the translation. 0 - None 1 - Match full translation 2 - Match projected translation on ground plane
    """
    ...


def clipSchedule(*args, allAbsolute: bool = ..., allRelative: bool = ..., blend: Optional[Union[Tuple[int, int], bool]] = ..., blendNode: Optional[Union[Tuple[int, int], bool]] = ..., blendUsingNode: Optional[Union[str, bool]] = ..., character: bool = ..., clipIndex: Optional[Union[int, bool]] = ..., cycle: Optional[Union[float, bool]] = ..., defaultAbsolute: bool = ..., enable: bool = ..., group: bool = ..., groupIndex: Optional[Union[int, bool]] = ..., groupName: Optional[Union[str, bool]] = ..., hold: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., insertTrack: Optional[Union[int, bool]] = ..., instance: Optional[Union[str, bool]] = ..., listCurves: bool = ..., listPairs: bool = ..., lock: bool = ..., mute: bool = ..., name: Optional[Union[str, bool]] = ..., postCycle: Optional[Union[float, bool]] = ..., preCycle: Optional[Union[float, bool]] = ..., remove: bool = ..., removeBlend: Optional[Union[Tuple[int, int], bool]] = ..., removeEmptyTracks: bool = ..., removeTrack: Optional[Union[int, bool]] = ..., rotationsAbsolute: bool = ..., scale: Optional[Union[float, bool]] = ..., shift: Optional[Union[int, bool]] = ..., shiftIndex: Optional[Union[int, bool]] = ..., solo: bool = ..., sourceClipName: bool = ..., sourceEnd: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., sourceStart: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., start: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., track: Optional[Union[int, bool]] = ..., weight: Optional[Union[float, bool]] = ..., weightStyle: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to create, edit and query clips and blends in the Trax editor. It operates on the clipScheduler node attached to the character. In query mode, if no flags are specified, returns an array of strings in this form:
     (clipName,clipIndex,clipStart,clipSourceStart,clipSourceEnd,clipScale,clipPreCycle,clipPostCycle,clipHold)

    Args:
        allAbsolute: (edit, query) - Set all channels to be calculated with absolute offsets.  This flag cannot be used in conjunction with the ar/allRelative, ra/rotationsAbsolute or da/defaultAbsolute flags.
        allRelative: (edit, query) - Set all channels to be calculated with relative offsets.  This flag cannot be used in conjunction with the aa/allAbsolute, ra/rotationsAbsolute or da/defaultAbsolute flags.
        blend: (create, query) - This flag is used to blend two clips, whose indices are provided as flag arguments.
        blendNode: (query) - This query only flag list all of the blend nodes associated with the blend defined by the two clip indices. This flag returns a string array. 			In query mode, this flag can accept a value.
        blendUsingNode: (create) - This flag is used to blend using an existing blend node. It is used in conjunction with the blend flag. The blend flag specifies the clip indices for the blend. The name of an existing animBlend node should be supplied supplied as an argument for the blendUsingNode flag.
        character: (query) - This flag is used to query which characters this scheduler controls. It returns an array of strings.
        clipIndex: (create, query) - Specify the index of the clip to schedule. In query mode, returns an array of strings in this form: (clipName,index,start,sourceStart,sourceEnd,scale,preCycle,postCycle) 			In query mode, this flag can accept a value.
        cycle: (create, query) - This flag is now obsolete. Use the postCycle flag instead.
        defaultAbsolute: (edit, query) - Sets all top-level channels except rotations in the clip to relative, and the remaining channels to absolute. This is the default during clip creation if no offset flag is specified.  This flag cannot be used in conjunction with the aa/allAbsolute, ar/allRelative, or ra/rotationsAbsolute flags.
        enable: (create, query) - This flag is used to enable or disable a clip. It must be used in conjunction with the ci/clipIndex flag. The specified clip will be enabled or disabled.
        group: (create) - This flag is used to add (true) or remove (false) a list of clips (specified with groupIndex) into a group.
        groupIndex: (create, multiuse) - This flag specifies a multiple number of clips to be added or removed from a group.
        groupName: (create, query) - This flag is used to specify the group that should be added to.  If no group by that name exists and new group is created with that name.  By default if this is not specified a new group will be created.
        hold: (create, query) - Specify how long to hold the last value of the clip after its normal or cycled end.
        insertTrack: (create) - This flag is used to insert a new empty track at the track index specified.
        instance: (create) - Create an instanced copy of the named clip. An instanced clip is one that is linked to an original clip. Thus, changes to the animation curve of the original curve will also modify all instanced clips. The name of the instanced clip is returned as a string.
        listCurves: (create, query) - This flag is used to list the animation curves associated with a clip. It should be used in conjunction with the clipIndex flag, which specifies the clip of interest.
        listPairs: (query) - This query only flag returns a string array containing the channels in a character that are used by a clip and the names of the animation curves that drive the channels. Each string in the string array consists of the name of a channel, a space, and the name of the animation curve animating that channel. This flag must be used with the ci/clipIndex flag.
        lock: (edit, query) - This flag specifies whether clips on a track are to be locked or not. Must be used in conjuction with the track flag.
        mute: (edit, query) - This flag specifies whether clips on a track are to be muted or not. Must be used in conjuction with the track flag.
        name: (create, query) - This flag is used to query the name of the clip node associated with the specified clip index, or to specify the name of the instanced clip during instancing. 			In query mode, this flag can accept a value.
        postCycle: (create, query) - Specify the number of times to repeat the clip after its normal end.
        preCycle: (create, query) - Specify the number of times to repeat the clip before its normal start.
        remove: (create) - This flag is used to remove a clip from the timeline. It must be used in conjunction with the ci/clipIndex flag. The specified clip will be removed from the timeline, but will still exist in the library and any instanced clips will remain in the timeline. To permanently remove a clip from the scene, the clip command should be used instead.
        removeBlend: (create) - This flag is used to remove an existing blend between two clips, whose indices are provided as flag arguments.
        removeEmptyTracks: (create) - This flag is used to remove all tracks that have no clips.
        removeTrack: (create) - This flag is used to remove the track with the specified index.  The track must have no clips on it before it can be removed.
        rotationsAbsolute: (edit, query) - Set all channels except rotations to be calculated with relative offsets.  Rotation channels will be calculated with absolute offsets.  This flag cannot be used in conjunction with the aa/allAbsolute, ar/allRelative or da/defaultAbsolute flags.
        scale: (create, query) - Specify the amount to scale the clip. Values must be greater than 0.
        shift: (create) - This flag allows multiple clips to be shifted by a certain number of tracks and works in conjunction with the shiftIndex flag.  The flag specifies the number of tracks to shift the associated clips.  Positive values shift the clips down an negative values shift the clips up.
        shiftIndex: (create, multiuse) - This flag allows multiple clips to be shifted by a certain number of tracks and works in conjunction with the shiftAmount flag.  The flag specifies the index of the clip to shift.  This flag can be used multiple times on the command line to specify a number of clips to shift.
        solo: (edit, query) - This flag specifies whether clips on a track are to be soloed or not. Must be used in conjuction with the track flag.
        sourceClipName: (create, query) - This flag is used to query the name of the source clip node associated with the specified clip index.
        sourceEnd: (create, query) - Specify where to end in the source clip's animation curves
        sourceStart: (create, query) - Specify where to start in the source clip's animation curves
        start: (create, query) - Specify the placement of the start of the clip
        track: (create, query) - Specify the track to operate on. For example, which track to place a clip on, which track to mute/lock/solo.  In query mode, it may be used in conjuction with the clipIndex flag to return the track number of a clip, where track 1 is the first track of the character. 			In query mode, this flag can accept a value.
        weight: (create, query) - This flag is used in to set or query the weight of the clip associated with the specified clip index.
        weightStyle: (create, query) - This flag is used to set or query the weightStyle attribute of the clip associated with the specified clip index.
    """
    ...


def clipSchedulerOutliner(*args, annotation: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., clipScheduler: str = ..., defineTemplate: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., fullPathName: bool = ..., height: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., isObscured: bool = ..., manage: bool = ..., noBackground: bool = ..., numberOfPopupMenus: bool = ..., parent: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., statusBarMessage: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., visible: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates/edits/queries a clip scheduler outliner control.

    Args:
        annotation: (create, edit, query) - Annotate the control with an extra string value.
        backgroundColor: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        clipScheduler: (edit) - Name of the clip scheduler for which to display information.
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
        statusBarMessage: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
        visible: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def cluster(*args, after: bool = ..., afterReference: bool = ..., before: bool = ..., bindState: bool = ..., components: bool = ..., deformerTools: bool = ..., envelope: Optional[Union[float, bool]] = ..., exclusive: Optional[Union[str, bool]] = ..., frontOfChain: bool = ..., geometry: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., name: Optional[Union[str, bool]] = ..., parallel: bool = ..., prune: bool = ..., relative: bool = ..., remove: bool = ..., resetGeometry: bool = ..., selectedComponents: bool = ..., split: bool = ..., useComponentTags: bool = ..., weightedNode: Optional[Union[Tuple[str, str], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The cluster command creates a cluster or edits the membership of
    an existing cluster. The command returns the name of the cluster
    node upon creation of a new cluster.
    
    After creating a cluster, the cluster's weights can be modified
    using the percent command or the set editor window.

    Args:
        after: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        bindState: (create) - When turned on, this flag adds in a compensation to ensure the clustered objects preserve their spatial position when clustered. This is required to prevent the geometry from jumping at the time the cluster is created in situations when the cluster transforms at cluster time are not identity.
        components: (query) - Returns the components used by the deformer
        deformerTools: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        envelope: (create, edit, query) - Set the envelope value for the deformer. Default is 1.0
        exclusive: (create, query) - Puts the deformation set in a deform partition.
        frontOfChain: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        name: (create) - Used to specify the name of the node being created.
        parallel: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        prune: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        relative: (create) - Enable relative mode for the cluster. In relative mode, Only the transformations directly above the cluster are used by the cluster. Default is off.
        remove: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        resetGeometry: (edit) - Reset the geometry matrices for the objects being deformed by the cluster. This flag is used to get rid of undesirable effects that happen if you scale an object that is deformed by a cluster.
        selectedComponents: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        split: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        useComponentTags: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
        weightedNode: (create, edit, query) - Transform node in the DAG above the cluster to which all percents are applied. The second DAGobject specifies the descendent of the first DAGobject from where the transformation matrix is evaluated. Default is the cluster handle.
    """
    ...


def combinationShape(*args, addDriver: bool = ..., allDrivers: bool = ..., blendShape: Optional[Union[str, bool]] = ..., combinationTargetIndex: Optional[Union[int, bool]] = ..., combinationTargetName: Optional[Union[str, bool]] = ..., combineMethod: Optional[Union[int, bool]] = ..., driverTargetIndex: Optional[Union[int, bool]] = ..., driverTargetName: Optional[Union[str, bool]] = ..., exist: bool = ..., removeDriver: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to create or edit drive relationship of blend shape targets

    Args:
        addDriver: () - Add drivers to the combination shape
        allDrivers: (query) - All drivers of the combination shape
        blendShape: (create) - Associated blend shape node of the combination shape 			In query mode, this flag can accept a value.
        combinationTargetIndex: (create) - Driven blend shape target index of the combination shape 			In query mode, this flag can accept a value.
        combinationTargetName: (create) - Driven blend shape target name of the combination shape 			In query mode, this flag can accept a value.
        combineMethod: (create, edit, query) - Combine method of the combination shape:  0 : Multiplication 1 : Lowest Weighting 2 : Lowest Weighting (Smooth)
        driverTargetIndex: (create, multiuse) - Driver blend shape target index of the combination shape
        driverTargetName: (create, multiuse) - Driver blend shape target name of the combination shape
        exist: (query) - If the combination shape exist
        removeDriver: () - Remove drivers from the combination shape
    """
    ...


def componentTag(*args, create: bool = ..., delete: bool = ..., injectionLocation: Optional[Union[str, bool]] = ..., modify: Optional[Union[str, bool]] = ..., newTagName: Optional[Union[str, bool]] = ..., queryEdit: bool = ..., rename: bool = ..., tagName: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This command allows you to create, delete and modify component tags

    Args:
        create: (create) - This creates a componentTag on the geometry. The name can be specified with the -newTagName option. If no new name is specified one will be generated. The name of the created tag is returned
        delete: (create) - This deletes the componentTags specified with the -tagName option.
        injectionLocation: (create) - The name of the injection node at which the componentTag will be edited. This is only necessary in the rare case where a particular componentTag can be altered at multiple injection locations.
        modify: (create) - This modifies the componentTag specified with the -tagName option. The mode determines whether components are, replaced, cleared, added or removed.
        newTagName: (create) - The name of the new componentTag to be created or the new name of the componentTag that is being renamed.
        queryEdit: (create) - This returns what edits are allowed with the given parameters. When the command is issued in Python a dictionary object containing what is allowed is returned.
        rename: (create) - This renames the componentTag specified with the -tagName option to the name specified with the -newTagName option
        tagName: (create, multiuse) - The name(s) of the componentTags to be edited. THis can be a single name or a list of names. The names can contain wildcard like '*' to match multiple existing componentTags.
    """
    ...


def connectJoint(*args, connectMode: bool = ..., parentMode: bool = ...) -> Any:
    r"""
    This command will connect two skeletons based on the two selected joints.
    The first selected joint can be made a child of the parent of the second
    selected joint or a child of the second selected joint, depending on
    the flags used.
    
    Note1: The first selected joint must be the root of a skeleton.
    The second selected joint must have a parent.
    
    Note2: If a joint name is specified in the command line, it is used as the
    child and the first selected joint will be the parent. If no joint
    name is given at the command line, two joints must be selected.

    Args:
        connectMode: (create) - The first selected joint will be parented under the parent of the second selected joint.
        parentMode: (create) - The first selected joint will be parented under the second selected joint. Both joints will be in the active list(selection list).
    """
    ...


def controller(*args, allControllers: bool = ..., children: bool = ..., group: bool = ..., index: Optional[Union[int, bool]] = ..., isController: Optional[Union[str, bool]] = ..., parent: bool = ..., pickWalkDown: bool = ..., pickWalkLeft: bool = ..., pickWalkRight: bool = ..., pickWalkUp: bool = ..., unparent: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Commands for managing animation sources

    Args:
        allControllers: (create, query) - When this flag is queried, returns all dependNode attached to a controller in the scene.
        children: (query) - Return true if the specified dependNode is a controller.
        group: (create, query) - Create a controller that is not associated with any object. This new controller will be the parent of all the selected objects.
        index: (edit, query) - In query mode, returns the index of the controller in the parent controller's list of children. In edit mode, reorder the parent controller's children connections so that the current controller is assigned the given index.
        isController: (create, query) - Returns true if the specified dependNode is a controller.
        parent: (create, edit, query) - Set or query the parent controller of the selected controller node.
        pickWalkDown: (query) - Return the first child.
        pickWalkLeft: (query) - Return the previous sibling.
        pickWalkRight: (query) - Return the next sibling.
        pickWalkUp: (query) - Return the parent.
        unparent: (edit) - Unparent all selected controller objects from their respective parent.
    """
    ...


def copyDeformerWeights(*args, destinationDeformer: Optional[Union[str, bool]] = ..., destinationShape: Optional[Union[str, bool]] = ..., mirrorInverse: bool = ..., mirrorMode: Optional[Union[str, bool]] = ..., noMirror: bool = ..., smooth: bool = ..., sourceDeformer: Optional[Union[str, bool]] = ..., sourceShape: Optional[Union[str, bool]] = ..., surfaceAssociation: Optional[Union[str, bool]] = ..., uvSpace: Optional[Union[Tuple[str, str], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to copy or mirror the deformer weights accross one
     of the three major axes.  The command can be used to mirror
     weights either from one surface to another or within the
     same surface.

    Args:
        destinationDeformer: (create, edit, query) - Specify the deformer used by the destination shape
        destinationShape: (create, edit, query) - Specify the destination deformed shape
        mirrorInverse: (create, edit, query) - Values are mirrored from the positive side to the negative.  If this flag is used then the direction is inverted.
        mirrorMode: (create, edit, query) - The mirrorMode flag defines the plane of mirroring (XY, YZ, or XZ) when the mirror flag is used. The default plane is XY.
        noMirror: (create, edit, query) - When the no mirror flag is used, the weights are copied instead of mirrored.
        smooth: (create, edit, query) - When the smooth flag is used, the weights are smoothly interpolated between the closest vertices, instead of assigned from the single closest.
        sourceDeformer: (create, edit, query) - Specify the deformer whose weights should be mirrored.  When queried, returns the deformers used by the source shapes.
        sourceShape: (create, edit, query) - Specify the source deformed shape
        surfaceAssociation: (create, edit, query) - The surfaceAssociation flag controls how the weights are transferred between the surfaces: "closestPoint", "rayCast", or "closestComponent". The default is closestComponent.
        uvSpace: (create, edit, query) - The uvSpace flag indicates that the weight transfer should occur in UV space, based on the source and destination UV sets specified.
    """
    ...


def copyFlexor(*args) -> Any:
    r"""
    This command copies an existing bone or joint flexor from one
    bone (joint) to another.  The attributes of the flexor and their
    connections as well as any tweaks in on the latticeFfd are copied
    from the original to the new flexor.  If the selected bone (joint)
    appears to be a mirror reflection of the bone (joint) of the
    existing flexor then the transform of the ffd lattice group gets
    reflected to the new bone (joint).  The arguments for the command
    are the name of the ffd Lattice and the name of the destination joint.
    If they are not specified at the command line, they will be picked
    up from the current selection list.

    Args:
    """
    ...


def copyKey(*args, animLayer: Optional[Union[str, bool]] = ..., animation: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., clipboard: Optional[Union[str, bool]] = ..., controlPoints: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., forceIndependentEulerAngles: bool = ..., hierarchy: Optional[Union[str, bool]] = ..., includeUpperBound: bool = ..., index: Optional[Union[int, bool]] = ..., option: Optional[Union[str, bool]] = ..., shape: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ...) -> Any:
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
    
    This command copies curve segments's hierarchies from
    specified targets and puts them in the clipboard.  Source
    curves are unchanged.  The pasteKey command applies these
    curves to other objects.
    
    The shape of the copied curve placed in the clipboard
    depends on the copyKey "-option" specified.  Each of these options
    below will be explained using an example.  For all the explanations,
    let us assume that the source animation curve (from which keys will
    be copied) has 5 keyframes at times 10, 15, 20, 25, and 30.
    
     copyKey -t "12:22" -option keys
    
    A 5-frame animation curve with one key at 15 and another key at 20
    is placed into the keyset clipboard.
    
     copyKey -t "12:22" -option curve
    
    A 10-frame animation is placed into the clipboard. The curve
    contains the original source-curve keys at times 15 and 20, as well
    as new keys inserted at times 12 and 22 to preserve the shape of the
    curve at the given time segment.
    
    
    
    
    TbaseKeySetCmd.h

    Args:
        animLayer: (create) - Specifies that the keys getting copied should come from this specified animation layer. If no keys on the object exist on this layer, then no keys are copied.
        animation: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        clipboard: (create) - Specifies the clipboard to which animation is copied. Valid clipboards are "api" and "anim".  The default clipboard is: anim
        controlPoints: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        float: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        forceIndependentEulerAngles: (create) - Specifies that the rotation curves should always be placed on the clipboard as independent Euler Angles. The default value is false.
        hierarchy: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        includeUpperBound: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        option: (create) - The option to use when performing the copyKey operation. Valid options are "keys," and "curve."  The default copy option is: keys
        shape: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        time: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
    """
    ...


def copySkinWeights(*args, destinationSkin: Optional[Union[str, bool]] = ..., influenceAssociation: Optional[Union[str, bool]] = ..., mirrorInverse: bool = ..., mirrorMode: Optional[Union[str, bool]] = ..., noBlendWeight: bool = ..., noMirror: bool = ..., normalize: bool = ..., sampleSpace: Optional[Union[int, bool]] = ..., selectedComponents: bool = ..., smooth: bool = ..., sourceSkin: Optional[Union[str, bool]] = ..., surfaceAssociation: Optional[Union[str, bool]] = ..., uvSpace: Optional[Union[Tuple[str, str], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to copy or mirror the skinCluster weights accross one
     of the three major axes.  The command can be used to mirror
     weights either from one surface to another or within the
     same surface.

    Args:
        destinationSkin: (create, edit, query) - Specify the destination skin shape
        influenceAssociation: (create, edit, multiuse, query) - The influenceAssociation flag controls how the influences on the source and target skins are matched up. The flag can be included multiple times to specify multiple association schemes that will be invoked one after the other until all influences have been matched up. Supported values are "closestJoint", "closestBone", "label", "name", "oneToOne". The default is closestJoint.
        mirrorInverse: (create, edit, query) - Values are mirrored from the positive side to the negative.  If this flag is used then the direction is inverted.
        mirrorMode: (create, edit, query) - The mirrorMode flag defines the plane of mirroring (XY, YZ, or XZ) when the mirror flag is used. The default plane is XY.
        noBlendWeight: (create, edit, query) - When the no blend flag is used, the blend weights on the skin cluster will not be copied across to the destination.
        noMirror: (create, edit, query) - When the no mirror flag is used, the weights are copied instead of mirrored.
        normalize: (create, edit, query) - Normalize the skin weights.
        sampleSpace: (create, edit, query) - Selects which space the attribute transfer is performed in. 0 is world space, 1 is model space. The default is world space.
        selectedComponents: (create, edit, query) - The selectedComponents flag can be used in combination with the sourceSkin and destinationSkin flags to specify that only the skin weights on the selected components should be copied.
        smooth: (create, edit, query) - When the smooth flag is used, the weights are smoothly interpolated between the closest vertices, instead of assigned from the single closest.
        sourceSkin: (create, edit, query) - Specify the source skin shape
        surfaceAssociation: (create, edit, query) - The surfaceAssociation flag controls how the weights are transferred between the surfaces: "closestPoint", "rayCast", or "closestComponent". The default is closestComponent.
        uvSpace: (create, edit, query) - The uvSpace flag indicates that the weight transfer should occur in UV space, based on the source and destination UV sets specified.
    """
    ...


def currentTime(*args, update: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    When given a time argument (with or without the -edit flag) this
    command sets the current global time.  The model updates and
    displays at the new time, unless "-update off" is present on the
    command line.

    Args:
        update: (create) - change the current time, but do not update the world. Default value is true.
    """
    ...


def curveRGBColor(*args, hueSaturationValue: bool = ..., list: bool = ..., listNames: bool = ..., remove: bool = ..., resetToFactory: bool = ..., resetToSaved: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates, changes or removes custom curve colors,
    which are used to draw the curves in the Graph Editor.
    The custom curve names may contain the wildcards
    "?", which marches a single character, and
    "*", which matches any number of characters.
    These colors are part of the UI and not part of the saved
    data for a model.  This command is not undoable.

    Args:
        hueSaturationValue: (create, query) - Indicates that rgb values are really hsv values.
        list: (create) - Writes out a list of all curve color names and their values.
        listNames: (create) - Returns an array of all curve color names.
        remove: (create) - Removes the named curve color.
        resetToFactory: (create) - Resets all the curve colors to their factory defaults.
        resetToSaved: (create) - Resets all the curve colors to their saved values.
    """
    ...


def cutKey(*args, animation: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., clear: bool = ..., controlPoints: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., includeUpperBound: bool = ..., index: Optional[Union[int, bool]] = ..., option: Optional[Union[str, bool]] = ..., selectKey: bool = ..., shape: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ...) -> Any:
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
    
    The cutKey command cuts curve segment hierarchies from specified
    targets and puts them in the clipboard.  The pasteKey command
    applies these curves to other objects.
    
    The shape of the cut curve placed in the clipboard, and
    the effect of the cutKey command on the source animation curve
    depends on the cutKey "-option" specified.  Each of these options
    below will be explained using an example.  For all the explanations,
    let us assume that the source animation curve (from which keys will
    be cut) has 5 keyframes at times 10, 15, 20, 25, and 30.
    
    TbaseKeySetCmd.h
    
    
     cutKey -t "12:22" -option keys
    
    Keyframes at times 15 and 20 are removed. All other keys are unchanged.
    A 5-frame animation curve is placed into the keyset clipboard.
    
     cutKey -t "12:22" -option keysCollapse
    
    Keyframes at times 15 and 20 are removed.  Shift all keys after time 20
    to the left by 5 frames, preserving all their values.
    A 5-frame animation curve is placed into the keyset clipboard.
    
     cutKey -t "12:22" -option keysConnect
    
    Keyframes at times 15 and 20 are removed.  Shift all keys after time 20
    to the left by 5 frames, and place the key that used to be at time 25 at the
    value of the key that used to be at time 15.
    A 5-frame animation curve is placed into the keyset clipboard.
    
     cutKey -t "12:22" -option curve
    
    Keyframes at times 15 and 20 are removed.  Keys are inserted at
    times 12 and 22.
    A 10-frame animation curve is placed into the keyset clipboard.
    
     cutKey -t "12:22" -option curveCollapse
    
    Keyframes at times 15 and 20 are removed.  Keys are inserted at
    times 12 and 22.  Shift all keys from time 22 to the left by 10 frames,
    preserving their values.
    A 10-frame animation curve is placed into the keyset clipboard.
    
     cutKey -t "12:22" -option curveConnect
    
    Keyframes at times 15 and 20 are removed.  Keys are inserted at
    times 12 and 22.  Shift all keys from time 22 to the left by 10 frames,
    and replace the key inserted at time 12 with the newly inserted key
    at time 22.
    A 10-frame animation curve is placed into the keyset clipboard.
    
     cutKey -t "12:22" -option areaCollapse
    
    Keyframes at times 15 and 20 are removed. Shift all keys from time 22
    to the left by 10 frames, preserving their values.
    A 10-frame animation curve is placed into the keyset clipboard.

    Args:
        animation: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        clear: (create) - Just remove the keyframes (i.e. do not overwrite the clipboard)
        controlPoints: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        float: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        hierarchy: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        includeUpperBound: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        option: (create) - Option for how to perform the cutKey operation.  Valid values for this flag are "keys", "curve", "curveCollapse", "curveConnect", "areaCollapse".  The default cut option is: keys
        selectKey: (create) - Select the keyframes of curves which have had keys removed
        shape: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        time: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
    """
    ...


def dagPose(*args, addToPose: bool = ..., atPose: bool = ..., bindPose: bool = ..., g: bool = ..., members: bool = ..., name: Optional[Union[str, bool]] = ..., remove: bool = ..., reset: bool = ..., restore: bool = ..., save: bool = ..., selection: bool = ..., worldParent: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to save and restore the matrix information for
    a dag hierarchy. Specifically, the data stored will restore the
    translate, rotate, scale, scale pivot, rotate pivot, rotation order,
    and (for joints) joint order for all the objects on the hierarchy.
    Data for other attributes is not stored by this command.
    
    This command can also be used to store a bindPose for an object.
    When you skin an object, a dagPose is automatically created for the
    skin.

    Args:
        addToPose: (create) - Allows adding the selected items to the dagPose.
        atPose: (query) - Query whether the hierarchy is at same position as the pose. Names of hierarchy members that are not at the pose position will be returned. An empty return list indicates that the hierarchy is at the pose.
        bindPose: (create, query) - Used to specify the bindPose for the selected hierarchy. Each hierarchy can have only a single bindPose, which is saved automatically at the time of a skin bind. The bindPose is used when adding influence objects, binding new skins, or adding flexors. Take care when modifying the bindPose with the -rs/-reset or -rm/-remove flags, since if the bindPose is ill-defined it can cause problems with subsequent skinning operations.
        g: (create) - This flag can be used in conjunction with the restore flag to signal that the members of the pose should be restored to the global pose. The global pose means not only is each object locally oriented with respect to its parents, it is also in the same global position that it was at when the pose was saved. If a hierarchy's parenting has been changed since the time that the pose was saved, you may have trouble reaching the global pose.
        members: (query) - Query the members of the specified pose. The pose should be specified using the selection list, the -bp/-bindPose or the -n/-name flag.
        name: (create, query) - Specify the name of the pose. This can be used during create, restore, reset, remove, and query operations to specify the pose to be created or acted upon.
        remove: (create) - Remove the selected joints from the specified pose.
        reset: (create) - Reset the pose on the selected joints. If you are resetting pose data for a bindPose, take care. It is appropriate to use the -rs/-reset flag if a joint has been reparented and/or appears to be exactly at the bindPose. However, a bindPose that is much different from the exact bindPose can cause problems with subsequent skinning operations.
        restore: (create) - Restore the hierarchy to a saved pose. To specify the pose, select the pose node, or use the -bp/-bindPose or -n/-name flag.
        save: (create) - Save a dagPose for the selected dag hierarchy. The name of the new pose will be returned.
        selection: (create, query) - Whether or not to store a pose for all items in the hierarchy, or for only the selected items.
        worldParent: (create) - Indicates that the selected pose member should be recalculated as if it is parented to the world. This is typically used when you plan to reparent the object to world as the next operation.
    """
    ...


def defineDataServer(*args, device: Optional[Union[str, bool]] = ..., server: Optional[Union[str, bool]] = ..., undefine: bool = ...) -> Any:
    r"""
    Connects to the specified data servername, creating a named device which
    then can be attached to device handlers.
    
    When the device is defined, it queries queries the server for data axis
    information.  The "CapChannels" present are represented as axis in form
    "channelName"."usage" for scalar channels and "channelName"."component"
    for compound channels. See listInputDeviceAxes to list axis names.
    
    Note that undoing 
    defineDataServer -d "myDevice" -s "myServer"
    
    does not break the connection with the data server until it cannot be
    redone.  Executing any other command (sphere for example) will cause
    this to occur.  Similarly, the command 
    defineDataServer -d "myDevice" -u
    
    does not break the connection with the data server until it cannot be
    undone.  Either flushUndo, or the 'defineDataServer' command falling"
    off the end of the undo queue causes this to occur, and the connection.
    to be broken.
    
    No return value.

    Args:
        device: (create) - specified the device name to be given to the server connection. device name must be unique or the command fails.
        server: (create) - specifies the name of the server with which the define device connects, and can be specifiied in two ways   name -- the name of the server socket Server names of the form name connect to the server socket on the localhost corresponding to name.  If name does not begin with "/", then /tmp/name is used. This is the default behavior of most servers. If name begins with "/", name denotes the full path to the socket.  host:service - a udp service on the specified host. The service can be any one of a "udp service name," a "port number," or a named service of "tcpmux," and they are found in that order. If host is omitted, the localhost is used.   In any case, if the server cannot be found, the device is not defined (created) and the command fails.
        undefine: (create) - undefines (destroys) the dataServer device, closing the connection with the server.
    """
    ...


def defineVirtualDevice(*args, axis: Optional[Union[int, bool]] = ..., channel: Optional[Union[str, bool]] = ..., clear: bool = ..., create: bool = ..., device: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., undefine: bool = ..., usage: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command defines a virtual device. Virtual devices act like real
    devices and are useful to manipulate/playback data when an command
    device is not connected to the computer.

    Args:
        axis: (create) - Specifies the axis number of the channel. All children have their axis number determined by their parent's axis number and the width of the parent channel. If this flag is not used, the order of the channel determines the axis number.
        channel: (create) - After a -create is started, channels may be added to the device definition. The channel string wil be the name of the channel being added to the device. The -channel flag must also be accompanied by the -usage flag and optionally by the -axis flag.
        clear: (create) - The -clear option will end a device definition and throw away any defined channels.
        create: (create) - Start defining a virtual device. If a device is currently being defined, the -create flag will produce an error.
        device: (create) - The -device flag ends the device definition. All of the channels between the -create flag and the -device flag are added to the specified device. If that device already exists, the command will fail and the device should be redefined with another device name. To see the currently defined devices, use the listInputDevices command. The -device flag is also used with -undefine to undefine a virtual device.
        parent: (create) - Specified the parent channel of the channel being defined. If the channel does not exist, or is an incompatible type, the command will fail.
        undefine: (create) - Undefines the device specified with the -device flag.
        usage: (create) - The -usage option is required for every -channel flag. It describes what usage type the defined channel is. The usage types are:   unknownscalar  posrot posRotquaternionposQuaternion  rotXYZrotYZXrotZXY rotXZYrotYXZrotZYX  posRotXYZposRotYZXposRotZXY posRotXZYposRotXZYposRotZYX  posXposYposZrotX rotYrotZ
    """
    ...


def deformableShape(*args, chain: bool = ..., createOriginalGeometry: bool = ..., createTweakNode: bool = ..., createUpstreamTagInjectionNode: bool = ..., deformShapeInAttr: bool = ..., deformShapeOutAttr: bool = ..., frontOfChain: bool = ..., localShapeInAttr: bool = ..., localShapeOutAttr: bool = ..., nodeChain: bool = ..., originalGeometry: bool = ..., outputPlugChain: bool = ..., plugChain: bool = ..., supportsComponentTags: bool = ..., tagInjectionList: bool = ..., tagInjectionNode: bool = ..., tweakNode: bool = ..., upstreamTagInjectionNode: bool = ..., worldShapeOutAttr: bool = ...) -> Any:
    r"""
    This command finds information about deforming shape(s).
    
    If no shapes are specified on the command then the curently selected
    shapes are used.

    Args:
        chain: (create) - This flag will return the list of deformers that deformer the specified shapes
        createOriginalGeometry: (create) - This creates an original geometry for the shape if it does not exist yet.
        createTweakNode: (create) - This creates a traditional tweak node if one did not exist yet.
        createUpstreamTagInjectionNode: (create) - This creates an upstream component tag injection node if an editable one does not exist yet.
        deformShapeInAttr: (create) - Returns the name of deform shape in attribute
        deformShapeOutAttr: (create) - Returns the name of deform shape out attribute
        frontOfChain: (create) - This flag will return the name of the plug on a shape node at the front end of the deformation chain. This can return an empty plug when none exists.
        localShapeInAttr: (create) - Returns the name of local shape in attribute
        localShapeOutAttr: (create) - Returns the name of local shape out attribute
        nodeChain: (create) - This flag will return the list of nodes through which the geometry passes to get to this shape
        originalGeometry: (create) - This flag will return the name of a plug on a node in the deformation chain (likely at the front end) that is the best candidate to be used as the originalGeometry. This can return an empty plug when none exists.
        outputPlugChain: (create) - This flag will return the list of output plugs leading to the shape
        plugChain: (create) - This flag will return the list of plugs leading to the shape (both input and output plugs)
        supportsComponentTags: (create) - Returns whether the shape supports component tags
        tagInjectionList: (create) - This flag will return the list of nodes which are non-procedural componentTag injection nodes
        tagInjectionNode: (create) - This flag will return the name of the non-referenced component tag injection node as high up in the deformation chain as possible. This can be the same as the input shape or an empty string when none exists.
        tweakNode: (create) - This flag will return the name of the tweak node in the deformation chain. This can return an empty string when none exists.
        upstreamTagInjectionNode: (create) - This flag will return the name of the non-referenced component tag injection node most upstream from (but not including) the input shape. This can be an empty string when none exists. If so, one can be created using the cti/createUpstreamTagInjectionNode flag.
        worldShapeOutAttr: (create) - Returns the name of world shape out attribute
    """
    ...


def deformer(*args, after: bool = ..., afterReference: bool = ..., before: bool = ..., components: bool = ..., deformerTools: bool = ..., exclusive: Optional[Union[str, bool]] = ..., frontOfChain: bool = ..., geometry: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., name: Optional[Union[str, bool]] = ..., parallel: bool = ..., prune: bool = ..., remove: bool = ..., selectedComponents: bool = ..., split: bool = ..., type: Optional[Union[str, bool]] = ..., useComponentTags: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a deformer of the specified type. The deformer
    will deform the selected objects.
    
    This command creates a deformer node and connects it to a deformation chain.
    If the deformer does not already exist, it is created. If the deformer already
    exists, the command lets you modify parameters on the named deformer.
    Unlike commands for specialized deformers, this command does not create or manage
    deformer-specific setups. Using this command allows deformation chains to be
    managed in a more general manner.

    Args:
        after: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        components: (query) - Returns the components used by the deformer
        deformerTools: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        exclusive: (create, query) - Puts the deformation set in a deform partition.
        frontOfChain: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        name: (create) - Used to specify the name of the node being created.
        parallel: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        prune: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        remove: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        selectedComponents: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        split: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        type: (create) - Specify the type of deformer to create. This flag is required in create mode. Typically the type should specify a loaded plugin deformer. This command should typically not be used to create one of the standard deformers such as sculpt, lattice, blendShape, wire and cluster, since they have their own customized commands which perform useful specialized functionality.
        useComponentTags: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
    """
    ...


def deformerEvaluator(*args, active: bool = ..., allowDownloadRejections: bool = ..., allowDownloads: bool = ..., asNodeName: bool = ..., asText: bool = ..., deformerChain: bool = ..., deformers: bool = ..., dumpInfo: bool = ..., dumpOutliner: bool = ..., gpuBlockPolicy: Optional[Union[str, bool]] = ..., isOpenCLValid: bool = ..., limitMinimumVerts: bool = ..., list: bool = ..., members: bool = ..., meshes: bool = ..., message: bool = ..., minimumVerts: Optional[Union[int, bool]] = ..., nodeInfo: bool = ..., nodeStatus: bool = ..., omitPassthroughs: bool = ..., outlinerHash: bool = ..., partition: bool = ..., purge: bool = ..., reuseMode: Optional[Union[Tuple[str, str], bool]] = ..., verbose: bool = ..., query: bool = ...) -> Any:
    r"""
    Print debug information about deformer evaluator status.  In
            query mode the debug information is returned as a string[],
            otherwise the information is displayed in the script editor.

    Args:
        active: (create, query) - Modifier to specify that instead of the current selection all active         nodes on the GPU should be queried.
        allowDownloadRejections: (create, query) - Specifies whether potentially rejecting parts of the graph that depend on GPU downloads is allowed.
        allowDownloads: (create, query) - Specifies whether downloads from GPU to CPU are allowed.
        asNodeName: (create, query) - Modifier to specify that when a certain node attribute is queried it should         return the name of the node instead. This is useful when querying multiple         nodes at a time and the results need to be lined up with the node names.
        asText: (create, query) - Modifier to specify that when the node state is queried the state should     be returned as text instead of a numeric code
        deformerChain: (create, query) - Query the state of the nodes in the deformation chain of the specified meshes.
        deformers: (create, query) - Return a list of all currently registered GPU deformers.
        dumpInfo: (create, query) - List information about all supported deformation chains as JSON.
        dumpOutliner: (create, query) - List information about all supported nodes as a python object.
        gpuBlockPolicy: (create, query) - Specifies the gpu blocking policy for a node.     Currently, we support the following blocking modes:     "off" "on" "group" "upstream" "upstreamExcl" "upstreamMesh" "downstream" "downstreamExcl" "groupDownload"     Default is "off" which means the node causes no blocking of the GPU.
        isOpenCLValid: (create, query) - Specifies whether OpenCL is valid/initialized.
        limitMinimumVerts: (create, query) - Specifies whether the limit on the minimum vert count of the geometry is used or not. The system configuration determines a certain minimum size for geometries to be allowed on GPU. When this flag is on this limit is obeyed. When this flag is off this limit is ignored. This is only used for debugging purposes and is not saved to the file or any preferences.
        list: (create, query) - Return a list of nodes that are currently active on the GPU.
        members: (create, query) - Return the names of the nodes that are in the same cluster as the specified nodes.
        meshes: (create, query) - Modifier to specify that only meshes need to be queried.
        message: (create, query) - Return the messages associated with the specified nodes.
        minimumVerts: (create, query) - Set the minimum vert count under which the geometry will not be allowed on the GPU (unless in a network with qualifying geometries). This is only used for debugging purposes and is not saved to the file or any preferences.
        nodeInfo: (create, query) - List all the information gathered during partitioning about the selected nodes
        nodeStatus: (create, query) - Return the state of the node on the GPU. When queried it will return         a numeric code unless the asText flag is used as well.
        omitPassthroughs: (create, query) - Whether opassthrough nodes like groupParts nodes should be ommitted from the dumped info or not
        outlinerHash: (create, query) - Return the unique hash value for the current outliner state.
        partition: (create, query) - Flag to force a repartition (for debug purposes only)
        purge: (create, query) - Purge the data of any unused gpu nodes
        reuseMode: (create, query) - Specifies how the GPU nodes can be reused when repartitioning. A mode has to be specified for each of the three node types (deformer and displayMesh). A mode for a node type is one of the following:       Mode "never" means they will never be reused   Mode "immediate" means that nodes will remain in memory during repartitioning but the ones that are not in use immediatley after that will be purged   Mode "always" means that all nodes will remain in memory during and after repartitioning for later reuse
        verbose: (create, query) - Print more verbose information of other flags.
    """
    ...


def deformerWeights(*args, attribute: Optional[Union[str, bool]] = ..., defaultValue: Optional[Union[float, bool]] = ..., deformer: Optional[Union[str, bool]] = ..., export: bool = ..., format: Optional[Union[str, bool]] = ..., ignoreName: bool = ..., im: bool = ..., method: Optional[Union[str, bool]] = ..., path: Optional[Union[str, bool]] = ..., positionTolerance: Optional[Union[float, bool]] = ..., remap: Optional[Union[str, bool]] = ..., shape: Optional[Union[str, bool]] = ..., skip: Optional[Union[str, bool]] = ..., vertexConnections: bool = ..., weightPrecision: Optional[Union[int, bool]] = ..., weightTolerance: Optional[Union[float, bool]] = ..., worldSpace: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to import and export deformer weights to and from a simple XML
     file. The weight data is stored in a per-vertex fashion along with a
     "point cloud" corresponding to the vertices from the geometry input to
     the deformer.
     For example a cluster deformer would have the following information:
     
    
    
    
    
    
    
    
    
     On import the weights are then mapped back to a specified deformer
     based on the specified mapping method. Note that the geometry used to
     perform the mapping association is not the visible shape but rather
     the incoming geometry to the deformer. For example, in the case of a
     skin cluster this would be the bind pose geometry.

    Args:
        attribute: (create, edit, multiuse, query) - Specify the long name of deformer attribute that should be imported/exported along with the deformerWeights. i.e. -at "envelope" -at "skinningMethod" etc.. No warning or error is given if a specified attribute does not exist on a particular deformer, making it possible to use this command with multiple deformers without aborting or slowing down the import/export process.  Currently supports numeric attributes and matrix attributes
        defaultValue: (create, edit, query) - Manually set the default value. Default values are values that are not written to file. For example, for blendShapes the default value is automatically set to 1.0 and these values are not written to disk. For skinClusters the value is 0.0. If all weights should be forced to be written to disk, set a defaultValue = -1.0.
        deformer: (create, edit, multiuse, query) - Specify the deformer whose weights should be exported or imported. If a pattern is supplied for the deformer name (i.e: cluster*), only the first deformer that matches the pattern will be imported/exported unless used in conjunction with the -skip option
        export: (create, edit, query) - Export the given deformer
        format: (create, edit, query) - Specify either "XML" or "JSON" as the file extension to save as.
        ignoreName: (create, edit, query) - Ignore the names of the layers on import, just use the order of the layers instead. This can be used when joint names have been changed. Leaving it on only name that match on import will be write to the deformer.
        im: (create, edit, query) - Import weights to the specified deformer. See the method flag for details on how the weights will be mapped to the destination deformer.
        method: (create, edit, query) - Specify the method used to map the weight during import. Valid values are: "index", "nearest", "barycentric", "bilinear" and "over". The "index" method uses the vertex index to map the weights onto the object. This is most useful when the destination object shares the same topology as the exported data. The "nearest" method finds the nearest vertex in the imported data set and sets the weight value to that value. This is best used when mapping a higher resolution mesh to a lower resolution. The "barycentric" and "bilinear" methods are only supported with polygon mesh exported with -vc/vertexConnections flag. The "barycentric" method finds the nearest triangle of the input geometry and rescales the weights at the triangle vertices according to the barycentric weights to each vertex of the nearest triangle. The "bilinear" method finds the nearest convex quad of the input geometry and rescales the weights at the quad vertices according to the bilinear weights to each vertex of the nearest convex quad. For non-quad polygon, the "bilinear" method will fall back to "barycentric" method. The "over" method is similar to the "index" method but the weights on the destination mesh are not cleared prior to mapping, so that unmatched indices keep their weights intact.
        path: (create, edit, query) - The path to the given file. Default to the current project.
        positionTolerance: (create, edit, query) - The position tolerance is used to determine the radius of search for the nearest method. This flag is only used with import. Defaults to a huge number.
        remap: (create, edit, multiuse, query) - Remap maps source regular expression to destination format. It maps any name that matches the regular expression (before the semi-colon) to the expression format (after the semi-colon). For example, -remap "test:(.*);$1" will rename all items in the test namespace to the global namespace. Accepts $1, $2, .., $9 as pattern holders in the expression format. Remap flag must be used together with import or export. When working with import, the name of the object from the xml file matching the regular expression is remapped to object in scene. When working with export, the name of the object from the scene matching the regular expression is remapped to object in xml file.
        shape: (create, edit, multiuse, query) - Specify the source shape. Export will write out all the deformers on the shape node into one file. If a pattern is supplied for the shape name (i.e: pCylinder*), only the first shape that matches the pattern will be imported/exported unless used in conjunction with the -skip option.
        skip: (create, edit, multiuse, query) - Skip any deformer, shape, or layer that whose name matches the given regular expression string
        vertexConnections: (create, edit, query) - Export vertex connection information, which is required for -m/-method "barycentric" and "bilinear". The flag is only used with -ex/-export flag. The vertex connection information is automatically loaded during import if available in xml file.
        weightPrecision: (create, edit, query) - Sets the output decimal precision for exported weights. The default value is 3.
        weightTolerance: (create, edit, query) - The weight tolerance is used to decide if a given weight value is close enough to the default value that it does not need to be included. This flag is only used with export. The default value is .001.
        worldSpace: (create, edit, query) - For spatially based association methods (nearest), the position should be based on the world space position rather then the local object space.
    """
    ...


def deltaMush(*args, after: bool = ..., afterReference: bool = ..., before: bool = ..., components: bool = ..., deformerTools: bool = ..., envelope: Optional[Union[float, bool]] = ..., exclusive: Optional[Union[str, bool]] = ..., frontOfChain: bool = ..., geometry: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., inwardConstraint: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., outwardConstraint: Optional[Union[float, bool]] = ..., parallel: bool = ..., pinBorderVertices: bool = ..., prune: bool = ..., remove: bool = ..., selectedComponents: bool = ..., smoothingIterations: Optional[Union[int, bool]] = ..., smoothingStep: Optional[Union[float, bool]] = ..., split: bool = ..., useComponentTags: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to create, edit and query deltaMush nodes.

    Args:
        after: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        components: (query) - Returns the components used by the deformer
        deformerTools: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        envelope: (create, edit, query) - Envelope of the delta mush node. The envelope determines the percent of deformation. Value is clamped to [0, 1] range. Default is 1.
        exclusive: (create, query) - Puts the deformation set in a deform partition.
        frontOfChain: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        inwardConstraint: (create, edit, query) - Constrains the movement of the vertex to not move inward from the input deforming shape to preserve the contour. Value is in the [0,1] range. Default is 0.0.
        name: (create) - Used to specify the name of the node being created.
        outwardConstraint: (create, edit, query) - Constrains the movement of the vertex to not move outward from the input deforming shape to preserve the contour. Value is in the [0,1] range. Default is 0.0.
        parallel: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        pinBorderVertices: (create, edit, query) - If enabled, vertices on mesh borders will be pinned to their current position during smoothing. Default is true.
        prune: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        remove: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        selectedComponents: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        smoothingIterations: (create, edit, query) - Number of smoothing iterations performed by the delta mush node. Default is 10.
        smoothingStep: (create, edit, query) - Step amount used per smoothing iteration. Value is clamped to [0, 1] range. A higher value may lead to instabilities but converges faster compared to a lower value. Default is 0.5.
        split: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        useComponentTags: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
    """
    ...


def deviceManager(*args, attachment: bool = ..., axisCoordChanges: bool = ..., axisIndex: Optional[Union[int, bool]] = ..., axisName: bool = ..., axisOffset: bool = ..., axisScale: bool = ..., deviceIndex: Optional[Union[int, bool]] = ..., deviceNameFromIndex: Optional[Union[int, bool]] = ..., numAxis: bool = ..., numDevices: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command queriers the internal device manager for information on attached devices.

    Args:
        attachment: (query) - Returns the plugs that a device and axis are attached to.  Expects the -deviceIndex and axisIndex to be used in conjunction.
        axisCoordChanges: (query) - Returns whether the axis coordinate changes.  Expects the -deviceIndex and -axisIndex flags to be used in conjunction.
        axisIndex: (create, edit, query) - Used usually in conjunction with other flags, to indicate the index of the axis.
        axisName: (query) - Returns the name of the axis.  Expects the -deviceIndex and -axisIndex flags to be used in conjunction.
        axisOffset: (query) - Returns the offset of the axis.  Expects the -deviceIndex and -axisIndex flags to be used in conjunction.
        axisScale: (query) - Returns the scale of the axis.  Expects the -deviceIndex and -axisIndex flags to be used in conjunction.
        deviceIndex: (create, edit, query) - Used usually in conjunction with other flags, to indicate the index of the device.
        deviceNameFromIndex: (query) - Returns the name of the device with the given index.
        numAxis: (query) - Returns the number of axis this device has.  Expects the -deviceIndex flag to be used.
        numDevices: (query) - Returns the number of devices currently attached.
    """
    ...


def disconnectJoint(*args, attachHandleMode: bool = ..., deleteHandleMode: bool = ...) -> Any:
    r"""
    This command will break a skeleton at the selected joint and delete
    any associated handles.

    Args:
        attachHandleMode: (create) - This flag is obsolete and no longer supported.
        deleteHandleMode: (create) - Delete the handle on the associated joint.
    """
    ...


def dopeSheetEditor(*args, autoFit: Optional[Union[str, bool]] = ..., autoFitTime: Optional[Union[str, bool]] = ..., control: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., displayActiveKeyTangents: str = ..., displayActiveKeys: str = ..., displayInfinities: str = ..., displayKeys: str = ..., displayTangents: str = ..., displayValues: str = ..., docTag: Optional[Union[str, bool]] = ..., exists: bool = ..., filter: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., hierarchyBelow: bool = ..., highlightConnection: Optional[Union[str, bool]] = ..., lockMainConnection: bool = ..., lookAt: str = ..., mainListConnection: Optional[Union[str, bool]] = ..., outliner: Optional[Union[str, bool]] = ..., panel: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., selectionConnection: Optional[Union[str, bool]] = ..., selectionWindow: Optional[Union[Tuple[float, float, float, float], bool]] = ..., showScene: bool = ..., showSummary: bool = ..., showTicks: bool = ..., snapTime: Optional[Union[str, bool]] = ..., snapValue: Optional[Union[str, bool]] = ..., stateString: bool = ..., unParent: bool = ..., unlockMainConnection: bool = ..., updateMainConnection: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Edit a characteristic of a dope sheet editor

    Args:
        autoFit: (edit, query) - on | off | tgl Auto fit-to-view.
        autoFitTime: (edit, query) - on | off | tgl Auto fit-to-view along the time axis, as well.
        control: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        displayActiveKeyTangents: (edit) - on | off | tgl Display active key tangents in the editor.
        displayActiveKeys: (edit) - on | off | tgl Display active keys in the editor.
        displayInfinities: (edit) - on | off | tgl Display infinities in the editor.
        displayKeys: (edit) - on | off | tgl Display keyframes in the editor.
        displayTangents: (edit) - on | off | tgl Display tangents in the editor.
        displayValues: (edit) - on | off | tgl Display active keys and tangents values in the editor.
        docTag: (create, edit, query) - Attaches a tag to the editor.
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        filter: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        forceMainConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        hierarchyBelow: (edit, query) - display animation for objects hierarchically
        highlightConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        lockMainConnection: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        lookAt: (edit) - all | selected | currentTime FitView helpers.
        mainListConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        outliner: (edit, query) - the name of the outliner which is associated with the dope sheet
        panel: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        selectionConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        selectionWindow: (edit, query) - The selection area specified as left, right, bottom, top respectively.
        showScene: (edit, query) - display the scene summary object
        showSummary: (edit, query) - display the summary object
        showTicks: (edit, query) - display per animation tick divider in channel
        snapTime: (edit, query) - none | integer | keyframe Keyframe move snap in time.
        snapValue: (edit, query) - none | integer | keyframe Keyframe move snap in values.
        stateString: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        unParent: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
    """
    ...


def dropoffLocator(*args) -> Any:
    r"""
    This command adds one or more dropoff locators to a wire curve, one for
    each selected curve point. The dropoff locators can be used to provide
    localized tuning of the wire deformation about the curve point.
    
    The arguments are two floats, the envelope and percentage, followed by
    the wire node name and then by the curve point(s).

    Args:
    """
    ...


def effector(*args, hide: bool = ..., name: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The effector command is used to set the name or hidden
    flag for the effector.  The standard edit (-e) and query (-q) flags are
    used for edit and query functions.

    Args:
        hide: (create, edit, query) - Specifies whether to hide drawing of effector if attached to a handle.
        name: (create, edit, query) - Specifies the name of the effector.
    """
    ...


def enableDevice(*args, apply: bool = ..., device: Optional[Union[str, bool]] = ..., enable: bool = ..., monitor: bool = ..., record: bool = ..., query: bool = ...) -> Any:
    r"""
    Sets (or queries) the device enable state for actions involving the device.
    
    
    -monitor
    affects all assignInputDevice and attachDeviceAttr actions for
    the named device
    -record
    controls if the device is recorded (by default) by a recordDevice
    action
    -apply channelName [channelName ... ]
    controls if data from the  device channel is applied (by default)
    by applyTake to the param curves attached to the named channel.
    
    Disabling a channel for applyTake cause applyTake to ignore
    the enable state of all "child" channels -- treating them as disabled.

    Args:
        apply: (create, query) - enable/disable "applyTake" for the specified channel(s)
        device: (create, query) - specifies the device to change
        enable: (create, query) - enable (or disable) monitor/record/apply
        monitor: (create, query) - enables/disables visible update for the device (default)
        record: (create, query) - enable/disable "recordDevice" device recording
    """
    ...


def evaluationManager(*args, cycleCluster: Optional[Union[str, bool]] = ..., disableInfo: Optional[Union[str, bool]] = ..., empty: bool = ..., enabled: bool = ..., fallbackTriggered: bool = ..., idleAction: Optional[Union[int, bool]] = ..., idleBuild: bool = ..., invalidate: bool = ..., manipulation: bool = ..., manipulationPrevalidation: bool = ..., manipulationReady: bool = ..., mode: Optional[Union[str, bool]] = ..., downstreamFrom: Optional[Union[str, bool]] = ..., nodeTypeGloballySerialize: bool = ..., nodeTypeParallel: bool = ..., nodeTypeSerialize: bool = ..., nodeTypeUntrusted: bool = ..., upstreamFrom: Optional[Union[str, bool]] = ..., reduceGraphRebuild: bool = ..., safeMode: bool = ..., query: bool = ...) -> Any:
    r"""
    Handles turning on and off the evaluation manager method of evaluating the DG.
    Query the 'mode' flag to see all available evaluation modes. The special mode
    'off' disables the evaluation manager.
    The scheduling override flags 'nodeTypeXXX' force certain node types to use
    specific scheduling types, even though the node descriptions might indicate
    otherwise. Use with caution; certain nodes may not react well to
    alternative scheduling types.
    Only one scheduling type override will be in force at a time, the most
    restrictive one. In order, they are untrusted, globally serialized, locally
    serialized, and parallel. The node types will however remember all overrides.
    For example, if you set a node type override to be untrusted, then to be
    parallel it will continue to use the untrusted override. If you then turn off
    the untrusted override, the scheduling will advance to the parallel one.
    The actual node scheduling type is always superceded by the overrides. For example, a
    serial node will still be considered as parallel if the node type has the
    parallel override set, even though 'serial' is a more restrictive scheduling type.
    See the 'dbpeek' command 'graph' operation with arguments 'evaluationGraph' and
    'scheduling' to see what scheduling type any particular node will end up using
    after the hierarchy of overrides and native scheduling types is applied.

    Args:
        cycleCluster: (create, query) - Returns a list of nodes that are stored together with the given one in a cycle cluster. The list will be empty when the evaluation mode is not active or the node is not in a cycle.
        disableInfo: (query) - Returns a list of strings that contain the reasons that the evaluation manager has been disabled (as distinct from it being deliberately turned off, e.g. because an unsupported node type or attribute value was encountered). If the list is empty then the evaluation manager is operating normally.
        empty: (query) - Valid in query mode only. Checks to see if the evaluation graph has any nodes in it. This is independent of the current mode.
        enabled: (query) - Valid in query mode only. Checks to see if the evaluation manager is currently enabled. This is independent of the current mode.
        fallbackTriggered: (query) - Valid in query mode only. Checks to see if fallback serial evaluation has been triggered. Will be true if errors during parallel execution have forced a fallback to serial mode. Will reset to false if the mode is changed again after the fallback was triggered.
        idleAction: (create, query) - This flag sets the actions EM will perform on idle. It accepts the following values:  0 - No action 1 - Graph Rebuild 2 - EM Manipulation Preparation 3 - Graph Rebuild and EM Manipulation Preparation   Where:  Graph Rebuild will rebuild the evaluation graph on an idle event as soon as it is able to do so. EM ManipulationPreparation will get the evaluation manager to perform all the steps necessary for EM manipulation to be available after the next idle event.   Note: These idle actions only apply to the graph attached to the normal context. All other graphs will be built according to their own rules.  The disadvantage of enabling idle actions is that for some workflows that are changing the graph frequently, or very large graphs, the graph build and manipulation preparation time may impact the workflow. If workflows are impacted it is suggested to turn idle actions off by passing this flag a value of 0.
        idleBuild: (create, query) - This flag is obsolete. Please use the -idleAction flag with a value of 1 in order to activate evaluation graph rebuild on idle.
        invalidate: (create, query) - This flag invalidates the graph. Value is used to control auto rebuilding on idle (false) or forced (true). This command should be used as a last resort. In query mode it checks to see if the graph is valid.
        manipulation: (create, query) - This flag is used to activate evaluation manager manipulation support.
        manipulationPrevalidation: (create, query) - This flag is used to activate evaluation manager manipulation prevalidation. Prevalidation checks for known patterns in manipulation.  In case of a successful prevalidation, there is no need to use dirty propagation in the first frame of manipulation to validate that EM manipulation can safely be used, and fast manipulation can start right away.
        manipulationReady: (query) - Valid in query mode only. Checks to see if the evaluation manager manipulation is currently ready/allowed. This is independent of the current mode.
        mode: (create, query) - Changes the current evaluation mode in the evaluation manager. Supported values are "off", "serial" and "parallel".
        downstreamFrom: (create, query) - Find the DG nodes that are immediately downstream of the named one in the evaluation graph. Note that the connectivity is via evaluation mode connections, not DG connections. In query mode the graph is walked and any nodes downstream of the named one are returned. The return type is alternating pairs of values that represent the graph level and the node name, e.g. if you walk downstream from A in the graph A -> B -> C then the return will be the array of strings ("0","A","1","B","2","C"). Scripts can deconstruct this information into something more visually recognizable. Note that cycles are likely to be present so any such scripts would have to handle them. 			In query mode, this flag needs a value.
        nodeTypeGloballySerialize: (create, query) - This flag is used only when the evaluation manager is in "parallel" mode but can be set at anytime. It activates or deactivates the override to force global serial scheduling for the class name argument(s) in the evaluation manager. Legal object values are class type names: e.g. "transform", "skinCluster", "mesh". When queried without specified nodes, it returns the list of nodes with the global serial scheduling override active. Scheduling overrides take precedence over all of the node and node type scheduling rules. Use with caution; certain nodes may not react well to alternative scheduling types.
        nodeTypeParallel: (create, query) - This flag is used only when the evaluation manager is in "parallel" mode but can be set at anytime. It activates or deactivates the override to force parallel scheduling for the class name argument(s) in the evaluation manager. Legal object values are class type names: e.g. "transform", "skinCluster", "mesh". When queried without specified nodes, it returns the list of nodes with the parallel scheduling override active. Scheduling overrides take precedence over all of the node and node type scheduling rules. Use with caution; certain nodes may not react well to alternative scheduling types.
        nodeTypeSerialize: (create, query) - This flag is used only when the evaluation manager is in "parallel" mode but can be set at anytime. It activates or deactivates the override to force local serial scheduling for the class name argument(s) in the evaluation manager. Legal object values are class type names: e.g. "transform", "skinCluster", "mesh". When queried without specified nodes, it returns the list of nodes with the local serial scheduling override active. Scheduling overrides take precedence over all of the node and node type scheduling rules. Use with caution; certain nodes may not react well to alternative scheduling types.
        nodeTypeUntrusted: (create, query) - This flag is used only when the evaluation manager is in "parallel" mode but can be set at anytime. It activates or deactivates the override to force untrusted scheduling for the class name argument(s) in the evaluation manager. Legal object values are class type names: e.g. "transform", "skinCluster", "mesh". When queried without specified nodes, it returns the list of nodes with the untrusted scheduling override active. Scheduling overrides take precedence over all of the node and node type scheduling rules. Use with caution; certain nodes may not react well to alternative scheduling types. Untrusted scheduling will allow nodes to be evaluated in a critical section, separately from any other node evaluation. It should be used only as a last resort since the lost parallelism caused by untrusted nodes can greatly reduce performance.
        upstreamFrom: (create, query) - Find the DG nodes that are immediately upstream of the named one in the evaluation graph. Note that the connectivity is via evaluation mode connections, not DG connections. In query mode the graph is walked and any nodes upstream of the named one are returned. The return type is alternating pairs of values that represent the graph level and the node name, e.g. if you walk upstream from C in the graph A -> B -> C then the return will be the array of strings ("0","C","1","B","2","A"). Scripts can deconstruct this information into something more visually recognizable. Note that cycles are likely to be present so any such scripts would have to handle them. 			In query mode, this flag needs a value.
        reduceGraphRebuild: (create, query) - This flag is used to activate evaluation manager mode to minimize rebuild when animated node are connected to EM prepopulated plug.
        safeMode: (create, query) - This flag activates/deactivates parallel evaluation safe mode. When enabled, parallel execution will fall back to serial when evaluation graph is missing dependencies. Detection is happening on scheduling of parallel evaluation, which means potential fallback will happen at the next evaluation. WARNING: This mode should be disabled with extreme caution. It will prevent parallel mode from falling back to serial mode when an invalid evaluation is detected. Sometimes the evaluation will still work correctly in those situations and use of this flag will keep the peak parallel performance running. However since the safe mode is used to catch invalid evaluation disabling it may also cause problems with evaluation, anything from invalid values, missing evaluation, or even crashes.
    """
    ...


def evaluator(*args, clusters: bool = ..., configuration: Optional[Union[str, bool]] = ..., enable: bool = ..., info: bool = ..., name: Optional[Union[str, bool]] = ..., nodeType: Optional[Union[str, bool]] = ..., nodeTypeChildren: bool = ..., priority: Optional[Union[int, bool]] = ..., valueName: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    Handles turning on and off custom evaluation overrides used by the evaluation
    manager.
    Query no flag to see all available custom evaluators.
    Query the 'enable' flag to check if an evaluator is currently enabled.
    If the 'name' flag isn't used then return all modes and their current
    active state.

    Args:
        clusters: (query) - This flag queries the list of clusters currently assigned to the named custom evaluator. The return value will be an array of strings where the array consists of a set of (number, string[]) groups. e.g. If an evaluator has 2 clusters with 2 and 3 nodes in them respectively the output would be something like: (2, 'transform2', 'transform3', 3, 'joint1', 'joint2', 'joint3')
        configuration: (create, multiuse, query) - Sends configuration information to a custom evaluator. It's up to the evaluator to understand what they mean. Multiple configuration messages can be sent in a single command. Query this flag for a given evaluator to find out what configuration messages it accepts.
        enable: (create, query) - Enables or disables a specific graph evaluation runtime, depending on the state of the flag.  In order to use this flag you must also specify the name in the 'name' argument. When the 'enable' flag is used in conjunction with the 'nodeType' flag then it is used to selectively turn on or off the ability of the given evaluator to handle nodes of the given type (i.e. it no longer toggles the evaluator enabled state). When the 'enable' flag is used in conjunction with the 'configuration' flag then it is passed along with the configuration message interpreted by the custom evaluator.
        info: (query) - Queries the evaluator information. Only valid in query mode since the information is generated by the evaluator's internal state and cannot be changed. In order to use this flag, the 'name' argument must also be specified.
        name: (create, query) - Names a particular DG evaluation override evaluator. Evaluators are registered automatically by name. Query this flag to get a list of available runtimes. When a runtime is registered it is enabled by default. Use the 'enable' flag to change its enabled state. 			In query mode, this flag can accept a value.
        nodeType: (create, multiuse, query) - Names a particular node type to be passed to the evaluator request. Evaluators can either use or ignore the node type information as passed. 			In query mode, this flag can accept a value.
        nodeTypeChildren: (create, query) - If enabled when using the 'nodeType' flag then handle all of the node types derived from the given one as well. Default is to only handle the named node type.
        priority: (create, query) - Query or set the evaluator priority. Custom evaluator with highest priority order will get the chance to claim the nodes first.  Evaluators must have unique priority values. In order to use this flag you must also specify the name in the 'name' argument.
        valueName: (query) - Queries a value from a given evaluator.  Evaluators can define a set of values for which they answer. 			In query mode, this flag can accept a value.
    """
    ...


def filter(*args, name: Optional[Union[str, bool]] = ..., type: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Creates or modifies a filter node.  Filter nodes are used by applyTake
    to modify recorded device data before assigning it to the param curves
    for the attached attributes.

    Args:
        name: (create, edit, query) - Name for created filter
        type: (create, edit, query) - Filter type to create, One of:  filterEuler            Euler angle "demangler" filterResample         Resamples input data at fixed output rate with several filtering options filterSimplify         Combines groups of data points that are almost linear into lines segments filterClosestSample     Resamples input data a fixed output rate using the closest sample point
    """
    ...


def filterCurve(*args, cutoffFrequency: Optional[Union[float, bool]] = ..., endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., filter: Optional[Union[str, bool]] = ..., keepKeysOnFrame: bool = ..., kernel: Optional[Union[str, bool]] = ..., keySync: bool = ..., maxTimeStep: Optional[Union[float, bool]] = ..., minTimeStep: Optional[Union[float, bool]] = ..., period: Optional[Union[float, bool]] = ..., precision: Optional[Union[float, bool]] = ..., precisionMode: Optional[Union[int, bool]] = ..., preserveKeyTangent: Optional[Union[str, bool]] = ..., sampleCount: Optional[Union[int, bool]] = ..., samplingRate: Optional[Union[float, bool]] = ..., selectedKeys: bool = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., timeTolerance: Optional[Union[float, bool]] = ..., tolerance: Optional[Union[float, bool]] = ..., useQuaternion: bool = ..., width: Optional[Union[Union[float, Tuple[float, float]], bool]] = ...) -> Any:
    r"""
    The filterCurve command takes a list of anim curve and filters
            them using a specified filter. The following filters are supported:
            butterworth
    euler
    gaussian
    keyReducer
    peakRemover
    keySync
    resample
    simplify

    Args:
        cutoffFrequency: (create) - Defines the cutoff frequency (in Hz) for the Butterworth filter.
        endTime: (create) - Specify the end time of the section to filter. If not specified, the last key of the animation curve is used to define the end time.
        filter: (create) - Specifies the filter type to use. The avalible filters are: butterworth euler (default) gaussian keyReducer peakRemover keySync resample simplify
        keepKeysOnFrame: (create) - When specified, a secondary filter pass is applied to position keys on whole frames. This flag is only supported by the Butterworth filter.
        kernel: (create) - The resample kernel is a decimation resampling filter used to resample dense data. It works on the keyframes and may not produce the desired results when used with sparse data.  The resample filter converts from either uniform or non-uniform timestep input data samples to the specified uniform timeStep. Various time domain filters are available and are specified with the kernel flag which selects the resampling kernel applied to the keyframes on the animation curves.   Kernel Values closest  Closest sample to output timestamp lirp  Linear interpolation between closest samples box  Box filter: moving average triangle  Triangle filter: (1 - |x|)  weighted moving average gaussian2  Gaussian2 Filter: (2^(-2x*x))  weighted moving average gaussian4  Gaussian4 Filter: (2^(-4x*x))  weighted moving average   This filter is only targeted at decimation resampling -- interpolation resampling is basically unsupported.  If your output framerate is much higher than your input frame rate (approximate, as the input timestep is not assumed to be regular) the lirp and triangle will interpolate (usually) and the rest will either average, or use the closest sample (depending on the phase and frequency of the input).  However this mode of operation may not give the expected result.
        keySync: (create) - When specified, a secondary filter pass is applied that adds a key to sibling curves (X,Y,Z) for each key that is encountered. This flag is only supported by the Key Reducer filter.
        maxTimeStep: (create) - Simplify filter.
        minTimeStep: (create) - Simplify filter.
        period: (create) - Resample filter
        precision: (create) - Defines the precision parameter. For the Key Reducer filter, this parameter specifies the error limit between the source and output curves. Greater values reduce precision. Lower values increase precision.
        precisionMode: (create) - Defines whether the precision value should be treated as: 0: An absolute value 1: A percentage.
        preserveKeyTangent: (create, multiuse) - When specified, keys whose in or out tangent type match the specified type are preserved. Supported tangent types: fixed linear flat smooth step clamped plateau stepnext auto This flag is only supported by the Key Reducer filter.
        sampleCount: (create) - Defines the Gaussian filter kernel dimension.
        samplingRate: (create) - Defines the rate at which keys are added to the Butterworth filtered curve in frames per second (FPS).
        selectedKeys: (create) - When specified, the filter is only applied to selected keys. This flag supercedes the startTime/endTime specification.
        startTime: (create) - Specify the start time to filter. If not specified, then the first key in the animation curve is used to get the start time.
        timeTolerance: (create) - Simplify filter.
        tolerance: (create) - Simplify filter.
        useQuaternion: (create) - Enable to use quaternion instead of euler.
        width: (create) - Defines the width of the Gaussian filter.
    """
    ...


def findDeformers(*args) -> Any:
    r"""
    This command finds all deformers for the specified shape(s).
    
    If no shapes are specified on the command then the curently selected
    shapes are used.

    Args:
    """
    ...


def findKeyframe(*args, animation: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., controlPoints: bool = ..., curve: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., includeUpperBound: bool = ..., index: Optional[Union[int, bool]] = ..., shape: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., timeSlider: bool = ..., which: Optional[Union[str, bool]] = ...) -> Any:
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
    
    This command will return the time (in current units) of the requested
    key. For the relative direction methods (next, previous) if
    -time is NOT specified they will use current time.
    If the specified object is not animated the command will return
    the current time.

    Args:
        animation: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        controlPoints: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        curve: (create) - Return a list of the existing curves driving the selected object or attributes. The which, index, floatRange, timeRange, and includeUpperBound flags are ignored when this flag is used.
        float: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        hierarchy: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        includeUpperBound: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        shape: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        time: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
        timeSlider: (create) - Get the next key time from the ticks displayed in the time slider. If this flag is set, then the -an/animation flag is ignored.
        which: (create) - next | previous | first | last How to find the key
    """
    ...


def flexor(*args, atBones: bool = ..., atJoints: bool = ..., deformerCommand: Optional[Union[str, bool]] = ..., list: bool = ..., name: Optional[Union[str, bool]] = ..., noScale: bool = ..., toSkeleton: bool = ..., type: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a flexor. A flexor a deformer plus a set of
    driving    attributes. For example, a flexor might be a sculpt object
    that is driven by a joint's x rotation and a cube's y position.

    Args:
        atBones: (create) - Add a flexor at bones. Flexor will be added at each of the selected bones, or at all bones in the selected skeleton if the -ts flag is also specified.
        atJoints: (create) - Add a flexor at joints. Flexor will be added at each of the selected joints, or at all joints in the selected skeleton if the -ts flag is specified.
        deformerCommand: (create) - String representing underlying deformer command string.
        list: (query) - List all possible types of flexors. Query mode only.
        name: (create) - This flag is obsolete.
        noScale: (create) - Do not auto-scale the flexor to the size of the nearby geometry.
        toSkeleton: (create) - Specifies that flexors will be added to the entire skeleton rather than just to the selected joints/bones. This flag is used in conjunction with the -ab and -aj flags.
        type: (create) - Specifies which type of flexor. To see list of valid types, use the "flexor -query -list" command.
    """
    ...


def flow(*args, divisions: Optional[Union[Tuple[int, int, int], bool]] = ..., localCompute: bool = ..., localDivisions: Optional[Union[Tuple[int, int, int], bool]] = ..., objectCentered: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The flow command creates a deformation lattice to `bend' the object
    that is animated along a curve of a motion path animation.
    The motion path animation has to have the follow option set to be on.

    Args:
        divisions: (query) - This flag specifies the number of lattice slices in x,y,z. The default values are 2 5 2. When queried, it returns the uint32_t uint32_t uint32_t
        localCompute: (query) - This flag specifies whether or not to have local control over the object deformation. Default value: is on when the lattice is around the curve, and is off when the lattice is around the object.  When queried, it returns a boolean
        localDivisions: (query) - This flag specifies the extent of the region of effect. Default values are 2 2 2. When queried, it returns the uint32_t uint32_t uint32_t
        objectCentered: (query) - This flag specifies whether to create the lattice around the selected object at its center, or to create the lattice around the curve. Default value is true. When queried, it returns a boolean
    """
    ...


def freeze(*args, allNodes: bool = ..., displayLayers: bool = ..., downstream: bool = ..., forceDownstream: bool = ..., frozen: bool = ..., invisible: bool = ..., noFreeze: bool = ..., unfreeze: bool = ..., upstream: bool = ..., query: bool = ...) -> Any:
    r"""
    When a node is frozen none of its inputs will be requested when they
    change, the node will use the inputs that existed at the time of freezing
    until the node is unfrozen.
    A node can be frozen in one of two ways; either directly, via setting the
    "frozen" attribute on the node to be true, or indirectly, via setting the
    "frozenAffected" extension attribute on the node to be true.
    This command lets you freeze nodes based on various criteria. See the flags
    for the types of criteria the command uses to decide what to freeze or unfreeze.
    The nodes that are selected are frozen directly. The nodes affected by directly
    frozen nodes, considering the argument settings, are frozen indirectly.
    If the frozen attribute, visibililty, or display layer mode has an input
    connection then the frozen state will not propagate because the node could
    be unfrozen or become visible at playback time.
    In query mode this command will find the nodes with each of the frozen states
    set (frozen, frozenAffected, and neither).

    Args:
        allNodes: (create, query) - Select which nodes are to be used for the operation. If it is not set then the selection list will be used. If nothing is selected all nodes in the scene will be used. This flag can be used in query mode to find the set of frozen nodes in the scene. It can also be used in create mode with filters (displayLayers, invisible, or frozen) to target a specific subset of nodes in the scene.
        displayLayers: (create, query) - If this flag is enabled then the display layers on the list to be processed will be walked. Any nodes they control will be added to the processing list, providing the display layer visibility control is off and not connected. Note: Animated visibility or enabled states will be treated as matches to be thorough. No attempt is made to check for static animation.
        downstream: (create, query) - If this flag is enabled then the frozen state will attempt to propagate downstream from the selected nodes. e.g. the mesh shape deformations being controlled by a skeleton rig.
        forceDownstream: (create, query) - If this flag is enabled then the frozen state will attempt to propagate downstream from the selected nodes. e.g. the mesh shape deformations being controlled by a skeleton rig. Unlike the downstream flag though this one will freeze downstream nodes even if they have other, unfrozen, inputs.
        frozen: (create, query) - If this flag is enabled then the list of nodes to be processed will be filtered out so that only nodes with the frozen attribute already set are included. Otherwise all nodes being processed will first have their frozen attribute set before propagating the frozen state. This flag would only be used if nodes were previously frozen and the command is used to propagate the frozen state through the graph.
        invisible: (create, query) - If this flag is enabled then the invisible nodes on the list to be processed will be walked. Any nodes below them in the DAG hierarchy will be added to the processing list, providing the visibility attribute is not connected. Note: Animated visibility states will be treated as a match to be thorough. No attempt is made to check for static animation.
        noFreeze: (create, query) - This flag previews the nodes that will be frozen without actually freezing them.
        unfreeze: (create, query) - If this flag is enabled then the nodes being processed will have their frozen state turned off instead of on. All of the same filtering and propagating will be done when deciding which nodes to modify. In query mode this flag switches from returning the already-frozen nodes to returning the unfrozen nodes.
        upstream: (create, query) - If this flag is enabled then the frozen state will attempt to propagate upstream through the selected nodes. e.g. the param curves feeding into a frozen transform. Heuristics are applied to this propagation to ensure that upstream nodes that are still used by unfrozen nodes will stay unfrozen themselves.
    """
    ...


def freezeOptions(*args, displayLayers: bool = ..., downstream: Optional[Union[str, bool]] = ..., explicitPropagation: bool = ..., invisible: bool = ..., referencedNodes: bool = ..., runtimePropagation: bool = ..., upstream: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command provides access to the options used by the evaluation manager to
    handle propagation and recognition of when a node is in a frozen state.
    See the individual flags for the different options available.
    These values are all stored as user preferences and persist across sessions.

    Args:
        displayLayers: (create, query) - If this option is enabled then any nodes that are in an enabled, invisible display layer will be considered to be frozen, and the frozen state will propagate accordingly.
        downstream: (create, query) - Controls how frozen state is propagated downstream from currently frozen nodes. Valid values are "none" for no propagation, "safe" for propagation downstream only when all upstream nodes are frozen, and "force" for propagation downstream when any upstream node is frozen.
        explicitPropagation: (create, query) - When turned on this will perform an extra pass when the evaluation graph is constructed to perform intelligent propagation of the frozen state to related nodes as specified by the currently enabled options of the evaluation graph. See also "runtimePropagation". This option performs more thorough propagation of the frozen state, but requires extra time for recalculating the evaluation graph.
        invisible: (create, query) - If this option is enabled then any nodes that are invisible, either directly or via an invisible parent node, will be considered to be frozen, and the frozen state will propagate accordingly.
        referencedNodes: (create, query) - If this option is enabled then any nodes that are referenced in from a frozen referenced node will also be considered to be frozen, and the frozen state will propagate accordingly.
        runtimePropagation: (create, query) - When turned on this will allow the frozen state to propagate during execution of the evaluation graph. See also "explicitPropagation". This option allows frozen nodes to be scheduled for evaluation, but once it discovers a node that is frozen it will prune the evaluation based on the current set of enabled options. It only works in the downstream direction.
        upstream: (create, query) - Controls how frozen state is propagated upstream from currently frozen nodes. Valid values are "none" for no propagation, "safe" for propagation upstream only when all downstream nodes are frozen, and "force" for propagation upstream when any downstream node is frozen.
    """
    ...


def geomBind(*args, bindMethod: Optional[Union[int, bool]] = ..., falloff: Optional[Union[float, bool]] = ..., geodesicVoxelParams: Optional[Union[Tuple[int, bool], bool]] = ..., maxInfluences: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to compute weights using geodesic voxel binding algorithm.
    It works by setting the right weights values on an already-existing skinCluster
    node.
    Since this command uses GPU acceleration, it is not supported on headless
    versions of Maya, i.e. batch mode.

    Args:
        bindMethod: (create) - Specifies which bind algorithm to use. By default, Geodesic Voxel will be used. Available algorithms are: 3 - Geodesic Voxel
        falloff: (create, edit, query) - Falloff controlling the bind stiffness. Valid values range from [0..1].
        geodesicVoxelParams: (create, edit, query) - Specifies the geodesic voxel binding parameters. This flag is composed of three parameters: 0 - Maximum voxel grid resolution which must be a power of two. (ie. 64, 128, 256, etc. ) 1 - Performs a post voxel state validation when enabled. Default values are 256 true.
        maxInfluences: (create, edit, query) - Specifies the maximum influences a vertex can have. By default, all influences are used (-1).
    """
    ...


def geometryConstraint(*args, layer: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., remove: bool = ..., targetList: bool = ..., weight: Optional[Union[float, bool]] = ..., weightAliasList: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Constrain an object's position based on the shape of the target
    surface(s) at the closest point(s) to the object.
    
    A geometryConstraint takes as input one or more surface shapes (the
    targets) and a DAG transform node (the object).  The
    geometryConstraint position constrained object such object lies on
    the surface of the target with the greatest weight value.  If two
    targets have the same weight value then the one with the lowest index
    is chosen.

    Args:
        layer: (create, edit) - Specify the name of the animation layer where the constraint should be added.
        name: (create, edit, query) - Sets the name of the constraint node to the specified name.  Default name is constrainedObjectName_constraintType
        remove: (edit) - removes the listed target(s) from the constraint.
        targetList: (query) - Return the list of target objects.
        weight: (create, edit, query) - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
        weightAliasList: (query) - Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
    """
    ...


def ghosting(*args, action: Optional[Union[str, bool]] = ..., allGhostedObjects: bool = ..., allInRange: bool = ..., customFrames: Optional[Union[int, bool]] = ..., enable: bool = ..., farOpacity: Optional[Union[float, bool]] = ..., frames: bool = ..., geometryFilter: bool = ..., ghostedObjects: bool = ..., ghostsStep: Optional[Union[int, bool]] = ..., hierarchy: bool = ..., jointFilter: bool = ..., locatorFilter: bool = ..., mode: Optional[Union[str, bool]] = ..., nearOpacity: Optional[Union[float, bool]] = ..., postColor: Optional[Union[Tuple[float, float, float], bool]] = ..., postFrames: Optional[Union[int, bool]] = ..., preColor: Optional[Union[Tuple[float, float, float], bool]] = ..., preFrames: Optional[Union[int, bool]] = ..., preset: Optional[Union[str, bool]] = ..., resetAll: bool = ..., useDriver: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Provides an aggregated interface to all of the node-base ghosting parameters, as well
    as the global preferences used by this command for ghosting actions.
    Query the 'enable' flag to check if ghost drawing is currently enabled.
    If you run in create mode with no 'action' set then you will be modifying the current values of the ghosting parameters.
    If you have 'action=ghost' set then you will be modifying the current values of the ghosting parameters and then applying them to selected objects.

    Args:
        action: (create) - Define the actions to be performed by the command. Legal values are "ghost", "unghost", and "unghostAll". The "ghost" will try to enable ghosting on all _visible_ DAG objects in the selection list. Imtermediate transform nodes will only be ghosted if axis display are active.
        allGhostedObjects: (edit) - Only works in edit mode, specifying that the edits are to be applied to all ghosted objects instead of just the selected ones.
        allInRange: (create, edit, query) - In create mode, define the default value for whether keyframe mode should use every keyframe in the playback range or use the specified values. In edit mode, modify the all-in-range value for all ghosts. In create mode with the "ghost" action, also set the custom ghost all-in-range value for the selected objects.
        customFrames: (create, edit, multiuse, query) - In create mode, define the default value for the list of custom ghost frames. In edit mode, modify the custom ghost frames for all ghosts. The special frame number "-9999999" is used to remove all custom frames, circumventing a quirk in the command engine that does not allow passing an empty list. In create mode with the "ghost" action, also set the custom ghost frames for the selected objects.
        enable: (create, query) - Enables or disables ghost visibility on the entire scene. This does not modify any of the node ghosting attributes, it only globally enables or disables the drawing of any ghosts that have been defined on nodes. This is a preference-based flag so its value will persist between sessions, even if you load a new file with different ghost attribute settings.
        farOpacity: (create, edit, query) - In create mode, define the default value for the opacity value for ghosts farthest away from the current time. In edit mode, modify the opacity value of ghosts farthest away from the current time for all ghosts. In create mode with the "ghost" action, also set the opacity value of ghosts farthest away from the current time for the selected objects.
        frames: (query) - Queries the current set of ghost frames on the selected objects based on the ghosting mode, parameters set on the object, and the current time when relevant. Ignores the state of the ghosting enabled flag.
        geometryFilter: (create, edit, query) - In create mode, enable or disable the default ghost geometry filter. In create mode with the "ghost" action set, also filter the selection to omit geometry nodes if this flag is false.
        ghostedObjects: (query) - Only works in query mode to find the names of all currently ghosted DAG nodes.
        ghostsStep: (create, edit, query) - In create mode, define the default value for the number of steps (keyframes or frames) between ghosts. In edit mode, modify the number of steps (keyframes or frames) between ghosts. In create mode with the "ghost" action, also set the default number of steps (keyframes or frames) between ghosts for the selected objects.
        hierarchy: (create, edit, query) - Enables or disables the ghost hierarchy default value. When no ghosting action is set it does not modify any of the node ghosting attributes, it only sets the preference for how future commands will filter the list of affected nodes. When used in conjunction with a ghosting action it will fist set the preference value and then use that new value as a filter on the ghosting action. If a ghosting action is specified without this flag then the current value of the preference is used in its place. This is a preference-based flag so its value will persist between sessions, even if you load a new file with different ghost attribute settings.
        jointFilter: (create, edit, query) - In create mode, enable or disable the default ghost joint filter. In create mode with the "ghost" action set, also filter the selection to omit joint nodes if this flag is false.
        locatorFilter: (create, edit, query) - In create mode, enable or disable the default ghost locator filter. In create mode with the "ghost" action set, also filter the selection to omit locator nodes if this flag is false.
        mode: (create, edit, query) - Define the default mode for ghosting actions. Legal values are "preAndPost", "pre", "post", "custom", and "keyframes".
        nearOpacity: (create, edit, query) - In create mode, define the default value for the opacity value for ghosts nearest to the current time. In edit mode, modify the opacity value of ghosts nearest to the current time for all ghosts. In create mode with the "ghost" action, also set the opacity value of ghosts nearest to the current time for the selected objects.
        postColor: (create, edit, query) - In create mode, define the default value for the color of ghosts after the current time. In edit mode, modify the color of ghosts after the current time for all ghosts. In create mode with the "ghost" action, also set the color of ghosts after the current time for the selected objects.
        postFrames: (create, edit, query) - In create mode, define the default value for the number of ghosted frames after the current time. In edit mode, modify the number of ghosted frames after the current time for all ghosts. In create mode with the "ghost" action, also set the default number of ghosted frames after the current time for the selected objects.
        preColor: (create, edit, query) - In create mode, define the default value for the color of ghosts before the current time. In edit mode, modify the color of ghosts before the current time for all ghosts. In create mode with the "ghost" action, also set the color of ghosts before the current time for the selected objects.
        preFrames: (create, edit, query) - In create mode, define the default value for the number of ghosted frames before the current time. In edit mode, modify the number of ghosted frames before the current time for all ghosts. In create mode with the "ghost" action, also set the default number of ghosted frames before the current time for the selected objects.
        preset: (create, edit, query) - Define the default mode for ghosting presets. Legal values are "1s", "2s", "4s", "5s", "10s", and "Custom". Setting anything other than "Custom" fixes ghosts at 3 pre frames, 3 post frames, with a step value of the preset (e.g. "2s" means show ghosts at every second frame or keyframe)
        resetAll: (create, edit) - Reset all ghosting options to their default values. Use with caution!
        useDriver: (create, edit, query) - In create mode, enable or disable the default ghost use driver value. In edit mode, modify the use driver value of all existing ghosts. In create mode with the "ghost" action, also set the use driver value for the selected objects.
    """
    ...


def hikGlobals(*args, releaseAllPinning: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Sets global HumanIK flags for the application.

    Args:
        releaseAllPinning: (edit, query) - Sets the global release all pinning hik flag. When this flag is set, all pinning states are ignored.
    """
    ...


def ikfkDisplayMethod(*args, display: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    The ikfkDisplayMethod command is used to specify how ik/fk
          blending should be shown

    Args:
        display: (create, query) - Specify how ik/fk blending should be shown when the handle is selected. Possible choices are "none" (do not display any blending), "ik" (only show ik),"fk" (only show fk), and "ikfk" (show both ik and fk).
    """
    ...


def ikHandle(*args, autoPriority: bool = ..., connectEffector: bool = ..., createCurve: bool = ..., createRootAxis: bool = ..., curve: Optional[Union[str, bool]] = ..., disableHandles: bool = ..., enableHandles: bool = ..., endEffector: Optional[Union[str, bool]] = ..., exists: str = ..., forceSolver: bool = ..., freezeJoints: bool = ..., jointList: bool = ..., name: Optional[Union[str, bool]] = ..., numSpans: Optional[Union[int, bool]] = ..., parentCurve: bool = ..., positionWeight: Optional[Union[float, bool]] = ..., priority: Optional[Union[int, bool]] = ..., rootOnCurve: bool = ..., rootTwistMode: bool = ..., setupForRPsolver: bool = ..., simplifyCurve: bool = ..., snapCurve: bool = ..., snapHandleFlagToggle: bool = ..., snapHandleToEffector: bool = ..., solver: Optional[Union[str, bool]] = ..., startJoint: Optional[Union[str, bool]] = ..., sticky: Optional[Union[str, bool]] = ..., twistType: Optional[Union[str, bool]] = ..., weight: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The handle command is used to create, edit, and query a handle
    within Maya.  The standard edit (-e) and query (-q) flags are
    used for edit and query functions.
    
    If there are 2 joints selected and neither -startJoint nor
    -endEffector flags are not specified, then the handle will be
    created from the selected joints.
    
    If a single joint is selected and neither -startJoint nor
    -endEffector flags are specified, then the handle will be
    created with the selected joint as the end-effector and the
    start joint will be the top of the joint chain containing the
    end effector.
    
    The default values of the flags are:
    
    -name "ikHandle#"
    -priority 1
    -weight 1.0
    -positionWeight 1.0
    -solver "ikRPsolver"
    -forceSolver on
    -snapHandleFlagToggle on
    -sticky off
    -createCurve true
    -simplifyCurve true
    -rootOnCurve true
    -twistType linear
    -createRootAxis false
    -parentCurve true
    -snapCurve false
    -numSpans 1
    -rootTwistMode false.
    
    These attributes can be specified in creation mode, edited in
    edit mode (-e) or queried in query mode (-q).

    Args:
        autoPriority: (edit) - Specifies that this handle's priority is assigned automatically.  The assigned priority will be based on the hierarchy distance from the root of the skeletal chain to the start joint of the handle.
        connectEffector: (create, edit) - This option is set to true as default, meaning that end-effector translate is connected with the endJoint translate.
        createCurve: (create) - Specifies if a curve should automatically be created for the ikSplineHandle.
        createRootAxis: (create) - Specifies if a root transform should automatically be created above the joints affected by the ikSplineHandle. This option is used to prevent the root flipping singularity on a motion path.
        curve: (create, edit, query) - Specifies the curve to be used by the ikSplineHandle. Joints will be moved to align with this curve. This flag is mandatory if you use the -freezeJoints option.
        disableHandles: (edit) - set given handles to full fk (ikBlend attribute = 0.0)
        enableHandles: (edit) - set given handles to full ik (ikBlend attribute = 1.0)
        endEffector: (create, edit, query) - Specifies the end-effector of the handle's joint chain. The end effector may be specified with a joint or an end-effector.  If a joint is specified, an end-effector will be created at the same position as the joint and this new end-effector will be used as the end-effector.
        exists: (edit) - Indicates if the specified handle exists or not.
        forceSolver: (create, edit, query) - Forces the solver to be used everytime. It could also be known as animSticky. So, after you set the first key the handle is sticky.
        freezeJoints: (create, edit) - Forces the curve, specfied by -curve option, to align itself along the existing joint chain. When false, or unspecified, the joints will be moved to positions along the specified curve.
        jointList: (edit) - Returns the list of joints that the handle is manipulating.
        name: (create, edit, query) - Specifies the name of the handle.
        numSpans: (create) - Specifies the number of spans in the automatically generated curve of the ikSplineHandle.
        parentCurve: (create) - Specifies if the curve should automatically be parented to the parent of the first joint affected by the ikSplineHandle.
        positionWeight: (create, edit, query) - Specifies the position/orientation weight of a handle. This is used to compute the "distance" between the goal position and the end-effector position.  A positionWeight of 1.0 computes the distance as the distance between positions only and ignores the orientations.  A positionWeight of 0.0 computes the distance as the distance between the orientations only and ignores the positions.  A positionWeight of 0.5 attempts to weight the distances equally but cannot actually compute this due to unit differences. Because there is no way to add linear units and angular units.
        priority: (create, edit, query) - Sets the priority of the handle.  Logically, all handles with a lower number priority are solved before any handles with a higher numbered priority.  (All handles of priority 1 are solved before any handles of priority 2 and so on.)  Handle priorities must be ] 0.
        rootOnCurve: (create, edit, query) - Specifies if the root is locked onto the curve of the ikSplineHandle.
        rootTwistMode: (create, edit, query) - Specifies whether the start joint is allowed to twist or not. If not, then the required twist is distributed over the remaining joints. This applies to all the twist types.
        setupForRPsolver: (edit) - If the flag is set and ikSolver is ikRPsolver, call RPRotateSetup for the new ikHandle. It is for ikRPsolver only.
        simplifyCurve: (create) - Specifies if the ikSplineHandle curve should be simplified.
        snapCurve: (create) - Specifies if the curve should automatically snap to the first joint affected by the ikSplineHandle.
        snapHandleFlagToggle: (create, edit, query) - Specifies that the handle position should be snapped to the end-effector position if the end-effector is moved by the user.  Setting this flag on allows you to use forward kinematics to pose or adjust your skeleton and then to animate it with inverse kinematics.
        snapHandleToEffector: (edit) - All handles are immediately moved so that the handle position and orientation matches the end-effector position and orientation.
        solver: (create, edit, query) - Specifies the solver.  The complete list of available solvers may not be known until run-time because some of the solvers may be implemented as plug-ins.  Currently the only valid solver are ikRPsolver, ikSCsolver and ikSplineSolver.
        startJoint: (create, edit, query) - Specifies the start joint of the handle's joint chain.
        sticky: (create, edit, query) - Specifies that this handle is "sticky". Valid values are "off", "sticky", "superSticky". Sticky handles are solved when the skeleton is being manipulated interactively.  If a character has sticky feet, the solver will attempt to keep them in the same position as the user moves the character's root.  If they were not sticky, they would move along with the root.
        twistType: (create, edit, query) - Specifies the type of interpolation to be used by the ikSplineHandle.  The interpolation options are "linear", "easeIn", "easeOut", and "easeInOut".
        weight: (create, edit, query) - Specifies the handles weight in error calculations.  The weight only applies when handle goals are in conflict and cannot be solved simultaneously.  When this happens, a solution is computed that weights the "distance" from each goal to the solution by the handle's weight and attempts to minimize this value.  The weight must be ]= 0.
    """
    ...


def ikHandleDisplayScale(*args, edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This action modifies and queries the current display size of ikHandle.
    The default display scale is 1.0.

    Args:
    """
    ...


def ikSolver(*args, epsilon: Optional[Union[float, bool]] = ..., maxIterations: Optional[Union[int, bool]] = ..., name: Optional[Union[str, bool]] = ..., solverType: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The ikSolver command is used to set the attributes for an IK Solver
    or create a new one. The standard edit (-e) and query (-q) flags are
    used for edit and query functions.

    Args:
        epsilon: (create, edit, query) - max error
        maxIterations: (create, edit, query) - Sets the max iterations for a solution
        name: (create, edit, query) - Name of solver
        solverType: (create, edit, query) - valid solverType (only ikSystem knows what is valid) for creation of a new solver (required)
    """
    ...


def ikSystem(*args, allowRotation: bool = ..., autoPriority: bool = ..., autoPriorityMC: bool = ..., autoPrioritySC: bool = ..., list: Optional[Union[Tuple[int, int], bool]] = ..., snap: bool = ..., solve: bool = ..., solverTypes: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The ikSystem command is used to set the global snapping flag for handles
    and set the global solve flag for solvers.  The standard edit (-e) and
    query (-q) flags are used for edit and query functions.

    Args:
        allowRotation: (edit, query) - Set true to allow rotation of an ik handle with keys set on translation.
        autoPriority: (edit) - set autoPriority for all ikHandles
        autoPriorityMC: (edit) - set autoPriority for all multiChain handles
        autoPrioritySC: (edit) - set autoPriority for all singleChain handles
        list: (edit, query) - returns the solver execution order when in query mode(list of strings) changes execution order when in edit mode (int old position, int new position)
        snap: (edit, query) - Set global snapping
        solve: (edit, query) - Set global solve
        solverTypes: (query) - returns a list of valid solverTypes ( query only )
    """
    ...


def ikSystemInfo(*args, globalSnapHandle: bool = ..., query: bool = ...) -> Any:
    r"""
    This action modifies and queries the current ikSystem controls.

    Args:
        globalSnapHandle: (create, query) - If this flag is off, all ikHandles will not be snapped.
    """
    ...


def insertJoint(*args) -> Any:
    r"""
    This command will insert a new joint under the given or selected joint. If
    the given joint has child joints, they will be reparented under the new
    inserted joint.
    
    The given joint(or selected joint) should not have skin attached.
    The command works on the selected joint. No options or flags are necessary.

    Args:
    """
    ...


def joint(*args, absolute: bool = ..., angleX: Optional[Union[float, bool]] = ..., angleY: Optional[Union[float, bool]] = ..., angleZ: Optional[Union[float, bool]] = ..., assumePreferredAngles: bool = ..., automaticLimits: bool = ..., children: bool = ..., component: bool = ..., degreeOfFreedom: Optional[Union[str, bool]] = ..., exists: Optional[Union[str, bool]] = ..., limitSwitchX: bool = ..., limitSwitchY: bool = ..., limitSwitchZ: bool = ..., limitX: Optional[Union[Tuple[float, float], bool]] = ..., limitY: Optional[Union[Tuple[float, float], bool]] = ..., limitZ: Optional[Union[Tuple[float, float], bool]] = ..., name: Optional[Union[str, bool]] = ..., orientJoint: str = ..., orientation: Optional[Union[Tuple[float, float, float], bool]] = ..., position: Optional[Union[Tuple[float, float, float], bool]] = ..., radius: Optional[Union[float, bool]] = ..., relative: bool = ..., rotationOrder: Optional[Union[str, bool]] = ..., scale: Optional[Union[Tuple[float, float, float], bool]] = ..., scaleCompensate: bool = ..., scaleOrientation: Optional[Union[Tuple[float, float, float], bool]] = ..., secondaryAxisOrient: str = ..., setPreferredAngles: bool = ..., stiffnessX: Optional[Union[float, bool]] = ..., stiffnessY: Optional[Union[float, bool]] = ..., stiffnessZ: Optional[Union[float, bool]] = ..., symmetry: bool = ..., symmetryAxis: Optional[Union[str, bool]] = ..., zeroScaleOrient: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The joint command is used to create, edit, and query, joints
    within Maya. (The standard edit(-e) and query(-q) flags are
    used for edit and query functions). If the object is not
    specified, the currently selected object (dag object) will be
    used.
    
    Multiple objects are allowed only for the edit mode. The same
    edit flags will be applied on all the joints selected, except
    for -p without -r (set joint position in the world space). An
    ik handle in the object list is equivalent to the list of
    joints the ik handle commands. When -ch/children is present,
    all the child joints of the specified joints, including the
    joints implied by possible ik handles, will also be included.
    
    In the creation mode, a new joint will be created as a child
    of a selected transform or starts a hierarchy by itself if no
    transform is selected. An ik handle will be treated as a
    transform in the creation mode.
    
    The default values of the arguments are:
    
    -degreeOfFreedom xyz
    
    -name "Joint#"
    
    -position 0 0 0
    
    -absolute
    
    -dof "xyz"
    
    -scale 1.0 1.0 1.0
    
    -scaleCompensate true
    
    -orientation 0.0 0.0 0.0
    
    -scaleOrientation 0.0 0.0 0.0
    
    -limitX -360 360
    
    -limitY -360 360
    
    -limitZ -360 360
    
    -angleX 0.0
    
    -angleY 0.0
    
    -angleZ 0.0
    
    -stiffnessX 0.0
    
    -stiffnessY 0.0
    
    -stiffnessZ 0.0
    
    -limitSwitchX no
    
    -limitSwitchY no
    
    -limitSwitchZ no
    
    -rotationOrder xyz
    
    Those arguments can be specified in the creation mode,
    editied in the edit mode (-e), or queried in the query mode
    (-q).

    Args:
        absolute: (create, edit, query) - The joint center position is in absolute world coordinates. (This is the default.)
        angleX: (create, edit, query) - Set the x-axis angle. When queried, this flag returns a float.
        angleY: (create, edit, query) - Set the y-axis angle. When queried, this flag returns a float.
        angleZ: (create, edit, query) - Set the z-axis angle. When queried, this flag returns a float.
        assumePreferredAngles: (edit) - Meaningful only in the edit mode. It sets the joint angles to the corresponding preferred angles.
        automaticLimits: (create) - Meaningful only in edit mode. It sets the joint to appropriate hinge joint with joint limits. It modifies the joint only if (a) it connects exactly to two joints (one parent, one child), (b) it does not lie on the line drawn between the two connected joints, and the plane it forms with the two connected joints is perpendicular to one of its rotation axes.
        children: (edit) - It tells the command to apply all the edit options not only to the selected joints, but also to their descendent joints in the DAG.
        component: (create, edit) - Use with the -position switch to position the joint relative to its parent (like -relative) but to compute new positions for all children joints so their world coordinate positions do not change.
        degreeOfFreedom: (create, edit, query) - Specifies the degrees of freedom for the IK. Valid strings consist of non-duplicate letters from x, y, and z. The letters in the string indicate what rotations are to be used by IK. The order a letter appear in the string does not matter. Examples are x, yz, xyz. When queried, this flag returns a string. Modifying dof will change the locking state of the corresponding rotation attributes. The rule is: if an rotation is turned into a dof, it will be unlocked if it is currently locked. When it is turned into a non-dof, it will be locked if it is not currently locked.
        exists: (query) - Does the named joint exist? When queried, this flag returns a boolean.
        limitSwitchX: (create, edit, query) - Use the limit the x-axis rotation? When queried, this flag returns a boolean.
        limitSwitchY: (create, edit, query) - Use the limit the y-axis rotation? When queried, this flag returns a boolean.
        limitSwitchZ: (create, edit, query) - Use the Limit the z-axis rotation? When queried, this flag returns a boolean.
        limitX: (create, edit, query) - Set lower and upper limits on the x-axis of rotation.  Also turns on the joint limit. When queried, this flag returns 2 floats.
        limitY: (create, edit, query) - Set lower and upper limits on the y-axis of rotation.  Also turns on the joint limit. When queried, this flag returns 2 floats.
        limitZ: (create, edit, query) - Set lower and upper limits on the z-axis of rotation.  Also turns on the joint limit. When queried, this flag returns 2 floats.
        name: (create, edit, query) - Specifies the name of the joint. When queried, this flag returns a string.
        orientJoint: (edit) - The argument can be one of the following strings: xyz, yzx, zxy, zyx, yxz, xzy, none.  It modifies the joint orientation and scale orientation so that the axis indicated by the first letter in the argument will be aligned with the vector from this joint to its first child joint. For example, if the argument is "xyz", the x-axis will point towards the child joint.  The alignment of the remaining two joint orient axes are dependent on whether or not the -sao/-secondaryAxisOrient flag is used. If the -sao flag is used, see the documentation for that flag for how the remaining axes are aligned.  In the absence of a user specification for the secondary axis orientation, the rotation axis indicated by the last letter in the argument will be aligned with the vector perpendicular to first axis and the vector from this joint to its parent joint.  The remaining axis is aligned according the right hand rule.  If the argument is "none", the joint orientation will be set to zero and its effect to the hierarchy below will be offset by modifying the scale orientation.  The flag will be ignored if:  A. the joint has non-zero rotations when the argument is not "none".  B. the joint does not have child joint, or the distance to the child joint is zero when the argument is not "none".  C. either flag -o or -so is set.
        orientation: (create, edit, query) - The joint orientation. When queried, this flag returns 3 floats.
        position: (create, edit, query) - Specifies the position of the center of the joint. This position may be relative to the joint's parent or in absolute world coordinates (see -r and -a below). When queried, this flag returns 3 floats.
        radius: (create, edit, query) - Specifies the joint radius.
        relative: (create, edit, query) - The joint center position is relative to the joint's parent.
        rotationOrder: (create, edit, query) - The rotation order of the joint. The argument can be one of the following strings: xyz, yzx, zxy, zyx, yxz, xzy.
        scale: (create, edit, query) - Scale of the joint. When queried, this flag returns 3 floats.
        scaleCompensate: (create, edit, query) - It sets the scaleCompenstate attribute of the joint to the given argument. When this is true, the scale of the parent joint will be compensated before any rotation of this joint is applied, so that the bone to the joint is scaled but not the bones to its child joints. When queried, this flag returns an boolean.
        scaleOrientation: (create, edit, query) - Set the orientation of the coordinate axes for scaling. When queried, this flag returns 3 floats.
        secondaryAxisOrient: (edit) - The argument can be one of the following strings: xup, xdown, yup, ydown, zup, zdown, none.  This flag is used in conjunction with the -oj/orientJoint flag. It specifies the scene axis that the second axis should align with. For example, a flag combination of "-oj yzx -sao yup" would result in the y-axis pointing down the bone, the z-axis oriented with the scene's positive y-axis, and the x-axis oriented according to the right hand rule.
        setPreferredAngles: (edit) - Meaningful only in the edit mode. It sets the preferred angles to the current joint angles.
        stiffnessX: (create, edit, query) - Set the stiffness (from 0 to 100.0) for x-axis. When queried, this flag returns a float.
        stiffnessY: (create, edit, query) - Set the stiffness (from 0 to 100.0) for y-axis. When queried, this flag returns a float.
        stiffnessZ: (create, edit, query) - Set the stiffness (from 0 to 100.0) for z-axis. When queried, this flag returns a float.
        symmetry: (create, edit) - Create a symmetric joint from the current joint.
        symmetryAxis: (create, edit) - This flag specifies the axis used to mirror symmetric joints. Any combination of x, y, z can be used. This option is only used when the symmetry flag is set to True.
        zeroScaleOrient: (edit) - It sets the scale orientation to zero and compensate the change by modifing the translation and joint orientation for joint or rotation for general transform of all its child transformations.  The flag will be ignored if the flag -so is set.
    """
    ...


def jointCluster(*args, aboveBound: Optional[Union[float, bool]] = ..., aboveCluster: bool = ..., aboveDropoffType: Optional[Union[str, bool]] = ..., aboveValue: Optional[Union[float, bool]] = ..., belowBound: Optional[Union[float, bool]] = ..., belowCluster: bool = ..., belowDropoffType: Optional[Union[str, bool]] = ..., belowValue: Optional[Union[float, bool]] = ..., deformerTools: bool = ..., joint: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The joint cluster command adds high-level controls to
    manage the cluster percentage values on a bound skin
    around a joint. JointClusters are one way
    to create smooth bending behaviour on skin when joints
    rotate.
    
    
    .                a <---- aboveBound
    .    ____________a_________
    .                a         \
    .     Joint1     a       Joint2
    .   _____________a_______    \
    .                a       \    \     b  <--- belowBound
    .                a        \    \  b
    .                          \    b
    .                           \ b  \
    .                           b\    \
    .                         b   \ Joint3
    
    
    CVs/vertices between Joint1 and aaaaa (aboveBound) receive only
    translation/rotation/scale from Joint1. CVs vertices between aaaa and
    bbbb transition between translation/rotatation/scale from Joint1 and
    Joint2. CV2 beyand bbbbb (below bound) receive only translation/
    rotation scale from Joint3.

    Args:
        aboveBound: (create, edit, query) - Specifies the where the drop-off begins in the direction of the bone above the joint. A value of 100 indicates the entire length of the bone. The default value is 10.
        aboveCluster: (query) - Returns the name of the cluster associated with the bone above this joint.
        aboveDropoffType: (create, edit, query) - Specifies the type of percentage drop-off in the direction of the bone above this joint. Valid values are "linear", "exponential", "sine" and "none". Default is linear.
        aboveValue: (create, edit, query) - Specifies the drop-off percentage of the joint cluster in the direction of the bone above the cluster. A value of 100 indicates the entire length of the bone. The default value is 50.
        belowBound: (create, edit, query) - Specifies where the drop-off ends in the direction of the bone below the joint. A value of 100 indicates the entire length of the bone. The default value is 10.
        belowCluster: (query) - Returns the name of the cluster associated with this joint.
        belowDropoffType: (create, edit, query) - Specifies the type of type of percentage drop-off in the direction of the bone below this joint. Valid values are "linear", "exponential", "sine" and "none". Default is linear.
        belowValue: (create, edit, query) - Specifies the drop-off percentage of the joint cluster in the direction of the joint below the cluster. A value of 100 indicates the entire length of the bone. The default value is 50.
        deformerTools: (query) - Used to query for the helper nodes associated with the jointCluster.
        joint: (create) - Specifies the joint that the cluster should act about.
        name: (create) - This flag is obsolete.
    """
    ...


def jointDisplayScale(*args, absolute: bool = ..., ikfk: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This action modifies and queries the current display size of
    skeleton joints. The joint display size is controlled by a
    scale factor; a scale factor of 1 sets the display size to its
    default, which is 1 in diameter.
    With the plain format, the float argument is the factor with
    respect to the default size. When -a/absolute is used, the
    float argument refers to the diameter of the joint
    display size.

    Args:
        absolute: (create, edit, query) - Interpret the float argument as the display size as opposed to the scale factor.
        ikfk: (create, edit, query) - Set the display size of ik/fk skeleton joints.
    """
    ...


def jointLattice(*args, after: bool = ..., afterReference: bool = ..., before: bool = ..., components: bool = ..., creasing: Optional[Union[float, bool]] = ..., deformerTools: bool = ..., exclusive: Optional[Union[str, bool]] = ..., frontOfChain: bool = ..., geometry: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., joint: Optional[Union[str, bool]] = ..., lengthIn: Optional[Union[float, bool]] = ..., lengthOut: Optional[Union[float, bool]] = ..., lowerBindSkin: Optional[Union[str, bool]] = ..., lowerTransform: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., parallel: bool = ..., prune: bool = ..., remove: bool = ..., rounding: Optional[Union[float, bool]] = ..., selectedComponents: bool = ..., split: bool = ..., upperBindSkin: Optional[Union[str, bool]] = ..., upperTransform: Optional[Union[str, bool]] = ..., useComponentTags: bool = ..., widthLeft: Optional[Union[float, bool]] = ..., widthRight: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates/edits/queries a jointLattice deformer. The name
    of the created/edited object is returned. Usually you would make use of
    this functionality through the higher level flexor command.

    Args:
        after: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        components: (query) - Returns the components used by the deformer
        creasing: (create, edit, query) - Affects the bulging of lattice points on the inside of the bend.  Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.
        deformerTools: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        exclusive: (create, query) - Puts the deformation set in a deform partition.
        frontOfChain: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        joint: (create) - Specifies the joint which will be used to drive the bulging behaviours.
        lengthIn: (create, edit, query) - Affects the location of lattice points on the parent bone.  Positive/negative values cause the points to move away/towards the joint. Changing this parameter also modifies the regions affected by the creasing, rounding and width parameters. Default value is 0.0. When queried, this flag returns a float.
        lengthOut: (create, edit, query) - Affects the location of lattice points on the child bone. Positive/negative values cause the points to move away/towards the joint. Changing this parameter also modifies the regions affected by the creasing, rounding and width parameters. Default value is 0.0. When queried, this flag returns a float.
        lowerBindSkin: (create) - Specifies the node which is performing the bind skin operation on the geometry associated with the lower bone.
        lowerTransform: (create) - Specifies which dag node is being used to rigidly transform the lower part of the lattice which this node is going to deform. If this flag is not specified an identity matrix will be assumed.
        name: (create) - Used to specify the name of the node being created.
        parallel: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        prune: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        remove: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        rounding: (create, edit, query) - Affects the bulging of lattice points on the outside of the bend. Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.
        selectedComponents: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        split: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        upperBindSkin: (create) - Specifies the node which is performing the bind skin operation on the geometry associated with the upper bone.
        upperTransform: (create) - Specifies which dag node is being used to rigidly transform the upper part of the lattice which this node is going to deform. If this flag is not specified an identity matrix will be assumed.
        useComponentTags: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
        widthLeft: (create, edit, query) - Affects the bulging of lattice points on the left side of the bend. Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.
        widthRight: (create, edit, query) - Affects the bulging of lattice points on the right side of the bend. Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.
    """
    ...


def keyframe(*args, absolute: bool = ..., adjustBreakdown: bool = ..., animation: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., breakdown: bool = ..., clipTime: Optional[Union[Tuple[float, float, float], bool]] = ..., controlPoints: bool = ..., eval: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., floatChange: Optional[Union[float, bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., includeUpperBound: bool = ..., index: Optional[Union[int, bool]] = ..., indexValue: bool = ..., keyframeCount: bool = ..., lastSelected: bool = ..., name: bool = ..., option: Optional[Union[str, bool]] = ..., relative: bool = ..., selected: bool = ..., shape: bool = ..., tickDrawSpecial: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., timeChange: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., valueChange: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
    
    This command edits the time and/or value of keys of
    specified objects and/or parameter curves
    
    Unless otherwise specified by the -query flag, the command
    defaults to editing keyframes.

    Args:
        absolute: (create) - Move amounts are absolute.
        adjustBreakdown: (create) - When false, moving keys will not preserve breakdown timing, when true (the default) breakdowns will be adjusted to preserve their timing relationship.
        animation: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        breakdown: (create, edit, query) - Sets the breakdown state for the key.  Returns an integer.  Default is false.  The breakdown state of a key cannot be set in the same command as it is moved (i.e., via the -tc or -fc flags).
        clipTime: (create) - Modifies the final time where a key is inserted using an offset, pivot, and scale.
        controlPoints: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        eval: (create, query) - Returns the value(s) of the animCurves when evaluated (without regard to input connections) at the times given by the -t/time or -f/float flags.  Cannot be used in combination with other query flags, and cannot be used with time ranges (-t "5:10"). When no -t or -f flags appear on the command line, the evals are queried at the current time.  Query returns a float[].
        float: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        floatChange: (create, edit, query) - How much (with -relative) or where (with -absolute) to move keys (on non-time-input animation curves) along the x (float) axis. Returns float[] when queried.
        hierarchy: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        includeUpperBound: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        indexValue: (create, query) - Query-only flag that returns an int for the key's index.
        keyframeCount: (create, query) - Returns an int for the number of keys found for the targets.
        lastSelected: (create, query) - When used in queries, this flag returns requested values for the last selected key.
        name: (create, query) - Returns the names of animCurves of specified nodes, attributes or keys.
        option: (create, edit) - Valid values are "move," "insert," "over," and "segmentOver." When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to make room for the segment.
        relative: (create) - Move amounts are relative to a key's current position.
        selected: (create, query) - When used in queries, this flag returns requested values for any active keys.
        shape: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        tickDrawSpecial: (create, edit) - Sets the special drawing state for this key when it is drawn as a tick in the timeline.
        time: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
        timeChange: (create, edit, query) - How much (with -relative) or where (with -absolute) to move keys (on time-input animation curves) along the x (time) axis.  Returns float[] when queried.
        valueChange: (create, edit, query) - How much (with -relative) or where (with -absolute) to move keys along the y (value) axis. Returns float[] when queried.
    """
    ...


def keyframeOutliner(*args, animCurve: str = ..., annotation: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., display: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., fullPathName: bool = ..., height: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., isObscured: bool = ..., manage: bool = ..., noBackground: bool = ..., numberOfPopupMenus: bool = ..., parent: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., statusBarMessage: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., visible: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates/edits/queries a keyframe outliner control.

    Args:
        animCurve: (edit) - Name of the animation curve for which to display keyframes.
        annotation: (create, edit, query) - Annotate the control with an extra string value.
        backgroundColor: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        display: (edit, query) - narrow | wide What columns to display.  When "narrow", time and value will be displayed, when "wide" tangent information will be displayed as well
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
        statusBarMessage: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
        visible: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def keyframeStats(*args, adjustableColumn: Optional[Union[int, bool]] = ..., adjustableColumn2: Optional[Union[int, bool]] = ..., adjustableColumn3: Optional[Union[int, bool]] = ..., adjustableColumn4: Optional[Union[int, bool]] = ..., adjustableColumn5: Optional[Union[int, bool]] = ..., adjustableColumn6: Optional[Union[int, bool]] = ..., animEditor: Optional[Union[str, bool]] = ..., annotation: Optional[Union[str, bool]] = ..., autoUnitWidth: Optional[Union[int, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., classicMode: bool = ..., columnAlign: Optional[Union[Tuple[int, str], bool]] = ..., columnAlign2: Optional[Union[Tuple[str, str], bool]] = ..., columnAlign3: Optional[Union[Tuple[str, str, str], bool]] = ..., columnAlign4: Optional[Union[Tuple[str, str, str, str], bool]] = ..., columnAlign5: Optional[Union[Tuple[str, str, str, str, str], bool]] = ..., columnAlign6: Optional[Union[Tuple[str, str, str, str, str, str], bool]] = ..., columnAttach: Optional[Union[Tuple[int, str, int], bool]] = ..., columnAttach2: Optional[Union[Tuple[str, str], bool]] = ..., columnAttach3: Optional[Union[Tuple[str, str, str], bool]] = ..., columnAttach4: Optional[Union[Tuple[str, str, str, str], bool]] = ..., columnAttach5: Optional[Union[Tuple[str, str, str, str, str], bool]] = ..., columnAttach6: Optional[Union[Tuple[str, str, str, str, str, str], bool]] = ..., columnOffset2: Optional[Union[Tuple[int, int], bool]] = ..., columnOffset3: Optional[Union[Tuple[int, int, int], bool]] = ..., columnOffset4: Optional[Union[Tuple[int, int, int, int], bool]] = ..., columnOffset5: Optional[Union[Tuple[int, int, int, int, int], bool]] = ..., columnOffset6: Optional[Union[Tuple[int, int, int, int, int, int], bool]] = ..., columnWidth: Optional[Union[Tuple[int, int], bool]] = ..., columnWidth1: Optional[Union[int, bool]] = ..., columnWidth2: Optional[Union[Tuple[int, int], bool]] = ..., columnWidth3: Optional[Union[Tuple[int, int, int], bool]] = ..., columnWidth4: Optional[Union[Tuple[int, int, int, int], bool]] = ..., columnWidth5: Optional[Union[Tuple[int, int, int, int, int], bool]] = ..., columnWidth6: Optional[Union[Tuple[int, int, int, int, int, int], bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., fullPathName: bool = ..., height: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., isObscured: bool = ..., manage: bool = ..., noBackground: bool = ..., numberOfPopupMenus: bool = ..., parent: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., precision: Optional[Union[int, bool]] = ..., preventOverride: bool = ..., rowAttach: Optional[Union[Tuple[int, str, int], bool]] = ..., statusBarMessage: Optional[Union[str, bool]] = ..., timeAnnotation: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., valueAnnotation: Optional[Union[str, bool]] = ..., visible: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    All of the group commands position their individual controls in columns
    starting at column 1.  The layout of each control (ie. column) can be
    customized using the -cw/columnWidth, -co/columnOffset,
    -cat/columnAttach, -cal/columnAlign, and
    -adj/adjustableColumn flags.  By default, columns are left aligned
    with no offset and are 100 pixels wide.  Only one column in any group can
    be adjustable.
    
    This command creates, edits, queries a keyframe stats control.

    Args:
        adjustableColumn: (create, edit) - Specifies which column has an adjustable size that changes with the sizing of the layout.  The column value is a 1-based index. Passing 0 as argument turns off the previous adjustable column.
        adjustableColumn2: (create, edit) - Specifies which column has an adjustable size that changes with the size of the parent layout. Ignored if there are not exactly two columns.
        adjustableColumn3: (create, edit) - Specifies that the column has an adjustable size that changes with the size of the parent layout. Ignored if there are not exactly three columns.
        adjustableColumn4: (create, edit) - Specifies which column has an adjustable size that changes with the size of the parent layout. Ignored if there are not exactly four columns.
        adjustableColumn5: (create, edit) - Specifies which column has an adjustable size that changes with the size of the parent layout. Ignored if there are not exactly five columns.
        adjustableColumn6: (create, edit) - Specifies which column has an adjustable size that changes with the size of the parent layout. Ignored if there are not exactly six columns.
        animEditor: (edit, query) - The name of the animation editor which is associated with the control
        annotation: (create, edit, query) - Annotate the control with an extra string value.
        autoUnitWidth: (create, edit, query) - When this is non-zero the time fied widget will automatically scale based on the unit time settings (frame or timecode). The value of autoUnitWidth specifies the number of digits that should be able to be displayed as the frame number. So a value of 4 will make sure frame number 8723 can be displayed. When the value is zero the normal widget width will be used.
        backgroundColor: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        classicMode: (edit, query) - Edit display mode. True means stats only, otherwise show time value.
        columnAlign: (create, edit, multiuse) - Arguments are : column number, alignment type. Possible alignments are: left | right | center. Specifies alignment type for the specified column.
        columnAlign2: (create, edit) - Sets the text alignment of both columns.  Ignored if there are not exactly two columns. Valid values are "left", "right", and "center".
        columnAlign3: (create, edit) - Sets the text alignment for all three columns.  Ignored if there are not exactly three columns. Valid values are "left", "right", and "center".
        columnAlign4: (create, edit) - Sets the text alignment for all four columns.  Ignored if there are not exactly four columns. Valid values are "left", "right", and "center".
        columnAlign5: (create, edit) - Sets the text alignment for all five columns.  Ignored if there are not exactly five columns. Valid values are "left", "right", and "center".
        columnAlign6: (create, edit) - Sets the text alignment for all six columns.  Ignored if there are not exactly six columns. Valid values are "left", "right", and "center".
        columnAttach: (create, edit, multiuse) - Arguments are : column number, attachment type, and offset. Possible attachments are: left | right | both. Specifies column attachment types and offets.
        columnAttach2: (create, edit) - Sets the attachment type of both columns. Ignored if there are not exactly two columns. Valid values are "left", "right", and "both".
        columnAttach3: (create, edit) - Sets the attachment type for all three columns. Ignored if there are not exactly three columns. Valid values are "left", "right", and "both".
        columnAttach4: (create, edit) - Sets the attachment type for all four columns. Ignored if there are not exactly four columns. Valid values are "left", "right", and "both".
        columnAttach5: (create, edit) - Sets the attachment type for all five columns. Ignored if there are not exactly five columns. Valid values are "left", "right", and "both".
        columnAttach6: (create, edit) - Sets the attachment type for all six columns. Ignored if there are not exactly six columns. Valid values are "left", "right", and "both".
        columnOffset2: (create, edit) - This flag is used in conjunction with the -columnAttach2 flag.  If that flag is not used then this flag will be ignored.  It sets the offset for the two columns.  The offsets applied are based on the attachments specified with the -columnAttach2 flag.  Ignored if there are not exactly two columns.
        columnOffset3: (create, edit) - This flag is used in conjunction with the -columnAttach3 flag.  If that flag is not used then this flag will be ignored.  It sets the offset for the three columns.  The offsets applied are based on the attachments specified with the -columnAttach3 flag.  Ignored if there are not exactly three columns.
        columnOffset4: (create, edit) - This flag is used in conjunction with the -columnAttach4 flag.  If that flag is not used then this flag will be ignored.  It sets the offset for the four columns.  The offsets applied are based on the attachments specified with the -columnAttach4 flag.  Ignored if there are not exactly four columns.
        columnOffset5: (create, edit) - This flag is used in conjunction with the -columnAttach5 flag.  If that flag is not used then this flag will be ignored.  It sets the offset for the five columns.  The offsets applied are based on the attachments specified with the -columnAttach5 flag.  Ignored if there are not exactly five columns.
        columnOffset6: (create, edit) - This flag is used in conjunction with the -columnAttach6 flag.  If that flag is not used then this flag will be ignored.  It sets the offset for the six columns.  The offsets applied are based on the attachments specified with the -columnAttach6 flag.  Ignored if there are not exactly six columns.
        columnWidth: (create, edit, multiuse) - Arguments are : column number, column width. Sets the width of the specified column where the first parameter specifies the column (1 based index) and the second parameter specifies the width.
        columnWidth1: (create, edit) - Sets the width of the first column. Ignored if there is not exactly one column.
        columnWidth2: (create, edit) - Sets the column widths of both columns. Ignored if there are not exactly two columns.
        columnWidth3: (create, edit) - Sets the column widths for all 3 columns. Ignored if there are not exactly 3 columns.
        columnWidth4: (create, edit) - Sets the column widths for all 4 columns. Ignored if there are not exactly 4 columns.
        columnWidth5: (create, edit) - Sets the column widths for all 5 columns. Ignored if there are not exactly 5 columns.
        columnWidth6: (create, edit) - Sets the column widths for all 6 columns. Ignored if there are not exactly 6 columns.
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
        precision: (edit, query) - Controls the number of digits to the right of the decimal point that will be displayed for float-valued channels. Default is 3.  Queried, returns an int.
        preventOverride: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        rowAttach: (create, edit, multiuse) - Arguments are : column, attachment type, offset. Possible attachments are: top | bottom | both. Specifies attachment types and offsets for the entire row.
        statusBarMessage: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        timeAnnotation: (create, edit, query) - Annotate the time field with an extra string value.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
        valueAnnotation: (create, edit, query) - Annotate the value field with an extra string value.
        visible: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def keyframeTangentControl(*args, annotation: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., fullPathName: bool = ..., height: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., isObscured: bool = ..., manage: bool = ..., noBackground: bool = ..., numberOfPopupMenus: bool = ..., parent: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., precision: Optional[Union[int, bool]] = ..., preventOverride: bool = ..., statusBarMessage: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., visible: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates, edits, queries a keyframe tangent control.
    The control displays fields for modifying the selected keyframe's tangent
    angle and weight.

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
        precision: (edit, query) - Controls the number of digits to the right of the decimal point that will be displayed. Default is 3. Queried, returns an int.
        preventOverride: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        statusBarMessage: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
        visible: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def keyingGroup(*args, activator: Optional[Union[str, bool]] = ..., addElement: str = ..., afterFilters: bool = ..., anyMember: Optional[Union[str, bool]] = ..., category: Optional[Union[str, bool]] = ..., clear: str = ..., color: Optional[Union[int, bool]] = ..., copy: Optional[Union[str, bool]] = ..., edges: bool = ..., editPoints: bool = ..., empty: bool = ..., excludeDynamic: bool = ..., excludeRotate: bool = ..., excludeScale: bool = ..., excludeTranslate: bool = ..., excludeVisibility: bool = ..., facets: bool = ..., flatten: str = ..., forceElement: str = ..., include: str = ..., intersection: Optional[Union[str, bool]] = ..., isIntersecting: Optional[Union[str, bool]] = ..., isMember: Optional[Union[str, bool]] = ..., layer: bool = ..., minimizeRotation: bool = ..., name: Optional[Union[str, bool]] = ..., noIntermediate: bool = ..., noSurfaceShader: bool = ..., noWarnings: bool = ..., nodesOnly: bool = ..., remove: str = ..., removeActivator: str = ..., renderable: bool = ..., setActiveFilter: Optional[Union[str, bool]] = ..., size: bool = ..., split: Optional[Union[str, bool]] = ..., subtract: Optional[Union[str, bool]] = ..., text: Optional[Union[str, bool]] = ..., union: Optional[Union[str, bool]] = ..., vertices: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to manage the membership of a keying group.  Keying
    groups allow users to effectively manage related keyframe data, allowing
    keys on attributes in the keying group to be set and edited as a single
    entity.

    Args:
        activator: (edit, query) - Sets the selected node(s) as activators for the given keying group. In query mode, returns list of objects that activate the given keying group
        addElement: (edit) - Adds the list of items to the given set.  If some of the items cannot be added to the set because they are in another set which is in the same partition as the set to edit, the command will fail.
        afterFilters: (edit) - Default state is false. This flag is valid in edit mode only. This flag is for use on sets that are acted on by deformers such as sculpt, lattice, blendShape. The default edit mode is to edit the membership of the group acted on by the deformer. If you want to edit the group but not change the membership of the deformer, set the flag to true.
        anyMember: (create) - An operation which tests whether any of the given items are members of the given set.
        category: (create, edit, query) - Sets the keying group's category. This is what the global, active keying group filter will use to match.
        clear: (edit) - An operation which removes all items from the given set making the set empty.
        color: (create, edit, query) - Defines the hilite color of the set. Must be a value in range [-1, 7] (one of the user defined colors).  -1 marks the color has being undefined and therefore not having any affect. Only the vertices of a vertex set will be displayed in this color.
        copy: (create) - Copies the members of the given set to a new set. This flag is for use in creation mode only.
        edges: (create, query) - Indicates the new set can contain edges only. This flag is for use in creation or query mode only. The default value is false.
        editPoints: (create, query) - Indicates the new set can contain editPoints only. This flag is for use in creation or query mode only. The default value is false.
        empty: (create) - Indicates that the set to be created should be empty. That is, it ignores any arguments identifying objects to be added to the set. This flag is only valid for operations that create a new set.
        excludeDynamic: (create) - When creating the keying group, exclude dynamic attributes.
        excludeRotate: (create) - When creating the keying group, exclude rotate attributes from transform-type nodes.
        excludeScale: (create) - When creating the keying group, exclude scale attributes from transform-type nodes.
        excludeTranslate: (create) - When creating the keying group, exclude translate attributes from transform-type nodes. For example, if your keying group contains joints only, perhaps you only want to include rotations in the keying group.
        excludeVisibility: (create) - When creating the keying group, exclude visibility attribute from transform-type nodes.
        facets: (create, query) - Indicates the new set can contain facets only. This flag is for use in creation or query mode only. The default value is false.
        flatten: (edit) - An operation that flattens the structure of the given set. That is, any sets contained by the given set will be replaced by its members so that the set no longer contains other sets but contains the other sets' members.
        forceElement: (edit) - For use in edit mode only. Forces addition of the items to the set. If the items are in another set which is in the same partition as the given set, the items will be removed from the other set in order to keep the sets in the partition mutually exclusive with respect to membership.
        include: (edit) - Adds the list of items to the given set.  If some of the items cannot be added to the set, a warning will be issued. This is a less strict version of the -add/addElement operation.
        intersection: (create) - An operation that returns a list of items which are members of all the sets in the list.
        isIntersecting: (create) - An operation which tests whether the sets in the list have common members.
        isMember: (create) - An operation which tests whether all the given items are members of the given set.
        layer: (create) - OBSOLETE. DO NOT USE.
        minimizeRotation: (create, edit, query) - This flag only affects the attribute contained in the immediate keyingGroup. It does not affect attributes in sub-keyingGroups. Those will need to set minimizeRotation on their respective keyingGroups
        name: (create) - Assigns string as the name for a new set. This flag is only valid for operations that create a new set.
        noIntermediate: (create, query) - Excludes intermediate objects when querying set members or using the subtract, union, itersection, or isIntersecting flags.
        noSurfaceShader: (create) - If set is renderable, do not connect it to the default surface shader.  Flag has no meaning or effect for non renderable sets. This flag is for use in creation mode only. The default value is false.
        noWarnings: (create) - Indicates that warning messages should not be reported such as when trying to add an invalid item to a set. (used by UI)
        nodesOnly: (query) - This flag is usable with the -q/query flag but is ignored if used with another queryable flags. This flag modifies the results of the set membership query such that when there are attributes (e.g. sphere1.tx) or components of nodes included in the set, only the nodes will be listed. Each node will only be listed once, even if more than one attribute or component of the node exists in the set.
        remove: (edit) - Removes the list of items from the given set.
        removeActivator: (edit) - Removes the selected node(s) as activators for the given keying group.
        renderable: (create, query) - This flag indicates that a special type of set should be created. This type of set (shadingEngine as opposed to objectSet) has certain restrictions on its membership in that it can only contain renderable elements such as lights and geometry. These sets are referred to as shading groups and are automatically connected to the "renderPartition" node when created (to ensure mutual exclusivity of the set's members with the other sets in the partition). This flag is for use in creation or query mode only. The default value is false which means a normal set is created.
        setActiveFilter: (create, edit, query) - Sets the global, active keying group filter, which will affect activation of keying groups. Only keying groups with categories that match the filter will be activated. If the setActiveFilter is set to "NoKeyingGroups", keying groups will not be activated at all. If the setActiveFilter is set to "AllKeyingGroups", we will activate any keying group rather than just those with matching categories.
        size: (query) - Use the size flag to query the length of the set.
        split: (create) - Produces a new set with the list of items and removes each item in the list of items from the given set.
        subtract: (create) - An operation between two sets which returns the members of the first set that are not in the second set.
        text: (create, edit, query) - Defines an annotation string to be stored with the set.
        union: (create) - An operation that returns a list of all the members of all sets listed.
        vertices: (create, query) - Indicates the new set can contain vertices only. This flag is for use in creation or query mode only. The default value is false.
    """
    ...


def keyTangent(*args, absolute: bool = ..., animation: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., controlPoints: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., g: bool = ..., hierarchy: Optional[Union[str, bool]] = ..., inAngle: Optional[Union[float, bool]] = ..., inTangentType: Optional[Union[str, bool]] = ..., inWeight: Optional[Union[float, bool]] = ..., includeUpperBound: bool = ..., index: Optional[Union[int, bool]] = ..., ix: Optional[Union[float, bool]] = ..., iy: Optional[Union[float, bool]] = ..., lock: bool = ..., outAngle: Optional[Union[float, bool]] = ..., outTangentType: Optional[Union[str, bool]] = ..., outWeight: Optional[Union[float, bool]] = ..., ox: Optional[Union[float, bool]] = ..., oy: Optional[Union[float, bool]] = ..., pluginTangentTypes: Optional[Union[str, bool]] = ..., relative: bool = ..., shape: bool = ..., stepAttributes: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., unify: bool = ..., weightLock: bool = ..., weightedTangents: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
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
    
    This command edits or queries tangent properties of keyframes
    in a keyset.  It is also used to edit or query the default
    tangent type of newly created keyframes (see the setKeyframe
    command for more information on how to override this default).
    
    Tangents help manage the shape of the animation curve and affect
    the interpolation between keys.  The tangent angle specifies the
    direction the curve will take as it leaves (or enters) a key.
    The tangent weight specifies how much influence the tangent angle
    has on the curve before the curve starts towards the next key.
    
    Maya internally represents tangents as x and y values.  Refer to the API
    documentation for MFnAnimCurve for a description of the relationship
    between tangent angle and weight and the internal x and y values.

    Args:
        absolute: (create, edit) - Changes to tangent positions are NOT relative to the current position.
        animation: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        controlPoints: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        float: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        g: (create) - Required for all operations on the global tangent type. The global tangent type is used by the setKeyframe command when tangent types have not been specifically applied, except in combination with flags such as 'i/insert' which preserve the shape of the curve.  It is also used when keys are set from the menu. The only flags that can appear on a keyTangent command with the 'g/global' flag are 'itt/inTangentType', 'ott/outTangentType' and 'wt/weightedTangents'.
        hierarchy: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        inAngle: (create, edit, query) - New value for the angle of the in-tangent. Returns a float[] when queried.
        inTangentType: (create, edit, query) - Specify the in-tangent type.  Valid values are "spline," "linear," "fast," "slow," "flat," "step," "stepnext," "fixed," "clamped," "plateau", "auto", "autoease", "automix", and "autocustom". Returns a string[] when queried.
        inWeight: (create, edit, query) - New value for the weight of the in-tangent. Returns a float[] when queried.
        includeUpperBound: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        ix: (create, edit, query) - New value for the x-component of the in-tangent. This is a unit independent representation of the tangent component. Returns a float[] when queried.
        iy: (create, edit, query) - New value for the y-component of the in-tangent. This is a unit independent representation of the tangent component. Returns a float[] when queried.
        lock: (create, edit, query) - Lock a tangent so in and out tangents move together. Returns an int[] when queried.
        outAngle: (create, edit, query) - New value for the angle of the out-tangent. Returns a float[] when queried.
        outTangentType: (create, edit, query) - Specify the out-tangent type.  Valid values are "spline," "linear," "fast," "slow," "flat," "step," "stepnext," "fixed," "clamped," "plateau" and "auto", "autoease", "automix", and "autocustom". Returns a string[] when queried.
        outWeight: (create, edit, query) - New value for the weight of the out-tangent. Returns a float[] when queried.
        ox: (create, edit, query) - New value for the x-component of the out-tangent. This is a unit independent representation of the tangent component. Returns a float[] when queried.
        oy: (create, edit, query) - New value for the y-component of the out-tangent. This is a unit independent representation of the tangent component. Returns a float[] when queried.
        pluginTangentTypes: (query) - Returns a list of the plug-in tangent types that have been loaded. Return type is a string array.
        relative: (create, edit) - Changes to tangent positions are relative to the current position.
        shape: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        stepAttributes: (create, edit) - The setKeyframe command will automatically set tangents for boolean and enumerated attributes to step.  This flag mirrors this behavior for the keyTangent command.  When set to false, tangents for these attributes will not be edited.  When set to true (the default) tangents for these attributes will be edited.
        time: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
        unify: (create, edit) - Unify a tangent so in and out tangents are equal and move together.
        weightLock: (create, edit, query) - Lock the weight of a tangent so it is fixed. Returns an int[] when queried. Note: weightLock is only obeyed within the graph editor.  It is not obeyed when -inWeight/-outWeight are issued from a command.
        weightedTangents: (create, edit, query) - Specify whether or not the tangents on the animCurve are weighted Note: switching a curve from weightedTangents true to false and back to true again will not preserve fixed tangents properly. Use undo instead.
    """
    ...


def lattice(*args, after: bool = ..., afterReference: bool = ..., before: bool = ..., commonParent: bool = ..., components: bool = ..., deformerTools: bool = ..., divisions: Optional[Union[Tuple[int, int, int], bool]] = ..., dualBase: bool = ..., exclusive: Optional[Union[str, bool]] = ..., freezeMapping: bool = ..., frontOfChain: bool = ..., geometry: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., latticeReset: bool = ..., ldivisions: Optional[Union[Tuple[int, int, int], bool]] = ..., minimumSize: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., objectCentered: bool = ..., outsideFalloffDistance: Optional[Union[float, bool]] = ..., outsideLattice: Optional[Union[int, bool]] = ..., parallel: bool = ..., position: Optional[Union[Tuple[float, float, float], bool]] = ..., prune: bool = ..., remove: bool = ..., removeTweaks: bool = ..., rotation: Optional[Union[Tuple[float, float, float], bool]] = ..., scale: Optional[Union[Tuple[float, float, float], bool]] = ..., selectedComponents: bool = ..., split: bool = ..., useComponentTags: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a lattice deformer that will deform the selected
    objects. If the object centered flag is used, the initial lattice will
    fit around the selected objects. The lattice will be selected
    when the command is completed. The lattice deformer has an associated
    base lattice. Only objects which are contained by the base lattice
    will be deformed by the lattice.

    Args:
        after: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        commonParent: (create) - Group the base lattice and the deformed lattice under a common transform. This means that you can resize the lattice without affecting the deformation by resizing the common transform.
        components: (query) - Returns the components used by the deformer
        deformerTools: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        divisions: (create, edit, query) - Set the number of lattice slices in x, y, z. Default is 2, 5, 2. When queried, this flag returns float float float. When you change the number of divisions, any tweaking or animation of lattice points must be redone.
        dualBase: (create) - Create a special purpose ffd deformer node which accepts 2 base lattices. The default is off which results in the creation of a normal ffd deformer node. Intended for internal usage only.
        exclusive: (create, query) - Puts the deformation set in a deform partition.
        freezeMapping: (create, edit, query) - The base position of the geometries points is fixed at the time this flag is set.  When mapping is frozen, moving the geometry with respect to the lattice will not cause the deformation to be recomputed.
        frontOfChain: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        latticeReset: (edit) - Reset the lattice to match its base position. This will undo any deformations that the lattice is causing. The lattice will only deform points that are enclosed within the lattice's reset (base) position.
        ldivisions: (create, edit, query) - Set the number of local lattice slices in x, y, z.
        minimumSize: (create) - Set the minimum size of a side of the lattice during creation using the objectCentered flag which causes the lattice size to be determined from the geometry that is being deformed. When f.e. the object is a flat plane this can avoid the lattice to have size 0.0 along one side.
        name: (create) - Used to specify the name of the node being created.
        objectCentered: (create) - Centers the lattice around the selected object(s) or components. Default is off which centers the lattice at the origin.
        outsideFalloffDistance: (create) - Set the falloff distance used when the setting for transforming points outside of the base lattice is set to 2. The distance value is a positive number which specifies the size of the falloff distance as a multiple of the base lattice size, thus a value of 1.0 specifies that only points up to the base lattice width/height/depth away are transformed. A value of 0.0 is equivalent to an outsideLattice value of 0 (i.e. no points outside the base lattice are transformed). A huge value is equivalent to transforming an outsideLattice value of 1 (i.e. all points are transformed).
        outsideLattice: (create) - Set the mode describing how points outside the base lattice are transformed. 0 (the default) specifies that no outside points are transformed. 1 specifies that all outside points are transformed, and 2 specifies that only those outside points which fall within the "falloff distance" (see the -ofd/outsideFalloffDistance flag) are transformed. When querying, the current setting for the lattice is returned.
        parallel: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        position: (create) - Used to specify the position of the newly created lattice.
        prune: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        remove: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        removeTweaks: (edit) - Remove any lattice deformations caused by moving lattice points. Translations/rotations and scales on the lattice itself are not removed.
        rotation: (create) - Used to specify the initial rotation of the newly created lattice.
        scale: (create) - Used to specify the initial scale of the newly created lattice.
        selectedComponents: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        split: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        useComponentTags: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
    """
    ...


def listAnimatable(*args, active: bool = ..., manip: bool = ..., manipHandle: bool = ..., shape: bool = ..., type: bool = ...) -> Any:
    r"""
    This command list the animatable attributes of a node.  Command flags
    allow filtering by the current manipulator, or node type.

    Args:
        active: (create) - This flag is obsolete and no longer supported.
        manip: (create) - Return only those attributes affected by the current manip. If there is no manip active and any other flags are specified, output is the same as if the "-manip" flag were not present.
        manipHandle: (create) - Return only those attributes affected by the current manip handle. If there is no manip handle active and any other flags are specified, output is the same as if the "-manipHandle" flag were not present.
        shape: (create) - This flag is obsolete and no longer supported.
        type: (create) - Instead of returning attributes, Return the types of nodes that are currently animatable.
    """
    ...


def marker(*args, attach: bool = ..., detach: bool = ..., frontTwist: Optional[Union[float, bool]] = ..., orientationMarker: bool = ..., positionMarker: bool = ..., sideTwist: Optional[Union[float, bool]] = ..., time: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., upTwist: Optional[Union[float, bool]] = ..., valueU: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The marker command creates one or two markers, on a motion path curve,
    at the specified time and location.
    The optionnal string argument is the parent object name.
    
    One can specify "-pm -om" option to create both, a position marker
    and an orientation marker.
    
    Since there is only one keyframe for each marker of the same type,
    no more than one marker of the same type with the same time value
    can exist.
    
    The default marker type is the position marker. The default time is
    the current time.

    Args:
        attach: (create) - This flag specifies to attach the selected 3D position markers to their parent geometry.
        detach: (create) - This flag specifies to detach the selected position markers from their parent geometry to the 3D space.
        frontTwist: (query) - This flag specifies the amount of twist angle about the front vector for the marker. Default is 0. When queried, this flag returns a angle.
        orientationMarker: (query) - This flag specifies creation of an orientation marker. Default is not set.. When queried, this flag returns a boolean.
        positionMarker: (query) - This flag specifies creation of a position marker. Default is set. When queried, this flag returns a boolean.
        sideTwist: (query) - This flag specifies  the amount of twist angle about the side vector for the marker. Default is 0. When queried, this flag returns a angle.
        time: (query) - This flag specifies the time for the marker. Default is the current time. When queried, this flag returns a time.
        upTwist: (query) - This flag specifies the amount of twist angle about the up vector for the marker. Default is 0. When queried, this flag returns a angle.
        valueU: (query) - This flag specifies the location of the position marker w.r.t. the parent geometry u parameterization. Default is the value at current time. When queried, this flag returns a linear.
    """
    ...


def mimicManipulation(*args, manipulations: Optional[Union[str, bool]] = ..., prevalidation: bool = ..., refresh: bool = ...) -> Any:
    r"""
    This command mimics what various manipulators do to support
    Evaluation-Manager-accelerated manipulation.  This command should be
    use for testing, debugging and benchmarking purposes.
    Manipulations are described using a string representing a JSON object.
    This object must have a member named "session" containing an array,
    where each member of that array represents a manipulation transaction,
    i.e. plugs set by a single manipulation action.  Each of these transactions
    is also an array of plugs to set.  A plug to set is an object with a
    "plug" member, which is a string describing the plug to be manipulated,
    and a "value" member, which is the value to set to this plug.  Note that
    only plugs with attributes of type "double" or "double3" can currently be
    set and the value must be a number or an array of 3 numbers.
    A session can be thought of as the global action of a manipulation, from
    the time the manipulator is grabbed to the moment it is released, including
    the movements in between.  A transaction can be thought of as one delta
    inside the manipulation after which evaluation must happen to show the
    results, like a single mouse movement while the manipulator is held after
    which evaluation and viewport refresh must occur.

    Args:
        manipulations: (create) - JSON string representing the manipulations to be performed.
        prevalidation: (create) - Flag to control if prevalidation of the manipulated plugs will be performed.  If it is and the plugs are already properly supported by the Evaluation Manager, Evaluation Manager manipulation will be used on the very first frame instead of requiring an initial frame with dirty propagation and DG evaluation to validate Evaluation Manager manipulation can be safely performed.
        refresh: (create) - Flag to control if a refresh is triggered after each manipulation. Note that refresh is necessary for evaluation to kick in.
    """
    ...


def mirrorJoint(*args, mirrorBehavior: bool = ..., mirrorXY: bool = ..., mirrorXZ: bool = ..., mirrorYZ: bool = ..., searchReplace: Optional[Union[Tuple[str, str], bool]] = ...) -> Any:
    r"""
    This command will duplicate a branch of the skeleton from the selected
    joint symmetrically about a plane in world space.
    There are three mirroring modes(xy-, yz-, xz-plane).

    Args:
        mirrorBehavior: (create) - The mirrorBehavior flag is used to specify that when performing the mirror, the joint orientation axes should be mirrored such that equal rotations on the original and mirrored joints will place the skeleton in a mirrored position (symmetric across the mirroring plane). Thus, animation curves from the original joints can be copied to the mirrored side to produce a similar (but symmetric) behavior. When mirrorBehavior is not specified, the joint orientation on the mirrored side will be identical to the source side.
        mirrorXY: (create) - mirror skeleton from the selected joint about xy-plane in world space.
        mirrorXZ: (create) - mirror skeleton from the selected joint about xz-plane in world space.
        mirrorYZ: (create) - mirror skeleton from the selected joint about yz-plane in world space.
        searchReplace: (create) - After performing the mirror, rename the new joints by searching the name for the first specified string and replacing it with the second specified string.
    """
    ...


def movieInfo(*args, counter: bool = ..., dropFrame: bool = ..., frameCount: bool = ..., frameDuration: bool = ..., height: bool = ..., movieTexture: bool = ..., negTimesOK: bool = ..., numFrames: bool = ..., quickTime: bool = ..., timeCode: bool = ..., timeCodeTrack: bool = ..., timeScale: bool = ..., twentyFourHourMax: bool = ..., width: bool = ...) -> Any:
    r"""
    movieInfo provides a mechanism for querying information about movie
    files.

    Args:
        counter: (create) - Query the 'counter' flag of the movie's timecode format. If this is true, the timecode returned by the -timeCode flag will be a simple counter. If false, the returned timecode will be an array of integers (hours, minutes, seconds, frames).
        dropFrame: (create) - Query the 'drop frame' flag of the movie's timecode format.
        frameCount: (create) - Query the number of frames in the movie file
        frameDuration: (create) - Query the frame duration of the movie's timecode format.
        height: (create) - Query the height of the movie
        movieTexture: (create) - If set, the string argument is interpreted as the name of a movie texture node, and the command then operates on the movie loaded by that node.
        negTimesOK: (create) - Query the 'neg times OK' flag of the movie's timecode format.
        numFrames: (create) - Query the whole number of frames per second of the movie's timecode format.
        quickTime: (create) - Query whether the movie is a QuickTime movie.
        timeCode: (create) - Query the timecode of the current movie frame.
        timeCodeTrack: (create) - Query whether the movie has a timecode track.
        timeScale: (create) - Query the timescale of the movie's timecode format.
        twentyFourHourMax: (create) - Query the '24 hour max' flag of the movie's timecode format.
        width: (create) - Query the width of the movie
    """
    ...


def movIn(*args, file: Optional[Union[str, bool]] = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ...) -> Any:
    r"""
    Imports a .mov file into animation curves connected to  the listed
    attributes. The attribute must be writable, since an animation curve
    will be created and connected to the attribute. If an animation curve
    already is connected to the attribute, the imported data is pasted onto
    that curve.
    
    The starting time used for the .mov file importation is the current time
    when the command is executed.
    
    Valid attribute types are numeric attributes; time attributes; linear
    attributes; angular attributes; compound attributes made of the types
    listed previously; and multi attributes composed of the types listed
    previously. If an unsuppoted attribute type is requested, the command
    will fail and no data will be imported. It is important that your
    user units are set to the same units used in the .mov file, otherwise
    linear and angular values will be incorrect.
    
    To export a .mov file, use the movOut command.

    Args:
        file: (create) - The name of the .mov file. If no extension is used, a .mov will be added.
        startTime: (create) - The default start time for importing the .mov file is the current time. The startTime option sets the starting time for the .mov data in the current time unit.
    """
    ...


def movOut(*args, comment: bool = ..., file: Optional[Union[str, bool]] = ..., precision: Optional[Union[int, bool]] = ..., time: Optional[Union[Tuple[float, float], bool]] = ...) -> Any:
    r"""
    Exports a .mov file from the listed attributes. Valid attribute types
    are numeric attributes; time attributes; linear attributes; angular
    attributes; compound attributes made of the types listed previously;
    and multi attributes composed of the types listed previously.
    
    Length, angle, and time values will be written to the file in the
    user units.
    
    If an unsupported attribute type is requested, the action will fail.
    The .mov file may be read back into Maya using the movIn command.

    Args:
        comment: (create) - If true, the attributes written to the .mov file will be listed in a commented section at the top of the .mov file. The default is false.
        file: (create) - The name of the .mov file. If no extension is used, a .mov will be added.
        precision: (create) - Sets the number of digits to the right of the decimal place in the .mov file. C: The default is 6.
        time: (create) - The time range to save as a .mov file. The default is the current time range.
    """
    ...


def mute(*args, disable: bool = ..., force: bool = ..., query: bool = ...) -> Any:
    r"""
    The mute command is used to disable and enable playback on a channel. When a channel is muted, it retains the value that it was at prior to being muted.

    Args:
        disable: (create) - Disable muting on the channels
        force: (create) - Forceable disable of muting on the channels. If there are keys on the mute channel, the animation and mute node will both be removed.  If this flag is not set, then mute nodes with animation will only be disabled.
    """
    ...


def nonLinear(*args, after: bool = ..., afterReference: bool = ..., autoParent: bool = ..., before: bool = ..., commonParent: bool = ..., components: bool = ..., defaultScale: bool = ..., deformerTools: bool = ..., exclusive: Optional[Union[str, bool]] = ..., frontOfChain: bool = ..., geometry: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., name: Optional[Union[str, bool]] = ..., parallel: bool = ..., prune: bool = ..., remove: bool = ..., selectedComponents: bool = ..., split: bool = ..., type: Optional[Union[str, bool]] = ..., useComponentTags: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a functional deformer of the specified type that
    will deform the selected objects.  The deformer consists of
    three nodes: The deformer driver that gets connected to the
    history of the selected objects, the deformer handle transform
    that controls position and orientation of the axis of the deformation
    and the deformer handle that maintains the deformation parameters.
    The type of the deformer handle shape created depends on the
    specified type of the deformer.  The deformer handle
    will be positioned at the center of the selected objects' bounding
    box and oriented to match the orientation of the leading object
    in the selection list.  The deformer handle transform will be
    selected when the command is completed.
    
    The nonLinear command has some flags which are specific to the
    nonLinear type specified with the -type flag. The flags correspond to
    the primary keyable attributes related to the specific type of
    nonLinear node. For example, if the type is "bend", then the flags
    "-curvature", "-lowBound" and "-highBound" may be used to initialize,
    edit or query those attribute values on the bend node. Examples
    of this are covered in the example section below.

    Args:
        after: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        autoParent: (create) - Parents the deformer handle under the selected object's transform. This flag is valid only when a single object is selected.
        before: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        commonParent: (create) - Creates a new transform and parents the selected object and the deformer handle under it.  This flag is valid only when a single object is selected.
        components: (query) - Returns the components used by the deformer
        defaultScale: (create) - Sets the scale of the deformation handle to 1.  By default the deformation handle is scaled to the match the largest dimension of the selected objects' bounding box. [deformerFlags] The attributes of the deformer handle shape can be set upon creation, edited and queried as normal flags using either the long or the short attribute name.  e.g.
        deformerTools: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        exclusive: (create, query) - Puts the deformation set in a deform partition.
        frontOfChain: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        name: (create) - Used to specify the name of the node being created.
        parallel: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        prune: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        remove: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        selectedComponents: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        split: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        type: (create) - Specifies the type of deformation. The current valid deformation types are:  bend, twist, squash, flare, sine and wave
        useComponentTags: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
    """
    ...


def normalConstraint(*args, aimVector: Optional[Union[Tuple[float, float, float], bool]] = ..., layer: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., remove: bool = ..., targetList: bool = ..., upVector: Optional[Union[Tuple[float, float, float], bool]] = ..., weight: Optional[Union[float, bool]] = ..., weightAliasList: bool = ..., worldUpObject: Optional[Union[str, bool]] = ..., worldUpType: Optional[Union[str, bool]] = ..., worldUpVector: Optional[Union[Tuple[float, float, float], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Constrain an object's orientation based on the normal of the target
    surface(s) at the closest point(s) to the object.
    
    A normalConstraint takes as input one or more surface shapes (the
    targets) and a DAG transform node (the object).  The normalConstraint
    orients the constrained object such that the aimVector (in the
    object's local coordinate system) aligns in world space to combined
    normal vector.  The upVector (again the the object's local coordinate
    system) is aligned in world space with the worldUpVector.  The
    combined normal vector is a weighted average of the normal vector
    for each target surface at the point closest to the constrained object.

    Args:
        aimVector: (create, edit, query) - Set the aim vector.  This is the vector in local coordinates that points at the target.  If not given at creation time, the default value of (1.0, 0.0, 0.0) is used.
        layer: (create, edit) - Specify the name of the animation layer where the constraint should be added.
        name: (create, edit, query) - Sets the name of the constraint node to the specified name.  Default name is constrainedObjectName_constraintType
        remove: (edit) - removes the listed target(s) from the constraint.
        targetList: (query) - Return the list of target objects.
        upVector: (create, edit, query) - Set local up vector.  This is the vector in local coordinates that aligns with the world up vector.  If not given at creation time, the default value of (0.0, 1.0, 0.0) is used.
        weight: (create, edit, query) - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
        weightAliasList: (query) - Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
        worldUpObject: (create, edit, query) - Set the DAG object use for worldUpType "object" and "objectrotation". See worldUpType for greater detail. The default value is no up object, which is interpreted as world space.
        worldUpType: (create, edit, query) - Set the type of the world up vector computation. The worldUpType can have one of 5 values: "scene", "object", "objectrotation", "vector", or "none". If the value is "scene", the upVector is aligned with the up axis of the scene and worldUpVector and worldUpObject are ignored. If the value is "object", the upVector is aimed as closely as possible to the origin of the space of the worldUpObject and the worldUpVector is ignored. If the value is "objectrotation" then the worldUpVector is interpreted as being in the coordinate space of the worldUpObject, transformed into world space and the upVector is aligned as closely as possible to the result. If the value is "vector", the upVector is aligned with worldUpVector as closely as possible and worldUpMatrix is ignored. Finally, if the value is "none" no twist calculation is performed by the constraint, with the resulting "upVector" orientation based previous orientation of the constrained object, and the "great circle" rotation needed to align the aim vector with its constraint. The default worldUpType is "vector".
        worldUpVector: (create, edit, query) - Set world up vector.  This is the vector in world coordinates that up vector should align with. See -wut/worldUpType (below)for greater detail. If not given at creation time, the default value of (0.0, 1.0, 0.0) is used.
    """
    ...


def orientConstraint(*args, createCache: Tuple[float, float] = ..., deleteCache: bool = ..., layer: Optional[Union[str, bool]] = ..., maintainOffset: bool = ..., name: Optional[Union[str, bool]] = ..., offset: Optional[Union[Tuple[float, float, float], bool]] = ..., remove: bool = ..., skip: Optional[Union[str, bool]] = ..., targetList: bool = ..., weight: Optional[Union[float, bool]] = ..., weightAliasList: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Constrain an object's orientation to match the orientation of the
    target or the average of a number of targets.
    
    An orientConstraint takes as input one or more "target" DAG transform
    nodes to control the orientation of the single "constraint object"
    DAG transform  The orientConstraint orients the constrained object
    to match the weighted average of the target world space orientations.

    Args:
        createCache: (edit) - This flag is used to generate an animation curve that serves as a cache for the constraint. The two arguments define the start and end frames.  The cache is useful if the constraint has multiple targets and the constraint's interpolation type is set to "no flip". The "no flip" mode prevents flipping during playback, but the result is dependent on the previous frame.  Therefore in order to consistently get the same result on a specific frame, a cache must be generated. This flag creates the cache and sets the constraint's interpolation type to "cache". If a cache exists already, it will be deleted and replaced with a new cache.
        deleteCache: (edit) - Delete an existing interpolation cache.
        layer: (create, edit) - Specify the name of the animation layer where the constraint should be added.
        maintainOffset: (create) - The offset necessary to preserve the constrained object's initial orientation will be calculated and used as the offset.
        name: (create, edit, query) - Sets the name of the constraint node to the specified name.  Default name is constrainedObjectName_constraintType
        offset: (create, edit, query) - Sets or queries the value of the offset. Default is 0,0,0.
        remove: (edit) - removes the listed target(s) from the constraint.
        skip: (create, edit, multiuse) - Specify the axis to be skipped. Valid values are "x", "y", "z" and "none". The default value in create mode is "none". This flag is multi-use.
        targetList: (query) - Return the list of target objects.
        weight: (create, edit, query) - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
        weightAliasList: (query) - Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
    """
    ...


def pairBlend(*args, attribute: Optional[Union[str, bool]] = ..., input1: bool = ..., input2: bool = ..., node: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The pairBlend node allows a weighted combinations of 2 inputs to be blended together. It is created automatically when keying or constraining an attribute which is already connected.
    Alternatively, the pairBlend command can be used to connect a pairBlend node to connected attributes of a node. The previously existing connections are rewired to input1 of the pairBlend node. Additional connections can then be made manually to input2 of the pairBlend node.
    
    The pairBlend command can also be used to query the inputs to an existing pairBlend node.

    Args:
        attribute: (create, multiuse) - The name of the attribute(s) which the blend will drive. This flag is required when creating the blend.
        input1: (query) - Returns a string array of the node(s) connected to input 1.
        input2: (query) - Returns a string array of the node(s) connected to input 2.
        node: (create) - The name of the node which the blend will drive. This flag is required when creating the blend.
    """
    ...


def parentConstraint(*args, createCache: Tuple[float, float] = ..., decompRotationToChild: bool = ..., deleteCache: bool = ..., layer: Optional[Union[str, bool]] = ..., maintainOffset: bool = ..., name: Optional[Union[str, bool]] = ..., remove: bool = ..., skipRotate: Optional[Union[str, bool]] = ..., skipTranslate: Optional[Union[str, bool]] = ..., targetList: bool = ..., weight: Optional[Union[float, bool]] = ..., weightAliasList: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Constrain an object's position and rotation so that it behaves as if it
    were a child of the target object(s). In the case of multiple targets,
    the overall position and rotation of the constrained object is the
    weighted average of each target's contribution to the position and
    rotation of the object.
    
    A parentConstraint takes as input one or more "target" DAG transform
    nodes at which to position and rotate the single "constraint
    object" DAG transform node.  The parentConstraint positions and rotates
    the constrained object at the weighted average of the world
    space position, rotation and scale target objects.

    Args:
        createCache: (edit) - This flag is used to generate an animation curve that serves as a cache for the constraint. The two arguments define the start and end frames.  The cache is useful if the constraint has multiple targets and the constraint's interpolation type is set to "no flip". The "no flip" mode prevents flipping during playback, but the result is dependent on the previous frame. Therefore in order to consistently get the same result on a specific frame, a cache must be generated. This flag creates the cache and sets the constraint's interpolation type to "cache". If a cache exists already, it will be deleted and replaced with a new cache.
        decompRotationToChild: (create) - During constraint creation, if the rotation offset between the constrained object and the target object is maintained, this flag indicates close to which object the offset rotation is decomposed. Setting this flag will make the rotation decomposition close to the constrained object instead of the target object, which is the default setting.
        deleteCache: (edit) - Delete an existing interpolation cache.
        layer: (create, edit) - Specify the name of the animation layer where the constraint should be added.
        maintainOffset: (create) - If this flag is specified the position and rotation of the constrained object will be maintained.
        name: (create, edit, query) - Sets the name of the constraint node to the specified name.  Default name is constrainedObjectName_constraintType
        remove: (edit) - removes the listed target(s) from the constraint.
        skipRotate: (create, multiuse) - Causes the axis specified not to be considered when constraining rotation.  Valid arguments are "x", "y", "z" and "none".
        skipTranslate: (create, multiuse) - Causes the axis specified not to be considered when constraining translation.  Valid arguments are "x", "y", "z" and "none".
        targetList: (query) - Return the list of target objects.
        weight: (create, edit, query) - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
        weightAliasList: (query) - Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
    """
    ...


def pasteKey(*args, animLayer: Optional[Union[str, bool]] = ..., animation: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., clipboard: Optional[Union[str, bool]] = ..., connect: bool = ..., copies: Optional[Union[int, bool]] = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., floatOffset: Optional[Union[float, bool]] = ..., includeUpperBound: bool = ..., index: Optional[Union[int, bool]] = ..., matchByName: bool = ..., option: Optional[Union[str, bool]] = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., timeOffset: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., valueOffset: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The pasteKey command pastes curve segment hierarchies from the
    clipboard onto other objects or curves. If the object hierarchy
    from which the curve segments were copied or cut does not match
    the object hierarchy being pasted to, pasteKey will paste as much
    as it can match in the hierarchy.  If animation from only one object
    is on the clipboard, it will be pasted to each of the target objects.
    If animation from more than one object is on the clipboard, selection
    list order determines what animation is pasted to which object.
    
    Valid operations include:
    
     One attribute to one or more attributes (Clipboard
    animation is pasted onto all target attributes.
    
     One attribute to one or more objects (Clipboard animation
    pasted onto target object, when attribute names match.)
    
    Many attributes to one or more objects
    
    Clipboard animation pasted onto targets when attribute names
    match.
    
    
    
    TbaseKeySetCmd.h
    
    The way the keyset clipboard will be pasted to the specified object's
    attributes depends on the paste "-option" specified. Each of these
    options below will be explained using an example. For all the
    explanations, let us assume that there is a curve segment
    with 20 frames of animation on the keyset clipboard (you can put
    curve segments onto the clipboard using the cutKey or
    copyKey commands). We will call the animation curve that
    we are pasting to the target curve:
    
    
    pasteKey -time 5 -option insert
    1. Shift all keyframes on the target curve after time 5 to the right
    by 20 frames (to make room for the 20-frame clipboard segment).
    
    2. Paste the 20-frame clipboard segment starting at time 5.
    
    
    pasteKey -time "5:10" -option replace
    
    1. Remove all keys on the target curve from 5 to 10.
    
    2. Paste the 20-frame clipboard curve at time 5. Keys from frame 11-25 will be
    overridden if a key is present on the clipboard curve.
    
    
    pasteKey -option replaceCompletely
    
    1. Remove all keys on the target curve.
    
    2. Paste the 20-frame clipboard curve, preserving
    the clipboard curve's original keyframe times.
    
    
    pasteKey -time 5 -option merge
    
    1.The clipboard curve segment will be pasted starting at time 5
    for its full 20-frame range until frame 25.
    
    2. If a keyframe on the target curve has the same time
    as a keyframe on the clipboard curve, it is overwritten.
    Otherwise, any keys that existed in the 5:25 range
    before the paste, will remain untouched
    
    
    pasteKey -time "3:10" -option scaleInsert
    
    1. Shift all keyframes on the target curve after time 3 to the right
    by 7 frames (to clear the range 3:10 to paste in)
    
    2. The clipboard curve segment will be scaled to fit the specified
    time range (i.e. the 20 frames on the clipboard will be scaled to
    fit into 7 frames), and then pasted into the range 3:10.
    
    
    pasteKey -time "3:10" -option scaleReplace
    
    1. Any existing keyframes in the target curve in the range 3:10
    are removed.
    
    2. The clipboard curve segment will be scaled to fit the specified
    time range (i.e. the 20 frames on the clipboard will be scaled to
    fit into 7 frames), and then pasted into the range 3:10.
    
    
    pasteKey -time "3:10" -option scaleMerge
    
    1. The clipboard curve segment will be scaled to fit the specified
    time range (i.e. the 20 frames on the clipboard will be scaled to
    fit into 7 frames).
    
    2. If there are keys on the target curve at the same time
    as keys on the clipboard curve, they are overwritten.
    Otherwise, keyframes on the target curve that
    existed in the 3:10 range before the paste, will
    remain untouched.
    
    
    pasteKey -time "3:10" -option fitInsert
    
    1. Shift all the keyframes on the target curve after time 3 to the right
    by 7 frames (to clear the range 3:10 to paste in)
    
    2. The first 7 frames of the clipboard curve segment will be
    pasted into the range 3:10.
    
    
    pasteKey -time "3:10" -option fitReplace
    
    1. Any existing frames in the target curve in the range 3:10
    are removed.
    
    2. The first 7 frames of the clipboard curve segment will be
    pasted into the range 3:10.
    
    
    pasteKey -time "3:10" -option fitMerge
    
    1. The first 7 frames of the clipboard curve segment
    will be pasted into the range 3:10.
    
    2. If there are keys on the target curve at the same time
    as keys on the clipboard curve, they are overwritten.
    Otherwise, keyframes on the target curve that
    existed in the 3:10 range before the paste, will
    remain untouched.

    Args:
        animLayer: (create) - Specifies that the keys getting pasted should be pasted onto curves on the specified animation layer.If that layer doesn't exist for the specified objects or attributes then the keys won't get pasted.
        animation: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        clipboard: (create) - Specifies the clipboard from which animation is pasted. Valid clipboards are "api" and "anim".  The default clipboard is: anim
        connect: (create) - When true, connect the source curve with the destination curve's value at the paste time. (This has the effect of shifting the clipboard curve in value to connect with the destination curve.) False preserves the source curve's original keyframe values. Default is false.
        copies: (create) - The number of times to paste the source curve.
        float: (create) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        floatOffset: (create) - How much to offset the pasted keys in time (for non-time-input animation curves).
        includeUpperBound: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index: (create) - index of a key on an animCurve       In query mode, this flag needs a value.
        matchByName: (create) - When true, we will only paste onto items in the scene whose node and attribute names match up exactly with a corresponding item in the clipboard. No hierarchy information is used. Default is false, and in this case the usual matching by hierarchy occurs.
        option: (create) - Valid values are "insert", "replace", "replaceCompletely", "merge", "scaleInsert," "scaleReplace", "scaleMerge", "fitInsert", "fitReplace", and "fitMerge". The default paste option is: "insert".
        time: (create) - time uniquely representing a key (or key range) on a time-based animCurve.  See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
        timeOffset: (create) - How much to offset the pasted keys in time (for time-input animation curves).
        valueOffset: (create) - How much to offset the pasted keys in value.
    """
    ...


def pathAnimation(*args, bank: bool = ..., bankScale: Optional[Union[float, bool]] = ..., bankThreshold: Optional[Union[float, bool]] = ..., curve: Optional[Union[str, bool]] = ..., endTimeU: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., endU: Optional[Union[float, bool]] = ..., follow: bool = ..., followAxis: Optional[Union[str, bool]] = ..., fractionMode: bool = ..., inverseFront: bool = ..., inverseUp: bool = ..., name: Optional[Union[str, bool]] = ..., startTimeU: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., startU: Optional[Union[float, bool]] = ..., upAxis: Optional[Union[str, bool]] = ..., useNormal: bool = ..., worldUpObject: Optional[Union[str, bool]] = ..., worldUpType: Optional[Union[str, bool]] = ..., worldUpVector: Optional[Union[Tuple[float, float, float], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The pathAnimation command constructs the necessary graph nodes
    and their interconnections for a motion path animation. Motion path
    animation requires a curve and one or more other objects.
    During the animation, the objects will be moved along the 3D curve
    or the curveOnSurface.
    
    There are two ways to specify the moving objects:
    
     by explicitly specifying their names in the command line, or
     by making the objects selected (interactively, or through a
    MEL command).
    
    
    Likewise, there are two ways to specify a motion curve:
    
     by explicitly specifying the name of the motion curve
    in the command line (i.e. using the -c curve_name option), or
     by selecting the moving objects first before selecting the
    motion curve. I.e. if the name of the motion curve is not
    provided in the command line, the curve will be taken to be the
    last selected object in the selection list.
    
    
    When the end time is not specified: only one keyframe
    will be created either at the current time, or at the specified
    start time.

    Args:
        bank: (query) - If on, enable alignment of the up axis of the moving object(s) to the curvature of the path geometry. Default is false. When queried, this flag returns a boolean.
        bankScale: (query) - This flag specifies a factor to scale the amount of bank angle. Default is 1.0 When queried, this flag returns a float.
        bankThreshold: (query) - This flag specifies the limit of the bank angle. Default is 90 degrees When queried, this flag returns an angle.
        curve: (query) - This flag specifies the name of the curve for the path. Default is NONE When queried, this flag returns a string.
        endTimeU: (multiuse, query) - This flag specifies the ending time of the animation for the u parameter. Default is NONE. When queried, this flag returns a time.
        endU: (query) - This flag specifies the ending value of the u parameterization for the animation. Default is the end parameterization value of the curve. When queried, this flag returns a linear.
        follow: (query) - If on, enable alignment of the front axis of the moving object(s). Default is false. When queried, this flag returns a boolean.
        followAxis: (query) - This flag specifies which object local axis to be aligned to the tangent of the path curve. Default is y When queried, this flag returns a string.
        fractionMode: (query) - If on, evaluation on the path is based on the fraction of length of the path curve. Default is false. When queried, this flag returns a boolean.
        inverseFront: (query) - This flag specifies whether or not to align the front axis of the moving object(s) to the opposite direction of the tangent vector of the path geometry. Default is false. When queried, this flag returns a boolean.
        inverseUp: (query) - This flag specifies whether or not to align the up axis of the moving object(s) to the opposite direction of the normal vector of the path geometry. Default is false. When queried, this flag returns a boolean.
        name: (query) - This flag specifies the name for the new motion path node. (instead of the default name) When queried, this flag returns a string.
        startTimeU: (multiuse, query) - This flag specifies the starting time of the animation for the u parameter. Default is the the current time. When queried, this flag returns a time.
        startU: (query) - This flag specifies the starting value of the u parameterization for the animation. Default is the start parameterization value of the curve. When queried, this flag returns a linear.
        upAxis: (query) - This flag specifies which object local axis to be aligned a computed up direction. Default is z When queried, this flag returns a string.
        useNormal: (create, edit, query) - This flag is now obsolete. Use -wut/worldUpType instead.
        worldUpObject: (create, edit, query) - Set the DAG object to use for worldUpType "object" and "objectrotation". See -wut/worldUpType for greater detail. The default value is no up object, which is interpreted as world space.
        worldUpType: (create, edit, query) - Set the type of the world up vector computation. The worldUpType can have one of 5 values: "scene", "object", "objectrotation", "vector", or "normal". If the value is "scene", the upVector is aligned with the up axis of the scene and worldUpVector and worldUpObject are ignored. If the value is "object", the upVector is aimed as closely as possible to the origin of the space of the worldUpObject and the worldUpVector is ignored. If the value is "objectrotation" then the worldUpVector is interpreted as being in the coordinate space of the worldUpObject, transformed into world space and the upVector is aligned as closely as possible to the result. If the value is "vector", the upVector is aligned with worldUpVector as closely as possible and worldUpObject is ignored. Finally, if the value is "normal" the upVector is aligned to the path geometry. The default worldUpType is "vector".
        worldUpVector: (create, edit, query) - Set world up vector.  This is the vector in world coordinates that up vector should align with. See -wut/worldUpType for greater detail. If not given at creation time, the default value of (0.0, 1.0, 0.0) is used.
    """
    ...


def percent(*args, addPercent: bool = ..., dropoffAxis: Optional[Union[Tuple[float, float, float], bool]] = ..., dropoffCurve: Optional[Union[str, bool]] = ..., dropoffDistance: Optional[Union[float, bool]] = ..., dropoffPosition: Optional[Union[Tuple[float, float, float], bool]] = ..., dropoffType: Optional[Union[str, bool]] = ..., multiplyPercent: bool = ..., value: Optional[Union[float, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command sets percent values on members of a weighted node such as
    a cluster or a jointCluster. With no flags specified the command sets
    the percent value for selected components of the specified node to the
    specified percent value. A dropoff from the specified percent value to
    0 can be specified from a point, plane or curve using a dropoff
    distance around that shape. The percent value can also be added or
    multiplied with existing percent values of the node components.

    Args:
        addPercent: (create) - Add the percent value specified with the -v flag to the existing percent values
        dropoffAxis: (create) - Specifies the axis along which to dropoff the percent value, starting from the dropoffPosition.
        dropoffCurve: (create) - Specifies the curve around which to dropoff the percent value.
        dropoffDistance: (create) - Specifies the dropoff distance from the point, plane or curve that was specified using the -dp -dax or -dc flags.
        dropoffPosition: (create) - Specifies the point around which to dropoff the percent value.
        dropoffType: (create) - Specifies the type of dropoff. Used in conjunction with the -dp, -dax or -dc flags. Default is linear. Valid values are: linear, sine, exponential, linearSquared, none.
        multiplyPercent: (create) - Multiply the percent value specified with the -v flag with existing percent values
        value: (create, query) - The percent value to be applied. The default is 1. In query mode, returns an array of doubles corresponding to the weights of the selected object components.
    """
    ...


def play(*args, forward: bool = ..., playSound: bool = ..., record: bool = ..., sound: Optional[Union[str, bool]] = ..., state: bool = ..., wait: bool = ..., query: bool = ...) -> Any:
    r"""
    This command starts and stops playback.
    In order to change the frame range of playback,
    see the playbackOptions command.

    Args:
        forward: (create, query) - When true, play back the animation from the currentTime to the maximum of the playback range. When false, play back from the currentTime to the minimum of the playback range.  When queried, returns an int.
        playSound: (create, query) - Specify whether or not sound should be used during playback
        record: (create, query) - enable the recording system and start one playback loop
        sound: (create, query) - Specify the sound node to be used during playback
        state: (create, query) - start or stop playing back
        wait: (create) - Wait till completion before returning control to command Window.
    """
    ...


def playbackOptions(*args, animationEndTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., animationStartTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., blockingAnim: bool = ..., by: Optional[Union[float, bool]] = ..., framesPerSecond: bool = ..., loop: Optional[Union[str, bool]] = ..., maxPlaybackSpeed: Optional[Union[float, bool]] = ..., maxTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., minTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., playbackSpeed: Optional[Union[float, bool]] = ..., selectionEndTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., selectionStartTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., selectionVisible: bool = ..., stepLoop: bool = ..., view: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command sets/queries certain values associated
    with playback: looping style, start/end times, etc.
    Only commands modifying the -minTime/maxTime,
    the -animationStartTime/animationEndTime,
    the -selectionStartTime/selectionEndTime/selectionVisible
    or the -by value are undoable.

    Args:
        animationEndTime: (create, edit, query) - Sets the end time of the animation.  Query returns a float.
        animationStartTime: (create, edit, query) - Sets the start time of the animation.  Query returns a float.
        blockingAnim: (create, query) - All tangents playback as stepped so that animation can be viewed in pure pose-to-pose form
        by: (create, edit, query) - Increment between times viewed during playback. (Default 1.0)
        framesPerSecond: (create, query) - Queries the actual playback rate.  Query returns a float.
        loop: (create, edit, query) - Controls if and how playback repeats.  Valid values are "once," "continuous," and "oscillate."  Query returns string.
        maxPlaybackSpeed: (create, edit, query) - Sets the desired maximum playback speed.  Query returns a float. The maxPlaybackSpeed is only used by Maya when your playbackSpeed is 0 (play every frame). The maxPlaybackSpeed will clamp the maximum playback rate to prevent it from going more than a certain amount. A maxPlaybackSpeed of 0 will give free (unclamped) playback.
        maxTime: (create, edit, query) - Sets the end of the playback time range.  Query returns a float.
        minTime: (create, edit, query) - Sets the start of the playback time range.  Query returns a float.
        playbackSpeed: (create, edit, query) - Sets the desired playback speed.  Query returns a float.
        selectionEndTime: (create, edit, query) - Sets the end time of the selection.  Query returns a float.
        selectionStartTime: (create, edit, query) - Sets the start time of the selection.  Query returns a float.
        selectionVisible: (create, edit, query) - Sets the selection visibility. Query returns current visibility.
        stepLoop: (create, query) - Turns on/off looping back to the start or end of the play range for step forward/backward one frame and step forward/backward one key.
        view: (create, edit, query) - Controls how many modelling views update during playback. Valid values are "all" and "active".  Query returns a string.
    """
    ...


def playblast(*args, activeEditor: bool = ..., cameraSetup: Optional[Union[Tuple[str, str], bool]] = ..., clearCache: bool = ..., codecOptions: bool = ..., combineSound: bool = ..., completeFilename: Optional[Union[str, bool]] = ..., compression: Optional[Union[str, bool]] = ..., editorPanelName: Optional[Union[str, bool]] = ..., endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., filename: Optional[Union[str, bool]] = ..., forceOverwrite: bool = ..., format: Optional[Union[str, bool]] = ..., frame: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., framePadding: Optional[Union[int, bool]] = ..., height: Optional[Union[int, bool]] = ..., indexFromZero: bool = ..., offScreen: bool = ..., offScreenViewportUpdate: bool = ..., options: bool = ..., percent: Optional[Union[int, bool]] = ..., quality: Optional[Union[int, bool]] = ..., rawFrameNumbers: bool = ..., replaceAudioOnly: bool = ..., replaceEndTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., replaceFilename: Optional[Union[str, bool]] = ..., replaceStartTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., sequenceTime: bool = ..., showOrnaments: bool = ..., sound: Optional[Union[str, bool]] = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., throwOnError: bool = ..., useTraxSounds: bool = ..., viewer: bool = ..., width: Optional[Union[int, bool]] = ..., widthHeight: Optional[Union[Tuple[int, int], bool]] = ...) -> Any:
    r"""
    This command playblasts the current playback range.
    Sound is optional.
    
    Note that the playblast command registers a condition called "playblasting"
    so that users can monitor whether playblasting is occurring. You may monitor the
    condition using the API (MConditionMessage) or a script (scriptJob and condition
    commands).

    Args:
        activeEditor: (create) - This flag will return the current model editor that would be used for playblast. It does not invoke playblast itself.
        cameraSetup: (create, multiuse) - Information about camera setup. The first string defines a camera setup MEL procedure. The camera setup procedure will be invoked before executing a playblast. The second string argument which is used as a camera identifier and is appended to the root file name to specify the final output file name(s). The command will fail there is not a pair of strings supplied to the argument.
        clearCache: (create) - When true, all previous temporary playblast files will be deleted before the new playblast files are created and the remaining temporary playblast files will be deleted when the application quits. Any playblast files that were explicitly given a name by the user will not be deleted.
        codecOptions: (create) - Brings up the OS specific dialog for setting playblast codec options, and does not run the playblast.
        combineSound: (create) - Combine the trax sounds into a single track. This might force a resampling of the sound if the sound paramters don't match up.
        completeFilename: (create) - When set, this string specifies the exact name of the output image. In contrast with the -f/filename flag, -cf/completeFilename does not append any frame number or extension string at the end of the filename. Additionally, playblast will not delete the image from disk after it is displayed. This flag should not be used in conjunction with -f/filename.
        compression: (create) - Specify the compression to use for the movie file.  To determine which settings are available on your system, use the `playblast -options` command. This will display a system-specific dialog with supported compression formats. When the 'format' flag is 'image', this flag is used to pass in the desired image format. If the format is 'image' and the compression flag is ommitted, the output format specified via the Render Globals preference (see -format) will be used. If compression is set to 'none', the iff image format will be used.
        editorPanelName: (create) - This optional flag specifies the name of the model editor or panel, which is to be used for playblast. The current model editor or panel won't be used for playblast unless its name is specified. Flag usage is specific to invoking playblast.
        endTime: (create) - Specify the end time of the playblast.  Default is the end time of the playback range displayed in the Time Slider. Overridden by -frame.
        filename: (create) - The filename to use for the output of this playblast. If the file already exists, a confirmation box will be displayed if playblast is performed interactively.  If playblast is executed from the command line and the file already exists, it will abort.
        forceOverwrite: (create) - Overwrite existing playblast files which may have the the same name as the one specified with the "-f" flag
        format: (create) - The format for the playblast output.    ValueDescription   "movie" This option selects a platform-specific default movie format. On Linux and Mac OSX the default movie format is Quicktime. On Windows the default movie format is Audio Video Interleave.    "avi" Set the format to Audio Video Interleave (Windows only)   "qt" Set the format to QuickTime (all platforms).   "avfoundation" Write movie by AVFoundation (Mac only).   "image" Outputs a sequence of image files. The image format will be the Output Format specified using Window > RenderEditors > RenderSettings > CommonTab. The resulting files use the value of the "-f" flag as a prefix, with an appended frame number, as in "myFile.0007.iff"   "iff" Same as "image"    The default value of the -fmt/format flag is "movie". Depending on the selected format, a platform-specific default application will be used to view results. For image sequences, the default application is "fcheck". For movies, the default application is Windows Media Player (on Windows), Quicktime Player (on Mac OSX), and Lqtplay (on Linux). Users can specify different applications via Maya's application preferences.
        frame: (create, multiuse) - List of frames to blast. One frame specified per flag. The frames can be specified in any order but will be output in an ordered sequence. When specified this flag will override any start/end range
        framePadding: (create) - Number of zeros used to pad file name. Typically set to 4 to support fcheck.
        height: (create) - Height of the final image. This value will be clamped if larger than the width of the active window. Windows: If not using fcheck, the width and height must each be divisible by 4.
        indexFromZero: (create) - Output frames starting with file.0000.ext and incrementing by one. Typically frames use the Maya time as their frame number. This option can only be used for frame based output formats.
        offScreen: (create) - When set, this toggle allow playblast to use an offscreen buffer to render the view. This allows playblast to work when the application is iconified, or obscured.
        offScreenViewportUpdate: (create) - When set, this toggle allows playblast to update the viewport while rendering with the offscreen buffer.
        options: (create) - Brings up a dialog for setting playblast options, and does not run the playblast.
        percent: (create) - Percentage of current view size  to use during blasting. Accepted values are integers between 10 and 100.  All other values are clamped to be within this range.  A value of 25 means 1/4 of the  current view size; a  value of 50  means half the current view size; a value of 100 means full size.  (Default is 50.)
        quality: (create) - Specify the compression quality factor to use for the movie file. Value should be in the 0-100 range
        rawFrameNumbers: (create) - Playblast typically numbers its frames sequentially, starting at zero. This flag will override the default action and frames will be numbered using the actual frames specified by the -frame or -startFrame/-endFrame flags.
        replaceAudioOnly: (create) - When set, this string dictates that only the audio will be replaced when the scene is re-playblasted.
        replaceEndTime: (create) - Specify the end time of a replayblast of an existing playblast.  Default is the start time of the playback range displayed in the Time Slider. Overridden by -frame.
        replaceFilename: (create) - When set, this string specifies the name of an input playblast file which will have frames replaced according to the replace start and end times.
        replaceStartTime: (create) - Specify the start time of a replayblast of an existing playblast.  Default is the start time of the playback range displayed in the Time Slider. Overridden by -frame.
        sequenceTime: (create) - Use sequence time
        showOrnaments: (create) - Sets whether or not model view ornaments (e.g. the axis icon) should be displayed
        sound: (create) - Specify the sound node to be used during playblast
        startTime: (create) - Specify the start time of the playblast.  Default is the start time of the playback range displayed in the Time Slider. Overridden by -frame.
        throwOnError: (create) - Playblast is tolerant of failures in most situations. When set, this toggle allows playblast to throw an error on these failures.
        useTraxSounds: (create) - Use sounds from TRAX.
        viewer: (create) - Specify whether a viewer should be launched for the playblast.  Default is "true".  Runs "fcheck" when -fmt is "image". The player for movie files depends on the OS: Windows uses Microsoft Media Player, Irix uses movieplayer, OSX uses QuickTime.
        width: (create) - Width of the final image. This value will be clamped if larger than the width of the active window. Windows: If not using fcheck, the width and height must each be divisible by 4.
        widthHeight: (create) - Final image's width and height. Values larger than the dimensions of the active window are clamped. A width and height of 0 means to use the window's current size. Windows: If not using fcheck, the width and height must each be divisible by 4.
    """
    ...


def pointConstraint(*args, layer: Optional[Union[str, bool]] = ..., maintainOffset: bool = ..., name: Optional[Union[str, bool]] = ..., offset: Optional[Union[Tuple[float, float, float], bool]] = ..., remove: bool = ..., skip: Optional[Union[str, bool]] = ..., targetList: bool = ..., weight: Optional[Union[float, bool]] = ..., weightAliasList: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Constrain an object's position to the position of the target object or
    to the average position of a number of targets.
    
    A pointConstraint takes as input one or more "target" DAG transform
    nodes at which to position the single "constraint object" DAG
    transform node.  The pointConstraint positions the constrained object
    at the weighted average of the world space position target
    objects.

    Args:
        layer: (create, edit) - Specify the name of the animation layer where the constraint should be added.
        maintainOffset: (create) - The offset necessary to preserve the constrained object's initial position will be calculated and used as the offset.
        name: (create, edit, query) - Sets the name of the constraint node to the specified name.  Default name is constrainedObjectName_constraintType
        offset: (create, edit, query) - Sets or queries the value of the offset. Default is 0,0,0.
        remove: (edit) - removes the listed target(s) from the constraint.
        skip: (create, edit, multiuse) - Specify the axis to be skipped. Valid values are "x", "y", "z" and "none". During creation, "none" is the default. This flag is multi-use.
        targetList: (query) - Return the list of target objects.
        weight: (create, edit, query) - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
        weightAliasList: (query) - Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
    """
    ...


def pointOnPolyConstraint(*args, layer: Optional[Union[str, bool]] = ..., maintainOffset: bool = ..., name: Optional[Union[str, bool]] = ..., offset: Optional[Union[Tuple[float, float, float], bool]] = ..., remove: bool = ..., skip: Optional[Union[str, bool]] = ..., targetList: bool = ..., weight: Optional[Union[float, bool]] = ..., weightAliasList: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Constrain an object's position to the position of the target object or
    to the average position of a number of targets.
    
    A pointOnPolyConstraint takes as input one or more "target" DAG transform
    nodes at which to position the single "constraint object" DAG
    transform node.  The pointOnPolyConstraint positions the constrained object
    at the weighted average of the world space position target
    objects.

    Args:
        layer: (create, edit) - Specify the name of the animation layer where the constraint should be added.
        maintainOffset: (create) - The offset necessary to preserve the constrained object's initial position will be calculated and used as the offset.
        name: (create, edit, query) - Sets the name of the constraint node to the specified name.  Default name is constrainedObjectName_constraintType
        offset: (create, edit, query) - Sets or queries the value of the offset. Default is 0,0,0.
        remove: (edit) - removes the listed target(s) from the constraint.
        skip: (create, edit, multiuse) - Specify the axis to be skipped. Valid values are "x", "y", "z" and "none". During creation, "none" is the default. This flag is multi-use.
        targetList: (query) - Return the list of target objects.
        weight: (create, edit, query) - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
        weightAliasList: (query) - Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
    """
    ...


def poleVectorConstraint(*args, layer: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., remove: bool = ..., targetList: bool = ..., weight: Optional[Union[float, bool]] = ..., weightAliasList: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Constrains the poleVector of an ikRPsolve handle to point at a
    target object or at the average position of a number of targets.
    
    An poleVectorConstraint takes as input one or more "target" DAG
    transform nodes at which to aim pole vector for an IK handle using
    the rotate plane solver.  The pole vector is adjust such that
    the in weighted average of the world space position target
    objects lies is the "rotate plane" of the handle.

    Args:
        layer: (create, edit) - Specify the name of the animation layer where the constraint should be added.
        name: (create, edit, query) - Sets the name of the constraint node to the specified name.  Default name is constrainedObjectName_constraintType
        remove: (edit) - removes the listed target(s) from the constraint.
        targetList: (query) - Return the list of target objects.
        weight: (create, edit, query) - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
        weightAliasList: (query) - Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
    """
    ...


def polyUniteSkinned(*args, centerPivot: bool = ..., constructionHistory: bool = ..., mergeUVSets: Optional[Union[int, bool]] = ..., objectPivot: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to combine poly mesh objects (as polyUnite)
    while retaining the smooth skinning setup on the
    combined object.

    Args:
        centerPivot: (create, edit, query) - Set the resulting object's pivot to the center of the selected objects bounding box.
        constructionHistory: (create, edit, query) - Turn the construction history on or off.
        mergeUVSets: (create, edit, query) - Specify how UV sets will be merged on the output mesh. The choices are 0 | 1 | 2. 0 = Do not merge. Each UV set on each mesh will become a new UV set in the output. 1 = Merge by name. UV sets with the same name will be merged. 2 = Merge by UV links. UV sets will be merged so that UV linking on the input meshes continues to work. The default is 1 (merge by name).
        objectPivot: (create, edit, query) - Set the resulting object's pivot to last selected object's pivot.
    """
    ...


def pose(*args, allPoses: bool = ..., apply: bool = ..., name: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to create character poses.

    Args:
        allPoses: (query) - This flag is used to query all the poses in the scene.
        apply: (create) - This flag is used in conjunction with the name flag to specify a pose should be applied to the character.
        name: (create, query) - In create mode, specify the pose name. In query mode, return a list of all the poses for the character. In apply mode, specify the pose to be applied.
    """
    ...


def poseEditor(*args, control: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., exists: bool = ..., filter: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., highlightConnection: Optional[Union[str, bool]] = ..., lockMainConnection: bool = ..., mainListConnection: Optional[Union[str, bool]] = ..., panel: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., selectionConnection: Optional[Union[str, bool]] = ..., stateString: bool = ..., unParent: bool = ..., unlockMainConnection: bool = ..., updateMainConnection: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates an editor that derives from the base editor
    class that has controls for deformer and control nodes.

    Args:
        control: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag: (create, edit, query) - Attaches a tag to the editor.
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        filter: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        forceMainConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        highlightConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        lockMainConnection: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        mainListConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        panel: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        selectionConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        stateString: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        unParent: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
    """
    ...


def posePanel(*args, control: bool = ..., copy: str = ..., createString: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., editString: bool = ..., exists: bool = ..., init: bool = ..., isUnique: bool = ..., label: Optional[Union[str, bool]] = ..., menuBarRepeatLast: bool = ..., menuBarVisible: bool = ..., needsInit: bool = ..., parent: Optional[Union[str, bool]] = ..., popupMenuProcedure: Optional[Union[str, bool]] = ..., poseEditor: bool = ..., replacePanel: str = ..., tearOff: bool = ..., tearOffCopy: Optional[Union[str, bool]] = ..., tearOffRestore: bool = ..., unParent: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a panel that derives from the base panel
    class that houses a poseEditor.

    Args:
        control: (query) - Returns the top level control for this panel. Usually used for getting a parent to attach popup menus. CAUTION: panels may not have controls at times.  This flag can return "" if no control is present.
        copy: (edit) - Makes this panel a copy of the specified panel.  Both panels must be of the same type.
        createString: (edit) - Command string used to create a panel
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag: (create, edit, query) - Attaches a tag to the Maya panel.
        editString: (edit) - Command string used to edit a panel
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        init: (create, edit) - Initializes the panel's default state.  This is usually done automatically on file -new and file -open.
        isUnique: (query) - Returns true if only one instance of this panel type is allowed.
        label: (edit, query) - Specifies the user readable label for the panel.
        menuBarRepeatLast: (create, edit, query) - Controls whether clicking on the menu header with the middle mouse button would repeat the last selected menu item.
        menuBarVisible: (create, edit, query) - Controls whether the menu bar for the panel is displayed.
        needsInit: (edit, query) - (Internal) On Edit will mark the panel as requiring initialization. Query will return whether the panel is marked for initialization.  Used during file -new and file -open.
        parent: (create) - Specifies the parent layout for this panel.
        popupMenuProcedure: (edit, query) - Specifies the procedure called for building the panel's popup menu(s). The default value is "buildPanelPopupMenu".  The procedure should take one string argument which is the panel's name.
        poseEditor: (query) - Query only flag that returns the name of an editor to be associated with the panel.
        replacePanel: (edit) - Will replace the specified panel with this panel.  If the target panel is within the same layout it will perform a swap.
        tearOff: (edit, query) - Will tear off this panel into a separate window with a paneLayout as the parent of the panel. When queried this flag will return if the panel has been torn off into its own window.
        tearOffCopy: (create) - Will create this panel as a torn of copy of the specified source panel.
        tearOffRestore: (create, edit) - Restores panel if it is torn off and focus is given to it. If docked, becomes the active panel in the docked window. This should be the default flag that is added to all panels instead of -to/-tearOff flag which should only be used to tear off the panel.
        unParent: (edit) - Specifies that the panel should be removed from its layout. This (obviously) cannot be used with query.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
    """
    ...


def proximityWrap(*args, addDrivers: str = ..., applyUserDefaults: bool = ..., canBeAdded: Optional[Union[str, bool]] = ..., driverIndices: bool = ..., dumpInfo: bool = ..., freeDriverIndex: bool = ..., removeDrivers: str = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a proximityWrap deformer, which deforms geometry based on the
    distance from its drivers.

    Args:
        addDrivers: (edit, multiuse) - Add connect new drivers to the proximityWrap node
        applyUserDefaults: (edit) - Flag used in with the addDriver flag. When set, new drivers will set the user default attributes from the option var settings. When the flag is not set, the user default attributes will not be set. Default is on.
        canBeAdded: (multiuse, query) - Returns true if all listed shapes can be added as drivers. The reason for an item returning false would be that it is already connected as a driver, it is connected as the deformed geometry or it represents in invalid object.
        driverIndices: (query) - List connected driver indices
        dumpInfo: (query) - Return a python dictionary containing information relating to the proximityWrap node. Some information is returned in string form in mel but the flag is meant to be used in python.
        freeDriverIndex: (query) - Returns the first index which has no driver connected
        removeDrivers: (edit, multiuse) - Remove connected drivers
    """
    ...


def readTake(*args, angle: Optional[Union[str, bool]] = ..., device: Optional[Union[str, bool]] = ..., frequency: Optional[Union[float, bool]] = ..., linear: Optional[Union[str, bool]] = ..., noTime: bool = ..., take: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This action reads a take (.mov) file to a defined device. 
    
    See also: writeTake, applyTake

    Args:
        angle: (create) - Sets the angular unit used in the take. Valid strings are "deg", "degree", "rad", and "radian".  C: The default is the current user angular unit.
        device: (create) - Specifies the device into which the take data is read. This is a required argument.
        frequency: (create) - The timestamp is ignored and the specified frequency is used. If timeStamp data is not in the .mov file, the -noTimestamp flag should also be used. This flag resample, instead the data is assumed to be at the specified frequency.  C: If the take file does not use time stamps, the default frequency is 60Hz.
        linear: (create) - Sets the linear unit used in the take. Valid strings are "mm", "millimeter", "cm", "centimeter", "m", "meter", "km", "kilometer", "in", "inch", "ft", "foot", "yd", "yard", "mi", and "mile".  C: The default is the current user linear unit.
        noTime: (create) - Specifies if the take (.mov) file contains time stamps.  C: The default is to assume time stamps are part of the take file.
        take: (create) - Reads the specified take file. It is safest to pass the full path to the flag.
    """
    ...


def recordDevice(*args, cleanup: bool = ..., data: bool = ..., device: Optional[Union[str, bool]] = ..., duration: Optional[Union[int, bool]] = ..., playback: bool = ..., state: bool = ..., wait: bool = ..., query: bool = ...) -> Any:
    r"""
    Starts and stops server side device recording. The data is recorded
    at the device rate. Once recorded, the data may be brought into Maya
    with the applyTake command. 
    
    See also: enableDevice, applyTake, readTake, writeTake

    Args:
        cleanup: (create) - Removes the recorded data from the device.
        data: (query) - Specifies if the device has recorded data. If the device is recording at the time of query, the flag will return false.  Q: When queried, this flag returns an int.
        device: (create, multiuse) - Specifies which device(s) to start record recording. The listed device(s) will start recording regardless of their record enable state.  C: The default is to start recording all devices that are record enabled.
        duration: (create, query) - Duration (in seconds) of the recording. When the duration expires, the device will still be in a recording state and must be told to stop recording.  C: The default is 60.  Q: When queried, this flag returns an int.
        playback: (create, query) - If any attribute is connected to an animation curve, the animation curve will play back while recording the device(s) including any animation curves attached to attributes being recorded.  C: The default is false.  Q: When queried, this flag returns an int.
        state: (create, query) - Start or stop device recording.  C: The default is true.  Q: When queried, this flag returns an int.
        wait: (create) - If -p/playback specified, wait until playback completion before returning control to the user. This flag is ignored if -p is not used.
    """
    ...


def removeJoint(*args) -> Any:
    r"""
    This command will remove the selected joint or the joint given at the
    command line from the skeleton.
    
    The given (or selected) joint should not be the root joint of the skeleton,
    and not have skin attached. The command works on the given (or selected)
    joint. No options or flags are necessary.

    Args:
    """
    ...


def reorderDeformers(*args, name: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This command changes the order in which 2 deformation nodes affect the
    output geometry. The first string argument is the name of deformer1,
    the second is deformer2, followed by the list of objects they
    deform.
    
    It inserts deformer2 before deformer1. Currently supported deformer
    nodes include: sculpt, cluster, jointCluster, lattice, wire,
    jointLattice, boneLattice, blendShape.

    Args:
        name: (create) - This flag is obsolete and is not used.
    """
    ...


def reroot(*args) -> Any:
    r"""
    This command will reroot a skeleton. The selected joint or the given joint
    at the command line will be the new    root of the skeleton. All ikHandles
    passing through the selected joint or above it will be deleted.
    
    The given(or selected) joint should not have skin attached. The    command
    works on the given or selected joint. No options or flags are necessary.

    Args:
    """
    ...


def rotationInterpolation(*args, convert: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    The rotationInterpolation command converts the rotation curves to the
            desired rotation interpolation representation. For example, an
            Euler-angled representation can be converted to Quaternion.

    Args:
        convert: (create, query) - Specifies the rotation interpolation mode for the curves after converting. Possible choices are "none" (unsynchronized Euler-angled curves which are compatible with pre-4.0 Maya curves), "euler" (Euler-angled curves with keyframes kept synchronized), "quaternion" (quaternion curves with keyframes kept synchronized, but the exact interpolation depends on individual tangents),  "quaternionSlerp" (applies quaternion slerp interpolation to the curve, ignoring tangent settings), "quaternionSquad" (applied cubic interpolation to the curve in quaternion space, ignoring tangent settings)
    """
    ...


def scaleConstraint(*args, layer: Optional[Union[str, bool]] = ..., maintainOffset: bool = ..., name: Optional[Union[str, bool]] = ..., offset: Optional[Union[Tuple[float, float, float], bool]] = ..., remove: bool = ..., scaleCompensate: bool = ..., skip: Optional[Union[str, bool]] = ..., targetList: bool = ..., weight: Optional[Union[float, bool]] = ..., weightAliasList: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Constrain an object's scale to the scale of the target object or
    to the average scale of a number of targets.
    
    A scaleConstraint takes as input one or more "target" DAG
    transform nodes to which to scale the single "constraint
    object" DAG transform node.  The scaleConstraint scales the
    constrained object at the weighted geometric mean of the
    world space target scale factors.

    Args:
        layer: (create, edit) - Specify the name of the animation layer where the constraint should be added.
        maintainOffset: (create) - The offset necessary to preserve the constrained object's initial scale will be calculated and used as the offset.
        name: (create, edit, query) - Sets the name of the constraint node to the specified name.  Default name is constrainedObjectName_constraintType
        offset: (create, edit, query) - Sets or queries the value of the offset. Default is 1,1,1.
        remove: (edit) - removes the listed target(s) from the constraint.
        scaleCompensate: (create, edit) - Used only when constraining a joint. It specify if a scaleCompensate will be applied on constrained joint. If true it will connect Tjoint.aCompensateForParentScale to scaleContraint.aConstraintScaleCompensate.
        skip: (create, edit, multiuse) - Specify the axis to be skipped. Valid values are "x", "y", "z" and "none". During creation, "none" is the default. This flag is multi-use.
        targetList: (query) - Return the list of target objects.
        weight: (create, edit, query) - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
        weightAliasList: (query) - Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
    """
    ...


def scaleKey(*args, animation: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., autoSnap: bool = ..., controlPoints: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., floatPivot: Optional[Union[float, bool]] = ..., floatScale: Optional[Union[float, bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., includeUpperBound: bool = ..., index: Optional[Union[int, bool]] = ..., newEndFloat: Optional[Union[float, bool]] = ..., newEndTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., newStartFloat: Optional[Union[float, bool]] = ..., newStartTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., scaleSpecifiedKeys: bool = ..., shape: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., timePivot: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., timeScale: Optional[Union[float, bool]] = ..., valuePivot: Optional[Union[float, bool]] = ..., valueScale: Optional[Union[float, bool]] = ...) -> Any:
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
    
    This command takes keyframes at (or within) the specified times (or time ranges)
    and scales them.  If no times are specified, the scale is applied to active keyframes
    or (if no keys are active) all keys of active objects.
    
    This command has two sets of flags for scaling in time/x-axis. One set of flags is
    for time-based animation curves, and the other set of flags is for float-based (unitless) animation curves.
    Most animation curves in Maya are time-based. Unitless animation curves are less common.
    Use the set of flags that corresponds to the type of animation curves being scaled.
    
    To scale all selected animation curves regardless of their type, use both sets of flags.

    Args:
        animation: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        autoSnap: (create) - Auto snap scaled keys if True. Default value depend on scaleKeyAutoSnap option
        controlPoints: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        float: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        floatPivot: (create) - Scale pivot along the x-axis for float-based (unitless) animCurves
        floatScale: (create) - Amount to scale along the x-axis for float-based (unitless) animation curves animCurves
        hierarchy: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        includeUpperBound: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        newEndFloat: (create) - The end of the float range to which the float-based (unitless) animation curves should be scaled.
        newEndTime: (create) - The end of the time range to which the time-based animation curves should be scaled.
        newStartFloat: (create) - The start of the float range to which the float-based (unitless) animation curves should be scaled.
        newStartTime: (create) - The start of the time range to which the time-based animation curves should be scaled.
        scaleSpecifiedKeys: (create) - Determines if only the specified keys are affected by the scale. If false, other keys may be adjusted with the scale. The default is true.
        shape: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        time: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
        timePivot: (create) - Scale pivot along the time-axis for time-based animation curves
        timeScale: (create) - Amount to scale along the time-axis for time-based animation curves
        valuePivot: (create) - Scale pivot along the value-axis
        valueScale: (create) - Amount of scale along the value-axis
    """
    ...


def sculpt(*args, after: bool = ..., afterReference: bool = ..., before: bool = ..., components: bool = ..., deformerTools: bool = ..., dropoffDistance: Optional[Union[float, bool]] = ..., dropoffType: Optional[Union[str, bool]] = ..., exclusive: Optional[Union[str, bool]] = ..., frontOfChain: bool = ..., geometry: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., groupWithLocator: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., insideMode: Optional[Union[str, bool]] = ..., maxDisplacement: Optional[Union[float, bool]] = ..., mode: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., objectCentered: bool = ..., parallel: bool = ..., prune: bool = ..., remove: bool = ..., sculptTool: Optional[Union[str, bool]] = ..., selectedComponents: bool = ..., split: bool = ..., useComponentTags: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates/edits/queries a sculpt object deformer. By default
    for creation mode an implicit sphere will be used as the sculpting
    object if no sculpt tool is specified. The name of the created/edited
    object is returned.

    Args:
        after: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        components: (query) - Returns the components used by the deformer
        deformerTools: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        dropoffDistance: (create, edit, query) - Specifies the distance from the surface of the sculpt object at which the sculpt object produces no deformation effect. Default is 1.0. When queried, this flag returns a float.
        dropoffType: (create, edit, query) - Specifies how the deformation effect drops off from maximum effect at the surface of the sculpt object to no effect at dropoff distance limit. Valid values are: linear | none. Default is linear. When queried, this flag returns a string.
        exclusive: (create, query) - Puts the deformation set in a deform partition.
        frontOfChain: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        groupWithLocator: (create) - Groups the sculptor and its locator together under a single transform. Default is off.
        ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        insideMode: (create, edit, query) - Specifies how the deformation algorithm deals with points that are inside the sculpting primitve. The choices are: ring | even. The default is even. When queried, this flag returns a string. Ring mode will tend to produce a contour like ring of points around the sculpt object as it passes through an object while even mode will try to spread the points out as evenly as possible across the surface of the sculpt object.
        maxDisplacement: (create, edit, query) - Defines the maximum amount the sculpt object may move a point on an object which it is deforming. Default is 1.0. When queried, this flag returns a float.
        mode: (create, edit, query) - Specifies which deformation algorithm the sculpt object should use. The choices are: flip | project | stretch. The default is stretch. When queried, this flag returns a string.
        name: (create) - Used to specify the name of the node being created.
        objectCentered: (create) - Places the sculpt and locator in the center of the bounding box of the selected object(s) or components. Default is off which centers the sculptor and locator at the origin.
        parallel: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        prune: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        remove: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        sculptTool: (create) - Use the specified NURBS object as the sculpt tool instead of the default implicit sphere.
        selectedComponents: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        split: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        useComponentTags: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
    """
    ...


def sculptTarget(*args, after: bool = ..., afterReference: bool = ..., before: bool = ..., components: bool = ..., deformerTools: bool = ..., exclusive: Optional[Union[str, bool]] = ..., frontOfChain: bool = ..., geometry: str = ..., geometryIndices: bool = ..., ignoreSelected: bool = ..., inbetweenWeight: float = ..., includeHiddenSelections: bool = ..., name: Optional[Union[str, bool]] = ..., parallel: bool = ..., prune: bool = ..., regenerate: bool = ..., remove: bool = ..., selectedComponents: bool = ..., snapshot: int = ..., split: bool = ..., target: int = ..., useComponentTags: bool = ..., edit: bool = ...) -> Any:
    r"""
    This command is used to specify the blend shape target to be
    modified by the sculpting tools and transform manipulators.

    Args:
        after: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        components: () - Returns the components used by the deformer
        deformerTools: () - Returns the name of the deformer tool objects (if any) as string string ...
        exclusive: (create) - Puts the deformation set in a deform partition.
        frontOfChain: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry: (edit, multiuse) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices: () - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        inbetweenWeight: (edit) - Specifies the in between target weight of the blend shape node that will be made editable by the sculpting and transform tools.
        includeHiddenSelections: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        name: (create) - Used to specify the name of the node being created.
        parallel: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        prune: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        regenerate: (edit) - When this flag is specified a new shape is created for the specified blend shape target, if the shape does not already exist. The name of the new shape is returned.
        remove: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        selectedComponents: () - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        snapshot: (edit) - This flag should only be used internally to add in-between target. When this flag is specified a snapshot of the shape will be taken for the specified in-between target when it does not exist yet. This flag specifies the base shape index and must be used with the -target and -inbetweenWeight flags, which specify the in-between target.
        split: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        target: (edit) - Specifies the target index of the blend shape node that will be made editable by the sculpting and transform tools.
        useComponentTags: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
    """
    ...


def sequenceManager(*args, addSequencerAudio: Optional[Union[str, bool]] = ..., attachSequencerAudio: Optional[Union[str, bool]] = ..., currentShot: Optional[Union[str, bool]] = ..., currentTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., listSequencerAudio: Optional[Union[str, bool]] = ..., listShots: bool = ..., modelPanel: Optional[Union[str, bool]] = ..., node: Optional[Union[str, bool]] = ..., writableSequencer: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The sequenceManager command manages sequences, shots, and their related scenes.

    Args:
        addSequencerAudio: (create) - Add an audio clip to the sequencer by specifying a filename
        attachSequencerAudio: (create) - Add an audio clip to the sequencer by specifying an audio node
        currentShot: (query) - Returns the shot that is being used at the current sequence time.
        currentTime: (create, query) - Set the current sequence time
        listSequencerAudio: (create) - List the audio clips added to the sequencer
        listShots: (create) - List all the currently defined shots across all scene segments
        modelPanel: (create, query) - Sets a dedicated modelPanel to be used as the panel that the sequencer will control.
        node: (query) - Returns the SequenceManager node, of which there is only ever one.
        writableSequencer: (query) - Get the writable sequencer node.  Create it if it doesn't exist.
    """
    ...


def setDrivenKeyframe(*args, attribute: Optional[Union[str, bool]] = ..., controlPoints: bool = ..., count: bool = ..., currentDriver: Optional[Union[str, bool]] = ..., driven: bool = ..., driver: bool = ..., driverValue: Optional[Union[float, bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., inTangentType: Optional[Union[str, bool]] = ..., insert: bool = ..., insertBlend: bool = ..., outTangentType: Optional[Union[str, bool]] = ..., shape: bool = ..., value: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command sets a driven keyframe.  A driven keyframe is similar
    to a regular keyframe. However, while a standard keyframe always has
    an x-axis of time in the graph editor, for a drivenkeyframe the
    user may choose any attribute as the x-axis of the graph editor.
    
    For example, you can keyframe the emission of a faucet so that
    so that it emits whenever the faucet handle is rotated around y.
    The faucet emission in this example is called the driven attribute.
    The handle rotation is called the driver. Once you have used
    setDrivenKeyframe to set up the relationship between the emission
    and the rotation, you can go to the graph editor and modify the
    relationship between the attributes just as you would modify the
    animation curve on any keyframed object.
    
    In the case of an attribute driven by a single driver, the
    dependency graph is connected like this:
    
    driver attribute ---> animCurve ---> driven attribute
    
    You can set driven keyframes with more than a single driver.
    The effects of the multiple drivers are combined together by
    a blend node.

    Args:
        attribute: (create, multiuse) - Attribute name to set keyframes on.
        controlPoints: (create) - Explicitly specify whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.
        count: (query) - Returns the count of driven/drivers attributes for the selected item instead of the names
        currentDriver: (create, query) - Set the driver to be used for the current driven keyframe to the attribute passed as an argument.
        driven: (query) - Returns list of driven attributes for the selected item.
        driver: (query) - Returns list of available drivers for the attribute.
        driverValue: (create, multiuse) - Value of the driver to use for this keyframe. Default value is the current value.
        hierarchy: (create) - Controls the objects this command acts on, relative to the specified (or active) target objects. Valid values are "above," "below," "both," and "none." Default is "hierarchy -query"
        inTangentType: (create) - The in tangent type for keyframes set by this command. Valid values are: "auto", clamped", "fast", "flat", "linear", "plateau", "slow", "spline", and "stepnext" Default is "keyTangent -q -g -inTangentType"
        insert: (create) - Insert keys at the given time(s) and preserve the shape of the animation curve(s). Note: the tangent type on inserted keys will be fixed so that the curve shape can be preserved.
        insertBlend: (create) - If true, a pairBlend node will be inserted for channels that have nodes other than animCurves driving them, so that such channels can have blended animation. If false, these channels will not have keys inserted. If the flag is not specified, the blend will be inserted based on the global preference for blending animation.
        outTangentType: (create) - The out tangent type for keyframes set by this command. Valid values are: "auto", "clamped", "fast", "flat", "linear", "plateau", "slow", "spline", "step", and "stepnext". Default is "keyTangent -q -g -outTangentType"
        shape: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true
        value: (create) - Value to set the keyframe at. Default is the current value.
    """
    ...


def setInfinity(*args, attribute: Optional[Union[str, bool]] = ..., controlPoints: bool = ..., hierarchy: Optional[Union[str, bool]] = ..., postInfinite: Optional[Union[str, bool]] = ..., preInfinite: Optional[Union[str, bool]] = ..., shape: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Set the infinity type before (after) a paramCurve's first
    (last) keyframe.

    Args:
        attribute: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        controlPoints: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        hierarchy: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        postInfinite: (create, query) - Set the infinity type after a paramCurve's last keyframe. Valid values are "constant", "linear", "cycle", "cycleRelative", "oscillate".
        preInfinite: (create, query) - Set the infinity type before a paramCurve's first keyframe. Valid values are "constant", "linear", "cycle", "cycleRelative", "oscillate".
        shape: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
    """
    ...


def setKeyframe(*args, adjustTangent: bool = ..., animLayer: Optional[Union[str, bool]] = ..., animated: bool = ..., attribute: Optional[Union[str, bool]] = ..., breakdown: bool = ..., clip: Optional[Union[str, bool]] = ..., controlPoints: bool = ..., dirtyDG: bool = ..., float: Optional[Union[float, bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., identity: bool = ..., inTangentType: Optional[Union[str, bool]] = ..., insert: bool = ..., insertBlend: bool = ..., minimizeRotation: bool = ..., noResolve: bool = ..., outTangentType: Optional[Union[str, bool]] = ..., preserveCurveShape: bool = ..., respectKeyable: bool = ..., shape: bool = ..., time: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., useCurrentLockedWeights: bool = ..., value: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates keyframes for the specified objects,
    or the active objects if none are specified on the command line.
    
    The default time for the new keyframes is the current time.
    Override this behavior with the "-t" flag on the command line.
    
    The default value for the keyframe is the current value
    of the attribute for which a keyframe is set.  Override
    this behavior with the "-v" flag on the command line.
    
    When setting keyframes on animation curves that do not have
    "time" as an input attribute (ie, they are unitless animation curves),
    use "-f/-float" to specify the unitless value at which to set a
    keyframe.
    
    The -time and -float flags may be combined in one command.
    
    This command sets up Dependency Graph relationships for
    proper evaluation of a given attribute at a given time.

    Args:
        adjustTangent: (create) - Adjsut tangent if insert keys
        animLayer: (create) - Specifies that the new key should be placed in the specified animation layer. Note that if the objects being keyframed are not already part of the layer, this flag will be ignored.
        animated: (create) - Add the keyframe only to the attribute(s) that have already a keyframe on. Default: false
        attribute: (create, multiuse) - Attribute name to set keyframes on.
        breakdown: (create, edit, query) - Sets the breakdown state for the key.  Default is false
        clip: (create) - Specifies that the new key should be placed in the specified clip. Note that if the objects being keyframed are not already part of the clip, this flag will be ignored.
        controlPoints: (create) - Explicitly specify whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.
        dirtyDG: (create) - Allow dirty messages to be sent out when a keyframe is set.
        float: (create, multiuse) - Float time at which to set a keyframe on float-based animation curves.
        hierarchy: (create) - Controls the objects this command acts on, relative to the specified (or active) target objects. Valid values are "above," "below," "both," and "none." Default is "hierarchy -query"
        identity: (create) - Sets an identity key on an animation layer.  An identity key is one that nullifies the effect of the anim layer.  This flag has effect only when the attribute being keyed is being driven by animation layers.
        inTangentType: (create) - The in tangent type for keyframes set by this command. Valid values are: "auto", clamped", "fast", "flat", "linear", "plateau", "slow", "spline", and "stepnext" Default is "keyTangent -q -g -inTangentType"
        insert: (create) - Insert keys at the given time(s) and preserve the shape of the animation curve(s). Note: the tangent type on inserted keys will be fixed so that the curve shape can be preserved.
        insertBlend: (create) - If true, a pairBlend node will be inserted for channels that have nodes other than animCurves driving them, so that such channels can have blended animation. If false, these channels will not have keys inserted. If the flag is not specified, the blend will be inserted based on the global preference for blending animation.
        minimizeRotation: (create) - For rotations, ensures that the key that is set is a minimum distance away from the previous key.  Default is false
        noResolve: (create) - When used with the -value flag, causes the specified value to be set directly onto the animation curve, without attempting to resolve the value across animation layers.
        outTangentType: (create) - The out tangent type for keyframes set by this command. Valid values are: "auto", "clamped", "fast", "flat", "linear", "plateau", "slow", "spline", "step", and "stepnext". Default is "keyTangent -q -g -outTangentType"
        preserveCurveShape: (create) - Sets the preserve curve shape when inserting keys. Default value depend on your keySetPreserveCurveShape option.
        respectKeyable: (create) - When used with the -attribute flag, prevents the keying of the non keyable attributes.
        shape: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true
        time: (create, multiuse) - Time at which to set a keyframe on time-based animation curves.
        useCurrentLockedWeights: (create) - If we are setting a key over an existing key, use that key tangent's locked weight value for the new locked weight value.  Default is false
        value: (create) - Value at which to set the keyframe. Using the value flag will not cause the keyed attribute to change to the specified value until the scene re-evaluates. Therefore, if you want the attribute to update to the new value immediately, use the setAttr command in addition to setting the key.
    """
    ...


def setKeyframeBlendshapeTargetWts(*args) -> Any:
    r"""
    This command can be used to keyframe per-point blendshape target weights. It operates
    on the currently selected objects as follows.
    When the base object is selected, then the target weights are keyed for all
    targets. When only target
    shapes are selected, then the weights for thoses targets are keyframed.

    Args:
    """
    ...


def setKeyPath(*args) -> Any:
    r"""
    The setKeyPath command either creates or edits the path (a nurbs curve)
    based on the current position of the selected object at the current time.

    Args:
    """
    ...


def shapeEditor(*args, clearSelection: bool = ..., control: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., exists: bool = ..., filter: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., highlightConnection: Optional[Union[str, bool]] = ..., lockMainConnection: bool = ..., lowestSelection: bool = ..., mainListConnection: Optional[Union[str, bool]] = ..., panel: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., selectionConnection: Optional[Union[str, bool]] = ..., stateString: bool = ..., targetControlList: bool = ..., targetList: bool = ..., unParent: bool = ..., unlockMainConnection: bool = ..., updateMainConnection: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., verticalSliders: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates an editor that derives from the base editor
    class that has controls for deformer, control nodes.

    Args:
        clearSelection: (edit) - Clear the shape editor selection.
        control: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag: (create, edit, query) - Attaches a tag to the editor.
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        filter: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        forceMainConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        highlightConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        lockMainConnection: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        lowestSelection: (query) - Query the lowest selection item.
        mainListConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        panel: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        selectionConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        stateString: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        targetControlList: (query) - Query the target control list.
        targetList: (query) - Query the target list.
        unParent: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
        verticalSliders: (create, edit, query) - Should the sliders be vertical?
    """
    ...


def shapePanel(*args, control: bool = ..., copy: str = ..., createString: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., editString: bool = ..., exists: bool = ..., init: bool = ..., isUnique: bool = ..., label: Optional[Union[str, bool]] = ..., menuBarRepeatLast: bool = ..., menuBarVisible: bool = ..., needsInit: bool = ..., parent: Optional[Union[str, bool]] = ..., popupMenuProcedure: Optional[Union[str, bool]] = ..., replacePanel: str = ..., shapeEditor: bool = ..., tearOff: bool = ..., tearOffCopy: Optional[Union[str, bool]] = ..., tearOffRestore: bool = ..., unParent: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a panel that derives from the base panel
    class that houses a shapeEditor.

    Args:
        control: (query) - Returns the top level control for this panel. Usually used for getting a parent to attach popup menus. CAUTION: panels may not have controls at times.  This flag can return "" if no control is present.
        copy: (edit) - Makes this panel a copy of the specified panel.  Both panels must be of the same type.
        createString: (edit) - Command string used to create a panel
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag: (create, edit, query) - Attaches a tag to the Maya panel.
        editString: (edit) - Command string used to edit a panel
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        init: (create, edit) - Initializes the panel's default state.  This is usually done automatically on file -new and file -open.
        isUnique: (query) - Returns true if only one instance of this panel type is allowed.
        label: (edit, query) - Specifies the user readable label for the panel.
        menuBarRepeatLast: (create, edit, query) - Controls whether clicking on the menu header with the middle mouse button would repeat the last selected menu item.
        menuBarVisible: (create, edit, query) - Controls whether the menu bar for the panel is displayed.
        needsInit: (edit, query) - (Internal) On Edit will mark the panel as requiring initialization. Query will return whether the panel is marked for initialization.  Used during file -new and file -open.
        parent: (create) - Specifies the parent layout for this panel.
        popupMenuProcedure: (edit, query) - Specifies the procedure called for building the panel's popup menu(s). The default value is "buildPanelPopupMenu".  The procedure should take one string argument which is the panel's name.
        replacePanel: (edit) - Will replace the specified panel with this panel.  If the target panel is within the same layout it will perform a swap.
        shapeEditor: (query) - Query only flag that returns the name of an editor to be associated with the panel.
        tearOff: (edit, query) - Will tear off this panel into a separate window with a paneLayout as the parent of the panel. When queried this flag will return if the panel has been torn off into its own window.
        tearOffCopy: (create) - Will create this panel as a torn of copy of the specified source panel.
        tearOffRestore: (create, edit) - Restores panel if it is torn off and focus is given to it. If docked, becomes the active panel in the docked window. This should be the default flag that is added to all panels instead of -to/-tearOff flag which should only be used to tear off the panel.
        unParent: (edit) - Specifies that the panel should be removed from its layout. This (obviously) cannot be used with query.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
    """
    ...


def shot(*args, audio: Optional[Union[str, bool]] = ..., clip: Optional[Union[str, bool]] = ..., clipDuration: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., clipOpacity: Optional[Union[float, bool]] = ..., clipSyncState: bool = ..., clipZeroOffset: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., copy: bool = ..., createCustomAnim: bool = ..., currentCamera: Optional[Union[str, bool]] = ..., customAnim: bool = ..., deleteCustomAnim: bool = ..., determineTrack: bool = ..., endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., favorite: bool = ..., flag1: bool = ..., flag10: bool = ..., flag11: bool = ..., flag12: bool = ..., flag2: bool = ..., flag3: bool = ..., flag4: bool = ..., flag5: bool = ..., flag6: bool = ..., flag7: bool = ..., flag8: bool = ..., flag9: bool = ..., hasCameraSet: bool = ..., hasStereoCamera: bool = ..., imagePlaneVisibility: bool = ..., linkAudio: Optional[Union[str, bool]] = ..., lock: bool = ..., mute: bool = ..., paste: bool = ..., pasteInstance: bool = ..., postHoldTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., preHoldTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., scale: Optional[Union[float, bool]] = ..., selfmute: bool = ..., sequenceDuration: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., sequenceEndTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., sequenceStartTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., shotName: Optional[Union[str, bool]] = ..., sourceDuration: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., track: Optional[Union[int, bool]] = ..., transitionInLength: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., transitionInType: Optional[Union[int, bool]] = ..., transitionOutLength: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., transitionOutType: Optional[Union[int, bool]] = ..., unlinkAudio: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Use this command to create a shot node or manipulate that node.

    Args:
        audio: (create, edit, query) - Specify the audio clip for this shot. Audio can be linked to a shot to allow playback of specific sounds when that shot is being displayed in the Sequencer. Refer to the shot node's documentation for details on how audio is used by shots and the Sequencer.
        clip: (create, edit, query) - The clip associated with this shot. This clip will be posted to the currentCamera's imagePlane. Refer to the shot node's documentation for details on how cameras are used by shots and the Sequencer.
        clipDuration: (create, edit, query) - Length of clip. This is used for the display of the clip indicator bar in the Sequencer.
        clipOpacity: (create, edit, query) - Opacity for the shot's clip, this value is assigned to the currentCamera's imagePlane. Refer to the shot node's documentation for details on how cameras are used by shots and the Sequencer.
        clipSyncState: (create, edit, query) - The viewport synchronization status of the clip associated with this shot. Return values are, 0 = no clip associated with this shot 1 = clip is fully in sync with viewport, and frames are 1:1 with sequencer 2 = clip is partially in sync with viewport, movie may be scaled to match sequencer 3 = clip not in sync with viewport (i.e. could have scale/time/camera differences)
        clipZeroOffset: (create, edit, query) - Specify which time of the clip corresponds to the beginning of the shot. This is used to properly align splitted clips.
        copy: (create, edit, query) - This flag is used to copy a shot to the clipboard. In query mode, this flag allows you to query what, if anything, has been copied into the shot clipboard.
        createCustomAnim: (edit) - Creates an animation layer and links the shot node's customAnim attr to the weight attr of the animation layer
        currentCamera: (create, edit, query) - The camera associated with this shot. Refer to the shot node's documentation for details on how cameras are used by shots and the Sequencer.
        customAnim: (query) - Returns the name of the animation layer node linked to this shot node's customAnim attr
        deleteCustomAnim: (edit) - Disconnects the animation layer from this shot's customAnim attr and deletes the animation layer node
        determineTrack: (edit, query) - Determines an available track for the shot. Returns a new track number or the existing track number if the current track is available.
        endTime: (create, edit, query) - The shot end time in the Maya timeline. Changing the startTime will extend the duration of a shot.
        favorite: (create, edit, query) - Make the shot a favorite. This is a UI indicator only to streamline navigation in the Sequencer panel
        flag1: (create, edit, query) - User specified state flag 1/12 for this shot
        flag10: (create, edit, query) - User specified state flag 10/12 for this shot
        flag11: (create, edit, query) - User specified state flag 11/12 for this shot
        flag12: (create, edit, query) - User specified state flag 12/12 for this shot
        flag2: (create, edit, query) - User specified state flag 2/12 for this shot
        flag3: (create, edit, query) - User specified state flag 3/12 for this shot
        flag4: (create, edit, query) - User specified state flag 4/12 for this shot
        flag5: (create, edit, query) - User specified state flag 5/12 for this shot
        flag6: (create, edit, query) - User specified state flag 6/12 for this shot
        flag7: (create, edit, query) - User specified state flag 7/12 for this shot
        flag8: (create, edit, query) - User specified state flag 8/12 for this shot
        flag9: (create, edit, query) - User specified state flag 9/12 for this shot
        hasCameraSet: (create, edit, query) - Returns true if the camera associated with this shot is a camera set.
        hasStereoCamera: (create, edit, query) - Returns true if the camera associated with this shot is a stereo camera.
        imagePlaneVisibility: (create, edit, query) - Visibility of the shot imageplane, this value is assigned to the currentCamera's imagePlane.
        linkAudio: (create, edit, query) - Specify an audio clip to link to this shot. Any currently linked audio will be unlinked.
        lock: (create, edit, query) - Lock a specific shot. This is different than locking an entire track, which is done via the shotTrack command
        mute: (create, edit, query) - Mute a specific shot. This is different than muting an entire track, which is done via the shotTrack command. Querying this attribute will return true if the shot is muted due to its own mute, its shot being muted, or its shot being unsoloed. See flag "selfmute" to query only the shot's own state.
        paste: (create, edit, query) - This flag is used to paste a shot or shots from the clipboard to the sequence timeline. Shots are added to the clipboard using the c/copy flag.
        pasteInstance: (create, edit, query) - This flag is used to paste an instance of a shot or shots from the clipboard to the sequence timeline. Unlike the p/paste flag, which duplicates the camera and image plane from the original source shot, the pi/pasteInstance flag shares the camera and image plane from the source shot. The audio node is duplicated.
        postHoldTime: (create, edit, query) - Specify the time length to append to the shot in the sequence timeline. This repeats the last frame of the shot, in sequence time, over the specified duration.
        preHoldTime: (create, edit, query) - Specify the time length to prepend to the shot in the sequence timeline. This repeats the first frame of the shot, in sequence time, over the specified duration.
        scale: (create, edit, query) - Specify an amount to scale the Maya frame range of the shot. This will affect the sequenceEndFrame, leaving the sequenceStartFrame unchanged.
        selfmute: (create, edit, query) - Query if this individual shot's own mute state is set. This is different from the flag "mute", which will return true if this shot is muted due to the track being muted or another track being soloed. Editing this flag will set this shot's own mute status (identical behavior as the flag "mute").
        sequenceDuration: (edit, query) - Return the sequence duration of the shot, which will include the holds and scale. This flag can only be queried.
        sequenceEndTime: (create, edit, query) - The shot end in the sequence timeline. Changing the endTime of a shot will scale it in sequence time.
        sequenceStartTime: (create, edit, query) - The shot start in the sequence timeline. Changing the startTime of a shot will shift it in sequence time.
        shotName: (create, edit, query) - Specify a user-defined name for this shot. This allows the assignment of names that are not valid as node names within Maya. Whenever the shotName attribute is defined its value is used in the UI.
        sourceDuration: (edit, query) - Return the number of source frames in the shot. This flag can only be queried.
        startTime: (create, edit, query) - The shot start time in the Maya timeline. Changing the startTime will extend the duration of a shot.
        track: (edit, query) - Specify the track in which this shot resides.
        transitionInLength: (create, edit, query) - Length of the transtion into the shot.
        transitionInType: (edit, query) - Specify the the type of transition for the transition into the shot. 0 = Fade 1 = Dissolve
        transitionOutLength: (create, edit, query) - Length of the transtion out of the shot.
        transitionOutType: (edit, query) - Specify the the type of transition for the transition out of the shot. 0 = Fade 1 = Dissolve
        unlinkAudio: (edit, query) - COMMENT Unlinks any currently linked audio.
    """
    ...


def shotRipple(*args, deleted: bool = ..., endDelta: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., startDelta: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    When Ripple Edit Mode is enabled, neighboring shots to the shot that gets manipulated
    are moved in sequence time to either make way or close up gaps corresponding to that
    node's editing.
    Given some parameters about the shot edit that just took place, this command
    will choose which other shots to move, and move them the appropriate amounts
    If no shot name is provided, the command will attempt to use the first selected shot.

    Args:
        deleted: (create, edit, query) - Specify whether this ripple edit is due to a shot deletion
        endDelta: (create, edit, query) - Specify the change in the end time in frames
        endTime: (create, edit, query) - Specify the initial shot end time in the sequence timeline.
        startDelta: (create, edit, query) - Specify the change in the start time in frames
        startTime: (create, edit, query) - Specify the initial shot start time in the sequence timeline.
    """
    ...


def simplify(*args, animation: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., controlPoints: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., floatTolerance: Optional[Union[float, bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., includeUpperBound: bool = ..., index: Optional[Union[int, bool]] = ..., shape: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., timeTolerance: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., valueTolerance: Optional[Union[float, bool]] = ...) -> Any:
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
    
    This command will simplify (reduce the number of keyframes) an animation
    curve.

    Args:
        animation: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        controlPoints: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        float: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        floatTolerance: (create) - Specify the x-axis tolerance (defaults to 0.05) for float-input animCurves such as those created by "Set Driven Keyframe". This flag is ignored on animCurves driven by time. Higher floatTolerance values will result in sparser keys which may less accurately represent the initial curve.
        hierarchy: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        includeUpperBound: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        shape: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        time: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
        timeTolerance: (create) - Specify the x-axis tolerance (defaults to 0.05 seconds) for time-input animCurves. This flag is ignored on animCurves driven by floats. Higher time tolerance values will result in sparser keys which may less accurately represent the initial curve.
        valueTolerance: (create) - Specify the value tolerance (defaults to 0.01)
    """
    ...


def skeletonEmbed(*args, mergedMesh: bool = ..., segmentationMethod: Optional[Union[int, bool]] = ..., segmentationResolution: Optional[Union[int, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command is used to embed a skeleton inside meshes.

    Args:
        mergedMesh: (query) - When specified, the query command merges selected meshes together and returns a Python object representing the merged mesh.
        segmentationMethod: (create) - Specifies which segmentation algorithm to use to determine what is inside the mesh and what is outside the mesh.  By default, boundary-and-fill-and-grow voxelization will be used.  Available algorithms are:   0  : Perfect mesh (no voxelization). This method works for "perfect meshes", i.e. meshes that are closed, watertight, 2-manifold and without self-intersection or interior/hidden geometry.  It segments the interior region of the mesh from the exterior using a pseudo-normal test. It does not use voxelization.  If mesh conditions are not respected, the segmentation is likely to be wrong.  This can make the segmentation process significantly longer and prevent successful skeleton embedding.   1 : Watertight mesh (flood fill). This method works for "watertight meshes", i.e. meshes for which faces completely separate the interior region of the mesh from the exterior.  The mesh can have degenerated faces, wrong face orientation, self-intersection, etc.  The method uses surface voxelization to classify as part of the interior region all voxels intersecting with a mesh face.  It then performs flood-filling from the outside, marking all reached voxels as part of the exterior region of the model.  Finally, all unreached voxels are marked as part of the interior region.  This method works so long as the mesh is watertight, i.e. without holes up to the voxelization resolution. Otherwise, flood-filling reaches the interior region and creates inaccurate segmentation.   2 : Imperfect mesh (flood fill + growing). This method works for meshes where holes could make the flood-filling step reach the interior region of the mesh, but that have face orientation consistent enough so filling them is possible.  First, it uses surface voxelization to classify as part of the interior region all voxels intersecting with a mesh face.  It then alternates flood-filling and growing steps.  The flood-filling tries to reach all voxels from the outside so that unreached voxels are marked as part of the interior region.  The growing step uses a relatively computation-intensive process to check for interior voxels in all neighbors to those already identified.  Any voxel identified as interior is likely to fill holes, allowing subsequent flood-filling steps to identify more interior voxels.   3 : Polygon soup (repair). This method has no manifold or face orientation requirements.  It reconstructs a mesh that wraps the input mesh with a given offset (3 times the voxel size) and uses this perfect 2-manifold mesh to segment the interior region from the exterior region of the model. Because of the offset, it might lose some of the details and merge parts that are proximal. However, this usually is not an issue with common models where body parts are not too close to one another.   99 : Direct skeleton (no embedding). This method does not try to perform embedding.  It simply returns the skeleton in its initial pose without any attempt at embedding inside the meshes, other than placing it in the meshes bounding box.
        segmentationResolution: (create) - Specifies which segmentation resolution to use for the voxel grid.  By default, 256x256x256 voxels will be used.
    """
    ...


def skinCluster(*args, addInfluence: str = ..., addToSelection: bool = ..., after: bool = ..., afterReference: bool = ..., baseShape: str = ..., before: bool = ..., bindMethod: Optional[Union[int, bool]] = ..., components: bool = ..., deformerTools: bool = ..., dropoffRate: Optional[Union[float, bool]] = ..., exclusive: Optional[Union[str, bool]] = ..., forceNormalizeWeights: bool = ..., frontOfChain: bool = ..., geometry: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., heatmapFalloff: Optional[Union[float, bool]] = ..., ignoreBindPose: bool = ..., ignoreHierarchy: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., influence: Optional[Union[str, bool]] = ..., lockWeights: bool = ..., maximumInfluences: Optional[Union[int, bool]] = ..., moveJointsMode: bool = ..., multi: bool = ..., name: Optional[Union[str, bool]] = ..., normalizeWeights: Optional[Union[int, bool]] = ..., nurbsSamples: Optional[Union[int, bool]] = ..., obeyMaxInfluences: bool = ..., parallel: bool = ..., polySmoothness: Optional[Union[float, bool]] = ..., prune: bool = ..., recacheBindMatrices: bool = ..., remove: bool = ..., removeFromSelection: bool = ..., removeInfluence: str = ..., removeUnusedInfluence: bool = ..., selectInfluenceVerts: str = ..., selectedComponents: bool = ..., skinMethod: Optional[Union[int, bool]] = ..., smoothWeights: float = ..., smoothWeightsMaxIterations: int = ..., split: bool = ..., toSelectedBones: bool = ..., toSkeletonAndTransforms: bool = ..., unbind: bool = ..., unbindKeepHistory: bool = ..., useComponentTags: bool = ..., useGeometry: bool = ..., volumeBind: Optional[Union[float, bool]] = ..., volumeType: Optional[Union[int, bool]] = ..., weight: float = ..., weightDistribution: Optional[Union[int, bool]] = ..., weightedInfluence: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The skinCluster command is used for smooth skinning in maya. It
    binds the selected geometry to the selected
    joints or skeleton by means of a skinCluster node.  Each point of the bound
    geometry can be affected by any number of joints.
    The extent to which each joint affects the motion of each point is
    regulated by a corresponding weight factor.  Weight factors can be
    modified using the skinPercent command.  The command returns the name
    of the new skinCluster.
    
    The skinCluster binds only a single geometry at a time. Thus, to bind
    multiple geometries, multiple skinCluster commands must be issued.
    
    Upon creation of a new skinCluster, the command can be used to add
    and remove transforms (not necessarily joints) that influence the
    motion of the bound skin points.  
    
    The skinCluster command can also be used to adjust parameters such
    as the dropoff, nurbs samples, polygon smoothness on a particular
    influence object. Note: Any custom weights on a skin point that
    the influence object affects will be lost after adjusting these
    parameters.

    Args:
        addInfluence: (edit, multiuse) - The specified transform or joint will be added to the list of transforms that influence the bound geometry. The maximum number of influences will be observed and only the weights of the cv's that the specified transform effects will change. This flag is multi-use.
        addToSelection: (edit) - When used in conjunction with the selectInfluenceVerts flag, causes the vertices afftected by the influence to be added to the current selection, without first de-selecting other vertices.
        after: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        baseShape: (edit, multiuse) - This flag can be used in conjunction with the -addInfluence flag to specify the shape that will be used as the base shape when an influence object with geometry is added to the skinCluster.  If the flag is not used then the command will make a copy of the influence object's shape and use that as a base shape.
        before: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        bindMethod: (create, query) - This flag sets the binding method. 0 - Closest distance between a joint and a point of the geometry. 1 - Closest distance between a joint, considering the skeleton hierarchy, and a point of the geometry. 2 - Surface heat map diffusion. 3 - Geodesic voxel binding.  geomBind command must be called after creating a skinCluster with this method.
        components: (query) - Returns the components used by the deformer
        deformerTools: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        dropoffRate: (create, edit, query) - Sets the rate at which the influence of a transform drops as the distance from that transform increases. The valid range is between 0.1 and 10.0.  In Create mode it sets the dropoff rate for all the bound joints.  In Edit mode the flag is used together with the inf/influence flag to set the dropoff rate of a particular influence.  Note: When the flag is used in Edit mode, any custom weights on the skin points the given transform influences will be lost.
        exclusive: (create, query) - Puts the deformation set in a deform partition.
        forceNormalizeWeights: (edit) - If the normalization mode is none or post, it is possible (indeed likely) for the weights in the skin cluster to no longer add up to 1.  This flag forces all weights to add back to 1 again.
        frontOfChain: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        heatmapFalloff: (create) - This flag sets the heatmap binding falloff. If set to 0.0 (default) the deformation will be smoother due to many small weights spread over the mesh surface per influence. However, if set to 1.0, corresponding to maximum falloff, the number of influences per point will be reduced and points will tend to be greatly influenced by their closest joint decreasing the overall spread of small weights. This flag only works when using heatmap binding.
        ignoreBindPose: (create, edit) - This flag is deprecated and no longer used.  It will be ignored if used.
        ignoreHierarchy: (create, query) - Deprecated. Use bindMethod flag instead. Disregard the place of the joints in the skeleton hierarchy when computing the closest joints that influence a point of the geometry.
        ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        influence: (edit, query) - This flag specifies the influence object that will be used for the current edit operation. In query mode, returns a string array of the influence objects (joints and transform).       In query mode, this flag can accept a value.
        lockWeights: (edit, query) - Lock the weights of the specified influence object to their current value or to the value specified by the -weight flag.
        maximumInfluences: (create, edit, query) - Sets the maximum number of transforms that can influence a point (have non-zero weight for the point) when the skinCluster is first created or a new influence is added.  Note: When this flag is used in Edit mode any custom weights will be lost and new weights will be reassigned to the whole skin.
        moveJointsMode: (edit) - If set to true, puts the skin into a mode where joints can be moved without modifying the skinning. If set to false, takes the skin out of move joints mode.
        multi: (create) - If true then the command will allow multiple skin clusters to be created on the target geometry. If false the command will generate an error if when trying to add a second skin cluster to the geometry.
        name: (create) - Used to specify the name of the node being created.
        normalizeWeights: (create, edit, query) - This flag sets the normalization mode. 0 - none, 1 - interactive, 2 - post (default) Interactive normalization makes sure the weights on the influences add up to 1.0, always. Everytime a weight is changed, the weights are automatically normalized.  This may make it difficult to perform weighting operations, as the normalization may interfere with the weights the user has set.  Post normalization leaves the weights the user has set as is, and only normalizes the weights at the moment it is needed (by dividing by the sum of the weights).  This makes it easier for users to weight their skins.
        nurbsSamples: (create, edit) - Sets the number of sample points that will be used along an influence curve or in each direction on an influence NURBS surface to influence the bound skin. The more the sample points the more closely the skin follows the influence NURBS curve/surface.
        obeyMaxInfluences: (create, edit, query) - When true, the skinCluster will continue to enforce the maximum influences each time the user modifies the weight, so that any given point is only weighted by the number of influences in the skinCluster's maximumInfluences attribute.
        parallel: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        polySmoothness: (create, edit) - This flag controls how accurately the skin control points follow a given polygon influence object. The higher the value of polySmoothnmess the more rounded the deformation resulting from a polygonal influence object will be.
        prune: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        recacheBindMatrices: (edit) - Forces the skinCluster node to recache its bind matrices.
        remove: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        removeFromSelection: (edit) - When used in conjunction with the selectInfluenceVerts flag, causes the vertices afftected by the influence to be removed from the current selection.
        removeInfluence: (edit, multiuse) - Remove the specified transform or joint from the list of transforms that influence the bound geometry The weights for the affected points are renormalized. This flag is multi-use.
        removeUnusedInfluence: (create, edit, query) - If this flag is set to true then transform or joint whose weights are all zero (they have no effect) will not be bound to the geometry.  Having this option set will help speed-up the playback of animation. In query mode, returns the number of transforms or joints whose weights are all zero.
        selectInfluenceVerts: (edit) - Given the name of a transform, this will select the verts or control points being influenced by this transform, so users may visualize which vertices are being influenced by the transform.
        selectedComponents: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        skinMethod: (create, edit, query) - This flag set the skinning method. 0 - classical linear skinning (default). 1 - dual quaternion (volume preserving), 2 - a weighted blend between the two.
        smoothWeights: (edit) - This flag is used to detect sudden jumps in skin weight values, which often indicates bad weighting, and then smooth out those jaggies in skin weights. The argument is the error tolerance ranging from 0 to 1.  A value of 1 means that the algorithm will smooth a vertex only if there is a 100% change in weight values from its neighbors.  The recommended default to use is 0.5 (50% change in weight value from the neighbors).
        smoothWeightsMaxIterations: (edit) - This flag is valid only with the smooth weights flag.  It is possible that not all the vertices detected as needing smoothing can be smoothed in 1 iteration (because all of their neighbors also have bad weighting and need to be smoothed). With more iterations, more vertices can be smoothed.  This flag controls the maximum number of iterations the algorithm will attempt to smooth weights. The default is 2 for this flag.
        split: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        toSelectedBones: (create) - geometry will be bound to the selected bones only.
        toSkeletonAndTransforms: (create) - geometry will be bound to the skeleton and any transforms in the hierarchy. If any of the transforms are also bindable objects, assume that only the last object passed to the command is the bindable object. The rest are treated as influences.
        unbind: (edit) - Unbinds the geometry from the skinCluster and deletes the skinCluster node
        unbindKeepHistory: (edit) - Unbinds the geometry from the skinCluster, but keeps the skinCluster node so that its weights can be used when the skin is rebound. To rebind, use the skinCluster command.
        useComponentTags: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
        useGeometry: (edit) - When adding an influence to a skinCluster, use the geometry parented under the influence transform to determine the weight dropoff of that influence.
        volumeBind: (create) - Creates a volume bind node and attaches it to the new skin cluster node. This node holds hull geometry parameters for a volume based weighting system. This system is used in interactive skinning. The value passed will determine the minimum weight value when initializing the volume. The volume in be increase to enclose all the vertices that are above this value.
        volumeType: (create) - Defines the initial shape of the binding volume (see volumeBind). 0 - Default (currently set to a capsule) 1 - Capsule, 2 - Cylinder.
        weight: (edit) - This flag is only valid in conjunction with the -addInfluence flag. It sets the weight for the influence object that is being added.
        weightDistribution: (create, edit, query) - This flag sets the weight distribution mode. 0 - distance (default), 1 - neighbors When normalizeWeights is in effect, and a weight has been reduced or removed altogether, the sum is usually brought back up to 1.0 by increasing the contributions of the other non-zero weights. However, if there are no other non-zero weights, the algorithm has to create some weights from thin air and distribute the residual weight between them. This attribute controls how that is done. "Distance" - the algorithm calculates weights from the world-space distances from the component to the transforms. "Neighbors" - the algorithm calculates weights from the weights on the neighboring components.
        weightedInfluence: (query) - This flag returns a string array of the influence objects (joints and transform) that have non-zero weighting.
    """
    ...


def skinPercent(*args, ignoreBelow: Optional[Union[float, bool]] = ..., normalize: bool = ..., pruneWeights: Optional[Union[float, bool]] = ..., relative: bool = ..., resetToDefault: bool = ..., transform: Optional[Union[str, bool]] = ..., transformMoveWeights: Optional[Union[str, bool]] = ..., transformValue: Optional[Union[Tuple[str, float], bool]] = ..., value: bool = ..., zeroRemainingInfluences: bool = ..., query: bool = ...) -> Any:
    r"""
    This command edits and queries the weight values on members of a
    skinCluster node, given as the first argument. If no object components
    are explicitly mentioned in the command line, the current selection
    list is used.
    
    Note that setting multiple weights in a single invocation of this
    command is far more efficient than calling it once per weighted
    vertex.

    Args:
        ignoreBelow: (query) - Limits the output of the -value and -transform queries to the entries whose weight values are over the specified limit.  This flag has to be used before the -query flag.       In query mode, this flag needs a value.
        normalize: (create) - If set, the weights not assigned by the -transformValue flag are normalized so that the sum of the all weights for the selected object component add up to 1. The default is on. NOTE: The skinCluster has a normalizeWeights attribute which when set to OFF overrides this attribute! If the skinCluster.normalizeWeights attribute is OFF, you must set it to Interactive in order to normalize weights using the skinPercent command.
        pruneWeights: (create) - Sets to zero any weight smaller than the given value for all the selected components. To use this command to set all the weights to zero, you must turn the -normalize flag "off" or the skinCluster node will normalize the weights to sum to one after pruning them. Weights for influences with a true value on their "Hold Weights" attribute will not be pruned.
        relative: (create) - Used with -transformValue to specify a relative setting of values. If -relative is true, the value passed to -tv is added to the previous value.  Otherwise, it replaces the previous value.
        resetToDefault: (create) - Sets the weights of the selected components to their default values, overwriting any custom weights.
        transform: (query) - In Mel, when used after the -query flag (without an argument) the command returns an array of strings corresponding to the names of the transforms influencing the selected object components.  If used before the -query flag (with a transform name), the command returns the weight of the selected object component corresponding to the given transform. The command will return an average weight if several components have been selected.  In Python, when used with None instead of the name of the transform, the command returns an array of strings corresponding to the names of the transforms influencing the selected object components. If used with a transform name, the command returns the weight of the selected object. The command will return an average weight if several components have been selected.        In query mode, this flag can accept a value.
        transformMoveWeights: (create, multiuse) - This flag is used to transfer weights from a source influence to one or more target influences. It acts on the selected vertices. The flag must be used at least twice to generate a valid command. The first flag usage indicates the source influence from which the weights will be copied. Subsequent flag usages indicate the target influences.
        transformValue: (create, multiuse) - Accepts a pair consisting of a transform name and a value and assigns that value as the weight of the selected object components corresponding to the given transform.
        value: (query) - Returns an array of doubles corresponding to the joint weights for the selected object component.
        zeroRemainingInfluences: (create) - If set, the weights not assigned by the -transformValue flag are set to 0. The default is off.
    """
    ...


def snapKey(*args, animation: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., controlPoints: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., includeUpperBound: bool = ..., index: Optional[Union[int, bool]] = ..., mergeDuplicate: bool = ..., shape: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., timeMultiple: Optional[Union[float, bool]] = ..., valueMultiple: Optional[Union[float, bool]] = ...) -> Any:
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
    
    This command "snaps" all target key times and/or values
    so that they have times and/or values that are multiples
    of the specified flag arguments.  If neither multiple is
    specified, default is time snapping with a multiple of 1.0.
    Note that this command will fail to move keys over other
    neighboring keys: a key's index will not change as a result
    of a snapKey operation.
    
    TbaseKeySetCmd.h

    Args:
        animation: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        controlPoints: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        float: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        hierarchy: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        includeUpperBound: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        mergeDuplicate: (create) - If this flag is present, keys with duplicated frame will be merged into 1. Default false
        shape: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        time: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
        timeMultiple: (create) - If this flag is present, key times will be snapped to a multiple of the specified float value.
        valueMultiple: (create) - If this flag is present, key values will be snapped to a multiple of the specified float value.
    """
    ...


def snapshot(*args, constructionHistory: bool = ..., endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., increment: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., motionTrail: bool = ..., name: Optional[Union[str, bool]] = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., update: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command can be used to create either a series of surfaces evaluated at
    the times specified by the command flags, or a motion trail displaying the
    trajectory of the object's pivot point at the times specified.
    
    If the constructionHistory flag is true, the output shapes or motion trail
    will re-update when modifications are made to the animation or construction
    history of the original shape. When construction history is used, the forceUpdate
    flag can be set to false to control when the snapshot recomputes, which will
    typically improve performance.

    Args:
        constructionHistory: (create, query) - update with changes to original geometry
        endTime: (create, edit, query) - time to stop copying target geometry Default: 10.0
        increment: (create, edit, query) - time increment between copies Default: 1.0
        motionTrail: (create) - Rather than create a series of surfaces, create a motion trail displaying the location of the object's pivot point at the specified time steps. Default is false.
        name: (create, edit, query) - the name of the snapshot node. Query returns string.
        startTime: (create, edit, query) - time to begin copying target geometry Default: 1.0
        update: (create, edit, query) - This flag can only be used if the snapshot has constructionHistory. It sets the snapshot node's update value. The update value controls whether the snapshot updates on demand (most efficient), when keyframes change (efficient), or whenever any history changes (least efficient). Valid values are "demand", "animCurve", "always". Default: "always"
    """
    ...


def snapshotBeadCtx(*args, exists: bool = ..., history: bool = ..., image1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., inTangent: bool = ..., name: Optional[Union[str, bool]] = ..., outTangent: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Creates a context for manipulating in and/or out tangent beads on the motion trail

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        inTangent: (edit, query) - Indicates that we will be showing beads for the in tangent when entering the context
        name: (create) - If this is a tool command, name the tool appropriately.
        outTangent: (edit, query) - Indicates that we will be showing beads for the out tangent when entering the context
    """
    ...


def snapshotModifyKeyCtx(*args, exists: bool = ..., history: bool = ..., image1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Creates a context for inserting/delete keys on an editable motion trail

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def softMod(*args, after: bool = ..., afterReference: bool = ..., before: bool = ..., bindState: bool = ..., components: bool = ..., curveInterpolation: Optional[Union[int, bool]] = ..., curvePoint: Optional[Union[float, bool]] = ..., curveValue: Optional[Union[float, bool]] = ..., deformerTools: bool = ..., envelope: Optional[Union[float, bool]] = ..., exclusive: Optional[Union[str, bool]] = ..., falloffAroundSelection: bool = ..., falloffBasedOnX: bool = ..., falloffBasedOnY: bool = ..., falloffBasedOnZ: bool = ..., falloffCenter: Optional[Union[Tuple[float, float, float], bool]] = ..., falloffMasking: bool = ..., falloffMode: Optional[Union[int, bool]] = ..., falloffRadius: Optional[Union[float, bool]] = ..., frontOfChain: bool = ..., geometry: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., name: Optional[Union[str, bool]] = ..., parallel: bool = ..., prune: bool = ..., relative: bool = ..., remove: bool = ..., resetGeometry: bool = ..., selectedComponents: bool = ..., split: bool = ..., useComponentTags: bool = ..., weightedNode: Optional[Union[Tuple[str, str], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The softMod command creates a softMod or edits the membership of
    an existing softMod. The command returns the name of the softMod
    node upon creation of a new softMod.

    Args:
        after: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        bindState: (create) - Specifying this flag adds in a compensation to ensure the softModed objects preserve their spatial position when softModed. This is required to prevent the geometry from jumping at the time the softMod is created in situations when the softMod transforms at softMod time are not identity.
        components: (query) - Returns the components used by the deformer
        curveInterpolation: (create, multiuse) - Ramp interpolation corresponding to the specified curvePoint position. Integer values of 0-3 are valid, corresponding to "none", "linear", "smooth" and "spline" respectively. This flag may only be used in conjunction with the curvePoint and curveValue flag.
        curvePoint: (create, multiuse) - Position of ramp value on normalized 0-1 scale. This flag may only be used in conjunction with the curveInterpolation and curveValue flags.
        curveValue: (create, multiuse) - Ramp value corresponding to the specified curvePoint position. This flag may only be used in conjunction with the curveInterpolation and curvePoint flags.
        deformerTools: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        envelope: (create, edit, query) - Set the envelope value for the deformer. Default is 1.0
        exclusive: (create, query) - Puts the deformation set in a deform partition.
        falloffAroundSelection: (create) - Falloff will be calculated around any selected components
        falloffBasedOnX: (create) - Falloff will be calculated using the X component.
        falloffBasedOnY: (create) - Falloff will be calculated using the Y component.
        falloffBasedOnZ: (create) - Falloff will be calculated using the Z component.
        falloffCenter: (create) - Set the falloff center point of the softMod.
        falloffMasking: (create) - Deformation will be restricted to selected components
        falloffMode: (create) - Set the falloff method used for the softMod.
        falloffRadius: (create) - Set the falloff radius of the softMod.
        frontOfChain: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        name: (create) - Used to specify the name of the node being created.
        parallel: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        prune: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        relative: (create) - Enable relative mode for the softMod. In relative mode, Only the transformations directly above the softMod are used by the softMod. Default is off.
        remove: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        resetGeometry: (edit) - Reset the geometry matrices for the objects being deformed by the softMod. This flag is used to get rid of undesirable effects that happen if you scale an object that is deformed by a softMod.
        selectedComponents: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        split: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        useComponentTags: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
        weightedNode: (create, edit, query) - Transform node in the DAG above the softMod to which all percents are applied. The second node specifies the descendent of the first node from where the transformation matrix is evaluated. Default is the softMod handle.
    """
    ...


def sound(*args, endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., file: Optional[Union[str, bool]] = ..., length: bool = ..., mute: bool = ..., name: Optional[Union[str, bool]] = ..., offset: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., sourceEnd: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., sourceStart: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Creates an audio node which can be used with UI commands such
    as soundControl or timeControl which support sound scrubbing
    and sound during playback.

    Args:
        endTime: (create, edit, query) - Time at which to end the sound.
        file: (create, edit, query) - Name of sound file.
        length: (query) - Query the length (in the current time unit) of the sound.
        mute: (create, edit, query) - Mute the audio clip.
        name: (create, edit, query) - Name to give the resulting audio node.
        offset: (create, edit, query) - Time at which to start the sound.
        sourceEnd: (create, edit, query) - Time offset from the start of the sound file at which to end the sound.
        sourceStart: (create, edit, query) - Time offset from the start of the sound file at which to start the sound.
    """
    ...


def substituteGeometry(*args, disableNonSkinDeformers: bool = ..., newGeometryToLayer: bool = ..., oldGeometryToLayer: bool = ..., reWeightDistTolerance: Optional[Union[float, bool]] = ..., retainOldGeometry: bool = ...) -> Any:
    r"""
    This command can be used to replace the geometry which is already connected
    to deformers with a new geometry. The weights on the old geometry will be
    retargeted to the new geometry.

    Args:
        disableNonSkinDeformers: (create) - This flag controls the state of deformers other than skin deformers after the substitution has taken place. If the flag is true then non-skin deformer nodes are left in a disabled state at the completion of the command. Default value is false.
        newGeometryToLayer: (create) - Create a new layer for the new geometry.
        oldGeometryToLayer: (create) - Create a new layer and move the old geometry to this layer
        reWeightDistTolerance: (create) - Specify the distance tolerance value to be used for retargeting weights. While transferring weights the command tries to find the corresponding vertices by overlapping the geometries with all deformers disabled. Sometimes this results in selection of unrelated vertices. (Example when a hole in the old geometry has been filled with new vertices in the new geometry.) This distance tolerance value is used to detect this kind of faults and either ignore these cases or to vary algorithm to find more corresponding vertices.
        retainOldGeometry: (create) - A copy of the old geometry should be retained
    """
    ...


def tangentConstraint(*args, aimVector: Optional[Union[Tuple[float, float, float], bool]] = ..., layer: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., remove: bool = ..., targetList: bool = ..., upVector: Optional[Union[Tuple[float, float, float], bool]] = ..., weight: Optional[Union[float, bool]] = ..., weightAliasList: bool = ..., worldUpObject: Optional[Union[str, bool]] = ..., worldUpType: Optional[Union[str, bool]] = ..., worldUpVector: Optional[Union[Tuple[float, float, float], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Constrain an object's orientation based on the tangent of the target
    curve[s] at the closest point[s] to the object.
    
    A tangentConstraint takes as input one or more NURBS curves (the
    targets) and a DAG transform node (the object).  The tangentConstraint
    orients the constrained object such that the aimVector (in the
    object's local coordinate system) aligns in world space to combined
    tangent vector.  The upVector (again the the object's local coordinate
    system) is aligned in world space with the worldUpVector.  The
    combined tangent vector is a weighted average of the tangent vector
    for each target curve at the point closest to the constrained object.

    Args:
        aimVector: (create, edit, query) - Set the aim vector.  This is the vector in local coordinates that points at the target.  If not given at creation time, the default value of (1.0, 0.0, 0.0) is used.
        layer: (create, edit) - Specify the name of the animation layer where the constraint should be added.
        name: (create, edit, query) - Sets the name of the constraint node to the specified name.  Default name is constrainedObjectName_constraintType
        remove: (edit) - removes the listed target(s) from the constraint.
        targetList: (query) - Return the list of target objects.
        upVector: (create, edit, query) - Set local up vector.  This is the vector in local coordinates that aligns with the world up vector.  If not given at creation time, the default value of (0.0, 1.0, 0.0) is used.
        weight: (create, edit, query) - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
        weightAliasList: (query) - Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
        worldUpObject: (create, edit, query) - Set the DAG object use for worldUpType "object" and "objectrotation". See worldUpType for greater detail. The default value is no up object, which is interpreted as world space.
        worldUpType: (create, edit, query) - Set the type of the world up vector computation. The worldUpType can have one of 5 values: "scene", "object", "objectrotation", "vector", or "none". If the value is "scene", the upVector is aligned with the up axis of the scene and worldUpVector and worldUpObject are ignored. If the value is "object", the upVector is aimed as closely as possible to the origin of the space of the worldUpObject and the worldUpVector is ignored. If the value is "objectrotation" then the worldUpVector is interpreted as being in the coordinate space of the worldUpObject, transformed into world space and the upVector is aligned as closely as possible to the result. If the value is "vector", the upVector is aligned with worldUpVector as closely as possible and worldUpMatrix is ignored. Finally, if the value is "none" no twist calculation is performed by the constraint, with the resulting "upVector" orientation based previous orientation of the constrained object, and the "great circle" rotation needed to align the aim vector with its constraint. The default worldUpType is "vector".
        worldUpVector: (create, edit, query) - Set world up vector.  This is the vector in world coordinates that up vector should align with. See -wut/worldUpType (below)for greater detail. If not given at creation time, the default value of (0.0, 1.0, 0.0) is used.
    """
    ...


def tension(*args, after: bool = ..., afterReference: bool = ..., before: bool = ..., components: bool = ..., deformerTools: bool = ..., envelope: Optional[Union[float, bool]] = ..., exclusive: Optional[Union[str, bool]] = ..., frontOfChain: bool = ..., geometry: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., inwardConstraint: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., outwardConstraint: Optional[Union[float, bool]] = ..., parallel: bool = ..., pinBorderVertices: bool = ..., prune: bool = ..., remove: bool = ..., selectedComponents: bool = ..., smoothingIterations: Optional[Union[int, bool]] = ..., smoothingStep: Optional[Union[float, bool]] = ..., split: bool = ..., useComponentTags: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to create, edit and query tension nodes.

    Args:
        after: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        components: (query) - Returns the components used by the deformer
        deformerTools: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        envelope: (create, edit, query) - Envelope of the tension node. The envelope determines the percent of deformation. Value is clamped to [0, 1] range. Default is 1.
        exclusive: (create, query) - Puts the deformation set in a deform partition.
        frontOfChain: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        inwardConstraint: (create, edit, query) - Constrains the movement of the vertex to not move inward from the input deforming shape to preserve the contour. Value is in the [0,1] range. Default is 0.0.
        name: (create) - Used to specify the name of the node being created.
        outwardConstraint: (create, edit, query) - Constrains the movement of the vertex to not move outward from the input deforming shape to preserve the contour. Value is in the [0,1] range.
        parallel: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        pinBorderVertices: (create, edit, query) - If enabled, vertices on mesh borders will be pinned to their current position during smoothing. Default is true.
        prune: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        remove: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        selectedComponents: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        smoothingIterations: (create, edit, query) - Number of smoothing iterations performed by the tension node. Default is 10.
        smoothingStep: (create, edit, query) - Step amount used per smoothing iteration. Value is clamped to [0, 1] range. A higher value may lead to instabilities but converges faster compared to a lower value. Default is 0.5.
        split: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        useComponentTags: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
    """
    ...


def textureDeformer(*args, after: bool = ..., afterReference: bool = ..., before: bool = ..., components: bool = ..., deformerTools: bool = ..., direction: Optional[Union[str, bool]] = ..., envelope: Optional[Union[float, bool]] = ..., exclusive: Optional[Union[str, bool]] = ..., frontOfChain: bool = ..., geometry: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., name: Optional[Union[str, bool]] = ..., offset: Optional[Union[float, bool]] = ..., parallel: bool = ..., pointSpace: Optional[Union[str, bool]] = ..., prune: bool = ..., remove: bool = ..., selectedComponents: bool = ..., split: bool = ..., strength: Optional[Union[float, bool]] = ..., useComponentTags: bool = ..., vectorOffset: Optional[Union[Tuple[float, float, float], bool]] = ..., vectorSpace: Optional[Union[str, bool]] = ..., vectorStrength: Optional[Union[Tuple[float, float, float], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a texture deformer for the object.
    The selected objects are the input geometry objects.
    The deformer node name will be returned.

    Args:
        after: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        components: (query) - Returns the components used by the deformer
        deformerTools: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        direction: (create) - Set the deformation direction of texture deformer It can only handle three types: "Normal", "Handle" and "Vector". "Normal"  each vertices use its own normal vector. "Handle"  all vertices use Up vector of the handle. "Vector"  each vertices use RGB color vector strings.
        envelope: (create) - Set the envelope of texture deformer. Envelope determines the percent of deformation. The final result is (color * normal * strength + offset) * envelope
        exclusive: (create, query) - Puts the deformation set in a deform partition.
        frontOfChain: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        name: (create) - Used to specify the name of the node being created.
        offset: (create) - Set the offset of texture deformer. Offset plus a translation on the final deformed vertices.
        parallel: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        pointSpace: (create) - Set the point space of texture deformer. It can only handle three strings: "World", "Local" and "UV". "World"   map world space to color space. "Local"	  map local space to color space. "UV"	  map UV space to color space. strings.
        prune: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        remove: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        selectedComponents: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        split: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        strength: (create) - Set the strength of texture deformer. Strength determines how strong the object is deformed.
        useComponentTags: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
        vectorOffset: (create) - Set the vector offset of texture deformer. Vector offset indicates the offset of the deformation on the vector mode.
        vectorSpace: (create) - Set the vector space of texture deformer. It can only handle three strings: "Object", "World" and "Tangent". "Object"   	use color vector in object space "World"	 	use color vector in world space "Tangent"	use color vector in tangent space strings.
        vectorStrength: (create) - Set the vector strength of texture deformer. Vector strength determines how strong the object is deformed on the vector mode.
    """
    ...


def timeEditor(*args, allClips: Optional[Union[str, bool]] = ..., clipId: Optional[Union[int, bool]] = ..., commonParentTrack: bool = ..., composition: Optional[Union[str, bool]] = ..., drivingClipsForAttr: Optional[Union[str, bool]] = ..., drivingClipsForObj: Optional[Union[Tuple[str, int], bool]] = ..., includeParent: bool = ..., mute: bool = ..., selectedClips: Optional[Union[str, bool]] = ..., topLevelClips: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    General Time Editor commands

    Args:
        allClips: (create) - Return an exhaustive (recursive) list of all clip IDs from the active composition. Arguments may be used to filter the returning result. An empty string will return clip IDs for all clip types:   roster   container   group
        clipId: (create, multiuse) - ID of the clip to be edited.
        commonParentTrack: (create) - Locate the common parent track node and track index of the given clip IDs. Requires a list of clip IDs to be specified using the clipId flag. The format of the returned string is "track_node:track_index". If the clips specified are on the same track node but in different track indexes, only the track node will be returned.
        composition: (create) - A flag to use in conjunction with -dca/drivingClipsForObj to indicate the name of composition to use. By default if this flag is not provided, current active composition will be used.
        drivingClipsForAttr: (create) - Return a list of clips driving the specified attribute(s). If the composition is not specified, current active composition will be used.
        drivingClipsForObj: (create) - Return a list of clips driving the specified object(s) with an integer value indicating the matching mode. If no object is specified explicitly, the selected object(s) will be used. Objects that cannot be driven by clips are ignored. If the composition is not specified, current active composition will be used. Default match mode is 0.  0: Include only the clip that has an exact match 1: Include any clip that contains all of the specified objects 2: Include any clip that contains any of the specified objects 3: Include all clips that do not include any of the specified objects
        includeParent: (create) - A toggle flag to use in conjunction with -dca/drivingClipsForObj. When toggled, parent clip is included in selection (the entire hierarchy will be selected).
        mute: (create, query) - Mute/unmute Time Editor.
        selectedClips: (create) - Return a list of clip IDs of currently selected Time Editor clips. Arguments may be used to filter the returning result. An empty string will return clip IDs for all clip types:   roster   container   group
        topLevelClips: (create) - Return a list of all top-level clip IDs from the active composition. Arguments may be used to filter the returning result. An empty string will return clip IDs for all clip types:   roster   container   group
    """
    ...


def timeEditorAnimSource(*args, addSource: str = ..., apply: bool = ..., bakeToAnimSource: str = ..., calculateTiming: bool = ..., copyAnimation: bool = ..., drivenClips: bool = ..., export: str = ..., isUnique: bool = ..., removeSource: str = ..., targetIndex: Optional[Union[str, bool]] = ..., targets: bool = ..., addObjects: Optional[Union[str, bool]] = ..., addRelatedKG: bool = ..., addSelectedObjects: bool = ..., attribute: Optional[Union[str, bool]] = ..., exclusive: bool = ..., importAllFbxTakes: bool = ..., importFbx: Optional[Union[str, bool]] = ..., importFbxTakes: Optional[Union[str, bool]] = ..., importMayaFile: Optional[Union[str, bool]] = ..., importOption: str = ..., importPopulateOption: str = ..., importedContainerNames: Optional[Union[str, bool]] = ..., includeRoot: bool = ..., populateImportedAnimSources: Optional[Union[str, bool]] = ..., poseClip: bool = ..., recursively: bool = ..., removeSceneAnimation: bool = ..., showAnimSourceRemapping: bool = ..., takeList: Optional[Union[str, bool]] = ..., takesToImport: Optional[Union[str, bool]] = ..., type: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Commands for managing animation sources.

    Args:
        addSource: (edit) - Add single new target attribute with its animation.
        apply: (edit) - Connect anim source's animation directly to the target objects. If the Time Editor is not muted, connect to scene storage instead.
        bakeToAnimSource: (edit) - Create a new anim source with the same animation as this anim source. All non-curve inputs will be baked down, whereas curve sources will be shared.
        calculateTiming: (edit, query) - Adjust start/duration when adding/removing sources. If query it returns the [start,duration] pair.
        copyAnimation: (edit) - Copy animation when adding source.
        drivenClips: (query) - Return all clips driven by the given anim source.
        export: (edit) - Export given anim source and the animation curves to a specified Maya file.
        isUnique: (query) - Return true if the anim source node is only driving a single clip.
        removeSource: (edit) - Remove single attribute.
        targetIndex: (query) - Get target index.
        targets: (query) - Get a list of all targets in this anim source.
        addObjects: (create, edit, query) - Populate the given object(s) and their attributes to anim source to Time Editor. For multiple object, pass each name separated by semicolon. In query mode, return the number of attributes that will be populated given the flags, along with the animation's first and last frames for the given object(s). Similar to -addSelectedObjects flag but acts on given object(s) instead. This flag will override the flag -addSelectedObjects.
        addRelatedKG: (create, edit, query) - During population, determine if associated keying groups should be populated or not. Normally used for populating HIK. By default the value is false.
        addSelectedObjects: (create, edit, query) - Populate the currently selected objects and their attributes to anim source or Time Editor. In query mode, return the number of attributes that will be populated given the flags, along with the animation's first and last frames.
        attribute: (create, edit, multiuse) - Populate a specific attribute on a object.
        exclusive: (create, edit) - Populate all types of animation sources which are not listed by "type" Flag.
        importAllFbxTakes: (create) - Import all FBX takes into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).
        importFbx: (create) - Import an animation from FBX file into the new anim source (for timeEditorAnimSource command) or new container (for timeEditorClip command).
        importFbxTakes: (create) - Import multiple FBX takes (separated by semicolons) into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).
        importMayaFile: (create) - Import an animation from Maya file into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).
        importOption: (edit) - Option for importing animation source. Specify either 'connect' or 'generate'. connect:  Only connect with nodes already existing in the scene.                   Importing an animation source that does not match with any element                   of the current scene will not create any clip.                   (connect is the default mode). generate: Import everything and generate new nodes for items not existing in the scene.
        importPopulateOption: (edit) - Option for population when importing.
        importedContainerNames: (create) - Internal use only. To be used along with populateImportedAnimSources to specify names for the created containers.
        includeRoot: (create, edit) - Populate transform (Translate, Rotate, Scale) of hierarchy root nodes.
        populateImportedAnimSources: (create) - Internal use only. Populate the Time Editor with clips using the Animation Sources specified (use ; as a delimiter for multiple anim sources).
        poseClip: (create) - Populate as pose clip with current attribute values.
        recursively: (create, edit) - Populate selection recursively, adding all the children.
        removeSceneAnimation: (create, edit) - If true, remove animation from scene when creating clips or anim sources. Only Time Editor will drive the removed scene animation.
        showAnimSourceRemapping: (create) - Show a remapping dialog when the imported anim source attributes do not match the scene attributes.
        takeList: (create) - Internal use only. To be used along with populateImportedAnimSources to specify the imported take names.
        takesToImport: (create) - Internal use only. To be used along with populateImportedAnimSources to specify the imported take indices.
        type: (create, edit, multiuse, query) - Only populate the specified type of animation source.
    """
    ...


def timeEditorBakeClips(*args, bakeToAnimSource: Optional[Union[str, bool]] = ..., bakeToClip: Optional[Union[str, bool]] = ..., clipId: Optional[Union[int, bool]] = ..., combineLayers: bool = ..., forceSampling: bool = ..., keepOriginalClip: bool = ..., path: Optional[Union[str, bool]] = ..., sampleBy: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., targetTrackIndex: Optional[Union[int, bool]] = ..., targetTracksNode: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to bake Time Editor clips and to blend them into a single clip.

    Args:
        bakeToAnimSource: (create) - Bake/merge the selected clips into the animation source.
        bakeToClip: (create) - Bake/merge the selected clips into a clip.
        clipId: (create, multiuse) - Clip IDs of the clips to bake.
        combineLayers: (create) - Combine the layers of the input clip.
        forceSampling: (create) - Force sampling on the whole time range when baking.
        keepOriginalClip: (create) - Keep the source clips after baking.
        path: (create, multiuse) - Full path of clips on which to operate. For example: composition1|track1|group; composition1|track1|group|track2|clip1.
        sampleBy: (create) - Sampling interval when baking crossfades and timewarps.
        targetTrackIndex: (create) - Specify the target track when baking containers. If targetTrackIndex is specified, the track index within the specified node is used. If targetTrackIndex is not specified or is the default value (-1), the track index within the current node is used. If targetTrackIndex is -2, a new track will be created.
        targetTracksNode: (create) - Target tracks node when baking containers.
    """
    ...


def timeEditorClip(*args, absolute: bool = ..., addAttribute: str = ..., allowShrinking: bool = ..., animSource: Optional[Union[str, bool]] = ..., audio: Optional[Union[str, bool]] = ..., blendMode: Optional[Union[int, bool]] = ..., children: Optional[Union[int, bool]] = ..., clipAfter: bool = ..., clipBefore: bool = ..., clipDataType: bool = ..., clipId: Optional[Union[int, bool]] = ..., clipIdFromNodeName: Optional[Union[int, bool]] = ..., clipIdFromPath: bool = ..., clipNode: bool = ..., clipPath: bool = ..., copyClip: bool = ..., crossfadeMode: Optional[Union[int, bool]] = ..., crossfadePlug: bool = ..., curveTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., defaultGhostRoot: bool = ..., drivenAttributes: bool = ..., drivenClipsBySource: Optional[Union[str, bool]] = ..., drivenObjects: bool = ..., drivenRootObjects: bool = ..., drivingSources: Optional[Union[str, bool]] = ..., duplicateClip: bool = ..., duration: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., emptySource: bool = ..., endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., existingOnly: bool = ..., exists: bool = ..., explode: int = ..., exportAllClips: bool = ..., exportFbx: str = ..., extend: bool = ..., extendParent: bool = ..., ghost: bool = ..., ghostRootAdd: str = ..., ghostRootRemove: str = ..., group: bool = ..., holdEnd: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., holdStart: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., importTakeDestination: Optional[Union[int, bool]] = ..., isContainer: bool = ..., listUserGhostRoot: bool = ..., loopEnd: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., loopStart: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., minClipDuration: bool = ..., modifyAnimSource: bool = ..., moveClip: Union[float, Tuple[float, float]] = ..., mute: bool = ..., name: Optional[Union[str, bool]] = ..., parent: int = ..., parentClipId: Optional[Union[int, bool]] = ..., parentGroupId: bool = ..., pasteClip: Union[float, Tuple[float, float]] = ..., path: str = ..., preserveAnimationTiming: bool = ..., razorClip: Union[float, Tuple[float, float]] = ..., remap: Tuple[str, str] = ..., remapNamespace: Optional[Union[Tuple[str, str], bool]] = ..., remapSource: Tuple[str, str] = ..., remappedSourceAttrs: bool = ..., remappedTargetAttrs: bool = ..., removeAttribute: str = ..., removeClip: bool = ..., removeCrossfade: bool = ..., removeWeightCurve: bool = ..., resetTiming: bool = ..., resetTransition: bool = ..., ripple: bool = ..., rootClipId: int = ..., rootPath: str = ..., scaleEnd: Union[float, Tuple[float, float]] = ..., scalePivot: Union[float, Tuple[float, float]] = ..., scaleStart: Union[float, Tuple[float, float]] = ..., setKeyframe: str = ..., speedRamping: Optional[Union[int, bool]] = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., timeWarp: bool = ..., timeWarpCurve: bool = ..., timeWarpType: Optional[Union[int, bool]] = ..., track: Optional[Union[str, bool]] = ..., tracksNode: bool = ..., transition: bool = ..., trimEnd: Union[float, Tuple[float, float]] = ..., trimStart: Union[float, Tuple[float, float]] = ..., truncated: bool = ..., uniqueAnimSource: bool = ..., userGhostRoot: bool = ..., weightCurve: bool = ..., zeroKeying: bool = ..., addObjects: Optional[Union[str, bool]] = ..., addRelatedKG: bool = ..., addSelectedObjects: bool = ..., attribute: Optional[Union[str, bool]] = ..., exclusive: bool = ..., importAllFbxTakes: bool = ..., importFbx: Optional[Union[str, bool]] = ..., importFbxTakes: Optional[Union[str, bool]] = ..., importMayaFile: Optional[Union[str, bool]] = ..., importOption: str = ..., importPopulateOption: str = ..., importedContainerNames: Optional[Union[str, bool]] = ..., includeRoot: bool = ..., populateImportedAnimSources: Optional[Union[str, bool]] = ..., poseClip: bool = ..., recursively: bool = ..., removeSceneAnimation: bool = ..., showAnimSourceRemapping: bool = ..., takeList: Optional[Union[str, bool]] = ..., takesToImport: Optional[Union[str, bool]] = ..., type: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command edits/queries Time Editor clips.

    Args:
        absolute: (query) - This flag is used in conjunction with other timing flags like -s/start, -d/duration, -ed/end, etc. to query (global) absolute time.
        addAttribute: (edit, multiuse) - Add new attribute to the clip.
        allowShrinking: (edit) - When extending clip, allow shrinking.
        animSource: (create, edit, query) - Populate based on animation source.
        audio: (create) - Create a clip with audio inside.
        blendMode: (edit, query) - Set the blending mode for the clips specified with the -clipId flags:  0 : normal          - absolute blend 1 : additive        - relative blend
        children: (query) - Get children clip IDs.
        clipAfter: (query) - Get the clip ID of the next clip.
        clipBefore: (query) - Get the clip ID of the previous clip.
        clipDataType: (query) - Query the type of data being driven by the given clip ID. Return values are:  0 : Animation       - Clip drives animation curves 1 : Audio           - Clip drives audio 3 : Group           - Clip is a group
        clipId: (create, edit, multiuse) - ID of the clip to be edited.
        clipIdFromNodeName: (query) - Get clip ID from clip node name.
        clipIdFromPath: (query) - Flag for querying the clip ID given the path. Clip path is a vertical-bar-delimited string to indicate a hierarchical structure of a clip. Please refer to the hierarchical path in outliner to see how it is represented. For example: composition1|track1|clip1 Note: To specify the path, this flag must appear before -query flag.
        clipNode: (query) - Flag for querying the name of the clip node.
        clipPath: (query) - Flag for querying the path given the clip ID. Clip path is a vertical bar delimited string to indicate a hierarchical structure of a clip. Please refer to the hierarchical path in outliner to see how it is represented. For example: composition1|track1|clip1. Note: If the clip is not connected to any track, it will return empty string.
        copyClip: (edit) - Get the selected clip IDs and store them in a list that could be used for pasting.
        crossfadeMode: (edit, query) - Set the crossfading mode between two clips that lie on the same track, and that are specified with the -clipId flags:  0 : linear          - Two clips are blended with a constant ratio 1 : step            - Left clip keeps its value until the middle of the crossfading region and then right clip's value is used 2 : hold left       - Use only left clip's value 3 : hold right      - Use only right clip's value 4 : custom          - User defined crossfade curve 5 : custom (spline) - User defined crossfade curve with spline preset
        crossfadePlug: (query) - Get plug path for a custom crossfade curve between 2 clips.
        curveTime: (query) - Query the curve local time in relation to the given clip.
        defaultGhostRoot: (edit, query) - Edit or query default ghost root variable. Determine whether to use the default ghost root (object driven by clip).
        drivenAttributes: (query) - Return a list of attributes driven by a clip.
        drivenClipsBySource: (query) - Returns the clips driven by the given source. Can filter the return result by the specified type, like animCurve, expression, constraint, etc. This flag must come before the -query flag.
        drivenObjects: (query) - Return an array of strings consisting of the names of all objects driven by the current clip and its children clips.
        drivenRootObjects: (query) - Return an array of strings consisting of the names of all root objects driven by this clip and its children clips.
        drivingSources: (query) - Return all sources driving the given clip. Can filter the return result by the specified type, like animCurve, expression, constraint, etc. If used after the -query flag (without an argument), the command returns all sources driving the given clip. To specify the type, this flag must appear before the -query flag. 			In query mode, this flag can accept a value.
        duplicateClip: (edit) - Duplicate clip into two clips with the same timing info.
        duration: (create, query) - Relative duration of the new clip.
        emptySource: (create) - Create a clip with an empty source.
        endTime: (query) - Query the relative end time of the clip.
        existingOnly: (edit) - This flag can only be used in edit mode, in conjunction with the animSource flag. Retain the animSource flag functionality but only bind attributes that are already part of the clip. It does not attempt to populate unbound source attributes to their default destination.
        exists: (query) - Return true if the specified clip exists.
        explode: (edit) - Reparent all tracks and their clips within a group out to its parent track node and remove the group.
        exportAllClips: (edit) - When used with the ef/exportFbx flag, export all clips.
        exportFbx: (edit) - Export currently selected clips to FBX files.
        extend: (edit) - Extend the clip to encompass all children.
        extendParent: (edit) - Extend parent to fit this clip.
        ghost: (edit, query) - Enable/disable ghosting for the specified clip.
        ghostRootAdd: (edit, multiuse) - Add path to specified node as a custom ghost root.
        ghostRootRemove: (edit, multiuse) - Remove path to specified node as a custom ghost root.
        group: (create) - Specify if the new container should be created as a group, containing other specified clips.
        holdEnd: (edit, query) - Hold clip's end to time.
        holdStart: (edit, query) - Hold clip's start to time.
        importTakeDestination: (create) - Specify how to organize imported FBX takes: 0 - Import takes into a group (default) 1 - Import takes into multiple compositions 2 - Import takes as a sequence of clips
        isContainer: (query) - Indicate if given clip ID is a container.
        listUserGhostRoot: (query) - Get user defined ghost root object for indicated clips.
        loopEnd: (edit, query) - Loop clip's end to time.
        loopStart: (edit, query) - Loop clip's start to time.
        minClipDuration: (query) - Returns the minimum allowed clip duration.
        modifyAnimSource: (create, edit) - When populating, automatically modify Anim Source without asking the user.
        moveClip: (edit) - Move clip by adding delta to its start time.
        mute: (edit, query) - Mute/Unmute the clip given a clip ID. In query mode, return the muted state of the clip. Clips muted by soloing are not affected by this flag.
        name: (edit, query) - Name of the clip. A clip will never have an empty name. If an empty string is provided, it will be replaced with "_".
        parent: (edit) - Specify group/object parent ID.
        parentClipId: (create, query) - Specify the parent clip ID of a clip to be created.
        parentGroupId: (query) - Return the parent group ID of the given clip.
        pasteClip: (edit) - Paste clip to the given time and track. Destination track is required to be specified through the track flag in the format "tracksNode:trackIndex". A trackIndex of -1 indicates that a new track will be created.
        path: (edit, multiuse) - Full path of the clip to be edited. For example: composition1|track1|clip1. 			In query mode, this flag can accept a value.
        preserveAnimationTiming: (create) - When used with the population command, it ensures the animation is offset within a clip in such way that it matches its original scene timing, regardless of the new clip's position.
        razorClip: (edit) - Razor clip into two clips at the specified time.
        remap: (edit) - Change animation source for a given clip item to a new one, specified by the target path. This removes all clips for the roster item and creates new clips from the Anim Source for the new target path.
        remapNamespace: (create, multiuse) - Remap namespace(s). Can only be used in create mode, in conjunction with the -importFbx/fbx, -importMayaFile/mf, or -attribute/at flags. This flag will replace any occurrences of a given namespace to an alternate specified namespace.  It takes in two string arguments. The first argument specifies the namespace to replace. The second argument specifies the replacement namespace. This flag cannot be used in conjunction with the -sar/showAnimSourceRemapping flag. Note that a track must be specified, and  must exist prior to invoking the timeEditorClip command with the -remapNamespace flag.
        remapSource: (edit) - Set animation source to be remapped for a given clip item to new one, specified by the target path.
        remappedSourceAttrs: (query) - Return an array of attribute indices and names of the source attributes of a remapped clip.
        remappedTargetAttrs: (query) - Return an array of attribute indices and names of the target attributes of a remapped clip.
        removeAttribute: (edit, multiuse) - Remove attribute from the clip.
        removeClip: (edit) - Remove clip of specified ID.
        removeCrossfade: (edit) - Remove custom crossfade between two clips specified by -clipId flags.
        removeWeightCurve: (create, edit, query) - Remove the weight curve connected to the clip.
        resetTiming: (edit) - Reset start and duration of a clip with the given clip ID to the values stored in its Anim Source.
        resetTransition: (edit) - Reset transition intervals between specified clips.
        ripple: (edit) - Apply rippling to a clip operation.
        rootClipId: (edit) - ID of the root clip. It is used together with various clip editing flags. When used, the effect of clip editing and its parameters will be affected by the given root clip. For example, moving a clip under the group root (usually in group tab view) will be performed in the local time space of the group root.
        rootPath: (edit) - Path of the root clip. It is used together with various clip editing flags. When used, the effect of clip editing and its parameters will be affected by the given root clip. For example, moving a clip under the group root (usually in group tab view) will be performed in the local time space of the group root.
        scaleEnd: (edit) - Scale the end time of the clip to the given time.
        scalePivot: (edit) - Scale the time of the clip based on the pivot. This should be used together with -scs/scaleStart or -sce/scaleEnd.
        scaleStart: (edit) - Scale the start time of the clip to the given time.
        setKeyframe: (edit, multiuse) - Set keyframe on a specific clip for a specified attribute.
        speedRamping: (edit, query) - To control the playback speed of the clip by animation curve:  1 : create - Attach a speed curve and a time warp curve to the clip to control the playback speed 2 : edit - Open the Graph editor to edit the speed curve 3 : enable - Create a time warp curve from current speed curve and attach to clip 4 : disable - Remove the time warp curve from clip 5 : delete - Delete the attached speed curve and time warp curve 6 : reset - Reset the speed curve back to the default 7 : convert to speed curve from time warp 8 : convert to time warp from speed curve  In query mode, return true if a speed curve is attached to the clip.
        startTime: (create, query) - Relative start time of the new clip.
        timeWarp: (query) - Return true if the clip is being warped by the speed curve. If no speed curve is attached to the clip, it will always return false.
        timeWarpCurve: (query) - Returns the name of the time warp curve connected to the clip.
        timeWarpType: (edit, query) - Time warp mode:  0: remapping - Connected time warp curve performs frame by frame remapping 1: speed curve - Connected time warp curve acts as a speed curve  In query mode, return time warp mode of a clip.
        track: (create, edit, query) - The new clip container will be created on the track in the format "trackNode:trackNumber", or on a track path, for example "composition1|track1". In query mode, return a string containing the track number and tracks node of the given clip ID. In create mode, if the track number is '-1' or not given at all, then a new track will be created. For example: "trackNode:-1"; "composition1|".
        tracksNode: (query) - Get tracks node if specified clip is a group clip.
        transition: (edit) - Create transition intervals between specified clips.
        trimEnd: (edit) - Trim the end time of the clip to the given time.
        trimStart: (edit) - Trim the start time of the clip to the given time.
        truncated: (query) - This flag is used in conjunction with other timing flags like -s/start, -d/duration, -ed/end, etc. to query (global) truncated time.
        uniqueAnimSource: (edit) - If a given clip is sharing its Anim Source node with another clip, make the Anim Source of this clip unique.
        userGhostRoot: (edit, query) - Edit or query custom ghost root variable. Determine whether to use user defined ghost root.
        weightCurve: (create, edit, query) - In edit mode, create a weight curve and connect it to the clip. In query mode, return the name of the weight curve connected to the clip.
        zeroKeying: (edit) - A toggle flag to use in conjunction with k/setKeyframe, set the value of the key frame(s) to be keyed to zero.
        addObjects: (create, edit, query) - Populate the given object(s) and their attributes to anim source to Time Editor. For multiple object, pass each name separated by semicolon. In query mode, return the number of attributes that will be populated given the flags, along with the animation's first and last frames for the given object(s). Similar to -addSelectedObjects flag but acts on given object(s) instead. This flag will override the flag -addSelectedObjects.
        addRelatedKG: (create, edit, query) - During population, determine if associated keying groups should be populated or not. Normally used for populating HIK. By default the value is false.
        addSelectedObjects: (create, edit, query) - Populate the currently selected objects and their attributes to anim source or Time Editor. In query mode, return the number of attributes that will be populated given the flags, along with the animation's first and last frames.
        attribute: (create, edit, multiuse) - Populate a specific attribute on a object.
        exclusive: (create, edit) - Populate all types of animation sources which are not listed by "type" Flag.
        importAllFbxTakes: (create) - Import all FBX takes into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).
        importFbx: (create) - Import an animation from FBX file into the new anim source (for timeEditorAnimSource command) or new container (for timeEditorClip command).
        importFbxTakes: (create) - Import multiple FBX takes (separated by semicolons) into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).
        importMayaFile: (create) - Import an animation from Maya file into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).
        importOption: (edit) - Option for importing animation source. Specify either 'connect' or 'generate'. connect:  Only connect with nodes already existing in the scene.                   Importing an animation source that does not match with any element                   of the current scene will not create any clip.                   (connect is the default mode). generate: Import everything and generate new nodes for items not existing in the scene.
        importPopulateOption: (edit) - Option for population when importing.
        importedContainerNames: (create) - Internal use only. To be used along with populateImportedAnimSources to specify names for the created containers.
        includeRoot: (create, edit) - Populate transform (Translate, Rotate, Scale) of hierarchy root nodes.
        populateImportedAnimSources: (create) - Internal use only. Populate the Time Editor with clips using the Animation Sources specified (use ; as a delimiter for multiple anim sources).
        poseClip: (create) - Populate as pose clip with current attribute values.
        recursively: (create, edit) - Populate selection recursively, adding all the children.
        removeSceneAnimation: (create, edit) - If true, remove animation from scene when creating clips or anim sources. Only Time Editor will drive the removed scene animation.
        showAnimSourceRemapping: (create) - Show a remapping dialog when the imported anim source attributes do not match the scene attributes.
        takeList: (create) - Internal use only. To be used along with populateImportedAnimSources to specify the imported take names.
        takesToImport: (create) - Internal use only. To be used along with populateImportedAnimSources to specify the imported take indices.
        type: (create, edit, multiuse, query) - Only populate the specified type of animation source.
    """
    ...


def timeEditorClipLayer(*args, addAttribute: str = ..., addLayer: str = ..., addObject: str = ..., allLayers: bool = ..., attribute: str = ..., attributeKeyable: Optional[Union[str, bool]] = ..., clipId: int = ..., index: int = ..., keySiblings: bool = ..., layerId: int = ..., layerName: Optional[Union[str, bool]] = ..., mode: int = ..., mute: bool = ..., name: bool = ..., path: str = ..., removeAttribute: str = ..., removeLayer: bool = ..., removeObject: str = ..., resetSolo: bool = ..., setKeyframe: bool = ..., solo: bool = ..., zeroKeying: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Time Editor clip layers commands

    Args:
        addAttribute: (edit) - Add given plug to a layer with a supplied layerId.
        addLayer: (edit) - Add a new layer with a given name.
        addObject: (edit) - Add given object with all its attributes in the clip to a layer with a supplied layerId.
        allLayers: (query) - Return all layers given clip ID.
        attribute: (edit, multiuse) - The attribute path to key.
        attributeKeyable: (query) - Return whether specified attribute is keyable.
        clipId: (edit) - ID of the clip this layer command operates on. 			In query mode, this flag can accept a value.
        index: (edit) - Layer index, used when adding new layer at specific location in the stack.
        keySiblings: (edit) - If set to true, additional attributes might be keyed while keying to achieve desired result.
        layerId: (edit) - Layer ID used in conjunction with other edit flags. 			In query mode, this flag can accept a value.
        layerName: (edit, query) - Edit layer name. In query mode, return the layer name given its layer ID and clip ID.
        mode: (edit) - To control the playback speed of the clip by animation curve:  0 : additive 1 : additive override 2 : override 3 : override passthrough
        mute: (edit) - Mute/unmute a layer given its layer ID and clip ID.
        name: (query) - Query the attribute name of a layer given its layer ID and clip ID.
        path: (edit) - Full path of a layer or a clip on which to operate. For example: composition1|track1|clip1|layer1; composition1|track1|group|track1|clip1. 			In query mode, this flag can accept a value.
        removeAttribute: (edit) - Remove given plug from a layer with a supplied layerId.
        removeLayer: (edit) - Remove layer with an ID.
        removeObject: (edit) - Remove given object with all its attributes in the clip to a layer with a supplied layerId.
        resetSolo: (edit) - Unsolo all soloed layers in a given clip ID.
        setKeyframe: (edit) - Set keyframe on specified attributes on specified layer of a clip. Use -clipId to indicate the specified clip. Use -layerId to indicate the specified layer of the clip. Use -attribute to indicate the specified attributes (if no attribute flag is used, all attribute will be keyed). Use -zeroKeying to indicate that zero offset from original animation should be keyed.
        solo: (edit) - Solo/unsolo a layer given its layers ID and clip ID.
        zeroKeying: (edit) - Indicate if the key to set should be zero offset from original animation.
    """
    ...


def timeEditorClipOffset(*args, applyToAllRoots: bool = ..., clipId: Optional[Union[int, bool]] = ..., matchClipId: Optional[Union[int, bool]] = ..., matchDstTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., matchObj: Optional[Union[str, bool]] = ..., matchOffsetRot: bool = ..., matchOffsetTrans: bool = ..., matchPath: Optional[Union[str, bool]] = ..., matchRotOp: Optional[Union[int, bool]] = ..., matchSrcTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., matchTransOp: Optional[Union[int, bool]] = ..., offsetTransform: bool = ..., path: Optional[Union[str, bool]] = ..., resetMatch: Optional[Union[int, bool]] = ..., resetMatchPath: Optional[Union[str, bool]] = ..., rootObj: Optional[Union[str, bool]] = ..., upVectorX: Optional[Union[float, bool]] = ..., upVectorY: Optional[Union[float, bool]] = ..., upVectorZ: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to compute an offset to apply on a source clip in order to
    automatically align it to a destination clip at a specified match element.
    For this command to work, offset objects must be specified for the character.

    Args:
        applyToAllRoots: (create) - Apply root offsets to all roots in the population. However, if the root objects are specified by rootObj flag, this flag will be ignored.
        clipId: (create, edit, multiuse) - ID of the clip to be edited.
        matchClipId: (create) - Specify the ID of a clip to match.
        matchDstTime: (create) - Specify the time on target clip.
        matchObj: (create) - Specify the object to match.
        matchOffsetRot: (query) - Get the rotation of the match offset matrix.
        matchOffsetTrans: (query) - Get the translation of the match offset matrix.
        matchPath: (create) - Full path of the clip to match. For example: composition1|track1|Group|track2|clip1
        matchRotOp: (create) - Specify the option for matching rotation.  0 : full - All rotation components are matched 1 : Y    - Y component is matched 2 : none - No rotation matching
        matchSrcTime: (create) - Specify the time on source clip.
        matchTransOp: (create) - Specify the option for matching translation.  0 : full - All translation components are matched 1 : XZ   - X and Z components are matched 2 : none - No translation matching
        offsetTransform: (create, query) - Create/get an offset for the specified clip.
        path: (create, edit, multiuse) - Full path of a clip to be edited. For example: composition1|track1|group; composition1|track1|group|track2|clip1. 			In query mode, this flag can accept a value.
        resetMatch: (create) - Specify clip ID to remove offset.
        resetMatchPath: (create) - Specify clip's full path to remove offset. For example: composition1|track1|Group|track2|clip1
        rootObj: (create, edit, multiuse, query) - Specify the root objects. If specified, this flag will take precedence over applyToAllRoots flag. When used in query mode, returns list of roots defined for the relocator.
        upVectorX: (create) - Specify the X coordinate of the up vector.
        upVectorY: (create) - Specify the Y coordinate of the up vector.
        upVectorZ: (create) - Specify the Z coordinate of the up vector.
    """
    ...


def timeEditorComposition(*args, active: bool = ..., allCompositions: bool = ..., createTrack: bool = ..., delete: bool = ..., duplicateFrom: Optional[Union[str, bool]] = ..., rename: Tuple[str, str] = ..., tracksNode: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Commands related to composition management inside Time Editor.

    Args:
        active: (edit, query) - Query or edit the active composition.
        allCompositions: (query) - Return all compositions inside Time Editor.
        createTrack: (create) - Create a default track when creating a new composition.
        delete: (edit, query) - Delete the composition.
        duplicateFrom: (create) - Duplicate the composition.
        rename: (edit) - Rename the composition of the first name to the second name.
        tracksNode: (query) - Query the tracks node of a composition.
    """
    ...


def timeEditorPanel(*args, activeClipEditMode: Optional[Union[int, bool]] = ..., activeTabRootClipId: bool = ..., activeTabTime: bool = ..., activeTabView: Optional[Union[int, bool]] = ..., autoFit: Optional[Union[str, bool]] = ..., autoFitTime: Optional[Union[str, bool]] = ..., control: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., displayActiveKeyTangents: str = ..., displayActiveKeys: str = ..., displayInfinities: str = ..., displayKeys: str = ..., displayTangents: str = ..., displayValues: str = ..., docTag: Optional[Union[str, bool]] = ..., exists: bool = ..., filter: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., groupIdForTabView: Optional[Union[int, bool]] = ..., highlightConnection: Optional[Union[str, bool]] = ..., keyingTarget: Optional[Union[int, bool]] = ..., layerId: int = ..., lockMainConnection: bool = ..., lookAt: str = ..., mainListConnection: Optional[Union[str, bool]] = ..., menu: Optional[Union[str, bool]] = ..., minClipWidth: Optional[Union[int, bool]] = ..., panel: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., selectionConnection: Optional[Union[str, bool]] = ..., setToPrevClipEditMode: bool = ..., snapTime: Optional[Union[str, bool]] = ..., snapToClip: bool = ..., snapToFrame: bool = ..., snapTolerance: Optional[Union[int, bool]] = ..., snapValue: Optional[Union[str, bool]] = ..., stateString: bool = ..., tabView: int = ..., timeCursor: bool = ..., unParent: bool = ..., unlockMainConnection: bool = ..., updateMainConnection: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Time Editor - non-linear animation editor

    Args:
        activeClipEditMode: (edit, query) - Set the appropriate clip edit mode for the editor.  0: Default Mode 1: Trim Mode 2: Scale Mode 3: Loop Mode 4: Hold Mode
        activeTabRootClipId: (query) - Get the clip id for which current active tab has been opened. In case of main tab, this will return -1 meaning there is no root clip.
        activeTabTime: (query) - Get current time displayed inside the active tab. This will be global time in case of the main tab and local time for others.
        activeTabView: (edit, query) - Get/set the index of the tab widget's (active) visible tab. Note: the index is zero-based.
        autoFit: (edit, query) - on | off | tgl Auto fit-to-view.
        autoFitTime: (edit, query) - on | off | tgl Auto fit-to-view along the time axis, as well.
        control: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        displayActiveKeyTangents: (edit) - on | off | tgl Display active key tangents in the editor.
        displayActiveKeys: (edit) - on | off | tgl Display active keys in the editor.
        displayInfinities: (edit) - on | off | tgl Display infinities in the editor.
        displayKeys: (edit) - on | off | tgl Display keyframes in the editor.
        displayTangents: (edit) - on | off | tgl Display tangents in the editor.
        displayValues: (edit) - on | off | tgl Display active keys and tangents values in the editor.
        docTag: (create, edit, query) - Attaches a tag to the editor.
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        filter: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        forceMainConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        groupIdForTabView: (query) - Get the group clip id for the given tab view index. To specify the tab index, this flag must appear before the -query flag.       In query mode, this flag needs a value.
        highlightConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        keyingTarget: (edit, query) - Set keying target to specified clip ID. If keying into layer, '-layer' flag must be used. In query mode, the clip id is omitted, and the name of the keying target will be returned.
        layerId: (edit) - Indicate layer ID of keying target.
        lockMainConnection: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        lookAt: (edit) - all | selected | currentTime FitView helpers.
        mainListConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        menu: (create) - Specify a script to be run when the editor is created.  The function will be passed one string argument which is the new editor's name.
        minClipWidth: (edit, query) - Set the minimum clip width.
        panel: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        selectionConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        setToPrevClipEditMode: (edit) - Revert to previous clip edit mode.
        snapTime: (edit, query) - none | integer | keyframe Keyframe move snap in time.
        snapToClip: (edit, query) - Enable/Disable snap-to-clip option in Time Editor while manipulating and drag-and-drop clips. When snapToClip is on all manipulated timing will land on a clip boundary if it is close to it.
        snapToFrame: (edit, query) - Enable/Disable snap-to-frame option in Time Editor while manipulating and drag-and-drop clips. When snapToFrame is on all manipulated timing will land on an exact frame.
        snapTolerance: (edit, query) - Set the tolerance value for snapping.
        snapValue: (edit, query) - none | integer | keyframe Keyframe move snap in values.
        stateString: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        tabView: (edit) - Create a tab view for the given group clip ID.
        timeCursor: (edit, query) - Activate the time cursor in Time Editor for scrubbing.
        unParent: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
    """
    ...


def timeEditorTracks(*args, activeClipWeight: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., activeClipWeightId: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., addTrack: int = ..., allClips: bool = ..., allTracks: bool = ..., allTracksRecursive: bool = ..., composition: bool = ..., path: str = ..., plugIndex: Optional[Union[int, bool]] = ..., removeTrack: int = ..., removeTrackByPath: str = ..., reorderTrack: Tuple[int, int] = ..., resetMute: bool = ..., resetSolo: bool = ..., selectedTracks: bool = ..., trackGhost: bool = ..., trackIndex: Optional[Union[int, bool]] = ..., trackMuted: bool = ..., trackName: Optional[Union[str, bool]] = ..., trackSolo: bool = ..., trackType: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Time Editor tracks commands

    Args:
        activeClipWeight: (query) - Get the clip weight at the specified time.
        activeClipWeightId: (query) - Get the clip ID carrying the active clip weight at the specified time.
        addTrack: (edit) - Add new track at the track index specified. Indices are 0-based. Specify -1 to add the track at the end.
        allClips: (query) - Return a list of clip IDs under the specified track.
        allTracks: (query) - Return a list of strings for all the immediate tracks for the given tracks node in the format "tracksNode:trackIndex".
        allTracksRecursive: (query) - Return a list of strings for all the tracks for the given tracks node, or return a list of strings for all tracks of all tracks nodes in the format "tracksNode:trackIndex". If the given root tracks node is from a composition, this command returns the tracks under that composition, including the tracks within groups that is under the same composition.
        composition: (query) - Return the composition the specified track belongs to.
        path: (edit) - Full path of a track node or a track on which to operate. For example: composition1|track1|group; composition1|track1. 			In query mode, this flag can accept a value.
        plugIndex: (edit, query) - Get the plug index of the specified track.
        removeTrack: (edit, multiuse) - Remove track at given index. It is a multi-use flag.
        removeTrackByPath: (edit, multiuse) - Remove track at given path. It is a multi-use flag. For example: composition1|track1|group|track1;
        reorderTrack: (edit) - Move the track relative to other tracks. The first argument is the track index (0-based). The second argument can be a positive or negative number to indicate the steps to move. Positive numbers move forward and negative numbers move backward.
        resetMute: (create) - Reset all the muted tracks in the active composition.
        resetSolo: (create) - Reset the soloing of all tracks on the active composition.
        selectedTracks: (query) - Return a list of the indices for all the selected tracks for the given tracks node, or return a list of strings for all selected tracks of all tracks nodes in the format "tracksNode:trackIndex".
        trackGhost: (edit, query) - Ghost all clips under track.
        trackIndex: (edit, query) - Specify the track index. This flag is used in conjunction with the other flags. 			In query mode, this flag can accept a value.
        trackMuted: (edit, query) - Return whether the track is muted.
        trackName: (edit, query) - Display name of the track.
        trackSolo: (edit, query) - Return whether the track is soloed.
        trackType: (edit, query) - Specify the track type. Can only be used together with -at/addTrack. Does not work by itself. In query mode, return the integer corresponding to the track type.   0: Animation Track (Default)  1: Audio Track
    """
    ...


def timeWarp(*args, deleteFrame: int = ..., frame: Optional[Union[float, bool]] = ..., g: bool = ..., interpType: Optional[Union[Tuple[int, str], bool]] = ..., moveFrame: Optional[Union[Tuple[int, float], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to create a time warp input to a set of animation curves.

    Args:
        deleteFrame: (edit) - The flag value indicates the 0-based index of the warp frame to delete. This flag can only be used in edit mode.
        frame: (create, edit, multiuse, query) - In create and edit mode, this flag can be used to specify warp frames added to the warp operation. In query mode, this flag returns a list of the frame values where warping occurs. The moveFrame flag command can be used to query the associated warped values.
        g: (create, edit, query) - In create mode, creates a global time warp node which impacts every animated object in the scene. In query mode, returns the global time warp node. Note: only one global time warp can exist in the scene.
        interpType: (create, edit, query) - This flag can be used to set the interpolation type for a given span. Valid interpolation types are linear, easeIn and easeOut. When queried, it returns a string array of the interpolation types for the specified time warp.
        moveFrame: (edit, query) - This flag can be used to move a singular warp frame. The first value specified indicates the 0-based index of the warp frame to move. The second value indicates the new warp frame value. This flag can only be used in edit and query mode. When queried, it returns an array of the warped frame values.
    """
    ...


def ubercam(*args) -> Any:
    r"""
    Use this command to create a "ubercam" with equivalent behavior
    to all cameras used by shots in the sequencer.

    Args:
    """
    ...


def volumeBind(*args, influence: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command for creating and editing volume binding nodes.
    The node is use for storing volume data to define skin weighting data.

    Args:
        influence: (edit, query) - Edit or Query the list of influences connected to the skin cluster.
        name: (create) - Used to specify the name of the node being created.
    """
    ...


def wire(*args, after: bool = ..., afterReference: bool = ..., before: bool = ..., components: bool = ..., crossingEffect: Optional[Union[float, bool]] = ..., deformerTools: bool = ..., dropoffDistance: Optional[Union[Tuple[int, float], bool]] = ..., envelope: Optional[Union[float, bool]] = ..., exclusive: Optional[Union[str, bool]] = ..., frontOfChain: bool = ..., geometry: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., groupWithBase: bool = ..., holder: Optional[Union[Tuple[int, str], bool]] = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., localInfluence: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., parallel: bool = ..., prune: bool = ..., remove: bool = ..., selectedComponents: bool = ..., split: bool = ..., useComponentTags: bool = ..., wire: Optional[Union[str, bool]] = ..., wireCount: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a wire deformer. 
    In the create mode the selection list is treated as the
    object(s) to be deformed, Wires are specified with the -w flag.
    Each wire can optionally have a holder which helps define the
    the regon of the object that is affected by the deformer.

    Args:
        after: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        components: (query) - Returns the components used by the deformer
        crossingEffect: (create, edit, query) - Set the amount of convolution effect. Varies from fully convolved at 0 to a simple additive effect at 1 (which is what you get with the filter off). Default is 0.  This filter should make its way into all blend nodes that deal with combining effects from multiple sources.
        deformerTools: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        dropoffDistance: (create, edit, multiuse, query) - Set the dropoff distance (second parameter) for the wire at index (first parameter).
        envelope: (create, edit, query) - Set the envelope value for the deformer. Default is 1.0
        exclusive: (create, query) - Puts the deformation set in a deform partition.
        frontOfChain: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        groupWithBase: (create) - Groups the wire with the base wire so that they can easily be moved together to create a ripple effect. Default is false.
        holder: (create, edit, multiuse, query) - Set the specified curve or surface (second parameter  as a holder for the wire at index (first parameter).
        ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        localInfluence: (create, edit, query) - Set the local control a wire has with respect to other wires irrespective of whether it is deforming the surface. Varies from no local effect at 0 to full local control at 1. Default is 0.
        name: (create) - Used to specify the name of the node being created.
        parallel: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        prune: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        remove: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        selectedComponents: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        split: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        useComponentTags: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
        wire: (create, edit, multiuse, query) - Specify or query the wire curve name.
        wireCount: (create, edit, query) - Set the number of wires.
    """
    ...


def wrinkle(*args, axis: Optional[Union[Tuple[float, float, float], bool]] = ..., branchCount: Optional[Union[int, bool]] = ..., branchDepth: Optional[Union[int, bool]] = ..., center: Optional[Union[Tuple[float, float, float], bool]] = ..., crease: Optional[Union[str, bool]] = ..., dropoffDistance: Optional[Union[float, bool]] = ..., envelope: Optional[Union[float, bool]] = ..., randomness: Optional[Union[float, bool]] = ..., style: Optional[Union[str, bool]] = ..., thickness: Optional[Union[float, bool]] = ..., uvSpace: Optional[Union[Tuple[float, float, float, float, float], bool]] = ..., wrinkleCount: Optional[Union[int, bool]] = ..., wrinkleIntensity: Optional[Union[float, bool]] = ...) -> Any:
    r"""
    The wrinkle command is used to create a network of wrinkles on a surface.
    It automatically creates a network of wrinkle curves that control a wire
    deformer. The wrinkle curves are attached to a cluster deformer.

    Args:
        axis: (create) - Specifies the plane of the wrinkle.
        branchCount: (create) - Specifies the number of branches per wrinkle. Default is 2.
        branchDepth: (create) - Specifies the depth of the branching. Default is 0.
        center: (create) - Specifies the center of the wrinkle.
        crease: (create, multiuse) - Specifies an existing curve to serve as the wrinkle.
        dropoffDistance: (create) - Specifies the dropoff distance around the center.
        envelope: (create) - The envelope globally attenuates the amount of deformation. Default is 1.0.
        randomness: (create) - Amount of randomness. Default is 0.2.
        style: (create) - Specifies the wrinkle style. Valid values are "radial" or "tangential"
        thickness: (create) - Wrinkle thickness. Default is 1.0.
        uvSpace: (create) - 1/2 length, 1/2 breadth, rotation angle, center u, v definition of a patch in uv space where the wrinkle is to be constructed.
        wrinkleCount: (create) - Specifies the number of wrinkle lines to be generated. Default is 3.
        wrinkleIntensity: (create) - Increasing the intensity makes it more wrinkly. Default is 0.5.
    """
    ...


def writeTake(*args, angle: Optional[Union[str, bool]] = ..., device: Optional[Union[str, bool]] = ..., linear: Optional[Union[str, bool]] = ..., noTime: bool = ..., precision: Optional[Union[int, bool]] = ..., take: Optional[Union[str, bool]] = ..., virtualDevice: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This action writes a take from a device with recorded data to a
    take (.mov) file. The writeTake action can also write the virtual
    definition of a device.
    
    See also: recordDevice, readTake, defineVirtualDevice

    Args:
        angle: (create) - Sets the angular unit used in the take. Valid strings are [deg|degree|rad|radian].  C: The default is the current user angular unit.
        device: (create) - Specifies the device that contains the take. This is a required argument. If the device does not contain a take, the action will fail.
        linear: (create) - Sets the linear unit used in the take. Valid strings are [mm|millimeter|cm|centimeter|m|meter|km|kilometer|in|inch|ft|foot|yd|yard|mi|mile]  C: The default is the current user linear unit.
        noTime: (create) - The take (.mov) file will not contain time stamps.  C: The default is to put time stamps in the take file.
        precision: (create) - Sets the number of digits to the right of the decimal place in the take file. C: The default is 6.
        take: (create) - Write out the take to a file with the specified name.
        virtualDevice: (create) - Writes out the virtual device definition to a mel script with the specified file name.
    """
    ...


