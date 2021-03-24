import datetime

now = datetime.datetime.now()

five_day_ago = now - datetime.timedelta(days=5)

now_string = now.strftime("%Y-%m-%d_%H-%M-%S")

file_name = 'save_fivedayago_time_' + now_string + '.txt'

time_file = open(file_name, 'w')

time_file.write(str(five_day_ago))

time_file.close()

