import serial
import serial.tools.list_ports
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv
import pandas as pd
import time

x_len = 200
y_range = [0, 4096]

def vals(sampler):
    temp_arr = []
    stp_f = 0
    i=0
    sampler= int(sampler)
    while(i< sampler*0.2):
        read = ser.readline()
        if (read != b''):
            read2 = read.decode('UTF-8')
            read2 = read2.strip("\n")
            read2 = read2.strip("\r")
            if(read2.find("BPM")!=-1):
                stp_f = 1
                print(stp_f)
                print(read2)
                return temp_arr, stp_f
        #print(read2)
            if(len(read2)>0 and len(read2)<5):
                read3 = int(read2)
                temp_arr.append(read3)
        i = i+1
    return temp_arr, stp_f

def animate(i, ys, sampler):
    temp_arr_2, stop = vals(sampler)
    if stop == 1:
        ani.event_source.stop()
    for x in temp_arr_2:
        ys.append(x)
    ys = ys[-x_len:]
    line2.set_ydata(ys)
    return line2

if __name__ == '__main__':

    cnt=1
    x= []
    y= []

    # ports = serial.tools.list_ports.comports()
    # for port, desc, hwid in sorted(ports):
    #         print("     {}: {} ".format(port, desc))
    # in_port = input("Please Choose one of the ports listed above:\n")
    #
    # in_baudr = input("Please input a baud rate >= 128000:\n")
    # if(int(in_baudr)<128000):
    #     in_baudr=128000

    # ser = serial.Serial(port=in_port, baudrate=in_baudr, bytesize=serial.EIGHTBITS, parity= serial.PARITY_NONE, timeout=2)

    ser = serial.Serial(port='Com3', baudrate='128000', bytesize=serial.EIGHTBITS, parity= serial.PARITY_NONE, timeout=2)
    in_sampler = input("Please input the sampling rate:\n")
    new_lineC = '\n'



    command = input("Enter the command you want to start with\n")
    if(command=="start"):
        if len(in_sampler) < 3:
            ser.write(in_sampler.encode('utf-8'))
            ser.write(new_lineC.encode('utf-8'))
            ser.write(new_lineC.encode('utf-8'))
        elif (len(in_sampler) < 4):
            ser.write(in_sampler.encode('utf-8'))
            ser.write(new_lineC.encode('utf-8'))
        else:
            ser.write(in_sampler.encode('utf-8'))
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        xs = list(range(0, 200))
        ys = [0] * x_len
        ax.set_ylim(y_range)
        line2, = ax.plot(xs, ys)
        ani = animation.FuncAnimation(fig, animate, fargs=(ys,in_sampler ), interval=1)
        plt.show()
    # try:
    #     ser.isOpen()
    #     print( "Serial Port is Open" )
    # except:
    #     print ( "Error in opening serial port ")
    #
    # if(ser.isOpen()):
    #     try:
    #         # read = ser.readline()
    #         # while(cnt<int(in_sampler)-1): # change this to minute
    #             # read = ser.readline()
    #             # if(read != b''):
    #             #     read2 = read.decode('UTF-8')
    #             #     read2 = read2.strip("\n")
    #
    #                 # with open('data.csv', 'a') as csv_file:
    #                 #     csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #                 #     info = {"time": cnt, "magnitude" : read2, "magnitude2": read}
    #                 #     csv_writer.writerow(info)
    #             # cnt = cnt + 1
    #             #print(cnt)
    #             #print(read)
    #         print ("the total number of samples: ")
    #         print (cnt+1)
    #
    #     except: Exception: print("error")
    # else:
    #     print("can't open serial port")

