SELECT
    id,
    -- side * height / 2 AS area  -- ❌ May cause incorrect result due to integer division
    side * height / 2.0 AS area  -- ✅ Correct
    -- side * height * 0.5 AS area    -- ✅ Correct: ensures floating-point multiplication
    -- 0.5 is double precision
    -- 0.5 promotes the whole expression to double precision
FROM
    triangles
ORDER BY
    id;
