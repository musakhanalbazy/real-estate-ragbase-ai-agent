"""Export captured leads to CSV.

Run:  python -m reporting.leads_report [stage]

Examples:
    python -m reporting.leads_report                # all leads
    python -m reporting.leads_report qualified       # only qualified leads

This is the simplest possible "dashboard" -- a CSV your sales team can
open in Excel/Sheets. The GET /admin/leads endpoint (app/main.py) serves
the same data as JSON if you'd rather build a real dashboard on top.
"""

import csv
import sys
from pathlib import Path

from memory.long_term_memory import list_leads

FIELDS = [
    "user_id", "platform", "name", "phone", "email",
    "property_type", "city_or_area", "budget_range", "financing_method",
    "purchase_timeline", "preferred_call_time", "site_visit_requested",
    "stage", "score", "message_count", "handoff_requested", "updated_at",
]


def export_csv(stage: str | None = None, out_path: str = "data/leads_export.csv") -> str:
    leads = list_leads(stage=stage)
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        for lead in leads:
            writer.writerow(lead)

    return out_path


if __name__ == "__main__":
    stage_filter = sys.argv[1] if len(sys.argv) > 1 else None
    path = export_csv(stage=stage_filter)
    print(f"Exported leads to {path}")
