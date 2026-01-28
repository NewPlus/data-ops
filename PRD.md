# 제품 요구사항 문서 (PRD)

## 1. 개요 (Executive Summary)

### 프로젝트 명

**DataOps 자동화 파이프라인 시스템**

### 제품 비전

AI 기반 데이터 정제 기술과 Apache Airflow를 활용하여 데이터 수집부터 최종 저장까지의 전체 파이프라인을 자동화하는 확장 가능한 DataOps 플랫폼 구축

### 주요 목표

1. **자동화된 데이터 파이프라인**: 수집 → LLM 정제 → 저장의 end-to-end 자동화
2. **LLM 기반 데이터 품질 향상**: 대규모 언어 모델을 활용한 지능형 데이터 정제
3. **효율적인 워크플로우 관리**: Apache Airflow 기반의 안정적인 오케스트레이션
4. **확장 가능한 아키텍처**: 다양한 데이터 소스 및 정제 작업 추가 지원

### 예상 효과

- 데이터 정제 시간 **70% 단축**
- 데이터 품질 **40% 향상**
- 수작업 대비 운영 비용 **60% 절감**
- 새로운 데이터 소스 추가 시간 **80% 단축**


## 2. 문제 정의 (Problem Statement)

### 현재 상황

- 데이터 수집, 정제, 저장 과정이 수작업으로 진행되어 많은 시간과 인력 소요
- 데이터 품질 관리가 일관되지 않아 신뢰도 저하
- 다양한 데이터 소스에서 수집되는 데이터의 형식과 품질이 제각각
- 데이터 파이프라인의 장애 및 오류 추적이 어려움

### 주요 문제점

1. **낮은 자동화 수준**: 대부분의 데이터 처리 작업이 수동으로 진행
2. **일관성 없는 데이터 품질**: 데이터 정제 기준이 명확하지 않고 작업자마다 다름
3. **긴 처리 시간**: 수작업으로 인한 병목 현상 발생
4. **확장성 부족**: 새로운 데이터 소스 추가 시 많은 개발 비용 발생
5. **모니터링 한계**: 파이프라인 실행 상태 및 오류 파악이 어려움

### 해결해야 할 과제

- 전체 데이터 파이프라인의 자동화 및 오케스트레이션
- LLM을 활용한 지능형 데이터 정제 시스템 구축
- 확장 가능한 모듈형 아키텍처 설계
- 실시간 모니터링 및 알림 체계 구축
- 데이터 품질 검증 자동화


## 3. 목표 및 목적 (Goals and Objectives)

### 비즈니스 목표

1. 데이터 처리 시간을 현재 대비 70% 단축
2. 데이터 품질 향상을 통한 의사결정 신뢰도 증대
3. 운영 비용 60% 절감 (인력 및 시간 절약)
4. 신규 데이터 소스 추가 시 개발 기간 80% 단축

### 기술적 목표

1. **완전 자동화**: 데이터 수집부터 저장까지 무인 자동 처리
2. **고성능 처리**: 대용량 데이터 처리 시 메모리 효율성 최적화
3. **안정성**: 99.5% 이상의 파이프라인 성공률 달성
4. **확장성**: 플러그인 방식의 데이터 소스 추가 지원
5. **추적성**: 모든 데이터 처리 과정의 로그 및 메타데이터 관리

### 성공 기준

- ✅ 일일 데이터 처리 파이프라인 자동 실행률 95% 이상
- ✅ LLM 기반 데이터 정제 정확도 90% 이상
- ✅ 파이프라인 평균 실행 시간 2시간 이내
- ✅ 시스템 가동률 99.5% 이상
- ✅ 코드 테스트 커버리지 80% 이상


## 4. 사용자 스토리 (User Stories)

### 데이터 엔지니어

- **US-001**: 데이터 엔지니어로서 새로운 데이터 소스를 빠르게 추가할 수 있어야 한다.
  - `src/collector/`에 수집 코드만 작성하면 자동으로 파이프라인에 통합
  
- **US-002**: 데이터 엔지니어로서 파이프라인 실행 상태를 실시간으로 모니터링할 수 있어야 한다.
  - Airflow UI를 통해 DAG 실행 상태, 로그, 성공/실패 여부 확인

- **US-003**: 데이터 엔지니어로서 파이프라인 오류 발생 시 빠르게 원인을 파악할 수 있어야 한다.
  - 상세한 에러 로그 및 스택 트레이스 제공

### 데이터 분석가

- **US-004**: 데이터 분석가로서 정제된 고품질 데이터를 CSV 형식으로 받을 수 있어야 한다.
  - `data/output/` 폴더에서 타임스탬프가 포함된 최신 CSV 파일 확인

- **US-005**: 데이터 분석가로서 데이터 정제 기준을 손쉽게 수정할 수 있어야 한다.
  - `resources/` 폴더의 YAML 파일 수정만으로 정제 규칙 변경

### 데이터 과학자

- **US-006**: 데이터 과학자로서 다양한 LLM 모델을 활용한 데이터 정제를 실험할 수 있어야 한다.
  - Task 파일에서 모델 종류, 프롬프트, 파라미터 변경 가능

- **US-007**: 데이터 과학자로서 중간 처리 결과(Parquet)를 확인할 수 있어야 한다.
  - `data/raw/`, `data/processed/` 폴더에서 각 단계별 데이터 조회

### 시스템 관리자

- **US-008**: 시스템 관리자로서 Docker Compose를 통해 전체 시스템을 손쉽게 배포할 수 있어야 한다.
  - `docker-compose up -d` 명령어 한 번으로 전체 환경 구성

- **US-009**: 시스템 관리자로서 파이프라인 실행 스케줄을 유연하게 관리할 수 있어야 한다.
  - Airflow DAG의 `schedule_interval` 설정으로 실행 주기 조정


## 5. 기능 요구사항 (Functional Requirements)

### 5.1 데이터 수집 (Data Ingestion)

- **FR-001**: `src/collector/` 폴더에 데이터 소스별 수집 모듈 구현
- **FR-002**: 수집된 데이터는 pandas DataFrame으로 변환
- **FR-003**: DataFrame을 Parquet 형식으로 `data/raw/` 폴더에 저장
- **FR-004**: Parquet 파일명에 데이터 소스명과 타임스탬프 포함
- **FR-005**: Parquet 저장 시 snappy 압축 적용
- **FR-006**: 데이터 수집 실패 시 자동 재시도 (최대 3회)

### 5.2 데이터 변환 (Data Transformation)

- **FR-007**: `resources/` 폴더의 task 파일(YAML/JSON)로 LLM 정제 작업 정의
- **FR-008**: Parquet 파일에서 데이터 읽기
- **FR-009**: LLM API를 호출하여 데이터 정제 수행
- **FR-010**: 정제된 데이터를 Parquet 형식으로 `data/processed/` 폴더에 저장
- **FR-011**: 청크 단위 처리를 통한 대용량 데이터 지원
- **FR-012**: LLM API rate limit 대응 (exponential backoff)

### 5.3 데이터 적재 (Data Loading)

- **FR-013**: 정제된 Parquet 파일을 CSV로 변환
- **FR-014**: CSV 파일을 `data/output/` 폴더에 저장
- **FR-015**: CSV 파일명에 타임스탬프 포함 (YYYYMMDD_HHMMSS 형식)
- **FR-016**: UTF-8 BOM 인코딩 적용 (Excel 호환성)
- **FR-017**: 인덱스 제외하고 저장

### 5.4 데이터 품질 관리 (Data Quality)

- **FR-018**: 필수 컬럼 존재 여부 검증
- **FR-019**: 결측치 비율 확인 및 임계값 초과 시 알림
- **FR-020**: 중복 데이터 자동 제거
- **FR-021**: 데이터 타입 검증
- **FR-022**: 품질 검증 실패 시 파이프라인 중단 및 알림

### 5.5 워크플로우 오케스트레이션

- **FR-023**: Apache Airflow DAG로 전체 파이프라인 구성
- **FR-024**: Task 간 의존성 관리 (수집 → 정제 → 저장)
- **FR-025**: XCom을 통한 Task 간 데이터 전달
- **FR-026**: 스케줄 기반 자동 실행 지원 (daily, hourly 등)
- **FR-027**: 수동 트리거 기능 제공
- **FR-028**: Task 실패 시 자동 재시도 및 알림

### 5.6 모니터링 및 알림

- **FR-029**: Airflow UI를 통한 파이프라인 모니터링
- **FR-030**: 각 Task별 실행 시간 및 상태 추적
- **FR-031**: 구조화된 JSON 로그 생성
- **FR-032**: 파이프라인 실패 시 이메일/슬랙 알림
- **FR-033**: 데이터 처리 건수 및 성공률 대시보드

### 5.7 데이터 카탈로그

- **FR-034**: 각 데이터 소스의 메타데이터 관리
- **FR-035**: 데이터 계보(lineage) 추적 기능
- **FR-036**: 파일 생성 시각, 크기, 행 수 등 기록
- **FR-037**: 데이터 스키마 버전 관리


## 6. 비기능 요구사항 (Non-Functional Requirements)

### 6.1 성능

- **NFR-001**: 100만 행 데이터 처리 시간 2시간 이내
- **NFR-002**: LLM API 응답 시간 평균 3초 이내
- **NFR-003**: Parquet 파일 압축률 70% 이상
- **NFR-004**: 메모리 사용량 8GB 이하 유지
- **NFR-005**: CPU 사용률 평균 70% 이하

### 6.2 확장성

- **NFR-006**: 새로운 데이터 소스 추가 시 1일 이내 개발 완료 가능
- **NFR-007**: 동시 실행 가능한 DAG 수 10개 이상
- **NFR-008**: 수평 확장 가능한 아키텍처 (Airflow Executor 변경 지원)
- **NFR-009**: 데이터 볼륨 증가 시 선형적 성능 유지

### 6.3 가용성

- **NFR-010**: 시스템 가동률 99.5% 이상
- **NFR-011**: 파이프라인 성공률 95% 이상
- **NFR-012**: 장애 복구 시간(MTTR) 1시간 이내
- **NFR-013**: 데이터 백업 주기 일 1회
- **NFR-014**: 재해 복구 계획(DR) 수립

### 6.4 보안

- **NFR-015**: API 키 및 민감 정보는 환경 변수로 관리
- **NFR-016**: `.env` 파일은 Git에 커밋 금지 (`.gitignore` 등록)
- **NFR-017**: Airflow 관리자 페이지 인증 필수
- **NFR-018**: 데이터 파일 접근 권한 제어
- **NFR-019**: 모든 API 호출 로그 기록

### 6.5 유지보수성

- **NFR-020**: 코드 테스트 커버리지 80% 이상
- **NFR-021**: PEP 8 스타일 가이드 100% 준수
- **NFR-022**: 모든 함수에 docstring 작성
- **NFR-023**: 타입 힌트 100% 적용
- **NFR-024**: CI/CD 파이프라인 구축 (자동 테스트 및 배포)


## 7. 기술 아키텍처 (Technical Architecture)

### 7.1 시스템 구성도

```
┌─────────────────────────────────────────────────────────────┐
│                    Apache Airflow Scheduler                  │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐    │
│  │ Collect Task │ → │ Clean Task   │ → │  Save Task   │    │
│  │              │   │  (LLM)       │   │              │    │
│  └──────────────┘   └──────────────┘   └──────────────┘    │
│         ↓                  ↓                    ↓           │
└─────────│──────────────────│────────────────────│───────────┘
          │                  │                    │
          ↓                  ↓                    ↓
    ┌──────────┐       ┌──────────┐       ┌──────────┐
    │data/raw/ │       │data/     │       │data/     │
    │*.parquet │       │processed/│       │output/   │
    │          │       │*.parquet │       │*.csv     │
    └──────────┘       └──────────┘       └──────────┘
          ↑                  ↑
          │                  │
    ┌──────────┐       ┌──────────┐
    │  Data    │       │   LLM    │
    │ Sources  │       │   API    │
    └──────────┘       └──────────┘
```

### 7.2 데이터 플로우

1. **수집 단계**
   - `src/collector/` 모듈이 외부 데이터 소스에서 데이터 수집
   - DataFrame으로 변환 후 `data/raw/` 폴더에 Parquet 저장

2. **정제 단계**
   - `data/raw/` Parquet 파일 읽기
   - `resources/` task 파일 기반으로 LLM API 호출
   - 정제된 데이터를 `data/processed/` 폴더에 Parquet 저장

3. **저장 단계**
   - `data/processed/` Parquet 파일 읽기
   - CSV로 변환하여 `data/output/` 폴더에 저장

### 7.3 기술 스택

**언어 및 프레임워크**
- Python 3.13+
- Apache Airflow 2.8+

**데이터 처리**
- pandas 2.0+
- numpy 1.24+
- pyarrow 14.0+ (Parquet 지원)

**LLM 통합**
- OpenAI Python SDK
- Anthropic SDK (선택사항)

**컨테이너 및 배포**
- Docker 24+
- Docker Compose 2.20+

**개발 도구**
- Black (코드 포맷터)
- Ruff (린터)
- mypy (타입 체커)
- pytest (테스트 프레임워크)

### 7.4 인프라

**로컬 개발 환경**
- Ubuntu 22.04 LTS
- Python 가상환경 (venv)
- SQLite (Airflow 메타데이터 DB)

**프로덕션 환경 (향후)**
- Kubernetes 클러스터
- PostgreSQL (Airflow 메타데이터 DB)
- Redis (Celery 브로커)
- S3-compatible 스토리지 (데이터 저장소)

### 7.5 배포 전략

**Phase 1: 로컬 개발 (현재)**
- Docker Compose 기반 로컬 배포
- `airflow standalone` 개발 모드

**Phase 2: 스테이징**
- Docker Compose 프로덕션 모드
- LocalExecutor 사용

**Phase 3: 프로덕션**
- Kubernetes + Helm Chart 배포
- CeleryExecutor 또는 KubernetesExecutor
- Blue-Green 배포 전략


## 8. 사용자 인터페이스 (User Interface/User Experience)

### 8.1 대시보드

**Airflow 웹 UI (http://localhost:8080)**
- DAG 목록 및 실행 상태 한눈에 확인
- 성공/실패/실행 중인 Task 시각화
- 최근 실행 이력 및 트렌드

### 8.2 파이프라인 관리 UI

**DAG 관리**
- DAG 활성화/비활성화 토글
- 수동 트리거 버튼
- 스케줄 설정 확인
- Task 의존성 그래프 시각화

**Task 관리**
- 개별 Task 로그 조회
- Task 재실행 기능
- Task 상태 실시간 모니터링

### 8.3 모니터링 UI

**실행 로그**
- Task별 상세 로그 조회
- 에러 스택 트레이스 확인
- 실행 시간 분석

**성능 메트릭**
- Task 실행 시간 추이 그래프
- 메모리 사용량 모니터링
- 성공률 통계

**알림 설정**
- 이메일 알림 설정 (향후 구현)
- Slack 알림 연동 (향후 구현)


## 9. 데이터 모델 (Data Model)

### 9.1 원본 데이터 스키마

**data/raw/*.parquet**
```python
{
    "id": "int64",                    # 고유 식별자
    "source": "string",               # 데이터 소스명
    "raw_text": "string",             # 원본 텍스트
    "created_at": "datetime64[ns]",   # 수집 시각
    "metadata": "string"              # JSON 형식의 메타데이터
}
```

### 9.2 변환 데이터 스키마

**data/processed/*.parquet**
```python
{
    "id": "int64",                    # 고유 식별자
    "source": "string",               # 데이터 소스명
    "raw_text": "string",             # 원본 텍스트
    "cleaned_text": "string",         # LLM 정제된 텍스트
    "llm_model": "string",            # 사용된 LLM 모델명
    "cleaning_task": "string",        # 적용된 task 파일명
    "created_at": "datetime64[ns]",   # 수집 시각
    "processed_at": "datetime64[ns]", # 정제 시각
    "metadata": "string"              # JSON 형식의 메타데이터
}
```

### 9.3 메타데이터

**LLM Task 정의 (resources/*.yaml)**
```yaml
task_name: string          # Task 이름
description: string        # Task 설명
system_message: string     # LLM 시스템 메시지
prompt: string            # LLM 프롬프트 템플릿
model: string             # LLM 모델명
temperature: float        # 생성 온도
max_tokens: int          # 최대 토큰 수
```

### 9.4 데이터 계보 (Data Lineage)

**파일 경로 기반 추적**
```
source_data 
  → data/raw/source1_20260128_120000.parquet 
  → data/processed/cleaned_20260128_120530.parquet 
  → data/output/final_data_20260128_121000.csv
```

**Airflow XCom을 통한 메타데이터 전달**
- Task ID별 입출력 파일 경로 기록
- 처리 시간, 데이터 건수 등 메트릭 저장


## 10. API 명세 (API Specifications)

### 10.1 파이프라인 실행 API

**Airflow REST API 활용**

```bash
# DAG 트리거
POST /api/v1/dags/{dag_id}/dagRuns
Content-Type: application/json

{
  "conf": {
    "data_source": "source1",
    "task_file": "cleaning_task_1.yaml"
  }
}
```

### 10.2 데이터 조회 API

**로컬 파일 시스템 기반**

```python
# Python 코드로 데이터 조회
import pandas as pd

# 원본 데이터 조회
df_raw = pd.read_parquet("data/raw/source1_20260128.parquet")

# 정제된 데이터 조회
df_processed = pd.read_parquet("data/processed/cleaned_20260128.parquet")

# 최종 CSV 조회
df_final = pd.read_csv("data/output/final_data_20260128.csv")
```

### 10.3 모니터링 API

```bash
# DAG 실행 상태 조회
GET /api/v1/dags/{dag_id}/dagRuns

# Task 인스턴스 상태 조회
GET /api/v1/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances

# Task 로그 조회
GET /api/v1/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/logs/{log_number}
```

### 10.4 설정 관리 API

```bash
# Airflow Variable 설정
POST /api/v1/variables
{
  "key": "llm_api_key",
  "value": "sk-..."
}

# Airflow Connection 설정
POST /api/v1/connections
{
  "connection_id": "llm_api",
  "conn_type": "http",
  "host": "api.openai.com",
  "password": "sk-..."
}
```


## 11. 보안 요구사항 (Security Requirements)

### 11.1 인증 및 권한

- Airflow 웹 UI 접근 시 사용자 인증 필수
- RBAC(Role-Based Access Control) 적용
- Admin, User, Viewer 역할 구분
- API 호출 시 Bearer Token 인증

### 11.2 데이터 암호화

- LLM API 키는 환경 변수로 관리
- `.env` 파일은 Git에 커밋 금지
- Airflow Connection의 비밀번호는 암호화 저장
- 데이터 전송 시 HTTPS/TLS 사용

### 11.3 감사 로그

- 모든 DAG 실행 이력 기록
- Task 실행 로그 자동 저장
- 파일 접근 로그 기록
- API 호출 로그 저장

### 11.4 네트워크 보안

- Airflow 웹 UI는 내부 네트워크에서만 접근
- 프로덕션 환경에서는 VPN 또는 방화벽 설정
- LLM API 호출 시 rate limiting 적용
- Docker 컨테이너 네트워크 격리


## 12. 성능 요구사항 (Performance Requirements)

### 12.1 처리량

- 시간당 50만 행 데이터 처리 가능
- 하루 최대 1,000만 행 처리
- 동시 실행 가능한 DAG: 10개
- 파일당 최대 크기: 5GB (압축 전 기준)

### 12.2 응답 시간

- Parquet 파일 읽기/쓰기: 평균 30초 이내
- LLM API 호출 응답: 평균 3초 이내
- CSV 변환: 평균 1분 이내
- 전체 파이프라인 실행: 2시간 이내 (100만 행 기준)

### 12.3 동시 처리

- Airflow LocalExecutor: 최대 4개 Task 동시 실행
- LLM API 병렬 호출: 최대 10개 요청/초
- 청크 크기: 10,000행 단위 처리

### 12.4 리소스 사용

- 메모리 사용량: 최대 8GB
- CPU 사용률: 평균 70% 이하
- 디스크 I/O: 최대 500MB/s
- Parquet 압축률: 최소 70%


## 13. 일정 및 마일스톤 (Timeline and Milestones)

### Phase 1: 기초 인프라 구축 (2주)

**목표**: 개발 환경 및 기본 아키텍처 구축

- Week 1
  - [x] 프로젝트 구조 설계
  - [x] GitHub 저장소 및 문서 구성
  - [ ] Docker Compose 환경 구축
  - [ ] Airflow 초기 설정

- Week 2
  - [ ] 데이터 폴더 구조 생성 (raw/processed/output)
  - [ ] 기본 유틸리티 함수 구현
  - [ ] pytest 테스트 환경 구축
  - [ ] CI/CD 기본 설정

### Phase 2: 핵심 기능 개발 (4주)

**목표**: 데이터 수집, 정제, 저장 기능 구현

- Week 3-4: 데이터 수집
  - [ ] `src/collector/` 모듈 구조 설계
  - [ ] 샘플 데이터 소스 수집 코드 구현
  - [ ] DataFrame → Parquet 저장 로직 구현
  - [ ] 수집 모듈 단위 테스트

- Week 5-6: LLM 정제
  - [ ] `src/cleaners/` 모듈 구현
  - [ ] LLM API 클라이언트 구현
  - [ ] `resources/` task 파일 파싱 로직
  - [ ] Parquet → LLM → Parquet 파이프라인
  - [ ] 에러 핸들링 및 재시도 로직

- Week 7: CSV 저장
  - [ ] `src/loaders/` 모듈 구현
  - [ ] Parquet → CSV 변환 로직
  - [ ] 파일명 타임스탬프 처리
  - [ ] 데이터 검증 로직

### Phase 3: 오케스트레이션 및 통합 (3주)

**목표**: Airflow DAG 구성 및 전체 파이프라인 통합

- Week 8-9
  - [ ] Airflow DAG 구현 (수집 → 정제 → 저장)
  - [ ] XCom 기반 Task 간 데이터 전달
  - [ ] 스케줄링 설정
  - [ ] 통합 테스트

- Week 10
  - [ ] 에러 핸들링 및 알림 기능
  - [ ] 로깅 개선
  - [ ] 성능 최적화
  - [ ] 문서화 완성

### Phase 4: 최적화 및 안정화 (2주)

**목표**: 성능 개선 및 프로덕션 준비

- Week 11
  - [ ] 대용량 데이터 처리 테스트
  - [ ] 메모리 최적화
  - [ ] 청킹 전략 개선
  - [ ] 성능 벤치마크

- Week 12
  - [ ] 보안 검토
  - [ ] 프로덕션 배포 가이드 작성
  - [ ] 사용자 매뉴얼 작성
  - [ ] 최종 테스트 및 배포

**총 예상 기간**: 12주 (약 3개월)


## 14. 성공 지표 (Success Metrics)

### 14.1 기술 지표

| 지표 | 목표 | 측정 방법 |
|------|------|-----------|
| 파이프라인 성공률 | 95% 이상 | Airflow DAG Run 성공/실패 비율 |
| 평균 처리 시간 | 2시간 이내 | Task 실행 시간 합계 |
| LLM 정제 정확도 | 90% 이상 | 샘플 데이터 수동 검증 |
| 메모리 사용량 | 8GB 이하 | 시스템 모니터링 |
| 코드 커버리지 | 80% 이상 | pytest-cov 리포트 |

### 14.2 비즈니스 지표

| 지표 | 목표 | 측정 방법 |
|------|------|-----------|
| 데이터 처리 시간 단축 | 70% 감소 | 수작업 대비 소요 시간 비교 |
| 운영 비용 절감 | 60% 감소 | 인력 비용 + 인프라 비용 비교 |
| 신규 소스 추가 시간 | 1일 이내 | 실제 개발 소요 시간 측정 |
| 데이터 품질 향상 | 40% 향상 | 에러율, 결측치 비율 비교 |

### 14.3 운영 지표

| 지표 | 목표 | 측정 방법 |
|------|------|-----------|
| 시스템 가동률 | 99.5% 이상 | Uptime 모니터링 |
| 평균 장애 복구 시간 (MTTR) | 1시간 이내 | 장애 발생~복구 시간 측정 |
| 일일 처리 데이터량 | 1,000만 행 | 처리된 총 데이터 행 수 |
| API 호출 실패율 | 5% 이하 | LLM API 호출 성공/실패 비율 |
| 알림 응답 시간 | 5분 이내 | 장애 발생~알림 전송 시간 |


## 15. 리스크 및 완화 전략 (Risks and Mitigation)

### 15.1 기술적 리스크

| 리스크 | 영향도 | 확률 | 완화 전략 |
|--------|--------|------|-----------|
| LLM API 장애 | 높음 | 중간 | - 자동 재시도 로직 구현<br>- 백업 LLM 모델 준비<br>- Circuit Breaker 패턴 적용 |
| 메모리 부족 | 높음 | 중간 | - 청크 단위 처리<br>- 메모리 프로파일링<br>- 스왑 메모리 설정 |
| Parquet 파일 손상 | 중간 | 낮음 | - 파일 검증 로직 추가<br>- 백업 파일 보관<br>- 체크섬 검증 |
| Airflow 스케줄러 장애 | 높음 | 낮음 | - Health check 설정<br>- 자동 재시작 스크립트<br>- 알림 설정 |

### 15.2 운영 리스크

| 리스크 | 영향도 | 확률 | 완화 전략 |
|--------|--------|------|-----------|
| API 키 노출 | 높음 | 낮음 | - 환경 변수 관리<br>- Git secrets 스캔<br>- 정기적 키 로테이션 |
| 디스크 공간 부족 | 중간 | 중간 | - 디스크 사용량 모니터링<br>- 자동 정리 스크립트<br>- 알림 임계값 설정 |
| 장기 실행 Task 타임아웃 | 중간 | 중간 | - Task 타임아웃 설정<br>- 프로그레스 로깅<br>- 중간 체크포인트 저장 |
| 네트워크 장애 | 중간 | 낮음 | - 재시도 로직<br>- 타임아웃 설정<br>- 폴백 전략 |

### 15.3 비즈니스 리스크

| 리스크 | 영향도 | 확률 | 완화 전략 |
|--------|--------|------|-----------|
| LLM API 비용 초과 | 높음 | 중간 | - 비용 모니터링 대시보드<br>- 일일 한도 설정<br>- 캐싱 전략 적용 |
| 데이터 정제 품질 저하 | 높음 | 중간 | - A/B 테스트<br>- 샘플링 검증<br>- 사용자 피드백 수집 |
| 확장성 한계 | 중간 | 중간 | - 성능 벤치마크<br>- 병목 지점 분석<br>- 점진적 확장 계획 |
| 규정 준수 이슈 | 낮음 | 낮음 | - 데이터 보안 정책 수립<br>- 개인정보 마스킹<br>- 감사 로그 관리 |


## 16. 향후 개선 사항 (Future Enhancements)

### 16.1 단기 로드맵 (3-6개월)

**데이터 소스 확장**
- [ ] API 기반 데이터 수집 모듈 추가
- [ ] 데이터베이스 커넥터 구현 (PostgreSQL, MySQL)
- [ ] 파일 기반 소스 지원 (Excel, JSON, XML)

**정제 기능 개선**
- [ ] 다양한 LLM 모델 지원 (Claude, Llama 등)
- [ ] 멀티모달 데이터 처리 (이미지, 오디오)
- [ ] 정제 결과 A/B 테스트 기능

**모니터링 강화**
- [ ] 커스텀 메트릭 대시보드
- [ ] Slack/이메일 알림 통합
- [ ] 데이터 품질 스코어 자동 계산

**성능 최적화**
- [ ] Dask를 활용한 병렬 처리
- [ ] 캐싱 레이어 추가
- [ ] 증분 처리(incremental load) 지원

### 16.2 장기 로드맵 (6-12개월)

**클라우드 마이그레이션**
- [ ] AWS S3 + Glue 통합
- [ ] Kubernetes 기반 배포
- [ ] 오토스케일링 구현

**고급 기능**
- [ ] 실시간 스트리밍 처리 (Apache Kafka)
- [ ] 데이터 카탈로그 시스템 (Apache Atlas)
- [ ] ML 기반 데이터 품질 예측
- [ ] 자동 스키마 진화(schema evolution)

**거버넌스**
- [ ] 데이터 계보(lineage) 시각화
- [ ] GDPR/개인정보보호법 준수 기능
- [ ] 데이터 버전 관리 시스템
- [ ] 감사 로그 분석 도구

**사용자 경험**
- [ ] 웹 기반 설정 UI
- [ ] 노코드 데이터 파이프라인 빌더
- [ ] 자동 문서 생성 도구
- [ ] 사용자 포털 구축


## 17. 부록 (Appendix)

### 17.1 용어 정의

| 용어 | 정의 |
|------|------|
| **DataOps** | 데이터 분석 및 관리 프로세스를 자동화하고 개선하는 방법론 |
| **ETL** | Extract, Transform, Load의 약자로 데이터 추출, 변환, 적재 과정 |
| **Parquet** | 컬럼 기반의 효율적인 데이터 저장 형식 |
| **LLM** | Large Language Model, 대규모 언어 모델 |
| **DAG** | Directed Acyclic Graph, Airflow의 워크플로우 정의 단위 |
| **XCom** | Airflow Task 간 데이터 전달 메커니즘 |
| **멱등성(Idempotency)** | 같은 작업을 여러 번 수행해도 결과가 동일한 특성 |
| **청킹(Chunking)** | 대용량 데이터를 작은 단위로 나누어 처리하는 기법 |
| **Circuit Breaker** | 장애 전파를 막기 위한 디자인 패턴 |
| **Data Lineage** | 데이터의 출처, 이동 경로, 변환 과정을 추적하는 기능 |

### 17.2 참고 자료

**공식 문서**
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [PyArrow Parquet Documentation](https://arrow.apache.org/docs/python/parquet.html)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)

**아키텍처 참고**
- "The Data Engineering Cookbook" by Andreas Kretz
- "Fundamentals of Data Engineering" by Joe Reis and Matt Housley
- "Data Pipelines Pocket Reference" by James Densmore

**베스트 프랙티스**
- [Airflow Best Practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html)
- [Python DataOps Guide](https://www.datacamp.com/community/tutorials/python-data-engineering)

### 17.3 관련 문서

**내부 문서**
- [GitHub Copilot 코딩 지침](/.github/copilot-instructions.md)
- [워크스페이스 설정](/.github/copilot-workspace.md)
- [기여 가이드라인](/.github/CONTRIBUTING.md)
- [README.md](/README.md)

**설계 문서 (향후 작성 예정)**
- 데이터 아키텍처 설계서
- API 명세서
- 보안 정책 문서
- 운영 매뉴얼
- 장애 대응 가이드

---

**문서 정보**
- **작성자**: DataOps Team
- **작성일**: 2026-01-28
- **최종 수정일**: 2026-01-28
- **버전**: 1.0
- **승인자**: yonghwan.lee
- **다음 리뷰 예정일**: 2026-02-28

