p = 1000
r = 7 / 100
n = [10, 20, 30]

for year in n:
    a = p * (1 + r) ** year
    print(f" year = {year},{a: .2f}")

n = 10
a = p * (1 + r) ** n
print(f" n = {n},{a: .2f}")

n = 20
a = p * (1 + r) ** n
print(f" n = {n},{a: .2f}")

n = 30
a = p * (1 + r) ** n
print(f" n = {n},{a: .2f}")


def calculate_invest_return(P: float, r: float, n: float):
    return p * (1 + r) ** n


""""""


def main():
    p_given = 1000
    r_given = 7 / 100
    years_given = [10, 20, 30]

    for year in years_given:
        inv_returns = calculate_invest_return(p_given, r_given, year)
        print(f"year = {year}, return = {inv_returns: .2f}")


if __name__ == "__main__":
    main()
