
getc a = truncate ((1000 - a + (a^2)/(1000-a))/2)
getb a = let c = getc a in truncate (1000 - a) - c 


pythagorean a b c = (a^2 + b^2 == c^2)

as = map fromIntegral [1 .. 333]
bs = map fromIntegral (map getb as)
cs = map getc as

trips = zipWith3 pythagorean as bs cs

-- right as = filter (\(a,b) -> b) (zip as trips)

