import dart_fss as dart

def api_open():
    f = open('api_key.txt')
    api_key = f.readline()
    return api_key

api_key = api_open()

dart.set_api_key(api_key=api_key)

crp_list = dart.get_corp_list()
samsung = crp_list.find_by_corp_name('삼성전자', exactly=True)[0] #

fs = samsung.extract_fs(bgn_de='20200101')
fs.save()

