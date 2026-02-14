# BorgCal — Product + Technical Blueprint (MVP)

## 1) Product Vision
BorgCal is a privacy-first personal planning system that combines:
- Calendar events and appointments
- Daily mood tracking + markdown journal
- Kanban task management with deadlines
- Visual analytics for trends and productivity

It is designed as a **self-hosted web app** that runs on your Windows PC and is reachable from your Android phone after login.

## 2) Locked Product Decisions (from PO feedback)
- Single-user MVP.
- One mood entry per day (editable).
- Journal uses markdown.
- Attachments supported in MVP, including optional audio.
- Push notifications only for MVP.
- One reminder per day; configurable by weekday; default 8:00 PM.
- Google/Outlook calendar sync is included in MVP.
- Kanban includes subtasks and recurring tasks in MVP.
- Tasks show on calendar before deadline using optional `appetite_days` setting.
- MVP access target: home network only.
- JSON backup for MVP; no auto-deletion by default.
- Minimal primary UI with richer settings pages.

## 3) Recommended Build Strategy

### Platform strategy
- **Primary app type**: Progressive Web App (PWA)
- **Server location**: Runs on your Windows PC (or a small home server)
- **Phone access**: Browser/PWA on Android over home network
- **Portability**: Web stack allows support for Windows, Linux, macOS, Android, and iOS

### Why this approach
- Maximizes cross-platform support with one codebase
- Supports offline-ish behavior with service worker + local cache
- Keeps data under your control on your own machine
- Easier secure hardening than several native apps

## 4) Core Features (MVP)

### A) Mood Tracking + Journal (priority)
1. Daily reminder notification sent to phone (one reminder/day)
2. One-tap quick check-in: 👍 / 👎
3. Optional expanded check-in:
   - Mood score (1–10)
   - Energy/stress tags
   - Markdown journal entry (target up to ~500–900 words)
4. One mood entry per day (editable)
5. Mood calendar heatmap
6. Weekly/monthly trend charts
7. Optional attachment upload in entry (including audio)

### B) Event / Appointment Tracking
1. Day/week/month calendar views
2. Event CRUD
3. Reminders + recurrence
4. Event category/color tags
5. Google/Outlook sync in MVP

### C) Kanban Board + Deadlines
1. Columns: Backlog / Planned / In Progress / Done
2. Drag-and-drop cards
3. Due dates + priority
4. Overdue indicators
5. Subtasks
6. Recurring tasks
7. Optional `appetite_days` estimate on task
8. Task appears on calendar from `deadline - appetite_days` through deadline

### D) Data Visualization
1. Mood trend lines + rolling averages
2. Correlation view:
   - Mood vs task completion
   - Mood vs appointment load
3. Productivity summaries:
   - Completed tasks per week
   - On-time completion rate

## 5) Security & Privacy Requirements

### Authentication
- Email/username + password (argon2id hashing)
- 2FA deferred until post-MVP
- Session timeout and forced re-auth for sensitive actions

### Transport security
- Home-network deployment for MVP
- HTTPS recommended where practical even on LAN
- Strict secure cookies + CSRF protection

### Data security
- Database stored on your PC
- Automated JSON backups to local folder
- Attachment storage with configurable size/type limits

### Privacy defaults
- No third-party analytics
- Minimal telemetry (off by default)
- Explicit backup/export controls
- No auto-delete policy in MVP

## 6) Proposed Architecture

### Frontend
- React + TypeScript + PWA support
- UI: calendar + kanban + charts (Recharts/ECharts)
- Notification permission for daily mood reminders
- Markdown editor + safe renderer for journals

### Backend
- API: FastAPI (Python)
- Auth: JWT + refresh token rotation
- Scheduler: APScheduler for weekday-specific reminder jobs
- Push channel: VAPID web push (PWA notifications)
- Calendar integrations: Google + Microsoft OAuth connectors

### Data
- PostgreSQL (primary)
- Filesystem storage for attachments and export bundles
- Redis optional (only if background throughput needs it)

### Deployment
- Docker Compose on Windows
- Reverse proxy (Caddy or Nginx)
- Home-network-first deployment for MVP
- Add a beginner-friendly Docker Desktop setup guide

## 7) Milestone Plan

### Milestone 1 — Foundation (1–2 weeks)
- Auth + single-user profile
- Mood quick check-in + expanded entry (one/day editable)
- Markdown journal CRUD
- Attachment upload/download for journal/mood entries
- Day/week/month calendar event CRUD
- Kanban CRUD with subtasks

### Milestone 2 — Integrations + reminders + charts (1–2 weeks)
- Weekday-configurable daily reminder flow (default 8 PM)
- Google/Outlook calendar sync
- Mood charts and heatmap
- Deadline + appetite-based task projection on calendar
- Recurring tasks

### Milestone 3 — Hardening + quality (1–2 weeks)
- Security hardening and threat review
- Backup/restore (JSON)
- Minimal UI polish + richer settings pages
- Accessibility-ready structure
- QA + bug fixes
- Windows Docker Desktop onboarding docs

## 8) Data Model (MVP entities)
- User
- MoodEntry
- JournalEntry
- Attachment
- CalendarEvent
- ExternalCalendarConnection
- ExternalCalendarMapping
- KanbanBoard
- KanbanColumn
- TaskCard
- TaskSubtask
- TaskRecurrenceRule
- ReminderSchedule
- ReminderSubscription

## 9) Acceptance Criteria (MVP)
1. Single user can login and use all core modules.
2. User can submit/edit one daily mood entry in 2 taps on phone.
3. User can write markdown journal entries and attach optional files/audio.
4. User can create/edit/delete events and kanban tasks including subtasks.
5. User can configure reminders by weekday (default 8 PM) and receives one push/day.
6. User can connect Google/Outlook and view synced calendar data.
7. Task deadline and `appetite_days` affect calendar visibility as configured.
8. Dashboard renders mood + task trend charts for selectable date ranges.
9. Data persists on host PC and can be backed up as JSON.

## 10) Known Risks + Mitigations
- Push notifications on mobile browsers can vary by vendor
  - Mitigation: focus on standards-compliant Web Push and test on target Android browser
- Calendar provider API complexity (OAuth, quotas, edge cases)
  - Mitigation: implement one-way sync first, then expand
- Self-hosted setup complexity for non-technical operator
  - Mitigation: provide step-by-step Docker Desktop onboarding and health checks
- Data loss risk
  - Mitigation: scheduled JSON backups + restore drill

## 11) Immediate Next Steps
1. Scaffold monorepo (`frontend`, `backend`, `infra`).
2. Start Milestone 1 vertical slice with mood/journal first.
3. Define DB schema including `appetite_days`, subtasks, recurrence, attachments.
4. Implement reminder scheduling defaults and settings UI.
5. Add Google/Microsoft OAuth app registration docs and integration stubs.


## 12) What You Need To Do Before Build Starts
1. **Pick your local hostname/device plan**
   - Confirm the Windows PC that will host BorgCal and stays on during normal use.
   - Confirm phone and PC are on the same home network for MVP.

2. **Create OAuth app credentials for calendar sync**
   - Create a Google OAuth app (Calendar scope).
   - Create a Microsoft OAuth app (Outlook Calendar scope).
   - Save client IDs/secrets for local `.env` configuration.

3. **Confirm notification/browser target on Android**
   - Choose your primary Android browser for PWA usage (Chrome preferred for predictable Web Push behavior).
   - Grant notification permissions in that browser.

4. **Decide attachment limits**
   - Choose max upload size per file (recommended MVP default: 25 MB).
   - Confirm allowed attachment types (images, pdf, audio files like mp3/m4a/wav).

5. **Install Windows prerequisites (with onboarding help)**
   - Install Docker Desktop.
   - Ensure virtualization is enabled and Docker can run Linux containers.

6. **Backup location decision**
   - Pick a local folder/drive for automated JSON backups.
   - Confirm approximate backup cadence (recommended: daily).

7. **Security baseline confirmation**
   - Confirm home-network-only access for MVP.
   - Confirm strong password policy for your account (2FA deferred post-MVP).

Use the non-technical setup guide at `docs/borgcal/windows-setup.md`. BorgCal can live on any drive (C, D, etc.). After you complete it, I can scaffold the app repository structure (`frontend`, `backend`, `infra`) so coding starts immediately.
