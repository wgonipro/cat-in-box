# Sensors: 

**Version:** 1.0  
**Date:** February 8, 2026  
**Designer:** Goniprow  
**Document Purpose:** Explain how different sensors should function.

---

## 1. Output Parsing
We can decide to either provide the player with _perfect_ sensor data, i.e. the
exact value for the given sensed parameter per the simulation, or provide the
player with _noisy_ sensor data.  

If _perfect_ sensor data is the *signal* that the artificial sensor is attempting
to read, then the frequency of this *signal* is one per tick (call it 1 Hz). Sensor 
noise should appear at higher frequencies, 10-50 Hz. To solve this, 
we can interpolate between the _perfect_ sensor data and adding random or non-random 
error before plotting the data for the player. 

In the following images, I show a potential _perfect_ sensor output and a _spoofed_
sensor output with a 40 Hz signal and a random Gaussian error with a standard
deviation of 0.1%.  

![Perfect Output](/documents/images/perfect_output.png)  
![Spoofed Output](/documents/images/spoofed_output.png)