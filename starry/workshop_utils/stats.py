import numpy as np
import starry


def set_random(map, sigma_l, norm=1.0):
    r"""
    Draw spherical harmonic coefficients from a zero-mean gaussian 
    with standard deviation 

        \alpha(l) = \mathrm{e}^{-\frac{l^2}{2\sigma_l^2}}

    """
    # Our hyperdistribution
    alpha = norm * np.array([np.exp(-l ** 2 / (2 * sigma_l) ** 2) 
                             for l in range(map.lmax + 1)])

    # Draw from it to instantiate our map
    map[:, :] = np.random.randn(map.N)
    for l in range(map.lmax + 1):
        map[l, :] *= alpha[l]


def MAP(lmax, flux, flux_err, lam=None, axis=[0, 1, 0], **flux_kwargs):
    """
    Solves the linear problem for the maximum a posteriori map
    coefficients and their variance given a series of `flux`
    measurements, their errors `flux_err`, and a vector of prior 
    variances on the map coefficients, `lam`.

    """
    # Instantiate a map and initialize its coefficients
    map = starry.Map(lmax)
    map.axis = axis
    map[:, :] = 1
    
    # Let's get the design matrix. This is the matrix
    # we dot into the `y` vector to get the flux. Since
    # 
    #       f = s^T A' R R y
    #
    # the design matrix is just
    #
    #       A = s^T A' R R
    #
    # In the beta version of starry, there's no method
    # to compute this, but we can get away with a little
    # HACK: the matrix `A` is just the *derivative* of the
    # flux with respect to `y`!
    _, grad = map.flux(**flux_kwargs, gradient=True)
    A = grad['y'].T

    # Now we solve the linear least squares problem:
    W = np.dot(A.T, A)
    if lam is not None:
        W[np.diag_indices_from(W)] += flux_err ** 2 / lam
    M = np.linalg.solve(W, A.T)

    # Compute and return the coefficient estimates and their variance
    yhat = np.dot(M, flux)
    yvar = flux_err ** 2 * np.linalg.inv(W)
    return yhat, yvar