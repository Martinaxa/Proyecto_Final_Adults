

Edad de 17 a 90 # 73 valores 
[17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 90]

workclass.unique() #8

(['State-gov', 'Self-emp-not-inc', 'Private', 'Federal-gov',
       'Local-gov', 'Self-emp-inc', 'Without-pay', 'Never-worked'],
      dtype=object)

['marital-status'].unique() #7

array(['Never-married', 'Married-civ-spouse', 'Divorced',
       'Married-spouse-absent', 'Separated', 'Married-AF-spouse',
       'Widowed'], dtype=object)

native_country.nunique() #41 countries
(['United-States', 'Cuba', 'Jamaica', 'India', 'Mexico', 'South',
       'Puerto-Rico', 'Honduras', 'England', 'Canada', 'Germany', 'Iran',
       'Philippines', 'Italy', 'Poland', 'Columbia', 'Cambodia',
       'Thailand', 'Ecuador', 'Laos', 'Taiwan', 'Haiti', 'Portugal',
       'Dominican-Republic', 'El-Salvador', 'France', 'Guatemala',
       'China', 'Japan', 'Yugoslavia', 'Peru',
       'Outlying-US(Guam-USVI-etc)', 'Scotland', 'Trinadad&Tobago',
       'Greece', 'Nicaragua', 'Vietnam', 'Hong', 'Ireland', 'Hungary',
       'Holand-Netherlands'], dtype=object)

relationship.unique() #6
array(['Not-in-family', 'Husband', 'Wife', 'Own-child', 'Unmarried',
       'Other-relative'], dtype=object)

sex.unique() #2
array(['Male', 'Female'], dtype=object)

df.education.unique() #9
array(['Bachelors', 'Educación Secundaria', 'Masters',
       'Educación Primaria', 'Some-college', 'Assoc-acdm', 'Assoc-voc',
       'Doctorate', 'Prof-school'], dtype=object)

occupation.unique() #14

array(['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners',
       'Prof-specialty', 'Other-service', 'Sales', 'Craft-repair',
       'Transport-moving', 'Farming-fishing', 'Machine-op-inspct',
       'Tech-support', 'Protective-serv', 'Armed-Forces',
       'Priv-house-serv'], dtype=object)

df['capital-gain'].nunique() #118 capital-gain
sorted_unique_gain_values = sorted(df['capital-gain'].unique())

# Muestra los valores únicos de la columna 'capital-gain' ordenados
print(sorted_unique_gain_values)
[0, 114, 401, 594, 914, 991, 1055, 1086, 1111, 1151, 1173, 1409, 1424, 1455, 1471, 1506, 1639, 1797, 1831, 1848, 2009, 2036, 2050, 2062, 2105, 2174, 2176, 2202, 2228, 2290, 2329, 2346, 2354, 2387, 2407, 2414, 2463, 2538, 2580, 2597, 2635, 2653, 2829, 2885, 2907, 2936, 2961, 2964, 2977, 2993, 3103, 3137, 3273, 3325, 3411, 3418, 3432, 3456, 3464, 3471, 3674, 3781, 3818, 3887, 3908, 3942, 4064, 4101, 4386, 4416, 4508, 4650, 4687, 4787, 4865, 4931, 4934, 5013, 5060, 5178, 5455, 5556, 5721, 6097, 6360, 6418, 6497, 6514, 6723, 6767, 6849, 7298, 7430, 7443, 7688, 7896, 7978, 8614, 9386, 9562, 10520, 10566, 10605, 11678, 13550, 14084, 14344, 15020, 15024, 15831, 18481, 20051, 22040, 25124, 25236, 27828, 34095, 41310]

df['capital-loss'].nunique() 
[0, 155, 213, 323, 419, 625, 653, 810, 880, 974, 1092, 1138, 1258, 1340, 1380, 1408, 1411, 1485, 1504, 1539, 1564, 1573, 1579, 1590, 1594, 1602, 1617, 1628, 1648, 1651, 1668, 1669, 1672, 1719, 1721, 1726, 1735, 1740, 1741, 1755, 1762, 1816, 1825, 1844, 1848, 1876, 1887, 1902, 1944, 1974, 1977, 1980, 2001, 2002, 2042, 2051, 2057, 2080, 2129, 2149, 2163, 2174, 2179, 2201, 2205, 2206, 2231, 2238, 2246, 2258, 2267, 2282, 2339, 2352, 2377, 2392, 2415, 2444, 2457, 2467, 2472, 2489, 2547, 2559, 2603, 2754, 2824, 3004, 3683, 3770, 3900, 4356]

df['hours-per-week'].nunique() #94

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 70, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 94, 95, 96, 97, 98, 99]