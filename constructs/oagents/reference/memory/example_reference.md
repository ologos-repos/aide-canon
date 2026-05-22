---
name: Backup Schedule
description: Nightly backup configuration and verification commands
type: reference
---

## Backup System

- Timer runs at 02:00 daily (system-level systemd timer)
- Backs up: auth DB, file storage, team chat config, git platform config
- Retention: Cloud (30 days), Offsite (60 days)
- Encrypted secrets via GPG

Verification: `sudo systemctl status backup.timer`
