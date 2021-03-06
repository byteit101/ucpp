import os


##### Load Configuration #####

# Project info (variables set by the configure script)

CPP_PROJECT_ROOT_DIR = os.environ["CPP_PROJECT_ROOT_DIR"]
CPP_PROJECT_WS_ROOT_DIR = os.environ["CPP_PROJECT_WS_ROOT_DIR"]
CPP_PROJECT_NAME = os.environ["CPP_PROJECT_NAME"]

# Read the .wrmakefile

f = file(".wrmakefile", "r")
wrmakefile = f.read()
f.close()

# Find all the C++ files in the current directory

file_names = []
for filename in os.listdir("."):
    if filename[-4:]==".cpp":
        file_names.append(filename[:-4])

file_names = [
"ADXL345_I2C",
"Accelerometer",
"AnalogChannel",
"AnalogModule",
"AnalogTrigger",
"AnalogTriggerOutput",
"CANJaguar",
"CInterfaces/CAccelerometer",
"CInterfaces/CAnalogChannel",
"CInterfaces/CCompressor",
"CInterfaces/CCounter",
"CInterfaces/CDigitalInput",
"CInterfaces/CDigitalOutput",
"CInterfaces/CDriverStation",
"CInterfaces/CEncoder",
"CInterfaces/CGearTooth",
"CInterfaces/CGyro",
"CInterfaces/CJaguar",
"CInterfaces/CJoystick",
"CInterfaces/CPWM",
"CInterfaces/CRelay",
"CInterfaces/CRobotDrive",
"CInterfaces/CSerialPort",
"CInterfaces/CServo",
"CInterfaces/CSolenoid",
"CInterfaces/CTimer",
"CInterfaces/CUltrasonic",
"CInterfaces/CVictor",
"CInterfaces/CWatchdog",
"CInterfaces/SimpleCRobot",
"Compressor",
"Counter",
"Dashboard",
"DigitalInput",
"DigitalModule",
"DigitalOutput",
"DigitalSource",
"DriverStation",
"DriverStationEnhancedIO",
"DriverStationLCD",
"Encoder",
"Error",
"ErrorBase",
"GearTooth",
"Gyro",
"HiTechnicCompass",
"I2C",
"InterruptableSensorBase",
"IterativeRobot",
"Jaguar",
"Joystick",
"Module",
"MotorSafetyHelper",
"Notifier",
"PIDController",
"PWM",
"Relay",
"Resource",
"RobotBase",
"RobotDrive",
"SafePWM",
"SensorBase",
"SerialPort",
"Servo",
"SimpleRobot",
"SmartDashboard",
"SmartDashboardPacketFactory",
"Solenoid",
"Synchronized",
"Task",
"Timer",
"Ultrasonic",
"Utility",
"Victor",
"Vision/AxisCamera",
"Vision/AxisCameraParams",
"Vision/BinaryImage",
"Vision/ColorImage",
"Vision/EnumCameraParameter",
"Vision/HSLImage",
"Vision/ImageBase",
"Vision/IntCameraParameter",
"Vision/MonoImage",
"Vision/PCVideoServer",
"Vision/RGBImage",
"Vision/Threshold",
"Vision2009/AxisCamera",
"Vision2009/BaeUtilities",
"Vision2009/FrcError",
"Vision2009/TrackAPI",
"Vision2009/VisionAPI",
"Watchdog"

]

##### Generate makefile sections #####

# Header section

header_section = """
# Makefile generated using Team 980's Makefile generation script
# Do not edit!!!
#
"""[1:]

#common config section (mostly variables)

common_section = """TRACE=0
TRACEON=$(TRACE:0=@)
TRACE_FLAG=$(TRACEON:1=)

MAKEFILE := Makefile

FLEXIBLE_BUILD := 1

BUILD_SPEC = PPC603gnu
DEBUG_MODE = 1
ifeq ($(DEBUG_MODE),1)
MODE_DIR := Debug
else
MODE_DIR := NonDebug
endif
OBJ_DIR := .
PRJ_ROOT_DIR := CPP_PROJECT_ROOT_DIR
WS_ROOT_DIR := CPP_PROJECT_WS_ROOT_DIR



#Global Build Macros
PROJECT_TYPE = DKM
DEFINES = 
EXPAND_DBG = 0


#BuildSpec specific Build Macros
VX_CPU_FAMILY = ppc
CPU = PPC603
TOOL_FAMILY = gnu
TOOL = gnu
TOOL_PATH = 
CC_ARCH_SPEC = -mcpu=603 -mstrict-align -mno-implicit-fp  -mlongcall
LIBPATH = 
LIBS = 

IDE_INCLUDES = -I.. -I$(WIND_BASE)/target/h -I$(WIND_BASE)/target/h/wrn/coreip

IDE_LIBRARIES = 



#BuildTool flags
ifeq ($(DEBUG_MODE),1)
DEBUGFLAGS_C-Compiler = -g
DEBUGFLAGS_C++-Compiler = -g
DEBUGFLAGS_Linker = -g
DEBUGFLAGS_Partial-Image-Linker = 
DEBUGFLAGS_Librarian = 
DEBUGFLAGS_Assembler = -g
else
DEBUGFLAGS_C-Compiler = -O2 -fstrength-reduce -fno-builtin
DEBUGFLAGS_C++-Compiler = -O2 -fstrength-reduce -fno-builtin
DEBUGFLAGS_Linker = -O2 -fstrength-reduce -fno-builtin
DEBUGFLAGS_Partial-Image-Linker = 
DEBUGFLAGS_Librarian = 
DEBUGFLAGS_Assembler = -O2 -fstrength-reduce -fno-builtin
endif


#Project Targets
PROJECT_TARGETS = CPP_PROJECT_NAME/$(MODE_DIR)/CPP_PROJECT_NAME.a


#Rules

# CPP_PROJECT_NAME
ifeq ($(DEBUG_MODE),1)
CPP_PROJECT_NAME/$(MODE_DIR)/% : DEBUGFLAGS_C-Compiler = -g
CPP_PROJECT_NAME/$(MODE_DIR)/% : DEBUGFLAGS_C++-Compiler = -g
CPP_PROJECT_NAME/$(MODE_DIR)/% : DEBUGFLAGS_Linker = -g
CPP_PROJECT_NAME/$(MODE_DIR)/% : DEBUGFLAGS_Partial-Image-Linker = 
CPP_PROJECT_NAME/$(MODE_DIR)/% : DEBUGFLAGS_Librarian = 
CPP_PROJECT_NAME/$(MODE_DIR)/% : DEBUGFLAGS_Assembler = -g
else
CPP_PROJECT_NAME/$(MODE_DIR)/% : DEBUGFLAGS_C-Compiler = -O2 -fstrength-reduce -fno-builtin
CPP_PROJECT_NAME/$(MODE_DIR)/% : DEBUGFLAGS_C++-Compiler = -O2 -fstrength-reduce -fno-builtin
CPP_PROJECT_NAME/$(MODE_DIR)/% : DEBUGFLAGS_Linker = -O2 -fstrength-reduce -fno-builtin
CPP_PROJECT_NAME/$(MODE_DIR)/% : DEBUGFLAGS_Partial-Image-Linker = 
CPP_PROJECT_NAME/$(MODE_DIR)/% : DEBUGFLAGS_Librarian = 
CPP_PROJECT_NAME/$(MODE_DIR)/% : DEBUGFLAGS_Assembler = -O2 -fstrength-reduce -fno-builtin
endif
CPP_PROJECT_NAME/$(MODE_DIR)/% : IDE_INCLUDES = -I.. -I$(WIND_BASE)/target/h -I$(WIND_BASE)/target/h/wrn/coreip 
CPP_PROJECT_NAME/$(MODE_DIR)/% : IDE_LIBRARIES = 
CPP_PROJECT_NAME/$(MODE_DIR)/% : PROJECT_TYPE = DKM
CPP_PROJECT_NAME/$(MODE_DIR)/% : DEFINES = 
CPP_PROJECT_NAME/$(MODE_DIR)/% : EXPAND_DBG = 0
CPP_PROJECT_NAME/$(MODE_DIR)/% : VX_CPU_FAMILY = ppc
CPP_PROJECT_NAME/$(MODE_DIR)/% : CPU = PPC603
CPP_PROJECT_NAME/$(MODE_DIR)/% : TOOL_FAMILY = gnu
CPP_PROJECT_NAME/$(MODE_DIR)/% : TOOL = gnu
CPP_PROJECT_NAME/$(MODE_DIR)/% : TOOL_PATH = 
CPP_PROJECT_NAME/$(MODE_DIR)/% : CC_ARCH_SPEC = -mcpu=603 -mstrict-align -mno-implicit-fp  -mlongcall
CPP_PROJECT_NAME/$(MODE_DIR)/% : LIBPATH = 
CPP_PROJECT_NAME/$(MODE_DIR)/% : LIBS = 
CPP_PROJECT_NAME/$(MODE_DIR)/% : OBJ_DIR := CPP_PROJECT_NAME/$(MODE_DIR)
"""

common_section=common_section.replace("CPP_PROJECT_NAME",CPP_PROJECT_NAME)
common_section=common_section.replace("CPP_PROJECT_ROOT_DIR",CPP_PROJECT_ROOT_DIR)
common_section=common_section.replace("CPP_PROJECT_WS_ROOT_DIR",CPP_PROJECT_WS_ROOT_DIR)


# individual files section
file_section=""

for filename in file_names:
    this_file = """
CPP_PROJECT_NAME/$(MODE_DIR)/Objects/CPP_PROJECT_NAME/FILENAME.o : CPP_PROJECT_ROOT_DIR/FILENAME.cpp
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi; echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL -D'SVN_REV="$(shell svnversion -n ..)"' $(DEFINES) -o "$@" -c "$<"

"""
    this_file=this_file.replace("CPP_PROJECT_NAME", CPP_PROJECT_NAME)
    this_file=this_file.replace("CPP_PROJECT_ROOT_DIR", CPP_PROJECT_ROOT_DIR)
    this_file=this_file.replace("FILENAME", filename)

    file_section+=this_file


#Linking section (mostly)

link_section="""
OBJECTS_CPP_PROJECT_NAME = """

object_line="	 CPP_PROJECT_NAME/$(MODE_DIR)/Objects/CPP_PROJECT_NAME/"

for filename in file_names:
    link_section += object_line+filename+".o \\\n"

link_section=link_section[:-2]+"\n"

link_section+="""
CPP_PROJECT_NAME/$(MODE_DIR)/CPP_PROJECT_NAME.a : $(OBJECTS_CPP_PROJECT_NAME)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)arppc crus "$@" $(OBJECTS_CPP_PROJECT_NAME)

CPP_PROJECT_NAME/$(MODE_DIR)/CPP_PROJECT_NAME_compile_file : $(FILE) ;

_clean :: CPP_PROJECT_NAME/$(MODE_DIR)/CPP_PROJECT_NAME_clean

CPP_PROJECT_NAME/$(MODE_DIR)/CPP_PROJECT_NAME_clean : 
	$(TRACE_FLAG)if [ -d "CPP_PROJECT_NAME" ]; then cd "CPP_PROJECT_NAME"; rm -rf $(MODE_DIR); fi

"""

link_section=link_section.replace("CPP_PROJECT_NAME",CPP_PROJECT_NAME)

# Dep-files section
# (On Linux, this section is removed because it gives errors)

dep_files_section = "\nDEP_FILES := "
x=0
for filename in file_names:
    this_file="CPP_PROJECT_NAME/$(MODE_DIR)/Objects/CPP_PROJECT_NAME/"+filename+".d "
    this_file=this_file.replace("CPP_PROJECT_NAME",CPP_PROJECT_NAME)
    dep_files_section+=this_file
    x+=1
    if (x==3):
        dep_files_section+="\\\n"
        x=0
if (x==0):
    dep_files_section=dep_files_section[:-2]
dep_files_section+="""
-include $(DEP_FILES)

"""

##### Generate Makefile #####

#combine all of the sections

generated = common_section + file_section + link_section + dep_files_section

makefile = header_section + wrmakefile.replace("%IDE_GENERATED%", generated)

print makefile
