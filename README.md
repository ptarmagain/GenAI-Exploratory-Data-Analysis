# Exploratory Data Analysis with GenAI

This is an application that uses generative AI to perform a low level EDA for a variety of data sources.

Example use
```
python explore.py
Enter line by line the files you wish to analyze. Enter 'done' when done.
cities
weather
electricity
done
Potential columns to join on: 'date\_time' and 'city' (assuming the 'date\_time' and 'city' values align in both datasets).

Useful insights:

* Understand weather patterns in different cities by analyzing temperature, precipitation, and wind speed alongside power consumption and production.
* Identify any correlations between power consumption, power production, and weather conditions in various cities.
* Determine if there are specific times of day, days of the week, or seasons when power consumption or production significantly increases or decreases in certain cities.
* Investigate the impact of fossil-free percentage on power consumption and production in different cities.
* Explore potential seasonal or regional trends by comparing power consumption and production data across cities and over time.
* Analyze the temporal granularity of the data to determine if higher granularity (e.g., hourly) provides more valuable insights compared to lower granularity (e.g., daily).
```
