from gainesville import get_city_cleaned, is_gainesville

def test_gainesville():
    assert get_city_cleaned("Gainesville") == "gainesville"
    assert get_city_cleaned("gainesville") == "gainesville"
    assert get_city_cleaned("GAINESVILLE") == "gainesville"
    assert get_city_cleaned("gAiNeSvIlLe") == "gainesville"
    assert get_city_cleaned("   gAiNeSvIlLe  ") == "gainesville"


def test_city():
    assert is_gainesville("gainesville") == True
    assert is_gainesville("New York") == False
    assert is_gainesville("chicago") == False
    assert is_gainesville("BoStOn") == False
