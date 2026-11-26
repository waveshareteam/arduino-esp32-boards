#ifndef Pins_Arduino_h
#define Pins_Arduino_h

#include <stdint.h>

// UART0 is connected to the on-board USB-to-UART bridge.
static const uint8_t TX = 37;
static const uint8_t RX = 38;

// Fixed serial transceivers: Serial1 is RS485 and Serial2 is RS232.
#define TX1 26
#define RX1 27
#define RS485_TX TX1
#define RS485_RX RX1
#define RS485_DIR 34
#define RS485_DE RS485_DIR

#define TX2 28
#define RX2 29
#define RS232_TX TX2
#define RS232_RX RX2

// Shared by the GT911 touch controller, ES8389 codec, RTC, and camera SCCB.
static const uint8_t SDA = 7;
static const uint8_t SCL = 8;

// Default SPI bus uses the first four GPIOs on the expansion header.
static const uint8_t MOSI = 32;
static const uint8_t MISO = 33;
static const uint8_t SCK = 49;
static const uint8_t SS = 50;

// Expansion-header GPIOs, in physical header enumeration order.
static const uint8_t D0 = 32;
static const uint8_t D1 = 33;
static const uint8_t D2 = 49;
static const uint8_t D3 = 50;
static const uint8_t D4 = 51;
static const uint8_t D5 = 48;
static const uint8_t D6 = 47;
static const uint8_t D7 = 46;
static const uint8_t D8 = 36;
static const uint8_t D9 = 25;
static const uint8_t D10 = 24;
static const uint8_t D11 = 5;
static const uint8_t D12 = 4;

// GPIO24/GPIO25 are also the USB 2.0 HS differential pair.
#define USB_DN 24
#define USB_DP 25

// Both on-board user LEDs are active low.
#define LED_BUILTIN 2
#define BUILTIN_LED LED_BUILTIN
#define LED_BUILTIN_ACTIVE LOW
#define LED_BUILTIN_INACTIVE HIGH
#define LED_USER1 2
#define LED_USER2 3

// MIPI-DSI LCD and GT911 touch controller.
#define LCD_INTERFACE_MIPI
#define LCD_RST 31
#define LCD_RST_IO LCD_RST
#define LCD_RST_ACTIVE_HIGH false
#define LCD_BL 30
#define LCD_BL_IO LCD_BL
#define LCD_BL_ON_LEVEL LOW
#define LCD_BL_OFF_LEVEL HIGH
#define TOUCH_RST 23
#define TOUCH_INT -1
#define CTP_RST TOUCH_RST
#define CTP_INT TOUCH_INT

// I2C aliases used by the on-board display and touch libraries.
#define I2C_SDA SDA
#define I2C_SCL SCL

// ES8389 audio codec.
#define I2S_DOUT 9
#define I2S_LRCLK 10
#define I2S_DIN 11
#define I2S_BCLK 12
#define I2S_MCLK 13
#define PA_POWER 53

// On-board TWAI transceiver.
#define TWAI_TX 22
#define TWAI_RX 21

// The microSD card uses SDMMC slot 0 in 4-bit mode.
#define BOARD_HAS_SDMMC
#define BOARD_SDMMC_SLOT 0
#define BOARD_SDMMC_CLK 43
#define BOARD_SDMMC_CMD 44
#define BOARD_SDMMC_D0 39
#define BOARD_SDMMC_D1 40
#define BOARD_SDMMC_D2 41
#define BOARD_SDMMC_D3 42
#define BOARD_SDMMC_POWER_CHANNEL 4
#define BOARD_SDMMC_POWER_PIN 45
#define BOARD_SDMMC_POWER_ON_LEVEL LOW

// ESP32-C5 wireless co-processor connected through ESP-Hosted SDIO slot 1.
#define BOARD_HAS_SDIO_ESP_HOSTED
#define BOARD_SDIO_ESP_HOSTED_CLK 18
#define BOARD_SDIO_ESP_HOSTED_CMD 19
#define BOARD_SDIO_ESP_HOSTED_D0 14
#define BOARD_SDIO_ESP_HOSTED_D1 15
#define BOARD_SDIO_ESP_HOSTED_D2 16
#define BOARD_SDIO_ESP_HOSTED_D3 17
#define BOARD_SDIO_ESP_HOSTED_RESET 54

// GPIO39-GPIO48 are powered by the ESP32-P4 on-chip LDO VO4.
#define BOARD_PERIMAN_IO_LDO_AUTO 1
#define BOARD_PERIMAN_IO_LDO0_CHANNEL 4
#define BOARD_PERIMAN_IO_LDO0_GPIO_MIN 39
#define BOARD_PERIMAN_IO_LDO0_GPIO_MAX 48
#define BOARD_PERIMAN_IO_LDO0_VOLTAGE_MV 3300

#endif /* Pins_Arduino_h */
