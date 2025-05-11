# This a test file for debugging for development purposes
# This file is not intended to be used in production

from sheet_config import log_to_sheet

log_to_sheet("Test Prompt", [{
    "name": "Test Name",
    "title": "CEO",
    "company": "Test Inc.",
    "email": "test@example.com",
    "linkedin_url": "https://linkedin.com/in/test"
}])
