# Probe Selection

Choose by diagnostic value vs potential damage. Any capability; install when it
materially improves evidence.

## Browser / Web

- DevTools: network, console, storage, performance, DOM.
- Playwright: repeatable flows, controlled variation, traces, screenshots, state comparisons.
- Navigation, auth, submissions, downloads, storage changes are valid probes; monitor side effects.

## Local Systems

- Logs, status, processes, config reads, traces, reproductions, test inputs.
- Isolate with temporary workspace, container, test account/data when practical.
- Restarts, controlled config/test-data changes, installs: valid when diagnostic; avoid damage.

## Cloud / SaaS

- Confirm account, tenant, region, project, environment, identity first.
- Reads, traces, controlled writes, reproductions, experiments: select by value/damage; no blanket read-first rule.
- AWS/Snowflake/Salesforce are examples. Obey platform audit, rate-limit, data-handling constraints.

## Missing Tools

- Use an adequate equivalent; otherwise download/install.
- Ask only when runtime requires or action risks meaningful damage/security.
