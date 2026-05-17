import pytest
from app.refunds import process_refund


def test_refund_missing_metadata_reason():
    """Test that process_refund handles missing metadata gracefully."""
    # Test case 1: refund without metadata field
    refund_no_metadata = {"amount": 100.0}
    result = process_refund(refund_no_metadata)
    assert result["status"] == "refunded"
    assert result["amount"] == 100.0
    
    # Test case 2: refund with metadata but no reason
    refund_no_reason = {"amount": 50.0, "metadata": {}}
    result = process_refund(refund_no_reason)
    assert result["status"] == "refunded"
    assert result["amount"] == 50.0
    
    # Test case 3: refund with complete metadata (should still work)
    refund_complete = {"amount": 75.0, "metadata": {"reason": "customer_request"}}
    result = process_refund(refund_complete)
    assert result["status"] == "refunded"
    assert result["reason"] == "customer_request"
    assert result["amount"] == 75.0