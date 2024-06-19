def solution(numbers):
    alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for k, v in zip(alpha, range(10)):
        numbers = numbers.replace(k,str(v))
    return int(numbers)