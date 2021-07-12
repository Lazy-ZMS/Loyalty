import datetime

def get_dict_file_from_kass(path):

    chequeItems = dict()

    f = open(path, 'r', 1, 'OEM')
    for line in f:
        # print(line)
        line = line.replace('\n', '')
        if not line:
            continue

        spisok = line.split('=')

        if len(spisok) < 2:
            continue

        cur_elem = spisok[1]

        if not spisok[1]:
            continue

        if spisok[0] == 'CASHCODE':
            cur_elem = int(spisok[1])
        elif spisok[0] == 'SHIFT':
            cur_elem = int(spisok[1])
        elif spisok[0] == 'SCODE':
            cur_elem = int(spisok[1])
        elif spisok[0] == 'DATE':
            cur_elem = datetime.date(2021, 5, 20)
        elif spisok[0] == 'TIME':
            cur_elem = datetime.time(15, 27)
        elif spisok[0] == 'CHECKNUM':
            cur_elem = int(spisok[1])
        elif spisok[0] == 'SUM1':
            cur_elem = float(spisok[1])
        elif spisok[0] == 'SUM2':
            cur_elem = float(spisok[1])
        elif spisok[0] == 'SUM':
            cur_elem = float(spisok[1])
        elif spisok[0] == 'SUMTYPE':
            cur_elem = int(spisok[1])
        elif spisok[0] == 'DISCTYPE':
            cur_elem = int(spisok[1])
        elif spisok[0] == 'DISCPERC':
            cur_elem = int(spisok[1])
        elif spisok[0] == 'DISCABS':
            cur_elem = int(spisok[1])
        elif spisok[0] == 'DOCNUM':
            cur_elem = int(spisok[1])
        elif spisok[0] == 'ERRORCODE':
            cur_elem = int(spisok[1])
        elif spisok[0] == 'CDEPT':
            cur_elem = int(spisok[1])

        chequeItems[spisok[0]] = cur_elem

    f.close()
    for str1 in chequeItems:
        print(str(str1) + ' = ' + str(chequeItems[str1]))

    return(chequeItems)

    # print(chequeItems)

    # print(chequeItems['TIME'] > datetime.time(16, 20))