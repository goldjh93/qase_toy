import re
from playwright.sync_api import  Playwright, sync_playwright, expect
from qase_integration import QaseClient

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://lawform.io/")
    
    # 예시 클릭 동작
    page.get_by_role("link", name="자동작성 자동작성 간단한 입력 및 선택만으로 법률문서를 쉽게 완성").click()

    # ---------------------
    context.close()
    browser.close()

# Qase 테스트 실행 함수
def run_test():
    qase_client = QaseClient(api_key='', project_code='CX')  # API 키 입력
    run_id = qase_client.create_run(title="Automated Test Run")  # 새로운 run 생성

    try:
        # Playwright 동작 실행
        with sync_playwright() as playwright:
            run(playwright)  # playwright 인자를 run 함수로 전달
        
        # 성공 시 Qase에 결과 전송
        qase_client.report_result(run_id=run_id, case_id=1, status="passed")
    except Exception as e:
        # 실패 시 Qase에 실패 결과 전송
        qase_client.report_result(run_id=run_id, case_id=1, status="failed")
        print(f"Test failed: {e}")

if __name__ == "__main__":
    run_test()

