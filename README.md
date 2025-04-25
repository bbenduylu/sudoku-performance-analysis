# Sudoku Performance Analysis
This project analyzes the performance of Sudoku games played by the user, focusing on completion time, win rates, and the difficulty levels. The goal is to understand how the player's win rate varies across different difficulty levels and over time, as well as the relationship between the time spent completing the puzzle and the win rate.

## Project Objective
The objective of this project is to:
- Analyze the win rates and completion times for easy and hard Sudoku puzzles.
- Investigate whether there is a correlation between time spent on a puzzle and the success rate.
- Examine how win rates change over time.

## Data Source  
- The data will be manually recorded from a Sudoku mobile application. Each day, data will be collected separately for **Easy and Hard** difficulty levels. The key metrics that will be tracked are:  
  - Number of games played per day (Easy & Hard)  
  - Win rate (%) (Easy & Hard)  
  - Number of error-free (perfect) wins (Easy & Hard)  
  - Fastest completion time (Easy & Hard)  
  - Average completion time (Easy & Hard)  
  - Winning streaks (Easy & Hard)  

## Data Collection Plan  
Data will be recorded daily in a **CSV file**. Below is the sample data:  

| Date       | Easy Games | Easy Win Rate | Easy Perfect Wins | Easy Fastest Time | Easy Average Time | Easy Winning Streak | Hard Games | Hard Win Rate | Hard Perfect Wins | Hard Fastest Time | Hard Average Time | Hard Winning Streak |
|------------|------------|---------------|--------------------|-------------------|-------------------|---------------------|------------|---------------|--------------------|-------------------|-------------------|---------------------|
| 2025-03-10 | 4          | 90%           | 3                  | 3.2               | 4.5               | 5                   | 2          | 70%           | 1                  | 5.8               | 7.3               | 2                   |
| 2025-03-11 | 5          | 85%           | 2                  | 3.0               | 4.8               | 4                   | 3          | 65%           | 1                  | 6.2               | 8.0               | 1                   |


### Hypothesis 1 - Easy vs Hard Win Rate Comparison

To test whether there is a statistically significant difference in win rates between easy and hard Sudoku puzzles, an independent t-test was conducted.

**H₀:** The mean win rates for easy and hard puzzles are equal.
**H₁:** The mean win rates for easy and hard puzzles are different.

### Visualization:

**Bar Chart Comparing Easy vs Hard Win Rates:**

![Win Rate Comparison](visualizations/screenshots/bar_chart.png)

