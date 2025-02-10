import numpy as np
from collections import Counter

def statistical_analysis(data):
    """
    computing basic statistical calculations!
    :param data: numpy array numbers
    :return: dictionary containing mean, median, variance, standard deviation, minimum, and maximum
    """

    data = np.array(data)
    mean = np.mean(data)
    median = np.median(data)
    variance = np.var(data)
    stdev = np.std(data)
    min_val = np.min(data)
    max_val = np.max(data)

    count = Counter(data)       #counting occurrence of each number.
    most_common = max(count.values())       #finding highest occurrence count.

    if most_common == 1:
        mode = 'NO MODE'
    else:
        mode = [float(num) for num, freq in count.items() if freq == most_common]       #all numbers that appear most frequently.
    
    return {
        '🔥 Mean' : mean,
        '🔥 Median' : median,
        '🔥 Mode' : mode,
        '🔥 Variance' : variance,
        '🔥 Standard Deviation' : stdev,
        '🔥 Minimum Value' : min_val,
        '🔥 Maximum Value' : max_val
    }

def user_info():
    while True:
        user = input('🔎 ENTER THE DATA (Separated by spaces) : ')
        numbers = user.split()
        try:
            value = list(map(float, numbers))
        except ValueError:
            print('ERROR : Please enter only integers❗')
            continue

        if len(numbers) < 3:
            print('Enter minimum 3 values❗')
            continue

        return value

user_data = user_info()
result = statistical_analysis(user_data)

print('\n🎉 STATISTICAL ANALYSIS RESULTS 🎉')
for key,value in result.items():
    print(f'{key} : {value:.2f}' if isinstance(value, (int, float)) else f'{key} : {value}')        #convert integers into float values of 2 decimal places or print value if its not an integer!


