
from scipy.stats import ttest_ind, chi2_contingency
import pandas as pd

def perform_t_test(df, group_col, value_col):
    """Performs an independent t-test between two groups."""
    groups = df[group_col].unique()
    if len(groups) != 2:
        return None, "T-test requires exactly two groups.", None

    group1 = df[df[group_col] == groups[0]][value_col]
    group2 = df[df[group_col] == groups[1]][value_col]
    
    stat, p_value = ttest_ind(group1.dropna(), group2.dropna())
    
    alpha = 0.05
    if p_value < alpha:
        conclusion = f"The difference is statistically significant (p={p_value:.3f})."
    else:
        conclusion = f"No significant difference was found (p={p_value:.3f})."
        
    return stat, p_value, conclusion

def perform_chi_squared(df, col1, col2):
    """Performs a Chi-squared test for association between two categorical variables."""
    contingency_table = pd.crosstab(df[col1], df[col2])
    chi2, p, _, _ = chi2_contingency(contingency_table)

    alpha = 0.05
    if p < alpha:
        conclusion = f"There is a significant association between {col1} and {col2} (p={p:.3f})."
    else:
        conclusion = f"There is no significant association between {col1} and {col2} (p={p:.3f})."
        
    return chi2, p, conclusion

