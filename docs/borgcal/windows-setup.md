# BorgCal — Simple Windows + Android Setup Guide (Non-Technical)

This guide is written for a non-technical setup.

## What you will install
- Docker Desktop on Windows (to run BorgCal)
- A modern browser on Android (Chrome recommended)

## Before you start
1. Use the Windows PC that will stay powered on most days.
2. Make sure your Android phone and that PC are on the same home Wi-Fi.
3. Create a folder for BorgCal data backups on **any drive you prefer** (C, D, or external), for example:
   - `D:\BorgCal\backups`


## Drive choice (important)
- **No, BorgCal does not have to be on the C drive.**
- You can use any drive/folder you want (for example `D:\BorgCal`).
- Just use the same folder path consistently in commands and settings.


## Fast path (you already installed Docker)
If Docker Desktop is already installed and running, skip Step 1 and do this:
1. Create your BorgCal folder on any drive (example: `D:\BorgCal`).
2. Put BorgCal project files in that folder.
3. In PowerShell run:
   - `cd <YOUR_BORGCAL_FOLDER>`
   - `docker compose up -d`
4. Open `http://localhost:8080` on your PC.
5. Open `http://<YOUR_PC_IP>:8080` on your Android phone (same Wi-Fi).
6. Add to Home screen + allow notifications.
7. Set reminders (weekday configurable, default 8:00 PM).
8. Connect Google + Microsoft calendars.
9. Test mood entry, markdown journal, task deadlines, and JSON backup.

## Step 1 — Install Docker Desktop on Windows
1. Open: https://www.docker.com/products/docker-desktop/
2. Download Docker Desktop for Windows.
3. Run installer with default options.
4. Restart PC if prompted.
5. Open Docker Desktop and wait until it says Docker is running.

## Step 2 — Prepare BorgCal project files
1. Create this folder on **any drive** (C, D, etc.):
   - Example: `D:\BorgCal`
2. Put the BorgCal project files there (we will scaffold this next).
3. Ensure you have a `.env` file when provided (contains app settings).


## Which files go in `D:\BorgCal`?
Right now in this repository, BorgCal has planning docs only (no runnable app scaffold yet).

### Put these in `D:\BorgCal` **when provided in the scaffold package**
- `docker-compose.yml`
- `.env` (from `.env.example`, filled with your values)
- `frontend/` (web app)
- `backend/` (API)
- `infra/` (reverse proxy/config scripts)
- `data/` (local persistent app data)
- `backups/` (JSON backup output)

### What you currently already have
- `docs/borgcal/README.md`
- `docs/borgcal/questions.md`
- `docs/borgcal/windows-setup.md`

If you want, I can generate the scaffold next so you can copy those runnable files straight into `D:\BorgCal` and start with one command.

## Step 3 — Start BorgCal
1. Open **PowerShell**.
2. Run:
   - `cd <YOUR_BORGCAL_FOLDER>`
   - Example: `cd D:\BorgCal`
   - `docker compose up -d`
3. Wait 1–2 minutes on first start.
4. Open browser on Windows:
   - `http://localhost:8080`

## Step 4 — Open from Android phone
1. Find your Windows local IP:
   - In PowerShell run: `ipconfig`
   - Look for IPv4 address (example: `192.168.1.55`)
2. On Android (same Wi-Fi), open:
   - `http://<YOUR_PC_IP>:8080`
   - Example: `http://192.168.1.55:8080`
3. Log in.
4. In browser menu, choose **Add to Home screen** (installs like an app/PWA).
5. Allow notifications when asked.

## Step 5 — Set daily mood reminder
1. In BorgCal, go to **Settings → Reminders**.
2. Keep default 8:00 PM for each weekday, or customize per day.
3. Save settings.
4. Confirm one test reminder is received.

## Step 6 — Connect calendar sync (Google + Outlook)
1. In BorgCal, open **Settings → Calendar Integrations**.
2. Click **Connect Google** and sign in.
3. Click **Connect Microsoft** and sign in.
4. Confirm events appear in calendar view.

## Step 7 — Verify mood + journal flow
1. Open today’s mood check-in.
2. Tap 👍 or 👎.
3. Add optional expanded score/tags.
4. Add a markdown journal note.
5. (Optional) Attach audio (example: banjo recording).
6. Save and reopen to confirm edits persist.

## Step 8 — Verify task + calendar flow
1. Create a task with due date.
2. Set optional `appetite_days` (example: 3).
3. Confirm task appears on calendar from 3 days before due date through due date.
4. Add subtasks and set recurrence if needed.

## Step 9 — Backup check
1. Open **Settings → Backups**.
2. Run a manual JSON backup.
3. Confirm backup file appears in your backup folder.

## Troubleshooting (quick)
- If phone cannot connect:
  - Confirm same Wi-Fi network.
  - Confirm Windows firewall allows Docker/app port (8080).
- If notifications do not arrive:
  - Check Android browser notification permission is allowed.
  - Ensure BorgCal reminder setting is enabled.
- If Docker does not start:
  - Reboot PC.
  - Re-open Docker Desktop and wait for “running” status.

## What to send me after your first setup attempt
- A screenshot of Docker Desktop showing “running”.
- Your PC IPv4 address (just the local one).
- Whether `http://<PC_IP>:8080` opens on Android.
- Whether a test reminder arrived.
