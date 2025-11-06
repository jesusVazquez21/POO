import pytest
from isbn import normalize_isbn, is_valid_isbn10, is_valid_isbn13, detect_isbn, INVALID, VALID_ISBN10, VALID_ISBN13

# ----------------------------
# FIXTURES
# ----------------------------
@pytest.fixture
def sample_isbns():
    return {
        "isbn10_valid_digit": "0306406152",
        "isbn10_valid_x": "0-8044-2957-X",
        "isbn10_invalid_checksum": "0306406153",
        "isbn10_invalid_length": "030640615",
        "isbn13_valid": "9780306406157",
        "isbn13_invalid_checksum": "9780306406158",
        "isbn13_invalid_length": "978030640615",
        "isbn_invalid_char": "97803A6406157"
    }

# ----------------------------
# PRUEBAS DE normalize_isbn
# ----------------------------
def test_normalize_isbn_removes_spaces_and_dashes():
    assert normalize_isbn("0-321-14653-0") == "0321146530"
    assert normalize_isbn(" 0 3 2 1 1 4 6 5 3 0 ") == "0321146530"

def test_normalize_isbn_allows_x_only_at_end():
    assert normalize_isbn("0-8044-2957-X") == "080442957X"
    with pytest.raises(ValueError):
        normalize_isbn("0X80442957")

def test_normalize_isbn_empty_or_none():
    assert normalize_isbn("") == ""
    assert normalize_isbn(None) == ""

def test_normalize_isbn_invalid_chars():
    with pytest.raises(ValueError):
        normalize_isbn("0-321-14653-A")

# ----------------------------
# PRUEBAS DE is_valid_isbn10
# ----------------------------
def test_is_valid_isbn10_valid(sample_isbns):
    assert is_valid_isbn10(sample_isbns["isbn10_valid_digit"])
    assert is_valid_isbn10(sample_isbns["isbn10_valid_x"])

def test_is_valid_isbn10_invalid(sample_isbns):
    assert not is_valid_isbn10(sample_isbns["isbn10_invalid_checksum"])
    assert not is_valid_isbn10(sample_isbns["isbn10_invalid_length"])
    assert not is_valid_isbn10(sample_isbns["isbn_invalid_char"])

# ----------------------------
# PRUEBAS DE is_valid_isbn13
# ----------------------------
def test_is_valid_isbn13_valid(sample_isbns):
    assert is_valid_isbn13(sample_isbns["isbn13_valid"])

def test_is_valid_isbn13_invalid(sample_isbns):
    assert not is_valid_isbn13(sample_isbns["isbn13_invalid_checksum"])
    assert not is_valid_isbn13(sample_isbns["isbn13_invalid_length"])
    assert not is_valid_isbn13(sample_isbns["isbn_invalid_char"])

# ----------------------------
# PRUEBAS DE detect_isbn
# ----------------------------
def test_detect_isbn_valid_cases(sample_isbns):
    assert detect_isbn(sample_isbns["isbn10_valid_digit"]) == VALID_ISBN10
    assert detect_isbn(sample_isbns["isbn13_valid"]) == VALID_ISBN13

def test_detect_isbn_invalid_cases(sample_isbns):
    assert detect_isbn(sample_isbns["isbn10_invalid_checksum"]) == INVALID
    assert detect_isbn("") == INVALID
    assert detect_isbn("123456789012345") == INVALID  # longitud inválida

# ----------------------------
# PRUEBAS DE PROPIEDADES
# ----------------------------
def test_normalization_idempotent():
    s = "0-8044-2957-X"
    assert normalize_isbn(normalize_isbn(s)) == normalize_isbn(s)

def test_equivalent_formats_same_result():
    """ISBNs equivalentes deben producir el mismo resultado"""
    raw = "978-0-306-40615-7"
    clean = "9780306406157"
    assert detect_isbn(raw) == detect_isbn(clean)
