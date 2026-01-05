# Project README

## Overview
This project uses a Raspberry Pi Pico along with several input and output components to create a custom electronics system. The system includes switches, rotary encoders, a slide potentiometer, and supporting parts like diodes and connectors. The goal is to read user inputs and process them using the microcontroller.

## FINAL CAD WITH ASSEMBLED PARTS
<img width="427" height="260" alt="image" src="https://github.com/user-attachments/assets/45e3b2cf-7882-4cbe-8e11-bacbc240fd29" />


## RENDER
<img width="945" height="626" alt="Render" src="https://github.com/user-attachments/assets/c992b6ff-e8fe-46c4-976b-63e58aa24077" />

## SCHEMATICS
<img width="945" height="626" alt="Schematics" src="https://github.com/user-attachments/assets/2c7b7453-1814-4a6d-8468-24df1f326aa3" />

## PCB
<img width="1126" height="626" alt="PCB" src="https://github.com/user-attachments/assets/9247aa6b-31e7-4ca8-8e1b-c53a03fb80e0" />

## CASE
<img width="427" height="260" alt="CAD" src="https://github.com/user-attachments/assets/03ece9e1-909b-4fd8-9556-926adccebf6b" />


## Bill of Materials (BOM)
| Component                   | Quantity | Price ($)  | Source                                                                                                                                                                                                                                                                        |
| --------------------------- | -------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cherry MX Blue Switch       | 1        | 2.00       | [AliExpress](https://www.aliexpress.com/item/1005006255961111.html?spm=a2g0o.cart.0.0.14a938daZ9cXHR&mp=1&pdp_npi=5%40dis%21CAD%21CAD%209.25%21CAD%201.63%21%21CAD%201.63%21%21%21%402103277f17603785192817446e4b13%2112000036489552472%21ct%21CA%216607241988%21%211%210)    |
| Cherry MX Red Switch        | 20       | 13.00      | [AliExpress](https://www.aliexpress.com/item/1005006255961111.html?spm=a2g0o.cart.0.0.14a938daZ9cXHR&mp=1&pdp_npi=5%40dis%21CAD%21CAD%2013.73%21CAD%2012.78%21%21CAD%2012.78%21%21%21%402103277f17603785192817446e4b13%2112000036489552484%21ct%21CA%216607241988%21%211%210) |
| S37735R Screen              | 1        | N/A        | Included in kit                                                                                                                                                                                                                                                               |
| 1N4148 Diode                | 22       | N/A        | Included in kit                                                                                                                                                                                                                                                               |
| Orpheus Pico                | 1        | N/A        | Included in kit                                                                                                                                                                                                                                                               |
| PCM5100 DAC                 | 1        | N/A        | Included in kit                                                                                                                                                                                                                                                               |
| EC11 Rotary Encoder         | 2        | N/A        | Included in kit                                                                                                                                                                                                                                                               |
| M3 18 mm Screw              | 4        | 1.06       | [BambuLab](https://us.store.bambulab.com/products/m3-button-head-cap-machine-screws-bhcs?id=42338644951176)                                                                                                                                                                   |
| M3 4 mm Screw               | 4        | 1.06       | [BambuLab](https://us.store.bambulab.com/products/m3-button-head-cap-machine-screws-bhcs?id=42338644721800)                                                                                                                                                                   |
| M2 5 mm Screw               | 2        | 1.02       | [BambuLab](https://us.store.bambulab.com/products/m2-button-head-cap-machine-screws-bhcs?id=42328200577160)                                                                                                                                                                   |
| Slide Potentiometer         | 1        | Included   | [Adafruit](https://www.adafruit.com/product/4219)                                                                                                                                                                                                                             |
| ADS ADC Module              | 1        | Included   | [Adafruit](https://www.adafruit.com/product/1083)                                                                                                                                                                                                                             |
| **Adafruit Parts Total**    | —        | **34.30**  | [Adafruit](https://www.adafruit.com/)                                                                                                                                                                                                                                         |
| **JLCPCB (PCB + Assembly)** | —        | **52.46**  | [JLCPCB](https://jlcpcb.com/)                                                                                                                                                                                                                                                 |
| **BambuLab Shipping**       | —        | **6.00**   | [BambuLab](https://us.store.bambulab.com/)                                                                                                                                                                                                                                    |
| **TOTAL COST (All Parts)**  | —        | **110.90** | —                                                                                                                                                                                                                                                                             |



## How It Works
- The Raspberry Pi Pico acts as the main controller.
- Switches and encoders are used for user input.
- The slide potentiometer provides analog input.
- The ADC and DAC handle analog-to-digital and digital-to-analog conversion.
- Diodes help protect and control signal flow.
