#!/usr/bin/python
# -*- encoding: utf-8 -*-
import time
import smbus
bus = smbus.SMBus(1) #(512MB ro 1024MB)
addr = 0x23 # i2c adress
while True:
  data = bus.read_i2c_block_data(addr,0x10)
  print ("Luminosity " ,"%.2f" % (data[1] + (256 * data[0]) / 1.2),"lx")
  time.sleep(0.5)
