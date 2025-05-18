## Spin-N-Win Assembly and Operation Manual

### ***Specifications ***

Standard Size ( 4’ Wheel ) :

Dimensions: 48”W x 30”D x 96”H
Current: 110 Vac / 6.5 Amps
Weight: Lbs
Shipping Weight:
Created Dimensions: 80”L x 46”W x 861/2” H

### **Assembly Instructions **


1) Remove shipping bracket from base cabinet and remove top cabinet from skid

2) Remove base cabinet from skid and place in approximate final location with room to work behind game.

3) Remove rear wood panel.

4) Place the top cabinet onto the base cabinet and attach with 4 5/16 bolts, washers, and nuts.
Note: bolts go through frame from bottom (nuts on top).

********* ***CAUTION*** *********

***Do not open upper rear door until the top cabinet is attached to base. The weight of the lamp fixtures on the***
***top door will tip the top cabinet.***

5) Remove the shipping brackets from the top cabinet

6) Wire connections:

  - 8 pin (data) pcb connector is plugged into j2 of the left (viewed from the back) lamp driver board.

  - 3 pin (ac) pcb connector is plugged into j1 or j7 of the same board as the data.

  - The other two connections are in-line. A 2 pin (12v) for the color wheel and a 3 pin (120v) for the
fluorescent lamps.

7) Feed the power cord through the hole in the rear panel and re-attach the rear panel.

### **Game Overview **






### **Programming **

**BUTTON** **FUNCTION**

**RESET/MENU** : 1.  Enter the Program Mode
2. Enter the new setting during programming.
3. During a ticket error condition;
Pressing it once will clear the tickets owed and return to attract mode.

**AUX1** 1.  Moves you forward through the selections within an option.
2. Used during diagnostic mode to toggle an output on or off.
3. During a ticket error condition;
Pressing it once will Dispense the number of tickets owed.

**AUX2** 1. Moves you backwards from one option to the next.
2. In Diagnostic mode, it cycles through the different tests.
3. During a ticket error condition;
Pressing it once will Dispense the number of tickets owed.

**AUX1 & AUX2** : When depressed at the same time, they will let you exit the
programming mode or diagnostic mode.






### **Options / Tests / Accounting **

To get in to the Option Menu, press th e ***Test/Menu*** . The seven segment display will display the software revision number ”100A *”*,
followed by the check sum number “ *3AD4* ”. *Actual software revision and check sum will vary* . After a pause, the seven segment
display will show “ *00* “. This is Option 0. Pressing ***AUX1*** or ***AUX2*** will increment or decrement through all the options. Pressing
the ***Test/Menu*** button will select that Option.

***Options:***

**Option 00:** **Select one of the following:**

**Range:** *0*           - Exit change nothing ( Pressing ***Test/Menu*** is the same as Pressing ***AUX1*** and ***AUX2*** Together)
*1*               - Run Diagnostics ( Pressing ***Test/Menu*** will place the game it Diagnostic Mode )
*2*               - Accounting ( Pressing ***Test/Menu*** will place the game it Accounting )

**Option 01:** **Load defaults**

*0*               - Exit change nothing ( Pressing ***Test/Menu*** is the same as Pressing ***AUX1*** and ***AUX2*** Together)
*1* – Load Defaults ( Pressing ***Test/Menu*** the one on the display will flash and set all options to the
factory settings )

**Option 02:** **Number of coins to start a game ( 1-4 )**

**Range:** *1 - 4*
Increment or decrement the value to the desired number of coins. Then press ***Test/Menu*** . The
value on the display will flash to let you know it has been saved.  Pressing ***AUX1*** and ***AUX2***
Together will move back to the Option Selection.

***Default: 2***







**Option 03:** **Change Payout Table ( 1 – 6 ).**

**Range:** *0*           - Exit change nothing Press ***MENU***

*1*               - Set Table #1

*2*               - Set Table #2

*3*               - Set Table #3

*4*               - Set Table #4

5- Set Table #5

*6* – Set Manually ( Pressing the ***MENU*** button will light the #1 bulb on the wheel and the display
will show the current number of tickets . )

*When selected, the lamp on the wheel will light and the current payout value will be displayed. Remember, for each wedge*
*on the wheel, all the lights within that wedge must be individualy programmed with the same value of tickets.*

Use ***AUX1/AUX2*** to change lamps.
Press “ ***Menu*** ” to change the value
Lamp will flash.
***AUX1/AUX2*** to increment/decrement value
Value can be set to: *1*               - *25* (step by 1)
*30*                      - *100* (step by 5)
*110*                      - *500* (step by 10)
*550*                      - 1000 (step by 50)
1100 - *9999* (step by 100)
10000 ( will display as *9999* )
“ ***Menu*** ” to accept and save
Press ***AUX1*** and ***AUX2*** at the same time to exit.

***NOTE: Changing the payout will force Option 4 to 0.***







**Option 4:** Call attendant to give tickets

This option sets the MAXIMUM number of tickets to be dispensed by the machine. Any tickets amounts
equal to or greater than the number set are not dispensed by the machine.  The tickets owed will be
displayed on the 7-Seg display Followed by “CALL 4 HELP”
To clear, the “ ***STOP*** ” button must be pressed and released,
then within 5 seconds pressed and held down until the
display shows “0000” (about 5 seconds).

**Range:** 0 – No call. All tickets paid out
Lowest to Highest Payout value
*9999* ***MAXIMUM number of tickets to be dispensed***
***Default: 0***

**Option5** : Tickets given if none won in game play.
This is the number of tickets to be dispensed if the player doesn’t press the STOP button or walked away
from the game, before option #10 has timed-out.

**Range** *0 -* 10 tickets
***Default: 5***

Option *6* : Value of ticket
**Range** *1*              - *4* tickets
***Default: 1***

Option *7* : Tickets Alarm Enable
**Range** *0*           - Disabled
*1* – Enabled
***Default: Enabled*** (Halt play until tickets are reloaded)

**Option** *8* : Jackpot Window Times
This option makes it easier or harder to win the Jackpot. 20 Easiest, 2 Hardest
**Range** *2* – *20* milliseconds
***Default: 5***

**Option** *9* : No pull timeout
**Range** *0* Start on Coin Drop
*5* – *30* seconds (5 second steps)
***Default: 15***

**Option** *10* : No play timeout
**Range** *0*, *20* – *90* seconds (5 second steps)
***Default: 20***

**Option** *11* : End of Game time
**Range** *1*           - *20* seconds
***Default: 4***







**Option 12** : Sound Volume
**Range** *1* – *9*
***Default: 5***
**Option 13** : Activate Attract Sound
**Range** 0 – 9 minutes
***Default: 2***

**Option 14** : Jackpot Bell
**Range** 0 – 9 minutes Enable *1* or Disable *0*
***Default: 1*** (enabled)






#### ***Test ***

There are 3 tests mode (Outputs, Inputs, Sound) that can be selected through Option 0. After “2” is
selected from Option 0 the 3 digits will display “_00” – “_02”. Press the “Reset” button to select the

test.

**Test 00** : Outputs.
Use the Aux1/Aux2 buttons to move through the outputs
Use RESET to toggle on and off.
AUX1 and AUX2 together to exit
00 = Odd # lamps (Marquee, Inner Ring, & Outer Ring)
01 = Even # lamps (Marquee, Inner Ring, & Outer Ring)
02 = Chase LEDs

03 = Stop Button Lamp
04 = Counters

05 = Handle Lock Solenoid

06 = Color Wheel Motor

07 = Ticket Motor
08 = TCALL lamp (optional)

**Test 01** : Inputs.
Use the Aux1/Aux2 buttons to move through the inputs
0=open, 1=closed
AUX1 and AUX2 together to exit
00 = Stop button
01 = Handle Lower Limit switch/sensor

02 = Ticket Notch

03 = Coin1 switch

04 = Coin2 switch.
05 = TCALL switch (optional)







**Test 02** :Sounds.
Use the Aux1/Aux2 buttons to move through the sounds
Use TEST to replay a sound.
AUX1 and AUX2 together to exit
00

01   "COININ.WAV"

02   "TIX PAYOUT2.WAV"

03   "ALARM_BUZZER.WAV"
04   "MUSIC LOOP.WAV"

05   "BIGSIXWHEEL2.WAV"

06   "HANDLE PULL5.WAV"

07   "PRESS TO STOP.WAV"

08   "POWERUP2.WAV"

09   "ATTRACT3.WAV"

10   "SPINNIN N WINNIN.WAV"

11   "PULLHANDLE1.WAV"

12   "THANKS FOR PLAYING_02.WAV"
13   "TRY AGAIN_02.WAV"
14

15   "COININ.WAV"

16   "TIX PAYOUT2.WAV"

17   "ALARM_BUZZER.WAV"
18   "MUSIC LOOP.WAV"

19   "BIGSIXWHEEL2.WAV"

20   "HANDLE PULL5.WAV"

21   "PRESS TO STOP.WAV"

22   "WHEELSTOP4.WAV"

23   "JACKPOT1.WAV"






#### ***Accountings ***

**Account 00** : Soft counters
On entry 7seg display will show “ 0 “ then scroll the value for counter #0.
The counter will be scrolled as “_00-00-00_”.

Press the AUX1 button to move up through the counters.
Press the AUX2 button to move back through the counters.
Pressing AUX1 and AUX2, when the display is not scrolling, will exit the test.

Counter 0: Games played
Counter 1: Games ended on jackpot.
Counter 2: Total Tickets given
Counter 3: Tickets per game
#### ***Error Codes ***

Upon encountering an error condition the 7seg display will flash “Er” plus the error condition code
(0-9) and make an alarm sound. So for a ticket error the 7seg display will flash “Er0”. After flashing the
error code the display will scroll “CALL 4 HELP”. The sequence will keep repeating until the ***AUX1***
***button*** is pressed or the game is reset.

***ErrC***      - Checksum Error.
On power up the checksum for the protected memory did not match or the
Program ROM has been updated.

When this is displayed ALL defaults have been restored and ALL
Soft-counters have been reset.

Pressing ***“*** ***STOP*** ***”*** ***button*** will cause the game to reset and reload the
protected memory..

On power up holding both the ***AUX1 and AUX2 buttons*** down will force
a checksum failure.







***ErrD***      - Checksum Error.

***ErrE***      - Checksum Error.

***Err0***       - Ticket Error.
The ticket machine was unable to dispense tickets due to either running out of tickets or a ticket
jam.

Clear the ticket jam and/or Reload the Tickets. When the optic sensor is blocked by reloading
the ticket dispenser, the game will display the number of tickets owed and th e ***Stop button*** will
flash. Press the Stop button to begin dispensing tickets.

Pressing “ ***Menu*** ” will clear any tickets owed.

If the optional ***TCALL*** switch is installed, activating it will show the
tickets owed and deactivating it will clear the tickets.






### **Cleaning and Routine Maintenance **

1. Polycarbonate Panels:

Skee-Ball, Inc. recommends using only “Kleenmaster Brillianize” which can be purchased through
Skee-Ball as Part Number 800600-1.

2. Electronics Board:

Skee Ball Inc. recommends using canned air to blow any dirt off the surface of the Electronics board.

3. Laminated Surfaces:

Skee-Ball, Inc. recommends “Kleenmaster Brillianize”.

4. Optical Sensors:

Skee-Ball, Inc. recommends using canned air to blow any dirt off of the surface of the sensors on a
weekly basis.

5. Hinges

Monthly, lightly spray the Ball Gate hinges with a light lubricant.

6. Painted Surfaces:

Skee Ball Inc. recommends using Windex or any other mild, non-abrasive household cleaner.






## **Electronics Schamatic **

**Overall System Components:**

1.  **LOGIC BOARD EA3729F1:** The central control board.
2.  **LAMP DRIVER 1, 2, 3, 4, 5:** Boards to drive lamps.
3.  **4 DIG. DISP.:** 4-digit display.
4.  **POWER SUPPLY EA2508:** Provides various DC and AC voltages.
5.  **SPKR(L) MS161:** Speaker.
6.  **COIN DOOR EA4166:** Coin mechanism interface.
7.  **TICKET DOOR (L) SM4131-1:** Ticket dispenser interface.
8.  **HANDLE SWITCH:** Input switch.
9.  **STOP BUTTON:** Input switch.
10. **ARROW LED PCB:** PCB for arrow indicator LEDs.
11. **STOP STROBE:** Strobe light assembly.
12. **LOAD:** An inductive load or solenoid.
13. **BELL:** A physical bell.
14. **COLOR MOTOR:** Motor for a color wheel or similar.
15. **Various Switches:** TEST, AUX 1, AUX 2, "6' ONLY" config switch.
16. **AC Input Assembly:** 3-way AC plug, main switch, fuse.

**Connections Details:**

**I. POWER INPUT & MAIN POWER SUPPLY (EA2508):**

*   **AC Input:**
    *   TO 3 WAY AC PLUG:
        *   BLK (Live) -> Main Power Switch (Terminal 1)
        *   WHT (Neutral) -> Main Power Switch (Terminal 2)
        *   GRN (Earth) -> Chassis Ground & POWER SUPPLY EA2508 Pin 2 (AC E)
    *   Main Power Switch Output:
        *   BLK (Live from Terminal 1) -> FUSE
        *   WHT (Neutral from Terminal 2) -> POWER SUPPLY EA2508 Pin 1 (AC N)
    *   FUSE Output:
        *   BLK (Live) -> POWER SUPPLY EA2508 Pin 3 (AC L)

*   **POWER SUPPLY EA2508 Outputs:**
    *   **Connector J1 (DC to LOGIC BOARD via 52022-8):**
        *   Pin 1 (+12VDC, YEL) -> LOGIC BOARD J1.1 (+12VDC)
        *   Pin 2 (GND, BLK) -> LOGIC BOARD J1.2 (GND)
        *   Pin 3 (+5VDC, RED) -> LOGIC BOARD J1.3 (+5VDC)
        *   Pin 4 (GND, BLK) -> LOGIC BOARD J1.4 (GND)
    *   **Connector J2 (AC to LOGIC BOARD and local AC loads):**
        *   Pin 1 (AC HOT, RED) -> LOGIC BOARD J2.1 (AC HOT)
        *   Pin 2 (AC N, BLK) -> LOGIC BOARD J2.2 (AC N)
        *   Pin 3 (EARTH, GRN) -> LOGIC BOARD J2.3 (EARTH)
    *   **Connector J3 (Switched AC Outputs, connected to LOGIC BOARD J3):**
        *   PS J3.1 (AC OUT, YEL) <-> LOGIC BOARD J3.9 (AC OUT)  *(Note: diagram shows YEL from PS J3.1 to LB J3.1)*
        *   PS J3.2 (AC N, BLK) <-> LOGIC BOARD J3.8 (AC N) *(Note: diagram shows BLK from PS J3.2 to LB J3.2)*
        *   PS J3.3 (SHLD) - No connection shown
        *   PS J3.4 (AC N, BLK) <-> LOGIC BOARD J3.6 (AC N)
        *   PS J3.5 (AC OUT, WHT) <-> LOGIC BOARD J3.5 (AC OUT)
        *   PS J3.6 (AC N, BLK) <-> LOGIC BOARD J3.4 (AC N)
        *   PS J3.7 (AC OUT, BLU) <-> LOGIC BOARD J3.7 (AC OUT)
        *   PS J3.8 (AC N) - No connection shown on PS side to LB
        *   PS J3.9 (AC OUT) - No connection shown on PS side to LB
        *(The LOGIC BOARD J3 pins are labeled 1-9: AC OUT, AC N, SHLD, AC N, AC OUT, AC N, AC OUT, AC N, AC OUT. The connections are:
        PS J3.9(YEL) to LB J3.1(AC OUT), PS J3.8(BLK) to LB J3.2(AC N)
        PS J3.7(BLU) to LB J3.3(AC OUT), PS J3.6(BLK) to LB J3.4(AC N)
        PS J3.5(WHT) to LB J3.5(AC OUT), PS J3.4(BLK) to LB J3.6(AC N)
        This needs to be interpreted as three AC pairs from PS J3 to LB J3.)*

    *   **Output to COLOR MOTOR (via 52022-10:**
        *   PS J3.1 (AC OUT, YEL) -> COLOR MOTOR Pin 1 (RED wire on motor)
        *   PS J3.2 (AC N, BLK) -> COLOR MOTOR Pin 2 (BLK wire on motor)
    *   **Output to LAMP DRIVER 1:**
        *   3-pin connector:
            *   Pin 1 (WHT) -> LAMP DRIVER 1, Input Pin 1 (+12V)
            *   Pin 2 (GRN) -> LAMP DRIVER 1, Input Pin 2 (+5V)
            *   Pin 3 (BLK) -> LAMP DRIVER 1, Input Pin 3 (GND)

**II. LOGIC BOARD EA3729F1 Connections:**

*   **J1 (DC Power Input from POWER SUPPLY J1 via 52022-8):**
    *   Pin 1: +12VDC (from PS J1.1, YEL)
    *   Pin 2: GND (from PS J1.2, BLK)
    *   Pin 3: +5VDC (from PS J1.3, RED)
    *   Pin 4: GND (from PS J1.4, BLK)
*   **J2 (AC Power Input from POWER SUPPLY J2):**
    *   Pin 1: AC HOT (from PS J2.1, RED)
    *   Pin 2: AC N (from PS J2.2, BLK)
    *   Pin 3: EARTH (from PS J2.3, GRN)
*   **J3 (AC Power distribution with POWER SUPPLY J3):**
    *   Pin 1: AC OUT (YEL, to PS J3.9)
    *   Pin 2: AC N (BLK, to PS J3.8)
    *   Pin 3: AC OUT (BLU, to PS J3.7)
    *   Pin 4: AC N (BLK, to PS J3.6)
    *   Pin 5: AC OUT (WHT, to PS J3.5)
    *   Pin 6: AC N (BLK, to PS J3.4)
    *   Pin 7: AC OUT
    *   Pin 8: AC N
    *   Pin 9: SHLD (Note: the diagram shows J3.1-J3.9 with labels AC OUT, AC N, SHLD, AC N, AC OUT, AC N, AC OUT, AC N, AC OUT. The connections above based on wire paths are slightly different in order than this labeling if it implies PS J3 pin numbers directly. The re-interpretation of PS J3 to LB J3 connections is complex).
*   **J14 (Outputs to various devices via 52022-11):**
    *   Pin 1: SHLD
    *   Pin 2: ARROW LED 1 -> ARROW LED PCB Pin 3
    *   Pin 3: ARROW LED 2 -> ARROW LED PCB Pin 2
    *   Pin 4: ARROW LED 3 -> ARROW LED PCB Pin 1
    *   Pin 5: ARROW LED SHLD -> ARROW LED PCB Pin 4
    *   Pin 6: STOP LAMP (RED) -> STOP STROBE Pin 1
    *   Pin 7: LOCK OUT (YEL) -> "LOAD" (solenoid/device) Pin 1
    *   Pin 8: +12VDC (BLK) -> Common +12V for STOP STROBE Pin 2, "LOAD" Pin 2
    *   Pin 9: GND
    *   Pin 10: +12VDC
    *   Pin 11: HANDLE SOLENOID (RED) -> "BELL" (solenoid/device) Pin 1
    *   Pin 12: +12VDC (BLK) -> "BELL" Pin 2
    *   Pins 13, 14, 15: +12VDC
*   **J15 (Inputs from Switches via 52022-12):**
    *   Pin 1: SHLD (WHT wire in cable) -> COM of HANDLE SWITCH, also common for other switches.
    *   Pin 2: HANDLE DOWN (No connection shown in this specific diagram)
    *   Pin 3: HANDLE UP (WHT wire in cable) -> NO of HANDLE SWITCH
    *   Pin 4: STOP BUTTON (RED wire in cable) -> STOP BUTTON Pin 1 (Pin 2 of Stop Button is common/SHLD)
    *   Pin 5: 6 FOOT GAME SELECT (BLK wire in cable) -> COM of "6' ONLY" Switch (NO contact of this switch goes to common/SHLD)
    *   Pin 6: +12VDC
*   **J16 (Switch connections via 52022-12):**
    *   Pin 1: +12VDC (RED wire in cable) -> COM of a 3-position switch.
    *   Pin 2: GND (BLK wire in cable) -> NC of another 3-position switch, also common/SHLD.
*   **J17 (To COIN DOOR EA4166 via 52022-14):**
    *   Pin 1: SHLD
    *   Pin 2: COIN COUNTER (BLU) -> COIN DOOR CTR Pin 2
    *   Pin 3: +12VDC
    *   Pin 4: GND (BLK) -> Common with J17.8
    *   Pin 5: +5VDC
    *   Pin 6: COIN 1 (RED) -> COIN DOOR COIN Pin 1
    *   Pin 7: COIN 2 ("6' ONLY" - no connection to this specific coin door)
    *   Pin 8: GND (BLK) -> COIN DOOR CTR Pin 1
*   **J18 (To TICKET DOOR SM4131-1 via 52022-15):**
    *   Pin 1: SHIELD
    *   Pin 2: TKT COUNTER (GRN) -> TICKET DOOR Pin 4
    *   Pin 3: +12VDC (YEL) -> TICKET DOOR Pin 3
    *   Pin 4: TKT NOTCH (RED) -> TICKET DOOR Pin 2
    *   Pin 5: +12VDC
    *   Pin 6: GND (BLK) -> TICKET DOOR Pin 1
    *   Pin 7: TKT MOTOR (ORG) -> (To Ticket Motor, part of SM4131-1 assembly)
    *   Pin 8: +5VDC
    *   Pin 9: GND
*   **J20 (To TEST/AUX Switches via 52022-16):**
    *   Pin 1: SHLD
    *   Pin 2: TEST (RED) -> TEST Switch Pin 1
    *   Pin 3: AUX 2 (WHT) -> AUX 2 Switch Pin 1
    *   Pin 4: AUX 1 (GRN) -> AUX 1 Switch Pin 1
    *   Pin 5: GND (BLK) -> Common Pin 2 for TEST, AUX 2, AUX 1 Switches
*   **J21 (AC Control Signals "TO P.S. AC OUT"):**
    *   Pin 1: YEL
    *   Pin 2: BLU
    *   Pin 3: WHT
    *(These are likely control signals to the Power Supply to switch specific AC outputs available on PS J3, which then feed back to LB J3. Or they directly drive AC loads if the PS J3 outputs are parallel.)*
*   **J22 (To 4 DIG. DISP. and SPKR(L) MS161):**
    *   **To SPKR(L) MS161 (via 52022-13):**
        *   Pin 1 (RED) -> SPKR(L) Pin 1
        *   Pin 2 (BLK) -> SPKR(L) Pin 2
    *   **To 4 DIG. DISP. (via 52022-1):**
        *   Pin 3: LED + (12V) (ORG) - Not directly to 4 DIG. DISP., but part of the bus
        *   Pin 4: LED + (12V) (ORG) - Not directly to 4 DIG. DISP.
        *   Pin 5: LED - (GND) (GRN) - Not directly to 4 DIG. DISP.
        *   Pin 6: LED - (GND) (GRN) - Not directly to 4 DIG. DISP.
        *   Pin 7: S-CLK (BRN) -> 4 DIG. DISP. Pin 3 (S-CLK)
        *   Pin 8: S-ENBL (BLU) -> 4 DIG. DISP. Pin 5 (S-ENBL)
        *   Pin 9: S-DATA (WHT) -> 4 DIG. DISP. Pin 4 (S-DATA)
        *   Pin 10: S-STRB (YEL) -> 4 DIG. DISP. Pin 6 (S-STRB)
        *   Pin 11: GND (BLK) -> 4 DIG. DISP. Pin 2 (GND)
        *   Pin 12: 5V (RED) -> 4 DIG. DISP. Pin 1 (5V)
        *(4 DIG. DISP also takes 12V (ORG) to its Pin 1, which is labeled 12V. This might be an error in my J22 pin 12 interpretation or the display has multiple power inputs. J22.12 is 5V. The 4 Dig Disp input pin 1 is ORG and labeled 12V. Its pin 2 is RED labeled 5V. So:
        4 DIG. DISP Pin 1 (12V, ORG) <- J22.3 or J22.4 (12V, ORG)
        4 DIG. DISP Pin 2 (5V, RED) <- J22.12 (5V, RED)
        4 DIG. DISP Pin 3 (GND, GRN) <- J22.11 (GND, BLK)
        4 DIG. DISP Pin 4 (S-CLK, BRN) <- J22.7 (S-CLK, BRN)
        4 DIG. DISP Pin 5 (S-DATA, WHT) <- J22.9 (S-DATA, WHT)
        4 DIG. DISP Pin 6 (S-ENBL, BLU) <- J22.8 (S-ENBL, BLU)
        4 DIG. DISP Pin 7 (S-STRB, YEL) <- J22.10 (S-STRB, YEL)
        The cable 52022-1 connects 4 DIG. DISP. pins 1-6 to J22 pins (ORG, RED, GRN, BLK, BRN, WHT, BLU, YEL) which map to J22 pins (12,11,7,9,8,10 respectively for signals, plus power).
        It seems the 4 Dig Disp uses: ORG(12V), RED(5V), GRN(GND), BLK(L-GND), BRN(S-CLK), WHT(S-DATA), BLU(S-STRB), YEL(S-ENBL) which are available from J22 and become the bus for Lamp Drivers)*

**III. 4 DIG. DISP. and LAMP DRIVER CHAIN:**

*   **4 DIG. DISP. Input (from LOGIC BOARD J22 via 52022-1):**
    *   Pin 1: 12V (ORG)
    *   Pin 2: 5V (RED)
    *   Pin 3: GND (GRN)
    *   Pin 4: S-CLK (BRN) (Diagram shows BLK L GND for pin 4 on display side)
    *   Pin 5: S-DATA (WHT) (Diagram shows BRN S-CLK for pin 5 on display side)
    *   Pin 6: S-ENBL (BLU) (Diagram shows WHT S-DATA for pin 6 on display side)
    *   Pin 7: S-STRB (YEL) (Diagram shows BLU S-STRB for pin 7 on display side)
    *   Pin 8: (Not labeled on display side but YEL S-ENBL is the last signal from J22)
    *(Re-checking 4 DIG. DISP input from J22 via 52022-1:
    J22.12 (RED, 5V) -> Disp Pin 2 (5V)
    J22.11 (BLK, GND) -> Disp Pin 3 (GND)
    J22.10 (YEL, S-STRB) -> Disp Pin 7 (S-STRB)
    J22.9 (WHT, S-DATA) -> Disp Pin 6 (S-DATA)
    J22.8 (BLU, S-ENBL) -> Disp Pin 8 (S-ENBL) (assuming Disp has 8 pins for this connector)
    J22.7 (BRN, S-CLK) -> Disp Pin 5 (S-CLK)
    J22.3/4 (ORG, 12V) -> Disp Pin 1 (12V)
    The Disp also has a BLK L-GND on its Pin 4, which is not clearly sourced from J22.
    The cable 52022-1 is an 8-wire cable. The 4 DIG. DISP block shows 8 input pins and 8 output pins.
    Input pins (color from J22 / 52022-1): 1:ORG(12V), 2:RED(5V), 3:GRN(GND), 4:BLK(L-GND), 5:BRN(S-CLK), 6:WHT(S-DATA), 7:BLU(S-STRB), 8:YEL(S-ENBL).
    This full set of 8 signals/power lines passes from 4 DIG. DISP output to LAMP DRIVER 1 input via 52022-5.)*

*   **LAMP DRIVER General Connections:**
    *   **Input Bus (8-pin connector, e.g., 52022-5 for LD1 from 4 DIG. DISP.):**
        *   Pin 1: ORG (+12V)
        *   Pin 2: RED (+5V)
        *   Pin 3: GRN (GND)
        *   Pin 4: BLK (L GND)
        *   Pin 5: BRN (S-CLK)
        *   Pin 6: WHT (S-DATA)
        *   Pin 7: BLU (S-STRB)
        *   Pin 8: YEL (S-ENBL)
    *   **Output (3-pin connector, e.g., 52022-2 from LD1 to LD2):**
        *   Pin 1: WHT (S-ENBL_OUT)
        *   Pin 2: GRN (S-STRB_OUT)
        *   Pin 3: BLK (S-CLK_OUT)
    *   **Daisy Chain Logic:**
        *   The main bus (Pins 1,2,3,4,6 of the 8-pin input) is paralleled to all Lamp Drivers.
        *   The signals S-CLK, S-STRB, S-ENBL are daisy-chained:
            *   Output of LDx (WHT, GRN, BLK) connects to Input Pins 8 (YEL), 7 (BLU), 5 (BRN) respectively of LDx+1.
    *   **Specific Daisy Chain Cables:**
        *   4 DIG. DISP. Output (8 pins) -> 52022-5 -> LAMP DRIVER 1 Input (8 pins)
        *   LAMP DRIVER 1 Output (3 pins) -> 52022-2 -> LAMP DRIVER 2 Input (pins 5,7,8)
        *   LAMP DRIVER 2 Output (3 pins) -> 52022-6 -> LAMP DRIVER 3 Input (pins 5,7,8)
        *   LAMP DRIVER 3 Output (3 pins) -> 52022-3 -> LAMP DRIVER 4 Input (pins 5,7,8)
        *   LAMP DRIVER 4 Output (3 pins) -> 52022-7 -> LAMP DRIVER 5 Input (pins 5,7,8)
        *   LAMP DRIVER 5 is the last in the chain.
    *   **Power for LAMP DRIVER 1:**
        *    Powered directly from POWER SUPPLY EA2508 output (WHT=+12V, GRN=+5V, BLK=GND).

**IV. Other Peripheral Components & Switches:**

*   **ARROW LED PCB (connected to LB J14 via 52022-11):**
    *   Pin 1: ARROW LED 3 (from J14.4)
    *   Pin 2: ARROW LED 2 (from J14.3)
    *   Pin 3: ARROW LED 1 (from J14.2)
    *   Pin 4: SHLD (from J14.5)
*   **STOP STROBE (connected to LB J14 via 52022-11):**
    *   Pin 1: STOP LAMP (from J14.6, RED wire)
    *   Pin 2: +12VDC (from J14.8, BLK wire)
*   **"LOAD" (solenoid/device, connected to LB J14 via 52022-11):**
    *   Pin 1: LOCK OUT (from J14.7, YEL wire)
    *   Pin 2: +12VDC (from J14.8, BLK wire)
*   **"BELL" (solenoid/device, connected to LB J14 via 52022-11):**
    *   Pin 1: HANDLE SOLENOID (from J14.11, RED wire)
    *   Pin 2: +12VDC (from J14.12, BLK wire)
*   **Separate AC Circuit for Bell/Load (near Power Supply):**
    *   **Physical BELL component:**
        *   Terminal 1: YEL wire, connects to Physical LOAD component Terminal 1.
        *   Terminal 2: RED wire, connects to one end of 10 OHM Resistor.
    *   **10 OHM Resistor:**
        *   One end: RED wire to Physical BELL Terminal 2.
        *   Other end: RED wire, T-junction to AC HOT (RED wire between LB J2.1 and PS J2.1).
    *   **Physical LOAD component (coil symbol):**
        *   Terminal 1: YEL wire, connects to Physical BELL component Terminal 1.
        *   Terminal 2: BLK wire, T-junction to AC N (BLK wire between LB J2.2 and PS J2.2).
*   **COLOR MOTOR (connected to PS J3 via 52022-10):**
    *   Pin 1 (RED wire on motor): YEL wire from PS J3.1 (AC OUT)
    *   Pin 2 (BLK wire on motor): BLK wire from PS J3.2 (AC N)
*   **HANDLE SWITCH (part of 52022-12):**
    *   COM: BLK wire (commoned with J15.1 SHLD, J16.2 GND, and other switch commons)
    *   NO: WHT wire (to J15.3 HANDLE UP)
*   **STOP BUTTON (part of 52022-12):**
    *   Pin 1: RED wire (to J15.4 STOP BUTTON)
    *   Pin 2: BLK wire (common/SHLD)
*   **"6' ONLY" Switch (3-position, part of 52022-12):**
    *   COM: BLK wire (to J15.5 6 FOOT GAME SELECT)
    *   NO: BLK wire (common/SHLD)
    *   NC: Not connected
*   **Other Configuration Switches (part of 52022-12):**
    *   Switch A (3-pos): COM -> RED wire from J16.1 (+12VDC). NO/NC not connected.
    *   Switch B (3-pos): NC -> BLK wire (common/SHLD from J16.2 GND). COM/NO not connected.
*   **COIN DOOR EA4166 (connected to LB J17 via 52022-14):**
    *   CTR Pin 1: BLK wire (to J17.8 GND)
    *   CTR Pin 2: BLU wire (to J17.2 COIN COUNTER)
    *   COIN Pin (single): RED wire (to J17.6 COIN 1)
*   **TICKET DOOR (L) SM4131-1 (connected to LB J18 via 52022-15):**
    *   Pin 1 (BLK): GND (to J18.6)
    *   Pin 2 (RED): TKT NOTCH (to J18.4)
    *   Pin 3 (YEL): +12VDC (to J18.3)
    *   Pin 4 (GRN): TKT COUNTER (to J18.2)


### **Trouble-shooting Guide **

The purpose of this guide is to help you pinpoint a problem area and eliminate the undue process of parts
swapping, expedite shipping charges and other hassles associated with a breakdown due to unknown causes. In
order to successfully follow this guide, it is imperative the individual understands the overall play of the game
and its test functions.

Reading the Game Play portion of the Assembly /Operating Manual will enable one to better understand how
and when certain functions relating to hardware (physical printed circuit board an components thereof) and
software (the program which actually commands the hardware) interact.

Reading the test portion of the Assembly/Operating Manual will enable one to pinpoint the problem area
quickly.

The overall content is written according to the most common problems of which
Skee-Ball Inc. has been aware. Listed below are general descriptions of the principal problems and suggested
point to troubleshoot.

Color Wheel is not spinning Check for 12 Vdc across the motor.

Check for broken or loose cable.

Replace color wheel motor

Check color wheel is seated between drive wheel and idler
Bearings.

One half of the light circle or Check data cables to and from lamp driver boards
Marquee lights not working
Check AC power cables

When game is turned on the bell Replace logic board.
continues to ring, lights are
flashing and tickets continues

to run.







Display shows “Err C” Pressing the “STOP” button will reset the game
and clear the error. If the problem continues
replace the logic board.

Display shows “Err 1” (Ticket Error) Refill tickets
Remove any tickets jammed in the dispenser
Clean the optic eye on dispenser
Replace the dispenser
