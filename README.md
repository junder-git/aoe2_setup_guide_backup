# THE ONE KEY BUILD

Make the following changes to make this script functional

![Alt text](image.png)  
  
![Alt text](image-1.png)  
  
![Alt text](image-2.png)  
  
![Alt text](image-3.png)  
  
  
# HOTKEYS  
## Load the definative hot keys then change the following...  
  
### Page - Unit commands  
Economic Buildings -> F12  
Garrison -> UNBIND  
Military Buildings -> UNBIND  
Set Gather Boint -> Extrabutton2 
Ungarrison -> Extrabutton2 
Delete Unit -> MiddleButton
  
### Page - Game commands  
Select all town centers -> Extrabutton2  
  
### Page - Scroll commands  
UNBIND all in this section  
  
### Page - zoom commands  
Zoom in -> UP  
Zoom out -> Down  
  
### Page - Gate commands  
Rotate gate colockwise -> WheelUp  
Rotate gate counter-clockwise -> WheelDown  
  
### Page - Villager build  
Cancel -> F10  
Set all remaining buildings to whatever single lowercase alphabetical character key you want...  
...so long as its unique to that building whether its milatry or eco.  

### Page - Town Center  
Go Back To Work -> Extrabutton1  
Villager -> F11  

===

# How to use...
## Extrabutton2  
The idea is to spam mouse side button 1 (the easiest to reach at the front of the mouse, Extrbutton2) for villagers no matter the context.
The ui is a bit glitchy, but it selects all TCs if not selected already then proceeds to que vils on further button presses at a rate of one per press.  
  
ALSO it gives waypoint control every time the button is pressed, kinda meh feature    
  
ALSO if vills are docked in TC it will ungarisson them before you proceed to q further villagers per press (with right click as garison enabled)
  
## Extrabutton1  
The Extra button one works well with sending vils from TC back to work (with right click as garison enabled)  
it also can be used to cancel the way point being set on the Extrabutton2 spam end,  
when done spamming tap Extrabutton1 keeping current active way point unchanged.  

  #  
  #  
    
### Feudal age ((Poles)) to fling food to open market for feudal age Saracen ally to buy.  
True market value is refelcted as +/-5 for Saracens and +/-30 on any other civ -> Excess food is to be sold by pole player to impact food cost on the open market. In such a way that tribute becomes closer to the 5% loss asymptote for food value then 30% fixed loss for food value...  
    
Say intial market investment made by pole goes through at 1000 food in feudal, thats 10 batches, so -3 over 100:100 and is now 100:70 true value for saracen to buy food. If they buy back to 100:100 true value it costs them (70+30)+5%!(in steps of three) gold (70+73+76... seek python)    
The sum of integers from 70 to 100 in intervals of 3 with 5% per interval is: 981.75 gold 
so effectively 1000 food costs them 982 gold tax to recive it open market vs 300 food tax direct...  
For this strat to work the saracen needs to access the food sold at some factor of gold tax much lower then that of the food tax to be worth the buy for a specific unit with food>gold cost ratio...    
  
For (Saracens) Battle Elephant: 120 Food, 70 Gold  
This unit needs market fair price ratio of food:gold to be 100:58 or lower. Any 100 batch of food bought or sold makes changes to market fair price by fixed amount of +/-3, so (100-58)/3 = 1400 food to get this ideal true value price ratio set for a saracen elephant all in gold from the open market.      
  
-> For now castle age 800 food cost can also come from any going rate < 100:58 in the open market too just cus...    
  
Note gold tiles are scarce and can run out for saracen in castle age pretty rapid.  
  
Poles dark age: build order, total::(2 houses 2 folwark 1 lumbercamp x farms) 7/25 on wood 18/25 farms after hunt+sheep   gathered => loom + click up  
Poles feudal age: build order, total::(200-cost stone walls 5 houses 3 folwork 2 lumbercamp 18+x farms)     
  
Saracen dark age: build order, total::(3 houses 1 lumbercamp 1 minecamp on gold 1 barracks) x/25 on wood x/25 on gold after hunt+sheep gathered => click up  
Saracen feudal age: build order, total::(5 houses market blacksmith 2 stables 2 minecamp on gold) if food < 100:58 buy => click up   
Saracen castle age: spam elephants  


  
