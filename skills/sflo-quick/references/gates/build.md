# Gate 2: Developer Build

**Agent:** Developer
**Input:** SCOPE.md from Gate 1
**Produces:** Complete implementation + `BUILD-STATUS.md`

## What the Developer Does

1. Read SCOPE.md - understand requirements and data sources
2. Implement the requirements using vertical slices
3. Connect to real data (NOT mock/sample)
4. Run self-checks before handing off

## BUILD-STATUS.md Template

```markdown
## Build Status

- Build: SUCCESS (zero errors)
- Data loading: [N] records from [source]
- Core features: All ACs addressed

## Self-Check

- [ ] Real data loads (not mock/sample)
- [ ] Core use case works end-to-end
- [ ] Error states handled gracefully
- [ ] Each acceptance criterion from SCOPE.md addressed
- [ ] [Add project-specific checks based on SCOPE.md]
```

## Gate Check (Orchestrator verifies)

- [ ] Build produces zero errors
- [ ] BUILD-STATUS.md exists with all checks marked
- [ ] Implementation runs and uses real data

**If build fails → BACK TO DEV. Do not proceed to Gate 3.**

## Developer Rules

1. **Real data only** - if the product claims 13M records but loads 85, it's broken
2. **Build must pass** - zero compilation/build errors before QA sees it
3. **Self-check is mandatory** - don't waste QA's time with obvious bugs
4. **Document what you built** - BUILD-STATUS.md is your receipt
