# Aquaponics

Aquaponics is a system that allows for the creation of an ecosystem that produces fish and plants for human consumption.

The methodology of Aquaponics is rooted in Permaculture; a way of living without adversely impacting the environment through harmful agricultural practices such as excessive use of fertilisers or land clearing for grazing animals.

Aquaponics is a combination of Hydroponics (growing plants in water) and Aquaculture (raising fish to eat). It combines the best of both systems without any wasteful practices such as dumping polluted water.

An Aquaponics system must have 7 key variables in balance in order to maintain a healthy ecosystem.

1. **pH:** the acid/base balance of the system.
2. **Ammonia:** The amount of ammonia that will be transformed into Nitrite. Toxic to fish.
3. **Nitrite:** The amount of Nitrite that will be transformed into Nitrate. Very toxic to fish.
4. **Nitrate:** The amount of Nitrate available to the plants that will use as nutrients.
5. **Water temperature:** ensuring a liveable temperatures for all inhabitants of the system.
6. **Dissolved oxygen (DO):** The amount of oxygen molecules available in the water.
7. **Electrical Conductivity (EC):** The electrical current measures the "salts" in the water, not actual salt but the reactivity of the nutrients available that also conduct electricity.

A healthy Aquaponics ecosystems most important factor are nitrifying bacteria, their health is paramount to the success of the system. Without them the water would be uninhabitable for fish and the plants would get no nutrients from the water.

The program I have designed will track these variables, store them and give basic analysis of all previous data available to the program.

## Using the app

To use this program you run the script Aquaponics.py follow the prompts.

### Option 1

Selecting 1 will add your data for today. As above the prompt will ask you for the 7 key variables and provide comments on the input given by you the user.

#### pH

Recommended pH levels for an aquaponics system ranges between 6.5 - 7.0. This keeps all organisms within the ecosystem happy (Bacteria, fish and plants).
Readings above 7 are troublesome to the plants within the system in terms of drawing nutrients from the water. This is referred to as "Nutrient lockout". 
Readings above 8 are dangerous for everything in the system. High pH readings are fixed by adding acid such as hydrochloric to the system.
Readings below 5 are dangerous for everything and readings below 6.5 are dangerous for fish. Low pH readings are fixed by adding limestone to the system.

#### Ammonia

Recommended levels of ammonia are below 0.75ppm due to being toxic to fish.
Readings above 0.75 could indicate a dead fish somewhere in the fish tank.
Readings above 1 require the user to stop feeding the fish until the levels have decreased below 0.75 due to fish feed adding ammonia to the system.
Readings above 2 are toxic to fish, to fix this the user must change 1/3 of the total water in the aquaponics system.

#### Nitrite

Recommended levels of nitrite are below 0.75ppm due to being very toxic to fish.
Readings above 0.75 could indicate damaged nitrifying bacteria.
Readings above 1 are toxic to fish, to fix this the user must change 1/3 of the total water in the aquaponics system.

#### Nitrate

Recommended levels of nitrate are below 300ppm due to being much less toxic to fish.
Readings above 150 indicate there are not enough plants in the system taking up the nutrients.
High Nitrate levels are fixed by planting more plants.

#### Temperature

Since there are multiple organisms cohabitating in this ecosystem all must be kept at a comfortable temperature.

Nitrifying bacteria die above 49 degrees C and below 0 degrees C
Below 4 degrees C there is no bacterial activity
Bacterial growth is slowed by 75% between 8-10 degrees C
Bacterial growth is slowed by 50% below 18 degrees C
Optimal bacterial growth is within the range of 25-30 degrees C

Root zone temperature differs between plant species but don't range outside 18 - 25 degrees C

Depending on fish species present depends on the preferable temperature.
One of the most common species used within aquaponics is Tilapia which are comfortable at 24 - 29 degrees C being a tropical freshwater fish.

Optimal Temperatures for a system with Tilapia for example would be 25 degrees C that would keep the plants fish and bacteria all comfortable.

#### Dissolved Oxygen (DO)

The number 1 cause of fish death and therefore system failure is a lack of oxygen in the system. There is a direct correlation between water temperature and the amount of oxygen available in it. The warmer the water the more the Dissolved Oxygen (DO) will drop.

To ensure that there is a good level DO is measured.
Different species require different saturation levels of oxygen. Cold water species such as Trout require 70% saturation or 6mg/L.
Tropical species such as Tilapia require 80% saturation or 5mg/L.

Therefore any reading below 5 will result in a warning to check equipment or lower temperature. Any level less than 5 will result in a tank of dead fish.

#### Electrical Conductivity (EC)

There are more ways to measure nutrients in the water than just Nitrate. A healthy system require other minerals that are present as salts in the system. Salts are measured with a device and a reading of electrical current is returned.

Readings above 1 are a good indication of nutrient availability in the water and good to keep a record of.

These inputs are stored within a csv file for later use. The user is then taken back to the main menu. The next Menu options will show what we can do with these entries.

### Option 2
Selecting 2 allows the user to view the previous data within the csv file then returns the user to the main menu.

### Option 3
Selecting 3 allows the user to delete a previous entry and appears as follows:

- User is shown the previous entries and is asked to enter the line number they are looking to delete.

- User is asked to confirm the line they are looking to delete.

- User is shown the line they have selected and asked if they want to delete that line with a Y/N prompt.

- Line is deleted and/or user is returned to the main menu.

### Option 4
Selecting 4 will analyse of all the data collected from each variable and will return a mean,median and standard deviation for each. The user will then be returned to the main menu.

### Option 5
Selecting 5 will exit the application.

**Thank you for reading this user guide.**


