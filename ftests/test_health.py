from apitest import ApiTest

def test_health():
    (
        ApiTest().health.get()
    )