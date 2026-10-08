#!/usr/bin/env python3
"""Validate this portable skill collection using only the standard library."""

import re
import sys
from pathlib import Path


def validate(root: Path) -> list[str]:
    """Check package structure, internal references, and accidental local content."""
    errors: list[str] = []
    skill_root = root / "skills"
    skill_files = sorted(skill_root.glob("*/SKILL.md"))
    if not skill_files:
        errors.append("No skills found")

    for skill_file in skill_files:
        skill_dir = skill_file.parent
        content = skill_file.read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
        if not frontmatter:
            errors.append(f"{skill_file.relative_to(root)}: missing frontmatter")
            continue
        fields = dict(re.findall(r"^([a-z-]+): (.+)$", frontmatter[1], re.M))
        if fields.get("name") != skill_dir.name:
            errors.append(f"{skill_dir.name}: name must match the directory")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill_dir.name):
            errors.append(f"{skill_dir.name}: invalid skill name")
        if len(skill_dir.name) > 64:
            errors.append(f"{skill_dir.name}: skill name is too long")
        if not fields.get("description", "").strip():
            errors.append(f"{skill_dir.name}: missing description")
        if len(fields.get("description", "")) > 1024:
            errors.append(f"{skill_dir.name}: description is too long")

        ui_file = skill_dir / "agents" / "openai.yaml"
        if not ui_file.is_file():
            errors.append(f"{skill_dir.name}: missing UI metadata")
        else:
            ui = ui_file.read_text(encoding="utf-8")
            if f"${skill_dir.name}" not in ui:
                errors.append(f"{skill_dir.name}: default prompt must name the skill")
            short = re.search(r'^  short_description: "(.*)"$', ui, re.M)
            if not short or not 25 <= len(short[1]) <= 64:
                errors.append(f"{skill_dir.name}: short description must be 25–64 chars")

    # Detect accidental personal paths and local-only document dependencies.
    # Project identifiers need an additional source-specific audit before release.
    banned = re.compile(
        r"/home/|/Users/|[A-Za-z]:\\Users\\|(?:^|/)\.idea/",
        re.I,
    )
    forbidden_names = {".system", "__pycache__", ".env"}
    text_suffixes = {".md", ".template", ".yaml", ".yml", ".py"}
    link_count = 0
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if ".git" in rel.parts:
            continue
        if path.is_symlink():
            errors.append(f"{rel}: symlink is not portable")
            continue
        if path.name in forbidden_names or path.suffix == ".pyc":
            errors.append(f"{rel}: local or system artifact")
        if not path.is_file() or path.suffix not in text_suffixes:
            continue
        content = path.read_text(encoding="utf-8")
        if path.name != "validate_package.py" and banned.search(content):
            errors.append(f"{rel}: absolute personal path or local-only dependency")
        if path.suffix not in {".md", ".template"}:
            continue
        for link in re.findall(r"\[[^\]\n]*\]\(([^)\s]+)\)", content):
            if re.match(r"[a-z][a-z0-9+.-]*:", link, re.I) or link.startswith("#"):
                continue
            target_text = link.split("#", 1)[0]
            target = (path.parent / target_text).resolve()
            link_count += 1
            if not target.is_relative_to(root.resolve()) or not target.exists():
                errors.append(f"{rel}: missing or external local link {link}")
            if skill_root in path.parents:
                containing_skill = skill_root / path.relative_to(skill_root).parts[0]
                if not target.is_relative_to(containing_skill.resolve()):
                    errors.append(f"{rel}: link leaves the independently portable skill")

    if not errors:
        print(f"PASS: {len(skill_files)} skills; {link_count} local links; portable references")
    return errors


if __name__ == "__main__":
    package_root = Path(__file__).resolve().parent.parent
    failures = validate(package_root)
    for failure in failures:
        print(f"FAIL: {failure}", file=sys.stderr)
    sys.exit(bool(failures))
