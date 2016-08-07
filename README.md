# SortSteamGames

This sorts my Steam games by rating from Metacritic.


## Motivation

I have 550+ games in my Steam library. It is a glorious burden, but I needed to find out what games were "most recommended" to play.

## What is actually happening

First I gathered my current game library "app_id"s from SteamAPI. It comes as a JSON file and only contains appids and gametime played.
To gather the game titles that are in my library, I have to parse my game library's JSON file along with a separate JSON file that 
contains the entire steam database of app_ids and corresponding game titles. From there I can determine what games are in my steam 
library and I save those titles and app_ids to a csv file. Then I can scrape metacritic for all the reviewed PC games and save that
information into a csv. Lastly, use excel to only show the matching data between the two csv files and easily sort by the highest 
critic or user ratings.
