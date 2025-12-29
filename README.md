# Project README

## Overview
This project uses a Raspberry Pi Pico along with several input and output components to create a custom electronics system. The system includes switches, rotary encoders, a slide potentiometer, and supporting parts like diodes and connectors. The goal is to read user inputs and process them using the microcontroller.

## RENDER
<img width="945" height="626" alt="Render" src="https://github.com/user-attachments/assets/c992b6ff-e8fe-46c4-976b-63e58aa24077" />

## SCHEMATICS
<img width="945" height="626" alt="Schematics" src="https://github.com/user-attachments/assets/2c7b7453-1814-4a6d-8468-24df1f326aa3" />

## PCB
<img width="1126" height="626" alt="PCB" src="https://github.com/user-attachments/assets/9247aa6b-31e7-4ca8-8e1b-c53a03fb80e0" />

## CASE
<img width="427" height="260" alt="CAD" src="https://github.com/user-attachments/assets/03ece9e1-909b-4fd8-9556-926adccebf6b" />


## Bill of Materials (BOM)

| Component | Designator(s) | Footprint | Quantity | Description |
|----------|---------------|-----------|----------|-------------|
| Mechanical Switches | SW1–SW39 | SW_Cherry_MX_1.00u_PCB | 19 | Cherry MX style push switches |
| Diodes | D1–D27 | D_DO-35_SOD27_P7.62mm | 22 | 1N4148 signal diodes |
| 8-Pin Header | J1 | PinSocket_1x08_P2.54mm | 1 | 8-pin connector |
| Extra Switches | SW5, SW10 | SW_Cherry_MX_1.00u_PCB | 2 | Additional push switches |
| ADC Chip | U1 | Adafruit_ADS1115 | 1 | ADS1015 analog-to-digital converter |
| Rotary Encoders | SW25, SW26 | Alps EC11E | 2 | Rotary encoders with push switch |
| Slide Potentiometer | RV1 | Slide_Pot_75mm | 1 | Adafruit slide potentiometer (4219) |
| 4-Pin Header | J2 | PinSocket_1x04_P2.54mm | 1 | SD card connector |
| Microcontroller | A1 | RaspberryPi_Pico | 1 | Raspberry Pi Pico microcontroller |
| DAC | U2 | PCM5100 | 1 | PCM5100 I2S digital-to-analog converter |

## How It Works
- The Raspberry Pi Pico acts as the main controller.
- Switches and encoders are used for user input.
- The slide potentiometer provides analog input.
- The ADC and DAC handle analog-to-digital and digital-to-analog conversion.
- Diodes help protect and control signal flow.
