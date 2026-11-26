# Waveshare ESP32 Boards

[English](README.md) | 中文

面向微雪（Waveshare）ESP32 系列开发板的实验性 Arduino 开发板管理器（Boards Manager）扩展包。本扩展包复用 **esp32 by Espressif Systems 4.0.0** 提供的 Arduino 核心与工具链。

## 支持的开发板

| 开发板 | 开发板标识符（FQBN） |
| --- | --- |
| Waveshare ESP32-P4-WIFI6-DB Touch LCD 10.1 | `waveshare:esp32:waveshare_esp32_p4_wifi6_db_touch_lcd_10_1` |
| Waveshare ESP32-P4-WIFI6-DB Touch LCD 7C | `waveshare:esp32:waveshare_esp32_p4_wifi6_db_touch_lcd_7c` |
| Waveshare ESP32-P4-POE-ETH | `waveshare:esp32:waveshare_p4_poe_eth` |

## 安装步骤

1. 在 Arduino IDE 2 中，打开开发板管理器（Boards Manager），安装 **esp32 by Espressif Systems 4.0.0**。
2. 打开 **文件 > 首选项 > 其他开发板管理器地址**（**File > Preferences > Additional boards manager URLs**），添加以下地址：
   `https://raw.githubusercontent.com/waveshareteam/arduino-esp32-boards/main/package_waveshare_index.json`
3. 在开发板管理器中搜索并安装 **Waveshare ESP32 Boards**，然后在 **Waveshare ESP32 Boards** 平台下选择对应的开发板。
4. 打开示例 [board_check.ino](examples/board_check/board_check.ino)，编译后选择开发板对应的串口并上传。

由于扩展包依赖核心平台路径引用配置，使用 Arduino CLI 时需要 1.0.4 或更高版本。

## 适用范围

当前预览版主要覆盖开发板选择和基础板级自检示例。显示、触摸、摄像头、以太网及其他产品示例需要单独进行回归测试；ESP32-C5 Hosted Wi-Fi 与 BLE 功能需要配套的 C5 专用 P4 库及协处理器固件。

开发板定义、引脚变体（variant）和板级检查示例来源于对应的微雪产品仓库及 Arduino-ESP32，许可证详见 [LICENSE](LICENSE)。

## 扩展包维护与发布

[Board package 工作流](.github/workflows/board-package.yml) 会在隔离的 Arduino CLI 环境中构建压缩包与临时索引、安装 Espressif 核心和 Waveshare 扩展包，并编译板级检查示例。向仓库推送代码或提交 Pull Request 时仅执行校验流程。

如需发布新版本，请在 `main` 分支手动运行 **Actions > Board package > Run workflow**，并输入尚未使用的版本号（例如 `0.1.2`）。校验通过后，工作流会将归档包上传到 GitHub prerelease，并更新公开索引文件（同时保留历史版本记录）。若 Release 发布成功但索引推送失败，可在与最新公开索引核对无误后，应用工作流产物中生成的索引文件进行恢复。

本工作流遵循 [Arduino 平台规范](https://docs.arduino.cc/arduino-cli/platform-specification/)、[包索引规范](https://docs.arduino.cc/arduino-cli/package_index_json-specification/)，并参考了 [ArduinoCore-samd 发布工作流](https://github.com/arduino/ArduinoCore-samd/blob/master/.github/workflows/release.yaml) 中的安装测试模式。

## Gitee 镜像

GitHub 为本项目的源仓库。发布工作流在完成 GitHub 发布后，会自动将同一份 ZIP 归档包以及适配 Gitee 的开发板管理器索引镜像到 [Gitee 仓库](https://gitee.com/pingshui11/arduino-esp32-boards)。请在 GitHub Actions 仓库密钥中配置具备该 Gitee 仓库推送权限的个人访问令牌 `GITEE_TOKEN`。

如需回填历史版本或重试失败的镜像同步，请手动运行 **Actions > Mirror board package to Gitee > Run workflow** 并填写对应版本号。镜像提交会在同一次提交中保存归档包和索引文件，并按最新镜像发布标签同步除 `package_waveshare_index.json` 和 `archives/` 外的其余仓库文件；回填较旧版本时不会回滚该源码快照。首次镜像成功后，Gitee 用户即可使用 [Gitee 索引地址](https://gitee.com/pingshui11/arduino-esp32-boards/raw/main/package_waveshare_index.json)。
