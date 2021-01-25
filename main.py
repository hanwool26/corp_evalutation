import dart_fss as dart

def api_open():
    f = open('api_key.txt')
    api_key = f.readline()
    return api_key

def get_corp_info(crp_list, corp_title="삼성전자"):
    return crp_list.find_by_corp_name(corp_title, exactly=True)

if __name__ == '__main__':
    api_key = api_open()  # API KEY read 하여 string 할당
    dart.set_api_key(api_key=api_key)

    crp_list = dart.get_corp_list()  # Loading corp list
    print("기업명 :", end=' ')
    corp_title = input()
    corp_info = get_corp_info(crp_list, corp_title)
    if corp_info == None:
        print(f'기업 없음{corp_title}')
    else:
        fs = corp_info[0].extract_fs(bgn_de='20200101')
        print(type(fs))


