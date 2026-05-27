Thrust Curve Reconstruction Tool
Akul Nagalikar — Aerospace Engineering, Texas A&M University
A load-cell based thrust measurement system built on Raspberry Pi that captures real-time thrust data from commercial model rocket motors and reconstructs their thrust curves using Python signal processing. Results are validated against manufacturer published data from thrustcurve.org.
What this project does:

Measures thrust force in real time using an HX711 load cell amplifier
Captures and saves data to CSV at 100Hz
Applies a Butterworth low-pass filter to remove sensor noise
Compares reconstructed curves against manufacturer .eng files
Calculates percent error on peak thrust and total impulse

Built with: Python • Raspberry Pi 3 • SolidWorks • HX711 load cell
