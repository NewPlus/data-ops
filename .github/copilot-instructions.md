# GitHub Copilot 코딩 지침

## 프로젝트 개요

Python 기반 DataOps 프로젝트입니다. Apache Airflow를 사용하여 데이터 수집, LLM 기반 정제, 저장까지의 전체 파이프라인을 자동화합니다.

### 데이터 파이프라인 아키텍처

1. **수집 단계**: `src/collector/`의 데이터 소스별 수집 코드 실행 → DataFrame → Parquet 저장 (`data/raw/`)
2. **정제 단계**: Parquet 읽기 → LLM 정제 (`resources/` task 정의 기반) → Parquet 저장 (`data/processed/`)
3. **저장 단계**: Parquet 읽기 → CSV 변환 및 저장 (`data/output/`)
4. **오케스트레이션**: 전체 과정을 Airflow DAG로 관리

모든 코드는 확장 가능하고 유지보수 가능하며 테스트 가능해야 합니다.

## 코딩 표준

### Python 코드 작성 규칙
- PEP 8 스타일 가이드 엄격히 준수
- Black 포맷터 사용 (line length: 100)
- 타입 힌트를 모든 함수 시그니처에 포함
- Docstring은 Google 스타일로 작성
- 변수명은 명확하고 설명적으로 작성 (약어 최소화)

### 코드 구조
```python
# 좋은 예시
def process_customer_data(
    df: pd.DataFrame,
    start_date: datetime,
    end_date: datetime
) -> pd.DataFrame:
    """고객 데이터를 처리하고 필터링합니다.
    
    Args:
        df: 원본 고객 데이터프레임
        start_date: 시작 날짜
        end_date: 종료 날짜
    
    Returns:
        처리된 데이터프레임
    
    Raises:
        ValueError: 날짜 범위가 유효하지 않을 때
    """
    # 구현...
```

## 아키텍처 가이드라인

### 프로젝트 구조
```
data-ops/
├── dags/               # Airflow DAG 파일
│   ├── data_pipeline.py
│   └── data_quality_check.py
├── src/
│   ├── collector/      # 데이터 수집 (향후 구현)
│   │   ├── source1_collector.py
│   │   └── source2_collector.py
│   ├── cleaners/       # LLM 기반 데이터 정제
│   │   └── llm_cleaner.py
│   ├── loaders/        # CSV 저장
│   │   └── csv_loader.py
│   ├── validators/     # 데이터 검증
│   └── utils/          # 유틸리티 함수
│       ├── llm_client.py
│       └── parquet_utils.py
├── resources/          # LLM task 정의 파일
│   ├── cleaning_task_1.yaml
│   └── cleaning_task_2.json
├── data/               # 데이터 저장소
│   ├── raw/           # 수집된 원본 Parquet
│   ├── processed/     # LLM 정제된 Parquet
│   └── output/        # 최종 CSV 파일
├── tests/              # 테스트 코드
├── logs/               # Airflow 로그
├── plugins/            # Airflow 커스텀 플러그인
├── config/             # 설정 파일
│   ├── airflow.cfg
│   └── llm_config.yaml
├── docker/             # Docker 설정
│   └── docker-compose.yaml
└── docs/               # 문서
```

### 디자인 패턴
- **Factory Pattern**: 다양한 데이터 소스 커넥터 생성
- **Strategy Pattern**: 다양한 데이터 처리 전략
- **Pipeline Pattern**: ETL 프로세스 구성
- **Singleton Pattern**: 데이터베이스 연결 관리

## 모범 사례

### 데이터 수집 (`src/collector/`)
```python
import pandas as pd
from pathlib import Path
from datetime import datetime

def collect_data_source1() -> str:
    """데이터 소스1에서 데이터를 수집하고 Parquet으로 저장합니다.
    
    Returns:
        저장된 Parquet 파일 경로
    """
    # 데이터 수집 로직 (향후 구현)
    data = []  # 실제 수집 로직으로 대체
    
    df = pd.DataFrame(data)
    
    # Parquet 저장
    output_dir = Path("data/raw")
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = output_dir / f"source1_{timestamp}.parquet"
    
    df.to_parquet(filepath, compression='snappy', index=False)
    return str(filepath)
```

### LLM 기반 데이터 정제
```python
import pandas as pd
import json
from pathlib import Path
from typing import Dict, Any

def load_cleaning_task(task_file: str) -> Dict[str, Any]:
    """resources/ 폴더의 task 파일을 로드합니다."""
    task_path = Path("resources") / task_file
    with open(task_path, 'r', encoding='utf-8') as f:
        if task_file.endswith('.json'):
            return json.load(f)
        elif task_file.endswith('.yaml'):
            import yaml
            return yaml.safe_load(f)

def clean_data_with_llm(input_parquet: str, task_file: str) -> str:
    """LLM을 사용하여 데이터를 정제합니다.
    
    Args:
        input_parquet: 입력 Parquet 파일 경로
        task_file: LLM task 정의 파일명
    
    Returns:
        정제된 Parquet 파일 경로
    """
    # Parquet 읽기
    df = pd.read_parquet(input_parquet)
    
    # Task 로드
    task = load_cleaning_task(task_file)
    
    # LLM 정제 로직
    # TODO: LLM API 호출 및 데이터 정제
    cleaned_df = df.copy()  # 실제 정제 로직으로 대체
    
    # 정제된 데이터 저장
    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = output_dir / f"cleaned_{timestamp}.parquet"
    
    cleaned_df.to_parquet(output_path, compression='snappy', index=False)
    return str(output_path)
```

### Parquet에서 CSV로 변환
```python
def parquet_to_csv(input_parquet: str, output_name: str) -> str:
    """Parquet 파일을 CSV로 변환하여 저장합니다.
    
    Args:
        input_parquet: 입력 Parquet 파일 경로
        output_name: 출력 CSV 파일명 (확장자 제외)
    
    Returns:
        저장된 CSV 파일 경로
    """
    df = pd.read_parquet(input_parquet)
    
    output_dir = Path("data/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = output_dir / f"{output_name}_{timestamp}.csv"
    
    df.to_csv(filepath, index=False, encoding='utf-8-sig')
    return str(filepath)
```

### 데이터 처리
- 대용량 데이터는 청크(chunk) 단위로 처리
- Parquet 파일 읽기/쓰기 시 압축 옵션 사용 (`compression='snappy'`)
- 메모리 사용량 모니터링 및 최적화
- 데이터 파이프라인은 멱등성(idempotency) 보장

### 에러 핸들링
```python
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10)
)
def fetch_data_from_api(url: str) -> dict:
    """API에서 데이터를 가져오며, 실패 시 재시도합니다."""
    # 구현...
```

### 로깅
```python
import logging
import structlog

logger = structlog.get_logger(__name__)

def process_data(data_id: str) -> None:
    logger.info("데이터 처리 시작", data_id=data_id)
    try:
        # 처리 로직
        logger.info("데이터 처리 완료", data_id=data_id)
    except Exception as e:
        logger.error("데이터 처리 실패", data_id=data_id, error=str(e))
        raise
```

## 공통 패턴

### Airflow DAG 기본 구조
```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'data-team',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

def collect_data(**context):
    """데이터를 수집하고 Parquet으로 저장합니다."""
    from src.collector.source1_collector import collect_data_source1
    
    filepath = collect_data_source1()
    # XCom으로 다음 task에 파일 경로 전달
    context['ti'].xcom_push(key='raw_parquet_path', value=filepath)
    return filepath

def clean_data_with_llm(**context):
    """LLM을 사용하여 데이터를 정제합니다."""
    from src.cleaners.llm_cleaner import clean_data_with_llm
    
    # 이전 task에서 파일 경로 받기
    ti = context['ti']
    raw_parquet_path = ti.xcom_pull(key='raw_parquet_path', task_ids='collect_data')
    
    # LLM 정제
    cleaned_path = clean_data_with_llm(raw_parquet_path, 'cleaning_task_1.yaml')
    ti.xcom_push(key='cleaned_parquet_path', value=cleaned_path)
    return cleaned_path

def save_to_csv(**context):
    """Parquet를 CSV로 변환하여 저장합니다."""
    from src.loaders.csv_loader import parquet_to_csv
    
    ti = context['ti']
    cleaned_path = ti.xcom_pull(key='cleaned_parquet_path', task_ids='clean_data')
    
    csv_path = parquet_to_csv(cleaned_path, 'final_data')
    return csv_path

with DAG(
    'data_pipeline',
    default_args=default_args,
    description='데이터 수집 → LLM 정제 → CSV 저장 파이프라인',
    schedule_interval='@daily',
    catchup=False,
    tags=['etl', 'llm', 'csv'],
) as dag:
    
    collect_task = PythonOperator(
        task_id='collect_data',
        python_callable=collect_data,
    )
    
    clean_task = PythonOperator(
        task_id='clean_data',
        python_callable=clean_data_with_llm,
    )
    
    save_task = PythonOperator(
        task_id='save_to_csv',
        python_callable=save_to_csv,
    )
    
    # 파이프라인 플로우: 수집 → 정제 → 저장
    collect_task >> clean_task >> save_task
```

### Airflow 병렬 처리 패턴 (Dynamic Task Mapping)

**여러 데이터 소스를 동시에 처리하는 경우 권장 패턴:**

```python
from airflow.decorators import dag, task
from datetime import datetime
from typing import Dict, List

@dag(
    schedule_interval='@daily',
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=['parallel', 'etl', 'llm']
)
def parallel_data_pipeline():
    """여러 데이터 소스를 병렬로 처리하는 파이프라인"""
    
    @task
    def get_data_sources() -> List[Dict[str, str]]:
        """처리할 데이터 소스 리스트 반환
        
        Returns:
            데이터 소스 정보 리스트
        """
        return [
            {"name": "review", "task_file": "review_task.yaml"},
            {"name": "order", "task_file": "order_task.yaml"},
            {"name": "article", "task_file": "article_task.yaml"}
        ]
    
    @task(pool='collector_pool')  # 동시 실행 수 제한
    def collect(source: Dict[str, str]) -> str:
        """데이터 수집
        
        Args:
            source: 데이터 소스 정보
            
        Returns:
            저장된 Parquet 파일 경로
        """
        from src.collector import get_collector
        
        collector = get_collector(source['name'])
        parquet_path = collector.collect()
        
        return parquet_path
    
    @task(pool='llm_pool')  # LLM API 호출 제한
    def clean(source: Dict[str, str], raw_path: str) -> str:
        """LLM 기반 데이터 정제
        
        Args:
            source: 데이터 소스 정보
            raw_path: 원본 Parquet 파일 경로
            
        Returns:
            정제된 Parquet 파일 경로
        """
        from src.cleaners.llm_cleaner import clean_data_with_llm
        
        cleaned_path = clean_data_with_llm(raw_path, source['task_file'])
        return cleaned_path
    
    @task
    def save(source: Dict[str, str], cleaned_path: str) -> str:
        """CSV 저장
        
        Args:
            source: 데이터 소스 정보
            cleaned_path: 정제된 Parquet 파일 경로
            
        Returns:
            저장된 CSV 파일 경로
        """
        from src.loaders.csv_loader import parquet_to_csv
        
        output_name = source['name']
        csv_path = parquet_to_csv(cleaned_path, output_name)
        
        return csv_path
    
    # 병렬 실행 플로우
    sources = get_data_sources()
    
    # expand()를 사용하여 각 데이터 소스마다 Task 생성
    raw_paths = collect.expand(source=sources)
    cleaned_paths = clean.expand(source=sources, raw_path=raw_paths)
    csv_paths = save.expand(source=sources, cleaned_path=cleaned_paths)
    
    # 의존성은 자동으로 설정됨
    # collect[각 소스] → clean[각 소스] → save[각 소스]

# DAG 인스턴스 생성
parallel_dag = parallel_data_pipeline()
```

**실행 흐름:**
```
get_data_sources() → 3개 소스 반환
    ↓
collect[review]  ━┓
collect[order]   ━╋━ 동시 실행 (병렬)
collect[article] ━┛
    ↓
clean[review]    ━┓
clean[order]     ━╋━ 동시 실행 (병렬)
clean[article]   ━┛
    ↓
save[review]     ━┓
save[order]      ━╋━ 동시 실행 (병렬)
save[article]    ━┛
    ↓
reviews.csv, orders.csv, articles.csv 생성
```

**Pool 설정 (리소스 제한):**
```bash
# Airflow CLI로 Pool 생성
airflow pools set collector_pool 3 "데이터 수집 동시 실행 제한"
airflow pools set llm_pool 5 "LLM API 호출 동시 실행 제한"
```

**에러 격리:**
- 각 데이터 소스는 독립적인 Task로 실행
- 하나의 소스 실패 시 다른 소스에 영향 없음
- 실패한 소스만 선택적으로 재실행 가능

```bash
# 특정 소스만 재실행
airflow tasks clear parallel_data_pipeline \
  --task-regex ".*\[order\].*" \
  --dag-run-id manual_20260128
```

### LLM API 클라이언트 예시
```python
import os
from openai import OpenAI
from typing import Dict, Any

class LLMClient:
    """LLM API 클라이언트"""
    
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key)
    
    def clean_text(self, text: str, task: Dict[str, Any]) -> str:
        """LLM을 사용하여 텍스트를 정제합니다.
        
        Args:
            text: 정제할 텍스트
            task: resources/의 task 정의
        
        Returns:
            정제된 텍스트
        """
        prompt = task.get('prompt', '')
        system_message = task.get('system_message', '데이터 정제 전문가')
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": f"{prompt}\n\n텍스트: {text}"}
            ],
            temperature=0.3,
        )
        
        return response.choices[0].message.content
```

### Resources Task 파일 예시 (YAML)
```yaml
# resources/cleaning_task_1.yaml
task_name: "고객_리뷰_정제"
description: "고객 리뷰 텍스트에서 욕설 제거 및 맞춤법 교정"
system_message: "당신은 고객 리뷰를 정제하는 전문가입니다."
prompt: |
  다음 고객 리뷰를 정제해주세요:
  1. 욕설 및 비속어 제거
  2. 맞춤법 교정
  3. 의미는 유지하면서 깔끔하게 정리
  
  정제된 텍스트만 반환하세요.
model: "gpt-4"
temperature: 0.3
max_tokens: 500
```

### CSV 저장 및 데이터 검증
```python
import pandas as pd
from pathlib import Path
from datetime import datetime

def save_to_csv(df: pd.DataFrame, filename: str, output_dir: str = "data/output") -> str:
    """데이터프레임을 CSV 파일로 저장합니다."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = f"{output_dir}/{filename}_{timestamp}.csv"
    df.to_csv(filepath, index=False, encoding='utf-8-sig')
    return filepath

def validate_data_quality(df: pd.DataFrame) -> bool:
    """데이터 품질을 검증합니다."""
    # 필수 컬럼 체크
    required_columns = ['id', 'name', 'date']
    if not all(col in df.columns for col in required_columns):
        return False
    
    # 결측치 체크
    if df[required_columns].isnull().any().any():
        return False
    
    # 중복 체크
    if df.duplicated(subset=['id']).any():
        return False
    
    return True
```

## 테스트 요구사항

### 테스트 커버리지
- 최소 80% 이상의 코드 커버리지 유지
- 모든 파이프라인 함수는 단위 테스트 필수
- 통합 테스트로 전체 워크플로우 검증

### 테스트 작성 규칙
```python
import pytest
from unittest.mock import Mock, patch

def test_process_data_success():
    """데이터 처리 성공 케이스를 테스트합니다."""
    # Given
    input_data = pd.DataFrame({"col1": [1, 2, 3]})
    
    # When
    result = process_data(input_data)
    
    # Then
    assert len(result) == 3
    assert "col1" in result.columns

def test_process_data_with_empty_dataframe():
    """빈 데이터프레임 처리를 테스트합니다."""
    # Given
    empty_df = pd.DataFrame()
    
    # When & Then
    with pytest.raises(ValueError):
        process_data(empty_df)
```

## 문서화 표준

### 함수 문서화
- 모든 public 함수는 상세한 docstring 필수
- 파라미터, 반환값, 예외사항 명시
- 사용 예시 포함

### README 작성
- 프로젝트 설명 및 목적
- 설치 방법 및 환경 설정
- 사용 예시 및 실행 방법
- 기여 가이드라인

## 보안 가이드라인

### 민감 정보 관리
- 절대 코드에 비밀번호, API 키 하드코딩 금지
- `.env` 파일 사용 및 `.gitignore`에 추가
- AWS Secrets Manager, HashiCorp Vault 사용 권장

### 데이터 보안
```python
import os
from dotenv import load_dotenv

load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")
API_KEY = os.getenv("API_KEY")
```

## 성능 고려사항

### 최적화 전략
- 벡터화 연산 사용 (루프 최소화)
- 불필요한 데이터 복사 방지
- 인덱싱 및 쿼리 최적화
- 병렬 처리 활용 (multiprocessing, dask)
- 캐싱 전략 적용

### 모니터링
```python
import time
from functools import wraps

def measure_time(func):
    """함수 실행 시간을 측정합니다."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.info(f"{func.__name__} 실행 시간: {end - start:.2f}초")
        return result
    return wrapper
```

## 응답 언어

모든 코드 주석, 문서, 그리고 생성되는 텍스트는 **한국어**로 작성해주세요.

