# Aquaponics

Aquaponics is a system that allows for the creation of an ecosystem that produces fish and plants for human consumption.

The methodology of Aquaponics is rooted in Permaculture; a way of living without adversely impacting the environment through harmful agricultural practices such as excessive use of fertilisers or land clearing for grazing animals.

Aquaponics is a combination of Hydroponics (growing plants in water) and Aquaculture (raising fish to eat). It combines the best of both systems without any wasteful practices such as dumping polluted water.

An Aquaponics system must have 7 key variables in balance in order to maintain a healthy ecosystem.

pH: the acid/base balance of the system.
Ammonia: The amount of ammonia that will be transformed into Nitrite. Toxic to fish.
Nitrite: The amount of Nitrite that will be transformed into Nitrate. Very toxic to fish.
Nitrate: The amount of Nitrate available to the plants that will use them as nutrients.
Water temperature: ensuring a liveable temperatures for all inhabitants of the system.
Dissolved oxygen (DO): The amount of oxygen molecules available in the water.
Conductivity (EC): The electrical current measures the "salts" in the water, not actual salt but the reactivity of the nutrients available that also conduct electricity.

A healthy Aquaponics ecosystems most important factor are nitrifying bacteria, their health is paramount to the success of the system. Without them the water would be uninhabitable for fish and the plants would get no nutrients from the water.

The program I have designed will track these variables, store them and give basic analysis of all previous data available to the program.

## Using the app

To use this program you run the script Aquaponics.py follow the prompts.

Selecting 1 will add your data for today. As above the prompt will ask you for the 7 key variables and provide comments on the input given by you the user.

### pH
Recommended pH levels for an aquaponics system ranges between 6.5 - 7.0.
Readings above 7 are troublesome to the plants within the system in terms of drawing nutrients from the water. This is referred to as "Nutrient lockout". 
Readings above 8 are dangerous for everything in the system. High pH readings are fixed by adding acid such as hydrochloric to the system.
Readings below 5 are dangerous for everything and readings below 6.5 are dangerous for fish. Low pH readings are fixed by adding limestone to the system.

### Ammonia
Recommended levels of ammonia are below 0.75ppm due to being toxic to fish.
Readings above 0.75 could indicate a dead fish somewhere in the fish tank.
Readings above 1 require the user to stop feeding the fish until the levels have decreased below 0.75 due to fish feed adding ammonia to the system.
Readings above 2 are toxic to fish, to fix this the user must change 1/3 of the total water in the aquaponics system.

### Nitrite
Recommended levels of nitrite are below 0.75ppm due to being very toxic to fish.
Readings above 0.75 could indicate damaged nitrifying bacteria.
Readings above 1 are toxic to fish, to fix this the user must change 1/3 of the total water in the aquaponics system.

### Nitrate
Recommended levels of nitrate are below 300ppm due to being much less toxic to fish.
Readings above 150 indicate there are not enough plants in the system taking up the nutrients.
High Nitrate levels are fixed by planting more plants.

### Temperature
Since there are multiple organisms cohabitating in this ecosystem all must be kept at a comfortable temperature.
Nitrifying bacteria die above 49 degrees C and below 0 degrees C
Below 4 degrees C there is no bacterial activity
Bacterial growth is slowed by 75% between 8-10 degrees C
Bacterial growth is slowed by 50% below 18 degrees C


