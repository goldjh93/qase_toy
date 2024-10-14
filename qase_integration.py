# qase_integration.py
from qaseio.api_client import ApiClient
from qaseio import ResultsApi
from qaseio.models import ResultCreate
from qaseio.configuration import Configuration


# qase_integration.py (Run 생성 추가)
from qaseio import RunsApi
from qaseio.models import RunCreate

class QaseClient:
    def __init__(self, api_key, project_code):
        config = Configuration()
        config.api_key['TokenAuth'] = api_key
        self.api_client = ApiClient(config)
        self.results_api = ResultsApi(self.api_client)
        self.runs_api = RunsApi(self.api_client)  # RunsApi 추가
        self.project_code = project_code

    def create_run(self, title="Automated Test Run"):
        # 새로운 실행(run)을 생성
        run_data = RunCreate(title=title)
        created_run = self.runs_api.create_run(self.project_code, run_data)
        return created_run.result.id  # 생성된 run_id 반환

    def report_result(self, run_id, case_id, status):
        # 기존 코드와 동일
        result_data = ResultCreate(
            case_id=case_id,
            status=status
        )
        self.results_api.create_result(self.project_code, run_id, result_data)


