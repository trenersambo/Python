# МОДУЛЬ № 4: создатель html-файла

# импорт 3-х функций из модуля № 3 USER

from user import tempr_view
from user import press_view
from user import speed_view


def create(device=1):
    style = 'style="font-size:18px; color:red;" '
    html = '<html>\n  ' \
           '<head></head>\n  ' \
           '<body>\n'

    html += f' <p {style}>Температура: {tempr_view(device)} c</p>\n'

    html += f' <p {style}>Wind_speed: {speed_view(device)} m/s</p>\n'

    html += f' <p {style}>Pressure: {press_view(device)} mmHg</p>\n'

    html += '  </body>\n' \
            '</html>'

    with open('index.html', 'a') as page:
        page.write(html)

    return html


def new_create(data, device=1):
    t, p, w = data
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>Temperature: {} c</p>\n' \
        .format(style, t)
    html += '    <p {}>Wind_speed: {} m/s</p>\n' \
        .format(style, w)
    html += '    <p {}>Pressure: {} mmHg</p>\n' \
        .format(style, p)
    html += '  </body>\n</html>'

    with open('new_index.html', 'w') as page:
        page.write(html)

    return data