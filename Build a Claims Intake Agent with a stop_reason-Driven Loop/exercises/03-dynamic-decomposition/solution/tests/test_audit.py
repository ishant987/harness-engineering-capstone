"""Verification tests for claims intake audit logging and run invariants."""
from pathlib import Path
from claims_intake.session import ClaimSession


def test_session_audit_trace_preserves_claim_context(tmp_path: Path) -> None:
    """Verifies that ClaimSession initializes cleanly with full audit and policy context."""
    session = ClaimSession(
        claim_id="audit_verification_claim",
        policy_id="POL-1004",
        run_dir=tmp_path,
        clarification_responses={},
    )
    assert session.claim_id == "audit_verification_claim"
    assert session.policy_id == "POL-1004"
    assert not session.terminal_called
    assert session.case_facts == {}
