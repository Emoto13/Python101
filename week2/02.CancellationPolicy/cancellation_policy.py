from datetime import datetime, timedelta
import collections

#TODO:1.separate group_function to more functions?  2.check if percents are positive 3.test get_cancellation_orice

def validate_dates(start, now):
    if start < now:
        raise ValueError('Start date cannot be earlier than now')

def validate_price(price):
    if price <= 0:
        raise ValueError('Price cannot be negative or 0')


def validate_conditions(conditions):
    counter = 0

    for condition in conditions:
        if not condition.get('hours'):
            counter += 1
        if condition.get('hours', 0) > 24:
            raise ValueError('Hours cannot be > 24.')

    if counter != 1:
        raise ValueError('Invalid conditions.')


def ensure_conditions(conditions):
    for condition in conditions:
        if 'hours' not in condition.keys():
            condition['hours'] = 0
            break
    return conditions

def sort_conditions(conditions):
    return list(sorted(conditions, key=lambda k: k['hours'], reverse = True))

def group_conditions(sorted_conditions):
    if len(sorted_conditions) == 1:
        return [(24, 0)]

    lst = []
    for condition in sorted_conditions:
        lst.append(condition.get('hours'))
    list_of_intervals = []
        
    for i in range(1, len(lst)): 
        list_of_intervals.append((lst[i - 1], lst[i]))

    return list_of_intervals 


def check_if_hours_left_are_bigger_than_the_intervals(hours_left, intervals):
    biggest_value_in_intervals = intervals[0][0]
    if hours_left > biggest_value_in_intervals:
        return biggest_value_in_intervals
    return hours_left    


def get_current_condition(conditions, start, now):
    return conditions[0]


def get_cancellation_fee(price, percent):
    return price * (percent / 100)

def convert_left_time_to_hours_left(left_time):
    seconds_left = left_time.total_seconds()
    hours_left = seconds_left / 3600
    return hours_left

def find_exact_value_of_hours_left(hours_left, intervals):
    for interval in intervals:
        start_of_interval = interval[0]
        end_of_interval = interval[1]

        if hours_left <= start_of_interval and hours_left > end_of_interval:
            return end_of_interval
    return hours_left        

def find_percent_corresponding_to_the_hours_left(hours_left, sorted_conditions):
    for condition in sorted_conditions:
        if condition.get('hours') == hours_left:
            return condition.get('percent')     


def get_cancellation_policy(
    conditions,
    price,
    start,
    now
):
    validate_price(price)
    validate_dates(start, now)
    conditions = ensure_conditions(conditions)

    sorted_conditions = sort_conditions(conditions)
    intervals = group_conditions(sorted_conditions)

    left_time = start - now
    hours_left = convert_left_time_to_hours_left(left_time)

    interval_hours_left = 0
    interval_hours_left = check_if_hours_left_are_bigger_than_the_intervals(hours_left, intervals)
    interval_hours_left = find_exact_value_of_hours_left(hours_left, intervals)

    percent = find_percent_corresponding_to_the_hours_left(interval_hours_left, sorted_conditions)

    return get_cancellation_fee(price, percent)




def main():
    now = datetime.now()
    booking_start = now + timedelta(hours=24)
    price = 1000
    conditions = [
        {'hours': 24, 'percent': 10},
        {'hours': 12, 'percent': 50},
        {'hours': 6, 'percent': 80},
        {'percent': 100}
    ]

    result = get_cancellation_policy(
        conditions,
        price,
        booking_start,
        now
    )
    print(result)


if __name__ == '__main__':
    main()
