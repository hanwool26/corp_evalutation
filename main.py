import dart_fss as dart

class Corp_evaluation():
    def __init__(self):
        print('Class 생성')
        with open('api_key.txt') as f:
            self.api_key = f.readline()

    def load_dart(self):
        dart.set_api_key(self.api_key)
        self.crp_list = dart.get_corp_list()

    def get_corp_info(self, corp_title):
        return self.crp_list.find_by_corp_name(corp_title, exactly=True)

if __name__ == '__main__':
    corp = Corp_evaluation()
    corp.load_dart()

    corp_title = input()
    corp_info = corp.get_corp_info(corp_title)

    if corp_info == None:
        print(f'기업 없음{corp_title}')
    else:
        fs = corp_info[0].extract_fs(bgn_de='20200101')
        print(type(fs))


