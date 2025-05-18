# Spin-N-Win Assembly and Operation Manual

## Specifications

### Standard Size (4’ Wheel)
-   **Dimensions:** 48”W x 30”D x 96”H
-   **Current:** 110 Vac / 6.5 Amps
-   **Weight:** [Value Not Specified] Lbs
-   **Shipping Weight:** [Value Not Specified]
-   **Crated Dimensions:** 80”L x 46”W x 86 1/2” H

## Assembly Instructions

1.  Remove shipping bracket from base cabinet and remove top cabinet from skid.
2.  Remove base cabinet from skid and place in approximate final location with room to work behind game.
3.  Remove rear wood panel.
4.  Place the top cabinet onto the base cabinet and attach with 4x 5/16 bolts, washers, and nuts.
    *   **Note:** Bolts go through frame from bottom (nuts on top).

>   ***CAUTION***
>   ***Do not open upper rear door until the top cabinet is attached to base. The weight of the lamp fixtures on the top door will tip the top cabinet.***

5.  Remove the shipping brackets from the top cabinet.
6.  **Wire connections:**
    *   8 pin (data) pcb connector is plugged into J2 of the left (viewed from the back) lamp driver board.
    *   3 pin (AC) pcb connector is plugged into J1 or J7 of the same board as the data.
    *   The other two connections are in-line:
        *   A 2 pin (12V) for the color wheel.
        *   A 3 pin (120V) for the fluorescent lamps.
7.  Feed the power cord through the hole in the rear panel and re-attach the rear panel.

## Game Overview
*(Section intentionally left blank in original document)*

## Programming

### Button Functions

-   **RESET/MENU**:
    1.  Enter the Program Mode.
    2.  Enter the new setting during programming.
    3.  During a ticket error condition: Pressing it once will clear the tickets owed and return to attract mode.

-   **AUX1**:
    1.  Moves you forward through the selections within an option.
    2.  Used during diagnostic mode to toggle an output on or off.
    3.  During a ticket error condition: Pressing it once will Dispense the number of tickets owed.

-   **AUX2**:
    1.  Moves you backwards from one option to the next.
    2.  In Diagnostic mode, it cycles through the different tests.
    3.  During a ticket error condition: Pressing it once will Dispense the number of tickets owed.

-   **AUX1 & AUX2** (pressed at the same time):
    1.  Exit the programming mode or diagnostic mode.

## Options / Tests / Accounting

**Entering Option Menu:**
1.  Press the **Test/Menu** button.
2.  The seven-segment display will show the software revision number (e.g., "*100A \**"), followed by the checksum number (e.g., "*3AD4\*"). *Actual software revision and checksum will vary.*
3.  After a pause, the seven-segment display will show "*00*". This is Option 0.
4.  Pressing **AUX1** or **AUX2** will increment or decrement through all the options.
5.  Pressing the **Test/Menu** button will select that Option.

### Options

-   **Option 00: Select Mode**
    -   **Range:**
        -   *0* - Exit change nothing (Pressing **Test/Menu** is the same as Pressing **AUX1** and **AUX2** Together)
        -   *1* - Run Diagnostics (Pressing **Test/Menu** will place the game in Diagnostic Mode)
        -   *2* - Accounting (Pressing **Test/Menu** will place the game in Accounting Mode)

-   **Option 01: Load Defaults**
    -   **Range:**
        -   *0* - Exit change nothing (Pressing **Test/Menu** is the same as Pressing **AUX1** and **AUX2** Together)
        -   *1* - Load Defaults (Pressing **Test/Menu** the one on the display will flash and set all options to factory settings)

-   **Option 02: Number of coins to start a game**
    -   **Range:** *1 - 4*
    -   Increment or decrement the value to the desired number of coins. Then press **Test/Menu**. The value on the display will flash to let you know it has been saved. Pressing **AUX1** and **AUX2** Together will move back to the Option Selection.
    -   **Default:** *2*

-   **Option 03: Change Payout Table**
    -   **Range:**
        -   *0* - Exit change nothing (Press **MENU**)
        -   *1* - Set Table #1
        -   *2* - Set Table #2
        -   *3* - Set Table #3
        -   *4* - Set Table #4
        -   *5* - Set Table #5
        -   *6* - Set Manually (Pressing the **MENU** button will light the #1 bulb on the wheel and the display will show the current number of tickets.)
    -   **Manual Setting (if Range *6* is selected):**
        -   When selected, the lamp on the wheel will light and the current payout value will be displayed.
        -   *Remember, for each wedge on the wheel, all the lights within that wedge must be individually programmed with the same value of tickets.*
        -   Use **AUX1/AUX2** to change lamps.
        -   Press **Menu** to change the value.
        -   Lamp will flash.
        -   Use **AUX1/AUX2** to increment/decrement value.
        -   **Value can be set to:**
            -   *1* - *25* (step by 1)
            -   *30* - *100* (step by 5)
            -   *110* - *500* (step by 10)
            -   *550* - *1000* (step by 50)
            -   *1100* - *9999* (step by 100)
            -   *10000* (will display as *9999*)
        -   Press **Menu** to accept and save.
        -   Press **AUX1** and **AUX2** at the same time to exit.
    -   **NOTE:** Changing the payout will force Option 4 to 0.

-   **Option 04: Call attendant to give tickets**
    -   This option sets the MAXIMUM number of tickets to be dispensed by the machine. Any ticket amounts equal to or greater than the number set are not dispensed by the machine. The tickets owed will be displayed on the 7-Seg display followed by “CALL 4 HELP”.
    -   To clear: The **STOP** button must be pressed and released, then within 5 seconds pressed and held down until the display shows “0000” (about 5 seconds).
    -   **Range:**
        -   *0* – No call. All tickets paid out.
        -   Lowest to Highest Payout value.
        -   *9999* - MAXIMUM number of tickets to be dispensed.
    -   **Default:** *0*

-   **Option 05: Tickets given if none won in game play**
    -   This is the number of tickets to be dispensed if the player doesn’t press the STOP button or walked away from the game, before option #10 has timed-out.
    -   **Range:** *0 - 10* tickets
    -   **Default:** *5*

-   **Option 06: Value of ticket**
    -   **Range:** *1 - 4* tickets
    -   **Default:** *1*

-   **Option 07: Tickets Alarm Enable**
    -   **Range:**
        -   *0* - Disabled
        -   *1* - Enabled (Halt play until tickets are reloaded)
    -   **Default:** *Enabled* (1)

-   **Option 08: Jackpot Window Times**
    -   This option makes it easier or harder to win the Jackpot. 20 Easiest, 2 Hardest.
    -   **Range:** *2 - 20* milliseconds
    -   **Default:** *5*

-   **Option 09: No pull timeout**
    -   **Range:**
        -   *0* - Start on Coin Drop
        -   *5 - 30* seconds (5 second steps)
    -   **Default:** *15*

-   **Option 10: No play timeout**
    -   **Range:** *0, 20 - 90* seconds (5 second steps)
    -   **Default:** *20*

-   **Option 11: End of Game time**
    -   **Range:** *1 - 20* seconds
    -   **Default:** *4*

-   **Option 12: Sound Volume**
    -   **Range:** *1 - 9*
    -   **Default:** *5*

-   **Option 13: Activate Attract Sound**
    -   **Range:** *0 - 9* minutes
    -   **Default:** *2*

-   **Option 14: Jackpot Bell**
    -   **Range:**
        -   *0* - Disable
        -   *1* - Enable
    -   **Default:** *1* (enabled)

## Test Modes

**Entering Test Mode:**
1.  Select Option 00.
2.  Set Range to *1* (Run Diagnostics).
3.  Press **Test/Menu**. The 3 digits will display “_00” – “_02”.
4.  Press the **Reset** button to select the test.

### Test 00: Outputs
-   Use **AUX1/AUX2** buttons to move through the outputs.
-   Use **RESET** to toggle on and off.
-   Press **AUX1** and **AUX2** together to exit.
-   Outputs:
    -   *00* = Odd # lamps (Marquee, Inner Ring, & Outer Ring)
    -   *01* = Even # lamps (Marquee, Inner Ring, & Outer Ring)
    -   *02* = Chase LEDs
    -   *03* = Stop Button Lamp
    -   *04* = Counters
    -   *05* = Handle Lock Solenoid
    -   *06* = Color Wheel Motor
    -   *07* = Ticket Motor
    -   *08* = TCALL lamp (optional)

### Test 01: Inputs
-   Use **AUX1/AUX2** buttons to move through the inputs.
-   Display shows: *0* = open, *1* = closed.
-   Press **AUX1** and **AUX2** together to exit.
-   Inputs:
    -   *00* = Stop button
    -   *01* = Handle Lower Limit switch/sensor
    -   *02* = Ticket Notch
    -   *03* = Coin1 switch
    -   *04* = Coin2 switch
    -   *05* = TCALL switch (optional)

### Test 02: Sounds
-   Use **AUX1/AUX2** buttons to move through the sounds.
-   Use **TEST** to replay a sound.
-   Press **AUX1** and **AUX2** together to exit.
-   Sounds:
    -   *00*
    -   *01* = "COININ.WAV"
    -   *02* = "TIX PAYOUT2.WAV"
    -   *03* = "ALARM_BUZZER.WAV"
    -   *04* = "MUSIC LOOP.WAV"
    -   *05* = "BIGSIXWHEEL2.WAV"
    -   *06* = "HANDLE PULL5.WAV"
    -   *07* = "PRESS TO STOP.WAV"
    -   *08* = "POWERUP2.WAV"
    -   *09* = "ATTRACT3.WAV"
    -   *10* = "SPINNIN N WINNIN.WAV"
    -   *11* = "PULLHANDLE1.WAV"
    -   *12* = "THANKS FOR PLAYING_02.WAV"
    -   *13* = "TRY AGAIN_02.WAV"
    -   *14*
    -   *15* = "COININ.WAV"
    -   *16* = "TIX PAYOUT2.WAV"
    -   *17* = "ALARM_BUZZER.WAV"
    -   *18* = "MUSIC LOOP.WAV"
    -   *19* = "BIGSIXWHEEL2.WAV"
    -   *20* = "HANDLE PULL5.WAV"
    -   *21* = "PRESS TO STOP.WAV"
    -   *22* = "WHEELSTOP4.WAV"
    -   *23* = "JACKPOT1.WAV"

## Accountings

**Entering Accounting Mode:**
1.  Select Option 00.
2.  Set Range to *2* (Accounting).
3.  Press **Test/Menu**.

**Soft Counters:**
-   On entry, 7-segment display will show “ *0* “ then scroll the value for counter #0.
-   The counter will be scrolled as “_00-00-00_”.
-   Press **AUX1** button to move up through the counters.
-   Press **AUX2** button to move back through the counters.
-   Pressing **AUX1** and **AUX2**, when the display is not scrolling, will exit the accounting mode.

-   **Counter 0:** Games played
-   **Counter 1:** Games ended on jackpot
-   **Counter 2:** Total Tickets given
-   **Counter 3:** Tickets per game

## Error Codes

-   Upon encountering an error condition the 7-segment display will flash “Er” plus the error condition code (0-9) and make an alarm sound.
-   Example: For a ticket error, the 7-segment display will flash “Er0”.
-   After flashing the error code, the display will scroll “CALL 4 HELP”.
-   The sequence will keep repeating until the **AUX1 button** is pressed or the game is reset.

-   **ErrC - Checksum Error:**
    -   **Condition:** On power up, the checksum for the protected memory did not match, or the Program ROM has been updated.
    -   **Result:** ALL defaults have been restored, and ALL Soft-counters have been reset.
    -   **Action:** Pressing the **STOP button** will cause the game to reset and reload the protected memory.
    -   **Note:** On power up, holding both the **AUX1 and AUX2 buttons** down will force a checksum failure.

-   **ErrD - Checksum Error:** (Description identical to ErrC in original document)

-   **ErrE - Checksum Error:** (Description identical to ErrC in original document)

-   **Err0 - Ticket Error:**
    -   **Condition:** The ticket machine was unable to dispense tickets due to either running out of tickets or a ticket jam.
    -   **Actions:**
        1.  Clear the ticket jam and/or Reload the Tickets.
        2.  When the optic sensor is blocked by reloading the ticket dispenser, the game will display the number of tickets owed and the **Stop button** will flash.
        3.  Press the **Stop button** to begin dispensing tickets.
    -   **Alternative Actions:**
        -   Pressing **Menu** will clear any tickets owed.
        -   If the optional **TCALL** switch is installed, activating it will show the tickets owed, and deactivating it will clear the tickets.

## Cleaning and Routine Maintenance

1.  **Polycarbonate Panels:**
    -   Skee-Ball, Inc. recommends using only “Kleenmaster Brillianize” (Part Number 800600-1).
2.  **Electronics Board:**
    -   Skee-Ball Inc. recommends using canned air to blow any dirt off the surface of the Electronics board.
3.  **Laminated Surfaces:**
    -   Skee-Ball, Inc. recommends “Kleenmaster Brillianize”.
4.  **Optical Sensors:**
    -   Skee-Ball, Inc. recommends using canned air to blow any dirt off the surface of the sensors on a weekly basis.
5.  **Hinges:**
    -   Monthly, lightly spray the Ball Gate hinges with a light lubricant.
6.  **Painted Surfaces:**
    -   Skee-Ball Inc. recommends using Windex® or any other mild, non-abrasive household cleaner.

## Electronics Schematic

### Overall System Components:
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

### Connections Details:

**I. POWER INPUT & MAIN POWER SUPPLY (EA2508):**

-   **AC Input:**
    -   To 3 WAY AC PLUG:
        -   BLK (Live) -> Main Power Switch (Terminal 1)
        -   WHT (Neutral) -> Main Power Switch (Terminal 2)
        -   GRN (Earth) -> Chassis Ground & POWER SUPPLY EA2508 Pin 2 (AC E)
    -   Main Power Switch Output:
        -   BLK (Live from Terminal 1) -> FUSE
        -   WHT (Neutral from Terminal 2) -> POWER SUPPLY EA2508 Pin 1 (AC N)
    -   FUSE Output:
        -   BLK (Live) -> POWER SUPPLY EA2508 Pin 3 (AC L)

-   **POWER SUPPLY EA2508 Outputs:**
    -   **Connector J1 (DC to LOGIC BOARD via 52022-8):**
        -   Pin 1 (+12VDC, YEL) -> LOGIC BOARD J1.1 (+12VDC)
        -   Pin 2 (GND, BLK) -> LOGIC BOARD J1.2 (GND)
        -   Pin 3 (+5VDC, RED) -> LOGIC BOARD J1.3 (+5VDC)
        -   Pin 4 (GND, BLK) -> LOGIC BOARD J1.4 (GND)
    -   **Connector J2 (AC to LOGIC BOARD and local AC loads):**
        -   Pin 1 (AC HOT, RED) -> LOGIC BOARD J2.1 (AC HOT)
        -   Pin 2 (AC N, BLK) -> LOGIC BOARD J2.2 (AC N)
        -   Pin 3 (EARTH, GRN) -> LOGIC BOARD J2.3 (EARTH)
    -   **Connector J3 (Switched AC Outputs, connected to LOGIC BOARD J3):**
        *(Note: The original text indicates some complexity in interpreting these connections. The following is based on wire path descriptions where available, otherwise direct pin mapping. The Logic Board J3 pins are labeled 1-9: AC OUT, AC N, SHLD, AC N, AC OUT, AC N, AC OUT, AC N, AC OUT.)*
        -   PS J3.1 (AC OUT, YEL) -> LOGIC BOARD J3.1 (AC OUT) or J3.9 (AC OUT) based on original text's ambiguity.
        -   PS J3.2 (AC N, BLK) -> LOGIC BOARD J3.2 (AC N) or J3.8 (AC N) based on original text's ambiguity.
        -   PS J3.3 (SHLD) - No connection shown.
        -   PS J3.4 (AC N, BLK) -> LOGIC BOARD J3.6 (AC N).
        -   PS J3.5 (AC OUT, WHT) -> LOGIC BOARD J3.5 (AC OUT).
        -   PS J3.6 (AC N, BLK) -> LOGIC BOARD J3.4 (AC N).
        -   PS J3.7 (AC OUT, BLU) -> LOGIC BOARD J3.7 (AC OUT) or J3.3 (AC OUT) based on original text's ambiguity.
        -   PS J3.8 (AC N) - No connection shown on PS side to LB, corresponds to LB J3.2 or J3.8.
        -   PS J3.9 (AC OUT) - No connection shown on PS side to LB, corresponds to LB J3.1 or J3.9.
        *(Original Text Interpretation: "This needs to be interpreted as three AC pairs from PS J3 to LB J3."
        PS J3.9(YEL) to LB J3.1(AC OUT), PS J3.8(BLK) to LB J3.2(AC N)
        PS J3.7(BLU) to LB J3.3(AC OUT), PS J3.6(BLK) to LB J3.4(AC N)
        PS J3.5(WHT) to LB J3.5(AC OUT), PS J3.4(BLK) to LB J3.6(AC N))*
    -   **Output to COLOR MOTOR (via 52022-10 from PS J3):**
        -   PS J3.1 (AC OUT, YEL) -> COLOR MOTOR Pin 1 (RED wire on motor)
        -   PS J3.2 (AC N, BLK) -> COLOR MOTOR Pin 2 (BLK wire on motor)
    -   **Output to LAMP DRIVER 1 (3-pin connector from Power Supply):**
        -   Pin 1 (WHT) -> LAMP DRIVER 1, Input Pin 1 (+12V)
        -   Pin 2 (GRN) -> LAMP DRIVER 1, Input Pin 2 (+5V)
        -   Pin 3 (BLK) -> LAMP DRIVER 1, Input Pin 3 (GND)

**II. LOGIC BOARD EA3729F1 Connections:**

-   **J1 (DC Power Input from POWER SUPPLY J1 via 52022-8):**
    -   Pin 1: +12VDC (from PS J1.1, YEL)
    -   Pin 2: GND (from PS J1.2, BLK)
    -   Pin 3: +5VDC (from PS J1.3, RED)
    -   Pin 4: GND (from PS J1.4, BLK)
-   **J2 (AC Power Input from POWER SUPPLY J2):**
    -   Pin 1: AC HOT (from PS J2.1, RED)
    -   Pin 2: AC N (from PS J2.2, BLK)
    -   Pin 3: EARTH (from PS J2.3, GRN)
-   **J3 (AC Power distribution with POWER SUPPLY J3):**
    *(Refer to PS J3 connection details above. LB J3 pins are 1-9: AC OUT, AC N, SHLD, AC N, AC OUT, AC N, AC OUT, AC N, AC OUT)*
-   **J14 (Outputs to various devices via 52022-11):**
    -   Pin 1: SHLD
    -   Pin 2: ARROW LED 1 -> ARROW LED PCB Pin 3
    -   Pin 3: ARROW LED 2 -> ARROW LED PCB Pin 2
    -   Pin 4: ARROW LED 3 -> ARROW LED PCB Pin 1
    -   Pin 5: ARROW LED SHLD -> ARROW LED PCB Pin 4
    -   Pin 6: STOP LAMP (RED) -> STOP STROBE Pin 1
    -   Pin 7: LOCK OUT (YEL) -> "LOAD" (solenoid/device) Pin 1
    -   Pin 8: +12VDC (BLK) -> Common +12V for STOP STROBE Pin 2, "LOAD" Pin 2
    -   Pin 9: GND
    -   Pin 10: +12VDC
    -   Pin 11: HANDLE SOLENOID (RED) -> "BELL" (solenoid/device) Pin 1
    -   Pin 12: +12VDC (BLK) -> "BELL" Pin 2
    -   Pins 13, 14, 15: +12VDC
-   **J15 (Inputs from Switches via 52022-12):**
    -   Pin 1: SHLD (WHT wire in cable) -> COM of HANDLE SWITCH, also common for other switches.
    -   Pin 2: HANDLE DOWN (No connection shown in this specific diagram)
    -   Pin 3: HANDLE UP (WHT wire in cable) -> NO of HANDLE SWITCH
    -   Pin 4: STOP BUTTON (RED wire in cable) -> STOP BUTTON Pin 1 (Pin 2 of Stop Button is common/SHLD)
    -   Pin 5: 6 FOOT GAME SELECT (BLK wire in cable) -> COM of "6' ONLY" Switch (NO contact of this switch goes to common/SHLD)
    -   Pin 6: +12VDC
-   **J16 (Switch connections via 52022-12):**
    -   Pin 1: +12VDC (RED wire in cable) -> COM of a 3-position switch.
    -   Pin 2: GND (BLK wire in cable) -> NC of another 3-position switch, also common/SHLD.
-   **J17 (To COIN DOOR EA4166 via 52022-14):**
    -   Pin 1: SHLD
    -   Pin 2: COIN COUNTER (BLU) -> COIN DOOR CTR Pin 2
    -   Pin 3: +12VDC
    -   Pin 4: GND (BLK) -> Common with J17.8
    -   Pin 5: +5VDC
    -   Pin 6: COIN 1 (RED) -> COIN DOOR COIN Pin 1
    -   Pin 7: COIN 2 ("6' ONLY" - no connection to this specific coin door)
    -   Pin 8: GND (BLK) -> COIN DOOR CTR Pin 1
-   **J18 (To TICKET DOOR SM4131-1 via 52022-15):**
    -   Pin 1: SHIELD
    -   Pin 2: TKT COUNTER (GRN) -> TICKET DOOR Pin 4
    -   Pin 3: +12VDC (YEL) -> TICKET DOOR Pin 3
    -   Pin 4: TKT NOTCH (RED) -> TICKET DOOR Pin 2
    -   Pin 5: +12VDC
    -   Pin 6: GND (BLK) -> TICKET DOOR Pin 1
    -   Pin 7: TKT MOTOR (ORG) -> (To Ticket Motor, part of SM4131-1 assembly)
    -   Pin 8: +5VDC
    -   Pin 9: GND
-   **J20 (To TEST/AUX Switches via 52022-16):**
    -   Pin 1: SHLD
    -   Pin 2: TEST (RED) -> TEST Switch Pin 1
    -   Pin 3: AUX 2 (WHT) -> AUX 2 Switch Pin 1
    -   Pin 4: AUX 1 (GRN) -> AUX 1 Switch Pin 1
    -   Pin 5: GND (BLK) -> Common Pin 2 for TEST, AUX 2, AUX 1 Switches
-   **J21 (AC Control Signals "TO P.S. AC OUT"):**
    -   Pin 1: YEL
    -   Pin 2: BLU
    -   Pin 3: WHT
    *(Likely control signals to Power Supply to switch AC outputs on PS J3)*
-   **J22 (To 4 DIG. DISP. and SPKR(L) MS161):**
    -   **To SPKR(L) MS161 (via 52022-13):**
        -   Pin 1 (RED) -> SPKR(L) Pin 1
        -   Pin 2 (BLK) -> SPKR(L) Pin 2
    -   **To 4 DIG. DISP. (via 52022-1, forms an 8-wire bus):**
        -   J22.3 or J22.4 (ORG, LED + 12V) -> 4 DIG. DISP. Pin 1 (12V)
        -   J22.12 (RED, 5V) -> 4 DIG. DISP. Pin 2 (5V)
        -   J22.11 (BLK, GND) -> 4 DIG. DISP. Pin 3 (GND)
        -   (Original text notes 4 DIG. DISP. Pin 4 is BLK L-GND, sourced from bus)
        -   J22.7 (BRN, S-CLK) -> 4 DIG. DISP. Pin 5 (S-CLK)
        -   J22.9 (WHT, S-DATA) -> 4 DIG. DISP. Pin 6 (S-DATA)
        -   J22.10 (YEL, S-STRB) -> 4 DIG. DISP. Pin 7 (S-STRB)
        -   J22.8 (BLU, S-ENBL) -> 4 DIG. DISP. Pin 8 (S-ENBL)
        *(The 8-wire bus for 4 DIG. DISP input and Lamp Drivers is:
        1: ORG (+12V), 2: RED (+5V), 3: GRN (GND), 4: BLK (L-GND),
        5: BRN (S-CLK), 6: WHT (S-DATA), 7: BLU (S-STRB), 8: YEL (S-ENBL))*

**III. 4 DIG. DISP. and LAMP DRIVER CHAIN:**

-   **Input Bus (8-pin connector from LOGIC BOARD J22 via 52022-1 to 4 DIG. DISP., then 52022-5 to LD1):**
    -   Pin 1: ORG (+12V)
    -   Pin 2: RED (+5V)
    -   Pin 3: GRN (GND)
    -   Pin 4: BLK (L GND)
    -   Pin 5: BRN (S-CLK)
    -   Pin 6: WHT (S-DATA)
    -   Pin 7: BLU (S-STRB)
    -   Pin 8: YEL (S-ENBL)
-   **Lamp Driver Output (3-pin connector for daisy chain signals):**
    -   Pin 1: WHT (S-ENBL_OUT)
    -   Pin 2: GRN (S-STRB_OUT)
    -   Pin 3: BLK (S-CLK_OUT)
-   **Daisy Chain Logic:**
    -   The main bus (Pins 1, 2, 3, 4, 6 of the 8-pin input: +12V, +5V, GND, L-GND, S-DATA) is paralleled to all Lamp Drivers.
    -   The signals S-CLK, S-STRB, S-ENBL are daisy-chained:
        -   Output of LDx (WHT, GRN, BLK) connects to Input Pins 8 (YEL), 7 (BLU), 5 (BRN) respectively of LDx+1.
-   **Specific Daisy Chain Cables:**
    -   4 DIG. DISP. Output (8 pins) -> 52022-5 -> LAMP DRIVER 1 Input (8 pins)
    -   LAMP DRIVER 1 Output (3 pins) -> 52022-2 -> LAMP DRIVER 2 Input (pins 5-BRN, 7-BLU, 8-YEL)
    -   LAMP DRIVER 2 Output (3 pins) -> 52022-6 -> LAMP DRIVER 3 Input (pins 5-BRN, 7-BLU, 8-YEL)
    -   LAMP DRIVER 3 Output (3 pins) -> 52022-3 -> LAMP DRIVER 4 Input (pins 5-BRN, 7-BLU, 8-YEL)
    -   LAMP DRIVER 4 Output (3 pins) -> 52022-7 -> LAMP DRIVER 5 Input (pins 5-BRN, 7-BLU, 8-YEL)
    -   LAMP DRIVER 5 is the last in the chain.
-   **Power for LAMP DRIVER 1:**
    -   Directly from POWER SUPPLY EA2508 output (3-pin connector):
        -   WHT -> +12V (LD1 Input Pin 1)
        -   GRN -> +5V (LD1 Input Pin 2)
        -   BLK -> GND (LD1 Input Pin 3)

**IV. Other Peripheral Components & Switches:**

-   **ARROW LED PCB (connected to LB J14 via 52022-11):**
    -   Pin 1: ARROW LED 3 (from J14.4)
    -   Pin 2: ARROW LED 2 (from J14.3)
    -   Pin 3: ARROW LED 1 (from J14.2)
    -   Pin 4: SHLD (from J14.5)
-   **STOP STROBE (connected to LB J14 via 52022-11):**
    -   Pin 1: STOP LAMP (from J14.6, RED wire)
    -   Pin 2: +12VDC (from J14.8, BLK wire)
-   **"LOAD" (solenoid/device, connected to LB J14 via 52022-11):**
    -   Pin 1: LOCK OUT (from J14.7, YEL wire)
    -   Pin 2: +12VDC (from J14.8, BLK wire)
-   **"BELL" (solenoid/device, connected to LB J14 via 52022-11):**
    -   Pin 1: HANDLE SOLENOID (from J14.11, RED wire)
    -   Pin 2: +12VDC (from J14.12, BLK wire)
-   **Separate AC Circuit for Physical Bell/Load (near Power Supply):**
    -   **Physical BELL component:**
        -   Terminal 1 (YEL wire) -> Physical LOAD component Terminal 1.
        -   Terminal 2 (RED wire) -> One end of 10 OHM Resistor.
    -   **10 OHM Resistor:**
        -   One end -> Physical BELL Terminal 2 (RED wire).
        -   Other end (RED wire) -> T-junction to AC HOT (RED wire between LB J2.1 and PS J2.1).
    -   **Physical LOAD component (coil symbol):**
        -   Terminal 1 (YEL wire) -> Physical BELL component Terminal 1.
        -   Terminal 2 (BLK wire) -> T-junction to AC N (BLK wire between LB J2.2 and PS J2.2).
-   **COLOR MOTOR (connected to PS J3 via 52022-10):**
    -   Pin 1 (RED wire on motor) -> YEL wire from PS J3.1 (AC OUT)
    -   Pin 2 (BLK wire on motor) -> BLK wire from PS J3.2 (AC N)
-   **HANDLE SWITCH (part of 52022-12, connected to LB J15):**
    -   COM: BLK wire (to J15.1 SHLD, commoned)
    -   NO: WHT wire (to J15.3 HANDLE UP)
-   **STOP BUTTON (part of 52022-12, connected to LB J15):**
    -   Pin 1: RED wire (to J15.4 STOP BUTTON)
    -   Pin 2: BLK wire (common/SHLD)
-   **"6' ONLY" Switch (3-position, part of 52022-12, connected to LB J15):**
    -   COM: BLK wire (to J15.5 6 FOOT GAME SELECT)
    -   NO: BLK wire (to common/SHLD)
    -   NC: Not connected
-   **Other Configuration Switches (part of 52022-12, connected to LB J16):**
    -   Switch A (3-pos): COM -> RED wire from J16.1 (+12VDC). NO/NC not connected.
    -   Switch B (3-pos): NC -> BLK wire (common/SHLD from J16.2 GND). COM/NO not connected.
-   **COIN DOOR EA4166 (connected to LB J17 via 52022-14):**
    -   CTR Pin 1: BLK wire (to J17.8 GND)
    -   CTR Pin 2: BLU wire (to J17.2 COIN COUNTER)
    -   COIN Pin (single): RED wire (to J17.6 COIN 1)
-   **TICKET DOOR (L) SM4131-1 (connected to LB J18 via 52022-15):**
    -   Pin 1 (BLK): GND (to J18.6)
    -   Pin 2 (RED): TKT NOTCH (to J18.4)
    -   Pin 3 (YEL): +12VDC (to J18.3)
    -   Pin 4 (GRN): TKT COUNTER (to J18.2)

## Trouble-shooting Guide

**Introduction:**
The purpose of this guide is to help you pinpoint a problem area and eliminate the undue process of parts swapping, expedite shipping charges, and other hassles associated with a breakdown due to unknown causes. In order to successfully follow this guide, it is imperative the individual understands the overall play of the game and its test functions.
Reading the Game Play portion of the Assembly /Operating Manual will enable one to better understand how and when certain functions relating to hardware (physical printed circuit board an components thereof) and software (the program which actually commands the hardware) interact.
Reading the test portion of the Assembly/Operating Manual will enable one to pinpoint the problem area quickly.
The overall content is written according to the most common problems of which Skee-Ball Inc. has been aware. Listed below are general descriptions of the principal problems and suggested point to troubleshoot.

-   **Problem: Color Wheel is not spinning**
    -   **Troubleshooting Steps:**
        1.  Check for 12 Vdc across the motor.
        2.  Check for broken or loose cable.
        3.  Replace color wheel motor.
        4.  Check color wheel is seated between drive wheel and idler bearings.

-   **Problem: One half of the light circle or Marquee lights not working**
    -   **Troubleshooting Steps:**
        1.  Check data cables to and from lamp driver boards.
        2.  Check AC power cables.

-   **Problem: When game is turned on the bell continues to ring, lights are flashing and tickets continues to run.**
    -   **Troubleshooting Steps:**
        1.  Replace logic board.

-   **Problem: Display shows “Err C”**
    -   **Troubleshooting Steps:**
        1.  Pressing the “STOP” button will reset the game and clear the error.
        2.  If the problem continues, replace the logic board.

-   **Problem: Display shows “Err 1” (Ticket Error)**
    -   **Troubleshooting Steps:**
        1.  Refill tickets.
        2.  Remove any tickets jammed in the dispenser.
        3.  Clean the optic eye on dispenser.
        4.  Replace the dispenser.
