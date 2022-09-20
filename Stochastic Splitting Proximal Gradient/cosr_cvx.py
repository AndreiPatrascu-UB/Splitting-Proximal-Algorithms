# Copyright (c) 2019-2020 Paul Irofti <paul@irofti.net>
# Copyright (c) 2020 Andrei Patrascu <andrei.patrascu@fmi.unibuc.ro>
# 
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
# 
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import cvxpy as cp

def cosr_cvx(sample, Delta, lam=50):
    m = sample.shape[0]

    x = cp.Variable(m)
    cost = 0.5*cp.sum_squares(x - sample)
    cost = cost + lam*cp.norm(Delta@x, 1)
    prob = cp.Problem(cp.Minimize(cost))
    prob.solve(solver=cp.CVXOPT, verbose=False)

    return x.value
