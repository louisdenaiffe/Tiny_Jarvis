# TINY_JARVIS JOURNAL

> <u>Note</u>: if images don't load first try, reload the page.

## Table of contents:
 - [July 5](#july-5-started-prototyping--visuals) : 3 hours
 - [July 6](#july-6-assembling-everything-together) : 4 hours
 - [July 7-8](#july-7-8-designing-the-pcbs) : 5 hours
 - [July 17](#july-17-receiving-the-pcbs-and-soldering) : 3 hours
 - [July 18](#july-18-working-on-a-new-pcb-prototype--voltage-checking) : 2 hours
 - [July 21](#july-21-schematic-and-pcb-error-checking) : 3 hours
 - [July 22](#july-22-more-schematic-before-ordering) : 2 hours
 - [July 23](#june-23-dfm-checks--silkscreen-logo-added) : 2 hours
 - [August 19](#august-19-receiving-the-pcb-batch-number-2) : 1 hour

 **Total**: 25 hours


> The hours here do NOT include the hours coding. Those are registered using Hackatime.

## July 5: Started prototyping + visuals

<table border="0">
  <tr>
    <td valign="top">
      <img src="https://cdn.hackclub.com/019f6692-acd1-7dd8-9a5f-7f35852d8203/paste-1784132312883.png" width="400px">
    </td>
    <td valign="top">
      <p>I received all the materials I needed to start prototyping:</p>
      <ul>
        <li>1x Pack of Female-to-Female (F-F) Jumper Wires (40pcs ribbon)</li>
        <li>1x Pack of Female-to-Male (F-M) Jumper Wires (40pcs ribbon)</li>
        <li>1.3" OLED</li>
        <li>2x MAX98357A I2S Amps: for transforming digital signal into analog for speaker (=amplifiers)</li>
        <li>Rotary Encoder Module 5 pin version (for volume)</li>
        <li>A LOT of Push buttons (way too many, I only need two)</li>
        <li>2x 3W Speaker</li>
        <li>Medium breadboard</li>
        <li>Cheap USB mic</li>
      </ul>
    </td>
  </tr>
</table>

The first difficulty was met when connecting all these components together during prototyping. The rotary encoder and OLED did not give me any trouble, I just had to connect them to the right GPIO pins on the Pi (The screen looks weird bc i wasnt using Luma).


<table border="0">
  <tr>
    <td>
      <img src="https://cdn.hackclub.com/019f6693-5e78-711d-9f17-6957b8e75dbd/paste-1784132358841.png" width="150">
    </td>
    <td>
      <img src="https://cdn.hackclub.com/019f6693-8d02-7f43-a5b6-faee9ba69a32/paste-1784132368397.png" width="150">
    </td>
  </tr>
</table>

However the soldering did not go as well; this was my first time soldering electronic components and it did not look good. 😅 I didn't have the right type of soldering iron to be faire, so I bought a new one (industral soldering iron).

<table border="0">
  <tr>
    <td>
      <img src="https://cdn.hackclub.com/019f6680-1b29-70d0-9e6c-37d84d8eb0f0/prototyping.jpg" width="150">
    </td>
    <td>
      <img src="https://cdn.hackclub.com/019f669f-14b5-7fe3-b0c1-0f6062149d63/paste-1784133128324.png" width="150">
    </td>
    <td>
      <img src="https://cdn.hackclub.com/019f669f-b6bc-7756-80f7-4c381a12ca55/paste-1784133162524.png" width="150">
    </td>
  </tr>
</table>

As a matter of fact, the speakers did not work, as the connection to the amp was too poor. So i decided to just connect the rpi5 via bluetooth to a small JBL speaker.

But in a PCB, this would be much different since the connection would be direct, so I will implement the amps + speakers in the PCB later on.

<u>tl;dr:</u> 
 - OLED screen works perfectly after a few code changes to the testing script
  - Rotary encoder and buttons work after learning how a breadboard works
  - USB mic works without flaw
  - Amps+speakers don't work rn but they'll work on a PCB

  Spent some time in [Piskel](https://www.piskelapp.com/) designing visuals (not as easy as it sounds)


<table border="0">
  <tr>
    <td>
      <img src="https://cdn.hackclub.com/019f66a5-508a-77c7-9c2a-b47e20f953b3/paste-1784133537475.png" width="150">
    </td>
    <td>
      <img src="https://cdn.hackclub.com/019f66a5-96e5-78f9-a60f-08bad59182ec/paste-1784133555530.png" width="150">
    </td>
    <td>
      <img src="https://cdn.hackclub.com/019f66a8-8844-7280-8244-3d438b5111eb/paste-1784133748390.png" width="150">
    </td>
    <td>
    <img src="https://cdn.hackclub.com/019f66a8-ecdf-7716-a163-5b531a83cf56/paste-1784133774152.png">
    </td>
  </tr>
</table>
(These are animated btw, just can't render them in a JOURNAL.md)


**Time spent this session: 3 hours (2 for prototyping and 1 for the oled screen animations)**

## July 6: Assembling everything together

Now here I don't know why but i decided I wanted to feel how the final product would be like so I assembled it all into a more compact, less prototype-looking way, but still technically a prototype.\
You'll understand.

![image](https://cdn.hackclub.com/019f66cc-8eb4-794b-9e8b-9c2a5fc2ce81/paste-1784136108680.png)

I spent an afternoon drilling holes into an old cigar box and trying to figure out how to place everything in the right way, making a lot of mistakes along the road.
Here's how it turned out:

<table border="0">
  <tr>
    <td>
      <img src="https://cdn.hackclub.com/019f66cd-f607-79b0-8238-a4f380b408de/paste-1784136196854.png" width="150">
    </td>
    <td>
      <img src="https://cdn.hackclub.com/019f66ce-1630-75c3-9a52-ebeb7f2eefe2/paste-1784136205713.png" width="150">
    </td>
    <td>
      <img src="https://cdn.hackclub.com/019f66ce-435f-72e1-a2f3-f511dfac64a9/paste-1784136217919.png" width="150">
    </td>
  </tr>
</table>

Pretty good, even if it wasn't perfect.\
Next up would be PCB making! I started researching as to how to make a PCB on websites such as SparkFun.

**Time spent this session: 4 hours (drilling holes in wood is NOT easy, trust me)**

## July 7-8: Designing the PCBs

Today I spent at least 2 hours learning everything I could about printed circuits and downloaded EasyEDA Pro (yes, ik, not KiCad).
Made my first schematic :

![image](https://cdn.hackclub.com/019f7144-2014-7ccf-a530-320e75e5a074/old_schematic.png)


In hindsight: this is horrible. Luckily I saw some other schematics and realised this wasn't the right path. Version 2 :


<table border="0">
  <tr>
    <td>
      <img src="https://cdn.hackclub.com/019f7144-ec38-7b82-8792-5ddf6fb689ab/new_schematic.png" width="150">
    </td>
    <td>
      <img src="https://cdn.hackclub.com/019f7146-6ca9-7aa6-bfc8-41119aebd0bf/pcb.jpg" width="150">
    </td>
  </tr>
</table>

Way better! After getting all the traces right and the DRC (Design Rule Checker) empty, I ordered from JLCPCB.

**Time spent this session: 5 hours**\
New skill acquired!

## July 17: Receiving the PCBs and soldering

Today I received my JLCPCB order!
<table border="0">
  <tr>
    <td>
      <img src="https://cdn.hackclub.com/019f713d-5fd3-72c7-81d7-2c55419a6003/IMG_5702.jpeg" width="150">
    </td>
    <td>
      <img src="https://cdn.hackclub.com/019f713d-97bd-7654-b5fa-9151fd0e1ece/IMG_5703.jpeg)" width="150">
    </td>
    <td>
      <img src="https://cdn.hackclub.com/019f713d-d997-7f42-8b90-e54e813f5346/IMG_5708.jpeg" width="150">
    </td>
  </tr>
</table>

Looks great! EXCEPT:
 - I had bought amplifier modules, but turns out I had actually placed the TQFN or smth package instead of holes needed to solder the module. And since I had taken the amps out of PCBa... yh. won't work.
 - One of the mounting holes of the OLED screen is on a trace.
 - Buttons are too small
 - I realized I forgot to check something: the DFM (checked again and yh, lots of red everywhere)

Soldering time with a 40 pins GPIO header I found on PineHut. I don't really know how to solder yet, so this is for practicing (there are 5 pcb boards and two gpio headers so I can train with them)

![image](https://cdn.hackclub.com/019f713d-f1ef-7cbe-81fe-b28468ac3720/IMG_5719.jpeg)

(I burnt the first board sooo bad)

**Time spent this session: 2-3 hours**

## July 18: working on a new PCB prototype + voltage checking

Today I spent a lot of time on EasyEDA Pro and JLCDFM online checker.

Managed to fix most of the issues:
 - Silkscreen to pad/silkscreen to hole: don’t care, they have a computer program that fixes that at JLCPCB, plus very unlikely. Can ignore.
 - Annular ring: the only issues are with the mounting holes. Can ignore.
 - Tht to smd: it needs a 2.03mm or more to be green; except that’s ridiculously high and not for consumer electronics, since mine are above the 0.25mm recommended threshold, fixed.
 - Pad spacing: fixed (by hand)

<table border="0">
  <tr>
    <td>
      <img src="https://cdn.hackclub.com/019f7555-feea-737d-a8f1-1bd4cc759117/paste-1784379997310.png" width="150">
    </td>
    <td>
      <img src="https://cdn.hackclub.com/019f7556-303b-73e2-a918-1af42ceefb85/paste-1784380009740.png" width="150">
    </td>
    <td>
      <img src="https://cdn.hackclub.com/019f7556-52e1-7554-987f-e434936ffe67/paste-1784380019259.png" width="150">
    </td>
  </tr>
</table>

Also: for the next batch, the amps will be included in the PCB assembly and won't need to be soldered by hand (which btw requires micro-soldering equipment and reflow station and whatnot).

Plus I did more soldering and tested the PCBs I received with the new multimeter I just bought.\
<u><b>Conclusion:</b></u> 3 shorts on bottom layer and 1 on top, so I'm getting better.

![image](https://cdn.hackclub.com/019f75d3-a373-7c63-a153-230085be33ea/paste-1784388230021.png)

Soon I'll be ordering the next batch of PCBs, however: I have a more limited budget and with delivery fees and whatnot, I'll be needing funding. On **JLCPCB**, when ordering the bare minimum and not buying the rotary encoder AND the oled screen, and while having to solder them by hand:

 - Merchandise Total: <b>$45.31</b>
 - Shipping Estimate: <b>$21.26</b>
 - Customs duties & taxes: <b>$13.32</b>

 Total: <b>~79.89</b>
 

**Time spent this session: 2 hours**

## July 21: Schematic and PCB error checking

Today I finally got some feedback on my PCB schematic on the Slack #electronics channel.
Lots of issues:
 - VCC wasn't actually connected to the VCC GPIO pins 💀
 - Resistors on the SD_MODE# pins of the amps were actually electrically incorrect, since they led into the void. Did some research and it should be: left channel --> SD_MODE connected to 3.3V/VCC (because it is > 1.4V, it activates left channel) and right channel --> 220 kΩ to 330 kΩ resistor in series between the SD_MODE and 3.3V/VCC (because combined with the chip's internal resistor, this drops the pins voltage into the <1.4V range required for right channel)
 - Some resistors weren't needed for the I2C OLED screen bc Raspberry Pi 5 alr has software pullups incorporated, and would've actually led to bad functioning.
 - GND wasn't connected to the GPIO pins either (great)
 - Rotary encoder didn't really need that decoupling cap, since it alr had filtering/debouncing caps and there are other decoupling caps on the PCB.

 Aaaand since I changed a lot of things in the schematic, I also had to change the PCB:
  - Ensure vias weren't literally on the silkscreen, which is actually a Design Rule I set but that auto-routing doesn't seem to care about
  - Vias not being ON pads was also a nice change to make
  - Resistors on the right side of the chips, same for decoupling caps to make everything simpler, needing to rewire most of the auto-routing's mediocre work.
  - While rewiring, made some 90 degree angle traces. Read that it wasn't best practice later and had to redo a ton of traces.

![image](https://cdn.hackclub.com/019f895b-d1c7-7ac2-bdbc-03b50a25691d/paste-1784715922891.png)

  **Time spent this session: 3 hours**

  ## July 22: More schematic before ordering

   - Turns out you also need to pour a copper fill on the bottom layer (better practice)
   - And that it's also standard practice to delete all GND traces cos there already is a GND fill.
   - More or less moving traces out of the way to make the GND fill new spaces where it wasn't before, to be brief.
   - Removed dead islands, isolated copper islands, or connected them to the main GND pour via... vias!
   - Learnt about the Exposed Thermal Pad, actually spent an hour debugging the DRC because I didn't know what it was
   - Acquired some precious knowledge through practice, like using vias to connect short GND traces on the top layer to GND on the bottom layer, not actually connecting all GND traces together since they are all connected via the copper fill.
   - Realized I didn't even know what GND was. Learnt it was the OV plane, the end of the cycle that electricity flows through.
   - Cleaned all the traces up, leaving as much distance as possible bwteen every pad, via and trace
   - Updated the PCB files in the `pcb/` directory. Still waiting for funding...


Looking good!
![image](https://cdn.hackclub.com/019f8f7b-894a-75f6-b331-c5652f07e6fe/paste-1784818663841.png)

**Time spent this session: 2 hours**

# June 23: DFM checks + silkscreen logo added!

- Crazy idea today: adding a cool silkscreen logo to the PCB (it's free I believe)

![image](https://cdn.hackclub.com/019f94d0-189b-7c66-b240-6cd3501add3c/paste-1784908092845.png)
 - Ofc I put the name of the author according to the [CC BY 3.0 License](https://creativecommons.org/licenses/by/3.0/) ([The Noun Project](https://thenounproject.com))
 - Also rerouted some traces on both layers that were going through the mounting holes (not good for connectivity)
 - Fixed some silkscreen going over components, learnt that it may cause the ink to bleed and lead to malfunctionings, even modern machines will detect it and avoid it (still good practice)
 - Oh and checked the JLCPCB online DFM for any errors I might've reintroduced with all these recent changes, which helped me detect the silkscreen issues and other THT to component clearance issues.

Feel like I'm really getting the hang of PCB making! At least at a hobby level

 **Time spent today: 2 hours**

 # August 19: Receiving the PCB batch number 2!
 - Ok so quick catchup: I asked for funding waited almmost three weeks, got refused, asked again, got refused, everytime for dumb reasons where the reviewers didn't look at my repo or even at my project (this was crazy btw, I had to fight for my life) 
 - So I decided to take the initiative and order the PCBs in early July, knowing that I would get the funding later to pay off the debt
 
 I got them today! This is a preview of what it would look like, not soldered yet and speakers not connected
![image](https://cdn.hackclub.com/01a01e08-cb3f-7aaf-9e4b-f9ef1785e805/IMG_5995.jpeg)

I then tried soldering for a bit, but realized that I wasn't making any progress and mostly just destroying the board, so
I made the choice of waiting until I got the 80$ to continue

**Time spent today : 1 hour**