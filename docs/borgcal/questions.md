# BorgCal — Product Decisions (Resolved)

This file records your answers and is now the source of truth for MVP scope.

## Product behavior
1. **User model:** Single user for MVP.
2. **Mood cadence:** One mood entry per user per day, editable.
3. **Journal format:** Markdown.
4. **Attachments:** Included in MVP (rare usage expected), including optional audio uploads (e.g., banjo recordings).

## Notifications
5. **Channels:** Web push only for MVP. SMS may be explored post-MVP.
6. **Reminder scheduling:** Configurable by weekday, default 8:00 PM for each day.
7. **Notification volume:** Exactly one reminder per day, no follow-up reminders.

## Calendar and tasks
8. **Calendar sync:** Google/Outlook sync is in MVP.
9. **Task depth:** Subtasks and recurring tasks are in MVP.
10. **Calendar/task integration:** Tasks appear on calendar based on deadline plus configurable lead time.
    - Add per-task `appetite_days` field (optional) to estimate effort duration.
    - Display tasks from `deadline - appetite_days` through deadline (inclusive).

## Security and hosting
11. **Access model:** MVP targets home-network access only; secure remote access is post-MVP.
12. **Deployment comfort:** User is not yet comfortable with Docker Desktop, so onboarding docs/setup helper are required.
13. **2FA:** Not required for MVP, potential future enhancement.

## Data and exports
14. **Export/backup:** JSON backup is sufficient for MVP.
15. **Retention:** Never delete data by default. Future option for archive/auto-delete may be added.

## UX preferences
16. **Experience style:** Minimal day-to-day UI with deeper, richer settings pages.
17. **Accessibility:** Not a strict MVP requirement, but architecture/UI choices should keep future accessibility settings straightforward.

## Implementation notes added from decisions
- MVP should include markdown rendering/sanitization for journal entries.
- MVP should include attachment storage strategy and size/type limits.
- MVP should include calendar-provider OAuth setup for Google/Outlook sync.
- MVP should include a simple Docker Desktop onboarding guide tailored for Windows.
