# Quality Assurance — Ologos Ecosystem Guardrails

## Scope
This skill defines the QA standards, review gates, and operational guardrails for the entire Ologos ecosystem. These standards apply to any AI operator or human administrator. They are not guidelines; they are requirements. Model-agnostic: the same standards apply whether the operator is Claude, GPT, Gemini, or any future model.

All actions should be evaluated against the Ecosystem Impact Levels defined in sysadmin.md. Higher impact levels require more rigorous QA.

---

## Fundamental Principles

### 1. Dev-First, Always
Every change that affects user-facing behavior must be developed and tested in the dev environment before touching production.

- **Frontend changes** (HTML, CSS, JS): edit in static/dev/, test on devbot.<domain>
- **Backend changes** (skills, prompts, validators): commit to dev branch, deploy dev container, test
- **Infrastructure changes** (tunnel, DNS, Docker): test on dev port/container first when possible
- Promote to prod only on explicit user approval
- If a change cannot be tested in dev (e.g., shared SearXNG config), flag it before making it

### 2. Verify Before Claiming Done
Never declare work complete without verification.

- After deploy: run health check, inspect logs for errors
- After UI change: visually verify (render to PNG or ask user for screenshot)
- After code change: import check, basic smoke test
- After Git push: verify remote received it (`git log --oneline -1` on target)
- After issue creation: confirm the URL was returned

### 3. No Black Boxes
Full observability across every layer. No silent failures.

- Every error must be logged with enough context to diagnose
- Every retry must log what failed and what's being retried
- Every model call must be traceable (which model, how long, success/failure)
- Every background job must report progress
- If something fails silently, that's a bug — fix the logging first, then fix the failure

---

## QA Agent (Primary Reviewer)

The QA agent (`qa-agent/agent.py`) is the primary quality reviewer for all work in this ecosystem. It runs an independent model (default: GPT-4.1 Mini) to review work produced by the primary operator. **The operator does not QA their own work — the QA agent does.**

### When to Run
- **Before committing**: Run against all changed/new files
- **Before declaring any task complete**: Run against the deliverables
- **Before closing an issue**: Run against the files that address the issue
- **During session wrap**: Run against any files changed during the session that haven't been reviewed yet

### How to Run
```bash
cd ~/repos/<ops-repo>/qa-agent/
python3 agent.py <files_or_dirs> [--issue '#NN']

# Examples:
python3 agent.py ../ops/                        # Review ops/ layer
python3 agent.py ../skills/cloudflare.md        # Review a single file
python3 agent.py ../qa-agent/ --issue '#17'     # Review with issue reference
python3 agent.py ../ops/ --provider gemini      # Swap model for comparison
```

### Interpreting Results
- **pass**: Commit and proceed
- **pass_with_warnings**: Review warnings. If they are intentional tradeoffs, proceed. If they are real issues, fix first.
- **fail**: Fix all fail items before committing. Re-run after fixes.

### Non-Negotiable
- The QA agent MUST be run before declaring work complete. Skipping it is a compliance violation logged in ops/qa_log.json.
- If the QA agent is unreachable (API error, timeout), flag it to the user and document in ops/qa_log.json. Do not silently skip.
- Results are automatically logged to ops/qa_log.json. Do not use `--no-log` in normal workflow.

---

## Code Quality Gates

These gates are checked by the QA agent automatically. The operator should also verify these before invoking the agent to avoid wasting API calls on obvious issues.

### Before Committing
- [ ] Code compiles/imports cleanly (test with `python3 -c "from app.module import function"`)
- [ ] No secrets, credentials, or internal URLs in the code or commit message
- [ ] No debug print statements left in (unless they serve as permanent logging)
- [ ] Changes are focused — don't bundle unrelated fixes in one commit
- [ ] **QA agent passed** (`python3 qa-agent/agent.py <changed_files>`)

### Before Deploying
- [ ] Committed and pushed to the correct branch (dev or main)
- [ ] If deploying to prod: changes were tested on dev first
- [ ] If deploying to dev: basic smoke test passes after deploy
- [ ] Container starts without errors (check `docker logs`)
- [ ] Health check returns 200

### Before Closing an Issue
- [ ] The fix actually addresses the issue as described
- [ ] Smoke tested in the relevant environment
- [ ] **QA agent passed** against the deliverables for this issue
- [ ] Issue comment documents what was done and how to verify
- [ ] Related memory/documentation updated if needed

---

## Content Quality Standards

### Generated Documents (PPTX, DOCX, XLSX)
- No placeholder text ("Description of...", "Insert content here")
- Content must be substantive and audience-appropriate
- Financial data must use appropriate visualizations (tables, charts, stats)
- User-provided numbers must appear verbatim in output
- Every claim should be supportable — no fabricated statistics without attribution
- Takeaway text must be a genuine insight, not a restatement of the title

### Chat Responses
- Answer the actual question asked, not a related one
- Surface uncertainty clearly — "I'm not sure" is better than a confident wrong answer
- Don't over-explain — match the user's level of detail
- If an action failed, say what failed and what the options are

### White Papers and Formal Documents
- All claims must be verifiable — cite sources
- No em dashes (AI tell) — use semicolons, colons, commas, or restructure
- Remove AI patterns: "It's important to note that...", "Let's delve into...", "In conclusion..."
- Audience-appropriate depth and vocabulary
- Remove all internal references (Ologos, telogos) unless explicitly requested

---

## Operational Guardrails

### Things That Require User Approval
- Deploying to production
- Deleting files, branches, or data
- Modifying .env files or credentials
- Changing Cloudflare tunnel or DNS configuration
- Creating or closing GitHub issues (unless part of an approved workflow)
- Sending messages to Telegram or external services
- Force-pushing or resetting Git history
- Installing new packages or tools on hosts

### Things That Don't Require Approval
- Reading files, checking status, running diagnostics
- Committing to dev branch
- Deploying to dev environment
- Creating draft documents in Downloads
- Running smoke tests
- Checking logs and health endpoints

### Blast Radius Assessment
Before any action, evaluate:
1. **Reversibility** — can this be undone? If not, confirm first.
2. **Scope** — does this affect only dev, or also prod? Only one service, or many?
3. **Visibility** — will users see this immediately? Is there a grace period?
4. **Data risk** — could this lose data? Corrupt state? Break running sessions?

If any answer raises concern, stop and confirm with the user.

### QA Logging (ops/)
Every quality-relevant event must be logged to the appropriate ops/ file as it occurs. Do not batch logging to session wrap.

**When to log to `ops/qa_log.json`:**
- After every artifact review (PPTX, DOCX, XLSX, PDF, SVG) — include pass/fail, model, rejection reason
- When a hallucination is caught — include what was claimed, what was true, how it was caught
- After every compliance check (dev-first, credential handling, blast radius assessment)
- After every regression test or smoke test

**When to update `ops/qa_watchlist.json`:**
- When an artifact type shows intermittent failures — add watch item with recurrence count
- When a hallucination pattern appears (same type of false claim recurring) — add watch item
- When a model shows consistent quality issues — add watch item
- When a watched concern is addressed — mark `status: "resolved"` with timestamp

**When to log to `ops/promotion_log.json`:**
- After every dev-to-prod promotion — include branch, commit, test results, verification
- If code goes directly to prod without dev testing — log as `violation: true` with justification

### QA Enforcement Automation

The ops/ logs are not just records — they drive enforcement. The operator and `scripts/ops-analyze.py` apply these rules automatically.

**Threshold alerts (auto-create watchlist items):**
- **QA rejection rate >30%** in last 10 reviews → watchlist item + recommend GitHub issue
- **Hallucination recurrence**: same `hallucination_type` appears 3+ times → watchlist item with pattern analysis
- **Dev-first violation**: any `violation: true` in promotion_log → watchlist item immediately
- **QA agent skipped**: if a commit happens without a corresponding qa_log entry → compliance failure logged retroactively

**Aggregate analysis (surfaced at session start via `scripts/ops-analyze.py`):**
- **By model**: which models have the highest QA failure rate? Flag models with >30% fail rate.
- **By artifact type**: which types (PPTX, DOCX, etc.) fail most? Direct skill improvement efforts.
- **By failure reason**: cluster rejection reasons to identify systemic issues vs one-off failures.
- **Promotion compliance**: what % of promotions followed dev-first? Any violations in last 7 days?

**Escalation rules:**
- First QA failure on a type/model combo: log it, move on
- Second failure (same type/model within 7 days): add watchlist item
- Third failure: auto-recommend GitHub issue creation to the operator
- Dev-first violation: always escalate immediately — log + watchlist + flag to user

**Hallucination tracking lifecycle:**
1. **Caught**: Log in qa_log.json with `type: "hallucination_catch"`, include claimed vs actual
2. **Pattern check**: Does this match a known hallucination pattern in qa_watchlist.json?
   - If yes: increment `recurrence_count` on the watchlist item, escalate severity
   - If no: if this is the second occurrence of the same type, create watchlist item
3. **Prevention**: When a hallucination pattern is identified, add a specific check to the relevant skill file or QA prompt
4. **Resolution**: Pattern is resolved when 10+ subsequent reviews of the same type pass without recurrence

See `ops/README.md` for schemas and conventions.

---

## Smoke Testing Standards

### After PPTX Changes
1. Generate a test deck with all slide types (title, section, content, two-column, quad, card_grid, table, bar_chart, stats, icon_content, closing)
2. Render to PNG and visually inspect
3. Check for: ghost placeholders, text overflow, missing logos, double bullets, correct colors
4. Verify on desktop AND mobile if UI-related

### After UI Changes
1. Check on desktop (sidebar visible, layout correct)
2. Check on mobile (hamburger works, responsive layout)
3. Check both light and dark themes
4. Check with and without active session in sidebar
5. Hard refresh to bust cache (increment CSS/JS version numbers)

### After Backend Changes
1. Import check: `python3 -c "from app.module import function"`
2. Health check: `curl /api/health`
3. Container logs: no errors in last 20 lines
4. If model-facing: trigger a test generation and verify output

### After Infrastructure Changes
1. Affected services respond to health checks
2. Cloudflare tunnel routes resolve
3. Other services not affected (check container status)
4. Verify from external network, not just localhost

---

## Issue Management

### Every Piece of Work Gets an Issue
- Before starting work, find or create the relevant GitHub issue
- Reference the issue number in commit messages (e.g., "#115")
- When work is done, comment on the issue with what was done
- Close issues only when the fix is deployed and verified

### Issue Quality
- Title: clear, specific, under 80 characters
- Body: problem statement, root cause (if known), proposed fix, acceptance criteria
- No secrets or internal credentials in issue text
- Label if applicable (but don't over-label)

### Session Wrap (MANDATORY — do not skip)
The operator MUST execute this checklist before ending any session. Do not wait to be reminded. If the user says "let's wrap" or "good session" or signals they are done, immediately begin this process.

**QA Agent Review:**
- [ ] QA agent run against all files changed during this session: `cd qa-agent/ && python3 agent.py <changed_files>`
- [ ] QA agent verdict is `pass` or `pass_with_warnings` (warnings reviewed and accepted)
- [ ] If QA agent failed: fix issues and re-run before proceeding with wrap
- [ ] If QA agent was unreachable: documented in ops/qa_log.json with reason

**Git Discipline:**
- [ ] Both repos clean (`git status` shows nothing uncommitted)
- [ ] All remotes pushed (origin + gitea for <ops-repo>; origin for <chatbot-repo>)
- [ ] <production-host> deployed on latest commit (verify with `git log --oneline -1` via SSH)
- [ ] Dev branch synced if applicable

**Documentation:**
- [ ] RECOVERY.md updated if any infrastructure, credentials, services, or deployment procedures changed
- [ ] Memory files updated if process, workflow, project status, or user preferences changed
- [ ] MEMORY.md index updated if new memory files were created
- [ ] CLAUDE.md updated if operational procedures changed

**Issue Tracking:**
- [ ] All work captured in GitHub issues (create if missing)
- [ ] Open issues updated with progress from this session
- [ ] Resolved issues closed with verification notes
- [ ] New issues opened for any deferred work or discovered problems

**Communication:**
- [ ] Telegram posted if significant work completed (infrastructure, features, outages)
- [ ] Summary provided to user covering: what was done, what's deployed, what's pending

**Backup Verification:**
- [ ] Verify backup timer is active: `systemctl status ologos-backup.timer` (if infrastructure was touched)
- [ ] If new credentials were added, verify they're in .env on all relevant hosts

**Architecture & Workflow Documentation:**
- [ ] If any system-level workflow, protocol, or agent behavior was added or modified, update the relevant diagram in `systems_architecture/`
- [ ] Regenerate affected SVG + PNG files; they are living documents, not one-time artifacts
- [ ] Verify symlinks to Downloads are current
- [ ] If new skills, session protocols, or operational patterns were introduced, the architecture diagrams must reflect them before the session ends

**Operational Intelligence (ops/):**
- [ ] All ops/ log files updated with events from this session (deploys, health checks, incidents, QA reviews, promotions)
- [ ] Watchlists reviewed — add new concerns discovered during session, resolve any addressed items
- [ ] ops/ files committed with other session wrap artifacts
- [ ] If a dev→prod promotion occurred, ensure promotion_log.json entry exists with full validation status

**Lessons Learned:**
- [ ] If any operational failure occurred this session (bug, gap, missed check, runtime surprise), add an entry to `ops/lessons_learned.json`
- [ ] If new lessons were added, run `python3 scripts/lessons-to-qa.py` to update the QA agent prompt
- [ ] Verify the QA prompt was updated: check that `qa-agent/prompts/qa_review.md` contains the new patterns

**Self-Check:**
- [ ] Did I make any claims during this session that I didn't verify? If so, verify now.
- [ ] Did I deploy anything to prod without testing on dev first? If so, flag it and log as violation in promotion_log.json.
- [ ] Are there any dangling background tasks or incomplete operations?

---

## Anti-Hallucination Checks

AI operators are prone to hallucination: stating things as fact that are not true, referencing code that doesn't exist, claiming actions were completed when they weren't, or fabricating data. These checks must be applied at every level.

### State Claims
- **Before asserting a file exists**: check with `ls` or `stat`, not memory
- **Before asserting a function exists**: grep for it, don't assume from a prior session
- **Before asserting a service is running**: run `docker ps` or health check
- **Before asserting code works**: import it or run a test, don't just read it
- **Before asserting a deploy succeeded**: check logs and health endpoint

### Content Claims
- **Numbers and statistics**: must have a source. If no source is available, say so explicitly. Never fabricate statistics.
- **API behavior**: verify against documentation or test, not training data memory. APIs change.
- **Configuration values**: read the current .env or config file. Don't recall from a previous session.
- **Git state**: run `git status`, `git log`, `git branch` rather than claiming state from memory.

### Conversation Claims
- **"I already did X"**: verify the artifact exists, the commit was pushed, the deploy is live. Memory of having done something is not proof.
- **"The file contains X"**: re-read the file if more than a few messages have passed since reading it.
- **"The user said X"**: re-read the conversation history if uncertain. Context compression can lose details.

### Output Claims
- **Generated documents**: verify they open, have the right number of pages/slides, contain the expected content
- **Architecture diagrams**: verify they render (SVG → PNG conversion)
- **Code changes**: verify they compile/import after editing

### Escalation
If you realize you've hallucinated or made a false claim:
1. Correct it immediately. Don't hope the user didn't notice.
2. State what was wrong and what the correct state is.
3. If an action was taken based on false information, assess whether it needs to be reversed.

### Context Degradation Alert
The QA agent must monitor for quality degradation caused by context window compression and proactively alert the human operator. This is a QA function, not a convenience function.

**Quality indicators to track:**
- Edit failures increasing (old_string not found — working from stale file state)
- Wrong repo/directory mistakes
- Assertions about code or state that turn out to be wrong on verification
- Forgetting user instructions given earlier in the session
- Recommitting work that was already committed
- Losing track of which branch (main vs dev) is active

**When quality degradation is detected, the QA agent must:**
1. Alert the user immediately: "QA notice: context reliability is declining"
2. Recommend session wrap if degradation is significant
3. If the user chooses to continue, increase verification frequency: re-read every file before editing, re-check git status before every commit, verify every claim before stating it
4. Log the degradation event for future pattern analysis (when ops/ persistence is built)

---

## Security Guardrails

### Credentials
- Never in code, commits, issues, or chat
- Only in .env files (gitignored)
- When user provides a credential: store in .env, don't echo it back
- When rotating: update all locations (both hosts, all .env files)

### Public Exposure
- Repo is PRIVATE — but treat every commit as if it could be public
- No internal IPs, hostnames, or architectural details in public-facing content
- Audit logs hash IPs and truncate prompts — maintain this standard
- SSRF protection, sandbox isolation, rate limiting must remain active

### Data Handling
- User-uploaded files: handled in sandbox, not persisted beyond session
- Generated artifacts: stored in downloads, cleaned up periodically
- Session history: no PII beyond conversation content
- Backups: encrypted, verified daily
