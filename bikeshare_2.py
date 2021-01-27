import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a **city, month, and day** to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('What city would you like to investigate? chicago, new york city or washington?')
        city = city.lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print('I do not recognise that city please try again')
        else:
            break
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('What moth would you like to investigate? all, january, february, march, april, may or june?')
        month = month.lower()
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print('I do not recognise that month please try again')
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('What day of the week would you like to investigate? all, monday, tuesday, wednesday, thrusday, friday, saturday or sunday?')
        day = day.lower()
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday', 'sunday'):
            print('I do not recognise that day of the week please try again')
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and *filters by month and day* if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]

    print('Most Common Month:', popular_month)

    # display the most common day of week
    popular_day_of_week = df['day'].mode()[0]

    print('Most Common Day_of_Week:', popular_day_of_week)

    # display the most common start hour

    # extract hour from Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    print('Most Common Start Station:', popular_start_station)


    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print('Most Common End Station:', popular_end_station)


    # display most frequent combination of start station and end station trip
    # New column created with the addition of columns Start and End Station
    df['Trip Stations'] = df['Start Station'] +' Finishing on ' + df['End Station']
    popular_trip = df['Trip Stations'].mode()[0]

    print('Most Common Trip:', popular_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    # convert the End Time column to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])

    # New column created with the Travel Time
    df['Travel Time'] = df['End Time'] - df['Start Time']

    # Calculation of most popular travel time and transform to minutes

    popular_travel_time = df['Travel Time'].mode()[0]

    popular_travel_time = popular_travel_time.total_seconds()/60
    print('Most Common Travel Time (minutes):', popular_travel_time)

    # display mean travel time
    mean_travel_time = df['Travel Time'].mean()

    mean_travel_time = mean_travel_time.total_seconds()/60
    print('Mean Travel Time (minutes):', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats_1(df):
    """Displays statistics on bikeshare users for Chicago & New York City."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types = df['User Type'].value_counts()
    print('User types are:', user_types)

    # Display counts of gender after filtering for Washington that does not record geder data
    gender_count = df['Gender'].value_counts()
    print('Gender counts are:', gender_count)

    # Display earliest, most recent, and most common year of birth
    earliest_yob = df['Birth Year'].min()

    print('Oldest traveler Birth Year:', earliest_yob)

    latest_yob = df['Birth Year'].max()

    print('Youngest traveler Birth Year:', latest_yob)

    most_common_yob = df['Birth Year'].mode()[0]

    print('Most Common Year of Birth:', most_common_yob)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats_2(df):
    """Displays statistics on bikeshare users for Washington."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types = df['User Type'].value_counts()
    print('User types are:', user_types)

    # Reminder that Washington does not record gender data or year of birth

    print('Reminder: Washington does not record gender data or year of birth')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Prompts user if they want to see 5 rows of data at a time"""

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no?\n').lower()
    start_loc = 0
    view_display = 'yes'
    if view_data == 'yes':
        while view_display =='yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_display = input('\nDo you wish to see the next 5 rows of data?: Enter yes or no.\n').lower()

    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city != 'washington':
            user_stats_1(df)
        else:
            user_stats_2(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
