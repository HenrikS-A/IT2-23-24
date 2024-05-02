def er_skuddår(årstall: int):
    """
    Skuddår er år som er delelige på 4 og som ikke er delelige med 100,
    med unntak for år som er delelige på 400
    """
    
    if årstall % 400 == 0:
        return True
    if årstall % 4 == 0 and not årstall % 100 == 0:
        return True
    return False


# Tester:
skuddår = [1704, 1708, 1712, 1716, 1720, 1724, 1728, 1732, 1736, 1740, 1744, 1748, 1752, 1756, 1760, 1764, 1768, 1772, 1776, 1780, 1784, 1788, 1792, 1796, 1804, 1808, 1812, 1816, 1820, 1824, 1828, 1832, 1836, 1840, 1844, 1848, 1852, 1856, 1860, 1864, 1868, 1872, 1876, 1880, 1884, 1888, 1892, 1896, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096, 2104, 2108, 2112, 2116, 2120, 2124, 2128, 2132, 2136, 2140, 2144, 2148, 2152, 2156, 2160, 2164, 2168, 2172, 2176, 2180, 2184, 2188, 2192, 2196]
for år in range(1704, 2197):
    if år in skuddår:
        assert er_skuddår(år) == True, f"{år} er et skuddår"
    else:
        assert er_skuddår(år) == False, f"{år} er IKKE et skuddår"

print("Alle testene fungerte.")
