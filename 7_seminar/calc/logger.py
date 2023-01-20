import datetime


def Log(initiator, func, arg):
    # прописать полный путь, чтоб работало
    with open('Lesson_007\calc\logs.json', 'a') as log_file:
        time = datetime.datetime.now().strftime('%D %H:%M:%S')

        if arg == '__Start__':
            log_file.write('{')
            log_file.write('\n  "Table": [\n    {')
            log_file.write(f'\n      "TimeStart": "{time}"')
            arg = 'null'

        log_file.write(',\n      "Event":\n        {')
        log_file.write(f'\n          "Time": "{time}",')
        log_file.write(f'\n          "EventInitiator": "{initiator}",')
        log_file.write(f'\n          "ToFunction": "{func}",')
        log_file.write(f'\n          "Arguments": "{arg}"')
        log_file.write('\n        }')

        if arg == '__End__':
            log_file.write('\n    }')
            log_file.write('\n  ]')
            log_file.write('\n}')
            arg = 'null'