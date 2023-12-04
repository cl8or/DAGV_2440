from typing import Union, Optional, List, Tuple, Any

def aimConstraint(*args, aimVector: Optional[Union[Tuple[float, float, float], bool]] = ..., aim: Optional[Union[Tuple[float, float, float], bool]] = ..., layer: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., maintainOffset: bool = ..., mo: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., offset: Optional[Union[Tuple[float, float, float], bool]] = ..., o: Optional[Union[Tuple[float, float, float], bool]] = ..., remove: bool = ..., rm: bool = ..., skip: Optional[Union[str, bool]] = ..., sk: Optional[Union[str, bool]] = ..., targetList: bool = ..., tl: bool = ..., upVector: Optional[Union[Tuple[float, float, float], bool]] = ..., u: Optional[Union[Tuple[float, float, float], bool]] = ..., weight: Optional[Union[float, bool]] = ..., w: Optional[Union[float, bool]] = ..., weightAliasList: bool = ..., wal: bool = ..., worldUpObject: Optional[Union[str, bool]] = ..., wuo: Optional[Union[str, bool]] = ..., worldUpType: Optional[Union[str, bool]] = ..., wut: Optional[Union[str, bool]] = ..., worldUpVector: Optional[Union[Tuple[float, float, float], bool]] = ..., wu: Optional[Union[Tuple[float, float, float], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        aimVector | aim: (create, edit, query) - Set the aim vector.  This is the vector in local coordinates that points at the target.  If not given at creation time, the default value of (1.0, 0.0, 0.0) is used.
        layer | l: (create, edit) - Specify the name of the animation layer where the constraint should be added.
        maintainOffset | mo: (create) - The offset necessary to preserve the constrained object's initial rotation will be calculated and used as the offset.
        name | n: (create, edit, query) - Sets the name of the constraint node to the specified name.  Default name is constrainedObjectName_constraintType
        offset | o: (create, edit, query) - Sets or queries the value of the offset. Default is 0,0,0.
        remove | rm: (edit) - removes the listed target(s) from the constraint.
        skip | sk: (create, edit, multiuse) - Specify the axis to be skipped. Valid values are "x", "y", "z" and "none". During creation, "none" is the default.
        targetList | tl: (query) - Return the list of target objects.
        upVector | u: (create, edit, query) - Set local up vector.  This is the vector in local coordinates that aligns with the world up vector.  If not given at creation time, the default value of (0.0, 1.0, 0.0) is used.
        weight | w: (create, edit, query) - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
        weightAliasList | wal: (query) - Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
        worldUpObject | wuo: (create, edit, query) - Set the DAG object use for worldUpType "object" and "objectrotation". See worldUpType for greater detail. The default value is no up object, which is interpreted as world space.
        worldUpType | wut: (create, edit, query) - Set the type of the world up vector computation. The worldUpType can have one of 5 values: "scene", "object", "objectrotation", "vector", or "none". If the value is "scene", the upVector is aligned with the up axis of the scene and worldUpVector and worldUpObject are ignored. If the value is "object", the upVector is aimed as closely as possible to the origin of the space of the worldUpObject and the worldUpVector is ignored. If the value is "objectrotation" then the worldUpVector is interpreted as being in the coordinate space of the worldUpObject, transformed into world space and the upVector is aligned as closely as possible to the result. If the value is "vector", the upVector is aligned with worldUpVector as closely as possible and worldUpMatrix is ignored. Finally, if the value is "none" no twist calculation is performed by the constraint, with the resulting "upVector" orientation based previous orientation of the constrained object, and the "great circle" rotation needed to align the aim vector with its constraint. The default worldUpType is "vector".
        worldUpVector | wu: (create, edit, query) - Set world up vector.  This is the vector in world coordinates that up vector should align with. See -wut/worldUpType (below)for greater detail. If not given at creation time, the default value of (0.0, 1.0, 0.0) is used.
    """
    ...


def animCurveEditor(*args, areCurvesSelected: bool = ..., acs: bool = ..., autoFit: Optional[Union[str, bool]] = ..., af: Optional[Union[str, bool]] = ..., autoFitTime: Optional[Union[str, bool]] = ..., aft: Optional[Union[str, bool]] = ..., classicMode: bool = ..., cm: bool = ..., clipTime: Optional[Union[str, bool]] = ..., ct: Optional[Union[str, bool]] = ..., constrainDrag: Optional[Union[int, bool]] = ..., cd: Optional[Union[int, bool]] = ..., control: bool = ..., ctl: bool = ..., curvesShown: bool = ..., cs: bool = ..., curvesShownForceUpdate: bool = ..., csf: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., denormalizeCurvesCommand: Optional[Union[str, bool]] = ..., dcc: Optional[Union[str, bool]] = ..., displayActiveKeyTangents: str = ..., dat: str = ..., displayActiveKeys: str = ..., dak: str = ..., displayInfinities: str = ..., di: str = ..., displayKeys: str = ..., dk: str = ..., displayNormalized: bool = ..., dn: bool = ..., displayTangents: str = ..., dtn: str = ..., displayValues: str = ..., dv: str = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., exists: bool = ..., ex: bool = ..., filter: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., fmc: Optional[Union[str, bool]] = ..., highlightAffectedCurves: bool = ..., hac: bool = ..., highlightConnection: Optional[Union[str, bool]] = ..., hlc: Optional[Union[str, bool]] = ..., keyMinScale: Optional[Union[float, bool]] = ..., kms: Optional[Union[float, bool]] = ..., keyScale: Optional[Union[float, bool]] = ..., ksc: Optional[Union[float, bool]] = ..., keyingTime: Optional[Union[str, bool]] = ..., kt: Optional[Union[str, bool]] = ..., lockMainConnection: bool = ..., lck: bool = ..., lockPlayRangeShades: Optional[Union[str, bool]] = ..., lpr: Optional[Union[str, bool]] = ..., lookAt: str = ..., la: str = ..., mainListConnection: Optional[Union[str, bool]] = ..., mlc: Optional[Union[str, bool]] = ..., menu: Optional[Union[str, bool]] = ..., m: Optional[Union[str, bool]] = ..., normalizeCurvesCommand: Optional[Union[str, bool]] = ..., ncc: Optional[Union[str, bool]] = ..., outliner: Optional[Union[str, bool]] = ..., o: Optional[Union[str, bool]] = ..., panel: Optional[Union[str, bool]] = ..., pnl: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., preSelectionHighlight: bool = ..., psh: bool = ..., renormalizeCurves: bool = ..., rnc: bool = ..., resultSamples: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., rs: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., resultScreenSamples: Optional[Union[int, bool]] = ..., rss: Optional[Union[int, bool]] = ..., resultUpdate: Optional[Union[str, bool]] = ..., ru: Optional[Union[str, bool]] = ..., selectionConnection: Optional[Union[str, bool]] = ..., slc: Optional[Union[str, bool]] = ..., showActiveCurveNames: bool = ..., acn: bool = ..., showBufferCurves: Optional[Union[str, bool]] = ..., sb: Optional[Union[str, bool]] = ..., showCurveNames: bool = ..., scn: bool = ..., showPlayRangeShades: Optional[Union[str, bool]] = ..., spr: Optional[Union[str, bool]] = ..., showResults: Optional[Union[str, bool]] = ..., sr: Optional[Union[str, bool]] = ..., showUpstreamCurves: bool = ..., suc: bool = ..., simpleKeyView: bool = ..., skv: bool = ..., smoothness: Optional[Union[str, bool]] = ..., s: Optional[Union[str, bool]] = ..., snapTime: Optional[Union[str, bool]] = ..., st: Optional[Union[str, bool]] = ..., snapValue: Optional[Union[str, bool]] = ..., sv: Optional[Union[str, bool]] = ..., stackedCurves: bool = ..., sc: bool = ..., stackedCurvesMax: Optional[Union[float, bool]] = ..., scx: Optional[Union[float, bool]] = ..., stackedCurvesMin: Optional[Union[float, bool]] = ..., scm: Optional[Union[float, bool]] = ..., stackedCurvesSpace: Optional[Union[float, bool]] = ..., scs: Optional[Union[float, bool]] = ..., stateString: bool = ..., sts: bool = ..., timelinePositionTop: bool = ..., tlp: bool = ..., unParent: bool = ..., up: bool = ..., unlockMainConnection: bool = ..., ulk: bool = ..., updateMainConnection: bool = ..., upd: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., valueLinesToggle: str = ..., vlt: str = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Edit a characteristic of a graph editor

    Args:
        areCurvesSelected | acs: (query) - Returns a boolean to know if at least one curve is selected in the graph editor.
        autoFit | af: (edit, query) - on | off | tgl Auto fit-to-view.
        autoFitTime | aft: (edit, query) - on | off | tgl Auto fit-to-view along the time axis, as well.
        classicMode | cm: (edit, query) - When on, the graph editor is displayed in "Classic Mode", otherwise "Suites Mode" is used.
        clipTime | ct: (edit, query) - Valid values: "on" "off" Display the clips with their offset and scale applied to the anim curves in the clip.
        constrainDrag | cd: (create, edit, query) - Constrains all Graph Editor animation curve drag operations to either the X-axis, the Y-axis, or to neither of those axes. Values to supply are: 0 for not constraining any axis, 1 for constraing the X-axis, or 2 for constraining the Y-axis. When used in queries, this flag returns the latter values and these values have the same interpretation as above. Note: when the shift key is pressed before dragging the animation curve, the first mouse movement will instead determine (and override) any prior set constrained axis.
        control | ctl: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        curvesShown | cs: (query) - Returns a string array containing the names of the animCurve nodes currently displayed in the graph editor.
        curvesShownForceUpdate | csf: (query) - Returns a string array containing the names of the animCurve nodes currently displayed in the graph editor. Unlike the curvesShown flag, this will force an update of the graph editor for the case where the mainListConnection has been modified since the last refresh.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        denormalizeCurvesCommand | dcc: (create, edit) - Sets the script that is run to denormalize curves in the graph editor. This is intended for internal use only.
        displayActiveKeyTangents | dat: (edit) - on | off | tgl Display active key tangents in the editor.
        displayActiveKeys | dak: (edit) - on | off | tgl Display active keys in the editor.
        displayInfinities | di: (edit) - on | off | tgl Display infinities in the editor.
        displayKeys | dk: (edit) - on | off | tgl Display keyframes in the editor.
        displayNormalized | dn: (edit, query) - When on, display all curves normalized to the range -1 to +1.
        displayTangents | dtn: (edit) - on | off | tgl Display tangents in the editor.
        displayValues | dv: (edit) - on | off | tgl Display active keys and tangents values in the editor.
        docTag | dtg: (create, edit, query) - Attaches a tag to the editor.
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        filter | f: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        forceMainConnection | fmc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        highlightAffectedCurves | hac: (edit, query) - When on, highlights the curve segment affected by the selected key/tangent
        highlightConnection | hlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        keyMinScale | kms: (edit, query) - The minimum key selection size in the graph editor. A value of 0.0 means there is no minimum size. A value of 1.0 means the minimum size is the size of a key with keyScale set to 1.0
        keyScale | ksc: (edit, query) - Scales the key size in the graph editor
        keyingTime | kt: (query) - The current time in the given curve to be keyed in the graph editor.
        lockMainConnection | lck: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        lockPlayRangeShades | lpr: (edit, query) - Valid values: "on" "off" "tgl" Lock Play Range Shades.
        lookAt | la: (edit) - all | selected | currentTime FitView helpers.
        mainListConnection | mlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        menu | m: (create) - Specify a script to be run when the editor is created.  The function will be passed one string argument which is the new editor's name.
        normalizeCurvesCommand | ncc: (create, edit) - Sets the script that is run to normalize curves in the graph editor. This is intended for internal use only.
        outliner | o: (edit, query) - The name of the outliner that is associated with the graph editor.
        panel | pnl: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent | p: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        preSelectionHighlight | psh: (edit, query) - When on, the curve/key/tangent under the mouse pointer is highlighted to ease selection.
        renormalizeCurves | rnc: (edit) - This flag causes the curve normalization factors to be recalculated.
        resultSamples | rs: (edit, query) - Specify the sampling for result curves Note: the smaller this number is, the longer it will take to update the display.
        resultScreenSamples | rss: (edit, query) - Specify the screen base result sampling for result curves. If 0, then results are sampled in time.
        resultUpdate | ru: (edit, query) - Valid values: "interactive" "delayed" Controls how changes to animCurves are reflected in the result curves (if results are being shown).  If resultUpdate is "interactive", then as interactive changes are being made to the animCurve, the result curves will be updated.  If modelUpdate is delayed (which is the default setting), then result curves are updated once the final change to an animCurve has been made.
        selectionConnection | slc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        showActiveCurveNames | acn: (edit, query) - Display the active curve(s)'s name.
        showBufferCurves | sb: (edit, query) - Valid values: "on" "off" "tgl" Display buffer curves.
        showCurveNames | scn: (edit, query) - Display the curves's name.
        showPlayRangeShades | spr: (edit, query) - Valid values: "on" "off" "tgl" Display Play Range Shades.
        showResults | sr: (edit, query) - Valid values: "on" "off" "tgl" Display result curves from expression or other non-keyed action.
        showUpstreamCurves | suc: (edit, query) - If true, the dependency graph is searched upstream for all curves that drive the selected plugs (showing multiple curves for example in a typical driven key setup, where first the driven key curve is encountered, followed by the actual animation curve that drives the source object). If false, only the first curves encountered will be shown. Note that, even if false, multiple curves can be shown if e.g. a blendWeighted node is being used to combine multiple curves.
        simpleKeyView | skv: (edit, query) - on | off Display simpler and smaller key.
        smoothness | s: (edit, query) - Valid values: "coarse" "rough" "medium" "fine" Specify the display smoothness of animation curves.
        snapTime | st: (edit, query) - none | integer | keyframe Keyframe move snap in time.
        snapValue | sv: (edit, query) - none | integer | keyframe Keyframe move snap in values.
        stackedCurves | sc: (edit, query) - Switches the display mode between normal (all curves sharing one set of axes) to stacked (each curve on its own value axis, stacked vertically).
        stackedCurvesMax | scx: (edit, query) - Sets the maximum value on the per-curve value axis when in stacked mode.
        stackedCurvesMin | scm: (edit, query) - Sets the minimum value on the per-curve value axis when in stacked mode.
        stackedCurvesSpace | scs: (edit, query) - Sets the spacing between curves when in stacked mode.
        stateString | sts: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        timelinePositionTop | tlp: (edit, query) - on | off | tgl Display timeline either at the top or bottom.
        unParent | up: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection | ulk: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection | upd: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
        valueLinesToggle | vlt: (edit) - on | off | tgl Display the value lines for high/low/zero of selected curves in the editor
    """
    ...


def animDisplay(*args, modelUpdate: Optional[Union[str, bool]] = ..., upd: Optional[Union[str, bool]] = ..., refAnimCurvesEditable: bool = ..., rae: bool = ..., timeCode: Optional[Union[str, bool]] = ..., tc: Optional[Union[str, bool]] = ..., timeCodeOffset: Optional[Union[str, bool]] = ..., tco: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command changes certain display options used by
    animation windows.

    Args:
        modelUpdate | upd: (create, edit, query) - Controls how changes to animCurves are propagated through the dependency graph. Valid modes are "none", "interactive" or "delayed". If modelUpdate is "none" then changing an animCurve will not cause the model to be updated (change currentTime in order to update the model).  If modelUpdate is "interactive" (which is the default setting), then as interactive changes are being made to the animCurve, the model will be updated.  If modelUpdate is delayed, then the model is updated once the final change to an animCurve has been made.  With modelUpdate set to either "interactive" or "delayed", changes to animCurves made via commands will also cause the model to be updated.
        refAnimCurvesEditable | rae: (create, edit, query) - Specify if animation curves from referenced files are editable.
        timeCode | tc: (create, edit, query) - Controls how time value are display. Valid values are "frame", "timecode", "fulltimecode". If the value is "frame" maya will display time in frame everywhere. If the value is "timecode" maya will display time in timecode in time slider, graph editor and dope sheet. If the value is "fulltimecode" maya will display time in timecode everywhere.
        timeCodeOffset | tco: (create, edit, query) - This flag has now been deprecated.  It still exists to not break legacy scripts, but it will now do nothing.  See the new timeCode command to set and query timeCodes.
    """
    ...


def animLayer(*args, addRelatedKG: bool = ..., akg: bool = ..., addSelectedObjects: bool = ..., aso: bool = ..., affectedLayers: bool = ..., afl: bool = ..., animCurves: bool = ..., anc: bool = ..., attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., baseAnimCurves: bool = ..., bac: bool = ..., bestAnimLayer: bool = ..., blr: bool = ..., bestLayer: bool = ..., bl: bool = ..., blendNodes: bool = ..., bld: bool = ..., children: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., collapse: bool = ..., col: bool = ..., copy: str = ..., cp: str = ..., copyAnimation: Optional[Union[str, bool]] = ..., ca: Optional[Union[str, bool]] = ..., copyNoAnimation: str = ..., cna: str = ..., excludeBoolean: bool = ..., ebl: bool = ..., excludeDynamic: bool = ..., edn: bool = ..., excludeEnum: bool = ..., een: bool = ..., excludeProxy: bool = ..., epr: bool = ..., excludeRotate: bool = ..., ert: bool = ..., excludeScale: bool = ..., esc: bool = ..., excludeTranslate: bool = ..., etr: bool = ..., excludeVisibility: bool = ..., evs: bool = ..., exists: bool = ..., ex: bool = ..., extractAnimation: Optional[Union[str, bool]] = ..., ea: Optional[Union[str, bool]] = ..., findCurveForPlug: Optional[Union[str, bool]] = ..., fcv: Optional[Union[str, bool]] = ..., forceUIRebuild: bool = ..., fur: bool = ..., forceUIRefresh: bool = ..., uir: bool = ..., layeredPlug: Optional[Union[str, bool]] = ..., lp: Optional[Union[str, bool]] = ..., lock: bool = ..., l: bool = ..., maxLayers: bool = ..., ml: bool = ..., moveLayerAfter: str = ..., mva: str = ..., moveLayerBefore: str = ..., mvb: str = ..., mute: bool = ..., m: bool = ..., override: bool = ..., o: bool = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., passthrough: bool = ..., pth: bool = ..., preferred: bool = ..., prf: bool = ..., removeAllAttributes: bool = ..., raa: bool = ..., removeAttribute: str = ..., ra: str = ..., removeSelectedObjects: bool = ..., rso: bool = ..., root: Optional[Union[str, bool]] = ..., r: Optional[Union[str, bool]] = ..., selected: bool = ..., sel: bool = ..., solo: bool = ..., s: bool = ..., weight: Optional[Union[float, bool]] = ..., w: Optional[Union[float, bool]] = ..., writeBlendnodeDestinations: bool = ..., wbd: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates and edits animation layers.

    Args:
        addRelatedKG | akg: (create, edit, query) - When adding or removing selected object(s) from the layer, adds associated keying group(s) to the object(s).
        addSelectedObjects | aso: (create, edit, query) - Adds selected object(s) to the layer.
        affectedLayers | afl: (query) - Return the layers that the currently selected object(s) are members of
        animCurves | anc: (create, edit, query) - In query mode returns the anim curves associated with this layer
        attribute | at: (create, edit, multiuse, query) - Adds a specific attribute on a object to the layer.
        baseAnimCurves | bac: (create, edit, query) - In query mode returns the base layer anim curves associated with this layer, if any.
        bestAnimLayer | blr: (create, edit, query) - In query mode returns the best anim layers for keying for the selected objects. If used in conjunction with -at, will return the best anim layers for keying for the specific plugs (attributes) specified.
        bestLayer | bl: (query) - Return the layer that will be keyed for specified attribute.
        blendNodes | bld: (create, edit, query) - In query mode returns the blend nodes associated with this layer
        children | c: (query) - Get the list of children layers. Return value is a string array.
        collapse | col: (create, edit, query) - Determine if a layer is collapse in the layer editor.
        copy | cp: (edit) - Copy from the layer.
        copyAnimation | ca: (create, edit) - Copy animation from specified layer to destination layer, only animation that are on attribute layered by both layer that are concerned.
        copyNoAnimation | cna: (edit) - Copy from layer without the animation curves.
        excludeBoolean | ebl: (create, edit, query) - When adding or removing selected object(s) from the layer, excludes any boolean attributes.
        excludeDynamic | edn: (create, edit, query) - When adding or removing selected object(s) from the layer, excludes any dynamic attributes.
        excludeEnum | een: (create, edit, query) - When adding or removing selected object(s) from the layer, excludes any enum attributes.
        excludeProxy | epr: (create, edit, query) - When adding or removing selected object(s) from the layer, excludes any proxy attributes.
        excludeRotate | ert: (create, edit, query) - When adding or removing selected object(s) from the layer, excludes the rotate attribute.
        excludeScale | esc: (create, edit, query) - When adding or removing selected object(s) from the layer, excludes the scale attribute.
        excludeTranslate | etr: (create, edit, query) - When adding or removing selected object(s) from the layer, excludes the translate attribute.
        excludeVisibility | evs: (create, edit, query) - When adding or removing selected object(s) from the layer, excludes the visibility attribute.
        exists | ex: (query) - Determine if a layer exists.
        extractAnimation | ea: (create, edit) - Transfer animation from specified layer to destination layer, only animation that are on attribute layered by both layer that are concerned.
        findCurveForPlug | fcv: (edit, query) - Finds the parameter curve containing the animation data for the specified plug on the given layer. 			In query mode, this flag needs a value.
        forceUIRebuild | fur: (create) - Rebuilds the animation layers user interface.
        forceUIRefresh | uir: (create) - Refreshes the animation layers user interface.
        layeredPlug | lp: (query) - Returns the plug on the blend node corresponding to the specified layer 			In query mode, this flag needs a value.
        lock | l: (create, edit, query) - Set the lock state of the specified layer. A locked layer cannot receive key. Default is false.
        maxLayers | ml: (query) - Returns the maximum number of anim layers supported by this product.
        moveLayerAfter | mva: (edit) - Move layer after the specified layer
        moveLayerBefore | mvb: (edit) - Move layer before the specified layer
        mute | m: (create, edit, query) - Set the mute state of the specified layer. Default is false.
        override | o: (create, edit, query) - Set the overide state of the specified layer. Default is false.
        parent | p: (create, edit, query) - Set the parent of the specified layer. Default is the animation layer root.
        passthrough | pth: (create, edit, query) - Set the passthrough state of the specified layer. Default is true.
        preferred | prf: (create, edit, query) - Determine if a layer is a preferred layer, the best layer algorithm will try to set keyframe in preferred layer first.
        removeAllAttributes | raa: (edit) - Remove all objects from the layer.
        removeAttribute | ra: (edit, multiuse) - Remove object from the layer.
        removeSelectedObjects | rso: (edit) - Removes selected object(s) from the layer.
        root | r: (query) - Return the base layer if it exist
        selected | sel: (create, edit, query) - Determine if a layer is selected, a selected layer will be show in the timecontrol, graph editor.
        solo | s: (create, edit, query) - Set the solo state of the specified layer. Default is false.
        weight | w: (create, edit, query) - Set the weight of the specified layer between 0.0 and 1.0. Default is 1.
        writeBlendnodeDestinations | wbd: (edit) - In edit mode writes the destination plugs of the blend nodes that belong to the layer into the blend node. This is used for layer import/export purposes and is not for general use.
    """
    ...


def animView(*args, endTime: Union[float, Tuple[float, float]] = ..., et: Union[float, Tuple[float, float]] = ..., maxValue: float = ..., max: float = ..., minValue: float = ..., min: float = ..., nextView: bool = ..., nv: bool = ..., previousView: bool = ..., pv: bool = ..., startTime: Union[float, Tuple[float, float]] = ..., st: Union[float, Tuple[float, float]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command allows you to specify the current view range within
    an animation editor.

    Args:
        endTime | et: () - End time to display within the editor
        maxValue | max: () - Upper value to display within the editor
        minValue | min: () - Lower value to display within the editor
        nextView | nv: (edit) - Switches to the next view.
        previousView | pv: (edit) - Switches to the previous view.
        startTime | st: () - Start time to display within the editor
    """
    ...


def applyTake(*args, channel: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., device: Optional[Union[str, bool]] = ..., d: Optional[Union[str, bool]] = ..., filter: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., preview: bool = ..., p: bool = ..., recurseChannel: bool = ..., rc: bool = ..., reset: bool = ..., r: bool = ..., specifyChannel: bool = ..., sc: bool = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., st: Optional[Union[Union[float, Tuple[float, float]], bool]] = ...) -> Any:
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
        channel | c: (create, multiuse) - This flag overrides the set channel enable value. If a channel is specified, it will be enabled.  C: The default is all applyTake enabled channels for the device(s).
        device | d: (create, multiuse) - Specifies which device contains the take.  C: The default is all applyTake enabled devices.
        filter | f: (create, multiuse) - This flag specifies the filters to use during the applyTake. If this flag is used multiple times, the ordering of the filters is from left to right.  C: The default is no filters.
        preview | p: (create) - Applies the take to blendDevice nodes attached to the target attributes connected to the device attachments. Animation curves attached to the attributes will not be altered, but for the time that preview data is defined, the preview data will be the data used during playback.  C: The default is to not preview.
        recurseChannel | rc: (create) - When this flag is used, the children of the channel(s) specified by -c/channel are also applied. C: The default is all of the enabled channels.
        reset | r: (create) - Resets the blendDevice nodes affected by -preview. The preview data is removed and if animation curves exist, they are used during playback.
        specifyChannel | sc: (create) - This flag is used with -c/channel flag. When used, applyTake will only work on the channels listed with the -c/channel flag.  C: The default is all of the enabled channels.
        startTime | st: (create) - The default start time for a take is determined at record time. The startTime option sets the starting time of the take in the current animation units.  C: The default is the first time stamp of the take. If a time stamp does not exist for the take, 0 is used.
    """
    ...


def autoKeyframe(*args, addAttr: str = ..., aa: str = ..., characterOption: Optional[Union[str, bool]] = ..., co: Optional[Union[str, bool]] = ..., listAttr: bool = ..., lsa: bool = ..., noReset: bool = ..., nr: bool = ..., state: bool = ..., st: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        addAttr | aa: (edit) - Add to the list of plugs (node.attribute) that autoKeyframe is currently considering for auto keying.  This list is transient and short-lived, and is reset as soon as autoKeyframe sets the keyframe or decides that no keyframe is to be set, on completion of the next set attribute.
        characterOption | co: (create, edit, query) - Valid options are: "standard", "all". Dictates whether when auto-keying characters the auto-key works as usual or whether it keys all of the character attributes. Default is "standard".
        listAttr | lsa: (query) - Returns the list of plugs (node.attribute) that autoKeyframe is currently considering for auto keying.  This list is transient and short-lived, and is reset as soon as autoKeyframe sets the keyframe or decides that no keyframe is to be set, on completion of the next set attribute.
        noReset | nr: (create, edit) - Must be used in conjunction with the state/st flag. When noReset/nr is specified, the list of plugs to be autokeyed is not cleared when the state changes
        state | st: (create, edit, query) - turns on/off remembering of modified attributes
    """
    ...


def backgroundEvaluationManager(*args, interrupt: bool = ..., i: bool = ..., mode: Optional[Union[str, bool]] = ..., m: Optional[Union[str, bool]] = ..., pause: bool = ..., p: bool = ..., resume: bool = ..., r: bool = ..., query: bool = ...) -> Any:
    r"""
    Allows user to pause and restart background evaluations.

    Args:
        interrupt | i: (create, query) - Enable or disable fast interrupt of background execution during interactive workflow.
        mode | m: (create, query) - Changes the current evaluation mode in the evaluation manager. Supported values are "serial" and "parallel".
        pause | p: (create, query) - Pause background evaluation. Will block till background evaluation is fully stopped. Can be queried to get the current state.
        resume | r: (create) - Resume background evaluation. Will start suspended evaluations unless someones else requested it.
    """
    ...


def bakeClip(*args, blend: Optional[Union[Tuple[int, int], bool]] = ..., b: Optional[Union[Tuple[int, int], bool]] = ..., clipIndex: Optional[Union[int, bool]] = ..., ci: Optional[Union[int, bool]] = ..., keepOriginals: bool = ..., k: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This command is used to bake clips and blends into a single clip.

    Args:
        blend | b: (create) - Specify the indices of the clips being blended.
        clipIndex | ci: (create, multiuse) - Specify the index of the clip to bake.
        keepOriginals | k: (create) - Keep original clips in the trax editor and place the merged clip into the visor. The default is to schedule the merged clip, and to keep the original clips in the visor.
        name | n: (create) - Specify the name of the new clip to create.
    """
    ...


def bakeDeformer(*args, colorizeSkeleton: bool = ..., cs: bool = ..., customRangeOfMotion: Optional[Union[Tuple[float, float], bool]] = ..., rom: Optional[Union[Tuple[float, float], bool]] = ..., dstMeshName: Optional[Union[str, bool]] = ..., dm: Optional[Union[str, bool]] = ..., dstSkeletonName: Optional[Union[str, bool]] = ..., ds: Optional[Union[str, bool]] = ..., hierarchy: bool = ..., hi: bool = ..., influences: Optional[Union[List[str], bool]] = ..., i: Optional[Union[List[str], bool]] = ..., maxInfluences: Optional[Union[int, bool]] = ..., mi: Optional[Union[int, bool]] = ..., pruneWeights: Optional[Union[float, bool]] = ..., pw: Optional[Union[float, bool]] = ..., smoothWeights: Optional[Union[int, bool]] = ..., sw: Optional[Union[int, bool]] = ..., srcMeshName: Optional[Union[str, bool]] = ..., sm: Optional[Union[str, bool]] = ..., srcSkeletonName: Optional[Union[str, bool]] = ..., ss: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    Given a rigged character, whose mesh shape is determined by a set of deformers, bakeDeformer calculates linear blend skin weights most closely approximating observed deformations. To do this, a test set of examples is generated by moving the rig through a range of motion. Results mesh and pose pairs are then used to solve a constrained optimization, solving for skinning weights. bakeDeformer automatically binds and applies resulting weights to the destination geometry. If the source and destination mesh/skeleton are identical, the command will replace the original deformations with a skinCluster and computed weights. See the below examples for sample usage.

    Args:
        colorizeSkeleton | cs: (create) - The new skin cluster created will have its skeleton colorized. Must be used with the -srcSkeletonName and -dstSkeletonName flags.
        customRangeOfMotion | rom: (create) - When this flag is specified with the frames for the range of motion to be used, the tool will step through each frame as a separate pose. Otherwise the tool will use the existing range of motion in the tool that rotates each influence 45 degrees.      Usage examples:       -rom "10:20" means all frames in the range from 10 to 20, inclusive, in the current time unit.   Omitting one end of a range means using either end of the animation range (or both), as in the following examples:   -rom "10:" means all frames from time 10 (in the current time unit) onwards to the maximum time in the animation range (on the timeline).   -rom ":10" means all frames from the minimum time on the animation range (on the timeline) up to (and including) time 10 (in the current time unit).   -rom ":" is a short form to specify all frames, from minimum to maximum time on the current animation range.    When using this flag, some of the joints in the specified range of motion may not have changed sufficiently. To improve bakeDeformer results or avoid algorithm errors, the command will return a list of influences that do not move enough in the specified range of motion. To detect these joints, the local transformation of each joint is compared between subsequent frames. We consider that a joint has sufficiently changed if any of the below criteria are met:      There is a rotation of at least 5 degrees, as determined by the shortest rotation between transforms. There is a translation of 1% or greater of the size of the largest bounding box containing all joints for each frame. There is a scaling change of at least 1%. This percentage represents the smallest scaling value over the largest scaling value (in absolute value).       If a joint has not met any of the criteria, it will be added to the warning of joints that have not moved enough.        The custom range of motion should be considered experimental.
        dstMeshName | dm: (create) - The destination mesh name.
        dstSkeletonName | ds: (create) - The destination skeleton name.
        hierarchy | hi: (create) - All children of the passed joints that are used in the influences flag are used.
        influences | i: (create) - A list of joints that are used as the influences to determine new weights.
        maxInfluences | mi: (create) - The maximum number of influences per vertex.
        pruneWeights | pw: (create) - On the newly created skin cluster, set any weight below the given the value to zero (post-processing). This will call the skinPercent command as follows: "skinPercent -pruneWeights [value] [skinClusterName] [dstMeshName]" where [value] is the value passed into this flag, [skinClusterName] is the name of the new skinCluster node created after running this tool, and [dstMeshName] is the mesh provided in the -dstMeshName flag.
        smoothWeights | sw: (create) - The number of smoothing iterations for smoothing weights (post-processing). This also renormalizes the remaining the weights.
        srcMeshName | sm: (create) - The source mesh name.
        srcSkeletonName | ss: (create) - The source skeleton name.
    """
    ...


def bakeResults(*args, animation: Optional[Union[str, bool]] = ..., an: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., bakeOnOverrideLayer: bool = ..., bol: bool = ..., controlPoints: bool = ..., cp: bool = ..., destinationLayer: Optional[Union[str, bool]] = ..., dl: Optional[Union[str, bool]] = ..., disableImplicitControl: bool = ..., dic: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., f: Optional[Union[Tuple[float, float], bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., hi: Optional[Union[str, bool]] = ..., includeUpperBound: bool = ..., iub: bool = ..., index: Optional[Union[int, bool]] = ..., minimizeRotation: bool = ..., mr: bool = ..., oversamplingRate: Optional[Union[int, bool]] = ..., osr: Optional[Union[int, bool]] = ..., preserveOutsideKeys: bool = ..., pok: bool = ..., removeBakedAnimFromLayer: bool = ..., rba: bool = ..., removeBakedAttributeFromLayer: bool = ..., ral: bool = ..., resolveWithoutLayer: Optional[Union[str, bool]] = ..., rwl: Optional[Union[str, bool]] = ..., sampleBy: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., sb: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., shape: bool = ..., s: bool = ..., simulation: bool = ..., sm: bool = ..., smart: Optional[Union[List[Union[bool, float]], bool]] = ..., sr: Optional[Union[List[Union[bool, float]], bool]] = ..., sparseAnimCurveBake: bool = ..., sac: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., t: Optional[Union[Tuple[float, float], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        animation | an: (create) - Where this command should get the animation to act on. Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects." See command description for details.
        attribute | at: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        bakeOnOverrideLayer | bol: (create) - If true, all layered and baked attribute will be added as a top override layer.
        controlPoints | cp: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        destinationLayer | dl: (create) - This flag can be used to specify an existing layer where the baked results should be stored. Use this flag with caution. If the destination layer already has animation on it that contributes to the final result, it will be replaced by the output of the bake. As a result, it is possible that the combined animation visible in the scene is different before / after the baking process.
        disableImplicitControl | dic: (create) - Whether to disable implicit control after the anim curves are obtained as the result of this command. An implicit control to an attribute is some function that affects the attribute without using an explicit dependency graph connection. The control of IK, via ik handles, is an example.
        float | f: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve. Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        hierarchy | hi: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        includeUpperBound | iub: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true. This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound. Note: when used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace." This flag has no effect on the curve pasted from the clipboard.
        index | index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        minimizeRotation | mr: (create) - Specify whether to minimize the local Euler component from key to key during baking of rotation channels.
        oversamplingRate | osr: (create) - Amount of samples per sampleBy period. Default is 1.
        preserveOutsideKeys | pok: (create) - Whether to preserve keys that are outside the bake range when there are directly connected animation curves or a pairBlend node which has an animation curve as its direct input. The default (false) is to remove frames outside the bake range. If the channel that you are baking is not controlled by a single animation curve, then a new animation curve will be created with keys only in the bake range. In the case of pairBlend-driven channels, setting pok to true will retain both the pairBlend and its input animCurve. The blended values will be baked onto the animCurve and the weight of the pairBlend weight will be keyed to the animCurve during the baked range.
        removeBakedAnimFromLayer | rba: (create) - If true, all baked animation will be removed from the layer. Otherwise all layer associated with the baked animation will be muted.
        removeBakedAttributeFromLayer | ral: (create) - If true, all baked attribute will be removed from the layer. Otherwise all layer associated with the baked attribute will be muted.
        resolveWithoutLayer | rwl: (create, multiuse) - This flag can be used to specify a list of layers to be merged together during the bake process. This is a multi-use flag. Its name refers to the fact that when solving for the value to key, it determines the proper value to key on the destination layer to achieve the same result as the merged layers.
        sampleBy | sb: (create) - Amount to sample by. Default is 1.0 in current timeUnit.
        shape | s: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        simulation | sm: (create) - Using this flag instructs the command to preform a simulation instead of just evaluating each attribute separately over the range of time. The simulation flag is required to bake animation that depends on the whole scene being evaluated at each time step such as dynamics. The default is false.
        smart | sr: (create) - Specify whether to enable smart bake and the optional smart bake tolerance.
        sparseAnimCurveBake | sac: (create) - When this is true and anim curves are being baked, do not insert any keys into areas of the curve where animation is defined. And, use as few keys as possible to bake the pre and post infinity behavior. When this is false, one key will be inserted at each time step. The default is false.
        time | t: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
    """
    ...


def bakeSimulation(*args, animation: Optional[Union[str, bool]] = ..., an: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., bakeOnOverrideLayer: bool = ..., bol: bool = ..., controlPoints: bool = ..., cp: bool = ..., destinationLayer: Optional[Union[str, bool]] = ..., dl: Optional[Union[str, bool]] = ..., disableImplicitControl: bool = ..., dic: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., f: Optional[Union[Tuple[float, float], bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., hi: Optional[Union[str, bool]] = ..., includeUpperBound: bool = ..., iub: bool = ..., index: Optional[Union[int, bool]] = ..., minimizeRotation: bool = ..., mr: bool = ..., preserveOutsideKeys: bool = ..., pok: bool = ..., removeBakedAnimFromLayer: bool = ..., rba: bool = ..., removeBakedAttributeFromLayer: bool = ..., ral: bool = ..., resolveWithoutLayer: Optional[Union[str, bool]] = ..., rwl: Optional[Union[str, bool]] = ..., sampleBy: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., sb: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., shape: bool = ..., s: bool = ..., simulation: bool = ..., sm: bool = ..., smart: Optional[Union[List[Union[bool, float]], bool]] = ..., sr: Optional[Union[List[Union[bool, float]], bool]] = ..., sparseAnimCurveBake: bool = ..., sac: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., t: Optional[Union[Tuple[float, float], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        animation | an: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute | at: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        bakeOnOverrideLayer | bol: (create) - If true, all layered and baked attributes will be added as a top override layer.
        controlPoints | cp: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        destinationLayer | dl: (create) - This flag can be used to specify an existing layer where the baked results should be stored.
        disableImplicitControl | dic: (create) - Whether to disable implicit control after the anim curves are obtained as the result of this command. An implicit control to an attribute is some function that affects the attribute without using an explicit dependency graph connection. The control of IK, via ik handles, is an example.
        float | f: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        hierarchy | hi: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        includeUpperBound | iub: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index | index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        minimizeRotation | mr: (create) - Specify whether to minimize the local euler component from key to key during baking of rotation channels.
        preserveOutsideKeys | pok: (create) - Whether to preserve keys that are outside the bake range when there are directly connected animation curves.  The default (false) is to remove frames outside the bake range.  If the channel that you are baking is not controlled by a single animation curve, then a new animation curve will be created with keys only in the bake range.
        removeBakedAnimFromLayer | rba: (create) - If true, all baked animation will be removed from the layer.
        removeBakedAttributeFromLayer | ral: (create) - If true, all baked attributes will be removed from the layer.
        resolveWithoutLayer | rwl: (create, multiuse) - This flag can be used to specify a list of layers to be merged together during the bake process. This is a multi-use flag. Its name refers to the fact that when solving for the value to key, it determines the proper value to key on the destination layer to achieve the same result as the merged layers.
        sampleBy | sb: (create) - Amount to sample by. Default is 1.0 in current timeUnit
        shape | s: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        simulation | sm: (create) - Using this flag instructs the command to preform a simulation instead of just evaluating each attribute separately over the range of time. The simulation flag is required to bake animation that that depends on the whole scene being evaluated at each time step such as dynamics. The default is true.
        smart | sr: (create) - Specify whether to enable smart bake and the optional smart bake tolerance.
        sparseAnimCurveBake | sac: (create) - When baking anim curves, do not insert any keys into areas of the curve where animation is defined.  And, use as few keys as possible to bake the pre and post infinity behaviors.  When this is false, one key will be inserted at each time step.  The default is false.
        time | t: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
    """
    ...


def bindSkin(*args, byClosestPoint: bool = ..., bcp: bool = ..., byPartition: bool = ..., bp: bool = ..., colorJoints: bool = ..., cj: bool = ..., delete: bool = ..., d: bool = ..., doNotDescend: bool = ..., dnd: bool = ..., enable: bool = ..., en: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., partition: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., toAll: bool = ..., ta: bool = ..., toSelectedBones: bool = ..., tsb: bool = ..., toSkeleton: bool = ..., ts: bool = ..., unbind: bool = ..., ub: bool = ..., unbindKeepHistory: bool = ..., ubk: bool = ..., unlock: bool = ..., ul: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        byClosestPoint | bcp: (create) - bind each point in the object to the segment closest to the point. The byClosestPoint and byPartition flags are mutually exclusive.  The byClosestPoint flag is the default.
        byPartition | bp: (create) - bind each group in the partition to the segment closest to the group's centroid. A partition must be specified with the -p/-partition flag
        colorJoints | cj: (create) - In bind mode, this flag assigns colors to the joints based on the colors assigned to the joint's skin set. In delete and unlock mode, this flag removes the colors from joints that are no longer bound as skin. In disable and unbindKeepHistory mode, this flag does nothing.
        delete | d: (create) - Detach the skin on the selected skeletons and remove all bind- related construction history.
        doNotDescend | dnd: (create) - Do not descend to shapes that are parented below the selected object(s). Bind only the selected objects.
        enable | en: (create) - Enable or disable a bind that has been disabled on the selected skeletons. To enable the bind on selected bones only, select the bones and use the -tsb flag with the -en flag. This flag is used when you want to temporarily disable the bind without losing the set information or the weight information of the skinning, for example if you want to modify the bindPose.
        name | n: (create) - This flag is obsolete.
        partition | p: (create) - Specify a partition to bind by. This is only valid when used with the -bp/-byPartition flag.
        toAll | ta: (create) - objects will be bound to the entire selected skeletons. Even bones with zero influence will be bound, whereas the toSkeleton will only bind non-zero influences.
        toSelectedBones | tsb: (create) - objects will be bound to the selected bones only.
        toSkeleton | ts: (create) - objects will be bound to the selected skeletons. The toSkeleton, toAll and toSelectedBones flags are mutually exclusive. The toSkeleton flag is the default.
        unbind | ub: (create) - unbind the selected objects. They will no longer move with the skeleton. Any bindSkin history that is no longer used will be deleted.
        unbindKeepHistory | ubk: (create) - unbind the selected objects. They will no longer move with the skeleton. However, existing weights on the skin will be kept for use the next time the skin is bound. This option is appropriate if you want to modify the skeleton without losing the weighting information on the skin.
        unlock | ul: (create) - unlock the selected objects. Since bindSkin will no longer give normal results if bound objects are moved away from the skeleton, bindSkin locks translate, rotate and scale. This command unlocks the selected objects translate, rotate and scale.
    """
    ...


def blendShape(*args, after: bool = ..., af: bool = ..., afterReference: bool = ..., ar: bool = ..., automatic: bool = ..., at: bool = ..., before: bool = ..., bf: bool = ..., components: bool = ..., cmp: bool = ..., copyDelta: Tuple[int, int, int] = ..., cd: Tuple[int, int, int] = ..., copyInBetweenDelta: Tuple[int, int, int, int] = ..., cid: Tuple[int, int, int, int] = ..., copyWeights: Tuple[int, int, int] = ..., cw: Tuple[int, int, int] = ..., deformerTools: bool = ..., dt: bool = ..., envelope: Optional[Union[float, bool]] = ..., en: Optional[Union[float, bool]] = ..., exclusive: Optional[Union[str, bool]] = ..., ex: Optional[Union[str, bool]] = ..., export: str = ..., ep: str = ..., exportTarget: Tuple[int, int] = ..., et: Tuple[int, int] = ..., flipTarget: Tuple[int, int] = ..., ft: Tuple[int, int] = ..., frontOfChain: bool = ..., foc: bool = ..., geometry: Optional[Union[str, bool]] = ..., g: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., gi: bool = ..., ignoreSelected: bool = ..., ip: str = ..., inBetween: bool = ..., ib: bool = ..., inBetweenIndex: int = ..., ibi: int = ..., inBetweenType: Optional[Union[str, bool]] = ..., ibt: Optional[Union[str, bool]] = ..., includeHiddenSelections: bool = ..., ihs: bool = ..., mergeSource: int = ..., mgs: int = ..., mergeTarget: int = ..., mgt: int = ..., mirrorDirection: int = ..., md: int = ..., mirrorTarget: Tuple[int, int] = ..., mt: Tuple[int, int] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., normalizationGroups: bool = ..., ng: bool = ..., origin: Optional[Union[str, bool]] = ..., o: Optional[Union[str, bool]] = ..., parallel: bool = ..., par: bool = ..., prune: bool = ..., pr: bool = ..., remove: bool = ..., rm: bool = ..., resetTargetDelta: Tuple[int, int] = ..., rtd: Tuple[int, int] = ..., selectedComponents: bool = ..., cms: bool = ..., split: bool = ..., sp: bool = ..., suppressDialog: bool = ..., sd: bool = ..., symmetryAxis: Optional[Union[str, bool]] = ..., sa: Optional[Union[str, bool]] = ..., symmetryEdge: Optional[Union[str, bool]] = ..., se: Optional[Union[str, bool]] = ..., symmetrySpace: Optional[Union[int, bool]] = ..., ss: Optional[Union[int, bool]] = ..., tangentSpace: bool = ..., ts: bool = ..., target: Optional[Union[Tuple[str, int, str, float], bool]] = ..., t: Optional[Union[Tuple[str, int, str, float], bool]] = ..., topologyCheck: bool = ..., tc: bool = ..., transform: Optional[Union[str, bool]] = ..., tr: Optional[Union[str, bool]] = ..., useComponentTags: bool = ..., uct: bool = ..., weight: Optional[Union[Tuple[int, float], bool]] = ..., w: Optional[Union[Tuple[int, float], bool]] = ..., weightCount: Optional[Union[int, bool]] = ..., wc: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        after | af: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference | ar: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        automatic | at: (create, edit) - The -automatic flag is used to specify deformer ordering in a way that choses between -frontOfChain and -before automatically. If the geometry being deformed is only affected by invertible deformers, the -frontOfChain mode is used, otherwise the -before mode is used.
        before | bf: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        components | cmp: (query) - Returns the components used by the deformer
        copyDelta | cd: (edit) - Set the base, source, and destination delta index values.
        copyInBetweenDelta | cid: (edit) - Set the base, target, source, and destination delta index values.
        copyWeights | cw: (edit) - Copy base, source, and destination weight index values.
        deformerTools | dt: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        envelope | en: (create, edit, query) - Set the envelope value for the deformer, controlling how much of the total deformation gets applied. Default is 1.0.
        exclusive | ex: (create, query) - Puts the deformation set in a deform partition.
        export | ep: (edit) - Export the shapes to the named file path.
        exportTarget | et: (edit, multiuse) - Specify the base and target index pairs for the export.
        flipTarget | ft: (edit, multiuse) - Flip the list of base and target pairs.
        frontOfChain | foc: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry | g: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices | gi: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected | ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        ip | ip: (edit) - Import the shapes from the named file path.
        inBetween | ib: (create, edit) - Indicate that the specified target should serve as an inbetween. An inbetween target is one that serves as an intermediate target between the base shape and another target.
        inBetweenIndex | ibi: (edit) - Only used with the -rtd/-resetTargetDelta flag to remove delta values for points in the inbetween target geometry defined by this index.
        inBetweenType | ibt: (create, edit) - Specify if the in-between target to be created is relative to the hero target or if it is absolute. If it is relative to hero targets, the in-between target will get any changes made to the hero target. Valid values are "relative" and "absolute". This flag should always be used with the -ib/-inBetween and -t/-target flags.
        includeHiddenSelections | ihs: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        mergeSource | mgs: (edit, multiuse) - List of source indexes for a merge.
        mergeTarget | mgt: (edit) - Target index of a merge
        mirrorDirection | md: (edit) - Mirror direction; 0 = negative, 1 = positive
        mirrorTarget | mt: (edit, multiuse) - Mirror the list of base and target pairs.
        name | n: (create) - Used to specify the name of the node being created.
        normalizationGroups | ng: (query) - Returns a list of the used normalization group IDs.
        origin | o: (create) - blendShape will be performed with respect to the world by default. Valid values are "world" and "local". The local flag will cause the blend shape to be performed with respect to the shape's local origin.
        parallel | par: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        prune | pr: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        remove | rm: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        resetTargetDelta | rtd: (edit, multiuse) - Remove all delta values for points in the target geometry, including all sequential targets defined by target index. Parameter list:  uint: the base object index uint: the target index
        selectedComponents | cms: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        split | sp: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        suppressDialog | sd: (create, edit) - Suppress dialog box and run the command as defined by the user.
        symmetryAxis | sa: (edit, query) - Axis for symmetry. Valid values are "X", "Y", and "Z".
        symmetryEdge | se: (edit, multiuse, query) - One or two symmetry edge names, separated by a ".". See the blendShape node's symmetryEdge attribute for legal values.
        symmetrySpace | ss: (edit, query) - Space for symmetry. 0 = Topological, 1 = Object, 2 = UV
        tangentSpace | ts: (create, edit) - Indicate that the delta of the specified target should be relative to the tangent space of the surface.
        target | t: (create, edit, multiuse, query) - Set target object as the index target shape for the base shape base object. The full influence of target shape takes effect when its shape weight is targetValue. Parameter list:  string: the base object int: index string: the target object double: target value
        topologyCheck | tc: (create) - Set the state of checking for a topology match between the shapes being blended. Default is on.
        transform | tr: (edit, query) - Set transform for target, then the deltas will become relative to a post transform. Typically the best workflow for this option is to choose a joint that is related to the fix you have introduced. This flag should be used only if the "Deformation order" of blendShape node is "Before".
        useComponentTags | uct: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
        weight | w: (create, edit, multiuse, query) - Set the weight value (second parameter) at index (first parameter).
        weightCount | wc: (create, edit, query) - Set the number of shape weight values.
    """
    ...


def blendShapeEditor(*args, control: bool = ..., ctl: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., exists: bool = ..., ex: bool = ..., filter: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., fmc: Optional[Union[str, bool]] = ..., highlightConnection: Optional[Union[str, bool]] = ..., hlc: Optional[Union[str, bool]] = ..., lockMainConnection: bool = ..., lck: bool = ..., mainListConnection: Optional[Union[str, bool]] = ..., mlc: Optional[Union[str, bool]] = ..., panel: Optional[Union[str, bool]] = ..., pnl: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., selectionConnection: Optional[Union[str, bool]] = ..., slc: Optional[Union[str, bool]] = ..., stateString: bool = ..., sts: bool = ..., targetControlList: bool = ..., tcl: bool = ..., targetList: bool = ..., tl: bool = ..., unParent: bool = ..., up: bool = ..., unlockMainConnection: bool = ..., ulk: bool = ..., updateMainConnection: bool = ..., upd: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., verticalSliders: bool = ..., vs: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates an editor that derives from the base editor
    class that has controls for blendShape, control nodes.

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
        targetControlList | tcl: (query) - 
        targetList | tl: (query) - 
        unParent | up: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection | ulk: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection | upd: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
        verticalSliders | vs: (create, edit, query) - 
    """
    ...


def blendShapePanel(*args, blendShapeEditor: bool = ..., be: bool = ..., control: bool = ..., ctl: bool = ..., copy: str = ..., cp: str = ..., createString: bool = ..., cs: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., editString: bool = ..., es: bool = ..., exists: bool = ..., ex: bool = ..., init: bool = ..., isUnique: bool = ..., iu: bool = ..., label: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., menuBarRepeatLast: bool = ..., mrl: bool = ..., menuBarVisible: bool = ..., mbv: bool = ..., needsInit: bool = ..., ni: bool = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., popupMenuProcedure: Optional[Union[str, bool]] = ..., pmp: Optional[Union[str, bool]] = ..., replacePanel: str = ..., rp: str = ..., tearOff: bool = ..., to: bool = ..., tearOffCopy: Optional[Union[str, bool]] = ..., toc: Optional[Union[str, bool]] = ..., tearOffRestore: bool = ..., tor: bool = ..., unParent: bool = ..., up: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a panel that derives from the base panel
    class that houses a blendShapeEditor.

    Args:
        blendShapeEditor | be: (query) - Query only flag that returns the name of an editor to be associated with the panel.
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


def blendTwoAttr(*args, attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., attribute0: Optional[Union[str, bool]] = ..., at0: Optional[Union[str, bool]] = ..., attribute1: Optional[Union[str, bool]] = ..., at1: Optional[Union[str, bool]] = ..., blender: Optional[Union[str, bool]] = ..., bl: Optional[Union[str, bool]] = ..., controlPoints: bool = ..., cp: bool = ..., driver: Optional[Union[int, bool]] = ..., d: Optional[Union[int, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., shape: bool = ..., s: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., t: Optional[Union[Tuple[float, float], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        attribute | at: (create, multiuse) - A list of attributes for the selected nodes for which a blendTwoAttr node will be created.       In query mode, this flag needs a value.
        attribute0 | at0: (create, edit, query) - The attribute that should be connected to the first input of the new blendTwoAttr node. When queried, it returns a string.
        attribute1 | at1: (create, edit, query) - The attribute that should be connected to the second input of the new blendTwoAttr node. When queried, it returns a string.
        blender | bl: (create, edit, query) - The blender attribute. This is the attribute that will be connected to the newly created blendTwoAttr node(s) blender attribute. This attribute controls how much of each of the two attributes to use in the blend. If this flag is not specified, a new animation curve is created whose value goes from 1 to 0 throughout the time range specified by the -t flag. If -t is not specified, an abrupt change from the value of the first to the value of the second attribute will occur at the current time when this command is issued.
        controlPoints | cp: (create) - Explicitly specify whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.
        driver | d: (create, edit, query) - The index of the driver attribute for this blend node (0 or 1) When queried, it returns an integer.
        name | n: (create, query) - name for the new blend node(s)
        shape | s: (create) - Consider all attributes of shapes below transforms as well, except "controlPoints". Default: true
        time | t: (create) - The time range between which the blending between the 2 attributes should occur. If a single time is specified, then the blend will cause an abrupt change from the first to the second attribute at that time.  If a range is specified, a smooth blending will occur over that time range. The default is to make a sudden transition at the current time.
    """
    ...


def bluePencilDrawCtx(*args, edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to create the blue pencil drawing context.

    Args:
    """
    ...


def bluePencilFrame(*args, activeViewport: bool = ..., avp: bool = ..., clear: bool = ..., clr: bool = ..., copy: bool = ..., cp: bool = ..., cutFrame: bool = ..., cut: bool = ..., delete: bool = ..., duplicate: bool = ..., dup: bool = ..., exportFrames: bool = ..., ex: bool = ..., importFrames: bool = ..., im: bool = ..., insert: bool = ..., ins: bool = ..., move: Optional[Union[Tuple[int, int, int], bool]] = ..., mv: Optional[Union[Tuple[int, int, int], bool]] = ..., moveCopy: Optional[Union[Tuple[int, int, int], bool]] = ..., mvc: Optional[Union[Tuple[int, int, int], bool]] = ..., moveToNext: bool = ..., mvn: bool = ..., paste: bool = ..., pst: bool = ..., relative: bool = ..., rel: bool = ..., retime: Optional[Union[int, bool]] = ..., ret: Optional[Union[int, bool]] = ..., scale: Optional[Union[Tuple[float, bool, int, int], bool]] = ..., sc: Optional[Union[Tuple[float, bool, int, int], bool]] = ..., scaleCopy: Optional[Union[Tuple[float, bool, int, int], bool]] = ..., scc: Optional[Union[Tuple[float, bool, int, int], bool]] = ..., stepBack: bool = ..., sb: bool = ..., stepForward: bool = ..., sf: bool = ...) -> Any:
    r"""
    Command to create or edit blue pencil frames.

    Args:
        activeViewport | avp: (create) - Create the frame in the active viewport's camera.
        clear | clr: (create) - Erase the data from one or more frames using the highlighted range in Maya's time slider.
        copy | cp: (create) - Copy the frame data in the selected range to the clipboard.
        cutFrame | cut: (create) - Copy the frame data in the selected range to the clipboard and remove the frames.
        delete | delete: (create) - Remove one or more frames using the highlighted range in Maya's time slider.
        duplicate | dup: (create) - Insert a frame at the current time that is a duplicate of the previous frame.
        exportFrames | ex: (create) - Show blue pencil export frame dialog.
        importFrames | im: (create) - Show blue pencil import frame dialog.
        insert | ins: (create) - Insert one or more empty frames using the highlighted range in the time slider.
        move | mv: (create) - Move the frames in the specified range by the given offset. Arguments are offset, range start, range end.
        moveCopy | mvc: (create) - Copy then move the frames in the specified range by the given offset. Arguments are offset, range start, range end.
        moveToNext | mvn: (create) - Move the current time to the next frame after retiming.
        paste | pst: (create) - Create new frames using the data in the clipboard at the current time.
        relative | rel: (create) - Set the retime action to shift the frames by a relative amount to add or remove space between frames. When the flag is not set, the spacing between the frames is set to the retime value.
        retime | ret: (create) - Shift frames or change the frame spacing in a selected range.
        scale | sc: (create) - Scale the frames in the specified range by the given factor. Arguments are scale factor, scale from end (true) or beginning (false), range start, range end.
        scaleCopy | scc: (create) - Copy then scale the frames in the specified range by the given factor. Arguments are scale factor, scale from end (true) or beginning (false), range start, range end.
        stepBack | sb: (create) - Set the current time to the previous blue pencil frame's time.
        stepForward | sf: (create) - Set the current time to the next blue pencil frame's time.
    """
    ...


def bluePencilLayer(*args, active: Optional[Union[int, bool]] = ..., act: Optional[Union[int, bool]] = ..., addLayer: bool = ..., add: bool = ..., count: bool = ..., cnt: bool = ..., delete: int = ..., deleteAll: bool = ..., da: bool = ..., editLocked: Tuple[bool, int] = ..., el: Tuple[bool, int] = ..., editName: Tuple[str, int] = ..., en: Tuple[str, int] = ..., editOpacity: Tuple[float, int] = ..., eo: Tuple[float, int] = ..., editState: Tuple[int, int] = ..., es: Tuple[int, int] = ..., editVis: Tuple[bool, int] = ..., ev: Tuple[bool, int] = ..., insert: int = ..., ins: int = ..., layerState: Tuple[int, int] = ..., ls: Tuple[int, int] = ..., move: Tuple[int, int] = ..., mv: Tuple[int, int] = ..., moveAll: bool = ..., mva: bool = ..., name: Tuple[str, int] = ..., n: Tuple[str, int] = ..., newCamera: str = ..., nc: str = ..., queryLocked: int = ..., ql: int = ..., queryName: int = ..., qn: int = ..., queryOpacity: int = ..., qo: int = ..., queryState: int = ..., qs: int = ..., queryVis: int = ..., qv: int = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to manage blue pencil layers. The command requires a camera name as argument.

    Args:
        active | act: (create, edit, query) - Sets the active layer index. Query returns the active layer index.
        addLayer | add: () - Creates a new layer.
        count | cnt: () - Returns the number of layers.
        delete | delete: () - Removes the layer at the specified index.
        deleteAll | da: () - Removes all layers.
        editLocked | el: () - Edit the layer's locked state.
        editName | en: () - Sets name of the layer at the specified index.
        editOpacity | eo: () - Sets the opacity of the layer at the specified index.
        editState | es: () - Edits the layer's state. 0: animated, 1: static.
        editVis | ev: () - Sets the visibility of the layer at the specified index.
        insert | ins: () - Creates a new layer at the given index.
        layerState | ls: () - Sets the layer state when adding a new layer. 0: animated, 1: static.
        move | mv: () - Moves a layer from one index to another.
        moveAll | mva: () - Moves all layers from the current camera to the given camera.
        name | n: () - Sets the name of the new layer when using addLayer or insertLayer.
        newCamera | nc: () - Sets a new camera to move layers to when using the move test.
        queryLocked | ql: () - Query the layer's locked state.
        queryName | qn: () - Returns the specified layer's name.
        queryOpacity | qo: () - Returns the specified layer's opacity.
        queryState | qs: () - Queries the layer's state. 0: animated, 1: static.
        queryVis | qv: () - Returns the specified layer's visibility.
    """
    ...


def bluePencilNode(*args, camera: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., exists: bool = ..., ex: bool = ..., frame: bool = ..., f: bool = ..., layer: bool = ..., l: bool = ..., layerName: Optional[Union[str, bool]] = ..., ln: Optional[Union[str, bool]] = ..., layerState: Optional[Union[int, bool]] = ..., ls: Optional[Union[int, bool]] = ..., refresh: bool = ..., r: bool = ..., refreshGhosting: bool = ..., rg: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to create the blue pencil node.

    Args:
        camera | c: (create, query) - Specifies the camera on which to create a new layer when creating the node. Query returns the name of the active camera.
        exists | ex: (create) - Returns true if the blue pencil node has been created.
        frame | f: (create) - Creates a new frame when creating the new layer when creating the node.
        layer | l: (create) - Create a new layer when creating the node.
        layerName | ln: (create) - Specifies the layer name of the new layer when creating the node.
        layerState | ls: (create) - Specifies the layer state of the new layer. 0: Animated, 1: Static.
        refresh | r: (create) - Refresh the viewport of the active camera.
        refreshGhosting | rg: (create) - Refresh the ghosting information.
    """
    ...


def bluePencilStroke(*args, frameAdded: bool = ..., fa: bool = ..., layerAdded: Optional[Union[int, bool]] = ..., la: Optional[Union[int, bool]] = ...) -> Any:
    r"""
    Command used to commit active blue pencil strokes.

    Args:
        frameAdded | fa: (create) - The index of the frame added for the new stroke. This is set to remove it when undoing.
        layerAdded | la: (create) - Sets the index of the added layer to remove it when undoing.
    """
    ...


def bluePencilUtil(*args, adjustBrushSize: bool = ..., abs: bool = ..., adjustOpacity: bool = ..., aop: bool = ..., arrowOptions: Optional[Union[Tuple[int, int], bool]] = ..., ao: Optional[Union[Tuple[int, int], bool]] = ..., arrowTool: bool = ..., at: bool = ..., brushOptions: Optional[Union[Tuple[int, int, int, int, int], bool]] = ..., bo: Optional[Union[Tuple[int, int, int, int, int], bool]] = ..., brushTool: bool = ..., bt: bool = ..., draw: bool = ..., d: bool = ..., drawColor: Optional[Union[Tuple[int, int, int], bool]] = ..., dc: Optional[Union[Tuple[int, int, int], bool]] = ..., ellipseOptions: Optional[Union[Tuple[int, int], bool]] = ..., elo: Optional[Union[Tuple[int, int], bool]] = ..., ellipseTool: bool = ..., elt: bool = ..., eraserOptions: Optional[Union[Tuple[int, int, int, int, int], bool]] = ..., eo: Optional[Union[Tuple[int, int, int, int, int], bool]] = ..., eraserTool: bool = ..., et: bool = ..., ghostColorNext: Optional[Union[Tuple[int, int, int], bool]] = ..., gcn: Optional[Union[Tuple[int, int, int], bool]] = ..., ghostColorOverride: bool = ..., gco: bool = ..., ghostColorPrevious: Optional[Union[Tuple[int, int, int], bool]] = ..., gcp: Optional[Union[Tuple[int, int, int], bool]] = ..., ghostNext: bool = ..., gn: bool = ..., ghostNextCount: Optional[Union[int, bool]] = ..., gnc: Optional[Union[int, bool]] = ..., ghostPrevious: bool = ..., gp: bool = ..., ghostPreviousCount: Optional[Union[int, bool]] = ..., gpc: Optional[Union[int, bool]] = ..., layerManager: bool = ..., lm: bool = ..., layerProperties: bool = ..., lp: bool = ..., lineOptions: Optional[Union[Tuple[int, int], bool]] = ..., lo: Optional[Union[Tuple[int, int], bool]] = ..., lineTool: bool = ..., lt: bool = ..., pencilOptions: Optional[Union[Tuple[int, int, int, int], bool]] = ..., po: Optional[Union[Tuple[int, int, int, int], bool]] = ..., pencilTool: bool = ..., pt: bool = ..., rectangleOptions: Optional[Union[Tuple[int, int], bool]] = ..., ro: Optional[Union[Tuple[int, int], bool]] = ..., rectangleTool: bool = ..., rt: bool = ..., refreshLayerManager: bool = ..., rlm: bool = ..., refreshTimelineDisplay: bool = ..., rtd: bool = ..., resetTool: bool = ..., r: bool = ..., textFontFamily: Optional[Union[str, bool]] = ..., tff: Optional[Union[str, bool]] = ..., textOptions: Optional[Union[Tuple[int, int, str], bool]] = ..., txo: Optional[Union[Tuple[int, int, str], bool]] = ..., textTool: bool = ..., tt: bool = ..., timelineFrameDisplay: Optional[Union[int, bool]] = ..., tfd: Optional[Union[int, bool]] = ..., transform: bool = ..., t: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Utility commands for blue pencil tool.

    Args:
        adjustBrushSize | abs: (create, edit, query) - Activates or deactivates the mode to adujst the brush size by dragging.
        adjustOpacity | aop: (create, edit, query) - Activates or deactivates the mode to adujst the brush opacity by dragging.
        arrowOptions | ao: (create, edit, query) - Set the arrow options. The arguments are size, opacity.
        arrowTool | at: (create, edit, query) - Activates the arrow tool. When queried, returns true if the arrow tool is active.
        brushOptions | bo: (create, edit, query) - Sets the brush options. The arguments in order are size, opacity, hardness pressure opacity, pressure size.
        brushTool | bt: (create, edit, query) - Activates the brush tool. When queried, returns true if the brush tool is active.
        draw | d: (create, edit, query) - Activates the drawing tool context. When queried, returns true if the drawing tool context is active.
        drawColor | dc: (create, edit, query) - Sets the current drawing color. Color format is RGB with values from 0-255. When queried, returns the current drawing color.
        ellipseOptions | elo: (create, edit, query) - Sets the ellipse options. The arguments are size, opacity.
        ellipseTool | elt: (create, edit, query) - Activates the ellipse tool. When queried, returns true if the ellipse tool is active.
        eraserOptions | eo: (create, edit, query) - Sets the brush options. The arguments in order are size, opacity, hardness pressure opacity, pressure size.
        eraserTool | et: (create, edit, query) - Activates the eraser tool. When queried, returns true if the eraser tool is active.
        ghostColorNext | gcn: (create, edit, query) - Sets the color for the ghosts of next frames.
        ghostColorOverride | gco: (create, edit, query) - Activates or deactivates the color override for the ghosts.
        ghostColorPrevious | gcp: (create, edit, query) - Sets the color for the ghosts of previous frames.
        ghostNext | gn: (create, edit, query) - Activates or deactivates the ghosting of next frames.
        ghostNextCount | gnc: (create, edit, query) - Sets the number of ghosts of next frames.
        ghostPrevious | gp: (create, edit, query) - Activates or deactivates the ghosting of previous frames.
        ghostPreviousCount | gpc: (create, edit, query) - Sets the number of ghosts of previous frames.
        layerManager | lm: (create, edit, query) - Shows the layer manager by showing the tool settings window. Query returns if the layer manager is shown.
        layerProperties | lp: (create, edit, query) - Show the layer properties dialog.
        lineOptions | lo: (create, edit, query) - Sets the line options. The arguments are size, opacity.
        lineTool | lt: (create, edit, query) - Activates the line tool. When queried, returns true if the line tool is active.
        pencilOptions | po: (create, edit, query) - Sets the pencil options. The arguments in order are size, opacity, pressure opacity, pressure size.
        pencilTool | pt: (create, edit, query) - Activates the pencil tool. When queried, returns true if the pencil tool is active.
        rectangleOptions | ro: (create, edit, query) - Sets the rectangle options. The arguments are size, opacity.
        rectangleTool | rt: (create, edit, query) - Activates the rectangle tool. When queried, returns true if the rectangle tool is active.
        refreshLayerManager | rlm: (create, edit, query) - Refresh the layer manager.
        refreshTimelineDisplay | rtd: (create, edit, query) - Refresh the timeline display frames.
        resetTool | r: (create, edit, query) - Restore tool settings to default values.
        textFontFamily | tff: (create, edit, query) - Sets the text font family.
        textOptions | txo: (create, edit, query) - Sets the text options. The arguments in order are size, opacity, font family name.
        textTool | tt: (create, edit, query) - Activates the text tool. When queried, returns true if the text tool is active.
        timelineFrameDisplay | tfd: (create, edit, query) - Sets the display mode for blue pencil frames in the timeline. Modes:  0 Show always 1 Show when context is active 2 Hide
        transform | t: (create, edit, query) - Activates the transform tool context. When queried, returns true if the transform tool context is active.
    """
    ...


def boneLattice(*args, after: bool = ..., af: bool = ..., afterReference: bool = ..., ar: bool = ..., before: bool = ..., bf: bool = ..., bicep: Optional[Union[float, bool]] = ..., bi: Optional[Union[float, bool]] = ..., components: bool = ..., cmp: bool = ..., deformerTools: bool = ..., dt: bool = ..., exclusive: Optional[Union[str, bool]] = ..., ex: Optional[Union[str, bool]] = ..., frontOfChain: bool = ..., foc: bool = ..., geometry: Optional[Union[str, bool]] = ..., g: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., gi: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., ihs: bool = ..., joint: Optional[Union[str, bool]] = ..., j: Optional[Union[str, bool]] = ..., lengthIn: Optional[Union[float, bool]] = ..., li: Optional[Union[float, bool]] = ..., lengthOut: Optional[Union[float, bool]] = ..., lo: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., parallel: bool = ..., par: bool = ..., prune: bool = ..., pr: bool = ..., remove: bool = ..., rm: bool = ..., selectedComponents: bool = ..., cms: bool = ..., split: bool = ..., sp: bool = ..., transform: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ..., tricep: Optional[Union[float, bool]] = ..., tr: Optional[Union[float, bool]] = ..., useComponentTags: bool = ..., uct: bool = ..., widthLeft: Optional[Union[float, bool]] = ..., wl: Optional[Union[float, bool]] = ..., widthRight: Optional[Union[float, bool]] = ..., wr: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates/edits/queries a boneLattice deformer. The name of
    the created/edited object is returned. Usually you would make use of
    this functionality through the higher level flexor command.

    Args:
        after | af: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference | ar: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before | bf: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        bicep | bi: (create, edit, query) - Affects the bulging of lattice points on the inside of the bend. Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.
        components | cmp: (query) - Returns the components used by the deformer
        deformerTools | dt: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        exclusive | ex: (create, query) - Puts the deformation set in a deform partition.
        frontOfChain | foc: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry | g: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices | gi: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected | ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections | ihs: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        joint | j: (create, edit, query) - Specifies which joint will be used to drive the bulging behaviors.
        lengthIn | li: (create, edit, query) - Affects the location of lattice points along the upper half of the bone. Positive/negative values cause the points to move away/towards the center of the bone.  Changing this parameter also modifies the regions affected by the creasing, rounding and width parameters. Default value is 0.0. When queried, this flag returns a float.
        lengthOut | lo: (create, edit, query) - Affects the location of lattice points along the lower half of the bone. Positive/negative values cause the points to move away/towards the center of the bone.  Changing this parameter also modifies the regions affected by the creasing, rounding and width parameters. Default value is 0.0. When queried, this flag returns a float.
        name | n: (create) - Used to specify the name of the node being created.
        parallel | par: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        prune | pr: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        remove | rm: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        selectedComponents | cms: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        split | sp: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        transform | t: (create) - Specifies which dag node is being used to rigidly transform the lattice which this node is going to deform.  If this flag is not specified an identity matrix will be assumed.
        tricep | tr: (create, edit, query) - Affects the bulging of lattice points on the outside of the bend. Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.
        useComponentTags | uct: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
        widthLeft | wl: (create, edit, query) - Affects the bulging of lattice points on the left side of the bend. Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.
        widthRight | wr: (create, edit, query) - Affects the bulging of lattice points on the right side of the bend. Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.
    """
    ...


def bufferCurve(*args, animation: Optional[Union[str, bool]] = ..., an: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., controlPoints: bool = ..., cp: bool = ..., exists: bool = ..., ex: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., f: Optional[Union[Tuple[float, float], bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., hi: Optional[Union[str, bool]] = ..., includeUpperBound: bool = ..., iub: bool = ..., index: Optional[Union[int, bool]] = ..., overwrite: bool = ..., ov: bool = ..., shape: bool = ..., s: bool = ..., swap: bool = ..., sw: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., t: Optional[Union[Tuple[float, float], bool]] = ..., useReferencedCurve: bool = ..., urc: bool = ..., query: bool = ...) -> Any:
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
        animation | an: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute | at: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        controlPoints | cp: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        exists | ex: (query) - Returns true if a buffer curve currently exists on the specified attribute; false otherwise.
        float | f: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        hierarchy | hi: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        includeUpperBound | iub: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index | index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        overwrite | ov: (create) - Create a buffer curve.  "true" means create a buffer curve whether or not one already existed.  "false" means if a buffer curve exists already then leave it alone.  If no flag is specified, then the command defaults to -overwrite false
        shape | s: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        swap | sw: (create) - For animated attributes which have buffer curves, swap the buffer curve with the current animation curve
        time | t: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
        useReferencedCurve | urc: (create, query) - In create mode, sets the buffer curve to the referenced curve. Curves which are not from file references will ignore this flag. In query mode, returns true if the selected keys are displaying their referenced curve as the buffer curve, and false if they are not.
    """
    ...


def buildBookmarkMenu(*args, editor: Optional[Union[str, bool]] = ..., ed: Optional[Union[str, bool]] = ..., type: Optional[Union[str, bool]] = ..., typ: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This command handles building the "dynamic" Bookmark
    menu, to show all bookmarks ("sets") of a specified
    type ("sets -text")
    
    menuName is the string returned by the "menu" command.

    Args:
        editor | ed: (create) - Name of the editor which this menu belongs to
        type | typ: (create) - Type of bookmark (sets -text) to display
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


def cacheEvaluator(*args, cacheFillMode: Optional[Union[str, bool]] = ..., cfm: Optional[Union[str, bool]] = ..., cacheFillOrder: Optional[Union[str, bool]] = ..., cfo: Optional[Union[str, bool]] = ..., cacheInvalidate: Optional[Union[Tuple[float, float], bool]] = ..., ci: Optional[Union[Tuple[float, float], bool]] = ..., cacheName: Optional[Union[str, bool]] = ..., cn: Optional[Union[str, bool]] = ..., cachedFrames: bool = ..., cfs: bool = ..., cachingPoints: bool = ..., cps: bool = ..., creationParameters: bool = ..., cp: bool = ..., delegateEvaluation: bool = ..., de: bool = ..., dynamicsAsyncRefresh: bool = ..., dar: bool = ..., dynamicsSupportActive: bool = ..., dsa: bool = ..., dynamicsSupportEnabled: bool = ..., dse: bool = ..., flushCache: Optional[Union[str, bool]] = ..., fc: Optional[Union[str, bool]] = ..., flushCacheRange: Optional[Union[Tuple[Tuple[float, float], bool], bool]] = ..., fcr: Optional[Union[Tuple[Tuple[float, float], bool], bool]] = ..., flushCacheSync: bool = ..., fcs: bool = ..., flushCacheWait: bool = ..., fcw: bool = ..., hybridCacheMode: Optional[Union[str, bool]] = ..., hcm: Optional[Union[str, bool]] = ..., layeredEvaluationActive: bool = ..., lea: bool = ..., layeredEvaluationCachingPoints: bool = ..., lec: bool = ..., layeredEvaluationEnabled: bool = ..., lee: bool = ..., listCacheNames: bool = ..., lcn: bool = ..., listCachedNodes: bool = ..., lcd: bool = ..., listValueNames: bool = ..., lvn: bool = ..., newAction: Optional[Union[str, bool]] = ..., na: Optional[Union[str, bool]] = ..., newActionParam: Optional[Union[str, bool]] = ..., nap: Optional[Union[str, bool]] = ..., newFilter: Optional[Union[str, bool]] = ..., nf: Optional[Union[str, bool]] = ..., newFilterParam: Optional[Union[str, bool]] = ..., nfp: Optional[Union[str, bool]] = ..., newRule: Optional[Union[str, bool]] = ..., nr: Optional[Union[str, bool]] = ..., newRuleParam: Optional[Union[str, bool]] = ..., nrp: Optional[Union[str, bool]] = ..., pauseInvalidation: bool = ..., pi: bool = ..., preventFrameSkip: bool = ..., pfs: bool = ..., resetRules: bool = ..., rr: bool = ..., resourceUsage: bool = ..., ru: bool = ..., resumeInvalidation: bool = ..., ri: bool = ..., safeMode: bool = ..., sf: bool = ..., safeModeMessages: bool = ..., sfm: bool = ..., safeModeTriggered: bool = ..., sft: bool = ..., valueName: Optional[Union[str, bool]] = ..., vn: Optional[Union[str, bool]] = ..., waitForCache: Optional[Union[float, bool]] = ..., wfc: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        cacheFillMode | cfm: (create, query) - Specifies the cache fill mode. Valid values are: "syncOnly" to fill cache during playback, "syncAsync" to cache during playback and in background,  and "asyncOnly" to fill cache only in background. Query returns current mode.
        cacheFillOrder | cfo: (create, query) - Specifies in which order the cache fills the timeline. Valid values are: "forward" to fill cache in forward direction, "backward" to fill cache backwards, "bidirectional" to fill cache in forward and backward directions simultaneously,  and "forwardFromBegin" to fill cache in forward direction from animation start.  Query returns current cache fill mode.
        cacheInvalidate | ci: (create) - Specifies the frame range in which cache should be invalidated. The range should be specified as a pair of positive integers.      Usage examples:       -ci "10:20"{Python equivalent: ('10','20')} means all frames         in the range from 10 to 20, inclusive, in the current time unit.        Omitting one end of a range means using either end of the animation range      (or both), as in the following examples:       -ci "10:" means all frames from time 10 (in the current time unit)         onwards to the maximum time in the animation range (on the timeline).   -ci ":10" means all frames from the minimum time on the animation range         (on the timeline) up to (and including) time 10 (in the current time unit).   -ci ":" is a short form to specify all frames, from minimum to         maximum time on the current animation range.
        cacheName | cn: (query) - Specifies the name of the cache from which to query a value. 			In query mode, this flag needs a value.
        cachedFrames | cfs: (query) - Get the list of frames with valid cache data. The result is an integer array containing multiple triplets of (cache-status, begin-frame, end-frame) For example, The result is an array of 9 integers [(0b01, 1, 3), (0b10, 7, 10), (0b11, 13, 15)]. In MEL, the result is typed as "int[9]". In Python, the result is typed as "Tuple[int,int,int][3]". The result suggests frames 1:3 (1,2,3), 7:10 (7,8,9,19), and 13:15 (13,14,15) are cached. No other frames contain valid cache data. The cache-status numbers are always 1 if "layeredEvaluationActive" is false. The cache-status can be one of {1,2,3}, when "layeredEvaluationActive" is true. It represents whether the frame is valid on animation cache or dynamics cache, the encoding is:  1 (0b01) : only animation cache is valid 2 (0b10) : only dynamics cache is valid 3 (0b11) : both animation and dynamics cache are valid  In the above example, it suggests: frames 1:3 are only valid in animation cache. frames 7:10 are only valid in dynamics cache. frames 13:15 are valid in both and considered as 'fully-cached'.
        cachingPoints | cps: (query) - Get list of nodes marked as caching points, i.e. nodes with at least one type of cache active.
        creationParameters | cp: (query) - Get the current mode creation parameters.  The result is a JSON string which represents an array with an element for each rule.  Each element is an association between the parameter name and its value when creating the rule.
        delegateEvaluation | de: (query) - Returns whether the specified node(s) are delegating to evaluation.
        dynamicsAsyncRefresh | dar: (create, query) - Enable / Disable Asynchronous Refresh in Dynamics Support mode. Traditionally, edits related to the simulation system require the user to re-playback the scene to see the result. When Asynchronous Refresh is active, Maya will process the simulation in the background and refresh the viewport once the result is ready. Note, the automatic refresh will not happen if the frame contains temproary edits. For example, an object is moved without setting the keyframe.
        dynamicsSupportActive | dsa: (query) - Query if the Dynamics Support mode is active. Dynamics Support mode is used to support Physics Simulation, such as Hair, or Fluid. It will be activated if such nodes are detected in the scene, and "enableDynamicsSupport" is set to true. When Dynamics Support mode is active, you will notice the following behavior:  Dynamics nodes will be frozen for uncached frame A separate dynamics cache line will appear on the Time Slider Dynamics cache starts after the animation cache was filled Dynamics cache only fills in the background Dynamics cache always fills forward from the beginning Dynamics cache evaluation may refresh foreground dynamics nodes (see the flag "dynamicsAsyncRefresh")
        dynamicsSupportEnabled | dse: (create, query) - Specifies if Dynamics nodes are allowed to participate in Cached Playback When disabled, Dynamics nodes will trigger "Safe mode" and prevent caching. When enabled, Dynamics nodes will participate in caching and trigger "Dynamics support mode". For more information check flag "dynamicsSupportActive".
        flushCache | fc: (create) - Specifies to flush the current cache. Valid values are: "keep" to store the existing cache as backup, and "destroy" to delete the current cache.
        flushCacheRange | fcr: (create) - Specifies the frame range in which cache should be flushed. By default it will destroy the cache - if the 'flushCache' is also set then it will define what to do with the cache range being flushed. The range should be specified as a pair of positive integers and a boolean.      Usage examples:       -flushCacheRange "10:20" on {Python equivalent: ('10','20',True)}                 means all frames in the range from 10 to 20, inclusive, in the current time unit.   -flushCacheRange "12:18" off {Python equivalent: ('12','18',False)}                 means all frames before 12 and after 18, not inclusive, in the current time unit.        Omitting one end of a range means using either end of the animation range      (or both), as in the following examples:       -flushCacheRange "10:" on means all frames from time 10 (in the current time unit)         onwards to the maximum time in the animation range (on the timeline).   -flushCacheRange ":10" on means all frames from the minimum time on the animation range         (on the timeline) up to (and including) time 10 (in the current time unit).   -flushCacheRange ":" on is a short form to specify all frames, from minimum to         maximum time on the current animation range.
        flushCacheSync | fcs: (create, query) - Specifies how to flush the cache: synchronously or asynchronously. True for synchronous, False for asynchronous.
        flushCacheWait | fcw: (create) - Wait for the cache destruction to be completed.
        hybridCacheMode | hcm: (create, query) - Specifies the hybrid cache mode. Valid values are: "disabled", not to use hybrid cache; "smp", to evaluate on the GPU meshes with GPU-supported deformation stacks if they use Smooth Mesh Preview (instead of caching them); "all", to evaluate on the GPU all meshes with PU-supported deformation stacks (instead of caching them). Query returns current mode.
        layeredEvaluationActive | lea: (query) - Query if the Layered Evaluation mode is active. When Layered Evaluation is active, the background cache fill process will be split into multiple passes for different contents (evaluation nodes). These contents are referred as different 'evaluation layers', representing different level of details (LoD) in animation evaluation. For example:  The first layer contains regular animations like a character motion.  The second layer contains dynamics simulations like a character's hair and cloth.   Maya will create separated cache and cache fill pass for each of the layers. Additional cache bars will be added to the Time Slider UI to represent these layers. The background cache fill pass for each of the layer will start in order. In the above example, two passes of background cache fill will be observed. In the first pass of background-cache-fill or playback-fill, only Character motions will be evaluated and filled, Hair and Clothes are frozen in-place. After the cache for first layer have been filled for all the frames, the second pass of cache fill will start to simulate Hairs and Clothes physics and fill the cache for the 2nd layer. Once the cache for the 2nd layer is filled for a frame, users can scrub the timeline to view the fully updated effects. Note, when layered evaluation is active, any foreground playback or manipulation will only evaluate the first evaluation layer, and all the FX contents will be frozen in the viewport until the background simulation is complete. For example, when rotating a character’s head, its hair will not follow in real time. If the flag "dynamicsAsyncRefresh" is enabled, the FX contents will be updated automatically after simulation cached up. Please refer to the flag for more detail.
        layeredEvaluationCachingPoints | lec: (query) - Get the list of nodes marked as caching points because of layered evaluation.
        layeredEvaluationEnabled | lee: (create, query) - Enable / Disable Layered Evaluation in Dynamics Support mode. Refering to flags "dynamicsSupportActive" and "layeredEvaluationActive" for details about layered evaluation enabled behavior. This flag is provided to support plugin developers for testing purpose. Disabling this option in production is not recommended. When disabled, dynamics nodes will share the same cache with regular animation. Allows dynamics nodes to be evaluated and stored to cache in the foreground. Background "cacheFillOrder" option will be locked to "forwardFromBegin". When used with cacheFillMode="syncOnly", it can also be used to support legacy dynamics nodes that cannot evaluate in the background.
        listCacheNames | lcn: (query) - Return the list of existing cache names.
        listCachedNodes | lcd: (query) - Returns the list of cached nodes.
        listValueNames | lvn: (query) - Return the list of value names that can be queried for the given cache.
        newAction | na: (create) - Specifies the name of the new action to create in the new filter/action rule.
        newActionParam | nap: (create) - Specifies the parameter string to pass to the new action to create in the new filter/action rule.
        newFilter | nf: (create) - Specifies the name of the new filter to create in the new filter/action rule.
        newFilterParam | nfp: (create) - Specifies the parameter string to pass to the new filter to create in the new filter/action rule.
        newRule | nr: (create) - Specifies the name of the new rule to create.
        newRuleParam | nrp: (create) - Specifies the parameter string to pass to the new rule to create.
        pauseInvalidation | pi: (create, query) - Pause all incoming invalidation of the cache. Work in symmetry with resumeInvalidation flag. PauseInvalidation can be called several time, useful in nesting situation. The same number of resume need to be called to resume the invalidation. If queried it will return how much time caching is paused, 0 means it is resumed.
        preventFrameSkip | pfs: (create, query) - Specifies if frame skipping is enabled. Following behavior is seen when frame skipping is enabled, and playback is set to play in real-time.  If cache can't be filled at real-time frame rate, frames will NOT be skipped. Once all frames have been looped over(and therefore all frames are cached), and if     playing back from cache still can't be done at real-time frame rate; frames WILL be skipped. If memory limit is reached before all frames are cached, frames WILL be skipped. If cache is invalidated will playing(like flushing it), frames will NOT     be skipped(until the cache is full again).
        resetRules | rr: (create) - Reset the cache configuration rules to an empty set of rules.
        resourceUsage | ru: (query) - Returns the current state of the resource usage as a string. 'unlimited' = the resource limits are being ignored, 'out' = the memory limit has been reached, 'low' = the memory usage is at 90% of the specified limit, 'okay' = memory usage is under 90% of the specified limit.
        resumeInvalidation | ri: (create, query) - Resume all incoming invalidation of the cache. Work in symmetry with pauseInvalidation flag. PauseInvalidation can be called several time, useful in nesting situation. The same number of resume need to be called to resume the invalidation. If queried it will return true if cache is resumed, false otherwise.
        safeMode | sf: (create, query) - Turns safe mode on or off. In query mode, it returns the status of the safe mode for cache evaluator.
        safeModeMessages | sfm: (query) - Prints the safe mode messages to the console.
        safeModeTriggered | sft: (query) - Returns if the safe mode was triggered for cache evaluator.
        valueName | vn: (query) - Specifies the name of the parameter for which to query the value. 			In query mode, this flag needs a value.
        waitForCache | wfc: (create) - Specifies to wait for cache to fill in background, with [Time to wait in seconds] timeout.
    """
    ...


def character(*args, addElement: str = ..., add: str = ..., addOffsetObject: Optional[Union[str, bool]] = ..., aoo: Optional[Union[str, bool]] = ..., anyMember: Optional[Union[str, bool]] = ..., am: Optional[Union[str, bool]] = ..., characterPlug: bool = ..., cp: bool = ..., clear: str = ..., cl: str = ..., empty: bool = ..., em: bool = ..., excludeDynamic: bool = ..., ed: bool = ..., excludeRotate: bool = ..., er: bool = ..., excludeScale: bool = ..., es: bool = ..., excludeTranslate: bool = ..., et: bool = ..., excludeVisibility: bool = ..., ev: bool = ..., flatten: str = ..., fl: str = ..., forceElement: str = ..., fe: str = ..., include: str = ..., intersection: Optional[Union[str, bool]] = ..., int: Optional[Union[str, bool]] = ..., isIntersecting: Optional[Union[str, bool]] = ..., ii: Optional[Union[str, bool]] = ..., isMember: Optional[Union[str, bool]] = ..., im: Optional[Union[str, bool]] = ..., library: bool = ..., lib: bool = ..., memberIndex: Optional[Union[int, bool]] = ..., mi: Optional[Union[int, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., noWarnings: bool = ..., nw: bool = ..., nodesOnly: bool = ..., no: bool = ..., offsetNode: bool = ..., ofs: bool = ..., remove: str = ..., rm: str = ..., removeOffsetObject: str = ..., roo: str = ..., root: Optional[Union[str, bool]] = ..., rt: Optional[Union[str, bool]] = ..., scheduler: bool = ..., sc: bool = ..., split: Optional[Union[str, bool]] = ..., sp: Optional[Union[str, bool]] = ..., subtract: Optional[Union[str, bool]] = ..., sub: Optional[Union[str, bool]] = ..., text: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ..., union: Optional[Union[str, bool]] = ..., un: Optional[Union[str, bool]] = ..., userAlias: Optional[Union[str, bool]] = ..., ua: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to manage the membership of a character.  Characters
    are a type of set that gathers together the attributes of a node or nodes
    that a user wishes to animate as a single entity.

    Args:
        addElement | add: (edit) - Adds the list of items to the given character.  If some of the items cannot be added to the character because they are in another character, the command will fail.  When another character is passed to to -addElement, is is added as a sub character.  When a node is passed in, it is expanded into its keyable attributes, which are then added to the character.
        addOffsetObject | aoo: (edit, query) - Indicates that the selected character member objects should be used when calculating and applying offsets. The flag argument is used to specify the character.
        anyMember | am: (create) - An operation which tests whether any of the given items are members of the given set.
        characterPlug | cp: (query) - Returns the plug on the character that corresponds to the specified character member.
        clear | cl: (edit) - An operation which removes all items from the given character.
        empty | em: (create) - Indicates that the character to be created should be empty. (i.e. it ignores any arguments identifying objects to be added to the character.
        excludeDynamic | ed: (create) - When creating the character, exclude dynamic attributes.
        excludeRotate | er: (create) - When creating the character, exclude rotate attributes from transform-type nodes.
        excludeScale | es: (create) - When creating the character, exclude scale attributes from transform-type nodes.
        excludeTranslate | et: (create) - When creating the character, exclude translate attributes from transform-type nodes. For example, if your character contains joints only, perhaps you only want to include rotations in the character.
        excludeVisibility | ev: (create) - When creating the character, exclude visibility attribute from transform-type nodes.
        flatten | fl: (edit) - An operation that flattens the structure of the given character. That is, any characters contained by the given character will be replaced by its members so that the character no longer contains other characters but contains the other characters' members.
        forceElement | fe: (edit) - For use in edit mode only. Forces addition of the items to the character. If the items are in another character which is in the character partition, the items will be removed from the other character in order to keep the characters in the character partition mutually exclusive with respect to membership.
        include | include: (edit) - Adds the list of items to the given character.  If some of the items cannot be added to the character, a warning will be issued. This is a less strict version of the -add/addElement operation.
        intersection | int: (query) - An operation that returns a list of items which are members of all the character in the list.  In general, characters should be mutually exclusive.
        isIntersecting | ii: (query) - An operation which tests whether or not the characters in the list have common members.  In general, characters should be mutually exclusive, so this should always return false.
        isMember | im: (query) - An operation which tests whether or not all the given items are members of the given character.
        library | lib: (query) - Returns the clip library associated with this character, if there is one. A clip library will only exist if you have created clips on your character.
        memberIndex | mi: (query) - Returns the memberIndex of the specified character member if used after the query flag. Or if used before the query flag, returns the member that corresponds to the specified index.
        name | n: (create) - Assigns string as the name for a new character. Valid for operations that create a new character.
        noWarnings | nw: (create) - Indicates that warning messages should not be reported such as when trying to add an invalid item to a character. (used by UI)
        nodesOnly | no: (query) - This flag modifies the results of character membership queries. When listing the attributes (e.g. sphere1.tx) contained in the character, list only the nodes.  Each node will only be listed once, even if more than one attribute or component of the node exists in the character.
        offsetNode | ofs: (query) - Returns the name of the characterOffset node used to add offsets to the root of the character.
        remove | rm: (edit) - Removes the list of items from the given character.
        removeOffsetObject | roo: (edit) - Indicates that the selected character offset objects should be removed as offsets. The flag argument is used to specify the character.
        root | rt: (create) - Specifies the transform node which will act as the root of the character being created. This creates a characterOffset node in addition to the character node, which can be used to add offsets to the character to change the direction of the character's animtion without inserting additional nodes in its hierarchy.
        scheduler | sc: (query) - Returns the scheduler associated with this character, if there is one. A scheduler will only exist if you have created clips on your character.
        split | sp: (create) - Produces a new set with the list of items and removes each item in the list of items from the given set.
        subtract | sub: (query) - An operation between two characters which returns the members of the first character that are not in the second character. In general, characters should be mutually exclusive.
        text | t: (create, edit, query) - Defines an annotation string to be stored with the character.
        union | un: (query) - An operation that returns a list of all the members of all characters listed.
        userAlias | ua: (query) - Returns the user defined alias for the given attribute on the character or and empty string if there is not one.  Characters automatically alias the attributes where character animation data is stored.  A user alias will exist when the automatic aliases are overridden using the aliasAttr command.
    """
    ...


def characterize(*args, activatePivot: bool = ..., apv: bool = ..., addAuxEffector: bool = ..., aae: bool = ..., addFloorContactPlane: bool = ..., afp: bool = ..., addMissingEffectors: bool = ..., ame: bool = ..., attributeFromHIKProperty: Optional[Union[str, bool]] = ..., ahk: Optional[Union[str, bool]] = ..., attributeFromHIKPropertyMode: Optional[Union[str, bool]] = ..., mhk: Optional[Union[str, bool]] = ..., autoActivateBodyPart: bool = ..., aab: bool = ..., changePivotPlacement: bool = ..., cpp: bool = ..., effectors: Optional[Union[str, bool]] = ..., ef: Optional[Union[str, bool]] = ..., fkSkeleton: Optional[Union[str, bool]] = ..., fk: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., nm: Optional[Union[str, bool]] = ..., pinHandFeet: bool = ..., phf: bool = ..., placeNewPivot: bool = ..., pnp: bool = ..., posture: Optional[Union[str, bool]] = ..., pos: Optional[Union[str, bool]] = ..., sourceSkeleton: Optional[Union[str, bool]] = ..., sk: Optional[Union[str, bool]] = ..., stancePose: Optional[Union[str, bool]] = ..., sp: Optional[Union[str, bool]] = ..., type: Optional[Union[str, bool]] = ..., typ: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        activatePivot | apv: (edit) - Activates a pivot that has been properly placed.  After activating this new pivot, you will now be able to rotate and translate about this pivot. A pivot behaves in all ways the same as an effector (it IS an effector, except that it is offset from the normal position of the effector to allow one to rotate about a different point.
        addAuxEffector | aae: (edit) - Adds an auxilliary (secondary) effector to an existing effector.
        addFloorContactPlane | afp: (edit) - Adds a floor contact plane to one of the hands or feet.  With this plane, you will be able to adjust the floor contact height.  Select a hand or foot effector and then issue the characterize command with this flag.
        addMissingEffectors | ame: (edit) - This flag tells the characterize command to look for any effectors that can be added to the skeleton. For example, if the user has deleted some effectors or added fingers to an existing skeleton, "characterize -e -addMissingEffectors" can be used to restore them.
        attributeFromHIKProperty | ahk: (query) - Query for the attribute name associated with a MotionBuilder property.
        attributeFromHIKPropertyMode | mhk: (query) - Query for the attribute name associated with a MotionBuilder property mode.
        autoActivateBodyPart | aab: (edit, query) - Query or change whether auto activation of character nodes representing body parts should be enabled.
        changePivotPlacement | cpp: (edit) - Reverts a pivot back into pivot placement mode.  A pivot that is in placement mode will not participate in full body manipulation until it has been activated with the -activatePivot flag.
        effectors | ef: (create) - Specify the effectors to be used by human IK by providing 2 pieces of information for each effector:  1) the partial path of the effector and 2) the name of the full body effector this represents.  1) and 2) are to be separated by white space, and multiple entries separated by ",". Normally, the effectors are automatically created.  This flag is for advanced users only.
        fkSkeleton | fk: (create, edit) - Specify the fk skeleton to be used by human IK by providing 2 pieces of information for each joint of the FK skeleton:  1) the partial path of the joint and 2) the name of the full body joint this represents.  1) and 2) are to be separated by white space, and multiple entries separated by ",". Normally, the fk control skeleton is automatically created.  This flag is for advanced users only.
        name | nm: (create) - At characterization (FBIK creation) time, use this flag to name your FBIK character. This will affect the name of the hikHandle node and the control rig will be put into a namespace that matches the name of your character.  If you do not specify the character name, a default one will be used. At the moment edit and query of the character name is not supported.
        pinHandFeet | phf: (create) - When the character is first being characterized, pin the hands and feet by default.
        placeNewPivot | pnp: (edit) - Creates a new pivot and puts it into placement mode.  Note that you will not be able to do full body manipulation about this pivot until you have activated it with the -activatePivot flag. A pivot behaves in all ways the same as an effector (it IS an effector, except that it is offset from the normal position of the effector to allow one to rotate about a different point). A new pivot created with this flag allow you to adjust the offset interactively before activating it.
        posture | pos: (create) - Specifies the posture of the character. Valid options are "biped" and "quadruped". The default is "biped".
        sourceSkeleton | sk: (create, edit) - This flag can be used to characterize a skeleton that has not been named or labelled according to the FBIK guidelines. It specifies the association between the actual joint names and the expected FBIK joint names. The format of the string is as follows: For each joint that the user wants to involve in the solve:  1) the partial path of the joint and 2) the name of the full body joint this represents.  1) and 2) are to be separated by white space, and multiple entries separated by ",".
        stancePose | sp: (create, query) - Specify the default stance pose to be used by human IK.  The stance pose is specified by providing 2 pieces of information for each joint involved in the solve: 1) the partial path to the joint and 2) 9 numbers representing translation rotation and scale. 1) and 2) are to be separated by white space, and multiple entries separated by ",". Normally, the stance pose is taken from the selected skeleton.  This flag is for advanced users only.
        type | typ: (create) - Specifies the technique used by the characterization to identify the joint type. Valid options are "label" and "name". When "label" is used, the joints must be labelled using the guidelines described in the Maya documentation. When name is used, the joint names must follow the naming conventions described in the Maya documentation. The default is "name". This flag cannot be used in conjunction with the sourceSkeleton flag.
    """
    ...


def characterMap(*args, mapAttr: Optional[Union[Tuple[str, str], bool]] = ..., ma: Optional[Union[Tuple[str, str], bool]] = ..., mapMethod: Optional[Union[str, bool]] = ..., mm: Optional[Union[str, bool]] = ..., mapNode: Optional[Union[Tuple[str, str], bool]] = ..., mn: Optional[Union[Tuple[str, str], bool]] = ..., mapping: Optional[Union[str, bool]] = ..., m: Optional[Union[str, bool]] = ..., proposedMapping: bool = ..., pm: bool = ..., unmapAttr: Optional[Union[Tuple[str, str], bool]] = ..., ua: Optional[Union[Tuple[str, str], bool]] = ..., unmapNode: Optional[Union[Tuple[str, str], bool]] = ..., umn: Optional[Union[Tuple[str, str], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to create a correlation between the attributes of 2 or more characters.

    Args:
        mapAttr | ma: (create, edit, query) - In query mode, this flag can be used to query the mapping stored by the specified map node. It returns an array of strings. In non-query mode, this flag can be used to create a mapping between the specified character members. Any previous mapping on the attributes is removed in favor of the newly specified mapping.
        mapMethod | mm: (create) - This is is valid in create mode only. It specifies how the mapping should be done. Valid options are: "byNodeName", "byAttrName", and "byAttrOrder". "byAttrOrder" is the default. The flags mean the following: "byAttrOrder" maps using the order that the character stores the attributes internally, "byAttrName" uses the attribute name to find a correspondence, "byNodeName" uses the node name *and* the attribute name to find a correspondence.
        mapNode | mn: (create, query) - This flag can be used to map all the attributes on the source node to their matching attributes on the destination node.
        mapping | m: (query) - This flag is valid in query mode only. It must be used before the query flag with a string argument. It is used for querying the mapping for a particular attribute.  A string array is returned.
        proposedMapping | pm: (query) - This flag is valid in query mode only. It is used to get an array of the mapping that the character map would prvide if called with the specified characters and the (optional) specified mappingMethod. If a character map exists on the characters, the map is not affected by the query operation.  A string array is returned.
        unmapAttr | ua: (create, edit) - This flag can be used to unmap the mapping stored by the specified map node.
        unmapNode | umn: (create) - This flag can be used to unmap all the attributes on the source node to their matching attributes on the destination node. Note that mapped attributes which do not have matching names, will not be unmapped.
    """
    ...


def choice(*args, attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., controlPoints: bool = ..., cp: bool = ..., index: Optional[Union[int, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., selector: Optional[Union[str, bool]] = ..., sl: Optional[Union[str, bool]] = ..., shape: bool = ..., s: bool = ..., sourceAttribute: Optional[Union[str, bool]] = ..., sa: Optional[Union[str, bool]] = ..., time: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., t: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        attribute | at: (create, multiuse) - specifies the attributes onto which choice node(s) should be created. The default is all keyable attributes of the given objects. Note that although this flag is not queryable, it can be used to qualify which attributes of the given objects to query.       In query mode, this flag needs a value.
        controlPoints | cp: (create) - Explicitly specify whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.
        index | index: (create, query) - specifies the multi-input index of the choice node to connect the source attribute to. When queried, returns a list of integers one per specified -t/time that indicates the multi-index of the choice node to use at that time.
        name | n: (create, query) - the name to give to any newly created choice node(s). When queried, returns a list of strings.
        selector | sl: (create, query) - specifies the attribute to be used as the choice node's selector. The value of the selector at a given time determines which of the choice node's multi-indices should be used as the output of the choice node at that time. This flag is only editable (it cannot be specified at creation time). When queried, returns a list of strings.
        shape | s: (create) - Consider all attributes of shapes below transforms as well, except "controlPoints". Default: true
        sourceAttribute | sa: (create) - specifies the attribute to connect to the choice node that will be selected at the given time(s) specified by -t/time.
        time | t: (create, multiuse) - specifies the time at which the choice should use the given source attribute, or the currently connected attribute if source attribute is not specified. The default is the curren time. Note that although this flag is not queryable, it can be used to qualify the times at which to query the other attributes.       In query mode, this flag needs a value.
    """
    ...


def clip(*args, absolute: bool = ..., abs: bool = ..., absoluteRotations: bool = ..., abr: bool = ..., active: Optional[Union[str, bool]] = ..., a: Optional[Union[str, bool]] = ..., addTrack: bool = ..., at: bool = ..., allAbsolute: bool = ..., aa: bool = ..., allClips: bool = ..., ac: bool = ..., allRelative: bool = ..., ar: bool = ..., allSourceClips: bool = ..., asc: bool = ..., animCurveRange: bool = ..., acr: bool = ..., character: bool = ..., ch: bool = ..., constraint: bool = ..., cn: bool = ..., copy: bool = ..., c: bool = ..., defaultAbsolute: bool = ..., da: bool = ..., duplicate: bool = ..., d: bool = ..., endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., end: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., expression: bool = ..., ex: bool = ..., ignoreSubcharacters: bool = ..., isolate: bool = ..., i: bool = ..., leaveOriginal: bool = ..., lo: bool = ..., mapMethod: Optional[Union[str, bool]] = ..., mm: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., newName: Optional[Union[str, bool]] = ..., nn: Optional[Union[str, bool]] = ..., paste: bool = ..., p: bool = ..., pasteInstance: bool = ..., pi: bool = ..., remove: bool = ..., rm: bool = ..., removeTrack: bool = ..., rt: bool = ..., rotationOffset: Optional[Union[Tuple[float, float, float], bool]] = ..., rof: Optional[Union[Tuple[float, float, float], bool]] = ..., rotationsAbsolute: bool = ..., ra: bool = ..., scheduleClip: bool = ..., sc: bool = ..., sourceClipName: bool = ..., scn: bool = ..., split: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., sp: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., s: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., translationOffset: Optional[Union[Tuple[float, float, float], bool]] = ..., tof: Optional[Union[Tuple[float, float, float], bool]] = ..., useChannel: Optional[Union[str, bool]] = ..., uc: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to create, edit and query character clips.

    Args:
        absolute | abs: (create) - This flag is now deprecated.  Use aa/allAbsolute, ar/allRelative, ra/rotationsAbsolute, or da/defaultAbsolute instead.  This flag controls whether the clip follows its keyframe values or whether they are offset by a value to maintain a smooth path. Default is true.
        absoluteRotations | abr: (create) - This flag is now deprecated.  Use aa/allAbsolute, ar/allRelative, ra/rotationsAbsolute, or da/defaultAbsolute instead. If true, this overrides the -absolute flag so that rotation channels are always calculated with absolute offsets. This allows you to have absolute offsets on rotations and relative offsets on all other channels.
        active | a: (edit, query) - Query or edit the active clip. This flag is not valid in create mode. Making a clip active causes its animCurves to be hooked directly to the character attributes in addition to being attached to the clip library node. This makes it easier to access the animCurves if you want to edit, delete or add additional animCruves to the clip.
        addTrack | at: () - This flag is now obsolete. Use the insertTrack flag on the clipSchedule command instead.
        allAbsolute | aa: (create) - Set all channels to be calculated with absolute offsets.  This flag cannot be used in conjunction with the ar/allRelative, ra/rotationsAbsolute or da/defaultAbsolute flags.
        allClips | ac: (query) - This flag is used to query all the clips in the scene. Nodes of type "animClip" that are storing poses, are not returned by this command.
        allRelative | ar: (create) - Set all channels to be calculated with relative offsets.  This flag cannot be used in conjunction with the aa/allAbsolute, ra/rotationsAbsolute or da/defaultAbsolute flags.
        allSourceClips | asc: (query) - This flag is used to query all the source clips in the scene. Nodes of type "animClip" that are storing poses or clip instances, are not returned by this command.
        animCurveRange | acr: (create) - This flag can be used at the time you create the clip instead of the startTime and endTime flags. It specifies that you want the range of the clip to span the range of keys in the clips associated animCurves.
        character | ch: (query) - This is a query only flag which operates on the specified clip. It returns the names of any characters that a clip is associated with.
        constraint | cn: (create) - This creates a clip out of any constraints on the character. The constraint will be moved off of the character and into the clip, so that it is only active for the duration of the clip, and its value can be scaled/offset/cycled according to the clip attributes.
        copy | c: (create, query) - This flag is used to copy a clip or clips to the clipboard. It should be used in conjunction with the name flag to copy the named clips on the specified character and its subcharacters. In query mode, this flag allows you to query what, if anything, has been copied into the clip clipboard.
        defaultAbsolute | da: (create) - Sets all top-level channels except rotations in the clip to relative, and the remaining channels to absolute. This is the default during clip creation if no offset flag is specified.  This flag cannot be used in conjunction with the aa/allAbsolute, ar/allRelative, or ra/rotationsAbsolute flags.
        duplicate | d: (query) - Duplicate the clip specified by the name flag. The start time of the new clip should be specified with the startTime flag.
        endTime | end: (create, edit, query) - Specify the clip end
        expression | ex: (create) - This creates a clip out of any expressions on the character. The expression will be moved off of the character and into the clip, so that it is only active for the duration of the clip, and its value can be scaled/offset/cycled according to the clip attributes.
        ignoreSubcharacters | ignoreSubcharacters: (create) - During clip creation, duplication and isolation, subcharacters are included by default. If you want to create a clip on the top level character only, or you want to duplicate the clip on the top level character without including subCharacters, use the ignoreSubcharacters flag.
        isolate | i: (create) - This flag should be used in conjunction with the name flag to specify that a clip or clips should be copied to a new clip library. The most common use of this flag is for export, when you want to only export certain clips from the character, without exporting all of the clips.
        leaveOriginal | lo: (create) - This flag is used when creating a clip to specify that the animation curves should be copied to the clip library, and left on the character.
        mapMethod | mm: (create) - This is is valid with the paste and pasteInstance flags only. It specifies how the mapping should be done. Valid options are: "byNodeName", "byAttrName", "byCharacterMap", "byAttrOrder", "byMapOrAttrName" and "byMapOrNodeName". "byAttrName" is the default. The flags mean the following: "byAttrOrder" maps using the order that the character stores the attributes internally, "byAttrName" uses the attribute name to find a correspondence, "byNodeName" uses the node name *and* the attribute name to find a correspondence, "byCharacterMap" uses the existing characterMap node to do the mapping. "byMapOrAttrName" uses a character map if one exists, otherwise uses the attribute name. "byMapOrNodeName" uses a character map if one exists, otherwise uses the attribute name.
        name | n: (create, multiuse, query) - In create mode, specify the clip name. In query mode, return a list of all the clips. In duplicate mode, specify the clip to be duplicated. In copy mode, specify the clip to be copied. This flag is multi-use, but multiple use is only supported with the copy flag. For use during create and with all other flags, only the first instance of the name flag will be utilized. 			In query mode, this flag can accept a value.
        newName | nn: (create) - Rename a clip. Must be used in conjunction with the clip name flag, which is used to specify the clip to be renamed.
        paste | p: (create) - This flag is used to paste a clip or clips from the clipboard to a character. Clips are added to the clipboard using the c/copy flag.
        pasteInstance | pi: (create) - This flag is used to paste an instance of a clip or clips from the clipboard to a character. Unlike the p/paste flag, which duplicates the animCurves from the original source clip, the pi/pasteInstance flag shares the animCurves from the source clip.
        remove | rm: (query) - Remove the clip specified by the name flag. The clip will be permanently removed from the library and deleted from any times where it has been scheduled.
        removeTrack | rt: (create) - This flag is now obsolete. Use removeTrack flag on the clipSchedule command instead.
        rotationOffset | rof: (create, query) - Return the channel offsets used to modify the clip's rotation.
        rotationsAbsolute | ra: (create) - Set all channels except rotations to be calculated with relative offsets.  Rotation channels will be calculated with absolute offsets.  This flag cannot be used in conjunction with the aa/allAbsolute, ar/allRelative or da/defaultAbsolute flags.
        scheduleClip | sc: (create) - This flag is used when creating a clip to specify whether or not the clip should immediately be scheduled at the current time. If the clip is not scheduled, the clip will be placed in the library for future use, but will not be placed on the timeline. This flag is for use only when creating a new clip or duplicating an existing. The default is true.
        sourceClipName | scn: (query) - This flag is for query only. It returns the name of the source clip that controls an instanced clip.
        split | sp: (create, edit) - Split an existing clip into two clips. The split occurs around the specified time.
        startTime | s: (create, edit, query) - Specify the clip start
        translationOffset | tof: (create, query) - Return the channel offsets used to modify the clip's translation.
        useChannel | uc: (create, multiuse) - Specify which channels should be acted on. This flag is valid only in conjunction with clip creation, and the isolate flag. The specified channels must be members of the character.
    """
    ...


def clipEditor(*args, allTrackHeights: int = ..., th: int = ..., autoFit: Optional[Union[str, bool]] = ..., af: Optional[Union[str, bool]] = ..., autoFitTime: Optional[Union[str, bool]] = ..., aft: Optional[Union[str, bool]] = ..., clipDropCmd: str = ..., cd: str = ..., clipStyle: Optional[Union[int, bool]] = ..., cs: Optional[Union[int, bool]] = ..., control: bool = ..., ctl: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., deleteCmd: str = ..., dc: str = ..., deselectAll: bool = ..., da: bool = ..., displayActiveKeyTangents: str = ..., dat: str = ..., displayActiveKeys: str = ..., dak: str = ..., displayInfinities: str = ..., di: str = ..., displayKeys: str = ..., dk: str = ..., displayTangents: str = ..., dtn: str = ..., displayValues: str = ..., dv: str = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., exists: bool = ..., ex: bool = ..., filter: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., fmc: Optional[Union[str, bool]] = ..., frameAll: bool = ..., fa: bool = ..., frameRange: Optional[Union[Tuple[float, float], bool]] = ..., fr: Optional[Union[Tuple[float, float], bool]] = ..., highlightConnection: Optional[Union[str, bool]] = ..., hlc: Optional[Union[str, bool]] = ..., highlightedBlend: Optional[Union[Tuple[str, str], bool]] = ..., hb: Optional[Union[Tuple[str, str], bool]] = ..., highlightedClip: Optional[Union[Tuple[str, str], bool]] = ..., hc: Optional[Union[Tuple[str, str], bool]] = ..., initialized: bool = ..., it: bool = ..., listAllCharacters: bool = ..., lac: bool = ..., listCurrentCharacters: bool = ..., lc: bool = ..., lockMainConnection: bool = ..., lck: bool = ..., lookAt: str = ..., la: str = ..., mainListConnection: Optional[Union[str, bool]] = ..., mlc: Optional[Union[str, bool]] = ..., manageSequencer: bool = ..., ms: bool = ..., menuContext: Optional[Union[str, bool]] = ..., mc: Optional[Union[str, bool]] = ..., panel: Optional[Union[str, bool]] = ..., pnl: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., selectBlend: Optional[Union[Tuple[str, str, str], bool]] = ..., sb: Optional[Union[Tuple[str, str, str], bool]] = ..., selectClip: Optional[Union[Tuple[str, str], bool]] = ..., sc: Optional[Union[Tuple[str, str], bool]] = ..., selectionConnection: Optional[Union[str, bool]] = ..., slc: Optional[Union[str, bool]] = ..., snapTime: Optional[Union[str, bool]] = ..., st: Optional[Union[str, bool]] = ..., snapValue: Optional[Union[str, bool]] = ..., sv: Optional[Union[str, bool]] = ..., stateString: bool = ..., sts: bool = ..., unParent: bool = ..., up: bool = ..., unlockMainConnection: bool = ..., ulk: bool = ..., updateMainConnection: bool = ..., upd: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Create a clip editor with the given name.

    Args:
        allTrackHeights | th: () - OBSOLETE flag. Use clipStyle instead.
        autoFit | af: (edit, query) - on | off | tgl Auto fit-to-view.
        autoFitTime | aft: (edit, query) - on | off | tgl Auto fit-to-view along the time axis, as well.
        clipDropCmd | cd: (edit) - Command executed when clip node is dropped on the TraX editor
        clipStyle | cs: (edit, query) - Set/return the clip track style in the specified editor. Default is 2. Valid values are 1-3.
        control | ctl: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        deleteCmd | dc: (edit) - Command executed when backspace key is pressed
        deselectAll | da: (edit) - Deselect all clips and blends in the editor.
        displayActiveKeyTangents | dat: (edit) - on | off | tgl Display active key tangents in the editor.
        displayActiveKeys | dak: (edit) - on | off | tgl Display active keys in the editor.
        displayInfinities | di: (edit) - on | off | tgl Display infinities in the editor.
        displayKeys | dk: (edit) - on | off | tgl Display keyframes in the editor.
        displayTangents | dtn: (edit) - on | off | tgl Display tangents in the editor.
        displayValues | dv: (edit) - on | off | tgl Display active keys and tangents values in the editor.
        docTag | dtg: (create, edit, query) - Attaches a tag to the editor.
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        filter | f: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        forceMainConnection | fmc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        frameAll | fa: (edit) - Frame view around all clips in the editor.
        frameRange | fr: (edit, query) - The editor's current frame range.
        highlightConnection | hlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        highlightedBlend | hb: (query) - Returns the highlighted blend, listed as scheduler and index
        highlightedClip | hc: (query) - Returns the highlighted clip, listed as scheduler and index
        initialized | it: (query) - Returns whether the clip editor is fully initialized, and has a port to draw through. If not, the -frameRange and -frameAll flags will fail.
        listAllCharacters | lac: (edit) - List all characters in the editor and outliner.
        listCurrentCharacters | lc: (edit) - List only the characters in the editor and outliner.
        lockMainConnection | lck: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        lookAt | la: (edit) - all | selected | currentTime FitView helpers.
        mainListConnection | mlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        manageSequencer | ms: (create, edit, query) - Sets/returns whether the clip editor should manage sequencer nodes.  If so, animation clips and characters are not represented.
        menuContext | mc: (query) - Returns a string array denoting the type of data object the cursor is over.  Returned values are: {"timeSlider"} {"nothing"} {"track", "track index", "character node name", "group name"} {"clip", "clip node name"}
        panel | pnl: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent | p: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        selectBlend | sb: (edit, query) - Select the blends specified by the scheduler name and the indicies of the two clips used in the blend. When queried, a string containing the scheduler name and the two clip indicies for all of the selected blends is returned.
        selectClip | sc: (edit, query) - Selects the clip specified by the scheduler name and the clip index. When queried, a string containing the scheduler and clip index of all of the selected clips is returned.
        selectionConnection | slc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        snapTime | st: (edit, query) - none | integer | keyframe Keyframe move snap in time.
        snapValue | sv: (edit, query) - none | integer | keyframe Keyframe move snap in values.
        stateString | sts: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        unParent | up: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection | ulk: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection | upd: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
    """
    ...


def clipMatching(*args, clipDst: Optional[Union[Tuple[str, float], bool]] = ..., cd: Optional[Union[Tuple[str, float], bool]] = ..., clipSrc: Optional[Union[Tuple[str, float], bool]] = ..., cs: Optional[Union[Tuple[str, float], bool]] = ..., matchRotation: Optional[Union[int, bool]] = ..., mr: Optional[Union[int, bool]] = ..., matchTranslation: Optional[Union[int, bool]] = ..., mt: Optional[Union[int, bool]] = ...) -> Any:
    r"""
    This command is used to compute an offset to apply on a source clip in order to
    automatically align it to a destination clip at a specified match element.
    For this command to work, offset objects must be specified for the character.

    Args:
        clipDst | cd: (create) - The clip to match so that the source clip can be offsetted correctly.  This flag takes in a clip name and the percentage value ranging from 0.0 to 1.0 in order to have the source clip match at a certain time in the destination clip.
        clipSrc | cs: (create) - The clip to offset so that it aligns with the destination clip.  This flag takes in a clip name and the percentage value ranging from 0.0 to 1.0 in order to have it match at a certain time in the clip.
        matchRotation | mr: (create) - This flag sets the rotation match type. By default, it is set to not match the rotation. 0 - None 1 - Match full rotation 2 - Match projected rotation on ground plane
        matchTranslation | mt: (create) - This flag sets the translation match type. By default, it is set to not match the translation. 0 - None 1 - Match full translation 2 - Match projected translation on ground plane
    """
    ...


def clipSchedule(*args, allAbsolute: bool = ..., aa: bool = ..., allRelative: bool = ..., ar: bool = ..., blend: Optional[Union[Tuple[int, int], bool]] = ..., b: Optional[Union[Tuple[int, int], bool]] = ..., blendNode: Optional[Union[Tuple[int, int], bool]] = ..., bn: Optional[Union[Tuple[int, int], bool]] = ..., blendUsingNode: Optional[Union[str, bool]] = ..., bun: Optional[Union[str, bool]] = ..., character: bool = ..., ch: bool = ..., clipIndex: Optional[Union[int, bool]] = ..., ci: Optional[Union[int, bool]] = ..., cycle: Optional[Union[float, bool]] = ..., c: Optional[Union[float, bool]] = ..., defaultAbsolute: bool = ..., da: bool = ..., enable: bool = ..., en: bool = ..., group: bool = ..., grp: bool = ..., groupIndex: Optional[Union[int, bool]] = ..., gri: Optional[Union[int, bool]] = ..., groupName: Optional[Union[str, bool]] = ..., gn: Optional[Union[str, bool]] = ..., hold: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., ph: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., insertTrack: Optional[Union[int, bool]] = ..., it: Optional[Union[int, bool]] = ..., instance: Optional[Union[str, bool]] = ..., listCurves: bool = ..., lc: bool = ..., listPairs: bool = ..., lp: bool = ..., lock: bool = ..., l: bool = ..., mute: bool = ..., m: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., postCycle: Optional[Union[float, bool]] = ..., poc: Optional[Union[float, bool]] = ..., preCycle: Optional[Union[float, bool]] = ..., prc: Optional[Union[float, bool]] = ..., remove: bool = ..., rm: bool = ..., removeBlend: Optional[Union[Tuple[int, int], bool]] = ..., rb: Optional[Union[Tuple[int, int], bool]] = ..., removeEmptyTracks: bool = ..., ret: bool = ..., removeTrack: Optional[Union[int, bool]] = ..., rt: Optional[Union[int, bool]] = ..., rotationsAbsolute: bool = ..., ra: bool = ..., scale: Optional[Union[float, bool]] = ..., sc: Optional[Union[float, bool]] = ..., shift: Optional[Union[int, bool]] = ..., sh: Optional[Union[int, bool]] = ..., shiftIndex: Optional[Union[int, bool]] = ..., shi: Optional[Union[int, bool]] = ..., solo: bool = ..., so: bool = ..., sourceClipName: bool = ..., scn: bool = ..., sourceEnd: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., se: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., sourceStart: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., ss: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., start: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., s: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., track: Optional[Union[int, bool]] = ..., t: Optional[Union[int, bool]] = ..., weight: Optional[Union[float, bool]] = ..., w: Optional[Union[float, bool]] = ..., weightStyle: Optional[Union[int, bool]] = ..., ws: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to create, edit and query clips and blends in the Trax editor. It operates on the clipScheduler node attached to the character. In query mode, if no flags are specified, returns an array of strings in this form:
     (clipName,clipIndex,clipStart,clipSourceStart,clipSourceEnd,clipScale,clipPreCycle,clipPostCycle,clipHold)

    Args:
        allAbsolute | aa: (edit, query) - Set all channels to be calculated with absolute offsets.  This flag cannot be used in conjunction with the ar/allRelative, ra/rotationsAbsolute or da/defaultAbsolute flags.
        allRelative | ar: (edit, query) - Set all channels to be calculated with relative offsets.  This flag cannot be used in conjunction with the aa/allAbsolute, ra/rotationsAbsolute or da/defaultAbsolute flags.
        blend | b: (create, query) - This flag is used to blend two clips, whose indices are provided as flag arguments.
        blendNode | bn: (query) - This query only flag list all of the blend nodes associated with the blend defined by the two clip indices. This flag returns a string array. 			In query mode, this flag can accept a value.
        blendUsingNode | bun: (create) - This flag is used to blend using an existing blend node. It is used in conjunction with the blend flag. The blend flag specifies the clip indices for the blend. The name of an existing animBlend node should be supplied supplied as an argument for the blendUsingNode flag.
        character | ch: (query) - This flag is used to query which characters this scheduler controls. It returns an array of strings.
        clipIndex | ci: (create, query) - Specify the index of the clip to schedule. In query mode, returns an array of strings in this form: (clipName,index,start,sourceStart,sourceEnd,scale,preCycle,postCycle) 			In query mode, this flag can accept a value.
        cycle | c: (create, query) - This flag is now obsolete. Use the postCycle flag instead.
        defaultAbsolute | da: (edit, query) - Sets all top-level channels except rotations in the clip to relative, and the remaining channels to absolute. This is the default during clip creation if no offset flag is specified.  This flag cannot be used in conjunction with the aa/allAbsolute, ar/allRelative, or ra/rotationsAbsolute flags.
        enable | en: (create, query) - This flag is used to enable or disable a clip. It must be used in conjunction with the ci/clipIndex flag. The specified clip will be enabled or disabled.
        group | grp: (create) - This flag is used to add (true) or remove (false) a list of clips (specified with groupIndex) into a group.
        groupIndex | gri: (create, multiuse) - This flag specifies a multiple number of clips to be added or removed from a group.
        groupName | gn: (create, query) - This flag is used to specify the group that should be added to.  If no group by that name exists and new group is created with that name.  By default if this is not specified a new group will be created.
        hold | ph: (create, query) - Specify how long to hold the last value of the clip after its normal or cycled end.
        insertTrack | it: (create) - This flag is used to insert a new empty track at the track index specified.
        instance | instance: (create) - Create an instanced copy of the named clip. An instanced clip is one that is linked to an original clip. Thus, changes to the animation curve of the original curve will also modify all instanced clips. The name of the instanced clip is returned as a string.
        listCurves | lc: (create, query) - This flag is used to list the animation curves associated with a clip. It should be used in conjunction with the clipIndex flag, which specifies the clip of interest.
        listPairs | lp: (query) - This query only flag returns a string array containing the channels in a character that are used by a clip and the names of the animation curves that drive the channels. Each string in the string array consists of the name of a channel, a space, and the name of the animation curve animating that channel. This flag must be used with the ci/clipIndex flag.
        lock | l: (edit, query) - This flag specifies whether clips on a track are to be locked or not. Must be used in conjuction with the track flag.
        mute | m: (edit, query) - This flag specifies whether clips on a track are to be muted or not. Must be used in conjuction with the track flag.
        name | n: (create, query) - This flag is used to query the name of the clip node associated with the specified clip index, or to specify the name of the instanced clip during instancing. 			In query mode, this flag can accept a value.
        postCycle | poc: (create, query) - Specify the number of times to repeat the clip after its normal end.
        preCycle | prc: (create, query) - Specify the number of times to repeat the clip before its normal start.
        remove | rm: (create) - This flag is used to remove a clip from the timeline. It must be used in conjunction with the ci/clipIndex flag. The specified clip will be removed from the timeline, but will still exist in the library and any instanced clips will remain in the timeline. To permanently remove a clip from the scene, the clip command should be used instead.
        removeBlend | rb: (create) - This flag is used to remove an existing blend between two clips, whose indices are provided as flag arguments.
        removeEmptyTracks | ret: (create) - This flag is used to remove all tracks that have no clips.
        removeTrack | rt: (create) - This flag is used to remove the track with the specified index.  The track must have no clips on it before it can be removed.
        rotationsAbsolute | ra: (edit, query) - Set all channels except rotations to be calculated with relative offsets.  Rotation channels will be calculated with absolute offsets.  This flag cannot be used in conjunction with the aa/allAbsolute, ar/allRelative or da/defaultAbsolute flags.
        scale | sc: (create, query) - Specify the amount to scale the clip. Values must be greater than 0.
        shift | sh: (create) - This flag allows multiple clips to be shifted by a certain number of tracks and works in conjunction with the shiftIndex flag.  The flag specifies the number of tracks to shift the associated clips.  Positive values shift the clips down an negative values shift the clips up.
        shiftIndex | shi: (create, multiuse) - This flag allows multiple clips to be shifted by a certain number of tracks and works in conjunction with the shiftAmount flag.  The flag specifies the index of the clip to shift.  This flag can be used multiple times on the command line to specify a number of clips to shift.
        solo | so: (edit, query) - This flag specifies whether clips on a track are to be soloed or not. Must be used in conjuction with the track flag.
        sourceClipName | scn: (create, query) - This flag is used to query the name of the source clip node associated with the specified clip index.
        sourceEnd | se: (create, query) - Specify where to end in the source clip's animation curves
        sourceStart | ss: (create, query) - Specify where to start in the source clip's animation curves
        start | s: (create, query) - Specify the placement of the start of the clip
        track | t: (create, query) - Specify the track to operate on. For example, which track to place a clip on, which track to mute/lock/solo.  In query mode, it may be used in conjuction with the clipIndex flag to return the track number of a clip, where track 1 is the first track of the character. 			In query mode, this flag can accept a value.
        weight | w: (create, query) - This flag is used in to set or query the weight of the clip associated with the specified clip index.
        weightStyle | ws: (create, query) - This flag is used to set or query the weightStyle attribute of the clip associated with the specified clip index.
    """
    ...


def clipSchedulerOutliner(*args, annotation: Optional[Union[str, bool]] = ..., ann: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., bgc: Optional[Union[Tuple[float, float, float], bool]] = ..., clipScheduler: str = ..., cs: str = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dgc: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., dpc: Optional[Union[str, bool]] = ..., enable: bool = ..., en: bool = ..., enableBackground: bool = ..., ebg: bool = ..., enableKeyboardFocus: bool = ..., ekf: bool = ..., exists: bool = ..., ex: bool = ..., fullPathName: bool = ..., fpn: bool = ..., height: Optional[Union[int, bool]] = ..., h: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., hlc: Optional[Union[Tuple[float, float, float], bool]] = ..., isObscured: bool = ..., io: bool = ..., manage: bool = ..., m: bool = ..., noBackground: bool = ..., nbg: bool = ..., numberOfPopupMenus: bool = ..., npm: bool = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., pma: bool = ..., preventOverride: bool = ..., po: bool = ..., statusBarMessage: Optional[Union[str, bool]] = ..., sbm: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., visible: bool = ..., vis: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., vcc: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., w: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates/edits/queries a clip scheduler outliner control.

    Args:
        annotation | ann: (create, edit, query) - Annotate the control with an extra string value.
        backgroundColor | bgc: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        clipScheduler | cs: (edit) - Name of the clip scheduler for which to display information.
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
        isObscured | io: (query) - Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.
        manage | m: (create, edit, query) - Manage state of the control.  An unmanaged control is not visible, nor does it take up any screen real estate.  All controls are created managed by default.
        noBackground | nbg: (create, edit) - Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
        numberOfPopupMenus | npm: (query) - Return the number of popup menus attached to this control.
        parent | p: (create, query) - The parent layout for this control.
        popupMenuArray | pma: (query) - Return the names of all the popup menus attached to this control.
        preventOverride | po: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        statusBarMessage | sbm: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
        visible | vis: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand | vcc: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width | w: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def cluster(*args, after: bool = ..., af: bool = ..., afterReference: bool = ..., ar: bool = ..., before: bool = ..., bf: bool = ..., bindState: bool = ..., bs: bool = ..., components: bool = ..., cmp: bool = ..., deformerTools: bool = ..., dt: bool = ..., envelope: Optional[Union[float, bool]] = ..., en: Optional[Union[float, bool]] = ..., exclusive: Optional[Union[str, bool]] = ..., ex: Optional[Union[str, bool]] = ..., frontOfChain: bool = ..., foc: bool = ..., geometry: Optional[Union[str, bool]] = ..., g: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., gi: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., ihs: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., parallel: bool = ..., par: bool = ..., prune: bool = ..., pr: bool = ..., relative: bool = ..., rel: bool = ..., remove: bool = ..., rm: bool = ..., resetGeometry: bool = ..., rg: bool = ..., selectedComponents: bool = ..., cms: bool = ..., split: bool = ..., sp: bool = ..., useComponentTags: bool = ..., uct: bool = ..., weightedNode: Optional[Union[Tuple[str, str], bool]] = ..., wn: Optional[Union[Tuple[str, str], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The cluster command creates a cluster or edits the membership of
    an existing cluster. The command returns the name of the cluster
    node upon creation of a new cluster.
    
    After creating a cluster, the cluster's weights can be modified
    using the percent command or the set editor window.

    Args:
        after | af: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference | ar: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before | bf: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        bindState | bs: (create) - When turned on, this flag adds in a compensation to ensure the clustered objects preserve their spatial position when clustered. This is required to prevent the geometry from jumping at the time the cluster is created in situations when the cluster transforms at cluster time are not identity.
        components | cmp: (query) - Returns the components used by the deformer
        deformerTools | dt: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        envelope | en: (create, edit, query) - Set the envelope value for the deformer. Default is 1.0
        exclusive | ex: (create, query) - Puts the deformation set in a deform partition.
        frontOfChain | foc: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry | g: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices | gi: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected | ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections | ihs: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        name | n: (create) - Used to specify the name of the node being created.
        parallel | par: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        prune | pr: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        relative | rel: (create) - Enable relative mode for the cluster. In relative mode, Only the transformations directly above the cluster are used by the cluster. Default is off.
        remove | rm: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        resetGeometry | rg: (edit) - Reset the geometry matrices for the objects being deformed by the cluster. This flag is used to get rid of undesirable effects that happen if you scale an object that is deformed by a cluster.
        selectedComponents | cms: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        split | sp: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        useComponentTags | uct: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
        weightedNode | wn: (create, edit, query) - Transform node in the DAG above the cluster to which all percents are applied. The second DAGobject specifies the descendent of the first DAGobject from where the transformation matrix is evaluated. Default is the cluster handle.
    """
    ...


def combinationShape(*args, addDriver: bool = ..., add: bool = ..., allDrivers: bool = ..., ald: bool = ..., blendShape: Optional[Union[str, bool]] = ..., bs: Optional[Union[str, bool]] = ..., combinationTargetIndex: Optional[Union[int, bool]] = ..., cti: Optional[Union[int, bool]] = ..., combinationTargetName: Optional[Union[str, bool]] = ..., ctn: Optional[Union[str, bool]] = ..., combineMethod: Optional[Union[int, bool]] = ..., cm: Optional[Union[int, bool]] = ..., driverTargetIndex: Optional[Union[int, bool]] = ..., dti: Optional[Union[int, bool]] = ..., driverTargetName: Optional[Union[str, bool]] = ..., dtn: Optional[Union[str, bool]] = ..., exist: bool = ..., ex: bool = ..., removeDriver: bool = ..., rmd: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to create or edit drive relationship of blend shape targets

    Args:
        addDriver | add: () - Add drivers to the combination shape
        allDrivers | ald: (query) - All drivers of the combination shape
        blendShape | bs: (create) - Associated blend shape node of the combination shape 			In query mode, this flag can accept a value.
        combinationTargetIndex | cti: (create) - Driven blend shape target index of the combination shape 			In query mode, this flag can accept a value.
        combinationTargetName | ctn: (create) - Driven blend shape target name of the combination shape 			In query mode, this flag can accept a value.
        combineMethod | cm: (create, edit, query) - Combine method of the combination shape:  0 : Multiplication 1 : Lowest Weighting 2 : Lowest Weighting (Smooth)
        driverTargetIndex | dti: (create, multiuse) - Driver blend shape target index of the combination shape
        driverTargetName | dtn: (create, multiuse) - Driver blend shape target name of the combination shape
        exist | ex: (query) - If the combination shape exist
        removeDriver | rmd: () - Remove drivers from the combination shape
    """
    ...


def componentTag(*args, create: bool = ..., cr: bool = ..., delete: bool = ..., d: bool = ..., injectionLocation: Optional[Union[str, bool]] = ..., il: Optional[Union[str, bool]] = ..., modify: Optional[Union[str, bool]] = ..., m: Optional[Union[str, bool]] = ..., newTagName: Optional[Union[str, bool]] = ..., ntn: Optional[Union[str, bool]] = ..., queryEdit: bool = ..., qe: bool = ..., rename: bool = ..., rn: bool = ..., tagName: Optional[Union[str, bool]] = ..., tn: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This command allows you to create, delete and modify component tags

    Args:
        create | cr: (create) - This creates a componentTag on the geometry. The name can be specified with the -newTagName option. If no new name is specified one will be generated. The name of the created tag is returned
        delete | d: (create) - This deletes the componentTags specified with the -tagName option.
        injectionLocation | il: (create) - The name of the injection node at which the componentTag will be edited. This is only necessary in the rare case where a particular componentTag can be altered at multiple injection locations.
        modify | m: (create) - This modifies the componentTag specified with the -tagName option. The mode determines whether components are, replaced, cleared, added or removed.
        newTagName | ntn: (create) - The name of the new componentTag to be created or the new name of the componentTag that is being renamed.
        queryEdit | qe: (create) - This returns what edits are allowed with the given parameters. When the command is issued in Python a dictionary object containing what is allowed is returned.
        rename | rn: (create) - This renames the componentTag specified with the -tagName option to the name specified with the -newTagName option
        tagName | tn: (create, multiuse) - The name(s) of the componentTags to be edited. THis can be a single name or a list of names. The names can contain wildcard like '*' to match multiple existing componentTags.
    """
    ...


def connectJoint(*args, connectMode: bool = ..., cm: bool = ..., parentMode: bool = ..., pm: bool = ...) -> Any:
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
        connectMode | cm: (create) - The first selected joint will be parented under the parent of the second selected joint.
        parentMode | pm: (create) - The first selected joint will be parented under the second selected joint. Both joints will be in the active list(selection list).
    """
    ...


def controller(*args, allControllers: bool = ..., ac: bool = ..., children: bool = ..., cld: bool = ..., group: bool = ..., g: bool = ..., index: Optional[Union[int, bool]] = ..., idx: Optional[Union[int, bool]] = ..., isController: Optional[Union[str, bool]] = ..., ic: Optional[Union[str, bool]] = ..., parent: bool = ..., p: bool = ..., pickWalkDown: bool = ..., pwd: bool = ..., pickWalkLeft: bool = ..., pwl: bool = ..., pickWalkRight: bool = ..., pwr: bool = ..., pickWalkUp: bool = ..., pwu: bool = ..., unparent: bool = ..., unp: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Commands for managing animation sources

    Args:
        allControllers | ac: (create, query) - When this flag is queried, returns all dependNode attached to a controller in the scene.
        children | cld: (query) - Return true if the specified dependNode is a controller.
        group | g: (create, query) - Create a controller that is not associated with any object. This new controller will be the parent of all the selected objects.
        index | idx: (edit, query) - In query mode, returns the index of the controller in the parent controller's list of children. In edit mode, reorder the parent controller's children connections so that the current controller is assigned the given index.
        isController | ic: (create, query) - Returns true if the specified dependNode is a controller.
        parent | p: (create, edit, query) - Set or query the parent controller of the selected controller node.
        pickWalkDown | pwd: (query) - Return the first child.
        pickWalkLeft | pwl: (query) - Return the previous sibling.
        pickWalkRight | pwr: (query) - Return the next sibling.
        pickWalkUp | pwu: (query) - Return the parent.
        unparent | unp: (edit) - Unparent all selected controller objects from their respective parent.
    """
    ...


def copyDeformerWeights(*args, destinationDeformer: Optional[Union[str, bool]] = ..., dd: Optional[Union[str, bool]] = ..., destinationShape: Optional[Union[str, bool]] = ..., ds: Optional[Union[str, bool]] = ..., mirrorInverse: bool = ..., mi: bool = ..., mirrorMode: Optional[Union[str, bool]] = ..., mm: Optional[Union[str, bool]] = ..., noMirror: bool = ..., nm: bool = ..., smooth: bool = ..., sm: bool = ..., sourceDeformer: Optional[Union[str, bool]] = ..., sd: Optional[Union[str, bool]] = ..., sourceShape: Optional[Union[str, bool]] = ..., ss: Optional[Union[str, bool]] = ..., surfaceAssociation: Optional[Union[str, bool]] = ..., sa: Optional[Union[str, bool]] = ..., uvSpace: Optional[Union[Tuple[str, str], bool]] = ..., uv: Optional[Union[Tuple[str, str], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to copy or mirror the deformer weights accross one
     of the three major axes.  The command can be used to mirror
     weights either from one surface to another or within the
     same surface.

    Args:
        destinationDeformer | dd: (create, edit, query) - Specify the deformer used by the destination shape
        destinationShape | ds: (create, edit, query) - Specify the destination deformed shape
        mirrorInverse | mi: (create, edit, query) - Values are mirrored from the positive side to the negative.  If this flag is used then the direction is inverted.
        mirrorMode | mm: (create, edit, query) - The mirrorMode flag defines the plane of mirroring (XY, YZ, or XZ) when the mirror flag is used. The default plane is XY.
        noMirror | nm: (create, edit, query) - When the no mirror flag is used, the weights are copied instead of mirrored.
        smooth | sm: (create, edit, query) - When the smooth flag is used, the weights are smoothly interpolated between the closest vertices, instead of assigned from the single closest.
        sourceDeformer | sd: (create, edit, query) - Specify the deformer whose weights should be mirrored.  When queried, returns the deformers used by the source shapes.
        sourceShape | ss: (create, edit, query) - Specify the source deformed shape
        surfaceAssociation | sa: (create, edit, query) - The surfaceAssociation flag controls how the weights are transferred between the surfaces: "closestPoint", "rayCast", or "closestComponent". The default is closestComponent.
        uvSpace | uv: (create, edit, query) - The uvSpace flag indicates that the weight transfer should occur in UV space, based on the source and destination UV sets specified.
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


def copyKey(*args, animLayer: Optional[Union[str, bool]] = ..., al: Optional[Union[str, bool]] = ..., animation: Optional[Union[str, bool]] = ..., an: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., clipboard: Optional[Union[str, bool]] = ..., cb: Optional[Union[str, bool]] = ..., controlPoints: bool = ..., cp: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., f: Optional[Union[Tuple[float, float], bool]] = ..., forceIndependentEulerAngles: bool = ..., fea: bool = ..., hierarchy: Optional[Union[str, bool]] = ..., hi: Optional[Union[str, bool]] = ..., includeUpperBound: bool = ..., iub: bool = ..., index: Optional[Union[int, bool]] = ..., option: Optional[Union[str, bool]] = ..., o: Optional[Union[str, bool]] = ..., shape: bool = ..., s: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., t: Optional[Union[Tuple[float, float], bool]] = ...) -> Any:
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
        animLayer | al: (create) - Specifies that the keys getting copied should come from this specified animation layer. If no keys on the object exist on this layer, then no keys are copied.
        animation | an: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute | at: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        clipboard | cb: (create) - Specifies the clipboard to which animation is copied. Valid clipboards are "api" and "anim".  The default clipboard is: anim
        controlPoints | cp: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        float | f: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        forceIndependentEulerAngles | fea: (create) - Specifies that the rotation curves should always be placed on the clipboard as independent Euler Angles. The default value is false.
        hierarchy | hi: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        includeUpperBound | iub: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index | index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        option | o: (create) - The option to use when performing the copyKey operation. Valid options are "keys," and "curve."  The default copy option is: keys
        shape | s: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        time | t: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
    """
    ...


def copySkinWeights(*args, destinationSkin: Optional[Union[str, bool]] = ..., ds: Optional[Union[str, bool]] = ..., influenceAssociation: Optional[Union[str, bool]] = ..., ia: Optional[Union[str, bool]] = ..., mirrorInverse: bool = ..., mi: bool = ..., mirrorMode: Optional[Union[str, bool]] = ..., mm: Optional[Union[str, bool]] = ..., noBlendWeight: bool = ..., nbw: bool = ..., noMirror: bool = ..., nm: bool = ..., normalize: bool = ..., nr: bool = ..., sampleSpace: Optional[Union[int, bool]] = ..., spa: Optional[Union[int, bool]] = ..., selectedComponents: bool = ..., sc: bool = ..., smooth: bool = ..., sm: bool = ..., sourceSkin: Optional[Union[str, bool]] = ..., ss: Optional[Union[str, bool]] = ..., surfaceAssociation: Optional[Union[str, bool]] = ..., sa: Optional[Union[str, bool]] = ..., uvSpace: Optional[Union[Tuple[str, str], bool]] = ..., uv: Optional[Union[Tuple[str, str], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to copy or mirror the skinCluster weights accross one
     of the three major axes.  The command can be used to mirror
     weights either from one surface to another or within the
     same surface.

    Args:
        destinationSkin | ds: (create, edit, query) - Specify the destination skin shape
        influenceAssociation | ia: (create, edit, multiuse, query) - The influenceAssociation flag controls how the influences on the source and target skins are matched up. The flag can be included multiple times to specify multiple association schemes that will be invoked one after the other until all influences have been matched up. Supported values are "closestJoint", "closestBone", "label", "name", "oneToOne". The default is closestJoint.
        mirrorInverse | mi: (create, edit, query) - Values are mirrored from the positive side to the negative.  If this flag is used then the direction is inverted.
        mirrorMode | mm: (create, edit, query) - The mirrorMode flag defines the plane of mirroring (XY, YZ, or XZ) when the mirror flag is used. The default plane is XY.
        noBlendWeight | nbw: (create, edit, query) - When the no blend flag is used, the blend weights on the skin cluster will not be copied across to the destination.
        noMirror | nm: (create, edit, query) - When the no mirror flag is used, the weights are copied instead of mirrored.
        normalize | nr: (create, edit, query) - Normalize the skin weights.
        sampleSpace | spa: (create, edit, query) - Selects which space the attribute transfer is performed in. 0 is world space, 1 is model space. The default is world space.
        selectedComponents | sc: (create, edit, query) - The selectedComponents flag can be used in combination with the sourceSkin and destinationSkin flags to specify that only the skin weights on the selected components should be copied.
        smooth | sm: (create, edit, query) - When the smooth flag is used, the weights are smoothly interpolated between the closest vertices, instead of assigned from the single closest.
        sourceSkin | ss: (create, edit, query) - Specify the source skin shape
        surfaceAssociation | sa: (create, edit, query) - The surfaceAssociation flag controls how the weights are transferred between the surfaces: "closestPoint", "rayCast", or "closestComponent". The default is closestComponent.
        uvSpace | uv: (create, edit, query) - The uvSpace flag indicates that the weight transfer should occur in UV space, based on the source and destination UV sets specified.
    """
    ...


def currentTime(*args, update: bool = ..., u: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    When given a time argument (with or without the -edit flag) this
    command sets the current global time.  The model updates and
    displays at the new time, unless "-update off" is present on the
    command line.

    Args:
        update | u: (create) - change the current time, but do not update the world. Default value is true.
    """
    ...


def curveRGBColor(*args, hueSaturationValue: bool = ..., hsv: bool = ..., list: bool = ..., l: bool = ..., listNames: bool = ..., ln: bool = ..., remove: bool = ..., r: bool = ..., resetToFactory: bool = ..., rf: bool = ..., resetToSaved: bool = ..., rs: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates, changes or removes custom curve colors,
    which are used to draw the curves in the Graph Editor.
    The custom curve names may contain the wildcards
    "?", which marches a single character, and
    "*", which matches any number of characters.
    These colors are part of the UI and not part of the saved
    data for a model.  This command is not undoable.

    Args:
        hueSaturationValue | hsv: (create, query) - Indicates that rgb values are really hsv values.
        list | l: (create) - Writes out a list of all curve color names and their values.
        listNames | ln: (create) - Returns an array of all curve color names.
        remove | r: (create) - Removes the named curve color.
        resetToFactory | rf: (create) - Resets all the curve colors to their factory defaults.
        resetToSaved | rs: (create) - Resets all the curve colors to their saved values.
    """
    ...


def cutKey(*args, animation: Optional[Union[str, bool]] = ..., an: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., clear: bool = ..., cl: bool = ..., controlPoints: bool = ..., cp: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., f: Optional[Union[Tuple[float, float], bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., hi: Optional[Union[str, bool]] = ..., includeUpperBound: bool = ..., iub: bool = ..., index: Optional[Union[int, bool]] = ..., option: Optional[Union[str, bool]] = ..., o: Optional[Union[str, bool]] = ..., selectKey: bool = ..., sl: bool = ..., shape: bool = ..., s: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., t: Optional[Union[Tuple[float, float], bool]] = ...) -> Any:
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
        animation | an: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute | at: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        clear | cl: (create) - Just remove the keyframes (i.e. do not overwrite the clipboard)
        controlPoints | cp: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        float | f: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        hierarchy | hi: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        includeUpperBound | iub: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index | index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        option | o: (create) - Option for how to perform the cutKey operation.  Valid values for this flag are "keys", "curve", "curveCollapse", "curveConnect", "areaCollapse".  The default cut option is: keys
        selectKey | sl: (create) - Select the keyframes of curves which have had keys removed
        shape | s: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        time | t: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
    """
    ...


def dagPose(*args, addToPose: bool = ..., a: bool = ..., atPose: bool = ..., ap: bool = ..., bindPose: bool = ..., bp: bool = ..., g: bool = ..., members: bool = ..., m: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., remove: bool = ..., rm: bool = ..., reset: bool = ..., rs: bool = ..., restore: bool = ..., r: bool = ..., save: bool = ..., s: bool = ..., selection: bool = ..., sl: bool = ..., worldParent: bool = ..., wp: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        addToPose | a: (create) - Allows adding the selected items to the dagPose.
        atPose | ap: (query) - Query whether the hierarchy is at same position as the pose. Names of hierarchy members that are not at the pose position will be returned. An empty return list indicates that the hierarchy is at the pose.
        bindPose | bp: (create, query) - Used to specify the bindPose for the selected hierarchy. Each hierarchy can have only a single bindPose, which is saved automatically at the time of a skin bind. The bindPose is used when adding influence objects, binding new skins, or adding flexors. Take care when modifying the bindPose with the -rs/-reset or -rm/-remove flags, since if the bindPose is ill-defined it can cause problems with subsequent skinning operations.
        g | g: (create) - This flag can be used in conjunction with the restore flag to signal that the members of the pose should be restored to the global pose. The global pose means not only is each object locally oriented with respect to its parents, it is also in the same global position that it was at when the pose was saved. If a hierarchy's parenting has been changed since the time that the pose was saved, you may have trouble reaching the global pose.
        members | m: (query) - Query the members of the specified pose. The pose should be specified using the selection list, the -bp/-bindPose or the -n/-name flag.
        name | n: (create, query) - Specify the name of the pose. This can be used during create, restore, reset, remove, and query operations to specify the pose to be created or acted upon.
        remove | rm: (create) - Remove the selected joints from the specified pose.
        reset | rs: (create) - Reset the pose on the selected joints. If you are resetting pose data for a bindPose, take care. It is appropriate to use the -rs/-reset flag if a joint has been reparented and/or appears to be exactly at the bindPose. However, a bindPose that is much different from the exact bindPose can cause problems with subsequent skinning operations.
        restore | r: (create) - Restore the hierarchy to a saved pose. To specify the pose, select the pose node, or use the -bp/-bindPose or -n/-name flag.
        save | s: (create) - Save a dagPose for the selected dag hierarchy. The name of the new pose will be returned.
        selection | sl: (create, query) - Whether or not to store a pose for all items in the hierarchy, or for only the selected items.
        worldParent | wp: (create) - Indicates that the selected pose member should be recalculated as if it is parented to the world. This is typically used when you plan to reparent the object to world as the next operation.
    """
    ...


def defineDataServer(*args, device: Optional[Union[str, bool]] = ..., d: Optional[Union[str, bool]] = ..., server: Optional[Union[str, bool]] = ..., s: Optional[Union[str, bool]] = ..., undefine: bool = ..., u: bool = ...) -> Any:
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
        device | d: (create) - specified the device name to be given to the server connection. device name must be unique or the command fails.
        server | s: (create) - specifies the name of the server with which the define device connects, and can be specifiied in two ways   name -- the name of the server socket Server names of the form name connect to the server socket on the localhost corresponding to name.  If name does not begin with "/", then /tmp/name is used. This is the default behavior of most servers. If name begins with "/", name denotes the full path to the socket.  host:service - a udp service on the specified host. The service can be any one of a "udp service name," a "port number," or a named service of "tcpmux," and they are found in that order. If host is omitted, the localhost is used.   In any case, if the server cannot be found, the device is not defined (created) and the command fails.
        undefine | u: (create) - undefines (destroys) the dataServer device, closing the connection with the server.
    """
    ...


def defineVirtualDevice(*args, axis: Optional[Union[int, bool]] = ..., ax: Optional[Union[int, bool]] = ..., channel: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., clear: bool = ..., cl: bool = ..., create: bool = ..., cr: bool = ..., device: Optional[Union[str, bool]] = ..., d: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., undefine: bool = ..., u: bool = ..., usage: Optional[Union[str, bool]] = ..., use: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command defines a virtual device. Virtual devices act like real
    devices and are useful to manipulate/playback data when an command
    device is not connected to the computer.

    Args:
        axis | ax: (create) - Specifies the axis number of the channel. All children have their axis number determined by their parent's axis number and the width of the parent channel. If this flag is not used, the order of the channel determines the axis number.
        channel | c: (create) - After a -create is started, channels may be added to the device definition. The channel string wil be the name of the channel being added to the device. The -channel flag must also be accompanied by the -usage flag and optionally by the -axis flag.
        clear | cl: (create) - The -clear option will end a device definition and throw away any defined channels.
        create | cr: (create) - Start defining a virtual device. If a device is currently being defined, the -create flag will produce an error.
        device | d: (create) - The -device flag ends the device definition. All of the channels between the -create flag and the -device flag are added to the specified device. If that device already exists, the command will fail and the device should be redefined with another device name. To see the currently defined devices, use the listInputDevices command. The -device flag is also used with -undefine to undefine a virtual device.
        parent | p: (create) - Specified the parent channel of the channel being defined. If the channel does not exist, or is an incompatible type, the command will fail.
        undefine | u: (create) - Undefines the device specified with the -device flag.
        usage | use: (create) - The -usage option is required for every -channel flag. It describes what usage type the defined channel is. The usage types are:   unknownscalar  posrot posRotquaternionposQuaternion  rotXYZrotYZXrotZXY rotXZYrotYXZrotZYX  posRotXYZposRotYZXposRotZXY posRotXZYposRotXZYposRotZYX  posXposYposZrotX rotYrotZ
    """
    ...


def deformableShape(*args, chain: bool = ..., ch: bool = ..., createOriginalGeometry: bool = ..., cog: bool = ..., createTweakNode: bool = ..., ctw: bool = ..., createUpstreamTagInjectionNode: bool = ..., cti: bool = ..., deformShapeInAttr: bool = ..., dsi: bool = ..., deformShapeOutAttr: bool = ..., dso: bool = ..., frontOfChain: bool = ..., foc: bool = ..., localShapeInAttr: bool = ..., lsi: bool = ..., localShapeOutAttr: bool = ..., lso: bool = ..., nodeChain: bool = ..., nch: bool = ..., originalGeometry: bool = ..., og: bool = ..., outputPlugChain: bool = ..., och: bool = ..., plugChain: bool = ..., pch: bool = ..., supportsComponentTags: bool = ..., sct: bool = ..., tagInjectionList: bool = ..., til: bool = ..., tagInjectionNode: bool = ..., ti: bool = ..., tweakNode: bool = ..., tw: bool = ..., upstreamTagInjectionNode: bool = ..., uti: bool = ..., worldShapeOutAttr: bool = ..., wso: bool = ...) -> Any:
    r"""
    This command finds information about deforming shape(s).
    
    If no shapes are specified on the command then the curently selected
    shapes are used.

    Args:
        chain | ch: (create) - This flag will return the list of deformers that deformer the specified shapes
        createOriginalGeometry | cog: (create) - This creates an original geometry for the shape if it does not exist yet.
        createTweakNode | ctw: (create) - This creates a traditional tweak node if one did not exist yet.
        createUpstreamTagInjectionNode | cti: (create) - This creates an upstream component tag injection node if an editable one does not exist yet.
        deformShapeInAttr | dsi: (create) - Returns the name of deform shape in attribute
        deformShapeOutAttr | dso: (create) - Returns the name of deform shape out attribute
        frontOfChain | foc: (create) - This flag will return the name of the plug on a shape node at the front end of the deformation chain. This can return an empty plug when none exists.
        localShapeInAttr | lsi: (create) - Returns the name of local shape in attribute
        localShapeOutAttr | lso: (create) - Returns the name of local shape out attribute
        nodeChain | nch: (create) - This flag will return the list of nodes through which the geometry passes to get to this shape
        originalGeometry | og: (create) - This flag will return the name of a plug on a node in the deformation chain (likely at the front end) that is the best candidate to be used as the originalGeometry. This can return an empty plug when none exists.
        outputPlugChain | och: (create) - This flag will return the list of output plugs leading to the shape
        plugChain | pch: (create) - This flag will return the list of plugs leading to the shape (both input and output plugs)
        supportsComponentTags | sct: (create) - Returns whether the shape supports component tags
        tagInjectionList | til: (create) - This flag will return the list of nodes which are non-procedural componentTag injection nodes
        tagInjectionNode | ti: (create) - This flag will return the name of the non-referenced component tag injection node as high up in the deformation chain as possible. This can be the same as the input shape or an empty string when none exists.
        tweakNode | tw: (create) - This flag will return the name of the tweak node in the deformation chain. This can return an empty string when none exists.
        upstreamTagInjectionNode | uti: (create) - This flag will return the name of the non-referenced component tag injection node most upstream from (but not including) the input shape. This can be an empty string when none exists. If so, one can be created using the cti/createUpstreamTagInjectionNode flag.
        worldShapeOutAttr | wso: (create) - Returns the name of world shape out attribute
    """
    ...


def deformer(*args, after: bool = ..., af: bool = ..., afterReference: bool = ..., ar: bool = ..., before: bool = ..., bf: bool = ..., components: bool = ..., cmp: bool = ..., deformerTools: bool = ..., dt: bool = ..., exclusive: Optional[Union[str, bool]] = ..., ex: Optional[Union[str, bool]] = ..., frontOfChain: bool = ..., foc: bool = ..., geometry: Optional[Union[str, bool]] = ..., g: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., gi: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., ihs: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., parallel: bool = ..., par: bool = ..., prune: bool = ..., pr: bool = ..., remove: bool = ..., rm: bool = ..., selectedComponents: bool = ..., cms: bool = ..., split: bool = ..., sp: bool = ..., type: Optional[Union[str, bool]] = ..., typ: Optional[Union[str, bool]] = ..., useComponentTags: bool = ..., uct: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        after | af: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference | ar: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before | bf: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        components | cmp: (query) - Returns the components used by the deformer
        deformerTools | dt: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        exclusive | ex: (create, query) - Puts the deformation set in a deform partition.
        frontOfChain | foc: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry | g: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices | gi: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected | ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections | ihs: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        name | n: (create) - Used to specify the name of the node being created.
        parallel | par: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        prune | pr: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        remove | rm: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        selectedComponents | cms: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        split | sp: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        type | typ: (create) - Specify the type of deformer to create. This flag is required in create mode. Typically the type should specify a loaded plugin deformer. This command should typically not be used to create one of the standard deformers such as sculpt, lattice, blendShape, wire and cluster, since they have their own customized commands which perform useful specialized functionality.
        useComponentTags | uct: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
    """
    ...


def deformerEvaluator(*args, active: bool = ..., act: bool = ..., allowDownloadRejections: bool = ..., adr: bool = ..., allowDownloads: bool = ..., adl: bool = ..., asNodeName: bool = ..., nm: bool = ..., asText: bool = ..., txt: bool = ..., deformerChain: bool = ..., dch: bool = ..., deformers: bool = ..., d: bool = ..., dumpInfo: bool = ..., di: bool = ..., dumpOutliner: bool = ..., dol: bool = ..., gpuBlockPolicy: Optional[Union[str, bool]] = ..., gbp: Optional[Union[str, bool]] = ..., isOpenCLValid: bool = ..., clv: bool = ..., limitMinimumVerts: bool = ..., lmv: bool = ..., list: bool = ..., ls: bool = ..., members: bool = ..., mbr: bool = ..., meshes: bool = ..., m: bool = ..., message: bool = ..., msg: bool = ..., minimumVerts: Optional[Union[int, bool]] = ..., mnv: Optional[Union[int, bool]] = ..., nodeInfo: bool = ..., ni: bool = ..., nodeStatus: bool = ..., ns: bool = ..., omitPassthroughs: bool = ..., opt: bool = ..., outlinerHash: bool = ..., olh: bool = ..., partition: bool = ..., prt: bool = ..., purge: bool = ..., prg: bool = ..., reuseMode: Optional[Union[Tuple[str, str], bool]] = ..., ru: Optional[Union[Tuple[str, str], bool]] = ..., verbose: bool = ..., v: bool = ..., query: bool = ...) -> Any:
    r"""
    Print debug information about deformer evaluator status.  In
            query mode the debug information is returned as a string[],
            otherwise the information is displayed in the script editor.

    Args:
        active | act: (create, query) - Modifier to specify that instead of the current selection all active         nodes on the GPU should be queried.
        allowDownloadRejections | adr: (create, query) - Specifies whether potentially rejecting parts of the graph that depend on GPU downloads is allowed.
        allowDownloads | adl: (create, query) - Specifies whether downloads from GPU to CPU are allowed.
        asNodeName | nm: (create, query) - Modifier to specify that when a certain node attribute is queried it should         return the name of the node instead. This is useful when querying multiple         nodes at a time and the results need to be lined up with the node names.
        asText | txt: (create, query) - Modifier to specify that when the node state is queried the state should     be returned as text instead of a numeric code
        deformerChain | dch: (create, query) - Query the state of the nodes in the deformation chain of the specified meshes.
        deformers | d: (create, query) - Return a list of all currently registered GPU deformers.
        dumpInfo | di: (create, query) - List information about all supported deformation chains as JSON.
        dumpOutliner | dol: (create, query) - List information about all supported nodes as a python object.
        gpuBlockPolicy | gbp: (create, query) - Specifies the gpu blocking policy for a node.     Currently, we support the following blocking modes:     "off" "on" "group" "upstream" "upstreamExcl" "upstreamMesh" "downstream" "downstreamExcl" "groupDownload"     Default is "off" which means the node causes no blocking of the GPU.
        isOpenCLValid | clv: (create, query) - Specifies whether OpenCL is valid/initialized.
        limitMinimumVerts | lmv: (create, query) - Specifies whether the limit on the minimum vert count of the geometry is used or not. The system configuration determines a certain minimum size for geometries to be allowed on GPU. When this flag is on this limit is obeyed. When this flag is off this limit is ignored. This is only used for debugging purposes and is not saved to the file or any preferences.
        list | ls: (create, query) - Return a list of nodes that are currently active on the GPU.
        members | mbr: (create, query) - Return the names of the nodes that are in the same cluster as the specified nodes.
        meshes | m: (create, query) - Modifier to specify that only meshes need to be queried.
        message | msg: (create, query) - Return the messages associated with the specified nodes.
        minimumVerts | mnv: (create, query) - Set the minimum vert count under which the geometry will not be allowed on the GPU (unless in a network with qualifying geometries). This is only used for debugging purposes and is not saved to the file or any preferences.
        nodeInfo | ni: (create, query) - List all the information gathered during partitioning about the selected nodes
        nodeStatus | ns: (create, query) - Return the state of the node on the GPU. When queried it will return         a numeric code unless the asText flag is used as well.
        omitPassthroughs | opt: (create, query) - Whether opassthrough nodes like groupParts nodes should be ommitted from the dumped info or not
        outlinerHash | olh: (create, query) - Return the unique hash value for the current outliner state.
        partition | prt: (create, query) - Flag to force a repartition (for debug purposes only)
        purge | prg: (create, query) - Purge the data of any unused gpu nodes
        reuseMode | ru: (create, query) - Specifies how the GPU nodes can be reused when repartitioning. A mode has to be specified for each of the three node types (deformer and displayMesh). A mode for a node type is one of the following:       Mode "never" means they will never be reused   Mode "immediate" means that nodes will remain in memory during repartitioning but the ones that are not in use immediatley after that will be purged   Mode "always" means that all nodes will remain in memory during and after repartitioning for later reuse
        verbose | v: (create, query) - Print more verbose information of other flags.
    """
    ...


def deformerWeights(*args, attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., defaultValue: Optional[Union[float, bool]] = ..., dv: Optional[Union[float, bool]] = ..., deformer: Optional[Union[str, bool]] = ..., df: Optional[Union[str, bool]] = ..., export: bool = ..., ex: bool = ..., format: Optional[Union[str, bool]] = ..., fm: Optional[Union[str, bool]] = ..., ignoreName: bool = ..., ig: bool = ..., im: bool = ..., method: Optional[Union[str, bool]] = ..., m: Optional[Union[str, bool]] = ..., path: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., positionTolerance: Optional[Union[float, bool]] = ..., pt: Optional[Union[float, bool]] = ..., remap: Optional[Union[str, bool]] = ..., r: Optional[Union[str, bool]] = ..., shape: Optional[Union[str, bool]] = ..., sh: Optional[Union[str, bool]] = ..., skip: Optional[Union[str, bool]] = ..., sk: Optional[Union[str, bool]] = ..., vertexConnections: bool = ..., vc: bool = ..., weightPrecision: Optional[Union[int, bool]] = ..., wp: Optional[Union[int, bool]] = ..., weightTolerance: Optional[Union[float, bool]] = ..., wt: Optional[Union[float, bool]] = ..., worldSpace: bool = ..., ws: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        attribute | at: (create, edit, multiuse, query) - Specify the long name of deformer attribute that should be imported/exported along with the deformerWeights. i.e. -at "envelope" -at "skinningMethod" etc.. No warning or error is given if a specified attribute does not exist on a particular deformer, making it possible to use this command with multiple deformers without aborting or slowing down the import/export process.  Currently supports numeric attributes and matrix attributes
        defaultValue | dv: (create, edit, query) - Manually set the default value. Default values are values that are not written to file. For example, for blendShapes the default value is automatically set to 1.0 and these values are not written to disk. For skinClusters the value is 0.0. If all weights should be forced to be written to disk, set a defaultValue = -1.0.
        deformer | df: (create, edit, multiuse, query) - Specify the deformer whose weights should be exported or imported. If a pattern is supplied for the deformer name (i.e: cluster*), only the first deformer that matches the pattern will be imported/exported unless used in conjunction with the -skip option
        export | ex: (create, edit, query) - Export the given deformer
        format | fm: (create, edit, query) - Specify either "XML" or "JSON" as the file extension to save as.
        ignoreName | ig: (create, edit, query) - Ignore the names of the layers on import, just use the order of the layers instead. This can be used when joint names have been changed. Leaving it on only name that match on import will be write to the deformer.
        im | im: (create, edit, query) - Import weights to the specified deformer. See the method flag for details on how the weights will be mapped to the destination deformer.
        method | m: (create, edit, query) - Specify the method used to map the weight during import. Valid values are: "index", "nearest", "barycentric", "bilinear" and "over". The "index" method uses the vertex index to map the weights onto the object. This is most useful when the destination object shares the same topology as the exported data. The "nearest" method finds the nearest vertex in the imported data set and sets the weight value to that value. This is best used when mapping a higher resolution mesh to a lower resolution. The "barycentric" and "bilinear" methods are only supported with polygon mesh exported with -vc/vertexConnections flag. The "barycentric" method finds the nearest triangle of the input geometry and rescales the weights at the triangle vertices according to the barycentric weights to each vertex of the nearest triangle. The "bilinear" method finds the nearest convex quad of the input geometry and rescales the weights at the quad vertices according to the bilinear weights to each vertex of the nearest convex quad. For non-quad polygon, the "bilinear" method will fall back to "barycentric" method. The "over" method is similar to the "index" method but the weights on the destination mesh are not cleared prior to mapping, so that unmatched indices keep their weights intact.
        path | p: (create, edit, query) - The path to the given file. Default to the current project.
        positionTolerance | pt: (create, edit, query) - The position tolerance is used to determine the radius of search for the nearest method. This flag is only used with import. Defaults to a huge number.
        remap | r: (create, edit, multiuse, query) - Remap maps source regular expression to destination format. It maps any name that matches the regular expression (before the semi-colon) to the expression format (after the semi-colon). For example, -remap "test:(.*);$1" will rename all items in the test namespace to the global namespace. Accepts $1, $2, .., $9 as pattern holders in the expression format. Remap flag must be used together with import or export. When working with import, the name of the object from the xml file matching the regular expression is remapped to object in scene. When working with export, the name of the object from the scene matching the regular expression is remapped to object in xml file.
        shape | sh: (create, edit, multiuse, query) - Specify the source shape. Export will write out all the deformers on the shape node into one file. If a pattern is supplied for the shape name (i.e: pCylinder*), only the first shape that matches the pattern will be imported/exported unless used in conjunction with the -skip option.
        skip | sk: (create, edit, multiuse, query) - Skip any deformer, shape, or layer that whose name matches the given regular expression string
        vertexConnections | vc: (create, edit, query) - Export vertex connection information, which is required for -m/-method "barycentric" and "bilinear". The flag is only used with -ex/-export flag. The vertex connection information is automatically loaded during import if available in xml file.
        weightPrecision | wp: (create, edit, query) - Sets the output decimal precision for exported weights. The default value is 3.
        weightTolerance | wt: (create, edit, query) - The weight tolerance is used to decide if a given weight value is close enough to the default value that it does not need to be included. This flag is only used with export. The default value is .001.
        worldSpace | ws: (create, edit, query) - For spatially based association methods (nearest), the position should be based on the world space position rather then the local object space.
    """
    ...


def deltaMush(*args, after: bool = ..., af: bool = ..., afterReference: bool = ..., ar: bool = ..., before: bool = ..., bf: bool = ..., components: bool = ..., cmp: bool = ..., deformerTools: bool = ..., dt: bool = ..., envelope: Optional[Union[float, bool]] = ..., en: Optional[Union[float, bool]] = ..., exclusive: Optional[Union[str, bool]] = ..., ex: Optional[Union[str, bool]] = ..., frontOfChain: bool = ..., foc: bool = ..., geometry: Optional[Union[str, bool]] = ..., g: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., gi: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., ihs: bool = ..., inwardConstraint: Optional[Union[float, bool]] = ..., iwc: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., outwardConstraint: Optional[Union[float, bool]] = ..., owc: Optional[Union[float, bool]] = ..., parallel: bool = ..., par: bool = ..., pinBorderVertices: bool = ..., pbv: bool = ..., prune: bool = ..., pr: bool = ..., remove: bool = ..., rm: bool = ..., selectedComponents: bool = ..., cms: bool = ..., smoothingIterations: Optional[Union[int, bool]] = ..., si: Optional[Union[int, bool]] = ..., smoothingStep: Optional[Union[float, bool]] = ..., ss: Optional[Union[float, bool]] = ..., split: bool = ..., sp: bool = ..., useComponentTags: bool = ..., uct: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to create, edit and query deltaMush nodes.

    Args:
        after | af: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference | ar: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before | bf: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        components | cmp: (query) - Returns the components used by the deformer
        deformerTools | dt: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        envelope | en: (create, edit, query) - Envelope of the delta mush node. The envelope determines the percent of deformation. Value is clamped to [0, 1] range. Default is 1.
        exclusive | ex: (create, query) - Puts the deformation set in a deform partition.
        frontOfChain | foc: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry | g: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices | gi: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected | ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections | ihs: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        inwardConstraint | iwc: (create, edit, query) - Constrains the movement of the vertex to not move inward from the input deforming shape to preserve the contour. Value is in the [0,1] range. Default is 0.0.
        name | n: (create) - Used to specify the name of the node being created.
        outwardConstraint | owc: (create, edit, query) - Constrains the movement of the vertex to not move outward from the input deforming shape to preserve the contour. Value is in the [0,1] range. Default is 0.0.
        parallel | par: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        pinBorderVertices | pbv: (create, edit, query) - If enabled, vertices on mesh borders will be pinned to their current position during smoothing. Default is true.
        prune | pr: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        remove | rm: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        selectedComponents | cms: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        smoothingIterations | si: (create, edit, query) - Number of smoothing iterations performed by the delta mush node. Default is 10.
        smoothingStep | ss: (create, edit, query) - Step amount used per smoothing iteration. Value is clamped to [0, 1] range. A higher value may lead to instabilities but converges faster compared to a lower value. Default is 0.5.
        split | sp: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        useComponentTags | uct: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
    """
    ...


def deviceManager(*args, attachment: bool = ..., att: bool = ..., axisCoordChanges: bool = ..., acc: bool = ..., axisIndex: Optional[Union[int, bool]] = ..., axi: Optional[Union[int, bool]] = ..., axisName: bool = ..., axn: bool = ..., axisOffset: bool = ..., axo: bool = ..., axisScale: bool = ..., axs: bool = ..., deviceIndex: Optional[Union[int, bool]] = ..., dvi: Optional[Union[int, bool]] = ..., deviceNameFromIndex: Optional[Union[int, bool]] = ..., dni: Optional[Union[int, bool]] = ..., numAxis: bool = ..., nax: bool = ..., numDevices: bool = ..., ndv: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command queriers the internal device manager for information on attached devices.

    Args:
        attachment | att: (query) - Returns the plugs that a device and axis are attached to.  Expects the -deviceIndex and axisIndex to be used in conjunction.
        axisCoordChanges | acc: (query) - Returns whether the axis coordinate changes.  Expects the -deviceIndex and -axisIndex flags to be used in conjunction.
        axisIndex | axi: (create, edit, query) - Used usually in conjunction with other flags, to indicate the index of the axis.
        axisName | axn: (query) - Returns the name of the axis.  Expects the -deviceIndex and -axisIndex flags to be used in conjunction.
        axisOffset | axo: (query) - Returns the offset of the axis.  Expects the -deviceIndex and -axisIndex flags to be used in conjunction.
        axisScale | axs: (query) - Returns the scale of the axis.  Expects the -deviceIndex and -axisIndex flags to be used in conjunction.
        deviceIndex | dvi: (create, edit, query) - Used usually in conjunction with other flags, to indicate the index of the device.
        deviceNameFromIndex | dni: (query) - Returns the name of the device with the given index.
        numAxis | nax: (query) - Returns the number of axis this device has.  Expects the -deviceIndex flag to be used.
        numDevices | ndv: (query) - Returns the number of devices currently attached.
    """
    ...


def disconnectJoint(*args, attachHandleMode: bool = ..., ahm: bool = ..., deleteHandleMode: bool = ..., dhm: bool = ...) -> Any:
    r"""
    This command will break a skeleton at the selected joint and delete
    any associated handles.

    Args:
        attachHandleMode | ahm: (create) - This flag is obsolete and no longer supported.
        deleteHandleMode | dhm: (create) - Delete the handle on the associated joint.
    """
    ...


def dopeSheetEditor(*args, autoFit: Optional[Union[str, bool]] = ..., af: Optional[Union[str, bool]] = ..., autoFitTime: Optional[Union[str, bool]] = ..., aft: Optional[Union[str, bool]] = ..., control: bool = ..., ctl: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., displayActiveKeyTangents: str = ..., dat: str = ..., displayActiveKeys: str = ..., dak: str = ..., displayInfinities: str = ..., di: str = ..., displayKeys: str = ..., dk: str = ..., displayTangents: str = ..., dtn: str = ..., displayValues: str = ..., dv: str = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., exists: bool = ..., ex: bool = ..., filter: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., fmc: Optional[Union[str, bool]] = ..., hierarchyBelow: bool = ..., hb: bool = ..., highlightConnection: Optional[Union[str, bool]] = ..., hlc: Optional[Union[str, bool]] = ..., lockMainConnection: bool = ..., lck: bool = ..., lookAt: str = ..., la: str = ..., mainListConnection: Optional[Union[str, bool]] = ..., mlc: Optional[Union[str, bool]] = ..., outliner: Optional[Union[str, bool]] = ..., o: Optional[Union[str, bool]] = ..., panel: Optional[Union[str, bool]] = ..., pnl: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., selectionConnection: Optional[Union[str, bool]] = ..., slc: Optional[Union[str, bool]] = ..., selectionWindow: Optional[Union[Tuple[float, float, float, float], bool]] = ..., sel: Optional[Union[Tuple[float, float, float, float], bool]] = ..., showScene: bool = ..., sc: bool = ..., showSummary: bool = ..., ss: bool = ..., showTicks: bool = ..., stk: bool = ..., snapTime: Optional[Union[str, bool]] = ..., st: Optional[Union[str, bool]] = ..., snapValue: Optional[Union[str, bool]] = ..., sv: Optional[Union[str, bool]] = ..., stateString: bool = ..., sts: bool = ..., unParent: bool = ..., up: bool = ..., unlockMainConnection: bool = ..., ulk: bool = ..., updateMainConnection: bool = ..., upd: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Edit a characteristic of a dope sheet editor

    Args:
        autoFit | af: (edit, query) - on | off | tgl Auto fit-to-view.
        autoFitTime | aft: (edit, query) - on | off | tgl Auto fit-to-view along the time axis, as well.
        control | ctl: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        displayActiveKeyTangents | dat: (edit) - on | off | tgl Display active key tangents in the editor.
        displayActiveKeys | dak: (edit) - on | off | tgl Display active keys in the editor.
        displayInfinities | di: (edit) - on | off | tgl Display infinities in the editor.
        displayKeys | dk: (edit) - on | off | tgl Display keyframes in the editor.
        displayTangents | dtn: (edit) - on | off | tgl Display tangents in the editor.
        displayValues | dv: (edit) - on | off | tgl Display active keys and tangents values in the editor.
        docTag | dtg: (create, edit, query) - Attaches a tag to the editor.
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        filter | f: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        forceMainConnection | fmc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        hierarchyBelow | hb: (edit, query) - display animation for objects hierarchically
        highlightConnection | hlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        lockMainConnection | lck: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        lookAt | la: (edit) - all | selected | currentTime FitView helpers.
        mainListConnection | mlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        outliner | o: (edit, query) - the name of the outliner which is associated with the dope sheet
        panel | pnl: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent | p: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        selectionConnection | slc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        selectionWindow | sel: (edit, query) - The selection area specified as left, right, bottom, top respectively.
        showScene | sc: (edit, query) - display the scene summary object
        showSummary | ss: (edit, query) - display the summary object
        showTicks | stk: (edit, query) - display per animation tick divider in channel
        snapTime | st: (edit, query) - none | integer | keyframe Keyframe move snap in time.
        snapValue | sv: (edit, query) - none | integer | keyframe Keyframe move snap in values.
        stateString | sts: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        unParent | up: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection | ulk: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection | upd: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
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


def effector(*args, hide: bool = ..., hi: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The effector command is used to set the name or hidden
    flag for the effector.  The standard edit (-e) and query (-q) flags are
    used for edit and query functions.

    Args:
        hide | hi: (create, edit, query) - Specifies whether to hide drawing of effector if attached to a handle.
        name | n: (create, edit, query) - Specifies the name of the effector.
    """
    ...


def enableDevice(*args, apply: bool = ..., a: bool = ..., device: Optional[Union[str, bool]] = ..., d: Optional[Union[str, bool]] = ..., enable: bool = ..., en: bool = ..., monitor: bool = ..., m: bool = ..., record: bool = ..., rec: bool = ..., query: bool = ...) -> Any:
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
        apply | a: (create, query) - enable/disable "applyTake" for the specified channel(s)
        device | d: (create, query) - specifies the device to change
        enable | en: (create, query) - enable (or disable) monitor/record/apply
        monitor | m: (create, query) - enables/disables visible update for the device (default)
        record | rec: (create, query) - enable/disable "recordDevice" device recording
    """
    ...


def evaluationManager(*args, cycleCluster: Optional[Union[str, bool]] = ..., ccl: Optional[Union[str, bool]] = ..., disableInfo: Optional[Union[str, bool]] = ..., di: Optional[Union[str, bool]] = ..., empty: bool = ..., mt: bool = ..., enabled: bool = ..., e: bool = ..., fallbackTriggered: bool = ..., ft: bool = ..., idleAction: Optional[Union[int, bool]] = ..., ia: Optional[Union[int, bool]] = ..., idleBuild: bool = ..., ib: bool = ..., invalidate: bool = ..., inv: bool = ..., manipulation: bool = ..., man: bool = ..., manipulationPrevalidation: bool = ..., mp: bool = ..., manipulationReady: bool = ..., mr: bool = ..., mode: Optional[Union[str, bool]] = ..., m: Optional[Union[str, bool]] = ..., downstreamFrom: Optional[Union[str, bool]] = ..., dst: Optional[Union[str, bool]] = ..., nodeTypeGloballySerialize: bool = ..., ntg: bool = ..., nodeTypeParallel: bool = ..., ntp: bool = ..., nodeTypeSerialize: bool = ..., nts: bool = ..., nodeTypeUntrusted: bool = ..., ntu: bool = ..., upstreamFrom: Optional[Union[str, bool]] = ..., ust: Optional[Union[str, bool]] = ..., reduceGraphRebuild: bool = ..., rgr: bool = ..., safeMode: bool = ..., sfm: bool = ..., query: bool = ...) -> Any:
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
        cycleCluster | ccl: (create, query) - Returns a list of nodes that are stored together with the given one in a cycle cluster. The list will be empty when the evaluation mode is not active or the node is not in a cycle.
        disableInfo | di: (query) - Returns a list of strings that contain the reasons that the evaluation manager has been disabled (as distinct from it being deliberately turned off, e.g. because an unsupported node type or attribute value was encountered). If the list is empty then the evaluation manager is operating normally.
        empty | mt: (query) - Valid in query mode only. Checks to see if the evaluation graph has any nodes in it. This is independent of the current mode.
        enabled | e: (query) - Valid in query mode only. Checks to see if the evaluation manager is currently enabled. This is independent of the current mode.
        fallbackTriggered | ft: (query) - Valid in query mode only. Checks to see if fallback serial evaluation has been triggered. Will be true if errors during parallel execution have forced a fallback to serial mode. Will reset to false if the mode is changed again after the fallback was triggered.
        idleAction | ia: (create, query) - This flag sets the actions EM will perform on idle. It accepts the following values:  0 - No action 1 - Graph Rebuild 2 - EM Manipulation Preparation 3 - Graph Rebuild and EM Manipulation Preparation   Where:  Graph Rebuild will rebuild the evaluation graph on an idle event as soon as it is able to do so. EM ManipulationPreparation will get the evaluation manager to perform all the steps necessary for EM manipulation to be available after the next idle event.   Note: These idle actions only apply to the graph attached to the normal context. All other graphs will be built according to their own rules.  The disadvantage of enabling idle actions is that for some workflows that are changing the graph frequently, or very large graphs, the graph build and manipulation preparation time may impact the workflow. If workflows are impacted it is suggested to turn idle actions off by passing this flag a value of 0.
        idleBuild | ib: (create, query) - This flag is obsolete. Please use the -idleAction flag with a value of 1 in order to activate evaluation graph rebuild on idle.
        invalidate | inv: (create, query) - This flag invalidates the graph. Value is used to control auto rebuilding on idle (false) or forced (true). This command should be used as a last resort. In query mode it checks to see if the graph is valid.
        manipulation | man: (create, query) - This flag is used to activate evaluation manager manipulation support.
        manipulationPrevalidation | mp: (create, query) - This flag is used to activate evaluation manager manipulation prevalidation. Prevalidation checks for known patterns in manipulation.  In case of a successful prevalidation, there is no need to use dirty propagation in the first frame of manipulation to validate that EM manipulation can safely be used, and fast manipulation can start right away.
        manipulationReady | mr: (query) - Valid in query mode only. Checks to see if the evaluation manager manipulation is currently ready/allowed. This is independent of the current mode.
        mode | m: (create, query) - Changes the current evaluation mode in the evaluation manager. Supported values are "off", "serial" and "parallel".
        downstreamFrom | dst: (create, query) - Find the DG nodes that are immediately downstream of the named one in the evaluation graph. Note that the connectivity is via evaluation mode connections, not DG connections. In query mode the graph is walked and any nodes downstream of the named one are returned. The return type is alternating pairs of values that represent the graph level and the node name, e.g. if you walk downstream from A in the graph A -> B -> C then the return will be the array of strings ("0","A","1","B","2","C"). Scripts can deconstruct this information into something more visually recognizable. Note that cycles are likely to be present so any such scripts would have to handle them. 			In query mode, this flag needs a value.
        nodeTypeGloballySerialize | ntg: (create, query) - This flag is used only when the evaluation manager is in "parallel" mode but can be set at anytime. It activates or deactivates the override to force global serial scheduling for the class name argument(s) in the evaluation manager. Legal object values are class type names: e.g. "transform", "skinCluster", "mesh". When queried without specified nodes, it returns the list of nodes with the global serial scheduling override active. Scheduling overrides take precedence over all of the node and node type scheduling rules. Use with caution; certain nodes may not react well to alternative scheduling types.
        nodeTypeParallel | ntp: (create, query) - This flag is used only when the evaluation manager is in "parallel" mode but can be set at anytime. It activates or deactivates the override to force parallel scheduling for the class name argument(s) in the evaluation manager. Legal object values are class type names: e.g. "transform", "skinCluster", "mesh". When queried without specified nodes, it returns the list of nodes with the parallel scheduling override active. Scheduling overrides take precedence over all of the node and node type scheduling rules. Use with caution; certain nodes may not react well to alternative scheduling types.
        nodeTypeSerialize | nts: (create, query) - This flag is used only when the evaluation manager is in "parallel" mode but can be set at anytime. It activates or deactivates the override to force local serial scheduling for the class name argument(s) in the evaluation manager. Legal object values are class type names: e.g. "transform", "skinCluster", "mesh". When queried without specified nodes, it returns the list of nodes with the local serial scheduling override active. Scheduling overrides take precedence over all of the node and node type scheduling rules. Use with caution; certain nodes may not react well to alternative scheduling types.
        nodeTypeUntrusted | ntu: (create, query) - This flag is used only when the evaluation manager is in "parallel" mode but can be set at anytime. It activates or deactivates the override to force untrusted scheduling for the class name argument(s) in the evaluation manager. Legal object values are class type names: e.g. "transform", "skinCluster", "mesh". When queried without specified nodes, it returns the list of nodes with the untrusted scheduling override active. Scheduling overrides take precedence over all of the node and node type scheduling rules. Use with caution; certain nodes may not react well to alternative scheduling types. Untrusted scheduling will allow nodes to be evaluated in a critical section, separately from any other node evaluation. It should be used only as a last resort since the lost parallelism caused by untrusted nodes can greatly reduce performance.
        upstreamFrom | ust: (create, query) - Find the DG nodes that are immediately upstream of the named one in the evaluation graph. Note that the connectivity is via evaluation mode connections, not DG connections. In query mode the graph is walked and any nodes upstream of the named one are returned. The return type is alternating pairs of values that represent the graph level and the node name, e.g. if you walk upstream from C in the graph A -> B -> C then the return will be the array of strings ("0","C","1","B","2","A"). Scripts can deconstruct this information into something more visually recognizable. Note that cycles are likely to be present so any such scripts would have to handle them. 			In query mode, this flag needs a value.
        reduceGraphRebuild | rgr: (create, query) - This flag is used to activate evaluation manager mode to minimize rebuild when animated node are connected to EM prepopulated plug.
        safeMode | sfm: (create, query) - This flag activates/deactivates parallel evaluation safe mode. When enabled, parallel execution will fall back to serial when evaluation graph is missing dependencies. Detection is happening on scheduling of parallel evaluation, which means potential fallback will happen at the next evaluation. WARNING: This mode should be disabled with extreme caution. It will prevent parallel mode from falling back to serial mode when an invalid evaluation is detected. Sometimes the evaluation will still work correctly in those situations and use of this flag will keep the peak parallel performance running. However since the safe mode is used to catch invalid evaluation disabling it may also cause problems with evaluation, anything from invalid values, missing evaluation, or even crashes.
    """
    ...


def evaluator(*args, clusters: bool = ..., cl: bool = ..., configuration: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., enable: bool = ..., en: bool = ..., info: bool = ..., i: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., nodeType: Optional[Union[str, bool]] = ..., nt: Optional[Union[str, bool]] = ..., nodeTypeChildren: bool = ..., ntc: bool = ..., priority: Optional[Union[int, bool]] = ..., p: Optional[Union[int, bool]] = ..., valueName: Optional[Union[str, bool]] = ..., vn: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    Handles turning on and off custom evaluation overrides used by the evaluation
    manager.
    Query no flag to see all available custom evaluators.
    Query the 'enable' flag to check if an evaluator is currently enabled.
    If the 'name' flag isn't used then return all modes and their current
    active state.

    Args:
        clusters | cl: (query) - This flag queries the list of clusters currently assigned to the named custom evaluator. The return value will be an array of strings where the array consists of a set of (number, string[]) groups. e.g. If an evaluator has 2 clusters with 2 and 3 nodes in them respectively the output would be something like: (2, 'transform2', 'transform3', 3, 'joint1', 'joint2', 'joint3')
        configuration | c: (create, multiuse, query) - Sends configuration information to a custom evaluator. It's up to the evaluator to understand what they mean. Multiple configuration messages can be sent in a single command. Query this flag for a given evaluator to find out what configuration messages it accepts.
        enable | en: (create, query) - Enables or disables a specific graph evaluation runtime, depending on the state of the flag.  In order to use this flag you must also specify the name in the 'name' argument. When the 'enable' flag is used in conjunction with the 'nodeType' flag then it is used to selectively turn on or off the ability of the given evaluator to handle nodes of the given type (i.e. it no longer toggles the evaluator enabled state). When the 'enable' flag is used in conjunction with the 'configuration' flag then it is passed along with the configuration message interpreted by the custom evaluator.
        info | i: (query) - Queries the evaluator information. Only valid in query mode since the information is generated by the evaluator's internal state and cannot be changed. In order to use this flag, the 'name' argument must also be specified.
        name | n: (create, query) - Names a particular DG evaluation override evaluator. Evaluators are registered automatically by name. Query this flag to get a list of available runtimes. When a runtime is registered it is enabled by default. Use the 'enable' flag to change its enabled state. 			In query mode, this flag can accept a value.
        nodeType | nt: (create, multiuse, query) - Names a particular node type to be passed to the evaluator request. Evaluators can either use or ignore the node type information as passed. 			In query mode, this flag can accept a value.
        nodeTypeChildren | ntc: (create, query) - If enabled when using the 'nodeType' flag then handle all of the node types derived from the given one as well. Default is to only handle the named node type.
        priority | p: (create, query) - Query or set the evaluator priority. Custom evaluator with highest priority order will get the chance to claim the nodes first.  Evaluators must have unique priority values. In order to use this flag you must also specify the name in the 'name' argument.
        valueName | vn: (query) - Queries a value from a given evaluator.  Evaluators can define a set of values for which they answer. 			In query mode, this flag can accept a value.
    """
    ...


def filter(*args, name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., type: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Creates or modifies a filter node.  Filter nodes are used by applyTake
    to modify recorded device data before assigning it to the param curves
    for the attached attributes.

    Args:
        name | n: (create, edit, query) - Name for created filter
        type | t: (create, edit, query) - Filter type to create, One of:  filterEuler            Euler angle "demangler" filterResample         Resamples input data at fixed output rate with several filtering options filterSimplify         Combines groups of data points that are almost linear into lines segments filterClosestSample     Resamples input data a fixed output rate using the closest sample point
    """
    ...


def filterCurve(*args, cutoffFrequency: Optional[Union[float, bool]] = ..., cof: Optional[Union[float, bool]] = ..., endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., e: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., filter: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., keepKeysOnFrame: bool = ..., kof: bool = ..., kernel: Optional[Union[str, bool]] = ..., ker: Optional[Union[str, bool]] = ..., keySync: bool = ..., ks: bool = ..., maxTimeStep: Optional[Union[float, bool]] = ..., mxs: Optional[Union[float, bool]] = ..., minTimeStep: Optional[Union[float, bool]] = ..., mns: Optional[Union[float, bool]] = ..., period: Optional[Union[float, bool]] = ..., per: Optional[Union[float, bool]] = ..., precision: Optional[Union[float, bool]] = ..., pre: Optional[Union[float, bool]] = ..., precisionMode: Optional[Union[int, bool]] = ..., pm: Optional[Union[int, bool]] = ..., preserveKeyTangent: Optional[Union[str, bool]] = ..., pkt: Optional[Union[str, bool]] = ..., sampleCount: Optional[Union[int, bool]] = ..., sc: Optional[Union[int, bool]] = ..., samplingRate: Optional[Union[float, bool]] = ..., sr: Optional[Union[float, bool]] = ..., selectedKeys: bool = ..., sk: bool = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., s: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., timeTolerance: Optional[Union[float, bool]] = ..., tto: Optional[Union[float, bool]] = ..., tolerance: Optional[Union[float, bool]] = ..., tol: Optional[Union[float, bool]] = ..., useQuaternion: bool = ..., uq: bool = ..., width: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., w: Optional[Union[Union[float, Tuple[float, float]], bool]] = ...) -> Any:
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
        cutoffFrequency | cof: (create) - Defines the cutoff frequency (in Hz) for the Butterworth filter.
        endTime | e: (create) - Specify the end time of the section to filter. If not specified, the last key of the animation curve is used to define the end time.
        filter | f: (create) - Specifies the filter type to use. The avalible filters are: butterworth euler (default) gaussian keyReducer peakRemover keySync resample simplify
        keepKeysOnFrame | kof: (create) - When specified, a secondary filter pass is applied to position keys on whole frames. This flag is only supported by the Butterworth filter.
        kernel | ker: (create) - The resample kernel is a decimation resampling filter used to resample dense data. It works on the keyframes and may not produce the desired results when used with sparse data.  The resample filter converts from either uniform or non-uniform timestep input data samples to the specified uniform timeStep. Various time domain filters are available and are specified with the kernel flag which selects the resampling kernel applied to the keyframes on the animation curves.   Kernel Values closest  Closest sample to output timestamp lirp  Linear interpolation between closest samples box  Box filter: moving average triangle  Triangle filter: (1 - |x|)  weighted moving average gaussian2  Gaussian2 Filter: (2^(-2x*x))  weighted moving average gaussian4  Gaussian4 Filter: (2^(-4x*x))  weighted moving average   This filter is only targeted at decimation resampling -- interpolation resampling is basically unsupported.  If your output framerate is much higher than your input frame rate (approximate, as the input timestep is not assumed to be regular) the lirp and triangle will interpolate (usually) and the rest will either average, or use the closest sample (depending on the phase and frequency of the input).  However this mode of operation may not give the expected result.
        keySync | ks: (create) - When specified, a secondary filter pass is applied that adds a key to sibling curves (X,Y,Z) for each key that is encountered. This flag is only supported by the Key Reducer filter.
        maxTimeStep | mxs: (create) - Simplify filter.
        minTimeStep | mns: (create) - Simplify filter.
        period | per: (create) - Resample filter
        precision | pre: (create) - Defines the precision parameter. For the Key Reducer filter, this parameter specifies the error limit between the source and output curves. Greater values reduce precision. Lower values increase precision.
        precisionMode | pm: (create) - Defines whether the precision value should be treated as: 0: An absolute value 1: A percentage.
        preserveKeyTangent | pkt: (create, multiuse) - When specified, keys whose in or out tangent type match the specified type are preserved. Supported tangent types: fixed linear flat smooth step clamped plateau stepnext auto This flag is only supported by the Key Reducer filter.
        sampleCount | sc: (create) - Defines the Gaussian filter kernel dimension.
        samplingRate | sr: (create) - Defines the rate at which keys are added to the Butterworth filtered curve in frames per second (FPS).
        selectedKeys | sk: (create) - When specified, the filter is only applied to selected keys. This flag supercedes the startTime/endTime specification.
        startTime | s: (create) - Specify the start time to filter. If not specified, then the first key in the animation curve is used to get the start time.
        timeTolerance | tto: (create) - Simplify filter.
        tolerance | tol: (create) - Simplify filter.
        useQuaternion | uq: (create) - Enable to use quaternion instead of euler.
        width | w: (create) - Defines the width of the Gaussian filter.
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


def findKeyframe(*args, animation: Optional[Union[str, bool]] = ..., an: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., controlPoints: bool = ..., cp: bool = ..., curve: bool = ..., c: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., f: Optional[Union[Tuple[float, float], bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., hi: Optional[Union[str, bool]] = ..., includeUpperBound: bool = ..., iub: bool = ..., index: Optional[Union[int, bool]] = ..., shape: bool = ..., s: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., t: Optional[Union[Tuple[float, float], bool]] = ..., timeSlider: bool = ..., ts: bool = ..., which: Optional[Union[str, bool]] = ..., w: Optional[Union[str, bool]] = ...) -> Any:
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
        animation | an: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute | at: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        controlPoints | cp: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        curve | c: (create) - Return a list of the existing curves driving the selected object or attributes. The which, index, floatRange, timeRange, and includeUpperBound flags are ignored when this flag is used.
        float | f: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        hierarchy | hi: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        includeUpperBound | iub: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index | index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        shape | s: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        time | t: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
        timeSlider | ts: (create) - Get the next key time from the ticks displayed in the time slider. If this flag is set, then the -an/animation flag is ignored.
        which | w: (create) - next | previous | first | last How to find the key
    """
    ...


def flexor(*args, atBones: bool = ..., ab: bool = ..., atJoints: bool = ..., aj: bool = ..., deformerCommand: Optional[Union[str, bool]] = ..., dc: Optional[Union[str, bool]] = ..., list: bool = ..., l: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., noScale: bool = ..., ns: bool = ..., toSkeleton: bool = ..., ts: bool = ..., type: Optional[Union[str, bool]] = ..., typ: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a flexor. A flexor a deformer plus a set of
    driving    attributes. For example, a flexor might be a sculpt object
    that is driven by a joint's x rotation and a cube's y position.

    Args:
        atBones | ab: (create) - Add a flexor at bones. Flexor will be added at each of the selected bones, or at all bones in the selected skeleton if the -ts flag is also specified.
        atJoints | aj: (create) - Add a flexor at joints. Flexor will be added at each of the selected joints, or at all joints in the selected skeleton if the -ts flag is specified.
        deformerCommand | dc: (create) - String representing underlying deformer command string.
        list | l: (query) - List all possible types of flexors. Query mode only.
        name | n: (create) - This flag is obsolete.
        noScale | ns: (create) - Do not auto-scale the flexor to the size of the nearby geometry.
        toSkeleton | ts: (create) - Specifies that flexors will be added to the entire skeleton rather than just to the selected joints/bones. This flag is used in conjunction with the -ab and -aj flags.
        type | typ: (create) - Specifies which type of flexor. To see list of valid types, use the "flexor -query -list" command.
    """
    ...


def flow(*args, divisions: Optional[Union[Tuple[int, int, int], bool]] = ..., dv: Optional[Union[Tuple[int, int, int], bool]] = ..., localCompute: bool = ..., lc: bool = ..., localDivisions: Optional[Union[Tuple[int, int, int], bool]] = ..., ld: Optional[Union[Tuple[int, int, int], bool]] = ..., objectCentered: bool = ..., oc: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The flow command creates a deformation lattice to `bend' the object
    that is animated along a curve of a motion path animation.
    The motion path animation has to have the follow option set to be on.

    Args:
        divisions | dv: (query) - This flag specifies the number of lattice slices in x,y,z. The default values are 2 5 2. When queried, it returns the uint32_t uint32_t uint32_t
        localCompute | lc: (query) - This flag specifies whether or not to have local control over the object deformation. Default value: is on when the lattice is around the curve, and is off when the lattice is around the object.  When queried, it returns a boolean
        localDivisions | ld: (query) - This flag specifies the extent of the region of effect. Default values are 2 2 2. When queried, it returns the uint32_t uint32_t uint32_t
        objectCentered | oc: (query) - This flag specifies whether to create the lattice around the selected object at its center, or to create the lattice around the curve. Default value is true. When queried, it returns a boolean
    """
    ...


def freeze(*args, allNodes: bool = ..., all: bool = ..., displayLayers: bool = ..., dl: bool = ..., downstream: bool = ..., dn: bool = ..., forceDownstream: bool = ..., fd: bool = ..., frozen: bool = ..., f: bool = ..., invisible: bool = ..., i: bool = ..., noFreeze: bool = ..., n: bool = ..., unfreeze: bool = ..., uf: bool = ..., upstream: bool = ..., up: bool = ..., query: bool = ...) -> Any:
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
        allNodes | all: (create, query) - Select which nodes are to be used for the operation. If it is not set then the selection list will be used. If nothing is selected all nodes in the scene will be used. This flag can be used in query mode to find the set of frozen nodes in the scene. It can also be used in create mode with filters (displayLayers, invisible, or frozen) to target a specific subset of nodes in the scene.
        displayLayers | dl: (create, query) - If this flag is enabled then the display layers on the list to be processed will be walked. Any nodes they control will be added to the processing list, providing the display layer visibility control is off and not connected. Note: Animated visibility or enabled states will be treated as matches to be thorough. No attempt is made to check for static animation.
        downstream | dn: (create, query) - If this flag is enabled then the frozen state will attempt to propagate downstream from the selected nodes. e.g. the mesh shape deformations being controlled by a skeleton rig.
        forceDownstream | fd: (create, query) - If this flag is enabled then the frozen state will attempt to propagate downstream from the selected nodes. e.g. the mesh shape deformations being controlled by a skeleton rig. Unlike the downstream flag though this one will freeze downstream nodes even if they have other, unfrozen, inputs.
        frozen | f: (create, query) - If this flag is enabled then the list of nodes to be processed will be filtered out so that only nodes with the frozen attribute already set are included. Otherwise all nodes being processed will first have their frozen attribute set before propagating the frozen state. This flag would only be used if nodes were previously frozen and the command is used to propagate the frozen state through the graph.
        invisible | i: (create, query) - If this flag is enabled then the invisible nodes on the list to be processed will be walked. Any nodes below them in the DAG hierarchy will be added to the processing list, providing the visibility attribute is not connected. Note: Animated visibility states will be treated as a match to be thorough. No attempt is made to check for static animation.
        noFreeze | n: (create, query) - This flag previews the nodes that will be frozen without actually freezing them.
        unfreeze | uf: (create, query) - If this flag is enabled then the nodes being processed will have their frozen state turned off instead of on. All of the same filtering and propagating will be done when deciding which nodes to modify. In query mode this flag switches from returning the already-frozen nodes to returning the unfrozen nodes.
        upstream | up: (create, query) - If this flag is enabled then the frozen state will attempt to propagate upstream through the selected nodes. e.g. the param curves feeding into a frozen transform. Heuristics are applied to this propagation to ensure that upstream nodes that are still used by unfrozen nodes will stay unfrozen themselves.
    """
    ...


def freezeOptions(*args, displayLayers: bool = ..., dl: bool = ..., downstream: Optional[Union[str, bool]] = ..., dn: Optional[Union[str, bool]] = ..., explicitPropagation: bool = ..., ep: bool = ..., invisible: bool = ..., inv: bool = ..., referencedNodes: bool = ..., rn: bool = ..., runtimePropagation: bool = ..., rt: bool = ..., upstream: Optional[Union[str, bool]] = ..., up: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command provides access to the options used by the evaluation manager to
    handle propagation and recognition of when a node is in a frozen state.
    See the individual flags for the different options available.
    These values are all stored as user preferences and persist across sessions.

    Args:
        displayLayers | dl: (create, query) - If this option is enabled then any nodes that are in an enabled, invisible display layer will be considered to be frozen, and the frozen state will propagate accordingly.
        downstream | dn: (create, query) - Controls how frozen state is propagated downstream from currently frozen nodes. Valid values are "none" for no propagation, "safe" for propagation downstream only when all upstream nodes are frozen, and "force" for propagation downstream when any upstream node is frozen.
        explicitPropagation | ep: (create, query) - When turned on this will perform an extra pass when the evaluation graph is constructed to perform intelligent propagation of the frozen state to related nodes as specified by the currently enabled options of the evaluation graph. See also "runtimePropagation". This option performs more thorough propagation of the frozen state, but requires extra time for recalculating the evaluation graph.
        invisible | inv: (create, query) - If this option is enabled then any nodes that are invisible, either directly or via an invisible parent node, will be considered to be frozen, and the frozen state will propagate accordingly.
        referencedNodes | rn: (create, query) - If this option is enabled then any nodes that are referenced in from a frozen referenced node will also be considered to be frozen, and the frozen state will propagate accordingly.
        runtimePropagation | rt: (create, query) - When turned on this will allow the frozen state to propagate during execution of the evaluation graph. See also "explicitPropagation". This option allows frozen nodes to be scheduled for evaluation, but once it discovers a node that is frozen it will prune the evaluation based on the current set of enabled options. It only works in the downstream direction.
        upstream | up: (create, query) - Controls how frozen state is propagated upstream from currently frozen nodes. Valid values are "none" for no propagation, "safe" for propagation upstream only when all downstream nodes are frozen, and "force" for propagation upstream when any downstream node is frozen.
    """
    ...


def geomBind(*args, bindMethod: Optional[Union[int, bool]] = ..., bm: Optional[Union[int, bool]] = ..., falloff: Optional[Union[float, bool]] = ..., fo: Optional[Union[float, bool]] = ..., geodesicVoxelParams: Optional[Union[Tuple[int, bool], bool]] = ..., gvp: Optional[Union[Tuple[int, bool], bool]] = ..., maxInfluences: Optional[Union[int, bool]] = ..., mi: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to compute weights using geodesic voxel binding algorithm.
    It works by setting the right weights values on an already-existing skinCluster
    node.
    Since this command uses GPU acceleration, it is not supported on headless
    versions of Maya, i.e. batch mode.

    Args:
        bindMethod | bm: (create) - Specifies which bind algorithm to use. By default, Geodesic Voxel will be used. Available algorithms are: 3 - Geodesic Voxel
        falloff | fo: (create, edit, query) - Falloff controlling the bind stiffness. Valid values range from [0..1].
        geodesicVoxelParams | gvp: (create, edit, query) - Specifies the geodesic voxel binding parameters. This flag is composed of three parameters: 0 - Maximum voxel grid resolution which must be a power of two. (ie. 64, 128, 256, etc. ) 1 - Performs a post voxel state validation when enabled. Default values are 256 true.
        maxInfluences | mi: (create, edit, query) - Specifies the maximum influences a vertex can have. By default, all influences are used (-1).
    """
    ...


def geometryConstraint(*args, layer: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., remove: bool = ..., rm: bool = ..., targetList: bool = ..., tl: bool = ..., weight: Optional[Union[float, bool]] = ..., w: Optional[Union[float, bool]] = ..., weightAliasList: bool = ..., wal: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        layer | l: (create, edit) - Specify the name of the animation layer where the constraint should be added.
        name | n: (create, edit, query) - Sets the name of the constraint node to the specified name.  Default name is constrainedObjectName_constraintType
        remove | rm: (edit) - removes the listed target(s) from the constraint.
        targetList | tl: (query) - Return the list of target objects.
        weight | w: (create, edit, query) - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
        weightAliasList | wal: (query) - Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
    """
    ...


def ghosting(*args, action: Optional[Union[str, bool]] = ..., act: Optional[Union[str, bool]] = ..., allGhostedObjects: bool = ..., ago: bool = ..., allInRange: bool = ..., a: bool = ..., customFrames: Optional[Union[int, bool]] = ..., cf: Optional[Union[int, bool]] = ..., enable: bool = ..., en: bool = ..., farOpacity: Optional[Union[float, bool]] = ..., fo: Optional[Union[float, bool]] = ..., frames: bool = ..., f: bool = ..., geometryFilter: bool = ..., gf: bool = ..., ghostedObjects: bool = ..., go: bool = ..., ghostsStep: Optional[Union[int, bool]] = ..., gs: Optional[Union[int, bool]] = ..., hierarchy: bool = ..., h: bool = ..., jointFilter: bool = ..., jf: bool = ..., locatorFilter: bool = ..., lf: bool = ..., mode: Optional[Union[str, bool]] = ..., m: Optional[Union[str, bool]] = ..., nearOpacity: Optional[Union[float, bool]] = ..., no: Optional[Union[float, bool]] = ..., postColor: Optional[Union[Tuple[float, float, float], bool]] = ..., poc: Optional[Union[Tuple[float, float, float], bool]] = ..., postFrames: Optional[Union[int, bool]] = ..., pof: Optional[Union[int, bool]] = ..., preColor: Optional[Union[Tuple[float, float, float], bool]] = ..., prc: Optional[Union[Tuple[float, float, float], bool]] = ..., preFrames: Optional[Union[int, bool]] = ..., prf: Optional[Union[int, bool]] = ..., preset: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., resetAll: bool = ..., r: bool = ..., useDriver: bool = ..., ud: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Provides an aggregated interface to all of the node-base ghosting parameters, as well
    as the global preferences used by this command for ghosting actions.
    Query the 'enable' flag to check if ghost drawing is currently enabled.
    If you run in create mode with no 'action' set then you will be modifying the current values of the ghosting parameters.
    If you have 'action=ghost' set then you will be modifying the current values of the ghosting parameters and then applying them to selected objects.

    Args:
        action | act: (create) - Define the actions to be performed by the command. Legal values are "ghost", "unghost", and "unghostAll". The "ghost" will try to enable ghosting on all _visible_ DAG objects in the selection list. Imtermediate transform nodes will only be ghosted if axis display are active.
        allGhostedObjects | ago: (edit) - Only works in edit mode, specifying that the edits are to be applied to all ghosted objects instead of just the selected ones.
        allInRange | a: (create, edit, query) - In create mode, define the default value for whether keyframe mode should use every keyframe in the playback range or use the specified values. In edit mode, modify the all-in-range value for all ghosts. In create mode with the "ghost" action, also set the custom ghost all-in-range value for the selected objects.
        customFrames | cf: (create, edit, multiuse, query) - In create mode, define the default value for the list of custom ghost frames. In edit mode, modify the custom ghost frames for all ghosts. The special frame number "-9999999" is used to remove all custom frames, circumventing a quirk in the command engine that does not allow passing an empty list. In create mode with the "ghost" action, also set the custom ghost frames for the selected objects.
        enable | en: (create, query) - Enables or disables ghost visibility on the entire scene. This does not modify any of the node ghosting attributes, it only globally enables or disables the drawing of any ghosts that have been defined on nodes. This is a preference-based flag so its value will persist between sessions, even if you load a new file with different ghost attribute settings.
        farOpacity | fo: (create, edit, query) - In create mode, define the default value for the opacity value for ghosts farthest away from the current time. In edit mode, modify the opacity value of ghosts farthest away from the current time for all ghosts. In create mode with the "ghost" action, also set the opacity value of ghosts farthest away from the current time for the selected objects.
        frames | f: (query) - Queries the current set of ghost frames on the selected objects based on the ghosting mode, parameters set on the object, and the current time when relevant. Ignores the state of the ghosting enabled flag.
        geometryFilter | gf: (create, edit, query) - In create mode, enable or disable the default ghost geometry filter. In create mode with the "ghost" action set, also filter the selection to omit geometry nodes if this flag is false.
        ghostedObjects | go: (query) - Only works in query mode to find the names of all currently ghosted DAG nodes.
        ghostsStep | gs: (create, edit, query) - In create mode, define the default value for the number of steps (keyframes or frames) between ghosts. In edit mode, modify the number of steps (keyframes or frames) between ghosts. In create mode with the "ghost" action, also set the default number of steps (keyframes or frames) between ghosts for the selected objects.
        hierarchy | h: (create, edit, query) - Enables or disables the ghost hierarchy default value. When no ghosting action is set it does not modify any of the node ghosting attributes, it only sets the preference for how future commands will filter the list of affected nodes. When used in conjunction with a ghosting action it will fist set the preference value and then use that new value as a filter on the ghosting action. If a ghosting action is specified without this flag then the current value of the preference is used in its place. This is a preference-based flag so its value will persist between sessions, even if you load a new file with different ghost attribute settings.
        jointFilter | jf: (create, edit, query) - In create mode, enable or disable the default ghost joint filter. In create mode with the "ghost" action set, also filter the selection to omit joint nodes if this flag is false.
        locatorFilter | lf: (create, edit, query) - In create mode, enable or disable the default ghost locator filter. In create mode with the "ghost" action set, also filter the selection to omit locator nodes if this flag is false.
        mode | m: (create, edit, query) - Define the default mode for ghosting actions. Legal values are "preAndPost", "pre", "post", "custom", and "keyframes".
        nearOpacity | no: (create, edit, query) - In create mode, define the default value for the opacity value for ghosts nearest to the current time. In edit mode, modify the opacity value of ghosts nearest to the current time for all ghosts. In create mode with the "ghost" action, also set the opacity value of ghosts nearest to the current time for the selected objects.
        postColor | poc: (create, edit, query) - In create mode, define the default value for the color of ghosts after the current time. In edit mode, modify the color of ghosts after the current time for all ghosts. In create mode with the "ghost" action, also set the color of ghosts after the current time for the selected objects.
        postFrames | pof: (create, edit, query) - In create mode, define the default value for the number of ghosted frames after the current time. In edit mode, modify the number of ghosted frames after the current time for all ghosts. In create mode with the "ghost" action, also set the default number of ghosted frames after the current time for the selected objects.
        preColor | prc: (create, edit, query) - In create mode, define the default value for the color of ghosts before the current time. In edit mode, modify the color of ghosts before the current time for all ghosts. In create mode with the "ghost" action, also set the color of ghosts before the current time for the selected objects.
        preFrames | prf: (create, edit, query) - In create mode, define the default value for the number of ghosted frames before the current time. In edit mode, modify the number of ghosted frames before the current time for all ghosts. In create mode with the "ghost" action, also set the default number of ghosted frames before the current time for the selected objects.
        preset | p: (create, edit, query) - Define the default mode for ghosting presets. Legal values are "1s", "2s", "4s", "5s", "10s", and "Custom". Setting anything other than "Custom" fixes ghosts at 3 pre frames, 3 post frames, with a step value of the preset (e.g. "2s" means show ghosts at every second frame or keyframe)
        resetAll | r: (create, edit) - Reset all ghosting options to their default values. Use with caution!
        useDriver | ud: (create, edit, query) - In create mode, enable or disable the default ghost use driver value. In edit mode, modify the use driver value of all existing ghosts. In create mode with the "ghost" action, also set the use driver value for the selected objects.
    """
    ...


def hikGlobals(*args, releaseAllPinning: bool = ..., rap: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Sets global HumanIK flags for the application.

    Args:
        releaseAllPinning | rap: (edit, query) - Sets the global release all pinning hik flag. When this flag is set, all pinning states are ignored.
    """
    ...


def ikfkDisplayMethod(*args, display: Optional[Union[str, bool]] = ..., d: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    The ikfkDisplayMethod command is used to specify how ik/fk
          blending should be shown

    Args:
        display | d: (create, query) - Specify how ik/fk blending should be shown when the handle is selected. Possible choices are "none" (do not display any blending), "ik" (only show ik),"fk" (only show fk), and "ikfk" (show both ik and fk).
    """
    ...


def ikHandle(*args, autoPriority: bool = ..., ap: bool = ..., connectEffector: bool = ..., ce: bool = ..., createCurve: bool = ..., ccv: bool = ..., createRootAxis: bool = ..., cra: bool = ..., curve: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., disableHandles: bool = ..., dh: bool = ..., enableHandles: bool = ..., eh: bool = ..., endEffector: Optional[Union[str, bool]] = ..., ee: Optional[Union[str, bool]] = ..., exists: str = ..., ex: str = ..., forceSolver: bool = ..., fs: bool = ..., freezeJoints: bool = ..., fj: bool = ..., jointList: bool = ..., jl: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., numSpans: Optional[Union[int, bool]] = ..., ns: Optional[Union[int, bool]] = ..., parentCurve: bool = ..., pcv: bool = ..., positionWeight: Optional[Union[float, bool]] = ..., pw: Optional[Union[float, bool]] = ..., priority: Optional[Union[int, bool]] = ..., p: Optional[Union[int, bool]] = ..., rootOnCurve: bool = ..., roc: bool = ..., rootTwistMode: bool = ..., rtm: bool = ..., setupForRPsolver: bool = ..., srp: bool = ..., simplifyCurve: bool = ..., scv: bool = ..., snapCurve: bool = ..., snc: bool = ..., snapHandleFlagToggle: bool = ..., shf: bool = ..., snapHandleToEffector: bool = ..., see: bool = ..., solver: Optional[Union[str, bool]] = ..., sol: Optional[Union[str, bool]] = ..., startJoint: Optional[Union[str, bool]] = ..., sj: Optional[Union[str, bool]] = ..., sticky: Optional[Union[str, bool]] = ..., s: Optional[Union[str, bool]] = ..., twistType: Optional[Union[str, bool]] = ..., tws: Optional[Union[str, bool]] = ..., weight: Optional[Union[float, bool]] = ..., w: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        autoPriority | ap: (edit) - Specifies that this handle's priority is assigned automatically.  The assigned priority will be based on the hierarchy distance from the root of the skeletal chain to the start joint of the handle.
        connectEffector | ce: (create, edit) - This option is set to true as default, meaning that end-effector translate is connected with the endJoint translate.
        createCurve | ccv: (create) - Specifies if a curve should automatically be created for the ikSplineHandle.
        createRootAxis | cra: (create) - Specifies if a root transform should automatically be created above the joints affected by the ikSplineHandle. This option is used to prevent the root flipping singularity on a motion path.
        curve | c: (create, edit, query) - Specifies the curve to be used by the ikSplineHandle. Joints will be moved to align with this curve. This flag is mandatory if you use the -freezeJoints option.
        disableHandles | dh: (edit) - set given handles to full fk (ikBlend attribute = 0.0)
        enableHandles | eh: (edit) - set given handles to full ik (ikBlend attribute = 1.0)
        endEffector | ee: (create, edit, query) - Specifies the end-effector of the handle's joint chain. The end effector may be specified with a joint or an end-effector.  If a joint is specified, an end-effector will be created at the same position as the joint and this new end-effector will be used as the end-effector.
        exists | ex: (edit) - Indicates if the specified handle exists or not.
        forceSolver | fs: (create, edit, query) - Forces the solver to be used everytime. It could also be known as animSticky. So, after you set the first key the handle is sticky.
        freezeJoints | fj: (create, edit) - Forces the curve, specfied by -curve option, to align itself along the existing joint chain. When false, or unspecified, the joints will be moved to positions along the specified curve.
        jointList | jl: (edit) - Returns the list of joints that the handle is manipulating.
        name | n: (create, edit, query) - Specifies the name of the handle.
        numSpans | ns: (create) - Specifies the number of spans in the automatically generated curve of the ikSplineHandle.
        parentCurve | pcv: (create) - Specifies if the curve should automatically be parented to the parent of the first joint affected by the ikSplineHandle.
        positionWeight | pw: (create, edit, query) - Specifies the position/orientation weight of a handle. This is used to compute the "distance" between the goal position and the end-effector position.  A positionWeight of 1.0 computes the distance as the distance between positions only and ignores the orientations.  A positionWeight of 0.0 computes the distance as the distance between the orientations only and ignores the positions.  A positionWeight of 0.5 attempts to weight the distances equally but cannot actually compute this due to unit differences. Because there is no way to add linear units and angular units.
        priority | p: (create, edit, query) - Sets the priority of the handle.  Logically, all handles with a lower number priority are solved before any handles with a higher numbered priority.  (All handles of priority 1 are solved before any handles of priority 2 and so on.)  Handle priorities must be ] 0.
        rootOnCurve | roc: (create, edit, query) - Specifies if the root is locked onto the curve of the ikSplineHandle.
        rootTwistMode | rtm: (create, edit, query) - Specifies whether the start joint is allowed to twist or not. If not, then the required twist is distributed over the remaining joints. This applies to all the twist types.
        setupForRPsolver | srp: (edit) - If the flag is set and ikSolver is ikRPsolver, call RPRotateSetup for the new ikHandle. It is for ikRPsolver only.
        simplifyCurve | scv: (create) - Specifies if the ikSplineHandle curve should be simplified.
        snapCurve | snc: (create) - Specifies if the curve should automatically snap to the first joint affected by the ikSplineHandle.
        snapHandleFlagToggle | shf: (create, edit, query) - Specifies that the handle position should be snapped to the end-effector position if the end-effector is moved by the user.  Setting this flag on allows you to use forward kinematics to pose or adjust your skeleton and then to animate it with inverse kinematics.
        snapHandleToEffector | see: (edit) - All handles are immediately moved so that the handle position and orientation matches the end-effector position and orientation.
        solver | sol: (create, edit, query) - Specifies the solver.  The complete list of available solvers may not be known until run-time because some of the solvers may be implemented as plug-ins.  Currently the only valid solver are ikRPsolver, ikSCsolver and ikSplineSolver.
        startJoint | sj: (create, edit, query) - Specifies the start joint of the handle's joint chain.
        sticky | s: (create, edit, query) - Specifies that this handle is "sticky". Valid values are "off", "sticky", "superSticky". Sticky handles are solved when the skeleton is being manipulated interactively.  If a character has sticky feet, the solver will attempt to keep them in the same position as the user moves the character's root.  If they were not sticky, they would move along with the root.
        twistType | tws: (create, edit, query) - Specifies the type of interpolation to be used by the ikSplineHandle.  The interpolation options are "linear", "easeIn", "easeOut", and "easeInOut".
        weight | w: (create, edit, query) - Specifies the handles weight in error calculations.  The weight only applies when handle goals are in conflict and cannot be solved simultaneously.  When this happens, a solution is computed that weights the "distance" from each goal to the solution by the handle's weight and attempts to minimize this value.  The weight must be ]= 0.
    """
    ...


def ikHandleDisplayScale(*args, edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This action modifies and queries the current display size of ikHandle.
    The default display scale is 1.0.

    Args:
    """
    ...


def ikSolver(*args, epsilon: Optional[Union[float, bool]] = ..., ep: Optional[Union[float, bool]] = ..., maxIterations: Optional[Union[int, bool]] = ..., mxi: Optional[Union[int, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., solverType: Optional[Union[str, bool]] = ..., st: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The ikSolver command is used to set the attributes for an IK Solver
    or create a new one. The standard edit (-e) and query (-q) flags are
    used for edit and query functions.

    Args:
        epsilon | ep: (create, edit, query) - max error
        maxIterations | mxi: (create, edit, query) - Sets the max iterations for a solution
        name | n: (create, edit, query) - Name of solver
        solverType | st: (create, edit, query) - valid solverType (only ikSystem knows what is valid) for creation of a new solver (required)
    """
    ...


def ikSystem(*args, allowRotation: bool = ..., ar: bool = ..., autoPriority: bool = ..., ap: bool = ..., autoPriorityMC: bool = ..., apm: bool = ..., autoPrioritySC: bool = ..., aps: bool = ..., list: Optional[Union[Tuple[int, int], bool]] = ..., ls: Optional[Union[Tuple[int, int], bool]] = ..., snap: bool = ..., sn: bool = ..., solve: bool = ..., sol: bool = ..., solverTypes: bool = ..., st: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The ikSystem command is used to set the global snapping flag for handles
    and set the global solve flag for solvers.  The standard edit (-e) and
    query (-q) flags are used for edit and query functions.

    Args:
        allowRotation | ar: (edit, query) - Set true to allow rotation of an ik handle with keys set on translation.
        autoPriority | ap: (edit) - set autoPriority for all ikHandles
        autoPriorityMC | apm: (edit) - set autoPriority for all multiChain handles
        autoPrioritySC | aps: (edit) - set autoPriority for all singleChain handles
        list | ls: (edit, query) - returns the solver execution order when in query mode(list of strings) changes execution order when in edit mode (int old position, int new position)
        snap | sn: (edit, query) - Set global snapping
        solve | sol: (edit, query) - Set global solve
        solverTypes | st: (query) - returns a list of valid solverTypes ( query only )
    """
    ...


def ikSystemInfo(*args, globalSnapHandle: bool = ..., gsh: bool = ..., query: bool = ...) -> Any:
    r"""
    This action modifies and queries the current ikSystem controls.

    Args:
        globalSnapHandle | gsh: (create, query) - If this flag is off, all ikHandles will not be snapped.
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


def joint(*args, absolute: bool = ..., a: bool = ..., angleX: Optional[Union[float, bool]] = ..., ax: Optional[Union[float, bool]] = ..., angleY: Optional[Union[float, bool]] = ..., ay: Optional[Union[float, bool]] = ..., angleZ: Optional[Union[float, bool]] = ..., az: Optional[Union[float, bool]] = ..., assumePreferredAngles: bool = ..., apa: bool = ..., automaticLimits: bool = ..., al: bool = ..., children: bool = ..., ch: bool = ..., component: bool = ..., co: bool = ..., degreeOfFreedom: Optional[Union[str, bool]] = ..., dof: Optional[Union[str, bool]] = ..., exists: Optional[Union[str, bool]] = ..., ex: Optional[Union[str, bool]] = ..., limitSwitchX: bool = ..., lsx: bool = ..., limitSwitchY: bool = ..., lsy: bool = ..., limitSwitchZ: bool = ..., lsz: bool = ..., limitX: Optional[Union[Tuple[float, float], bool]] = ..., lx: Optional[Union[Tuple[float, float], bool]] = ..., limitY: Optional[Union[Tuple[float, float], bool]] = ..., ly: Optional[Union[Tuple[float, float], bool]] = ..., limitZ: Optional[Union[Tuple[float, float], bool]] = ..., lz: Optional[Union[Tuple[float, float], bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., orientJoint: str = ..., oj: str = ..., orientation: Optional[Union[Tuple[float, float, float], bool]] = ..., o: Optional[Union[Tuple[float, float, float], bool]] = ..., position: Optional[Union[Tuple[float, float, float], bool]] = ..., p: Optional[Union[Tuple[float, float, float], bool]] = ..., radius: Optional[Union[float, bool]] = ..., rad: Optional[Union[float, bool]] = ..., relative: bool = ..., r: bool = ..., rotationOrder: Optional[Union[str, bool]] = ..., roo: Optional[Union[str, bool]] = ..., scale: Optional[Union[Tuple[float, float, float], bool]] = ..., s: Optional[Union[Tuple[float, float, float], bool]] = ..., scaleCompensate: bool = ..., sc: bool = ..., scaleOrientation: Optional[Union[Tuple[float, float, float], bool]] = ..., so: Optional[Union[Tuple[float, float, float], bool]] = ..., secondaryAxisOrient: str = ..., sao: str = ..., setPreferredAngles: bool = ..., spa: bool = ..., stiffnessX: Optional[Union[float, bool]] = ..., stx: Optional[Union[float, bool]] = ..., stiffnessY: Optional[Union[float, bool]] = ..., sty: Optional[Union[float, bool]] = ..., stiffnessZ: Optional[Union[float, bool]] = ..., stz: Optional[Union[float, bool]] = ..., symmetry: bool = ..., sym: bool = ..., symmetryAxis: Optional[Union[str, bool]] = ..., sa: Optional[Union[str, bool]] = ..., zeroScaleOrient: bool = ..., zso: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        absolute | a: (create, edit, query) - The joint center position is in absolute world coordinates. (This is the default.)
        angleX | ax: (create, edit, query) - Set the x-axis angle. When queried, this flag returns a float.
        angleY | ay: (create, edit, query) - Set the y-axis angle. When queried, this flag returns a float.
        angleZ | az: (create, edit, query) - Set the z-axis angle. When queried, this flag returns a float.
        assumePreferredAngles | apa: (edit) - Meaningful only in the edit mode. It sets the joint angles to the corresponding preferred angles.
        automaticLimits | al: (create) - Meaningful only in edit mode. It sets the joint to appropriate hinge joint with joint limits. It modifies the joint only if (a) it connects exactly to two joints (one parent, one child), (b) it does not lie on the line drawn between the two connected joints, and the plane it forms with the two connected joints is perpendicular to one of its rotation axes.
        children | ch: (edit) - It tells the command to apply all the edit options not only to the selected joints, but also to their descendent joints in the DAG.
        component | co: (create, edit) - Use with the -position switch to position the joint relative to its parent (like -relative) but to compute new positions for all children joints so their world coordinate positions do not change.
        degreeOfFreedom | dof: (create, edit, query) - Specifies the degrees of freedom for the IK. Valid strings consist of non-duplicate letters from x, y, and z. The letters in the string indicate what rotations are to be used by IK. The order a letter appear in the string does not matter. Examples are x, yz, xyz. When queried, this flag returns a string. Modifying dof will change the locking state of the corresponding rotation attributes. The rule is: if an rotation is turned into a dof, it will be unlocked if it is currently locked. When it is turned into a non-dof, it will be locked if it is not currently locked.
        exists | ex: (query) - Does the named joint exist? When queried, this flag returns a boolean.
        limitSwitchX | lsx: (create, edit, query) - Use the limit the x-axis rotation? When queried, this flag returns a boolean.
        limitSwitchY | lsy: (create, edit, query) - Use the limit the y-axis rotation? When queried, this flag returns a boolean.
        limitSwitchZ | lsz: (create, edit, query) - Use the Limit the z-axis rotation? When queried, this flag returns a boolean.
        limitX | lx: (create, edit, query) - Set lower and upper limits on the x-axis of rotation.  Also turns on the joint limit. When queried, this flag returns 2 floats.
        limitY | ly: (create, edit, query) - Set lower and upper limits on the y-axis of rotation.  Also turns on the joint limit. When queried, this flag returns 2 floats.
        limitZ | lz: (create, edit, query) - Set lower and upper limits on the z-axis of rotation.  Also turns on the joint limit. When queried, this flag returns 2 floats.
        name | n: (create, edit, query) - Specifies the name of the joint. When queried, this flag returns a string.
        orientJoint | oj: (edit) - The argument can be one of the following strings: xyz, yzx, zxy, zyx, yxz, xzy, none.  It modifies the joint orientation and scale orientation so that the axis indicated by the first letter in the argument will be aligned with the vector from this joint to its first child joint. For example, if the argument is "xyz", the x-axis will point towards the child joint.  The alignment of the remaining two joint orient axes are dependent on whether or not the -sao/-secondaryAxisOrient flag is used. If the -sao flag is used, see the documentation for that flag for how the remaining axes are aligned.  In the absence of a user specification for the secondary axis orientation, the rotation axis indicated by the last letter in the argument will be aligned with the vector perpendicular to first axis and the vector from this joint to its parent joint.  The remaining axis is aligned according the right hand rule.  If the argument is "none", the joint orientation will be set to zero and its effect to the hierarchy below will be offset by modifying the scale orientation.  The flag will be ignored if:  A. the joint has non-zero rotations when the argument is not "none".  B. the joint does not have child joint, or the distance to the child joint is zero when the argument is not "none".  C. either flag -o or -so is set.
        orientation | o: (create, edit, query) - The joint orientation. When queried, this flag returns 3 floats.
        position | p: (create, edit, query) - Specifies the position of the center of the joint. This position may be relative to the joint's parent or in absolute world coordinates (see -r and -a below). When queried, this flag returns 3 floats.
        radius | rad: (create, edit, query) - Specifies the joint radius.
        relative | r: (create, edit, query) - The joint center position is relative to the joint's parent.
        rotationOrder | roo: (create, edit, query) - The rotation order of the joint. The argument can be one of the following strings: xyz, yzx, zxy, zyx, yxz, xzy.
        scale | s: (create, edit, query) - Scale of the joint. When queried, this flag returns 3 floats.
        scaleCompensate | sc: (create, edit, query) - It sets the scaleCompenstate attribute of the joint to the given argument. When this is true, the scale of the parent joint will be compensated before any rotation of this joint is applied, so that the bone to the joint is scaled but not the bones to its child joints. When queried, this flag returns an boolean.
        scaleOrientation | so: (create, edit, query) - Set the orientation of the coordinate axes for scaling. When queried, this flag returns 3 floats.
        secondaryAxisOrient | sao: (edit) - The argument can be one of the following strings: xup, xdown, yup, ydown, zup, zdown, none.  This flag is used in conjunction with the -oj/orientJoint flag. It specifies the scene axis that the second axis should align with. For example, a flag combination of "-oj yzx -sao yup" would result in the y-axis pointing down the bone, the z-axis oriented with the scene's positive y-axis, and the x-axis oriented according to the right hand rule.
        setPreferredAngles | spa: (edit) - Meaningful only in the edit mode. It sets the preferred angles to the current joint angles.
        stiffnessX | stx: (create, edit, query) - Set the stiffness (from 0 to 100.0) for x-axis. When queried, this flag returns a float.
        stiffnessY | sty: (create, edit, query) - Set the stiffness (from 0 to 100.0) for y-axis. When queried, this flag returns a float.
        stiffnessZ | stz: (create, edit, query) - Set the stiffness (from 0 to 100.0) for z-axis. When queried, this flag returns a float.
        symmetry | sym: (create, edit) - Create a symmetric joint from the current joint.
        symmetryAxis | sa: (create, edit) - This flag specifies the axis used to mirror symmetric joints. Any combination of x, y, z can be used. This option is only used when the symmetry flag is set to True.
        zeroScaleOrient | zso: (edit) - It sets the scale orientation to zero and compensate the change by modifing the translation and joint orientation for joint or rotation for general transform of all its child transformations.  The flag will be ignored if the flag -so is set.
    """
    ...


def jointCluster(*args, aboveBound: Optional[Union[float, bool]] = ..., ab: Optional[Union[float, bool]] = ..., aboveCluster: bool = ..., ac: bool = ..., aboveDropoffType: Optional[Union[str, bool]] = ..., adt: Optional[Union[str, bool]] = ..., aboveValue: Optional[Union[float, bool]] = ..., av: Optional[Union[float, bool]] = ..., belowBound: Optional[Union[float, bool]] = ..., bb: Optional[Union[float, bool]] = ..., belowCluster: bool = ..., bc: bool = ..., belowDropoffType: Optional[Union[str, bool]] = ..., bdt: Optional[Union[str, bool]] = ..., belowValue: Optional[Union[float, bool]] = ..., bv: Optional[Union[float, bool]] = ..., deformerTools: bool = ..., dt: bool = ..., joint: Optional[Union[str, bool]] = ..., j: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        aboveBound | ab: (create, edit, query) - Specifies the where the drop-off begins in the direction of the bone above the joint. A value of 100 indicates the entire length of the bone. The default value is 10.
        aboveCluster | ac: (query) - Returns the name of the cluster associated with the bone above this joint.
        aboveDropoffType | adt: (create, edit, query) - Specifies the type of percentage drop-off in the direction of the bone above this joint. Valid values are "linear", "exponential", "sine" and "none". Default is linear.
        aboveValue | av: (create, edit, query) - Specifies the drop-off percentage of the joint cluster in the direction of the bone above the cluster. A value of 100 indicates the entire length of the bone. The default value is 50.
        belowBound | bb: (create, edit, query) - Specifies where the drop-off ends in the direction of the bone below the joint. A value of 100 indicates the entire length of the bone. The default value is 10.
        belowCluster | bc: (query) - Returns the name of the cluster associated with this joint.
        belowDropoffType | bdt: (create, edit, query) - Specifies the type of type of percentage drop-off in the direction of the bone below this joint. Valid values are "linear", "exponential", "sine" and "none". Default is linear.
        belowValue | bv: (create, edit, query) - Specifies the drop-off percentage of the joint cluster in the direction of the joint below the cluster. A value of 100 indicates the entire length of the bone. The default value is 50.
        deformerTools | dt: (query) - Used to query for the helper nodes associated with the jointCluster.
        joint | j: (create) - Specifies the joint that the cluster should act about.
        name | n: (create) - This flag is obsolete.
    """
    ...


def jointDisplayScale(*args, absolute: bool = ..., a: bool = ..., ikfk: Optional[Union[float, bool]] = ..., ik: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        absolute | a: (create, edit, query) - Interpret the float argument as the display size as opposed to the scale factor.
        ikfk | ik: (create, edit, query) - Set the display size of ik/fk skeleton joints.
    """
    ...


def jointLattice(*args, after: bool = ..., af: bool = ..., afterReference: bool = ..., ar: bool = ..., before: bool = ..., bf: bool = ..., components: bool = ..., cmp: bool = ..., creasing: Optional[Union[float, bool]] = ..., cr: Optional[Union[float, bool]] = ..., deformerTools: bool = ..., dt: bool = ..., exclusive: Optional[Union[str, bool]] = ..., ex: Optional[Union[str, bool]] = ..., frontOfChain: bool = ..., foc: bool = ..., geometry: Optional[Union[str, bool]] = ..., g: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., gi: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., ihs: bool = ..., joint: Optional[Union[str, bool]] = ..., j: Optional[Union[str, bool]] = ..., lengthIn: Optional[Union[float, bool]] = ..., li: Optional[Union[float, bool]] = ..., lengthOut: Optional[Union[float, bool]] = ..., lo: Optional[Union[float, bool]] = ..., lowerBindSkin: Optional[Union[str, bool]] = ..., lb: Optional[Union[str, bool]] = ..., lowerTransform: Optional[Union[str, bool]] = ..., lt: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., parallel: bool = ..., par: bool = ..., prune: bool = ..., pr: bool = ..., remove: bool = ..., rm: bool = ..., rounding: Optional[Union[float, bool]] = ..., ro: Optional[Union[float, bool]] = ..., selectedComponents: bool = ..., cms: bool = ..., split: bool = ..., sp: bool = ..., upperBindSkin: Optional[Union[str, bool]] = ..., ub: Optional[Union[str, bool]] = ..., upperTransform: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., useComponentTags: bool = ..., uct: bool = ..., widthLeft: Optional[Union[float, bool]] = ..., wl: Optional[Union[float, bool]] = ..., widthRight: Optional[Union[float, bool]] = ..., wr: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates/edits/queries a jointLattice deformer. The name
    of the created/edited object is returned. Usually you would make use of
    this functionality through the higher level flexor command.

    Args:
        after | af: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference | ar: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before | bf: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        components | cmp: (query) - Returns the components used by the deformer
        creasing | cr: (create, edit, query) - Affects the bulging of lattice points on the inside of the bend.  Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.
        deformerTools | dt: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        exclusive | ex: (create, query) - Puts the deformation set in a deform partition.
        frontOfChain | foc: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry | g: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices | gi: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected | ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections | ihs: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        joint | j: (create) - Specifies the joint which will be used to drive the bulging behaviours.
        lengthIn | li: (create, edit, query) - Affects the location of lattice points on the parent bone.  Positive/negative values cause the points to move away/towards the joint. Changing this parameter also modifies the regions affected by the creasing, rounding and width parameters. Default value is 0.0. When queried, this flag returns a float.
        lengthOut | lo: (create, edit, query) - Affects the location of lattice points on the child bone. Positive/negative values cause the points to move away/towards the joint. Changing this parameter also modifies the regions affected by the creasing, rounding and width parameters. Default value is 0.0. When queried, this flag returns a float.
        lowerBindSkin | lb: (create) - Specifies the node which is performing the bind skin operation on the geometry associated with the lower bone.
        lowerTransform | lt: (create) - Specifies which dag node is being used to rigidly transform the lower part of the lattice which this node is going to deform. If this flag is not specified an identity matrix will be assumed.
        name | n: (create) - Used to specify the name of the node being created.
        parallel | par: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        prune | pr: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        remove | rm: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        rounding | ro: (create, edit, query) - Affects the bulging of lattice points on the outside of the bend. Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.
        selectedComponents | cms: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        split | sp: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        upperBindSkin | ub: (create) - Specifies the node which is performing the bind skin operation on the geometry associated with the upper bone.
        upperTransform | ut: (create) - Specifies which dag node is being used to rigidly transform the upper part of the lattice which this node is going to deform. If this flag is not specified an identity matrix will be assumed.
        useComponentTags | uct: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
        widthLeft | wl: (create, edit, query) - Affects the bulging of lattice points on the left side of the bend. Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.
        widthRight | wr: (create, edit, query) - Affects the bulging of lattice points on the right side of the bend. Positive/negative values cause the points to bulge outwards/inwards. Default value is 0.0. When queried, this flag returns a float.
    """
    ...


def keyframe(*args, absolute: bool = ..., a: bool = ..., adjustBreakdown: bool = ..., abd: bool = ..., animation: Optional[Union[str, bool]] = ..., an: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., breakdown: bool = ..., bd: bool = ..., clipTime: Optional[Union[Tuple[float, float, float], bool]] = ..., ct: Optional[Union[Tuple[float, float, float], bool]] = ..., controlPoints: bool = ..., cp: bool = ..., eval: bool = ..., ev: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., f: Optional[Union[Tuple[float, float], bool]] = ..., floatChange: Optional[Union[float, bool]] = ..., fc: Optional[Union[float, bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., hi: Optional[Union[str, bool]] = ..., includeUpperBound: bool = ..., iub: bool = ..., index: Optional[Union[int, bool]] = ..., indexValue: bool = ..., iv: bool = ..., keyframeCount: bool = ..., kc: bool = ..., lastSelected: bool = ..., lsl: bool = ..., name: bool = ..., n: bool = ..., option: Optional[Union[str, bool]] = ..., o: Optional[Union[str, bool]] = ..., relative: bool = ..., r: bool = ..., selected: bool = ..., sl: bool = ..., shape: bool = ..., s: bool = ..., tickDrawSpecial: bool = ..., tds: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., t: Optional[Union[Tuple[float, float], bool]] = ..., timeChange: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., tc: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., valueChange: Optional[Union[float, bool]] = ..., vc: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        absolute | a: (create) - Move amounts are absolute.
        adjustBreakdown | abd: (create) - When false, moving keys will not preserve breakdown timing, when true (the default) breakdowns will be adjusted to preserve their timing relationship.
        animation | an: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute | at: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        breakdown | bd: (create, edit, query) - Sets the breakdown state for the key.  Returns an integer.  Default is false.  The breakdown state of a key cannot be set in the same command as it is moved (i.e., via the -tc or -fc flags).
        clipTime | ct: (create) - Modifies the final time where a key is inserted using an offset, pivot, and scale.
        controlPoints | cp: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        eval | ev: (create, query) - Returns the value(s) of the animCurves when evaluated (without regard to input connections) at the times given by the -t/time or -f/float flags.  Cannot be used in combination with other query flags, and cannot be used with time ranges (-t "5:10"). When no -t or -f flags appear on the command line, the evals are queried at the current time.  Query returns a float[].
        float | f: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        floatChange | fc: (create, edit, query) - How much (with -relative) or where (with -absolute) to move keys (on non-time-input animation curves) along the x (float) axis. Returns float[] when queried.
        hierarchy | hi: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        includeUpperBound | iub: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index | index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        indexValue | iv: (create, query) - Query-only flag that returns an int for the key's index.
        keyframeCount | kc: (create, query) - Returns an int for the number of keys found for the targets.
        lastSelected | lsl: (create, query) - When used in queries, this flag returns requested values for the last selected key.
        name | n: (create, query) - Returns the names of animCurves of specified nodes, attributes or keys.
        option | o: (create, edit) - Valid values are "move," "insert," "over," and "segmentOver." When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to make room for the segment.
        relative | r: (create) - Move amounts are relative to a key's current position.
        selected | sl: (create, query) - When used in queries, this flag returns requested values for any active keys.
        shape | s: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        tickDrawSpecial | tds: (create, edit) - Sets the special drawing state for this key when it is drawn as a tick in the timeline.
        time | t: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
        timeChange | tc: (create, edit, query) - How much (with -relative) or where (with -absolute) to move keys (on time-input animation curves) along the x (time) axis.  Returns float[] when queried.
        valueChange | vc: (create, edit, query) - How much (with -relative) or where (with -absolute) to move keys along the y (value) axis. Returns float[] when queried.
    """
    ...


def keyframeOutliner(*args, animCurve: str = ..., ac: str = ..., annotation: Optional[Union[str, bool]] = ..., ann: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., bgc: Optional[Union[Tuple[float, float, float], bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., display: Optional[Union[str, bool]] = ..., dsp: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dgc: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., dpc: Optional[Union[str, bool]] = ..., enable: bool = ..., en: bool = ..., enableBackground: bool = ..., ebg: bool = ..., enableKeyboardFocus: bool = ..., ekf: bool = ..., exists: bool = ..., ex: bool = ..., fullPathName: bool = ..., fpn: bool = ..., height: Optional[Union[int, bool]] = ..., h: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., hlc: Optional[Union[Tuple[float, float, float], bool]] = ..., isObscured: bool = ..., io: bool = ..., manage: bool = ..., m: bool = ..., noBackground: bool = ..., nbg: bool = ..., numberOfPopupMenus: bool = ..., npm: bool = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., pma: bool = ..., preventOverride: bool = ..., po: bool = ..., statusBarMessage: Optional[Union[str, bool]] = ..., sbm: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., visible: bool = ..., vis: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., vcc: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., w: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates/edits/queries a keyframe outliner control.

    Args:
        animCurve | ac: (edit) - Name of the animation curve for which to display keyframes.
        annotation | ann: (create, edit, query) - Annotate the control with an extra string value.
        backgroundColor | bgc: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        display | dsp: (edit, query) - narrow | wide What columns to display.  When "narrow", time and value will be displayed, when "wide" tangent information will be displayed as well
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
        isObscured | io: (query) - Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.
        manage | m: (create, edit, query) - Manage state of the control.  An unmanaged control is not visible, nor does it take up any screen real estate.  All controls are created managed by default.
        noBackground | nbg: (create, edit) - Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
        numberOfPopupMenus | npm: (query) - Return the number of popup menus attached to this control.
        parent | p: (create, query) - The parent layout for this control.
        popupMenuArray | pma: (query) - Return the names of all the popup menus attached to this control.
        preventOverride | po: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        statusBarMessage | sbm: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
        visible | vis: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand | vcc: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width | w: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def keyframeStats(*args, adjustableColumn: Optional[Union[int, bool]] = ..., adj: Optional[Union[int, bool]] = ..., adjustableColumn2: Optional[Union[int, bool]] = ..., ad2: Optional[Union[int, bool]] = ..., adjustableColumn3: Optional[Union[int, bool]] = ..., ad3: Optional[Union[int, bool]] = ..., adjustableColumn4: Optional[Union[int, bool]] = ..., ad4: Optional[Union[int, bool]] = ..., adjustableColumn5: Optional[Union[int, bool]] = ..., ad5: Optional[Union[int, bool]] = ..., adjustableColumn6: Optional[Union[int, bool]] = ..., ad6: Optional[Union[int, bool]] = ..., animEditor: Optional[Union[str, bool]] = ..., ae: Optional[Union[str, bool]] = ..., annotation: Optional[Union[str, bool]] = ..., ann: Optional[Union[str, bool]] = ..., autoUnitWidth: Optional[Union[int, bool]] = ..., auw: Optional[Union[int, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., bgc: Optional[Union[Tuple[float, float, float], bool]] = ..., classicMode: bool = ..., cm: bool = ..., columnAlign: Optional[Union[Tuple[int, str], bool]] = ..., cal: Optional[Union[Tuple[int, str], bool]] = ..., columnAlign2: Optional[Union[Tuple[str, str], bool]] = ..., cl2: Optional[Union[Tuple[str, str], bool]] = ..., columnAlign3: Optional[Union[Tuple[str, str, str], bool]] = ..., cl3: Optional[Union[Tuple[str, str, str], bool]] = ..., columnAlign4: Optional[Union[Tuple[str, str, str, str], bool]] = ..., cl4: Optional[Union[Tuple[str, str, str, str], bool]] = ..., columnAlign5: Optional[Union[Tuple[str, str, str, str, str], bool]] = ..., cl5: Optional[Union[Tuple[str, str, str, str, str], bool]] = ..., columnAlign6: Optional[Union[Tuple[str, str, str, str, str, str], bool]] = ..., cl6: Optional[Union[Tuple[str, str, str, str, str, str], bool]] = ..., columnAttach: Optional[Union[Tuple[int, str, int], bool]] = ..., cat: Optional[Union[Tuple[int, str, int], bool]] = ..., columnAttach2: Optional[Union[Tuple[str, str], bool]] = ..., ct2: Optional[Union[Tuple[str, str], bool]] = ..., columnAttach3: Optional[Union[Tuple[str, str, str], bool]] = ..., ct3: Optional[Union[Tuple[str, str, str], bool]] = ..., columnAttach4: Optional[Union[Tuple[str, str, str, str], bool]] = ..., ct4: Optional[Union[Tuple[str, str, str, str], bool]] = ..., columnAttach5: Optional[Union[Tuple[str, str, str, str, str], bool]] = ..., ct5: Optional[Union[Tuple[str, str, str, str, str], bool]] = ..., columnAttach6: Optional[Union[Tuple[str, str, str, str, str, str], bool]] = ..., ct6: Optional[Union[Tuple[str, str, str, str, str, str], bool]] = ..., columnOffset2: Optional[Union[Tuple[int, int], bool]] = ..., co2: Optional[Union[Tuple[int, int], bool]] = ..., columnOffset3: Optional[Union[Tuple[int, int, int], bool]] = ..., co3: Optional[Union[Tuple[int, int, int], bool]] = ..., columnOffset4: Optional[Union[Tuple[int, int, int, int], bool]] = ..., co4: Optional[Union[Tuple[int, int, int, int], bool]] = ..., columnOffset5: Optional[Union[Tuple[int, int, int, int, int], bool]] = ..., co5: Optional[Union[Tuple[int, int, int, int, int], bool]] = ..., columnOffset6: Optional[Union[Tuple[int, int, int, int, int, int], bool]] = ..., co6: Optional[Union[Tuple[int, int, int, int, int, int], bool]] = ..., columnWidth: Optional[Union[Tuple[int, int], bool]] = ..., cw: Optional[Union[Tuple[int, int], bool]] = ..., columnWidth1: Optional[Union[int, bool]] = ..., cw1: Optional[Union[int, bool]] = ..., columnWidth2: Optional[Union[Tuple[int, int], bool]] = ..., cw2: Optional[Union[Tuple[int, int], bool]] = ..., columnWidth3: Optional[Union[Tuple[int, int, int], bool]] = ..., cw3: Optional[Union[Tuple[int, int, int], bool]] = ..., columnWidth4: Optional[Union[Tuple[int, int, int, int], bool]] = ..., cw4: Optional[Union[Tuple[int, int, int, int], bool]] = ..., columnWidth5: Optional[Union[Tuple[int, int, int, int, int], bool]] = ..., cw5: Optional[Union[Tuple[int, int, int, int, int], bool]] = ..., columnWidth6: Optional[Union[Tuple[int, int, int, int, int, int], bool]] = ..., cw6: Optional[Union[Tuple[int, int, int, int, int, int], bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dgc: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., dpc: Optional[Union[str, bool]] = ..., enable: bool = ..., en: bool = ..., enableBackground: bool = ..., ebg: bool = ..., enableKeyboardFocus: bool = ..., ekf: bool = ..., exists: bool = ..., ex: bool = ..., fullPathName: bool = ..., fpn: bool = ..., height: Optional[Union[int, bool]] = ..., h: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., hlc: Optional[Union[Tuple[float, float, float], bool]] = ..., isObscured: bool = ..., io: bool = ..., manage: bool = ..., m: bool = ..., noBackground: bool = ..., nbg: bool = ..., numberOfPopupMenus: bool = ..., npm: bool = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., pma: bool = ..., precision: Optional[Union[int, bool]] = ..., pre: Optional[Union[int, bool]] = ..., preventOverride: bool = ..., po: bool = ..., rowAttach: Optional[Union[Tuple[int, str, int], bool]] = ..., rat: Optional[Union[Tuple[int, str, int], bool]] = ..., statusBarMessage: Optional[Union[str, bool]] = ..., sbm: Optional[Union[str, bool]] = ..., timeAnnotation: Optional[Union[str, bool]] = ..., tan: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., valueAnnotation: Optional[Union[str, bool]] = ..., van: Optional[Union[str, bool]] = ..., visible: bool = ..., vis: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., vcc: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., w: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        adjustableColumn | adj: (create, edit) - Specifies which column has an adjustable size that changes with the sizing of the layout.  The column value is a 1-based index. Passing 0 as argument turns off the previous adjustable column.
        adjustableColumn2 | ad2: (create, edit) - Specifies which column has an adjustable size that changes with the size of the parent layout. Ignored if there are not exactly two columns.
        adjustableColumn3 | ad3: (create, edit) - Specifies that the column has an adjustable size that changes with the size of the parent layout. Ignored if there are not exactly three columns.
        adjustableColumn4 | ad4: (create, edit) - Specifies which column has an adjustable size that changes with the size of the parent layout. Ignored if there are not exactly four columns.
        adjustableColumn5 | ad5: (create, edit) - Specifies which column has an adjustable size that changes with the size of the parent layout. Ignored if there are not exactly five columns.
        adjustableColumn6 | ad6: (create, edit) - Specifies which column has an adjustable size that changes with the size of the parent layout. Ignored if there are not exactly six columns.
        animEditor | ae: (edit, query) - The name of the animation editor which is associated with the control
        annotation | ann: (create, edit, query) - Annotate the control with an extra string value.
        autoUnitWidth | auw: (create, edit, query) - When this is non-zero the time fied widget will automatically scale based on the unit time settings (frame or timecode). The value of autoUnitWidth specifies the number of digits that should be able to be displayed as the frame number. So a value of 4 will make sure frame number 8723 can be displayed. When the value is zero the normal widget width will be used.
        backgroundColor | bgc: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
        classicMode | cm: (edit, query) - Edit display mode. True means stats only, otherwise show time value.
        columnAlign | cal: (create, edit, multiuse) - Arguments are : column number, alignment type. Possible alignments are: left | right | center. Specifies alignment type for the specified column.
        columnAlign2 | cl2: (create, edit) - Sets the text alignment of both columns.  Ignored if there are not exactly two columns. Valid values are "left", "right", and "center".
        columnAlign3 | cl3: (create, edit) - Sets the text alignment for all three columns.  Ignored if there are not exactly three columns. Valid values are "left", "right", and "center".
        columnAlign4 | cl4: (create, edit) - Sets the text alignment for all four columns.  Ignored if there are not exactly four columns. Valid values are "left", "right", and "center".
        columnAlign5 | cl5: (create, edit) - Sets the text alignment for all five columns.  Ignored if there are not exactly five columns. Valid values are "left", "right", and "center".
        columnAlign6 | cl6: (create, edit) - Sets the text alignment for all six columns.  Ignored if there are not exactly six columns. Valid values are "left", "right", and "center".
        columnAttach | cat: (create, edit, multiuse) - Arguments are : column number, attachment type, and offset. Possible attachments are: left | right | both. Specifies column attachment types and offets.
        columnAttach2 | ct2: (create, edit) - Sets the attachment type of both columns. Ignored if there are not exactly two columns. Valid values are "left", "right", and "both".
        columnAttach3 | ct3: (create, edit) - Sets the attachment type for all three columns. Ignored if there are not exactly three columns. Valid values are "left", "right", and "both".
        columnAttach4 | ct4: (create, edit) - Sets the attachment type for all four columns. Ignored if there are not exactly four columns. Valid values are "left", "right", and "both".
        columnAttach5 | ct5: (create, edit) - Sets the attachment type for all five columns. Ignored if there are not exactly five columns. Valid values are "left", "right", and "both".
        columnAttach6 | ct6: (create, edit) - Sets the attachment type for all six columns. Ignored if there are not exactly six columns. Valid values are "left", "right", and "both".
        columnOffset2 | co2: (create, edit) - This flag is used in conjunction with the -columnAttach2 flag.  If that flag is not used then this flag will be ignored.  It sets the offset for the two columns.  The offsets applied are based on the attachments specified with the -columnAttach2 flag.  Ignored if there are not exactly two columns.
        columnOffset3 | co3: (create, edit) - This flag is used in conjunction with the -columnAttach3 flag.  If that flag is not used then this flag will be ignored.  It sets the offset for the three columns.  The offsets applied are based on the attachments specified with the -columnAttach3 flag.  Ignored if there are not exactly three columns.
        columnOffset4 | co4: (create, edit) - This flag is used in conjunction with the -columnAttach4 flag.  If that flag is not used then this flag will be ignored.  It sets the offset for the four columns.  The offsets applied are based on the attachments specified with the -columnAttach4 flag.  Ignored if there are not exactly four columns.
        columnOffset5 | co5: (create, edit) - This flag is used in conjunction with the -columnAttach5 flag.  If that flag is not used then this flag will be ignored.  It sets the offset for the five columns.  The offsets applied are based on the attachments specified with the -columnAttach5 flag.  Ignored if there are not exactly five columns.
        columnOffset6 | co6: (create, edit) - This flag is used in conjunction with the -columnAttach6 flag.  If that flag is not used then this flag will be ignored.  It sets the offset for the six columns.  The offsets applied are based on the attachments specified with the -columnAttach6 flag.  Ignored if there are not exactly six columns.
        columnWidth | cw: (create, edit, multiuse) - Arguments are : column number, column width. Sets the width of the specified column where the first parameter specifies the column (1 based index) and the second parameter specifies the width.
        columnWidth1 | cw1: (create, edit) - Sets the width of the first column. Ignored if there is not exactly one column.
        columnWidth2 | cw2: (create, edit) - Sets the column widths of both columns. Ignored if there are not exactly two columns.
        columnWidth3 | cw3: (create, edit) - Sets the column widths for all 3 columns. Ignored if there are not exactly 3 columns.
        columnWidth4 | cw4: (create, edit) - Sets the column widths for all 4 columns. Ignored if there are not exactly 4 columns.
        columnWidth5 | cw5: (create, edit) - Sets the column widths for all 5 columns. Ignored if there are not exactly 5 columns.
        columnWidth6 | cw6: (create, edit) - Sets the column widths for all 6 columns. Ignored if there are not exactly 6 columns.
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
        isObscured | io: (query) - Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.
        manage | m: (create, edit, query) - Manage state of the control.  An unmanaged control is not visible, nor does it take up any screen real estate.  All controls are created managed by default.
        noBackground | nbg: (create, edit) - Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
        numberOfPopupMenus | npm: (query) - Return the number of popup menus attached to this control.
        parent | p: (create, query) - The parent layout for this control.
        popupMenuArray | pma: (query) - Return the names of all the popup menus attached to this control.
        precision | pre: (edit, query) - Controls the number of digits to the right of the decimal point that will be displayed for float-valued channels. Default is 3.  Queried, returns an int.
        preventOverride | po: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        rowAttach | rat: (create, edit, multiuse) - Arguments are : column, attachment type, offset. Possible attachments are: top | bottom | both. Specifies attachment types and offsets for the entire row.
        statusBarMessage | sbm: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        timeAnnotation | tan: (create, edit, query) - Annotate the time field with an extra string value.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
        valueAnnotation | van: (create, edit, query) - Annotate the value field with an extra string value.
        visible | vis: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand | vcc: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width | w: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def keyframeTangentControl(*args, annotation: Optional[Union[str, bool]] = ..., ann: Optional[Union[str, bool]] = ..., backgroundColor: Optional[Union[Tuple[float, float, float], bool]] = ..., bgc: Optional[Union[Tuple[float, float, float], bool]] = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., dragCallback: Optional[Union[str, bool]] = ..., dgc: Optional[Union[str, bool]] = ..., dropCallback: Optional[Union[str, bool]] = ..., dpc: Optional[Union[str, bool]] = ..., enable: bool = ..., en: bool = ..., enableBackground: bool = ..., ebg: bool = ..., enableKeyboardFocus: bool = ..., ekf: bool = ..., exists: bool = ..., ex: bool = ..., fullPathName: bool = ..., fpn: bool = ..., height: Optional[Union[int, bool]] = ..., h: Optional[Union[int, bool]] = ..., highlightColor: Optional[Union[Tuple[float, float, float], bool]] = ..., hlc: Optional[Union[Tuple[float, float, float], bool]] = ..., isObscured: bool = ..., io: bool = ..., manage: bool = ..., m: bool = ..., noBackground: bool = ..., nbg: bool = ..., numberOfPopupMenus: bool = ..., npm: bool = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., popupMenuArray: bool = ..., pma: bool = ..., precision: Optional[Union[int, bool]] = ..., pre: Optional[Union[int, bool]] = ..., preventOverride: bool = ..., po: bool = ..., statusBarMessage: Optional[Union[str, bool]] = ..., sbm: Optional[Union[str, bool]] = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., visible: bool = ..., vis: bool = ..., visibleChangeCommand: Optional[Union[str, bool]] = ..., vcc: Optional[Union[str, bool]] = ..., width: Optional[Union[int, bool]] = ..., w: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates, edits, queries a keyframe tangent control.
    The control displays fields for modifying the selected keyframe's tangent
    angle and weight.

    Args:
        annotation | ann: (create, edit, query) - Annotate the control with an extra string value.
        backgroundColor | bgc: (create, edit, query) - The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.
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
        isObscured | io: (query) - Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.
        manage | m: (create, edit, query) - Manage state of the control.  An unmanaged control is not visible, nor does it take up any screen real estate.  All controls are created managed by default.
        noBackground | nbg: (create, edit) - Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.
        numberOfPopupMenus | npm: (query) - Return the number of popup menus attached to this control.
        parent | p: (create, query) - The parent layout for this control.
        popupMenuArray | pma: (query) - Return the names of all the popup menus attached to this control.
        precision | pre: (edit, query) - Controls the number of digits to the right of the decimal point that will be displayed. Default is 3. Queried, returns an int.
        preventOverride | po: (create, edit, query) - If true, this flag prevents overriding the control's attribute via the control's right mouse button menu.
        statusBarMessage | sbm: (create, edit) - Extra string to display in the status bar when the mouse is over the control.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
        visible | vis: (create, edit, query) - The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its parent layout(s).
        visibleChangeCommand | vcc: (create, edit, query) - Command that gets executed when visible state of the control changes.
        width | w: (create, edit, query) - The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.
    """
    ...


def keyingGroup(*args, activator: Optional[Union[str, bool]] = ..., act: Optional[Union[str, bool]] = ..., addElement: str = ..., add: str = ..., afterFilters: bool = ..., af: bool = ..., anyMember: Optional[Union[str, bool]] = ..., am: Optional[Union[str, bool]] = ..., category: Optional[Union[str, bool]] = ..., cat: Optional[Union[str, bool]] = ..., clear: str = ..., cl: str = ..., color: Optional[Union[int, bool]] = ..., co: Optional[Union[int, bool]] = ..., copy: Optional[Union[str, bool]] = ..., cp: Optional[Union[str, bool]] = ..., edges: bool = ..., eg: bool = ..., editPoints: bool = ..., ep: bool = ..., empty: bool = ..., em: bool = ..., excludeDynamic: bool = ..., ed: bool = ..., excludeRotate: bool = ..., er: bool = ..., excludeScale: bool = ..., es: bool = ..., excludeTranslate: bool = ..., et: bool = ..., excludeVisibility: bool = ..., ev: bool = ..., facets: bool = ..., fc: bool = ..., flatten: str = ..., fl: str = ..., forceElement: str = ..., fe: str = ..., include: str = ..., intersection: Optional[Union[str, bool]] = ..., int: Optional[Union[str, bool]] = ..., isIntersecting: Optional[Union[str, bool]] = ..., ii: Optional[Union[str, bool]] = ..., isMember: Optional[Union[str, bool]] = ..., im: Optional[Union[str, bool]] = ..., layer: bool = ..., l: bool = ..., minimizeRotation: bool = ..., mr: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., noIntermediate: bool = ..., ni: bool = ..., noSurfaceShader: bool = ..., nss: bool = ..., noWarnings: bool = ..., nw: bool = ..., nodesOnly: bool = ..., no: bool = ..., remove: str = ..., rm: str = ..., removeActivator: str = ..., rac: str = ..., renderable: bool = ..., r: bool = ..., setActiveFilter: Optional[Union[str, bool]] = ..., fil: Optional[Union[str, bool]] = ..., size: bool = ..., s: bool = ..., split: Optional[Union[str, bool]] = ..., sp: Optional[Union[str, bool]] = ..., subtract: Optional[Union[str, bool]] = ..., sub: Optional[Union[str, bool]] = ..., text: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ..., union: Optional[Union[str, bool]] = ..., un: Optional[Union[str, bool]] = ..., vertices: bool = ..., v: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to manage the membership of a keying group.  Keying
    groups allow users to effectively manage related keyframe data, allowing
    keys on attributes in the keying group to be set and edited as a single
    entity.

    Args:
        activator | act: (edit, query) - Sets the selected node(s) as activators for the given keying group. In query mode, returns list of objects that activate the given keying group
        addElement | add: (edit) - Adds the list of items to the given set.  If some of the items cannot be added to the set because they are in another set which is in the same partition as the set to edit, the command will fail.
        afterFilters | af: (edit) - Default state is false. This flag is valid in edit mode only. This flag is for use on sets that are acted on by deformers such as sculpt, lattice, blendShape. The default edit mode is to edit the membership of the group acted on by the deformer. If you want to edit the group but not change the membership of the deformer, set the flag to true.
        anyMember | am: (create) - An operation which tests whether any of the given items are members of the given set.
        category | cat: (create, edit, query) - Sets the keying group's category. This is what the global, active keying group filter will use to match.
        clear | cl: (edit) - An operation which removes all items from the given set making the set empty.
        color | co: (create, edit, query) - Defines the hilite color of the set. Must be a value in range [-1, 7] (one of the user defined colors).  -1 marks the color has being undefined and therefore not having any affect. Only the vertices of a vertex set will be displayed in this color.
        copy | cp: (create) - Copies the members of the given set to a new set. This flag is for use in creation mode only.
        edges | eg: (create, query) - Indicates the new set can contain edges only. This flag is for use in creation or query mode only. The default value is false.
        editPoints | ep: (create, query) - Indicates the new set can contain editPoints only. This flag is for use in creation or query mode only. The default value is false.
        empty | em: (create) - Indicates that the set to be created should be empty. That is, it ignores any arguments identifying objects to be added to the set. This flag is only valid for operations that create a new set.
        excludeDynamic | ed: (create) - When creating the keying group, exclude dynamic attributes.
        excludeRotate | er: (create) - When creating the keying group, exclude rotate attributes from transform-type nodes.
        excludeScale | es: (create) - When creating the keying group, exclude scale attributes from transform-type nodes.
        excludeTranslate | et: (create) - When creating the keying group, exclude translate attributes from transform-type nodes. For example, if your keying group contains joints only, perhaps you only want to include rotations in the keying group.
        excludeVisibility | ev: (create) - When creating the keying group, exclude visibility attribute from transform-type nodes.
        facets | fc: (create, query) - Indicates the new set can contain facets only. This flag is for use in creation or query mode only. The default value is false.
        flatten | fl: (edit) - An operation that flattens the structure of the given set. That is, any sets contained by the given set will be replaced by its members so that the set no longer contains other sets but contains the other sets' members.
        forceElement | fe: (edit) - For use in edit mode only. Forces addition of the items to the set. If the items are in another set which is in the same partition as the given set, the items will be removed from the other set in order to keep the sets in the partition mutually exclusive with respect to membership.
        include | include: (edit) - Adds the list of items to the given set.  If some of the items cannot be added to the set, a warning will be issued. This is a less strict version of the -add/addElement operation.
        intersection | int: (create) - An operation that returns a list of items which are members of all the sets in the list.
        isIntersecting | ii: (create) - An operation which tests whether the sets in the list have common members.
        isMember | im: (create) - An operation which tests whether all the given items are members of the given set.
        layer | l: (create) - OBSOLETE. DO NOT USE.
        minimizeRotation | mr: (create, edit, query) - This flag only affects the attribute contained in the immediate keyingGroup. It does not affect attributes in sub-keyingGroups. Those will need to set minimizeRotation on their respective keyingGroups
        name | n: (create) - Assigns string as the name for a new set. This flag is only valid for operations that create a new set.
        noIntermediate | ni: (create, query) - Excludes intermediate objects when querying set members or using the subtract, union, itersection, or isIntersecting flags.
        noSurfaceShader | nss: (create) - If set is renderable, do not connect it to the default surface shader.  Flag has no meaning or effect for non renderable sets. This flag is for use in creation mode only. The default value is false.
        noWarnings | nw: (create) - Indicates that warning messages should not be reported such as when trying to add an invalid item to a set. (used by UI)
        nodesOnly | no: (query) - This flag is usable with the -q/query flag but is ignored if used with another queryable flags. This flag modifies the results of the set membership query such that when there are attributes (e.g. sphere1.tx) or components of nodes included in the set, only the nodes will be listed. Each node will only be listed once, even if more than one attribute or component of the node exists in the set.
        remove | rm: (edit) - Removes the list of items from the given set.
        removeActivator | rac: (edit) - Removes the selected node(s) as activators for the given keying group.
        renderable | r: (create, query) - This flag indicates that a special type of set should be created. This type of set (shadingEngine as opposed to objectSet) has certain restrictions on its membership in that it can only contain renderable elements such as lights and geometry. These sets are referred to as shading groups and are automatically connected to the "renderPartition" node when created (to ensure mutual exclusivity of the set's members with the other sets in the partition). This flag is for use in creation or query mode only. The default value is false which means a normal set is created.
        setActiveFilter | fil: (create, edit, query) - Sets the global, active keying group filter, which will affect activation of keying groups. Only keying groups with categories that match the filter will be activated. If the setActiveFilter is set to "NoKeyingGroups", keying groups will not be activated at all. If the setActiveFilter is set to "AllKeyingGroups", we will activate any keying group rather than just those with matching categories.
        size | s: (query) - Use the size flag to query the length of the set.
        split | sp: (create) - Produces a new set with the list of items and removes each item in the list of items from the given set.
        subtract | sub: (create) - An operation between two sets which returns the members of the first set that are not in the second set.
        text | t: (create, edit, query) - Defines an annotation string to be stored with the set.
        union | un: (create) - An operation that returns a list of all the members of all sets listed.
        vertices | v: (create, query) - Indicates the new set can contain vertices only. This flag is for use in creation or query mode only. The default value is false.
    """
    ...


def keyTangent(*args, absolute: bool = ..., a: bool = ..., animation: Optional[Union[str, bool]] = ..., an: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., controlPoints: bool = ..., cp: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., f: Optional[Union[Tuple[float, float], bool]] = ..., g: bool = ..., hierarchy: Optional[Union[str, bool]] = ..., hi: Optional[Union[str, bool]] = ..., inAngle: Optional[Union[float, bool]] = ..., ia: Optional[Union[float, bool]] = ..., inTangentType: Optional[Union[str, bool]] = ..., itt: Optional[Union[str, bool]] = ..., inWeight: Optional[Union[float, bool]] = ..., iw: Optional[Union[float, bool]] = ..., includeUpperBound: bool = ..., iub: bool = ..., index: Optional[Union[int, bool]] = ..., ix: Optional[Union[float, bool]] = ..., iy: Optional[Union[float, bool]] = ..., lock: bool = ..., l: bool = ..., outAngle: Optional[Union[float, bool]] = ..., oa: Optional[Union[float, bool]] = ..., outTangentType: Optional[Union[str, bool]] = ..., ott: Optional[Union[str, bool]] = ..., outWeight: Optional[Union[float, bool]] = ..., ow: Optional[Union[float, bool]] = ..., ox: Optional[Union[float, bool]] = ..., oy: Optional[Union[float, bool]] = ..., pluginTangentTypes: Optional[Union[str, bool]] = ..., ptt: Optional[Union[str, bool]] = ..., relative: bool = ..., r: bool = ..., shape: bool = ..., s: bool = ..., stepAttributes: bool = ..., sa: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., t: Optional[Union[Tuple[float, float], bool]] = ..., unify: bool = ..., uni: bool = ..., weightLock: bool = ..., wl: bool = ..., weightedTangents: bool = ..., wt: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        absolute | a: (create, edit) - Changes to tangent positions are NOT relative to the current position.
        animation | an: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute | at: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        controlPoints | cp: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        float | f: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        g | g: (create) - Required for all operations on the global tangent type. The global tangent type is used by the setKeyframe command when tangent types have not been specifically applied, except in combination with flags such as 'i/insert' which preserve the shape of the curve.  It is also used when keys are set from the menu. The only flags that can appear on a keyTangent command with the 'g/global' flag are 'itt/inTangentType', 'ott/outTangentType' and 'wt/weightedTangents'.
        hierarchy | hi: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        inAngle | ia: (create, edit, query) - New value for the angle of the in-tangent. Returns a float[] when queried.
        inTangentType | itt: (create, edit, query) - Specify the in-tangent type.  Valid values are "spline," "linear," "fast," "slow," "flat," "step," "stepnext," "fixed," "clamped," "plateau", "auto", "autoease", "automix", and "autocustom". Returns a string[] when queried.
        inWeight | iw: (create, edit, query) - New value for the weight of the in-tangent. Returns a float[] when queried.
        includeUpperBound | iub: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index | index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        ix | ix: (create, edit, query) - New value for the x-component of the in-tangent. This is a unit independent representation of the tangent component. Returns a float[] when queried.
        iy | iy: (create, edit, query) - New value for the y-component of the in-tangent. This is a unit independent representation of the tangent component. Returns a float[] when queried.
        lock | l: (create, edit, query) - Lock a tangent so in and out tangents move together. Returns an int[] when queried.
        outAngle | oa: (create, edit, query) - New value for the angle of the out-tangent. Returns a float[] when queried.
        outTangentType | ott: (create, edit, query) - Specify the out-tangent type.  Valid values are "spline," "linear," "fast," "slow," "flat," "step," "stepnext," "fixed," "clamped," "plateau" and "auto", "autoease", "automix", and "autocustom". Returns a string[] when queried.
        outWeight | ow: (create, edit, query) - New value for the weight of the out-tangent. Returns a float[] when queried.
        ox | ox: (create, edit, query) - New value for the x-component of the out-tangent. This is a unit independent representation of the tangent component. Returns a float[] when queried.
        oy | oy: (create, edit, query) - New value for the y-component of the out-tangent. This is a unit independent representation of the tangent component. Returns a float[] when queried.
        pluginTangentTypes | ptt: (query) - Returns a list of the plug-in tangent types that have been loaded. Return type is a string array.
        relative | r: (create, edit) - Changes to tangent positions are relative to the current position.
        shape | s: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        stepAttributes | sa: (create, edit) - The setKeyframe command will automatically set tangents for boolean and enumerated attributes to step.  This flag mirrors this behavior for the keyTangent command.  When set to false, tangents for these attributes will not be edited.  When set to true (the default) tangents for these attributes will be edited.
        time | t: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
        unify | uni: (create, edit) - Unify a tangent so in and out tangents are equal and move together.
        weightLock | wl: (create, edit, query) - Lock the weight of a tangent so it is fixed. Returns an int[] when queried. Note: weightLock is only obeyed within the graph editor.  It is not obeyed when -inWeight/-outWeight are issued from a command.
        weightedTangents | wt: (create, edit, query) - Specify whether or not the tangents on the animCurve are weighted Note: switching a curve from weightedTangents true to false and back to true again will not preserve fixed tangents properly. Use undo instead.
    """
    ...


def lattice(*args, after: bool = ..., af: bool = ..., afterReference: bool = ..., ar: bool = ..., before: bool = ..., bf: bool = ..., commonParent: bool = ..., cp: bool = ..., components: bool = ..., cmp: bool = ..., deformerTools: bool = ..., dt: bool = ..., divisions: Optional[Union[Tuple[int, int, int], bool]] = ..., dv: Optional[Union[Tuple[int, int, int], bool]] = ..., dualBase: bool = ..., db: bool = ..., exclusive: Optional[Union[str, bool]] = ..., ex: Optional[Union[str, bool]] = ..., freezeMapping: bool = ..., fm: bool = ..., frontOfChain: bool = ..., foc: bool = ..., geometry: Optional[Union[str, bool]] = ..., g: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., gi: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., ihs: bool = ..., latticeReset: bool = ..., lr: bool = ..., ldivisions: Optional[Union[Tuple[int, int, int], bool]] = ..., ldv: Optional[Union[Tuple[int, int, int], bool]] = ..., minimumSize: Optional[Union[float, bool]] = ..., mns: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., objectCentered: bool = ..., oc: bool = ..., outsideFalloffDistance: Optional[Union[float, bool]] = ..., ofd: Optional[Union[float, bool]] = ..., outsideLattice: Optional[Union[int, bool]] = ..., ol: Optional[Union[int, bool]] = ..., parallel: bool = ..., par: bool = ..., position: Optional[Union[Tuple[float, float, float], bool]] = ..., pos: Optional[Union[Tuple[float, float, float], bool]] = ..., prune: bool = ..., pr: bool = ..., remove: bool = ..., rm: bool = ..., removeTweaks: bool = ..., rt: bool = ..., rotation: Optional[Union[Tuple[float, float, float], bool]] = ..., ro: Optional[Union[Tuple[float, float, float], bool]] = ..., scale: Optional[Union[Tuple[float, float, float], bool]] = ..., s: Optional[Union[Tuple[float, float, float], bool]] = ..., selectedComponents: bool = ..., cms: bool = ..., split: bool = ..., sp: bool = ..., useComponentTags: bool = ..., uct: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a lattice deformer that will deform the selected
    objects. If the object centered flag is used, the initial lattice will
    fit around the selected objects. The lattice will be selected
    when the command is completed. The lattice deformer has an associated
    base lattice. Only objects which are contained by the base lattice
    will be deformed by the lattice.

    Args:
        after | af: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference | ar: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before | bf: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        commonParent | cp: (create) - Group the base lattice and the deformed lattice under a common transform. This means that you can resize the lattice without affecting the deformation by resizing the common transform.
        components | cmp: (query) - Returns the components used by the deformer
        deformerTools | dt: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        divisions | dv: (create, edit, query) - Set the number of lattice slices in x, y, z. Default is 2, 5, 2. When queried, this flag returns float float float. When you change the number of divisions, any tweaking or animation of lattice points must be redone.
        dualBase | db: (create) - Create a special purpose ffd deformer node which accepts 2 base lattices. The default is off which results in the creation of a normal ffd deformer node. Intended for internal usage only.
        exclusive | ex: (create, query) - Puts the deformation set in a deform partition.
        freezeMapping | fm: (create, edit, query) - The base position of the geometries points is fixed at the time this flag is set.  When mapping is frozen, moving the geometry with respect to the lattice will not cause the deformation to be recomputed.
        frontOfChain | foc: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry | g: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices | gi: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected | ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections | ihs: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        latticeReset | lr: (edit) - Reset the lattice to match its base position. This will undo any deformations that the lattice is causing. The lattice will only deform points that are enclosed within the lattice's reset (base) position.
        ldivisions | ldv: (create, edit, query) - Set the number of local lattice slices in x, y, z.
        minimumSize | mns: (create) - Set the minimum size of a side of the lattice during creation using the objectCentered flag which causes the lattice size to be determined from the geometry that is being deformed. When f.e. the object is a flat plane this can avoid the lattice to have size 0.0 along one side.
        name | n: (create) - Used to specify the name of the node being created.
        objectCentered | oc: (create) - Centers the lattice around the selected object(s) or components. Default is off which centers the lattice at the origin.
        outsideFalloffDistance | ofd: (create) - Set the falloff distance used when the setting for transforming points outside of the base lattice is set to 2. The distance value is a positive number which specifies the size of the falloff distance as a multiple of the base lattice size, thus a value of 1.0 specifies that only points up to the base lattice width/height/depth away are transformed. A value of 0.0 is equivalent to an outsideLattice value of 0 (i.e. no points outside the base lattice are transformed). A huge value is equivalent to transforming an outsideLattice value of 1 (i.e. all points are transformed).
        outsideLattice | ol: (create) - Set the mode describing how points outside the base lattice are transformed. 0 (the default) specifies that no outside points are transformed. 1 specifies that all outside points are transformed, and 2 specifies that only those outside points which fall within the "falloff distance" (see the -ofd/outsideFalloffDistance flag) are transformed. When querying, the current setting for the lattice is returned.
        parallel | par: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        position | pos: (create) - Used to specify the position of the newly created lattice.
        prune | pr: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        remove | rm: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        removeTweaks | rt: (edit) - Remove any lattice deformations caused by moving lattice points. Translations/rotations and scales on the lattice itself are not removed.
        rotation | ro: (create) - Used to specify the initial rotation of the newly created lattice.
        scale | s: (create) - Used to specify the initial scale of the newly created lattice.
        selectedComponents | cms: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        split | sp: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        useComponentTags | uct: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
    """
    ...


def listAnimatable(*args, active: bool = ..., act: bool = ..., manip: bool = ..., m: bool = ..., manipHandle: bool = ..., mh: bool = ..., shape: bool = ..., s: bool = ..., type: bool = ..., typ: bool = ...) -> Any:
    r"""
    This command list the animatable attributes of a node.  Command flags
    allow filtering by the current manipulator, or node type.

    Args:
        active | act: (create) - This flag is obsolete and no longer supported.
        manip | m: (create) - Return only those attributes affected by the current manip. If there is no manip active and any other flags are specified, output is the same as if the "-manip" flag were not present.
        manipHandle | mh: (create) - Return only those attributes affected by the current manip handle. If there is no manip handle active and any other flags are specified, output is the same as if the "-manipHandle" flag were not present.
        shape | s: (create) - This flag is obsolete and no longer supported.
        type | typ: (create) - Instead of returning attributes, Return the types of nodes that are currently animatable.
    """
    ...


def marker(*args, attach: bool = ..., a: bool = ..., detach: bool = ..., d: bool = ..., frontTwist: Optional[Union[float, bool]] = ..., ft: Optional[Union[float, bool]] = ..., orientationMarker: bool = ..., om: bool = ..., positionMarker: bool = ..., pm: bool = ..., sideTwist: Optional[Union[float, bool]] = ..., st: Optional[Union[float, bool]] = ..., time: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., t: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., upTwist: Optional[Union[float, bool]] = ..., ut: Optional[Union[float, bool]] = ..., valueU: Optional[Union[float, bool]] = ..., u: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        attach | a: (create) - This flag specifies to attach the selected 3D position markers to their parent geometry.
        detach | d: (create) - This flag specifies to detach the selected position markers from their parent geometry to the 3D space.
        frontTwist | ft: (query) - This flag specifies the amount of twist angle about the front vector for the marker. Default is 0. When queried, this flag returns a angle.
        orientationMarker | om: (query) - This flag specifies creation of an orientation marker. Default is not set.. When queried, this flag returns a boolean.
        positionMarker | pm: (query) - This flag specifies creation of a position marker. Default is set. When queried, this flag returns a boolean.
        sideTwist | st: (query) - This flag specifies  the amount of twist angle about the side vector for the marker. Default is 0. When queried, this flag returns a angle.
        time | t: (query) - This flag specifies the time for the marker. Default is the current time. When queried, this flag returns a time.
        upTwist | ut: (query) - This flag specifies the amount of twist angle about the up vector for the marker. Default is 0. When queried, this flag returns a angle.
        valueU | u: (query) - This flag specifies the location of the position marker w.r.t. the parent geometry u parameterization. Default is the value at current time. When queried, this flag returns a linear.
    """
    ...


def mimicManipulation(*args, manipulations: Optional[Union[str, bool]] = ..., m: Optional[Union[str, bool]] = ..., prevalidation: bool = ..., p: bool = ..., refresh: bool = ..., r: bool = ...) -> Any:
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
        manipulations | m: (create) - JSON string representing the manipulations to be performed.
        prevalidation | p: (create) - Flag to control if prevalidation of the manipulated plugs will be performed.  If it is and the plugs are already properly supported by the Evaluation Manager, Evaluation Manager manipulation will be used on the very first frame instead of requiring an initial frame with dirty propagation and DG evaluation to validate Evaluation Manager manipulation can be safely performed.
        refresh | r: (create) - Flag to control if a refresh is triggered after each manipulation. Note that refresh is necessary for evaluation to kick in.
    """
    ...


def mirrorJoint(*args, mirrorBehavior: bool = ..., mb: bool = ..., mirrorXY: bool = ..., mxy: bool = ..., mirrorXZ: bool = ..., mxz: bool = ..., mirrorYZ: bool = ..., myz: bool = ..., searchReplace: Optional[Union[Tuple[str, str], bool]] = ..., sr: Optional[Union[Tuple[str, str], bool]] = ...) -> Any:
    r"""
    This command will duplicate a branch of the skeleton from the selected
    joint symmetrically about a plane in world space.
    There are three mirroring modes(xy-, yz-, xz-plane).

    Args:
        mirrorBehavior | mb: (create) - The mirrorBehavior flag is used to specify that when performing the mirror, the joint orientation axes should be mirrored such that equal rotations on the original and mirrored joints will place the skeleton in a mirrored position (symmetric across the mirroring plane). Thus, animation curves from the original joints can be copied to the mirrored side to produce a similar (but symmetric) behavior. When mirrorBehavior is not specified, the joint orientation on the mirrored side will be identical to the source side.
        mirrorXY | mxy: (create) - mirror skeleton from the selected joint about xy-plane in world space.
        mirrorXZ | mxz: (create) - mirror skeleton from the selected joint about xz-plane in world space.
        mirrorYZ | myz: (create) - mirror skeleton from the selected joint about yz-plane in world space.
        searchReplace | sr: (create) - After performing the mirror, rename the new joints by searching the name for the first specified string and replacing it with the second specified string.
    """
    ...


def movieInfo(*args, counter: bool = ..., cn: bool = ..., dropFrame: bool = ..., df: bool = ..., frameCount: bool = ..., f: bool = ..., frameDuration: bool = ..., fd: bool = ..., height: bool = ..., h: bool = ..., movieTexture: bool = ..., mt: bool = ..., negTimesOK: bool = ..., nt: bool = ..., numFrames: bool = ..., nf: bool = ..., quickTime: bool = ..., qt: bool = ..., timeCode: bool = ..., tc: bool = ..., timeCodeTrack: bool = ..., tt: bool = ..., timeScale: bool = ..., ts: bool = ..., twentyFourHourMax: bool = ..., tf: bool = ..., width: bool = ..., w: bool = ...) -> Any:
    r"""
    movieInfo provides a mechanism for querying information about movie
    files.

    Args:
        counter | cn: (create) - Query the 'counter' flag of the movie's timecode format. If this is true, the timecode returned by the -timeCode flag will be a simple counter. If false, the returned timecode will be an array of integers (hours, minutes, seconds, frames).
        dropFrame | df: (create) - Query the 'drop frame' flag of the movie's timecode format.
        frameCount | f: (create) - Query the number of frames in the movie file
        frameDuration | fd: (create) - Query the frame duration of the movie's timecode format.
        height | h: (create) - Query the height of the movie
        movieTexture | mt: (create) - If set, the string argument is interpreted as the name of a movie texture node, and the command then operates on the movie loaded by that node.
        negTimesOK | nt: (create) - Query the 'neg times OK' flag of the movie's timecode format.
        numFrames | nf: (create) - Query the whole number of frames per second of the movie's timecode format.
        quickTime | qt: (create) - Query whether the movie is a QuickTime movie.
        timeCode | tc: (create) - Query the timecode of the current movie frame.
        timeCodeTrack | tt: (create) - Query whether the movie has a timecode track.
        timeScale | ts: (create) - Query the timescale of the movie's timecode format.
        twentyFourHourMax | tf: (create) - Query the '24 hour max' flag of the movie's timecode format.
        width | w: (create) - Query the width of the movie
    """
    ...


def movIn(*args, file: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., st: Optional[Union[Union[float, Tuple[float, float]], bool]] = ...) -> Any:
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
        file | f: (create) - The name of the .mov file. If no extension is used, a .mov will be added.
        startTime | st: (create) - The default start time for importing the .mov file is the current time. The startTime option sets the starting time for the .mov data in the current time unit.
    """
    ...


def movOut(*args, comment: bool = ..., c: bool = ..., file: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., precision: Optional[Union[int, bool]] = ..., pre: Optional[Union[int, bool]] = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., t: Optional[Union[Tuple[float, float], bool]] = ...) -> Any:
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
        comment | c: (create) - If true, the attributes written to the .mov file will be listed in a commented section at the top of the .mov file. The default is false.
        file | f: (create) - The name of the .mov file. If no extension is used, a .mov will be added.
        precision | pre: (create) - Sets the number of digits to the right of the decimal place in the .mov file. C: The default is 6.
        time | t: (create) - The time range to save as a .mov file. The default is the current time range.
    """
    ...


def mute(*args, disable: bool = ..., d: bool = ..., force: bool = ..., f: bool = ..., query: bool = ...) -> Any:
    r"""
    The mute command is used to disable and enable playback on a channel. When a channel is muted, it retains the value that it was at prior to being muted.

    Args:
        disable | d: (create) - Disable muting on the channels
        force | f: (create) - Forceable disable of muting on the channels. If there are keys on the mute channel, the animation and mute node will both be removed.  If this flag is not set, then mute nodes with animation will only be disabled.
    """
    ...


def nonLinear(*args, after: bool = ..., af: bool = ..., afterReference: bool = ..., ar: bool = ..., autoParent: bool = ..., ap: bool = ..., before: bool = ..., bf: bool = ..., commonParent: bool = ..., cp: bool = ..., components: bool = ..., cmp: bool = ..., defaultScale: bool = ..., ds: bool = ..., deformerTools: bool = ..., dt: bool = ..., exclusive: Optional[Union[str, bool]] = ..., ex: Optional[Union[str, bool]] = ..., frontOfChain: bool = ..., foc: bool = ..., geometry: Optional[Union[str, bool]] = ..., g: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., gi: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., ihs: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., parallel: bool = ..., par: bool = ..., prune: bool = ..., pr: bool = ..., remove: bool = ..., rm: bool = ..., selectedComponents: bool = ..., cms: bool = ..., split: bool = ..., sp: bool = ..., type: Optional[Union[str, bool]] = ..., typ: Optional[Union[str, bool]] = ..., useComponentTags: bool = ..., uct: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        after | af: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference | ar: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        autoParent | ap: (create) - Parents the deformer handle under the selected object's transform. This flag is valid only when a single object is selected.
        before | bf: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        commonParent | cp: (create) - Creates a new transform and parents the selected object and the deformer handle under it.  This flag is valid only when a single object is selected.
        components | cmp: (query) - Returns the components used by the deformer
        defaultScale | ds: (create) - Sets the scale of the deformation handle to 1.  By default the deformation handle is scaled to the match the largest dimension of the selected objects' bounding box. [deformerFlags] The attributes of the deformer handle shape can be set upon creation, edited and queried as normal flags using either the long or the short attribute name.  e.g.
        deformerTools | dt: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        exclusive | ex: (create, query) - Puts the deformation set in a deform partition.
        frontOfChain | foc: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry | g: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices | gi: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected | ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections | ihs: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        name | n: (create) - Used to specify the name of the node being created.
        parallel | par: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        prune | pr: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        remove | rm: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        selectedComponents | cms: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        split | sp: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        type | typ: (create) - Specifies the type of deformation. The current valid deformation types are:  bend, twist, squash, flare, sine and wave
        useComponentTags | uct: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
    """
    ...


def normalConstraint(*args, aimVector: Optional[Union[Tuple[float, float, float], bool]] = ..., aim: Optional[Union[Tuple[float, float, float], bool]] = ..., layer: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., remove: bool = ..., rm: bool = ..., targetList: bool = ..., tl: bool = ..., upVector: Optional[Union[Tuple[float, float, float], bool]] = ..., u: Optional[Union[Tuple[float, float, float], bool]] = ..., weight: Optional[Union[float, bool]] = ..., w: Optional[Union[float, bool]] = ..., weightAliasList: bool = ..., wal: bool = ..., worldUpObject: Optional[Union[str, bool]] = ..., wuo: Optional[Union[str, bool]] = ..., worldUpType: Optional[Union[str, bool]] = ..., wut: Optional[Union[str, bool]] = ..., worldUpVector: Optional[Union[Tuple[float, float, float], bool]] = ..., wu: Optional[Union[Tuple[float, float, float], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        aimVector | aim: (create, edit, query) - Set the aim vector.  This is the vector in local coordinates that points at the target.  If not given at creation time, the default value of (1.0, 0.0, 0.0) is used.
        layer | l: (create, edit) - Specify the name of the animation layer where the constraint should be added.
        name | n: (create, edit, query) - Sets the name of the constraint node to the specified name.  Default name is constrainedObjectName_constraintType
        remove | rm: (edit) - removes the listed target(s) from the constraint.
        targetList | tl: (query) - Return the list of target objects.
        upVector | u: (create, edit, query) - Set local up vector.  This is the vector in local coordinates that aligns with the world up vector.  If not given at creation time, the default value of (0.0, 1.0, 0.0) is used.
        weight | w: (create, edit, query) - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
        weightAliasList | wal: (query) - Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
        worldUpObject | wuo: (create, edit, query) - Set the DAG object use for worldUpType "object" and "objectrotation". See worldUpType for greater detail. The default value is no up object, which is interpreted as world space.
        worldUpType | wut: (create, edit, query) - Set the type of the world up vector computation. The worldUpType can have one of 5 values: "scene", "object", "objectrotation", "vector", or "none". If the value is "scene", the upVector is aligned with the up axis of the scene and worldUpVector and worldUpObject are ignored. If the value is "object", the upVector is aimed as closely as possible to the origin of the space of the worldUpObject and the worldUpVector is ignored. If the value is "objectrotation" then the worldUpVector is interpreted as being in the coordinate space of the worldUpObject, transformed into world space and the upVector is aligned as closely as possible to the result. If the value is "vector", the upVector is aligned with worldUpVector as closely as possible and worldUpMatrix is ignored. Finally, if the value is "none" no twist calculation is performed by the constraint, with the resulting "upVector" orientation based previous orientation of the constrained object, and the "great circle" rotation needed to align the aim vector with its constraint. The default worldUpType is "vector".
        worldUpVector | wu: (create, edit, query) - Set world up vector.  This is the vector in world coordinates that up vector should align with. See -wut/worldUpType (below)for greater detail. If not given at creation time, the default value of (0.0, 1.0, 0.0) is used.
    """
    ...


def orientConstraint(*args, createCache: Tuple[float, float] = ..., cc: Tuple[float, float] = ..., deleteCache: bool = ..., dc: bool = ..., layer: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., maintainOffset: bool = ..., mo: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., offset: Optional[Union[Tuple[float, float, float], bool]] = ..., o: Optional[Union[Tuple[float, float, float], bool]] = ..., remove: bool = ..., rm: bool = ..., skip: Optional[Union[str, bool]] = ..., sk: Optional[Union[str, bool]] = ..., targetList: bool = ..., tl: bool = ..., weight: Optional[Union[float, bool]] = ..., w: Optional[Union[float, bool]] = ..., weightAliasList: bool = ..., wal: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Constrain an object's orientation to match the orientation of the
    target or the average of a number of targets.
    
    An orientConstraint takes as input one or more "target" DAG transform
    nodes to control the orientation of the single "constraint object"
    DAG transform  The orientConstraint orients the constrained object
    to match the weighted average of the target world space orientations.

    Args:
        createCache | cc: (edit) - This flag is used to generate an animation curve that serves as a cache for the constraint. The two arguments define the start and end frames.  The cache is useful if the constraint has multiple targets and the constraint's interpolation type is set to "no flip". The "no flip" mode prevents flipping during playback, but the result is dependent on the previous frame.  Therefore in order to consistently get the same result on a specific frame, a cache must be generated. This flag creates the cache and sets the constraint's interpolation type to "cache". If a cache exists already, it will be deleted and replaced with a new cache.
        deleteCache | dc: (edit) - Delete an existing interpolation cache.
        layer | l: (create, edit) - Specify the name of the animation layer where the constraint should be added.
        maintainOffset | mo: (create) - The offset necessary to preserve the constrained object's initial orientation will be calculated and used as the offset.
        name | n: (create, edit, query) - Sets the name of the constraint node to the specified name.  Default name is constrainedObjectName_constraintType
        offset | o: (create, edit, query) - Sets or queries the value of the offset. Default is 0,0,0.
        remove | rm: (edit) - removes the listed target(s) from the constraint.
        skip | sk: (create, edit, multiuse) - Specify the axis to be skipped. Valid values are "x", "y", "z" and "none". The default value in create mode is "none". This flag is multi-use.
        targetList | tl: (query) - Return the list of target objects.
        weight | w: (create, edit, query) - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
        weightAliasList | wal: (query) - Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
    """
    ...


def pairBlend(*args, attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., input1: bool = ..., i1: bool = ..., input2: bool = ..., i2: bool = ..., node: Optional[Union[str, bool]] = ..., nd: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The pairBlend node allows a weighted combinations of 2 inputs to be blended together. It is created automatically when keying or constraining an attribute which is already connected.
    Alternatively, the pairBlend command can be used to connect a pairBlend node to connected attributes of a node. The previously existing connections are rewired to input1 of the pairBlend node. Additional connections can then be made manually to input2 of the pairBlend node.
    
    The pairBlend command can also be used to query the inputs to an existing pairBlend node.

    Args:
        attribute | at: (create, multiuse) - The name of the attribute(s) which the blend will drive. This flag is required when creating the blend.
        input1 | i1: (query) - Returns a string array of the node(s) connected to input 1.
        input2 | i2: (query) - Returns a string array of the node(s) connected to input 2.
        node | nd: (create) - The name of the node which the blend will drive. This flag is required when creating the blend.
    """
    ...


def parentConstraint(*args, createCache: Tuple[float, float] = ..., cc: Tuple[float, float] = ..., decompRotationToChild: bool = ..., dr: bool = ..., deleteCache: bool = ..., dc: bool = ..., layer: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., maintainOffset: bool = ..., mo: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., remove: bool = ..., rm: bool = ..., skipRotate: Optional[Union[str, bool]] = ..., sr: Optional[Union[str, bool]] = ..., skipTranslate: Optional[Union[str, bool]] = ..., st: Optional[Union[str, bool]] = ..., targetList: bool = ..., tl: bool = ..., weight: Optional[Union[float, bool]] = ..., w: Optional[Union[float, bool]] = ..., weightAliasList: bool = ..., wal: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        createCache | cc: (edit) - This flag is used to generate an animation curve that serves as a cache for the constraint. The two arguments define the start and end frames.  The cache is useful if the constraint has multiple targets and the constraint's interpolation type is set to "no flip". The "no flip" mode prevents flipping during playback, but the result is dependent on the previous frame. Therefore in order to consistently get the same result on a specific frame, a cache must be generated. This flag creates the cache and sets the constraint's interpolation type to "cache". If a cache exists already, it will be deleted and replaced with a new cache.
        decompRotationToChild | dr: (create) - During constraint creation, if the rotation offset between the constrained object and the target object is maintained, this flag indicates close to which object the offset rotation is decomposed. Setting this flag will make the rotation decomposition close to the constrained object instead of the target object, which is the default setting.
        deleteCache | dc: (edit) - Delete an existing interpolation cache.
        layer | l: (create, edit) - Specify the name of the animation layer where the constraint should be added.
        maintainOffset | mo: (create) - If this flag is specified the position and rotation of the constrained object will be maintained.
        name | n: (create, edit, query) - Sets the name of the constraint node to the specified name.  Default name is constrainedObjectName_constraintType
        remove | rm: (edit) - removes the listed target(s) from the constraint.
        skipRotate | sr: (create, multiuse) - Causes the axis specified not to be considered when constraining rotation.  Valid arguments are "x", "y", "z" and "none".
        skipTranslate | st: (create, multiuse) - Causes the axis specified not to be considered when constraining translation.  Valid arguments are "x", "y", "z" and "none".
        targetList | tl: (query) - Return the list of target objects.
        weight | w: (create, edit, query) - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
        weightAliasList | wal: (query) - Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
    """
    ...


def pasteKey(*args, animLayer: Optional[Union[str, bool]] = ..., al: Optional[Union[str, bool]] = ..., animation: Optional[Union[str, bool]] = ..., an: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., clipboard: Optional[Union[str, bool]] = ..., cb: Optional[Union[str, bool]] = ..., connect: bool = ..., c: bool = ..., copies: Optional[Union[int, bool]] = ..., cp: Optional[Union[int, bool]] = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., f: Optional[Union[Tuple[float, float], bool]] = ..., floatOffset: Optional[Union[float, bool]] = ..., fo: Optional[Union[float, bool]] = ..., includeUpperBound: bool = ..., iub: bool = ..., index: Optional[Union[int, bool]] = ..., matchByName: bool = ..., mn: bool = ..., option: Optional[Union[str, bool]] = ..., o: Optional[Union[str, bool]] = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., t: Optional[Union[Tuple[float, float], bool]] = ..., timeOffset: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., to: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., valueOffset: Optional[Union[float, bool]] = ..., vo: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        animLayer | al: (create) - Specifies that the keys getting pasted should be pasted onto curves on the specified animation layer.If that layer doesn't exist for the specified objects or attributes then the keys won't get pasted.
        animation | an: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute | at: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        clipboard | cb: (create) - Specifies the clipboard from which animation is pasted. Valid clipboards are "api" and "anim".  The default clipboard is: anim
        connect | c: (create) - When true, connect the source curve with the destination curve's value at the paste time. (This has the effect of shifting the clipboard curve in value to connect with the destination curve.) False preserves the source curve's original keyframe values. Default is false.
        copies | cp: (create) - The number of times to paste the source curve.
        float | f: (create) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        floatOffset | fo: (create) - How much to offset the pasted keys in time (for non-time-input animation curves).
        includeUpperBound | iub: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index | index: (create) - index of a key on an animCurve       In query mode, this flag needs a value.
        matchByName | mn: (create) - When true, we will only paste onto items in the scene whose node and attribute names match up exactly with a corresponding item in the clipboard. No hierarchy information is used. Default is false, and in this case the usual matching by hierarchy occurs.
        option | o: (create) - Valid values are "insert", "replace", "replaceCompletely", "merge", "scaleInsert," "scaleReplace", "scaleMerge", "fitInsert", "fitReplace", and "fitMerge". The default paste option is: "insert".
        time | t: (create) - time uniquely representing a key (or key range) on a time-based animCurve.  See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
        timeOffset | to: (create) - How much to offset the pasted keys in time (for time-input animation curves).
        valueOffset | vo: (create) - How much to offset the pasted keys in value.
    """
    ...


def pathAnimation(*args, bank: bool = ..., b: bool = ..., bankScale: Optional[Union[float, bool]] = ..., bs: Optional[Union[float, bool]] = ..., bankThreshold: Optional[Union[float, bool]] = ..., bt: Optional[Union[float, bool]] = ..., curve: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., endTimeU: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., etu: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., endU: Optional[Union[float, bool]] = ..., eu: Optional[Union[float, bool]] = ..., follow: bool = ..., f: bool = ..., followAxis: Optional[Union[str, bool]] = ..., fa: Optional[Union[str, bool]] = ..., fractionMode: bool = ..., fm: bool = ..., inverseFront: bool = ..., inverseUp: bool = ..., iu: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., startTimeU: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., stu: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., startU: Optional[Union[float, bool]] = ..., su: Optional[Union[float, bool]] = ..., upAxis: Optional[Union[str, bool]] = ..., ua: Optional[Union[str, bool]] = ..., useNormal: bool = ..., un: bool = ..., worldUpObject: Optional[Union[str, bool]] = ..., wuo: Optional[Union[str, bool]] = ..., worldUpType: Optional[Union[str, bool]] = ..., wut: Optional[Union[str, bool]] = ..., worldUpVector: Optional[Union[Tuple[float, float, float], bool]] = ..., wu: Optional[Union[Tuple[float, float, float], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        bank | b: (query) - If on, enable alignment of the up axis of the moving object(s) to the curvature of the path geometry. Default is false. When queried, this flag returns a boolean.
        bankScale | bs: (query) - This flag specifies a factor to scale the amount of bank angle. Default is 1.0 When queried, this flag returns a float.
        bankThreshold | bt: (query) - This flag specifies the limit of the bank angle. Default is 90 degrees When queried, this flag returns an angle.
        curve | c: (query) - This flag specifies the name of the curve for the path. Default is NONE When queried, this flag returns a string.
        endTimeU | etu: (multiuse, query) - This flag specifies the ending time of the animation for the u parameter. Default is NONE. When queried, this flag returns a time.
        endU | eu: (query) - This flag specifies the ending value of the u parameterization for the animation. Default is the end parameterization value of the curve. When queried, this flag returns a linear.
        follow | f: (query) - If on, enable alignment of the front axis of the moving object(s). Default is false. When queried, this flag returns a boolean.
        followAxis | fa: (query) - This flag specifies which object local axis to be aligned to the tangent of the path curve. Default is y When queried, this flag returns a string.
        fractionMode | fm: (query) - If on, evaluation on the path is based on the fraction of length of the path curve. Default is false. When queried, this flag returns a boolean.
        inverseFront | inverseFront: (query) - This flag specifies whether or not to align the front axis of the moving object(s) to the opposite direction of the tangent vector of the path geometry. Default is false. When queried, this flag returns a boolean.
        inverseUp | iu: (query) - This flag specifies whether or not to align the up axis of the moving object(s) to the opposite direction of the normal vector of the path geometry. Default is false. When queried, this flag returns a boolean.
        name | n: (query) - This flag specifies the name for the new motion path node. (instead of the default name) When queried, this flag returns a string.
        startTimeU | stu: (multiuse, query) - This flag specifies the starting time of the animation for the u parameter. Default is the the current time. When queried, this flag returns a time.
        startU | su: (query) - This flag specifies the starting value of the u parameterization for the animation. Default is the start parameterization value of the curve. When queried, this flag returns a linear.
        upAxis | ua: (query) - This flag specifies which object local axis to be aligned a computed up direction. Default is z When queried, this flag returns a string.
        useNormal | un: (create, edit, query) - This flag is now obsolete. Use -wut/worldUpType instead.
        worldUpObject | wuo: (create, edit, query) - Set the DAG object to use for worldUpType "object" and "objectrotation". See -wut/worldUpType for greater detail. The default value is no up object, which is interpreted as world space.
        worldUpType | wut: (create, edit, query) - Set the type of the world up vector computation. The worldUpType can have one of 5 values: "scene", "object", "objectrotation", "vector", or "normal". If the value is "scene", the upVector is aligned with the up axis of the scene and worldUpVector and worldUpObject are ignored. If the value is "object", the upVector is aimed as closely as possible to the origin of the space of the worldUpObject and the worldUpVector is ignored. If the value is "objectrotation" then the worldUpVector is interpreted as being in the coordinate space of the worldUpObject, transformed into world space and the upVector is aligned as closely as possible to the result. If the value is "vector", the upVector is aligned with worldUpVector as closely as possible and worldUpObject is ignored. Finally, if the value is "normal" the upVector is aligned to the path geometry. The default worldUpType is "vector".
        worldUpVector | wu: (create, edit, query) - Set world up vector.  This is the vector in world coordinates that up vector should align with. See -wut/worldUpType for greater detail. If not given at creation time, the default value of (0.0, 1.0, 0.0) is used.
    """
    ...


def percent(*args, addPercent: bool = ..., ap: bool = ..., dropoffAxis: Optional[Union[Tuple[float, float, float], bool]] = ..., dax: Optional[Union[Tuple[float, float, float], bool]] = ..., dropoffCurve: Optional[Union[str, bool]] = ..., dc: Optional[Union[str, bool]] = ..., dropoffDistance: Optional[Union[float, bool]] = ..., dds: Optional[Union[float, bool]] = ..., dropoffPosition: Optional[Union[Tuple[float, float, float], bool]] = ..., dp: Optional[Union[Tuple[float, float, float], bool]] = ..., dropoffType: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., multiplyPercent: bool = ..., mp: bool = ..., value: Optional[Union[float, bool]] = ..., v: Optional[Union[float, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command sets percent values on members of a weighted node such as
    a cluster or a jointCluster. With no flags specified the command sets
    the percent value for selected components of the specified node to the
    specified percent value. A dropoff from the specified percent value to
    0 can be specified from a point, plane or curve using a dropoff
    distance around that shape. The percent value can also be added or
    multiplied with existing percent values of the node components.

    Args:
        addPercent | ap: (create) - Add the percent value specified with the -v flag to the existing percent values
        dropoffAxis | dax: (create) - Specifies the axis along which to dropoff the percent value, starting from the dropoffPosition.
        dropoffCurve | dc: (create) - Specifies the curve around which to dropoff the percent value.
        dropoffDistance | dds: (create) - Specifies the dropoff distance from the point, plane or curve that was specified using the -dp -dax or -dc flags.
        dropoffPosition | dp: (create) - Specifies the point around which to dropoff the percent value.
        dropoffType | dt: (create) - Specifies the type of dropoff. Used in conjunction with the -dp, -dax or -dc flags. Default is linear. Valid values are: linear, sine, exponential, linearSquared, none.
        multiplyPercent | mp: (create) - Multiply the percent value specified with the -v flag with existing percent values
        value | v: (create, query) - The percent value to be applied. The default is 1. In query mode, returns an array of doubles corresponding to the weights of the selected object components.
    """
    ...


def play(*args, forward: bool = ..., f: bool = ..., playSound: bool = ..., ps: bool = ..., record: bool = ..., rec: bool = ..., sound: Optional[Union[str, bool]] = ..., s: Optional[Union[str, bool]] = ..., state: bool = ..., st: bool = ..., wait: bool = ..., w: bool = ..., query: bool = ...) -> Any:
    r"""
    This command starts and stops playback.
    In order to change the frame range of playback,
    see the playbackOptions command.

    Args:
        forward | f: (create, query) - When true, play back the animation from the currentTime to the maximum of the playback range. When false, play back from the currentTime to the minimum of the playback range.  When queried, returns an int.
        playSound | ps: (create, query) - Specify whether or not sound should be used during playback
        record | rec: (create, query) - enable the recording system and start one playback loop
        sound | s: (create, query) - Specify the sound node to be used during playback
        state | st: (create, query) - start or stop playing back
        wait | w: (create) - Wait till completion before returning control to command Window.
    """
    ...


def playbackOptions(*args, animationEndTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., aet: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., animationStartTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., ast: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., blockingAnim: bool = ..., ba: bool = ..., by: Optional[Union[float, bool]] = ..., framesPerSecond: bool = ..., fps: bool = ..., loop: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., maxPlaybackSpeed: Optional[Union[float, bool]] = ..., mps: Optional[Union[float, bool]] = ..., maxTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., max: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., minTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., min: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., playbackSpeed: Optional[Union[float, bool]] = ..., ps: Optional[Union[float, bool]] = ..., selectionEndTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., set: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., selectionStartTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., sst: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., selectionVisible: bool = ..., sv: bool = ..., stepLoop: bool = ..., slp: bool = ..., view: Optional[Union[str, bool]] = ..., v: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command sets/queries certain values associated
    with playback: looping style, start/end times, etc.
    Only commands modifying the -minTime/maxTime,
    the -animationStartTime/animationEndTime,
    the -selectionStartTime/selectionEndTime/selectionVisible
    or the -by value are undoable.

    Args:
        animationEndTime | aet: (create, edit, query) - Sets the end time of the animation.  Query returns a float.
        animationStartTime | ast: (create, edit, query) - Sets the start time of the animation.  Query returns a float.
        blockingAnim | ba: (create, query) - All tangents playback as stepped so that animation can be viewed in pure pose-to-pose form
        by | by: (create, edit, query) - Increment between times viewed during playback. (Default 1.0)
        framesPerSecond | fps: (create, query) - Queries the actual playback rate.  Query returns a float.
        loop | l: (create, edit, query) - Controls if and how playback repeats.  Valid values are "once," "continuous," and "oscillate."  Query returns string.
        maxPlaybackSpeed | mps: (create, edit, query) - Sets the desired maximum playback speed.  Query returns a float. The maxPlaybackSpeed is only used by Maya when your playbackSpeed is 0 (play every frame). The maxPlaybackSpeed will clamp the maximum playback rate to prevent it from going more than a certain amount. A maxPlaybackSpeed of 0 will give free (unclamped) playback.
        maxTime | max: (create, edit, query) - Sets the end of the playback time range.  Query returns a float.
        minTime | min: (create, edit, query) - Sets the start of the playback time range.  Query returns a float.
        playbackSpeed | ps: (create, edit, query) - Sets the desired playback speed.  Query returns a float.
        selectionEndTime | set: (create, edit, query) - Sets the end time of the selection.  Query returns a float.
        selectionStartTime | sst: (create, edit, query) - Sets the start time of the selection.  Query returns a float.
        selectionVisible | sv: (create, edit, query) - Sets the selection visibility. Query returns current visibility.
        stepLoop | slp: (create, query) - Turns on/off looping back to the start or end of the play range for step forward/backward one frame and step forward/backward one key.
        view | v: (create, edit, query) - Controls how many modelling views update during playback. Valid values are "all" and "active".  Query returns a string.
    """
    ...


def playblast(*args, activeEditor: bool = ..., ae: bool = ..., cameraSetup: Optional[Union[Tuple[str, str], bool]] = ..., cs: Optional[Union[Tuple[str, str], bool]] = ..., clearCache: bool = ..., cc: bool = ..., codecOptions: bool = ..., co: bool = ..., combineSound: bool = ..., csd: bool = ..., completeFilename: Optional[Union[str, bool]] = ..., cf: Optional[Union[str, bool]] = ..., compression: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., editorPanelName: Optional[Union[str, bool]] = ..., epn: Optional[Union[str, bool]] = ..., endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., et: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., filename: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., forceOverwrite: bool = ..., fo: bool = ..., format: Optional[Union[str, bool]] = ..., fmt: Optional[Union[str, bool]] = ..., frame: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., fr: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., framePadding: Optional[Union[int, bool]] = ..., fp: Optional[Union[int, bool]] = ..., height: Optional[Union[int, bool]] = ..., h: Optional[Union[int, bool]] = ..., indexFromZero: bool = ..., ifz: bool = ..., offScreen: bool = ..., os: bool = ..., offScreenViewportUpdate: bool = ..., osv: bool = ..., options: bool = ..., o: bool = ..., percent: Optional[Union[int, bool]] = ..., p: Optional[Union[int, bool]] = ..., quality: Optional[Union[int, bool]] = ..., qlt: Optional[Union[int, bool]] = ..., rawFrameNumbers: bool = ..., rfn: bool = ..., replaceAudioOnly: bool = ..., rao: bool = ..., replaceEndTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., ret: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., replaceFilename: Optional[Union[str, bool]] = ..., rf: Optional[Union[str, bool]] = ..., replaceStartTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., rst: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., sequenceTime: bool = ..., sqt: bool = ..., showOrnaments: bool = ..., orn: bool = ..., sound: Optional[Union[str, bool]] = ..., s: Optional[Union[str, bool]] = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., st: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., throwOnError: bool = ..., toe: bool = ..., useTraxSounds: bool = ..., uts: bool = ..., viewer: bool = ..., v: bool = ..., width: Optional[Union[int, bool]] = ..., w: Optional[Union[int, bool]] = ..., widthHeight: Optional[Union[Tuple[int, int], bool]] = ..., wh: Optional[Union[Tuple[int, int], bool]] = ...) -> Any:
    r"""
    This command playblasts the current playback range.
    Sound is optional.
    
    Note that the playblast command registers a condition called "playblasting"
    so that users can monitor whether playblasting is occurring. You may monitor the
    condition using the API (MConditionMessage) or a script (scriptJob and condition
    commands).

    Args:
        activeEditor | ae: (create) - This flag will return the current model editor that would be used for playblast. It does not invoke playblast itself.
        cameraSetup | cs: (create, multiuse) - Information about camera setup. The first string defines a camera setup MEL procedure. The camera setup procedure will be invoked before executing a playblast. The second string argument which is used as a camera identifier and is appended to the root file name to specify the final output file name(s). The command will fail there is not a pair of strings supplied to the argument.
        clearCache | cc: (create) - When true, all previous temporary playblast files will be deleted before the new playblast files are created and the remaining temporary playblast files will be deleted when the application quits. Any playblast files that were explicitly given a name by the user will not be deleted.
        codecOptions | co: (create) - Brings up the OS specific dialog for setting playblast codec options, and does not run the playblast.
        combineSound | csd: (create) - Combine the trax sounds into a single track. This might force a resampling of the sound if the sound paramters don't match up.
        completeFilename | cf: (create) - When set, this string specifies the exact name of the output image. In contrast with the -f/filename flag, -cf/completeFilename does not append any frame number or extension string at the end of the filename. Additionally, playblast will not delete the image from disk after it is displayed. This flag should not be used in conjunction with -f/filename.
        compression | c: (create) - Specify the compression to use for the movie file.  To determine which settings are available on your system, use the `playblast -options` command. This will display a system-specific dialog with supported compression formats. When the 'format' flag is 'image', this flag is used to pass in the desired image format. If the format is 'image' and the compression flag is ommitted, the output format specified via the Render Globals preference (see -format) will be used. If compression is set to 'none', the iff image format will be used.
        editorPanelName | epn: (create) - This optional flag specifies the name of the model editor or panel, which is to be used for playblast. The current model editor or panel won't be used for playblast unless its name is specified. Flag usage is specific to invoking playblast.
        endTime | et: (create) - Specify the end time of the playblast.  Default is the end time of the playback range displayed in the Time Slider. Overridden by -frame.
        filename | f: (create) - The filename to use for the output of this playblast. If the file already exists, a confirmation box will be displayed if playblast is performed interactively.  If playblast is executed from the command line and the file already exists, it will abort.
        forceOverwrite | fo: (create) - Overwrite existing playblast files which may have the the same name as the one specified with the "-f" flag
        format | fmt: (create) - The format for the playblast output.    ValueDescription   "movie" This option selects a platform-specific default movie format. On Linux and Mac OSX the default movie format is Quicktime. On Windows the default movie format is Audio Video Interleave.    "avi" Set the format to Audio Video Interleave (Windows only)   "qt" Set the format to QuickTime (all platforms).   "avfoundation" Write movie by AVFoundation (Mac only).   "image" Outputs a sequence of image files. The image format will be the Output Format specified using Window > RenderEditors > RenderSettings > CommonTab. The resulting files use the value of the "-f" flag as a prefix, with an appended frame number, as in "myFile.0007.iff"   "iff" Same as "image"    The default value of the -fmt/format flag is "movie". Depending on the selected format, a platform-specific default application will be used to view results. For image sequences, the default application is "fcheck". For movies, the default application is Windows Media Player (on Windows), Quicktime Player (on Mac OSX), and Lqtplay (on Linux). Users can specify different applications via Maya's application preferences.
        frame | fr: (create, multiuse) - List of frames to blast. One frame specified per flag. The frames can be specified in any order but will be output in an ordered sequence. When specified this flag will override any start/end range
        framePadding | fp: (create) - Number of zeros used to pad file name. Typically set to 4 to support fcheck.
        height | h: (create) - Height of the final image. This value will be clamped if larger than the width of the active window. Windows: If not using fcheck, the width and height must each be divisible by 4.
        indexFromZero | ifz: (create) - Output frames starting with file.0000.ext and incrementing by one. Typically frames use the Maya time as their frame number. This option can only be used for frame based output formats.
        offScreen | os: (create) - When set, this toggle allow playblast to use an offscreen buffer to render the view. This allows playblast to work when the application is iconified, or obscured.
        offScreenViewportUpdate | osv: (create) - When set, this toggle allows playblast to update the viewport while rendering with the offscreen buffer.
        options | o: (create) - Brings up a dialog for setting playblast options, and does not run the playblast.
        percent | p: (create) - Percentage of current view size  to use during blasting. Accepted values are integers between 10 and 100.  All other values are clamped to be within this range.  A value of 25 means 1/4 of the  current view size; a  value of 50  means half the current view size; a value of 100 means full size.  (Default is 50.)
        quality | qlt: (create) - Specify the compression quality factor to use for the movie file. Value should be in the 0-100 range
        rawFrameNumbers | rfn: (create) - Playblast typically numbers its frames sequentially, starting at zero. This flag will override the default action and frames will be numbered using the actual frames specified by the -frame or -startFrame/-endFrame flags.
        replaceAudioOnly | rao: (create) - When set, this string dictates that only the audio will be replaced when the scene is re-playblasted.
        replaceEndTime | ret: (create) - Specify the end time of a replayblast of an existing playblast.  Default is the start time of the playback range displayed in the Time Slider. Overridden by -frame.
        replaceFilename | rf: (create) - When set, this string specifies the name of an input playblast file which will have frames replaced according to the replace start and end times.
        replaceStartTime | rst: (create) - Specify the start time of a replayblast of an existing playblast.  Default is the start time of the playback range displayed in the Time Slider. Overridden by -frame.
        sequenceTime | sqt: (create) - Use sequence time
        showOrnaments | orn: (create) - Sets whether or not model view ornaments (e.g. the axis icon) should be displayed
        sound | s: (create) - Specify the sound node to be used during playblast
        startTime | st: (create) - Specify the start time of the playblast.  Default is the start time of the playback range displayed in the Time Slider. Overridden by -frame.
        throwOnError | toe: (create) - Playblast is tolerant of failures in most situations. When set, this toggle allows playblast to throw an error on these failures.
        useTraxSounds | uts: (create) - Use sounds from TRAX.
        viewer | v: (create) - Specify whether a viewer should be launched for the playblast.  Default is "true".  Runs "fcheck" when -fmt is "image". The player for movie files depends on the OS: Windows uses Microsoft Media Player, Irix uses movieplayer, OSX uses QuickTime.
        width | w: (create) - Width of the final image. This value will be clamped if larger than the width of the active window. Windows: If not using fcheck, the width and height must each be divisible by 4.
        widthHeight | wh: (create) - Final image's width and height. Values larger than the dimensions of the active window are clamped. A width and height of 0 means to use the window's current size. Windows: If not using fcheck, the width and height must each be divisible by 4.
    """
    ...


def pointConstraint(*args, layer: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., maintainOffset: bool = ..., mo: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., offset: Optional[Union[Tuple[float, float, float], bool]] = ..., o: Optional[Union[Tuple[float, float, float], bool]] = ..., remove: bool = ..., rm: bool = ..., skip: Optional[Union[str, bool]] = ..., sk: Optional[Union[str, bool]] = ..., targetList: bool = ..., tl: bool = ..., weight: Optional[Union[float, bool]] = ..., w: Optional[Union[float, bool]] = ..., weightAliasList: bool = ..., wal: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Constrain an object's position to the position of the target object or
    to the average position of a number of targets.
    
    A pointConstraint takes as input one or more "target" DAG transform
    nodes at which to position the single "constraint object" DAG
    transform node.  The pointConstraint positions the constrained object
    at the weighted average of the world space position target
    objects.

    Args:
        layer | l: (create, edit) - Specify the name of the animation layer where the constraint should be added.
        maintainOffset | mo: (create) - The offset necessary to preserve the constrained object's initial position will be calculated and used as the offset.
        name | n: (create, edit, query) - Sets the name of the constraint node to the specified name.  Default name is constrainedObjectName_constraintType
        offset | o: (create, edit, query) - Sets or queries the value of the offset. Default is 0,0,0.
        remove | rm: (edit) - removes the listed target(s) from the constraint.
        skip | sk: (create, edit, multiuse) - Specify the axis to be skipped. Valid values are "x", "y", "z" and "none". During creation, "none" is the default. This flag is multi-use.
        targetList | tl: (query) - Return the list of target objects.
        weight | w: (create, edit, query) - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
        weightAliasList | wal: (query) - Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
    """
    ...


def pointOnPolyConstraint(*args, layer: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., maintainOffset: bool = ..., mo: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., offset: Optional[Union[Tuple[float, float, float], bool]] = ..., o: Optional[Union[Tuple[float, float, float], bool]] = ..., remove: bool = ..., rm: bool = ..., skip: Optional[Union[str, bool]] = ..., sk: Optional[Union[str, bool]] = ..., targetList: bool = ..., tl: bool = ..., weight: Optional[Union[float, bool]] = ..., w: Optional[Union[float, bool]] = ..., weightAliasList: bool = ..., wal: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Constrain an object's position to the position of the target object or
    to the average position of a number of targets.
    
    A pointOnPolyConstraint takes as input one or more "target" DAG transform
    nodes at which to position the single "constraint object" DAG
    transform node.  The pointOnPolyConstraint positions the constrained object
    at the weighted average of the world space position target
    objects.

    Args:
        layer | l: (create, edit) - Specify the name of the animation layer where the constraint should be added.
        maintainOffset | mo: (create) - The offset necessary to preserve the constrained object's initial position will be calculated and used as the offset.
        name | n: (create, edit, query) - Sets the name of the constraint node to the specified name.  Default name is constrainedObjectName_constraintType
        offset | o: (create, edit, query) - Sets or queries the value of the offset. Default is 0,0,0.
        remove | rm: (edit) - removes the listed target(s) from the constraint.
        skip | sk: (create, edit, multiuse) - Specify the axis to be skipped. Valid values are "x", "y", "z" and "none". During creation, "none" is the default. This flag is multi-use.
        targetList | tl: (query) - Return the list of target objects.
        weight | w: (create, edit, query) - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
        weightAliasList | wal: (query) - Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
    """
    ...


def poleVectorConstraint(*args, layer: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., remove: bool = ..., rm: bool = ..., targetList: bool = ..., tl: bool = ..., weight: Optional[Union[float, bool]] = ..., w: Optional[Union[float, bool]] = ..., weightAliasList: bool = ..., wal: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Constrains the poleVector of an ikRPsolve handle to point at a
    target object or at the average position of a number of targets.
    
    An poleVectorConstraint takes as input one or more "target" DAG
    transform nodes at which to aim pole vector for an IK handle using
    the rotate plane solver.  The pole vector is adjust such that
    the in weighted average of the world space position target
    objects lies is the "rotate plane" of the handle.

    Args:
        layer | l: (create, edit) - Specify the name of the animation layer where the constraint should be added.
        name | n: (create, edit, query) - Sets the name of the constraint node to the specified name.  Default name is constrainedObjectName_constraintType
        remove | rm: (edit) - removes the listed target(s) from the constraint.
        targetList | tl: (query) - Return the list of target objects.
        weight | w: (create, edit, query) - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
        weightAliasList | wal: (query) - Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
    """
    ...


def polyUniteSkinned(*args, centerPivot: bool = ..., cp: bool = ..., constructionHistory: bool = ..., ch: bool = ..., mergeUVSets: Optional[Union[int, bool]] = ..., muv: Optional[Union[int, bool]] = ..., objectPivot: bool = ..., op: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command to combine poly mesh objects (as polyUnite)
    while retaining the smooth skinning setup on the
    combined object.

    Args:
        centerPivot | cp: (create, edit, query) - Set the resulting object's pivot to the center of the selected objects bounding box.
        constructionHistory | ch: (create, edit, query) - Turn the construction history on or off.
        mergeUVSets | muv: (create, edit, query) - Specify how UV sets will be merged on the output mesh. The choices are 0 | 1 | 2. 0 = Do not merge. Each UV set on each mesh will become a new UV set in the output. 1 = Merge by name. UV sets with the same name will be merged. 2 = Merge by UV links. UV sets will be merged so that UV linking on the input meshes continues to work. The default is 1 (merge by name).
        objectPivot | op: (create, edit, query) - Set the resulting object's pivot to last selected object's pivot.
    """
    ...


def pose(*args, allPoses: bool = ..., ap: bool = ..., apply: bool = ..., a: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to create character poses.

    Args:
        allPoses | ap: (query) - This flag is used to query all the poses in the scene.
        apply | a: (create) - This flag is used in conjunction with the name flag to specify a pose should be applied to the character.
        name | n: (create, query) - In create mode, specify the pose name. In query mode, return a list of all the poses for the character. In apply mode, specify the pose to be applied.
    """
    ...


def poseEditor(*args, control: bool = ..., ctl: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., exists: bool = ..., ex: bool = ..., filter: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., fmc: Optional[Union[str, bool]] = ..., highlightConnection: Optional[Union[str, bool]] = ..., hlc: Optional[Union[str, bool]] = ..., lockMainConnection: bool = ..., lck: bool = ..., mainListConnection: Optional[Union[str, bool]] = ..., mlc: Optional[Union[str, bool]] = ..., panel: Optional[Union[str, bool]] = ..., pnl: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., selectionConnection: Optional[Union[str, bool]] = ..., slc: Optional[Union[str, bool]] = ..., stateString: bool = ..., sts: bool = ..., unParent: bool = ..., up: bool = ..., unlockMainConnection: bool = ..., ulk: bool = ..., updateMainConnection: bool = ..., upd: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates an editor that derives from the base editor
    class that has controls for deformer and control nodes.

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
        unParent | up: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection | ulk: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection | upd: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
    """
    ...


def posePanel(*args, control: bool = ..., ctl: bool = ..., copy: str = ..., cp: str = ..., createString: bool = ..., cs: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., editString: bool = ..., es: bool = ..., exists: bool = ..., ex: bool = ..., init: bool = ..., isUnique: bool = ..., iu: bool = ..., label: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., menuBarRepeatLast: bool = ..., mrl: bool = ..., menuBarVisible: bool = ..., mbv: bool = ..., needsInit: bool = ..., ni: bool = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., popupMenuProcedure: Optional[Union[str, bool]] = ..., pmp: Optional[Union[str, bool]] = ..., poseEditor: bool = ..., pe: bool = ..., replacePanel: str = ..., rp: str = ..., tearOff: bool = ..., to: bool = ..., tearOffCopy: Optional[Union[str, bool]] = ..., toc: Optional[Union[str, bool]] = ..., tearOffRestore: bool = ..., tor: bool = ..., unParent: bool = ..., up: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a panel that derives from the base panel
    class that houses a poseEditor.

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
        poseEditor | pe: (query) - Query only flag that returns the name of an editor to be associated with the panel.
        replacePanel | rp: (edit) - Will replace the specified panel with this panel.  If the target panel is within the same layout it will perform a swap.
        tearOff | to: (edit, query) - Will tear off this panel into a separate window with a paneLayout as the parent of the panel. When queried this flag will return if the panel has been torn off into its own window.
        tearOffCopy | toc: (create) - Will create this panel as a torn of copy of the specified source panel.
        tearOffRestore | tor: (create, edit) - Restores panel if it is torn off and focus is given to it. If docked, becomes the active panel in the docked window. This should be the default flag that is added to all panels instead of -to/-tearOff flag which should only be used to tear off the panel.
        unParent | up: (edit) - Specifies that the panel should be removed from its layout. This (obviously) cannot be used with query.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
    """
    ...


def proximityWrap(*args, addDrivers: str = ..., ad: str = ..., applyUserDefaults: bool = ..., aud: bool = ..., canBeAdded: Optional[Union[str, bool]] = ..., cba: Optional[Union[str, bool]] = ..., driverIndices: bool = ..., di: bool = ..., dumpInfo: bool = ..., dui: bool = ..., freeDriverIndex: bool = ..., fdi: bool = ..., removeDrivers: str = ..., rd: str = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a proximityWrap deformer, which deforms geometry based on the
    distance from its drivers.

    Args:
        addDrivers | ad: (edit, multiuse) - Add connect new drivers to the proximityWrap node
        applyUserDefaults | aud: (edit) - Flag used in with the addDriver flag. When set, new drivers will set the user default attributes from the option var settings. When the flag is not set, the user default attributes will not be set. Default is on.
        canBeAdded | cba: (multiuse, query) - Returns true if all listed shapes can be added as drivers. The reason for an item returning false would be that it is already connected as a driver, it is connected as the deformed geometry or it represents in invalid object.
        driverIndices | di: (query) - List connected driver indices
        dumpInfo | dui: (query) - Return a python dictionary containing information relating to the proximityWrap node. Some information is returned in string form in mel but the flag is meant to be used in python.
        freeDriverIndex | fdi: (query) - Returns the first index which has no driver connected
        removeDrivers | rd: (edit, multiuse) - Remove connected drivers
    """
    ...


def readTake(*args, angle: Optional[Union[str, bool]] = ..., a: Optional[Union[str, bool]] = ..., device: Optional[Union[str, bool]] = ..., d: Optional[Union[str, bool]] = ..., frequency: Optional[Union[float, bool]] = ..., f: Optional[Union[float, bool]] = ..., linear: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., noTime: bool = ..., nt: bool = ..., take: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This action reads a take (.mov) file to a defined device. 
    
    See also: writeTake, applyTake

    Args:
        angle | a: (create) - Sets the angular unit used in the take. Valid strings are "deg", "degree", "rad", and "radian".  C: The default is the current user angular unit.
        device | d: (create) - Specifies the device into which the take data is read. This is a required argument.
        frequency | f: (create) - The timestamp is ignored and the specified frequency is used. If timeStamp data is not in the .mov file, the -noTimestamp flag should also be used. This flag resample, instead the data is assumed to be at the specified frequency.  C: If the take file does not use time stamps, the default frequency is 60Hz.
        linear | l: (create) - Sets the linear unit used in the take. Valid strings are "mm", "millimeter", "cm", "centimeter", "m", "meter", "km", "kilometer", "in", "inch", "ft", "foot", "yd", "yard", "mi", and "mile".  C: The default is the current user linear unit.
        noTime | nt: (create) - Specifies if the take (.mov) file contains time stamps.  C: The default is to assume time stamps are part of the take file.
        take | t: (create) - Reads the specified take file. It is safest to pass the full path to the flag.
    """
    ...


def recordDevice(*args, cleanup: bool = ..., c: bool = ..., data: bool = ..., da: bool = ..., device: Optional[Union[str, bool]] = ..., d: Optional[Union[str, bool]] = ..., duration: Optional[Union[int, bool]] = ..., dr: Optional[Union[int, bool]] = ..., playback: bool = ..., p: bool = ..., state: bool = ..., st: bool = ..., wait: bool = ..., w: bool = ..., query: bool = ...) -> Any:
    r"""
    Starts and stops server side device recording. The data is recorded
    at the device rate. Once recorded, the data may be brought into Maya
    with the applyTake command. 
    
    See also: enableDevice, applyTake, readTake, writeTake

    Args:
        cleanup | c: (create) - Removes the recorded data from the device.
        data | da: (query) - Specifies if the device has recorded data. If the device is recording at the time of query, the flag will return false.  Q: When queried, this flag returns an int.
        device | d: (create, multiuse) - Specifies which device(s) to start record recording. The listed device(s) will start recording regardless of their record enable state.  C: The default is to start recording all devices that are record enabled.
        duration | dr: (create, query) - Duration (in seconds) of the recording. When the duration expires, the device will still be in a recording state and must be told to stop recording.  C: The default is 60.  Q: When queried, this flag returns an int.
        playback | p: (create, query) - If any attribute is connected to an animation curve, the animation curve will play back while recording the device(s) including any animation curves attached to attributes being recorded.  C: The default is false.  Q: When queried, this flag returns an int.
        state | st: (create, query) - Start or stop device recording.  C: The default is true.  Q: When queried, this flag returns an int.
        wait | w: (create) - If -p/playback specified, wait until playback completion before returning control to the user. This flag is ignored if -p is not used.
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


def reorderDeformers(*args, name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This command changes the order in which 2 deformation nodes affect the
    output geometry. The first string argument is the name of deformer1,
    the second is deformer2, followed by the list of objects they
    deform.
    
    It inserts deformer2 before deformer1. Currently supported deformer
    nodes include: sculpt, cluster, jointCluster, lattice, wire,
    jointLattice, boneLattice, blendShape.

    Args:
        name | n: (create) - This flag is obsolete and is not used.
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


def rotationInterpolation(*args, convert: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    The rotationInterpolation command converts the rotation curves to the
            desired rotation interpolation representation. For example, an
            Euler-angled representation can be converted to Quaternion.

    Args:
        convert | c: (create, query) - Specifies the rotation interpolation mode for the curves after converting. Possible choices are "none" (unsynchronized Euler-angled curves which are compatible with pre-4.0 Maya curves), "euler" (Euler-angled curves with keyframes kept synchronized), "quaternion" (quaternion curves with keyframes kept synchronized, but the exact interpolation depends on individual tangents),  "quaternionSlerp" (applies quaternion slerp interpolation to the curve, ignoring tangent settings), "quaternionSquad" (applied cubic interpolation to the curve in quaternion space, ignoring tangent settings)
    """
    ...


def scaleConstraint(*args, layer: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., maintainOffset: bool = ..., mo: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., offset: Optional[Union[Tuple[float, float, float], bool]] = ..., o: Optional[Union[Tuple[float, float, float], bool]] = ..., remove: bool = ..., rm: bool = ..., scaleCompensate: bool = ..., sc: bool = ..., skip: Optional[Union[str, bool]] = ..., sk: Optional[Union[str, bool]] = ..., targetList: bool = ..., tl: bool = ..., weight: Optional[Union[float, bool]] = ..., w: Optional[Union[float, bool]] = ..., weightAliasList: bool = ..., wal: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Constrain an object's scale to the scale of the target object or
    to the average scale of a number of targets.
    
    A scaleConstraint takes as input one or more "target" DAG
    transform nodes to which to scale the single "constraint
    object" DAG transform node.  The scaleConstraint scales the
    constrained object at the weighted geometric mean of the
    world space target scale factors.

    Args:
        layer | l: (create, edit) - Specify the name of the animation layer where the constraint should be added.
        maintainOffset | mo: (create) - The offset necessary to preserve the constrained object's initial scale will be calculated and used as the offset.
        name | n: (create, edit, query) - Sets the name of the constraint node to the specified name.  Default name is constrainedObjectName_constraintType
        offset | o: (create, edit, query) - Sets or queries the value of the offset. Default is 1,1,1.
        remove | rm: (edit) - removes the listed target(s) from the constraint.
        scaleCompensate | sc: (create, edit) - Used only when constraining a joint. It specify if a scaleCompensate will be applied on constrained joint. If true it will connect Tjoint.aCompensateForParentScale to scaleContraint.aConstraintScaleCompensate.
        skip | sk: (create, edit, multiuse) - Specify the axis to be skipped. Valid values are "x", "y", "z" and "none". During creation, "none" is the default. This flag is multi-use.
        targetList | tl: (query) - Return the list of target objects.
        weight | w: (create, edit, query) - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
        weightAliasList | wal: (query) - Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
    """
    ...


def scaleKey(*args, animation: Optional[Union[str, bool]] = ..., an: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., autoSnap: bool = ..., asp: bool = ..., controlPoints: bool = ..., cp: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., f: Optional[Union[Tuple[float, float], bool]] = ..., floatPivot: Optional[Union[float, bool]] = ..., fp: Optional[Union[float, bool]] = ..., floatScale: Optional[Union[float, bool]] = ..., fs: Optional[Union[float, bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., hi: Optional[Union[str, bool]] = ..., includeUpperBound: bool = ..., iub: bool = ..., index: Optional[Union[int, bool]] = ..., newEndFloat: Optional[Union[float, bool]] = ..., nef: Optional[Union[float, bool]] = ..., newEndTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., net: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., newStartFloat: Optional[Union[float, bool]] = ..., nsf: Optional[Union[float, bool]] = ..., newStartTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., nst: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., scaleSpecifiedKeys: bool = ..., ssk: bool = ..., shape: bool = ..., s: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., t: Optional[Union[Tuple[float, float], bool]] = ..., timePivot: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., tp: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., timeScale: Optional[Union[float, bool]] = ..., ts: Optional[Union[float, bool]] = ..., valuePivot: Optional[Union[float, bool]] = ..., vp: Optional[Union[float, bool]] = ..., valueScale: Optional[Union[float, bool]] = ..., vs: Optional[Union[float, bool]] = ...) -> Any:
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
        animation | an: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute | at: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        autoSnap | asp: (create) - Auto snap scaled keys if True. Default value depend on scaleKeyAutoSnap option
        controlPoints | cp: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        float | f: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        floatPivot | fp: (create) - Scale pivot along the x-axis for float-based (unitless) animCurves
        floatScale | fs: (create) - Amount to scale along the x-axis for float-based (unitless) animation curves animCurves
        hierarchy | hi: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        includeUpperBound | iub: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index | index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        newEndFloat | nef: (create) - The end of the float range to which the float-based (unitless) animation curves should be scaled.
        newEndTime | net: (create) - The end of the time range to which the time-based animation curves should be scaled.
        newStartFloat | nsf: (create) - The start of the float range to which the float-based (unitless) animation curves should be scaled.
        newStartTime | nst: (create) - The start of the time range to which the time-based animation curves should be scaled.
        scaleSpecifiedKeys | ssk: (create) - Determines if only the specified keys are affected by the scale. If false, other keys may be adjusted with the scale. The default is true.
        shape | s: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        time | t: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
        timePivot | tp: (create) - Scale pivot along the time-axis for time-based animation curves
        timeScale | ts: (create) - Amount to scale along the time-axis for time-based animation curves
        valuePivot | vp: (create) - Scale pivot along the value-axis
        valueScale | vs: (create) - Amount of scale along the value-axis
    """
    ...


def sculpt(*args, after: bool = ..., af: bool = ..., afterReference: bool = ..., ar: bool = ..., before: bool = ..., bf: bool = ..., components: bool = ..., cmp: bool = ..., deformerTools: bool = ..., dt: bool = ..., dropoffDistance: Optional[Union[float, bool]] = ..., dds: Optional[Union[float, bool]] = ..., dropoffType: Optional[Union[str, bool]] = ..., drt: Optional[Union[str, bool]] = ..., exclusive: Optional[Union[str, bool]] = ..., ex: Optional[Union[str, bool]] = ..., frontOfChain: bool = ..., foc: bool = ..., geometry: Optional[Union[str, bool]] = ..., g: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., gi: bool = ..., groupWithLocator: bool = ..., gwl: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., ihs: bool = ..., insideMode: Optional[Union[str, bool]] = ..., im: Optional[Union[str, bool]] = ..., maxDisplacement: Optional[Union[float, bool]] = ..., mxd: Optional[Union[float, bool]] = ..., mode: Optional[Union[str, bool]] = ..., m: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., objectCentered: bool = ..., oc: bool = ..., parallel: bool = ..., par: bool = ..., prune: bool = ..., pr: bool = ..., remove: bool = ..., rm: bool = ..., sculptTool: Optional[Union[str, bool]] = ..., st: Optional[Union[str, bool]] = ..., selectedComponents: bool = ..., cms: bool = ..., split: bool = ..., sp: bool = ..., useComponentTags: bool = ..., uct: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates/edits/queries a sculpt object deformer. By default
    for creation mode an implicit sphere will be used as the sculpting
    object if no sculpt tool is specified. The name of the created/edited
    object is returned.

    Args:
        after | af: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference | ar: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before | bf: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        components | cmp: (query) - Returns the components used by the deformer
        deformerTools | dt: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        dropoffDistance | dds: (create, edit, query) - Specifies the distance from the surface of the sculpt object at which the sculpt object produces no deformation effect. Default is 1.0. When queried, this flag returns a float.
        dropoffType | drt: (create, edit, query) - Specifies how the deformation effect drops off from maximum effect at the surface of the sculpt object to no effect at dropoff distance limit. Valid values are: linear | none. Default is linear. When queried, this flag returns a string.
        exclusive | ex: (create, query) - Puts the deformation set in a deform partition.
        frontOfChain | foc: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry | g: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices | gi: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        groupWithLocator | gwl: (create) - Groups the sculptor and its locator together under a single transform. Default is off.
        ignoreSelected | ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections | ihs: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        insideMode | im: (create, edit, query) - Specifies how the deformation algorithm deals with points that are inside the sculpting primitve. The choices are: ring | even. The default is even. When queried, this flag returns a string. Ring mode will tend to produce a contour like ring of points around the sculpt object as it passes through an object while even mode will try to spread the points out as evenly as possible across the surface of the sculpt object.
        maxDisplacement | mxd: (create, edit, query) - Defines the maximum amount the sculpt object may move a point on an object which it is deforming. Default is 1.0. When queried, this flag returns a float.
        mode | m: (create, edit, query) - Specifies which deformation algorithm the sculpt object should use. The choices are: flip | project | stretch. The default is stretch. When queried, this flag returns a string.
        name | n: (create) - Used to specify the name of the node being created.
        objectCentered | oc: (create) - Places the sculpt and locator in the center of the bounding box of the selected object(s) or components. Default is off which centers the sculptor and locator at the origin.
        parallel | par: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        prune | pr: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        remove | rm: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        sculptTool | st: (create) - Use the specified NURBS object as the sculpt tool instead of the default implicit sphere.
        selectedComponents | cms: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        split | sp: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        useComponentTags | uct: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
    """
    ...


def sculptTarget(*args, after: bool = ..., af: bool = ..., afterReference: bool = ..., ar: bool = ..., before: bool = ..., bf: bool = ..., components: bool = ..., cmp: bool = ..., deformerTools: bool = ..., dt: bool = ..., exclusive: Optional[Union[str, bool]] = ..., ex: Optional[Union[str, bool]] = ..., frontOfChain: bool = ..., foc: bool = ..., geometry: str = ..., g: str = ..., geometryIndices: bool = ..., gi: bool = ..., ignoreSelected: bool = ..., inbetweenWeight: float = ..., ibw: float = ..., includeHiddenSelections: bool = ..., ihs: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., parallel: bool = ..., par: bool = ..., prune: bool = ..., pr: bool = ..., regenerate: bool = ..., r: bool = ..., remove: bool = ..., rm: bool = ..., selectedComponents: bool = ..., cms: bool = ..., snapshot: int = ..., s: int = ..., split: bool = ..., sp: bool = ..., target: int = ..., t: int = ..., useComponentTags: bool = ..., uct: bool = ..., edit: bool = ...) -> Any:
    r"""
    This command is used to specify the blend shape target to be
    modified by the sculpting tools and transform manipulators.

    Args:
        after | af: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference | ar: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before | bf: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        components | cmp: () - Returns the components used by the deformer
        deformerTools | dt: () - Returns the name of the deformer tool objects (if any) as string string ...
        exclusive | ex: (create) - Puts the deformation set in a deform partition.
        frontOfChain | foc: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry | g: (edit, multiuse) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices | gi: () - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected | ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        inbetweenWeight | ibw: (edit) - Specifies the in between target weight of the blend shape node that will be made editable by the sculpting and transform tools.
        includeHiddenSelections | ihs: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        name | n: (create) - Used to specify the name of the node being created.
        parallel | par: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        prune | pr: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        regenerate | r: (edit) - When this flag is specified a new shape is created for the specified blend shape target, if the shape does not already exist. The name of the new shape is returned.
        remove | rm: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        selectedComponents | cms: () - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        snapshot | s: (edit) - This flag should only be used internally to add in-between target. When this flag is specified a snapshot of the shape will be taken for the specified in-between target when it does not exist yet. This flag specifies the base shape index and must be used with the -target and -inbetweenWeight flags, which specify the in-between target.
        split | sp: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        target | t: (edit) - Specifies the target index of the blend shape node that will be made editable by the sculpting and transform tools.
        useComponentTags | uct: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
    """
    ...


def sequenceManager(*args, addSequencerAudio: Optional[Union[str, bool]] = ..., asa: Optional[Union[str, bool]] = ..., attachSequencerAudio: Optional[Union[str, bool]] = ..., ata: Optional[Union[str, bool]] = ..., currentShot: Optional[Union[str, bool]] = ..., cs: Optional[Union[str, bool]] = ..., currentTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., ct: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., listSequencerAudio: Optional[Union[str, bool]] = ..., lsa: Optional[Union[str, bool]] = ..., listShots: bool = ..., lsh: bool = ..., modelPanel: Optional[Union[str, bool]] = ..., mp: Optional[Union[str, bool]] = ..., node: Optional[Union[str, bool]] = ..., nd: Optional[Union[str, bool]] = ..., writableSequencer: Optional[Union[str, bool]] = ..., ws: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The sequenceManager command manages sequences, shots, and their related scenes.

    Args:
        addSequencerAudio | asa: (create) - Add an audio clip to the sequencer by specifying a filename
        attachSequencerAudio | ata: (create) - Add an audio clip to the sequencer by specifying an audio node
        currentShot | cs: (query) - Returns the shot that is being used at the current sequence time.
        currentTime | ct: (create, query) - Set the current sequence time
        listSequencerAudio | lsa: (create) - List the audio clips added to the sequencer
        listShots | lsh: (create) - List all the currently defined shots across all scene segments
        modelPanel | mp: (create, query) - Sets a dedicated modelPanel to be used as the panel that the sequencer will control.
        node | nd: (query) - Returns the SequenceManager node, of which there is only ever one.
        writableSequencer | ws: (query) - Get the writable sequencer node.  Create it if it doesn't exist.
    """
    ...


def setDrivenKeyframe(*args, attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., controlPoints: bool = ..., cp: bool = ..., count: bool = ..., cnt: bool = ..., currentDriver: Optional[Union[str, bool]] = ..., cd: Optional[Union[str, bool]] = ..., driven: bool = ..., dn: bool = ..., driver: bool = ..., dr: bool = ..., driverValue: Optional[Union[float, bool]] = ..., dv: Optional[Union[float, bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., hi: Optional[Union[str, bool]] = ..., inTangentType: Optional[Union[str, bool]] = ..., itt: Optional[Union[str, bool]] = ..., insert: bool = ..., i: bool = ..., insertBlend: bool = ..., ib: bool = ..., outTangentType: Optional[Union[str, bool]] = ..., ott: Optional[Union[str, bool]] = ..., shape: bool = ..., s: bool = ..., value: Optional[Union[float, bool]] = ..., v: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        attribute | at: (create, multiuse) - Attribute name to set keyframes on.
        controlPoints | cp: (create) - Explicitly specify whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.
        count | cnt: (query) - Returns the count of driven/drivers attributes for the selected item instead of the names
        currentDriver | cd: (create, query) - Set the driver to be used for the current driven keyframe to the attribute passed as an argument.
        driven | dn: (query) - Returns list of driven attributes for the selected item.
        driver | dr: (query) - Returns list of available drivers for the attribute.
        driverValue | dv: (create, multiuse) - Value of the driver to use for this keyframe. Default value is the current value.
        hierarchy | hi: (create) - Controls the objects this command acts on, relative to the specified (or active) target objects. Valid values are "above," "below," "both," and "none." Default is "hierarchy -query"
        inTangentType | itt: (create) - The in tangent type for keyframes set by this command. Valid values are: "auto", clamped", "fast", "flat", "linear", "plateau", "slow", "spline", and "stepnext" Default is "keyTangent -q -g -inTangentType"
        insert | i: (create) - Insert keys at the given time(s) and preserve the shape of the animation curve(s). Note: the tangent type on inserted keys will be fixed so that the curve shape can be preserved.
        insertBlend | ib: (create) - If true, a pairBlend node will be inserted for channels that have nodes other than animCurves driving them, so that such channels can have blended animation. If false, these channels will not have keys inserted. If the flag is not specified, the blend will be inserted based on the global preference for blending animation.
        outTangentType | ott: (create) - The out tangent type for keyframes set by this command. Valid values are: "auto", "clamped", "fast", "flat", "linear", "plateau", "slow", "spline", "step", and "stepnext". Default is "keyTangent -q -g -outTangentType"
        shape | s: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true
        value | v: (create) - Value to set the keyframe at. Default is the current value.
    """
    ...


def setInfinity(*args, attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., controlPoints: bool = ..., cp: bool = ..., hierarchy: Optional[Union[str, bool]] = ..., hi: Optional[Union[str, bool]] = ..., postInfinite: Optional[Union[str, bool]] = ..., poi: Optional[Union[str, bool]] = ..., preInfinite: Optional[Union[str, bool]] = ..., pri: Optional[Union[str, bool]] = ..., shape: bool = ..., s: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Set the infinity type before (after) a paramCurve's first
    (last) keyframe.

    Args:
        attribute | at: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        controlPoints | cp: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        hierarchy | hi: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        postInfinite | poi: (create, query) - Set the infinity type after a paramCurve's last keyframe. Valid values are "constant", "linear", "cycle", "cycleRelative", "oscillate".
        preInfinite | pri: (create, query) - Set the infinity type before a paramCurve's first keyframe. Valid values are "constant", "linear", "cycle", "cycleRelative", "oscillate".
        shape | s: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
    """
    ...


def setKeyframe(*args, adjustTangent: bool = ..., adt: bool = ..., animLayer: Optional[Union[str, bool]] = ..., al: Optional[Union[str, bool]] = ..., animated: bool = ..., an: bool = ..., attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., breakdown: bool = ..., bd: bool = ..., clip: Optional[Union[str, bool]] = ..., c: Optional[Union[str, bool]] = ..., controlPoints: bool = ..., cp: bool = ..., dirtyDG: bool = ..., dd: bool = ..., float: Optional[Union[float, bool]] = ..., f: Optional[Union[float, bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., hi: Optional[Union[str, bool]] = ..., identity: bool = ..., id: bool = ..., inTangentType: Optional[Union[str, bool]] = ..., itt: Optional[Union[str, bool]] = ..., insert: bool = ..., i: bool = ..., insertBlend: bool = ..., ib: bool = ..., minimizeRotation: bool = ..., mr: bool = ..., noResolve: bool = ..., nr: bool = ..., outTangentType: Optional[Union[str, bool]] = ..., ott: Optional[Union[str, bool]] = ..., preserveCurveShape: bool = ..., pcs: bool = ..., respectKeyable: bool = ..., rk: bool = ..., shape: bool = ..., s: bool = ..., time: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., t: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., useCurrentLockedWeights: bool = ..., lw: bool = ..., value: Optional[Union[float, bool]] = ..., v: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        adjustTangent | adt: (create) - Adjsut tangent if insert keys
        animLayer | al: (create) - Specifies that the new key should be placed in the specified animation layer. Note that if the objects being keyframed are not already part of the layer, this flag will be ignored.
        animated | an: (create) - Add the keyframe only to the attribute(s) that have already a keyframe on. Default: false
        attribute | at: (create, multiuse) - Attribute name to set keyframes on.
        breakdown | bd: (create, edit, query) - Sets the breakdown state for the key.  Default is false
        clip | c: (create) - Specifies that the new key should be placed in the specified clip. Note that if the objects being keyframed are not already part of the clip, this flag will be ignored.
        controlPoints | cp: (create) - Explicitly specify whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.
        dirtyDG | dd: (create) - Allow dirty messages to be sent out when a keyframe is set.
        float | f: (create, multiuse) - Float time at which to set a keyframe on float-based animation curves.
        hierarchy | hi: (create) - Controls the objects this command acts on, relative to the specified (or active) target objects. Valid values are "above," "below," "both," and "none." Default is "hierarchy -query"
        identity | id: (create) - Sets an identity key on an animation layer.  An identity key is one that nullifies the effect of the anim layer.  This flag has effect only when the attribute being keyed is being driven by animation layers.
        inTangentType | itt: (create) - The in tangent type for keyframes set by this command. Valid values are: "auto", clamped", "fast", "flat", "linear", "plateau", "slow", "spline", and "stepnext" Default is "keyTangent -q -g -inTangentType"
        insert | i: (create) - Insert keys at the given time(s) and preserve the shape of the animation curve(s). Note: the tangent type on inserted keys will be fixed so that the curve shape can be preserved.
        insertBlend | ib: (create) - If true, a pairBlend node will be inserted for channels that have nodes other than animCurves driving them, so that such channels can have blended animation. If false, these channels will not have keys inserted. If the flag is not specified, the blend will be inserted based on the global preference for blending animation.
        minimizeRotation | mr: (create) - For rotations, ensures that the key that is set is a minimum distance away from the previous key.  Default is false
        noResolve | nr: (create) - When used with the -value flag, causes the specified value to be set directly onto the animation curve, without attempting to resolve the value across animation layers.
        outTangentType | ott: (create) - The out tangent type for keyframes set by this command. Valid values are: "auto", "clamped", "fast", "flat", "linear", "plateau", "slow", "spline", "step", and "stepnext". Default is "keyTangent -q -g -outTangentType"
        preserveCurveShape | pcs: (create) - Sets the preserve curve shape when inserting keys. Default value depend on your keySetPreserveCurveShape option.
        respectKeyable | rk: (create) - When used with the -attribute flag, prevents the keying of the non keyable attributes.
        shape | s: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true
        time | t: (create, multiuse) - Time at which to set a keyframe on time-based animation curves.
        useCurrentLockedWeights | lw: (create) - If we are setting a key over an existing key, use that key tangent's locked weight value for the new locked weight value.  Default is false
        value | v: (create) - Value at which to set the keyframe. Using the value flag will not cause the keyed attribute to change to the specified value until the scene re-evaluates. Therefore, if you want the attribute to update to the new value immediately, use the setAttr command in addition to setting the key.
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


def shapeEditor(*args, clearSelection: bool = ..., cs: bool = ..., control: bool = ..., ctl: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., exists: bool = ..., ex: bool = ..., filter: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., fmc: Optional[Union[str, bool]] = ..., highlightConnection: Optional[Union[str, bool]] = ..., hlc: Optional[Union[str, bool]] = ..., lockMainConnection: bool = ..., lck: bool = ..., lowestSelection: bool = ..., ls: bool = ..., mainListConnection: Optional[Union[str, bool]] = ..., mlc: Optional[Union[str, bool]] = ..., panel: Optional[Union[str, bool]] = ..., pnl: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., selectionConnection: Optional[Union[str, bool]] = ..., slc: Optional[Union[str, bool]] = ..., stateString: bool = ..., sts: bool = ..., targetControlList: bool = ..., tcl: bool = ..., targetList: bool = ..., tl: bool = ..., unParent: bool = ..., up: bool = ..., unlockMainConnection: bool = ..., ulk: bool = ..., updateMainConnection: bool = ..., upd: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., verticalSliders: bool = ..., vs: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates an editor that derives from the base editor
    class that has controls for deformer, control nodes.

    Args:
        clearSelection | cs: (edit) - Clear the shape editor selection.
        control | ctl: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        docTag | dtg: (create, edit, query) - Attaches a tag to the editor.
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        filter | f: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        forceMainConnection | fmc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        highlightConnection | hlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        lockMainConnection | lck: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        lowestSelection | ls: (query) - Query the lowest selection item.
        mainListConnection | mlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        panel | pnl: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent | p: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        selectionConnection | slc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        stateString | sts: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        targetControlList | tcl: (query) - Query the target control list.
        targetList | tl: (query) - Query the target list.
        unParent | up: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection | ulk: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection | upd: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
        verticalSliders | vs: (create, edit, query) - Should the sliders be vertical?
    """
    ...


def shapePanel(*args, control: bool = ..., ctl: bool = ..., copy: str = ..., cp: str = ..., createString: bool = ..., cs: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., editString: bool = ..., es: bool = ..., exists: bool = ..., ex: bool = ..., init: bool = ..., isUnique: bool = ..., iu: bool = ..., label: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., menuBarRepeatLast: bool = ..., mrl: bool = ..., menuBarVisible: bool = ..., mbv: bool = ..., needsInit: bool = ..., ni: bool = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., popupMenuProcedure: Optional[Union[str, bool]] = ..., pmp: Optional[Union[str, bool]] = ..., replacePanel: str = ..., rp: str = ..., shapeEditor: bool = ..., se: bool = ..., tearOff: bool = ..., to: bool = ..., tearOffCopy: Optional[Union[str, bool]] = ..., toc: Optional[Union[str, bool]] = ..., tearOffRestore: bool = ..., tor: bool = ..., unParent: bool = ..., up: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a panel that derives from the base panel
    class that houses a shapeEditor.

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
        shapeEditor | se: (query) - Query only flag that returns the name of an editor to be associated with the panel.
        tearOff | to: (edit, query) - Will tear off this panel into a separate window with a paneLayout as the parent of the panel. When queried this flag will return if the panel has been torn off into its own window.
        tearOffCopy | toc: (create) - Will create this panel as a torn of copy of the specified source panel.
        tearOffRestore | tor: (create, edit) - Restores panel if it is torn off and focus is given to it. If docked, becomes the active panel in the docked window. This should be the default flag that is added to all panels instead of -to/-tearOff flag which should only be used to tear off the panel.
        unParent | up: (edit) - Specifies that the panel should be removed from its layout. This (obviously) cannot be used with query.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
    """
    ...


def shot(*args, audio: Optional[Union[str, bool]] = ..., aud: Optional[Union[str, bool]] = ..., clip: Optional[Union[str, bool]] = ..., cl: Optional[Union[str, bool]] = ..., clipDuration: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., cd: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., clipOpacity: Optional[Union[float, bool]] = ..., co: Optional[Union[float, bool]] = ..., clipSyncState: bool = ..., css: bool = ..., clipZeroOffset: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., czo: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., copy: bool = ..., c: bool = ..., createCustomAnim: bool = ..., cca: bool = ..., currentCamera: Optional[Union[str, bool]] = ..., cc: Optional[Union[str, bool]] = ..., customAnim: bool = ..., ca: bool = ..., deleteCustomAnim: bool = ..., dca: bool = ..., determineTrack: bool = ..., dt: bool = ..., endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., et: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., favorite: bool = ..., fav: bool = ..., flag1: bool = ..., f1: bool = ..., flag10: bool = ..., f10: bool = ..., flag11: bool = ..., f11: bool = ..., flag12: bool = ..., f12: bool = ..., flag2: bool = ..., f2: bool = ..., flag3: bool = ..., f3: bool = ..., flag4: bool = ..., f4: bool = ..., flag5: bool = ..., f5: bool = ..., flag6: bool = ..., f6: bool = ..., flag7: bool = ..., f7: bool = ..., flag8: bool = ..., f8: bool = ..., flag9: bool = ..., f9: bool = ..., hasCameraSet: bool = ..., hcs: bool = ..., hasStereoCamera: bool = ..., hsc: bool = ..., imagePlaneVisibility: bool = ..., ipv: bool = ..., linkAudio: Optional[Union[str, bool]] = ..., la: Optional[Union[str, bool]] = ..., lock: bool = ..., lck: bool = ..., mute: bool = ..., m: bool = ..., paste: bool = ..., p: bool = ..., pasteInstance: bool = ..., pi: bool = ..., postHoldTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., pst: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., preHoldTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., prt: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., scale: Optional[Union[float, bool]] = ..., s: Optional[Union[float, bool]] = ..., selfmute: bool = ..., sm: bool = ..., sequenceDuration: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., sqd: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., sequenceEndTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., set: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., sequenceStartTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., sst: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., shotName: Optional[Union[str, bool]] = ..., sn: Optional[Union[str, bool]] = ..., sourceDuration: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., sd: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., st: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., track: Optional[Union[int, bool]] = ..., trk: Optional[Union[int, bool]] = ..., transitionInLength: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., til: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., transitionInType: Optional[Union[int, bool]] = ..., tit: Optional[Union[int, bool]] = ..., transitionOutLength: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., tol: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., transitionOutType: Optional[Union[int, bool]] = ..., tot: Optional[Union[int, bool]] = ..., unlinkAudio: bool = ..., ula: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Use this command to create a shot node or manipulate that node.

    Args:
        audio | aud: (create, edit, query) - Specify the audio clip for this shot. Audio can be linked to a shot to allow playback of specific sounds when that shot is being displayed in the Sequencer. Refer to the shot node's documentation for details on how audio is used by shots and the Sequencer.
        clip | cl: (create, edit, query) - The clip associated with this shot. This clip will be posted to the currentCamera's imagePlane. Refer to the shot node's documentation for details on how cameras are used by shots and the Sequencer.
        clipDuration | cd: (create, edit, query) - Length of clip. This is used for the display of the clip indicator bar in the Sequencer.
        clipOpacity | co: (create, edit, query) - Opacity for the shot's clip, this value is assigned to the currentCamera's imagePlane. Refer to the shot node's documentation for details on how cameras are used by shots and the Sequencer.
        clipSyncState | css: (create, edit, query) - The viewport synchronization status of the clip associated with this shot. Return values are, 0 = no clip associated with this shot 1 = clip is fully in sync with viewport, and frames are 1:1 with sequencer 2 = clip is partially in sync with viewport, movie may be scaled to match sequencer 3 = clip not in sync with viewport (i.e. could have scale/time/camera differences)
        clipZeroOffset | czo: (create, edit, query) - Specify which time of the clip corresponds to the beginning of the shot. This is used to properly align splitted clips.
        copy | c: (create, edit, query) - This flag is used to copy a shot to the clipboard. In query mode, this flag allows you to query what, if anything, has been copied into the shot clipboard.
        createCustomAnim | cca: (edit) - Creates an animation layer and links the shot node's customAnim attr to the weight attr of the animation layer
        currentCamera | cc: (create, edit, query) - The camera associated with this shot. Refer to the shot node's documentation for details on how cameras are used by shots and the Sequencer.
        customAnim | ca: (query) - Returns the name of the animation layer node linked to this shot node's customAnim attr
        deleteCustomAnim | dca: (edit) - Disconnects the animation layer from this shot's customAnim attr and deletes the animation layer node
        determineTrack | dt: (edit, query) - Determines an available track for the shot. Returns a new track number or the existing track number if the current track is available.
        endTime | et: (create, edit, query) - The shot end time in the Maya timeline. Changing the startTime will extend the duration of a shot.
        favorite | fav: (create, edit, query) - Make the shot a favorite. This is a UI indicator only to streamline navigation in the Sequencer panel
        flag1 | f1: (create, edit, query) - User specified state flag 1/12 for this shot
        flag10 | f10: (create, edit, query) - User specified state flag 10/12 for this shot
        flag11 | f11: (create, edit, query) - User specified state flag 11/12 for this shot
        flag12 | f12: (create, edit, query) - User specified state flag 12/12 for this shot
        flag2 | f2: (create, edit, query) - User specified state flag 2/12 for this shot
        flag3 | f3: (create, edit, query) - User specified state flag 3/12 for this shot
        flag4 | f4: (create, edit, query) - User specified state flag 4/12 for this shot
        flag5 | f5: (create, edit, query) - User specified state flag 5/12 for this shot
        flag6 | f6: (create, edit, query) - User specified state flag 6/12 for this shot
        flag7 | f7: (create, edit, query) - User specified state flag 7/12 for this shot
        flag8 | f8: (create, edit, query) - User specified state flag 8/12 for this shot
        flag9 | f9: (create, edit, query) - User specified state flag 9/12 for this shot
        hasCameraSet | hcs: (create, edit, query) - Returns true if the camera associated with this shot is a camera set.
        hasStereoCamera | hsc: (create, edit, query) - Returns true if the camera associated with this shot is a stereo camera.
        imagePlaneVisibility | ipv: (create, edit, query) - Visibility of the shot imageplane, this value is assigned to the currentCamera's imagePlane.
        linkAudio | la: (create, edit, query) - Specify an audio clip to link to this shot. Any currently linked audio will be unlinked.
        lock | lck: (create, edit, query) - Lock a specific shot. This is different than locking an entire track, which is done via the shotTrack command
        mute | m: (create, edit, query) - Mute a specific shot. This is different than muting an entire track, which is done via the shotTrack command. Querying this attribute will return true if the shot is muted due to its own mute, its shot being muted, or its shot being unsoloed. See flag "selfmute" to query only the shot's own state.
        paste | p: (create, edit, query) - This flag is used to paste a shot or shots from the clipboard to the sequence timeline. Shots are added to the clipboard using the c/copy flag.
        pasteInstance | pi: (create, edit, query) - This flag is used to paste an instance of a shot or shots from the clipboard to the sequence timeline. Unlike the p/paste flag, which duplicates the camera and image plane from the original source shot, the pi/pasteInstance flag shares the camera and image plane from the source shot. The audio node is duplicated.
        postHoldTime | pst: (create, edit, query) - Specify the time length to append to the shot in the sequence timeline. This repeats the last frame of the shot, in sequence time, over the specified duration.
        preHoldTime | prt: (create, edit, query) - Specify the time length to prepend to the shot in the sequence timeline. This repeats the first frame of the shot, in sequence time, over the specified duration.
        scale | s: (create, edit, query) - Specify an amount to scale the Maya frame range of the shot. This will affect the sequenceEndFrame, leaving the sequenceStartFrame unchanged.
        selfmute | sm: (create, edit, query) - Query if this individual shot's own mute state is set. This is different from the flag "mute", which will return true if this shot is muted due to the track being muted or another track being soloed. Editing this flag will set this shot's own mute status (identical behavior as the flag "mute").
        sequenceDuration | sqd: (edit, query) - Return the sequence duration of the shot, which will include the holds and scale. This flag can only be queried.
        sequenceEndTime | set: (create, edit, query) - The shot end in the sequence timeline. Changing the endTime of a shot will scale it in sequence time.
        sequenceStartTime | sst: (create, edit, query) - The shot start in the sequence timeline. Changing the startTime of a shot will shift it in sequence time.
        shotName | sn: (create, edit, query) - Specify a user-defined name for this shot. This allows the assignment of names that are not valid as node names within Maya. Whenever the shotName attribute is defined its value is used in the UI.
        sourceDuration | sd: (edit, query) - Return the number of source frames in the shot. This flag can only be queried.
        startTime | st: (create, edit, query) - The shot start time in the Maya timeline. Changing the startTime will extend the duration of a shot.
        track | trk: (edit, query) - Specify the track in which this shot resides.
        transitionInLength | til: (create, edit, query) - Length of the transtion into the shot.
        transitionInType | tit: (edit, query) - Specify the the type of transition for the transition into the shot. 0 = Fade 1 = Dissolve
        transitionOutLength | tol: (create, edit, query) - Length of the transtion out of the shot.
        transitionOutType | tot: (edit, query) - Specify the the type of transition for the transition out of the shot. 0 = Fade 1 = Dissolve
        unlinkAudio | ula: (edit, query) - COMMENT Unlinks any currently linked audio.
    """
    ...


def shotRipple(*args, deleted: bool = ..., d: bool = ..., endDelta: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., ed: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., et: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., startDelta: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., sd: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., st: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    When Ripple Edit Mode is enabled, neighboring shots to the shot that gets manipulated
    are moved in sequence time to either make way or close up gaps corresponding to that
    node's editing.
    Given some parameters about the shot edit that just took place, this command
    will choose which other shots to move, and move them the appropriate amounts
    If no shot name is provided, the command will attempt to use the first selected shot.

    Args:
        deleted | d: (create, edit, query) - Specify whether this ripple edit is due to a shot deletion
        endDelta | ed: (create, edit, query) - Specify the change in the end time in frames
        endTime | et: (create, edit, query) - Specify the initial shot end time in the sequence timeline.
        startDelta | sd: (create, edit, query) - Specify the change in the start time in frames
        startTime | st: (create, edit, query) - Specify the initial shot start time in the sequence timeline.
    """
    ...


def simplify(*args, animation: Optional[Union[str, bool]] = ..., an: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., controlPoints: bool = ..., cp: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., f: Optional[Union[Tuple[float, float], bool]] = ..., floatTolerance: Optional[Union[float, bool]] = ..., ft: Optional[Union[float, bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., hi: Optional[Union[str, bool]] = ..., includeUpperBound: bool = ..., iub: bool = ..., index: Optional[Union[int, bool]] = ..., shape: bool = ..., s: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., t: Optional[Union[Tuple[float, float], bool]] = ..., timeTolerance: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., tt: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., valueTolerance: Optional[Union[float, bool]] = ..., vt: Optional[Union[float, bool]] = ...) -> Any:
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
        animation | an: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute | at: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        controlPoints | cp: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        float | f: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        floatTolerance | ft: (create) - Specify the x-axis tolerance (defaults to 0.05) for float-input animCurves such as those created by "Set Driven Keyframe". This flag is ignored on animCurves driven by time. Higher floatTolerance values will result in sparser keys which may less accurately represent the initial curve.
        hierarchy | hi: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        includeUpperBound | iub: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index | index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        shape | s: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        time | t: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
        timeTolerance | tt: (create) - Specify the x-axis tolerance (defaults to 0.05 seconds) for time-input animCurves. This flag is ignored on animCurves driven by floats. Higher time tolerance values will result in sparser keys which may less accurately represent the initial curve.
        valueTolerance | vt: (create) - Specify the value tolerance (defaults to 0.01)
    """
    ...


def skeletonEmbed(*args, mergedMesh: bool = ..., mm: bool = ..., segmentationMethod: Optional[Union[int, bool]] = ..., sm: Optional[Union[int, bool]] = ..., segmentationResolution: Optional[Union[int, bool]] = ..., sr: Optional[Union[int, bool]] = ..., query: bool = ...) -> Any:
    r"""
    This command is used to embed a skeleton inside meshes.

    Args:
        mergedMesh | mm: (query) - When specified, the query command merges selected meshes together and returns a Python object representing the merged mesh.
        segmentationMethod | sm: (create) - Specifies which segmentation algorithm to use to determine what is inside the mesh and what is outside the mesh.  By default, boundary-and-fill-and-grow voxelization will be used.  Available algorithms are:   0  : Perfect mesh (no voxelization). This method works for "perfect meshes", i.e. meshes that are closed, watertight, 2-manifold and without self-intersection or interior/hidden geometry.  It segments the interior region of the mesh from the exterior using a pseudo-normal test. It does not use voxelization.  If mesh conditions are not respected, the segmentation is likely to be wrong.  This can make the segmentation process significantly longer and prevent successful skeleton embedding.   1 : Watertight mesh (flood fill). This method works for "watertight meshes", i.e. meshes for which faces completely separate the interior region of the mesh from the exterior.  The mesh can have degenerated faces, wrong face orientation, self-intersection, etc.  The method uses surface voxelization to classify as part of the interior region all voxels intersecting with a mesh face.  It then performs flood-filling from the outside, marking all reached voxels as part of the exterior region of the model.  Finally, all unreached voxels are marked as part of the interior region.  This method works so long as the mesh is watertight, i.e. without holes up to the voxelization resolution. Otherwise, flood-filling reaches the interior region and creates inaccurate segmentation.   2 : Imperfect mesh (flood fill + growing). This method works for meshes where holes could make the flood-filling step reach the interior region of the mesh, but that have face orientation consistent enough so filling them is possible.  First, it uses surface voxelization to classify as part of the interior region all voxels intersecting with a mesh face.  It then alternates flood-filling and growing steps.  The flood-filling tries to reach all voxels from the outside so that unreached voxels are marked as part of the interior region.  The growing step uses a relatively computation-intensive process to check for interior voxels in all neighbors to those already identified.  Any voxel identified as interior is likely to fill holes, allowing subsequent flood-filling steps to identify more interior voxels.   3 : Polygon soup (repair). This method has no manifold or face orientation requirements.  It reconstructs a mesh that wraps the input mesh with a given offset (3 times the voxel size) and uses this perfect 2-manifold mesh to segment the interior region from the exterior region of the model. Because of the offset, it might lose some of the details and merge parts that are proximal. However, this usually is not an issue with common models where body parts are not too close to one another.   99 : Direct skeleton (no embedding). This method does not try to perform embedding.  It simply returns the skeleton in its initial pose without any attempt at embedding inside the meshes, other than placing it in the meshes bounding box.
        segmentationResolution | sr: (create) - Specifies which segmentation resolution to use for the voxel grid.  By default, 256x256x256 voxels will be used.
    """
    ...


def skinCluster(*args, addInfluence: str = ..., ai: str = ..., addToSelection: bool = ..., ats: bool = ..., after: bool = ..., af: bool = ..., afterReference: bool = ..., ar: bool = ..., baseShape: str = ..., bsh: str = ..., before: bool = ..., bf: bool = ..., bindMethod: Optional[Union[int, bool]] = ..., bm: Optional[Union[int, bool]] = ..., components: bool = ..., cmp: bool = ..., deformerTools: bool = ..., dt: bool = ..., dropoffRate: Optional[Union[float, bool]] = ..., dr: Optional[Union[float, bool]] = ..., exclusive: Optional[Union[str, bool]] = ..., ex: Optional[Union[str, bool]] = ..., forceNormalizeWeights: bool = ..., fnw: bool = ..., frontOfChain: bool = ..., foc: bool = ..., geometry: Optional[Union[str, bool]] = ..., g: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., gi: bool = ..., heatmapFalloff: Optional[Union[float, bool]] = ..., hmf: Optional[Union[float, bool]] = ..., ignoreBindPose: bool = ..., ibp: bool = ..., ignoreHierarchy: bool = ..., ih: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., ihs: bool = ..., influence: Optional[Union[str, bool]] = ..., inf: Optional[Union[str, bool]] = ..., lockWeights: bool = ..., lw: bool = ..., maximumInfluences: Optional[Union[int, bool]] = ..., mi: Optional[Union[int, bool]] = ..., moveJointsMode: bool = ..., mjm: bool = ..., multi: bool = ..., mul: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., normalizeWeights: Optional[Union[int, bool]] = ..., nw: Optional[Union[int, bool]] = ..., nurbsSamples: Optional[Union[int, bool]] = ..., ns: Optional[Union[int, bool]] = ..., obeyMaxInfluences: bool = ..., omi: bool = ..., parallel: bool = ..., par: bool = ..., polySmoothness: Optional[Union[float, bool]] = ..., ps: Optional[Union[float, bool]] = ..., prune: bool = ..., pr: bool = ..., recacheBindMatrices: bool = ..., rbm: bool = ..., remove: bool = ..., rm: bool = ..., removeFromSelection: bool = ..., rfs: bool = ..., removeInfluence: str = ..., ri: str = ..., removeUnusedInfluence: bool = ..., rui: bool = ..., selectInfluenceVerts: str = ..., siv: str = ..., selectedComponents: bool = ..., cms: bool = ..., skinMethod: Optional[Union[int, bool]] = ..., sm: Optional[Union[int, bool]] = ..., smoothWeights: float = ..., sw: float = ..., smoothWeightsMaxIterations: int = ..., swi: int = ..., split: bool = ..., sp: bool = ..., toSelectedBones: bool = ..., tsb: bool = ..., toSkeletonAndTransforms: bool = ..., tst: bool = ..., unbind: bool = ..., ub: bool = ..., unbindKeepHistory: bool = ..., ubk: bool = ..., useComponentTags: bool = ..., uct: bool = ..., useGeometry: bool = ..., ug: bool = ..., volumeBind: Optional[Union[float, bool]] = ..., vb: Optional[Union[float, bool]] = ..., volumeType: Optional[Union[int, bool]] = ..., vt: Optional[Union[int, bool]] = ..., weight: float = ..., wt: float = ..., weightDistribution: Optional[Union[int, bool]] = ..., wd: Optional[Union[int, bool]] = ..., weightedInfluence: bool = ..., wi: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        addInfluence | ai: (edit, multiuse) - The specified transform or joint will be added to the list of transforms that influence the bound geometry. The maximum number of influences will be observed and only the weights of the cv's that the specified transform effects will change. This flag is multi-use.
        addToSelection | ats: (edit) - When used in conjunction with the selectInfluenceVerts flag, causes the vertices afftected by the influence to be added to the current selection, without first de-selecting other vertices.
        after | af: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference | ar: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        baseShape | bsh: (edit, multiuse) - This flag can be used in conjunction with the -addInfluence flag to specify the shape that will be used as the base shape when an influence object with geometry is added to the skinCluster.  If the flag is not used then the command will make a copy of the influence object's shape and use that as a base shape.
        before | bf: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        bindMethod | bm: (create, query) - This flag sets the binding method. 0 - Closest distance between a joint and a point of the geometry. 1 - Closest distance between a joint, considering the skeleton hierarchy, and a point of the geometry. 2 - Surface heat map diffusion. 3 - Geodesic voxel binding.  geomBind command must be called after creating a skinCluster with this method.
        components | cmp: (query) - Returns the components used by the deformer
        deformerTools | dt: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        dropoffRate | dr: (create, edit, query) - Sets the rate at which the influence of a transform drops as the distance from that transform increases. The valid range is between 0.1 and 10.0.  In Create mode it sets the dropoff rate for all the bound joints.  In Edit mode the flag is used together with the inf/influence flag to set the dropoff rate of a particular influence.  Note: When the flag is used in Edit mode, any custom weights on the skin points the given transform influences will be lost.
        exclusive | ex: (create, query) - Puts the deformation set in a deform partition.
        forceNormalizeWeights | fnw: (edit) - If the normalization mode is none or post, it is possible (indeed likely) for the weights in the skin cluster to no longer add up to 1.  This flag forces all weights to add back to 1 again.
        frontOfChain | foc: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry | g: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices | gi: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        heatmapFalloff | hmf: (create) - This flag sets the heatmap binding falloff. If set to 0.0 (default) the deformation will be smoother due to many small weights spread over the mesh surface per influence. However, if set to 1.0, corresponding to maximum falloff, the number of influences per point will be reduced and points will tend to be greatly influenced by their closest joint decreasing the overall spread of small weights. This flag only works when using heatmap binding.
        ignoreBindPose | ibp: (create, edit) - This flag is deprecated and no longer used.  It will be ignored if used.
        ignoreHierarchy | ih: (create, query) - Deprecated. Use bindMethod flag instead. Disregard the place of the joints in the skeleton hierarchy when computing the closest joints that influence a point of the geometry.
        ignoreSelected | ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections | ihs: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        influence | inf: (edit, query) - This flag specifies the influence object that will be used for the current edit operation. In query mode, returns a string array of the influence objects (joints and transform).       In query mode, this flag can accept a value.
        lockWeights | lw: (edit, query) - Lock the weights of the specified influence object to their current value or to the value specified by the -weight flag.
        maximumInfluences | mi: (create, edit, query) - Sets the maximum number of transforms that can influence a point (have non-zero weight for the point) when the skinCluster is first created or a new influence is added.  Note: When this flag is used in Edit mode any custom weights will be lost and new weights will be reassigned to the whole skin.
        moveJointsMode | mjm: (edit) - If set to true, puts the skin into a mode where joints can be moved without modifying the skinning. If set to false, takes the skin out of move joints mode.
        multi | mul: (create) - If true then the command will allow multiple skin clusters to be created on the target geometry. If false the command will generate an error if when trying to add a second skin cluster to the geometry.
        name | n: (create) - Used to specify the name of the node being created.
        normalizeWeights | nw: (create, edit, query) - This flag sets the normalization mode. 0 - none, 1 - interactive, 2 - post (default) Interactive normalization makes sure the weights on the influences add up to 1.0, always. Everytime a weight is changed, the weights are automatically normalized.  This may make it difficult to perform weighting operations, as the normalization may interfere with the weights the user has set.  Post normalization leaves the weights the user has set as is, and only normalizes the weights at the moment it is needed (by dividing by the sum of the weights).  This makes it easier for users to weight their skins.
        nurbsSamples | ns: (create, edit) - Sets the number of sample points that will be used along an influence curve or in each direction on an influence NURBS surface to influence the bound skin. The more the sample points the more closely the skin follows the influence NURBS curve/surface.
        obeyMaxInfluences | omi: (create, edit, query) - When true, the skinCluster will continue to enforce the maximum influences each time the user modifies the weight, so that any given point is only weighted by the number of influences in the skinCluster's maximumInfluences attribute.
        parallel | par: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        polySmoothness | ps: (create, edit) - This flag controls how accurately the skin control points follow a given polygon influence object. The higher the value of polySmoothnmess the more rounded the deformation resulting from a polygonal influence object will be.
        prune | pr: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        recacheBindMatrices | rbm: (edit) - Forces the skinCluster node to recache its bind matrices.
        remove | rm: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        removeFromSelection | rfs: (edit) - When used in conjunction with the selectInfluenceVerts flag, causes the vertices afftected by the influence to be removed from the current selection.
        removeInfluence | ri: (edit, multiuse) - Remove the specified transform or joint from the list of transforms that influence the bound geometry The weights for the affected points are renormalized. This flag is multi-use.
        removeUnusedInfluence | rui: (create, edit, query) - If this flag is set to true then transform or joint whose weights are all zero (they have no effect) will not be bound to the geometry.  Having this option set will help speed-up the playback of animation. In query mode, returns the number of transforms or joints whose weights are all zero.
        selectInfluenceVerts | siv: (edit) - Given the name of a transform, this will select the verts or control points being influenced by this transform, so users may visualize which vertices are being influenced by the transform.
        selectedComponents | cms: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        skinMethod | sm: (create, edit, query) - This flag set the skinning method. 0 - classical linear skinning (default). 1 - dual quaternion (volume preserving), 2 - a weighted blend between the two.
        smoothWeights | sw: (edit) - This flag is used to detect sudden jumps in skin weight values, which often indicates bad weighting, and then smooth out those jaggies in skin weights. The argument is the error tolerance ranging from 0 to 1.  A value of 1 means that the algorithm will smooth a vertex only if there is a 100% change in weight values from its neighbors.  The recommended default to use is 0.5 (50% change in weight value from the neighbors).
        smoothWeightsMaxIterations | swi: (edit) - This flag is valid only with the smooth weights flag.  It is possible that not all the vertices detected as needing smoothing can be smoothed in 1 iteration (because all of their neighbors also have bad weighting and need to be smoothed). With more iterations, more vertices can be smoothed.  This flag controls the maximum number of iterations the algorithm will attempt to smooth weights. The default is 2 for this flag.
        split | sp: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        toSelectedBones | tsb: (create) - geometry will be bound to the selected bones only.
        toSkeletonAndTransforms | tst: (create) - geometry will be bound to the skeleton and any transforms in the hierarchy. If any of the transforms are also bindable objects, assume that only the last object passed to the command is the bindable object. The rest are treated as influences.
        unbind | ub: (edit) - Unbinds the geometry from the skinCluster and deletes the skinCluster node
        unbindKeepHistory | ubk: (edit) - Unbinds the geometry from the skinCluster, but keeps the skinCluster node so that its weights can be used when the skin is rebound. To rebind, use the skinCluster command.
        useComponentTags | uct: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
        useGeometry | ug: (edit) - When adding an influence to a skinCluster, use the geometry parented under the influence transform to determine the weight dropoff of that influence.
        volumeBind | vb: (create) - Creates a volume bind node and attaches it to the new skin cluster node. This node holds hull geometry parameters for a volume based weighting system. This system is used in interactive skinning. The value passed will determine the minimum weight value when initializing the volume. The volume in be increase to enclose all the vertices that are above this value.
        volumeType | vt: (create) - Defines the initial shape of the binding volume (see volumeBind). 0 - Default (currently set to a capsule) 1 - Capsule, 2 - Cylinder.
        weight | wt: (edit) - This flag is only valid in conjunction with the -addInfluence flag. It sets the weight for the influence object that is being added.
        weightDistribution | wd: (create, edit, query) - This flag sets the weight distribution mode. 0 - distance (default), 1 - neighbors When normalizeWeights is in effect, and a weight has been reduced or removed altogether, the sum is usually brought back up to 1.0 by increasing the contributions of the other non-zero weights. However, if there are no other non-zero weights, the algorithm has to create some weights from thin air and distribute the residual weight between them. This attribute controls how that is done. "Distance" - the algorithm calculates weights from the world-space distances from the component to the transforms. "Neighbors" - the algorithm calculates weights from the weights on the neighboring components.
        weightedInfluence | wi: (query) - This flag returns a string array of the influence objects (joints and transform) that have non-zero weighting.
    """
    ...


def skinPercent(*args, ignoreBelow: Optional[Union[float, bool]] = ..., ib: Optional[Union[float, bool]] = ..., normalize: bool = ..., nrm: bool = ..., pruneWeights: Optional[Union[float, bool]] = ..., prw: Optional[Union[float, bool]] = ..., relative: bool = ..., r: bool = ..., resetToDefault: bool = ..., rtd: bool = ..., transform: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ..., transformMoveWeights: Optional[Union[str, bool]] = ..., tmw: Optional[Union[str, bool]] = ..., transformValue: Optional[Union[Tuple[str, float], bool]] = ..., tv: Optional[Union[Tuple[str, float], bool]] = ..., value: bool = ..., v: bool = ..., zeroRemainingInfluences: bool = ..., zri: bool = ..., query: bool = ...) -> Any:
    r"""
    This command edits and queries the weight values on members of a
    skinCluster node, given as the first argument. If no object components
    are explicitly mentioned in the command line, the current selection
    list is used.
    
    Note that setting multiple weights in a single invocation of this
    command is far more efficient than calling it once per weighted
    vertex.

    Args:
        ignoreBelow | ib: (query) - Limits the output of the -value and -transform queries to the entries whose weight values are over the specified limit.  This flag has to be used before the -query flag.       In query mode, this flag needs a value.
        normalize | nrm: (create) - If set, the weights not assigned by the -transformValue flag are normalized so that the sum of the all weights for the selected object component add up to 1. The default is on. NOTE: The skinCluster has a normalizeWeights attribute which when set to OFF overrides this attribute! If the skinCluster.normalizeWeights attribute is OFF, you must set it to Interactive in order to normalize weights using the skinPercent command.
        pruneWeights | prw: (create) - Sets to zero any weight smaller than the given value for all the selected components. To use this command to set all the weights to zero, you must turn the -normalize flag "off" or the skinCluster node will normalize the weights to sum to one after pruning them. Weights for influences with a true value on their "Hold Weights" attribute will not be pruned.
        relative | r: (create) - Used with -transformValue to specify a relative setting of values. If -relative is true, the value passed to -tv is added to the previous value.  Otherwise, it replaces the previous value.
        resetToDefault | rtd: (create) - Sets the weights of the selected components to their default values, overwriting any custom weights.
        transform | t: (query) - In Mel, when used after the -query flag (without an argument) the command returns an array of strings corresponding to the names of the transforms influencing the selected object components.  If used before the -query flag (with a transform name), the command returns the weight of the selected object component corresponding to the given transform. The command will return an average weight if several components have been selected.  In Python, when used with None instead of the name of the transform, the command returns an array of strings corresponding to the names of the transforms influencing the selected object components. If used with a transform name, the command returns the weight of the selected object. The command will return an average weight if several components have been selected.        In query mode, this flag can accept a value.
        transformMoveWeights | tmw: (create, multiuse) - This flag is used to transfer weights from a source influence to one or more target influences. It acts on the selected vertices. The flag must be used at least twice to generate a valid command. The first flag usage indicates the source influence from which the weights will be copied. Subsequent flag usages indicate the target influences.
        transformValue | tv: (create, multiuse) - Accepts a pair consisting of a transform name and a value and assigns that value as the weight of the selected object components corresponding to the given transform.
        value | v: (query) - Returns an array of doubles corresponding to the joint weights for the selected object component.
        zeroRemainingInfluences | zri: (create) - If set, the weights not assigned by the -transformValue flag are set to 0. The default is off.
    """
    ...


def snapKey(*args, animation: Optional[Union[str, bool]] = ..., an: Optional[Union[str, bool]] = ..., attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., controlPoints: bool = ..., cp: bool = ..., float: Optional[Union[Tuple[float, float], bool]] = ..., f: Optional[Union[Tuple[float, float], bool]] = ..., hierarchy: Optional[Union[str, bool]] = ..., hi: Optional[Union[str, bool]] = ..., includeUpperBound: bool = ..., iub: bool = ..., index: Optional[Union[int, bool]] = ..., mergeDuplicate: bool = ..., md: bool = ..., shape: bool = ..., s: bool = ..., time: Optional[Union[Tuple[float, float], bool]] = ..., t: Optional[Union[Tuple[float, float], bool]] = ..., timeMultiple: Optional[Union[float, bool]] = ..., tm: Optional[Union[float, bool]] = ..., valueMultiple: Optional[Union[float, bool]] = ..., vm: Optional[Union[float, bool]] = ...) -> Any:
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
        animation | an: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute | at: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        controlPoints | cp: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        float | f: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        hierarchy | hi: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        includeUpperBound | iub: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index | index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        mergeDuplicate | md: (create) - If this flag is present, keys with duplicated frame will be merged into 1. Default false
        shape | s: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        time | t: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
        timeMultiple | tm: (create) - If this flag is present, key times will be snapped to a multiple of the specified float value.
        valueMultiple | vm: (create) - If this flag is present, key values will be snapped to a multiple of the specified float value.
    """
    ...


def snapshot(*args, constructionHistory: bool = ..., ch: bool = ..., endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., et: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., increment: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., i: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., motionTrail: bool = ..., mt: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., st: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., update: Optional[Union[str, bool]] = ..., u: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        constructionHistory | ch: (create, query) - update with changes to original geometry
        endTime | et: (create, edit, query) - time to stop copying target geometry Default: 10.0
        increment | i: (create, edit, query) - time increment between copies Default: 1.0
        motionTrail | mt: (create) - Rather than create a series of surfaces, create a motion trail displaying the location of the object's pivot point at the specified time steps. Default is false.
        name | n: (create, edit, query) - the name of the snapshot node. Query returns string.
        startTime | st: (create, edit, query) - time to begin copying target geometry Default: 1.0
        update | u: (create, edit, query) - This flag can only be used if the snapshot has constructionHistory. It sets the snapshot node's update value. The update value controls whether the snapshot updates on demand (most efficient), when keyframes change (efficient), or whenever any history changes (least efficient). Valid values are "demand", "animCurve", "always". Default: "always"
    """
    ...


def snapshotBeadCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., inTangent: bool = ..., i: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., outTangent: bool = ..., o: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Creates a context for manipulating in and/or out tangent beads on the motion trail

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        inTangent | i: (edit, query) - Indicates that we will be showing beads for the in tangent when entering the context
        name | n: (create) - If this is a tool command, name the tool appropriately.
        outTangent | o: (edit, query) - Indicates that we will be showing beads for the out tangent when entering the context
    """
    ...


def snapshotModifyKeyCtx(*args, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: Optional[Union[str, bool]] = ..., i1: Optional[Union[str, bool]] = ..., image2: Optional[Union[str, bool]] = ..., i2: Optional[Union[str, bool]] = ..., image3: Optional[Union[str, bool]] = ..., i3: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Creates a context for inserting/delete keys on an editable motion trail

    Args:
        exists | ex: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history | ch: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1 | i1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2 | i2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3 | i3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name | n: (create) - If this is a tool command, name the tool appropriately.
    """
    ...


def softMod(*args, after: bool = ..., af: bool = ..., afterReference: bool = ..., ar: bool = ..., before: bool = ..., bf: bool = ..., bindState: bool = ..., bs: bool = ..., components: bool = ..., cmp: bool = ..., curveInterpolation: Optional[Union[int, bool]] = ..., ci: Optional[Union[int, bool]] = ..., curvePoint: Optional[Union[float, bool]] = ..., cp: Optional[Union[float, bool]] = ..., curveValue: Optional[Union[float, bool]] = ..., cv: Optional[Union[float, bool]] = ..., deformerTools: bool = ..., dt: bool = ..., envelope: Optional[Union[float, bool]] = ..., en: Optional[Union[float, bool]] = ..., exclusive: Optional[Union[str, bool]] = ..., ex: Optional[Union[str, bool]] = ..., falloffAroundSelection: bool = ..., fas: bool = ..., falloffBasedOnX: bool = ..., fbx: bool = ..., falloffBasedOnY: bool = ..., fby: bool = ..., falloffBasedOnZ: bool = ..., fbz: bool = ..., falloffCenter: Optional[Union[Tuple[float, float, float], bool]] = ..., fc: Optional[Union[Tuple[float, float, float], bool]] = ..., falloffMasking: bool = ..., fm: bool = ..., falloffMode: Optional[Union[int, bool]] = ..., fom: Optional[Union[int, bool]] = ..., falloffRadius: Optional[Union[float, bool]] = ..., fr: Optional[Union[float, bool]] = ..., frontOfChain: bool = ..., foc: bool = ..., geometry: Optional[Union[str, bool]] = ..., g: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., gi: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., ihs: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., parallel: bool = ..., par: bool = ..., prune: bool = ..., pr: bool = ..., relative: bool = ..., rel: bool = ..., remove: bool = ..., rm: bool = ..., resetGeometry: bool = ..., rg: bool = ..., selectedComponents: bool = ..., cms: bool = ..., split: bool = ..., sp: bool = ..., useComponentTags: bool = ..., uct: bool = ..., weightedNode: Optional[Union[Tuple[str, str], bool]] = ..., wn: Optional[Union[Tuple[str, str], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    The softMod command creates a softMod or edits the membership of
    an existing softMod. The command returns the name of the softMod
    node upon creation of a new softMod.

    Args:
        after | af: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference | ar: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before | bf: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        bindState | bs: (create) - Specifying this flag adds in a compensation to ensure the softModed objects preserve their spatial position when softModed. This is required to prevent the geometry from jumping at the time the softMod is created in situations when the softMod transforms at softMod time are not identity.
        components | cmp: (query) - Returns the components used by the deformer
        curveInterpolation | ci: (create, multiuse) - Ramp interpolation corresponding to the specified curvePoint position. Integer values of 0-3 are valid, corresponding to "none", "linear", "smooth" and "spline" respectively. This flag may only be used in conjunction with the curvePoint and curveValue flag.
        curvePoint | cp: (create, multiuse) - Position of ramp value on normalized 0-1 scale. This flag may only be used in conjunction with the curveInterpolation and curveValue flags.
        curveValue | cv: (create, multiuse) - Ramp value corresponding to the specified curvePoint position. This flag may only be used in conjunction with the curveInterpolation and curvePoint flags.
        deformerTools | dt: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        envelope | en: (create, edit, query) - Set the envelope value for the deformer. Default is 1.0
        exclusive | ex: (create, query) - Puts the deformation set in a deform partition.
        falloffAroundSelection | fas: (create) - Falloff will be calculated around any selected components
        falloffBasedOnX | fbx: (create) - Falloff will be calculated using the X component.
        falloffBasedOnY | fby: (create) - Falloff will be calculated using the Y component.
        falloffBasedOnZ | fbz: (create) - Falloff will be calculated using the Z component.
        falloffCenter | fc: (create) - Set the falloff center point of the softMod.
        falloffMasking | fm: (create) - Deformation will be restricted to selected components
        falloffMode | fom: (create) - Set the falloff method used for the softMod.
        falloffRadius | fr: (create) - Set the falloff radius of the softMod.
        frontOfChain | foc: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry | g: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices | gi: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected | ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections | ihs: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        name | n: (create) - Used to specify the name of the node being created.
        parallel | par: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        prune | pr: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        relative | rel: (create) - Enable relative mode for the softMod. In relative mode, Only the transformations directly above the softMod are used by the softMod. Default is off.
        remove | rm: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        resetGeometry | rg: (edit) - Reset the geometry matrices for the objects being deformed by the softMod. This flag is used to get rid of undesirable effects that happen if you scale an object that is deformed by a softMod.
        selectedComponents | cms: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        split | sp: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        useComponentTags | uct: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
        weightedNode | wn: (create, edit, query) - Transform node in the DAG above the softMod to which all percents are applied. The second node specifies the descendent of the first node from where the transformation matrix is evaluated. Default is the softMod handle.
    """
    ...


def sound(*args, endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., et: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., file: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., length: bool = ..., l: bool = ..., mute: bool = ..., m: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., offset: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., o: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., sourceEnd: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., se: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., sourceStart: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., ss: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Creates an audio node which can be used with UI commands such
    as soundControl or timeControl which support sound scrubbing
    and sound during playback.

    Args:
        endTime | et: (create, edit, query) - Time at which to end the sound.
        file | f: (create, edit, query) - Name of sound file.
        length | l: (query) - Query the length (in the current time unit) of the sound.
        mute | m: (create, edit, query) - Mute the audio clip.
        name | n: (create, edit, query) - Name to give the resulting audio node.
        offset | o: (create, edit, query) - Time at which to start the sound.
        sourceEnd | se: (create, edit, query) - Time offset from the start of the sound file at which to end the sound.
        sourceStart | ss: (create, edit, query) - Time offset from the start of the sound file at which to start the sound.
    """
    ...


def substituteGeometry(*args, disableNonSkinDeformers: bool = ..., dnd: bool = ..., newGeometryToLayer: bool = ..., ngl: bool = ..., oldGeometryToLayer: bool = ..., ogl: bool = ..., reWeightDistTolerance: Optional[Union[float, bool]] = ..., wdt: Optional[Union[float, bool]] = ..., retainOldGeometry: bool = ..., rog: bool = ...) -> Any:
    r"""
    This command can be used to replace the geometry which is already connected
    to deformers with a new geometry. The weights on the old geometry will be
    retargeted to the new geometry.

    Args:
        disableNonSkinDeformers | dnd: (create) - This flag controls the state of deformers other than skin deformers after the substitution has taken place. If the flag is true then non-skin deformer nodes are left in a disabled state at the completion of the command. Default value is false.
        newGeometryToLayer | ngl: (create) - Create a new layer for the new geometry.
        oldGeometryToLayer | ogl: (create) - Create a new layer and move the old geometry to this layer
        reWeightDistTolerance | wdt: (create) - Specify the distance tolerance value to be used for retargeting weights. While transferring weights the command tries to find the corresponding vertices by overlapping the geometries with all deformers disabled. Sometimes this results in selection of unrelated vertices. (Example when a hole in the old geometry has been filled with new vertices in the new geometry.) This distance tolerance value is used to detect this kind of faults and either ignore these cases or to vary algorithm to find more corresponding vertices.
        retainOldGeometry | rog: (create) - A copy of the old geometry should be retained
    """
    ...


def tangentConstraint(*args, aimVector: Optional[Union[Tuple[float, float, float], bool]] = ..., aim: Optional[Union[Tuple[float, float, float], bool]] = ..., layer: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., remove: bool = ..., rm: bool = ..., targetList: bool = ..., tl: bool = ..., upVector: Optional[Union[Tuple[float, float, float], bool]] = ..., u: Optional[Union[Tuple[float, float, float], bool]] = ..., weight: Optional[Union[float, bool]] = ..., w: Optional[Union[float, bool]] = ..., weightAliasList: bool = ..., wal: bool = ..., worldUpObject: Optional[Union[str, bool]] = ..., wuo: Optional[Union[str, bool]] = ..., worldUpType: Optional[Union[str, bool]] = ..., wut: Optional[Union[str, bool]] = ..., worldUpVector: Optional[Union[Tuple[float, float, float], bool]] = ..., wu: Optional[Union[Tuple[float, float, float], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
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
        aimVector | aim: (create, edit, query) - Set the aim vector.  This is the vector in local coordinates that points at the target.  If not given at creation time, the default value of (1.0, 0.0, 0.0) is used.
        layer | l: (create, edit) - Specify the name of the animation layer where the constraint should be added.
        name | n: (create, edit, query) - Sets the name of the constraint node to the specified name.  Default name is constrainedObjectName_constraintType
        remove | rm: (edit) - removes the listed target(s) from the constraint.
        targetList | tl: (query) - Return the list of target objects.
        upVector | u: (create, edit, query) - Set local up vector.  This is the vector in local coordinates that aligns with the world up vector.  If not given at creation time, the default value of (0.0, 1.0, 0.0) is used.
        weight | w: (create, edit, query) - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
        weightAliasList | wal: (query) - Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
        worldUpObject | wuo: (create, edit, query) - Set the DAG object use for worldUpType "object" and "objectrotation". See worldUpType for greater detail. The default value is no up object, which is interpreted as world space.
        worldUpType | wut: (create, edit, query) - Set the type of the world up vector computation. The worldUpType can have one of 5 values: "scene", "object", "objectrotation", "vector", or "none". If the value is "scene", the upVector is aligned with the up axis of the scene and worldUpVector and worldUpObject are ignored. If the value is "object", the upVector is aimed as closely as possible to the origin of the space of the worldUpObject and the worldUpVector is ignored. If the value is "objectrotation" then the worldUpVector is interpreted as being in the coordinate space of the worldUpObject, transformed into world space and the upVector is aligned as closely as possible to the result. If the value is "vector", the upVector is aligned with worldUpVector as closely as possible and worldUpMatrix is ignored. Finally, if the value is "none" no twist calculation is performed by the constraint, with the resulting "upVector" orientation based previous orientation of the constrained object, and the "great circle" rotation needed to align the aim vector with its constraint. The default worldUpType is "vector".
        worldUpVector | wu: (create, edit, query) - Set world up vector.  This is the vector in world coordinates that up vector should align with. See -wut/worldUpType (below)for greater detail. If not given at creation time, the default value of (0.0, 1.0, 0.0) is used.
    """
    ...


def tension(*args, after: bool = ..., af: bool = ..., afterReference: bool = ..., ar: bool = ..., before: bool = ..., bf: bool = ..., components: bool = ..., cmp: bool = ..., deformerTools: bool = ..., dt: bool = ..., envelope: Optional[Union[float, bool]] = ..., en: Optional[Union[float, bool]] = ..., exclusive: Optional[Union[str, bool]] = ..., ex: Optional[Union[str, bool]] = ..., frontOfChain: bool = ..., foc: bool = ..., geometry: Optional[Union[str, bool]] = ..., g: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., gi: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., ihs: bool = ..., inwardConstraint: Optional[Union[float, bool]] = ..., iwc: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., outwardConstraint: Optional[Union[float, bool]] = ..., owc: Optional[Union[float, bool]] = ..., parallel: bool = ..., par: bool = ..., pinBorderVertices: bool = ..., pbv: bool = ..., prune: bool = ..., pr: bool = ..., remove: bool = ..., rm: bool = ..., selectedComponents: bool = ..., cms: bool = ..., smoothingIterations: Optional[Union[int, bool]] = ..., si: Optional[Union[int, bool]] = ..., smoothingStep: Optional[Union[float, bool]] = ..., ss: Optional[Union[float, bool]] = ..., split: bool = ..., sp: bool = ..., useComponentTags: bool = ..., uct: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to create, edit and query tension nodes.

    Args:
        after | af: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference | ar: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before | bf: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        components | cmp: (query) - Returns the components used by the deformer
        deformerTools | dt: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        envelope | en: (create, edit, query) - Envelope of the tension node. The envelope determines the percent of deformation. Value is clamped to [0, 1] range. Default is 1.
        exclusive | ex: (create, query) - Puts the deformation set in a deform partition.
        frontOfChain | foc: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry | g: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices | gi: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected | ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections | ihs: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        inwardConstraint | iwc: (create, edit, query) - Constrains the movement of the vertex to not move inward from the input deforming shape to preserve the contour. Value is in the [0,1] range. Default is 0.0.
        name | n: (create) - Used to specify the name of the node being created.
        outwardConstraint | owc: (create, edit, query) - Constrains the movement of the vertex to not move outward from the input deforming shape to preserve the contour. Value is in the [0,1] range.
        parallel | par: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        pinBorderVertices | pbv: (create, edit, query) - If enabled, vertices on mesh borders will be pinned to their current position during smoothing. Default is true.
        prune | pr: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        remove | rm: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        selectedComponents | cms: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        smoothingIterations | si: (create, edit, query) - Number of smoothing iterations performed by the tension node. Default is 10.
        smoothingStep | ss: (create, edit, query) - Step amount used per smoothing iteration. Value is clamped to [0, 1] range. A higher value may lead to instabilities but converges faster compared to a lower value. Default is 0.5.
        split | sp: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        useComponentTags | uct: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
    """
    ...


def textureDeformer(*args, after: bool = ..., af: bool = ..., afterReference: bool = ..., ar: bool = ..., before: bool = ..., bf: bool = ..., components: bool = ..., cmp: bool = ..., deformerTools: bool = ..., dt: bool = ..., direction: Optional[Union[str, bool]] = ..., d: Optional[Union[str, bool]] = ..., envelope: Optional[Union[float, bool]] = ..., en: Optional[Union[float, bool]] = ..., exclusive: Optional[Union[str, bool]] = ..., ex: Optional[Union[str, bool]] = ..., frontOfChain: bool = ..., foc: bool = ..., geometry: Optional[Union[str, bool]] = ..., g: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., gi: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., ihs: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., offset: Optional[Union[float, bool]] = ..., o: Optional[Union[float, bool]] = ..., parallel: bool = ..., par: bool = ..., pointSpace: Optional[Union[str, bool]] = ..., ps: Optional[Union[str, bool]] = ..., prune: bool = ..., pr: bool = ..., remove: bool = ..., rm: bool = ..., selectedComponents: bool = ..., cms: bool = ..., split: bool = ..., sp: bool = ..., strength: Optional[Union[float, bool]] = ..., s: Optional[Union[float, bool]] = ..., useComponentTags: bool = ..., uct: bool = ..., vectorOffset: Optional[Union[Tuple[float, float, float], bool]] = ..., vo: Optional[Union[Tuple[float, float, float], bool]] = ..., vectorSpace: Optional[Union[str, bool]] = ..., vsp: Optional[Union[str, bool]] = ..., vectorStrength: Optional[Union[Tuple[float, float, float], bool]] = ..., vs: Optional[Union[Tuple[float, float, float], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a texture deformer for the object.
    The selected objects are the input geometry objects.
    The deformer node name will be returned.

    Args:
        after | af: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference | ar: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before | bf: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        components | cmp: (query) - Returns the components used by the deformer
        deformerTools | dt: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        direction | d: (create) - Set the deformation direction of texture deformer It can only handle three types: "Normal", "Handle" and "Vector". "Normal"  each vertices use its own normal vector. "Handle"  all vertices use Up vector of the handle. "Vector"  each vertices use RGB color vector strings.
        envelope | en: (create) - Set the envelope of texture deformer. Envelope determines the percent of deformation. The final result is (color * normal * strength + offset) * envelope
        exclusive | ex: (create, query) - Puts the deformation set in a deform partition.
        frontOfChain | foc: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry | g: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices | gi: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        ignoreSelected | ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections | ihs: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        name | n: (create) - Used to specify the name of the node being created.
        offset | o: (create) - Set the offset of texture deformer. Offset plus a translation on the final deformed vertices.
        parallel | par: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        pointSpace | ps: (create) - Set the point space of texture deformer. It can only handle three strings: "World", "Local" and "UV". "World"   map world space to color space. "Local"	  map local space to color space. "UV"	  map UV space to color space. strings.
        prune | pr: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        remove | rm: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        selectedComponents | cms: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        split | sp: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        strength | s: (create) - Set the strength of texture deformer. Strength determines how strong the object is deformed.
        useComponentTags | uct: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
        vectorOffset | vo: (create) - Set the vector offset of texture deformer. Vector offset indicates the offset of the deformation on the vector mode.
        vectorSpace | vsp: (create) - Set the vector space of texture deformer. It can only handle three strings: "Object", "World" and "Tangent". "Object"   	use color vector in object space "World"	 	use color vector in world space "Tangent"	use color vector in tangent space strings.
        vectorStrength | vs: (create) - Set the vector strength of texture deformer. Vector strength determines how strong the object is deformed on the vector mode.
    """
    ...


def timeEditor(*args, allClips: Optional[Union[str, bool]] = ..., alc: Optional[Union[str, bool]] = ..., clipId: Optional[Union[int, bool]] = ..., id: Optional[Union[int, bool]] = ..., commonParentTrack: bool = ..., cpt: bool = ..., composition: Optional[Union[str, bool]] = ..., cp: Optional[Union[str, bool]] = ..., drivingClipsForAttr: Optional[Union[str, bool]] = ..., dca: Optional[Union[str, bool]] = ..., drivingClipsForObj: Optional[Union[Tuple[str, int], bool]] = ..., dco: Optional[Union[Tuple[str, int], bool]] = ..., includeParent: bool = ..., ip: bool = ..., mute: bool = ..., m: bool = ..., selectedClips: Optional[Union[str, bool]] = ..., sc: Optional[Union[str, bool]] = ..., topLevelClips: Optional[Union[str, bool]] = ..., tlc: Optional[Union[str, bool]] = ..., query: bool = ...) -> Any:
    r"""
    General Time Editor commands

    Args:
        allClips | alc: (create) - Return an exhaustive (recursive) list of all clip IDs from the active composition. Arguments may be used to filter the returning result. An empty string will return clip IDs for all clip types:   roster   container   group
        clipId | id: (create, multiuse) - ID of the clip to be edited.
        commonParentTrack | cpt: (create) - Locate the common parent track node and track index of the given clip IDs. Requires a list of clip IDs to be specified using the clipId flag. The format of the returned string is "track_node:track_index". If the clips specified are on the same track node but in different track indexes, only the track node will be returned.
        composition | cp: (create) - A flag to use in conjunction with -dca/drivingClipsForObj to indicate the name of composition to use. By default if this flag is not provided, current active composition will be used.
        drivingClipsForAttr | dca: (create) - Return a list of clips driving the specified attribute(s). If the composition is not specified, current active composition will be used.
        drivingClipsForObj | dco: (create) - Return a list of clips driving the specified object(s) with an integer value indicating the matching mode. If no object is specified explicitly, the selected object(s) will be used. Objects that cannot be driven by clips are ignored. If the composition is not specified, current active composition will be used. Default match mode is 0.  0: Include only the clip that has an exact match 1: Include any clip that contains all of the specified objects 2: Include any clip that contains any of the specified objects 3: Include all clips that do not include any of the specified objects
        includeParent | ip: (create) - A toggle flag to use in conjunction with -dca/drivingClipsForObj. When toggled, parent clip is included in selection (the entire hierarchy will be selected).
        mute | m: (create, query) - Mute/unmute Time Editor.
        selectedClips | sc: (create) - Return a list of clip IDs of currently selected Time Editor clips. Arguments may be used to filter the returning result. An empty string will return clip IDs for all clip types:   roster   container   group
        topLevelClips | tlc: (create) - Return a list of all top-level clip IDs from the active composition. Arguments may be used to filter the returning result. An empty string will return clip IDs for all clip types:   roster   container   group
    """
    ...


def timeEditorAnimSource(*args, addSource: str = ..., asc: str = ..., apply: bool = ..., ap: bool = ..., bakeToAnimSource: str = ..., bas: str = ..., calculateTiming: bool = ..., ct: bool = ..., copyAnimation: bool = ..., cp: bool = ..., drivenClips: bool = ..., dc: bool = ..., export: str = ..., ex: str = ..., isUnique: bool = ..., iu: bool = ..., removeSource: str = ..., rs: str = ..., targetIndex: Optional[Union[str, bool]] = ..., ti: Optional[Union[str, bool]] = ..., targets: bool = ..., trg: bool = ..., addObjects: Optional[Union[str, bool]] = ..., ao: Optional[Union[str, bool]] = ..., addRelatedKG: bool = ..., akg: bool = ..., addSelectedObjects: bool = ..., aso: bool = ..., attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., exclusive: bool = ..., exc: bool = ..., importAllFbxTakes: bool = ..., aft: bool = ..., importFbx: Optional[Union[str, bool]] = ..., fbx: Optional[Union[str, bool]] = ..., importFbxTakes: Optional[Union[str, bool]] = ..., ft: Optional[Union[str, bool]] = ..., importMayaFile: Optional[Union[str, bool]] = ..., mf: Optional[Union[str, bool]] = ..., importOption: str = ..., io: str = ..., importPopulateOption: str = ..., ipo: str = ..., importedContainerNames: Optional[Union[str, bool]] = ..., icn: Optional[Union[str, bool]] = ..., includeRoot: bool = ..., irt: bool = ..., populateImportedAnimSources: Optional[Union[str, bool]] = ..., pia: Optional[Union[str, bool]] = ..., poseClip: bool = ..., poc: bool = ..., recursively: bool = ..., rec: bool = ..., removeSceneAnimation: bool = ..., rsa: bool = ..., showAnimSourceRemapping: bool = ..., sar: bool = ..., takeList: Optional[Union[str, bool]] = ..., tl: Optional[Union[str, bool]] = ..., takesToImport: Optional[Union[str, bool]] = ..., toi: Optional[Union[str, bool]] = ..., type: Optional[Union[str, bool]] = ..., typ: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Commands for managing animation sources.

    Args:
        addSource | asc: (edit) - Add single new target attribute with its animation.
        apply | ap: (edit) - Connect anim source's animation directly to the target objects. If the Time Editor is not muted, connect to scene storage instead.
        bakeToAnimSource | bas: (edit) - Create a new anim source with the same animation as this anim source. All non-curve inputs will be baked down, whereas curve sources will be shared.
        calculateTiming | ct: (edit, query) - Adjust start/duration when adding/removing sources. If query it returns the [start,duration] pair.
        copyAnimation | cp: (edit) - Copy animation when adding source.
        drivenClips | dc: (query) - Return all clips driven by the given anim source.
        export | ex: (edit) - Export given anim source and the animation curves to a specified Maya file.
        isUnique | iu: (query) - Return true if the anim source node is only driving a single clip.
        removeSource | rs: (edit) - Remove single attribute.
        targetIndex | ti: (query) - Get target index.
        targets | trg: (query) - Get a list of all targets in this anim source.
        addObjects | ao: (create, edit, query) - Populate the given object(s) and their attributes to anim source to Time Editor. For multiple object, pass each name separated by semicolon. In query mode, return the number of attributes that will be populated given the flags, along with the animation's first and last frames for the given object(s). Similar to -addSelectedObjects flag but acts on given object(s) instead. This flag will override the flag -addSelectedObjects.
        addRelatedKG | akg: (create, edit, query) - During population, determine if associated keying groups should be populated or not. Normally used for populating HIK. By default the value is false.
        addSelectedObjects | aso: (create, edit, query) - Populate the currently selected objects and their attributes to anim source or Time Editor. In query mode, return the number of attributes that will be populated given the flags, along with the animation's first and last frames.
        attribute | at: (create, edit, multiuse) - Populate a specific attribute on a object.
        exclusive | exc: (create, edit) - Populate all types of animation sources which are not listed by "type" Flag.
        importAllFbxTakes | aft: (create) - Import all FBX takes into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).
        importFbx | fbx: (create) - Import an animation from FBX file into the new anim source (for timeEditorAnimSource command) or new container (for timeEditorClip command).
        importFbxTakes | ft: (create) - Import multiple FBX takes (separated by semicolons) into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).
        importMayaFile | mf: (create) - Import an animation from Maya file into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).
        importOption | io: (edit) - Option for importing animation source. Specify either 'connect' or 'generate'. connect:  Only connect with nodes already existing in the scene.                   Importing an animation source that does not match with any element                   of the current scene will not create any clip.                   (connect is the default mode). generate: Import everything and generate new nodes for items not existing in the scene.
        importPopulateOption | ipo: (edit) - Option for population when importing.
        importedContainerNames | icn: (create) - Internal use only. To be used along with populateImportedAnimSources to specify names for the created containers.
        includeRoot | irt: (create, edit) - Populate transform (Translate, Rotate, Scale) of hierarchy root nodes.
        populateImportedAnimSources | pia: (create) - Internal use only. Populate the Time Editor with clips using the Animation Sources specified (use ; as a delimiter for multiple anim sources).
        poseClip | poc: (create) - Populate as pose clip with current attribute values.
        recursively | rec: (create, edit) - Populate selection recursively, adding all the children.
        removeSceneAnimation | rsa: (create, edit) - If true, remove animation from scene when creating clips or anim sources. Only Time Editor will drive the removed scene animation.
        showAnimSourceRemapping | sar: (create) - Show a remapping dialog when the imported anim source attributes do not match the scene attributes.
        takeList | tl: (create) - Internal use only. To be used along with populateImportedAnimSources to specify the imported take names.
        takesToImport | toi: (create) - Internal use only. To be used along with populateImportedAnimSources to specify the imported take indices.
        type | typ: (create, edit, multiuse, query) - Only populate the specified type of animation source.
    """
    ...


def timeEditorBakeClips(*args, bakeToAnimSource: Optional[Union[str, bool]] = ..., bas: Optional[Union[str, bool]] = ..., bakeToClip: Optional[Union[str, bool]] = ..., btc: Optional[Union[str, bool]] = ..., clipId: Optional[Union[int, bool]] = ..., id: Optional[Union[int, bool]] = ..., combineLayers: bool = ..., cl: bool = ..., forceSampling: bool = ..., fs: bool = ..., keepOriginalClip: bool = ..., koc: bool = ..., path: Optional[Union[str, bool]] = ..., pt: Optional[Union[str, bool]] = ..., sampleBy: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., sb: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., targetTrackIndex: Optional[Union[int, bool]] = ..., tti: Optional[Union[int, bool]] = ..., targetTracksNode: Optional[Union[str, bool]] = ..., ttn: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to bake Time Editor clips and to blend them into a single clip.

    Args:
        bakeToAnimSource | bas: (create) - Bake/merge the selected clips into the animation source.
        bakeToClip | btc: (create) - Bake/merge the selected clips into a clip.
        clipId | id: (create, multiuse) - Clip IDs of the clips to bake.
        combineLayers | cl: (create) - Combine the layers of the input clip.
        forceSampling | fs: (create) - Force sampling on the whole time range when baking.
        keepOriginalClip | koc: (create) - Keep the source clips after baking.
        path | pt: (create, multiuse) - Full path of clips on which to operate. For example: composition1|track1|group; composition1|track1|group|track2|clip1.
        sampleBy | sb: (create) - Sampling interval when baking crossfades and timewarps.
        targetTrackIndex | tti: (create) - Specify the target track when baking containers. If targetTrackIndex is specified, the track index within the specified node is used. If targetTrackIndex is not specified or is the default value (-1), the track index within the current node is used. If targetTrackIndex is -2, a new track will be created.
        targetTracksNode | ttn: (create) - Target tracks node when baking containers.
    """
    ...


def timeEditorClip(*args, absolute: bool = ..., abs: bool = ..., addAttribute: str = ..., aa: str = ..., allowShrinking: bool = ..., eas: bool = ..., animSource: Optional[Union[str, bool]] = ..., asr: Optional[Union[str, bool]] = ..., audio: Optional[Union[str, bool]] = ..., au: Optional[Union[str, bool]] = ..., blendMode: Optional[Union[int, bool]] = ..., bm: Optional[Union[int, bool]] = ..., children: Optional[Union[int, bool]] = ..., chl: Optional[Union[int, bool]] = ..., clipAfter: bool = ..., ca: bool = ..., clipBefore: bool = ..., cb: bool = ..., clipDataType: bool = ..., cdt: bool = ..., clipId: Optional[Union[int, bool]] = ..., id: Optional[Union[int, bool]] = ..., clipIdFromNodeName: Optional[Union[int, bool]] = ..., idn: Optional[Union[int, bool]] = ..., clipIdFromPath: bool = ..., idp: bool = ..., clipNode: bool = ..., cln: bool = ..., clipPath: bool = ..., clp: bool = ..., copyClip: bool = ..., ccl: bool = ..., crossfadeMode: Optional[Union[int, bool]] = ..., cfm: Optional[Union[int, bool]] = ..., crossfadePlug: bool = ..., cfp: bool = ..., curveTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., cvt: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., defaultGhostRoot: bool = ..., dgr: bool = ..., drivenAttributes: bool = ..., dat: bool = ..., drivenClipsBySource: Optional[Union[str, bool]] = ..., dcs: Optional[Union[str, bool]] = ..., drivenObjects: bool = ..., dos: bool = ..., drivenRootObjects: bool = ..., dro: bool = ..., drivingSources: Optional[Union[str, bool]] = ..., dsc: Optional[Union[str, bool]] = ..., duplicateClip: bool = ..., dcl: bool = ..., duration: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., d: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., emptySource: bool = ..., ems: bool = ..., endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., et: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., existingOnly: bool = ..., exo: bool = ..., exists: bool = ..., exs: bool = ..., explode: int = ..., epl: int = ..., exportAllClips: bool = ..., eac: bool = ..., exportFbx: str = ..., ef: str = ..., extend: bool = ..., ex: bool = ..., extendParent: bool = ..., exp: bool = ..., ghost: bool = ..., gh: bool = ..., ghostRootAdd: str = ..., gra: str = ..., ghostRootRemove: str = ..., grr: str = ..., group: bool = ..., grp: bool = ..., holdEnd: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., he: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., holdStart: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., hs: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., importTakeDestination: Optional[Union[int, bool]] = ..., itd: Optional[Union[int, bool]] = ..., isContainer: bool = ..., ict: bool = ..., listUserGhostRoot: bool = ..., lug: bool = ..., loopEnd: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., le: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., loopStart: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., ls: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., minClipDuration: bool = ..., mcd: bool = ..., modifyAnimSource: bool = ..., mas: bool = ..., moveClip: Union[float, Tuple[float, float]] = ..., mcl: Union[float, Tuple[float, float]] = ..., mute: bool = ..., m: bool = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., parent: int = ..., p: int = ..., parentClipId: Optional[Union[int, bool]] = ..., pid: Optional[Union[int, bool]] = ..., parentGroupId: bool = ..., pgd: bool = ..., pasteClip: Union[float, Tuple[float, float]] = ..., pcl: Union[float, Tuple[float, float]] = ..., path: str = ..., pt: str = ..., preserveAnimationTiming: bool = ..., pat: bool = ..., razorClip: Union[float, Tuple[float, float]] = ..., rcl: Union[float, Tuple[float, float]] = ..., remap: Tuple[str, str] = ..., rmp: Tuple[str, str] = ..., remapNamespace: Optional[Union[Tuple[str, str], bool]] = ..., rns: Optional[Union[Tuple[str, str], bool]] = ..., remapSource: Tuple[str, str] = ..., rs: Tuple[str, str] = ..., remappedSourceAttrs: bool = ..., rms: bool = ..., remappedTargetAttrs: bool = ..., rmt: bool = ..., removeAttribute: str = ..., ra: str = ..., removeClip: bool = ..., rmc: bool = ..., removeCrossfade: bool = ..., rcf: bool = ..., removeWeightCurve: bool = ..., rwc: bool = ..., resetTiming: bool = ..., rt: bool = ..., resetTransition: bool = ..., rtr: bool = ..., ripple: bool = ..., rpl: bool = ..., rootClipId: int = ..., rti: int = ..., rootPath: str = ..., rpt: str = ..., scaleEnd: Union[float, Tuple[float, float]] = ..., sce: Union[float, Tuple[float, float]] = ..., scalePivot: Union[float, Tuple[float, float]] = ..., scp: Union[float, Tuple[float, float]] = ..., scaleStart: Union[float, Tuple[float, float]] = ..., scs: Union[float, Tuple[float, float]] = ..., setKeyframe: str = ..., k: str = ..., speedRamping: Optional[Union[int, bool]] = ..., src: Optional[Union[int, bool]] = ..., startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., s: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., timeWarp: bool = ..., tw: bool = ..., timeWarpCurve: bool = ..., twc: bool = ..., timeWarpType: Optional[Union[int, bool]] = ..., twt: Optional[Union[int, bool]] = ..., track: Optional[Union[str, bool]] = ..., trk: Optional[Union[str, bool]] = ..., tracksNode: bool = ..., trn: bool = ..., transition: bool = ..., tra: bool = ..., trimEnd: Union[float, Tuple[float, float]] = ..., tre: Union[float, Tuple[float, float]] = ..., trimStart: Union[float, Tuple[float, float]] = ..., trs: Union[float, Tuple[float, float]] = ..., truncated: bool = ..., trc: bool = ..., uniqueAnimSource: bool = ..., uas: bool = ..., userGhostRoot: bool = ..., ugr: bool = ..., weightCurve: bool = ..., wc: bool = ..., zeroKeying: bool = ..., zk: bool = ..., addObjects: Optional[Union[str, bool]] = ..., ao: Optional[Union[str, bool]] = ..., addRelatedKG: bool = ..., akg: bool = ..., addSelectedObjects: bool = ..., aso: bool = ..., attribute: Optional[Union[str, bool]] = ..., at: Optional[Union[str, bool]] = ..., exclusive: bool = ..., exc: bool = ..., importAllFbxTakes: bool = ..., aft: bool = ..., importFbx: Optional[Union[str, bool]] = ..., fbx: Optional[Union[str, bool]] = ..., importFbxTakes: Optional[Union[str, bool]] = ..., ft: Optional[Union[str, bool]] = ..., importMayaFile: Optional[Union[str, bool]] = ..., mf: Optional[Union[str, bool]] = ..., importOption: str = ..., io: str = ..., importPopulateOption: str = ..., ipo: str = ..., importedContainerNames: Optional[Union[str, bool]] = ..., icn: Optional[Union[str, bool]] = ..., includeRoot: bool = ..., irt: bool = ..., populateImportedAnimSources: Optional[Union[str, bool]] = ..., pia: Optional[Union[str, bool]] = ..., poseClip: bool = ..., poc: bool = ..., recursively: bool = ..., rec: bool = ..., removeSceneAnimation: bool = ..., rsa: bool = ..., showAnimSourceRemapping: bool = ..., sar: bool = ..., takeList: Optional[Union[str, bool]] = ..., tl: Optional[Union[str, bool]] = ..., takesToImport: Optional[Union[str, bool]] = ..., toi: Optional[Union[str, bool]] = ..., type: Optional[Union[str, bool]] = ..., typ: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command edits/queries Time Editor clips.

    Args:
        absolute | abs: (query) - This flag is used in conjunction with other timing flags like -s/start, -d/duration, -ed/end, etc. to query (global) absolute time.
        addAttribute | aa: (edit, multiuse) - Add new attribute to the clip.
        allowShrinking | eas: (edit) - When extending clip, allow shrinking.
        animSource | asr: (create, edit, query) - Populate based on animation source.
        audio | au: (create) - Create a clip with audio inside.
        blendMode | bm: (edit, query) - Set the blending mode for the clips specified with the -clipId flags:  0 : normal          - absolute blend 1 : additive        - relative blend
        children | chl: (query) - Get children clip IDs.
        clipAfter | ca: (query) - Get the clip ID of the next clip.
        clipBefore | cb: (query) - Get the clip ID of the previous clip.
        clipDataType | cdt: (query) - Query the type of data being driven by the given clip ID. Return values are:  0 : Animation       - Clip drives animation curves 1 : Audio           - Clip drives audio 3 : Group           - Clip is a group
        clipId | id: (create, edit, multiuse) - ID of the clip to be edited.
        clipIdFromNodeName | idn: (query) - Get clip ID from clip node name.
        clipIdFromPath | idp: (query) - Flag for querying the clip ID given the path. Clip path is a vertical-bar-delimited string to indicate a hierarchical structure of a clip. Please refer to the hierarchical path in outliner to see how it is represented. For example: composition1|track1|clip1 Note: To specify the path, this flag must appear before -query flag.
        clipNode | cln: (query) - Flag for querying the name of the clip node.
        clipPath | clp: (query) - Flag for querying the path given the clip ID. Clip path is a vertical bar delimited string to indicate a hierarchical structure of a clip. Please refer to the hierarchical path in outliner to see how it is represented. For example: composition1|track1|clip1. Note: If the clip is not connected to any track, it will return empty string.
        copyClip | ccl: (edit) - Get the selected clip IDs and store them in a list that could be used for pasting.
        crossfadeMode | cfm: (edit, query) - Set the crossfading mode between two clips that lie on the same track, and that are specified with the -clipId flags:  0 : linear          - Two clips are blended with a constant ratio 1 : step            - Left clip keeps its value until the middle of the crossfading region and then right clip's value is used 2 : hold left       - Use only left clip's value 3 : hold right      - Use only right clip's value 4 : custom          - User defined crossfade curve 5 : custom (spline) - User defined crossfade curve with spline preset
        crossfadePlug | cfp: (query) - Get plug path for a custom crossfade curve between 2 clips.
        curveTime | cvt: (query) - Query the curve local time in relation to the given clip.
        defaultGhostRoot | dgr: (edit, query) - Edit or query default ghost root variable. Determine whether to use the default ghost root (object driven by clip).
        drivenAttributes | dat: (query) - Return a list of attributes driven by a clip.
        drivenClipsBySource | dcs: (query) - Returns the clips driven by the given source. Can filter the return result by the specified type, like animCurve, expression, constraint, etc. This flag must come before the -query flag.
        drivenObjects | dos: (query) - Return an array of strings consisting of the names of all objects driven by the current clip and its children clips.
        drivenRootObjects | dro: (query) - Return an array of strings consisting of the names of all root objects driven by this clip and its children clips.
        drivingSources | dsc: (query) - Return all sources driving the given clip. Can filter the return result by the specified type, like animCurve, expression, constraint, etc. If used after the -query flag (without an argument), the command returns all sources driving the given clip. To specify the type, this flag must appear before the -query flag. 			In query mode, this flag can accept a value.
        duplicateClip | dcl: (edit) - Duplicate clip into two clips with the same timing info.
        duration | d: (create, query) - Relative duration of the new clip.
        emptySource | ems: (create) - Create a clip with an empty source.
        endTime | et: (query) - Query the relative end time of the clip.
        existingOnly | exo: (edit) - This flag can only be used in edit mode, in conjunction with the animSource flag. Retain the animSource flag functionality but only bind attributes that are already part of the clip. It does not attempt to populate unbound source attributes to their default destination.
        exists | exs: (query) - Return true if the specified clip exists.
        explode | epl: (edit) - Reparent all tracks and their clips within a group out to its parent track node and remove the group.
        exportAllClips | eac: (edit) - When used with the ef/exportFbx flag, export all clips.
        exportFbx | ef: (edit) - Export currently selected clips to FBX files.
        extend | ex: (edit) - Extend the clip to encompass all children.
        extendParent | exp: (edit) - Extend parent to fit this clip.
        ghost | gh: (edit, query) - Enable/disable ghosting for the specified clip.
        ghostRootAdd | gra: (edit, multiuse) - Add path to specified node as a custom ghost root.
        ghostRootRemove | grr: (edit, multiuse) - Remove path to specified node as a custom ghost root.
        group | grp: (create) - Specify if the new container should be created as a group, containing other specified clips.
        holdEnd | he: (edit, query) - Hold clip's end to time.
        holdStart | hs: (edit, query) - Hold clip's start to time.
        importTakeDestination | itd: (create) - Specify how to organize imported FBX takes: 0 - Import takes into a group (default) 1 - Import takes into multiple compositions 2 - Import takes as a sequence of clips
        isContainer | ict: (query) - Indicate if given clip ID is a container.
        listUserGhostRoot | lug: (query) - Get user defined ghost root object for indicated clips.
        loopEnd | le: (edit, query) - Loop clip's end to time.
        loopStart | ls: (edit, query) - Loop clip's start to time.
        minClipDuration | mcd: (query) - Returns the minimum allowed clip duration.
        modifyAnimSource | mas: (create, edit) - When populating, automatically modify Anim Source without asking the user.
        moveClip | mcl: (edit) - Move clip by adding delta to its start time.
        mute | m: (edit, query) - Mute/Unmute the clip given a clip ID. In query mode, return the muted state of the clip. Clips muted by soloing are not affected by this flag.
        name | n: (edit, query) - Name of the clip. A clip will never have an empty name. If an empty string is provided, it will be replaced with "_".
        parent | p: (edit) - Specify group/object parent ID.
        parentClipId | pid: (create, query) - Specify the parent clip ID of a clip to be created.
        parentGroupId | pgd: (query) - Return the parent group ID of the given clip.
        pasteClip | pcl: (edit) - Paste clip to the given time and track. Destination track is required to be specified through the track flag in the format "tracksNode:trackIndex". A trackIndex of -1 indicates that a new track will be created.
        path | pt: (edit, multiuse) - Full path of the clip to be edited. For example: composition1|track1|clip1. 			In query mode, this flag can accept a value.
        preserveAnimationTiming | pat: (create) - When used with the population command, it ensures the animation is offset within a clip in such way that it matches its original scene timing, regardless of the new clip's position.
        razorClip | rcl: (edit) - Razor clip into two clips at the specified time.
        remap | rmp: (edit) - Change animation source for a given clip item to a new one, specified by the target path. This removes all clips for the roster item and creates new clips from the Anim Source for the new target path.
        remapNamespace | rns: (create, multiuse) - Remap namespace(s). Can only be used in create mode, in conjunction with the -importFbx/fbx, -importMayaFile/mf, or -attribute/at flags. This flag will replace any occurrences of a given namespace to an alternate specified namespace.  It takes in two string arguments. The first argument specifies the namespace to replace. The second argument specifies the replacement namespace. This flag cannot be used in conjunction with the -sar/showAnimSourceRemapping flag. Note that a track must be specified, and  must exist prior to invoking the timeEditorClip command with the -remapNamespace flag.
        remapSource | rs: (edit) - Set animation source to be remapped for a given clip item to new one, specified by the target path.
        remappedSourceAttrs | rms: (query) - Return an array of attribute indices and names of the source attributes of a remapped clip.
        remappedTargetAttrs | rmt: (query) - Return an array of attribute indices and names of the target attributes of a remapped clip.
        removeAttribute | ra: (edit, multiuse) - Remove attribute from the clip.
        removeClip | rmc: (edit) - Remove clip of specified ID.
        removeCrossfade | rcf: (edit) - Remove custom crossfade between two clips specified by -clipId flags.
        removeWeightCurve | rwc: (create, edit, query) - Remove the weight curve connected to the clip.
        resetTiming | rt: (edit) - Reset start and duration of a clip with the given clip ID to the values stored in its Anim Source.
        resetTransition | rtr: (edit) - Reset transition intervals between specified clips.
        ripple | rpl: (edit) - Apply rippling to a clip operation.
        rootClipId | rti: (edit) - ID of the root clip. It is used together with various clip editing flags. When used, the effect of clip editing and its parameters will be affected by the given root clip. For example, moving a clip under the group root (usually in group tab view) will be performed in the local time space of the group root.
        rootPath | rpt: (edit) - Path of the root clip. It is used together with various clip editing flags. When used, the effect of clip editing and its parameters will be affected by the given root clip. For example, moving a clip under the group root (usually in group tab view) will be performed in the local time space of the group root.
        scaleEnd | sce: (edit) - Scale the end time of the clip to the given time.
        scalePivot | scp: (edit) - Scale the time of the clip based on the pivot. This should be used together with -scs/scaleStart or -sce/scaleEnd.
        scaleStart | scs: (edit) - Scale the start time of the clip to the given time.
        setKeyframe | k: (edit, multiuse) - Set keyframe on a specific clip for a specified attribute.
        speedRamping | src: (edit, query) - To control the playback speed of the clip by animation curve:  1 : create - Attach a speed curve and a time warp curve to the clip to control the playback speed 2 : edit - Open the Graph editor to edit the speed curve 3 : enable - Create a time warp curve from current speed curve and attach to clip 4 : disable - Remove the time warp curve from clip 5 : delete - Delete the attached speed curve and time warp curve 6 : reset - Reset the speed curve back to the default 7 : convert to speed curve from time warp 8 : convert to time warp from speed curve  In query mode, return true if a speed curve is attached to the clip.
        startTime | s: (create, query) - Relative start time of the new clip.
        timeWarp | tw: (query) - Return true if the clip is being warped by the speed curve. If no speed curve is attached to the clip, it will always return false.
        timeWarpCurve | twc: (query) - Returns the name of the time warp curve connected to the clip.
        timeWarpType | twt: (edit, query) - Time warp mode:  0: remapping - Connected time warp curve performs frame by frame remapping 1: speed curve - Connected time warp curve acts as a speed curve  In query mode, return time warp mode of a clip.
        track | trk: (create, edit, query) - The new clip container will be created on the track in the format "trackNode:trackNumber", or on a track path, for example "composition1|track1". In query mode, return a string containing the track number and tracks node of the given clip ID. In create mode, if the track number is '-1' or not given at all, then a new track will be created. For example: "trackNode:-1"; "composition1|".
        tracksNode | trn: (query) - Get tracks node if specified clip is a group clip.
        transition | tra: (edit) - Create transition intervals between specified clips.
        trimEnd | tre: (edit) - Trim the end time of the clip to the given time.
        trimStart | trs: (edit) - Trim the start time of the clip to the given time.
        truncated | trc: (query) - This flag is used in conjunction with other timing flags like -s/start, -d/duration, -ed/end, etc. to query (global) truncated time.
        uniqueAnimSource | uas: (edit) - If a given clip is sharing its Anim Source node with another clip, make the Anim Source of this clip unique.
        userGhostRoot | ugr: (edit, query) - Edit or query custom ghost root variable. Determine whether to use user defined ghost root.
        weightCurve | wc: (create, edit, query) - In edit mode, create a weight curve and connect it to the clip. In query mode, return the name of the weight curve connected to the clip.
        zeroKeying | zk: (edit) - A toggle flag to use in conjunction with k/setKeyframe, set the value of the key frame(s) to be keyed to zero.
        addObjects | ao: (create, edit, query) - Populate the given object(s) and their attributes to anim source to Time Editor. For multiple object, pass each name separated by semicolon. In query mode, return the number of attributes that will be populated given the flags, along with the animation's first and last frames for the given object(s). Similar to -addSelectedObjects flag but acts on given object(s) instead. This flag will override the flag -addSelectedObjects.
        addRelatedKG | akg: (create, edit, query) - During population, determine if associated keying groups should be populated or not. Normally used for populating HIK. By default the value is false.
        addSelectedObjects | aso: (create, edit, query) - Populate the currently selected objects and their attributes to anim source or Time Editor. In query mode, return the number of attributes that will be populated given the flags, along with the animation's first and last frames.
        attribute | at: (create, edit, multiuse) - Populate a specific attribute on a object.
        exclusive | exc: (create, edit) - Populate all types of animation sources which are not listed by "type" Flag.
        importAllFbxTakes | aft: (create) - Import all FBX takes into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).
        importFbx | fbx: (create) - Import an animation from FBX file into the new anim source (for timeEditorAnimSource command) or new container (for timeEditorClip command).
        importFbxTakes | ft: (create) - Import multiple FBX takes (separated by semicolons) into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).
        importMayaFile | mf: (create) - Import an animation from Maya file into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).
        importOption | io: (edit) - Option for importing animation source. Specify either 'connect' or 'generate'. connect:  Only connect with nodes already existing in the scene.                   Importing an animation source that does not match with any element                   of the current scene will not create any clip.                   (connect is the default mode). generate: Import everything and generate new nodes for items not existing in the scene.
        importPopulateOption | ipo: (edit) - Option for population when importing.
        importedContainerNames | icn: (create) - Internal use only. To be used along with populateImportedAnimSources to specify names for the created containers.
        includeRoot | irt: (create, edit) - Populate transform (Translate, Rotate, Scale) of hierarchy root nodes.
        populateImportedAnimSources | pia: (create) - Internal use only. Populate the Time Editor with clips using the Animation Sources specified (use ; as a delimiter for multiple anim sources).
        poseClip | poc: (create) - Populate as pose clip with current attribute values.
        recursively | rec: (create, edit) - Populate selection recursively, adding all the children.
        removeSceneAnimation | rsa: (create, edit) - If true, remove animation from scene when creating clips or anim sources. Only Time Editor will drive the removed scene animation.
        showAnimSourceRemapping | sar: (create) - Show a remapping dialog when the imported anim source attributes do not match the scene attributes.
        takeList | tl: (create) - Internal use only. To be used along with populateImportedAnimSources to specify the imported take names.
        takesToImport | toi: (create) - Internal use only. To be used along with populateImportedAnimSources to specify the imported take indices.
        type | typ: (create, edit, multiuse, query) - Only populate the specified type of animation source.
    """
    ...


def timeEditorClipLayer(*args, addAttribute: str = ..., aa: str = ..., addLayer: str = ..., al: str = ..., addObject: str = ..., ao: str = ..., allLayers: bool = ..., all: bool = ..., attribute: str = ..., a: str = ..., attributeKeyable: Optional[Union[str, bool]] = ..., ak: Optional[Union[str, bool]] = ..., clipId: int = ..., cid: int = ..., index: int = ..., idx: int = ..., keySiblings: bool = ..., ks: bool = ..., layerId: int = ..., lid: int = ..., layerName: Optional[Union[str, bool]] = ..., ln: Optional[Union[str, bool]] = ..., mode: int = ..., m: int = ..., mute: bool = ..., mu: bool = ..., name: bool = ..., n: bool = ..., path: str = ..., pt: str = ..., removeAttribute: str = ..., ra: str = ..., removeLayer: bool = ..., rl: bool = ..., removeObject: str = ..., ro: str = ..., resetSolo: bool = ..., rs: bool = ..., setKeyframe: bool = ..., k: bool = ..., solo: bool = ..., sl: bool = ..., zeroKeying: bool = ..., zk: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Time Editor clip layers commands

    Args:
        addAttribute | aa: (edit) - Add given plug to a layer with a supplied layerId.
        addLayer | al: (edit) - Add a new layer with a given name.
        addObject | ao: (edit) - Add given object with all its attributes in the clip to a layer with a supplied layerId.
        allLayers | all: (query) - Return all layers given clip ID.
        attribute | a: (edit, multiuse) - The attribute path to key.
        attributeKeyable | ak: (query) - Return whether specified attribute is keyable.
        clipId | cid: (edit) - ID of the clip this layer command operates on. 			In query mode, this flag can accept a value.
        index | idx: (edit) - Layer index, used when adding new layer at specific location in the stack.
        keySiblings | ks: (edit) - If set to true, additional attributes might be keyed while keying to achieve desired result.
        layerId | lid: (edit) - Layer ID used in conjunction with other edit flags. 			In query mode, this flag can accept a value.
        layerName | ln: (edit, query) - Edit layer name. In query mode, return the layer name given its layer ID and clip ID.
        mode | m: (edit) - To control the playback speed of the clip by animation curve:  0 : additive 1 : additive override 2 : override 3 : override passthrough
        mute | mu: (edit) - Mute/unmute a layer given its layer ID and clip ID.
        name | n: (query) - Query the attribute name of a layer given its layer ID and clip ID.
        path | pt: (edit) - Full path of a layer or a clip on which to operate. For example: composition1|track1|clip1|layer1; composition1|track1|group|track1|clip1. 			In query mode, this flag can accept a value.
        removeAttribute | ra: (edit) - Remove given plug from a layer with a supplied layerId.
        removeLayer | rl: (edit) - Remove layer with an ID.
        removeObject | ro: (edit) - Remove given object with all its attributes in the clip to a layer with a supplied layerId.
        resetSolo | rs: (edit) - Unsolo all soloed layers in a given clip ID.
        setKeyframe | k: (edit) - Set keyframe on specified attributes on specified layer of a clip. Use -clipId to indicate the specified clip. Use -layerId to indicate the specified layer of the clip. Use -attribute to indicate the specified attributes (if no attribute flag is used, all attribute will be keyed). Use -zeroKeying to indicate that zero offset from original animation should be keyed.
        solo | sl: (edit) - Solo/unsolo a layer given its layers ID and clip ID.
        zeroKeying | zk: (edit) - Indicate if the key to set should be zero offset from original animation.
    """
    ...


def timeEditorClipOffset(*args, applyToAllRoots: bool = ..., atr: bool = ..., clipId: Optional[Union[int, bool]] = ..., id: Optional[Union[int, bool]] = ..., matchClipId: Optional[Union[int, bool]] = ..., mci: Optional[Union[int, bool]] = ..., matchDstTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., mdt: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., matchObj: Optional[Union[str, bool]] = ..., mob: Optional[Union[str, bool]] = ..., matchOffsetRot: bool = ..., mor: bool = ..., matchOffsetTrans: bool = ..., mot: bool = ..., matchPath: Optional[Union[str, bool]] = ..., mpt: Optional[Union[str, bool]] = ..., matchRotOp: Optional[Union[int, bool]] = ..., mro: Optional[Union[int, bool]] = ..., matchSrcTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., mst: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., matchTransOp: Optional[Union[int, bool]] = ..., mto: Optional[Union[int, bool]] = ..., offsetTransform: bool = ..., oft: bool = ..., path: Optional[Union[str, bool]] = ..., pt: Optional[Union[str, bool]] = ..., resetMatch: Optional[Union[int, bool]] = ..., rsm: Optional[Union[int, bool]] = ..., resetMatchPath: Optional[Union[str, bool]] = ..., rmp: Optional[Union[str, bool]] = ..., rootObj: Optional[Union[str, bool]] = ..., rob: Optional[Union[str, bool]] = ..., upVectorX: Optional[Union[float, bool]] = ..., upx: Optional[Union[float, bool]] = ..., upVectorY: Optional[Union[float, bool]] = ..., upy: Optional[Union[float, bool]] = ..., upVectorZ: Optional[Union[float, bool]] = ..., upz: Optional[Union[float, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to compute an offset to apply on a source clip in order to
    automatically align it to a destination clip at a specified match element.
    For this command to work, offset objects must be specified for the character.

    Args:
        applyToAllRoots | atr: (create) - Apply root offsets to all roots in the population. However, if the root objects are specified by rootObj flag, this flag will be ignored.
        clipId | id: (create, edit, multiuse) - ID of the clip to be edited.
        matchClipId | mci: (create) - Specify the ID of a clip to match.
        matchDstTime | mdt: (create) - Specify the time on target clip.
        matchObj | mob: (create) - Specify the object to match.
        matchOffsetRot | mor: (query) - Get the rotation of the match offset matrix.
        matchOffsetTrans | mot: (query) - Get the translation of the match offset matrix.
        matchPath | mpt: (create) - Full path of the clip to match. For example: composition1|track1|Group|track2|clip1
        matchRotOp | mro: (create) - Specify the option for matching rotation.  0 : full - All rotation components are matched 1 : Y    - Y component is matched 2 : none - No rotation matching
        matchSrcTime | mst: (create) - Specify the time on source clip.
        matchTransOp | mto: (create) - Specify the option for matching translation.  0 : full - All translation components are matched 1 : XZ   - X and Z components are matched 2 : none - No translation matching
        offsetTransform | oft: (create, query) - Create/get an offset for the specified clip.
        path | pt: (create, edit, multiuse) - Full path of a clip to be edited. For example: composition1|track1|group; composition1|track1|group|track2|clip1. 			In query mode, this flag can accept a value.
        resetMatch | rsm: (create) - Specify clip ID to remove offset.
        resetMatchPath | rmp: (create) - Specify clip's full path to remove offset. For example: composition1|track1|Group|track2|clip1
        rootObj | rob: (create, edit, multiuse, query) - Specify the root objects. If specified, this flag will take precedence over applyToAllRoots flag. When used in query mode, returns list of roots defined for the relocator.
        upVectorX | upx: (create) - Specify the X coordinate of the up vector.
        upVectorY | upy: (create) - Specify the Y coordinate of the up vector.
        upVectorZ | upz: (create) - Specify the Z coordinate of the up vector.
    """
    ...


def timeEditorComposition(*args, active: bool = ..., act: bool = ..., allCompositions: bool = ..., acp: bool = ..., createTrack: bool = ..., ct: bool = ..., delete: bool = ..., duplicateFrom: Optional[Union[str, bool]] = ..., df: Optional[Union[str, bool]] = ..., rename: Tuple[str, str] = ..., ren: Tuple[str, str] = ..., tracksNode: bool = ..., tn: bool = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Commands related to composition management inside Time Editor.

    Args:
        active | act: (edit, query) - Query or edit the active composition.
        allCompositions | acp: (query) - Return all compositions inside Time Editor.
        createTrack | ct: (create) - Create a default track when creating a new composition.
        delete | delete: (edit, query) - Delete the composition.
        duplicateFrom | df: (create) - Duplicate the composition.
        rename | ren: (edit) - Rename the composition of the first name to the second name.
        tracksNode | tn: (query) - Query the tracks node of a composition.
    """
    ...


def timeEditorPanel(*args, activeClipEditMode: Optional[Union[int, bool]] = ..., ace: Optional[Union[int, bool]] = ..., activeTabRootClipId: bool = ..., atr: bool = ..., activeTabTime: bool = ..., att: bool = ..., activeTabView: Optional[Union[int, bool]] = ..., atv: Optional[Union[int, bool]] = ..., autoFit: Optional[Union[str, bool]] = ..., af: Optional[Union[str, bool]] = ..., autoFitTime: Optional[Union[str, bool]] = ..., aft: Optional[Union[str, bool]] = ..., control: bool = ..., ctl: bool = ..., defineTemplate: Optional[Union[str, bool]] = ..., dt: Optional[Union[str, bool]] = ..., displayActiveKeyTangents: str = ..., dat: str = ..., displayActiveKeys: str = ..., dak: str = ..., displayInfinities: str = ..., di: str = ..., displayKeys: str = ..., dk: str = ..., displayTangents: str = ..., dtn: str = ..., displayValues: str = ..., dv: str = ..., docTag: Optional[Union[str, bool]] = ..., dtg: Optional[Union[str, bool]] = ..., exists: bool = ..., ex: bool = ..., filter: Optional[Union[str, bool]] = ..., f: Optional[Union[str, bool]] = ..., forceMainConnection: Optional[Union[str, bool]] = ..., fmc: Optional[Union[str, bool]] = ..., groupIdForTabView: Optional[Union[int, bool]] = ..., gtv: Optional[Union[int, bool]] = ..., highlightConnection: Optional[Union[str, bool]] = ..., hlc: Optional[Union[str, bool]] = ..., keyingTarget: Optional[Union[int, bool]] = ..., kt: Optional[Union[int, bool]] = ..., layerId: int = ..., l: int = ..., lockMainConnection: bool = ..., lck: bool = ..., lookAt: str = ..., la: str = ..., mainListConnection: Optional[Union[str, bool]] = ..., mlc: Optional[Union[str, bool]] = ..., menu: Optional[Union[str, bool]] = ..., m: Optional[Union[str, bool]] = ..., minClipWidth: Optional[Union[int, bool]] = ..., mcw: Optional[Union[int, bool]] = ..., panel: Optional[Union[str, bool]] = ..., pnl: Optional[Union[str, bool]] = ..., parent: Optional[Union[str, bool]] = ..., p: Optional[Union[str, bool]] = ..., selectionConnection: Optional[Union[str, bool]] = ..., slc: Optional[Union[str, bool]] = ..., setToPrevClipEditMode: bool = ..., spe: bool = ..., snapTime: Optional[Union[str, bool]] = ..., st: Optional[Union[str, bool]] = ..., snapToClip: bool = ..., stc: bool = ..., snapToFrame: bool = ..., stf: bool = ..., snapTolerance: Optional[Union[int, bool]] = ..., sto: Optional[Union[int, bool]] = ..., snapValue: Optional[Union[str, bool]] = ..., sv: Optional[Union[str, bool]] = ..., stateString: bool = ..., sts: bool = ..., tabView: int = ..., tv: int = ..., timeCursor: bool = ..., tc: bool = ..., unParent: bool = ..., up: bool = ..., unlockMainConnection: bool = ..., ulk: bool = ..., updateMainConnection: bool = ..., upd: bool = ..., useTemplate: Optional[Union[str, bool]] = ..., ut: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Time Editor - non-linear animation editor

    Args:
        activeClipEditMode | ace: (edit, query) - Set the appropriate clip edit mode for the editor.  0: Default Mode 1: Trim Mode 2: Scale Mode 3: Loop Mode 4: Hold Mode
        activeTabRootClipId | atr: (query) - Get the clip id for which current active tab has been opened. In case of main tab, this will return -1 meaning there is no root clip.
        activeTabTime | att: (query) - Get current time displayed inside the active tab. This will be global time in case of the main tab and local time for others.
        activeTabView | atv: (edit, query) - Get/set the index of the tab widget's (active) visible tab. Note: the index is zero-based.
        autoFit | af: (edit, query) - on | off | tgl Auto fit-to-view.
        autoFitTime | aft: (edit, query) - on | off | tgl Auto fit-to-view along the time axis, as well.
        control | ctl: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        defineTemplate | dt: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        displayActiveKeyTangents | dat: (edit) - on | off | tgl Display active key tangents in the editor.
        displayActiveKeys | dak: (edit) - on | off | tgl Display active keys in the editor.
        displayInfinities | di: (edit) - on | off | tgl Display infinities in the editor.
        displayKeys | dk: (edit) - on | off | tgl Display keyframes in the editor.
        displayTangents | dtn: (edit) - on | off | tgl Display tangents in the editor.
        displayValues | dv: (edit) - on | off | tgl Display active keys and tangents values in the editor.
        docTag | dtg: (create, edit, query) - Attaches a tag to the editor.
        exists | ex: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        filter | f: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        forceMainConnection | fmc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        groupIdForTabView | gtv: (query) - Get the group clip id for the given tab view index. To specify the tab index, this flag must appear before the -query flag.       In query mode, this flag needs a value.
        highlightConnection | hlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        keyingTarget | kt: (edit, query) - Set keying target to specified clip ID. If keying into layer, '-layer' flag must be used. In query mode, the clip id is omitted, and the name of the keying target will be returned.
        layerId | l: (edit) - Indicate layer ID of keying target.
        lockMainConnection | lck: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        lookAt | la: (edit) - all | selected | currentTime FitView helpers.
        mainListConnection | mlc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        menu | m: (create) - Specify a script to be run when the editor is created.  The function will be passed one string argument which is the new editor's name.
        minClipWidth | mcw: (edit, query) - Set the minimum clip width.
        panel | pnl: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent | p: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        selectionConnection | slc: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        setToPrevClipEditMode | spe: (edit) - Revert to previous clip edit mode.
        snapTime | st: (edit, query) - none | integer | keyframe Keyframe move snap in time.
        snapToClip | stc: (edit, query) - Enable/Disable snap-to-clip option in Time Editor while manipulating and drag-and-drop clips. When snapToClip is on all manipulated timing will land on a clip boundary if it is close to it.
        snapToFrame | stf: (edit, query) - Enable/Disable snap-to-frame option in Time Editor while manipulating and drag-and-drop clips. When snapToFrame is on all manipulated timing will land on an exact frame.
        snapTolerance | sto: (edit, query) - Set the tolerance value for snapping.
        snapValue | sv: (edit, query) - none | integer | keyframe Keyframe move snap in values.
        stateString | sts: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        tabView | tv: (edit) - Create a tab view for the given group clip ID.
        timeCursor | tc: (edit, query) - Activate the time cursor in Time Editor for scrubbing.
        unParent | up: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        unlockMainConnection | ulk: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection | upd: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useTemplate | ut: (create) - Forces the command to use a command template other than the current one.
    """
    ...


def timeEditorTracks(*args, activeClipWeight: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., acw: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., activeClipWeightId: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., aci: Optional[Union[Union[float, Tuple[float, float]], bool]] = ..., addTrack: int = ..., at: int = ..., allClips: bool = ..., ac: bool = ..., allTracks: bool = ..., atc: bool = ..., allTracksRecursive: bool = ..., atr: bool = ..., composition: bool = ..., cp: bool = ..., path: str = ..., pt: str = ..., plugIndex: Optional[Union[int, bool]] = ..., pi: Optional[Union[int, bool]] = ..., removeTrack: int = ..., rt: int = ..., removeTrackByPath: str = ..., rtp: str = ..., reorderTrack: Tuple[int, int] = ..., rot: Tuple[int, int] = ..., resetMute: bool = ..., rm: bool = ..., resetSolo: bool = ..., rs: bool = ..., selectedTracks: bool = ..., st: bool = ..., trackGhost: bool = ..., tgh: bool = ..., trackIndex: Optional[Union[int, bool]] = ..., ti: Optional[Union[int, bool]] = ..., trackMuted: bool = ..., tm: bool = ..., trackName: Optional[Union[str, bool]] = ..., tn: Optional[Union[str, bool]] = ..., trackSolo: bool = ..., ts: bool = ..., trackType: Optional[Union[int, bool]] = ..., tt: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Time Editor tracks commands

    Args:
        activeClipWeight | acw: (query) - Get the clip weight at the specified time.
        activeClipWeightId | aci: (query) - Get the clip ID carrying the active clip weight at the specified time.
        addTrack | at: (edit) - Add new track at the track index specified. Indices are 0-based. Specify -1 to add the track at the end.
        allClips | ac: (query) - Return a list of clip IDs under the specified track.
        allTracks | atc: (query) - Return a list of strings for all the immediate tracks for the given tracks node in the format "tracksNode:trackIndex".
        allTracksRecursive | atr: (query) - Return a list of strings for all the tracks for the given tracks node, or return a list of strings for all tracks of all tracks nodes in the format "tracksNode:trackIndex". If the given root tracks node is from a composition, this command returns the tracks under that composition, including the tracks within groups that is under the same composition.
        composition | cp: (query) - Return the composition the specified track belongs to.
        path | pt: (edit) - Full path of a track node or a track on which to operate. For example: composition1|track1|group; composition1|track1. 			In query mode, this flag can accept a value.
        plugIndex | pi: (edit, query) - Get the plug index of the specified track.
        removeTrack | rt: (edit, multiuse) - Remove track at given index. It is a multi-use flag.
        removeTrackByPath | rtp: (edit, multiuse) - Remove track at given path. It is a multi-use flag. For example: composition1|track1|group|track1;
        reorderTrack | rot: (edit) - Move the track relative to other tracks. The first argument is the track index (0-based). The second argument can be a positive or negative number to indicate the steps to move. Positive numbers move forward and negative numbers move backward.
        resetMute | rm: (create) - Reset all the muted tracks in the active composition.
        resetSolo | rs: (create) - Reset the soloing of all tracks on the active composition.
        selectedTracks | st: (query) - Return a list of the indices for all the selected tracks for the given tracks node, or return a list of strings for all selected tracks of all tracks nodes in the format "tracksNode:trackIndex".
        trackGhost | tgh: (edit, query) - Ghost all clips under track.
        trackIndex | ti: (edit, query) - Specify the track index. This flag is used in conjunction with the other flags. 			In query mode, this flag can accept a value.
        trackMuted | tm: (edit, query) - Return whether the track is muted.
        trackName | tn: (edit, query) - Display name of the track.
        trackSolo | ts: (edit, query) - Return whether the track is soloed.
        trackType | tt: (edit, query) - Specify the track type. Can only be used together with -at/addTrack. Does not work by itself. In query mode, return the integer corresponding to the track type.   0: Animation Track (Default)  1: Audio Track
    """
    ...


def timeWarp(*args, deleteFrame: int = ..., df: int = ..., frame: Optional[Union[float, bool]] = ..., f: Optional[Union[float, bool]] = ..., g: bool = ..., interpType: Optional[Union[Tuple[int, str], bool]] = ..., it: Optional[Union[Tuple[int, str], bool]] = ..., moveFrame: Optional[Union[Tuple[int, float], bool]] = ..., mf: Optional[Union[Tuple[int, float], bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command is used to create a time warp input to a set of animation curves.

    Args:
        deleteFrame | df: (edit) - The flag value indicates the 0-based index of the warp frame to delete. This flag can only be used in edit mode.
        frame | f: (create, edit, multiuse, query) - In create and edit mode, this flag can be used to specify warp frames added to the warp operation. In query mode, this flag returns a list of the frame values where warping occurs. The moveFrame flag command can be used to query the associated warped values.
        g | g: (create, edit, query) - In create mode, creates a global time warp node which impacts every animated object in the scene. In query mode, returns the global time warp node. Note: only one global time warp can exist in the scene.
        interpType | it: (create, edit, query) - This flag can be used to set the interpolation type for a given span. Valid interpolation types are linear, easeIn and easeOut. When queried, it returns a string array of the interpolation types for the specified time warp.
        moveFrame | mf: (edit, query) - This flag can be used to move a singular warp frame. The first value specified indicates the 0-based index of the warp frame to move. The second value indicates the new warp frame value. This flag can only be used in edit and query mode. When queried, it returns an array of the warped frame values.
    """
    ...


def ubercam(*args) -> Any:
    r"""
    Use this command to create a "ubercam" with equivalent behavior
    to all cameras used by shots in the sequencer.

    Args:
    """
    ...


def volumeBind(*args, influence: Optional[Union[str, bool]] = ..., inf: Optional[Union[str, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    Command for creating and editing volume binding nodes.
    The node is use for storing volume data to define skin weighting data.

    Args:
        influence | inf: (edit, query) - Edit or Query the list of influences connected to the skin cluster.
        name | n: (create) - Used to specify the name of the node being created.
    """
    ...


def wire(*args, after: bool = ..., af: bool = ..., afterReference: bool = ..., ar: bool = ..., before: bool = ..., bf: bool = ..., components: bool = ..., cmp: bool = ..., crossingEffect: Optional[Union[float, bool]] = ..., ce: Optional[Union[float, bool]] = ..., deformerTools: bool = ..., dt: bool = ..., dropoffDistance: Optional[Union[Tuple[int, float], bool]] = ..., dds: Optional[Union[Tuple[int, float], bool]] = ..., envelope: Optional[Union[float, bool]] = ..., en: Optional[Union[float, bool]] = ..., exclusive: Optional[Union[str, bool]] = ..., ex: Optional[Union[str, bool]] = ..., frontOfChain: bool = ..., foc: bool = ..., geometry: Optional[Union[str, bool]] = ..., g: Optional[Union[str, bool]] = ..., geometryIndices: bool = ..., gi: bool = ..., groupWithBase: bool = ..., gw: bool = ..., holder: Optional[Union[Tuple[int, str], bool]] = ..., ho: Optional[Union[Tuple[int, str], bool]] = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., ihs: bool = ..., localInfluence: Optional[Union[float, bool]] = ..., li: Optional[Union[float, bool]] = ..., name: Optional[Union[str, bool]] = ..., n: Optional[Union[str, bool]] = ..., parallel: bool = ..., par: bool = ..., prune: bool = ..., pr: bool = ..., remove: bool = ..., rm: bool = ..., selectedComponents: bool = ..., cms: bool = ..., split: bool = ..., sp: bool = ..., useComponentTags: bool = ..., uct: bool = ..., wire: Optional[Union[str, bool]] = ..., w: Optional[Union[str, bool]] = ..., wireCount: Optional[Union[int, bool]] = ..., wc: Optional[Union[int, bool]] = ..., edit: bool = ..., query: bool = ...) -> Any:
    r"""
    This command creates a wire deformer. 
    In the create mode the selection list is treated as the
    object(s) to be deformed, Wires are specified with the -w flag.
    Each wire can optionally have a holder which helps define the
    the regon of the object that is affected by the deformer.

    Args:
        after | af: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        afterReference | ar: (create, edit) - The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then the -after mode is used when adding the new deformer, otherwise the -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
        before | bf: (create, edit) - If the default behavior for insertion/appending into/onto the existing chain is not the desired behavior then this flag can be used to force the command to place the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
        components | cmp: (query) - Returns the components used by the deformer
        crossingEffect | ce: (create, edit, query) - Set the amount of convolution effect. Varies from fully convolved at 0 to a simple additive effect at 1 (which is what you get with the filter off). Default is 0.  This filter should make its way into all blend nodes that deal with combining effects from multiple sources.
        deformerTools | dt: (query) - Returns the name of the deformer tool objects (if any) as string string ...
        dropoffDistance | dds: (create, edit, multiuse, query) - Set the dropoff distance (second parameter) for the wire at index (first parameter).
        envelope | en: (create, edit, query) - Set the envelope value for the deformer. Default is 1.0
        exclusive | ex: (create, query) - Puts the deformation set in a deform partition.
        frontOfChain | foc: (create, edit) - This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
        geometry | g: (edit, multiuse, query) - The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
        geometryIndices | gi: (query) - Complements the -geometry flag in query mode. Returns the multi index of each geometry.
        groupWithBase | gw: (create) - Groups the wire with the base wire so that they can easily be moved together to create a ripple effect. Default is false.
        holder | ho: (create, edit, multiuse, query) - Set the specified curve or surface (second parameter  as a holder for the wire at index (first parameter).
        ignoreSelected | ignoreSelected: (create) - Tells the command to not deform objects on the current selection list
        includeHiddenSelections | ihs: (create) - Apply the deformer to any visible and hidden objects in the selection list. Default is false.
        localInfluence | li: (create, edit, query) - Set the local control a wire has with respect to other wires irrespective of whether it is deforming the surface. Varies from no local effect at 0 to full local control at 1. Default is 0.
        name | n: (create) - Used to specify the name of the node being created.
        parallel | par: (create, edit) - Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
        prune | pr: (edit) - Removes any points not being deformed by the deformer in its current configuration from the deformer set.
        remove | rm: (edit, multiuse) - Specifies that objects listed after the -g flag should be removed from this deformer.
        selectedComponents | cms: (query) - Returns the components used by the deformer that are currently selected. This intersects the current selection with the components affected by the deformer.
        split | sp: (create, edit) - Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
        useComponentTags | uct: (create) - When this flag is specified a setup using componentTags will be created. This means no groupId, groupParts, tweak or objectSet nodes will be created and connected to the new deformer.
        wire | w: (create, edit, multiuse, query) - Specify or query the wire curve name.
        wireCount | wc: (create, edit, query) - Set the number of wires.
    """
    ...


def wrinkle(*args, axis: Optional[Union[Tuple[float, float, float], bool]] = ..., ax: Optional[Union[Tuple[float, float, float], bool]] = ..., branchCount: Optional[Union[int, bool]] = ..., brc: Optional[Union[int, bool]] = ..., branchDepth: Optional[Union[int, bool]] = ..., bd: Optional[Union[int, bool]] = ..., center: Optional[Union[Tuple[float, float, float], bool]] = ..., ct: Optional[Union[Tuple[float, float, float], bool]] = ..., crease: Optional[Union[str, bool]] = ..., cr: Optional[Union[str, bool]] = ..., dropoffDistance: Optional[Union[float, bool]] = ..., dds: Optional[Union[float, bool]] = ..., envelope: Optional[Union[float, bool]] = ..., en: Optional[Union[float, bool]] = ..., randomness: Optional[Union[float, bool]] = ..., rnd: Optional[Union[float, bool]] = ..., style: Optional[Union[str, bool]] = ..., st: Optional[Union[str, bool]] = ..., thickness: Optional[Union[float, bool]] = ..., th: Optional[Union[float, bool]] = ..., uvSpace: Optional[Union[Tuple[float, float, float, float, float], bool]] = ..., uv: Optional[Union[Tuple[float, float, float, float, float], bool]] = ..., wrinkleCount: Optional[Union[int, bool]] = ..., wc: Optional[Union[int, bool]] = ..., wrinkleIntensity: Optional[Union[float, bool]] = ..., wi: Optional[Union[float, bool]] = ...) -> Any:
    r"""
    The wrinkle command is used to create a network of wrinkles on a surface.
    It automatically creates a network of wrinkle curves that control a wire
    deformer. The wrinkle curves are attached to a cluster deformer.

    Args:
        axis | ax: (create) - Specifies the plane of the wrinkle.
        branchCount | brc: (create) - Specifies the number of branches per wrinkle. Default is 2.
        branchDepth | bd: (create) - Specifies the depth of the branching. Default is 0.
        center | ct: (create) - Specifies the center of the wrinkle.
        crease | cr: (create, multiuse) - Specifies an existing curve to serve as the wrinkle.
        dropoffDistance | dds: (create) - Specifies the dropoff distance around the center.
        envelope | en: (create) - The envelope globally attenuates the amount of deformation. Default is 1.0.
        randomness | rnd: (create) - Amount of randomness. Default is 0.2.
        style | st: (create) - Specifies the wrinkle style. Valid values are "radial" or "tangential"
        thickness | th: (create) - Wrinkle thickness. Default is 1.0.
        uvSpace | uv: (create) - 1/2 length, 1/2 breadth, rotation angle, center u, v definition of a patch in uv space where the wrinkle is to be constructed.
        wrinkleCount | wc: (create) - Specifies the number of wrinkle lines to be generated. Default is 3.
        wrinkleIntensity | wi: (create) - Increasing the intensity makes it more wrinkly. Default is 0.5.
    """
    ...


def writeTake(*args, angle: Optional[Union[str, bool]] = ..., a: Optional[Union[str, bool]] = ..., device: Optional[Union[str, bool]] = ..., d: Optional[Union[str, bool]] = ..., linear: Optional[Union[str, bool]] = ..., l: Optional[Union[str, bool]] = ..., noTime: bool = ..., nt: bool = ..., precision: Optional[Union[int, bool]] = ..., pre: Optional[Union[int, bool]] = ..., take: Optional[Union[str, bool]] = ..., t: Optional[Union[str, bool]] = ..., virtualDevice: Optional[Union[str, bool]] = ..., vd: Optional[Union[str, bool]] = ...) -> Any:
    r"""
    This action writes a take from a device with recorded data to a
    take (.mov) file. The writeTake action can also write the virtual
    definition of a device.
    
    See also: recordDevice, readTake, defineVirtualDevice

    Args:
        angle | a: (create) - Sets the angular unit used in the take. Valid strings are [deg|degree|rad|radian].  C: The default is the current user angular unit.
        device | d: (create) - Specifies the device that contains the take. This is a required argument. If the device does not contain a take, the action will fail.
        linear | l: (create) - Sets the linear unit used in the take. Valid strings are [mm|millimeter|cm|centimeter|m|meter|km|kilometer|in|inch|ft|foot|yd|yard|mi|mile]  C: The default is the current user linear unit.
        noTime | nt: (create) - The take (.mov) file will not contain time stamps.  C: The default is to put time stamps in the take file.
        precision | pre: (create) - Sets the number of digits to the right of the decimal place in the take file. C: The default is 6.
        take | t: (create) - Write out the take to a file with the specified name.
        virtualDevice | vd: (create) - Writes out the virtual device definition to a mel script with the specified file name.
    """
    ...


