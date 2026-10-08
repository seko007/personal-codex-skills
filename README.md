# Personal Engineering Skills

調査、実装、レビュー、見積もり、文書整理で使う個人用スキル集です。特定の業務、会社、フレームワーク、開発環境に依存する規則を取り除き、利用先のプロジェクト規約に合わせて使える形にしています。

## 構成

| 配置 | 役割 |
| --- | --- |
| `skills/` | 実際に呼び出すスキル。各フォルダを単独でコピーできる |
| `skills/*/references/` | そのスキルが必要に応じて読む補助資料。同じフォルダで配布する |
| `templates/` | プロジェクトに合わせて編集してから採用する雛形 |
| `guides/` | 人が構成や運用を理解するための説明 |
| `scripts/validate_package.py` | 構成、内部リンク、名前、混入禁止情報の簡易検査 |

スキルからパッケージ直下の共有資料を必須参照させていません。一つだけインストールしても参照先が欠けない構成です。

## スキル一覧

| スキル | 用途 |
| --- | --- |
| [bug-triage](skills/bug-triage/SKILL.md) | 期待値、再現条件、原因、修正案の整理 |
| [code-review](skills/code-review/SKILL.md) | 差分と要件を照合し、具体的な不具合・回帰を指摘 |
| [backend-implementation](skills/backend-implementation/SKILL.md) | API、保存、整合性、副作用を含む実装 |
| [task-analysis](skills/task-analysis/SKILL.md) | 要件調査、影響範囲、意思決定の整理 |
| [pre-implementation-matrix](skills/pre-implementation-matrix/SKILL.md) | 実装・回帰・移行・復旧の対応表 |
| [software-effort-estimation](skills/software-effort-estimation/SKILL.md) | 前提と仕様パターンに基づく工数見積もり |
| [issue-commit-message](skills/issue-commit-message/SKILL.md) | 差分に基づく課題付きコミットメッセージ |
| [markdown-document-governance](skills/markdown-document-governance/SKILL.md) | 現在仕様、変更計画、履歴の配置・整理 |
| [context-handoff](skills/context-handoff/SKILL.md) | 作業フェーズの境界で必要最小限の引継ぎ |

## 利用方法

必要なスキルのフォルダを、利用するCodex環境のスキル配置先へフォルダごとコピーします。例えば `skills/bug-triage/` を配置し、`$bug-triage` を指定して調査を依頼できます。`references/` と `agents/` も一緒にコピーしてください。設定された配置先は利用環境で確認してください。

[AGENTS.md.template](templates/AGENTS.md.template) は新規プロジェクト用の雛形です。利用先の既存 `AGENTS.md` と照合し、必要な項目を採用します。このファイルを置くだけではプロジェクト指示書として有効になりません。

[SDD運用ガイド](guides/spec-driven-development.md) と変更文書の雛形は、仕様の確認・計画・実装を分けたいプロジェクトで任意に採用します。既存の運用を一律に置き換えません。

## 検査

パッケージのルートで実行します。

```sh
python3 scripts/validate_package.py
```

この検査は実環境でのスキル動作や公開権限を保証するものではありません。採用後は、実際の依頼に対する動作を確認して改善してください。

## 配布範囲

このディレクトリを独立したGitリポジトリの内容として扱えます。元資料、バックアップ、システム付属スキル、キャッシュ、個別課題の資料は含めません。ライセンスは未設定です。再配布条件は、所有者が公開時に決めてください。

抽出・変更方針は [再利用と保守](guides/reuse-and-maintenance.md) を参照してください。
