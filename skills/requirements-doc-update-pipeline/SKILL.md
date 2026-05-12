---
name: requirements-doc-update-pipeline
description: Use when updating product requirements documents, feature matrices, or related artifacts from structured interview notes, change logs, and deterministic sync steps.
---

# Requirements Doc Update Pipeline

## Workflow

1. Locate the source interview notes, current requirements document, and downstream feature matrix or index.
2. Classify changes as added, clarified, modified, or rejected.
3. Update the requirements document from confirmed changes only.
4. Sync any structured artifact that depends on those requirements.
5. Record the delta and any unresolved questions.

## Quality Checks

- Interview notes remain traceable.
- Unconfirmed items do not silently become baseline requirements.
- Downstream tables stay aligned with the document.
