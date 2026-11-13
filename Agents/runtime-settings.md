# 런타임 설정 기록

2026-11-13, 설치된 Band CLI의 `runtime template show --json --reveal`에서 필요한 필드만 확인했습니다. 다음은 **저장된 템플릿**의 값이며 현재 room 세션의 실제 유효 설정과 다를 수 있습니다. 기밀값·인증정보는 포함하지 않습니다.

| 설정 | Coordinator | Code Author | Code Reviewer |
|---|---|---|---|
| Handle | `@yeop99/coordinator` | `@yeop99/code-author` | `@yeop99/code-reviewer` |
| Harness | Codex | Codex | Codex |
| Transport | `codex-app-server` | `codex-app-server` | `codex-app-server` |
| 명시된 Model | `gpt-6.1-sol` | 미지정 (`null`) | 미지정 (`null`) |
| 명시된 Effort | `medium` | 미지정 (`null`) | 미지정 (`null`) |
| Approval policy | `on-request` | `on-request` | 미지정 (`null`) |
| Tool sandbox | `workspace-write` | `danger-full-access` | 미지정 (`null`) |
| 인증 방식 | 기존 런타임 인증 상속 | 기존 런타임 인증 상속 | 기존 런타임 인증 상속 |
| 작업 경로 | 저장소 내 `band-work/toy-result`의 절대경로 | 동일 | 동일 |

미지정 값은 실제 모델·권한이 없다는 뜻이 아닙니다. 런타임 기본값이나 세션 설정을 확인해야 하며, 제출 문서에 임의의 값을 채우면 안 됩니다.

Code Author는 Node 탐색 오류 때문에 설치된 Codex의 네이티브 실행 파일 절대경로를 사용합니다. 다른 두 템플릿은 `codex`를 사용합니다. 해당 경로는 기기와 설치 버전에 종속되므로 복제하지 말고 각 기기에서 Test runtime으로 확인합니다.

## 새 팀에 적용하기 전 확정할 항목

- 각 역할의 실제 handle과 지침 파일.
- 명시적인 모델 ID와 추론 수준, 실제 세션에 적용됐는지 여부.
- 별도 결과 저장소의 절대경로와 병렬 작업 경로.
- 파일·Git·Band 소켓·Docker·브라우저 검사에 필요한 권한.
- 연습용 승인 방식과 제출용 무인 실행의 차이.
- 사용 시 공유 메모리 연결과 인증정보의 저장 위치.

현재 Code Author의 넓은 접근 권한은 관측값이며 새 팀의 권장 기본값이 아닙니다. 권한을 무조건 넓히거나 승인 요청만 끄는 것으로 환경 검증을 대신하지 않습니다.
