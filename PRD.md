# 제품 요구사항 문서 (PRD)

## 1. 개요 (Executive Summary)

### 프로젝트 명

**범용 LLM 기반 DataOps 파이프라인 템플릿**

### 제품 비전

어떤 형태의 데이터든 LLM을 활용하여 자동으로 정제하고 구조화된 테이블 형태로 변환하는 **재사용 가능한 DataOps 템플릿 플랫폼** 구축. 
조직이나 프로젝트에서 새로운 데이터 소스가 추가되더라도 최소한의 설정만으로 즉시 사용 가능한 파이프라인 제공.

### 핵심 컨셉

**"Write Once, Use Everywhere"**

이 프로젝트는 **데이터 형태에 관계없이 재사용 가능한 범용 파이프라인 템플릿**을 제공합니다:

1. **입력**: 어떤 형태의 데이터든 수집 가능
   - 비정형 텍스트 (고객 리뷰, 이메일, 문서)
   - 반정형 데이터 (JSON, XML, 로그)
   - 웹 데이터 (HTML, 크롤링 결과)
   - 파일 데이터 (Excel, PDF, CSV)

2. **처리**: LLM이 자동으로 테이블 구조 생성
   - YAML 파일에 원하는 컬럼만 정의
   - LLM이 데이터를 분석하여 자동 추출
   - 비정형 → 정형(테이블) 변환 자동화

3. **출력**: 항상 동일한 형태의 테이블(CSV)
   - 모든 데이터 소스의 결과물이 표준화된 형식
   - 일관된 메타 컬럼 + 사용자 정의 컬럼
   - 즉시 분석 가능한 구조화된 데이터

**핵심 차별점**: 기존 ETL 도구와 달리, 데이터 형태마다 별도의 파싱 로직을 작성할 필요가 없습니다. LLM이 자동으로 데이터를 이해하고 테이블로 변환합니다.

### 주요 목표

1. **범용 데이터 처리 템플릿**: 텍스트, JSON, HTML 등 모든 비정형/반정형 데이터를 테이블 형태로 자동 변환
2. **LLM 기반 지능형 정제**: 데이터 형태에 관계없이 LLM이 자동으로 구조를 파악하고 정제
3. **즉시 사용 가능한 파이프라인**: 수집 코드와 정제 Task만 정의하면 자동으로 전체 파이프라인 구성
4. **확장 가능한 템플릿 구조**: 새로운 데이터 소스 추가 시 기존 템플릿 재사용
5. **설정 기반 커스터마이징**: 코드 수정 없이 YAML 파일로 정제 규칙 정의

### 예상 효과

- 파이프라인 재사용률 **90% 이상** (템플릿 기반)
- 신규 데이터 소스 추가 시간 **80% 단축** (8시간 이내)
- LLM 기반 자동 구조화로 수작업 **100% 제거**
- 다양한 데이터 형태(텍스트/JSON/HTML) **통합 처리** 가능
- 프로젝트 간 파이프라인 공유로 개발 비용 **80% 절감**


## 2. 문제 정의 (Problem Statement)

### 현재 상황

- 조직마다 다양한 형태의 비정형/반정형 데이터를 수집하지만 일관된 처리 방법이 없음
- 새로운 데이터 소스가 추가될 때마다 개별 파이프라인을 처음부터 구축해야 함
- 데이터 형태(텍스트, JSON, HTML 등)마다 다른 파싱 로직과 정제 로직이 필요
- 비정형 데이터를 구조화된 테이블로 변환하는 작업이 수작업으로 진행
- 데이터 정제 기준이 프로젝트마다 다르고 재사용이 어려움

### 주요 문제점

1. **재사용성 부족**: 프로젝트/팀마다 유사한 파이프라인을 반복 개발
2. **비정형 데이터 처리의 어려움**: 데이터 형태가 다양하여 통일된 처리 방법이 없음
3. **수동 구조화 작업**: 비정형 데이터를 테이블 형태로 변환하는 작업이 수작업
4. **긴 초기 구축 시간**: 새로운 데이터 소스 추가 시 파이프라인 전체를 새로 구축
5. **유지보수 비용 증가**: 데이터 소스마다 독립적인 코드베이스로 관리 부담 가중

### 해결해야 할 과제

- **템플릿 기반 파이프라인**: 모든 데이터 소스에 재사용 가능한 범용 파이프라인 구축
- **LLM 기반 자동 구조화**: 비정형 데이터를 LLM이 자동으로 분석하여 테이블로 변환
- **플러그 앤 플레이 구조**: 수집 코드와 설정 파일만 추가하면 즉시 작동하는 구조
- **설정 기반 커스터마이징**: 코드 수정 없이 YAML 파일로 정제 규칙 정의
- **표준화된 데이터 출력**: 모든 데이터 소스의 결과물을 통일된 테이블 형태로 제공


## 3. 목표 및 목적 (Goals and Objectives)

### 비즈니스 목표

1. **파이프라인 재사용률 극대화**: 새로운 데이터 소스 추가 시 기존 템플릿 90% 이상 재사용
2. **초기 구축 시간 단축**: 신규 데이터 소스 추가 시 1일 이내 파이프라인 가동
3. **운영 비용 절감**: 유사한 파이프라인 반복 개발 비용 80% 절감
4. **범용성 확보**: 텍스트, JSON, HTML 등 모든 형태의 데이터 처리 지원

### 기술적 목표

1. **템플릿화된 아키텍처**: 코어 파이프라인은 수정 없이 설정만으로 동작
2. **LLM 기반 자동 구조화**: 어떤 데이터든 자동으로 테이블 형태로 변환
3. **플러그인 시스템**: `src/collector/`에 수집 코드만 추가하면 자동 통합
4. **설정 주도 개발**: YAML 파일로 정제 규칙, 스키마, 검증 로직 정의
5. **표준화된 출력**: 모든 데이터 소스의 결과물을 동일한 테이블 스키마로 제공

### 성공 기준

- ✅ 새로운 데이터 소스 추가 시 템플릿 재사용률 90% 이상
- ✅ LLM 기반 테이블 구조화 성공률 95% 이상
- ✅ 신규 데이터 소스 파이프라인 구축 시간 8시간 이내
- ✅ 최소 5개 이상의 서로 다른 데이터 형태(텍스트, JSON, HTML 등) 처리 검증
- ✅ 모든 출력 데이터가 동일한 테이블 형식(CSV)으로 제공
- ✅ 코드 수정 없이 설정 파일(YAML)만으로 80% 이상 커스터마이징 가능
- ✅ 3개 이상의 데이터 소스를 병렬 처리하여 전체 파이프라인 실행 시간 50% 단축
- ✅ 병렬 처리 시 하나의 데이터 소스 실패가 다른 소스에 영향을 주지 않음 (에러 격리 100%)


## 4. 사용자 스토리 (User Stories)

### 데이터 엔지니어

- **US-001**: 데이터 엔지니어로서 새로운 데이터 소스를 추가할 때 기존 템플릿을 그대로 활용할 수 있어야 한다.
  - `src/collector/`에 수집 코드만 작성하면 자동으로 파이프라인에 통합
  - 코어 파이프라인 코드는 수정하지 않음
  
- **US-002**: 데이터 엔지니어로서 비정형 데이터를 테이블로 변환하는 작업을 LLM에게 위임할 수 있어야 한다.
  - 텍스트, JSON, HTML 등 어떤 형태든 자동으로 테이블 구조 생성
  - `resources/` YAML 파일에 원하는 테이블 스키마만 정의

- **US-003**: 데이터 엔지니어로서 다른 팀의 데이터 파이프라인을 내 프로젝트에 쉽게 복사하여 사용할 수 있어야 한다.
  - 템플릿 구조로 인해 높은 재사용성 확보
  - 수집 모듈과 설정 파일만 복사하면 즉시 작동

### 데이터 분석가

- **US-004**: 데이터 분석가로서 어떤 데이터 소스든 항상 동일한 형태의 테이블(CSV)로 받을 수 있어야 한다.
  - 모든 데이터 소스의 결과물이 표준화된 CSV 형식으로 제공
  - `data/output/` 폴더에서 일관된 구조의 파일 확인

- **US-005**: 데이터 분석가로서 원하는 컬럼 구조를 자연어로 정의할 수 있어야 한다.
  - YAML 파일에 "고객명, 연락처, 주소를 추출해주세요"와 같이 작성
  - LLM이 자동으로 해당 컬럼을 추출하여 테이블 생성

### 데이터 과학자

- **US-006**: 데이터 과학자로서 LLM이 비정형 데이터를 어떻게 구조화하는지 실험할 수 있어야 한다.
  - 다양한 프롬프트 전략으로 테이블 구조화 성능 비교
  - Few-shot 예시를 추가하여 정확도 향상 테스트

- **US-007**: 데이터 과학자로서 동일한 원본 데이터에 대해 여러 정제 Task를 실험할 수 있어야 한다.
  - `resources/` 폴더에 여러 YAML 파일 생성
  - 각 Task별 정제 결과를 비교하여 최적의 방법 선택

### 시스템 관리자

- **US-008**: 시스템 관리자로서 Docker Compose를 통해 전체 시스템을 손쉽게 배포할 수 있어야 한다.
  - `docker-compose up -d` 명령어 한 번으로 전체 환경 구성

- **US-009**: 시스템 관리자로서 파이프라인 실행 스케줄을 유연하게 관리할 수 있어야 한다.
  - Airflow DAG의 `schedule_interval` 설정으로 실행 주기 조정


## 4.1 실제 사용 사례 (Use Cases)

이 템플릿 플랫폼이 어떻게 다양한 데이터 형태를 처리하는지 보여주는 실제 예시입니다.

### Use Case 1: 고객 리뷰 텍스트 → 테이블 변환

**입력 데이터 (비정형 텍스트)**
```
김철수: 이 제품 정말 좋아요! 배송도 빠르고 품질도 훌륭합니다. ★★★★★
박영희: 가격 대비 별로였어요. 2점 드립니다.
익명: 그냥 그래요 보통입니다
```

**Task 파일 (resources/review_extraction.yaml)**
```yaml
output_schema:
  - column_name: "customer_name"
    extraction_rule: "고객 이름 추출, 없으면 '익명'"
  - column_name: "rating"
    extraction_rule: "별점을 1-5 정수로 변환"
  - column_name: "review_text"
    extraction_rule: "리뷰 내용을 정제"
  - column_name: "sentiment"
    extraction_rule: "긍정/부정/중립 분류"
```

**출력 결과 (CSV 테이블)**
| customer_name | rating | review_text | sentiment | source | created_at | processed_at |
|---------------|--------|-------------|-----------|--------|------------|--------------|
| 김철수 | 5 | 제품 정말 좋아요! 배송도 빠르고 품질도 훌륭합니다. | 긍정 | reviews | 2026-01-28 | 2026-01-28 |
| 박영희 | 2 | 가격 대비 별로였어요. | 부정 | reviews | 2026-01-28 | 2026-01-28 |
| 익명 | 3 | 그냥 그래요 보통입니다 | 중립 | reviews | 2026-01-28 | 2026-01-28 |

---

### Use Case 2: JSON API 응답 → 테이블 변환

**입력 데이터 (JSON)**
```json
{
  "user": {"name": "John Doe", "contact": {"email": "john@example.com", "phone": "+1-555-1234"}},
  "order": {"id": "ORD-123", "items": [{"product": "Laptop", "price": 1200}], "total": 1200},
  "timestamp": "2026-01-28T10:30:00Z"
}
```

**Task 파일 (resources/order_extraction.yaml)**
```yaml
output_schema:
  - column_name: "customer_name"
    extraction_rule: "user.name 추출"
  - column_name: "email"
    extraction_rule: "user.contact.email 추출"
  - column_name: "order_id"
    extraction_rule: "order.id 추출"
  - column_name: "product_list"
    extraction_rule: "order.items의 모든 제품명을 쉼표로 연결"
  - column_name: "total_amount"
    extraction_rule: "order.total 추출"
```

**출력 결과 (CSV 테이블)**
| customer_name | email | order_id | product_list | total_amount | source | created_at |
|---------------|-------|----------|--------------|--------------|--------|------------|
| John Doe | john@example.com | ORD-123 | Laptop | 1200 | api_orders | 2026-01-28 |

---

### Use Case 3: HTML 웹페이지 → 테이블 변환

**입력 데이터 (HTML)**
```html
<div class="article">
  <h1>AI 기술의 미래</h1>
  <span class="author">작성자: 홍길동</span>
  <span class="date">2026-01-28</span>
  <p class="content">인공지능 기술이 빠르게 발전하고 있습니다...</p>
  <div class="tags">AI, 기술, 미래</div>
</div>
```

**Task 파일 (resources/article_extraction.yaml)**
```yaml
output_schema:
  - column_name: "title"
    extraction_rule: "h1 태그의 제목 추출"
  - column_name: "author"
    extraction_rule: "작성자 이름 추출"
  - column_name: "published_date"
    extraction_rule: "날짜를 YYYY-MM-DD 형식으로 변환"
  - column_name: "content_summary"
    extraction_rule: "본문을 100자 이내로 요약"
  - column_name: "tags"
    extraction_rule: "태그들을 리스트로 추출"
```

**출력 결과 (CSV 테이블)**
| title | author | published_date | content_summary | tags | source | created_at |
|-------|--------|----------------|-----------------|------|--------|------------|
| AI 기술의 미래 | 홍길동 | 2026-01-28 | 인공지능 기술이 빠르게 발전하고 있습니다... | AI, 기술, 미래 | web_articles | 2026-01-28 |

---

### 템플릿 재사용성 증명

위 세 가지 완전히 다른 데이터 형태(텍스트, JSON, HTML)를 처리했지만:

✅ **동일한 파이프라인 코드** 사용
✅ **동일한 Airflow DAG** 사용
✅ **설정 파일(YAML)만 변경**하여 처리
✅ **모든 출력이 동일한 CSV 테이블** 형식

이것이 바로 **재사용 가능한 템플릿 플랫폼**의 핵심입니다!


## 5. 기능 요구사항 (Functional Requirements)

### 5.1 코어 기능

#### FR-001: 템플릿 기반 데이터 수집
- **설명**: BaseCollector 인터페이스를 상속한 수집 모듈을 자동으로 인식하고 파이프라인에 통합
- **우선순위**: 필수
- **세부사항**:
  - `src/collector/` 폴더에 새로운 Collector 클래스 추가
  - BaseCollector 인터페이스 구현 (collect 메서드 필수)
  - JSON 직렬화 가능한 레코드 목록 반환
  - 수집 결과는 다음 Task로 JSON 형태로 전달

#### FR-002: LLM 기반 자동 테이블 구조화
- **설명**: 비정형 데이터(텍스트, JSON, HTML 등)를 LLM을 활용하여 자동으로 테이블 형태로 변환
- **우선순위**: 필수
- **세부사항**:
  - `resources/` 폴더의 Task 파일(YAML)에 출력 스키마 정의
  - LLM이 자동으로 데이터 파싱 및 필드 추출
  - 정제된 데이터를 `data/processed/` 폴더에 Parquet 형식으로 저장
  - 동적 스키마 지원 (Task 파일에서 자유롭게 컬럼 정의)

#### FR-003: 표준화된 CSV 출력
- **설명**: 모든 데이터 소스의 결과물을 동일한 테이블 형식(CSV)으로 제공
- **우선순위**: 필수
- **세부사항**:
  - Parquet → CSV 자동 변환
  - 메타 컬럼 자동 추가 (source, created_at, updated_at 등)
  - UTF-8 with BOM 인코딩으로 Excel 호환성 확보
  - `data/output/` 폴더에 타임스탬프 포함 파일명으로 저장

#### FR-004: 데이터별 병렬 처리
- **설명**: 여러 데이터 소스를 동시에 수집하고 각각 독립적으로 정제 및 저장 처리
- **우선순위**: 필수
- **세부사항**:
  - Airflow의 Dynamic Task Mapping 또는 TaskGroup 활용
  - 각 데이터 소스별로 독립적인 파이프라인 실행
  - 수집 → 정제 → 저장 과정이 데이터별로 병렬 수행
  - 하나의 데이터 소스 실패 시 다른 데이터 소스에 영향 없음
  - 리소스 제약 조건 설정 가능 (동시 실행 수 제한)

#### FR-005: 플러그인 시스템
- **설명**: 새로운 Collector나 Cleaner를 코드 수정 없이 추가 가능한 구조
- **우선순위**: 중요
- **세부사항**:
  - 파이썬 데코레이터 또는 메타클래스 기반 자동 등록
  - Airflow DAG가 자동으로 새로운 모듈 감지
  - 테스트 전용 DAG 자동 생성

#### FR-006: 설정 기반 커스터마이징
- **설명**: 코드 수정 없이 YAML 파일로 데이터 정제 규칙, 스키마, 검증 로직 정의
- **우선순위**: 필수
- **세부사항**:
  - Task 파일에서 출력 스키마, LLM 프롬프트, 검증 규칙 정의
  - JSON 또는 YAML 형식 지원
  - 버전 관리 및 히스토리 추적

#### FR-007: 데이터 품질 검증
- **설명**: 정제된 데이터의 품질을 자동으로 검증
- **우선순위**: 중요
- **세부사항**:
  - 필수 컬럼 존재 여부 확인
  - 데이터 타입 검증
  - 결측치 비율 체크
  - 중복 데이터 감지
  - Task 파일에 검증 규칙 정의 가능

### 5.2 부가 기능

#### FR-008: 재시도 및 에러 핸들링
- 자동 재시도 로직 (exponential backoff)
- 실패한 데이터 로그 저장
- 알림 시스템 (이메일, Slack 등)

#### FR-009: 모니터링 및 로깅
- 파이프라인 실행 상태 추적
- 데이터 처리 통계 (처리 시간, 성공률 등)
- 구조화된 로깅 (structlog)

#### FR-010: 스케줄링
- Airflow를 통한 주기적 실행 (cron 표현식)
- 백필(backfill) 지원
- 의존성 관리

### 5.3 병렬 처리 상세 설계

#### 데이터별 독립 파이프라인
각 데이터 소스는 다음과 같이 독립적으로 실행됩니다:

```
데이터 소스 A: 수집 → 정제 → 저장
데이터 소스 B: 수집 → 정제 → 저장  (동시 실행)
데이터 소스 C: 수집 → 정제 → 저장
```

#### Airflow 병렬 처리 구현 방식

**방법 1: Dynamic Task Mapping (권장)**
```python
from airflow.decorators import task

@task
def collect_data(source_name: str) -> str:
    """데이터 수집"""
    return f"data/raw/{source_name}.parquet"

@task
def clean_data(parquet_path: str) -> str:
    """데이터 정제"""
    return f"data/processed/{parquet_path}"

@task
def save_to_csv(parquet_path: str) -> str:
    """CSV 저장"""
    return f"data/output/{parquet_path}.csv"

# 동적으로 데이터 소스 리스트 생성
data_sources = ["source_a", "source_b", "source_c"]

# 병렬 실행
raw_files = collect_data.expand(source_name=data_sources)
processed_files = clean_data.expand(parquet_path=raw_files)
csv_files = save_to_csv.expand(parquet_path=processed_files)
```

**방법 2: TaskGroup (대안)**
```python
from airflow.utils.task_group import TaskGroup

for source in data_sources:
    with TaskGroup(group_id=f"pipeline_{source}") as tg:
        collect = PythonOperator(task_id=f"collect_{source}", ...)
        clean = PythonOperator(task_id=f"clean_{source}", ...)
        save = PythonOperator(task_id=f"save_{source}", ...)
        
        collect >> clean >> save
```

#### 리소스 관리

**Pool 설정으로 동시 실행 수 제한:**
```python
# Airflow Pool 생성
# airflow pools set parallel_pool 5 "병렬 처리 Pool"

collect_task = PythonOperator(
    task_id='collect_data',
    pool='parallel_pool',  # 최대 5개까지 동시 실행
    priority_weight=10,     # 우선순위 설정
)
```

#### 에러 격리
- 하나의 데이터 소스 실패가 다른 데이터 소스에 영향을 주지 않도록 격리
- 각 파이프라인은 독립적인 트랜잭션으로 처리
- 실패한 데이터 소스만 선택적으로 재실행 가능

#### 성능 최적화
- 데이터 크기에 따라 병렬 처리 수 동적 조정
- LLM API 호출 속도 제한(rate limiting) 고려
- 대용량 데이터는 청크 단위로 분할 처리


## 7. 기술 아키텍처 (Technical Architecture)

### 7.2 데이터 플로우

#### 기본 파이프라인 구조

1. **수집 단계 (Collection)**
  - `src/collector/` 모듈이 외부 데이터 소스에서 데이터 수집
  - JSON 직렬화 가능한 레코드 목록으로 반환
  - 다음 단계로 JSON 형태 전달

2. **정제 단계 (Cleaning)**
  - 수집 단계 JSON 레코드를 입력으로 사용
  - `resources/` task 파일 기반으로 LLM API 호출
  - 정제 결과를 JSON 레코드 또는 표준 테이블 구조로 변환

3. **저장 단계 (Loading)**
  - 정제 결과를 CSV로 변환하여 `data/output/` 폴더에 저장
  - 파일명 패턴: `{source_name}_{timestamp}.csv`

#### 병렬 처리 플로우

여러 데이터 소스가 있을 경우, 각각 독립적으로 파이프라인이 실행됩니다:

```
시간축 →

┌─────────────────────────────────────────────────────────────┐
│ 데이터 소스 A (고객 리뷰)                                     │
├─────────────────────────────────────────────────────────────┤
│  [수집] → [정제] → [저장] → ✅ reviews.csv                    │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 데이터 소스 B (주문 데이터)                                   │
├─────────────────────────────────────────────────────────────┤
│  [수집] → [정제] → [저장] → ✅ orders.csv                     │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 데이터 소스 C (웹페이지 기사)                                 │
├─────────────────────────────────────────────────────────────┤
│  [수집] → [정제] → [저장] → ✅ articles.csv                   │
└─────────────────────────────────────────────────────────────┘

👆 모든 파이프라인이 동시에 실행됨 (병렬 처리)
   하나가 실패해도 다른 파이프라인에 영향 없음
```

#### XCom을 통한 파일 경로 전달

각 Task는 Airflow XCom을 사용하여 다음 Task에 파일 경로를 전달합니다:

```python
# Task 1: 수집
def collect_data(**context):
  records = [{"ticker": "AAPL", "market_price": 100.0}]
  # 다음 Task에 JSON 레코드 전달
  context['ti'].xcom_push(key='raw_records', value=records)
  return records

# Task 2: 정제
def clean_data(**context):
  # 이전 Task에서 레코드 받기
  ti = context['ti']
  raw_records = ti.xcom_pull(key='raw_records', task_ids='collect_data')
    
  cleaned_records = raw_records  # 정제 로직 적용 후 결과
  ti.xcom_push(key='cleaned_records', value=cleaned_records)
  return cleaned_records

# Task 3: 저장
def save_to_csv(**context):
  ti = context['ti']
  cleaned_records = ti.xcom_pull(key='cleaned_records', task_ids='clean_data')
    
  csv_path = "data/output/source_a_20260128.csv"
  return csv_path
```

#### 병렬 처리 흐름 예시

**Airflow DAG 구조 (Dynamic Task Mapping 방식):**

```python
from airflow.decorators import dag, task
from datetime import datetime

@dag(
    schedule_interval='@daily',
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=['parallel', 'etl']
)
def parallel_data_pipeline():
    
    @task
    def get_data_sources():
        """처리할 데이터 소스 리스트 반환"""
        return [
            {"name": "review", "task_file": "review_task.yaml"},
            {"name": "order", "task_file": "order_task.yaml"},
            {"name": "article", "task_file": "article_task.yaml"}
        ]
    
    @task
    def collect(source: dict) -> list[dict]:
      """데이터 수집"""
      from src.collector import get_collector
      collector = get_collector(source['name'])
      return list(collector.collect())
    
    @task
    def clean(source: dict, raw_records: list[dict]) -> list[dict]:
      """LLM 정제"""
      from src.cleaners.llm_cleaner import clean_data_with_llm
      return clean_data_with_llm(raw_records, source['task_file'])
    
    @task
    def save(cleaned_records: list[dict]) -> str:
      """CSV 저장"""
      from src.loaders.csv_loader import records_to_csv
      return records_to_csv(cleaned_records)
    
    # 병렬 실행 플로우
    sources = get_data_sources()
    raw_records = collect.expand(source=sources)
    cleaned_records = clean.expand(source=sources, raw_records=raw_records)
    csv_paths = save.expand(cleaned_records=cleaned_records)

parallel_data_pipeline()
```

**실행 결과:**
```
DAG Run 시작
  ├─ get_data_sources (완료) → 3개 소스 반환
  │
  ├─ collect[review]  ━┓
  ├─ collect[order]   ━╋━ 동시 실행 (병렬)
  ├─ collect[article] ━┛
  │
  ├─ clean[review]    ━┓
  ├─ clean[order]     ━╋━ 동시 실행 (병렬)
  ├─ clean[article]   ━┛
  │
  ├─ save[review]     ━┓
  ├─ save[order]      ━╋━ 동시 실행 (병렬)
  └─ save[article]    ━┛

결과: reviews.csv, orders.csv, articles.csv 생성
```

#### 리소스 제약 관리

**동시 실행 수 제한 (Pool 설정):**
```bash
# Airflow CLI로 Pool 생성
airflow pools set collector_pool 3 "데이터 수집 Pool"
airflow pools set llm_pool 5 "LLM 처리 Pool"
```

**DAG에서 Pool 사용:**
```python
@task(pool='collector_pool')
def collect(source: dict) -> str:
    """최대 3개까지만 동시 실행"""
    pass

@task(pool='llm_pool')
def clean(source: dict, raw_path: str) -> str:
    """최대 5개까지만 동시 실행"""
    pass
```

#### 에러 처리 및 격리

- 각 데이터 소스는 독립적인 Task로 실행
- 하나의 소스 실패 시 다른 소스에 영향 없음
- 실패한 소스만 선택적으로 재실행 가능

**실패 시나리오 예시:**
```
✅ collect[review]  → ✅ clean[review]  → ✅ save[review]  → reviews.csv
✅ collect[order]   → ❌ clean[order]   → (중단)          → (없음)
✅ collect[article] → ✅ clean[article] → ✅ save[article] → articles.csv

결과: order만 실패, 나머지는 정상 완료
```

**재실행 명령:**
```bash
# order 관련 Task만 선택적으로 재실행
airflow tasks clear parallel_data_pipeline \
  --task-regex ".*\[order\].*" \
  --dag-run-id manual_20260128
```

### 7.2.1 템플릿 동작 원리

**핵심: 코드는 그대로, 설정만 변경**

```
┌─────────────────────────────────────────────────────────────────┐
│                    재사용 가능한 코어 파이프라인                   │
│                        (수정 불필요)                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Step 1: 데이터 수집 (플러그인 방식)                     │   │
│  │                                                           │   │
│  │  src/collector/                                           │   │
│  │  ├── review_collector.py    ← 사용자가 추가              │   │
│  │  ├── api_collector.py       ← 사용자가 추가              │   │
│  │  └── web_collector.py       ← 사용자가 추가              │   │
│  │                                                           │   │
│  │  모두 BaseCollector 상속 → 자동으로 파이프라인에 통합     │   │
│  └─────────────────────────────────────────────────────────┘   │
│                          ↓                                       │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Step 2: LLM 기반 구조화 (설정 주도)                     │   │
│  │                                                           │   │
│  │  resources/                                               │   │
│  │  ├── review_task.yaml       ← 사용자가 스키마 정의       │   │
│  │  ├── order_task.yaml        ← 사용자가 스키마 정의       │   │
│  │  └── article_task.yaml      ← 사용자가 스키마 정의       │   │
│  │                                                           │   │
│  │  LLM이 자동으로 비정형 → 테이블 변환                      │   │
│  └─────────────────────────────────────────────────────────┘   │
│                          ↓                                       │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Step 3: 표준화된 CSV 출력 (자동)                        │   │
│  │                                                           │   │
│  │  모든 출력이 동일한 테이블 형식:                          │   │
│  │  [메타 컬럼] + [사용자 정의 컬럼]                         │   │
│  │                                                           │   │
│  │  data/output/                                             │   │
│  │  ├── reviews_20260128.csv                                │   │
│  │  ├── orders_20260128.csv                                 │   │
│  │  └── articles_20260128.csv                               │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘

📌 핵심 포인트:
   - 새로운 데이터 소스 추가 시 Collector 1개 + Task 파일 1개만 작성
   - 파이프라인 코어 코드는 절대 수정하지 않음
   - Airflow DAG는 자동으로 생성되거나 파라미터만 변경
```

### 7.3 기술 스택

### Phase 1: 기초 인프라 구축 (2주)

**목표**: 개발 환경 및 기본 아키텍처 구축

- Week 1
  - [x] 프로젝트 구조 설계
  - [x] GitHub 저장소 및 문서 구성
  - [ ] Docker Compose 환경 구축
  - [ ] Airflow 초기 설정
  - [ ] BaseCollector 인터페이스 설계

- Week 2
  - [ ] 데이터 폴더 구조 생성 (raw/processed/output)
  - [ ] 템플릿화된 파이프라인 코어 구현
  - [ ] Task 파일 파서 구현
  - [ ] 기본 유틸리티 함수 구현
  - [ ] pytest 테스트 환경 구축

### Phase 2: 핵심 기능 개발 (4주)

**목표**: 템플릿 기반 데이터 처리 기능 구현

- Week 3-4: 플러그인 시스템 및 샘플 Collector
  - [ ] BaseCollector 추상 클래스 구현
  - [ ] 샘플 Collector 3개 구현 (텍스트, JSON, HTML)
  - [ ] Collector 자동 발견 및 등록 메커니즘
  - [ ] DataFrame → Parquet 저장 로직 구현
  - [ ] 수집 모듈 단위 테스트

- Week 5-6: LLM 기반 구조화 엔진
  - [ ] `src/cleaners/` 템플릿 모듈 구현
  - [ ] LLM API 클라이언트 구현 (OpenAI, Anthropic)
  - [ ] Task 파일 YAML 파싱 로직
  - [ ] LLM 프롬프트 엔지니어링 (구조화 전용)
  - [ ] LLM 응답 → DataFrame 변환 로직
  - [ ] Few-shot 예시 처리
  - [ ] 에러 핸들링 및 재시도 로직
  - [ ] **3가지 다른 데이터 형태로 템플릿 검증**

- Week 7: 표준화된 CSV 저장
  - [ ] `src/loaders/` 모듈 구현
  - [ ] 동적 스키마 → CSV 변환 로직
  - [ ] 메타 컬럼 자동 추가
  - [ ] 파일명 타임스탬프 처리
  - [ ] 데이터 검증 로직
  - [ ] **출력 형식 표준화 검증**

### Phase 3: 오케스트레이션 및 통합 (3주)

**목표**: Airflow 템플릿 DAG 구성 및 전체 파이프라인 통합

