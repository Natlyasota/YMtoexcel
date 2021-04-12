import argparse
from YandexMetric2Excel import YandexMetric2Excel

########################################################################################################################
#                                                    Точка входа                                                       #
########################################################################################################################

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='yandex-metric-to-excel')
    parser.add_argument('-c', '--config', help='файл конфигурации', default='config.json')
    parser.add_argument('-f', '--from_date', help='начальная дата (2020-05-01 или {today|yesterday|ndaysAgo})',
                        default='6daysAgo')
    parser.add_argument('-t', '--to_date', help='конечная дата (2020-05-31 или {today|yesterday|ndaysAgo})',
                        default='today')
    parser.add_argument('-o', '--output', help='каталог для вывода', default='data')
    cmd_args = parser.parse_args()
    YandexMetric2Excel(cmd_args).to_excel()
