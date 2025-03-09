# Sudoku Performance Analysis

## Project Proposal

## Motivation  
This project aims to analyze my Sudoku playing performance over time. By collecting daily game statistics, I will explore patterns in my playing efficiency, error rates, and winning streaks.

## Data Source  
- The data will be manually recorded from a Sudoku mobile application. Each day, data will be collected separately for **Easy and Hard** difficulty levels. The key metrics that will be tracked are:  
  - Number of games played per day (Easy & Hard)  
  - Win rate (%) (Easy & Hard)  
  - Number of error-free (perfect) wins (Easy & Hard)  
  - Fastest completion time (Easy & Hard)  
  - Average completion time (Easy & Hard)  
  - Winning streaks (Easy & Hard)  

## Data Collection Plan  
Data will be recorded daily in a **CSV file**. Below is the sample CSV format:

Date,Easy Games,Easy Win Rate,Easy Perfect Wins,Easy Fastest Time,Easy Average Time,Easy Winning Streak,Hard Games,Hard Win Rate,Hard Perfect Wins,Hard Fastest Time,Hard Average Time,Hard Winning Streak
2025-03-10,4,90,3,3.2,4.5,5,2,70,1,5.8,7.3,2
2025-03-11,5,85,2,3.0,4.8,4,3,65,1,6.2,8.0,1

## Planned Analysis  
- **Performance Trends**: Tracking how win rate and average completion time change over time.  
- **Improvement Analysis**: Checking if my average completion time decreases.  
- **Frequency vs. Performance**: Analyzing if playing more frequently leads to better performance.  
- **Winning Streaks**: Identifying how often I maintain consecutive wins.  
- **Difficulty Level Comparison**: Comparing performance between Easy and Hard games to evaluate the impact of difficulty level.  

## Next Steps  
- **Collect Data**: Record daily statistics separately for Easy and Hard levels.  
- **Store Data**: Maintain a structured CSV file for consistency.  
- **Clean & Process Data**: Ensure correct formatting and handle missing values.  
- **Perform Exploratory Data Analysis (EDA)**: Use Python (`pandas`, `matplotlib`) to generate insights.  
- **Compare Performance**: Analyze trends in win rates, completion times, and streaks.  
- **Update Repository**: Regularly commit new data and analysis scripts to GitHub.  
- **Summarize Findings**: Create reports or visualizations to showcase key insights.  
