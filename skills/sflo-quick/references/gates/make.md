# MAKE

Produce `MAKE.md` while building the smallest usable end-to-end candidate.

Name candidates `M1`, `M2`, and onward. Keep current candidate, last proven candidate, and repair count in one status block; append history below. Before changing a proven candidate, save its recoverable snapshot and record the reference. For each candidate, record changed work-product paths, the intended delta, evidence references, and the cumulative repair count; keep observed results in `CHECK.md`. Give the last proven candidate a recoverable reference appropriate to the project, such as a commit, snapshot, or retained artifact set.

Treat builder self-checks as readiness signals; CHECK supplies passing evidence from a non-builder context. MAKE passes when the current candidate is ready for direct probing. After CHECK passes, mark that candidate as last proven while preserving its recovery reference.
