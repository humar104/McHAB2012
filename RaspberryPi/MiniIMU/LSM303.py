import Adafruit_I2C



class LSM303:
    #I2C addresses for LSM303
    __ACCEL_ADDRESS = 0x32
    __MAG_ADDRESS = 0xd3

    # device types

    __LSM303DLH_DEVICE = 0
    __LSM303DLM_DEVICE = 1
    __LSM303DLHC_DEVICE = 2
    __LSM303_DEVICE_AUTO = 3

    # SA0_A states

    _LSM303_SA0_A_LOW 0
    _LSM303_SA0_A_HIGH 1
    _LSM303_SA0_A_AUTO 2

    # register addresses

    _LSM303_CTRL_REG1_A 0x20
    _LSM303_CTRL_REG2_A 0x21
    _LSM303_CTRL_REG3_A 0x22
    _LSM303_CTRL_REG4_A 0x23
    _LSM303_CTRL_REG5_A 0x24
    _LSM303_CTRL_REG6_A 0x25 # DLHC only
    _LSM303_HP_FILTER_RESET_A 0x25 # DLH, DLM only
    _LSM303_REFERENCE_A 0x26
    _LSM303_STATUS_REG_A 0x27

    _LSM303_OUT_X_L_A 0x28
    _LSM303_OUT_X_H_A 0x29
    _LSM303_OUT_Y_L_A 0x2A
    _LSM303_OUT_Y_H_A 0x2B
    _LSM303_OUT_Z_L_A 0x2C
    _LSM303_OUT_Z_H_A 0x2D

    _LSM303_FIFO_CTRL_REG_A 0x2E # DLHC only
    _LSM303_FIFO_SRC_REG_A 0x2F # DLHC only

    _LSM303_INT1_CFG_A 0x30
    _LSM303_INT1_SRC_A 0x31
    _LSM303_INT1_THS_A 0x32
    _LSM303_INT1_DURATION_A 0x33
    _LSM303_INT2_CFG_A 0x34
    _LSM303_INT2_SRC_A 0x35
    _LSM303_INT2_THS_A 0x36
    _LSM303_INT2_DURATION_A 0x37

    _LSM303_CLICK_CFG_A 0x38 # DLHC only
    _LSM303_CLICK_SRC_A 0x39 # DLHC only
    _LSM303_CLICK_THS_A 0x3A # DLHC only
    _LSM303_TIME_LIMIT_A 0x3B # DLHC only
    _LSM303_TIME_LATENCY_A 0x3C # DLHC only
    _LSM303_TIME_WINDOW_A 0x3D # DLHC only

    _LSM303_CRA_REG_M 0x00
    _LSM303_CRB_REG_M 0x01
    _LSM303_MR_REG_M 0x02

    _LSM303_OUT_X_H_M 0x03
    _LSM303_OUT_X_L_M 0x04
    _LSM303_OUT_Y_H_M -1 # The addresses of the Y and Z magnetometer output registers
    _LSM303_OUT_Y_L_M -2 # are reversed on the DLM and DLHC relative to the DLH.
    _LSM303_OUT_Z_H_M -3 # These four defines have dummy values so the library can
    _LSM303_OUT_Z_L_M -4 # determine the correct address based on the device type.

    _LSM303_SR_REG_M 0x09
    _LSM303_IRA_REG_M 0x0A
    _LSM303_IRB_REG_M 0x0B
    _LSM303_IRC_REG_M 0x0C

    _LSM303_WHO_AM_I_M 0x0F # DLM only

    _LSM303_TEMP_OUT_H_M 0x31 # DLHC only
    _LSM303_TEMP_OUT_L_M 0x32 # DLHC only

    _LSM303DLH_OUT_Y_H_M 0x05
    _LSM303DLH_OUT_Y_L_M 0x06
    _LSM303DLH_OUT_Z_H_M 0x07
    _LSM303DLH_OUT_Z_L_M 0x08

    _LSM303DLM_OUT_Z_H_M 0x05
    _LSM303DLM_OUT_Z_L_M 0x06
    _LSM303DLM_OUT_Y_H_M 0x07
    _LSM303DLM_OUT_Y_L_M 0x08

    _LSM303DLHC_OUT_Z_H_M 0x05
    _LSM303DLHC_OUT_Z_L_M 0x06
    _LSM303DLHC_OUT_Y_H_M 0x07
    _LSM303DLHC_OUT_Y_L_M 0x08

    def __init__(self, accel_address = ACCEL_ADDRESS, mag_address = MAG_ADDRESS):
        self.accel = Adafruit_I2C.Adafruit_I2C(accel_address)
        self.mag = Adafruit_I2C.Adafruit_I2C(mag_address)

    def enableDefault():
        #Enable Accelerometer
        self.accel.write8(LSM303_CTRL_REG1_A, 0x27)
        #Enable Magnetometer
        self.mag.write8(LSM_MR_REG_M, 0x00)

