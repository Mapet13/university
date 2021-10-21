roots :: (Double, Double, Double) -> (Double, Double)
roots (a, b, c) =
  let d = sqrt (b * b - 4 * a * c)
      e = 2 * a
   in ((- b - d) / e, (- b + d) / e)

unitVec2D :: (Double, Double) -> (Double, Double)
unitVec2D (a, b) =
  let len = sqrt (a ^ 2 + b ^ 2)
   in (a / len, b / len)

unitVec3D :: (Double, Double, Double) -> (Double, Double, Double)
unitVec3D (a, b, c) =
  let len = sqrt (a ^ 2 + b ^ 2 + c ^ 2)
   in (a / len, b / len, c / len)

haron :: (Double, Double, Double) -> Double
haron (a, b, c) =
  let p = (a + b + c) / 2.0
   in sqrt (p * (p - a) * (p - b) * (p - c))