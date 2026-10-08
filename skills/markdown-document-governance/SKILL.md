---
name: markdown-document-governance
description: Create, update, or organize repository Markdown while preserving document authority, current specifications, change records, and project-specific placement rules.
---

# Markdown Document Governance

文書の役割と承認状態を確認し、現在仕様と調査・計画・履歴の混同を防ぐ。

1. 利用先の `AGENTS.md`、文書の入口、対象ディレクトリの配置・命名・frontmatter規則を確認する。存在しない規約を参照必須にしない。
2. ユーザー指定の対象と保存先を尊重する。正本や配置規則と衝突する場合は、その関係を示して判断を求める。
3. 文書の役割を、現在仕様、契約・判断、変更仕様、計画、検証結果、手順、参考、履歴から特定する。
4. 利用先に管理規則がない場合や管理方法の設計を頼まれた場合は、[正本とライフサイクル](references/document-authority.md) を必要な範囲で使う。全案件へ固定の階層・メタデータを強制しない。
5. 同じ主題の正本を重複作成しない。承認済みの現在仕様を、下書きや過去計画で上書きしない。
6. 移動・整理は依頼範囲に限定し、参照リンクと後継関係を確認する。過去資料を更新停止とする運用がある場合はそれに従う。

文書の承認、実装開始、公開・外部投稿は別の行為として扱う。保存先がGit管理内かどうかだけで公開許可や正本性を判断しない。作業の規模に応じて記録し、軽微な変更のためだけに大量の文書を増やさない。
