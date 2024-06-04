import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series(df['race'].value_counts().fillna(0))

    # What is the average age of men?
    age = df.loc[df['sex'] == 'Male', ['sex', 'age']]
    average_age_men = round(age['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    whole_num = df['education'].count()
    bachelors = df.loc[df['education'] == 'Bachelors', ['education']]
    bach_num = bachelors['education'].count()
    percentage_bachelors = round(bach_num * 100 / whole_num, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    options = ['Bachelors', 'Masters', 'Doctorate']
    advanced = df.loc[df['education'].isin(options), ['education', 'salary']]
    higher_education = advanced['education'].count()
    lower = df.loc[~df['education'].isin(options), ['education', 'salary']]
    lower_education = lower['education'].count()

    # percentage with salary >50K
    advanced_rich = advanced.loc[advanced['salary'] == '>50K']
    advanced_rich_num = advanced_rich['education'].count()
    higher_education_rich = round(advanced_rich_num * 100 / higher_education, 1)
    lower_rich = lower.loc[lower['salary'] == '>50K']
    lower_rich_num = lower_rich['education'].count()
    lower_education_rich = round(lower_rich_num * 100 / lower_education, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df.loc[df['hours-per-week'] == 1, ['hours-per-week', 'salary']]
    num_min_workers = min_workers['hours-per-week'].count()
    rich_min = min_workers.loc[min_workers['salary'] == '>50K']
    rich_min_num = rich_min['hours-per-week'].count()
    rich_percentage = round(rich_min_num * 100 / num_min_workers, 1)

    # What country has the highest percentage of people that earn >50K?
    df_high_in = df.loc[df.salary == '>50K']
    df_pop = df.groupby('native-country')['native-country'].count()
    df_high_in_pop = df_high_in.groupby('native-country')['native-country'].count()
    highest_earning_country = (df_high_in_pop/df_pop *100).idxmax()
    highest_earning_country_percentage = round(df_high_in_pop/df_pop * 100, 1).max()

    # Identify the most popular occupation for those who earn >50K in India.

    rich_people = df.loc[df['salary'] == '>50K']
    rich_India = rich_people.loc[df['native-country'] == 'India']
    occupations = rich_India.groupby('occupation')['occupation'].count()
    top_IN_occupation = occupations.idxmax()

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
