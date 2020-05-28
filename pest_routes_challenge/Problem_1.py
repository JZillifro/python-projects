# Jacob Zillifro

from datetime import date, timedelta
import argparse

# start: season start
# end: season end
# freq: frequency
# last_service: last completed service
# n: Amount of upcoming services to calculate
def print_service_dates(start, end, freq, last_service, n):
    i = 0
    cur = start
    while i < n:
        if cur <= (last_service + timedelta(days=freq)):
            cur = last_service + timedelta(days=freq)

        if cur > end:
            if last_service + timedelta(days=freq/2) < end:
                cur = end
                last_service = cur
                print(last_service)
                i += 1

            start = start.replace(year=start.year+1)
            end = end.replace(year=end.year + 1)
            cur = start
            last_service = cur - timedelta(days=freq)

        else:
            last_service = cur
            print(last_service)
            i+=1

# needs input checking!
parser = argparse.ArgumentParser()
parser.add_argument("-ss", "--ss")
parser.add_argument("-se", "--se")
parser.add_argument("-f", "--f", type=int)
parser.add_argument("-lcs", "--lcs")
parser.add_argument("-n", "--n", type=int)
args = parser.parse_args()

lcs_input = args.lcs
ss_input = args.ss
se_input = args.se
freq_input = args.f
n = args.n

last_service_array = [int(x) for x in lcs_input.split('/')]
last_service_date = date(year=last_service_array[2], month=last_service_array[0], day=last_service_array[1])

# find the proper start date
start_service_array = [int(x) for x in ss_input.split('/')]
start_service_date = date(year=last_service_date.year, month=start_service_array[0], day=start_service_array[1])

# find the proper end date
end_service_array = [int(x) for x in se_input.split('/')]
end_service_date = date(year=start_service_date.year, month=end_service_array[0], day=end_service_array[1])
if(end_service_date < start_service_date):
    end_service_date = end_service_date.replace(year=(end_service_date.year+1))

print_service_dates(start_service_date, end_service_date, freq_input, last_service_date, n)