from findatapy.market.datavendor import DataVendor
import pytest
import pandas as pd
from datetime import datetime

def test_data_vendor_init():
    vendor = DataVendor()
    assert isinstance(vendor, DataVendor)

def test_get_data():
    vendor = DataVendor()
    start_date = '2022-01-01'
    end_date = '2022-12-31'
    symbol = 'AAPL'
    
    data = vendor.get_data(symbol, start_date, end_date)
    assert isinstance(data, pd.DataFrame)
    assert not data.empty
    assert data.index[0] >= pd.to_datetime(start_date)
    assert data.index[-1] <= pd.to_datetime(end_date)

def test_invalid_dates():
    vendor = DataVendor()
    with pytest.raises(ValueError):
        vendor.get_data('AAPL', '2022-13-01', '2022-12-31')
    with pytest.raises(ValueError):
        vendor.get_data('AAPL', '2022-01-01', '2022-01-32')

def test_invalid_symbol():
    vendor = DataVendor()
    with pytest.raises(ValueError):
        vendor.get_data('INVALID_SYMBOL', '2022-01-01', '2022-12-31')

def test_date_range():
    vendor = DataVendor()
    start = '2022-01-01'
    end = '2021-12-31'
    with pytest.raises(ValueError):
        vendor.get_data('AAPL', start, end)

if __name__ == '__main__':
    pytest.main()