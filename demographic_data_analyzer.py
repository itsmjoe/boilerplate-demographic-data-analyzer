import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
  
    race_count = df['race'].value_counts()
  
    average_age_men = df.loc[df['sex'] == 'Male', 'age'].mean().round(decimals=1)
  
    education_counts = df['education'].value_counts()
    bachelors_count = education_counts.get('Bachelors', 0)
    total_count = education_counts.sum()
    percentage_bachelors = (bachelors_count / total_count * 100).round(decimals=1)
  
    salary_counts = df.groupby(df['education'])['salary'].value_counts()
    high_salary_counts = salary_counts.loc[(slice(None), '>50K')]
  
    higher_education_counts = salary_counts.loc[['Bachelors', 'Masters', 'Doctorate']].sum()
    lower_education_counts = salary_counts.sum() - higher_education_counts
  
    high_education_rich_count = high_salary_counts.loc[['Bachelors', 'Masters', 'Doctorate']].sum()
    lower_education_rich_count = high_salary_counts.sum() - high_education_rich_count
  
    higher_education_rich = float((high_education_rich_count / higher_education_counts * 100).round(decimals=1))
    lower_education_rich = float((lower_education_rich_count / lower_education_counts * 100).round(decimals=1))
  
    min_work_hours = df['hours-per-week'].min()
  
    hours_worked_salary_counts = df.groupby(df['hours-per-week'])['salary'].value_counts()
    min_hours_worked_salary_counts = hours_worked_salary_counts.loc[min_work_hours, :]
  
    num_min_workers = min_hours_worked_salary_counts.sum()
  
    rich_percentage = float((min_hours_worked_salary_counts.get('>50K', 0) / num_min_workers * 100).round(decimals=1))
  
    country_counts = df.groupby(df['native-country'])['salary'].count()
    country_rich_counts = df.groupby(df['native-country'])['salary'].apply(lambda x: (x == '>50K').sum())
    country_counts_df = pd.DataFrame({'counts': country_counts, 'rich-counts': country_rich_counts})
    country_counts_df['rich-percent'] = (country_counts_df['rich-counts'] / country_counts_df['counts'] * 100).round(decimals=1)
    top_country = country_counts_df.sort_values('rich-percent', ascending=False).head(1)
  
    highest_earning_country = top_country.index[0]
    highest_earning_country_percentage = top_country['rich-percent'].iloc[0]
  
    india_df = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_df['occupation'].value_counts().idxmax()
  

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
