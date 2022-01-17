import pyzed.sl as sl

OBJECT_DETECTED_STARTING_FROM_PERCENT = 40
CONFIDENCE_THRESHOLD = 50
MAXIMUM_DISTANCE_IN_METERS = 30
MEASUREMENTS_PER_SECOND = 15
ACCURACY = 5


class zed2():

    zed = None
    init_params = None

    def __init__(self):
        self.zed = sl.Camera()

        self.init_params = sl.InitParameters()
        self.init_params.camera_resolution = sl.RESOLUTION.HD1080
        self.init_params.camera_fps = MEASUREMENTS_PER_SECOND
        self.init_params.coordinate_units = sl.UNIT.METER
        self.init_params.coordinate_system = sl.COORDINATE_SYSTEM.RIGHT_HANDED_Y_UP
        self.init_params.depth_mode = sl.DEPTH_MODE.ULTRA
        self.init_params.depth_maximum_distance = MAXIMUM_DISTANCE_IN_METERS


    def clean_up(self):
        self.zed.disable_object_detection()
        self.zed.disable_positional_tracking()
        self.zed.close()


    def start(self):
        status = self.zed.open(self.init_params)
        if status != sl.ERROR_CODE.SUCCESS:
            print(repr(status))
            exit()

        # Enable positional tracking module
        positional_tracking_parameters = sl.PositionalTrackingParameters()

        # If the camera is static in space, enabling this setting below provides better depth quality and faster computation
        positional_tracking_parameters.set_as_static = True
        self.zed.enable_positional_tracking(positional_tracking_parameters)

        obj_param = sl.ObjectDetectionParameters()
        obj_param.detection_model = sl.DETECTION_MODEL.MULTI_CLASS_BOX_ACCURATE
        obj_param.enable_tracking = True
        self.zed.enable_object_detection(obj_param)

        obj_runtime_param = sl.ObjectDetectionRuntimeParameters()
        obj_runtime_param.detection_confidence_threshold = OBJECT_DETECTED_STARTING_FROM_PERCENT
        obj_runtime_param.object_class_filter = [sl.OBJECT_CLASS.PERSON]

        runtime_params = sl.RuntimeParameters()
        runtime_params.confidence_threshold = CONFIDENCE_THRESHOLD

        objects = sl.Objects()

        self.run(objects, obj_runtime_param, runtime_params)

        self.clean_up()

    def run(self, objects, obj_runtime_param, runtime_params):
        while(1):
            if self.zed.grab(runtime_params) == sl.ERROR_CODE.SUCCESS:
                    returned_state = self.zed.retrieve_objects(objects, obj_runtime_param)

                    if (returned_state == sl.ERROR_CODE.SUCCESS and objects.is_new):
                        obj_array = objects.object_list
                        # Write into SQLlite Database
                        print(obj_array)