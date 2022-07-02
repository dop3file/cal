from calendar import monthrange

import pytz
import datetime

import colorama
from colorama import Fore, Back, Style


def draw_calendar(date: datetime.datetime):
    month: str = date.strftime("%B %Y")
    time: str = date.strftime("%H:%M")
    week_days_header = ['Su','Mo','Tu','We','Th','Fr','Sa']
    month_count_days: int = monthrange(date.year, int(date.strftime("%m")))[1]
    month_first_week_day_index: int = week_days_header.index(datetime.datetime(date.year, date.month, 1).strftime('%a')[:2])
    today_number_day = int(date.strftime('%d'))


    month_blank_step: str = int((len(' '.join(week_days_header)) - len(month)) / 2) * ' '
    time_blank_step: str = int((len(' '.join(week_days_header)) - len(time)) / 2) * ' '

    print(month_blank_step + month + month_blank_step)
    print(time_blank_step + time + time_blank_step)
    [print(f'{week_day} ', end='') for week_day in week_days_header]
    print('')

    print(' ' * (3 * month_first_week_day_index), end='')

    last_date_number_in_first_line = 0

    # print first date numbers line
    for _, date_number in zip(range(month_first_week_day_index, 7), range(1, month_count_days + 1)) :
        if date_number == today_number_day:
            print(Back.WHITE + Fore.BLACK + f' {date_number}', end=' ')
            print(Style.RESET_ALL, end='')
        else:
            print(f' {date_number}', end=' ')
    else:
        last_date_number_in_first_line = date_number
        print('')

    #print other date numbers line
    for week_day_index, date_number in enumerate(range(last_date_number_in_first_line + 1, month_count_days + 1)):
        if week_day_index % 7 == 0 and week_day_index != 0:
            print('')
        print(f' {date_number} ' if len(str(date_number)) == 1 else f'{date_number} ', end='')

def main():
    colorama.init()

    timezone_minsk = pytz.timezone("Europe/Minsk")
    date_minsk: datetime.datetime = datetime.datetime.now(timezone_minsk)

    draw_calendar(date_minsk)

if __name__ == '__main__':
    main()
