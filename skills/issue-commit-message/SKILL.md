---
name: issue-commit-message
description: Draft or improve Git commit messages grounded in the actual diff and the repository's conventions, with issue identifiers when required or supplied.
---

# Issue Commit Message

1. 利用先のコミット規約と指定言語を確認する。
2. `git status --short` とステージ済み差分を確認する。ステージ済み変更がなければ未ステージ差分を読み、どの差分を根拠にしたか示す。未追跡ファイルを自動的に対象へ含めない。
3. 指定された課題番号を使う。ブランチから番号を読み取れる場合は候補にできるが、別課題と混ざる場合は確認する。番号必須でなければ番号なしでも作成する。
4. 実際の変更目的と内容だけを書く。課題タイトルだけで未実装の要件まで書かない。
5. 無関係な変更が混ざる場合は、必要に応じてコミット分割を提案する。

利用先に書式がなければ、短い要約と必要な補足を使う。課題番号がある場合の例:

```text
TASK-123: 入力エラーの表示を改善

- 入力欄の名称をエラー文へ反映
- 条件付き必須項目の案内を調整
```

箇条書きの数を固定しない。検証結果は実施した場合だけ記載する。メッセージ作成の依頼では `git add`、コミット、pushを実行しない。実行も依頼された場合は、その範囲と利用先の規約に従う。
