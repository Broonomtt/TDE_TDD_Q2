import pytest
from calcmult import mult


@pytest.mark.parametrize('n1,n2,produto', [(0, 0, 0), (-2,-5,10), (-2, 7,-14), (7.5, 5.4,40.5), (-1.0, -2.0,2.0), ('DOIS', 2, None)])
def test_mult(n1,n2, produto):
    assert mult(n1,n2) == produto
