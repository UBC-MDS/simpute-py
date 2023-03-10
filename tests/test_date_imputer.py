from simpute_py.date_imputer import date_imputer
from io import StringIO
import pandas as pd
import pytest


csv_string = """
Case #,Date,Continent,Country,Deaths,Driver,Description,Source
1,4/2/2013,North America,USA,2,0," Tesla car crashes into tree, burns ",https://www.tag24.de/nachrichten/unfall/tesla-kracht-gegen-baum-und-brennt-aus-zwei-tote-und-drei-schwerverletzte-2584180
2,11/2/2013,North America,USA,1,0, Tesla veers into oncoming traffic ,https://www.ksbw.com/article/hollister-crash-kills-4-tesla-big-rig/40898893?utm_campaign=snd-autopilot
3,7/4/2014,North America,USA,3,1, Unlicensed driver hits pedestrian ,https://yle.fi/uutiset/3-12576787
4,7/4/2014,North America,USA,,1, Man in wheelchair hit crossing road , https://www.wfla.com/news/man-in-wheelchair-fatally-struck-by-suv-tesla-in-pasco-county/
5,,,USA,1,0, Tesla crashes at high speed ,https://www.boothbayregister.com/article/southport-accident-victim-named/163623
6,12/30/2014,North America,USA,1,1, Tesla hits motorcycle ,https://www.ksl.com/article/50445474/motorcyclist-dies-in-i-15-collision-with-tesla-on-autopilot-uhp-says
7,1/22/2015,North America,USA,1,1, Tesla goes airborne and crashes ,https://www.wpxi.com/news/local/least-1-person-killed-fatal-crash-pine-township/ARDDKESNLZAX7EABJBPELT4KZY/?outputType=amp
8,6/22/2015,North America,USA,1,1, Out of control Tesla hits pedestrians ,https://whatchinareads.com/article/?uid=00e9b6f6ff4d11ec98bbc7030b3aab5e
9,11/18/2015,North America,USA,1,0,3-car accident involving Tesla,https://fox5sandiego.com/traffic/82-year-old-killed-in-rollover-crash-identified/
10,12/22/2015,North America,Canada,1,1, Motorcycle crashes into Tesla ,https://www.staradvertiser.com/2022/07/09/breaking-news/kihei-man-46-dead-after-motorcycle-collision-in-wailuku/
"""

def test_date_imputer():
    col = 'Date'
    csvStringIO = StringIO(csv_string)

    # before imputation there are null values
    input_df = pd.read_csv(csvStringIO, sep=",", parse_dates=['Date'])
    assert input_df.loc[:, col].isnull().any()

    # after imputation, no null values anymore
    output_df = date_imputer(input_df, col)
    assert output_df.loc[:, col].isnull().any() == False
