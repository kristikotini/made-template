Project Plan
===============

Assessing the Impact of Weather on Accidents in German Regions
---------------------------------------------------------------


## Main Question
**_How does weather, particularly seasonal variations, impact the rate and nature of accidents in different regions of Germany?"_**

## Description
Road safety is an important concern in Germany. Accidents are one of the main indicators of how safe a road is.
Weather conditions, particularly the influence of precipitation play a crucial role in these accidents.
This project focuses on analyzing the relation between weather factors and road accidents in various German regions.

Accidents involving road vehicles are a significant problem due to their impact on human lives, infrastructure, and the economy.
Weather conditions can increase the risk of these happening, but their exact influence needs to be studied.

Using advanced data engineering and analytical methods, in this project will examine historical accident data from 10 Bundesländer/Federal States and detailed weather/precipitation data.
This analysis aims to reveal patterns, correlations, and potential causal relationships between weather conditions and accidents.

## Datasources

### Datasource1: Accidents: Federal states, months, location, severity of injury
* Metadata URL: [Accidents Metadata](https://www.govdata.de/ckan/dataset/verungluckte-bundeslander-monate-ortslage-schwere-derverletzung.rdf)
* Data URL: [Accidents Data](https://www-genesis.destatis.de/genesis/downloads/00/tables/46241-0024_00.csv)
* Data Type: `text/CSV`


This dataset includes road traffic accident statistics for 10 federal states in Germany throughout the timeline [**Jan-2021**, **Nov-2022**]. <br>
It has information for each state divided on the following sub-categories:

- Place/Ortslage
    - inner town/innerorts
    - out of town (without motorways)/außerorts (ohne Autobahnen)
    - on highways/auf Autobahnen
- Severity of injury/Schwere der Verletzung
    - Killed/Getötete 
    - Slightly injured/Leichtverletzte
    - Seriously injured/Schwerverletzte
    - In total/Insgesamt

For each place we have all 4 severities of injury and a total for that place. As well as an overall total for the number of accidents for that land.

### Datasource2: Regional Averages GE - Monthly - Precipitation
* Data URL: [Main dir](https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/precipitation/)
    * All data of 12 months:
        * [January](https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/precipitation/regional_averages_rr_01.txt)
        * [February](https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/precipitation/regional_averages_rr_02.txt)
        * [March](https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/precipitation/regional_averages_rr_03.txt)
        * [April](https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/precipitation/regional_averages_rr_04.txt)
        * [May](https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/precipitation/regional_averages_rr_05.txt)
        * [June](https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/precipitation/regional_averages_rr_06.txt)
        * [July](https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/precipitation/regional_averages_rr_07.txt)
        * [August](https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/precipitation/regional_averages_rr_08.txt)
        * [September](https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/precipitation/regional_averages_rr_09.txt)
        * [October](https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/precipitation/regional_averages_rr_10.txt)
        * [November](https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/precipitation/regional_averages_rr_11.txt)
        * [December](https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/precipitation/regional_averages_rr_12.txt)
* Data Type: `text/CSV`

Each dataset includes average precipitation for a given month of all the federal states in Germany from the year **1881** till **2023**.

## Work Packages

1. Data pipeline enhancement [#1][i1]
2. Tests for Pipeline [#2][i2]
3. Questions and relations [#3][i3]
4. Visuals [#4][i4]
5. Final report [#5][i5]
6. General refactor & last enhancements [#6][i6]

[i1]: https://github.com/kristikotini/made-template/issues/1
[i2]: https://github.com/kristikotini/made-template/issues/2
[i3]: https://github.com/kristikotini/made-template/issues/3
[i4]: https://github.com/kristikotini/made-template/issues/4
[i5]: https://github.com/kristikotini/made-template/issues/5
[i6]: https://github.com/kristikotini/made-template/issues/6
