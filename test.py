# from playwright.sync_api import sync_playwright
# import QaseClient

# # Qase 클라이언트 설정
# qase_client = QaseClient(api_key='f9e57705b80194db2428136bcaede8aa0a11454d04360afea75b702551a96bc0', project_code='CX')

# def test_login_page():
#     with sync_playwright() as p:
#         browser = p.chromium.launch()
#         page = browser.new_page()
#         page.goto('https://lawform.io/')
#         assert page.title() == "Login"
#         browser.close()

# def test_login_with_qase():
#     try:
#         test_login_page()
#         qase_client.report_result(case_id=1, status="passed")
#     except Exception as e:
#         qase_client.report_result(case_id=1, status="failed")
#         print(f"Test failed: {e}")
from playwright.sync_api import sync_playwright
from qaseio.api_client import ApiClient
from qaseio import ResultsApi
from qaseio.models import ResultCreate
from qaseio.configuration import Configuration

# QaseClient 클래스 정의
class QaseClient:
    def __init__(self, api_key, project_code):
        config = Configuration()
        config.api_key['TokenAuth'] = api_key
        self.api_client = ApiClient(config)
        self.results_api = ResultsApi(self.api_client)
        self.project_code = project_code

    def report_result(self, case_id, status):
        result_data = ResultCreate(
            case_id=case_id,
            status=status
        )
        self.results_api.create_result(self.project_code, result_data)

# Qase 클라이언트 설정
qase_client = QaseClient(api_key='', project_code='CX')

def test_login_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://lawform.io/')
        assert page.title() == "Login"
        browser.close()

def test_login_with_qase():
    try:
        test_login_page()
        qase_client.report_result(case_id=1, status="passed")
    except Exception as e:
        qase_client.report_result(case_id=1, status="failed")
        print(f"Test failed: {e}")
