import starry


def orbit(time, porb=1, a=30, inc=90, ecc=0, w=90, Omega=0, tref=0):
    """Return the cartesian components of a planet's Keplerian orbit."""
    star = starry.kepler.Primary(lmax=0)
    planet = starry.kepler.Secondary(lmax=0)
    planet.tref = tref
    planet.porb = porb
    planet.a = a
    planet.Omega = Omega
    planet.ecc = ecc
    planet.w = w
    planet.inc = inc
    system = starry.kepler.System(star, planet)
    system.compute(time)
    return planet.X, planet.Y, planet.Z