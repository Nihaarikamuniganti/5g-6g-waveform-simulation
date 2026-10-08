# 5g-6g-waveform-simulation
Simulating CP-OFDM vs. advanced 5G/6G waveforms, PAPR analysis, and fading channels using Python/MATLAB.
# Advanced 5G/6G Waveform Performance Evaluation

## Overview
This repository contains Python-based simulation frameworks exploring physical layer (PHY) characteristics for next-generation wireless communication systems. It focuses on multicarrier modulation, channel impairments, and Peak-to-Average Power Ratio (PAPR) analysis.

## Key Features
* **Multicarrier Modulation:** Simulates baseband signal generation using high-order QAM mapping (16-QAM/64-QAM) coupled with IFFT operations.
* **Channel Modeling:** Incorporates Rayleigh fading channel effects to evaluate signal robustness in dynamic multipath environments.
* **PAPR Analysis:** Computes power distribution metrics to assess power amplifier linearity constraints for 5G/6G deployment scenarios.

## Tech Stack
* **Language:** Python
* **Libraries:** NumPy, SciPy, Matplotlib

## How to Run
```bash
python waveform_simulation.py
