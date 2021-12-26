# insurance-calcs.py
## Description
- quotes for coverage between $11,500 and $19,500
- split into low and high coverage segments
- linear regression
- plots quotes and best fit for both segments

## Screenshot
![plot](https://user-images.githubusercontent.com/46288522/146912676-0fd0361a-d58a-41aa-9264-0eff2c382bd1.jpg)

# weather-analysis.py
## Description
- historical weather data: 1943-present, minimum/maximum daily temperatures (source : BOM)
- cleaned data, merged data1 and data2, calculated daily difference value (max - min)
- created rolling means, std for each series
- plotted results

## Observations
- increase in both max and min over time period, however daily difference difference is steady
- daily difference std is as expected at sqrt(max_std^2 + min_std^2) / sqrt(2)

## Possible further analysis
- normalise std series by mean series, what is the correlation?
- show Bollinger shading (mean plus/minus 2*std)
- break max/min into seasons, is there a difference in trend at season level?
- changes to hottest/coldest tme of year? earlier/later?

## Screenshot
![rolling_mean](https://user-images.githubusercontent.com/46288522/147409377-f12bcdfe-88d4-4ed0-ab72-7fed539567ba.jpg)
![rolling_std](https://user-images.githubusercontent.com/46288522/147409379-5eb0b274-8533-4182-b144-e5264d77ae60.jpg)
