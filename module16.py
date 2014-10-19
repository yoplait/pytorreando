co_tax_calc = lambda tax : tax * 0.0451

def calc_taxes(agi,strategy):
  return strategy(agi)

state_taxes_owed = calc_taxes(100000.00, co_tax_calc)
print state_taxes_owed
