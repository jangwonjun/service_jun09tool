import gspread
from oauth2client.service_account import ServiceAccountCredentials

class product():
    def __init__(self):
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive',
        ]

        product = []
        self.product_review_data = []
        self.result = []
        self.one_raw_product = []
    

        json_file_name = 'corded-cable-406413-ff3111370462.json'

        credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
        gc = gspread.authorize(credentials)

        spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1wjeReW66xOzi5oqvf2U94pcTaM66DyPkWVWcFa5fXpI/edit?usp=sharing'

        # 스프레스시트 문서 가져오기
        doc = gc.open_by_url(spreadsheet_url)

        # 시트 선택하기
        worksheet = doc.worksheet('상품조회')

        # 범위(셀 위치 리스트) 가져오기
        range_list = worksheet.range('A2:D3')

        self.index_num = worksheet.row_count

        # 범위에서 각 셀 값 가져오기
        for cell in range_list:
            product.append(cell.value)
    
    
        self.one_raw_product = [product[i:i+4] for i in range(0, len(product), 4)]
                
        print(f"raw matterial : {self.one_raw_product}")
        
        for i in range(len(self.one_raw_product)):
            inner_list = []  # 각 아이템을 담을 내부 리스트 생성
            for item in self.one_raw_product[i]:
                inner_list.append(item)  # 내부 리스트에 각 아이템 추가
            self.product_review_data.append(inner_list)  # 외부 리스트에 내부 리스트 추가

            
            
    def product_review(self):
        print(self.product_review_data[1])
        return self.product_review_data


if __name__ == '__main__':
    data = product()
    print(data)