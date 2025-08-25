UPDATE productions_info AS pi
SET duration = pi.duration
  + (15 * (pi.id < 15)::int)
  + (20 * (pi.id >= 20)::int)
WHERE pi.synopsis IS NULL;
