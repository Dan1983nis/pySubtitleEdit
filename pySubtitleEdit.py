import sys
import datetime
import os

def main():
    if len(sys.argv) < 3:
        print('Usage: python main.py <srt file> <delay (in sec)> <optional: format time input, for example: %H:%M:%S,%f>')
        quit()
    file_name = os.path.join(os.getcwd(), sys.argv[1])
    delay_time = int(sys.argv[2])
    format = "%H:%M:%S,%f"
    if len(sys.argv) == 4:
        format = sys.argv[3]
    value_delay_input = delay_time
    sign = int(value_delay_input / abs(value_delay_input))
    time_delay_value = abs(value_delay_input)
    delay_time = datetime.timedelta(seconds = time_delay_value)
    zero_time = datetime.datetime.strptime('0', '%S')
    lines=[]
    with open(file_name,'r') as fr:
        lines = fr.readlines()
        fr.close
    tmp_file_name = file_name[:file_name.rfind('\\')] + '\\tmp_' + file_name[file_name.rfind('\\')+1:]
    print('Saving modified file to: {0}'.format(tmp_file_name))
    with open(tmp_file_name,'w') as fw:
        for line in lines:
            new_line = line
            elements = line.split(' ')
            if '-->' in elements:
                start_time = datetime.datetime.strptime(elements[0], format)
                end_time = datetime.datetime.strptime(elements[2].strip('\n'), format)
                prevoius_start_time = start_time
                if (sign == -1):
                    start_time = start_time - delay_time
                    if start_time > zero_time:
                        end_time = end_time - delay_time
                    else:
                        start_time = prevoius_start_time
                elif (sign == 1):
                    start_time = start_time + delay_time
                    if start_time > zero_time:
                        end_time = end_time + delay_time
                    else:
                        start_time = prevoius_start_time
                my_list = [str(start_time.strftime(format))[:-3], " ", "-->", " ",str(end_time.strftime(format))[:-3]]
                new_line = ''.join(my_list) + '\n'
            fw.write(new_line)
        fw.close()


if __name__ == '__main__':
    main()
