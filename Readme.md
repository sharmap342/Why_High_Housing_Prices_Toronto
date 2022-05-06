### Introduction 

We all know how unaffordable Toronto housing market is in the recent years. To understand the causes of hight housing prices in the City of Toronto, I took on this project. I did not do any modelling but did some exploratory data analysis and interactive visualization to understand the high housing prices for the city of Toronto.             

Check out this app to visualize housing prices for the different parts of Toronto.        

One of the biggest challenge during this project was unavailability of data in a form that can be used for analysis in python aka in the csv format. I had to download housing data as pdf files from Toronto Regional Real Estate Board's (TRREB) website (https://trreb.ca/index.php/market-news/market-watch/market-watch-archive). The data was scrapped from these pdf files csv files.   


### Project Structure 

This project is structured in the following way:
```nohighlight      
├── README.md          <- This file.    
├── data                    
│   ├── raw            <- The original, immutable data dump (due to large size not hosted on github).\        
│   ├── processed      <- transformed data to csv files                           
│   └── cleaned        <- The final, canonical data sets for modeling.                        
│                        
├── notebooks          <- Jupyter notebooks. `1.0-jqp-initial-data-exploration`Naming convention is a number\ 
│   ├── 1_Data_Scrapping.ipynb <- Describes the process for scrapping data from pdf files to csv files.  
│   ├── 2_Data_Cleaning_EDA    <- Describes the process of cleaning data and exploratory data analysis.   
│   └── 3_Data_Visualization   <- Describes the steps to make a interactive map visualization.  
│  
├── references         <- Some images to explain data visually.  
│  
├── reports            <- Report summarizing findings from the study.  
│  
├── requirements.txt   <- The requirements file for reproducing the analysis environment  
│  
├── src                <- Source code for deploying the app.  
│   ├── __init__.py    <- Makes src a Python module  
│   │  
│   ├── app.py         <- Script to make an app using streamlit  
│   │  
│   ├── data_dic.py    <- Script that describes the plotted variables in a dictionary  
│   │  
│   ├── plotly_vis.py  <- Script to make an interactive map visualization using plotly  
```

### References

The list of references is provided in the report. 