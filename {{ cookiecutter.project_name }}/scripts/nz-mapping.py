import pandas as pd
import {{ cookiecutter.package_slug }} as pack

nz = pd.read_csv('../data/nz-population.csv')

reduced = nz.filter(items=['NZ_area', 'Count', 'geo_level'])
print(reduced.head())

print("\n")

reduced = pack.tolower(reduced, 'NZ_area')
reduced = pack.toupper(reduced, 'geo_level')
print(reduced.head())
