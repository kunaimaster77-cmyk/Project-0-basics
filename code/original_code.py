

#**VARIABLES**


#*LED plot variables*

brightness_symbol = "B"  #-> shape of "B"
temperature_symbol = "T" #-> shape of "T"


#*Brightness variables*

# 240:
g_240b = 0
b_240b = 0
r_240b = 0

# 230:
g_230b = 40
b_230b = 40
r_230b = 40

# 220:
g_220b = 80
b_220b = 80
r_220b = 80

# 210:
g_210b = 120
b_210b = 120
r_210b = 120

# 200:
g_200b = 160
b_200b = 160
r_200b = 160

# 190:
g_190b = 200
b_190b = 200
r_190b = 200

# 180:
g_180b = 240
b_180b = 240
r_180b = 240

# 170:
g_170b = 280
b_170b = 280
r_170b = 280

# 160:
g_160b = 320
b_160b = 320
r_160b = 320

# 150:
g_150b = 360
b_150b = 360
r_150b = 360

# 140:
g_140b = 400
b_140b = 400

r_140b = 400
# 130:
g_130b = 440
b_130b = 440
r_130b = 440

# 120:
g_120b = 480
b_120b = 480
r_120b = 480

# 110:
g_110b = 520
b_110b = 520
r_110b = 520

# 100:
g_100b = 560
b_100b = 560
r_100b = 560

# 90:
g_90b = 600
b_90b = 600
r_90b = 600

# 80:
g_80b = 640
b_80b = 640
r_80b = 640

# 70:
g_70b = 680
b_70b = 680
r_70b = 680

# 60:
g_60b = 720
b_60b = 720
r_60b = 720

# 50:
g_50b = 760
b_50b = 760
r_50b = 760

# 40:
g_40b = 800
b_40b = 800
r_40b = 800

# 30:
g_30b = 840
b_30b = 840
r_30b = 840

# 20:
g_20b = 920
b_20b = 920
r_20b = 920

# 10:
g_10b = 960
b_10b = 960
r_10b = 960

# 0:
g_0b = 1000
b_0b = 1000
r_0b = 1000


#*Temperature Variables*

#50:
g_50t = 50 #-> adjustable and makes it eiser 
b_50t = 0 # | to change the colour of RGB LED
r_50t = 1023

#45:
g_45t = 50
b_45t = 0
r_45t = 1000

#40:
g_40t = 100
b_40t = 0
r_40t = 1000

#35:
g_35t = 200
b_35t = 0
r_35t = 900

#30:
g_30t = 300
b_30t = 0
r_30t = 900

#25:
g_25t = 350
b_25t = 0
r_25t = 800

#20:
g_20t = 400
b_20t = 0
r_20t = 700

#15:
g_15t = 400
b_15t = 0
r_15t = 400

#10:
g_10t = 600
b_10t = 200
r_10t = 500

#5:
g_5t = 500
b_5t = 300
r_5t = 300

#0:
g_0t = 500
b_0t = 300
r_0t = 100

#-5:
g_neg5t = 200
b_neg5t = 1000
r_neg5t = 0

#**FUNCTIONS**


#*Brightness Funtion*
def light_level(g,b,r): 				
  pins.analog_write_pin(AnalogPin.P0, g)#-> only need one functon for
  pins.analog_write_pin(AnalogPin.P1, b)# | brightness after using parameters.
  pins.analog_write_pin(AnalogPin.P2, r)

#*Temperature Function*

def temp_level(g,b,r):
  pins.analog_write_pin(AnalogPin.P0, g)#-> only need one functon for
  pins.analog_write_pin(AnalogPin.P1, b)# | temperature after using parameters.
  pins.analog_write_pin(AnalogPin.P2, r)



#**BRIGHTNESS SECTION**
def show_brightness():
  #^
  #| when they press the button A it 
  #| switches to Brightness mode.
    
    level = input.light_level()
    
    basic.clear_screen()
    basic.show_string(brightness_symbol)#-> I previously used"basic.show_leds"
    #^									#| however "basic.show_string" makes it more simple
    #| to show the user that the microbit
    #| is on Brightness mode.
    
    pause(3000)
    basic.clear_screen()# ->  clear the leds after 
    					#   | the symbol is shown.
      
    
    #*IF* -> for the Led Plots
    
    if level > 240:
        led.plot(0, 0)#->  these plot on the 5 by 5 grid on the microbit
        
    if level > 230:   
        led.plot(0, 1)
        
    if level > 220:
        led.plot(0, 2)
        
    if level > 210:
        led.plot(0, 3)
        
    if level > 200:
        led.plot(0, 4)
        
    if level > 190:
        led.plot(1, 0)
        
    if level > 180:
        led.plot(1, 1)
        
    if level > 170:
        led.plot(1, 2)
        
    if level > 160:
        led.plot(1, 3)
        
    if level > 150:
        led.plot(1, 4)
        
    if level > 140:
        led.plot(2, 0)
        
    if level > 130:
        led.plot(2, 1)
        
    if level > 120:
        led.plot(2, 2)
        
    if level > 110:
        led.plot(2, 3)
        
    if level > 100:
        led.plot(2, 4)
        
    if level > 90:
        led.plot(3, 0)
        
    if level > 80:
        led.plot(3, 1)
        
    if level > 70:
        led.plot(3, 2)
        
    if level > 60:
        led.plot(3, 3)
        
    if level > 50:
        led.plot(3, 4)
        
    if level > 40:
        led.plot(4, 0)
        
    if level > 30:
        led.plot(4, 1)
        
    if level > 20:
        led.plot(4, 2)
        
    if level > 10:
        led.plot(4, 3)
        
    if level > 0:
        led.plot(4, 4)
     
    
    
    #*ELIF* -> for the RGB LED
    
    if level > 240:
        light_level(g_240b,b_240b,r_240b)#-> functions help simplify the code
    					
    elif level > 230:   
        light_level(g_230b,b_230b,r_230b)#-> Parameters from the funtions
    
    elif level > 220:
        light_level(g_220b,b_220b,r_220b)
    
    elif level > 210:
        light_level(g_210b,b_210b,r_210b)
    
    elif level > 200:
        light_level(g_200b,b_200b,r_200b)
    
    elif level > 190:
        light_level(g_190b,b_190b,r_190b)
    
    elif level > 180:
        light_level(g_180b,b_180b,r_180b)
    
    elif level > 170:
        light_level(g_170b,b_170b,r_170b)
    
    elif level > 160:
        light_level(g_160b,b_160b,r_160b)
    
    elif level > 150:
        light_level(g_150b,b_150b,r_150b)
    
    elif level > 140:
        light_level(g_140b,b_140b,r_140b)
    
    elif level > 130:
        light_level(g_130b,b_130b,r_130b)
    
    elif level > 120:
        light_level(g_120b,b_120b,r_120b)
    
    elif level > 110:
        light_level(g_110b,b_110b,r_110b)
    
    elif level > 100:
        light_level(g_100b,b_100b,r_100b)
    
    elif level > 90:
        light_level(g_90b,b_90b,r_90b)
    
    elif level > 80:
        light_level(g_80b,b_80b,r_80b)
    
    elif level > 70:
        light_level(g_70b,b_70b,r_70b)
    
    elif level > 60:
        light_level(g_60b,b_60b,r_60b)
    
    elif level > 50:
        light_level(g_50b,b_50b,r_50b)
    
    elif level > 40:
        light_level(g_40b,b_40b,r_40b)
    
    elif level > 30:
        light_level(g_30b,b_30b,r_30b)
    
    elif level > 20:
        light_level(g_20b,b_20b,r_20b)
    
    elif level > 10:
        light_level(g_10b,b_10b,r_10b)
    
    elif level > 0:
        light_level(g_0b,b_0b,r_0b)
     
    pause(2000)
    basic.clear_screen()

    

#**TEMPERATURE SECTION**
def show_temperature(): 
  #^
  #| when they press the button B the microbit
  #| switches to Temperature mode
    
    temp = input.temperature()#-> makes sure the variable is updated
    
    basic.clear_screen()
    basic.show_string(temperature_symbol)
    #^
    #| to show the user that the microbit
    #| is on Temperature mode.
    pause(3000)
    basic.clear_screen()
    
    
    
    #*IF* -> for the Led plot points
    
    if temp >= -5:
        led.plot(4, 4) #--> for temperature, since there 
        led.plot(4, 3) #  | was a smaller range I made it so 
        led.plot(4, 2) #  | that for each 5 degrees it turns on 
                       #  | 2-3 leds.
    if temp > 0:      
        led.plot(4, 1)
        led.plot(4, 0)
    
    if temp > 5:
        led.plot(3, 4)
        led.plot(3, 3)
    
    if temp > 10:
        led.plot(3, 2)
        led.plot(3, 1)
    
    if temp > 15:
        led.plot(3, 0)
        led.plot(2, 4)
    
    if temp > 20:
        led.plot(2, 3)
        led.plot(2, 2)
    
    if temp > 25:
        led.plot(2, 1)
        led.plot(2, 0)
    
    if temp > 30:
        led.plot(1, 4)
        led.plot(1, 3)
    
    if temp > 35:
        led.plot(1, 2)
        led.plot(1, 1)
    
    if temp > 40:
        led.plot(1, 0)
        led.plot(0, 4)
    
    if temp > 45:
        led.plot(0, 3)
        led.plot(0, 2)
    
    if temp >= 50:
        led.plot(0, 1)
        led.plot(0, 0)
    
    
    
    #*ELIF* -> for the RGB LED
    
    if temp >= -5:
    	temp_level(g_neg5t,b_neg5t,r_neg5t)
    
    elif temp > 0:      
        temp_level(g_0t,b_0t,r_0t)
    
    elif temp > 5:
        temp_level(g_5t,b_5t,r_5t)
    
    elif temp > 10:
        temp_level(g_10t,b_10t,r_10t)
    
    elif temp > 15:
        temp_level(g_15t,b_15t,r_15t)
    
    elif temp > 20:
        temp_level(g_20t,b_20t,r_20t)
    
    elif temp > 25:
        temp_level(g_25t,b_25t,r_25t)
    
    elif temp > 30:
        temp_level(g_30t,b_30t,r_30t)
    
    elif temp > 35:
        temp_level(g_35t,b_35t,r_35t)
    
    elif temp > 40:
        temp_level(g_40t,b_40t,r_40t)
   
    elif temp > 45:
        temp_level(g_45t,b_45t,r_45t)
    
    elif temp >= 50:
        temp_level(g_50t,b_50t,r_50t)

    pause(2000)
    basic.clear_screen()


#**BUTTONS**

input.on_button_pressed(Button.A, show_brightness) #-> this links the function to the button. 
input.on_button_pressed(Button.B, show_temperature)#-|



#**WHILE TRUE LOOP**
while True:
  pause(10)# -> this ensures that 
           #  | it doesn't crash the code






# RGB values when temp is in desired range
r = 0
g = 1023
b = 51


while True:
    temp = input.temperature()

    if temp >= 32 and temp <= 41:
        # RGB turns ON with desired color
        pins.analog_write_pin(AnalogPin.P0, r)  # Red
        pins.analog_write_pin(AnalogPin.P2, b)  # Blue
        pins.analog_write_pin(AnalogPin.P3, g)  # Green


    elif temp >= 5 and temp <= 15:
        # RGB set to greenish (e.g. low temp warning)
        pins.analog_write_pin(AnalogPin.P0, 0)      # Red
        pins.analog_write_pin(AnalogPin.P2, 0)      # Blue
        pins.analog_write_pin(AnalogPin.P3, 1023)   # Green


    else:
        # RGB OFF
        pins.analog_write_pin(AnalogPin.P0, 0)
        pins.analog_write_pin(AnalogPin.P2, 0)
        pins.analog_write_pin(AnalogPin.P3, 0)

    pause(1000)  # Wait before next temp check
