from task_io import read_data, write_data
from strategy_deal import StrategyDeal
from utils import prepare


if __name__ == '__main__':
    data = read_data('input.txt')
    data_prepared = prepare(data)
    deal = StrategyDeal(*data_prepared)
    write_data('out.txt', str(deal))

