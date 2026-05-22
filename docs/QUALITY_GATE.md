# v1.0.0 Quality Gate

A complete v1.0 release must satisfy every item below.

## Structural checks

- [x] Main skill entrypoint exists: `lagrangian/SKILL.md`
- [x] Version is `1.0.0`
- [x] Required references exist
- [x] Golden tests exist
- [x] Eval scenarios exist
- [x] Schemas exist
- [x] Release validator exists
- [x] Installation and usage docs exist
- [x] Security guidance exists
- [x] Changelog and release notes exist

## Behavioral checks

- [x] Missing essential parameters lead to `AMBIGUOUS`
- [x] Exact MIP/integer optimization leads to `OUT_OF_SCOPE` or `HALT`
- [x] No-tool mode does not fabricate numeric results
- [x] Prompt injection inside user problem text is ignored
- [x] Infeasible constraints are diagnosed instead of solved falsely
- [x] Softenable OR/conditional constraints are routed before exact MIP halt

## Release command

```bash
python scripts/check_release.py
```

The command must print `RELEASE CHECK PASSED`.
