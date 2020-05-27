# EmbeddedProject
Project Description: 
I developed a heart monitor that samples the ECG signal obtained from the ECG sensor. The Sensor transmits the ECG reading to the blue pill, which does some processing on the data. This processing includes: converting the analog signal into a digital signal. The digital signal is then used for further analysis including: calculating the BPM rate and transmitting 1 minute worth of digital samples to the PC through UART. On the PC, the digital signal can be plotted against time. 
The application allows the user to choose the Com Port, baud rate and sampling rate of preference. 

Difficulties faced and what I Learnt:
-	Handling multiple interrupts at the same time. When 3 interrupts were activated at the same time the program was so slow
-	Had to use a high sampling rate. Because a low one with the amount of data being sent wasn’t very efficient. The time taken to transmit was longer than the time between two interrupts. Therefore, other necessary parts of the code weren’t executed
-	Not very familiar with python. Unnoticeable mistakes because of being used to the C++ syntax occurred and caused the code to crash

Assumptions:
-	The sampling rate would be in the range of 100 to 1000
-	The user would type Start and then the graph and the BPM would be automatically shown

