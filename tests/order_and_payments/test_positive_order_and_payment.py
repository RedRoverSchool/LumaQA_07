from data.fake_data import FakeData


class TestOrderAndPayments(FakeData):

    def test_order_and_payments_positive(self, open_main_page):
        print(open_main_page)
