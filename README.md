# Project-0-basics
This was one of my first projects I made around 3 months in learning robotics when I just turned 14. I wanted A Micro:bit project that changes an RGB LED's colour and brightness based on surrounding temperature or brightness and display the levels on the Microbit's LED grid. I didnt end up fixing and finishing it so recently i decided to debug it 

## Objective
At the start i wrote down my initial objective:
"The objective of this project is to change the colour and brightness of an RGB LED based on the temperature or brightness of the surroundings. Button A switches to brightness mode and Button B switches to temperature mode, with the values displayed on the micro:bit. The project also aims to display the temperature/brightness using the LED grid." 

## Resources:
For the whole project i used tinkercad online because i had little access to hardware
- I made the cicruit using a microbit and an RGB LED:
<img width="100" alt="image" src="https://github.com/user-attachments/assets/2245d463-48ce-4932-86b8-a80557cf7722" />

## Original Code

This is my origional code that i made and i couldnt fix the errors:

[View the original MicroPython code](code/original_code.py)

## Debuging

### First fix:
I decided the start with temperature so i created a new file just for that seperatly and ther were quite a few bugs in that seperatly so i had to fix them:
##
First temp error: Temperature thresholds checked in the wrong order. (e.g if temp >= -5:)
Almost every normal temperature satisfies this condition, so the later temperature conditions never get checked. The LED can therefore use the wrong colour.
Fix: I recoded it from the highest threshold downwards, starting at 50°C and working towards −5°C.
##
Second temp error: there was a whole lotof redundent code i didnt realise that was sitting there so i celaned it all up (e.g in the origional code lines 

### Second fix:



### Final code


