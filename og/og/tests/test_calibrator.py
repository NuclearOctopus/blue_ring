# Append app folder to path so the functions to test can be imported
import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from calibrator import sheet_pull

def test_row_count():
    """Get the row count for the dataframe and see if it has enough records.
    If there are less than 500, something is wrong with the data source."""
    
    test_df = sheet_pull()
    
    assert len(test_df.index) >= 500