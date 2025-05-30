# Sudoku Performance Analysis

This project analyzes personal performance data from Sudoku games, focusing on how player success relates to completion time, win rate, and experience.

## Contents
- Classification analysis to find a critical time threshold for success
- Regression modeling to predict average completion time based on performance features
- ROC curve evaluation and linear regression with R² = 0.73

## Files
- `DSAProject-2.ipynb`: Main analysis notebook (Colab-based)
- `data/`: Optional folder for daily performance logs

## Summary
Players who complete easy-level Sudoku puzzles in under 4.47 minutes are significantly more likely to win (AUC = 0.91). Performance metrics such as win rate, experience, and streaks were strong predictors of completion time.

## Future Work
- Extend analysis to hard-level puzzles
- Develop adaptive feedback based on performance trends
- Investigate time-based fatigue or time-of-day effects on performance.
