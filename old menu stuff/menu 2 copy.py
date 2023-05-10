import time

def split(word):
    return [char for char in word]

def month_string_to_number(string):
    m = {
        'janv': "01",
        'févr': "02",
        'mars': "03",
        'avri':"04",
         'mai':"05",
         'juin':"06",
         'juil':"07",
         'août':"08",
         'sept':"09",
         'octo':10,
         'nove':11,
         'déce':12
        }
    s = string.strip()[:4].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')

def create_file_name(day1):
    app = []
    year = time.strftime("%Y")
    year = year.lstrip("2")
    year = year.lstrip("0")
    print(year)
    month = day1[2]
    
    month = month_string_to_number(month)
    month = str(month)
    day = day1[1]
    if len(day) <= 2:
        day = "0" + day
    app = year + month + day
    return app




file_name = create_file_name(lundi_dates)
