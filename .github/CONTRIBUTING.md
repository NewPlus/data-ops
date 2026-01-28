# 기여 가이드라인

## 시작하기

이 프로젝트에 기여해주셔서 감사합니다! 아래 가이드라인을 따라주세요.

### 개발 환경 설정

```bash
# 저장소 클론
git clone https://github.com/your-org/data-ops.git
cd data-ops

# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 환경 변수 설정
cp .env.example .env
# .env 파일을 편집하여 필요한 환경 변수 설정
```

## 개발 프로세스

1. **이슈 생성**: 작업 시작 전 이슈를 먼저 생성하고 논의
2. **브랜치 생성**: 적절한 명명 규칙에 따라 브랜치 생성
3. **코드 작성**: 코딩 표준 및 스타일 가이드 준수
4. **테스트 작성**: 새로운 기능에 대한 테스트 코드 작성
5. **커밋**: 명확한 커밋 메시지 작성
6. **Pull Request**: 리뷰를 위한 PR 생성

## Pull Request 프로세스

### PR 생성 전 체크리스트

- [ ] 코드가 PEP 8 스타일 가이드를 준수하는가?
- [ ] 모든 테스트가 통과하는가?
- [ ] 새로운 기능에 대한 테스트를 추가했는가?
- [ ] 문서를 업데이트했는가?
- [ ] 커밋 메시지가 규칙을 준수하는가?

### PR 생성 단계

1. 변경 사항을 feature 브랜치에 커밋
2. 원격 저장소에 push
3. GitHub에서 Pull Request 생성
4. PR 템플릿에 따라 설명 작성
5. 관련 이슈 링크
6. 리뷰어 지정

### PR 템플릿

```markdown
## 변경 사항 요약
<!-- 무엇을 변경했는지 간략히 설명 -->

## 변경 이유
<!-- 왜 이 변경이 필요한지 설명 -->

## 관련 이슈
Closes #이슈번호

## 테스트 방법
<!-- 어떻게 테스트했는지 설명 -->

## 스크린샷 (선택사항)
<!-- UI 변경이 있는 경우 스크린샷 첨부 -->

## 체크리스트
- [ ] 테스트 통과
- [ ] 코드 스타일 준수
- [ ] 문서 업데이트
```

## 코드 리뷰 가이드라인

### 리뷰어 역할

- 코드의 논리적 정확성 검증
- 성능 및 보안 이슈 확인
- 코딩 표준 준수 여부 확인
- 테스트 커버리지 검토
- 건설적인 피드백 제공

### 리뷰 시 중점 사항

1. **기능성**: 코드가 의도한 대로 동작하는가?
2. **가독성**: 코드를 이해하기 쉬운가?
3. **유지보수성**: 향후 수정이 용이한가?
4. **성능**: 성능 이슈가 없는가?
5. **보안**: 보안 취약점이 없는가?
6. **테스트**: 충분한 테스트가 있는가?

## 커밋 메시지 형식

### 커밋 메시지 규칙

```
<타입>(<범위>): <제목>

<본문>

<푸터>
```

### 타입

- `feat`: 새로운 기능 추가
- `fix`: 버그 수정
- `docs`: 문서 변경
- `style`: 코드 포맷팅, 세미콜론 누락 등
- `refactor`: 코드 리팩토링
- `test`: 테스트 코드 추가/수정
- `chore`: 빌드, 설정 파일 변경

### 예시

```
feat(pipeline): 고객 데이터 ETL 파이프라인 추가

- PostgreSQL에서 고객 데이터 추출
- 데이터 정규화 및 변환
- S3에 Parquet 형식으로 저장

Closes #123
```

## 브랜치 명명 규칙

### 브랜치 타입

- `feature/`: 새로운 기능 개발
- `bugfix/`: 버그 수정
- `hotfix/`: 긴급 수정
- `refactor/`: 코드 리팩토링
- `docs/`: 문서 작업
- `test/`: 테스트 추가/수정

### 예시

```
feature/customer-data-pipeline
bugfix/fix-data-validation-error
hotfix/critical-memory-leak
refactor/optimize-data-loading
docs/update-installation-guide
test/add-integration-tests
```

## 테스트

### 테스트 실행

```bash
# 모든 테스트 실행
pytest

# 커버리지와 함께 테스트 실행
pytest --cov=src --cov-report=html

# 특정 테스트 파일 실행
pytest tests/test_pipeline.py

# 특정 테스트 함수 실행
pytest tests/test_pipeline.py::test_process_data
```

### 테스트 작성 가이드

- 각 함수마다 최소 하나의 테스트 작성
- 성공 케이스와 실패 케이스 모두 테스트
- Edge case 고려
- Mock 및 Fixture 적절히 활용
- 테스트는 독립적이고 반복 가능해야 함

## 문서화

### 문서 작성 위치

- **코드 내 Docstring**: 함수, 클래스, 모듈 설명
- **README.md**: 프로젝트 개요 및 시작 가이드
- **docs/**: 상세 기술 문서
- **Wiki**: 설계 문서, 아키텍처 다이어그램

### Docstring 예시

```python
def extract_customer_data(
    start_date: datetime,
    end_date: datetime,
    customer_ids: List[int] = None
) -> pd.DataFrame:
    """지정된 기간의 고객 데이터를 추출합니다.
    
    Args:
        start_date: 데이터 추출 시작 날짜
        end_date: 데이터 추출 종료 날짜
        customer_ids: 특정 고객 ID 리스트 (선택사항)
    
    Returns:
        고객 데이터가 포함된 DataFrame
        
    Raises:
        ValueError: 날짜 범위가 유효하지 않을 때
        DatabaseError: 데이터베이스 연결 실패 시
        
    Example:
        >>> start = datetime(2024, 1, 1)
        >>> end = datetime(2024, 1, 31)
        >>> df = extract_customer_data(start, end)
        >>> print(df.head())
    """
    # 구현...
```

## 질문 및 지원

- **이슈**: 버그 리포트 및 기능 요청
- **Discussions**: 일반적인 질문 및 논의
- **Slack/Discord**: 실시간 커뮤니케이션 (있는 경우)

감사합니다! 🎉

