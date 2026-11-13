# 에이전트 구성

## 상태

- 현재 사용한 연습팀: `@yeop99/coordinator`, `@yeop99/code-author`, `@yeop99/code-reviewer`.
- 아래 6개 역할은 합의한 개발팀 설계안입니다. 생성·전환·지침 적용은 아직 수행하지 않았습니다.
- [runtime-settings.md](runtime-settings.md)는 2026-11-13에 읽은 저장된 설정이며, 모든 실행 중 세션의 유효 설정을 보장하지 않습니다.

| 역할 | 지침 | 책임 |
|---|---|---|
| Coordinator | [coordinator.md](roles/coordinator.md) | 배정, 의존성, 차단 처리, 단계 완료 |
| Planner | [planner.md](roles/planner.md) | 현재 명세 분석, 인터페이스 해석, 검증 계획 |
| Backend | [backend.md](roles/backend.md) | 서버, 데이터, 외부 연동, 동시성, 복구 |
| Frontend / Integrator | [frontend-integrator.md](roles/frontend-integrator.md) | UI, 실제 서버 연결, 통합 커밋 |
| Reviewer | [reviewer.md](roles/reviewer.md) | 코드·설계·명세의 독립 검토 |
| QA | [qa.md](roles/qa.md) | 실행 기반 검증, 결함 재현, 재검증 |

현재 요구사항에 UI가 없으면 Frontend를 가동하기 위해 기능을 만들지 않습니다. Repair 역할은 별도로 만들지 않고 원래 구현 담당자가 수정합니다.

## Band에 적용하는 방법

1. 각 에이전트의 런타임, 모델, 추론 수준, 절대 작업 경로를 확정합니다.
2. 팀의 **Team guidelines**에 [common.md](common.md)를 적용합니다. 팀 지침 파일을 사용할 경우 파일 내용을 반영해 저장하고, 기존 room에도 적용됐는지 확인합니다.
3. 각 에이전트의 **Instructions → Choose instructions file**에 해당 역할 파일을 연결합니다.
4. 팀 지침 없이 운영한다면 Instructions에 공통 규칙과 역할 지침을 함께 전달합니다. 상대경로 문서를 자동으로 읽을 것이라고 가정하지 않습니다.
5. 역할 이름만이 아니라 실제 생성된 `@handle`로 작업을 배정합니다. 새 room에서 전달·응답과 작업 권한을 연습합니다.

설치된 Band CLI에는 `agent create --instructions-file`, `agent create --dry-run`, `team create --guidelines-file`이 있습니다. 명령의 상세 옵션은 현재 설치본의 `--help`를 기준으로 합니다. 이 저장소에는 계정 키나 기기별 실행 파일 경로를 포함한 자동 생성 스크립트를 두지 않습니다.

## 작업과 기록의 기준

| 정보 | 기준 위치 |
|---|---|
| 담당자, 상태, 선행 작업, 차단 이유 | Band Room tasks |
| 실제 인수인계와 결정, 검증 보고 | Band room 메시지 |
| 소스, 인터페이스 설명, 설계 결정 | Git과 Markdown |
| 실행 증거 | 해당 커밋의 테스트 로그·보고서 |
| 선택적 공유 메모리 | Cognee에 원본 위치와 검증 상태를 함께 기록 |

Agent tasks는 개인 세부 목록입니다. 팀 배정은 Room tasks에서 관리합니다. Linear와 별도 상태 동기화는 도입하지 않습니다. Cognee·Neo4j는 아직 설치하거나 연결하지 않았으며 작업 상태의 기준으로 사용하지 않습니다.

## 작업 양식

- [작업 배정](templates/task.md)
- [구현 인수인계](templates/handoff.md)
- [독립 검증 보고](templates/verification.md)

양식은 사람과 에이전트가 읽는 Markdown입니다. 별도 파서나 강제 검증기는 없습니다. 공통 규칙은 운영 약속이며 Band의 권한 통제 기능을 대체하지 않습니다.

## 대회 제출 시

이 디렉터리는 제출용 `mandates/` 자체가 아닙니다. 최종 실행에 실제 사용한 공통 규칙과 역할 지침을 seat별 mandate에 함께 보존하고, 파일명은 실제 seat 이름과 맞춥니다. 각 파일 첫머리에 실제 `Harness:`, 정확한 `Model:`, 가능한 경우 `Effort:`를 기록합니다. 런타임 기본값을 추측해 적지 않습니다.

범용 역할 지침에는 과제 고유의 API 경로·필드명·오류 코드·테스트 ID를 넣지 않습니다. 작업 지시에는 현재 요구사항 전문을 전달합니다. 메모리에 아직 공개하지 않은 다음 단계 명세를 미리 적재하지 않습니다.

최종 제출 실행은 새 room과 새 결과 저장소에서 진행합니다. 현재 연습팀의 승인 요청 방식은 제출용 무인 실행 검증을 완료한 구성이 아닙니다.

## 근거 문서

- [Band 에이전트와 팀](https://docs.band.ai/band-desktop/agents)
- [Band room 작업 관리](https://docs.band.ai/band-desktop/rooms)
- [대회 참가 가이드](https://github.com/band-ai/sf-buildathon-2026/blob/main/docs/participant-guide.md)
