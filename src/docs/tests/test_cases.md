AquaRoot-X Test Cases

Purpose

These test cases describe the expected behaviour of the initial soil moisture monitoring prototype.

Test| Input condition| Expected result
1| Soil moisture value is above the dry threshold| IRRIGATE
2| Soil moisture value is below the dry threshold| MONITOR
3| Sensor reading changes| Arduino reads and displays the new value
4| Sensor is disconnected| Detect and report the sensor issue (planned enhancement)

Testing Status

These are planned test cases. Actual hardware testing has not yet been completed.

Safety

Do not connect a water pump directly to an Arduino output pin. Use a suitably rated relay or motor driver and an appropriate power supply.
