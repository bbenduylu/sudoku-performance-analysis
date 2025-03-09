
# Sudoku Performance Analysis

# Project Proposal

# Motivation  
This project aims to analyze my Sudoku playing performance over time. By collecting daily game statistics, I will explore patterns in my playing efficiency, error rates, and winning streaks.

# Data Source
-The data will be manually recorded from a Sudoku mobile application. Each day, data will be collected separately for **Easy and Hard** difficulty levels. The key metrics that will be tracked are:  
- Number of games played per day (Easy & Hard)  
- Win rate (%) (Easy & Hard)  
- Number of error-free (perfect) wins (Easy & Hard)  
- Fastest completion time (Easy & Hard)  
- Average completion time (Easy & Hard)  
- Winning streaks (Easy & Hard)  
 

# Data Collection Plan  
Data will be recorded daily in a **CSV file**. Below is the sample CSV format:  

```csv
Date,Easy Games,Easy Win Rate,Easy Perfect Wins,Easy Fastest Time,Easy Average Time,Easy Winning Streak,Hard Games,Hard Win Rate,Hard Perfect Wins,Hard Fastest Time,Hard Average Time,Hard Winning Streak
2025-03-10,4,90,3,3.2,4.5,5,2,70,1,5.8,7.3,2
2025-03-11,5,85,2,3.0,4.8,4,3,65,1,6.2,8.0,1

# Planned Analysis  
- Performance trends: Tracking how win rate and average completion time change over time.  
- Improvement analysis: Checking if my average completion time decreases.  
- Frequency vs. performance: Analyzing if playing more frequently leads to better performance.  
- Winning streaks: Identifying how often I maintain consecutive wins.
- Comparing performance between Easy and Hard games to evaluate the impact of difficulty level.

# Next Steps 
1. Start recording daily Sudoku statistics separately for Easy and Hard levels.
2. Store data in a structured CSV file.  
3. Begin initial exploratory data analysis (EDA) using Python.  
4. Regularly update the GitHub repository with findings and code.  


# Project Repository: [Sudoku Performance Analysis](https://github.com/bbenduylu/sudoku-performance-analysis)

