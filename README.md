# Line Coding
Line coding is the process of converting digital data to digital signals.Line coding converts a sequence of
bits to a digital signal. At the sender, digital data are encoded into a digital signal; at the
receiver, the digital data are recreated by decoding the digital signal.
# Line Coding Schemes
### Unipolar NRZ (Non-Return-to-Zero)
Unipolar scheme was designed as a non-return-to-zero (NRZ) scheme
in which the **positive voltage defines bit 1 and the zero voltage defines bit 0**. It is called
NRZ because the signal does not return to zero at the middle of the bit
### NRZ-L (NRZ-Level)
The level of the voltage determines the value of the bit.
### NRZ-I  (NRZ-Invert)
The change or lack of change in the level of the voltage determines the value of the bit. **If there is no change, the bit is 0; if there is a change, the
bit is 1.**
### Manchester
The idea of RZ (transition at the middle of the bit) and the idea of NRZ-L are combined
into the Manchester scheme. In Manchester encoding, the duration of the bit is divided
into two halves. The voltage remains at one level during the first half and moves to the
other level in the second half. The transition at the middle of the bit provides synchronization.
### Differential Manchester
Differential Manchester combines the ideas of RZ and
NRZ-I. There is always a transition at the middle of the bit, but the bit values are determined at the beginning of the bit. If the next bit is 0, there is a transition; if the next bit
is 1, there is none.
### AMI ( alternate mark inversion)
A neutral zero voltage represents binary 0. Binary 1s are represented by alternating positive and negative voltages.
### Pseudoternary
A variation of AMI encoding is called pseudoternary in which the 1 bit is encoded as a zero voltage and
the 0 bit is encoded as alternating positive and negative voltages.
### 2B1Q
Two binary, one quaternary (2B1Q), uses data
patterns of size 2 and encodes the 2-bit patterns as one signal element belonging to a
four-level signal. 
# Implementation and Working
The implementation of above LCS done in python.I use matplotlib.pyplot to plot graph and matplotlib.patches to show legend in which I just remind plotting rules.

Its working is very friendly.Take binary string and validate it to ensure it contains only '0's and '1's.In case of any chracter other than binary it prompt to re-enter binary string.On success,it show menu to select Line Coding Scheme.
One interesting thing is that program not stop after showing one output.It will show  menu to select whether you want to continue or exit.Continue  will take you to the start of program.  
