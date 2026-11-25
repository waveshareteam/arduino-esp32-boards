# Waveshare ESP32 Boards

Experimental Arduino Boards Manager package for the Waveshare ESP32-P4-WIFI6-DB Touch LCD 10.1. It uses the Arduino core and toolchain from **esp32 by Espressif Systems 4.0.0**.

## Install

1. In Arduino IDE 2, install **esp32 by Espressif Systems 4.0.0** from Boards Manager.
2. Open **File > Preferences > Additional boards manager URLs** and add:
   `https://raw.githubusercontent.com/waveshareteam/arduino-esp32-boards/main/package_waveshare_index.json`
3. In Boards Manager, install **Waveshare ESP32 Boards**. Select **Waveshare ESP32-P4-WIFI6-DB Touch LCD 10.1** from the Waveshare platform.
4. Open [board_check.ino](examples/board_check/board_check.ino), compile, select the board's serial port, and upload.

The board identifier is `waveshare:esp32:waveshare_esp32_p4_wifi6_db_touch_lcd_10_1`. Arduino CLI 1.0.4 or newer is needed for the referenced core platform path setting.

## Scope

This preview covers board selection and the board check sketch. Display, touch, camera and the other product examples require separate regression testing. ESP32-C5 Hosted Wi-Fi and BLE require C5-specific P4 libraries and coprocessor firmware.

The board definition, variant and board check sketch come from the Waveshare 10.1 product repository. See [LICENSE](LICENSE).

## Maintain the package

The [Board package workflow](.github/workflows/board-package.yml) builds an archive and a temporary index, installs both the Espressif core and the Waveshare package in an isolated Arduino CLI environment, and compiles the board check example. Pushes and pull requests run verification only.

To publish a release, run **Actions > Board package > Run workflow** on `main` with an unused version such as `0.1.1`. After verification passes, the workflow uploads the archive to a GitHub prerelease and updates the public index while retaining older entries. If the release succeeds but the index push fails, recover by applying the generated index from the workflow artifact after checking it against the latest public index.

The workflow follows the [Arduino platform specification](https://docs.arduino.cc/arduino-cli/platform-specification/), [package index specification](https://docs.arduino.cc/arduino-cli/package_index_json-specification/), and the install test pattern in the [ArduinoCore-samd release workflow](https://github.com/arduino/ArduinoCore-samd/blob/master/.github/workflows/release.yaml).

## Gitee mirror

GitHub is the source repository. The release workflow mirrors the same ZIP and a Gitee-specific Boards Manager index to [Gitee](https://gitee.com/pingshui11/arduino-esp32-boards) after publishing to GitHub. Configure the GitHub Actions repository secret `GITEE_TOKEN` with a Gitee personal access token that can push to that repository.

To backfill an existing release or retry a failed mirror, run **Actions > Mirror board package to Gitee > Run workflow** with its version. The mirror stores the archive and index in the same commit. Gitee users can add the [Gitee index](https://gitee.com/pingshui11/arduino-esp32-boards/raw/main/package_waveshare_index.json) after the first successful mirror.
