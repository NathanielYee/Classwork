'''
Nathaniel Yee
DS 2500
Create a model if you were to open a burger store and create a risk analysis using drv
'''

from drv import DRV, E

def main():
    burger = DRV({250:.25,500:.25,750:.25,1000:.25})
    fries = DRV({200:.10,500:.30,1000:.40,5000:.20})
    coke = DRV({100:.05,1000:.8,2000:.15})

    profit = 0.25 * burger + 0.50 * fries + 1.0 * coke
    expenses = DRV({2500:.20,2000:.30,1800:.50}) # The expenses will always be 2500

    net = profit - expenses
    annual_net = 365 * net # profit per year $808

    print('expected annual net:', E(annual_net))
    annual_net.plot()

if __name__ == '__main__':
    main()