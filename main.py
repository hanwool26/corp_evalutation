import dart_fss as dart

api_key = 'cf795452c3cbfc9cd6f778baf04c4db18fd1acde'
dart.set_api_key(api_key=api_key)

crp_list = dart.get_corp_list()
samsung = crp_list.find_by_corp_name('삼성전자', exactly=True)[0] #

fs = samsung.extract_fs(bgn_de='20120101')

fs.save()

