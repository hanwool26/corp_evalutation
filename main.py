import dart_fss as dart

def api_open():
    f = open('api_key.txt')
    api_key = f.readline()
    return api_key

def get_corp_info(corp_title="삼성전자"):
    return crp_list.find_by_corp_name(corp_title, exactly=True)[0]

api_key = api_open()
dart.set_api_key(api_key=api_key)

crp_list = dart.get_corp_list()  # Loading corp list

if __name__ == '__main__':
    print("기업명 :", end=' ')
    corp_title = input()
    corp_info = get_corp_info(corp_title)
    if corp_info == None:
        print(f'기업 없음{corp_title}')
    else:
        fs = corp_info.extract_fs(bgn_de='20200101')
        fs.save()



