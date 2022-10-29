from enum import IntEnum, auto


class Connection(IntEnum):
    SERIAL = auto()
    NETWORK = auto()


class TemperatureUnits(IntEnum):
    NA = -1
    F = 0
    C = 1
    K = 2


class PressureUnits(IntEnum):
    NA = -1
    PSI = 0
    BAR = 1
    KPA = 2


class OperatingState(IntEnum):
    NA = -1
    IDLING = 0
    STARTING = 2
    RUNNING = 3
    STOPPING = 5
    ERROR_LOCKOUT = 6
    ERROR = 7
    HELIUM_COOLDOWN = 8
    POWER_ERROR = 9
    RECOVERED_FROM_ERROR = 15


class Warnings(IntEnum):
    NO_WARNINGS = 0
    COOLANT_IN_HIGH = 1
    COOLANT_IN_LOW = 2
    COOLANT_OUT_HIGH = 4
    COOLANT_OUT_LOW = 8
    OIL_HIGH = 16
    OIL_LOW = 32
    HELIUM_HIGH = 64
    HELIUM_LOW = 128
    LOW_PRESSURE_HIGH = 256
    LOW_PRESSURE_LOW = 512
    HIGH_PRESSURE_HIGH = 1024
    HIGH_PRESSURE_LOW = 2048
    DELTA_PRESSURE_HIGH = 4096
    DELTA_PRESSURE_LOW = 8192
    STATIC_PRESSURE_HIGH = 131072
    STATIC_PRESSURE_LOW = 262144
    COLD_HEAD_MOTOR_STALL = 524288


class Errors(IntEnum):
    NO_WARNINGS = 0
    COOLANT_IN_HIGH = 1
    COOLANT_IN_LOW = 2
    COOLANT_OUT_HIGH = 4
    COOLANT_OUT_LOW = 8
    OIL_HIGH = 16
    OIL_LOW = 32
    HELIUM_HIGH = 64
    HELIUM_LOW = 128
    LOW_PRESSURE_HIGH = 256
    LOW_PRESSURE_LOW = 512
    HIGH_PRESSURE_HIGH = 1024
    HIGH_PRESSURE_LOW = 2048
    DELTA_PRESSURE_HIGH = 4096
    DELTA_PRESSURE_LOW = 8192
    MOTOR_CURRENT_LOW = 16384
    THREE_PHASE_ERROR = 32768
    STATIC_PRESSURE_HIGH = 131072
    STATIC_PRESSURE_LOW = 262144