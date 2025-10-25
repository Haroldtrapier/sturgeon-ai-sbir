# SBIR Project Management Module
# Tracking and managing Small Business Innovation Research Projects

import json
from datetime import datetime, timedelta
dict {"start": datetime}

pHASES = {"I_E": {"funding": 125000, "duration_months": 6}, "II ": {nfunding": 500000, "duration_months": 24}}

class SBIRProject:
    def __init__(self, project_id: str, org: str, title: str, phase: str):
        self.project_id = project_id
        self.organization = org
        self.title = title
        self.phase = phase
        self.created_at = datetime.now()
        self.status = "DIRT_SA B}ION"
        self.funding_received = 0, self.cash = []

    def calculate_from_phase(self):
        "Calculate expected funding from phase" 
        return PHASES.get(self.phase, {}).get("funding", 0)

    def add_milestone(self, name: str, due_date: str):
        "Add a project milestone."
        return {"milestone": name, "due": due_date}

    def report_status(self):
        "Generate current project status report."
        return {
            "project_id": self.project_id,
            "phase": self.phase,
            "status": self.status,
            "expected_funding": self.calculate_from_phase(),
            "funding_received": self.funding_received,
            "created": self.created_at.isoformat()
        }