# Waveshare ESP32 Boards

Experimental Arduino Boards Manager package for the Waveshare ESP32-P4-WIFI6-DB Touch LCD 10.1. It uses the Arduino core and toolchain from **esp32 by Espressif Systems 4.0.0**.

## Install

1. In Arduino IDE 2, install **esp32 by Espressif Systems 4.0.0** from Boards Manager.
2. Open **File > Preferences > Additional boards manager URLs** and add:
   `https://raw.githubusercontent.com/ycorez/arduino-esp32-boards/main/package_waveshare_index.json`
3. In Boards Manager, install **Waveshare ESP32 Boards**. Select **Waveshare ESP32-P4-WIFI6-DB Touch LCD 10.1** from the Waveshare platform.
4. Open [board_check.ino](examples/board_check/board_check.ino), compile, select the board's serial port, and upload.

The board identifier is `waveshare:esp32:waveshare_esp32_p4_wifi6_db_touch_lcd_10_1`. Arduino CLI 1.0.4 or newer is needed for the referenced core platform path setting.

## Scope

This preview covers board selection and the board check sketch. Display, touch, camera and the other product examples require separate regression testing. ESP32-C5 Hosted Wi-Fi and BLE require C5-specific P4 libraries and coprocessor firmware.

The board definition, variant and board check sketch come from the Waveshare 10.1 product repository. See [LICENSE](LICENSE).
